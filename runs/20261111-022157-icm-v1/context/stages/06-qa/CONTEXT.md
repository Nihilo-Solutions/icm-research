---
stage: 06-qa
model: claude-fable-5-2
effort: high
max_tokens: 64000
tools: []
reference: [brief.md, evidence-standard.md]
---
# L2: Stage 06, red-team review

The harness has already run deterministic checks (section presence, citation IDs, unverified tagging, dashes, source list). Their results are included below. Your job is the judgment part.

## Inputs

* The final report
* The verified claim ledger
* The deterministic check results

## Process

Read the report as a skeptical client's CISO and as a skeptical investor. Find:

1. The 10 statements most likely to be wrong or overstated, and why. Check each against the ledger: is the cited claim's status and wording at least as strong as the sentence that uses it?
2. Contradictions between sections.
3. Brief requirements that are missing or answered only vaguely.
4. Recommendations that rest on unverified claims or assumptions without saying so.
5. Anything that would embarrass Nihilo in front of a regulated buyer.

## Output

Markdown with those five sections, then a short "Fix list" in priority order. Each fix names the section and the exact change. Do not rewrite the report.
