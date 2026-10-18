---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Teams Device Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-teams-device-usage-preview?view=o365-worldwide
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
description: The Microsoft Teams device usage report reveals how users connect to Teams across desktop, mobile, and web. Learn to access and interpret the data in minutes.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: a427b6c8-c20f-078b-4a42-3ec699b4b662
document_version_independent_id: f0928764-63c5-dd16-b20a-432b5a9c8e32
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-teams-device-usage-preview.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-teams-device-usage-preview
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-teams-device-usage-preview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 487e63b2-ba8f-1b30-54da-6a5306b4b385
---

# Microsoft Teams Device Usage Report - Microsoft 365 admin | Microsoft Learn

The Microsoft Teams device usage report provides an overview of device usage activity in Teams, including the number of daily active users by device type. You can quickly see what devices licensed users across your organization are using to access Teams.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Microsoft Teams device usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft Teams**, and then select the **Device usage** tab.

## Interpret the Microsoft Teams device usage report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the Microsoft Teams device usage report.](../../media/e46c7f7c-8371-4a20-ae82-b20df64b0205.png)](../../media/e46c7f7c-8371-4a20-ae82-b20df64b0205.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Teams user device activity report column options.](../../media/3358d5d9-931b-4d30-931f-450b2f5717da.png)](../../media/3358d5d9-931b-4d30-931f-450b2f5717da.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| User name | The display name of the user. |
| Windows | Selected if the user was active in the Teams desktop client on a Windows-based computer. |
| Mac | Selected if the user was active in the Teams desktop client on a macOS computer. |
| iOS | Selected if the user was active on the Teams mobile client for iOS. |
| Android phone | Selected if the user was active on the Teams mobile client for Android. |
| Chrome OS | Selected if the user was active in the Teams desktop client on a ChromeOS computer. |
| Linux | Selected if the user was active in the Teams desktop client on a Linux computer. |
| Web | Selected if the user was active in the Teams web client on devices. |
| Last activity date (UTC) | The last date (UTC) that the user participated in a Teams activity. |
| Is licensed | Selected if the user is licensed to use Teams. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).