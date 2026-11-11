<!-- {"wp": "WP-Q05A", "models": ["claude-fable-5-2"], "fallbacks": 0, "stop_reason": "end_turn", "cost_usd": 1.782, "searches": 12, "fetches": 20} -->
# WP-Q05A: Q5, contracts and vendor terms per hosting model

### Findings

All pages accessed 2026-11-11. Page dates are given where the page shows one.

#### Anthropic: commercial terms for a firm that builds on or hosts Claude for clients

[confirmed Q5] Building client-facing systems on the API falls inside the license grant in section A.1 of the Commercial Terms (effective Jun 17, 2025), which extends to products a customer offers its own customers and end users. Subject to these Terms, Anthropic gives Customer permission to use the Services, including to power products and services Customer makes available to its own customers and end users {S22}

[confirmed Q5] Resale of the Services is barred by section D.4 unless Anthropic expressly approves it. Customer may not and must not attempt to (a) access the Services to build a competing product or service, including to train competing AI models or resell the Services except as expressly approved by Anthropic {S22}

[confirmed Q5] The Usage Policy (page shows "Effective Nov 12, 2026", one day after this run) lists unauthorized resale or proxying of Claude access among its platform-abuse prohibitions, and names routing through consumer subscriptions as an example. Resell, proxy, or otherwise provide access to Claude through unauthorized means, including services that route requests through consumer subscriptions or misrepresent the product or client being used {S28}

[inference Q5] A Nihilo-hosted ICM system with real workflow logic on top of the API reads as "powering a product" (allowed). Passing through raw API access or seats at a markup reads as "resale" (needs approval). The terms do not define the line, so get it confirmed in writing before pricing a managed service on token markup.

[confirmed Q5] Account-level responsibility stays with the contracting customer under D.5, so in a Nihilo-hosted model every client user's activity is Nihilo's responsibility toward Anthropic. Customer is responsible for all activity under its account. {S22}

[confirmed Q5] An accuracy warning to end users is a contractual duty under D.3, which Nihilo's client contract and UI would need to carry. Customer acknowledges, and must notify its Users, that factual assertions in Outputs should not be relied upon without independently checking their accuracy {S22}

[confirmed Q5] Indemnity runs from the customer to Anthropic for third-party claims tied to user inputs or policy violations (K.2). Customer will defend Anthropic and its personnel, successors, and assigns from and against any Anthropic Claim (as defined below) and indemnify them for any judgment that a court of competent jurisdiction grants a third party on such Anthropic Claim or that an arbitrator awards a third party under any Customer-approved settlement of such Anthropic Claim. “Anthropic Claim” means any third-party claim, suit, or proceeding related to Customer’s or its Users’ (a) Inputs or other data provided by Customer, or (b) use of the Services in violation of the Usage Policy, the Service Specific Terms, or Section D.4 (Use Restrictions). {S22}

[confirmed Q5] Twelve months of fees is the ceiling on each side's liability under L.3.a, with consequential damages excluded. is limited to Fees paid by Customer for the Services in the previous 12 months {S22}

[inference Q5] In the Nihilo-hosted model, Nihilo sits between an uncapped client claim and a vendor whose liability is capped at Nihilo's own 12-month spend. Nihilo's client contract needs its own cap and insurance sized to that gap.

[confirmed Q5] Thirty days' notice is all Anthropic owes before terminating for convenience (I.2.a), and suspension is possible when a user breaches the policies. Each party may terminate these Terms at any time for convenience with Notice, except Anthropic must provide 30 days prior Notice. {S22}

[confirmed Q5] High-risk use cases in the Usage Policy (legal, finance, credit, insurance, employment, healthcare access and others) carry a human-review and AI-disclosure requirement. we require that a qualified person remain accountable for what is delivered or decided, and that the impacted individual knows AI was involved in the advice or decision {S28}

[confirmed Q5] Internal drafting, research, summarization and general business operations sit in the listed exclusions from those high-risk requirements. Internal drafting, research, summarization, or analysis that is not the ultimate High-risk AI Recommendation delivered. Business operations that do not advise or decide about a specific individual. {S28}

[confirmed Q5] Responsibility for what an agent does through tools and connected systems is placed on whoever builds or deploys it. Users are responsible for ensuring that agents they build or deploy, including actions those agents take through tools, browsers, or connected systems, comply with this Usage Policy. {S28}

