<!-- {"wp": "WP-B1", "models": ["claude-fable-5-2"], "fallbacks": 0, "stop_reason": "end_turn", "cost_usd": 1.207, "searches": 12, "fetches": 21} -->
# WP-B1: Baseline, the paper and the repo

### Findings

All pages were accessed 2026-11-11. GitHub's commit history, tags page and issue #17 could not be fetched, so those items are tagged unverified below.

**B1: the paper**

[confirmed B1] The arXiv record for 2603.16021 carries the title "Interpretable Context Methodology: Folder Structure as Agentic Architecture," names Jake Van Clief and David McDermott as authors, and files it under cs.AI and cs.HC. {S1}

[confirmed B1] Two versions exist: the first submission dated 2026-03-17 and v2 dated 2026-03-18, with the unversioned URL resolving to v2. {S1} An independent October 2026 write-up likewise counted only v1 and v2. {S12}

[confirmed B1] Both HTML renderings (v1 and v2) carry a CC BY 4.0 license label, and their in-document title ends in "Agent Architecture" where the arXiv listing says "Agentic Architecture". {S4} Cite the arXiv listing title.

[confirmed B1] A single combined affiliation line (Eduba, University of Edinburgh, Palm Coast, Florida) and an eduba.io contact address accompany the two author names. {S4} The line does not say which author belongs to which institution, so "a University of Edinburgh paper" is an overclaim.

[confirmed B1] ResearchGate tags the item as a preprint dated March 2026. {S16} An independent reviewer (Hosaka blog, October 2026) also treats it as a self-published preprint. {S12}

[unverified B1] "Not peer reviewed" rests on absence: no retrieved page showed a journal reference, DOI or venue, but the fetch tool returned condensed arXiv metadata. Next check: open https://arxiv.org/abs/2603.16021 in a browser and read the "Comments" and "Journal reference" fields, then search the ACM Digital Library and Google Scholar for the exact title.

**B8: the MWP name**

[corrected B8] The brief called "Model Workspace Protocol (MWP)" an unverified alternate name. Version 1 of the paper used Model Workspace Protocol (MWP) as the method's name throughout the abstract and body. {S4}

[confirmed B8] Version 2, posted a day later, swaps that name for Interpretable Context Methodology (ICM) in the same sentences. {S4}

[confirmed B8] The arXiv listing's abstract was not updated and still introduces the method as MWP. {S1}

[confirmed B8] The repo still carries the old name in three places:
- The LICENSE copyright holder reads "Model Workspace Protocol Contributors". {S5}
- The canonical conventions file is headed "MWP Conventions". {S9}
- The README's origin note cites the paper under a Model Workspace Protocol title, credits Van Clief alone, and links to a placeholder path. {S2}

