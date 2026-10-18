---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Planner usage reports - Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/planner-activity?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Access the Microsoft Planner usage report in the admin center to monitor how your organization uses Planner and track active users.
ms.date: 2026-09-01T00:00:00.0000000Z
author: hlu
ms.author: hlu
manager: Peter.Bergen
ms.topic: how-to
ms.service: microsoft-365-admin
locale: en-us
document_id: dc2e7aa2-8363-dbe9-65bc-e85086859edb
document_version_independent_id: dc2e7aa2-8363-dbe9-65bc-e85086859edb
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/planner-activity.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/planner-activity
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/planner-activity.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1bb724a6-ed07-4064-971d-80071e714f16
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b9e0ece8-b7ea-432b-9fb5-167c6aef3222
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 6ab34f76-34d8-45d1-72b3-228ca5402782
---

# Microsoft Planner usage reports - Microsoft 365 - Microsoft 365 admin | Microsoft Learn

The Microsoft Planner usage report gives you a view of how people in your organization are using Planner. You can see the number of active users across your tenant, how that number trends over time, and per-user activity details such as how many days each person was active and when they were last active.

Note

This report covers Planner Usage only for basic and premium plans. Planner Agent is included in the Microsoft Copilot Agents report: [Microsoft 365 Copilot Agents reports](microsoft-365-copilot-agents-new).

## How to get to the Microsoft Planner report

1. In the Microsoft 365 admin center, go to the **Reports** &gt; **Usage** page.
2. From the left navigation, select **Planner**.

## Interpret the Microsoft Planner report

You can view the activity in the Planner report by choosing the **Periods** filter at the top of the page. Available periods are **Past 7 days**, **Past 28 days**, **Past 90 days**, and **Past 180 days**.

### Summary metrics

| Item | Description |
| --- | --- |
| **Total unique users** | The number of distinct users who performed at least one intentional Planner action during the selected period. Usage metrics reflect activity across all Planner plan types. |
| **Active users** (chart) | The number of daily active users on Planner for each day in the selected period. A user is counted on a given day if they performed at least one intentional action that day. |

### Microsoft Planner usage details table

| Item | Description |
| --- | --- |
| **Username** | The email address of the user who performed the activity. You can display the actual email address or make this field anonymous. See Make the user-specific data anonymous. |
| **Active days** | The number of distinct days within the selected period on which the user performed at least one intentional Planner action. |
| **Last activity date** | The date and time of the most recent intentional Planner action performed by the user. This date is the user's most recent activity overall, and isn't limited to the selected period. |

Important

The usage details table lists every user who was active in Planner at least once in the past 180 days, regardless of which period you select. The **Periods** filter applies only to the **Active days** column - changing the period changes the number of active days shown for each user, but it doesn't change which users appear in the table. As a result, a user can appear in the table with **0** active days if they were active within the past 180 days but not within the selected period. This behavior is consistent with other Microsoft 365 usage reports, such as the Microsoft 365 Copilot Chat report.

Select **Choose columns** to add or remove columns from the table.

You can also export the report data into a .csv file by selecting **Export**. This action exports data for all users and lets you do simple sorting and filtering for further analysis. If you have fewer than 2,000 users, you can sort and filter within the table in the report itself. If you have more than 2,000 users, filter and sort in the exported file.

## What counts as active usage

A user is counted as **active** on a given day if they performed at least one *intentional action* in Planner on that day.

An intentional action is a deliberate action a user takes in the product. Actions that happen without the user doing anything - such as background synchronization by a Planner client, or notifications generated by the service - aren't counted.

**Total unique users** is the number of distinct users who performed at least one intentional action during the selected period. Because a user is counted only once regardless of how many actions they took, this number isn't the sum of the daily values in the Active users chart. **Active days** in the details table is the number of separate days on which a user was counted as active during the same period.

Note

This definition is also shown in the product. Select **See metric definition** next to the Active users chart in the Planner report.

### Where activity is measured

Activity is counted across the Planner experiences a user can work in, including:

- Planner on the web
- Planner in Microsoft Teams
- Planner in Outlook
- Planner in Loop
- Planner mobile apps

Usage metrics reflect activity across all Planner plan types.

### Activity that counts toward active usage

A user counts as active when they take a deliberate action in one of the Planner experiences listed earlier. The following activities count toward active usage.

**Creating and changing content**

| Activity |
| --- |
| Creating, modifying, or deleting a plan |
| Creating, modifying, or deleting a task |
| Creating, modifying, or deleting a bucket |
| Creating, modifying, or deleting a goal |
| Creating, modifying, or deleting a dependency |
| Creating, modifying, or deleting a calendar |
| Modifying user settings |

**Opening and working with content**

| Activity |
| --- |
| Opening a plan, or a plan's buckets, tasks, goals, dependencies, or calendar |
| Opening a task |
| Opening a goal, or the tasks in a goal |
| Opening a bucket |
| Opening a dependency, or the dependencies of a task |
| Opening a calendar |
| Viewing tasks assigned to you, or plans you own |

**Moving between Planner views**

| Activity |
| --- |
| Opening Planner Hub |
| Opening My Tasks |
| Opening the Board view |
| Opening the Grid view |
| Opening the Schedule view |
| Opening the Timeline view |
| Opening the Charts view |
| Opening the corresponding user-level Board, Grid, Schedule, or Charts views |

**On mobile**

| Activity |
| --- |
| Attaching a file from the camera |
| Attaching a file from the photo gallery |
| Opening the Hub, My Tasks, or Settings tab |

Note

Planner continues to add capabilities, and new user-initiated interactions are included in active usage as they become available. The activities above describe the kinds of interaction that count rather than an exhaustive, permanent list.

### Activity that doesn't count toward active usage

The following activities don't count as active usage:

- Automatic background reads and polling performed by a Planner component. For example, a task list component periodically refreshes the current user's information without any user interaction.
- Data synchronization performed by a Planner client without user interaction.
- Notifications generated or delivered by the service.
- Actions performed by a service account or by an application on the user's behalf.

Note

This report shows commercial Planner usage. It doesn't include activity from personal Microsoft accounts.

## Make the user-specific data anonymous

To make the data in the Planner report and in the exported .csv file anonymous, you must be a Global Administrator. This action hides identifiable information such as display names, email addresses, and group names in reports and their exports.

1. In the Microsoft 365 admin center, go to **Settings** &gt; **Org Settings**. Under the **Services** tab, select **Reports**.
2. Select **Reports**, and then select **Concealed user, group, and site names in all reports**.
3. Select **Save changes**.

This setting applies to all Microsoft 365 usage reports in the admin center, including the Planner report and its exported .csv file.