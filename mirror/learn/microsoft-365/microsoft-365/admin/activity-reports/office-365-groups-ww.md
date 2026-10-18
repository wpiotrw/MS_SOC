---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft 365 Apps Groups Activity Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/office-365-groups-ww?view=o365-worldwide
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
- AdminTemplateSet
- GAUpdates
search.appverid:
- BCS160
- MET150
- MOE150
- GEA150
ms.assetid: a27f1a99-3557-4f85-9560-a28e3d822a40
ai-usage: ai-assisted
description: The Microsoft 365 apps Groups activity report displays member counts, storage use, and message activity. Learn how to access and analyze group data in the admin center.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: da19d290-8b64-1b63-3743-2f2a49a7a690
document_version_independent_id: da19d290-8b64-1b63-3743-2f2a49a7a690
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/office-365-groups-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/office-365-groups-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/office-365-groups-ww.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e2c9f30c-00ec-44c0-846c-b20dbfb3283f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/702271fe-87d7-4493-828b-2d6fde3de8ab
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: e02cb752-73d2-0412-96bf-0b85f664706e
---

# Microsoft 365 Apps Groups Activity Report - Microsoft 365 admin | Microsoft Learn

The Microsoft 365 apps Groups activity report provides insight into the activity of groups in your organization. It includes details about how many groups are created and used.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Microsoft 365 Apps Groups activity report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft 365 apps**.
5. Select the **Groups activity** tab. If you don't see the tab, select the three dots, and then select **Groups activity**.

## Interpret the Microsoft 365 apps Groups activity report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the Microsoft 365 Groups activity report.](../../media/ab90e30b-8938-4110-ab3d-ee472a4cfe21.png)](../../media/ab90e30b-8938-4110-ab3d-ee472a4cfe21.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Microsoft 365 Groups activity report column options.](../../media/1600556a-f5f1-47d9-b325-cd77c78f4004.png)](../../media/1600556a-f5f1-47d9-b325-cd77c78f4004.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| Group name | The name of the group. |
| Deleted | The number of deleted groups. If the group is deleted, but had activity in the reporting period it shows up in the grid with this flag set to true. |
| Group owner | The name of the group owner. |
| Last activity date (UTC) | This date shows the most recent activity in an email conversation, Viva Engage, or the site. |
| Type | The type of group. This type can be private or public group. |
| Emails received in Exchange | The number of messages received by the group. |
| Emails in Exchange (total) | The total number of items in the group's mailbox. |
| Mailbox storage used for Exchange (MB) | The storage used by the group's mailbox. |
| SharePoint files (total) | The number of files stored in SharePoint group sites. |
| SharePoint files (active) | The number of files in the SharePoint group site that were acted on (viewed or modified, synched, shared internally or externally) during the reporting period. |
| Total site storage used for SharePoint (MB) | The amount of storage in MB used during the reporting period. |
| Messages in Viva Engage (posted) | The number of messages posted in the Viva Engage group over the reporting period. |
| Messages in Viva Engage (read) | The number of conversations read in the Viva Engage group over the reporting period. |
| Messages in Viva Engage (liked) | The number of messages liked in the Viva Engage group over the reporting period. |
| Members | The number of members in the group. |
| External members | The number of external users in the group. |
| Total organized meetings | The sum of one-time scheduled and recurring meetings a user organized during the specified time period. |
| Channel messages | The number of unique messages that a user posted in a team chat during the specified time period. This number includes original posts and replies. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).