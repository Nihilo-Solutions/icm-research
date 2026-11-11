#!/usr/bin/env python3
"""ICM research harness: runs the six stages of this workspace against the Claude API.

  python harness/icm.py new [--label NAME]          start a run (freezes L0 to L3 into the run)
  python harness/icm.py run 02 [--only WP-Q06A]     run one stage (needs the previous stage approved)
  python harness/icm.py approve 02 --note "..."     record human sign-off for a stage
  python harness/icm.py status | cost               see where the run is and what it cost
  python harness/icm.py refresh-context             re-freeze L0 to L3 after you edit them (logged)
  python harness/icm.py all --auto                  run every stage with no gates (not recommended)

Add --dry-run to any run command to exercise the whole pipeline offline with a fake API.
"""
from __future__ import annotations

import argparse
import asyncio
import getpass
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ledger import (CLAIMS_SCHEMA, EXTRACT_INSTRUCTIONS, VERDICTS_SCHEMA, SourceRegistry,  # noqa: E402
                    apply_verdict, deterministic_checks, finalize_report, render_ledger,
                    render_with_markers, select_for_verification, validate_claims, CLAIM_ID)
from llm import BudgetExceeded, Claude, SpendCapReached, build_tools, last_json_block, system_blocks  # noqa: E402
from workspace import STAGES, Run, load_config, stage_name  # noqa: E402


# ------------------------------------------------------------------ helpers
def stage_prompt(run: Run, stage: str, ttl: str) -> tuple[dict, list[dict], str]:
    fm, body = run.l2(stage)
    texts = [("L0_identity_and_rules", run.l0())]
    for name in fm.get("reference", []):
        texts.append((f"L3_{name.replace('.', '_')}", run.l3(name)))
    preamble = (f"Run date: {run.run_date}\n\n<stage_instructions stage=\"{stage}\">\n{body}\n"
                f"</stage_instructions>\n\n")
    return fm, system_blocks(texts, ttl), preamble


def registry(run: Run) -> SourceRegistry:
    return SourceRegistry(run.dir / "sources.json")


def header(**kv) -> str:
    return "<!-- " + json.dumps(kv) + " -->\n"


# ------------------------------------------------------------------ stage 01
async def stage_01(run: Run, cfg: dict, claude: Claude, args) -> str:
    stage = "01-plan"
    fm, system, pre = stage_prompt(run, stage, cfg["api"]["cache_ttl"])
    res = await claude.turn(stage=stage, name="plan", model=fm["model"], system=system,
                            user=pre + "<task>Review the work packages in L3_workpackages_yaml against the brief.</task>",
                            effort=fm["effort"], max_tokens=fm["max_tokens"])
    out = run.out_dir(stage) / "plan-review.md"
    out.write_text(header(models=res.models_served, cost_usd=round(res.cost_usd, 3)) + res.text)
    return f"Wrote {out.relative_to(run.dir)} (${res.cost_usd:.2f})"


