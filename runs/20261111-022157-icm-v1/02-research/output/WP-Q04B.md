<!-- {"wp": "WP-Q04B", "models": ["claude-fable-5-2"], "fallbacks": 0, "stop_reason": "end_turn", "cost_usd": 2.186, "searches": 11, "fetches": 17} -->
# WP-Q04B: Q4, Anthropic surfaces

### Findings

All sources were retrieved on 2026-11-11. Page dates are given where the page shows one. `claude.com/pricing` shows no date.

**Seat prices and plan terms**

[confirmed Q4] Anthropic's pricing page lists two Team seat types for teams of 2 to 150: Standard at $20 per seat per month on annual billing ($25 monthly) and Premium at $100 ($125 monthly). The Team plan support article, marked as updated the day before access, repeats the same four prices for US customers, before tax. {S157}

[confirmed Q4] The same page prices Enterprise at US$20 per seat per month, billed annually with a 20 seat minimum, plus usage at API rates.

[confirmed Q4] Budgeting for Enterprise means forecasting consumption, because the seat fee buys access only and chat, Claude Code, and Cowork tokens are all billed at standard API rates with no included allowance. Cost control comes from spend limits that admins set per organization and per user. {S167} The article is dated September 1, 2026.

[confirmed Q4] Seat minimums depend on the purchase path: 20 for self-serve and 50 for sales-assisted, at the same seat price and feature set.

[confirmed Q4] List price is a ceiling for large deals: sales can negotiate volume and committed-spend discounts, and the rates are unpublished.

[confirmed Q4] No surface in this package carries its own fee: a Team seat, or the single Enterprise seat on new and self-serve plans, already includes Claude Code. {S171} Web, desktop, mobile, and Cowork access ride on the same Enterprise seat. {S167} No extra license is needed for Cursor, other VS Code forks, or JetBrains IDEs. {S171}

[corrected Q4] Some secondary sources say only Premium Team seats include Claude Code (one comparison site describes Premium seats as the ones that add Claude Code {S172}). Anthropic's own article contradicts this, describing Claude Code as part of every Team seat and extra usage as the only Premium difference.

[confirmed Q4] Team usage allowances scale off the Pro plan: 1.25x per session on Standard seats and 6.25x on Premium, each with a weekly cap. Limits are tracked per member, not pooled across the team. {S157}

[confirmed Q4] A pooled monthly API credit of up to $500 comes with Team. {S156} Claude Code and the Claude apps are excluded from those credits, which leaves them useful only for API-based builds. {S171}

[estimate Q4] A 5-person firm on Team pays 5 x $20 = $100 per month on annual billing, or 5 x $25 = $125 on monthly billing, for Standard seats (Standard seat list prices).

[estimate Q4] A 5-person firm that wants Enterprise-only controls must buy the 20-seat minimum: 20 x $20 = $400 per month, plus usage (Enterprise seat price and minimum {S156}).

[estimate Q4] A 5,000-person company pays 5,000 x $20 = $100,000 per month in list seat fees, before usage and before any negotiated discount (Enterprise list price). Team is not an option at that size because it stops at 150 seats. {S157}

**Admin and security controls by plan**

[confirmed Q4] The plan comparison table gives both Team and Enterprise SSO, domain verification, central billing, admin controls for remote and local connectors, managed deployment of the desktop app, usage analytics, organization-wide skills deployment, and organization instructions. {S156}

[confirmed Q4] Enterprise alone gets domain capture, role-based access, SCIM, audit logs, the Compliance API, custom data retention, a HIPAA-ready option, and inference hooks in that table. {S156} The Enterprise card adds network-level access control and IP allowlisting. {S156}

[unverified Q4] Anthropic's two pages disagree on Team identity features. The Team plan support article credits Team with domain capture, JIT provisioning, and role-based permissioning. {S157} The pricing comparison table marks domain capture and role-based access as absent on Team. {S156} The custom roles article also limits custom roles to Enterprise. {S165} I treat the pricing table as more authoritative because it is the plan-by-plan source, but that is a judgment. Next check: open Organization settings in Nihilo's own Claude Team plan and look for a Roles page and a domain capture setting.

[confirmed Q4] Model training is not a data-use concern on business plans: the Claude Code admin docs exclude Team, Enterprise, API, and cloud provider traffic from it. {S159}

[confirmed Q4] Three further Enterprise-only data controls matter for regulated buyers: customer-managed encryption keys, US-only inference, and a HIPAA-ready configuration with a BAA.

