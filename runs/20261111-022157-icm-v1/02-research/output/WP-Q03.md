<!-- {"wp": "WP-Q03", "models": ["claude-fable-5-2"], "fallbacks": 0, "stop_reason": "end_turn", "cost_usd": 1.662, "searches": 18, "fetches": 20} -->
# WP-Q03: Q3, gaps between ICM and enterprise needs

### Findings

Access date for every source below: 2026-11-11. I ran out of fetch budget, so several vendor pages were seen only as search excerpts. Those claims are tagged `unverified` with the URL to open.

**Baseline: what ICM as published leaves open**

[confirmed Q3] The authors' own comparison table concedes three operational gaps: a failed stage is re-run by hand, a person makes every branching decision, and stages execute one after another. {S4} Source: arXiv v2 HTML, dated 18 Mar 2026.

[confirmed Q3] Multi-user load falls outside the method's design: the paper labels ICM local-first and names queueing, state isolation, and deployment infrastructure as things an adopter would have to add.

[confirmed Q3] Version history is something the operator creates: the paper and the README both point to committing stage outputs to Git after each run. {S4} {S2}

[confirmed Q3] Tracing a bad output back to the instruction or file that caused it is manual today, a state the authors call "observability but not traceability". Their proposed fixes (provenance markers, a Verify section, markdown breakpoints) are not built. {S4}

[confirmed Q3] Quality control in the reference repo consists of checkpoints for human steering plus audit checklists that the agent itself runs before writing output. No controlled comparison against a monolithic prompt exists. {S4}

[confirmed Q3] Cross-run memory is rejected on purpose by one repo convention ("Docs over outputs"), which keeps agents from learning patterns out of earlier outputs. So "no memory" is partly a design choice, not only an omission.

[inference Q3] I found no guidance on access control, secrets, scheduling, or automated regression tests in the full v2 text or the README. I did not open `_core/CONVENTIONS.md`.

**Platform maturity that applies to several gaps**

[confirmed Q3] Claude Managed Agents carries a beta label, and every endpoint needs the `managed-agents-2026-04-01` header. Anthropic excludes it from Zero Data Retention and from HIPAA BAA coverage because sessions are stateful. {S124}

[unverified Q3] The fetched overview names Claude API, Claude Platform on AWS, and Claude Models on Google Cloud (Anthropic managed) {S124} as platforms. Microsoft Foundry is not on that list, so I could not confirm Managed Agents for an Azure-first build. Next check: open the Microsoft Foundry Claude documentation and the Managed Agents reference page for platform support.

[confirmed Q3] Version numbers in the Claude Agent SDK docs sit below 1.0 (TypeScript 0.3.x, Python 0.2.x), and an experimental session API was withdrawn in TypeScript 0.3.142.

[unverified Q3] The Agent SDK pages I fetched do not state a GA or beta label. Next check: open the Agent SDK overview and changelog on code.claude.com.

[confirmed Q3] Microsoft's Learn page (last updated 2026-10-15) positions Durable Task Scheduler as the recommended backend for Durable Functions and the Durable Task SDKs. {S128} Those SDKs run on Azure Container Apps, AKS, App Service, and VMs. {S128}

[unverified Q3] Vendor blog excerpts report GA of the Dedicated SKU {S132} and later GA of the Consumption SKU {S133}; trade press dates the first to November 2025 and a secondary blog dates the second to 2026-03-31. I did not fetch the blogs. Next check: open the two techcommunity.microsoft.com announcements.

**Run history** (logging detail: see WP-Q12)

[confirmed Q3] A Managed Agents session keeps its complete event log on Anthropic's servers, retrievable through the API. {S124}

[confirmed Q3] Scheduled runs each leave a deployment run record, holding the session ID on success or an error on failure. {S123}

[confirmed Q3] The Claude Agent SDK writes each session (prompt, tool calls, tool results, responses) to disk without extra code. {S122} Those files stay on the machine that made them unless a session store adapter mirrors them to your own backend.

[confirmed Q3] Durable Task Scheduler ships a dashboard per scheduler that lists orchestration instances with status, duration, input, and output, and lets an operator pause, terminate, or restart one. Dashboard access runs through identity and role-based access control. {S128}

