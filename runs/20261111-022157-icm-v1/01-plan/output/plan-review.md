<!-- {"models": ["claude-fable-5-2"], "cost_usd": 0.963} -->
# Stage 01: plan review of the work packages

Run date: 2026-11-11. This stage checks coverage only. Nothing below is evidence. Product names and URLs I suggest are search leads from general knowledge and must be confirmed by the stage 02 workers.

**Summary:** the 23 packages cover every baseline item and every numbered question at headline level. I found one full gap (running cost inputs), eight partial gaps, and five packages too large for one worker.

## 1. Coverage table

| Requirement | Owning package | Notes |
|---|---|---|
| B1 paper identity, license, review status | WP-B1 | Covered. Analysis of what the license permits belongs to WP-Q17. |
| B2 repo and license | WP-B1 | Covered. Same split with WP-Q17. |
| B3 core design | WP-B1 | Covered. |
| B4 five layers | WP-B1 | Covered. |
| B5 evidence base and poor-fit cases | WP-B1 | Covered. |
| B6 community critiques | WP-B1 | Covered. Sources will likely be community level. |
| B7 ecosystem (Eduba, Skool, tools, partner program) | WP-B2 | Covered. |
| B7 trademark checks | WP-Q17 | Covered. |
| B8 "Model Workspace Protocol" | WP-B1 | Covered. Partial GAP: if the name is confirmed, WP-Q17 does not search it as a mark. |
| Q1 latest paper version and repo state | WP-B1 and WP-Q01 | Overlap, see section 3. |
| Q1 changes, follow-ups, tooling, case studies, talks | WP-Q01 | Covered. |
| Q1 independent evidence | WP-Q01 | Covered, with an indirect-evidence fallback. |
| Q2 portability, all sub-bullets | WP-Q02 | Covered. |
| Q3 the eleven named gaps | WP-Q03 | Covered, but too large (section 4). |
| Q3 "every gap", beyond the named list | GAP (partial) | No must_answer line asks for gaps the brief did not name. |
| Q4 Microsoft surfaces | WP-Q04A | Covered. |
| Q4 Claude Team/Enterprise, desktop, Claude Code | WP-Q04B | Covered. |
| Q4 Google Workspace, Slack, custom web app | WP-Q04B | Covered, but the package is too large. |
| Q5 data residency | WP-Q05 | Facts on where Claude is processed sit in WP-Q06A and WP-Q06B. |
| Q5 processor obligations, DPA, BAA | WP-Q05 | Covered. |
| Q5 security review friction | WP-Q05 | Overlaps WP-Q15. |
| Q5 required certifications | WP-Q05 | Overlaps WP-Q13 and WP-Q15. |
| Q5 liability and insurance | WP-Q05 | Overlaps WP-Q15. |
| Q5 operating cost and margin | GAP | No package collects token prices or Azure service prices. |
| Q5 buyout or transfer path | WP-Q05 (partial) | Named, but no angle on tenant-to-tenant transfer mechanics or who owns the deliverables. |
| Q5 regulated buyer reaction | WP-Q05 | Covered. Likely thin evidence. |
| Q6 Azure services and Claude in Foundry | WP-Q06A | Covered. |
| Q6 "Claude and others" (non-Claude models) | GAP (partial) | No package records which non-Claude models each cloud offers. The portability score needs it. |
| Q6 AWS and GCP | WP-Q06B | Covered. Borderline size. |
| Q7 concrete limits | WP-Q07 | Covered. |
| Q7 break points and fix patterns | WP-Q07 | Covered. |
| Q8 Microsoft 365, Google, Salesforce, HubSpot, Dynamics | WP-Q08A | Covered. SharePoint, Outlook, Teams, and Excel are not named one by one. |
| Q8 SAP through mainframe | WP-Q08B | Covered, but too large. |
| Q9 MCP governance, all sub-bullets | WP-Q09 | Covered. |
| Q10 shared versus private layers, leakage, change workflow | WP-Q10 | Covered. |
| Q10 who owns and edits which files | WP-Q10 (partial) | Implied by CODEOWNERS but not a must_answer line. |
| Q11 security, all sub-bullets | WP-Q11 | Covered, including per hosting model. |
| Q12 capture, destinations, retention, immutability, PII, alerting, dashboard | WP-Q12 | Covered. |
| Q12 attributable to a user, replayable | WP-Q12 (partial) | Neither is a must_answer line. |
| Q13 framework mapping | WP-Q13 | Covered, but too large when combined with costs. |
| Q13 first certification, cost, timeline | WP-Q13 | Covered. |
| Q14 comparables and funded programs | WP-Q14 | Covered. |
| Q14 delivery time, standardized versus tailored, buyout price logic | GAP (partial) | Not in must_answer. |
| Q15 requirements, procurement paths, shortest path | WP-Q15 | Covered. |
| Q16 competitors and native coverage | WP-Q16 | Covered. Overlaps WP-Q04A, WP-Q04B, and WP-B2. |
| Q17 licenses, trademarks, attribution | WP-Q17 | Covered. |
| Matrix: usable by non-technical staff | WP-Q04A, WP-Q04B | Covered. |
| Matrix: security and least privilege | WP-Q09, WP-Q10, WP-Q11 | Covered. |
| Matrix: oversight | WP-Q12 | Covered. |
| Matrix: integration reach | WP-Q08A, WP-Q08B | Covered. |
| Matrix: scalability | WP-Q07 | Covered. |
| Matrix: fit for small firms, fit for enterprise | WP-Q04, Q05, Q13, Q14, Q15 | Covered. |
| Matrix: build effort for a part-time team | GAP (partial) | Only "setup effort" per surface in Q4. Nothing on templates or accelerators for the runtime build. |
| Matrix: running cost per client per month | GAP | Same gap as Q5 operating cost. |
| Matrix: compliance evidence, portability | WP-Q12, Q13, Q02, Q06B | Covered. |
| Prototype: Claude in Foundry from Nihilo's own subscriptions | WP-Q06A (partial) | "On what terms" should explicitly include subscription eligibility and default quota. |
| Prototype: SharePoint as test case 2, and the failed trial claims | WP-Q04A, WP-Q08A (partial) | No line tests the brief's claim that SharePoint lacks fine-grained security, MCP, and app connections. |

