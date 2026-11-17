---
layout: Conceptual
title: Use the Insights tab to analyze auto-labeling policies in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/auto-label-insights-tab
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use the Insights tab to review simulation findings and enforcement results for Microsoft Purview auto-labeling policies.
f1.keywords:
- NOCSH
ms.author: v-reezaali
author: ReezaAli149
manager: laurawi
audience: Admin
ms.service: purview
ms.subservice: purview-information-protection
ms.date: 2026-11-16T00:00:00.0000000Z
ms.collection:
- purview-compliance
ms.topic: article
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: b4bc11dd-6da9-975f-5c1c-0a97cf706227
document_version_independent_id: b4bc11dd-6da9-975f-5c1c-0a97cf706227
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/auto-label-insights-tab.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: auto-label-insights-tab
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/auto-label-insights-tab.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e93ec8b3-13be-122e-7e74-4baa1476263d
---

# Use the Insights tab to analyze auto-labeling policies in Microsoft Purview | Microsoft Learn

The **Insights** tab provides an at-a-glance view of an auto-labeling policy's performance directly in the policy details panel. Its contents vary depending on whether the policy is running in simulation or enforcement mode, helping you understand how the policy identifies or labels content.

This article describes the newer Insights layout. Available fields and review options can vary by portal experience.

Availability also depends on the policy's mode and locations:

- **Simulation:** The tab is available for policies that include Exchange, SharePoint, or OneDrive.
- **Enforcement:** The tab is available only when the policy includes SharePoint or OneDrive.

The tab isn't available for disabled policies or Exchange-only policies that are turned on. For an Exchange-only policy that's turned on, use [Activity explorer](data-classification-activity-explorer) to review email labeling activity.

