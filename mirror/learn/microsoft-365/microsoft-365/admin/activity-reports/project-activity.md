---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Project Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/project-activity?view=o365-worldwide
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
ms.custom: 
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Project Activity report helps you track Microsoft Project usage across your organization. Learn how to view user activity, collaboration metrics, and engagement insights today.
ms.date: 2026-09-29T00:00:00.0000000Z
locale: en-us
document_id: 88b68222-3eac-0447-de7f-9b7ba70f1794
document_version_independent_id: 88b68222-3eac-0447-de7f-9b7ba70f1794
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/project-activity.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/project-activity
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/project-activity.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
platformId: 1d53914a-3c27-fed5-9103-f117903e6cb7
---

# Project Activity Report - Microsoft 365 admin | Microsoft Learn

Use the Project Activity report to quickly answer three questions:

- Who is actively using Project?
- Which client are they using (web or desktop)?
- How much project and task activity is happening?

To jump to details, go to View the Project Activity report in the Microsoft 365 admin center or User activity table.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Project Activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Project**.

## Interpret the Project Activity report

Use the Project Activity report to see the activity and usage of Project in your organization.

Use the report timeline to analyze usage over **7, 30, 90, or 180 days**.

- Selecting a specific day updates the per-user table for that day.
- Daily drill-down is available only for the most recent **28 days**.

[![Screenshot of the Microsoft Project activity report.](../../media/project-activity.png)](../../media/project-activity.png#lightbox)

The Project activity report contains four summary charts. Start with **Active users** for adoption trends, then use **Project Activity** and **Task activity** for deeper engagement signals:

- **Active users** - Shows the daily active users on each day over time. Currently, this chart includes only Project for the Web and Microsoft Project desktop client.
- **Active users (by client)** - Shows the daily active users on each day over time, broken out by client (Project for the Web vs. Project).
- **Project Activity** - Shows the number of daily sessions of Project over time, for each client (Project for the Web and Project).
- **Task activity** - Shows the daily number of tasks created or edited over time in Project for the Web

The report also has a table that shows activity for each Project user in your environment.

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Project activity report column options.](../../media/project-activity-columns.png)](../../media/project-activity-columns.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

### Privacy settings affect on the dashboard

If users or admins set their privacy settings to **Neither**, the **Project activity** chart for Project doesn't show accurate metrics. The numbers are undercounted. For more information on privacy settings, see [Use policy settings to manage privacy controls for Microsoft 365 Apps for enterprise](/en-us/deployoffice/privacy/manage-privacy-controls).

### User activity table

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| User name | The user's principal name. |
| Display name | The full name of the user. |
| Last activity date | The latest date the user in that row had activity in Project, including any of the activities in the summary reports. |
| Projects visited (Desktop) | The number of projects opened by the user in Project during the time range selected in the top right of the page. |
| Projects visited (Web) | The number of projects visited by the user in Project for the Web during the time range selected in the top right of the page. |
| Tasks created (Web) | The number of tasks created by the user in Project for the Web during the time range selected in the top right of the page. |
| Tasks edited (Web) | The number of tasks edited by the user in Project for the Web during the time range selected in the top right of the page. |
| Other | This value is true if the user performed an activity in Project or in Project for the Web (that isn't covered by the other columns) during the time range selected at the top of the page. If the user didn't perform any activity during this time, this value is false. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).