## 2. Gaps

1. **Running cost inputs (full gap).** No package owns model token prices per cloud or Azure service prices. Q5 margin, the running cost score, and the Q14 pricing basis all depend on them. Fix: new package WP-X1.
2. **Q3 open-ended gaps.** Add a line asking for gaps beyond the named eleven.
3. **Q6 non-Claude models.** Add one line each to WP-Q06A and WP-Q06B.
4. **Q5 buyout mechanics.** Add transfer mechanics and deliverable ownership terms.
5. **Q12 attribution and replay.** Add explicit lines.
6. **Q14 tier details.** Add delivery time, standardized versus tailored, and buyout price comparables.
7. **Q10 file ownership.** Add an explicit line.
8. **Build effort.** Add a line to WP-Q06A on reference implementations and infrastructure templates.
9. **Prototype prerequisites.** Add lines to WP-Q06A (eligibility, quota) and WP-Q04A (test the failed SharePoint trial claims).
10. **MWP trademark.** Add the name to WP-Q17, conditional on WP-B1.

One ambiguity in the brief needs a human call. Step 3 says the architectures draw on "Q5 and Q14", but the architecture facts sit in Q4, Q6, and Q7. I have assumed all five feed step 3.

## 3. Overlaps

If workers run in parallel, they cannot read each other's output. The non-owner should write "see WP-X" and spend no searches on the item.