**Versioning**

[confirmed Q3] Managed Agents can mount a GitHub repository into the session sandbox, pinned to a named branch or a commit SHA. {S130} Through the GitHub MCP server the agent can then branch, commit, and push. {S130} Status: beta {S130}.

[inference Q3] An ICM workspace kept in Git can therefore run "at commit X" and return its outputs as a branch or pull request. That gives per-run versioning without changing the folder model.

[unverified Q3] A Learn excerpt says Azure Blob versioning creates a new version on every write or delete {S134} and is unsupported on hierarchical namespace accounts {S134}. Next check: open learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview.

**Memory**

[confirmed Q3] Memory stores in Managed Agents are beta, behind their own header (`agent-memory-2026-07-22`). {S120} A store holds text documents and appears to the agent as a directory in the sandbox. {S120}

[confirmed Q3] Limits: 100 kB per memory and 10,000 memories per store {S120}, and eight stores per session {S120}.

[confirmed Q3] Each change to a memory produces an immutable version usable for audit and restore. History is kept for 30 days by default, so longer retention means exporting it. {S120}

[confirmed Q3] Anthropic warns that a prompt injection can plant content in a writable store that later sessions trust, and recommends read-only attachment for reference material. {S120}

[confirmed Q3] Sessions on self-hosted environments cannot attach memory stores when reached through Claude Platform on AWS or Claude Models on Google Cloud. {S120}

[inference Q3] The mapping to ICM is direct: L3 reference as a read-only store, per-team notes as a read-write store. The safer default for regulated clients is still ICM's own approach: humans edit L3 files in Git.

**Concurrency** (limits: see the scalability package)

[confirmed Q3] Forking an Agent SDK session copies the conversation only; file edits from a fork land in the shared directory where other sessions see them. Each run therefore needs its own working copy.

[unverified Q3] Claude Code docs excerpts describe separate git worktrees for parallel sessions {S135}, each on its own branch {S136}. Next check: open code.claude.com/docs/en/worktrees.

[confirmed Q3] Durable Task Scheduler pushes work items to connected apps, which may handle several at once. Task hubs give each team or environment a separately managed workload. Hubs on one scheduler still compete for the same resources.

[confirmed Q3] Orchestrator and activity payloads are capped at 1 MB. {S128} [inference] Stages should pass file paths or commit references through the orchestrator, not file contents.

[unverified Q3] Temporal is the cloud-neutral alternative: its GitHub excerpt shows an MIT license {S137}, and its integrations page excerpt lists LangGraph, Mastra, OpenAI Agents SDK, and Pydantic AI {S138}. I saw no Claude Agent SDK integration in that excerpt. Next check: open docs.temporal.io/integrations and github.com/temporalio/temporal.

**Multi-user editing** (ownership patterns: see WP-Q10)

[unverified Q3] GitHub docs excerpts say code owners get a review request automatically when a pull request touches their files {S139} and a protected branch can block merging until a code owner approves {S140}. Next check: open the "About code owners" and "About protected branches" pages on docs.github.com.

[confirmed Q3] Memory store updates accept a content-hash precondition, so a concurrent write is rejected instead of silently overwritten.

[inference Q3] Git review covers technical editors only. How a non-technical owner proposes a change to an L3 file without Git is not solved by any product I found here; see WP-Q10 and the surfaces package.

**Access control per layer and stage** (see WP-Q10)

[confirmed Q3] Agent SDK permission rules for Read and Edit accept path patterns, and one Edit rule covers every built-in tool that writes files. A matching deny rule holds even in `bypassPermissions` mode. {S129}

[confirmed Q3] For headless runs the docs pair an explicit tool allowlist with `dontAsk` mode, which turns every would-be prompt into a denial. {S129} Checks that must fire on every call belong in a `PreToolUse` hook. {S129}

[confirmed Q3] These rules have holes: a Bash deny pattern for `rm *` does not catch `/bin/rm`, and read-only Bash commands and file reads inside the working directory run without approval {S129}.

[inference Q3] Path rules are guardrails, not isolation. Hard per-layer control means mounting only the stage's folders into the sandbox and enforcing storage RBAC underneath.

