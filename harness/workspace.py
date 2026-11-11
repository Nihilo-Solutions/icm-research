"""Workspace and run management: context layers, run folders, manifest, approvals, event log.

This file is the "folder as architecture" part of ICM plus the pieces the method leaves out:
run history (one folder per run), versioning (a frozen, hashed copy of L0 to L3 per run),
approvals (who signed off on each stage, when), and an append-only event log.
"""
from __future__ import annotations

import datetime as dt
import getpass
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STAGES = ["01-plan", "02-research", "03-verify", "04-architect", "05-synthesize", "06-qa"]
CONTEXT_GLOBS = ["CLAUDE.md", "CONTEXT.md", "reference/*", "stages/*/CONTEXT.md"]


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def today() -> str:
    return dt.date.today().isoformat()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stage_name(arg: str) -> str:
    """Accept '2', '02', or '02-research'."""
    arg = arg.strip()
    for s in STAGES:
        if s == arg or s.split("-")[0] == arg.zfill(2):
            return s
    raise SystemExit(f"Unknown stage '{arg}'. Stages: {', '.join(STAGES)}")


def parse_front_matter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        return yaml.safe_load(fm) or {}, body.strip()
    return {}, text.strip()


def load_config() -> dict:
    return yaml.safe_load((ROOT / "harness" / "config.yaml").read_text())


class Run:
    """One run of the workspace. Everything a run produces lives under runs/<run_id>/ (L4)."""

    def __init__(self, run_id: str):
        self.id = run_id
        self.dir = ROOT / "runs" / run_id
        if not self.dir.exists():
            raise SystemExit(f"No run named {run_id}. Create one with: python harness/icm.py new")
        self.manifest_path = self.dir / "manifest.json"
        self.events_path = self.dir / "events.jsonl"

    # ---------- creation and lookup ----------
    @classmethod
    def create(cls, label: str = "") -> "Run":
        run_id = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + (f"-{label}" if label else "")
        d = ROOT / "runs" / run_id
        d.mkdir(parents=True)
        manifest = {
            "run_id": run_id,
            "created_at": now_iso(),
            "run_date": today(),
            "created_by": getpass.getuser(),
            "git_commit": _git_head(),
            "context_versions": [],
            "approvals": {},
            "stages": {},
        }
        (d / "manifest.json").write_text(json.dumps(manifest, indent=2))
        (ROOT / "runs" / "LATEST").write_text(run_id)
        run = cls(run_id)
        run.snapshot_context(reason="run created")
        return run

    @classmethod
    def latest_or(cls, run_id: str | None) -> "Run":
        if run_id:
            return cls(run_id)
        latest = ROOT / "runs" / "LATEST"
        if not latest.exists():
            raise SystemExit("No runs yet. Create one with: python harness/icm.py new")
        return cls(latest.read_text().strip())

    # ---------- manifest ----------
    @property
    def manifest(self) -> dict:
        return json.loads(self.manifest_path.read_text())

    def update_manifest(self, fn) -> None:
        m = self.manifest
        fn(m)
        self.manifest_path.write_text(json.dumps(m, indent=2))

    @property
    def run_date(self) -> str:
        return self.manifest["run_date"]

    # ---------- context snapshot (versioning) ----------
    def snapshot_context(self, reason: str) -> None:
        """Freeze L0 to L3 into this run so later edits never change what a run used."""
        ctx = self.dir / "context"
        if ctx.exists():
            shutil.rmtree(ctx)
        hashes = {}
        for pattern in CONTEXT_GLOBS:
            for src in sorted(ROOT.glob(pattern)):
                if src.is_file():
                    rel = src.relative_to(ROOT)
                    dst = ctx / rel
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                    hashes[str(rel)] = sha256(src)
        self.update_manifest(lambda m: m["context_versions"].append(
            {"at": now_iso(), "reason": reason, "git_commit": _git_head(), "files": hashes}))

    def ctx_path(self, rel: str) -> Path:
        return self.dir / "context" / rel

    def l0(self) -> str:
        return self.ctx_path("CLAUDE.md").read_text()

    def l2(self, stage: str) -> tuple[dict, str]:
        return parse_front_matter(self.ctx_path(f"stages/{stage}/CONTEXT.md").read_text())

    def l3(self, name: str) -> str:
        return self.ctx_path(f"reference/{name}").read_text()

    def workpackages(self) -> dict:
        return yaml.safe_load(self.l3("workpackages.yaml"))

    # ---------- stage folders ----------
    def out_dir(self, stage: str) -> Path:
        d = self.dir / stage / "output"
        d.mkdir(parents=True, exist_ok=True)
        return d

    def raw_dir(self, stage: str) -> Path:
        d = self.dir / "raw" / stage
        d.mkdir(parents=True, exist_ok=True)
        return d

    # ---------- approvals (human review between stages) ----------
    def require_previous_approved(self, stage: str) -> None:
        idx = STAGES.index(stage)
        if idx == 0:
            return
        prev = STAGES[idx - 1]
        if prev not in self.manifest["approvals"]:
            raise SystemExit(
                f"Stage {prev} is not approved for run {self.id}.\n"
                f"Review runs/{self.id}/{prev}/output/, then run:\n"
                f"  python harness/icm.py approve {prev.split('-')[0]} --note \"...\"\n"
                f"(Use --auto to skip gates, which removes the human review ICM depends on.)")

    def approve(self, stage: str, by: str, note: str, skip: bool = False) -> None:
        status = self.manifest["stages"].get(stage, {}).get("status")
        if status != "done" and not skip:
            raise SystemExit(f"Stage {stage} has status '{status or 'not run'}', so there is nothing to approve. "
                             f"Run it first, or pass --skip to record a deliberate skip.")
        out = self.dir / stage / "output"
        files = sorted(p for p in out.rglob("*") if p.is_file()) if out.exists() else []
        # Hashing the approved outputs means a later edit to them is detectable.
        hashes = {str(p.relative_to(out)): sha256(p) for p in files}
        self.update_manifest(lambda m: m["approvals"].__setitem__(
            stage, {"by": by, "at": now_iso(), "note": note, "skipped": skip, "output_hashes": hashes}))
        self.log_event({"type": "approval", "stage": stage, "by": by, "note": note, "skipped": skip})

    def mark_stage(self, stage: str, status: str, **extra) -> None:
        self.update_manifest(lambda m: m["stages"].__setitem__(
            stage, {"status": status, "at": now_iso(), **extra}))

    # ---------- event log (append only) ----------
    def log_event(self, event: dict) -> None:
        event = {"ts": now_iso(), **event}
        with self.events_path.open("a") as f:
            f.write(json.dumps(event) + "\n")

    def events(self) -> list[dict]:
        if not self.events_path.exists():
            return []
        return [json.loads(line) for line in self.events_path.read_text().splitlines() if line.strip()]

    def spent_usd(self) -> float:
        return round(sum(e.get("cost_usd", 0.0) for e in self.events() if e.get("type") == "api_call"), 4)


def _git_head() -> str | None:
    try:
        return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True,
                              text=True, timeout=5).stdout.strip() or None
    except Exception:
        return None