| Item | Packages touching it | Owner | Others should |
|---|---|---|---|
| Paper version, repo state, license field | WP-B1, WP-Q01, WP-Q17 | WP-B1 | WP-Q01 covers only what changed and outside evidence. WP-Q17 covers only what the licenses permit. |
| Claude in Foundry page (same start URL) | WP-Q02, WP-Q06A, WP-Q04A | WP-Q06A for catalog, regions, terms, feature limits | WP-Q02 reads it only for Claude Code feature behavior. WP-Q04A covers only Claude inside Copilot Studio. |
| Foundry Agent Service | WP-Q04A, WP-Q04B | The custom-runtime package (WP-Q04C if split) | WP-Q04A drops it. |
| Foundry and Bedrock quotas | WP-Q06A, WP-Q06B, WP-Q07 | WP-Q07 | The Q6 packages cover availability only. |
| SharePoint limits | WP-Q04A, WP-Q07, WP-Q10 | WP-Q07 for sync and file limits, WP-Q10 for the permission model | WP-Q04A summarizes surface fit and tests the failed trial claims. |
| Official MCP servers from Microsoft, Google, HubSpot, Slack | WP-Q04A, WP-Q04B, WP-Q08A, WP-Q09 | WP-Q08A for existence and status | The Q4 packages cover whether the surface can use MCP. WP-Q09 covers governance. |
| Claude Enterprise admin controls and audit logs | WP-Q04B, WP-Q09, WP-Q10, WP-Q12, WP-Q16 | WP-Q04B for the feature list and prices | WP-Q12 owns audit log and compliance API detail. The others refer to it. |
| OpenTelemetry GenAI conventions, tracing | WP-Q03, WP-Q12 | WP-Q12 | WP-Q03 names it as the run history solution and defers. |
| Git versioning | WP-Q03, WP-Q06A, WP-Q07, WP-Q10 | WP-Q03 for the pattern | WP-Q06A covers the service choice, WP-Q07 the limits, WP-Q10 the review workflow. |
| Certifications | WP-Q05, WP-Q13, WP-Q15 | WP-Q13 for cost and timeline, WP-Q15 for what buyers demand | WP-Q05 covers only how the need differs by hosting model. |
| Insurance | WP-Q05, WP-Q15 | WP-Q15 for required limits | WP-Q05 covers liability differences by hosting model. |
| Marketplace consulting offers, partner programs | WP-Q14, WP-Q15 | WP-Q14 for listed prices and funding, WP-Q15 for listing and program requirements | Neither repeats the other's fetches. |
| Tool poisoning, prompt injection through connectors | WP-Q09, WP-Q11 | WP-Q09 for MCP-specific classes and CVEs | WP-Q11 maps them to OWASP and ATLAS. |
| Eduba | WP-B2, WP-Q16 | WP-B2 | WP-Q16 refers to it. |

## 4. Suggested edits to `workpackages.yaml`

### Packages too large for one worker

| Package | Why | Proposal |
|---|---|---|
| WP-Q03 | Eleven gaps, each needing a solution plus maturity evidence | Split into state gaps and control gaps |
| WP-Q04B | Eight surfaces or runtimes times six attributes, plus pricing | Move Google, Slack, and custom runtimes to WP-Q04C |
| WP-Q05 | Three models times eight dimensions, plus vendor terms and four regulatory regimes | Split contracts from operating model |
| WP-Q08B | Nine systems plus gateways and RPA | Move on-prem and no-API systems to WP-Q08C |
| WP-Q13 | Five frameworks plus cost research | Split mapping from cost and timeline |

WP-Q06B (two clouds) and WP-Q11 are borderline. I would keep them whole and raise WP-Q06B's caps.

With WP-X1 and the five splits, the plan goes from 23 to 29 workers. The worst-case budget rises from 575 to 725 searches and from 460 to 580 fetches, plus the WP-Q06B cap raise. The cheaper alternative is to keep the packages whole and raise their caps, but answers on the later items will be thinner.

The file defines no field for ownership, so I put deferral notes in `angles`. If your runner accepts a new field, a `defer_to` list would be cleaner.

### New package for cost inputs

```yaml
  - id: WP-X1
    title: Cross-cutting, running cost inputs
    refs: [Q5, Q6, Q14]
    must_answer:
      - Per-token prices for current Claude models on the Anthropic API, Microsoft Foundry, Amazon Bedrock, and Google Cloud, each from the vendor's own pricing page, with access date
      - Batch and prompt caching discounts where the vendor page lists them
      - List prices at small scale for the Azure services named in Q6 and Q12 (Container Apps, Functions, Storage, Key Vault, private endpoints, Service Bus, Log Analytics ingestion and retention, Sentinel)
      - A worked monthly running cost for one small client and one mid-market client, tagged estimate, with run volume assumptions stated
    angles:
      - Vendor pricing pages only, no secondary price aggregators
      - Seat prices are owned by WP-Q04A and WP-Q04B, do not search them here
    start_urls:
      - https://claude.com/pricing  # unconfirmed URL
      - https://azure.microsoft.com/en-us/pricing/details/container-apps/  # unconfirmed URL
      - https://azure.microsoft.com/en-us/pricing/details/monitor/  # unconfirmed URL
```

### Split WP-Q03

