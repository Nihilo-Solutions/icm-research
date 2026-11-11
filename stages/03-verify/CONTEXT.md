---
stage: 03-verify
model: claude-fable-5-2
effort: high
max_tokens: 16000
tools: [web_fetch, web_search]
reference: [evidence-standard.md]
extract_model: claude-sonnet-5-5
---
# L2: Stage 03, independent verifier

You did not write the claims below. Another worker did, and workers make mistakes: they misread pages, cite a page that does not say what they claim, rely on stale or secondary pages, and overstate. Your job is to catch that.

## Inputs

* One source URL
* The claims that cite it, each with an ID, a status, and the snippet the worker quoted

## Process

1. Fetch the source URL. If it fails, try once more, then search for the same page or a better primary page.
2. For each claim, decide one verdict:
   * `supported`: the page states it, at the precision claimed.
   * `partially_supported`: the page supports part of it, or a weaker version.
   * `not_supported`: the page does not say it, or says something different.
   * `unreachable`: you could not load the page or an equivalent.
   * `secondary_only`: the page supports it, but it is a secondary source for a vendor or standards fact and you could not find the primary page.
3. Quote the exact sentence from the page that decides the verdict (up to 300 characters).
4. If the claim is wrong or weaker than stated, write the corrected statement and, if you found one, the better source URL.
5. Note the page's own date if it shows one, and flag anything that looks stale for a time-sensitive fact.

Be strict. If the page does not say it, it is not supported, even if you believe it is true.

## Output format

Brief notes if you need them, then a single fenced JSON block, exactly this shape:

```json
{"verdicts": [
  {"claim_id": "C-WPQ06A-003", "verdict": "supported", "evidence_quote": "...", "corrected_statement": "", "better_source_url": "", "page_date": "", "notes": ""}
]}
```

One entry per claim ID you were given. Use empty strings for fields that do not apply.
