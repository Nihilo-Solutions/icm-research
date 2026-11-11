<!-- {"wp": "WP-Q04C", "models": ["claude-fable-5-2"], "rendered_from_raw": true, "claims_extracted": false} -->
# WP-Q04C: Q4, Google Workspace, Slack, and custom web app runtimes

### Findings

All pages accessed 2026-11-11. Page dates are given where the page shows one.

**Claude Agent SDK (self-hosted runtime behind a custom web app)**

[confirmed Q4] Project instructions, skills, and hooks kept on disk work in Agent SDK agents as they do in Claude Code, since the two share one foundation. {S89}

[confirmed Q4] With the "project" source enabled, a root CLAUDE.md in the working directory enters context when the session starts, and CLAUDE.md files in subfolders are pulled in on demand. {S89}

[inference Q4] The Agent SDK is the only runtime in this package that can load an ICM folder unchanged. L0 CLAUDE.md is native. L1 and L2 CONTEXT.md, L3 reference files, and L4 `output/` folders are ordinary files the agent reads and writes with its file tools. CONTEXT.md is not an auto-load filename, so CLAUDE.md must route to it, as ICM already does.

[confirmed Q4] Leaving `settingSources` unset pulls in user, project, and local settings, and Anthropic tells multi-tenant hosts not to rely on that default: give each tenant its own filesystem, pass an empty list, and switch off auto memory. {S89}

[inference Q4] That isolation advice conflicts with folder-native ICM. An empty `settingSources` also stops CLAUDE.md loading, so a multi-client host must either run one container per client workspace or inject L0 through `systemPrompt`.

[confirmed Q4] MCP servers attach through the `mcpServers` option.

[confirmed Q4] A programmatic hook can block a tool call by returning a deny decision with a reason.

[confirmed Q4] Nihilo would operate this runtime itself: every session is a `claude` CLI subprocess holding a shell, a working directory, and session files on the container disk. {S213}

[confirmed Q4] A container restart or scale-down wipes that local state, and the `SessionStore` adapter copies transcripts only, so working-directory artifacts need a mounted volume or separate sync. {S213} For ICM this means L4 run outputs need their own storage design.

[confirmed Q4] Anthropic's starting size is 1 GiB RAM, 5 GiB disk, and 1 CPU per agent, with a minimal container near $0.05 per hour and token spend usually far larger.

[estimate Q4] An always-on minimal container costs about $36.50 per month before tokens (730 hours x $0.05, from the hosting page figure above).

[confirmed Q4] OpenTelemetry export is switched on through container environment variables, and prompt text and tool inputs stay out of the export unless opted in. {S213}

[confirmed Q4] User authentication belongs at a gateway in front of the agent container, and sessions have no built-in timeout, so `maxTurns` must bound them. {S213}

[confirmed Q4] Microsoft's Claude models page (updated 2026-09-22) names the Claude Agent SDK as one way to build agents on Claude in Foundry. {S193} Anthropic's hosting page covers Amazon Bedrock and Google Cloud's Agent Platform endpoints. {S213} A search excerpt of the SDK quickstart, not fetched in full, shows a `CLAUDE_CODE_USE_FOUNDRY=1` switch.

[confirmed Q4] Products built on the SDK may not offer claude.ai login or plan rate limits without Anthropic's prior approval, so API-key authentication is required. {S221} Source is a search excerpt of the official overview page, not fetched in full.

[unverified Q4] GA or preview label for the Agent SDK. The fetched pages show no beta banner, and the hosting page references TypeScript v0.3.234 and Python v0.2.140 {S213}, both below 1.0. Next check: open https://code.claude.com/docs/en/agent-sdk/overview and both changelogs for a stability statement.

**Claude Managed Agents (Anthropic-hosted runtime)**

[confirmed Q4] Status is beta: every endpoint needs the `managed-agents-2026-04-01` header, and access is on by default for API accounts. {S124}

[confirmed Q4] Anthropic runs the agent loop and sandbox, with file, shell, web, and MCP tools, cron-style scheduled deployments, and event history kept server-side. {S124}

