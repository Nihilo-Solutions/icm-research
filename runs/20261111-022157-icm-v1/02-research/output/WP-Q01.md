<!-- {"wp": "WP-Q01", "models": ["claude-fable-5-2"], "rendered_from_raw": true, "claims_extracted": false} -->
# WP-Q01: Q1, validity and current progress of ICM

### Findings

All sources were accessed 2026-11-11. "Indirect" means the study is independent of the ICM authors but does not test ICM itself.

[confirmed Q1] The arXiv record for 2603.16021 holds two versions, v1 dated 17 March 2026 and v2 dated 18 March 2026, both 34 KB. {S10} {S1}

[unverified Q1] I found no v3 or later revision, but my only view of the full submission history is a search-engine copy about 238 days old. Next check: open arxiv.org/abs/2603.16021 live and read "Submission history". For current version facts, see WP-B1.

[confirmed Q1] The v1 to v2 revision includes a rename: the body of v1 introduces the method as Model Workspace Protocol (MWP) {S11}, while the body of v2 introduces it as Interpretable Context Methodology (ICM) {S4}. The abstract field on the v2 arXiv page still carries the MWP wording. {S10} This is the origin of B8's alternate name (see WP-B1).

[inference Q1] Both versions are the same size and I did not diff the full texts, so v2 looks like a rename, not new content. Next check: diff arxiv.org/html/2603.16021v1 against v2.

[unverified Q1] Peer-review status is unknown. A community wiki names ACM Transactions on Interactive Intelligent Systems as the journal the paper was submitted to {S20}, but I found no ACM or author page confirming it. Next check: search dl.acm.org for the title, or ask the authors.

[unverified Q1] I found no follow-up paper from either author. The lead author's 28 August 2026 essay still points only to the March preprint. {S104} Next check: arXiv author search for "Van Clief" and the Google Scholar profile linked from alphaXiv.

[unverified Q1] I found no paper citing 2603.16021, and I could not load the Semantic Scholar or Google Scholar citation lists. Next check: open api.semanticscholar.org/arXiv:2603.16021 and the Google Scholar "cited by" link.

[confirmed Q1] The reference repo's landing page counts 21 commits on main, 5 open issues, 9 open pull requests, 1.4k stars, and 243 forks. {S2}

[unverified Q1] Commit-level history and release tags could not be read. GitHub's commits and tags pages refused my fetches, and the landing page lists no release. Next check: clone the repo and run `git log --since=2026-03-01 --stat` and `git tag`.

[confirmed Q1] The pull-request queue is the best available view of change themes. Nine PRs are open and three are closed; the open ones include August 2026 community fixes for 16 stale MWP references, 9 broken `_core` paths, an unregistered `voice-driven-animation` workspace, and a proposed convention validator with CI. {S13} A README paper-reference fix from 22 April 2026 is also still open. {S13}

[confirmed Q1] The rename is incomplete in the published material. The README's "academic treatment" line still uses the Model Workspace Protocol title. {S2} The paper's footnote gives a repo URL ending in "-ICM-" {S4}, which differs from the live repo path.

[inference Q1] Documentation fixes left unmerged for three to seven months suggest the reference repo is lightly maintained. Nihilo should pin a commit and treat the repo as a pattern description, not a supported product.

[confirmed Q1] A trademark claim is pending in the repo. PR #16, opened by the owner on 6 October 2026 {S13} and still open, would put trademark symbols on the full name and on "ICM" in the README title, and would add a "Name and Trademark" notice separating the MIT grant on files from any rights in the names. {S14}

[inference Q1] PR #16 is a draft claim, not evidence of a registration. Pass it to WP-Q17, which should check USPTO for filings by Jake Van Clief, the owner the notice names {S14}.

[confirmed Q1] New official tooling exists: the same GitHub account publishes `icm-architect`, an MIT-licensed agent skill (13 commits, 2.0k stars) that scaffolds a new ICM workspace or restructures an existing folder into one. {S21}

