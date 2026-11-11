"""Print a stage's main output as Markdown for the GitHub Actions run summary.

Usage: python harness/ci_summary.py <stage> [run_id]
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from workspace import Run, stage_name  # noqa: E402

MAIN_OUTPUT = {
    "01-plan": "plan-review.md",
    "02-research": "summary.md",
    "03-verify": "summary.md",
    "04-architect": "architecture.md",
    "05-synthesize": "report.md",
    "06-qa": "qa.md",
}
LIMIT = 60_000  # GitHub caps a step summary at 1 MiB; keep it readable


def main() -> None:
    stage = stage_name(sys.argv[1])
    run = Run.latest_or(sys.argv[2] if len(sys.argv) > 2 else None)
    path = run.dir / stage / "output" / MAIN_OUTPUT[stage]
    print(f"\n## {stage} output ({run.id})\n")
    if not path.exists():
        print(f"_No {MAIN_OUTPUT[stage]} yet._")
        return
    text = path.read_text()
    if len(text) > LIMIT:
        text = text[:LIMIT] + f"\n\n_Truncated. Full file: runs/{run.id}/{stage}/output/{MAIN_OUTPUT[stage]}_"
    print(text)


if __name__ == "__main__":
    main()