[unverified Q5] Whether Anthropic runs a reseller or services-partner program open to a two-to-three person firm, and on what terms. The Usage Policy mentions "authorized resellers" and Anthropic's site links to "Service partners" and "Powered by Claude" pages, but I did not fetch them. Next check: open https://claude.com/partners/services and https://claude.com/partners/powered-by-claude, then ask Anthropic sales whether a managed ICM service needs D.4 approval.

#### Anthropic: DPA, sub-processors, retention, zero data retention

[confirmed Q5] No separate signature is needed for Anthropic's DPA (effective Feb 24, 2025), because the Commercial Terms pull it in by reference. Data submitted through the Services will be processed in accordance with the Anthropic Data Processing Addendum (“DPA”), which is incorporated into these Terms by reference. {S22}

[confirmed Q5] Roles under the DPA are fixed: the contracting customer is controller and Anthropic is its processor. With respect to Customer Personal Data, Customer is the controller and Anthropic is Customer’s processor. {S23}

[confirmed Q5] A processor-to-processor transfer module is already built into the DPA, which fits the case where Nihilo is itself a processor for its client. the terms of the SCCs Module Two (controller to processor) and/or Module Three (processor to processor), as completed as described in Schedule 3 of this DPA, are hereby incorporated by reference {S23}

[confirmed Q5] Sub-processor changes at Anthropic work by general authorization with a 15-day objection window. Customer may, on the basis of reasonable data privacy or data security concerns, object to Anthropic’s use of such Subprocessor by providing Anthropic with written notice of the objection within fifteen (15) days of the date of such notice {S23}

[confirmed Q5] Breach notice from Anthropic has a 48-hour outer limit. Anthropic will notify Customer in writing without undue delay, but in any event within 48 hours, after becoming aware of any Security Breach {S23}

[confirmed Q5] Deletion or return of customer data follows within 30 days of the agreement ending, with carve-outs for legal holds, disputes and combating harmful use. Within thirty (30) days of the date of termination or expiration of the Agreement, Anthropic will: delete all copies of Customer Data (including Customer Personal Data) processed by Anthropic or any Subprocessors {S23}

[confirmed Q5] Special categories of personal data are listed as "None" in the DPA's description of processing, so health or similar data is outside the default scope. **Special categories of personal data (if applicable)**: None. {S23}

[unverified Q5] Anthropic's current sub-processor list. The DPA points to https://www.anthropic.com/subprocessors, but my fetch returned only a Trust Center shell with no list. Next check: open that URL in a browser and save a dated copy for Nihilo's own sub-processor schedule.

[confirmed Q5] Default API retention is up to 30 days (privacy article dated July 1, 2026), with exceptions for features the customer controls, zero data retention agreements, policy enforcement and law. For Anthropic API users, we automatically delete inputs and outputs on our backend within 30 days of receipt or generation {S38}

[confirmed Q5] Flagged content is kept far longer than the default, whatever arrangement is in place. We retain inputs and outputs for up to 2 years and trust and safety classification scores for up to 7 years if your chat is flagged by our automated trust and safety systems as violating our Usage Policy. {S38}

[confirmed Q5] Zero data retention (ZDR) is an approval-based arrangement requested through sales and switched on one organization at a time. To request ZDR for your organization, contact the Anthropic sales team. ZDR is enabled per organization; each new organization requires ZDR to be enabled separately by your account team {S27}

[unverified Q5] ZDR eligibility criteria for a small firm. No Anthropic page I retrieved publishes them. Next check: ask Anthropic sales whether a low-volume Console organization qualifies, and get the answer in writing.

[confirmed Q5] ZDR scope is limited to the Messages and Token Counting APIs and Claude Code used with commercial API keys. Console use, Claude Managed Agents, and the Team and Enterprise product interfaces fall outside it. **Claude Console:** Any usage in the Claude Console, including playground. **Claude Managed Agents:** Claude Managed Agents is a stateful resource; session transcripts persist until you delete them. **Claude Teams and Claude Enterprise product interfaces:** These interfaces are not ZDR-eligible. {S27}

[confirmed Q5] Several features an ICM runtime might lean on are marked ineligible for both ZDR and HIPAA readiness in Anthropic's table: Agent Skills, Batch processing, the Files API, the MCP connector, the code execution tool and Claude Managed Agents. Agent Skills | `/v1/skills` `/v1/messages` with `skills` | No | No | Skill data retained according to standard policy. Batch processing | `/v1/messages/batches` | No | No | 29-day retention; async storage required. Files API | `/v1/files` | No | No | Files retained until explicitly deleted or they reach their configured expiration. MCP connector | `/v1/messages` with `mcp_servers` | No | No | Data retained according to standard policy. {S27}