[confirmed Q1] `icm-architect` moves away from the paper's Claude-only setup. Workspaces it builds use `AGENTS.md` as the entry file {S21}, where the paper's Layer 0 is `CLAUDE.md` {S4}. Its README lists Codex, Gemini CLI, Cursor, GitHub Copilot, and Claude Code as supported through the Agent Skills format. {S21}

[confirmed Q1] `icm-architect` also changes the vocabulary and the review rule. It describes three primitives (sequence, shelf, catalog) and five forms (Pipeline, Record library, Knowledge bundle, Context map, System map). {S21} A stage check may now be a person, a script, or a small model {S21}, where the paper puts a human at each stage boundary {S4}.

[unverified Q1] The first release date of `icm-architect` is not shown on the page. It existed by 28 August 2026, when the author's essay linked it. {S104} Next check: read the first commit date in a clone.

[confirmed Q1] The author says a hosted deployment product is being built (author source). His August essay claims his team built a first iteration of a platform and a connector for its deployment layer. {S104} A Skool comment by him invites alpha testers for software to deploy ICM at scale. {S108}

[unverified Q1] The platform's name, availability, price, and security posture are unknown. Next check: watch the video embedded in the essay and ask Eduba directly.

[unverified Q1] A certification may now exist. A search snippet of lyceum.eduba.io advertises "The First Eduba ICM Certification" tied to a paid cohort course {S80}, but the page blocked my fetch. If real, this corrects B7's "no certification program found". Next check: open lyceum.eduba.io in a browser (see WP-B7).

[unverified Q1] Community size has grown well past the paper's 52 invited users. The author self-reports almost 47k members {S104}, but I did not load the Skool page. See WP-B7.

[unverified Q1] One community post reports a scaling limit: agents start skipping information as folders multiply {S109} (community report, snippet only). Next check: open the Skool "Taurus" post (see WP-B7 and Q7).

[confirmed Q1] The authors have published no enterprise ICM case study. Eduba's case-study page lists seven engagements dated 2022 to 2025, mostly AI training and research {S105}, and none of them mentions ICM.

[inference Q1] The "outside adopters" in the paper are not arms-length. The paper names Edinburgh, ICR Research, and the Academy of International Affairs in Bonn as external users. {S4} Eduba's own client list includes ICR Research and an Academy of International Affairs {S105}, and Edinburgh is the authors' stated affiliation {S4}.

[unverified Q1] Reported commercial wins are anecdotes without names or evidence. The author's essay mentions a community member's thirty thousand dollar engagement and firms paying Eduba to teach staff to build. {S104} Next check: ask Eduba for referenceable ICM clients.

[unverified Q1] I found no conference talk on ICM by the authors. The only event trace is an AI Tinkerers listing for an ICM demo in Columbus on 4 May 2026 {S110} (snippet only, presenter unknown). Eduba cites a UKICER 2025 presentation on AI workflows {S105}, which predates the paper. Next check: open the AI Tinkerers page and the author's YouTube channel.

[confirmed Q1] The paper claims no measured advantage. Its v2 text concedes that staged loading was never benchmarked against a monolithic prompt on the same tasks, and that only Claude Opus 4.6 and Sonnet 4.6 were tested. {S4}

[unverified Q1] I found no independent evaluation of ICM itself. Searches for benchmarks, comparisons, critiques, and citing papers returned only author material, a wiki, derivative GitHub projects, and community blogs such as one written by a paying member of the author's group {S111}. Next check: repeat the Semantic Scholar, OpenReview, and ACL Anthology searches quarterly.

[estimate Q1] The only cost numbers are the authors' own. Figure 3 gives representative counts of about 5.6k, 5.5k, and 4.9k tokens for three stages, against about 42k for a monolithic prompt, from one workspace. {S4} Summing the stages gives about 16k input tokens, roughly 62% fewer than one 42k call (16.0 / 42 = 0.38). This excludes output and tool-loop tokens and is not a measured run.

