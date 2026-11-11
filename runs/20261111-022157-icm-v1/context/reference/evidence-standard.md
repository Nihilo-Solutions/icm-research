# L3: Evidence standard

## How to write findings (research and verify stages)

* One claim per paragraph. Keep it to one or two sentences, so the citation attaches to exactly that claim.
* Start each claim paragraph with its status tag in square brackets: `[confirmed]`, `[corrected]`, `[unverified]`, `[estimate]`, or `[inference]`.
* Put the brief's reference at the start of the tag when the claim answers a specific item, for example `[confirmed B2]`, `[unverified Q6]`, `[estimate Q14]`.
* For `[corrected]`, state both what was believed and what the source says.
* For `[unverified]`, end with "Next check:" and a concrete action (a URL to open, a person to ask, a search to run, a test to perform).
* For `[estimate]`, state the arithmetic or the basis and cite each input.
* For time-sensitive facts, include the page's own date if it shows one ("page updated 2026-10-14").

## Source quality ladder

1. Vendor documentation and official pricing pages
2. Standards bodies and regulators (NIST, ISO, OWASP, AICPA, MITRE, EU official journal, USPTO, EUIPO)
3. The ICM paper (arXiv) and the reference repo (GitHub)
4. Vendor blogs, official announcements, conference talks by the vendor
5. Reputable secondary sources (analyst firms, established trade press)
6. Community posts, forums, social media, marketplaces (use only to find leads, or label as "community report")

If the best source you found is level 5 or 6 for a vendor fact, keep looking for the level 1 page. If you cannot find it, say so.

## Independence

When judging whether ICM works, separate evidence from the authors and their community (paper, repo, Skool, Eduba, the authors' social posts) from independent evidence. Label which is which.

## Things that must always be tagged unverified unless a primary page says so

* Any price or fee
* Any claim that a model is available in a specific cloud region
* Any certification, compliance attestation, or legal status
* Any trademark search result (the USPTO and EUIPO search tools are interactive web apps that are often not fetchable; if you cannot load results, say so and give the exact search to run by hand)
* Any user count, revenue, or customer number
