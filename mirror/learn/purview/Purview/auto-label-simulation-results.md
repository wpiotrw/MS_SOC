---
layout: Conceptual
title: Review simulation results for auto-labeling policies in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/auto-label-simulation-results
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to review Microsoft Purview auto-labeling simulation results and decide whether a policy is ready for enforcement.
f1.keywords:
- NOCSH
ms.author: v-reezaali
author: ReezaAli149
manager: laurawi
audience: Admin
ms.service: purview
ms.subservice: purview-information-protection
ms.date: 2026-10-14T00:00:00.0000000Z
ms.collection:
- purview-compliance
ms.topic: article
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: 7af94d93-8ea0-aae3-e594-1e54c2b2f2aa
document_version_independent_id: 7af94d93-8ea0-aae3-e594-1e54c2b2f2aa
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/auto-label-simulation-results.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: auto-label-simulation-results
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/auto-label-simulation-results.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: cd2eacb4-6a4b-7261-2998-0fc0d3554d98
---

# Review simulation results for auto-labeling policies in Microsoft Purview | Microsoft Learn

Before you enforce an auto-labeling policy, run it in simulation mode. Simulation reports policy matches without applying or removing labels. Review the match results and source distribution to decide whether the policy is ready for enforcement.

This article describes the newer simulation overview page. Available fields and review options can vary by portal experience. To review policy results after you turn on a policy, see [Monitor your auto-labeling policy](apply-sensitivity-label-automatically#monitoring-your-auto-labeling-policy).

For existing SharePoint and OneDrive files, simulation uses available classification results. Restarting simulation reevaluates policy matches; it doesn't itself reclassify the content after a SIT change. See [Auto-labeling classification and simulation concepts](auto-label-classification-simulation) to distinguish direct SIT tests, classification refresh, and enforcement.

Important

Before you begin, make sure that you have the required roles and permissions. For more information, see [Policy-level labeling activity for SharePoint and OneDrive](apply-sensitivity-label-automatically#policy-level-labeling-activity-for-sharepoint-and-onedrive).

To view matched text in a file on **Items to review**, you also need the **Data Classification Content Viewer** role.

## Review the simulation overview

Make sure the policy is running in simulation mode and has started evaluating the configured locations. Then follow these steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com/).
2. Select **Solutions** &gt; **Information Protection** &gt; **Policies** &gt; **Auto-labeling policies**.
3. Select the name of a policy that is running in simulation mode.
4. In the policy details panel, select **Summary** &gt; **View details** to open the **Simulation overview** page.

On the **Simulation overview** page, the following key metrics about the policy are available:

| Field | Description |
| --- | --- |
| **Label** | The sensitivity label that the policy applies to matched items. |
| **Status** | Simulation status: **Simulation in progress**, **Simulation almost complete**, **Simulation complete**, **Simulation expiring soon**, **Expired**, or **Policy can't be published**. |
| **Duration** | The length of time the simulation has been running in days and hours. |
| **Matched items** | The total number of items that matched the policy conditions across all workloads. |
| **Sample items** | When displayed, the number of sampled items available for review. Samples are retained for 30 days. See Preserve results before editing or rerunning. |
| **Policy matches per rule** | Shows details about the policy rules and their matches:  - **Total Rules:** the number of rules in the policy, not the number of rules with matches.  - **Total Matches:** the number of items that matched rules. - **Rule name:** the name of the rule in the policy.  - **Matches:** the number of items that matched this rule.  - **Location:** The workload where matches occurred (Exchange, SharePoint, or OneDrive).  Use the per-rule match counts to identify which rules matched and whether each rule produces the expected results. |
| **Matches by source** | A donut chart showing matches distributed across workloads, with an item count and percentage for each of the following workloads:  - **Exchange**: Email messages that matched the policy. Matched Exchange items are based on sampled data and might not represent all mailboxes in the policy scope.  - **SharePoint**: Files in SharePoint sites that matched.  - **OneDrive**: Files in OneDrive accounts that matched. |
| **Sensitive info types** | This table lists the sensitive information types (SITs) detected across the matched items and the number of matches for each type. Use it to identify which SITs produce the most matches. |
| **Configuration details** | Shows the policy's locations, exclusions, and rule configuration. Review these details alongside the match results to check the policy scope. |
| **Review sample items** | Select **Review sample items**, when displayed, to open **Items to review**. For each item, you can:  - Preview the file or email content, where supported and with the required permissions.  - View properties such as the file location, modified date, and detected SITs.  - Read a **Contextual summary**, in supported portal experiences, that explains why the item matched. Viewing matched content requires the **Data Classification Content Viewer** role. |

Note

The **Matched items** count is an **estimate**, not a count of successfully labeled files. Enforcement results can differ because files or classification results change, other active policies affect the outcome, or labeling fails. For details, see [Simulation doesn't guarantee enforcement](auto-label-classification-simulation#simulation-doesnt-guarantee-enforcement).

## Preserve results before editing or rerunning

Before you edit an auto-labeling policy or restart simulation, export any available results that you need for later comparison. Check the exported file before you make changes.

Don't assume that sample retention guarantees access to results from earlier runs in the policy view or export. Export-size limits are separate from prior-run availability. Don't rely on filters or a larger export limit to recover results that are no longer available.