[confirmed Q1] Indirect, staging versus one prompt: the closest controlled test favors staging. Sun et al. (arXiv 2406.00507) ran summary drafting, critique, and refinement as three separate prompts and as one combined prompt, and the three-prompt chain won. {S112} The scope is summarization only.

[confirmed Q1] Indirect, staged work with human inspection: the main evidence is the AI Chains study (CHI 2022). Twenty participants got better task outcomes with chained LLM steps and rated that setup more transparent and controllable. {S113} Higher-quality outcomes occurred about 82% of the time. {S114} The sample is small and the models are from 2022.

[confirmed Q1] Indirect, scoped context: the core premise has outside support. Chroma's technical report covers 18 LLMs and records falling performance as inputs lengthen in every experiment. {S115} This is a vendor report.

[confirmed Q1] Indirect, vendor guidance: Anthropic's engineering advice points the same way, though it is guidance, not measurement. It recommends the smallest high-signal token set. {S102} It describes Claude Code as loading `CLAUDE.md` up front and pulling other files on demand. {S102}

[confirmed Q1] Indirect, counter-signal: two sources warn the benefit may shrink. Anthropic expects less prescriptive engineering to be needed as models improve. {S102} The ICM paper admits its scoping argument weakens if models attend reliably to 200,000 tokens. {S4}

[confirmed Q1] Indirect, always-loaded context files: the closest test of an L0-style file is discouraging. Gloaguen et al. (arXiv 2602.11988v3) report flat task success and inference cost more than 20% higher on average when coding agents get repository context files, across LLMs, agents, and both generated and developer-written files. {S103}

[confirmed Q1] The same study separates two kinds of content. Agents obey explicit instructions in these files, but overview-style descriptions of the repository add nothing. {S103}

[inference Q1] Mapped to ICM, L0 and L1 are mostly overview and routing, while L2 stage contracts are explicit instructions. The evidence favors keeping L0 and L1 minimal and investing effort in L2.

[confirmed Q1] Indirect, always-on versus selective loading: only one small ablation compares these directly. Khatri (arXiv 2607.27250, 28 July 2026) ran 288 evaluated runs on 17 tasks with Claude Code and Codex, and context strategy made no measurable difference to correctness within a 10 to 15 point bound. {S106}

[confirmed Q1] Indirect, efficiency: one study cuts the other way on cost. Lulla et al. (arXiv 2601.20404v2) ran agents on 124 pull requests in 10 repositories and associate an AGENTS.md file with 28.64% lower median runtime and 16.58% fewer output tokens, with comparable completion. {S107}

[confirmed Q1] Indirect, human-written reference files: the best support for L3-style material is SkillsBench (arXiv 2602.12670v4). Over 87 tasks and 18 model and harness pairings, curated Skills moved the pass rate from 33.9% to 50.5%, with per-configuration gains of 4.1 to 25.7 points. {S116}

[confirmed Q1] Indirect, model-written context: a warning for agent-generated workspaces sits in the same benchmark. Skills the model wrote for itself scored 8.1 to 11.5 points below having no Skills, in all three configurations tested. {S116}

[inference Q1] The workspace-builder and `icm-architect` both have a model write the context files. Nihilo should have a domain expert write or heavily edit L2 and L3, and should evaluate each generated workspace before client use.

[confirmed Q1] Indirect, one agent versus many: ICM's single-agent premise has support on reasoning tasks. Tran and Kiela (arXiv 2604.02460) find single agents match or beat multi-agent systems on multi-hop reasoning once reasoning tokens are equalized. {S117} I read a mirror's summary, not the arXiv page.

[confirmed Q1] Indirect, counter-example: the opposite result exists for breadth-first research. Anthropic's internal evaluation had an Opus 4 lead with Sonnet 4 subagents beat a lone Opus 4 by 90.2%, at about 15 times the tokens of a chat. {S118} This is a vendor self-report, read via a secondary blog quoting it.

[confirmed Q1] Indirect, vendor guidance on chaining: Anthropic's "Building effective agents" backs the staged pattern for tasks that split into fixed subtasks. It frames prompt chaining as accepting latency in exchange for accuracy. {S119} It also warns that frameworks can hide prompts and responses and complicate debugging. {S119}