[confirmed Q3] Managed Agents offers three tool policies (`always_allow`, `always_ask`, `auto`), settable per toolset. {S126} Individual tools can override the toolset default. {S126} MCP tools start at `always_ask`. {S126}

[confirmed Q3] The permission outcome of every tool call is written onto its event, which gives an audit field for free. {S126} Anthropic states that `auto` is no substitute for human review, since approved calls execute unseen and may be irreversible. {S126}

**Secrets handling**

[confirmed Q3] Vaults in Managed Agents hide an environment-variable secret from the model: the sandbox holds a placeholder and the real value is swapped in when a request leaves. {S125} Substitution can be limited to named hosts. {S125} Status: beta {S125}.

[confirmed Q3] Limits and caveats: 20 credentials per vault {S125}; no environment-variable credentials on self-hosted sandboxes yet {S125}; clients that sign requests with the secret (AWS SigV4, for example) break {S125}.

[confirmed Q3] Anthropic's own skill documentation forbids putting keys or tokens in memory stores, because they would be replayed into later sessions. Source: anthropics/skills on GitHub, search excerpt. The same logic applies to ICM context files [inference].

[unverified Q3] For the Azure-hosted path, Learn excerpts describe Container Apps secrets defined as Key Vault references, fetched through a managed identity {S141}, and advise Key Vault over app-stored secrets in production {S142}. I did not retrieve Key Vault's GA date. Next check: open learn.microsoft.com/en-us/azure/container-apps/manage-secrets.

**Scheduling**

[confirmed Q3] Scheduled deployments in Managed Agents take a cron expression and a timezone, down to one-minute granularity. {S123} Status: beta {S123}.

[confirmed Q3] Operational limits: 1,000 scheduled deployments per organization {S123}; start-time jitter of up to 15 percent of the interval, capped at 9 minutes {S123}; no backfill of missed triggers after a pause {S123}; no retry of a rate-limited trigger until the next slot {S123}.

[unverified Q3] Launch date: trade press reports June 9, 2026 {S143}. Next check: open platform.claude.com/docs/en/release-notes/overview.

[unverified Q3] On Azure, Learn excerpts describe Container Apps jobs with a Schedule trigger driven by cron expressions evaluated in UTC {S144} and an execution history tab per job {S145}. Next check: open learn.microsoft.com/en-us/azure/container-apps/jobs.

**Error handling**

[confirmed Q3] Durable execution on Azure means the platform retries and persists state so code survives failures and interruptions. {S128}

[confirmed Q3] An Agent SDK run that stops on a turn or budget limit can be resumed by session ID with a higher limit. Connection or process failures return no result message at all, so the caller must detect them. {S122}

[confirmed Q3] Managed Agents pauses a deployment automatically after an unrecoverable session-creation error and records the failed run. {S123} Run outcomes also arrive as webhook events. {S123}

[inference Q3] The clean pattern is one durable activity per ICM stage, with the human review gate modeled as a wait for an external event. That replaces "manual re-run" with retry, resume, and an explicit paused state.

**Testing and evals**

[unverified Q3] promptfoo's GitHub README excerpt says the project is part of OpenAI and still MIT licensed {S146}; the company blog excerpt confirms the acquisition agreement and a pledge to stay open source {S147}. A third-party tracker shows about 25,000 GitHub stars in September 2026 {S148}. Next check: open github.com/promptfoo/promptfoo for license, stars, and latest release.

[unverified Q3] promptfoo's docs excerpt lists a Claude Agent SDK provider that can run against a directory prepared with files before the tests start {S149}. That is the closest fit I found for regression-testing an ICM stage folder. Next check: open promptfoo.dev/docs/providers/claude-agent-sdk and run it against one sample stage.

[confirmed Q3] Microsoft announced general availability of evaluations, monitoring, and tracing in Microsoft Foundry (post modified 2026-03-17). {S127} Only the title and date rendered on fetch; the body text is from the search excerpt.

[unverified Q3] Learn excerpts show built-in agent evaluators such as Task Adherence, Tool Selection, and Tool Input Accuracy {S150}, with Task Completion and Intent Resolution still marked preview {S151}. The blog's quick start assumes a Foundry project with an agent and an Azure OpenAI deployment {S127}, so I could not confirm scoring of a Claude Agent SDK run hosted outside Foundry. Next check: open learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators and test with an exported trace.

