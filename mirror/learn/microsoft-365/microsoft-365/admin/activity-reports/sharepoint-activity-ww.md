---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: SharePoint Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/sharepoint-activity-ww?view=o365-worldwide
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
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The SharePoint activity report helps you monitor licensed user activity, file sharing, and storage trends in Microsoft 365. Export data for deeper analysis.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: f48c0174-f570-2724-749a-59e72b478291
document_version_independent_id: f48c0174-f570-2724-749a-59e72b478291
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/sharepoint-activity-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/sharepoint-activity-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/sharepoint-activity-ww.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: c8365b7a-f36d-623a-65a5-ef3c64cf374d
---

# SharePoint Activity Report - Microsoft 365 admin | Microsoft Learn

The SharePoint Activity report provides details about the activity of every licensed SharePoint user by looking at their interaction with files. The report helps you understand the level of collaboration by showing the number of files shared.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the SharePoint activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **SharePoint**.
5. On the report page, select the **Activity** tab.

## Interpret the SharePoint Activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the SharePoint activity report.](../../media/5a0a96f-0e4f-4fb9-8baa-3262275b3d1f.png)](../../media/5a0a96f-0e4f-4fb9-8baa-3262275b3d1f.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the columns available for the SharePoint activity report.](../../media/3c396cd1-9701-4712-8eaa-eb7bba702aa8.png)](../../media/3c396cd1-9701-4712-8eaa-eb7bba702aa8.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| Username | The email address of the user who performed the activity on the SharePoint Site. |
| Last activity date (UTC) | The latest date a file activity was performed or a page was visited for the selected date range. To see activity that occurred on a specific date, select the date directly in the chart. |
| Files viewed or edited | The number of files that the user uploaded, downloaded, modified, or viewed. |
| Files synced | The number of files that are synced from a user's local device to the SharePoint site. |
| Files shared internally | The count of files that are shared with users within the organization, or with users within groups (that might include external users). |
| Files shared externally | The number of files that are shared with users outside of the organization. |
| Pages visited | The visits to unique pages by the user. |
| Deleted | This value indicates that the user's license was removed.**NOTE:** Activity for a deleted user still displays in the report as long as the user was licensed at some time during the selected time period. The Deleted column helps you to note that the user might no longer be active, but contributed to the data in the report. |
| Deleted date | The date when the user's license was removed. |
| Product assigned | The Microsoft 365 products that are licensed to the user. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).