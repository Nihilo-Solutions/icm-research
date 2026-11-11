<!-- {"wp": "WP-Q04A", "models": ["claude-fable-5-2"], "fallbacks": 0, "stop_reason": "end_turn", "cost_usd": 2.375, "searches": 16, "fetches": 20} -->
# WP-Q04A: Q4, Microsoft surfaces for non-technical users

### Findings

All pages were accessed 2026-11-11. Page dates are the pages' own `ms.date` values where shown. "Lead" means search-result text from a page I could not fetch in full, so it is not treated as evidence.

**Claude in Copilot Studio and Foundry**

[confirmed Q4] Four Claude models show as generally available primary models for standard-harness agents on Microsoft's model table (page dated 2026-10-22): Claude Sonnet 4.6, Claude Opus 4.6, Claude Opus 4.7, and Claude Opus 4.8. {S181}

[confirmed Q4] Outside the United States column, each of those Claude rows carries a cross-geo flag, meaning data may be processed and stored beyond the organization's geographic boundary. {S181} The US Government table shows GPT-4o only. {S181}

[unverified Q4] Claude Sonnet 5 in Copilot Studio is not settled. A search-result excerpt of the "What's new" page announces it as generally available {S191}, but the fetched table covers only "selected models" and omits it. Next check: fetch https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new and open the model picker in Nihilo's tenant.

[confirmed Q4] Contract terms for Claude inside Microsoft 365 Copilot and Copilot Studio run through Microsoft rather than Anthropic: under the subprocessor arrangement, the Microsoft Product Terms and DPA cover usage, with a carve-out for models carrying the Anthropic models with Data Retention label (page dated 2026-11-04). {S37}

[confirmed Q4] Tenants in the EU, EFTA, and UK start with Claude switched off, and Claude traffic in these products sits outside the EU Data Boundary commitment. {S37}

[confirmed Q4] GCC High, DoD, federal GCC, and other sovereign clouds get no Claude option at all {S37}; non-federal GCC gained an opt-in setting on July 22, 2026. {S37}

[confirmed Q4] Two admin switches gate Claude for makers: external models must be turned on per environment or environment group in the Power Platform admin center, and the Anthropic provider must be allowed in the Microsoft 365 admin center.

[confirmed Q4] Security-group scoping exists: an admin can limit Anthropic access to named users or Entra ID groups, and the assignment holds across both Copilot and Copilot Studio. {S37}

[confirmed Q4] Some advanced Claude models (Microsoft names Claude Fable 5 and Claude Mythos 5) fall under Anthropic's own commercial terms and DPA, with Anthropic keeping most inputs and outputs for up to 30 days, and they stay off until a tenant admin opts in.

[confirmed Q4] Billing treats Claude Opus 4.7 as a reasoning model: Microsoft's worked example prices one follow-up message at 141 Copilot Credits of premium token charge, and 461 credits when the same question opens a fresh conversation. {S187}

[estimate Q4] At the capacity-pack rate of $0.008 per credit ($200 / 25,000), those examples cost about $1.13 and $3.69 per message (141 x 0.008 and 461 x 0.008), before feature rates. Inputs: pack price and size {S175}, credit counts {S187}.

[inference Q4] ICM loads long layered instructions at each stage, which is the pattern Microsoft's billing page says drives credit use. A Claude Opus-orchestrated ICM agent in Copilot Studio is likely costly per run for anyone without a Microsoft 365 Copilot seat.

