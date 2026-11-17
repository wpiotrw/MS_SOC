---
layout: Conceptual
title: Monitor Cloud PCs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/monitor-cloud-pcs-overview
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about the new Monitor Cloud PCs page for Windows 365 Cloud PCs managed in Microsoft Intune, including how to use its dashboards, tabs, and filters.
keywords: Monitor Cloud PCs, reporting, monitoring, troubleshooting
author: rachellelcheung
ms.author: racheun
ms.date: 2026-09-29T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ai-usage: ai-assisted
ms.reviewer: mattsha
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure;
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: a3a54772-dc0e-bd77-2151-60608a665ac0
document_version_independent_id: a3a54772-dc0e-bd77-2151-60608a665ac0
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/monitor-cloud-pcs-overview.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/monitor-cloud-pcs-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/monitor-cloud-pcs-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 72a03d62-86a7-82b5-494c-71cdd7050085
---

# Monitor Cloud PCs | Microsoft Learn

Windows 365 monitoring gives you a unified view of Cloud PC connection health, performance, and configuration. Use these pages to monitor your environment, investigate user-reported issues, compare Cloud PCs, and identify trends that might require further attention.

- **Connection health** provides an environment-wide view of connection activity, reliability, sign-in performance, Cloud PC health, and network responsiveness.
- **Users and devices** provides detailed connection and performance data for individual users and Cloud PCs, including errors, CPU, memory, disk, and network activity.
- **Configuration monitoring** shows how connection activity is distributed across client platforms, deployment settings, Cloud PC configurations, operating-system versions, and application components.

Together, these pages support a progressive investigation workflow. Start with **Connection health** to identify broad patterns, use **Users and devices** to examine affected Cloud PCs, and review **Configuration monitoring** to determine whether the behavior is associated with a shared configuration.

Using the **View data** table, administrators can get even more granular details about connections.

## Access Monitor Cloud PCs

To access **Monitor Cloud PCs:**

1. Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com/).
2. Select **Devices**.
3. Under **Manage Windows 365 Cloud PCs**, select **Monitor Cloud PCs**.

Note

The legacy reports remain available under **Reports** &gt; **Cloud PC Overview** (under Windows 365).

Each monitoring page follows a top-to-bottom workflow. Selections made at the top of a page affect its charts, visualizations, and tables. Use these controls to define the population and time period that you want to analyze.

### Step 1: Select a page

Select the page that best matches your task:

| **Page** | Use |
| --- | --- |
| **Connection health** | Understand the performance and reliability of user connections across your environment. |
| **User and devices** | Review the detailed connection and performance history of a specific user or Cloud PC. |
| **Configuration monitoring** | Analyze end-to-end connection configurations across your environment or for a specific group of connections. |

### Step 2: Slice and filter the data

After selecting a page, refine the data displayed:

1. Select the **data series** that is most relevant to your analysis. Data-series options represent configuration attributes that can affect the Windows 365 connection experience.
2. Use the time-range picker to select the period that you want to analyze. Note that data freshness depends on the selected time range. Data for 2-hour and 4-hour ranges can be available with a latency of as little as 3 minutes. Longer time ranges will have higher data latency.
3. Apply client, service, and host configuration filters to focus on a specific group of connections, users, or Cloud PCs.
4. Review the charts and tables using the same selected context.

Note

Slicing and filtering help you create cohorts of connections, users, or devices that share selected characteristics. On the **User and devices** page, the cohort is already limited to connections associated with the selected user or Cloud PC.

### View detailed data

Select **View data** at the bottom of a monitoring page to examine the underlying tabular data. The available tables and columns depend on the current page.

The data shown in **View data** reflects the time range and page-level filters that you selected. Use table columns, sorting, filtering, and search to investigate individual connections and identify common characteristics among affected users or Cloud PCs.

## Understand monitoring data with Windows 365 Admin Assistant (preview)

You can use [Windows 365 Admin Assistant](https://go.microsoft.com/fwlink/?LinkId=2382618) in the Microsoft Intune admin center to ask natural-language questions about Cloud PC monitoring data. The Assistant helps you interpret connection metrics, compare groups of connections, and investigate patterns across connection history, health signals, and configuration data.

For example, you can ask:

- What does mean time to failure measure?
- How do connection failure rates compare across regions?
- What happened during [user UPN]'s most recent Cloud PC connection?
- Are connection failures associated with a particular client version or connection protocol?

Specify the user or Cloud PC, time range, and other details relevant to your question. Review the supporting data to validate the Assistant's explanation. A pattern or correlation doesn't necessarily identify the cause of an issue.

## Known limitations

- **Monitor Cloud PCs** pages don't refresh automatically. The displayed information reflects when the page was loaded or last refreshed.
- Data freshness depends on the selected time range. Data for 2-hour and 4-hour ranges can be available with a latency of as little as 3 minutes. Longer time ranges will have higher data latency.
- Only administrators whose roles have no scope tags assigned can access **Monitor Cloud PCs**.