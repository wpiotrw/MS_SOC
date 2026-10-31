---
layout: Conceptual
title: Learn about auto-expanding archiving | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/autoexpanding-archiving
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
ms.reviewer: sspandey11
manager: laurawi
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1017
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-mailboxes
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
ms.assetid: 37cdbb02-a24a-4093-8bdb-2a7f0b3a19ee
description: Learn about auto-expanding archiving, which provides additional archive storage for Exchange Online mailboxes.
locale: en-us
document_id: 40906380-b761-8e76-a010-f5b3d11987b6
document_version_independent_id: 40906380-b761-8e76-a010-f5b3d11987b6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/autoexpanding-archiving.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: autoexpanding-archiving
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/autoexpanding-archiving.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 075bd32c-a5b2-acc3-82e5-0b991d505d7e
---

# Learn about auto-expanding archiving | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Archive mailboxes in Microsoft Purview provide user mailboxes and shared mailboxes with additional mailbox storage space. After an archive mailbox is enabled, up to 100 GB of additional storage becomes available.

This archiving feature in Microsoft Purview (called *auto-expanding archiving*) provides up to 1.5 TB of additional storage in archive mailboxes. When the storage quota in the archive mailbox is reached, Microsoft Purview automatically (and incrementally) increases the size of the archive until the archive mailbox reaches 1.5 TB.

For step-by-step instructions for turning on auto-expanding archiving, see [Enable auto-expanding archiving](enable-autoexpanding-archiving).

## How auto-expanding archiving works

When auto-expanding archiving is enabled for a user's mailbox archive or a shared mailbox archive, Microsoft Purview periodically checks the size of the archive mailbox. When the archive mailbox gets close to its storage limit, additional storage space is automatically created and this process continues until the mailbox archive reaches 1.5 TB. The additional storage creation happens automatically, which means administrators don't have to request additional archive storage or manage auto-expanding archiving.

Important

Microsoft is increasing the maximum auto-expanding archive capacity for eligible Exchange Online mailboxes from 1.5 TB to 3 TB. Rollout begins in mid-October 2026 and is expected to complete by late October.

The increase applies to mailboxes assigned the following eligible licenses:

- Office 365 E5, A5, or G5
- Microsoft 365 E5, A5, or G5
- Microsoft 365 Purview Suite
- Microsoft 365 Purview Suite FLW, EDU, or GOV
- Microsoft Defender + Purview Suite FLW
- Microsoft 365 F5 Compliance
- Microsoft 365 F5 Security + Compliance
- The combination of the eDiscovery & Audit, Insider Risk Management, and Information Protection & Governance mini suites

Qualifying offerings that include Microsoft Purview E5 capabilities, such as E7, also support the increase. **For all other licenses, the existing 1.5 TB limit remains unchanged.**

For E5 licenses, verify that **Records Management** is selected and remains enabled in the user's license settings.

If auto-expanding archiving is already enabled, no additional configuration or per-GB charge applies. Existing archive content, retention policies, and holds are unchanged. Verify license eligibility and monitor archive growth.

Here's a quick overview of the process.

![Overview of the auto-expanding archiving process.](media/74355385-d990-44fe-8a87-6c3639d1f63f.png)

1. Archiving is enabled for a user mailbox or a shared mailbox. An archive mailbox with 100 GB of storage space is created, and the warning quota for the archive mailbox is set to 90 GB.
2. An administrator enables auto-expanding archiving for the mailbox. If the mailbox has a hold or retention policy applied to it, the storage quota for the archive mailbox is increased to 110 GB and the archive warning quota is increased to 100 GB.

    Then, when the archive mailbox (including the Recoverable Items folder) reaches its storage quota, the archive mailbox is converted to an auto-expanding archive. Extra storage space is added until it reaches a maximum size of 1.5 TB. It can take up to 30 days for the additional storage space to be provisioned.
3. Microsoft Purview automatically adds more storage space when necessary.

For information what happens when the maximum 1.5 TB is reached, and other size-related limitations for email storage, see Important considerations and limitations for auto-expanding archiving on this page.

## What gets moved to the additional archive storage space?

To make efficient use of auto-expanding archive storage, folders may get moved. Microsoft Purview determines which folders get moved when additional storage is added to the archive. Sometimes when a folder is moved, one or more subfolders are automatically created and items from the original folder are distributed to these folders to facilitate the moving process. You might need to communicate this behavior to end users after enabling their mailbox for auto-expanding archives, to help set expectations.

When viewing the archive portion of the folder list in Outlook, these subfolders are displayed under the original folder. The naming convention that Microsoft 365 uses to name these subfolders is **&lt;folder name&gt;\_yyyy (Created on mmm dd, yyyy h\_mm)**, where:

- **yyyy** is the year the messages in the folder were received.
- **mmm dd, yyyy h\_m** is the date and time that the subfolder was created by Office 365, in UTC format, based on the user's time zone and regional settings in Outlook.

The following screenshots show a folder list before and after messages are moved to an auto-expanded archive.

**Before additional storage is added**

![Folder list of archive mailbox before auto-expanding archive is provisioned.](media/5d6d6420-e562-4912-aaab-1c111762b3f6.png)

**After additional storage is added**

![Folder list of archive mailbox after auto-expanding archive is provisioned.](media/c03c5f51-23fa-4fc2-b887-7e7e5cce30da.png)

Note

In some scenarios, a small number of archive mailboxes might display "Inbox\_Archive" and/or "Sent Items\_Archive" folders. These folders, if present, are part of organizational enhancements to maintain the archive folder structure. Users can continue to access their archived emails without any issues, and these folders don't affect the functionality or performance of the mailbox.

As previously described, Microsoft Purview moves items to subfolders (and names them using the naming convention described above) to help distribute content to an auxiliary archive. But moving items to subfolders might not always be the case. Sometimes an entire folder may be moved to an auxiliary archive. In this case, the folder will retain its original name. It won't be apparent in the folder list in Outlook that the folder was moved to an auxiliary archive.

## Important considerations and limitations for auto-expanding archiving

Auto-expanded archiving is supported by new Outlook for Windows, classic Outlook for Windows, and Outlook on the web.

If a mailbox with an auto-expanding archive reaches a total of 1.5 TB of data stored in the auto-expanding archive, no more data will be stored in the auto-expanding archive or moved from the main archive to the auto-expanding archive.

Note

The size that counts toward the 1.5 TB limit is the total of all items in the archive, including items in the Recoverable Items folder. An archive can therefore approach its limit even when the visible item size looks smaller. Additional storage is provisioned automatically and can take up to 30 days, and auto-expanding archiving supports a growth rate of no more than 1 GB per day.

Should the main archive also reaches its quota, no more data will be stored there, which can result in the primary mailbox also reaching its quota. Then, processing can stop for sending or receiving email and other items. To reduce this risk and minimize liability for your organization, we recommend using Microsoft 365 retention policies to delete content that no longer has business value. Configure these policies to [delete items after a specified period](retention-settings#settings-for-retaining-and-deleting-content). If you're not yet familiar with retention policies that can automatically delete email and other Microsoft 365 items, see [Learn about retention policies and retention labels](retention).

Auto-expanding archiving is supported only for mailboxes used for individual users (or shared mailboxes) with a growth rate that doesn't exceed 1 GB per day. A user's archive mailbox is intended for just that user. Using journaling, transport rules, or auto-forwarding rules to copy messages to an archive mailbox isn't permitted. Microsoft reserves the right to deny additional archiving in instances where a user's archive mailbox is used to store archive data for other users or in other cases of the inappropriate use.

Here are some things to consider before you enable a mailbox for auto-expanding archives:

- Users can access any folder in their archive mailbox, including ones that were moved to the auto-expanded storage area.
- If an archive mailbox has at least one auto-expanded storage area, users can't delete a folder from the archive mailbox or from the auxiliary archive. In other words, after an auto-expanded storage area has been provisioned, they can't delete any folders in the archive.
- Users can delete items in an auto-expanded storage area. However, they can't use the [Recover Deleted Items feature](https://support.microsoft.com/office/recover-deleted-items-in-outlook-for-windows-49e81f3c-c8f4-4426-a0b9-c0fd751d48ce) to recover an item after auto-expanding archiving is enabled for their mailbox.
- Users can search for items in an auto-expanded archive with the following limitations:

    - For classic Outlook on Windows, search is restricted to the current Outlook search scope. For example, search from the primary mailbox won’t return items from auto-expanded archives.
    - Not supported in a cloud-only archive situation (primary mailbox still on-premises).
- Item counts in Outlook and Read/Unread counts (in Outlook and Outlook on the web) in an auto-expanded archive might not be accurate.

## Auto-expanding archiving and other compliance features

This section explains the functionality between auto-expanding archiving and other compliance features.

- **eDiscovery:** When you use an eDiscovery tool, such as Content Search, the additional storage areas in an auto-expanded archive are also searched.
- **Retention:** When you put a mailbox on hold by using methods such as Microsoft 365 retention, eDiscovery case holds, and Litigation Hold in Exchange Online, content located in an auto-expanded archive is also placed on hold.
- **Messaging records management (MRM):** If you use MRM deletion policies in Exchange Online to permanently delete expired mailbox items, expired items located in the auto-expanded archive will also be deleted.