[confirmed Q4] CLAUDE.md is not loaded automatically: the migration guide maps the SDK's system prompt and CLAUDE.md hierarchy to one `system` string on a server-versioned Agent, and local directories become uploaded or mounted session files.

[confirmed Q4] A GitHub repository can be mounted into the session sandbox, and skills under its root `.claude/skills` folder are picked up once per session from the checked-out state.

[inference Q4] ICM on Managed Agents needs a small adapter. L0 goes into the Agent `system` string (versioned, which helps audit). L1 to L3 arrive as a mounted Git repo that the system prompt tells the agent to read. L4 must be pushed back to Git or downloaded, because the sandbox is per session.

[confirmed Q4] MCP servers are declared on the Agent, their credentials come from a Vault attached to the Session, and each tool carries a permission policy of `always_allow`, `always_ask`, or `auto`.

[confirmed Q4] Pre and post tool-use hooks do not carry over; the calling application must review tool events itself or set built-in tools to `always_ask`.

[confirmed Q4] Zero Data Retention and HIPAA BAA coverage are both unavailable, including when self-hosted sandboxes are used. {S124}

[confirmed Q4] Tool execution can sit in an Anthropic cloud sandbox or in a self-hosted sandbox on the customer's infrastructure. {S124}

[confirmed Q4] Supported platforms are the Claude API, Claude Platform on AWS, and Claude Models on Google Cloud (Anthropic managed). {S124} Microsoft Foundry is not in that list.

[confirmed Q4] Anthropic's pricing page charges $0.08 per session-hour of active runtime on top of standard token rates.

[estimate Q4] 100 runs a month at 15 minutes each is 25 session-hours, or about $2.00 of runtime before tokens (25 x $0.08).

**Microsoft Foundry Agent Service**

[confirmed Q4] The service has three agent types (prompt, voice-based prompt, hosted); a hosted agent is the customer's own code shipped as a container image or source .zip. {S207} Page updated 2026-10-26.

[confirmed Q4] A Microsoft Foundry blog post dated 2026-09-09 reports Hosted Agents reaching general availability on July 9, 2026, Toolboxes also GA, and agent skills and tool search still in public preview. {S217}

[confirmed Q4] Each hosted-agent session gets a VM-isolated sandbox with a persistent `$HOME` and `/files`, an idle timeout configurable from 2 to 240 minutes, and deletion after 30 days of inactivity.

[confirmed Q4] Hosted agents support Python and C#, sandbox sizes run from 0.5 vCPU with 1 GiB to 2 vCPU with 4 GiB, and session disk tops out at 20 GiB. {S210}

[confirmed Q4] Deployment creates a dedicated Microsoft Entra agent identity and endpoint per hosted agent, and user-invoked calls from Microsoft 365 channels can use On-Behalf-Of delegation. {S210}

[confirmed Q4] Platform controls include Azure RBAC over who creates and invokes agents, content filters, and virtual network options for prompt and hosted agents.

[confirmed Q4] Remote MCP servers are supported with key, Microsoft Entra, OAuth passthrough, or unauthenticated access. {S207}

[confirmed Q4] A Toolbox publishes a curated tool set behind one managed MCP-compatible endpoint with central authentication and versioning.

[confirmed Q4] Hosted agents receive an Application Insights connection string automatically and emit OpenTelemetry traces when built on the protocol libraries.

[confirmed Q4] Published agents can be surfaced in Microsoft Teams and Microsoft Copilot, with the platform bridging to the Activity protocol. {S207} {S210}

[confirmed Q4] Prompt agents carry no platform fee beyond model tokens and tool charges, while hosted agents are billed on container compute per hour.

[unverified Q4] Hosted-agent compute rates. The fetched pricing page rendered the vCPU and memory rates as "$-" placeholders. {S208} A Microsoft blog search excerpt from the April 2026 preview gave $0.0994 per vCPU-hour and $0.0118 per GiB-hour. Next check: open https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/ in a browser with East US selected.