For more information on simulation, see [Review simulation results for auto-labeling policies](auto-label-simulation-results). For more information on enforcement, see [Monitor your auto-labeling policy](apply-sensitivity-label-automatically#monitoring-your-auto-labeling-policy).

Important

Before you begin, make sure that you have the required roles and permissions. For more information, see [Policy-level labeling activity for SharePoint and OneDrive](apply-sensitivity-label-automatically#policy-level-labeling-activity-for-sharepoint-and-onedrive).

To open the Insights tab:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com/).
2. Select **Solutions** &gt; **Information Protection** &gt; **Policies** &gt; **Auto-labeling policies**.
3. Select a policy that is running in simulation mode or is turned on and includes SharePoint or OneDrive.
4. In the policy details panel, select **Insights**.
5. (Optional) Select **View details** to open the full policy overview. For policies in enforcement mode, earlier portal experiences might open Activity explorer instead.

**Simulation mode:** When the policy runs in simulation mode, the Insights tab shows a lightweight summary of the simulation findings. These findings include:

- General information about the policy, including **Label**, **Status**, **Duration**, **Results** (or total matches), and **Sample items**, when displayed.
- **Turn on date**, which shows scheduled automatic activation when configured; otherwise, no date is shown. This date isn't confirmation that activation succeeded. The separate **Start date/time** field shows the displayed simulation start date and time.
- **Rules and matches**, which shows the total number of rules in the policy and the total matches found. The rule total doesn't count only rules with matches. To identify which rules matched, select **View details** and review the per-rule match counts on the full simulation overview.
- **Matches by source**, which is a donut chart of matches across Exchange (purple), SharePoint (green), and OneDrive (blue).
- **Matches by sensitive info type**, which is a table listing each detected sensitive information type (SIT) and its match count.

Note

Exchange matched-item counts are estimates based on sampled data.

**Enforcement mode:** When the policy is actively labeling files, the Insights tab shows reported progress and labeling activity. Progress is periodically refreshed, while activity covers the last 30 days. These measures aren't directly interchangeable.

Note

Policy-level enforcement metrics and the **Labeled items** view report only files in SharePoint and OneDrive. They don't include Exchange email, including voicemail messages stored in Exchange. To verify labeling for an Exchange email, use [Activity explorer](data-classification-activity-explorer) and allow [60 to 90 minutes for the activity to appear](data-classification-activity-explorer#when-activities-appear).

| Field | Description |
| --- | --- |
| **Sensitivity label** | The sensitivity label applied by the policy. |
| **Status** | The current status of the policy. |
| **Turn on date** | The activation date and time displayed by the portal. Don't use this field as an immutable record of the policy's first activation. If the policy was edited after it was turned on, this date can show the most recent edit. |
| **Total labeled to date** | Reported labeling progress for SharePoint and OneDrive, based on periodically refreshed stored item and signal state for the policy. This isn't an immutable lifetime operation count or a real-time inventory of distinct files currently protected by the policy. |
| **Duration** | The number of days calculated from the displayed enforcement turn-on date. |
| **Last simulated results** | Estimated matches from the most recent simulation before enforcement was turned on. These estimates aren't a fixed target for enforcement. |
| **Completed on** | The date when the most recent simulation completed. |
| **Count of auto-labeled and failed files** | A donut chart of recorded labeling operations in the last 30 days, not distinct files: - **Labeled (green):** Successful labeling operations. - **Failed (red):** Failed labeling operations.The combined total includes both successful and failed operations. A file can contribute more than once, including a failure followed by a success. |
| **Labeling failures** | The card summarizes failed labeling activity in the last 30 days and shows the **Top 3 failure reasons**, sorted by volume. For more information, see [Resolve auto-labeling failures in SharePoint and OneDrive files](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/auto-labeling-failures-sharepoint-onedrive). |
| **Top 10 sensitive info types** | The table lists the sensitive information types (SITs) most frequently detected when this policy applied labels during the last 30 days. It includes the **Files labeled** count for each SIT. |
| **Labels per source** | A breakdown of successful and failed labeling activity in the last 30 days for SharePoint and OneDrive. Use it to identify whether failures are concentrated in a specific workload. |

For the daily trend, select **View details** and open **Overview** in the newer full review experience. **Labeling activity overview** shows separate successful and failed operation counts for the last 30 days, not distinct-file counts. For removal policies, the chart is **Label removal activity overview**. This chart isn't part of the newer Insights layout.

Review failure reasons even when few files fail. Transient infrastructure failures are retried automatically, but configuration, protection, or file format failures might require action regardless of volume. Some unsupported files require no action. Follow the reason-specific guidance in [Resolve auto-labeling failures in SharePoint and OneDrive files](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/auto-labeling-failures-sharepoint-onedrive).

Note

The Insights tab provides less data for non-Microsoft locations.

## Compare progress and labeling activity

Labeling activity counts recorded operations in the selected time window, not every file access, scan, evaluation, or retry. **Total labeled to date** uses refreshed stored state rather than a history of operations. Editing a policy doesn't necessarily reset its progress.

Before comparing counts, align the policy, workloads, scope, filters, UTC interval, observation time, and reporting freshness. Compare successful activity with successful progress, not the donut's combined successful-plus-failed total. A displayed **Turn on date** isn't proof of first-ever enforcement; check the policy's creation, enablement, and change history.

### Total labeled to date is lower than the 30-day count

Repeated actual labeling operations can count the same file more than once, for example when a label is applied and later changed. Deleting a file doesn't remove its historical activity. Changes to stored state, including file deletions, can reduce refreshed progress. Independent reporting delays or incomplete reports can also affect the comparison.

### Total labeled to date is higher than the 30-day count

Older activity can fall outside the activity window while still contributing to progress. Recent activity can also be delayed or missing from a report. For activity reporting information, see [Get started with Activity explorer](data-classification-activity-explorer).

If first-ever enforcement is verified to be within the last 30 days, older activity outside the window doesn't explain the gap. Check reporting freshness and completeness, how progress is calculated, and how failures are treated. Don't assume that successful activity must always equal or exceed reported progress, or that every mismatch is expected.

### Choose a measure for reporting

Use activity to report recent labeling operations and **Total labeled to date** to report progress as of its latest refresh. Neither measure alone proves the number of distinct files currently protected. Unavailable or partial reports don't mean that zero files were labeled.

For comparison examples and diagnostic and escalation guidance, see [Troubleshoot auto-labeling count mismatches](/en-us/troubleshoot/microsoft-365/purview/sensitivity-labels/troubleshoot-auto-labeling-policies#numbers-dont-agree-or-exchange-activity-is-missing).