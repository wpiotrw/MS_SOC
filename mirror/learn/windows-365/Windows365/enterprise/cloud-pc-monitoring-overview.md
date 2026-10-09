---
layout: Conceptual
title: Cloud PC monitoring overview (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/cloud-pc-monitoring-overview
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about the new Cloud PC monitoring and reporting platform for Windows 365 Cloud PCs managed in Microsoft Intune, including how to use its dashboards, tabs, and filters during public preview.
keywords: 
author: DougCoombs
ms.author: docoombs
manager: dougeby
ms.date: 2026-03-31T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
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
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/cloud-pc-monitoring-overview.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/cloud-pc-monitoring-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/cloud-pc-monitoring-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 9487a31d-a082-e520-6937-b54cc93ffe1d
---

# Cloud PC monitoring overview (preview) | Microsoft Learn

Important

Cloud PC monitoring is in public preview. Preview features are tagged with **(preview)** in the admin user interface and might have restricted or limited functionality. These features are subject to change before general availability (GA) and are fully supported by Microsoft. Preview features are considered unfinished, might not be suitable for production workloads, and should be used with caution.

This overview is intended for Intune administrators who monitor and troubleshoot Windows 365, as well as help desk and operations center engineers. It explains how to use the Windows 365 monitoring and reporting platform for Cloud PCs managed in Microsoft Intune. This feature is available in public preview.

For the latest information and to engage with the community, see the [Windows 365 public preview documentation](/en-us/windows-365/public-preview).

Cloud PC monitoring introduces an entirely new reporting and monitoring experience that provides:

- **Tenant-level operations analysis, help desk detail, and end-to-end configuration details** — enabling both broad monitoring and targeted investigation from a single interface.
- **Rich visualizations** — interactive charts for key connection metrics, including counts, failure rates, latencies, and health trends.
- **Flexible data series and filters** — change how data is grouped (for example, by region, client type, or OS version) and apply filters to isolate specific cohorts and accelerate troubleshooting.
- **Contextualized data for multi-dimensional analysis** — selections made at the top of the page (tab, data series, time range, and filters) cascade to all components below, including visualizations and tables.
- **Detailed tabular data** — access performance, connection configuration, connection events, and connection error data through the **View data** fly-out on every page.

## Access Cloud PC monitoring

To access Cloud PC monitoring, sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431) and select **Reports** &gt; **Cloud PC monitoring (preview)**.

Note

The legacy reports remain available under **Reports** &gt; **Cloud PC overview**.

The monitoring page is organized for an intuitive top-to-bottom flow. A selection made at the top of the page affects nearly all data and components on the page, including visualizations and tables. This lets you create the context and focus needed for any scenario.

![Screenshot that shows Cloud PC monitoring connection health page.](media/cloud-pc-monitoring/cloud-pc-monitoring-connection-health.png)

### Step 1: Select a tab

Choose the tab that matches your task:

| Tab | Use |
| --- | --- |
| **Connection health** | Understand the performance and reliability of user connections across your tenant. |
| **User and devices** | Investigate the detailed history of specific users or devices. Useful for help desk scenarios. |
| **Configuration monitoring** | Understand end-to-end connection configurations aggregated across your environment or for a specific connection or set of connections. |

### Step 2: Slice and filter data

After selecting a tab, refine the data shown on the page:

1. Set the **data series** to the configuration variable that's most relevant to your analysis. Data series options reflect variables that commonly affect Windows 365 and Cloud PCs.
2. Use the **time range** picker to select the time period you want to analyze.
3. Apply **filters** based on client, service, and host configuration variables to focus on specific cohorts for troubleshooting and analysis.

Note

Slicing and filtering options are designed to develop a cohort of like groups of entities (connections, users, devices, etc.). For User and Devices the cohort has already been isolated to connections pertaining to a single user or device.

## Known limitations

- Monitoring pages don't automatically refresh. The information shown reflects the time when the page was loaded or last refreshed.
- Connection data can be delayed by up to 15 minutes and is provided at a 2-minute granularity.
- Cloud PC health data can be delayed by up to 30 minutes and is provided at approximately 30-minute granularity.
- Aggregate metrics, such as Mean time to failure, are averaged over time. Their delay and granularity depend on how frequently the averages are calculated.