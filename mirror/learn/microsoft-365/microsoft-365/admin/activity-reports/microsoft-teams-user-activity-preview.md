---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Teams User Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-teams-user-activity-preview?view=o365-worldwide
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
- GAUpdates
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Microsoft Teams User activity report shows usage trends, meetings, calls, and messaging data. Learn how to access and interpret it in the Microsoft 365 admin center.
ms.date: 2026-07-07T00:00:00.0000000Z
locale: en-us
document_id: 9e8bbc80-90d7-5bb5-520d-87db92c10c16
document_version_independent_id: b69c7d34-18ed-b3a3-fc4e-7ed2ab86d5c5
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-teams-user-activity-preview.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-teams-user-activity-preview
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-teams-user-activity-preview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 59e3bd72-515b-4ad5-fd36-a0436815324b
---

# Microsoft Teams User Activity Report - Microsoft 365 admin | Microsoft Learn

The Microsoft Teams User activity report provides insights into the Microsoft Teams activity in your organization.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Microsoft Teams User activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft Teams**.
5. On the report page, select the **User activity** tab.

## Interpret the Microsoft Teams User activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

To ensure data quality, the system performs daily data validation checks for the past three days and fills any detected gaps. You might notice differences in historical data during this process.

[![Screenshot of the Microsoft Teams user activity report.](../../media/user-activity-charts.png)](../../media/user-activity-charts.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Microsoft Teams user activity report column options.](../../media/user-activity-columns.png)](../../media/user-activity-columns.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The exported format for **audio time**, **video time**, and **screen share time** follows ISO 8601 duration format.

| Metric | Mapped metric in export | Definition |
| --- | --- | --- |
| User name | User Principal Name | The email address of the user. You can display the actual email address or make this field anonymous. |
| Tenant name | Tenant Display Name | The name of an internal or external tenant where a user belongs.If a user belongs to an external tenant, corresponding data metrics like post messages or reply messages, are calculated based on their interactions in shared channels of the admin's tenant. Interactions done by the user in their own tenant (outside of shared channels of the given tenant) aren't considered for the admin usage report of given tenant. |
| Is external | Is External | Indicates if the user is an external user or not. |
| Shared channel tenant names | Shared Channel Tenant Display Names | The names of internal or external tenants of shared channels where the user participated. |
| Channel messages | Team Chat Message Count | The number of unique messages that the user posted in a team chat during the specified time period. This count includes original posts and replies. |
| Posts | Post Messages | The number of post messages in all channels during the specified time period. A post is the original message in a teams chat. |
| Replies | Reply Messages | The number of replied messages in all channels during the specified time period. |
| Urgent messages | Urgent Messages | The number of urgent messages during the specified time period. |
| Chat messages | Private Chat Message Count | The number of unique messages that the user posted in a private chat during the specified time period. |
| Total meetings | Meeting Count | Refer to the "Total participated meetings" metric, as defined later in this table, as the current metric and "Total participated meetings" share the same definition. The current metric is being gradually phased out in favor of "Total participated meetings." |
| 1:1 calls | Call Count | The number of 1:1 calls that the user participated in during the specified time period. |
| Last activity date (UTC) | Last Activity Date | The last date that the user participated in a Microsoft Teams activity. |
| Meetings participated ad hoc | Ad Hoc Meetings Attended Count | The number of unplanned meetings a user participated in during the specified time period. |
| Meetings organized ad hoc | Ad Hoc Meetings Organized Count | The number of unplanned meetings a user organized during the specified time period.**NOTE:** MeetNow meetings initiated from a chat are reflected in the Teams user activity report as "Ad Hoc Meetings Organized." MeetNow meetings initiated from Teams calendar are reflected in the Teams user activity report as "Scheduled One-Time Meetings Organized." |
| Total organized meetings | Meetings Organized Count | The sum of one-time scheduled, recurring, improvised, and unclassified meetings a user organized during the specified time period. |
| Total participated meetings | Meetings Attended Count | The sum of the one-time scheduled, recurring, unplanned, and unclassified meetings a user participated in during the specified time period. |
| Meetings organized scheduled one-time | Scheduled One-time Meetings Organized Count | The number of one-time scheduled meetings a user organized during the specified time period.**NOTE:** MeetNow meetings initiated from Teams calendar are reflected in the Teams user activity report as "Scheduled One-Time Meetings Organized." MeetNow meetings initiated from a chat are reflected in the Teams user activity report as "Ad Hoc Meetings Organized." |
| Meetings organized scheduled recurring | Scheduled Recurring Meetings Organized Count | The number of recurring meetings a user organized during the specified time period. |
| Meetings participated scheduled one-time | Scheduled One-time Meetings Attended Count | The number of the one-time scheduled meetings a user participated in during the specified time period. |
| Meetings participated scheduled recurring | Scheduled Recurring Meetings Attended Count | The number of the recurring meetings a user participated in during the specified time period. |
| Is licensed | Is Licensed | Selected if the user is licensed to use Teams. |
| Other activity | Has Other Action | The user is active but performed activities other than exposed action types offered in the report. For example, sending or replying to channel messages and chat messages, and scheduling or participating in 1:1 calls and meetings. Examples actions are when a user changes the Teams status or the Teams status message or opens a Channel Message post but doesn't reply. |
| Audio Duration | - | Same definition as "Audio Duration (In Seconds)" and formatted by ISO 8601 - Wikipedia |
| Video Duration | - | Same definition as "Video Duration (In Seconds)" and formatted by ISO 8601 - Wikipedia |
| Screen Share Session Duration | - | Same definition as Screen Share Session Duration (In Seconds) and formatted by ISO 8601 - Wikipedia |
| Audio Duration (In Seconds) | Audio Time (Min) | Total time the user participated in meetings or calls where audio was enabled. Counts the entire meeting or call duration if the user sent or received audio, not just time speaking or unmuted. Includes meetings initiated via screen share from Chat (SSFC) when audio is enabled. Applies to both senders and receivers; nonoptimized VDI clients might show nonzero minutes without active audio use. |
| Video Duration (In Seconds) | Video Time (Min) | Total time the user participated in meetings or calls where video was enabled. Counts the entire meeting or call duration if the user sent or received video, not just time the camera was on. Includes SSFC meetings when video is enabled. Applies to both senders and receivers; nonoptimized VDI clients might show nonzero minutes without active video use. |
| Screen Share Session Duration (In Seconds) | Screen Share Session Time (Min) | Total duration of sessions in which screen sharing occurred. If screen sharing took place at any point during a user session, the full session duration is included in this metric. This metric does not represent the exact amount of time content was actively shared. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

Note

- Metric counts include Teams client built-in features, but don't include changes to chat and channel through service integration, such as Teams app posts or replies and emails in the channel.
- Audio and video duration metrics represent participation time in meetings where audio or video was enabled, not active speaking or camera-on time.