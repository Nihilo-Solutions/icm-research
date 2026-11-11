# ICM research harness

A staged, verifiable research pipeline for the brief "ICM as an enterprise service", built as an ICM workspace and run against the Claude API with Claude Fable 5.2 (`claude-fable-5-2`).

It replaces a single research-agent session with six stages, a human sign-off between each, and a claim ledger where every fact traces back to a source the API itself attached.

## Why this beats a single research agent run

| Problem with one long agent session | What this harness does instead |
|---|---|
| Coverage drifts: the agent goes deep on 5 questions and skims 12 | 22 work packages, each with a `must_answer` checklist, run in parallel; stage 01 checks coverage against the brief before you spend money |
| URLs in the report can be invented or misremembered | Sources come only from the API's citation and fetch blocks. A source ID the model writes that the API did not attach is dropped. A "confirmed" fact with no attached citation is downgraded to unverified automatically |
| The writer grades its own homework | Stage 03 is a separate verifier with a fresh context that re-fetches every cited page and rules supported, partial, not supported, unreachable, or secondary only |
| Synthesis quietly adds facts from memory | Stages 04 to 06 have no web access and must cite ledger claim IDs. Unknown IDs are caught, unverified claims are force-labeled, section 9 is generated from the ledger, not written by the model |
| No audit trail | Every request and response is saved, every call logged with request ID, model actually served, tokens, searches, and cost. Each run freezes a hashed copy of L0 to L3, and each approval hashes the outputs it approved |
| Security topics can trip refusals | Fable 5.2 runs with server-side fallback, and the log shows which model answered |

It also doubles as Nihilo's first internal ICM case study: it fixes the run history, overwrite, and versioning critiques (baseline item B6) and produces exactly the kind of evidence Q3 and Q12 ask about.

## Layout (ICM layers)

```
CLAUDE.md                     L0  identity and evidence rules (loaded in every stage)
CONTEXT.md                    L1  routing: what each stage does
reference/                    L3  brief.md, evidence-standard.md, style.md, workpackages.yaml
stages/NN-*/CONTEXT.md        L2  one stage's inputs, process, outputs; front matter sets model, effort, tools, L3 files
runs/<run-id>/                L4  one folder per run, never overwritten
  context/                        frozen copy of L0 to L3 used by this run
  manifest.json                   context hashes, git commit, approvals with output hashes
  events.jsonl                    one line per API call or approval
  raw/<stage>/                    full request and response JSON (replay and audit)
  sources.json                    run-wide source registry (S1, S2, ...) from API citations
  NN-stage/output/                the stage's handoff to the next stage
harness/                      Python runner (icm.py, llm.py, ledger.py, workspace.py, fake.py, config.yaml)
tests/                        offline tests, no API key needed
```

The same folder also works in Claude Code: open it, and the agent can read `CLAUDE.md` and each stage's `CONTEXT.md` the usual ICM way. The harness is what you use when you want parallel workers, verification, budgets, and logs.

## Running it from GitHub (recommended for following along)

The repo carries two workflows:

* **Tests** runs the offline test suite on every push.
* **Research run** (Actions tab, "Run workflow") runs one harness command: `new`, `run`, `approve`, or `status`. It writes the stage output and the run's cost table to the workflow summary page, commits everything under `runs/` back to `main`, and uploads the raw API payloads as a 90-day artifact. Approvals made here record your GitHub username.

One-time setup: add your Claude API key as a repository secret named `ANTHROPIC_API_KEY` (Settings, Secrets and variables, Actions), or from a terminal:

```
gh secret set ANTHROPIC_API_KEY -R Nihilo-Solutions/icm-research
```

A gated study from the Actions tab looks like: `new` (label it) > `run 01` > read the summary > `approve 01` with a note > `run 02` with `only` set to three packages as a pilot > `run 02` > `approve 02` > and so on through 06. The final report lands at `runs/<run-id>/05-synthesize/output/report.md`, readable right on GitHub with Mermaid diagrams rendered.

You can mix local and GitHub runs on the same study. Pull before you start locally and push when you finish, because both write `runs/LATEST` and the manifest.

## Local setup

1. Python 3.11 or later, then `pip install -r requirements.txt`.
2. In the Claude Console, create a workspace named something like `icm-research`, set a workspace spend limit, and create an API key in it. This keeps the run's cost visible on its own line in Usage.
3. Confirm web search is enabled for the organization (Console, Settings, Capabilities). If it is off, every research call fails with a 400.
4. `export ANTHROPIC_API_KEY=...`
5. Run the offline checks: `python -m pytest -q tests` (uses a fake API; costs nothing).

## Running a study