[confirmed Q4] Enterprise is the only plan with custom roles, which decide which capabilities (chat, Cowork, Claude Code, web search) and which connectors a member can use. {S165} Roles attach to groups, and a member in several groups gets the union of grants. {S165}

[confirmed Q4] A role can be as fine-grained as a single tool on a connector, with three settings: always allow, needs approval, or blocked. Admins can set a hard ceiling for all roles with the organization-wide tool policy, because the tighter setting always prevails.

[confirmed Q4] Because Anthropic's servers do the enforcing, a blocked tool stays blocked in web and desktop chat, Cowork, and Claude Code alike. Two gaps remain in role-based connector control: connectors a member runs on their own machine, and Cowork deployed on a third-party platform.

**Chat with Projects, skills, and connectors (Team and Enterprise)**

[confirmed Q4] Company-wide standing instructions are limited to one 3,000-character block that an Owner writes and that applies to every conversation. {S163} Ordinary members cannot see the text, and a conflicting personal instruction loses to it. {S163} This is guidance to the model, not enforcement: Anthropic flags that contradictory instructions can produce varying behavior. {S163} The article is dated August 31, 2026.

[confirmed Q4] A project bundles its own chats, an uploaded knowledge base, and a project instruction field. {S160} Large reference sets are handled by automatic retrieval (RAG) on paid plans, which Anthropic says raises capacity up to 10x. {S160}

[confirmed Q4] Team and Enterprise members share projects at two levels: view (read and chat) or edit (change instructions, knowledge, and membership). {S160} Project sharing is an owner-controlled toggle, with per-role granularity reserved for Enterprise. {S160}

[confirmed Q4] A redesigned projects feature is in beta, starting in Claude Code on Pro, Max, and Ultra, with Team and Enterprise scheduled to follow. {S160}

[confirmed Q4] A zip upload containing a SKILL.md file is how owners on Team and Enterprise push a skill to everyone. {S166} Code execution is a hard dependency for skills. {S166} Claude Code picks up the same provisioned skills when a user signs in with the organization's Claude account. {S166}

[confirmed Q4] Department-specific skills need Enterprise, because the only scoping mechanism is a plugin assigned to a group. {S166} Malicious-content scanning of uploaded skills is also an Enterprise-only switch.

[confirmed Q4] Change control for user-built skills is available: under the review-required policy nothing reaches the organization library, including updates, without owner approval of that exact version. {S166} The inventory keeps a version history per item. {S166}

[confirmed Q4] Every plan, including Team and Enterprise, can attach remote MCP servers as custom connectors in chat, Cowork, and Claude Desktop. {S161} Adding a connector is an owner-level act (plus Libraries-manage custom roles on Enterprise), after which members must each connect with their own account. {S161}

[confirmed Q4] Public internet exposure to Anthropic's IP ranges is a precondition for any custom connector, since the calls originate in Anthropic's cloud even for desktop users. {S161} Private-network hosting therefore only works with a firewall allowlist for those ranges. {S161}

[confirmed Q4] Authentication options are OAuth sign-in or fixed request headers such as an API key. {S161} A fixed credential is shared by all members who use the connector, which makes a narrowly scoped key essential. {S161}

[confirmed Q4] Anthropic's own guidance names hidden instructions from malicious servers and unannounced tool changes as risks of custom connectors. {S161}

[confirmed Q4] Cowork and claude.ai cannot see local MCP servers from `claude_desktop_config.json`, which Anthropic describes as a different mechanism from custom connectors. {S161}

**Claude desktop app and Cowork**

[confirmed Q4] Anthropic positions Cowork as Claude Code's agentic architecture without the terminal, sold on all paid plans through Claude Desktop for macOS, Windows, and Linux (beta). {S168}

[confirmed Q4] Local folders the user connects are the boundary of Cowork's file reach on desktop, with read and write access inside them. {S168}

[confirmed Q4] Two instruction levels exist in Cowork: global instructions for every session, and folder instructions that apply when a local folder is selected. {S168} Folder instructions are writable by the agent itself mid-session, per the same article. {S168}

[unverified Q4] The fetched Cowork articles do not say which file holds folder instructions. They also do not say whether Cowork auto-loads a `CLAUDE.md` or `CONTEXT.md` from a connected folder. Next check: connect an ICM workspace folder in Cowork on Nihilo's Team plan, ask Claude which instruction files it loaded, and read `claude.com/docs/cowork/overview`.

[confirmed Q4] Per-project files, instructions, and memory are available in Cowork, along with sub-agent coordination for parallel work. {S168} Recurring runs do not depend on a user's laptop, because Cowork schedules execute cloud-side. {S168}