[unverified Q4] Whether Claude Sonnet 4.6 (tagged General, not Deep) also triggers the premium token rate was not found. Next check: the reasoning-model definition in the Copilot Studio Licensing Guide (https://go.microsoft.com/fwlink/?linkid=2320995).

[confirmed Q4] Foundry deployments of Claude require accepting Azure Marketplace terms on a paid subscription, and Microsoft's page (dated 2026-09-21) rules out Cloud Solution Provider subscriptions and credit-only sponsored or trial subscriptions. {S55}

[confirmed Q4] Data retention for Claude on Foundry is a setting Anthropic controls, not Microsoft, per the troubleshooting table on that page. {S55}

[unverified Q4] Sources disagree on whether Foundry Agent Service accepts Claude as its model (owned by WP-Q04C). An older ai-foundry page excerpt says it does {S192}; the current Claude models page excerpt lists only Microsoft Agent Framework and the Claude Agent SDK under agent support {S193}; a Microsoft Q&A answer about seven months old says the create_agent API does not {S194}. The current Learn page is the more authoritative, but I only have its excerpt. Next check: fetch https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/model-region-support.

[unverified Q4] Lead: Anthropic's Foundry documentation excerpt describes Anthropic as an independent processor, with customers under Anthropic's data use terms. {S26} Next check: fetch https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry and the Learn data-privacy page for Claude in Foundry.

[confirmed Q4] Bring-your-own models, Foundry models included, sit outside the Copilot Credit rate table and are billed separately. {S187}

**Microsoft 365 Copilot**

[confirmed Q4] Microsoft lists the Microsoft 365 Copilot add-on at $30.00 per user per month, paid yearly, on top of a qualifying Microsoft 365 plan {S175} (no page date shown).

[confirmed Q4] For firms on Business plans, the Microsoft 365 Copilot Business add-on lists at $21.00 per user per month paid yearly, cut to $18.00 for the first year on annual purchases made July 1 to December 31, 2026, or $25.20 on a monthly subscription. {S176} Business plans top out at 300 licensed users. {S179}

[estimate Q4] Seat cost before base licenses and discounts: 5 users x $21 = $105 per month ($90 at the promo price); 5,000 users x $30 = $150,000 per month at list. Inputs: Business add-on price {S176}, enterprise add-on price {S175}.

[confirmed Q4] MCP reaches Microsoft 365 Copilot only through declarative agents: an MCP server is attached as a plugin action, its tools are discovered at runtime by default, and the server itself runs outside Microsoft 365 {S185} (page dated 2026-10-28, no preview label). Doc: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-plugins

[unverified Q4] I did not retrieve an explicit GA statement for MCP plugins in declarative agents. A trade-press item reports GA since June 2026. {S195} Next check: fetch https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new.

[confirmed Q4] User consent is built in: the first data send to a plugin triggers a prompt, and tools that change data keep asking for confirmation unless the developer overrides the default. {S185}

[confirmed Q4] Practical ceilings apply: past five plugins the agent falls back to semantic matching on plugin descriptions, more than about 10 tools can degrade answers, and large tool payloads get truncated. {S185}

[unverified Q4] Lead: Learn search-result text gives an 8,000-character cap on declarative agent instructions and warns against parking instructions in SharePoint documents, because knowledge content passes through cross-prompt-injection classifiers and can be blocked or sanitized. {S196} Next check: fetch https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-instructions.

[inference Q4] If that lead holds, a declarative agent can carry L0 in its instructions field and L3 as knowledge, but L1 and L2 `CONTEXT.md` files cannot safely live as knowledge, and L4 run artifacts have no native home.

[unverified Q4] Lead: SharePoint and OneDrive knowledge in declarative agents needs each signed-in user to hold a Microsoft 365 Copilot license. {S197} Next check: fetch https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/knowledge-sources.

[confirmed Q4] Copilot Cowork, Code, Autopilot, and the Work IQ APIs are metered in Copilot Credits on top of the seat license. {S176}

[unverified Q4] Lead: Copilot Cowork loads custom skills from `SKILL.md` files in a OneDrive folder (/Documents/Cowork/skills/), up to 50 {S198} {S199}, asks for approval before each action {S200}, and cannot delete OneDrive or SharePoint files {S199}. This is the closest Microsoft-native analog to an ICM folder workspace I found. Next check: fetch https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork and test numbered stage folders with output handoff in Nihilo's tenant.

[confirmed Q4] Audit posture for Copilot comes with the platform: prompts and responses are logged, follow the tenant's retention policies, and are reachable by eDiscovery and Microsoft Purview. {S176}

**Copilot Studio**

[confirmed Q4] Three runtimes, which Microsoft calls harnesses, sit under Copilot Studio (page dated 2026-10-19): the GitHub Copilot harness for multi-step reasoning work, the Customer Conversation harness, and the standard harness for rule-based agents and agent flows.

[confirmed Q4] ICM-relevant features cluster in the GitHub Copilot harness: skills, memory, native creation and editing of Word, Excel, PowerPoint, and PDF files, a per-task sandbox, and tool calls across connectors, knowledge, MCP, and connected agents. {S182}

[confirmed Q4] Despite the name, no customer data goes to the GitHub Copilot service when that harness runs in Copilot Studio. {S182}

[confirmed Q4] The standard harness covers two of the three MCP primitives, tools and resources, and only with generative orchestration turned on {S173} (page dated 2026-08-26). Doc: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp

[confirmed Q4] Remote MCP servers must use the Streamable transport, SSE having been dropped after August 2025, and the onboarding wizard offers no auth, an API key, or OAuth 2.0 with dynamic discovery, dynamic registration, or manual setup {S180} (page dated 2026-10-30).

[unverified Q4] GA or preview status of Copilot Studio MCP: neither fetched page carries a preview label, but I retrieved no explicit GA statement. Next check: fetch the Copilot Studio "What's new" page and the Power Platform release plan.

[confirmed Q4] A governance hook exists: MCP connections ride on Power Platform connectors, so a data policy that restricts connectors also restricts the MCP server and its tools. {S180}

[confirmed Q4] Tool definitions are not pinned: server-side changes flow into the agent automatically, and responsibility for non-Microsoft servers rests with the customer. {S173}

[inference Q4] That auto-refresh behavior is the precondition for the rug-pull risk in Q9, so third-party MCP servers on this surface need an allowlist and change monitoring.

[confirmed Q4] Tenant-level MCP control lives in the Microsoft 365 admin center Tools registry (Agents > Tools), where admins see Microsoft-hosted and approved custom servers and, for supported servers, control individual tools {S177} (page dated 2026-10-08).

[confirmed Q4] Microsoft-hosted MCP status is split three ways. Work IQ MCP is generally available as part of the Work IQ API. {S177} Its Copilot Studio integration is preview and tied to the GitHub Copilot harness. {S177} The per-workload servers (SharePoint, OneDrive, Mail, Teams, and others) are preview, kept for backward compatibility, and flagged as unfit for production or new projects. {S177}

[confirmed Q4] A capacity pack costs $200.00 per month for 25,000 Copilot Credits, licensed tenant-wide {S175}, and unused credits expire monthly {S184}.

[unverified Q4] The pay-as-you-go price per Copilot Credit could not be read from the primary page: the Azure pricing page rendered the price cell as `$-` when fetched. {S183} Secondary sources give $0.01. {S201} Next check: open https://azure.microsoft.com/en-us/pricing/details/copilot-studio/ in a browser, or read the Licensing Guide PDF.

[confirmed Q4] Standard-harness rates (page dated 2026-10-30) are 1 credit per classic answer, 2 per generative answer, 5 per agent action, 10 per tenant-graph-grounded message, 13 per 100 agent flow actions, and 10 per 1,000 tokens when a reasoning model orchestrates. {S187}

[confirmed Q4] Seat holders ride free in interactive use: when an agent runs under a Microsoft 365 Copilot user's authenticated identity in Copilot Chat, Teams, or SharePoint, those rates show no charge, within fair-use limits. {S184} {S187}

[confirmed Q4] Autonomous runs are the exception: agent flows started by an event trigger or another flow burn credits at the standard rate even in a fully licensed tenant. {S187}

[confirmed Q4] GitHub Copilot harness agents need Copilot Credits even for Microsoft 365 Copilot seat holders {S175}, and they follow a different billing scheme from the table above {S187}.

[unverified Q4] Credit rates for the GitHub Copilot harness were not retrieved. Next check: fetch https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-overview.

[confirmed Q4] Capacity has a hard stop: at 125% of prepaid capacity an environment's agents stop responding, mid-conversation included, unless a pay-as-you-go plan absorbs the overage. {S187}

[confirmed Q4] Throughput caps are set per Dataverse environment (page dated 2026-10-27): generative AI messages are limited to 50 per minute and 1,000 per hour with 1 to 10 packs, rising to 100 and 2,000 on pay-as-you-go or for Microsoft 365 Copilot users. {S190}

[confirmed Q4] SharePoint as a Copilot Studio knowledge source ingests Word, PowerPoint, and PDF files, plus Excel on the upload path; Markdown appears on neither list. {S190}

[confirmed Q4] Folder-style navigation fails on that knowledge source: questions that name a file, list a folder's contents, or count files go unanswered. {S190}

[confirmed Q4] The upload path refreshes every four to six hours and holds at most 1,000 files, 50 folders, and 10 subfolder levels per source. {S190} Without a Microsoft 365 Copilot license in the tenant, generative answers use only SharePoint files under 7 MB, against 200 MB with the license and tenant graph grounding. {S190}

[confirmed Q4] Access is per user: every unstructured knowledge source makes each user sign in at runtime, a single shared credential is unsupported, and files labeled confidential or highly confidential on the upload path are skipped without an error. {S190}

[inference Q4] ICM cannot be hosted as "a SharePoint folder added as knowledge" in Copilot Studio. Markdown context files are not indexed, routing by file name fails, and a four to six hour sync lag breaks stage handoff.

[inference Q4] ICM on Copilot Studio means re-expressing the layers: L0 as agent instructions, L2 stages as skills (GitHub Copilot harness) or topics and agent flows (standard harness), L3 as knowledge converted to Word or PDF, and L4 written by connector or MCP tools.

**Teams bots**

[confirmed Q4] The Teams SDK no longer ships its own AI layer: its AI packages and MCP plugin are deprecated, and developers are told to pair Teams activity routing and streaming with an outside model client or agent framework (page dated 2026-10-09).

[confirmed Q4] MCP in a Teams bot is therefore the developer's own MCP client: the documented samples reach remote servers over HTTP, discover tool schemas at runtime, and hand the tools to the agent loop. Doc: https://learn.microsoft.com/en-us/microsoftteams/platform/teams-sdk/in-depth-guides/ai-integrations/build-agent

[confirmed Q4] Model choice depends on the framework: the TypeScript sample is locked to the OpenAI chat-completions protocol {S189}, while the Python sample uses Microsoft Agent Framework, described as multi-backend {S189}.

[unverified Q4] Lead: a Learn search result says Microsoft Agent Framework can build agents on Claude. {S202} Next check: fetch https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/model-providers/anthropic and run a Claude-backed Teams sample.

[confirmed Q4] State is the developer's job too: a run starts with no history by default, and production bots are pointed to an external store such as Redis or Cosmos DB. {S189}

[inference Q4] A Teams bot is a chat front door for a custom agent runtime. Every ICM layer and every control (logging, approvals, least privilege) lives in Nihilo's code and hosting, so platform seat cost is lowest and build effort is highest of the four surfaces.

**SharePoint and OneDrive-synced folders**

[confirmed Q4] SharePoint supports 50,000 unique permission scopes per list or library, with 5,000 as the recommended ceiling {S179} (page dated 2026-10-06). Version history allows 50,000 major and 511 minor versions. {S179} Sync performance guidance tops out at 300,000 files, and a full decoded path may not exceed 400 characters. {S179}

[confirmed Q4] Once a list, library, or folder holds more than 100,000 items, inheritance can no longer be broken at that level, though individual items inside still can. {S179}

[corrected Q4] The brief says SharePoint could not give fine-grained security control. Microsoft Graph documents app permissions narrower than a site: Selected scopes exist for a single list, list item, folder, or file, in delegated and application modes, with read, write, owner, or fullcontrol roles {S178} (overview dated 2024-11-07, older than six months, so treat as suspect until tested).

[corrected Q4] A secondary blog updated 2025-10-28 reported the list-level permission endpoints as beta only. {S203} The current Graph reference (dated 2026-06-05) shows the listItem permission call under v1.0. {S186}

[confirmed Q4] Selected scopes start at zero access: consent in Entra ID grants nothing until someone adds an explicit permission on the specific site, list, item, or file. {S178}

[confirmed Q4] Each list, folder, or file grant to an app breaks inheritance on that resource, so it draws down the unique-permission budget above. {S178}

[confirmed Q4] In delegated mode the effective access is the overlap of the app's grant and the signed-in user's rights {S178}; app-only tokens have no user in the loop and are rated higher risk {S178}.

[corrected Q4] The brief says SharePoint could not be reached through MCP. Work IQ MCP now allows /sites/ resource paths and can fetch binary file content {S188}, and a preview SharePoint MCP server also exists {S177}, though it is marked legacy.

[confirmed Q4] Work IQ MCP acts as the signed-in user: calls carry that user's Microsoft 365 permissions under Entra authentication, and a tenant policy layer blocks create, update, delete, and action calls until an admin enables them {S188} (page dated 2026-10-26).

[confirmed Q4] File reads through Work IQ MCP default to a 4 MB raw-file cap, configurable per path {S188}, and its retrieve search tool is still in public preview {S188}.

[unverified Q4] Lead: the Work IQ API overview excerpt says application-only authentication is unsupported and usage is paid in Copilot Credits. {S204} If so, unattended scheduled ICM runs cannot use Work IQ MCP and need a Graph app registration with Selected scopes. Next check: fetch https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/api-overview.

[corrected Q4] The brief says other applications could not connect to SharePoint. Copilot Studio's plan comparison lists prebuilt, premium, and custom Power Platform connectors {S175}, and the Graph Selected permissions above give any registered app scoped SharePoint access.

[unverified Q4] Lead: the Agent 365 CLI route for registering your own remote MCP server is preview and names Claude Code among supported clients, alongside Copilot Studio, Visual Studio Code, and GitHub Copilot CLI; declarative agents are excluded. {S205} Whether Claude Code or the Claude desktop app can connect to Work IQ MCP directly was not found. Next check: fetch https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/build-reuse-mcp-servers and test from Claude Code.

[inference Q4] A SharePoint or OneDrive-synced folder can hold every ICM layer as files, with versioning and per-folder permissions, but it is storage, not a runtime. A non-technical user still needs an agent surface on top.

[inference Q4] Scoping an agent to one department is cleanest at the site or library boundary (Sites.Selected or Lists.SelectedOperations.Selected), because folder and file grants each consume a unique permission scope.

**Governance add-on cost**

[unverified Q4] Lead: a Microsoft Tech Community post excerpt prices Microsoft Agent 365 at $15 per user per month standalone. {S206} Next check: fetch https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295 and the official pricing page.

### Answer summary

**Q4, Microsoft surfaces.** No Microsoft surface runs an ICM folder workspace as published. Each one forces the layers to be re-expressed or the runtime to be built. Setup effort and fit ratings below are [inference].

| Surface | ICM layers it can represent [inference] | MCP | Admin and security controls | Cost | Setup effort | Fit: 5 people | Fit: 5,000 people |
|---|---|---|---|---|---|---|---|
| Microsoft 365 Copilot (declarative agents, Copilot Cowork) | L0 in instructions, L3 as knowledge; L1, L2, L4 weak. Cowork skills may cover L2 (lead only) | Only as plugin actions inside declarative agents {S185}; no preview label, GA unverified | Logging, retention, eDiscovery, Purview {S176}; write confirmations {S185} | $30.00 per user per month {S175}, or $21.00 Business add-on {S176}; Cowork metered | Low | Good if already on Microsoft 365 | Good for reach, but seat cost is high and ICM fidelity is low |
| Copilot Studio agents | L0 as instructions, L2 as skills or topics and flows, L3 as converted knowledge, L4 via tools | Tools and resources {S173}, Streamable transport only {S180}; GA unverified | Data policies cover MCP {S180}; Tools registry {S177}; model and region switches | $200.00 per 25,000 credits {S175}; pay-as-you-go rate unverified; no charge for seat holders in interactive use {S184} | Medium | Workable on pay-as-you-go; low-code skill still needed | Strongest Microsoft-native option for governance; watch credit burn with Claude Opus |
| Teams bots | All layers, but only as Nihilo builds them | Developer wires an MCP client directly {S189} | Whatever the custom runtime implements | Hosting and model costs only (not researched) | High | Poor unless reused across clients | Good as the front door to a custom runtime |
| SharePoint or OneDrive-synced folders | All layers as files; no runtime | Work IQ MCP is GA {S177}; per-workload SharePoint server is preview and legacy | Graph Selected scopes down to folder or file {S178}; 5,000 recommended unique scopes {S179} | Included in Microsoft 365 plans; Work IQ API metered | Low for storage | Good as the file store | Good as the file store if scoped by site or library |

**Claude in Copilot Studio and Foundry.** Copilot Studio offers Claude Sonnet 4.6 and Claude Opus 4.6 to 4.8 as GA primary models under Microsoft's terms, with Anthropic as subprocessor. They are cross-geo outside the US, off by default in the EU, EFTA, and UK, and absent from GCC High and DoD. Foundry model deployments of Claude need Azure Marketplace terms and a non-CSP paid subscription. Foundry Agent Service support for Claude is unverified.

**SharePoint limits relevant to ICM.** Permission granularity reaches folder and file level. The practical ceiling is 5,000 unique scopes per library (50,000 supported). Versioning is deep (50,000 major versions). Sync guidance tops out at 300,000 files.

**The failed trial claims.** All three are out of date on paper. SharePoint can give an app per-list, per-folder, or per-file access through Graph Selected scopes. It can be reached through MCP (Work IQ MCP, GA). Other applications can connect through Graph and Power Platform connectors. Three caveats [inference]:
* Microsoft's MCP path acts as the signed-in user, not as a narrowly scoped agent identity.
* Copilot Studio's SharePoint knowledge source ignores Markdown and cannot navigate folders.
* None of this has been tested hands-on yet.

### Coverage checklist

* **Four surfaces: layers, MCP, controls, cost, setup effort, fit.** Partly covered. Layers, setup effort, and fit are inference. Still open: explicit GA statements for MCP in Copilot Studio and declarative agents; the pay-as-you-go credit rate; GitHub Copilot harness billing. Declarative agent limits and Copilot Cowork rest on search-result leads. Teams bot hosting cost and Teams admin policies were not researched.
* **Whether Copilot Studio or Foundry agents can use Claude, and on what terms.** Copilot Studio: covered. Foundry model access and terms: covered. Foundry Agent Service with Claude: not covered; sources conflict and WP-Q04C owns it.
* **SharePoint limits relevant to ICM.** Covered for permission granularity, unique-scope limits, versioning, and sync from the primary limits page. Deeper sync behavior belongs to WP-Q07 and the permission model to WP-Q10.
* **Test the failed trial claims against current docs.** Covered on paper: all three corrected with caveats. The Graph Selected overview page is two years old, and no hands-on test was run.

### Open questions

* **GA status of MCP in Copilot Studio.** Next check: fetch https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new and search the Power Platform release plan for "Model Context Protocol".
* **GA status of MCP plugins in declarative agents.** Next check: fetch https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new.
* **Pay-as-you-go price per Copilot Credit.** Next check: load the Azure pricing page in a browser with region set to East US, or read the Licensing Guide PDF.
* **GitHub Copilot harness.** Which models can it use (Claude or not), and what are its credit rates? Next check: fetch the billing-credit-overview and skills-overview pages under /microsoft-copilot-studio/agents-experience/.
* **Claude Sonnet 5 and the reasoning-model surcharge.** Next check: open the model picker in Nihilo's tenant and run one test message per model with consumption reporting on.
* **Foundry Agent Service with Claude.** Next check: WP-Q04C to fetch the Agent Service model support page and try creating an agent on a Claude deployment.
* **Nihilo's Azure subscription type.** CSP subscriptions cannot deploy Claude in Foundry. Next check: the engineer confirms the offer type of both subscriptions in Cost Management.
* **Work IQ MCP for unattended runs and non-Microsoft clients.** Next check: fetch the Work IQ API overview and permissions pages, then try connecting Claude Code to the Work IQ MCP endpoint in Nihilo's tenant.
* **Does Work IQ MCP honor Selected scopes for a custom app registration, or only the user's full permissions?** Next check: register an app with Lists.SelectedOperations.Selected, grant one library, and call `fetch` on a path outside it.
* **Copilot Cowork as an ICM host.** Next check: fetch the Cowork overview and use-cowork pages, then build a two-stage workspace with `SKILL.md` files in OneDrive and check whether stage 01 output reaches stage 02.
* **Declarative agent limits and licensing** (8,000-character instructions, instruction-offloading warning, per-user license for SharePoint knowledge). Next check: fetch the declarative-agent-instructions and knowledge-sources pages.
* **Scopes behind Copilot Studio's SharePoint knowledge.** A search-result lead mentions delegated Sites.Read.All and Files.Read.All. Next check: fetch https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-unstructured-data.
* **Microsoft Agent 365 price and prerequisites.** Next check: fetch the Tech Community GA post and the official pricing page.
* **Teams bot running cost and admin controls.** Next check: Azure Bot Service pricing page and Teams app permission policy docs, or hand to WP-Q04C.

## Sources attached by the API

- S26: Claude in Microsoft Foundry https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- S37: Claude models from Anthropic in Microsoft Online Services https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
- S55: Deploy and use Claude models in Microsoft Foundry - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude
- S173: Extend your agent with Model Context Protocol - Microsoft Copilot Studio https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
- S175: Microsoft Copilot Studio Plans and Pricing https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
- S176: Microsoft Copilot Plans and Pricing—AI for Business | Microsoft 365 https://www.microsoft.com/en-us/microsoft-365-copilot/pricing
- S177: Understand MCP server options in Agent 365 https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview
- S178: Overview of Selected Permissions in OneDrive and SharePoint - Microsoft Graph https://learn.microsoft.com/en-us/graph/permissions-selected-overview
- S179: SharePoint limits - Service Descriptions https://learn.microsoft.com/en-us/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits
- S180: Connect your agent to an existing Model Context Protocol (MCP) server - Microsoft Copilot Studio https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
- S181: Select a primary AI model for your agent - Microsoft Copilot Studio https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
- S182: Harnesses in Copilot Studio - Microsoft Copilot Studio https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview#standard-harness
- S183: Copilot Studio | Pay as you go pricing https://azure.microsoft.com/en-us/pricing/details/copilot-studio/
- S184: Standard harness licensing - Microsoft Copilot Studio https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
- S185: MCP and API plugins for declarative agents https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-plugins
- S186: Create permission on a listItem - Microsoft Graph v1.0 https://learn.microsoft.com/en-us/graph/api/listitem-post-permissions
- S187: Billing rates and management - Microsoft Copilot Studio https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management#copilot-credits-billing-rates
- S188: Work IQ MCP tool reference https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/tool-reference
- S189: Build an agent in Teams https://learn.microsoft.com/en-us/microsoftteams/platform/teams-sdk/in-depth-guides/ai-integrations/build-agent
- S190: Quotas and limits - Microsoft Copilot Studio https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas
- S191: What's new in Copilot Studio - Microsoft Copilot Studio https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- S192: use foundry models claude https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/use-foundry-models-claude
- S193: Claude models in Microsoft Foundry - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models
- S194: Can Claude models be used with Foundry Agent Service's create_agent API (threads/runs pattern) for portal visibility? - Microsoft Q&A https://learn.microsoft.com/en-us/answers/questions/5861158/can-claude-models-be-used-with-foundry-agent-servi
- S195: Microsoft 365 Copilot MCP Agents Reach Government Clouds: GCC, GCC High and DoD Limits https://windowsforum.com/news/microsoft-365-copilot-mcp-agents-reach-government-clouds-gcc-gcc-high-and-dod-limits.451766/
- S196: Write effective instructions for declarative agents https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-instructions
- S197: Add knowledge sources to your declarative agent https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/knowledge-sources
- S198: Use Copilot Cowork https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork
- S199: Copilot Cowork common questions https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
- S200: Copilot Cowork overview https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
- S201: Copilot Studio Pricing in 2026: What Credits Actually Cost https://coworker.ai/blog/copilot-studio-pricing
- S202: Anthropic https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/model-providers/anthropic
- S203: Microsoft Graph SelectedOperations Permissions to SharePoint - Vladilen https://vladilen.com/software/selected-permissions-in-sharepoint/
- S204: Microsoft Work IQ API https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/api-overview
- S205: Build or Reuse MCP Servers for a Microsoft 365 Copilot Plugin https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/build-reuse-mcp-servers
- S206: Microsoft 365 E7 and Agent 365 are now generally available https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295

_153 search results consulted; 36 sources cited._
