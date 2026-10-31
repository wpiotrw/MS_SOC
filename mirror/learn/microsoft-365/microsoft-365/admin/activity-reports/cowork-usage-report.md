---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Copilot Cowork usage - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: The Cowork usage helps admins measure usage, adoption, and retention.
customer intent: As an IT administrator, I want to interpret the metrics so I can understand usage, adoption, and retention.
ms.date: 2026-09-08T00:00:00.0000000Z
ms.author: tiaraquan
author: tiaraquan
manager: dansimp
ms.reviewer: tiaraquan
audience: Admin
ms.topic: concept-article
ms.service: microsoft-copilot
ms.subservice: cowork
ms.update-cycle: 180-days
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- m365copilot
- magic-ai-copilot
ai-usage: ai-assisted
locale: en-us
document_id: f5ccb61b-4b3d-58f4-98ad-b9b2d6567213
document_version_independent_id: f5ccb61b-4b3d-58f4-98ad-b9b2d6567213
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/cowork-usage-report.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/cowork-usage-report
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/cowork-usage-report.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 053855c6-1ae4-501b-90ed-69a1d84d1f6a
---

# Copilot Cowork usage - Microsoft 365 admin | Microsoft Learn

The Cowork usage dashboard provides visibility into how users in your organization engage with Cowork. Use this dashboard to track usage, adoption trends, and monitor user retention. Use the dashboard to:

- Gain visibility into usage and adoption trends across your organization.
- Track active users, total tasks, average tasks per user, and retention over time.
- View daily activity and drill into user-level details.
- Monitor grace period status and set up access for [usage-based billing](/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits).
- Export data for offline analysis and reporting.

Note

