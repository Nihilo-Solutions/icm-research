<!-- {"wp": "WP-B2", "models": ["claude-fable-5-2"], "rendered_from_raw": true, "claims_extracted": false} -->
# WP-B2: Baseline, the ecosystem around ICM

### Findings

All pages were accessed 2026-11-11. No page showed its own date unless noted.

**Eduba**

[confirmed B7] The eduba.io homepage pitches a veteran-owned consulting and training business under three headings: Build, Teach, Govern.

[confirmed B7] Under Build, the stated deliverables are multi-agent systems and production infrastructure, plus advice on what to leave unbuilt. {S68}

[confirmed B7] The fetched homepage text never uses "ICM" or "Interpretable Context Methodology" (my reading of the page; an absence cannot be cited to a line). Its navigation does link out to the Clief Notes group on Skool. {S68}

[corrected B7] The brief said Eduba does not name ICM. Search-index excerpts of lyceum.eduba.io show ICM named outright as the subject of Eduba's certification program. {S80} Direct fetch of that subdomain was blocked, so this rests on excerpts only.

[confirmed B7] Five people appear in the team section: Jake Van Clief (Founder and CEO), David McDermott (Chief Architect), Kay K. (Design and Technical Lead), Matthew Creamer (CRO), and Nicholas Rondino (COO). {S68} The first two are the ICM paper's authors.

[confirmed B7] The terms of service on chat.eduba.io (last updated July 14, 2026) name the contracting party as Van Clief Media LLC, a Florida registrant trading as Eduba. {S79}

[confirmed B7] Software is now part of the Eduba offer, which the brief missed. Its terms list a product called Edubaware for standing up structured AI context systems, with file and folder management, multi-provider model access, workflow runs, credential storage, and multi-organization sharing. {S79}

[confirmed B7] A second product, Ledger at talent.eduba.io, places vetted community members with hiring companies. {S79}

[confirmed B7] Regulated workloads are excluded by those terms: HIPAA or FISMA covered use is barred, and health or cardholder data needs Eduba's written agreement. {S79}

[confirmed B7] A competing-use clause also sits in the prohibited-activities list, barring anyone from building a rival product or service with the Services. {S79}

[unverified B7] Edubaware maturity is not settled. Closed testing with a wider rollout "next week" is how a recent LinkedIn post by the founder describes it {S81} (search excerpt, level 6 source). A chat.eduba.io excerpt advertises organizations, role-based access, and per-workspace message history for audit {S82} (not fetched). Next check: open https://chat.eduba.io/for-enterprise and https://auth.eduba.io in a browser.

[confirmed B7, vendor self-report] Client names on the homepage include Pacific Life and Colgate-Palmolive (via Correlation One) and KPMG UK, with a figure of 600+ employees trained. {S68} None of this is independently verified.

[inference] Eduba's training numbers are inconsistent across its own pages: 600+ on eduba.io, 1000+ on the Skool about page {S69}, and 1,500+ for Pacific Life alone in the Lyceum excerpt {S80}. Treat all of them as marketing.

**Clief Notes on Skool**

[confirmed B7] The Skool about page counter read 55.3k members when fetched uncached, with the group marked public and free and attributed to Jake Van Clief. {S69}

[confirmed B7] Other member figures are stale copy. The same page's description still says 43,000+ {S69}, the plans page says 50,000+ {S69}, and eduba.io says 12,500+ {S68}. Use the live counter.

[confirmed B7] Three plans appear on the Skool plans page (fetched uncached): Standard at $0/month, Premium at $11/month, and VIP at $97/month.

[confirmed B7] Premium buyers get downloadable Vault packages, a monthly group session, and Discord access; VIP adds a monthly one-hour live call with Jake, recordings, and custom packages.

[confirmed B7] Prices have moved several times in 2026. A March 9 announcement put Premium at $7/mo {S83} (search excerpt). A June 30 sale post by Matthew Creamer listed Premium at $27 cut to $14 and VIP at $97 cut to $67. {S74} Today's $11 Premium matches neither.

[unverified B7] One third-party review lists a $5,000 one-time Lifetime VIP that includes The Lyceum. {S84} The public plans page does not show it. Next check: view https://www.skool.com/cliefnotes/plans while logged in.

[confirmed B7] The official icm-architect README points readers to Clief Notes as the ICM community. {S21}

**Community and official tools**

[confirmed B7] Taurus exists. A Skool post titled "ICM on enterprise level - introducing Taurus" went up on June 10 under Show Your Work, authored by Arjen Stet, and shows 32 likes and 42 comments. {S75}

[confirmed B7] Search-index excerpts of the GitHub repo astetic-dev/taurus describe a small Tauri desktop app that hosts several Claude Code sessions as terminal tabs, its stated contribution being to start each agent in the correct process folder. {S85} The repo calls the method "Interpreted Context Methodology".

[unverified B7] Taurus maturity details come from search excerpts only, because the repo fetch failed (fetch budget exhausted). Version 0.7.7 is dated September 27 and adds a native macOS build beside Windows; agent choices are Claude Code, a Gemini-backed CLI, and Grok Build. {S85} {S86} License, stars, and contributor count are unknown. Next check: open https://github.com/astetic-dev/taurus and its releases page.

