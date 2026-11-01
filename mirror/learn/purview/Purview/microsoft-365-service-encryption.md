---
layout: Conceptual
title: Service encryption and key management - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/microsoft-365-service-encryption
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-encryption
ms.date: 2023-12-15T00:00:00.0000000Z
search.appverid:
- MET150
ms.collection:
- Strat_O365_Enterprise
- purview-compliance
description: Understand service encryption's role in data resiliency in Microsoft 365. Learn about two key management options for Microsoft 365 workloads.
locale: en-us
document_id: 1c39d7dd-9137-5cb2-dbf5-599f15fef025
document_version_independent_id: 1c39d7dd-9137-5cb2-dbf5-599f15fef025
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/microsoft-365-service-encryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: microsoft-365-service-encryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/microsoft-365-service-encryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 342458bf-c404-7ccc-6d22-452debe8a3ea
---

# Service encryption and key management - Microsoft Purview | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

In addition to using volume-level encryption, Exchange Online, Microsoft Teams, SharePoint Online, OneDrive for Business, and Windows 365 Cloud PCs also use service encryption to encrypt customer data.

Service encryption allows for two key management options, Microsoft-managed keys and customer-managed keys.

Service encryption provides multiple benefits:

- Provides a layer of protection for all Microsoft 365 services and Windows 365 Cloud PCs. For Microsoft 365 services, service encryption is an extra layer of protection is on top of BitLocker.
- Provides separation of Windows operating system administrators from access to application data stored or processed by the operating system.
- Includes a Customer Key option that enables multitenant services to provide per-tenant key management.
- Enhances the ability of Microsoft 365 and Windows 365 to meet your specific compliance requirements regarding encryption.

## What are Microsoft-managed keys?

By default, Microsoft manages all cryptographic keys including the root keys for service encryption. This option, called *Microsoft-managed keys*, is enabled by default for Exchange Online, SharePoint Online, OneDrive for Business, and Windows 365 Cloud PCs. Microsoft-managed keys provide default service encryption unless you decide to onboard using Customer Key. If, at a later date, you decide to stop using Customer Key without following the data purge path, then your data stays encrypted using the Microsoft-managed keys. Your data is always encrypted at this default level at a minimum.

## What is Customer Key?

Customer Key is a customer-managed key solution. With Customer Key, you supply root keys used with service encryption and you manage these keys using Azure Key Vault while Microsoft manages all other keys. Customer Key is available for Exchange, SharePoint and OneDrive for Business, and Windows 365 Cloud PCs (Enterprise and Frontline modes).

Windows 365 support for Microsoft Purview Customer Key is generally available, including Windows 365 Frontline (Dedicated and Shared).

Using Customer Key, you generate your own cryptographic keys. You can use an on-premises Hardware Service Module (HSM) or Azure Key Vault (AKV) to generate your keys. AKV lets you control and manage the cryptographic keys used by Microsoft 365. Customer Key uses the keys stored in the AKV as the root of one of the key chains that encrypts your mailbox data or files.

Customer Key provides you with more control over how Microsoft processes your data. For example, You can use Customer Key as a technical control if you want to terminate service with Microsoft or remove a portion of your data stored in the cloud. Removing data ensures no one, including Microsoft, can access or process the data. Customer Key is in addition and complementary to Customer Lockbox that you use to control access to your data by Microsoft personnel.

To learn how to set up Customer Key for Exchange Online, Microsoft Teams, SharePoint Online, including Team Sites, and OneDrive for Business, see these articles:

- [Overview of Customer Key](customer-key-overview)
- [Set up Customer Key](customer-key-set-up)
- [Manage Customer Key](customer-key-manage)
- [Roll or rotate a Customer Key or an availability key](customer-key-availability-key-roll)
- [Understand the availability key](customer-key-availability-key-understand)