[confirmed B8] An open third-party pull request (#12, August 2026) offers to finish the MWP to ICM rename and counts 16 stale references. {S13}

**B2: the repo**

[confirmed B2] github.com/RinDig/Interpretable-Context-Methodology is live and public, labeled MIT, with 1.4k stars, 243 forks, 42 watchers and 21 commits on main. {S2} Other pages fetched in the same session showed older cached counts (1k to 1.2k stars), so treat 1.4k as approximate.

[confirmed B2] The LICENSE file holds the standard MIT text, including the rights to use, modify, sublicense and sell, conditioned on keeping the copyright and permission notice. {S5}

[confirmed B2] GitHub's releases page for the repo is empty. {S3}

[confirmed B2] Open work items stand at 5 issues and 9 pull requests, with 3 pull requests closed. {S13}

[unverified B2] The latest commit date on main is unknown because GitHub's commit pages refused the fetch. A search snippet of the owner's repository list shows "Updated Oct 6, 2026". {S17} A third-party tracker reports a last push on Oct 6, 2026, creation on Feb 22, 2026, and no commits in the following 30 days. {S18} That date matches the owner opening the still-unmerged PR #16 from a side branch {S14}, so main may be older. Next check: open /commits/main in a browser or run `git log -1 --format=%cd origin/main`.

[unverified B2] The contributor count was not shown (the Contributors panel rendered empty), and the tags page could not be fetched. Next check: open /graphs/contributors and /tags in a browser.

[confirmed B2] PR #16, opened by the repo owner on 2026-10-06, would retitle the README with trademark symbols on the full name and on "ICM", and add a section saying the MIT License covers the files but grants no rights in the names. {S14} Its draft notice names Jake Van Clief as the mark owner. {S14} The PR is still open. {S14}

[inference B2] PR #16 signals intent to claim the names as trademarks. It is not evidence of a registration, and it changes the naming risk that WP-Q17 must assess.

[confirmed B2] The repo links printed in the paper point to earlier names: "Model-Workspace-Protocol-MWP-" in v1 and "Interpretable-Context-Methodology-ICM-" in v2. {S4} A third-party project cites yet another spelling, "Interpreted-Context-Methdology", and remarks that the typo is upstream. {S19} Whether the old URLs redirect was not tested.

[confirmed B2] Credit in the README goes to Jake Van Clief alone as creator {S2}, while the paper lists two authors.

**B3: core design**

[confirmed B3] Handoff works through an `output/` subfolder in every stage, which the following stage reads as its input. {S9} The README's sample tree shows numbered stage folders (`01-research`, `02-script`, `03-production`), each with its own `CONTEXT.md`, `references/` and `output/`. {S2}

[confirmed B3] Per-stage instructions live in that stage's `CONTEXT.md`, structured as a three-part contract of inputs, process and outputs. {S4}

[confirmed B3] Non-AI work (data fetching, file moves, formatting, email sending) falls to local Python scripts in the paper's description. {S4}

[confirmed B3] Review happens at stage boundaries, where a person may inspect and edit the output before the next stage starts. {S4} The conventions file makes in-stage checkpoints optional and lets linear stages run straight through. {S9}

[inference B3] Human review is a convention, not an enforced gate. Nothing in the retrieved files blocks a stage from running on unreviewed output, so Nihilo would have to build approval gates.

[corrected B3] The brief says markdown files direct "one agent". The paper's own implementations had Claude Opus 4.6 as the main agent hand sub-tasks to Claude Sonnet 4.6 through Agent Teams. {S4} "One orchestrating agent, plus sub-agents" is the accurate reading.

[confirmed B3] Folder naming differs between sources. The paper's examples use underscores (`01_research`) {S4}, while the repo conventions prescribe lowercase with hyphens and `01-` style prefixes {S9}.

**B4: five layers**

[confirmed B4] The README's layer table matches the brief's file names: Layer 0 `CLAUDE.md`, Layer 1 `CONTEXT.md`, Layer 2 stage `CONTEXT.md`, Layer 3 reference material, Layer 4 working artifacts. {S2} The repo conventions file and the paper's Figure 1 give the same list.

[confirmed B4] The paper's role descriptions agree with the brief: global identity for Layer 0, workspace task routing for Layer 1, and a stage contract for Layer 2. {S4}

[corrected B4] The brief lists "voice, style, SOPs" for L3. The paper's own Layer 3 examples are design systems, voice rules, build conventions, style guides and domain knowledge packaged as skill files {S4}; SOPs are not named.

[confirmed B4] Layer 0 depends on a Claude Code behavior: `CLAUDE.md` is loaded automatically into every conversation. {S9} Layer 3 can also include bundled Claude Code skills in a `skills/` folder. {S9} Both matter for WP-Q02 (portability).

**B5: evidence base and poor fits**

[corrected B5] The brief says "about 52 invited users". Fifty-two is the membership of the invite-only community the authors drew observations from. {S4} The one quantified result (30 reporting a U-shaped editing pattern) comes from 33 of those members. {S4}

[confirmed B5] Data collection was conversational, with no structured interviews or usage logging, and the authors concede selection and enthusiasm bias. {S4}

[confirmed B5] Testing covered one model family only, Claude Opus 4.6 and Sonnet 4.6. {S4} Claude Code was the runtime for every workspace described. {S4}

[confirmed B5] A controlled comparison against monolithic prompting was never run, so the quality claim leans on prior literature and practitioner judgment. {S4}

[confirmed B5] Content production accounts for most active use, with academic and policy deployments still early. {S4}

[confirmed B5] External adoption is asserted at the University of Edinburgh Neuropolitics Lab, ICR Research and the Academy of International Affairs in Bonn, with details withheld under NDA. {S4} This is author-reported and not independently verified.

[confirmed B5] The paper's list of poor fits matches the brief: real-time multi-agent collaboration, high-concurrency use by many simultaneous users, and complex branching driven by AI decisions mid-pipeline. {S4}

[confirmed B5] The paper's comparison table adds two more weaknesses: error recovery is a manual re-run of the failed stage, and execution is sequential by design. {S4}

**B6: critiques**

[unverified B6] The phrase "a map, not an engine" did not appear in any source retrieved across six targeted searches, so its origin and author are unknown. Next check: ask whoever wrote the brief for the source, and search inside Skool (login required), YouTube comments, Reddit and X.

[unverified B6] No retrieved source states "no memory, no run history, stages overwrite outputs, no versioning" as a critique in those words. The findings below show what primary sources support for each part.

[confirmed B6] On versioning: the paper offers Git commits of stage outputs after each run as the way to get version history. {S4} Versioning is something the user adds, not something the method does.

[inference B6] On overwriting: output files are named by topic slug and artifact type, written into a single `output/` folder per stage {S9}, with no run ID or timestamp. A re-run on the same topic would therefore replace the earlier file unless Git captured it.

[confirmed B6] On memory and run history: GitHub issue #15 (user xnfinite, 2026-09-09) reports that after weeks of daily use, frequently used files outgrow what a session reads, catalog entries go stale, and earlier agent advice "is just gone". {S7} The same user published add-on skills for a ledger, verifier and maintenance checker, and asks whether the conventions should cover post-build maintenance. {S7} This is a community report, not an author statement.

[unverified B6] Issue #17, "Separation of agent definition from working state ?" (user rupertlssmith, 2026-10-22), looks relevant but its body could not be fetched. Next check: open https://github.com/RinDig/Interpretable-Context-Methodology/issues/17 in a browser.

[confirmed B6] The authors concede a related gap. Their own wording is that ICM gives "observability but not traceability", with no direct way to trace an output phrase back to the instruction or file that caused it. {S4} The debugging ideas proposed to close that gap remain unbuilt. {S4}

[confirmed B6] Independent critique 1 (Hosaka blog, 2026-10-23): the reviewers discount the U-shape finding as self-reported, informally collected, from a small selected group on one model family. {S12} They also flag a mismatch between the preprint's anti-framework thesis and Eduba's site copy, which advertises building multi-agent systems. {S12}

[confirmed B6] Independent critique 2 (Dominik J. blog, May 2026): for software projects the paper omits any check that a context rule still matches the code, and setup overhead is described as real. {S15}

[confirmed B6] Repo hygiene signals: open third-party pull requests propose fixing 9 broken path references, correcting documentation that points at things that do not exist, and adding a convention validator with CI. {S13}

### Answer summary

- **B1.** Confirmed with one gap. Title, authors, arXiv ID and dates match the brief, and v2 (2026-03-18) is the latest version. {S1} The license is CC BY 4.0. {S4} Preprint status is confirmed by secondary sources. "Not peer reviewed" is unverified because it rests on absence of evidence.
- **B2.** Confirmed. The repo is live, MIT-labeled, at about 1.4k stars and 243 forks with 21 commits. {S2} It has no releases. {S3} The latest commit date on main and the contributor count are unverified. New and material: the owner has an open PR to mark the names as trademarks and state that MIT grants no rights in them. {S14}
- **B3.** Confirmed with two corrections. Numbered stage folders hand off through `output/`. {S9} Per-stage markdown contracts and local scripts are as described. Corrections: the "one agent" delegates to sub-agents in the paper's own builds {S4}, and `[inference]` human review is a convention, not an enforced gate.
- **B4.** Confirmed. The five layers and file names match the brief. {S2} Minor correction: SOPs are not in the paper's L3 examples. L0 relies on Claude Code auto-loading `CLAUDE.md`. {S9}
- **B5.** Confirmed with one correction. The 52 figure is community size; the single quantified finding rests on 33 members. {S4} Claude-only testing and the lack of any controlled comparison are stated by the authors. {S4} The three poor-fit cases match the brief.
- **B6.** Mostly unverified as worded. The "map, not an engine" phrase was not found anywhere. The substance is partly supported: versioning is delegated to Git {S4}, a user reports lost history across sessions in issue #15 {S7}, and the authors admit a traceability gap {S4}. `[inference]` Same-topic re-runs overwrite outputs.
- **B8.** Corrected. MWP was the method's original name in v1 {S4}, replaced by ICM in v2 {S4}. It persists in the arXiv abstract, the LICENSE copyright line and the conventions file. {S5} {S9} {S1} `[inference]` Nihilo should treat MWP and ICM as the same thing and expect clients to find both names.

### Coverage checklist

1. Exact title, authors, arXiv ID, submission date, latest version and date, license, peer review status: **partly covered.** Everything is sourced except peer review status, which is supported only by absence plus secondary "preprint" labels.
2. Repo URL, license file contents, latest commit or release date, stars and contributors: **partly covered.** URL, LICENSE text, no-releases status, stars, forks, watchers and commit count are sourced. The latest commit date on main and the contributor count are not, because the pages were blocked or rendered empty.
3. Numbered stage folders with `output/` handoff, per-stage markdown roles, local scripts, human review: **covered**, with corrections on sub-agents and on review being unenforced.
4. Five layers L0 to L4 with the same file names: **covered.**
5. Evidence base and stated poor-fit cases: **covered.**
6. Where the "map, not an engine" and related critiques appear, and who made them: **partly covered.** The exact phrase and its author were not found. Substantive equivalents are sourced to issue #15, the paper's own limitations and two independent blogs.
7. Any primary mention of "Model Workspace Protocol" or "MWP": **covered.** It appears in arXiv v1, the arXiv abstract, LICENSE, CONVENTIONS.md and the README.

### Open questions

1. **Peer review status.** Next check: read the "Comments" and "Journal reference" fields on the arXiv abstract page in a browser, then search the ACM Digital Library and Google Scholar for the title.
2. **Latest commit date on main, tags and contributor count.** Next check: open /commits/main, /tags and /graphs/contributors in a browser, or clone and run `git log -1` and `git shortlog -sn`.
3. **Source of "a map, not an engine".** Next check: ask the brief's author where it came from, then search Skool (Clief Notes), Reddit, X and YouTube with a logged-in session.
4. **Issue #17 body.** Next check: open the issue in a browser and record whether it documents the overwrite or state-mixing problem.
5. **Overwrite behavior in practice.** Next check: clone the repo, run the `script-to-animation` workspace twice on the same topic, and diff `output/` to confirm whether the first run's files are replaced.
6. **Trademark status (for WP-Q17).** PR #16 shows intent only. Next check: search USPTO for "Interpretable Context Methodology" and "ICM" with Jake Van Clief or Eduba as owner, and recheck whether PR #16 has merged.
7. **Old repo URLs.** Next check: request the three earlier repo names and record whether GitHub redirects them.
8. **Lead for the B7 owner.** A community wiki claims Eduba runs a twelve-week certification program through a "Lyceum" platform {S20}, which conflicts with the brief's "no certification program found". This is a low-quality source. Next check: look for the program on eduba.io.
9. **Lead for WP-Q01.** A second repo under the same account, RinDig/icm-architect, ships an agent skill that claims to work in non-Claude agents. {S21} Next check: fetch that repo and confirm license, date and portability claims.

## Sources attached by the API

- S1: Interpretable Context Methodology: Folder Structure as Agentic Architecture https://arxiv.org/abs/2603.16021
- S2: GitHub - RinDig/Interpretable-Context-Methodology: Folder structure as agent architecture.  ICM replaces framework-level orchestration with filesystem structure. https://github.com/RinDig/Interpretable-Context-Methodology
- S3: Releases · RinDig/Interpretable-Context-Methodology https://github.com/RinDig/Interpretable-Context-Methodology/releases
- S4: Interpretable Context Methodology: Folder Structure as Agent Architecture https://arxiv.org/html/2603.16021v2
- S5: Interpretable-Context-Methodology/LICENSE at main · RinDig/Interpretable-Context-Methodology https://github.com/RinDig/Interpretable-Context-Methodology/blob/main/LICENSE
- S7: Pattern proposal: an operating layer for a workspace after it exists (ledger, verifier, maintenance) · Issue #15 · RinDig/Interpretable-Context-Methodology https://github.com/RinDig/Interpretable-Context-Methodology/issues/15
- S9: Interpretable-Context-Methodology/_core/CONVENTIONS.md at main · RinDig/Interpretable-Context-Methodology https://github.com/RinDig/Interpretable-Context-Methodology/blob/main/_core/CONVENTIONS.md
- S12: Files on Disk as State: Reading the Interpretable Context Methodology https://blog.hosaka.fm/files-on-disk-as-state-what-we-take-from-the-interpretable-context-methodology/
- S13: Pull requests · RinDig/Interpretable-Context-Methodology https://github.com/RinDig/Interpretable-Context-Methodology/pulls
- S14: Add trademark marks and name notice to README by RinDig · Pull Request #16 · RinDig/Interpretable-Context-Methodology https://github.com/RinDig/Interpretable-Context-Methodology/pull/16
- S15: Your Folder Tree Is Already a Context Engine — dominikj111 https://dominikj111.github.io/blog/model-workspace-protocol-context-cascade/
- S16: Jake Van Clief's research works https://www.researchgate.net/scientific-contributions/Jake-Van-Clief-2327822377
- S17: RinDig (JV) / Repositories · GitHub https://github.com/RinDig?tab=repositories
- S18: RinDig/Interpretable-Context-Methodology https://hotskills.dev/skill/rindig-interpretable-context-methodology/
- S19: GitHub - TerraByte-Dev/ICM-Doc: A clinic for the folders your AI agent lives in. Diagnose, repair, or build an ICM (Interpretable Context Methodology) structure — markdown only, no dependencies. · GitHub https://github.com/TerraByte-Dev/ICM-Doc
- S20: Interpretable Context Methodology - Learn AI - Miraheze https://ai.miraheze.org/wiki/Interpretable_Context_Methodology
- S21: GitHub - RinDig/icm-architect: Agent skill: design any process, idea, or problem into an ICM workspace (folder structure as agent architecture), or restructure an existing folder into one · GitHub https://github.com/RinDig/icm-architect

_115 search results consulted; 17 sources cited._