[confirmed Q5] Client-side tools (bash, text editor, memory) are eligible under both arrangements because they run in the customer's own environment. Bash tool | `/v1/messages` with `bash` tool | Yes | Yes | Client-side tool run in your environment. Memory tool | `/v1/messages` with `memory` tool | Yes | Yes | Client-side memory storage where you control data retention. {S27}

[inference Q5] For regulated clients, the ICM runtime should use the plain Messages API with tools, files and MCP calls executed in the Azure environment (Nihilo's or the client's), not Anthropic-hosted Skills, Files, MCP connector or Managed Agents. That keeps the workload inside what ZDR and the BAA can cover.

[confirmed Q5] The newest "Covered Models" (the Fable and Mythos lines) force 30-day retention and override any ZDR commitment, per the Service Specific Terms (effective Aug 31, 2026). Customer agrees that Anthropic may retain and perform safety reviews on Inputs, Outputs, and other data regarding Customer’s use of the Covered Models. For clarity, this supersedes any modified retention commitments (e.g., ZDR) provided by Anthropic that may otherwise apply to Customer’s use of the Services. {S31}

[confirmed Q5] Beta features come without indemnity and with a tiny liability cap, which matters if a client build depends on one. Anthropic’s liability related to Beta Services is limited to the lesser of $1,000 and Fees paid by Customer for the Services in the previous 12 months. {S31}

#### Anthropic: BAA availability

[confirmed Q5] BAA coverage exists for three surfaces only: the first-party API, Claude in Microsoft Foundry, and Enterprise plans (privacy article "updated over a week ago"). Anthropic provides a BAA covering our HIPAA-ready services, such as use of our first-party API, Claude in Microsoft Foundry, or Enterprise plans. {S24}

[inference Q5] Nihilo's current Claude Team plan is not on that list, so no PHI should go through it. A secondary source says Team cannot enable HIPAA at all, but I did not find that sentence on a primary page.

[confirmed Q5] One BAA covers one organization, and Console, cloud Cowork and beta features are excluded. the BAA only covers the single organization that accepted it, and excludes features such as Claude Console, Cowork in the cloud, or features currently in beta {S24}

[confirmed Q5] Two enablement paths exist for the API: self-serve in the Console with the standard BAA, or through sales for a negotiated one. Most organizations can enable it directly in the Claude Console with Anthropic’s standard BAA; organizations that require a negotiated BAA should work with their account team. {S27}

[confirmed Q5] Sources differ slightly here: the privacy-center article says the Primary Owner signs the BAA and then contacts Anthropic to switch PHI processing on. To use the 1P API with PHI, your organization’s Primary Owner will need to sign a BAA and then reach out to your Anthropic contact or our Sales team to get this turned on. {S24} The developer docs are more detailed and describe both paths, so I treat them as the fuller account. Whether self-serve appears for a given organization is still to be tested.

[confirmed Q5] HIPAA enablement on an API organization is irreversible and organization-wide, so PHI and non-PHI work need separate organizations. Once HIPAA readiness is enabled for your organization, the configuration is permanent and cannot be disabled by an administrator. If you need both HIPAA-ready and general-purpose API access, use separate organizations for each. {S27}

[confirmed Q5] Under the BAA on a HIPAA-ready API organization, the Batch API, Files API, Skills API, code execution and web fetch are blocked, and external MCP data flows are available but uncovered. Batch API | ❌ *Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users* {S24}

[confirmed Q5] Claude through Microsoft Foundry (either hosting option) qualifies when two things are in place: a BAA with Anthropic, and a HIPAA configuration on the Azure subscription requested through Anthropic's account team. Claude in Microsoft Foundry (Hosted on Anthropic or Hosted on Azure) is an eligible service for customers with a BAA with Anthropic plus the HIPAA configuration enabled on the Azure subscription. Request the HIPAA configuration through your Anthropic account team. {S27}

[corrected Q5] Some secondary write-ups from mid-2026 say HIPAA readiness is not available on Microsoft Foundry. Anthropic's current primary pages (above) list Foundry as eligible. The primary pages are more recent and authoritative.