[confirmed Q4] Microsoft advises against auto-loading code, configuration, or trusted instructions from upload-writable paths when uploaders are untrusted, and says to keep session data apart from application files.

[inference Q4] In a hosted agent, ICM L0 to L3 should be baked into the container image or pulled read-only from Git at start, with L4 in `$HOME` or external storage. No Foundry page describes native loading of CLAUDE.md or CONTEXT.md.

[confirmed Q4] The Microsoft Copilot harness (preview, page updated 2026-11-04) is an optional managed runtime for prompt agents with file read and write, shell, web fetch, and subagent tools plus skills. {S220}

[confirmed Q4] Foundry skills are versioned resources packaged as a directory or ZIP with `SKILL.md` at the root. {S220}

[confirmed Q4] The harness does not support bring-your-own-model, and its sandbox is not a durable output store. {S220}

[unverified Q4] Whether Claude models can back prompt agents. The overview names GPT-4o, Llama, and DeepSeek as example models. {S207} A Microsoft Q&A answer from about April 2026 said Claude was not supported for the `create_agent` API. A 2025 Ignite blog said the Claude family was available in the service. Next check: filter https://ai.azure.com/catalog/models by `capabilities=agentsv2` and read the model-region-support page.

[confirmed Q4] Hosted agents reason with models from the Foundry catalog, and Microsoft Agent Framework supports agents on Claude models. {S210} {S193}

[unverified Q4] Whether the Claude Agent SDK, with its CLI subprocess, runs inside a Foundry hosted agent. The overview lists an "Anthropic Agent SDK" option, but its link points to the `anthropic-sdk-python` client library repo. {S207} Next check: look for a Claude Agent SDK sample under https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents, then test one container in Nihilo's tenant.

[confirmed Q4] Claude in Foundry needs an Azure Marketplace subscription billed in Claude Consumption Units, and Foundry applies no built-in content filtering to Claude at deployment. {S193}

**Slack: Claude Tag**

[confirmed Q4] Claude Tag is a public beta limited to Team and Enterprise plans on Anthropic's own service, excluding individual plans and third-party deployments. {S209} {S211}

[confirmed Q4] Slack members need no Claude seat for channel work; that work draws on an organization usage balance capped by an Owner-set spend limit, with no per-seat surcharge. {S209}

[confirmed Q4] The underlying plans list Team Standard seats at $20 per month billed annually ($25 monthly) for 2 to 150 people, and Enterprise at $20 per seat per month with a 20-seat minimum plus usage at API rates.

[confirmed Q4] Behavior is shaped per scope (organization, workspace, or channel) by four layers: connectors, plugins and skills, custom instructions, and channel memory. {S211}

[confirmed Q4] A claude.ai Project's instructions and knowledge are not read in Slack, and a channel cannot be pointed at a Project. {S211}

[confirmed Q4] A repository's own CLAUDE.md is read when Claude starts work in that repository.

[inference Q4] In Claude Tag, L0 maps to organization or workspace custom instructions, L1 and L2 map to channel instructions (one channel per workflow or department), L3 maps to skills or a granted Git repo, and L4 has no home, because sandbox files are discarded unless pushed to a branch or posted in the thread. It does not load an ICM folder as such.

[confirmed Q4] Custom MCP servers can be added through the custom-connector path. {S211}

[confirmed Q4] Each Slack thread runs in its own sandbox that never holds provisioned credentials; a proxy injects them at the network boundary, and outbound traffic is default-deny. {S212}

[confirmed Q4] Connector credentials are shared service-account credentials, so every member of a channel can direct Claude to use whatever that account can read or write.

[confirmed Q4] Scoping a credential to one channel does not wall off knowledge: notes saved from a public channel are visible to sessions across the workspace.

[confirmed Q4] Owners get an Activity page covering scheduled work, memory, and an hourly JSON export of proxy network events (Git and MCP traffic excluded), but there is no per-action log of each task and its requester.

