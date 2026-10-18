---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Viva Engage Groups Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/viva-engage-groups-activity-report-ww?view=o365-worldwide
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
description: The Viva Engage groups activity report tracks group creation and engagement across your tenant. Learn how to interpret each metric and export results for reporting.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: 74fe3beb-5d95-1259-46db-0251902edc6e
document_version_independent_id: 74fe3beb-5d95-1259-46db-0251902edc6e
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/viva-engage-groups-activity-report-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/viva-engage-groups-activity-report-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/viva-engage-groups-activity-report-ww.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 88bf0c49-5b78-1813-2240-23883bb97f33
---

# Viva Engage Groups Activity Report - Microsoft 365 admin | Microsoft Learn

The Viva Engage groups activity report provides insights into the activity of Viva Engage groups in your organization. You can also see how many Viva Engage groups are created and used.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Viva Engage groups activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Viva Engage**, and then select the **Groups activity** tab.

## Interpret the Viva Engage groups activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the Microsoft Viva Engage groups activity report.](../../media/3afdafe5-9269-402e-8264-c7695ceb227d.png)](../../media/3afdafe5-9269-402e-8264-c7695ceb227d.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Viva Engage groups activity report column options.](../../media/54744932-34fe-48c3-9779-1d10c3f05be1.png)](../../media/54744932-34fe-48c3-9779-1d10c3f05be1.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| Group name | The name of the group. |
| Group admin | The name of the group administrator, or owner. |
| Deleted | The number of deleted Viva Engage groups. If the group is deleted, but had activity in the reporting period it shows up in the grid with this flag set to true. |
| Type | The type of group, public or private. |
| Connected to Office 365 | Indicates whether the Viva Engage group is also a Microsoft 365 Group. |
| Last activity date (UTC) | The latest date the group read, posted, or liked a message. |
| Members | The number of members in the group. |
| Posted | The number of messages posted in the Viva Engage group over the reporting period. |
| Read | The number of conversations read in the Viva Engage group over the reporting period. |
| Liked | The number of messages liked in the Viva Engage group over the reporting period. |
| Network name | The full name of the network that the group belongs to. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).