[unverified Q1] I found no study comparing ICM-style staged folders with RAG or with a named agent framework on quality, cost, or reliability. Next check: run Nihilo's own A/B test (same task and model, single prompt versus ICM stages versus RAG), logging tokens, human edits, and rubric scores.

[inference Q1] ICM's component ideas each have independent support in adjacent settings: staging, scoped context, human-curated reference files, and human review points. ICM as a package has none, and the supporting studies are mostly coding-agent and summarization work, not knowledge-work reporting.

### Answer summary

**What is the latest version of the paper and repo?** See WP-B1. I found no version after v2 of 18 March 2026, but the absence of a v3 rests on a stale listing.

**What has changed since March 2026?**
- **Paper:** the only confirmed change is the v1 to v2 rename from MWP to ICM. No follow-up paper, peer-review outcome, or citing paper was found (all unverified).
- **Repo:** it shows 21 commits and no visible release. Nine PRs are open, mostly community fixes for stale MWP references and broken paths. Commit-level history could not be read.
- **Naming:** an owner PR from 6 October 2026 would add trademark marks and a naming notice. It is not merged.
- **Official tooling:** `icm-architect` is new. It is vendor-neutral, uses `AGENTS.md`, and allows non-human stage checks. The author also says a deployment platform is in development (details unverified).
- **Certification:** an Eduba ICM certification may exist (unverified, snippet only).
- **Enterprise case studies:** none published. Eduba's listed engagements predate the paper and do not mention ICM.
- **Talks:** no author conference talk on ICM was found. There is one community meetup listing (unverified).

**Is there independent evidence that ICM improves quality, cost, or reliability?** No direct evidence was found, and the paper itself reports no controlled comparison. The indirect evidence is mixed:
- **Supports the pattern:** prompt chaining beat a single combined prompt in one summarization study. A 20-person study found chained steps improved outcomes and control. Curated skill files raised pass rates by 16.6 points on average.
- **Cautions:** always-loaded context files did not improve coding-agent success and raised cost by over 20% in one study. Model-written skills scored below baseline.
- **Not tested:** nothing compares ICM-style staging with RAG or agent frameworks.

[inference] Nihilo can sell ICM as a transparent, reviewable way to organize work. It should not claim measured quality or cost gains until it has its own A/B data.

### Coverage checklist

- **Every change to the paper and repo since March 2026:** partly covered. The paper rename, repo counts, PR themes, and trademark PR are sourced. The commit log, tags, and a live check for a v3 were blocked or stale.
- **Follow-up papers, official tooling, enterprise case studies, talks, with dates:** partly covered. Tooling (`icm-architect`) and the lack of Eduba ICM case studies are sourced. Follow-up papers, the certification, the platform details, and talks are unverified with next checks.
- **Independent evidence comparing ICM-style staged context with single prompts, RAG, or agent frameworks:** covered as a negative. None was found, the paper concedes none exists, and the claim of absence is tagged unverified.
- **Closest indirect evidence, clearly labeled:** covered. Eleven sources are labeled indirect, including counter-evidence. Nothing addresses RAG directly.

### Open questions

- **Is there an arXiv v3 or a journal version?** Open arxiv.org/abs/2603.16021 live and search dl.acm.org for the title.
- **What do the 21 commits contain, and are there tags?** Clone the repo and run `git log --stat` and `git tag`.
- **Does any paper cite 2603.16021?** Check the Semantic Scholar and Google Scholar citing lists.
- **Is the Eduba ICM certification real, and on what terms?** Open lyceum.eduba.io in a browser and hand the result to WP-B7.
- **What is the author's deployment platform?** Watch the video in the 28 August 2026 Substack essay and ask Eduba for its name, hosting model, and price.
- **Has a trademark application been filed for "Interpretable Context Methodology" or "ICM"?** WP-Q17 should search USPTO by owner name, prompted by PR #16.
- **When was `icm-architect` first released, and how does it relate to B7's `icm-template` and workspace generator?** Read its first commit date and hand the result to WP-B7.
- **Are there referenceable enterprise ICM deployments?** Ask Eduba for named clients with measured outcomes.
- **Does ICM beat a single prompt or RAG on Nihilo's target workflow (monthly client reporting)?** Run an internal A/B test with fixed model, task, and rubric.
- **Do agents skip files as workspaces grow?** Open the Skool "Taurus" post and test with a workspace of 50 or more folders (links to Q7).

