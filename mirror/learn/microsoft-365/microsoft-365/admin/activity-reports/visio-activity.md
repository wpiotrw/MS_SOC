---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Visio Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/visio-activity?view=o365-worldwide
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
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Visio Activity report tracks Visio for the web and desktop app usage in your organization. Learn how Microsoft 365 admins can access and interpret the report.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: cb34c628-8bba-1011-d097-32aa528ccb49
document_version_independent_id: cb34c628-8bba-1011-d097-32aa528ccb49
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/visio-activity.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/visio-activity
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/visio-activity.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 68bd7ab4-57a9-44e2-5420-86ec553310e9
---

# Visio Activity Report - Microsoft 365 admin | Microsoft Learn

The Visio Activity report provides insight into the activity of every Visio user in your organization.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Visio Activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Visio**.

## Interpret the Visio Activity report

The report displays trends over the last 7, 30, 90, or 180 days. If you select a particular day in the report, the per-user data table updates to display users' usage for that day.

Note

The Visio report currently becomes available within 72 hours. Microsoft is working to reduce the latency to 48 hours like other reports.

[![Screenshot of the Visio activity report.](../../media/visio-activity-charts.png)](../../media/visio-activity-charts.png#lightbox)

- **Active users** Shows the daily active users on each day over time. This metric includes Visio for the web and Visio desktop app usage.
- **Platforms** Shows the daily active users on each day over time, broken down by platform: Web and Desktop.
- **Platforms (total users)** Shows the aggregated active users for the selected time window, broken down by platform: Web and Desktop.

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

### Visio licensed usage

Use this report to filter for Visio licensed usage. Each of the charts includes a filter to select the user segment.

- **All users** Shows the usage for Visio licensed users, including Visio Plan 1 and Visio Plan 2, and seeded usage, such as using Visio that comes as part of a Microsoft 365 commercial subscription.
- **Visio licensed users** Shows the usage for Visio licensed users only, including Visio Plan 1 and Visio Plan 2.

[![Licensed users filter for the Visio activity report in Microsoft 365.](../../media/visio-license-filter.png)](../../media/visio-license-filter.png#lightbox)

Note

[Learn more about Visio seeded capabilities](https://www.microsoft.com/microsoft-365/visio/visio-in-microsoft-365), and about [Visio plans and pricing](https://www.microsoft.com/microsoft-365/visio/microsoft-visio-plans-and-pricing-compare-visio-options?rtc=1&amp;activetab=tabs%3aprimaryr1).

### User details table

The report includes a table that shows the user details with active usage in your environment during the selected time window.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| User name | The user principal name |
| Display name | The full name of the user |
| Last activity date | The latest date the user in that row had activity in Visio, including any of the activities in the summary reports |
| Desktop | This metric indicates whether that user used the Visio desktop app at least once during the selected time window |
| Web | This metric indicates whether that user used Visio for the web at least once during the selected time window |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).