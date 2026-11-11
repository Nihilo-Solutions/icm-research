<!-- {"wp": "WP-X1", "models": ["claude-fable-5-2"], "fallbacks": 0, "stop_reason": "end_turn", "cost_usd": 2.002, "searches": 17, "fetches": 15} -->
# WP-X1: Cross-cutting, running cost inputs

### Findings

All pages were accessed 2026-11-11. Prices are USD list prices per million tokens (MTok) unless stated.

**Claude API (Anthropic)**

[confirmed Q6] Anthropic's pricing page (no page date shown) lists input / output per MTok: Claude Fable 5.2 $8 / $40, Claude Opus 5.5 $4 / $20, Claude Sonnet 5.5 $2 / $10, and Claude Haiku 5.5 $0.10 / $0.50 for prompts up to 100,000 tokens ($0.50 / $2.50 above that) {S43}.

[confirmed Q6] Prompt caching multipliers on base input are 1.25x for a 5-minute write, 2x for a 1-hour write, and 0.05x for a hit on Opus 5.5 and Sonnet 5.5 (0.025x on Fable 5.2) {S43}. In dollars, a cache hit is $0.20 on Opus 5.5 and $0.10 on Sonnet 5.5 {S43}.

[confirmed Q6] Asynchronous batch jobs on the Claude API cost half the standard input and output rate {S43}, which gives $2 / $10 for Opus 5.5 and $1 / $5 for Sonnet 5.5 {S43}. Batch and caching discounts stack {S43}.

[confirmed Q6] US-only routing costs 10% more across every token category for Claude 4.6 and later {S43}.

[confirmed Q6] The same text costs more tokens on current models: Anthropic reports about a 30% higher token count from the tokenizer used by Claude 4.7 and later {S43}.

[confirmed Q6] Claude Managed Agents sessions pay standard token rates plus $0.08 per session-hour while running {S43}, and get no batch discount {S43}.

**Microsoft Foundry**

[confirmed Q6] Claude in Microsoft Foundry has no separate rate card: Anthropic rates usage at the Claude API per-model prices, then converts to Claude Consumption Units (CCUs) at $0.01 each on the Azure Marketplace bill {S43}.

[confirmed Q6] Microsoft Learn (ms.date 2026-10-22) agrees: the CCU conversion uses Anthropic's published per-model token rates, after contractual discounts {S50}, and the page describes CCU as a billing-format change that leaves price untouched {S50}. Microsoft does not print the CCU dollar price; it points to the Claude offer on Azure Marketplace {S50}.

[confirmed Q6] US Data Zone Standard deployments in Foundry carry the same 1.1x multiplier as US-only inference on the Claude API {S43}.

[confirmed Q5] Foundry Claude spend is metered hourly, invoiced monthly in arrears, with no prepaid CCU credits {S50}, and counts against a Microsoft Azure Consumption Commitment {S50}.

[unverified Q6] Whether the 50% batch discount is available through Foundry is not stated on either fetched page. Next check: open https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry and look for Batch API support.

[unverified Q6] A search snippet of Microsoft Learn says subscriptions without an active pay-as-you-go billing method, such as free trial or startup-credit accounts, cannot use Claude in Foundry {S55}. I did not fetch the page. Next check: open https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude and confirm the billing type of Nihilo's two subscriptions.

**Amazon Bedrock**

[unverified Q6] AWS's Bedrock pricing page (updated 2026-11-09) did not render its Anthropic price tables when fetched, so no Bedrock per-token price is confirmed from AWS. Secondary lead: a 2026-11-01 reading of that page reports $4 / $20 for Opus 5.5 and $2 / $10 for Sonnet 5.5 on the global profile, with the EU profile 10% higher {S56}. Next check: open https://aws.amazon.com/bedrock/pricing/ in a browser, Anthropic tab, and record the Global and Geo/In-region rows.

