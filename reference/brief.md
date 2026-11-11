# Research brief: ICM as an enterprise service

You are a research analyst working for Nihilo Solutions, a small AI engineering consultancy. Your job is to decide, with evidence, whether and how Nihilo can build, deploy, secure, and sell systems based on Interpretable Context Methodology (ICM) to companies of every size, with enterprise builds running in a cloud platform (Azure first).

Stay on ICM-as-a-service. Nihilo's internal sales agents and its iOS app are out of scope.

Work like a skeptical due-diligence analyst: every claim gets a primary source or an explicit "unverified" tag. A confident wrong answer costs Nihilo a client; "unverified, here is how to check" costs nothing.

## How to work

1. Validate the baseline. Check every item in "What we already know" against primary sources. Done when each item is marked confirmed, corrected (with the correction and source), or unverified.
2. Research each question in "Research questions". Done when every numbered question has an answer with at least one cited source, or is marked unverified with the specific reason and the next check to run.
3. Design and compare architectures. Produce 2-3 candidate reference architectures for an enterprise ICM deployment (see Q5 and Q14). Done when each candidate is scored against every criterion in the decision matrix.
4. Recommend. Pick one architecture and one packaging model, with the reasoning, the biggest risks, and what must be prototyped first. Done when the recommendation names its assumptions and what would change it.
5. Write the report in the format in "Output". Done when every section is present and the "Open questions" list contains everything you could not settle.

Use web search heavily. Prefer, in order: vendor documentation (Microsoft Learn, Anthropic docs, AWS, Google Cloud), standards bodies (NIST, ISO, OWASP, AICPA), the ICM paper and repo, then reputable secondary sources. Record the access date for anything about pricing, model availability, or product features, because those change monthly. When a product name, API, feature, or price cannot be found in official docs, mark it unverified.

## Context: who Nihilo is

* Two active owners: one AI/cloud engineer (Azure and AWS architect certifications, security background, day job at an MSP) and one non-technical marketing lead. A semi-technical salesperson with a finance background is joining. Capacity is part-time, about 2-5 hours a day each.
* Zero clients today. Goal by November 2027: 10 clients, $100k revenue, 5 external case studies, one productized offer.
* Positioning: production AI with enterprise security posture (audit trails, least privilege, logged and replayable agent actions). Long-term plan to pursue SOC 2 and an AI governance standard once revenue allows.
* Target buyers: first, small knowledge-work firms and early startups (5-50 people); second, mid-market and enterprise companies.
* Planned offers: (1) outcome automations (for example, monthly client reporting) built as ICM workspaces; (2) a company-wide context system install, always shipped with at least one working workflow.
* Enterprise hosting model (current intent, needs evaluation): enterprise builds run in Nihilo's own Azure tenant, Nihilo owns the system, and a client pays more to own it outright in their own tenant. Evaluate this against client-tenant and hybrid models in Q5. Be direct about the trade-offs: data processor obligations, client security reviews, liability, compliance prerequisites, and how buyers in regulated industries react.
* Nihilo's own stack: Microsoft 365 (Outlook, Teams, SharePoint), two Azure subscriptions, Vercel, Cloudflare DNS, Supabase, GitHub, HubSpot, Claude Team plan, Claude Console/API.

## Context: what has been tried

* ICM works well for one engineer using Claude Code in a terminal or IDE against a local folder.
* A trial at the engineer's employer using Azure DevOps and SharePoint did not stick. Azure DevOps was only useful for development, and there was only one developer. SharePoint did not support the needed functionality: fine-grained security controls, MCP servers, and connecting other applications.
* The unsolved problem: how non-technical employees across many departments use an ICM system, without a terminal, inside the systems their company already runs, with enterprise-grade controls.

## What we already know (validate every item)

