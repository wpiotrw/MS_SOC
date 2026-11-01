---
layout: Conceptual
title: BitLocker for encryption | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/office-365-bitlocker-and-distributed-key-manager-for-encryption
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-09-08T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.collection:
- Strat_O365_Enterprise
- purview-compliance
- Strat_O365_Enterprise
description: Learn about how Office 365 uses BitLocker encryption, reducing the potential for data theft due to lost or stolen computers and disks.
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: 7455cb2b-04fe-6608-1073-0c835a0d1836
document_version_independent_id: 7455cb2b-04fe-6608-1073-0c835a0d1836
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/office-365-bitlocker-and-distributed-key-manager-for-encryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: office-365-bitlocker-and-distributed-key-manager-for-encryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/office-365-bitlocker-and-distributed-key-manager-for-encryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 2a1edcb6-4098-da0a-f05c-37587b91a0a3
---

# BitLocker for encryption | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Microsoft servers use BitLocker to encrypt the disk drives containing customer data at rest at the volume-level. BitLocker encryption is a data protection feature that is built into Windows. BitLocker is one of the technologies used to safeguard against threats in case there are lapses in other processes or controls (e.g., access control or recycling of hardware) that could lead to someone gaining physical access to disks containing customer data. In this case, BitLocker eliminates the potential for data theft or exposure because of lost, stolen, or inappropriately decommissioned computers and disks.

BitLocker is deployed with Advanced Encryption Standard (AES) 256-bit encryption on disks containing customer data in Exchange Online, SharePoint Online, and Skype for Business. Disk sectors are encrypted with a Full Volume Encryption Key (FVEK), which is encrypted with the Volume Master Key (VMK), which in turn is bound to the Trusted Platform Module (TPM) in the server. The VMK directly protects the FVEK and therefore, protecting the VMK becomes critical. The following figure illustrates an example of the BitLocker key protection chain for a given server (in this case, using an Exchange Online server).

The following table describes the BitLocker key protection chain for a given server (in this case, an Exchange Online server).

| KEY PROTECTOR | GRANULARITY | HOW GENERATED? | WHERE IS IT STORED? | PROTECTION |
| --- | --- | --- | --- | --- |
| AES 256-bit External Key | Per Server | BitLocker APIs | TPM or Secret Safe | Lockbox / Access Control |
|  |  |  | Mailbox Server Registry | TPM encrypted |
| 48-digit Numerical Password | Per Disk | BitLocker APIs | Active Directory | Lockbox / Access Control |
| X.509 Certificate as Data Recovery Agent (DRA) also called Public Key Protector | Environment (for example, Exchange Online multitenant) | Microsoft CA | Build System | No one user has the full password to the private key. The password is under physical protection. |

BitLocker key management involves the management of recovery keys that are used to unlock/recover encrypted disks in a Microsoft data center. Microsoft 365 stores the master keys in a secured share, only accessible by individuals who have been screened and approved. The credentials for the keys are stored in a secured repository for access control data (what we call a "secret store"), which requires a high level of elevation and management approvals to access using a just-in-time access elevation tool.

BitLocker supports keys which fall into two management categories:

- BitLocker-managed keys, which are short-lived and tied to the lifetime of an operating system instance installed on a server or to a given disk. These keys are deleted and reset during server reinstallation or disk formatting.
- BitLocker recovery keys, which are managed outside of BitLocker but used for disk decryption. BitLocker uses recovery keys for the scenario in which an operating system is reinstalled, and encrypted data disks already exist. Recovery keys are also used by Managed Availability monitoring probes in Exchange Online where a responder may need to unlock a disk.

BitLocker-protected volumes are encrypted with a full volume encryption key, which in turn is encrypted with a volume master key. BitLocker uses FIPS-compliant algorithms to ensure that encryption keys are never stored or sent over the wire in the clear. The Microsoft 365 implementation of customer data-at-rest-protection doesn't deviate from the default BitLocker implementation.