[confirmed Q6] Anthropic's page supports the structure but not the numbers: regional and multi-region endpoints run 10% above global ones {S43}, and readers are sent to AWS and Google for official prices on those two platforms {S43}.

[confirmed Q6] Batch inference on Bedrock is priced 50% under on-demand, but only for selected models {S46}. AWS also notes that Sonnet 5.5 cache reads were cut by half from October 7, 2026 {S46}.

[confirmed Q6] AWS's batch-supported model list names Claude Opus 5, Claude Sonnet 4.6, and Claude Haiku 4.5 but has no row for Sonnet 5.5, Opus 5.5, or Haiku 5.5 {S51}. A secondary source says the same of the pricing table: batch cells for those three models read N/A {S57}. Do not budget a batch discount on Bedrock for current models.

**Google Cloud**

[confirmed Q6] Google's Partner Models pricing page (no page date; product labeled "Partner models on Agent Platform" {S49}) lists in its first table: Sonnet 5.5 $2 / $10 with batch $1 / $5 and cache hit $0.10; Opus 5.5 $4 / $20 with cache hit $0.20; Claude Haiku 5.5 $0.10 / $0.50 up to 100K input tokens; Claude Fable 5.2 $8 / $40 {S49}. The fetched text does not label tables by tab; I read the first as Global because Global is the first tab.

[confirmed Q6] The later tables on the same page are 10% higher: Sonnet 5.5 $2.20 / $11 and Opus 5.5 $4.40 / $22 {S49}.

[unverified Q6] Google's first table shows Opus 5.5 batch at $2.50 / $12.50 {S49}, which is not half of $4 / $20, while the later tables show $2.20 / $11 {S49}, exactly half the regional rate. This looks like a page error. Next check: look up the Opus 5.5 batch SKU in the Google Cloud billing SKU list.

**Azure services: what the vendor pages confirmed**

[unverified Q6] No Azure dollar list price could be confirmed. The fetched pricing pages for Container Apps, Azure Monitor, and Azure Functions show "$-" placeholders in every price cell {S44} {S45} {S52}, the Microsoft Sentinel page returned no price table, and the Azure Retail Prices API could not be fetched here. Next check: run the Azure pricing calculator for East US, or query https://prices.azure.com/api/retail/prices by service and region, and record each meter below.

[confirmed Q6] Each subscription gets a monthly Container Apps consumption allowance of 180,000 vCPU-seconds, 360,000 GiB-seconds, and 2 million requests {S44}. Apps scaled to zero cost nothing {S44}, and job executions bill at the active rate from start to finish {S44}.

[confirmed Q6] Adding a private endpoint to a Container Apps environment switches on the hourly Management meter that also applies to the Dedicated plan {S44}. Its price is unknown.

[confirmed Q6] Function apps share a per-subscription monthly allowance: 250,000 executions and 100,000 GB-s on Flex Consumption {S52}, or 1 million requests and 400,000 GB-s on the legacy Consumption plan {S52}.

[estimate Q6] The legacy Consumption rate works out to $0.000016 per GB-s. Basis: the pricing page's own example charges $17.6 for 1.1 million billable GB-s {S52}, and 17.6 / 1,100,000 = 0.000016.

[unverified Q6] Flex Consumption lead rates are $0.000026 per GB-s and $0.40 per million executions. A Microsoft Learn example uses these as assumed rates {S53}, the page was last updated 2025-10-30, and it tells readers to check the pricing page {S53}. Next check: pricing calculator, Functions, Flex Consumption, East US.

[confirmed Q12] Pay-as-you-go Analytics Logs ingestion carries a 5 GB monthly allowance per billing account {S45}. Free retention is 31 days for Analytics Logs, or 90 days once Microsoft Sentinel is enabled on the workspace {S45}, and paid retention runs to 2 years interactive and 12 years long-term {S45}.

[confirmed Q12] Turning on Sentinel in a simplified-tier workspace moves Analytics Logs ingestion onto Sentinel meters {S45}. Sentinel sells pay-as-you-go and commitment tiers from 100 GB per day {S48}, plus a 50 GB promotional tier in preview through December 31, 2026 {S48}.