[confirmed Q5] Bedrock and Google Cloud's Agent Platform are outside Anthropic's HIPAA readiness (the cloud provider's own compliance terms apply), and Claude Platform on AWS has no HIPAA readiness at all. **Partner-operated platforms:** Amazon Bedrock and Google Cloud’s Agent Platform. **Claude Platform on AWS:** HIPAA readiness is not available on Claude Platform on AWS. {S27}

[confirmed Q5] Claude Code routed through Foundry, Bedrock or Google Cloud is available but not BAA-covered. Claude Code (local mode) is covered only when Claude Code connects directly to Anthropic, not through a cloud provider or gateway {S24}

#### Who the processor is, per route to Claude

[confirmed Q5] Processor identity depends on the route: Anthropic is the processor on its own API, Claude Platform on AWS, the Anthropic-managed Google Cloud offering and Microsoft Foundry, while on Bedrock and the Google-managed offering the cloud provider holds that role. This page covers the Claude API (`api.anthropic.com`), Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed), and Claude in Microsoft Foundry, where Anthropic is the data processor. On Claude Models on Google Cloud (Google managed) and Amazon Bedrock, the cloud provider is the data processor {S27}

[confirmed Q5] In Foundry, Microsoft's page (last updated 2026-06-29) describes Claude as a third-party Marketplace offering in which Anthropic is seller, operator and independent processor under Anthropic's own terms. For both hosting options, Anthropic is the seller and operator of Claude models in Microsoft Foundry and acts as an independent data processor for prompts and outputs associated with Claude models. Anthropic's terms of use govern your use of the Claude models. {S39}

[confirmed Q5] Microsoft's own DPA still applies in Foundry, but only to the surrounding Foundry experience, infrastructure and billing data. Microsoft processes data for these services under the Microsoft Products and Services Data Protection Addendum and applicable Marketplace terms. {S39}

[confirmed Q5] Whoever owns the Azure billing account accepts Anthropic's Marketplace offer, so in a client-tenant deployment the client, not Nihilo, becomes Anthropic's contracting party. Subscribe to the **Claude Platform on Foundry** offer through Azure Marketplace or the Microsoft Foundry portal model catalog. Accept the offer on your Azure billing account. {S33}

[confirmed Q5] Cloud Solution Provider subscriptions cannot deploy Claude models in Foundry (page last updated 2026-09-22). The following subscription types aren't supported for Claude models: - Free trial subscriptions - Student subscriptions - Credit-based subscriptions - Enterprise accounts in South Korea - Cloud Solution Provider (CSP) subscriptions {S33}

[inference Q5] This matters for Nihilo's channel: small clients who buy Azure through an MSP on CSP cannot host Claude in their own tenant via Foundry. They would need a direct Microsoft Customer Agreement subscription, or the Anthropic API directly.

[confirmed Q5] Residency differs by Foundry hosting option: the Azure-hosted option keeps data at rest in the chosen Azure geography, while the Anthropic-hosted option may process outside Azure and outside the selected region. Data at rest is stored in the selected Azure geography and processing is scoped to applicable "global" or "DataZone" deployment options on Microsoft Foundry. | Data might be processed outside Azure, including outside the selected Azure region. {S33} Regions and model lists belong to WP-Q06A and WP-Q06B.

[confirmed Q5] The two vendors word the Azure-hosted boundary differently. Microsoft says prompts and outputs never leave Azure. Anthropic's page adds an exception, and is the more precise of the two. Only usage metadata and content flagged by Anthropic’s safety systems egress to Anthropic. {S26}

[confirmed Q5] Inside Microsoft 365 Copilot and Copilot Studio the contract picture is different: there Anthropic acts as Microsoft's sub-processor under Microsoft's Product Terms and DPA, except for models labeled as requiring data retention (page last updated 2026-11-04). Unless models are labeled "Anthropic models with Data Retention," the Microsoft Product Terms and Microsoft Data Protection Addendum (DPA) apply to the use of Claude models from Anthropic through Microsoft's enterprise Online Services. {S37}

[confirmed Q5] EU residency commitments do not extend to those Copilot-embedded Claude models, which are off by default for EU and UK tenants. Claude models deployed in Microsoft offerings such as Microsoft Copilot, Researcher, Copilot Studio, Power Platform, and Copilot in Microsoft 365 apps are currently excluded from the EU Data Boundary, and when applicable, in-country processing commitments. Customers within the EU Data Boundary and customers in the UK have Claude models disabled by default. {S37}

[unverified Q5] Whether ZDR can be enabled for Claude in Foundry. A Microsoft employee's Q&A answer (July 2026) points to an Anthropic request form at https://claude.com/form/azure-data-retention-request, but Anthropic's retention docs list ZDR only for its API, Claude Platform on AWS and the Anthropic-managed Google offering. Next check: open the form URL and ask Anthropic to confirm in writing.