[confirmed Q4] Two execution locations are offered to Team and Enterprise: Anthropic's infrastructure, or the member's own computer with code confined to a virtual machine. {S162} Cloud execution defaults to on for Team and off for Enterprise. {S162}

[confirmed Q4] Per-task human approval is the default for any connector tool that can write, and only an owner-level organization setting lifts it. Owners can also remove the automatic approval mode from members' mode selector entirely. {S162}

[confirmed Q4] Project creation in Cowork is ungoverned at the organization level today. {S162} Collaboration is limited to sharing individual artifacts, since a Cowork session itself has no sharing feature. {S168}

[confirmed Q4] A Team customer has no central way to manage or delete the history of local Cowork sessions, which lives on each laptop; retrieval through the Compliance API is an Enterprise capability. Audit log and Compliance API depth belongs to WP-Q12.

[confirmed Q4] Skills, connectors, and sub-agents can travel together in a single plugin. {S168} A required setting in the owner-run plugin marketplace force-installs a plugin for all members and blocks removal. Per-group targeting is Enterprise-only. {S162}

[confirmed Q4] System policies are the control channel for Claude Desktop on both plans, deployed as MDM configuration profiles on macOS and Group Policy or Intune on Windows. Policy keys can restrict which folders Cowork may mount and disable local MCP servers and desktop extensions. {S164} Another key forces sign-in to a named organization.

[confirmed Q4] An MDM tool is optional on Enterprise, where a beta section of Organization settings exposes several of the same controls. {S164}

[confirmed Q4] The read-only folder flag is not a hard write barrier: Anthropic notes that shell commands, MCP servers, and hooks in the Code tab bypass it.

[confirmed Q4] Business plans cannot use the desktop app's screen-control feature (computer use), which remains a Pro and Max research preview.

[confirmed Q4] BAA coverage for Cowork is conditional on a HIPAA configuration that the Primary Owner must apply to local mode. Cloud-run Cowork is lost once that configuration is on. {S162} PHI work in the IDE extensions is ruled out, because VS Code and JetBrains sit outside the BAA even with that configuration. {S171}

**Claude Code in the desktop app or an IDE**

[confirmed Q4] A non-terminal user reaches Claude Code through the Code tab of Claude Desktop, choosing environment, project folder, permission mode, and model from on-screen controls. {S158} Anthropic recommends this route for Team and Enterprise members because nothing else needs installing.

[confirmed Q4] An ICM workspace launched at its root gets only root-and-above `CLAUDE.md` content up front, with subfolder `CLAUDE.md` files deferred until the agent first reads something in that subfolder. {S170} No override logic exists between levels: every discovered file is appended to context. {S170}

[confirmed Q4] Hard guarantees need hooks or settings, since Anthropic classes `CLAUDE.md` content as context that the model may not follow strictly. {S170}

[confirmed Q4] A workspace configured for the CLI needs no second configuration for the desktop app, which uses the same settings files. {S158} Project `CLAUDE.md` files and MCP servers from `~/.claude.json` or `.mcp.json` carry over too. {S158} That second citation is a search extract of the same docs page; my full fetch was cut off before that section.

[confirmed Q4] The `@path` import syntax lets a `CLAUDE.md` force other files into context at launch, nested up to four hops. {S170}

[confirmed Q4] Long ICM runs carry a context risk: compaction restores the root `CLAUDE.md` but drops nested ones until the agent touches their folder again.

[confirmed Q4] Company-wide instructions are possible through a managed-policy `CLAUDE.md` that user settings cannot switch off. {S170} Admins who prefer one artifact can inline that text in managed settings under the `claudeMd` key. {S170}

[confirmed Q4] Three delivery channels exist for Claude Code's managed settings (the Claude admin console, MDM, or a file on disk), and the result outranks anything a user or project sets. {S159} Only Team and Enterprise customers get the console channel. {S159}

[confirmed Q4] An admin can use managed settings to allowlist MCP servers, limit hooks and plugin marketplaces, sandbox execution, and refuse skills or MCP servers that originate in user or project folders. {S159}

[confirmed Q4] Permission modes in the Code tab range from Manual, with a diff to accept or reject per change, to Auto, where a classifier screens actions. Users on business plans cannot self-enable the bypass mode, and the available mode list is itself an admin-restrictable setting. {S158}

[confirmed Q4] MCP reaches the Code tab two ways: connectors with a graphical setup flow, and MCP servers added through settings files. {S158}