**Azure services: lead prices from secondary sources (all unverified)**

[unverified Q6] Container Apps active usage lead: $0.000024 per vCPU-second in East US, per a secondary source citing the Azure Retail Prices API {S58}, and about $0.000003 per GiB-second {S59}. Next check: pricing calculator, Container Apps, Consumption.

[unverified Q6] Private endpoint lead: $0.01 per hour each (about $7.30 per month) plus $0.01 per GB processed {S60}. Next check: pricing calculator, Azure Private Link.

[unverified Q6] Key Vault lead: $0.03 per 10,000 operations, no base fee {S61}. Next check: pricing calculator, Key Vault Standard.

[unverified Q6] Service Bus lead: Basic $0.05 per million operations; Standard $0.0135 per hour (about $10 per month) with the first 13 million operations included {S62}. Whether private endpoints require the Premium tier was not checked. Next check: pricing calculator, Service Bus, plus the Service Bus networking doc on Microsoft Learn.

[unverified Q6] Blob Storage hot LRS lead: $0.018 per GB-month in East US {S63}. A second source quotes $0.0208 {S64}, which matches a Microsoft Learn sample price that the page calls fictitious {S54}, so I trust the lower figure more. Next check: pricing calculator, Storage Accounts, Block Blob, Hot, LRS.

[unverified Q12] Log Analytics lead: $2.30 per GB for Analytics Logs {S65} and $0.10 per GB-month for retention beyond the free window {S66}. Next check: pricing calculator, Azure Monitor, Log Analytics.

[unverified Q12] Microsoft Sentinel lead: $4.30 per GB pay-as-you-go in East US (read from the Retail Prices API on 2026-09-28) and $161.25 per day for the 50 GB tier {S67}. One source says this is a single combined meter, so the Log Analytics rate should not be added on top {S65}. Next check: Sentinel cost estimator at https://microsoft.com/en-us/security/pricing/microsoft-sentinel/cost-estimator.

**Worked monthly running cost**

[inference Q14] Volume assumptions are mine and untested. A "stage-run" is one ICM stage executed once, summing all model turns.

| Assumption | Small client | Mid-market client |
|---|---|---|
| Stage-runs per month | 200 | 5,000 |
| Tokens per stage-run (input / output) | 60,000 / 6,000 | 80,000 / 8,000 |
| Compute per stage-run | 5 min at 0.5 vCPU, 1 GiB | 5 min at 1 vCPU, 2 GiB |
| Logs ingested | 0.1 GB | 10 GB |
| Storage | 10 GB | 200 GB |
| Private endpoints | 0 | 5 |
| Queue and SIEM | none | Service Bus Standard, Sentinel on |

[estimate Q14] Small client tokens: 12 MTok input x $2 + 1.2 MTok output x $10 = $36 per month on Sonnet 5.5, or $72 on Opus 5.5 (12 x $4 + 1.2 x $20), using Anthropic's list rates {S43}. With caching (70% hits, 10% 5-minute writes, 20% uncached) Sonnet 5.5 drops to $20.64: 8.4 x $0.10 + 1.2 x $2.50 + 2.4 x $2 + $12 output.

[estimate Q14] Small client Azure cost is under $1. Compute is 30,000 vCPU-s and 60,000 GiB-s, inside the Container Apps free grant {S44}; logs sit inside the 5 GB allowance {S45}; storage is 10 GB x $0.018 = $0.18 at the unverified lead price. Total: about $37 per month, range about $21 to $72. Three private endpoints would add about $22 at the lead price.

[estimate Q14] Mid-market tokens: 400 MTok x $2 + 40 MTok x $10 = $1,200 per month on Sonnet 5.5, $2,400 on Opus 5.5, or $688 on Sonnet 5.5 with the same caching mix (280 x $0.10 + 40 x $2.50 + 80 x $2 + $400). US Data Zone adds 10% ($1,320 uncached), per the 1.1x multiplier {S43}.