#### Microsoft: hosting for third parties, DPA, BAA

[confirmed Q5] Reselling or redistributing Azure services is prohibited as a general rule in the Product Terms (Microsoft Customer Agreement view). Customer may not resell or redistribute the Microsoft Azure Services, or allow multiple users to directly or indirectly access any Microsoft Azure Service feature that is made available on a per user basis (e.g., Microsoft Entra ID). {S34}

[confirmed Q5] The "Azure Customer Solution" clause is the exception that makes a Nihilo-hosted model licensable: third parties may use Azure services when that use is tied to the customer's own solution, and the customer answers for their compliance. Despite anything to the contrary in Customer’s licensing agreement, Customer may permit third parties to access and use the Microsoft Azure Services solely in connection with the use of that Customer Solution. Customer is responsible for: (1) ensuring that third parties who access, use or distribute the Customer Solution comply with these terms, the terms and conditions of Customer's licensing agreement, and all applicable laws {S34}

[unverified Q5] The exact current definition of "Customer Solution". A search snippet from Microsoft's licensing guidance says the solution must add "primary and significant functionality" to Azure, but I did not load the Product Terms glossary. Next check: open https://www.microsoft.com/licensing/guidance/Azure-Customer-Solution and the Product Terms glossary, and confirm an ICM workspace runtime qualifies.

[confirmed Q5] Third-party models in Foundry sit outside Microsoft's own product commitments. Any third-party models that Microsoft makes available through Microsoft Foundry Models (including in a Model Catalog, Model Registry, or otherwise), but which are not Foundry Models sold by Azure or First-Party Consumption Services, are Non-Microsoft Products and subject to the terms for Non-Microsoft Products. {S34}

[confirmed Q5] No separate signature is needed for Microsoft's HIPAA BAA, which comes through the Product Terms and DPA. The Learn page is dated 2023-04-06, older than six months, so treat it as suspect until rechecked. There is no separate contract to sign to enter into a HIPAA Business Associate Agreement (BAA) with Microsoft because the HIPAA BAA is available via the Microsoft Product Terms (formerly Online Services Terms) by default to all customers who are covered entities or business associates under HIPAA. {S30}

[confirmed Q5] For a SaaS provider on Azure, Microsoft's stated position is that the provider's healthcare customers sign a BAA with the provider, not with Microsoft (same 2023 page). If you're a SaaS provider of a healthcare solution deployed on Azure, your customers who are healthcare providers or covered entities under HIPAA can sign a BAA directly with you. They don't need to have a BAA in place with Microsoft to use your SaaS solution. {S30}

[confirmed Q5] Custom BAAs are off the table with Microsoft (same 2023 page). Microsoft can't use a customer's BAA. {S30}

[unverified Q5] Current text of the Microsoft Products and Services DPA (sub-processor notice period, incident notification wording) and whether Foundry, Container Apps and the other planned services are in HIPAA BAA scope. I found only third-party copies of older DPA versions; those copies contemplate the customer acting as a processor with Microsoft as sub-processor. Next check: download the current DPA from https://aka.ms/dpa and the BAA from https://aka.ms/baa, and check the "Cloud services in audit scope" page on Microsoft Learn.

#### Law: what makes Nihilo a processor or business associate

[confirmed Q5] GDPR Article 28 requires a written contract between controller and processor covering subject matter, duration, nature and purpose, data types and data subjects (EUR-Lex text via search result, not a full fetch). by a processor shall be governed by a contract or other legal act under Union or Member State law, that is binding on the processor with regard to the controller and that sets out the subject-matter and duration of the processing, the nature ... The contract or the other legal act referred to in paragraphs 3 and 4 shall be in writing, including in electronic form. {S40}

[confirmed Q5] Sub-processors need the controller's prior written authorization under Article 28(2). The processor shall not engage another processor without prior specific or general written authorisation of the controller. {S40}

[confirmed Q5] Flow-down is mandatory under Article 28(4): the sub-processor contract must carry the same data protection obligations as the controller's contract with the processor (reproduction of the GDPR text, secondary site). Where a processor engages another processor for carrying out specific processing activities on behalf of the controller, the same data protection obligations as set out in the contract or other legal act between the controller and the processor as referred to in paragraph 3 shall be imposed on that other processor {S41}

[confirmed Q5] Liability for a sub-processor's failure stays with the first processor (reproduction of the GDPR text, secondary site). Where that other processor fails to fulfil its data protection obligations, the initial processor shall remain fully liable to the controller for the performance of that other processor's obligations. {S42}