# ------------------------------------------------------------------ stage 02
async def stage_02(run: Run, cfg: dict, claude: Claude, args) -> str:
    stage = "02-research"
    fm, system, pre = stage_prompt(run, stage, cfg["api"]["cache_ttl"])
    wps = run.workpackages()
    defaults = wps.get("defaults", {})
    packages = wps["packages"]
    if args.only:
        wanted = {w.strip() for w in args.only.split(",")}
        packages = [p for p in packages if p["id"] in wanted]
    out = run.out_dir(stage)
    reg = registry(run)

    async def worker(p: dict) -> dict:
        wp = p["id"]
        if (out / f"{wp}.claims.json").exists() and not args.force:
            return {"wp": wp, "skipped": True}
        task = {k: p[k] for k in ("id", "title", "refs", "must_answer", "angles", "start_urls") if k in p}
        urls = "\n".join(p.get("start_urls", []))
        user = (pre + "<work_package>\n" + yaml.safe_dump(task, sort_keys=False, allow_unicode=True)
                + "</work_package>\n" + (f"\nStart URLs you may fetch directly:\n{urls}\n" if urls else ""))
        tools = build_tools(fm["tools"], cfg, p.get("max_searches", defaults.get("max_searches", 25)),
                            p.get("max_fetches", defaults.get("max_fetches", 20)))
        res = await claude.turn(stage=stage, name=wp, model=fm["model"], system=system, user=user,
                                tools=tools, effort=fm["effort"], max_tokens=fm["max_tokens"])
        meta = dict(wp=wp, models=sorted(set(res.models_served)), fallbacks=len(res.fallbacks),
                    stop_reason=res.stop_reason, cost_usd=round(res.cost_usd, 3),
                    searches=res.usage.get("web_search_requests"), fetches=res.usage.get("web_fetch_requests"))
        if res.refusal:
            (out / f"{wp}.md").write_text(header(**meta) + f"# {wp} declined\n\n{json.dumps(res.refusal, indent=2)}\n"
                                          "\nRephrase the work package or narrow it, then rerun with --only.\n")
            return {**meta, "refused": True}
        md, quotes, consulted = render_with_markers(res.blocks, reg, run.run_date, wp)
        ids = sorted(set(re.findall(r"\{(S\d+)\}", md)), key=lambda s: int(s[1:]))
        by_id = reg.by_id()
        src = "\n".join(f"- {s}: {by_id[s]['title']} {by_id[s]['url']}" for s in ids)
        (out / f"{wp}.md").write_text(
            header(**meta) + f"# {wp}: {p['title']}\n\n{md}\n\n## Sources attached by the API\n\n{src}\n\n"
            f"_{len(consulted)} search results consulted; {len(ids)} sources cited._\n")
        extracted = await claude.extract_json(
            stage=stage, name=f"{wp}.extract", model=fm.get("extract_model", "claude-sonnet-5-5"),
            schema=CLAIMS_SCHEMA, instructions=EXTRACT_INSTRUCTIONS,
            content=f"Work package {wp}, main ref {p['refs'][0]}.\n\n{md}")
        claims, oq = validate_claims(wp, p["refs"][0], extracted, set(ids), quotes)
        (out / f"{wp}.claims.json").write_text(json.dumps({"meta": meta, "claims": claims, "open_questions": oq}, indent=1))
        reg.save()
        return {**meta, "claims": Counter(c["status"] for c in claims)}

    results = await asyncio.gather(*(worker(p) for p in packages), return_exceptions=True)
    reg.save()
    lines = ["# Stage 02 summary", "", "| Work package | Status | Claims by status | Searches | Fetches | Model(s) | Cost |",
             "|---|---|---|---|---|---|---|"]
    failures = 0
    for p, r in zip(packages, results):
        if isinstance(r, BaseException):
            failures += 1
            if isinstance(r, (BudgetExceeded, SpendCapReached)):
                lines.append(f"| {p['id']} | stopped: {r} | | | | | |")
            else:
                lines.append(f"| {p['id']} | error: {type(r).__name__}: {str(r)[:120]} | | | | | |")
            continue
        if r.get("skipped"):
            lines.append(f"| {p['id']} | kept from earlier attempt | | | | | |")
            continue
        status = "declined (see file)" if r.get("refused") else "done"
        claims = ", ".join(f"{k} {v}" for k, v in sorted(r.get("claims", {}).items()))
        lines.append(f"| {p['id']} | {status} | {claims} | {r.get('searches')} | {r.get('fetches')} | "
                     f"{', '.join(r['models'])} | ${r['cost_usd']} |")
    (out / "summary.md").write_text("\n".join(lines) + "\n")
    return f"{len(packages) - failures}/{len(packages)} work packages finished. See {stage}/output/summary.md"


