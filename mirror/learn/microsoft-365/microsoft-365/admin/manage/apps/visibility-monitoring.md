---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Monitor the health of apps in Microsoft Copilot Managed Runtime (preview) - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/visibility-monitoring?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how to monitor the operational health of apps created in your solution.
ms.date: 2026-09-25T00:00:00.0000000Z
author: mikferland-msft
ms.author: miferlan
manager: zoraz
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
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 61dca861-fc8b-33be-c1b4-84c888dab23e
---

# Monitor the health of apps in Microsoft Copilot Managed Runtime (preview) - Microsoft 365 admin | Microsoft Learn

[This article is prerelease documentation and is subject to change.]

To measure and improve operational health metrics for apps in Copilot Managed Runtime for your organization, go to the **Monitor** page under **Apps** in the [Microsoft 365 admin center](https://admin.microsoft.com/AdminPortal/Home#/homepage).

Important

- This is a preview feature.
- These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?LinkId=2373139), and are available before an official release so that customers can get early access and provide feedback.

The following roles can access the **Monitor** experience: AI admin, AI reader, Global admin, Global reader, and Power Platform admin. All roles can use this experience to understand the aggregate operational health of apps in Copilot Managed Runtime that are created in their tenant. Global admin and Power Platform admin can create and manage alerts and see metrics. AI admin, AI reader, and Global reader can see metrics, but can only view alert rules and triggered alert details. They can't create and manage alert rules. Metrics are calculated by aggregating daily or hourly event logs from runtime activity. They're not real-time. For more information about which roles can manage apps and which roles are read-only, see [Roles and responsibilities](roles-responsibilities).

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

Admins can use *alerts* to track the operational health of their apps. Admins set up custom thresholds and get notifications when metrics for their apps pass specific thresholds. Create alerts on any metrics in the **Monitor** area of the Microsoft 365 admin center.

Best practices when setting up alerts for health metrics:

- The system evaluates alerts after it produces new metrics. Metrics are either 24-hour or 1-hour aggregates. This condition means an alert rule in the **Monitor** area is evaluated every 24 hours after the newest 24-hour aggregates are produced or every 1 hour after the newest 1-hour aggregate is produced. An alert rule does an on-demand evaluation upon its creation.
- In the alert configuration panel, you can change whether an alert considers the last 24 hours or last 1 hour worth of data by selecting 1 hour or 24 hours in the **Data review period** dropdown.
- Alert rules are alerts that admins create to monitor their apps. You can edit, delete, and turn an alert rule on or off. You can place alert rules on a specific app.
- A *triggered alert* occurs when an app passes the admin defined threshold of the alert rule that monitors it. You can select the triggered alert to learn which app triggered the alert rule and the value of its metric that triggered the rule.

### When to use alerts

- Admins use alerts to find apps that are used more than expected. For example, an admin creates an alert to know if an app exceeds 50 launches a day.
- Admins use alerts to find apps with degraded health, and work with their makers to fix issues.
- For operations, admins create alerts to know if apps are slow to open for users.

### Prerequisites

- You must be a Global admin or Power Platform admin to create and manage alert rules, and view triggered alert details. AI admin, AI reader, and Global reader can view alert rules and triggered alert details, but they can't create or manage alert rules.

### Create an alert for an app

You can create an alert for a specific app from either the **Monitor** page or the **All apps** page.

### Option 1: Create an alert from the Monitor page

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
2. In the navigation pane, select **Apps**, and then select the **Monitor** tab.
3. Select **+ New alert** to open the alert configuration panel.
4. In the **Alert rule name**, enter a name for the alert.
5. Select **Select resource**, and then select the app that you want to monitor.
6. In the **Metric** list, select the metric for the custom threshold. The available metrics are listed earlier in this article.
7. In the **Operator** list, select **Is Under**, **Is Over**, or **Equals**.
8. In the **Select value** use the arrows to set the threshold value.
9. **Data review period**: Specifies how far back the alert evaluates data.
    - **24 hours**: Evaluates data from the previous 24 hours.
    - **1 hour**: Evaluates data from the previous hour and enables hourly aggregation for the metric.
    - In the **Monitor** tab within the details pane of an app, you can view charts for both 24-hour and 1-hour aggregations on an app's metric if an alert was configured with the 1-hour data review period on that metric for that app. For example, if you configured an alert with a 1-hour data review period on an app's Time to Interactive metric, you could see 24-hour and 1-hour aggregations on the chart for the Time to Interactive metric for that app. Use the **Review period** list above the chart to switch between views.
