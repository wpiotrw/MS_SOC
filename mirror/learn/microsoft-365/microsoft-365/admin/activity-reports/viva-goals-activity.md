---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Viva Goals Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/viva-goals-activity?view=o365-worldwide
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
ai-usage: ai-assisted
description: The Viva Goals activity report helps Microsoft 365 admins track adoption, active users, and OKRs created. Explore usage trends in the admin center today.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: eb5e94c2-757e-0ab7-bb57-c7c3a1711c78
document_version_independent_id: eb5e94c2-757e-0ab7-bb57-c7c3a1711c78
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/viva-goals-activity.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/viva-goals-activity
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/viva-goals-activity.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/9b6d25c0-129d-4937-8f74-9735091f7a1b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/da35f1ac-2acf-4ff6-869e-e7f682cca509
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 2a7d9710-4946-2b60-b3a8-8ca02b969086
---

# Viva Goals Activity Report - Microsoft 365 admin | Microsoft Learn

The Viva Goals report helps you understand the activity and usage of Viva Goals in your organization. It also helps you understand the level of collaboration by showing the active usage and the number of objectives and key results (OKRs) created.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Viva Goals activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Viva Goals**.

## Interpret the Viva Goals activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the Viva Goals activity report.](../../media/viva-goals-cfr/cfr-1.jpg)](../../media/viva-goals-cfr/cfr-1.jpg#lightbox)

- **Active users** shows the number of daily active users on each day over time. This count includes Viva Goals on the web and Teams app usage.
- **Active self-service users** shows the number of daily active users with self-service license each day over time.
- **Active users by client type** shows the number of daily active users on each day over time, displayed by client type (Viva Goals for the Web, Viva Goals on Teams, Viva Goals on Azure DevOps, and more).
- **User actions by activities** shows the daily number of actions created or edited over time by Viva Goals users. This count includes Viva Goals on all client types.
- **Active Viva Goals organizations** shows the daily active organizations each day over time. This count includes all the activities in a Viva Goals organization.

The report also has a table that shows activity for each Viva Goals user in your organization.

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of choosing and removing contents from the report.](../../media/viva-goals-cfr/cfr-2.jpg)](../../media/viva-goals-cfr/cfr-2.jpg#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

## User activity table

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| User name | The user's principal name. |
| Display name | The full name of the user. |
| Last activity date | The latest date the user in that row had activity in Viva Goals, including any of the activities. |
| Is self-serve trial | Indicates whether the user has a self-serve trial license. |
| Microsoft Teams | Indicates whether the user uses the Viva Goals app on Microsoft Teams. |
| Slack | Indicates whether the user uses the Viva Goals integration on Slack. |
| Azure DevOps | Indicates whether the user uses the Viva Goals integration on Azure DevOps. |
| Web | Indicates whether the user uses Viva Goals on web. |
| Check-ins | Number of check-ins done by the user on Viva Goals within the time range selected. |
| OKRs created | Number of OKRs created by the user on Viva Goals within the time range selected. |
| Projects created | Number of Projects created by the user on Viva Goals within the time range selected. |
| OKR engagement | Number of reactions on the OKRs by the user on Viva Goals within the time range selected. |
| Dashboards created | Number of Dashboards created by the user on Viva Goals within the time range selected. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).