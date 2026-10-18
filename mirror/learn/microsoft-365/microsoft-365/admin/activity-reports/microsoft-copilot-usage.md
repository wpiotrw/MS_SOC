---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Copilot Chat Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-copilot-usage?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: cmcatee
author: cmcatee-MSFT
manager: scotv
ms.reviewer: kols
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-copilot
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- m365copilot
- magic-ai-copilot
ms.custom:
- GAUpdates
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Microsoft Copilot Chat usage insights show active users, prompt counts, and app adoption across Teams, Outlook, and Microsoft Edge. Start tracking engagement now.
ms.date: 2026-07-10T00:00:00.0000000Z
locale: en-us
document_id: c41ea213-f810-a449-4480-dcdb94b696ef
document_version_independent_id: c41ea213-f810-a449-4480-dcdb94b696ef
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-copilot-usage.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-copilot-usage
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-copilot-usage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/aea41c7c-4aab-4537-be31-cf69a45a8878
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3ac528d8-7a58-4a01-8499-095fc1c5fb1b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 54127370-2fc0-91fb-197f-10373247df65
---

# Microsoft Copilot Chat Usage Report - Microsoft 365 admin | Microsoft Learn

The Microsoft Copilot Chat usage report provides insights into active usage of Microsoft Copilot Chat. The report includes total active users, average daily active users, total prompts submitted, and average prompts submitted per user. The report also shows the last activity date, prompts submitted, and active days per user, anonymized by default. For Copilot activity on a given day, the report typically becomes available within 48 hours of the end of that day (in UTC). To view all reports, see [Microsoft 365 Reports in the admin center overview](activity-reports).

## Watch: Track adoption with the Microsoft Copilot Chat usage report

Note

The report currently supports only users without a Microsoft Copilot license who interact with Copilot Chat in Teams, Outlook, m365.cloud.microsoft/chat, Microsoft Copilot (app), Microsoft Edge, Word, Excel, PowerPoint, and OneNote.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Microsoft Copilot Chat usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft Copilot**, and then select **Copilot Chat**.

## Interpret the Microsoft Copilot Chat usage report

Use this report to see the usage of Microsoft Copilot Chat in your organization. At the top, filter by different periods. You can view the Microsoft Copilot Chat report over the last 7, 28, 90, or 180 days.

