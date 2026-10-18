---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Teams Team Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-teams-usage-activity?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: cmcatee
author: cmcatee-MSFT
manager: scotv
ms.reviewer: hlu
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
ms.custom:
- campaignIDs-batch1
- GAUpdates
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Microsoft Teams Team usage report helps you track active users, channels, and meetings in Microsoft 365 admin center. Analyze team collaboration trends and boost performance.
ms.date: 2026-04-03T00:00:00.0000000Z
locale: en-us
document_id: 86e5dec5-c503-834b-9c2c-78a47d192fc6
document_version_independent_id: 86e5dec5-c503-834b-9c2c-78a47d192fc6
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-teams-usage-activity.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-teams-usage-activity
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-teams-usage-activity.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 2f323cde-d49b-3738-6b53-2d5bc1b5ec3a
---

# Microsoft Teams Team Usage Report - Microsoft 365 admin | Microsoft Learn

The Microsoft Teams Team usage report provides an overview of the usage activity in Teams, including the number of active users, channels, and messages. You can quickly see how many users across your organization are using Teams to communicate and collaborate. The report also includes other Teams-specific activities, like the number of active guests, meetings, and messages.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

[![Screenshot of the Microsoft Teams usage report.](../../media/teams-usage.png)](../../media/teams-usage.png#lightbox)

## View the Microsoft Teams Team usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft Teams**.
5. On the report page, select the **Team usage** tab.

## Interpret the Microsoft Teams Team usage report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

Note

Activity dates in this report are based on Coordinated Universal Time (UTC). Post counts attributed to a given day reflect messages sent between 12:00 AM and 11:59 PM UTC, which might differ from your organization's local time zone.

To ensure data quality, the system performs daily data validation checks for the past three days and fills any detected gaps. You might notice differences in historical data during the process.

Important

Data for a given day appears within 48 hours. For example, data for January 10th appears in the report by January 12th.

Use the Team usage report to view channel and team usage, including data about individual teams. The **Team usage** tab displays the following charts:

- **Channel usage**: Tracks the number of channel uses, by activity type, over time.

    [![Screenshot of the Microsoft Teams channel usage report. .](../../media/teams-usage-channel.png)](../../media/teams-usage-channel.png#lightbox)
- **Team usage**: Tracks the number of teams, by type and activity, over time.

    [![Screenshot of the Microsoft Teams team usage report.](../../media/teams-usage-usage.png)](../../media/teams-usage-usage.png#lightbox)

Additionally, the chart includes usage details for individual teams, such as last activity date, active users, active channels, and other data.

[![Screenshot of the Microsoft Teams usage table.](../../media/teams-usage-table.png)](../../media/teams-usage-table.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot showing the choose columns list in the Microsoft Teams usage report.](../../media/teams-usage-columns.png)](../../media/teams-usage-columns.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The exported format for **audio time**, **video time**, and **screen share time** follows ISO8601 duration format.

### Channel usage metrics

The Channel usage chart shows data about the following metrics.

| Metric | Definition |
| --- | --- |
| Active channel users | This metric is the total of internal active users, active guests, and external active users.<br>- **Internal active users** - Users that have at least one panel action in the specified time period. This metric excludes guests.<br>- **Active guests** - Guests that have at least one panel action in the specified time period. A guest is a person from outside your organization who accesses shared resources by signing in to a guest account in my directory.<br>- **External active user** - External participants that have at least one panel action in the specified time period. An external participant is a person from outside your organization who is participating in a resource - such as a shared channel - using their own identity and not a guest account in your directory. |
| Active channels | Valid channels in active teams that have at least one active user in the specified time period. This metric includes public, private, or shared channels. |
| Channel messages | The number of unique messages that the user posted in a private chat during the specified time period. |

Note

Panel action refers to any action taken by the user in the panel within Microsoft Teams.

### Team usage metrics

The Teams usage chart shows data on the following metrics.

| Metric | Definition |
| --- | --- |
| Private teams | A private team that is either active or inactive. |
| Public teams | A public team that is either active or inactive. |
| Active private teams | A team that's private and active. |
| Active public teams | A team that's public and active. |

### Teams details

You can view data for the following metrics for individual teams.

| Metric | Definition |
| --- | --- |
| Team ID | Team identifier |
| Internal active users | Users that have at least one panel action in the specified time period, including guests.Internal users and guests that reside in the same tenant. Internal users exclude guests. |
| Active guests | Guests that have at least one panel action in the specified time period.A guest is defined as persons from outside your organization who access shared resources by signing in to a guest account in my directory. |
| External active users | External participants that have at least one panel action in the specified time period.An external participant is defined as a person from outside your organization who is participating in a resource - such as a shared channel - using their own identity and not a guest account in your directory. |
| Active channels | Valid channels in active teams that have at least one active user in the specified time period. This metric includes public, private, or shared channels. |
| Active shared channels | Valid shared channels in active teams that have at least one active user in the specified time.A shared channel is defined as a Teams channel that you can share with people outside the team. These people can be inside your organization or from other Microsoft Entra organizations.**NOTE:** For shared channels that include external users, the report might undercount the number of active shared channels due to current telemetry limitations. |
| Total organized meetings | The sum of one-time scheduled, recurring, improvised, and unclassified meetings a user organized during the specified time period. |
| Posts | Count of all the post messages originally created in a channel during the specified time period. Cross-posted messages are counted only in the channel where they were originally created and aren't included in the post count of channels that received the cross-post. |
| Replies | Count of all the reply messages in channels in the specified time period. |
| Mentions | Count of all mentions made in the specified time period. |
| Reactions | Number of reactions an active user made in the specified time period. |
| Urgent messages | Count of urgent messages in the specified time period. |
| Channel messages | The number of unique messages that the user posted in a team chat during the specified time period. |
| Last activity date | The latest date that any member of the team committed an action. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

Note

Metric counts include Teams client built-in features, but don't include changes to chat and channel through service integration, such as Teams app posts or replies and emails in the channel.