# ------------------------------------------------------------------ stage 03
async def stage_03(run: Run, cfg: dict, claude: Claude, args) -> str:
    stage = "03-verify"
    fm, system, pre = stage_prompt(run, stage, cfg["api"]["cache_ttl"])
    src_dir = run.dir / "02-research" / "output"
    claims, oqs = [], []
    for f in sorted(src_dir.glob("*.claims.json")):
        d = json.loads(f.read_text())
        claims += d["claims"]
        oqs += d["open_questions"]
    reg = registry(run)
    by_id = reg.by_id()
    selected = select_for_verification(claims, cfg["verify"]["scope"])
    groups: dict[str, list[dict]] = defaultdict(list)
    for c in selected:
        groups[c["source_ids"][0]].append(c)
    size = int(cfg["verify"]["max_claims_per_call"])
    chunks = [(sid, g[i:i + size]) for sid, g in groups.items() for i in range(0, len(g), size)]
    out = run.out_dir(stage)
    notes_dir = out / "verifier-notes"
    notes_dir.mkdir(exist_ok=True)
    verdicts: dict[str, dict] = {}

    async def verify(n: int, sid: str, chunk: list[dict]) -> None:
        src = by_id[sid]
        lines = []
        for c in chunk:
            q = " | ".join(f"\"{t[:280]}\"" for t in c["quotes"].get(sid, [])[:2]) or "(none)"
            lines.append(f"- {c['id']} | status {c['status']} | {c['statement']}\n  Worker's quoted snippet(s): {q}")
        user = (pre + f"<task>\nSource URL: {src['url']}\nSource title: {src['title']}\n\n"
                "Claims citing this source:\n" + "\n".join(lines) + "\n</task>")
        res = await claude.turn(stage=stage, name=f"v{n:03d}", model=fm["model"], system=system, user=user,
                                tools=build_tools(fm["tools"], cfg, max_searches=3, max_fetches=4),
                                effort=fm["effort"], max_tokens=fm["max_tokens"])
        md, _, _ = render_with_markers(res.blocks, reg, run.run_date, "verify")
        (notes_dir / f"v{n:03d}.md").write_text(header(source=sid, models=res.models_served, cost_usd=round(res.cost_usd, 3)) + md)
        if res.refusal:
            return
        parsed = last_json_block(res.text)
        if parsed is None:
            parsed = await claude.extract_json(
                stage=stage, name=f"v{n:03d}.extract", model=fm.get("extract_model", "claude-sonnet-5-5"),
                schema=VERDICTS_SCHEMA, content=res.text,
                instructions="Extract the verifier's verdict for every claim ID in these notes. Do not change any verdict.")
        ids = {c["id"] for c in chunk}
        for v in parsed.get("verdicts", []):
            if v.get("claim_id") in ids:
                verdicts[v["claim_id"]] = v

    results = await asyncio.gather(*(verify(n, sid, ch) for n, (sid, ch) in enumerate(chunks, 1)),
                                   return_exceptions=True)
    errors = [r for r in results if isinstance(r, BaseException)]
    final = [apply_verdict(c, verdicts.get(c["id"]), reg, run.run_date, []) for c in claims]
    reg.save()
    (out / "ledger.json").write_text(json.dumps({"claims": final, "open_questions": oqs}, indent=1))
    (out / "ledger.md").write_text(render_ledger(final, oqs, reg))
    vc = Counter(c.get("verdict") for c in final)
    fc = Counter(c["final_status"] for c in final)
    bad = [c for c in final if c.get("verdict") in ("not_supported", "partially_supported", "unreachable")]
    summary = ["# Stage 03 summary", "",
               f"Claims: {len(final)}. Checked: {len(selected)} in {len(chunks)} verifier calls. Errors: {len(errors)}.", "",
               "Verdicts: " + ", ".join(f"{k} {v}" for k, v in vc.most_common()), "",
               "Final status: " + ", ".join(f"{k} {v}" for k, v in fc.most_common()), "",
               "## Claims the verifier changed or rejected", ""]
    for c in bad:
        summary.append(f"- {c['id']} ({c['verdict']}, now {c['final_status']}): {c['statement']}\n"
                       f"  Verifier: {c.get('evidence_quote', '')[:300]} {c.get('verifier_notes', '')[:300]}")
    for e in errors:
        summary.append(f"- ERROR: {type(e).__name__}: {str(e)[:300]}")
    (out / "summary.md").write_text("\n".join(summary) + "\n")
    return f"Ledger written: {len(final)} claims, {vc.get('not_supported', 0)} rejected, {len(errors)} errors."


# ------------------------------------------------------------------ stages 04 to 06
def load_ledger(run: Run) -> tuple[list[dict], str]:
    d = run.dir / "03-verify" / "output"
    return json.loads((d / "ledger.json").read_text())["claims"], (d / "ledger.md").read_text()


