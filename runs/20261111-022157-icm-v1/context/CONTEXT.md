# L1: Workspace routing

This workspace answers the research brief in `reference/brief.md`. It runs in six stages. Each stage reads the previous stage's `output/` for the current run, and a human approves each stage before the next one starts.

| Stage | Folder | Job | Tools | Output |
|---|---|---|---|---|
| 01 | `stages/01-plan` | Check that the work packages cover every requirement in the brief | none | `plan-review.md` |
| 02 | `stages/02-research` | One worker per work package: search, read, write cited findings | web search, web fetch | `WP-*.md`, `WP-*.claims.json` |
| 03 | `stages/03-verify` | A separate verifier re-reads every cited source and checks each claim | web fetch, web search | `ledger.json`, `ledger.md` |
| 04 | `stages/04-architect` | Candidate architectures, scored decision matrix, recommendation, prototype plan | none | `architecture.md` |
| 05 | `stages/05-synthesize` | Write the final report in the brief's format | none | `report.md` |
| 06 | `stages/06-qa` | Deterministic checks plus a red-team read | none | `qa.md` |

## Layers

* L0: `CLAUDE.md` (identity and evidence rules, loaded in every stage)
* L1: this file (routing, read by the harness and by humans)
* L2: `stages/NN-*/CONTEXT.md` (one stage's inputs, process, outputs; front matter sets model, effort, tools, and which L3 files to load)
* L3: `reference/` (the brief, the evidence standard, the work packages, style)
* L4: `runs/<run-id>/` (every run's outputs, raw API responses, event log, approvals, and a frozen copy of L0 to L3)

## Rules for routing

* Stage outputs never overwrite another run. Each run gets its own folder under `runs/`.
* A stage only reads from its own run folder and from L0 to L3.
* Stage 04 and later never touch the web. They only use the verified ledger, so every fact in the report traces back to a checked source.
* Editing L0 to L3 changes future runs only. The run folder keeps the exact context it used.