[unverified Q4] It is unclear which control governs connectors inside desktop Code tab sessions. A search extract of the desktop docs says no MCP setting or `managed-mcp.json` reaches the claude.ai connectors that the desktop app hands to local and SSH sessions. {S158} The custom roles article says role-based connector permissions are enforced in Claude Code and combine with managed settings on a most-restrictive basis. I could not read the full section, and I did not test it. Next check: fetch the "How connectors reach Claude Code" section of `code.claude.com/docs/en/mcp`, then test a blocked connector on a managed device.

[confirmed Q4] IDE users get a graphical Claude Code panel through the VS Code extension, which signs in with any paid Claude subscription or a Console account. {S169} Allowed commands, hooks, and MCP servers come from the same `~/.claude/settings.json` the CLI uses.

[confirmed Q4] A `/mcp` dialog in the VS Code panel handles adding, removing, and authenticating MCP servers. Only a subset of CLI commands and skills is available in the panel. {S169}

**ICM layer mapping and fit**

[inference Q4] Claude Code (Code tab or IDE) represents all five ICM layers, because it works directly on the workspace folder. Only L0 (`CLAUDE.md`) loads automatically. The L1 and L2 `CONTEXT.md` files are ordinary files that the agent opens when `CLAUDE.md` routes it there, unless they are pulled in with `@path` imports. This builds on the `CLAUDE.md` loading findings above and on B3 and B4 as stated in the brief.

[inference Q4] Cowork on desktop with a connected local folder is the closest non-terminal match. It can hold the real folder (L1 to L4), with folder instructions standing in for L0. How faithfully it loads L0 is unverified (see above), and the agent can rewrite folder instructions, which weakens L0 integrity.

[inference Q4] Chat with Projects only approximates ICM. Organization instructions act as a company L0, project instructions as L0 and L1, skills as L2 stage contracts and L3 reference, project knowledge as L3, and chat outputs as L4. There are no numbered stage folders, no `output/` handoff, and no file diff review between stages.

[inference Q4] Setup effort rises in this order: chat with Projects (owner creates a project, uploads reference files, provisions skills), then Cowork (desktop install, folder access, device policy for larger fleets), then Claude Code (workspace folder, managed settings, MCP configuration, user training on permission modes).

[inference Q4] A 5-person firm lands on Team and gets SSO, connector admin, organization skills, and organization instructions. Per the pricing table it gets no audit logs, SCIM, role-based access, or Compliance API. Nihilo's audit-trail promise to small firms therefore has to come from elsewhere, such as Git history on the workspace or its own logging. One native option on Team is OpenTelemetry streaming of Cowork events, which Anthropic says does not replace audit logging.

[inference Q4] A 5,000-person company needs Enterprise. Custom roles, per-group plugins, per-tool connector permissions, and device policy give a workable way to separate departments. The ICM folder itself still lives per user or per repo, so shared storage and versioning must come from outside these surfaces (owned by the Q7 package).

### Answer summary

Q4, Anthropic surfaces only. All three surfaces come with the same seat, so there is no per-surface fee. Citations are in the findings above.

- **Team:** $20 per Standard seat per month on annual billing ($25 monthly), $100 per Premium seat ($125 monthly), 2 to 150 seats.
- **Enterprise:** $20 per seat per month billed annually, 20 seat minimum (50 if sales-assisted), plus all usage at API rates.

| | Chat with Projects, skills, connectors | Claude desktop app with Cowork | Claude Code in the Code tab or an IDE |
|---|---|---|---|
| ICM layers | [inference] Approximates L0 to L4 with organization and project instructions, skills, and knowledge; no stage folders or `output/` handoffs | [inference] L1 to L4 as a real connected folder; L0 through folder or global instructions; auto-loading unverified | [inference] All five; only `CLAUDE.md` auto-loads, the rest are files the agent reads |
| MCP | Remote MCP as custom connectors, owner-added, reachable from Anthropic's IP ranges | Same custom connectors; local MCP servers and desktop extensions exist in the desktop app but not in Cowork | Connectors plus MCP servers from settings files; `/mcp` dialog in VS Code |
| Admin and security | Both plans: SSO, connector admin, organization skills and instructions. Enterprise only: custom roles, per-tool connector permissions, SCIM, audit logs, Compliance API | Cowork on/off, cloud on/off, approval settings, required plugins, device policy for folders and local MCP. Local session history stays on laptops | Managed settings (console, MDM, file), managed `CLAUDE.md`, MCP allowlists, hook limits, sandboxing, restricted permission modes |
| Setup effort | [inference] Lowest | [inference] Low to medium | [inference] Medium |
| Fit for 5 people | [inference] Good and cheap on Team, but no native audit logs or role-based access | [inference] Best non-terminal option for a real ICM folder; governance is thin on Team | [inference] Works for the builder and technical staff; too much for most office staff |
| Fit for 5,000 people | [inference] Good on Enterprise for ICM-shaped assistants; not a faithful ICM runtime | [inference] Governable on Enterprise with device policy and roles; per-laptop folders and no session sharing limit it | [inference] Strongest controls; realistic for technical teams, not for all 5,000 staff |