[![Screenshot showing the number of active users for Microsoft Copilot Chat usage.](../../media/copilot-chat-usage.png)](../../media/copilot-chat-usage.png#lightbox)

- **Active users** shows the total number of users who submitted at least one prompt to Microsoft Copilot Chat during the selected period.
- **Average daily active users** indicates the average number of people using Microsoft Copilot Chat per day over the selected period.
- **Total prompts submitted** refers to the overall number of prompts users sent to Microsoft Copilot Chat during the selected period.
- **Average prompts submitted per user** represents the mean number of prompts each active user sent to Microsoft Copilot Chat during the selected period.

In **Recommendations**, the recommended action card highlights where admins can update settings to pin Copilot to make it easier for users in the organization to find and use Copilot in apps like Teams and Outlook.

[![Screenshot showing the pop-up message to pin Copilot for all users.](../../media/microsoft-copilot-pin.png)](../../media/microsoft-copilot-pin.png#lightbox)

You see the following summary charts in this report as default view:

[![Screenshot showing the chart to evaluate adoption by app for Microsoft Copilot Chat.](../../media/copilot-chat-summary.png)](../../media/copilot-chat-summary.png#lightbox)

- **Summary view** shows you the total usage of Microsoft Copilot Chat of the time frame.
- **Trend view** shows you the daily time trend of Microsoft Copilot Chat of the time frame.

You can switch between **Summary** view and **Trend** view. When switching to **Trend** view, you can select one or multiple entry points in the dropdown list to see daily usage or compare among entry points.

[![Screenshot showing the chart in Trend view to analyze adoption by app for Microsoft Copilot Chat.](../../media/copilot-chat-adoption.png)](../../media/copilot-chat-adoption.png#lightbox)

The following table shows app details for active Microsoft Copilot Chat users:

| App | Details | More information |
| --- | --- | --- |
| Edge | Microsoft Copilot Chat was used from the sidebar in the Microsoft Edge browser. | [Copilot - Microsoft Edge](https://www.microsoft.com/edge/features/copilot) |
| Microsoft Copilot (app) | Microsoft Copilot Chat was used in the desktop, mobile, or web version of the Microsoft Copilot (app), including the following entry points: Microsoft365.com, Office.com, M365Copilot.com, Microsoft 365 desktop app, Microsoft 365 mobile app, M365.cloud.microsoft | [Overview of Microsoft Copilot Chat](/en-us/copilot/overview) |
| Teams | Microsoft Copilot Chat was used in Teams. | [Manage Copilot Chat in Teams](/en-us/copilot/manage#manage--chat-in-teams) |
| Outlook | Microsoft Copilot Chat was used in Outlook. | [Manage Copilot Chat on the web, in the Microsoft Copilot app, and in Outlook](/en-us/copilot/manage#manage--chat-on-the-web-in-the-microsoft-365--app-and-in-outlook) |
| m365.cloud.microsoft/chat | Microsoft Copilot Chat was used in m365.cloud.microsoft/chat. | [Manage Microsoft Copilot Chat](/en-us/copilot/manage#how-to-ensure-users-access--chat) |
| Word | Microsoft Copilot Chat was used in Word. | [Overview of Microsoft Copilot Chat](/en-us/copilot/overview) |
| Excel | Microsoft Copilot Chat was used in Excel. Edit mode in Excel isn't currently included in active usage metrics. Support for this mode might be added in a future release. | [Overview of Microsoft Copilot Chat](/en-us/copilot/overview) |
| PowerPoint | Microsoft Copilot Chat was used in PowerPoint. Edit mode in PowerPoint isn't currently included in active usage metrics. Support for this mode might be added in a future release. | [Overview of Microsoft Copilot Chat](/en-us/copilot/overview) |
| OneNote | Microsoft Copilot Chat was used in PowerPoint. | [Overview of Microsoft Copilot Chat](/en-us/copilot/overview) |

You can view a table that shows each active user who accessed Microsoft Copilot Chat over the past 180 days.

[![Screenshot showing the table list of data for active users for Microsoft Copilot Chat.](../../media/microsoft-copilot-export.png)](../../media/microsoft-copilot-export.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

### User last activity table

| Metric | Definition |
| --- | --- |
| **Username** | The user's principal name. |
| **Display name** | The full name of the user. |
| **Prompts submitted** | The total number of prompts submitted by this user to Microsoft Copilot Chat during the specified period. |
| **Active days** | The total number of days the user submitted prompts to Microsoft Copilot Chat within the specified timeframe. |
| **Last activity date (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat in Teams, Outlook, m365.cloud.microsoft/chat, Microsoft Edge, the Microsoft Copilot (app), Word, Excel, PowerPoint, or OneNote. This date remains fixed even if the timeframe of the report is changed. |
| **Last activity date of Teams (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat in Teams. This date remains fixed even if the timeframe of the report is changed. |
| **Last activity date of Outlook (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat in Outlook. This date remains fixed even if the timeframe of the report is changed. |
| **Last activity date of m365.cloud.microsoft/chat (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat in m365.cloud.microsoft/chat. This date remains fixed even if the timeframe of the report is changed. |
| **Last activity date of Microsoft Copilot (app) (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat in Microsoft Copilot (app). This date remains fixed even if the timeframe of the report is changed. |
| **Last activity date of Edge (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat from the sidebar in the Microsoft Edge browser. This date remains fixed even if the timeframe of the report is changed. |
| **Last activity date of Word (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat in Word. This date remains fixed even if the timeframe of the report is changed. |
| **Last activity date of Excel (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat in Excel. This date remains fixed even if the timeframe of the report is changed. |
| **Last activity date of PowerPoint (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat in PowerPoint. This date remains fixed even if the timeframe of the report is changed. |
| **Last activity date of OneNote (UTC)** | The most recent date on which the user sent a message to Microsoft Copilot Chat in OneNote. This date remains fixed even if the timeframe of the report is changed. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

## FAQ

### Does this report include only the Copilot Chat usage for users without a Microsoft Copilot license in the organization?

Yes. To view Copilot Chat usage for Microsoft Copilot licensed users in the organization, see the [Microsoft Copilot usage report](microsoft-365-copilot-usage) in the Microsoft 365 admin center.