```
python harness/icm.py new --label icm-v1
python harness/icm.py run 01                      # coverage review, about a dollar
#   read runs/<id>/01-plan/output/plan-review.md, edit reference/workpackages.yaml if needed, then:
python harness/icm.py refresh-context             # only if you edited L0 to L3 (logged in the manifest)
python harness/icm.py approve 01 --note "added Purview angle to WP-Q12"

python harness/icm.py run 02 --only WP-B1,WP-Q06A,WP-Q14   # pilot three packages to calibrate cost
python harness/icm.py cost
python harness/icm.py run 02                      # the rest (finished packages are kept, not redone)
python harness/icm.py approve 02 --note "..."

python harness/icm.py run 03 && python harness/icm.py approve 03 --note "..."
python harness/icm.py run 04 && python harness/icm.py approve 04 --note "..."
python harness/icm.py run 05 && python harness/icm.py approve 05 --note "..."
python harness/icm.py run 06
python harness/icm.py status
```

Useful flags: `--force` redoes work packages that already have output, `--run <id>` targets an older run, `--dry-run` exercises any stage with the fake API, `approve 01 --skip` records a deliberate skip.

### What to review at each gate

* 01: the coverage table and gaps. Fix `workpackages.yaml` now; it is the cheapest point to change scope.
* 02: `summary.md` (claims by status per package, searches, cost, model served), then skim any package with many unverified claims or a declined status. Rerun a weak package with `--only WP-xx --force`.
* 03: `summary.md` lists every claim the verifier rejected or weakened. Spot-check a few against the pages yourself. `ledger.md` is what stages 04 and 05 will see.
* 04: the architectures, matrix, recommendation, and prototype plan. This is the judgment layer, so this is where your domain knowledge matters most.
* 05: `report.md` is the deliverable. `report-traceable.md` is the same text with claim IDs, so you can trace any sentence to the ledger.
* 06: `qa.md`, deterministic failures first, then the red-team fix list.

## Cost

All figures are estimates. Pricing in `harness/config.yaml` comes from Anthropic's model pages, accessed 2026-11-10: Fable 5.2 is $8 input and $40 output per million tokens, cache reads $0.20; web search is $10 per 1,000 searches; web fetch has no fee beyond tokens.

| Stage | Rough estimate | Basis |
|---|---|---|
| 01 plan | $1 or less | one call, about 15k tokens in |
| 02 research | $60 to $180 | 22 workers, up to 25 searches and 20 fetches each; search results count as input tokens |
| 03 verify | $20 to $60 | one call per cited source, about 100 to 150 calls |
| 04 to 06 | $5 to $15 | three long calls over the ledger |

The default budget guard is $175 per run (`run.budget_usd`). Pilot three packages first, run `cost`, and scale the estimate before running the rest. The Start usage tier caps API spend at $500 per month.

Cost levers, in order of impact: lower `max_searches` and `max_fetches` per package in `workpackages.yaml`; set `verify.scope: risky`; set `effort: medium` for stage 02; turn on `dynamic_filtering` (see below).

## Things to know about Fable 5.2 (from Anthropic's docs, accessed 2026-11-10)

* Released November 9, 2026. Model ID `claude-fable-5-2`. 1M context, 128K max output.
* Adaptive thinking is always on; control depth with `output_config.effort` (default `high`). Do not send `temperature`, `top_p`, `top_k`, prefill, or `tool_choice` of `any` or `tool` (all return 400). The harness sends none of these.
* Requires 30-day data retention; it is not available under zero data retention. Do not feed client confidential data through this research setup.
* It has its own rate limit bucket (Start tier: 4,000 RPM, 500k uncached input tokens per minute). Cached input does not count toward that limit, which is why the shared L0 and L3 system prompt is cached.
* Structured JSON outputs cannot be combined with citations, so research workers write cited prose and a cheaper Sonnet 5.5 call converts it into the claim list.

## Not yet verified (test on the first real run)

* Whether web search citations still attach to Claude's text when dynamic filtering is on. It is off by default (`allowed_callers: ["direct"]`) to protect the audit trail. Try it on one package and compare the claims file before switching.
* Whether `web_fetch_20260318` accepts `allowed_callers`. If the API rejects it, the harness retries once without it.
* How often security-heavy packages (WP-Q09, WP-Q11) trigger a refusal and fall back. Check `fallback` in `events.jsonl`.
* Real per-package cost. The table above is an estimate until the pilot runs.

## Known limits

* The verifier checks claims against the page they cite. It catches misreadings and stale pages, not errors that the page itself contains.
* Trademark searches (Q17) usually need a human: the USPTO and EUIPO tools are interactive apps. Expect those claims to come back unverified with manual search steps.
* Claims are extracted by a model from tagged paragraphs. The deterministic checks stop invented sources, but a badly split paragraph can still merge two facts under one citation. Spot-check the ledger at gate 03.
