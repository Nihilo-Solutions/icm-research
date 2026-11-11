---
stage: 01-plan
model: claude-fable-5-2
effort: high
max_tokens: 64000
tools: []
reference: [brief.md, evidence-standard.md, workpackages.yaml]
---
# L2: Stage 01, plan review

## Inputs

* The brief (`brief.md`)
* The work packages (`workpackages.yaml`)

## Process

1. List every requirement in the brief that the research stage must settle: baseline items B1 to B8, questions Q1 to Q17 and each of their sub-bullets, and the facts that steps 3 to 5 (architectures, recommendation, prototype plan) will need.
2. For each requirement, name the work package that covers it, or write "GAP".
3. Find overlaps where two packages will duplicate expensive searching, and say which package should own the item.
4. Suggest additional search angles or start URLs where a package looks thin. Only suggest URLs you are confident exist, and mark each "unconfirmed URL".
5. Flag any package whose scope is too large for one worker with about 25 searches and 20 page fetches, and propose a split.

Do not research. Do not use your memory as evidence. This stage only checks coverage.

## Outputs

A Markdown document with these sections:

1. Coverage table: requirement, owning package, notes
2. Gaps
3. Overlaps
4. Suggested edits to `workpackages.yaml`, as YAML snippets the human can paste
5. Risks to the research plan (for example, items likely to stay unverified, such as trademark searches)
