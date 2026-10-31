---
layout: Conceptual
title: How Exchange Online secures your email secrets | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/exchange-online-secures-email-secrets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-03-31T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
ms.collection:
- purview-compliance
description: 'In addition to the Microsoft Trust Center that provides Security, Privacy, and Compliance Information for Microsoft 365, learn how Microsoft helps protect secrets you store in its data centers. '
locale: en-us
document_id: 0ea35d4a-11af-dd7c-daba-9edda978ab04
document_version_independent_id: 0ea35d4a-11af-dd7c-daba-9edda978ab04
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/exchange-online-secures-email-secrets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: exchange-online-secures-email-secrets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/exchange-online-secures-email-secrets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6a585d33-2e08-2cae-2607-47aa23f49e6e
---

# How Exchange Online secures your email secrets | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

This article describes how Microsoft secures your email secrets in its data centers.

## How we secure secret information provided by you

In addition to the Office 365 Trust Center that provides [Security, Privacy, and Compliance Information for Office 365](/en-us/compliance/assurance/stp-get-started?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json), we use a technology called Distributed Key Manager (DKM).

[Distributed Key Manager](office-365-bitlocker-and-distributed-key-manager-for-encryption) (DKM) is a client-side technology that uses a set of secret keys to encrypt and decrypt information. Only members of a specific security group in Active Directory Domain Services can access those keys in order to decrypt the data that is encrypted by DKM. In Exchange Online, only certain service accounts under which the Exchange processes run are part of that security group. No human is given credentials that are part of this security group and therefore no human has access to the keys that can decrypt these secrets.

For debugging, troubleshooting, or auditing purposes, a data center administrator must request elevated access to gain temporary credentials that are part of the security group. This process requires multiple levels of legal approval. If access is granted, all activity is logged and audited. Access is only granted for a set interval of time after which it automatically expires.

For extra protection, DKM technology includes automated key rollover and archiving. Automated rollover and archiving ensure that you can continue to access your older content without having to rely on the same key indefinitely.

## Where Exchange Online uses DKM

Microsoft uses [Distributed Key Manager](office-365-bitlocker-and-distributed-key-manager-for-encryption) to encrypt your secrets in Exchange Online data centers. For example:

- Email account credentials for connected accounts. Connected accounts are third-party accounts such as Hotmail, Gmail, and Yahoo! mail accounts.
- Customer Key. If you're using [Customer Key](customer-key-overview), you'll use [Azure Key Vault](/en-us/azure/key-vault/key-vault-whatis) to safeguard your secrets.