---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Viva Engage Device Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/viva-engage-device-usage-report-ww?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
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
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Viva Engage Device usage report shows which devices your users access Viva Engage on, including daily users by device type and per-user details. Get started today.
ms.date: 2026-06-11T00:00:00.0000000Z
locale: en-us
document_id: 0f3d4933-67fb-0f1c-5508-f6898af73b83
document_version_independent_id: 0f3d4933-67fb-0f1c-5508-f6898af73b83
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/viva-engage-device-usage-report-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/viva-engage-device-usage-report-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/viva-engage-device-usage-report-ww.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: cc966807-d87c-3551-9186-1002fc730c7a
---

# Viva Engage Device Usage Report - Microsoft 365 admin | Microsoft Learn

The Viva Engage Device usage report helps you understand which devices your users prefer for accessing Viva Engage. Use this data to identify adoption patterns across web, mobile, and other platforms—so you can optimize your deployment strategy and support for each device type.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Viva Engage Device usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Viva Engage**.
5. On the report page, select the **Device usage** tab.

## Interpret the Viva Engage Device usage report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the Microsoft Viva Engage device usage report.](../../media/e21af4c0-0ad2-4485-8ab1-2f82d7dfa90e.png)](../../media/e21af4c0-0ad2-4485-8ab1-2f82d7dfa90e.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Microsoft Viva Engage device usage report column options.](../../media/fc1fc8db-e197-4878-85c7-7ba0d67b9379.png)](../../media/fc1fc8db-e197-4878-85c7-7ba0d67b9379.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

| Metric | Definition |
| --- | --- |
| Username | The email address of the user. You can display the actual email address or make this field anonymous. This grid shows users who logged in to Viva Engage using the Microsoft 365 account or who logged in to the network using single sign-on. |
| Display name | The full name of the user. You can display the actual email address or make this field anonymous. |
| User state | One of three values: Active, Deleted, or Suspended. These reports show data for active, suspended, and deleted users. They don't reflect pending users, because pending users can't post, read, or like a message. |
| State change date (UTC) | The date on which the user's state was changed in Viva Engage. |
| Last activity date (UTC) | The last date (UTC) that the user participated in a Viva Engage activity. |
| Web | Indicates if the user used Viva Engage on the web. |
| Windows phone | Indicates if the user used Viva Engage on a Windows phone. |
| Android phone | Indicates if the user used Viva Engage on an Android phone. |
| iPhone | Indicates if the user used Viva Engage on an iPhone. |
| iPad | Indicates if the user used Viva Engage on an iPad. |
| other | Indicates if the user used Viva Engage on another client, which wasn't listed previously. This metric includes Viva Engage Embed, SharePoint Web Part, Viva Engage, and select Outlook emails. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).