[confirmed Q4] Organizations with Zero Data Retention, a customer-managed encryption policy, or the HIPAA configuration cannot use Claude Tag. {S212}

[confirmed Q4] By default any member of the paired Slack workspace can invoke Claude; Team plans can narrow this to organization members, and only Enterprise can narrow it by role.

[confirmed Q4] Setup is a one-time Owner task (pair the workspace with a code, set a spend limit, add channels), after which members need no per-user setup.

[confirmed Q4] Anthropic's hosting guide gives a Slack chat bot as an example of the Agent SDK's long-running session pattern. {S213} A custom Slack bot on a self-hosted runtime is therefore an alternative to Claude Tag.

[unverified Q4] A slack.com help excerpt says Claude Tag replaces the earlier Claude app in Slack from August 3, 2026. Next check: open https://slack.com/help/articles/53532192117267-Use-Claude-in-Slack.

**Google: Gemini Enterprise and Google Workspace**

[confirmed Q4] Google lists Gemini Enterprise Business from $21 per seat per month for up to 300 seats, and Standard/Plus from $30 with unlimited seats, ADK or third-party agents, VPC-SC, and customer-managed keys.

[confirmed Q4] Custom MCP server data stores in the Standard, Plus, Pay-as-you-go, and Frontline editions accept only HTTPS StreamableHTTP servers, with OAuth 2.0 or no authentication. {S216} Page updated 2026-10-30.

[confirmed Q4] An organization policy blocks custom MCP data stores until an admin overrides it, imported tools start disabled with a cap of 100 enabled, and every call asks the user to confirm unless the tool is annotated read-only.

[confirmed Q4] Private MCP servers are reached through Agent Gateway, currently in `us-central1` and `europe-west1`, and a Sensitive Data Protection policy can be attached to the connector. {S216}

[unverified Q4] GA or preview status of custom MCP in Gemini Enterprise. The fetched setup page shows no preview label. Google release-note excerpts, not fetched in full, call the Business edition connection and the unauthenticated option Public Preview. Next check: read https://docs.cloud.google.com/gemini/enterprise/docs/release-notes and https://support.google.com/g/answer/16719009.

[confirmed Q4] Google Workspace Studio gained custom steps built with Apps Script, Beta third-party integrations (including HubSpot, Jira, QuickBooks, Salesforce, and Slack), and webhooks on 2026-09-17, all off until an admin enables them and subject to approval settings.

[confirmed Q4] Those Studio features cover Business Starter, Standard, and Plus and Enterprise Standard and Plus editions. {S219}

[confirmed Q4] Shared Gems live in Google Drive under Drive sharing settings, and admins can switch Gem sharing by organizational unit or group. {S222} Source is a search excerpt of Google's admin help page, not fetched in full.

[confirmed Q4] A Studio flow can prompt a private Gem through the "Ask a Gem" step, provided the Gem's knowledge base is Drive files. {S223} Source is a search excerpt of the Workspace Updates blog, not fetched in full.

