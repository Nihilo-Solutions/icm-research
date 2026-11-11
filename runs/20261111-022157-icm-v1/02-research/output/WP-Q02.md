<!-- {"wp": "WP-Q02", "models": ["claude-fable-5-2"], "rendered_from_raw": true, "claims_extracted": false} -->
# WP-Q02: Q2, model portability

### Findings

Access date for every source below is 2026-11-11. The Anthropic, agents.md, and GitHub pages showed no page date. The arXiv paper is v2, dated 2026-03-18. I ran out of page fetches before opening the community repos and the Amazon Bedrock and Google Cloud platform pages, so those items rest on search snippets and are tagged accordingly.

[confirmed Q2] The paper's evidence comes only from Claude Code sessions driven by Claude Opus 4.6. {S4}

[confirmed Q2] Sub-agent delegation in those runs relied on Claude Code's Agent Teams capability, with stage sub-tasks handed from Opus 4.6 to Sonnet 4.6. {S4}

[confirmed Q2] L0 is the one layer tied to a Claude Code filename: the README labels it `CLAUDE.md` and marks it as always loaded, at about 800 tokens. {S2}

[confirmed Q2] Automatic L0 loading is a Claude Code behavior, not an ICM mechanism: the launcher pulls in `CLAUDE.md` from the working directory and each parent folder and joins them, with no file replacing another. {S94}

[inference Q2] L1 to L4 load only because the agent follows the routing text and opens files with its read tool. `CONTEXT.md` is not a filename Claude Code auto-loads; the subfolder files it does auto-load are `CLAUDE.md` and `CLAUDE.local.md`, and only after Claude touches a file in that folder. {S94}

[confirmed Q2] Run control in the repo is two plain typed keywords, `setup` and `status`, defined in a table in the root `CLAUDE.md`. {S2} {S91}

[inference Q2] Custom slash commands and hooks are not dependencies of ICM as published: the paper and README never mention hooks, and the run triggers are typed words, not `/commands`.

[unverified Q2] I did not open `_core/CONVENTIONS.md` or the sample workspace folders, so a `.claude/` folder (settings, hooks, registered skills) inside a workspace is not ruled out. Next check: browse `workspaces/*/` in the repo for any `.claude/` directory and read `_core/CONVENTIONS.md`.

[confirmed Q2] The README's workspace layout places a `skills/` folder at the workspace root and labels it Layer 3 domain knowledge. {S2}

[unverified Q2] ICM "skills" look like plain reference files loaded by path, not Claude Code registered skills: a third-party skills index reports seven skills in the repo {S18}, and its listing shows a path under `workspaces/course-deck-production/skills/`, not `.claude/skills/`. Community index, snippet only. Next check: confirm the paths in the repo tree.

[confirmed Q2] The paper claims model independence by design, saying the protocol needs no model-specific capability, while conceding that equal results on another model remain an empirical question. {S4}

[confirmed Q2] Cross-model results do not exist in the paper: its validity section limits testing to one Claude model family and lists runs on GPT, Gemini, and open-weight models such as Llama as future work. {S4}

[confirmed Q2] The Claude Agent SDK is Claude Code under the hood: installing either the TypeScript or Python package normally brings a native Claude Code binary with it {S92}, so SDK agents inherit the CLI's filesystem features. {S89}

[confirmed Q2] An SDK agent pointed at an ICM folder picks up `CLAUDE.md`, `.claude/` skills, subagents, commands, and settings-file hooks from disk when `settingSources` is left unset, since unset now means user plus project plus local. {S89}

[corrected Q2] Older guidance held that the SDK loads nothing from disk unless `settingSources` is set (a search snippet of the platform.claude.com copy of the page still reads that way {S95}, and a blog about 273 days old ties the opt-in behavior to SDK v0.1.0 {S96}). The code.claude.com page fetched in full today says the opposite, as cited in the previous finding. I treat the fetched page as more authoritative, since the other two are an unfetched snippet and an old secondary post.

[inference Q2] Because that default flipped between SDK versions, Nihilo should always pass `settingSources` explicitly and pin the SDK version per client build.

[confirmed Q2] Pointing the SDK at a workspace is done through the `cwd` option. Project settings and hooks are read only from that folder's `.claude/`, with no fallback to parents {S89}, while `CLAUDE.md` files in parent folders still load. {S89}

