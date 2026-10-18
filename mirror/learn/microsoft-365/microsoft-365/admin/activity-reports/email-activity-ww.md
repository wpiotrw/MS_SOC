---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Exchange Email Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/email-activity-ww?view=o365-worldwide
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
search.appverid:
- BCS160
- MET150
- MOE150
- GEA150
ms.assetid: 1cbe2c00-ca65-4fb9-9663-1bbfa58ebe44
ai-usage: ai-assisted
description: The Exchange email activity report helps admins track sends, reads, and meeting activity across Microsoft 365. Explore charts, metrics, and filters to manage usage.
ms.date: 2026-04-24T00:00:00.0000000Z
locale: en-us
document_id: 7624e740-4a9c-9e23-cdb1-a742e2b004d9
document_version_independent_id: 7624e740-4a9c-9e23-cdb1-a742e2b004d9
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/email-activity-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/email-activity-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/email-activity-ww.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: d6b3aed6-a9c7-4c62-25f2-0bfc5bd2ac1b
---

# Exchange Email Activity Report - Microsoft 365 admin | Microsoft Learn

The Exchange email activity report provides a high-level view of email traffic within your organization. Use the Exchange email activity report to understand the trends and per-user level details of the email activity within your organization.

Note

The Exchange email activity report is only available for mailboxes that are associated with users who have licenses.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Exchange email activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Exchange**.
5. On the report page, select the **Email activity** tab.

## Interpret the Exchange email activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated. The data in each report usually covers up to the last 24 to 48 hours.

You can view your users' email activity by looking at the **Activity** and **Users** charts.

[![Screenshot of the email activity report.](../../media/5eb1d9e9-8106-4843-acb7-c0238c0da816.png)](../../media/5eb1d9e9-8106-4843-acb7-c0238c0da816.png#lightbox)

The **Activity** chart helps you understand the trend of the amount of email activity going on in your organization. You can see the split of email send, email read, email received, meeting created, or meeting interacted activities. On the **Activity** chart, the Y axis is the count of activity of the type email sent, email received, email read, meeting created, and meeting interacted.

The **User** chart helps you understand the trend of the number of unique users who are generating the email activities. You can look at the trend of users performing email sending, email reading, email receiving, meeting creating, or meeting interacting activities. On the **Users** activity chart, the Y axis is the users performing activity of the type email sent, email received, email read, meeting created, or meeting interacted.

The X axis on both charts is the selected date range for this specific report.

You can filter the series you see on either chart by selecting an item in the legend.

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the email activity report column options.](../../media/80ffa0ad-61c5-4a6f-8a1d-5f6730ff7da9.png)](../../media/80ffa0ad-61c5-4a6f-8a1d-5f6730ff7da9.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table shows a breakdown of the email activities at the per-user level. This data shows all users that have an Exchange product assigned to them and their email activities.

| Metric | Definition |
| --- | --- |
| Username | The email address of the user. |
| Display name | The full name of the user. |
| Deleted | Refers to the user whose current state is deleted, but was active during some part of the reporting period of the report. |
| Deleted date | The date the user was deleted. |
| Last activity date | The last time the user performed a read or send email activity. |
| Send actions | The number of times an email send action was recorded for the user. |
| Receive actions | The number of times an email received action was recorded for the user. |
| Read actions | The number of times an email read action was recorded for the user. |
| Meeting created actions | The number of times a meeting request send action was recorded for the user. |
| Meeting interacted actions | The number of times a meeting request accept, tentative, decline, or cancel action was recorded for the user. |
| Product assigned | The products that are assigned to this user. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).