def unknown_ids(text: str, claims: list[dict]) -> list[str]:
    known = {c["id"] for c in claims}
    return sorted(set(re.findall(CLAIM_ID, text)) - known)


async def stage_04(run: Run, cfg: dict, claude: Claude, args) -> str:
    stage = "04-architect"
    fm, system, pre = stage_prompt(run, stage, cfg["api"]["cache_ttl"])
    claims, ledger_md = load_ledger(run)
    res = await claude.turn(stage=stage, name="architect", model=fm["model"], system=system,
                            user=pre + f"<ledger>\n{ledger_md}\n</ledger>", effort=fm["effort"],
                            max_tokens=fm["max_tokens"])
    out = run.out_dir(stage) / "architecture.md"
    out.write_text(header(models=res.models_served, cost_usd=round(res.cost_usd, 3)) + res.text)
    unk = unknown_ids(res.text, claims)
    return f"Wrote {out.relative_to(run.dir)} (${res.cost_usd:.2f}). Unknown claim IDs: {unk or 'none'}"


async def stage_05(run: Run, cfg: dict, claude: Claude, args) -> str:
    stage = "05-synthesize"
    fm, system, pre = stage_prompt(run, stage, cfg["api"]["cache_ttl"])
    claims, ledger_md = load_ledger(run)
    arch = (run.dir / "04-architect" / "output" / "architecture.md").read_text()
    res = await claude.turn(stage=stage, name="report", model=fm["model"], system=system,
                            user=pre + f"<ledger>\n{ledger_md}\n</ledger>\n\n<stage_04_output>\n{arch}\n</stage_04_output>",
                            effort=fm["effort"], max_tokens=fm["max_tokens"])
    out = run.out_dir(stage)
    traceable = res.text
    (out / "report-traceable.md").write_text(traceable)
    final, stats = finalize_report(traceable, claims, registry(run))
    (out / "report.md").write_text(final)
    (out / "finalize-stats.json").write_text(json.dumps(stats, indent=1))
    return f"Wrote report.md and report-traceable.md (${res.cost_usd:.2f}). {stats}"


async def stage_06(run: Run, cfg: dict, claude: Claude, args) -> str:
    stage = "06-qa"
    fm, system, pre = stage_prompt(run, stage, cfg["api"]["cache_ttl"])
    claims, ledger_md = load_ledger(run)
    d5 = run.dir / "05-synthesize" / "output"
    traceable = (d5 / "report-traceable.md").read_text()
    final = (d5 / "report.md").read_text()
    stats = json.loads((d5 / "finalize-stats.json").read_text())
    checks = deterministic_checks(traceable, final, stats, claims)
    res = await claude.turn(stage=stage, name="redteam", model=fm["model"], system=system,
                            user=pre + "<deterministic_checks>\n" + "\n".join(checks) + "\n</deterministic_checks>\n\n"
                            f"<report>\n{traceable}\n</report>\n\n<ledger>\n{ledger_md}\n</ledger>",
                            effort=fm["effort"], max_tokens=fm["max_tokens"])
    out = run.out_dir(stage) / "qa.md"
    out.write_text("# QA\n\n## Deterministic checks\n\n" + "\n".join(f"- {c}" for c in checks)
                   + "\n\n## Red-team review\n\n" + res.text + "\n")
    fails = sum(1 for c in checks if c.startswith("[FAIL"))
    return f"Wrote {out.relative_to(run.dir)}. Deterministic failures: {fails}."


RUNNERS = {"01-plan": stage_01, "02-research": stage_02, "03-verify": stage_03,
           "04-architect": stage_04, "05-synthesize": stage_05, "06-qa": stage_06}


# ------------------------------------------------------------------ CLI
def make_claude(run: Run, cfg: dict, dry: bool) -> Claude:
    client = None
    if dry:
        from fake import FakeAsyncAnthropic
        client = FakeAsyncAnthropic()
    return Claude(run, cfg, client=client)