[confirmed Q5] Record-keeping and breach notice to the controller are direct processor duties (EUR-Lex snippet, Articles 30 and 33). Each processor and, where applicable, the processor's representative shall maintain a record of all categories of processing activities carried out on behalf of a controller, containing: The processor shall notify the controller without undue delay after becoming aware of a personal data breach. {S40}

[confirmed Q5] Under HIPAA, HHS guidance (last reviewed October 21, 2026) treats any subcontractor handling PHI for a business associate as a business associate itself. A business associate also is any subcontractor that creates, receives, maintains, or transmits PHI on behalf of another business associate. {S29}

[confirmed Q5] HHS's own examples of business associates include cloud providers, managed service providers with system access, and third-party chatbot vendors, which between them describe every Nihilo hosting model. IT contractor or vendor (*e.g.*, EHR vendor, Managed Services Provider) that provides maintenance and/or support services (either in person or remotely) for information systems that require the contractor or vendor to create, receive, maintain, or transmit ePHI. {S29}

[confirmed Q5] Timing matters: the downstream BAA has to exist before any PHI moves to the subcontractor, and the covered entity does not need its own BAA with that subcontractor. A business associate must establish a BAA with its subcontractor before disclosing PHI to the subcontractor for work to be done for a covered entity. A covered entity is not required to establish a BAA directly with a subcontractor of its business associate. {S29}

#### Ownership of deliverables and what a buyout must transfer

[confirmed Q5] Output ownership sits with whoever is Anthropic's contracting customer. As between the parties and to the extent permitted by applicable law, Anthropic agrees that Customer (a) retains all rights to its Inputs, and (b) owns its Outputs. {S22}

[inference Q5] In the Nihilo-hosted model that customer is Nihilo, so the client owns its outputs only if Nihilo's client contract says so. In the client-tenant model the client is the customer and owns outputs directly.

[confirmed Q5] Training on customer content is ruled out in the Commercial Terms. Anthropic may not train models on Customer Content from Services. {S22}

[confirmed Q5] Nihilo's Anthropic agreement cannot be handed to a client, since assignment needs Anthropic's written consent. Neither party may assign its rights or delegate its obligations under these Terms without the other party’s prior written consent {S22}

[inference Q5] A buyout therefore means the client opens its own Anthropic relationship (its own Console organization or its own Foundry Marketplace acceptance). Any BAA or ZDR arrangement is per organization and has to be re-established by the client.

[confirmed Q5] Paying for bespoke work does not by itself make the client the copyright owner under US law. Per Copyright Office Circular 30 (revised 08/2024), a commissioned work is "made for hire" only when it fits one of nine listed categories and a signed written agreement says so. There must be a written agreement between the party that ordered or commissioned the work and individual(s) who actually created the work. The agreement must be signed by all parties. If a work fails to satisfy any of these requirements, it is not a work made for hire. {S36}

[inference Q5] Software, scripts and ICM context files are not obviously within the nine categories, so by default Nihilo keeps the copyright in what it builds. That supports the "Nihilo owns it, client pays to own it" model, but only if the contract states a license during the term and an express written assignment at buyout. Next check: have counsel draft the assignment clause and confirm the formalities under 17 U.S.C. 204, which I did not retrieve.

[confirmed Q5] Moving an Azure subscription to the client's directory is possible but destructive for identity: role assignments and custom roles are wiped (Microsoft Learn, last updated 2026-06-16). all role assignments and custom roles in Azure role-based access control (Azure RBAC) are **permanently** deleted from the source directory and aren't transferred to the target directory {S35}

[confirmed Q5] Managed identities and Key Vault need rework after such a transfer. You must delete, re-create, and attach the managed identities to the appropriate resource. You must update the tenant ID associated with the key vaults. {S35}

[confirmed Q5] Customer-managed keys can turn a transfer into permanent data loss. If you're using encryption at rest for a resource, such as a storage account or SQL database, that has a dependency on a key vault that is being transferred, it can lead to an unrecoverable scenario. {S35}

[confirmed Q5] Some services cannot move at all (AKS clusters, for example), and CSP subscriptions cannot change directory. You cannot transfer your AKS cluster and its associated resources to a different directory. For Azure Cloud Solution Providers (CSP) subscriptions, changing the Microsoft Entra directory for the subscription isn't supported. {S35}

[confirmed Q5] Old credentials survive the move, so a clean handover includes rotating them. Until the credentials are updated, users will continue to have access after the transfer. {S35}

