---
layout: Conceptual
title: Learn about archive mailboxes for Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-mailboxes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-10-14T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-mailboxes
ms.collection:
- purview-compliance
description: Learn about archive mailboxes to provide extra mailbox storage for users.
locale: en-us
document_id: 77ed15f2-2f58-8b89-4ac3-3723f7283f76
document_version_independent_id: 77ed15f2-2f58-8b89-4ac3-3723f7283f76
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-mailboxes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-mailboxes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-mailboxes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
platformId: 034e300a-dc37-091a-bcbc-1bbf58e29831
---

# Learn about archive mailboxes for Microsoft Purview | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use this article if you're an Exchange or compliance administrator and want to learn about mailbox archives that provide more storage space for users' online mailboxes. This additional mailbox storage might be needed to support your organization's message retention, eDiscovery, and hold requirements.

Note

Mailbox users can learn more about their archive mailbox storage by using the following article: [Manage email storage with online archive mailboxes](https://support.microsoft.com/office/manage-email-storage-with-online-archive-mailboxes-1cae7d17-7813-4fe8-8ca2-9a5494e9a721)

After you turn on archive mailboxes, sometimes also known as *In-Place Archiving*, a user's current mailbox becomes their *primary mailbox* and an additional and associated mailbox is created, called the *archive mailbox*.

Both mailboxes are considered a user's mailbox for compliance features such as Content search from the Microsoft Purview portal, Microsoft 365 retention, and Litigation Hold.

Users can access and store messages in their archive mailboxes by using Outlook and Outlook on the web. Users can also move or copy messages between their primary mailbox and their archive mailbox. They can also recover deleted items from the Recoverable Items folder in their archive mailbox by using the [Recover Deleted Items tool](https://support.microsoft.com/office/recover-deleted-items-in-outlook-for-windows-49e81f3c-c8f4-4426-a0b9-c0fd751d48ce).

## Managing archive mailboxes with messaging records management (MRM)

Messages can also be moved automatically to the archive mailbox by the [default Exchange retention policy](/en-us/exchange/security-and-compliance/messaging-records-management/default-retention-policy) from the [messaging records management (MRM) feature](/en-us/exchange/security-and-compliance/messaging-records-management/messaging-records-management). This default policy is automatically assigned to every mailbox and does the following actions:

- Moves items that are two years or older from a user's primary mailbox to their archive mailbox.
- Moves items that are 14 days or older from the Recoverable Items folder in the user's primary mailbox to the Recoverable Items folder in their archive mailbox.

You can customize your organization's Exchange MRM policy with [retention tags](/en-us/exchange/security-and-compliance/messaging-records-management/retention-tags-and-policies). For an example configuration, see [Customize an archive and deletion policy for mailboxes in your organization](set-up-an-archive-and-deletion-policy-for-mailboxes).

Note

MRM, like Microsoft 365 retention policies and retention labels, can also automatically delete emails after a specified period. As an older technology than Microsoft 365 retention, MRM continues to work side-by-side with retention policies and retention labels from Microsoft Purview. For more information, see [Use retention policies and retention labels instead of older features](retention#use-retention-policies-and-retention-labels-instead-of-older-features).

## Auto-expanding archiving

After a user's archive mailbox is enabled, up to 100 GB of extra storage becomes available. If users need more storage space than this 100 GB, enable auto-expanding archiving to provide up to 1.5 TB of additional storage in archive mailboxes. For more information, see [Learn about auto-expanding archiving](autoexpanding-archiving).

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

## Auto-archiving

If a user's primary mailbox fills up, auto-archiving helps prevent mail flow disruptions by automatically moving the oldest items to the archive mailbox when mailbox usage exceeds a safe threshold, which is 96% of the mailbox quota by default. Unlike the time-based MRM archive policy, auto-archiving is *threshold-based*: it's triggered by mailbox size rather than by item age, and it complements your existing archive and deletion policies without changing them.

Auto-archiving requires the archive mailbox to be provisioned and to have remaining storage capacity. Items tagged **Never Move to Archive** and recently received items are excluded, and the threshold is configurable for the organization. Setting the threshold to 100 turns off auto-archiving for the tenant. For more information, see [Auto-archiving in Exchange Online](/en-us/exchange/security-and-compliance/messaging-records-management/auto-archiving).