[confirmed Q3] Outcomes in Managed Agents attach a markdown rubric to a session and grade the artifact in a separate context window. Iterations default to 3 and max out at 20. {S131} Status: beta {S131}.

[inference Q3] Outcomes is a runtime acceptance gate, close to the Verify section the paper proposes. It is not a regression suite, so it complements promptfoo-style tests rather than replacing them.

[unverified Q3] The Claude Console Evaluation tool tests prompts across scenarios {S152} and supports CSV import and generated test cases {S153}, per docs and blog excerpts. It appears to work on single prompts, not multi-stage folder runs. Next check: open platform.claude.com/docs/en/test-and-evaluate/eval-tool.

**Rollback**

[confirmed Q3] File checkpointing in the Agent SDK records edits made through the Write, Edit, and NotebookEdit tools and can restore earlier file states. {S121}

[confirmed Q3] Its documented blind spots are Bash-made changes, subagent edits, directory operations, remote files, and anything outside the originating session; the docs point to git for the rest.

[inference Q3] ICM leans on local scripts and subagents, which are exactly the blind spots. Git revert of the run branch is the rollback of record; checkpointing is a convenience inside one session.

[confirmed Q3] Memory stores have no restore endpoint; rolling back means writing an old version's content back. {S120}

[inference Q3] Nothing rolls back external side effects such as a sent email or a CRM write. The control is prevention: `always_ask` or an approval queue on write tools.

**Tracing standard** (owned by WP-Q12)

[unverified Q3] GitHub excerpts show the OpenTelemetry GenAI conventions moved to a dedicated repository {S154}, with `gen_ai.*` attributes marked Development {S155}. Next check: WP-Q12 should open github.com/open-telemetry/semantic-conventions-genai.

### Answer summary

**Q3. Gaps between ICM as published and what an enterprise needs, with the best existing solution and its maturity.**

| Gap | Published ICM | Best existing fix | Maturity |
|---|---|---|---|
| Run history | Files on disk; optional Git commits | Durable Task Scheduler history and dashboard, plus Agent SDK transcripts mirrored to a session store. Managed alternative: session event log and deployment runs | Durable Task Scheduler: Microsoft's recommended backend {S128}, GA dates unverified. Managed Agents: beta {S124} |
| Versioning | Manual Git | Git repo per workspace, branch or commit per run; Managed Agents GitHub mount | Git: mature. GitHub mount: beta {S130} |
| Memory | None by design | Human-edited L3 in Git; optional Managed Agents memory stores | Memory stores: beta {S120}, 30-day version history {S120} |
| Concurrency | Sequential, local-first | Isolated working copy per run, plus a durable queue | Durable Task Scheduler as above; worktrees unverified |
| Multi-user editing | Not addressed | Pull requests with code owners | Mature for technical users (unverified this session); no fix found for non-technical editors |
| Access control | Not addressed | Agent SDK path rules and hooks, plus storage RBAC; Managed Agents permission policies | SDK below 1.0, label unverified; policies beta {S126} |
| Secrets | Not addressed | Azure Key Vault references with managed identity; Managed Agents vaults | Key Vault path unverified this session; vaults beta {S125} |
| Scheduling | Not addressed | Azure Container Apps jobs; Managed Agents scheduled deployments | Jobs unverified this session; deployments beta {S123} |
| Error handling | Manual re-run | Durable orchestration with one activity per stage | Durable Task Scheduler as above |
| Testing and evals | Self-run audit checklists | promptfoo for regression tests, Outcomes rubrics as runtime gates, Microsoft Foundry evaluations | promptfoo status unverified; Outcomes beta {S131}; Foundry GA {S127} with some evaluators in preview (unverified) |
| Rollback | Git, if used | Git revert of the run branch; file checkpointing inside a session | Checkpointing has documented blind spots |

[inference] Every gap has a workable fix today, but no single GA product closes them all. Claude Managed Agents covers the most gaps in one place, yet it is beta throughout, excluded from ZDR and HIPAA BAA coverage, and not confirmed on Microsoft Foundry.

