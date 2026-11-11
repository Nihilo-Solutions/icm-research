---
stage: 04-architect
model: claude-fable-5-2
effort: xhigh
max_tokens: 64000
tools: []
reference: [brief.md, evidence-standard.md, style.md]
---
# L2: Stage 04, architecture, recommendation, prototype plan

## Inputs

* The verified claim ledger: every claim with its final status after independent verification, grouped by brief item. Each claim has an ID like `C-WPQ06A-003`.
* The open questions from research and verification.

You have no web access in this stage, on purpose. Every fact you use must come from the ledger.

## Rules

* Cite ledger claims inline by ID in square brackets, for example `[C-WPQ06A-003]`. Cite only IDs that appear in the ledger. Never invent an ID.
* If you need a fact that is not in the ledger, state it as an assumption, tagged `[assumption]`, and add it to the assumptions list. Do not present it as fact.
* If a claim you rely on has status `unverified`, write "(unverified)" next to its citation and count it as a risk.
* Scores are judgments: tag the matrix as `[inference]` and give a one-line justification per cell that cites claim IDs where possible.

## Process

1. Build the hosting model comparison for Q5 as a table: rows are data residency, processor obligations and contracts, security review friction, required certifications, liability and insurance, operating cost and margin, buyout or transfer path, regulated buyer reaction; columns are Nihilo-hosted, client-tenant, hybrid.
2. Design 2 or 3 candidate reference architectures for an enterprise ICM deployment that solve the unsolved problem in the brief (non-technical staff, no terminal, inside existing systems, enterprise controls). Make them genuinely different (for example, Microsoft-native surface, custom web app on an agent runtime in the client tenant, hybrid control plane). For each: a Mermaid flowchart, the components by layer (surface, runtime, model access, workspace storage and versioning, identity, secrets, network, logging, integrations), how L0 to L4 map onto it, and its hosting model.
3. Score each candidate 1 to 5 on every criterion in the brief's decision matrix, with a one-line justification per cell. Show totals, and also show a weighted total using these weights, which reflect Nihilo's goals: non-technical usability 2, security 2, oversight 2, integration reach 1, scalability 1, small-firm fit 2, enterprise fit 1, build effort 2, running cost 1, compliance evidence 1, portability 1. Say how the ranking changes without weights.
4. Recommend one architecture and one packaging model. Give the reasoning, the three biggest risks, the assumptions, and what evidence would change the call.
5. Write the prototype plan: the smallest build that proves the recommended architecture, with test case 1 in Nihilo's own Azure tenant and Microsoft 365, and test case 2 on SharePoint. Give scope, steps, a time estimate for a part-time engineer (labeled estimate), and pass or fail criteria that are measurable.

## Outputs

Markdown with these sections, using the brief's numbering:

* 4. Hosting model comparison
* 5. Candidate architectures and decision matrix
* 6. Recommendation (chosen architecture, packaging, pricing basis, assumptions, what would change the call)
* 7. Prototype plan
* Assumptions list