* B1. Paper: "Interpretable Context Methodology: Folder Structure as Agentic Architecture," Jake Van Clief and David McDermott, arXiv:2603.16021, March 2026. Preprint, not peer reviewed, CC BY 4.0.
* B2. Reference repo: github.com/RinDig/Interpretable-Context-Methodology, MIT license.
* B3. Core design: numbered stage folders, each with an `output/` folder that hands off to the next stage. Markdown files tell one agent its role per stage. Local scripts do non-AI work. A human reviews between stages.
* B4. Five context layers: L0 `CLAUDE.md` (global identity), L1 workspace `CONTEXT.md` (routing), L2 stage `CONTEXT.md` (inputs, process, outputs), L3 stable reference (voice, style, SOPs), L4 per-run artifacts.
* B5. Evidence base: informal, self-reported, about 52 invited users; Claude models only; no controlled comparison; mostly content production work. Self-stated poor fit: real-time multi-agent work, high concurrency, complex AI-driven branching.
* B6. Community critiques: "a map, not an engine." No memory, no run history, stages overwrite outputs, no versioning.
* B7. Ecosystem: Eduba (eduba.io) sells AI build, teaching, and consulting without naming ICM. Clief Notes community on Skool (~55k members, paid tiers). Community tools include an enterprise launcher called "Taurus," an `icm-template` skill set, and a workspace generator. No official partner or certification program found. No trademark found for the full name, but the USPTO was not searched directly, and "ICM" and "Eduba" were not checked.
* B8. One unverified reference to an alternate name, "Model Workspace Protocol (MWP)."

## Research questions

### A. The method itself

1. Validity and current progress. What is the latest version of the paper and repo? What has changed since March 2026: new releases, follow-up papers, official tooling, enterprise case studies, talks? Is there independent evidence (not from the authors or their community) that ICM improves output quality, cost, or reliability compared with a single large prompt, RAG, or agent frameworks?
2. Model portability. Does ICM work with non-Claude models, or with Claude reached through Azure AI Foundry, AWS Bedrock, or Google Vertex AI? What breaks when you move off Claude Code (skills, `CLAUDE.md` loading, subagents, hooks)?
3. Gaps. List every gap between ICM as published and what an enterprise needs: run history, versioning, memory, concurrency, multi-user editing, access control per layer and stage, secrets handling, scheduling, error handling, testing and evals, rollback. For each gap, give the best existing solution (product, open-source tool, or pattern) and its maturity.

### B. Deployment

4. Surfaces for non-technical users. Compare every realistic way an employee can use an ICM workspace without a terminal: Claude Team/Enterprise (Projects, skills, connectors, admin controls); Claude desktop app; Claude Code via the desktop app or IDE; Microsoft 365 Copilot / Copilot Studio agents; Teams bots; SharePoint and OneDrive-synced folders; Google Workspace; Slack; a custom web app backed by an agent runtime (for example, the Claude Agent SDK or Azure AI Foundry Agent Service). For each surface, cover: which ICM layers it can represent; whether it supports MCP; admin and security controls; cost per seat; setup effort; fit for 5-person versus 5,000-person companies.
5. Hosting models. Compare three models in depth: (a) Nihilo-hosted in Nihilo's Azure tenant; (b) deployed in the client's tenant, on their Azure, AWS, or GCP; (c) hybrid, for example a control plane in Nihilo's tenant with data and execution in the client's. For each model, cover: data residency; data processor obligations and needed contracts (DPA, BAA); client security review friction; required certifications; Nihilo's liability and insurance; operating cost and margin; buyout or transfer path; how mid-market regulated buyers (finance, healthcare-adjacent, legal) react.
6. Cloud reference architectures. For Azure first, then AWS and GCP, specify the services an enterprise ICM deployment would use: model access (Azure AI Foundry with Claude and others); agent runtime and compute (Container Apps, Functions, AKS); workspace storage and versioning (Git-backed repos, Blob); identity (Entra ID, managed identities, RBAC); secrets (Key Vault, BYOK/CMK); networking (private endpoints, VNet); scheduling and queues. Confirm which Claude models are actually available in each cloud's catalog today, in which regions, and on what terms.
7. Scalability. How does an ICM deployment scale across workspaces, departments, concurrent users and runs, and data volume? Where does the folder-as-architecture model break, and what pattern fixes it (a workspace per department, a shared L0-L3 library with per-team L4, Git branching per run, a job queue)? Give concrete limits where they exist (context window sizes, API rate limits, MCP connection limits).

### C. Integration

8. Legacy and mainstream systems with read and write. How does an ICM system read from and write to: Microsoft 365 (SharePoint, Outlook, Teams, Excel); Google Workspace; Salesforce; HubSpot; Dynamics 365; SAP; NetSuite; QuickBooks; ServiceNow; Jira; on-prem SQL Server and Oracle; file shares; mainframe or green-screen systems with no API. For each, cover: the connection method (official MCP server, vendor API, Microsoft Graph, Power Automate or Logic Apps connectors, RPA, or a database gateway); maturity; auth model; the safest way to grant write access (scoped service accounts, approval queues, dry-run modes).
9. MCP in the enterprise. What is the current state of MCP governance: gateways or registries; allowlisting; auth (OAuth for remote servers); per-tool permission scoping; logging; known vulnerabilities (tool poisoning, rug-pull updates, confused deputy)? Which vendors (Microsoft, Anthropic, cloud providers, security vendors) offer MCP governance today?
10. Cross-department use. How should one company context system serve sales, finance, ops, HR, legal, and support at once? Cover: shared versus department-private layers; preventing data leakage between departments (for example, HR data reaching sales agents); who owns and edits which files; how non-technical owners propose changes safely (review, approval, versioning).