[inference] For an Azure-first, regulated-buyer build, the lower-risk stack is: Git for versioning and review, Claude Agent SDK in Azure Container Apps for execution, Durable Task Scheduler for run history, concurrency, and error handling, Azure Key Vault for secrets, and promptfoo for tests. The cost is that Nihilo owns the glue code.

[inference] Two gaps have no good off-the-shelf answer: safe editing by non-technical owners, and rollback of external side effects. Both need design work in WP-Q10 and the security package.

### Coverage checklist

Must answer: for each gap, the best existing product, tool, or pattern, and its maturity with evidence.

* Run history: covered. Primary docs fetched for Managed Agents, Agent SDK sessions, Durable Task Scheduler. GA dates for Durable Task Scheduler rest on unfetched vendor blogs.
* Versioning: covered. Git from the paper, Managed Agents GitHub mount fetched. Blob versioning unverified.
* Memory: covered. Memory stores page fetched with limits, status, and risks.
* Concurrency: partly covered. Pattern and Durable Task Scheduler facts sourced; worktrees and Temporal unverified; hard rate limits left to the scalability package.
* Multi-user editing: partly covered. Git review pattern only from excerpts; no solution found for non-technical editors.
* Access control per layer and stage: covered at tool level (both permission pages fetched). Storage-level isolation is inference; deferred to WP-Q10.
* Secrets handling: covered for Managed Agents vaults (fetched). Azure Key Vault path unverified.
* Scheduling: covered for Managed Agents (fetched). Azure Container Apps jobs unverified.
* Error handling: covered. Durable Task Scheduler, Agent SDK, and deployment failure behavior fetched.
* Testing and evals: partly covered. Outcomes fetched; promptfoo, Foundry evaluator details, and the Console tool rest on excerpts. No tool was tested against an ICM workspace.
* Rollback: covered. File checkpointing page fetched with limitations.

### Open questions

1. Is Claude Managed Agents reachable through Microsoft Foundry? Next check: Microsoft Foundry Claude docs and the Managed Agents reference page.
2. What is the release status (GA or beta) of the Claude Agent SDK? Next check: the SDK overview and changelog on code.claude.com.
3. Can promptfoo's Claude Agent SDK provider run a real ICM stage folder and assert on output files? Next check: a one-hour spike on the `script-to-animation` workspace.
4. Can Microsoft Foundry evaluators score a Claude Agent SDK run hosted in Azure Container Apps? Next check: the Foundry evaluation docs for trace-based evaluation, then a test with an exported OpenTelemetry trace.
5. Does Temporal offer a Claude Agent SDK integration? Next check: docs.temporal.io/integrations.
6. Does the Durable Task SDK cleanly wrap an Agent SDK run as an activity, including human approval as an external event? Next check: build the two-stage prototype.
7. Does `_core/CONVENTIONS.md` or any open pull request in the ICM repo add run history, versioning, or access rules? Next check: read that file and the 9 open pull requests.
8. What does the community repo KakkoiDev/icm-runtime actually do? Its search excerpt claims auditable, token-metered, tamper-evident runs, but I could not fetch it. Next check: open github.com/KakkoiDev/icm-runtime and check license, commits, and last activity.
9. The eight excerpt-only items above (Durable Task Scheduler GA dates, Blob versioning, worktrees, GitHub code owners, Key Vault references, Container Apps jobs, promptfoo license, Foundry evaluator labels) need a fetch of the primary page.
10. Lead for the B8 owner: the arXiv abstract listing still uses the name Model Workspace Protocol (MWP) {S1}, while the v2 full text says Interpretable Context Methodology {S4}. Next check: compare v1 and v2 on arXiv.

## Sources attached by the API