```yaml
  - id: WP-Q03A
    title: Q3, state gaps (run history, versioning, memory, rollback, concurrency, multi-user editing)
    refs: [Q3]
    must_answer:
      - For each of run history, versioning, memory, rollback, concurrency, and multi-user editing, the best existing product, open-source tool, or pattern, and its maturity with evidence (GA or preview, release date, adoption signals)
      - Any enterprise gap in this group that the brief did not name
    angles:
      - Git-based versioning for agent workspaces, durable workflow engines (Temporal, Azure Durable Functions)
      - Claude Managed Agents and Claude Agent SDK features for sessions and memory
      - Tracing detail is owned by WP-Q12, name it and write see WP-Q12

  - id: WP-Q03B
    title: Q3, control gaps (access control, secrets, scheduling, error handling, testing and evals)
    refs: [Q3]
    must_answer:
      - For each of access control per layer and stage, secrets handling, scheduling, error handling, and testing and evals, the best existing product, open-source tool, or pattern, and its maturity with evidence
      - Any enterprise gap in this group that the brief did not name (for example cost controls, audit, identity propagation)
    angles:
      - LLM eval tools (promptfoo, Foundry evaluations, Anthropic eval tooling), secrets managers, Agent SDK permissions
      - Cross-department access patterns are owned by WP-Q10
```

### Split WP-Q04B

```yaml
  - id: WP-Q04B
    title: Q4, Anthropic surfaces
    refs: [Q4]
    must_answer:
      - For Claude Team and Enterprise (Projects, skills, connectors, admin controls), the Claude desktop app, and Claude Code via desktop app or IDE, cover which ICM layers each can represent, MCP support, admin and security controls, cost per seat, setup effort, and fit for 5-person versus 5,000-person companies
      - Current Claude Team and Enterprise seat prices and admin features from Anthropic's own pages, with access date
    angles:
      - claude.com pricing, Anthropic support articles on Projects, skills, connectors, admin controls
      - Audit log and compliance API detail is owned by WP-Q12
    start_urls:
      - https://claude.com/pricing  # unconfirmed URL

  - id: WP-Q04C
    title: Q4, Google Workspace, Slack, and custom web app runtimes
    refs: [Q4]
    must_answer:
      - For Google Workspace, Slack, and a custom web app on an agent runtime (Claude Agent SDK, Claude Managed Agents, Foundry Agent Service), cover which ICM layers each can represent, MCP support, admin and security controls, cost per seat or per use, setup effort, and fit for 5-person versus 5,000-person companies
      - For each runtime, GA or preview status and whether it can load a folder-based workspace
    angles:
      - Claude in Slack, Gemini or Google Workspace agent options with MCP
      - Foundry Agent Service docs and pricing, Agent SDK hosting guidance
      - Existence of official MCP servers is owned by WP-Q08A
```

### Split WP-Q05

```yaml
  - id: WP-Q05A
    title: Q5, contracts and vendor terms per hosting model
    refs: [Q5]
    must_answer:
      - For Nihilo-hosted, client-tenant, and hybrid, cover data residency, processor obligations, and the contracts needed (DPA, BAA, subprocessor lists)
      - What Anthropic and Microsoft require of a company that resells or hosts Claude for third parties (commercial terms, BAA availability, data retention, zero data retention eligibility)
      - Who owns deliverables and what a buyout must transfer contractually
    angles:
      - Anthropic commercial terms, DPA, BAA, usage policy for third-party apps
      - Microsoft Products and Services DPA
      - GDPR Article 28 processor obligations, HIPAA business associate rules (HHS)
      - Where Claude is processed per cloud is owned by WP-Q06A and WP-Q06B
    start_urls:
      - https://www.anthropic.com/legal/commercial-terms  # unconfirmed URL
      - https://eur-lex.europa.eu/eli/reg/2016/679/oj  # unconfirmed URL

  - id: WP-Q05B
    title: Q5, operating model, liability, and buyer reaction per hosting model
    refs: [Q5]
    must_answer:
      - For each hosting model, cover security review friction, liability exposure, the technical buyout or transfer path (moving subscriptions or resources between tenants, redeploying from infrastructure as code), and how regulated mid-market buyers (finance, healthcare-adjacent, legal) react
      - Azure Lighthouse and multi-tenant patterns for MSP-style managed services, including what Lighthouse cannot delegate
      - Third-party service provider expectations in financial services (FFIEC, SEC, NYDFS Part 500)
    angles:
      - Azure Lighthouse docs, Azure subscription transfer between Entra tenants
      - Certification cost is owned by WP-Q13B, insurance limits by WP-Q15, running cost by WP-X1
    start_urls:
      - https://learn.microsoft.com/en-us/azure/lighthouse/overview  # unconfirmed URL
```