## Sources attached by the API

- S1: Interpretable Context Methodology: Folder Structure as Agentic Architecture https://arxiv.org/abs/2603.16021
- S2: GitHub - RinDig/Interpretable-Context-Methodology: Folder structure as agent architecture.  ICM replaces framework-level orchestration with filesystem structure. https://github.com/RinDig/Interpretable-Context-Methodology
- S4: Interpretable Context Methodology: Folder Structure as Agent Architecture https://arxiv.org/html/2603.16021v2
- S10: Interpretable Context Methodology: Folder Structure as Agentic Architecture https://arxiv.org/abs/2603.16021v2
- S11: Interpretable Context Methodology: Folder Structure as Agent Architecture https://arxiv.org/html/2603.16021v1
- S13: Pull requests · RinDig/Interpretable-Context-Methodology https://github.com/RinDig/Interpretable-Context-Methodology/pulls
- S14: Add trademark marks and name notice to README by RinDig · Pull Request #16 · RinDig/Interpretable-Context-Methodology https://github.com/RinDig/Interpretable-Context-Methodology/pull/16
- S20: Interpretable Context Methodology - Learn AI - Miraheze https://ai.miraheze.org/wiki/Interpretable_Context_Methodology
- S21: GitHub - RinDig/icm-architect: Agent skill: design any process, idea, or problem into an ICM workspace (folder structure as agent architecture), or restructure an existing folder into one · GitHub https://github.com/RinDig/icm-architect
- S80: The Lyceum https://lyceum.eduba.io/
- S102: Effective context engineering for AI agents https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- S103: Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents? https://arxiv.org/abs/2602.11988
- S104: Augmenting Human Intellect https://jakevanclief.substack.com/p/augmenting-human-intellect
- S105: All Case Studies | EDUBA https://eduba.io/works
- S106: Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories https://arxiv.org/abs/2607.27250
- S107: On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents https://arxiv.org/abs/2601.20404
- S108: Jake Van Clief https://www.skool.com/@jake-van-clief-2217?g=cliefnotes
- S109: Clief Notes · 🛠️ Show Your Work https://www.skool.com/cliefnotes?c=bfec5b7bad724c8fa4e5164cb7a34141
- S110: Interpretable Context Methodology (ICM) Projects https://atlanta.aitinkerers.org/technologies/interpretable-context-methodology-icm
- S111: Jake Van Clief's ICM Folder System, From A Guy Who Runs It https://filesnfolders.com/blog/jake-van-clief-icm-folder-system
- S112: Prompt Chaining or Stepwise Prompt? Refinement in Text Summarization https://arxiv.org/pdf/2406.00507
- S113: AI Chains: Transparent and Controllable Human-AI Interaction https://arxiv.org/pdf/2110.01691
- S114: AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts https://dl.acm.org/doi/fullHtml/10.1145/3491102.3517582
- S115: Context Rot: How Increasing Input Tokens Impacts LLM Performance https://www.trychroma.com/research/context-rot
- S116: SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks https://arxiv.org/html/2602.12670v4
- S117: Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets https://www.scholarfeed.org/paper/2604.02460
- S118: Anthropic: How we built our multi-agent research system https://simonwillison.net/2025/Jun/14/multi-agent-research-system/
- S119: Building effective AI agents \ Anthropic https://www.anthropic.com/research/building-effective-agents

_184 search results consulted; 28 sources cited. Claims not yet extracted (credit ran out); the next run 02 extracts them._