[confirmed Q5] Microsoft itself lists two alternatives to a transfer: rebuild in the target and copy data, or leave the subscription in place and delegate access with Azure Lighthouse. Re-create the resources and copy data to the target directory and subscription. Use Azure Lighthouse to delegate resources so that users in the target directory can access the subscription in the source directory. {S35}

[unverified Q5] Whether a Claude deployment and its Marketplace subscription survive a subscription transfer between tenants or billing accounts. The transfer article does not list Foundry or Marketplace offers. Next check: test with a throwaway subscription in Nihilo's two Azure subscriptions, and ask Microsoft Support.

[inference Q5] Design for buyout from day one: one Azure subscription per client, everything in infrastructure-as-code, no AKS, and no customer-managed keys that tie to Nihilo's Key Vault. The cleanest buyout is a scripted redeploy into the client's tenant plus a data copy, not a subscription transfer.

### Answer summary

**Q5, contracts and vendor terms per hosting model.** The table is [inference] built from the findings above.

| Item | (a) Nihilo-hosted | (b) Client tenant | (c) Hybrid |
|---|---|---|---|
| Who contracts with Microsoft | Nihilo, relying on the Azure Customer Solution clause | Client | Both |
| Who contracts with Anthropic | Nihilo (API or Foundry Marketplace) | Client (accepts the Marketplace offer on its billing account) | Client for inference; Nihilo only if the control plane calls Claude |
| Nihilo's GDPR role | Processor; Microsoft and Anthropic are its sub-processors | Processor only to the extent Nihilo staff can access personal data | Processor for whatever content, logs or telemetry reach Nihilo's tenant |
| Contracts Nihilo must offer | DPA with sub-processor list and flow-down; MSA with liability cap; output ownership clause | Services agreement; a lighter DPA covering access | Both, scoped to the control plane |
| PHI clients | BAA client to Nihilo; Microsoft BAA via Product Terms; Anthropic BAA on a separate HIPAA-ready organization or Foundry HIPAA configuration | Client holds the Microsoft and Anthropic BAAs; Nihilo signs a BAA as a contractor with access | As (b), plus (a) if PHI can reach the control plane |
| Data residency | Set by Nihilo's Azure region and Claude hosting option | Set by the client | Client data follows (b); control-plane data follows (a) |
| Buyout | IP assignment, redeploy or subscription transfer, new Anthropic relationship, credential rotation | Mostly an IP assignment and access removal | Remove or hand over the control plane |

* **Data residency.** [inference] Residency is a deployment choice, not a hosting-model property. The Azure-hosted Foundry option keeps data at rest in the selected geography; the Anthropic-hosted option does not promise that. Details are with WP-Q06A and WP-Q06B.
* **Processor obligations.** GDPR Article 28 needs a written contract, sub-processor authorization and flow-down, and leaves the first processor liable for its sub-processors. [inference] In model (a) Nihilo carries that for both Microsoft and Anthropic. In model (b) the chain does not run through Nihilo.
* **What Anthropic requires.** Building products for your own customers is allowed. Reselling the Services needs express approval. The customer is responsible for all account activity, must pass on an accuracy notice, indemnifies Anthropic for user inputs and policy breaches, and faces a 12-month-fees liability cap. The DPA is automatic. A BAA is available for the API, Foundry and Enterprise plans only, per organization, with a restricted feature set. Default retention is up to 30 days and flagged content up to 2 years. ZDR is by approval per organization and excludes Skills, Files, the MCP connector, code execution, Managed Agents and the newest Covered Models.
* **What Microsoft requires.** No resale of Azure, but third parties may use Azure services through a Customer Solution, with Nihilo responsible for their compliance. Claude in Foundry is a Non-Microsoft Product under Anthropic's terms. CSP subscriptions cannot deploy Claude in Foundry. Microsoft's BAA is automatic and non-negotiable, but the source page is from 2023 and the current DPA text is unverified.
* **Ownership and buyout.** [inference] By default Nihilo owns the copyright in what it builds and, in model (a), is the contractual owner of outputs. A buyout must transfer by contract: a written IP assignment for workspace files, scripts and infrastructure code; output and data ownership; the Azure environment (redeploy preferred); exported logs and run history; and rotated credentials. The Anthropic agreement, BAA and ZDR do not transfer. The client needs its own.
* **Regulated buyers.** [inference] Model (a) is the hardest sell to them: Nihilo becomes a business associate or processor with two sub-processors, a small balance sheet, and Anthropic liability capped at Nihilo's own spend. Model (b) puts the vendor paper directly between the client and Microsoft and Anthropic, which is the pattern their security teams already know.

