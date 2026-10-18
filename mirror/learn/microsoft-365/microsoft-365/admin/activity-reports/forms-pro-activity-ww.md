---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Dynamics 365 Customer Voice Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/forms-pro-activity-ww?view=o365-worldwide
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
description: The Dynamics 365 Customer Voice activity report helps admins track survey creation and response trends. Discover how to view and analyze user activity today.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: 16a3a810-bcf2-d7eb-2160-c10d5489d3ce
document_version_independent_id: 16a3a810-bcf2-d7eb-2160-c10d5489d3ce
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/forms-pro-activity-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/forms-pro-activity-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/forms-pro-activity-ww.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/470d0db9-ad2e-4233-9613-8c6e5ad393ac
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/59c00359-2c5e-4ffd-bf1f-e6de7bb59c4d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: bb443895-c3e2-327b-3e59-e2e25d83d2cb
---

# Dynamics 365 Customer Voice Activity Report - Microsoft 365 admin | Microsoft Learn

The Dynamics 365 Customer Voice activity report provides insight into the activity of every user licensed to use it by looking at their interactions with it. The report also helps you understand the level of collaboration going on by looking at the number of Pro Surveys created and Pro Surveys to which the users responded.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Dynamics 365 Customer Voice Activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** dashboard homepage, on the Dynamics 365 Customer Voice card, select **View more**.

## Interpret the Dynamics 365 Customer Voice Activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Dynamics 365 Customer Voice activity report.](../../media/a7e57d18-1ac8-4d4b-bd70-83361505dc3e.png)](../../media/a7e57d18-1ac8-4d4b-bd70-83361505dc3e.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Dynamics 365 Customer Voice activity report column options.](../../media/5ab66f4b-32eb-4c9b-9683-1157ae9e2c0a.png)](../../media/5ab66f4b-32eb-4c9b-9683-1157ae9e2c0a.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| Username | The email address of the user who performed the activity on Microsoft Forms. |
| Last activity date (UTC) | The latest date the user performed a form activity for the selected date range. To see activity that occurred on a specific date, select the date directly in the chart.This action filters the table to display file activity data only for users who performed the activity on that specific day. |
| Number of surveys created | The number of surveys that the user created. |
| Number of survey responses | The number of responses from responders to whom the survey was distributed. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).