[estimate Q14] Mid-market Azure cost is about $134 per month, built entirely on the unverified lead prices above:

| Item | Arithmetic | Monthly |
|---|---|---|
| Container Apps | (1,500,000 - 180,000) vCPU-s x $0.000024 + (3,000,000 - 360,000) GiB-s x $0.000003 | $39.60 |
| Private endpoints | 5 x $0.01 x 730 h | $36.50 |
| Service Bus Standard | $0.0135 x 730 h | $9.86 |
| Sentinel ingestion | 10 GB x $4.30 | $43.00 |
| Blob Storage | 200 GB x $0.018 | $3.60 |
| Key Vault | allowance | $1.00 |

Total with tokens: about $1,334 per month, range about $822 (cached) to $2,534 (all Opus 5.5).

[estimate Q6] Claude Managed Agents runtime for the same mid-market load would be 416.7 session-hours x $0.08 {S43} = $33.33, close to the Container Apps lead figure.

[inference Q14] The estimates exclude seat licenses (owned by WP-Q04A and WP-Q04B), the Container Apps Management meter, web search tool fees, egress, log retention beyond the free window, and Nihilo labor.

[inference Q5] Tokens are about 90% of mid-market running cost ($1,200 of $1,334) and about 97% for the small client. List prices are the same in either tenant. The one structural difference is that free grants are per subscription, so clients in a Nihilo-hosted subscription share one grant.

### Answer summary

**Q5 (operating cost and margin by hosting model).** [inference] Running cost does not separate the hosting models: about $37 per month for a small client and about $1,334 for a mid-market client under my assumptions, mostly tokens. In the Nihilo-hosted model Nihilo carries that bill and pays Foundry Claude usage monthly in arrears {S50}; in the client-tenant model the client pays it directly. Margin depends on service fees and labor, which this package does not cover.

**Q6 (model access terms and service costs).** Claude token prices are confirmed for the Claude API, for Foundry (same rates, billed as CCUs), and for Google Cloud's global endpoint. Bedrock prices are unverified from AWS's own page; leads say global rates match Anthropic and regional rates are 10% higher. Batch is confirmed at 50% off on the Claude API and listed on Google Cloud, not documented for current models on Bedrock, and unknown on Foundry. Azure service prices are unverified in dollars; billing structure and free grants are confirmed.

**Q14 (pricing basis).** [inference] Per-client running cost is small enough that pricing should be driven by labor and value, not infrastructure. The number to measure first is tokens per stage-run, because every estimate here scales linearly with it.

### Coverage checklist

- Per-token prices for current Claude models on the Anthropic API, Microsoft Foundry, Amazon Bedrock, and Google Cloud: partly covered. Anthropic, Foundry, and Google Cloud are confirmed from vendor pages; Bedrock is unverified because the AWS tables did not render.
- Batch and prompt caching discounts where the vendor page lists them: covered for Anthropic and Google Cloud (with one flagged anomaly); partly covered for Bedrock (structure only); not covered for batch on Foundry.
- List prices at small scale for the named Azure services: partly covered. Free grants, retention windows, and meter structure are confirmed; every dollar price is a secondary lead tagged unverified.
- Worked monthly running cost for one small and one mid-market client: covered, tagged estimate, assumptions stated. Token inputs are confirmed; Azure inputs are unverified leads.

### Open questions

