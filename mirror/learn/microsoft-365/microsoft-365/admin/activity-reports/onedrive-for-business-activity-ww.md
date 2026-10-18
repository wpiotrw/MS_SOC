---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: OneDrive Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/onedrive-for-business-activity-ww?view=o365-worldwide
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
description: The OneDrive Activity insights help admins track files viewed, synced, and shared. Discover how to view and interpret the activity report in Microsoft 365.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: 0da557b4-a6cc-5eca-e85b-2f5d93ad15b1
document_version_independent_id: 0da557b4-a6cc-5eca-e85b-2f5d93ad15b1
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/onedrive-for-business-activity-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/onedrive-for-business-activity-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/onedrive-for-business-activity-ww.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: b87b3761-80b0-305f-184f-f383417dad66
---

# OneDrive Activity Report - Microsoft 365 admin | Microsoft Learn

The OneDrive Activity report provides insight for every user licensed to use OneDrive by looking at their interaction with files on OneDrive. It also helps you understand the level of collaboration by looking at the number of files shared.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the OneDrive Activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **OneDrive**, and then select the **Activity** tab.

## Interpret the OneDrive Activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the Microsoft OneDrive activity report.](../../media/c89df0b0-2611-4acf-9ef7-17cedf7977be.png)](../../media/c89df0b0-2611-4acf-9ef7-17cedf7977be.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the OneDrive activity report column options.](../../media/252f311f-ffde-4e5a-9158-2b822bf86964.png)](../../media/252f311f-ffde-4e5a-9158-2b822bf86964.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| Username | The user name of the owner of the OneDrive account. |
| Last activity date (UTC) | The most recent day file activity occurred on the OneDrive account for the selected date range. To see activity that occurred on a specific date, select the date directly in the chart. |
| Files viewed or edited | The number of files that the user uploaded, downloaded, modified, or viewed. |
| Files synced | The number of files synced between a user's local device to the OneDrive account. |
| Files shared internally | The number of files shared with users within the organization, or with users within groups (that might include external users). |
| Files shared externally | The number of files shared with users outside of the organization. |
| Deleted | This metric indicates that the user's license was removed.**NOTE**: Activity for a deleted user displays in a report as long as they were licensed at some time during the selected time period. The **Deleted** column helps you to note that the user might no longer be active, but contributed to the data in the report. |
| Deleted date | The date when the user's license was removed. |
| Product assigned | The Microsoft 365 products that are licensed to the user. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).