[inference] "Enterprise launcher" overstates Taurus. What I retrieved shows a desktop wrapper around terminal agent sessions, with no evidence of SSO, RBAC, or audit logging. It does not solve Nihilo's no-terminal problem. Whether GitHub account astetic-dev is Arjen Stet is likely but not confirmed.

[confirmed B7] The `icm-template` skill set exists at github.com/ktnCodes/icm-template. Three Claude Code skills ship in it: /icm-scaffold, /icm-sync, and /icm-context-scaffold. {S70}

[confirmed B7] That repo is MIT licensed and shows 33 stars, 4 forks, 2 commits, and no releases. {S70} Optional adapter files cover Claude Code, Cursor, GitHub Copilot, and Windsurf. {S70}

[inference] icm-template is an early, single-author project (two commits). It is useful as a pattern reference, not as a dependency.

[confirmed B7] An official workspace generator exists inside the reference repo. Its workspace-builder is a five-stage workspace (discovery, mapping, scaffolding, questionnaire design, validation) that outputs a new workspace. {S2}

[confirmed B7] A community web generator exists at workflowcreate.netlify.app. Titled "ICM Workspace Builder" and labeled as based on the Clief Notes community, it runs a guided wizard, returns a populated .zip, and describes a six-layer variant of ICM. {S76} Its author and source code are not identified on the page.

[confirmed B7] A community CLI generator exists on PyPI as `icm-workspace-template`. The page I fetched (0.13.0, released May 31, 2026, with 0.19.0 flagged as newer) carries an Alpha classifier, calls itself experimental and unofficial, and names "Hobo" as maintainer.

[unverified B7] Other generators appeared in search results only: carloswecare/icm-builder, dmed05/icm-concept, sarmad4444/icm-factory. Their maturity is unchecked. Next check: open each repo and read commits, license, and issues.

[confirmed B7] The brief missed an official tool: github.com/RinDig/icm-architect. It is an MIT-licensed agent skill in the open Agent Skills format, showing 2.0k stars, 284 forks, and 13 commits. {S21} Two modes are offered: Build from a described process, and Restructure an existing folder.

[confirmed B7] For comparison, the main reference repo shows 1.4k stars, 243 forks, and 21 commits under MIT. {S2}

[confirmed B7] A volunteer-run catalog at github.com/FiSimply/clief-notes-index lists 72 community tools in 7 categories for March to June 2026, including an ICM / Workspace category. {S71} It is the best lead list for further tool checks.

[inference] The GitHub topic "icm" is not a usable ecosystem measure. Its 126 repositories mix in unrelated uses of the acronym, such as poker tooling. {S72}

**Partner, certification, implementer programs**

[corrected B7] The brief said no certification program was found. Eduba's homepage advertises The Lyceum as a twelve-week certification program with skill-level cohorts and capstone work.

[unverified B7] Lyceum specifics rest on search excerpts because lyceum.eduba.io refused the fetch. Those excerpts show an "Eduba ICM Certification" for individuals, three tracks (Technical, Business, Creator), a waitlist, and pricing to be announced at cohort launch. {S80} Next check: open https://lyceum.eduba.io and https://lyceum.eduba.io/terms/ in a browser.

[unverified B7] I found no partner, reseller, licensed-implementer, or agency certification program. Nothing of the kind appears on the eduba.io homepage, the two RinDig READMEs, or the Skool about and plans pages. Absence is not proof. Next check: email info@eduba.io and read https://chat.eduba.io/for-enterprise.

[inference] The nearest things to a channel are the individual Lyceum certificate and the Ledger talent marketplace {S79}. Neither authorizes a firm to sell "official" ICM work.

[inference] Community norm is to disclaim endorsement. One third-party ICM field guide instructs redistributors not to imply backing from Jake Van Clief or Eduba {S87} (search excerpt, level 6).

### Answer summary

**B7, Eduba.** Corrected in part. Eduba sells AI build, teaching, and governance consulting, and its homepage does not name ICM. But Eduba does name ICM on its Lyceum certification pages (excerpt only), and it now also sells software (Edubaware, Ledger). It is run by Jake Van Clief and David McDermott with three other named executives, under Van Clief Media LLC. [inference] Edubaware makes Eduba a direct product competitor to an "ICM as a service" offer, not just an upstream method author.

**B7, Clief Notes.** Confirmed. The live counter shows 55.3k members. Plans are Standard $0, Premium $11/month, VIP $97/month, and prices have changed at least three times this year.

**B7, community tools.** Confirmed, with corrections:
- Taurus is real but is a desktop launcher for terminal agent sessions, not an enterprise platform.
- `icm-template` is real, MIT, and very early.
- Workspace generators exist both officially (workspace-builder in the reference repo) and in the community (a Netlify wizard, an alpha PyPI CLI).
- The official icm-architect skill was missing from the brief.