[inference Q2] The repo's pattern (step into a workspace and its own `CLAUDE.md` takes over {S91}) maps to setting `cwd` to the workspace folder per run. The root `CLAUDE.md` above it will also load, because all levels are additive and child-folder files load only on demand. {S89}

[confirmed Q2] Registering a skill from code is not possible in the SDK: the only route is a `SKILL.md` folder under `.claude/skills/` that the loader discovers. {S89}

[confirmed Q2] Subagent delegation survives the move to the SDK: definitions can be passed inline through the `agents` option (with the `Agent` tool allowed) or loaded from `.claude/agents/` through the project source. {S89}

[confirmed Q2] A hosted SDK build cannot reuse the paper's delegation mechanism directly: the SDK docs treat agent teams as something the CLI does and offer no SDK option for it. {S89}

[confirmed Q2] Hook coverage in the SDK is broader than in the CLI: settings-file shell hooks still fire and the app can add in-process callbacks {S89}, and the TypeScript package covers extra events such as `SessionStart` and `SessionEnd` that Python lacks. {S89}

[confirmed Q2] Switching an SDK agent to Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, or Microsoft Foundry takes an environment variable plus that cloud's credentials (for Foundry, `CLAUDE_CODE_USE_FOUNDRY=1`). {S92}

[confirmed Q2] Provider choice does not remove the features ICM leans on: Anthropic's availability page puts the CLI, the Agent SDK, subagents, hooks, commands, skills, `CLAUDE.md` memory, and MCP servers in its works-everywhere group. {S90}

[confirmed Q2] Scheduling and hosted sessions are the casualties off a Claude subscription: Routines (`/schedule`), cloud sessions, Claude Code in Slack, and Claude Code Desktop need a claude.ai sign-in and cannot be reached with a Console API key or a cloud provider. {S90}

[confirmed Q2] For Microsoft Foundry the documented substitutes are `/loop` for scheduling and GitHub Actions for cloud sessions {S90}, and GitLab CI/CD is listed as unavailable there. {S90}

[confirmed Q2] Amazon Bedrock is the one provider column where Claude Code's web search tool is marked absent; the same table marks it present for Microsoft Foundry and Claude Platform on AWS. {S90}

[confirmed Q2] Choosing the Hosted on Azure option in Foundry costs four API features that matter for agent builds: code execution, Agent Skills, the Files API, and programmatic tool calling all fail there by design with a 400 error. {S26}

[confirmed Q2] No manual feature flags are needed for that case in Claude Code, since the client itself recognizes an Azure-hosted deployment and scales back what it attempts. {S26}

[confirmed Q2] One MCP-related gap applies on Azure-hosted Foundry deployments: tool search does not work there. {S90}

[confirmed Q2] Anthropic's hosted agent runtime is not an option through Azure: Claude Managed Agents sits on the Foundry page's unsupported list, next to the Message Batches, Admin, and Compliance APIs. {S26}

[confirmed Q2] Skills on the Messages API are a separate, server-side mechanism: they are uploaded through `/v1/skills`, named by `skill_ids` in the `container` parameter, and run inside the code execution container with no network access. {S93}

[confirmed Q2] A skill built for one surface stays there: uploads to claude.ai, uploads through the API, and Claude Code's on-disk skills are three separate stores with no sync. {S93}

[inference Q2] The Foundry page's "Agent Skills not supported when hosted on Azure" and the Claude Code page's "skills work on every provider" do not conflict. The first is the server-side API mechanism; the second is local `SKILL.md` folders read from disk. Local skills should therefore work against an Azure-hosted deployment, but I did not test it.

[confirmed Q2] Amazon Bedrock is missing from the cloud platform list on the Agent Skills page, which names the Claude API, Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed), and Microsoft Foundry (Hosted on Anthropic). {S93}

[confirmed Q2] API Agent Skills carry a compliance cost: the page marks them as outside zero data retention arrangements and not HIPAA eligible. {S93}

[inference Q2] The raw Messages API has no workspace loader. `CLAUDE.md` loading, `.claude/` skills, subagents, and hooks are documented as things the Claude Code binary does against a local filesystem. A direct-API build must read the ICM files itself and place them in the prompt, which the SDK docs also allow through `systemPrompt`. {S89}

[confirmed Q2] Client-facing SDK builds have to authenticate with API keys or a cloud provider, not a claude.ai plan: Anthropic bars third-party products built on the SDK from offering claude.ai login or rate limits unless previously approved. {S92}