1. Bedrock Claude prices from AWS. Next check: open https://aws.amazon.com/bedrock/pricing/ in a browser and record the Anthropic Global and Geo/In-region rows, including batch cells.
2. Azure dollar prices for Container Apps, Functions, Blob Storage, Key Vault, Private Link, Service Bus, Log Analytics, and Sentinel. Next check: Azure pricing calculator for East US, or the Retail Prices API, then rerun the two estimates.
3. Container Apps Management meter price when a private endpoint is used. Next check: pricing calculator, Container Apps, Dedicated plan management row.
4. Batch API on Foundry. Next check: Anthropic's Claude in Microsoft Foundry doc page, feature support section.
5. Google Cloud Opus 5.5 batch price ($2.50 / $12.50 versus an expected $2 / $10). Next check: Google Cloud billing SKU list.
6. Whether Nihilo's two Azure subscriptions can buy Claude in Foundry. Next check: confirm each subscription's billing type against the Microsoft Learn deployment prerequisites.
7. Service Bus tier needed for private endpoints. Next check: Microsoft Learn, Service Bus network security page.
8. Real tokens and compute seconds per stage-run. Next check: instrument the prototype and log usage per stage for one full workflow.

## Sources attached by the API

- S43: Pricing https://platform.claude.com/docs/en/about-claude/pricing
- S44: Azure Container Apps - Pricing | Microsoft Azure https://azure.microsoft.com/en-us/pricing/details/container-apps/
- S45: Pricing - Azure Monitor | Microsoft Azure https://azure.microsoft.com/en-us/pricing/details/monitor/
- S46: Amazon Bedrock Pricing – AWS https://aws.amazon.com/bedrock/pricing/
- S48: Microsoft Sentinel Pricing | Microsoft Security https://www.microsoft.com/security/pricing/microsoft-sentinel/
- S49: Partner Models Pricing https://cloud.google.com/model-garden/partner-models/pricing
- S50: Claude consumption units (CCU) billing in Microsoft Foundry - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-billing
- S51: Supported Regions and models for batch inference - Amazon Bedrock https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-supported.html
- S52: Pricing - Functions | Microsoft Azure https://azure.microsoft.com/en-us/pricing/details/functions/
- S53: Estimating consumption-based costs in Azure Functions https://learn.microsoft.com/en-us/azure/azure-functions/functions-consumption-costs?tabs=portal
- S54: Estimate the Cost of Using Azure Blob Storage https://learn.microsoft.com/en-us/azure/storage/blobs/blob-storage-estimate-costs
- S55: Deploy and use Claude models in Microsoft Foundry - Microsoft Foundry https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude
- S56: AWS Bedrock Pricing: Claude Costs and Budgets https://kevinwelter.com/en/blog/aws-bedrock-kosten
- S57: Amazon Bedrock Pricing: Model Rates and a $1,270 App Budget https://omidsaffari.com/blog/amazon-bedrock-pricing
- S58: Azure Container Apps Pricing: Consumption vs Dedicated, and the Idle Bill (2026) https://www.devzero.io/blog/azure-container-apps-pricing
- S59: Azure Container Apps Cost Optimization: The Essential Guide https://www.nops.io/blog/azure-container-apps-cost-optimization-guide/
- S60: Azure Private Link Pricing - Cost Breakdown & Savings Guide https://www.pump.co/blog/azure-private-link-pricing/
- S61: Azure Key Vault Pricing 2026: Standard vs Premium vs HSM - EnvManager https://envmanager.com/blog/azure-key-vault-pricing
- S62: Optimizing Azure Service Bus - Azure FinOps Essentials https://azure-finops-essentials.mindbyte.nl/p/azure-service-bus-tier-optimization
- S63: Azure Blob Storage Pricing: Full Cost Breakdown (2026) https://www.eon.io/blog/azure-blob-storage-pricing
- S64: Azure Storage Pricing Guide: Costs Explained & Examples https://www.lucidity.cloud/feeds/blog/azure-storage-cost
- S65: Microsoft Sentinel data tiers: what they cost, and what they cost you · Avalon Web Services https://www.awservices.org/blog/microsoft-sentinel-data-tiers-cost
- S66: Sentinel & ISOC Cost Planner https://sentinelcalculator.lockbasecyber.com/
- S67: Microsoft Sentinel Pricing Calculator 2026 — KeMeT Tech https://kemettech.net/tools/sentinel-cost-calculator

_164 search results consulted; 24 sources cited._
