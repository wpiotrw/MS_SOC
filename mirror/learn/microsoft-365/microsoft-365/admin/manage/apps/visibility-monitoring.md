---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Monitor the health of apps in Microsoft Copilot Managed Runtime - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/visibility-monitoring?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how to monitor the operational health of apps created in your solution.
ms.date: 2026-11-17T00:00:00.0000000Z
author: arjunmayur
ms.author: arjunmayur
manager: alaug
ms.reviewer: mkaur
ms.topic: concept-article
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ai-usage: ai-assisted
locale: en-us
document_id: 883c45fd-9998-e628-7ffd-ffbedf29b9ee
document_version_independent_id: 883c45fd-9998-e628-7ffd-ffbedf29b9ee
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/visibility-monitoring.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/visibility-monitoring
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/visibility-monitoring.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 61dca861-fc8b-33be-c1b4-84c888dab23e
---

# Monitor the health of apps in Microsoft Copilot Managed Runtime - Microsoft 365 admin | Microsoft Learn

To measure and improve operational health metrics for apps in Copilot Managed Runtime for your organization, go to the **Monitor** page under **Apps** in the [Microsoft 365 admin center](https://admin.microsoft.com/AdminPortal/Home#/homepage).

Both Manage and read-only roles can access the **Monitor** experience and use it to understand the aggregate operational health of apps in Copilot Managed Runtime that are created in their tenant. Manage roles can see metrics and create and manage alerts. Read-only roles can see metrics and view alert rules and triggered alert details, but they can't create or manage alert rules. Metrics are calculated by aggregating daily or hourly event logs from runtime activity. They're not real-time. For more information about which roles can manage apps and which roles are read-only, see [Roles and responsibilities](roles-responsibilities).

This article helps you understand the apps inventory and monitor application health.

## Architecture

To produce health metrics and generate recommendations, the **Monitor** experience requires runtime activity. Unused apps don't have metrics.

[![Diagram of the backend architecture of Monitor in the Microsoft 365 admin center](media/mac-monitor-architecture.png)](media/mac-monitor-architecture.png#lightbox)

## Monitor use cases

The purpose of the **Monitor** area of the Microsoft 365 admin center is to bring attention to apps in Copilot Managed Runtime that have degraded operational health and highlight apps that have opportunities for improvement.

## View an app's health metrics

1. Go to the **All apps** list page under **Apps** in the Microsoft 365 admin center.
2. Select a specific app to open the details pane.
3. Within the pane, select the **Monitor** tab to view operational health metrics and a time-series chart for each available metric.

## Available metrics for apps in Copilot Managed Runtime

The **Monitor** experience provides the following operational health metrics for apps in Copilot Managed Runtime.

| Metric | Definition | Support |
| --- | --- | --- |
| App open success rate | A percentage that describes how often end users can successfully open the app. | Preview |
| Time to interactive (TTI) | The time (in seconds) it takes for a screen to become interactive after it starts loading. | Preview |
| App session count | The number of distinct user sessions in an app in one day. A session begins when a user opens the app and ends after a period of inactivity or when the app is closed. | Preview |
| Data request success rate | A percentage that describes how often data requests coming from an app are successful. | Preview |
| Data request latency | The average time (in seconds) it takes for all data requests made by the app to complete during a session. | Preview |

## Create alerts for your apps

Admins can use *alerts* to track the operational health of their apps. Admins set up custom thresholds and get notifications when metrics for their apps pass specific thresholds. Create alerts on any metrics in the **Monitor** area of the Microsoft 365 admin center. See [Create alerts for your apps](alerts) for more details

## FAQs

### How does Monitor in the Microsoft 365 admin center coexist with Application Insights?

**Monitor** in the Microsoft 365 admin center doesn't require Azure subscriptions.

Application Insights contains a superset of runtime event logs.

- It contains event logs that are beyond the scope of Monitor's app metrics.
- It allows for customer-defined data retention.
- It allows for custom traces, which support custom events, metrics, and dimensions.
- Event logs can be correlated and joined across apps that emit data to the same Application Insights instance.

### How frequently are metrics updated and what determines their aggregation rate?

Metrics aggregate at a point in time, according to their aggregation rate. The default aggregation rate is every 24 hours. For example, the **App open success rate** metric calculates daily and has only one value per day. If there's an alert that has a data review period of an hour, metrics calculate hourly. See the alert section for more details.

### How far back can I view metric data?

You can view metric data for up to 28 days for 24 hour aggregates.

### How are time-based metrics calculated? For example, what percentile is used?

Time-based metrics report out the 75th percentile.