[confirmed Q2] Hosting several clients on one SDK process is unsafe with default options: some host-level inputs load no matter what `settingSources` says {S89}, and Anthropic's guidance is a separate filesystem per tenant, `settingSources: []`, and auto memory disabled. {S89}

[inference Q2] Following that guidance turns off automatic `CLAUDE.md` loading. A multi-tenant ICM host would either inject L0 through `systemPrompt` or run one isolated container per client with the project source on.

[confirmed Q2] Instructions in `CLAUDE.md` are advisory on every platform: Claude Code delivers the file as a user message after the system prompt, with no guarantee of strict compliance {S94}, and the docs point to a PreToolUse hook for anything that must be blocked. {S94}

[corrected Q2] The brief's product names are out of date on Anthropic's pages. "Azure AI Foundry" appears as Microsoft Foundry {S26}, and "Google Vertex AI" appears as Google Cloud's Agent Platform, though the switch is still `CLAUDE_CODE_USE_VERTEX`. {S90} Google's own current name was not checked.

[confirmed Q2] The closest cross-vendor equivalent of L0 is AGENTS.md: a plain Markdown instruction file with no required fields, now stewarded by the Agentic AI Foundation under the Linux Foundation. {S88}

[confirmed Q2] Codex from OpenAI, Jules and Gemini CLI from Google, Cursor, the GitHub Copilot coding agent, VS Code, Aider, goose, opencode, and Devin all appear on the site's list of compatible agents. {S88}

[confirmed Q2] Per-folder scoping works differently from Claude Code: with nested AGENTS.md files the nearest one takes precedence {S88}, whereas Claude Code concatenates every `CLAUDE.md` it finds. {S94}

[confirmed Q2] Maintaining two root files is no longer required for Claude Code: from v2.1.277 it reads a repository's `AGENTS.md` when no `CLAUDE.md` sits in the working directory or above {S94}, and a `CLAUDE.md` can pull the shared file in with an `@AGENTS.md` import. {S94}

[confirmed Q2] Codex-style `AGENTS.override.md` files do not carry over: Claude Code's docs list them, with `AGENTS.local.md` and `.agents/` folders, as not read. {S94}

[unverified Q2] Whether the Agent SDK reads `AGENTS.md` the same way is not stated on the pages I fetched; the AGENTS.md section is written for Claude Code sessions. Next check: run an SDK `query()` in a folder that has only `AGENTS.md` and inspect the loaded instructions.

[inference Q2] AGENTS.md covers L0 only. L1 and L2 `CONTEXT.md` files are ordinary files any file-reading agent can open. Subagents, hooks, and slash commands have no cross-vendor convention in anything I retrieved.

[unverified Q2] Skills may have their own portability route. Trade guides report that the `SKILL.md` format became an open standard in December 2025 and is read by GitHub Copilot, Cursor, Gemini CLI, and OpenAI Codex {S97}, and `.agents/skills` is described as the emerging neutral folder. {S97} Secondary sources only; I did not load agentskills.io. Next check: open agentskills.io and each vendor's skills documentation.

[unverified Q2] Community report, Gemini: a GitHub repo (CatoPaus/icm) describes an ICM reference implementation on Firebase Genkit running only on a Gemini model, with `GEMINI.md` as Layer 0. {S98} Snippet only, no quality data. Next check: open the repo and look for run outputs or any comparison with Claude.

[unverified Q2] Community reports, Codex and others: ICM-Doc advertises that it works with Claude Code, Codex, Cursor, and opencode {S19}; icm-builder-skill generates an `AGENTS.md` plus per-tool entry files {S99}; icm-runtime packages ICM as skills for Claude Code, pi, and Codex. {S100} Snippets only; these show ports exist, not that output quality holds. Next check: open each repo for logged runs.

[unverified Q2] Open-weight models: community guides say coding agents need at least 64k tokens of context while Ollama defaults to 4k on smaller GPUs {S101}, and weak tool calling is the other failure they report. Not a vendor source and not ICM-specific. Next check: read Ollama's context-length documentation, then run one ICM stage on a local model.

