---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Viva Engage Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/viva-engage-activity-report-ww?view=o365-worldwide
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
description: The Viva Engage Activity report helps admins track user engagement by showing how many users post, like, or read messages. Learn how to view and interpret it.
ms.date: 2026-06-11T00:00:00.0000000Z
locale: en-us
document_id: 54018fcd-d64a-d4d2-770d-201838329e51
document_version_independent_id: 54018fcd-d64a-d4d2-770d-201838329e51
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/viva-engage-activity-report-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/viva-engage-activity-report-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/viva-engage-activity-report-ww.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 58289eb6-f14b-7eaa-6e8e-afd53cd10fbe
---

# Viva Engage Activity Report - Microsoft 365 admin | Microsoft Learn

The Viva Engage Activity report helps you understand the level of engagement of your organization with Viva Engage by looking at the number of unique users who use Viva Engage to post, like, or read a message and the amount of activity generated across the organization.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Viva Engage Activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Viva Engage**.
5. On the report page, select the **Activity** tab.

## Interpret the Viva Engage Activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the Microsoft Viva Engage activity report.](../../media/9b251183-c2b3-430c-ab2d-58bf11e7e3ae.png)](../../media/9b251183-c2b3-430c-ab2d-58bf11e7e3ae.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Viva Engage activity report column options.](../../media/7ef6351d-f7e9-4504-913d-2c2df9062bf6.png)](../../media/7ef6351d-f7e9-4504-913d-2c2df9062bf6.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

| Metric | Definition |
| --- | --- |
| Username | The email address of the user. You can display the actual email address or make this field anonymous. This grid shows users who logged into Viva Engage using the Microsoft 365 account or who logged into the network using single sign-on. |
| Display name | The full name of the user. You can display the actual email address or make this field anonymous. |
| User state | One of three values: Activated, Deleted, or Suspended. These reports show data for active, suspended, and deleted users. They don't reflect pending users, because pending users can't post, read, or like a message. |
| State change date (UTC) | The date on which the user's state was changed in Viva Engage. |
| Last activity date (UTC) | The last date that the user posted, read, or liked a message. |
| Posted | The number of messages the user posted during the time period you specified. |
| Read | The number of conversations that the user read during the time period you specified. |
| Liked | The number of messages that the user liked during the time period you specified. |
| Product assigned | The products that are assigned to this user. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).