### Split WP-Q08B

```yaml
  - id: WP-Q08B
    title: Q8, SAP, NetSuite, QuickBooks, ServiceNow, Jira
    refs: [Q8]
    must_answer:
      - Same fields as WP-Q08A for SAP, NetSuite, QuickBooks, ServiceNow, and Jira
    angles:
      - SAP MCP or SAP BTP AI, NetSuite AI connector or MCP, Intuit QuickBooks MCP, ServiceNow MCP, Atlassian remote MCP server

  - id: WP-Q08C
    title: Q8, on-prem databases, file shares, and systems with no API
    refs: [Q8]
    must_answer:
      - Same fields as WP-Q08A for on-prem SQL Server and Oracle, file shares, and mainframe or green-screen systems with no API
      - Gateways for on-prem (on-premises data gateway, Azure Arc, Azure Relay, private link), RPA options (Power Automate desktop), and their auth models
    angles:
      - Microsoft on-premises data gateway, Power Automate desktop terminal emulation, database MCP servers from Microsoft or Oracle
```

### Split WP-Q13

```yaml
  - id: WP-Q13A
    title: Q13, compliance evidence mapping
    refs: [Q13]
    must_answer:
      - Which SOC 2 Trust Services Criteria apply, from AICPA sources, and which ICM artifacts (logs, review gates, version history) serve as evidence
      - NIST AI RMF 1.0 functions and the Generative AI Profile (NIST AI 600-1) actions that logging, review gates, and versioning satisfy
      - ISO/IEC 42001 and ISO/IEC 27001 controls that apply, noting where the standard text could not be read
      - EU AI Act obligations and dates relevant to a deployer or provider of this kind of system, including any changes from the digital omnibus
    start_urls:
      - https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf  # unconfirmed URL
      - https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf  # unconfirmed URL
      - https://eur-lex.europa.eu/eli/reg/2024/1689/oj  # unconfirmed URL

  - id: WP-Q13B
    title: Q13, first certification, cost and timeline
    refs: [Q13]
    must_answer:
      - Realistic first certification or attestation for a two-to-three person firm (SOC 2 Type 1 or Type 2, ISO 27001, ISO 42001), with cited cost and timeline figures, or estimates labeled as such with basis
      - Lower-cost interim proof points buyers accept before an audit (completed questionnaires, self-assessments, a public trust page)
    angles:
      - Published figures from auditors and compliance automation vendors (Vanta, Drata), labeled as vendor marketing
      - What buyers demand is owned by WP-Q15
```

### Lines to add to existing packages