[inference] None of the three surfaces gives non-technical staff a shared, versioned ICM workspace with enterprise audit on the Team plan. Cowork plus an organization plugin is the nearest packaged route.

### Coverage checklist

- **Layers, MCP, admin and security, cost, setup effort, and fit for each of the three surfaces: partly covered.**
  - MCP, admin and security controls, and cost per seat are sourced from Anthropic pages.
  - ICM layer mapping, setup effort, and fit are inference, because no vendor page addresses ICM.
  - Two points are unverified: how Cowork loads instruction files from a connected folder, and which control governs connectors in desktop Code tab sessions.
  - The Claude Code desktop docs page was truncated on fetch, so its enterprise configuration section was read only through search extracts.
  - The JetBrains plugin page was not fetched.
- **Current Team and Enterprise seat prices and admin features from Anthropic's own pages, with access date: covered.**
  - Prices come from `claude.com/pricing` and two support articles, accessed 2026-11-11.
  - One conflict between Anthropic pages on Team identity features is reported as unverified.

### Open questions

- **Team identity features:** does Team include domain capture and role-based permissioning (support article) or not (pricing table)? Next check: inspect Organization settings in Nihilo's Team plan, or ask Anthropic sales.
- **Team context window:** the Team support article says 200k {S157}, while the pricing table says up to 1M depending on model {S156}. Next check: open the context window help link from the pricing page and confirm per model.
- **Cowork and ICM files:** what file stores folder instructions, and does Cowork load `CLAUDE.md` or `CONTEXT.md` from a connected folder? Next check: hands-on test with an ICM workspace on Nihilo's Team plan.
- **Connector governance in Code tab sessions:** do role-based connector permissions and managed MCP settings both apply to connectors that the desktop app passes to Claude Code? Next check: read the full `code.claude.com/docs/en/mcp` section and test on a managed device.
- **New projects beta:** when does it reach Team and Enterprise, and does it change project instructions, sharing, or knowledge? Next check: re-read the "What are projects?" article and the Claude Code projects doc monthly.
- **Real Enterprise cost per seat:** usage at API rates and negotiated discounts are unknown. Next check: ask Anthropic sales for a quote, and run a metered pilot using the spend report.
- **JetBrains parity:** not verified beyond seat coverage. Next check: fetch `https://code.claude.com/docs/en/platforms`.
- **Audit logs, Compliance API, and OpenTelemetry detail:** owned by WP-Q12; the plan-level availability above should be reconciled with that package.

## Sources attached by the API

- S156: Plans & pricing | Claude by Anthropic https://claude.com/pricing
- S157: What is the Team plan? | Claude Help Center https://support.claude.com/en/articles/9266767-what-is-the-team-plan
- S158: Desktop application - Claude Code Docs https://code.claude.com/docs/en/desktop
- S159:  https://code.claude.com/docs/en/admin-setup
- S160: What are projects? | Claude Help Center https://support.claude.com/en/articles/9517075-what-are-projects
- S161: Get started with custom connectors using remote MCP | Claude Help Center https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- S162: Use Claude Cowork on Team and Enterprise plans | Claude Help Center https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
- S163: Set organization instructions | Claude Help Center https://support.claude.com/en/articles/14546867-set-organization-instructions
- S164: Enterprise configuration for Claude Desktop | Claude Help Center https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop
- S165: Manage custom roles on Enterprise plans | Claude Help Center https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans
- S166: Provision and manage skills for your organization | Claude Help Center https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization
- S167: What is the Enterprise plan? | Claude Help Center https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan
- S168: Get started with Claude Cowork | Claude Help Center https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- S169:  https://code.claude.com/docs/en/vs-code
- S170:  https://code.claude.com/docs/en/memory
- S171: Use Claude Code with your Team or Enterprise plan | Claude Help Center https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan
- S172: Claude Teams vs Enterprise (2026): Team Plan Price and Seats https://www.layer3labs.io/comparisons/claude-team-vs-enterprise

_104 search results consulted; 17 sources cited._