The details provided in the Cowork dashboard are calculated using a [methodology optimized for Cowork](https://microsoft.github.io/CopilotAnalyticsLabs/Cowork_Methodology.pdf).

## Access reporting data

Important

To view the reporting data in this dashboard, you need the appropriate permissions. For more information, see [Usage report permissions](/en-us/microsoft-365/admin/activity-reports/activity-reports#before-you-begin). For more information, see [About admin roles](/en-us/microsoft-365/admin/add-users/about-admin-roles), [Assign admin roles](/en-us/microsoft-365/admin/add-users/assign-admin-roles), and [Microsoft 365 usage reports overview](/en-us/microsoft-365/admin/activity-reports/activity-reports).

**To access the report:**

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
2. In the left navigation, select **Copilot**.
3. Under the **Copilot** section, select **Cowork**.
4. Select either:
    1. **Overview** to view Cowork adoption and usage at a glance.
    2. **Usage** to view key engagement indicators at a glance. If you select the **Usage** tab, at the top of the page, use the **Date range selector** to filter the report data. The default view shows the past 28 days. All summary metrics, charts, and the usage details table update to reflect the selected time period.

Note

The report header shows when data was last refreshed. Check the **Last updated** timestamp in the upper-right corner to understand the recency of the data.

## Overview tab

| Metric | Description |
| --- | --- |
| Active Cowork users | Unique count of users who submitted at least one prompt in a Cowork task (conversational request), or had at least one scheduled task executed by Cowork on their behalf during the selected time period.Select **View usage** on the card to open the Usage tab and explore daily activity, average tasks per user, and retention trends behind the headline number. |
| Total Cowork tasks | Total number of Cowork tasks during the selected time period. A task represents a single conversation thread within Cowork, including both user-initiated conversations and scheduled task executions. If a user continues an existing task by asking additional questions, it counts as the same task.Select **View usage** on the card to open the Usage tab and explore daily activity, average tasks per user, and retention trends behind the headline number. |
| Grace period | The number of days remaining in your usage-based billing grace period before action is required to prevent loss of Cowork access. When a grace period is active, the dashboard shows a banner and a countdown of the days remaining.To avoid losing Cowork access, select [Set up consumptive billing](/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits) before the date shown on the Grace period card. |

### Take action from the Overview tab

The **Top actions for you** section highlights tasks that need your attention:

- **Pending requests for Cowork**: Review users who requested Cowork access, along with the date they requested it, and set up consumptive billing to grant access.
- **Manage plugins for Cowork**: Manage the plugins that add skills and connectors to extend what Cowork can do for your organization. Select **Go to Tools** to manage plugins.

## Usage tab

Four cards at the top of the Usage tab provide an at-a-glance view of key engagement indicators. Each card also shows a week-over-week trend indicator, so you can quickly assess whether usage is growing or declining.

| Metric | Description |
| --- | --- |
| Active Cowork users | Unique count of users who submitted at least one prompt in a Cowork task (conversational request), or had at least one scheduled task executed by Cowork on their behalf during the selected time period. |
| Total Cowork tasks | Total number of Cowork tasks during the selected time period. A task represents a single conversation thread within Cowork, including both user-initiated conversations and scheduled task executions. If a user continues an existing task by asking additional questions, it counts as the same task. |
| Average tasks | Average number of tasks per active user during the selected time period. The average is calculated as Total Cowork Tasks divided by Active Cowork Users. |
| Retained Cowork users | Number of users who were active during the previous seven-day period and were also active during the most recent seven-day period. This metric measures ongoing engagement and user retention. |

Tip

A high ratio of Retained Cowork users to Active Cowork users indicates that users are returning to Cowork consistently, which is a strong signal of sustained adoption.

### Adoption section

The Adoption section contains two charts that help you understand usage patterns over time.

| Chart | Description |
| --- | --- |
| Daily active users | This line chart shows the trend of daily active users across the selected date range. Use it to:<br>- Spot day-of-week patterns, such as lower usage on weekends.<br>- Identify spikes or dips that might correspond to product launches, announcements, or outages.<br>- Track whether adoption is trending up or down over time. |
| Tasks by type | This chart breaks down total tasks into two categories: <br>- **User-initiated**: A task started directly by a user through a conversational interaction with Cowork. If a user continues an existing task by asking additional questions, it still counts as the same task. You can view these tasks under **My Tasks** within the Cowork experience.<br>- **Scheduled**: A task automatically executed by Cowork on behalf of a user based on a defined schedule. You can view completed scheduled task executions under **Scheduled &gt; Runs** within the Cowork experience. Use the **Summary view** to compare total volumes across task types, or switch to Trend to see how each type changed over the selected period. |

### Cowork usage details

The **Cowork usage details** table lists individual users who had activity in Cowork dating back to April 1, 2026. Use this information to investigate usage at the user level and export data for further analysis.

| Column name | Description |
| --- | --- |
| User ID | The user's email address. |
| Display name | The user's display name as it appears in your organization's directory. |
| Total tasks | Total number of tasks (user-initiated and scheduled) attributed to this user. |
| Scheduled tasks | Number of tasks that Cowork automatically executed on this user's behalf. |
| User-initiated tasks | Number of tasks this user started through direct interaction. |
| Active days | Number of days during the selected time period on which this user had at least one Cowork prompt. |
| Last activity date | The most recent date on which this user had a Cowork prompt. |

### Export usage data

Select **Export** above the usage details to download the full dataset as a CSV file. The exported file includes all users listed in the table.

Note

The table header shows the total number of users returned. For example, `982 items` means 982 users had Cowork activity during the selected period or since April 1, 2026.

## Value tab

Important

This feature is part of [Frontier preview program](https://www.microsoft.com/microsoft-365-copilot/frontier-program). Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities might change over time.

The **Value** tab helps your organization understand how Copilot Cowork is being used and where it provides value. It brings together assisted hours by Copilot Cowork and task category details so you can identify usage patterns and communicate the potential impact of Cowork.

Use the dashboard to review assisted hours for a selected period and explore how credits and assisted hours are distributed across different types of work.

### View the Value dashboard

To view the Microsoft Cowork **Value** dashboard:

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
2. Go to **Copilot** &gt; **Cowork**, and then select the **Value** tab.
3. Choose the **Date range** to filter your data.

    The **Date range** of the dashboard supports two time views:

    - **Last 28 days**: Shows data for the most recent 28-day period through the latest available data refresh. Use this date range to compare a consistent four-week period without the variation caused by months of different lengths.
    - **Month to date**: Shows data from the first day of the current calendar month through the latest available data refresh. Use this date range to track progress within the current month.

### Understand the metrics

The summary cards provide an at-a-glance view of Cowork activity for the selected time period.

#### Cowork assisted hours

Assisted hours is a directional estimate of employee hours that benefited from Cowork during the selected time period. These estimates are calculated using a methodology optimized for Cowork that categorizes activities into common types of work and applies estimated time impacts informed by productivity research and observed usage patterns.

Assisted hours help organizations understand the scale of work supported by Cowork across different task categories and identify where Cowork is having the greatest impact.

Assisted hours are an estimate and should be used as a directional metric. They aren't a direct measurement of time saved, productivity gains, business outcomes, or realized value. Actual impact may vary based on the work performed and how Cowork is used.

To learn more about how Cowork assisted hours is calculated, including task categorization approach, research sources, and estimation methodology, see [Cowork Assisted Hours Methodology](https://microsoft.github.io/CopilotAnalyticsLabs/Cowork_Methodology.pdf).

### Understand Assisted hours by task category

The **Assisted hours by task category** table shows the most common categories of Cowork tasks during the selected time period. Categories are based on the primary type of work performed. Use this table to understand how Cowork activity, employee impact, and credit consumption are distributed across different types of work.

| Metric | What it shows |
| --- | --- |
| Task category | The type of work associated with Cowork activity, such as analysis and research, document and content creation, email workflows, meeting workflows, communication workflows, specialized workflows, and writing or debugging code. For more information, see [task categories](https://microsoft.github.io/CopilotAnalyticsLabs/Cowork_Methodology.pdf). |
| Users | The number of users with activity assigned to the task category during the selected time period. |
| Assisted hours | The estimated employee hours that benefited from Cowork for tasks assigned to the category. |
| Credits spent | The number of Copilot credits used for tasks assigned to the category during the selected time period. |

## Settings tab

The **Settings** tab provides quick access to the controls and policies that govern Copilot Cowork in your organization. These settings are also available under Copilot settings, making it easy to manage Cowork-specific configurations from a single location.

### View the Settings dashboard

Use the dashboard to help manage and monitor adoption, consumption, and limits for Copilot Cowork. In addition, use these settings to manage Copilot Cowork external AI models and AI providers.

To view the Microsoft Cowork **Settings** dashboard:

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
2. Go to **Copilot** &gt; **Cowork**, and then select the **Settings** tab.
3. Choose from the available settings related to Copilot Cowork.