```yaml
# WP-B1, add to angles
      - Owns the paper version, repo state, and license fields. WP-Q01 and WP-Q17 defer here.
# WP-B1, add to start_urls
      - https://github.com/RinDig/Interpretable-Context-Methodology/releases  # unconfirmed URL

# WP-Q01, replace the first must_answer line
      - Every change to the paper and repo since March 2026 (version diffs, releases, commit themes). Current version facts are owned by WP-B1.

# WP-Q02, add to start_urls
      - https://agents.md  # unconfirmed URL

# WP-Q04A, add to must_answer
      - Test the brief's failed trial claims against current docs. Can SharePoint give an agent fine-grained, per-folder access, can it be reached through MCP, and can other applications connect to it
# WP-Q04A, add to angles
      - Microsoft Graph selected-scope permissions for SharePoint sites, lists, and files
      - Foundry Agent Service is owned by WP-Q04C, sync and file limits by WP-Q07

# WP-Q06A, add to must_answer
      - Subscription eligibility, Marketplace prerequisites, and default quota for deploying Claude in Foundry from a small pay-as-you-go tenant
      - Which non-Claude models are available in Foundry for the same agent pattern
      - Microsoft or Anthropic reference implementations, quickstarts, or infrastructure templates that cut build effort for a small team
# WP-Q06A, add to angles
      - Quotas are owned by WP-Q07, prices by WP-X1

# WP-Q06B, add to must_answer
      - Which non-Claude models each cloud offers for the same agent pattern
      - Audit logging and monitoring equivalents in each cloud, one doc link each
# WP-Q06B, add per-package caps
    max_searches: 35
    max_fetches: 28
# WP-Q06B, add to start_urls
      - https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html  # unconfirmed URL

# WP-Q08A, replace the first must_answer line
      - For each system, and for SharePoint, Outlook, Teams, and Excel separately within Microsoft 365, the connection method (official MCP server, vendor API, Microsoft Graph, Power Automate or Logic Apps connector), maturity (GA, preview, community), auth model, and the safest way to grant write access

# WP-Q10, add to must_answer
      - Who owns and who may edit each layer (L0 to L4), and how that ownership is enforced
# WP-Q10, add to start_urls
      - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners  # unconfirmed URL

# WP-Q11, add to angles
      - Check whether OWASP publishes separate guidance for agentic applications or MCP, and use it if current

# WP-Q12, add to must_answer
      - How the end user's identity is carried through the agent to each tool call and log record (attribution)
      - What must be stored to replay a run (model version, prompts, context file versions, tool inputs and outputs) and which tools store it
# WP-Q12, add to start_urls
      - https://opentelemetry.io/docs/specs/semconv/gen-ai/  # unconfirmed URL
      - https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview  # unconfirmed URL

# WP-Q14, add to must_answer
      - Delivery times and the standardized versus tailored split in comparable public offers
      - Public comparables for buyout pricing logic (build-operate-transfer, license buyout, source code transfer fees), or mark unverified
# WP-Q14, add to angles
      - Running cost inputs are owned by WP-X1, partner program requirements by WP-Q15

# WP-Q15, add to start_urls
      - https://sharedassessments.org/sig/  # unconfirmed URL

# WP-Q16, add to angles
      - Seat prices and feature lists for Claude Enterprise and Copilot are owned by WP-Q04A and WP-Q04B. Eduba is owned by WP-B2.

# WP-Q17, add to must_answer
      - If WP-B1 confirms the name, the same searches for "Model Workspace Protocol" and "MWP"
# WP-Q17, add to start_urls
      - https://www.tmdn.org/tmview/  # unconfirmed URL
      - https://euipo.europa.eu/eSearch/  # unconfirmed URL
```

## 5. Risks to the research plan

These are planning assumptions, not findings.

1. **Trademark searches will probably stay unverified.** The USPTO and EUIPO tools are interactive and often not fetchable. Expect manual search steps and plan a human pass.
2. **Independent evidence for ICM may not exist.** WP-Q01 will likely return only indirect evidence, and the report must not let it stand in for direct proof.
3. **Community facts are gated and soft.** The Skool member count and tier prices may sit behind a login, and the B6 critiques may trace only to forum posts.
4. **Prices that are not public.** Enterprise seat prices, Glean pricing, insurance premiums, and audit fees are often quote-only. Expect `unverified` or `estimate` tags, and vendor marketing as the only source for certification costs.
5. **Region and model availability moves monthly.** Anything dated before about 2026-05-11 is suspect under the six-month rule. Workers should record each page's date.
6. **Product names in the brief may be stale.** The brief says "Azure AI Foundry" and the work packages say "Microsoft Foundry". Workers should record the current name as a `corrected` finding rather than search only the old one.
7. **ISO standards are paywalled.** Control-level mapping for ISO/IEC 42001 and 27001 will likely rest on secondary summaries and must be labeled that way.
8. **The EU AI Act timeline is in motion.** Any digital omnibus change needs the official text, not commentary.
9. **Partner and marketplace pages may not fetch.** Partner Center content can require sign-in, and marketplace listings may render client-side.
10. **Legal questions need a lawyer.** Processor obligations, BAA eligibility, liability, and attribution language can be researched but not settled here. The report should carry them to Open questions.
11. **Regulated buyer reaction has no primary source.** Regulator guidance shows what buyers must ask, not how they react. Interviews with two or three target buyers are the real check.
12. **Parallel workers cannot share findings.** The ownership notes in section 3 only work if non-owners defer. Otherwise expect duplicate spend and conflicting answers that stage 03 must reconcile.
13. **Community pages are an injection surface.** Skool, GitHub issues, and marketplace listings are untrusted input. Workers should report any embedded instructions as findings.
14. **Synthesis may creep into research.** WP-Q14 and WP-Q15 ask workers to propose tiers and a path. Those answers should be tagged `inference` so the later stages can revisit them.