---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Copilot Search Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-search-usage?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: cmcatee
author: cmcatee-MSFT
manager: scotv
ms.reviewer: kols
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-copilot
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- m365copilot
ms.custom:
- GAUpdates
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Copilot Search usage report empowers Microsoft 365 admins to monitor user activity, search behaviors, and engagement trends. Learn how to drive adoption now.
ms.date: 2026-04-03T00:00:00.0000000Z
locale: en-us
document_id: 160dca80-7451-ce57-5510-fae571754ccf
document_version_independent_id: 160dca80-7451-ce57-5510-fae571754ccf
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-365-copilot-search-usage.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-365-copilot-search-usage
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-365-copilot-search-usage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: f201d976-25f5-9d9f-15f4-5859b2bf9461
---

# Microsoft Copilot Search Usage Report - Microsoft 365 admin | Microsoft Learn

Note

The Copilot Search usage report is currently in public preview. Deployment processes and functionality might change before this report becomes generally available. During the public preview phase, you might notice some unexpected behaviors. These observations help Microsoft improve the product before general availability.

The Microsoft Copilot Search usage report provides a detailed view of both organizational and individual user activity with Copilot Search across platforms. It includes trend charts for active usage and search activity at the organization level, and insights into each user's search behavior during a selected timeframe. The report reflects user behaviors within one hour. With these insights, you can easily track Copilot Search usage trends and make informed decisions about how to drive further adoption within your organization.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Copilot Search usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft Copilot**, and then select **Copilot Search**.

## Interpret the Copilot Search usage report

At the top, filter by different timeframes. You can view the Copilot Search usage report over the last 7, 30, 90, or 180 days.

You can view several metrics for Copilot Search usage:

[![Screenshot of the Copilot Search usage report.](../../media/copilot-search-usage-metrics.png)](../../media/copilot-search-usage-metrics.png#lightbox)

The following table lists the features included for active users of Copilot Search:

| Copilot app | Features | What counts as active usage |
| --- | --- | --- |
| Microsoft Copilot app | Search | A licensed Microsoft Copilot user completes at least one of the following actions:<br>1. Types in a query, keyword, or natural language to find information about files, people, answers, and other content and lands in the results page.<br>2. Types in a query and selects or engages with query suggestions in the search box.<br>3. Selects an item from the options displayed in the search box dropdown list |

To learn more about the Copilot Search feature, see [Microsoft Copilot Search](/en-us/microsoft-365/copilot/microsoft-365-copilot-search).

- **Active users** shows the total number of users with a Microsoft Copilot license in your organization who completed a Copilot Search query within the Microsoft Copilot app over the selected timeframe.
- **Average daily active users** shows the average daily number of individuals who actively used Copilot Search over the selected timeframe.
- **Total searches** shows the number of distinct search queries made in Copilot Search by active users in the selected timeframe, consistent with the set of behaviors summarized in the **active users** definition.
- **Average searches per user** shows the average number of distinct search queries made by active users in the selected timeframe.

You see the following trend view charts in this report as default view:

[![Screenshot of the Copilot Search  active users chart.](../../media/copilot-search-usage-active-users-trend.png)](../../media/copilot-search-usage-active-users-trend.png#lightbox)

**Active users trend view** shows you the daily trend view of active usage of Copilot Search over the selected time frame. When you hover over a specific day on this chart, you see the total number of active users for that day. This interactive feature helps you quickly understand daily usage patterns with Copilot Search across your organization.

[![Screenshot of the Copilot Search total searches chart.](../../media/copilot-search-usage-total-searches-trend.png)](../../media/copilot-search-usage-total-searches-trend.png#lightbox)

**Total searches trend view** shows a daily trend of searches made by active users over the selected timeframe. When you hover over a specific day on this chart, you see the total number of searches for that day. This interactive feature helps you quickly understand daily engagement patterns with Copilot search across your organization.

### User activity table

| Metric | Definition |
| --- | --- |
| User ID | The user's principal ID |
| Display name | The user's full name |
| Total searches | Total number of distinct search queries the active user made during the selected timeframe |
| Last activity date (UTC) | The date when the user was most recently active in Copilot Search |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

The User activity table includes user-level details about each active Copilot Search user, including their total searches and their last activity date in Copilot Search.

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

## FAQ

### What user actions count as active usage of Copilot Search?

A user is active in Copilot Search if they have a Microsoft Copilot license and perform an intentional search action by using the Copilot Search feature. Simply opening the Copilot Search page doesn't count as active usage. The user is only counted as active if they interact with the search box by submitting a query, searching for people, searching for a file, or searching for content.

### What platforms does Copilot Search active usage include?

Copilot Search active usage includes user activity within the Microsoft Copilot app across desktop, web, and mobile platforms. The report counts any intentional search action that you perform on any of these platforms during the selected timeframe toward active usage.

### What's the scope of the user-level table?

The user-level table in the report shows all users who were licensed for Microsoft Copilot at any point over the past 180 days, even if the user removed the license or never had any Copilot active usage.