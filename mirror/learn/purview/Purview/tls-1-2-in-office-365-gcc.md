---
layout: Conceptual
title: Disabling TLS 1.0 and 1.1 in Microsoft 365 GCC High and DoD | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/tls-1-2-in-office-365-gcc
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discusses how Microsoft is disabling support for TLS 1.1 and 1.0 in GCC High and DoD environments in Microsoft 365.
author: k-reagle
manager: laurawi
search.appverid:
- MET150
audience: Admin
ms.service: purview
ms.subservice: purview-encryption
ms.topic: article
ms.reviewer: chvukosw
ms.date: 2025-01-10T00:00:00.0000000Z
ms.author: kreagle
ms.collection:
- purview-compliance
locale: en-us
document_id: 36b7a800-7963-7e51-d955-7f8c79c3bb82
document_version_independent_id: 36b7a800-7963-7e51-d955-7f8c79c3bb82
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/tls-1-2-in-office-365-gcc.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: tls-1-2-in-office-365-gcc
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/tls-1-2-in-office-365-gcc.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
platformId: 2194c7a5-b50c-3237-a233-c6e30dc79d3f
---

# Disabling TLS 1.0 and 1.1 in Microsoft 365 GCC High and DoD | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

## Summary

In order to comply with the latest compliance standards for the Federal Risk and Authorization Management Program (FedRAMP), we are disabling Transport Layer Security (TLS) versions 1.1 and 1.0 in Microsoft 365 for GCC High and DoD environments. This change was previously announced through Microsoft Support in [Preparing for the mandatory use of TLS 1.2 in Office 365](https://support.microsoft.com/help/4057306/preparing-for-tls-1-2-in-office-365).

The security of your data is important, and we are committed to transparency about changes that could affect your use of the service.

Although the [Microsoft TLS 1.0 implementation](https://support.microsoft.com/help/3117336) has no known security vulnerabilities, we remain committed to the FedRAMP compliance standards. Therefore, we disabled TLS 1.1 and 1.0 in Microsoft 365 in GCC High and DoD environments on January 15, 2020.

## More information

Starting on January 15, 2020, Microsoft 365 in the GCC High and DoD environments will disable TLS 1.1 and 1.0.

By January 15, 2020, all combinations of client servers and browser servers should use TLS version 1.2 (or a later version) to make sure that all connections can be made without issues to Microsoft 365. This may require updates to certain combinations of client servers and browser servers.

For SharePoint and OneDrive, you'll need to update and configure .NET to support TLS 1.2. For information, see [How to enable TLS 1.2 on clients](/en-us/mem/configmgr/core/plan-design/security/enable-tls-1-2-client).

You must update your client computers to make sure that you maintain uninterrupted access to Office 365 GCC High and DoD.

You'll need to update applications that call Microsoft 365 APIs over TLS 1.0 or TLS 1.1 to use TLS 1.2. .NET 4.5 defaults to TLS 1.1. To update your .NET configuration, see [How to enable Transport Layer Security (TLS) 1.2 on clients](/en-us/mem/configmgr/core/plan-design/security/enable-tls-1-2-client). For more information, see [Preparing for the mandatory use of TLS 1.2 in Office 365](https://support.microsoft.com/help/4057306/preparing-for-tls-1-2-in-office-365).

We know that the following client applications cannot use TLS 1.2:

- Android 4.3 and earlier versions
- Firefox version 5.0 and earlier versions
- Internet Explorer 8-10 on Windows 7 and earlier versions
- Internet Explorer 10 on Windows Phone 8.0
- Safari 6.0.4/OS X 10.8.4 and earlier versions

Although current analysis of connections to Microsoft Online services shows that most services and endpoints see little TLS 1.1 and 1.0 usage, we're providing notice of this change so that you can update any affected clients or servers as necessary before support for TLS 1.1 and 1.0 ends. If you are using any on-premises infrastructure for hybrid scenarios or Active Directory Federation Services (AD FS), make sure that the infrastructure can support both inbound and outbound connections that use TLS 1.2 (or a later version).

In addition to the outages that you might experience if you use the listed clients that cannot use TLS 1.2, removing TLS 1.1 and 1.0 will prevent you from being able to use the following Microsoft product:

- Lync phone

## References

For guidance and references to help make sure that your clients are using TLS 1.2, see [Preparing for the mandatory use of TLS 1.2 in Office 365](https://support.microsoft.com/help/4057306/preparing-for-tls-1-2-in-office-365).