- S1: Interpretable Context Methodology: Folder Structure as Agentic Architecture https://arxiv.org/abs/2603.16021
- S2: GitHub - RinDig/Interpretable-Context-Methodology: Folder structure as agent architecture.  ICM replaces framework-level orchestration with filesystem structure. https://github.com/RinDig/Interpretable-Context-Methodology
- S4: Interpretable Context Methodology: Folder Structure as Agent Architecture https://arxiv.org/html/2603.16021v2
- S120: Using agent memory https://platform.claude.com/docs/en/managed-agents/memory
- S121:  https://code.claude.com/docs/en/agent-sdk/file-checkpointing
- S122:  https://code.claude.com/docs/en/agent-sdk/sessions
- S123: Scheduled deployments https://platform.claude.com/docs/en/managed-agents/scheduled-deployments
- S124: Claude Managed Agents overview https://platform.claude.com/docs/en/managed-agents/overview
- S125: Authenticate with vaults https://platform.claude.com/docs/en/managed-agents/vaults
- S126: Permission policies https://platform.claude.com/docs/en/managed-agents/permission-policies
- S127: Microsoft Foundry Observability Generally Available https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/generally-available-evaluations-monitoring-and-tracing-in-microsoft-foundry/4502760
- S128: Durable Task Scheduler - Durable Task https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-task-scheduler/durable-task-scheduler
- S129:  https://code.claude.com/docs/en/agent-sdk/permissions.md
- S130: Accessing GitHub https://platform.claude.com/docs/en/managed-agents/github
- S131: Define outcomes https://platform.claude.com/docs/en/managed-agents/define-outcomes
- S132: Announcing Azure Functions Durable Task Scheduler Dedicated SKU GA & Consumption SKU Public Preview https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-azure-functions-durable-task-scheduler-dedicated-sku-ga--consumption-/4465328
- S133: The Durable Task Scheduler Consumption SKU is now Generally Available https://techcommunity.microsoft.com/blog/appsonazureblog/the-durable-task-scheduler-consumption-sku-is-now-generally-available/4506682
- S134: Blob Versioning in Azure Storage - Azure Storage https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview
- S135: Run parallel sessions with worktrees - Claude Code Docs https://code.claude.com/docs/en/worktrees
- S136: Common workflows - Claude Code Docs https://code.claude.com/docs/en/common-workflows
- S137: GitHub - temporalio/temporal: Temporal service · GitHub https://github.com/temporalio/temporal
- S138: Integrations https://docs.temporal.io/integrations
- S139: About code owners - GitHub Docs https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- S140: About protected branches - GitHub Docs https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- S141: Manage secrets in Azure Container Apps https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets
- S142: Security overview in Azure Container Apps https://learn.microsoft.com/en-us/azure/container-apps/security
- S143: Claude Managed Agents Add Cron Schedules and Credential Vaults：Anthropic Beta Puts Agents on Autopilot https://www.techtimes.com/articles/318163/20260610/claude-managed-agents-add-cron-schedules-credential-vaultsanthropic-beta-puts-agents-autopilot.htm
- S144: Jobs in Azure Container Apps https://learn.microsoft.com/en-us/azure/container-apps/jobs
- S145: Create a job with Azure Container Apps using the Azure portal https://learn.microsoft.com/en-us/azure/container-apps/jobs-get-started-portal
- S146: GitHub - promptfoo/promptfoo: Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, DeepSeek, and more. Simple declarative configs with command line and CI/CD integration. Used by OpenAI and Anthropic. · GitHub https://github.com/promptfoo/promptfoo
- S147: Promptfoo is joining OpenAI https://www.promptfoo.dev/blog/promptfoo-joining-openai/
- S148: promptfoo - AI Tool by promptfoo https://205055.xyz/skill/promptfoo/promptfoo/
- S149: Claude Agent SDK https://www.promptfoo.dev/docs/providers/claude-agent-sdk/
- S150: Run evaluations from the Microsoft Foundry portal - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app
- S151: Built-in Evaluators Reference - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators
- S152: Using the Evaluation Tool - Claude Platform Docs https://platform.claude.com/docs/en/test-and-evaluate/eval-tool
- S153: Evaluate prompts in the developer console https://claude.com/blog/evaluate-prompts
- S154: Releases · open-telemetry/semantic-conventions · GitHub https://github.com/open-telemetry/semantic-conventions/releases
- S155: semantic-conventions-genai/docs/gen-ai/gen-ai-agent-spans.md at main · open-telemetry/semantic-conventions-genai · GitHub https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md

_169 search results consulted; 39 sources cited._