### D. Security, oversight, compliance

11. Security controls. Map ICM deployments to the OWASP Top 10 for LLM Applications (current version) and MITRE ATLAS. Cover: indirect prompt injection through files and connectors; excessive agency; data exfiltration through tool calls; secrets in context files; least-privilege tool access; isolating research steps (untrusted input) from action steps (writes and sends). Recommend concrete controls per hosting model.
12. Monitoring, logging, and oversight. Design how every data movement and every agent action is logged, attributable to a user, replayable, and reviewable. Include: what to capture (prompts, tool calls, inputs, outputs, file diffs, approvals); where it goes (Azure Monitor / Log Analytics, Microsoft Sentinel, Microsoft Purview, OpenTelemetry for GenAI, Anthropic and Foundry tracing); retention; immutability; PII handling in logs; alerting on anomalous actions; the dashboard a client's compliance officer would see.
13. Compliance mapping. Show how a well-built ICM deployment produces evidence for: SOC 2 (relevant Trust Services Criteria); NIST AI RMF 1.0 and the Generative AI Profile (NIST AI 600-1); ISO/IEC 42001; ISO/IEC 27001; the EU AI Act, where clients have EU exposure. Which of these can Nihilo realistically pursue first given its size and budget, at what approximate cost and timeline? Cite sources for any cost figures, and mark estimates as estimates.

### E. Commercial

14. Packaging and pricing. Propose service tiers for small firms (5-50), mid-market, and enterprise: scope; delivery time; what is standardized versus tailored; setup fee; monthly retainer or managed-service fee; buyout price logic for the Nihilo-hosted model. Ground the prices in comparable public offerings (AI automation agencies, Microsoft partners selling Copilot deployments, managed AI services). Never invent a price: cite it or mark it as an estimate with its basis.
15. Selling enterprise builds. What does an enterprise buyer require before signing with a two-to-three person firm: security questionnaires; insurance; certifications; references; procurement paths (Azure Marketplace listing, Microsoft partner programs)? What is the shortest credible path to the first enterprise deal, and which proof points matter most?
16. Competitors and differentiation. Who else sells ICM implementations or close equivalents (context engineering, "company brain," AI knowledge workspace services)? How do Claude Enterprise, Microsoft 365 Copilot with Copilot Studio, Glean, and similar products already cover this need natively? What can a small firm offer that these do not?
17. IP and naming. Confirm the paper and repo licenses permit commercial use with attribution. Check USPTO (and EUIPO if relevant) for "Interpretable Context Methodology," "ICM" in software and consulting classes, "Eduba," and "Clief Notes." Recommend safe attribution language for a Nihilo-branded offer.

## Decision matrix for the architectures (step 3)

Score each candidate architecture 1-5 on each criterion, with a one-line justification:

* Usable by non-technical staff
* Security and least privilege
* Oversight: logging, replay, attribution
* Integration reach (legacy plus mainstream, read and write)
* Scalability across departments and users
* Fit for small firms
* Fit for enterprise and regulated buyers
* Build effort for a part-time two-to-three person team
* Running cost per client per month
* Compliance evidence produced
* Portability between clouds and models

## Output

Return one report in Markdown, written in plain American English, with sentence-case headings and no em dashes. Sections:

1. Executive summary (10 lines max): the recommendation, the top 3 risks, the first thing to prototype.
2. Baseline validation: each "What we already know" item with its status and source.
3. Answers to questions 1-17, numbered to match, each with sources.
4. Hosting model comparison (Q5) as a table.
5. Candidate architectures with diagrams (Mermaid) and the scored decision matrix.
6. Recommendation: chosen architecture, packaging, pricing basis, assumptions, what would change the call.
7. Prototype plan: the smallest build that proves the recommended architecture, using Nihilo's own Azure tenant and Microsoft 365 as test case 1 and SharePoint as test case 2, with pass/fail criteria.
8. Open questions: everything unsettled, each with the specific next check.
9. Sources: every URL cited, with access date.
