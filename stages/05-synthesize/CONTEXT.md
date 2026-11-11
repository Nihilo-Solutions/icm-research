---
stage: 05-synthesize
model: claude-fable-5-2
effort: high
max_tokens: 128000
tools: []
reference: [brief.md, evidence-standard.md, style.md]
---
# L2: Stage 05, final report

## Inputs

* The verified claim ledger
* The open questions list
* The approved stage 04 output (sections 4 to 7 and assumptions)

You have no web access in this stage. Every fact comes from the ledger.

## Rules

* Cite ledger claims inline by ID in square brackets, for example `[C-WPB1-002]`. Only cite IDs in the ledger. The harness turns these into numbered sources and builds section 9 for you, so do not write section 9.
* A claim with status `unverified` must be written as unverified in the sentence that uses it.
* Never upgrade a claim's certainty. If the ledger says `partially_supported`, write the weaker version.
* Keep stage 04's sections 4 to 7 substantively unchanged. You may tighten wording and fix consistency with sections 1 to 3. If you find a contradiction between stage 04 and the ledger, keep the ledger's version and list the contradiction under open questions.

## Process

1. Section 2, baseline validation: one row per item B1 to B8 with status (confirmed, corrected, unverified), the correction if any, and citations.
2. Section 3: answer Q1 to Q17, numbered to match, each with citations. Answer the question first, then the evidence.
3. Insert sections 4 to 7 from stage 04.
4. Section 8, open questions: every unverified claim that matters, every open question from research and verification, every assumption from stage 04, each with its specific next check.
5. Write section 1, executive summary, last: at most 10 lines, with the recommendation, the top 3 risks, and the first thing to prototype.

## Output

One Markdown report with sections 1 to 8 in the brief's format, sentence-case headings, no em dashes or en dashes.