async def run_stage(run: Run, stage: str, args) -> None:
    cfg = load_config()
    if not args.auto:
        run.require_previous_approved(stage)
    claude = make_claude(run, cfg, args.dry_run)
    print(f"[{run.id}] {stage}: starting (run spent so far ${claude.spent:.2f} of ${claude.budget:.2f})")
    run.mark_stage(stage, "running")
    try:
        msg = await RUNNERS[stage](run, cfg, claude, args)
    except (BudgetExceeded, SpendCapReached) as e:
        run.mark_stage(stage, "stopped", reason=str(e))
        raise SystemExit(f"{stage} stopped: {e}")
    run.mark_stage(stage, "done", spent_usd=round(claude.spent, 3))
    print(f"[{run.id}] {stage}: {msg}\n  Run total: ${claude.spent:.2f}")
    if not args.auto:
        print(f"  Review runs/{run.id}/{stage}/output/ then: python harness/icm.py approve {stage[:2]} --note \"...\"")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new"); p.add_argument("--label", default="")
    for name in ("run", "all"):
        p = sub.add_parser(name)
        if name == "run":
            p.add_argument("stage")
        p.add_argument("--run"); p.add_argument("--only", help="comma-separated work package IDs (stage 02)")
        p.add_argument("--force", action="store_true", help="redo work packages that already have output")
        p.add_argument("--auto", action="store_true", help="skip human approval gates")
        p.add_argument("--dry-run", action="store_true", help="use a fake API, no cost")
    p = sub.add_parser("approve"); p.add_argument("stage"); p.add_argument("--run")
    p.add_argument("--note", default=""); p.add_argument("--by", default=getpass.getuser())
    p.add_argument("--skip", action="store_true", help="approve a stage you chose not to run (for example 01)")
    for name in ("status", "cost", "refresh-context"):
        p = sub.add_parser(name); p.add_argument("--run")
    args = ap.parse_args()

    if args.cmd == "new":
        run = Run.create(args.label)
        print(f"Created run {run.id}. Context frozen into runs/{run.id}/context/.\nNext: python harness/icm.py run 01")
        return
    run = Run.latest_or(getattr(args, "run", None))
    if args.cmd == "run":
        asyncio.run(run_stage(run, stage_name(args.stage), args))
    elif args.cmd == "all":
        if not args.auto:
            raise SystemExit("'all' runs every stage without human review, so it needs --auto. "
                             "For a gated run, use 'run 01', 'approve 01', 'run 02', and so on.")
        for s in STAGES:
            asyncio.run(run_stage(run, s, args))
    elif args.cmd == "approve":
        s = stage_name(args.stage)
        run.approve(s, args.by, args.note, skip=args.skip)
        print(f"{'Skipped' if args.skip else 'Approved'} {s} for run {run.id} by {args.by}.")
    elif args.cmd == "refresh-context":
        run.snapshot_context(reason="manual refresh")
        print(f"Re-froze L0 to L3 for run {run.id}. The change is recorded in manifest.json context_versions.")
    elif args.cmd == "status":
        m = run.manifest
        print(f"Run {run.id} (created {m['created_at']}, {len(m['context_versions'])} context version(s))")
        for s in STAGES:
            st = m["stages"].get(s, {}).get("status", "not run")
            ap_ = m["approvals"].get(s)
            print(f"  {s:15} {st:9} " + (f"approved by {ap_['by']} {ap_['at']}" if ap_ else ""))
        print(f"  Spent: ${run.spent_usd():.2f}")
    elif args.cmd == "cost":
        by = defaultdict(lambda: [0.0, 0, 0, 0])
        for e in run.events():
            if e.get("type") == "api_call":
                b = by[(e["stage"], e["model_served"])]
                b[0] += e["cost_usd"]; b[1] += 1; b[2] += e.get("web_search_requests") or 0
                b[3] += e.get("cache_read") or 0
        print(f"{'stage':15} {'model':22} {'calls':>5} {'searches':>8} {'cache read tok':>14} {'cost':>9}")
        for (s, mdl), (c, n, ws, cr) in sorted(by.items()):
            print(f"{s:15} {mdl:22} {n:5} {ws:8} {cr:14} ${c:8.2f}")
        print(f"Total ${run.spent_usd():.2f} (estimate from the pricing table in config.yaml)")


if __name__ == "__main__":
    main()
