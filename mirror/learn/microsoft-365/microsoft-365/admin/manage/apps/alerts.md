---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Create alerts for your apps - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/apps/alerts?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: App alerts help admins catch slow launches, usage spikes, and degraded health in Copilot Managed Runtime apps. Learn how to set up and manage alert rules.
author: arjunmayur
manager: alaug
ms.author: arjunmayur
ms.reviewer: mkaur
contributors: joshuapartlow
ms.date: 2026-11-17T00:00:00.0000000Z
ms.topic: concept-article
ms.service: microsoft-365
ms.subservice: managed-apps-admin
ai-usage: ai-assisted
locale: en-us
document_id: f4caf1ac-a620-7a83-9075-de3cb0284b3f
document_version_independent_id: f4caf1ac-a620-7a83-9075-de3cb0284b3f
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/apps/alerts.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/apps/alerts
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/apps/alerts.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 077045c6-31de-d4bf-efd9-02a07b3bf6b6
---

# Create alerts for your apps - Microsoft 365 admin | Microsoft Learn

[This article is prerelease documentation and is subject to change.]

Power Platform and Global admins can use alerts to track the operational health of their Copilot Managed Runtime apps. Admins set up custom thresholds and get notifications when metrics for their apps pass specific thresholds. Create alerts for any metric in the Monitor section under Apps in the Microsoft 365 admin center.

Important

- This is a preview feature.
- These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?LinkId=2373139), and are available before an official release so that customers can get early access and provide feedback.

Keep the following principles in mind:

- Alerts are evaluated after new metrics are produced. By default, all metrics are 24-hour aggregates, which means an alert rule with a 24 hour Data review period in the Monitor area is evaluated every 24 hours after the newest 24-hour aggregates are produced. However, you can also create an alert rule with a 1 hour Data review period. This enables an hourly aggregation on the app's metric the alert rule is configured with. Alert rules with a 24 hour Data review period do an on-demand evaluation upon their creation.
- Alert rules are alerts that admins create to monitor their apps. You can edit, delete, and turn an alert rule on or off. You can place alert rules on a specific app.
- A triggered alert occurs when an app an alert rule monitors pass specific thresholds that the admin defines when configuring the alert rule. You can select the triggered alert to learn what app triggered the alert rule.

## When to use alerts

- Teams and admins use alerts to find apps that are used more than expected. For example, an admin creates an alert to know if an app exceeds 50 launches a day.
- Teams use alerts to find apps with degraded health, and work with their makers to fix issues.
- For operations, admins create alerts to know if apps in their production environment are slow to open for users.

## Prerequisites

- You must be a Global or Power Platform admin to create, read, update, or delete alerts. AI Admins, Global Reader, and AI reader can view alert rules and triggered alert details, but they cannot create, update, or delete alert rules.

## Alert creation options

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
    - **Email**: You can specify up to 5 users (including security groups) to receive an email when the alert triggers. The email comes from **microsoft-noreply@microsoft.com** for alerts with a 24 hour review period and **azure-noreply@microsoft** for alerts with a 1 hour review period.
12. Select **Save**.

### Option 2: Create an alert from the All apps page

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
2. In the navigation pane, select **Apps**, and then select the **All apps** tab.
3. Select the app that you want to create an alert on. In the details pane, select the **Monitor** tab.
4. In the upper-left corner of the **Monitor** tab, select **+ New alert rule** .
5. When you select the **+ New alert rule** link to create an alert, the admin center autofills the information for the **Resource** field so you can create an alert on that specific app.
6. Fill in the information for the alert rule as listed in the **Create an alert from the Monitor page** section.

## Monitor critical resources with low-latency alerts (preview)

Use low-latency alerts to evaluate supported resource metrics every hour instead of waiting for the daily evaluation. These alerts can help you detect issues sooner on mission-critical applications and other resources.

For example, you can create a low-latency alert for a production app to check whether its **App open success rate** falls below 95%. The rule evaluates each hour after new hourly metrics are produced and can fire when the condition is met.

### How low-latency alerts work

By default, Monitor metrics refresh every 24 hours, and alerts evaluate those metrics after the new 24-hour aggregates are produced. When you create a low-latency alert with **Data review period** set to **1 Hour**, Monitor enables hourly aggregation for the selected metric on the selected app. The rule evaluates after new hourly metrics are produced and can fire each hour if its condition is met.

Hourly aggregation applies only to that app and metric. It doesn't enable hourly aggregation for every metric on the app. The metric summary on the left side of the app's Monitor tab in its detail pane continue to show 24-hour aggregates.

Hourly alert rules do not perform an on-demand evaluation when it's created since new hourly data isn't available.

Note

Low-latency alerts use an hourly refresh and evaluation schedule. They aren't real-time alerts.

### Requirements and limits

- Meet the existing alert prerequisites.
- Each tenant can configure up to 10 low-latency alerts. Reserve these alerts for mission-critical applications.
- You can configure only one low-latency alert per resource per metric. For example, you can't create two low-latency rules for the same app's **App open success rate**, even if their thresholds or severities differ.

