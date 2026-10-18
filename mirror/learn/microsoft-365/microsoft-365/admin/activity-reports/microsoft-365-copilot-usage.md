---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Copilot Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage?view=o365-worldwide
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
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-copilot
ms.update-cycle: 180-days
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- m365copilot
- magic-ai-copilot
ms.custom:
- campaignIDs-batch1
- GAUpdates
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Microsoft Copilot usage report helps admins measure user adoption, prompt activity, and agent engagement. Explore key metrics and insights today.
ms.date: 2026-07-14T00:00:00.0000000Z
locale: en-us
document_id: 3a319e42-09b0-2774-66de-ac6b2de894f8
document_version_independent_id: 3a319e42-09b0-2774-66de-ac6b2de894f8
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-365-copilot-usage
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-365-copilot-usage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: d3d688f2-7d6a-e315-3dd7-7979a384c2e2
---

# Microsoft Copilot Usage Report - Microsoft 365 admin | Microsoft Learn

The Microsoft Copilot usage report provides a summary of how users adopt, retain, and engage with Microsoft Copilot and its associated enabled apps. For Copilot activity on a given day, the report typically becomes available within 48 hours of the end of that day (in UTC).

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Microsoft Copilot usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft Copilot**, and then select **Copilot**.
5. On the report page, select the **Usage** tab to view adoption and usage metrics.

## Interpret the Microsoft Copilot usage report

At the top, you can filter by different timeframes. You can view the Microsoft Copilot report over the last 7, 28, 90, or 180 days.

You can view several numbers for Microsoft Copilot usage, which highlight the enablement number and the adoption of the enablement:

[![Screenshot showing Microsoft Copilot usage summary information.](../../media/copilot-usage-hero.png)](../../media/copilot-usage-hero.png#lightbox)

- **Enabled Users** shows the total number of unique users in your organization with Microsoft Copilot licenses over the selected timeframe.
- **Active Users** shows the total number of enabled users in your organization who tried a user-initiated Microsoft Copilot feature, in one or more apps in Microsoft 365 over the selected timeframe.
- **Active users rate** shows the number of active users in your organization divided by the number of enabled users.

In **Recommendations**, the recommended action card highlights [Microsoft Copilot Dashboard](/en-us/viva/insights/org-team-insights/copilot-dashboard), where you can deliver insights to your IT leaders to explore Copilot readiness, adoption, and impact in Viva Insights.

- **Total prompts submitted** shows the total number of prompts users sent to Microsoft Copilot Chat during the selected time frame.
- **Average prompts submitted per user** represents the mean number of prompts each active user sent to Microsoft Copilot Chat during the selected timeframe.

In the **Adoption** section, **Adoption by app** shows enabled users and active users of Copilot in Microsoft 365 apps.

You see the following summary charts in this report as default view:

[![Screenshot showing Microsoft Copilot usage adoption chart.](../../media/m365-copilot-adoption.png)](../../media/m365-copilot-adoption.png#lightbox)

The definitions for **Enabled Users** and **Active Users** metrics are the same as provided earlier.

- **Summary view** shows the total usage of Microsoft Copilot apps of the time frame.
- **Trend view** shows the daily time trend of Microsoft Copilot apps of the time frame.

When switching to **Trend** view, you can select one product in the dropdown list to see daily usage.

[![Screenshot showing the dropdown list of products for Microsoft Copilot adoption chart.](../../media/copilot-usage-trend-view2.png)](../../media/copilot-usage-trend-view2.png#lightbox)

In the **Prompts submitted** section, **Summary view** shows the total number of prompts users submitted to Microsoft Copilot Chat over the selected time frame.

[![Screenshot showing the summary view of prompts submitted for the Microsoft Copilot adoption chart.](../../media/copilot-usage-prompts-submitted-summary.png)](../../media/copilot-usage-prompts-submitted-summary.png#lightbox)

**Trend view** shows the daily trend of prompts submitted in Microsoft Copilot over the selected time frame.

[![Screenshot showing the trend view of prompts submitted for the Microsoft Copilot adoption chart.](../../media/copilot-usage-prompts-submitted-trend.png)](../../media/copilot-usage-prompts-submitted-trend.png#lightbox)

**Copilot Chat adoption** shows enabled users and total usage of Copilot Chat and split usage between Copilot Chat (work) and Copilot Chat (web).

[![Screenshot showing the business chat usage chart in the Microsoft Copilot usage report.](../../media/m365-copilot-chat-adoption.png)](../../media/m365-copilot-chat-adoption.png#lightbox)

The following table lists the features for active users of Copilot apps:

| Copilot app | Features | How to use | Learn more about the feature |
| --- | --- | --- | --- |
| Microsoft Edge | Copilot Chat (web) | Type a message into the chat window or select a suggested prompt and submit. Or select **Ask Copilot** in the right-click of contextual web info. | [Copilot - Microsoft Edge](https://www.microsoft.com/edge/features/copilot?msockid=057d787df18f67b829a16cd9f58f6564&amp;form=MA13FJ&amp;ch=1) |
|  | Copilot Chat (work) | Type a message into the chat window or select a suggested prompt and submit. | [Copilot - Microsoft Edge](https://www.microsoft.com/edge/features/copilot?msockid=057d787df18f67b829a16cd9f58f6564&amp;form=MA13FJ&amp;ch=1) |
| Microsoft Copilot (app) | Copilot Chat (web) | Type a message into the chat window or select a suggested prompt and submit. | [Get started with Microsoft Copilot Chat](https://support.microsoft.com/topic/get-started-with-microsoft-365-copilot-business-chat-5b00a52d-7296-48ee-b938-b95b7209f737) |
|  | Copilot Chat (work) | Type a message into the chat window or select a suggested prompt and submit. | [Get started with Microsoft Copilot Chat](https://support.microsoft.com/topic/get-started-with-microsoft-365-copilot-business-chat-5b00a52d-7296-48ee-b938-b95b7209f737) |
| Outlook | Summarize an Outlook email thread | In an email thread, select **Summarize by Copilot** or **Summarize** at the top of the email thread. (User experience is slightly different among web, Windows, Mac, or mobile.) | [Summarize an email thread with Copilot in Outlook - Microsoft Support](https://support.microsoft.com/office/summarize-an-email-thread-with-copilot-in-outlook-a79873f2-396b-46dc-b852-7fe5947ab640#ID0EBBJ=New_Outlook) |
|  | Generate an Outlook email draft | Select Copilot icon from the toolbar, select **Draft with Copilot**, type a prompt in Copilot box, and submit. (User experience is slightly different among web, Windows, Mac, or mobile.) | [Draft an email message with Copilot in Outlook - Microsoft Support](https://support.microsoft.com/office/draft-an-email-message-with-copilot-in-outlook-3eb1d053-89b8-491c-8a6e-746015238d9b#ID0EDBH=New_Outlook) |
|  | Coach | Select the Copilot icon in the email message, and then select **Coaching by Copilot**. Copilot reviews email and offers suggestions on improving the tone, clarity, and reader sentiment. (User experience is slightly different among web, Windows, Mac, or mobile.) | [Email coaching with Copilot in Outlook - Microsoft Support](https://support.microsoft.com/office/email-coaching-with-copilot-in-outlook-91a3cd56-1586-4a31-85c7-2eb8cdb02405) |
|  | Copilot Chat (work) | Go to the left side of Outlook web app, select Copilot from the apps list, type a prompt, and send. This feature is included in the Outlook app level and all up Microsoft 365 active usage count effective August 28, 2024. | [Get started with Microsoft Copilot Chat](https://support.microsoft.com/topic/get-started-with-microsoft-365-copilot-business-chat-5b00a52d-7296-48ee-b938-b95b7209f737) |
|  | Copilot Chat (web) | Go to the left navigation of Outlook app, select Copilot from the apps list and select **Web** option at the top of the chat pane, type a prompt into the chat window or select a suggested prompt and submit. This feature is included in the Outlook app level and all up Microsoft 365 active usage count effective July 01, 2025. | [Get started with Microsoft Copilot Chat](https://support.microsoft.com/topic/get-started-with-microsoft-365-copilot-business-chat-5b00a52d-7296-48ee-b938-b95b7209f737) |
|  | App Chat | Go to top right corner of Outlook web app, select Copilot placed next to settings option, type a prompt, and send. This feature is included in the Outlook app level and all up Microsoft 365 active usage count effective August 17, 2024. | [Frequently asked questions about Copilot in Outlook](https://support.microsoft.com/office/frequently-asked-questions-about-copilot-in-outlook-07420c70-099e-4552-8522-7d426712917b) |
| Teams | Summarizing key points during meetings | Summarizing key discussion points during meeting using Copilot in Microsoft Teams. | [Get started with Copilot in Microsoft Teams meetings - Microsoft Support](https://support.microsoft.com/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1) |
|  | Summarize chats and channel conversations | Type a prompt or select a prompt from **More prompts** in Copilot compose box in a chat or channel and submit. | [Use Copilot in Microsoft Teams chat and channels - Microsoft Support](https://support.microsoft.com/office/use-copilot-in-microsoft-teams-chat-and-channels-cccccca2-9dc8-49a9-ab76-b1a8ee21486c) |
|  | Rewrite and adjust messages | Write a message in message box, select **Rewrite/Adjust** in Copilot beneath the message box to rewrite or adjust the whole or specific selection of the message. | [Rewrite and adjust your messages with Copilot in Microsoft Teams - Microsoft Support](https://support.microsoft.com/office/rewrite-and-adjust-your-messages-with-copilot-in-microsoft-teams-53315d9c-93be-45ab-9004-2f8205725cc7) |
|  | Intelligent Recap | Select the **Recap** tab in the meeting chat for Teams calendar event and view the AI Notes section after the meeting ends (meeting is recorded and transcribed). | [Get started with Microsoft Copilot in Teams - Microsoft Support](https://support.microsoft.com/office/get-started-with-copilot-for-microsoft-365-in-teams-60c37fde-6e13-4412-8101-40bbbc711ec9) |
|  | Interpreter | Turn on Interpreter under the **More** icon and listen to a meeting in one of the selected languages. | [Interpreter in Microsoft Teams meetings and calls](https://support.microsoft.com/office/interpreter-in-microsoft-teams-meetings-and-calls-c7efe2bb-535d-42ab-a5c4-d2d91619b46d) |
|  | Facilitator | Turn on Facilitator under the **More** icon and activate AI-generated notes; or interact with Facilitator or Facilitator-generated content during or after a meeting. | [Facilitator in Microsoft Teams meetings](https://support.microsoft.com/office/facilitator-in-microsoft-teams-meetings-37657f91-39b5-40eb-9421-45141e3ce9f6) |
|  | Copilot Chat (work) | Go to Chat on the left side of Teams, select Copilot from the top of your Teams chat list, type a prompt, and send. | [Get started with Microsoft Copilot in Teams - Microsoft Support](https://support.microsoft.com/office/get-started-with-copilot-for-microsoft-365-in-teams-60c37fde-6e13-4412-8101-40bbbc711ec9) |
|  | Copilot Chat (web) | Go to the left navigation of Teams application, select Copilot from the apps list and select **Web** option at the top of the chat pane, type a prompt into the chat window or select a suggested prompt and submit. This feature is included in the Teams app level and all up Microsoft 365 active usage count effective July 01, 2025. | [Get started with Microsoft Copilot in Teams - Microsoft Support](https://support.microsoft.com/office/get-started-with-copilot-for-microsoft-365-in-teams-60c37fde-6e13-4412-8101-40bbbc711ec9) |
| Word | All Copilot in Word features are automatically included in the Microsoft Copilot usage report. Usage of any Copilot in Word feature counts towards the Active users metric and is indicated in the per-user Last activity date (UTC).**NOTE:** **Edit with Word** counts towards "Prompts submitted in Copilot Chat (work)," but **Edit with Excel** and **Edit with PowerPoint** don't. |  | To learn more about Copilot in Word features, refer to [Welcome to Copilot in Word - Microsoft Support](https://support.microsoft.com/office/welcome-to-copilot-in-word-2135e85f-a467-463b-b2f0-c51a46d625d1). |
| Excel | All Copilot in Excel features are automatically included in the Microsoft Copilot usage report. Usage of any Copilot in Excel feature counts towards the Active users metric and is indicated in the per-user Last activity date (UTC). | To learn more about Copilot in Excel features, refer to [Get started with Copilot in Excel - Microsoft Support](https://support.microsoft.com/office/get-started-with-copilot-in-excel-d7110502-0334-4b4f-a175-a73abdfc118a). |  |
| PowerPoint | All Copilot in PowerPoint features are automatically included in the Microsoft Copilot usage report. Usage of any Copilot in PowerPoint feature counts towards the Active users metric and is indicated in the per-user Last activity date (UTC). |  | To learn more about Copilot in PowerPoint features, refer to [Welcome to Copilot in PowerPoint - Microsoft Support](https://support.microsoft.com/office/welcome-to-copilot-in-powerpoint-57133c75-24c0-4519-8096-d0dadf25fb8d). |
| OneNote | All Copilot in OneNote features are automatically included in the Microsoft Copilot usage report. Usage of any Copilot in OneNote feature counts towards the Active users metric and is indicated in the per-user Last activity date (UTC). |  | To learn more about Copilot in OneNote features, refer to [Welcome to Copilot in OneNote - Microsoft Support](https://support.microsoft.com/office/welcome-to-copilot-in-onenote-34b30802-02ae-4676-a88c-82f8d5e586dd). |
| Loop | All Copilot in Loop features are automatically included in the Microsoft Copilot usage report. Usage of any Copilot in Loop feature counts towards the Active users metric and is indicated in the per-user Last activity date (UTC). As of December 11, 2025, user views of Loop documents generated by the Facilitator feature in Teams meetings are included in active usage for the Loop app and all-up Microsoft Copilot usage. |  | To learn more about Copilot in Loop features, refer to [Get started with Microsoft Copilot in Loop - Microsoft Support](https://support.microsoft.com/office/get-started-with-copilot-for-microsoft-365-in-loop-966eb1a2-b5ec-4532-8a9d-f1aaeda7f90e). |

Note

Active users of Word, Excel, and PowerPoint data is incomplete before January 25, 2024.

Important

The metrics displayed in the Microsoft Copilot usage report come from data that classified as required service data. Optional diagnostic data isn't required for comprehensive information, but this requirement might change in the future. [Learn more about required service data](/en-us/DeployOffice/privacy/required-service-data).

In the **Adoption** section, you might see a recommendation card:

[![Screenshot showing the recommendation card for Microsoft Copilot adoption.](../../media/copilot-usage-recommendation.png)](../../media/copilot-usage-recommendation.png#lightbox)

To learn more about using organizational messages for Microsoft Copilot, see [Drive adoption with Microsoft Copilot Usage report's Organizational Messages feature](/en-us/microsoft-365/copilot/track-copilot-adoption).

You can export the report data into an Excel .csv file by selecting the ellipses and then **Export** in the top corner of the chart.

You can view a table list to show each Microsoft Copilot enabled user's last activity date among Microsoft Copilot apps.

[![Screenshot showing the activity for the Microsoft Copilot usage report.](../../media/copilot-usage-last-activity.png)](../../media/copilot-usage-last-activity.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot showing the columns you can select for the Microsoft Copilot usage report.](../../media/copilot-usage-chat-columns.png)](../../media/copilot-usage-chat-columns.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

To ensure data quality, the system performs daily data validation checks for the past three days and fills any gaps it detects. You might notice differences in historical data during the process.

### User last activity table

| Metric | Definition |
| --- | --- |
| User name | The user's principal name. |
| Display name | The full name of the user. |
| Prompts submitted (any app) | Total number of prompts a user submitted in Copilot across all in-scope host applications during the selected timeframe. |
| Copilot Chat (work) prompts submitted | The total number of prompts this user submitted to Copilot Chat (work) during the selected timeframe. |
| Copilot Chat (web) prompts submitted | The total number of prompts this user submitted to Copilot Chat (web) during the selected timeframe. |
| Active Days | The total number of days the user submitted prompts to Microsoft Copilot Chat within the selected timeframe. |
| Last activity date (UTC (Universal Time Code)) | The most recent date the user sent a message to Microsoft Copilot Chat in Teams, Outlook, m365.cloud.microsoft/chat, Microsoft Edge, the Microsoft Copilot (app), Word, Excel, PowerPoint, or OneNote. This date remains fixed even if the timeframe of the report is changed. |
| Last activity date of Teams Copilot (UTC) | The latest date the user had activity in Microsoft Teams Copilot, including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of Word Copilot (UTC) | The latest date the user had activity in Word Copilot, including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of Excel Copilot (UTC) | The latest date the user had activity in Excel Copilot, including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of PowerPoint Copilot (UTC) | The latest date the user had activity in PowerPoint Copilot, including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of Outlook Copilot (UTC) | The latest date the user had activity in Outlook Copilot, including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of OneNote Copilot (UTC) | The latest date the user had activity in OneNote Copilot, including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of Loop Copilot (UTC) | The latest date the user had activity in Loop Copilot, including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of Copilot Chat (work) (UTC) | The latest date the user had activity in Copilot Chat (work), including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of Copilot Chat (web) (UTC) | The latest date the user had activity in Copilot Chat (web), including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of Microsoft 365 App (UTC) | The most recent date the user had activity in Copilot Chat in an entry point Microsoft 365 App, including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |
| Last activity date of Microsoft Edge (UTC) | The most recent date the user had activity in Copilot Chat in entry point Microsoft Edge, including any of the intentional activities, regardless of the selected timeframe of past 7, 28, 90, or 180 days. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

## FAQ

### How is a user considered active in Microsoft Copilot usage?

A user is active in a given app if they perform an intentional action for an AI-powered capability. For example, if a user selects the Copilot icon in the Word ribbon to open the Copilot chat pane, this action doesn't count towards active usage. However, if the user interacts with the chat pane by submitting a prompt, this action counts towards active usage.

### What's the difference between the user activity table and audit log?

Audit log data that powers Microsoft Purview solutions, such as Data Security Posture Management for AI (previously called AI Hub), is built for data security and compliance purposes. It provides comprehensive visibility into Copilot interactions for these use cases. For example, it helps to discover data oversharing risks or to collect interactions for regulatory compliance or legal purposes. It's not, however, intended to be used as the basis for Copilot usage reporting. Any aggregated metrics that you build on top of this data, such as "prompt count" or "active user count," might not be consistent with the corresponding data points in the official Copilot usage reports provided by Microsoft. Microsoft can't provide guidance about how to use audit log data as the basis for usage reporting, nor can we guarantee that aggregated usage metrics built on top of audit log data matched similar usage metrics reported in other tools.

To access accurate information on Microsoft Copilot usage, use one of the following reports: the [Microsoft Copilot usage report](microsoft-365-copilot-usage) in the Microsoft 365 Admin Center or the [Copilot Dashboard](/en-us/viva/insights/org-team-insights/copilot-dashboard) in Viva Insights.

### What's the scope of the user-level table?

The user-level table in the report shows all users who were licensed for Microsoft Copilot at any point over the past 180 days, even if the user later removed the license or never had any Copilot active usage.

### I assigned the Microsoft Copilot license to users, but why is the 'last activity date' for users empty in rare cases?

Based on system constraints, some users might not have a 'last activity date' in the user-level table of the report under the following conditions:

1. The user used Microsoft Copilot within a short time window (less than 24 hours) after the Microsoft Copilot license was assigned.
2. The user later had no other Microsoft Copilot usage up to the date on which the report is viewed.

### Why is the 'Last activity date of Word, Excel, PowerPoint, OneNote, or Outlook Copilot (UTC)' sometimes blank or newer than the actual date, even when users recently used Copilot features?

A known limitation might cause this problem. For various reasons, uploading client events data for Copilot features in Word, Excel, PowerPoint, OneNote, and Outlook can be delayed. For example, if end users disconnect from the internet immediately after taking a Copilot action, the data upload is delayed.

### How do the numbers in this report compare to what is shown in the Microsoft Copilot Dashboard in Viva Insights?

The data in these reports is based on the same underlying definitions of active usage, but the population of users included in the analysis and the timeframe displayed might differ. To learn more, see [Use Microsoft Copilot Dashboard advanced features with a Viva Insights subscription](/en-us/viva/insights/org-team-insights/copilot-dashboard-advanced-features#setup-and-licenses).