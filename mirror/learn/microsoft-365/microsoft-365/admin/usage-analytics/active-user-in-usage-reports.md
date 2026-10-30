---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Active Users in Microsoft 365 Usage Reports - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/active-user-in-usage-reports?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-06-12T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: m365-core
ms.subservice: activity-reports
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom: AdminSurgePortfolio
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 093a6d0d-890b-489e-9f46-b15687d3fe4f
description: Discover how active users are defined in Microsoft 365 usage reports, including Exchange, Teams, SharePoint, and adoption metrics. Learn more today.
locale: en-us
document_id: 8100e31a-0312-fd5e-805f-7c04dbe1c4d0
document_version_independent_id: d0b8f728-3aa2-685a-e78d-5f8dce194c72
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/usage-analytics/active-user-in-usage-reports.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/usage-analytics/active-user-in-usage-reports
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/usage-analytics/active-user-in-usage-reports.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 2f8814c1-3624-22fc-beef-36bfbe566a53
---

# Active Users in Microsoft 365 Usage Reports - Microsoft 365 admin | Microsoft Learn

## Active users in usage reports

An active user of Microsoft 365 products for [Microsoft 365 usage analytics](usage-analytics) and the [Activity Reports in the admin center](../activity-reports/activity-reports) is defined as follows.

| **Product** | **Definition of an active user** | **Notes** |
| --- | --- | --- |
| **Exchange Online** | Any user who performs any of the following actions: <br>- Marks as read.<br>- Sends messages.<br>- Creates appointments.<br>- Sends meeting requests.<br>- Accepts (as tentative) or declines meeting requests.<br>- Cancels meetings. | No calendar information is represented. |
| **SharePoint in Microsoft 365** | Any user who interacts with a file by: <br>- Creating.<br>- Modifying.<br>- Viewing.<br>- Deleting.<br>- Sharing internally or externally.<br>- Synchronizing to clients on any site.<br>- Viewed a page on any site. | The active user metrics for SharePoint in Microsoft 365 Usage Analytics template app only reflect users who filed activity against a SharePoint Team site or a Group site. The template app is updated to synchronize the definition to the same as on the usage reports in the admin center. |
| **OneDrive for Business** | Any user who interacts with a file by: <br>- Creating.<br>- Modifying.<br>- Viewing.<br>- Deleting.<br>- Sharing internally or externally.<br>- Synchronizing to clients. |  |
| **Microsoft Viva Engage** | Any user who: <br>- Reads a message.<br>- Posts a message.<br>- Likes a message. |  |
| **Skype for Business** | Any user who participates in a peer-to-peer session including: <br>- Instant messaging.<br>- Audio and video calls.<br>- Application sharing.<br>- File transfers.<br>- Organized or participated in a conference. |  |
| **Microsoft 365** | Any user who activates their Microsoft 365 Apps for enterprise, Visio Pro, or Project Pro subscription on at least one device. |  |
| **Microsoft 365 Groups** | Any group member that has mailbox activity (if a message was sent to the group) | This definition is enhanced with group site file activity and Viva Engage group activity. For example, file activity on group site and message posted to Viva Engage group associated with the group. This data is currently not available in the Microsoft 365 Usage Analytics template app |
| **Microsoft Teams** | Any user who participates in: <br>- Chat messages.<br>- Private chat messages.<br>- Calls.<br>- Meetings.<br>- Other activity.<br><br> Other activity is defined as the number of other team activities by the user including: <br>- Liking messages.<br>- Using apps.<br>- Working on files.<br>- Searching.<br>- Following teams and channels.<br>- Adding a team or channel as a favorite. |  |

## Adoption metrics for Microsoft 365 active users

[Microsoft 365 usage analytics](usage-analytics) includes more adoption metrics related to active users to show adoption of the products over time. These metrics are valid for the month, year, and product you select. They're defined as follows.

| **Metric** | **Description** |
| --- | --- |
| **EnabledUsers** | Number of users enabled to use the product in the month. |
| **ActiveUsers** | Number of users active in the month. |
| **MoMReturningUsers** | Number of users active in the month that were also active in the preceding month. |
| **FirstTimeUsers** | Number of users active in the month that never used the service before. |
| **CumulativeActiveUsers** | Number of users active in the month plus any preceding month. |
| **ActiveUsers(%)** | Percent of users, rounded to the nearest tenth, active in the month compared to the number of users enabled in that month. |
| **MoMReturningUsers(%)** | Percent of users, rounded to the nearest tenth, active in the month that were also active in the preceding month compared to the number of active users. |