**B7, partner or certification program.** Corrected. A certification program for individuals exists (The Lyceum). No partner or implementer program for firms was found; that part stays unverified.

**B7, trademarks.** Not in this package's checklist and not researched here.

### Coverage checklist

- **What Eduba sells, whether it names ICM, who runs it:** covered. Homepage and terms were fetched. Lyceum ICM naming is from excerpts only.
- **Clief Notes member count, tiers, prices:** covered. About and plans pages were fetched uncached. Lifetime VIP is unverified.
- **Taurus, icm-template, workspace generator (existence, where, by whom, maturity):** partly covered. Existence and location are settled for all three. Taurus repo metadata, the Taurus author link, and the Netlify tool's author are not settled.
- **Official partner, certification, or implementer program:** partly covered. Certification is confirmed on eduba.io with details unverified. Absence of a partner program cannot be proven from public pages.

### Open questions

1. Lyceum price, dates, and whether it has run a cohort yet. Next check: open https://lyceum.eduba.io in a browser, or email lyceum@eduba.io.
2. Whether Eduba offers or plans any partner or implementer arrangement. Next check: email info@eduba.io, and read https://chat.eduba.io/for-enterprise.
3. Edubaware feature set, pricing, and availability. Next check: fetch https://chat.eduba.io/for-enterprise and https://auth.eduba.io, and watch the vendor video "What Is Edubaware?" on YouTube.
4. Taurus license, stars, and maintainer identity. Next check: open https://github.com/astetic-dev/taurus and its LICENSE file.
5. Who built workflowcreate.netlify.app and whether source is public. Next check: view page source and search the Skool Resources & Finds category.
6. Lifetime VIP at $5,000. Next check: logged-in view of the Skool plans page.
7. Lead for the B1 owner: the Lyceum excerpt describes ICM as peer-reviewed while noting only a submission to ACM TiiS {S80}. Submission is not peer review. Next check: search ACM TiiS for an accepted paper.
8. Lead for the B8 owner: the reference README still titles the paper "Model Workspace Protocol", and icm-template cites the repo under an older MWP name {S70} {S2}. This suggests MWP was the earlier name. Next check: compare arXiv v1 and v2 abstracts.

## Sources attached by the API

- S2: GitHub - RinDig/Interpretable-Context-Methodology: Folder structure as agent architecture.  ICM replaces framework-level orchestration with filesystem structure. https://github.com/RinDig/Interpretable-Context-Methodology
- S21: GitHub - RinDig/icm-architect: Agent skill: design any process, idea, or problem into an ICM workspace (folder structure as agent architecture), or restructure an existing folder into one · GitHub https://github.com/RinDig/icm-architect
- S68: EDUBA https://eduba.io
- S69: Clief Notes https://www.skool.com/cliefnotes/about?jg=true&aj=true&auth=true
- S70: GitHub - ktnCodes/icm-template: A model-agnostic template for organizing AI workflows using folder structure — based on the Interpretable Context Methodology https://github.com/ktnCodes/icm-template
- S71: GitHub - FiSimply/clief-notes-index: Community-maintained index of tools, skills, and resources shared on Clief Notes (skool.com/cliefnotes). Searchable, categorized, open for contributions. https://github.com/FiSimply/clief-notes-index
- S72: Build software better, together https://github.com/topics/icm?o=desc&s=updated
- S74: 🎆 GOOD NEWS: THE SALE STAYS OPEN. HAPPY 4TH 🎆  · Clief Notes https://www.skool.com/cliefnotes/good-news-the-sale-stays-open-happy-4th
- S75: ICM on enterprise level - introducing Taurus · Clief Notes https://www.skool.com/cliefnotes/icm-on-enterprise-level-introducing-taurus
- S76: ICM Workspace Builder https://workflowcreate.netlify.app/
- S79: Terms of Service - Eduba https://chat.eduba.io/terms
- S80: The Lyceum https://lyceum.eduba.io/
- S81: Jake Van Clief - Eduba https://www.linkedin.com/in/jake-van-clief-74b66915a/
- S82: Eduba — chat.eduba.io https://chat.eduba.io/
- S83: The community is staying free BUT.... · Clief Notes https://www.skool.com/cliefnotes/the-community-is-staying-free-but
- S84: Clief Notes Review 2026: Legit Free AI Lessons? https://aifunnelinsider.com/clief-notes-review-2026/
- S85: GitHub - astetic-dev/taurus: Taurus - a Windows desktop launcher that runs multiple Claude Code agents as embedded terminal tabs, each started in the right process folder. Built around the Interpreted Context Methodology (ICM). · GitHub https://github.com/astetic-dev/taurus
- S86: Release Taurus 0.7.7 — Taurus on the Mac · astetic-dev/taurus · GitHub https://github.com/astetic-dev/taurus/releases/tag/v0.7.7
- S87: icm-field-guide/NOTICE.md at main · jonathanmalkin/icm-field-guide · GitHub https://github.com/jonathanmalkin/icm-field-guide/blob/main/NOTICE.md

_112 search results consulted; 19 sources cited. Claims not yet extracted (credit ran out); the next run 02 extracts them._
