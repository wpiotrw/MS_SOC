---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Exchange Mailbox Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/mailbox-usage?view=o365-worldwide
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
ms.assetid: beffbe01-ce2d-4614-9ae5-7898868e2729
ai-usage: ai-assisted
description: The Exchange Mailbox usage report gives admins insights into user and shared mailbox activity, storage consumption, and quota thresholds. Start optimizing your tenant now.
ms.date: 2026-04-03T00:00:00.0000000Z
locale: en-us
document_id: e612a4e4-d051-27a7-e54a-bb1ac3fe0849
document_version_independent_id: 653be32f-e4e8-8a72-98b3-a629238ecbd5
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/mailbox-usage.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/mailbox-usage
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/mailbox-usage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 3de19c21-f74a-252f-426f-22cd66548a4b
---

# Exchange Mailbox Usage Report - Microsoft 365 admin | Microsoft Learn

The Exchange Mailbox usage report provides information about users with a user mailbox and the level of activity by each user. Activity is based on the email send, read, create appointment, send meeting, accept meeting, decline meeting, and cancel meeting activity. The report provides information about how much storage each user mailbox consumes, and how many of them are approaching storage quotas. The mailbox usage report also contains information about mailboxes shared among users, providing storage and quota data on shared mailboxes.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Exchange Mailbox usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)).

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Exchange**.
5. On the report page, select the **Email activity** tab.
6. Under **Email activity**, select **View More**.
7. From the **Email activity** drop-down list, select **Exchange** &gt; **Mailbox usage**.

## Interpret the Exchange Mailbox usage report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated. The data in each report usually covers up to the last 24 to 48 hours.

You can view your organization's Exchange mailbox usage by looking at the **Mailbox**, **Storage**, and **Quota** charts.

To access shared mailbox information, change the drop-down selection at the top right of the charts to **Shared**. If your tenant doesn't have shared mailboxes, you can't view any shared mailbox information.

Note

You can't currently export the summary chart information for shared mailboxes. This known issue will be corrected in a future update.

[![Mailbox usage report.](../../media/9f610e91-cbc1-4e59-b824-7b1ddd84b738.png)](../../media/9f610e91-cbc1-4e59-b824-7b1ddd84b738.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screesnhot that shows the Mailbox usage report - choose columns.](../../media/ea3d0b18-6ac6-41b0-9bb9-4844f040ea75.png)](../../media/ea3d0b18-6ac6-41b0-9bb9-4844f040ea75.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

### The Mailbox chart

The **Mailbox** chart shows the total number of user or shared mailboxes in your organization, and the total number of user mailboxes that are active on any given day of the reporting period. A user mailbox is active if it had an email activity that included at least one of the following actions:

- Send
- Read
- Create appointment
- Send meeting
- Accept meeting
- Decline meeting
- Cancel meeting activity

Note

Shared mailboxes don't have activity independent of a user mailbox, so the report shows only a count of shared mailboxes when you select this mailbox type.

On the **Mailbox** chart:

- The Y axis is the number of user or shared mailboxes.
- The X axis is the selected date range for this specific report.

### The Storage chart

The **Storage** chart shows the amount of storage used in your organization by mailbox type. The **Storage** chart doesn't include archive mailboxes. For more information about auto-expanding archiving, see [Overview of auto-expanding archiving in Microsoft 365](../../compliance/autoexpanding-archiving).

On the **Storage** chart:

- The Y axis is the amount of storage used by user or shared mailboxes in your organization.
- The X axis is the selected date range for this specific report.

### The Quota chart

The **Quota** chart shows the number of user or shared mailboxes in each quota category. There are four quota categories:

- **Good**: The number of users or shared mailboxes whose storage used is below the "issue warning" quota.
- **Warning**: The number of users or shared mailboxes whose storage used is at or above the "issue warning" quota, but below the "prohibit send" quota.
- **Can't send**: The number of users or shared mailboxes whose storage used is at or above the "prohibit send" quota, but below the "prohibit send/receive" quota.
- **Can't send/receive**: The number of users or shared mailboxes whose storage used is at or above the "prohibit send/receive" quota.

On the **Quota** chart:

- The Y axis is the number of user or shared mailboxes in each storage quota.
- The X axis is the quota category.

Filter the charts you see by selecting an item in the legend.

### Exchange mailbox usage per mailbox table

The following table shows a breakdown of mailbox usage at the per mailbox level.

| Metric | Definition |
| --- | --- |
| Recipient type | Either Shared or User. |
| User name | The email address of the user. |
| Display Name | The full name of the user. |
| Deleted | The mailbox whose current state is deleted, but was active during some part of the reporting period of the report. |
| Deleted date | The date the mailbox was deleted. |
| Create date | The date the mailbox was created. |
| Last activity date | The date the mailbox last had an email send or read activity. |
| Item count | The total number of items in the mailbox. |
| Storage used (MB) | The total storage used. |
| Deleted Item Count | The total number of recoverable items in the mailbox. |
| Deleted Item Size (MB) | The total size of all recoverable items in the mailbox. |
| Issue warning quota (MB) | The mailbox storage limit when the mailbox owner receives a warning that it's about to hit the storage quota. |
| Prohibit send quota (MB) | The mailbox storage limit when the mailbox can no longer send emails. |
| Prohibit send receive quota (MB) | The mailbox storage limit when the mailbox can no longer send or receive emails. |
| Recoverable Item Quota (MB) | The mailbox storage limit for recoverable (deleted) items in the mailbox when the mailbox can no longer delete emails. |
| Report Period | The time period for which the report is available. |
| Has Archive | Shows if the mailbox has an online archive enabled. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

To learn more about the recoverable items folder, see [Recoverable Items folder in Exchange Online](/en-us/exchange/security-and-compliance/recoverable-items-folder/recoverable-items-folder#recoverable-items-mailbox-quotas).