### Supported products and metrics

Low-latency alerts support all metrics that Monitor supports for Copilot Managed Runtime apps.

### View hourly metrics and triggered alerts

After you create a low-latency alert, use the app's chart to view hourly data for the metric you selected:

1. Under **Apps** &gt; **All apps**, open the relevant app.
2. In the app details pane, select the **Monitor** tab and the metric or chart associated with the low-latency alert.
3. Set **Review period** to **1 hour** to view the metric's hourly time series. The only available chart time range for this review period is **24 hours**.
4. If the low-latency alert fired within the selected time range, a banner appears and indicates that it fired during the time range selected above the timeseries.

The alert's **Data review period** controls the data aggregation and scheduled evaluation cadence for the rule. The chart's **Review period** controls the aggregation shown in the chart. The chart time range controls how much history is displayed: for a **1 hour** review period, the chart displays **24 hours** of history.

The metric summary on the left side of the resource pane still shows 24-hour aggregates, even when you're viewing an hourly chart.

Note

A banner that indicates an alert fired within the selected time range doesn't, by itself, mean the alert is currently firing, that the issue is unresolved, or that the resource is experiencing an outage now.

## When an alert triggers

If you select to receive email notifications when any app triggers an alert, the user and/or groups you specified under the email notification option get an email when the alert fires.

In the **Monitor** experience, the **Triggered alerts** tab shows you a list of all the alerts in your tenant that triggered. The **Last triggered** column updates to the latest time that the alert triggered. Selecting a triggered alert shows you information about the alert rule configuration and what app triggered that alert. If an alert configured with a data review period of 1 hour didn't trigger for more than 24 hours, the triggered alert disappears from the *Triggered alerts* list. If an alert was configured with a data review period of 24 hours and didn't trigger for more than 48 hours, the triggered alert disappears from the list.

## How to manage alert rules

You can manage your alert rules by going to **Monitor** under **Apps** and then selecting the **Alert rules** tab. You can turn your alert rules on or off and edit and delete them. To edit or delete, select the menu option and select the desired action.

## Tips and best practices

Follow these best practices:

- **Start small**: Create a few high-value rules first, such as performance-open times, error rates, and usage spikes.
- **Name consistently**: Use clear names like **Prod – Copilot Managed Runtime – Availability &lt; 90**.
- **Set appropriate severity**: Use **High** for production-impacting metrics and **Medium** or **Low** for trend monitoring.
- **Manage the 60-rule limit**: Delete obsolete rules.
- **Choose data review period wisely**: Use the 1-hour option for mission-critical applications where you need to know as soon as possible when operational health degrades. Notifications for these alerts are sent out much more frequently compared to the 24-hour option.
- **Validate email routing**: Ensure recipients can receive emails from **azure-noreply@microsoft.com** and **microsoft-noreply@microsoft.com**.

## FAQ

### How many alert rules can I turn on at one time?

A tenant can have up to 60 alert rules total - up to 50 alert rules with a 24 hour data review period and up to 10 alert rules with a 1 hour data review period. Hourly alert rules that are turned off count towards the limit of 10. 24 hour alert rules that are turned off do not count towards the limit of 50. This limit encourages a focused set of high-value alerts. Over time, review and retire alert rules as underlying issues are resolved. If you reach this limit, consider cleaning up or consolidating existing rules.

### What's the difference between an alert rule and a triggered alert?

An *alert rule* is a monitoring rule you configure, including the metric, threshold, severity, and notification.

A *triggered alert* is an instance when an app meets the rule's condition. For example, the **Is under 90% for app open success rate** condition is met.

### Who can create and manage alerts?

You need a Global admin or Power Platform admin role to create and manage alerts. Read-only roles can view alert rules and triggered alerts. For which roles have each kind of access, see [Roles and responsibilities](roles-responsibilities).

### Does the severity level affect how alerts are processed?

The **Severity**, such as **Low**, **Medium**, or **High**, is a classification label for triage and reporting. It doesn't change evaluation frequency or email notification behavior.

### I created an hourly alert rule, why can't I see any data or alert triggering right after?

The first check runs after the first full hour, once there's at least one data point.

### Why are there gaps in the hourly chart?

An hour with no activity has no data point.

### Will I get an email every hour while the problem lasts?

You get an email as soon as a low-latency alert fires, then a reminder every four hours while the issue continues. Reminders stop when the issue resolves or after seven days, whichever comes first. If the issue comes back after it resolves, you get a new notification.

### Can I see more than 24 hours for hourly timeseries, or export hourly data?

No, the hourly chart covers the last 24 hours only and Monitor's data export feature only covers daily metric aggregates.

### Can hourly alerts be opted into the 'When an alert fires' trigger on the Power Platform for Admins V2 Connector?

At the moment, no, only alerts that have a 24-hour data review period can be opted in. Learn more: [Route alert notifications to any connector backed destination (preview)](/en-us/power-platform/admin/monitoring/alerts#route-alert-notifications-to-any-connector-backed-destination-preview)