### Coverage checklist

* **Data residency, processor obligations and contracts (DPA, BAA, sub-processor lists) for all three models:** partly covered. Contract structure and legal duties are sourced. The Anthropic sub-processor list did not load, the current Microsoft DPA text was not retrieved, and the hybrid model is analysis only, since no vendor page describes it. Residency detail is deferred to WP-Q06A and WP-Q06B by design.
* **What Anthropic and Microsoft require of a company that resells or hosts Claude (commercial terms, BAA, retention, ZDR eligibility):** mostly covered. Anthropic's terms, DPA, BAA scope, retention and ZDR scope are confirmed from primary pages. Open items: the "resale" boundary and any partner program, ZDR eligibility criteria, ZDR on Foundry, and the Customer Solution definition.
* **Who owns deliverables and what a buyout must transfer:** partly covered. Output ownership, non-assignability, work-for-hire rules and Azure transfer mechanics are confirmed. The assignment formalities (17 U.S.C. 204), non-US law, and Marketplace subscription behavior on transfer are not.

### Open questions

1. Does a managed ICM service count as "resale" under Commercial Terms D.4? Next check: written question to Anthropic sales; read https://claude.com/partners/services.
2. Anthropic's current sub-processor list. Next check: open https://www.anthropic.com/subprocessors in a browser.
3. Will Anthropic grant ZDR, or self-serve HIPAA enablement, to a low-volume organization? Next check: look for the HIPAA compliance card at platform.claude.com/settings/privacy in Nihilo's Console organization; ask sales about ZDR.
4. Is ZDR available for Claude in Foundry? Next check: open https://claude.com/form/azure-data-retention-request and confirm with Anthropic.
5. Current Microsoft DPA and BAA text, and whether Foundry and Container Apps are in BAA scope. Next check: https://aka.ms/dpa, https://aka.ms/baa, and the "Cloud services in audit scope" Learn page.
6. Exact "Customer Solution" definition and whether a thin ICM runtime meets it. Next check: Product Terms glossary and the Azure Customer Solution guidance page.
7. Does a Foundry Claude deployment survive a subscription or billing transfer? Next check: test between Nihilo's two subscriptions.
8. Can client staff be seated on Nihilo's Claude Team plan without breaching the terms? Not addressed on any page retrieved. Next check: ask Anthropic support; the safer default is that each client buys its own seats.
9. IP assignment wording and non-US client rules (UK and EU copyright, GDPR representative duties). Next check: engage counsel for an MSA, DPA and BAA template set.
10. The Usage Policy shows an effective date of Nov 12, 2026. Next check: re-read it after that date and compare against the version history for changes to the resale and high-risk sections.

## Sources attached by the API

- S22: Commercial Terms of Service https://www.anthropic.com/legal/commercial-terms
- S23: Data Processing Addendum https://www.anthropic.com/legal/data-processing-addendum
- S24: Business Associate Agreements (BAA) for Commercial Customers | Anthropic Privacy Center https://privacy.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers
- S26: Claude in Microsoft Foundry https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- S27: API and data retention https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
- S28: Usage Policy https://www.anthropic.com/legal/aup
- S29: Business Associates Frequently Asked Questions (FAQs) https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html
- S30: HIPAA - Azure Compliance https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us
- S31: Service Specific Terms https://www.anthropic.com/legal/service-specific-terms
- S33: Compare hosting options for Claude models in Microsoft Foundry - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-hosting-comparison
- S34: Microsoft Product Terms https://www.microsoft.com/licensing/terms/productoffering/MicrosoftAzure/MCA#ServiceSpecificTerms
- S35: Transfer an Azure subscription to a different Microsoft Entra directory https://learn.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription
- S36:  https://www.copyright.gov/circs/circ30.pdf
- S37: Claude models from Anthropic in Microsoft Online Services https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
- S38: How long do you store my organization’s data? | Anthropic Privacy Center https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
- S39: Data, privacy, and security for use of Anthropic Claude models in Microsoft Foundry - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/claude-models/data-privacy
- S40: Consolidated TEXT: 32016R0679 — EN — 04.05.2016 https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02016R0679-20160504
- S41: Article 28 📖 GDPR. Processor https://gdpr-text.com/read/article-28/
- S42: GDPR Article 28. Processor https://streamlex.eu/articles/gdpr-en-art-28/

_112 search results consulted; 19 sources cited._