10. In the **Severity** list, select **Low**, **Medium**, or **High**.
11. In the **Notification type**list, select one of the following options:
    - **None**: No email is sent. Return to the Monitor area to check the alert status.
    - **Email**: All Global and Power Platform admins receive an email when the alert triggers. The email comes from **microsoft-noreply@microsoft.com**.
12. Select **Save**.

### Option 2: Create an alert from the All apps page

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
2. In the navigation pane, select **Apps**, and then select the **All apps** tab.
3. Select the app that you want to create an alert on. In the details pane, select the **Monitor** tab.
4. In the upper-left corner of the **Monitor** tab, select **+ New alert rule** .
5. When you select the **+ New alert rule** link to create an alert, the admin center autofills the information for the **Resource** field so you can create an alert on that specific app.
6. Fill in the information for the alert rule as listed in the **Create an alert from the Monitor page** section.

### When an alert triggers

If you select to receive email notifications when any app triggers an alert, Global and Power Platform admins get an email notification.

In the **Monitor** experience, the **Triggered alerts** tab shows you a list of all the alerts in your tenant that have triggered. The **Last triggered** column updates to the latest time that the alert triggered. Clicking into a triggered alert shows you information about the alert rule configuration and what app triggered that alert. If an alert configured with a data review period of 1-hour hasn't triggered for more than 24 hours, the triggered alert disappears from the *Triggered alerts* list. If an alert was configured with a data review period of 24-hours and hasn't triggered for more than 48 hours, the triggered alert disappears from the list.

### How to manage alert rules

You can manage your alert rules by going to **Monitor** and then selecting the **Alert rules** tab. You can turn your alert rules on or off and edit and delete them. To edit or delete, select the menu option and select the desired action.

### Tips and best practices

Follow these best practices:

- **Start small**: Create a few high-value rules first, such as performance-open times, error rates, and usage spikes.
- **Name consistently**: Use clear names like **Prod – Copilot Managed Runtime – Availability &lt; 90**.
- **Set appropriate severity**: Use **High** for production-impacting metrics and **Medium** or **Low** for trend monitoring.
- **Manage the 10-rule limit**: Delete obsolete rules.
- **Choose data review period wisely**: Use the 1-hour option for mission-critical applications where you need to know as soon as possible when operational health degrades. Notifications for these alerts are sent out much more frequently compared to the 24-hour option.
- **Validate email routing**: Ensure recipients can receive emails from azure-noreply@microsoft.com.

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

You can view metric data for up to 28 days.

### How are time-based metrics calculated? For example, what percentile is used?

Time-based metrics report out the 75th percentile.

### How many alert rules can I turn on at one time?

A tenant can have up to 10 alert rules at a time (including both active and disabled rules). This limit encourages a focused set of high-value alerts. Over time, review and retire alert rules as underlying issues are resolved. If you reach this limit, consider cleaning up or consolidating existing rules.

### What's the difference between an alert rule and a triggered alert?

An *alert rule* is a monitoring rule you configure, including the metric, threshold, severity, and notification.

A *triggered alert* is an instance when an app meets the rule's condition. For example, the **Is under 90% for app open success rate** condition is met.

### Who can create and manage alerts?

You must be a Global admin or Power Platform admin to create and manage alerts.

### Does the severity level affect how alerts are processed?

The **Severity**, such as **Low**, **Medium**, or **High** is a classification label for triage and reporting. It doesn't change evaluation frequency or email notification behavior.