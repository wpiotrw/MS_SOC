---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Forms Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/forms-activity-ww?view=o365-worldwide
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
description: The Microsoft Forms activity report shows form creation, responses, and collaboration trends. Learn how to view and interpret this admin center report today.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: 57d85246-6552-19ec-032b-85eb04b7afc0
document_version_independent_id: 57d85246-6552-19ec-032b-85eb04b7afc0
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/forms-activity-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/forms-activity-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/forms-activity-ww.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 869710a2-5f53-f599-b5bc-01789173b115
---

# Forms Activity Report - Microsoft 365 admin | Microsoft Learn

The Forms activity report provides details about user interaction with forms for every user licensed to use Microsoft Forms. The report also helps you understand the level of collaboration by showing the number of forms created and the number of forms the user responded to.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Forms activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Forms**.

## Interpret the Forms activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the Microsoft Forms activity report.](../../media/275fb0a1-b9d9-4233-8aaf-e7df73cc705f.png)](../../media/275fb0a1-b9d9-4233-8aaf-e7df73cc705f.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Forms activity report column options.](../../media/0c9b0b69-5dc7-43ea-8e2c-54407b6ce2ab.png)](../../media/0c9b0b69-5dc7-43ea-8e2c-54407b6ce2ab.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| Username | The email address of the user who performed the activity in Microsoft Forms. |
| Last activity date (UTC) | The latest date a user performed a form activity for the selected date range. To see activity that occurred on a specific date, select the date directly in the chart. This filter displays file activity data only for users who performed the activity on that specific day. |
| Number of forms created | The number of forms that the user created. |
| Number of forms responded | The number of forms that the user submitted responses to. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).