[inference Q2] Moving to a non-Claude model changes five things:
* The root filename (use `AGENTS.md` or a per-tool twin).
* The delegation mechanism (Agent Teams and Claude subagents are product features).
* Hooks and permission rules (enforcement must be rebuilt per harness).
* The runtime (the Claude Agent SDK's documented providers are all routes to Claude).
* Output quality, which nobody has measured.

### Answer summary

**Q2. Does ICM work with non-Claude models, or with Claude reached through Azure AI Foundry, AWS Bedrock, or Google Vertex AI?**

Claude through the clouds: yes, with the Claude Code CLI or the Claude Agent SDK. Anthropic lists the CLI, the Agent SDK, subagents, hooks, commands, skills, `CLAUDE.md` memory, and MCP servers as working on every provider. {S90} [inference] For an Azure-first build, the Agent SDK with `CLAUDE_CODE_USE_FOUNDRY=1` is the lowest-friction way to keep ICM's folder behavior intact.

Non-Claude models: by design yes, by evidence unknown. All of the paper's testing used a single Claude model family. {S4} The only non-Claude reports I found are unverified community repos.

**Q2. What breaks when you move off Claude Code (skills, `CLAUDE.md` loading, subagents, hooks)?**

| Feature | Claude Code CLI on Foundry, Bedrock, or Google Cloud | Claude Agent SDK, same providers | Messages API called directly | Non-Claude harness |
|---|---|---|---|---|
| L0 auto-load | Yes, `CLAUDE.md` (or `AGENTS.md` if no `CLAUDE.md`) | Yes, through the project source {S89}; set it explicitly | No loader; app injects it [inference] | `AGENTS.md` or a tool-specific file |
| L1 to L4 | Agent reads files by path | Same | App must supply file tools or pre-assemble context [inference] | Agent reads files by path [inference] |
| Skills | Local `SKILL.md` folders | Local folders only, no registration API {S89} | Separate server-side Skills API {S93}; fails on Azure-hosted Foundry {S26} | Open standard reported, unverified |
| Subagents | Yes; Agent Teams is CLI only | `agents` option or `.claude/agents/` {S89}; no Agent Teams | None built in [inference] | Product-specific [inference] |
| Hooks | Settings-file hooks | Settings-file hooks plus callbacks {S89} | None [inference] | Product-specific [inference] |
| Scheduling | `/schedule` needs claude.ai {S90}; use `/loop` or CI | Own scheduler [inference] | Own scheduler [inference] | Own scheduler [inference] |

[inference] ICM itself depends on very little: one auto-loaded root file, file read and write tools, a shell for scripts, and optional delegation. The paper's Agent Teams delegation is the only published behavior with no SDK equivalent option; SDK subagents are the substitute.

[inference] The bigger portability risk on Azure is the hosting option, not the model. Hosted on Azure removes server-side skills, code execution, the Files API, and tool search, so an ICM build there should keep skills and scripts local to its own container.

[inference] Ship every workspace with an `AGENTS.md` that holds L0 and a one-line `CLAUDE.md` that imports it. That keeps the same folder usable in Claude Code and in the AGENTS.md-compatible tools.

### Coverage checklist

* Whether ICM as published depends on Claude Code features: partly covered. Paper, README, and root `CLAUDE.md` were read in full; `_core/CONVENTIONS.md` and the workspace folders were not opened.
* How each feature behaves in the Claude API, Claude Agent SDK, Claude in Microsoft Foundry, Claude on Amazon Bedrock, Claude on Google Cloud: partly covered. Agent SDK, Foundry, and Claude Code per-provider behavior are sourced from fetched vendor pages. The Bedrock and Google Cloud platform pages were not fetched, so their API-level limits rest on the Agent Skills and feature-availability pages. Direct Messages API behavior for `CLAUDE.md`, subagents, and hooks is inference.
* Whether the Agent SDK can load `CLAUDE.md` and skills from a folder, and on which platforms: covered, including the changed `settingSources` default and the four cloud routes.
* What breaks with non-Claude models and whether AGENTS.md covers the same ground: partly covered. AGENTS.md and Claude Code's handling of it are sourced from primary pages. Skills-standard support and per-tool subagent or hook behavior rest on secondary sources or inference.
* Any reports of ICM run on non-Claude models: partly covered. Four community repos found by search snippet; none fetched, none with quality evidence, no independent evaluation found.

### Open questions

* Do local `SKILL.md` skills and subagents work from the Agent SDK against a Foundry deployment hosted on Azure? Next check: run a two-stage ICM workspace in Nihilo's tenant against both hosting options and compare.
* Does the Agent SDK read `AGENTS.md` when no `CLAUDE.md` exists? Next check: a one-file SDK test, plus the SDK TypeScript and Python reference pages.
* Which `settingSources` default applies to the SDK version Nihilo will pin? Next check: fetch https://platform.claude.com/docs/en/agent-sdk/claude-code-features and the SDK changelog, and compare with the code.claude.com copy.
* Does any sample workspace in the ICM repo ship a `.claude/` folder (hooks, settings, registered skills)? Next check: browse `workspaces/*/` and read `_core/CONVENTIONS.md`.
* What are the API-level feature limits for Claude on Amazon Bedrock and on Google Cloud? Next check: fetch https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock and https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/overview.
* Is there any measured ICM result on GPT, Gemini, or an open-weight model? Next check: open CatoPaus/icm, KakkoiDev/icm-runtime, TerraByte-Dev/ICM-Doc, and AI-Deamon/icm-builder-skill for logged runs, then run the repo's `script-to-animation` workspace on one non-Claude harness and compare outputs by hand.
* Is the Agent Skills format an open standard with first-party support in Codex, Gemini CLI, and GitHub Copilot? Next check: agentskills.io and each vendor's skills documentation.
* Can Claude Code or the Agent SDK be pointed at a non-Claude model through an LLM gateway in a supported way? Next check: https://code.claude.com/docs/en/llm-gateway and Anthropic's commercial terms.
* What does Google currently call the product Anthropic's docs name "Google Cloud's Agent Platform"? Next check: the Google Cloud documentation page for Claude models.

## Sources attached by the API

- S2: GitHub - RinDig/Interpretable-Context-Methodology: Folder structure as agent architecture.  ICM replaces framework-level orchestration with filesystem structure. https://github.com/RinDig/Interpretable-Context-Methodology
- S4: Interpretable Context Methodology: Folder Structure as Agent Architecture https://arxiv.org/html/2603.16021v2
- S18: RinDig/Interpretable-Context-Methodology https://hotskills.dev/skill/rindig-interpretable-context-methodology/
- S19: GitHub - TerraByte-Dev/ICM-Doc: A clinic for the folders your AI agent lives in. Diagnose, repair, or build an ICM (Interpretable Context Methodology) structure — markdown only, no dependencies. · GitHub https://github.com/TerraByte-Dev/ICM-Doc
- S26: Claude in Microsoft Foundry https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- S88: AGENTS.md https://agents.md
- S89:  https://code.claude.com/docs/en/agent-sdk/claude-code-features
- S90:  https://code.claude.com/docs/en/feature-availability
- S91: Interpretable-Context-Methodology/CLAUDE.md at main · RinDig/Interpretable-Context-Methodology https://github.com/RinDig/Interpretable-Context-Methodology/blob/main/CLAUDE.md
- S92:  https://code.claude.com/docs/en/agent-sdk/quickstart
- S93: Agent Skills https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- S94:  https://code.claude.com/docs/en/memory.md
- S95: Use Claude Code features in the SDK - Claude API Docs https://platform.claude.com/docs/en/agent-sdk/claude-code-features
- S96: The Definitive Guide to the Claude Agent SDK: Building the Next Generation of AI https://datapoetica.medium.com/the-definitive-guide-to-the-claude-agent-sdk-building-the-next-generation-of-ai-69fda0a0530f
- S97: The Agent Skills Standard: One SKILL.md, Every Tool — AgentsCamp https://agentscamp.com/guides/skills/agent-skills-open-standard
- S98: GitHub - CatoPaus/icm · GitHub https://github.com/CatoPaus/icm
- S99: GitHub - AI-Deamon/icm-builder-skill: ICM Builder — global AI agent skill that scaffolds complete ICM (Interpretable Context Methodology) workspaces. Interview, design, build AGENTS.md, CONTEXT.md room files, and skill stubs for any project. · GitHub https://github.com/AI-Deamon/icm-builder-skill
- S100: GitHub - KakkoiDev/icm-runtime: Interpretable Context Methodology (ICM) - bash runtime + reusable coding agent skills for structured multi-stage AI workflows · GitHub https://github.com/KakkoiDev/icm-runtime
- S101: Claude Code vs Codex vs OpenCode on Local Models (Ollama) · Aliteq https://aliteq.com/run-coding-agents-on-local-models-ollama

_94 search results consulted; 19 sources cited. Claims not yet extracted (credit ran out); the next run 02 extracts them._
