---
layout: Conceptual
title: Overview of Customer Key - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/customer-key-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.reviewer: chrwarren
ms.date: 2025-02-03T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
ms.custom:
- seo-marvel-apr2020
- sfi-ga-nochange
description: In this article, learn about how Microsoft Purview Customer Key works to protect your data in Microsoft's datacenters using keys you provide and control.
locale: en-us
document_id: 6a3a6d3d-823d-6b0f-98f4-c8051caa35e5
document_version_independent_id: 6a3a6d3d-823d-6b0f-98f4-c8051caa35e5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/customer-key-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: customer-key-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/customer-key-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 1eb8eab3-70db-b754-9399-82712cbfb542
---

# Overview of Customer Key - Microsoft Purview | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Microsoft 365 provides baseline, volume-level encryption through BitLocker and Distributed Key Manager (DKM). Windows 365 Enterprise and Business Cloud PC disks are encrypted using Azure Storage server-side encryption (SSE).

To give you more control, Microsoft 365 also offers an added layer of encryption for your content through Customer Key. This content includes data from Microsoft Exchange, SharePoint, OneDrive, Teams, and Windows 365 Cloud PCs (Enterprise), including Windows 365 Frontline Dedicated and Shared modes.

BitLocker isn’t supported as an encryption option for Windows 365 Cloud PCs. For details, see [Using Windows 10 virtual machines in Intune](/en-us/mem/intune/fundamentals/windows-10-virtual-machines).

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## How service encryption, BitLocker, SSE, and Customer Key work together

Your Microsoft 365 data is always encrypted at rest using BitLocker and Distributed Key Manager (DKM). For details, see [How Exchange secures your email secrets](exchange-online-secures-email-secrets).

Customer Key adds extra protection against unauthorized access to your data. It complements BitLocker disk encryption and server-side encryption (SSE) in Microsoft data centers. Customer Key helps you meet compliance or regulatory requirements by letting you control the root encryption keys at the application level.

You explicitly authorize Microsoft 365 to use your encryption keys to deliver value-added services like eDiscovery, anti-malware, anti-spam, and search indexing. Microsoft 365 uses these keys to encrypt your data at rest, as described in the [Online Services Terms (OST)](https://www.microsoft.com/licensing/docs/view/licensing-use-rights).

## Customer Key with hybrid deployments

Customer Key encrypts only data at rest in the cloud. It doesn’t protect on-premises mailboxes or files. To protect on-premises data, use a separate method like BitLocker.

## Learn about data encryption policies

A data encryption policy (DEP) defines the encryption hierarchy. Services use this hierarchy to encrypt data with both the keys you manage and the availability key that Microsoft protects. You create a DEP using PowerShell cmdlets, then assign it to encrypt application data.

Customer Key supports three types of DEPs. Each type uses different cmdlets and protects a different kind of data:

### DEP for Multiple Microsoft 365 workloads

These DEPs encrypt data across several Microsoft 365 workloads for all users in the tenant:

- **Windows 365 Cloud PCs** (Enterprise), including Frontline Dedicated and Shared modes ([details](/en-us/windows-365/enterprise/purview-customer-key))
- **Teams**: Chat messages, media messages, calls/meeting recordings (in Teams storage), notifications, Cortana suggestions, status messages
- **Microsoft 365 Copilot** interactions
- **Exchange**: User/signal information and mailboxes not covered by a mailbox DEP
- **Microsoft Purview Information Protection**: EDM data (schemas, rule packages, salts), sensitivity label configurations

Note

For EDM and Teams, the DEP encrypts new data from assignment. For Exchange, it encrypts all existing and new data.

**Not encrypted by multi-workload DEPs** (protected by other methods):

- SharePoint and OneDrive data (use SharePoint DEP)
- Teams files and recordings saved in SharePoint/OneDrive
- Teams Live Events, Viva Engage, Planner

You can create multiple DEPs per tenant but assign only one at a time. Encryption begins automatically after assignment.

### DEPs for Exchange mailboxes

Mailbox DEPs give you more control over individual Exchange Online mailboxes. You can use them to encrypt data in UserMailbox, MailUser, Group, PublicFolder, and Shared mailboxes.

You can have up to 50 active mailbox DEPs per tenant. You can assign one DEP to multiple mailboxes, but only one DEP per mailbox.

By default, Exchange mailboxes are encrypted using Microsoft-managed keys. When you assign a Customer Key DEP, the service rewraps existing encrypted mailboxes on next access. Unencrypted mailboxes are marked for a move, with encryption occurring after the move completes. For details on move priorities, see [Move requests in the Microsoft 365 service](/en-us/exchange/mailbox-migration/office-365-migration-best-practices#move-requests-in-the-microsoft-365-or-office-365-service).

You can later refresh the DEP or assign a different one as described in [Manage Customer Key for Office 365](customer-key-manage).

Each mailbox must meet licensing requirements to use Customer Key. For more info, see [Prerequisites](customer-key-set-up#prerequisites).

You can assign DEPs to shared, public folder, and group mailboxes as long as your tenant meets the licensing requirements for user mailboxes. You don’t need separate licenses for non-user-specific mailboxes.

You can also request that Microsoft purge specific DEPs when leaving the service. Revoking access to your keys triggers deletion of the availability key, resulting in cryptographic deletion of your data. For details, see [Revoke your keys and start the data purge path process](customer-key-manage#revoke-your-keys-and-start-the-data-purge-path).

### DEP for SharePoint and OneDrive

This DEP encrypts content stored in SharePoint and OneDrive, including Teams files stored in SharePoint. Multi-geo tenants can create one DEP per geo; single-geo tenants can create one DEP. For setup instructions, see [Set up Customer Key](customer-key-set-up).

### Encryption ciphers used by Customer Key

Customer Key uses different encryption ciphers to protect keys, as shown in the following diagrams.

The key hierarchy used for DEPs that encrypt data across multiple Microsoft 365 workloads is similar to the one used for individual Exchange mailboxes. The corresponding Microsoft 365 Workload Key replaces the Mailbox Key.

#### Encryption ciphers used to encrypt keys for Exchange

![Encryption ciphers for Exchange Customer Key.](media/customerkeyencryptionhierarchiesexchangeskype.png)

#### Encryption ciphers used to encrypt keys for SharePoint and OneDrive

![Encryption ciphers for SharePoint Customer Key.](media/customerkeyencryptionhierarchiessharepointonedriveteamsfiles.png)