[unverified Q4] MCP support in Gems or Workspace Studio. No fetched Google page describes an MCP client setting for either, and one secondary source says the Workspace side panel has no interface for adding MCP servers. Next check: search the Workspace Studio help center (https://support.google.com/workspace-studio) for "MCP".

[inference Q4] Google surfaces cannot load an ICM folder. A Gem collapses L0 and L2 into one instruction field with Drive files as L3. Studio flow steps can imitate stage handoffs, and Drive folders can hold L4. All of it runs on Gemini models, outside the Claude-only evidence base in B5.

[unverified Q4] Google Workspace seat prices. Only secondary sources were retrieved (one cites $14 per user per month for Business Standard on annual terms). Next check: https://workspace.google.com/pricing.

[estimate Q4] Gemini Enterprise at starting list prices: 5 seats x $21 = $105 per month; 5,000 seats x $30 = $150,000 per month before negotiated discounts (prices from Google's subscriptions page above).

### Answer summary

Q4, for Google Workspace, Slack, and a custom web app on an agent runtime. The table restates the findings above; the fit columns are `[inference]`.

| Surface | Status | ICM layers it can represent | MCP | Admin and security controls | Cost | Setup effort | Fit: 5 people | Fit: 5,000 people |
|---|---|---|---|---|---|---|---|---|
| Google Workspace (Gems, Workspace Studio) | Studio integrations Beta, custom steps limited preview | L0 and L2 collapsed into Gem instructions, L3 as Drive files, L4 as Drive folders by convention; no folder loading | Not found (unverified) | Admin console toggles by OU or group, step approvals, webhook URL allowlist on some editions | Included in Workspace editions; seat price unverified | Low | Good for simple flows if the client is already on Google | Weak for ICM: user-owned flows, Gemini only |
| Gemini Enterprise | Custom MCP status unverified | Agent instructions plus connectors; no folder loading | Yes: remote StreamableHTTP, OAuth, admin-enabled actions | Org policy gates, per-action confirmation, VPC-SC and CMEK on Standard/Plus | From $21 (Business) or $30 (Standard/Plus) per seat per month | Medium | Possible on Business edition | Viable governance, but it is not ICM and not Claude |
| Slack: Claude Tag | Public beta | L0 as org or workspace instructions, L1 and L2 as channel instructions, L3 as skills or repo, no durable L4 | Yes: custom connector | Scoped connectors, credential proxy, default-deny egress, spend limits; no per-action log; no ZDR, CMEK, or HIPAA | Team or Enterprise plan plus usage balance | Low | Strong: fastest no-terminal surface | Usable for teams, but shared service accounts and thin audit are gaps for regulated buyers |
| Claude Agent SDK, self-hosted | No beta label found; pre-1.0 versions | All five layers, folder loaded as is | Yes | Whatever Nihilo builds: hooks, permissions, egress proxy, OTel; runs in any tenant | Tokens plus roughly $0.05 per container-hour | High: web UI, auth gateway, storage, isolation | Overkill unless Nihilo hosts a shared platform | Strongest fit for client-tenant deployment and audit needs |
| Claude Managed Agents | Beta | L0 as versioned system string, L1 to L3 as mounted repo, L4 must be exported | Yes, with Vault credentials | Per-tool permission policies, server-side history, self-hosted sandbox option; no ZDR or HIPAA | Tokens plus $0.08 per session-hour | Medium: still needs a front end | Good for scheduled automations | Blocked for healthcare-adjacent buyers; not offered through Foundry |
| Foundry Agent Service | Hosted agents and Toolboxes GA; Copilot harness and skills preview | Prompt agent: instructions plus skills. Hosted agent: whatever the container loads | Yes: remote MCP and Toolbox | Entra agent identity, RBAC, VNet, App Insights tracing, Teams and Copilot publishing | Tokens plus tools; hosted compute rate unverified | Medium to high | Too heavy | Best Azure-native governance; Claude and ICM folder fit unproven |

- `[inference]` No surface in this package gives non-technical staff a ready-made ICM workspace. Claude Tag is the closest out-of-the-box option, and the Agent SDK is the only one that preserves the folder model, at the cost of building the whole application around it.
- `[inference]` For Azure-first enterprise builds, the test that matters is whether the Claude Agent SDK runs inside a Foundry hosted agent (for Entra identity, VNet, and tracing) or whether Nihilo must host it on plain Azure compute and add those controls itself.
- `[inference]` For regulated buyers, Managed Agents and Claude Tag both lose on data-handling eligibility today, which pushes those deals toward self-hosted Agent SDK or Foundry.

### Coverage checklist

- **Layers, MCP, admin and security controls, cost, setup effort, and 5 versus 5,000 fit for each surface: partly covered.** Slack (Claude Tag), Claude Agent SDK, Claude Managed Agents, and Foundry Agent Service are covered from fetched vendor pages. Google is weaker: Gemini Enterprise MCP and pricing are confirmed, but Gems rest on search excerpts, Workspace MCP support was not found, and Workspace seat prices are unverified. Foundry hosted-agent compute rates are unverified. Setup effort and fit are inferences.
- **GA or preview status and folder-loading ability for each runtime: partly covered.** Managed Agents (beta, no CLAUDE.md auto-load) and Foundry (hosted agents GA, harness preview, no native folder loading) are confirmed. Agent SDK folder loading is confirmed, but its GA designation is not. Whether the Claude Agent SDK runs in a Foundry hosted agent, and whether Claude can back Foundry prompt agents, are open.

### Open questions

1. Does the Claude Agent SDK run inside a Foundry hosted agent? Next check: inspect the foundry-samples hosted-agents folder, then deploy a test container in Nihilo's tenant with `CLAUDE_CODE_USE_FOUNDRY=1`.
2. Can Claude models back Foundry prompt agents and the Copilot harness? Next check: the `agentsv2` catalog filter and https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions.
3. What are the current hosted-agent compute rates? Next check: the Azure pricing page in a browser, or the Azure pricing calculator.
4. Is the Agent SDK formally GA, and what support terms apply? Next check: the SDK overview page and Anthropic's commercial terms.
5. Is Gemini Enterprise custom MCP GA or preview, per edition? Next check: both Google release-notes pages named above.
6. Do Gems or Workspace Studio support MCP, and what do Workspace seats cost? Next check: Workspace Studio help center and workspace.google.com/pricing.
7. What does Claude Tag usage actually cost per channel? Anthropic's own advice is a pilot with a spend limit. Next check: run a two-week pilot in Nihilo's Slack and read the per-channel usage page.
8. "Claude for Google Workspace" appears as an extension in Anthropic's site navigation and was not researched here. Next check: open https://claude.com/claude-for-google-workspace and coordinate with the worker covering Claude Team and Enterprise surfaces.
9. Will Claude Tag's audit gaps (no per-action requester log, MCP traffic missing from the network export) close at GA? Next check: re-read https://claude.com/docs/claude-tag/admins/audit.md at GA, and check whether the Enterprise Compliance API covers Claude Tag sessions.

## Sources attached by the API

- S89:  https://code.claude.com/docs/en/agent-sdk/claude-code-features
- S124: Claude Managed Agents overview https://platform.claude.com/docs/en/managed-agents/overview
- S193: Claude models in Microsoft Foundry - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models
- S207: What is Microsoft Foundry Agent Service? - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- S208: Foundry Agent Service - Pricing | Microsoft Azure https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/
- S209:  https://support.claude.com/en/articles/11506255-get-started-with-claude-in-slack
- S210: Hosted agents in Foundry Agent Service - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents
- S211:  https://claude.com/docs/claude-tag/admins/customize.md
- S212:  https://claude.com/docs/claude-tag/concepts/security-and-data.md
- S213:  https://code.claude.com/docs/en/agent-sdk/hosting
- S216: Set up your custom MCP server data store  |  Gemini Enterprise  |  Google Cloud Documentation https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server
- S217: What's new in Microsoft Foundry: July and August 2026 | Microsoft Foundry Blog https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-july-august-2026/
- S219: Google Workspace Updates: Automate workflows with custom starters and steps, third-party integrations, and webhooks in Workspace Studio https://workspaceupdates.googleblog.com/2026/09/automate-workflows-with-custom-starters-and-steps-third-party-integrations-and-webhooks-in-Workspace-Studio.html
- S220: Use the Microsoft Copilot harness with prompt agents - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/use-tools-skills-copilot-harness
- S221: Agent SDK overview - Claude Code Docs https://code.claude.com/docs/en/agent-sdk/overview
- S222: As an administrator, you control whether your users can: https://knowledge.workspace.google.com/admin/gemini/turn-gem-sharing-on-or-off
- S223: Google Workspace Updates: Use your Gems in your Google Workspace Studio flows https://workspaceupdates.googleblog.com/2026/04/use-your-gems-in-your-google-workspace-studio-flows.html

_122 search results consulted; 17 sources cited. Claims not yet extracted (credit ran out); the next run 02 extracts them._
