---
layout: Conceptual
title: Disabling TLS 1.0 and 1.1 for Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/tls-1.0-and-1.1-deprecation-for-office-365
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Describes TLS 1.0 and 1.1 deprecation and disablement for Microsoft 365.
author: k-reagle
manager: laurawi
search.appverid:
- MET150
audience: ITPro
ms.service: purview
ms.subservice: purview-encryption
ms.topic: article
ms.author: kreagle
ms.reviewer: pefrem
ms.date: 2025-01-16T00:00:00.0000000Z
locale: en-us
document_id: 113c6c28-4535-8bbf-9992-136ed2889829
document_version_independent_id: 113c6c28-4535-8bbf-9992-136ed2889829
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/tls-1.0-and-1.1-deprecation-for-office-365.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: tls-1.0-and-1.1-deprecation-for-office-365
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/tls-1.0-and-1.1-deprecation-for-office-365.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 57860e84-d006-2eb1-7f11-3d8b79ce8d2e
---

# Disabling TLS 1.0 and 1.1 for Microsoft 365 | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Important

We have already disabled TLS 1.0 and 1.1 for most Microsoft 365 services in the world wide environment. For Microsoft 365 operated by 21 Vianet, TLS 1.0/1.1 was disabled on June 30, 2023.

As of October 31, 2018, the Transport Layer Security (TLS) 1.0 and 1.1 protocols are deprecated for the Microsoft 365 service. The effect for end-users is minimal. This change has been publicized for over two years, with the first public announcement made in December 2017. This article is only intended to cover the Office 365 local client in relation to the Office 365 service but can also apply to on-premises TLS issues with Office and Office Online Server/Office Web Apps.

For SharePoint and OneDrive, you'll need to update and configure .NET to support TLS 1.2. For information, see [How to enable TLS 1.2 on clients](/en-us/mem/configmgr/core/plan-design/security/enable-tls-1-2-client).

## Office 365 and TLS overview

The Office client relies on the Windows web service (WINHTTP) to send and receive traffic over TLS protocols. The Office client can use TLS 1.2 if the web service of the local computer can use TLS 1.2. All Office clients can use TLS protocols, as TLS and SSL protocols are part of the operating system and not specific to the Office client.

### On Windows 8 and later versions

By default, the TLS 1.2 and 1.1 protocols are available if no network devices are configured to reject TLS 1.2 traffic.

### On Windows 7

TLS 1.1 and 1.2 protocols are not available without the [KB 3140245](https://support.microsoft.com/help/3140245) update. The update addresses this issue and adds the following registry sub key:

```console
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp
```

Note

Windows 7 users who do not have this update are affected as of October 31, 2018. [KB 3140245](https://support.microsoft.com/help/3140245) has details about how to change WINHTTP settings to enable TLS protocols.

#### More information

The value of the **DefaultSecureProtocols** registry key that the KB article describes determines which network protocols can be used:

| DefaultSecureProtocols Value | Protocol enabled |
| --- | --- |
| 0x00000008 | Enable SSL 2.0 by default |
| 0x00000020 | Enable SSL 3.0 by default |
| 0x00000080 | Enable TLS 1.0 by default |
| 0x00000200 | Enable TLS 1.1 by default |
| 0x00000800 | Enable TLS 1.2 by default |
| 0x00002000 | Enable TLS 1.3 by default |

## Office clients and TLS registry keys

You can refer to [KB 4057306 Preparing for the mandatory use of TLS 1.2 in Office 365](https://support.microsoft.com/help/4057306). This is a general article for IT administrators, and it's official documentation about the TLS 1.2 change.

The following table shows the appropriate registry key values in Office 365 clients after October 31, 2018.

| Enabled protocols for Office 365 service after October 31, 2018 | Hexadecimal value |
| --- | --- |
| TLS 1.0 + 1.1 + 1.2 | 0x00000A80 |
| TLS 1.1 + 1.2 | 0x00000A00 |
| TLS 1.0 + 1.2 | 0x00000880 |
| TLS 1.2 | 0x00000800 |

Important

Don't use the SSL 2.0 and 3.0 protocols, which can also be set by using the **DefaultSecureProtocols** key. SSL 2.0 and 3.0 are considered outdated and insecure protocols. The best practice is to end the use of SSL 2.0 and SSL 3.0, although the decision to do this ultimately depends on what best meets your product needs. For more information about SSL 3.0 vulnerabilities, refer to [KB 3009008](https://support.microsoft.com/help/3009008).

You can use the default Windows Calculator in Programmer mode to set up the same reference registry key values. For more information, see [KB 3140245 Update to enable TLS 1.1 and TLS 1.2 as a default secure protocols in WinHTTP in Windows](https://support.microsoft.com/help/3140245).

Regardless if the Windows 7 update ([KB 3140245](https://support.microsoft.com/help/3140245)) is installed or not, the DefaultSecureProtocols registry sub key isn't present and must be added manually or through a group policy object (GPO). That is, unless you have to customize what secure protocols are enabled or restricted, this key is not required. You only need the Windows 7 SP1 ([KB 3140245](https://support.microsoft.com/help/3140245)) update.

## Update and configure the .NET Framework to support TLS 1.2

You'll need to update applications that call Microsoft 365 APIs over TLS 1.0 or TLS 1.1 to use TLS 1.2. .NET 4.5 defaults to TLS 1.1. To update your .NET configuration, see [How to enable Transport Layer Security (TLS) 1.2 on clients](/en-us/mem/configmgr/core/plan-design/security/enable-tls-1-2-client).

## More information

For more information, see [Preparing for the mandatory use of TLS 1.2 in Office 365](https://support.microsoft.com/help/4057306/preparing-for-tls-1-2-in-office-365).

## References

The following resources provide guidance to help make sure that your clients are using TLS 1.2 or a later version and to disable TLS 1.0 and 1.1:

- For Windows 7 clients that connect to Office 365, make sure that TLS 1.2 is the default secure protocol in WinHTTP in Windows. For more information, see [KB 3140245 - Update to enable TLS 1.1 and TLS 1.2 as default secure protocols in WinHTTP in Windows](https://support.microsoft.com/help/3140245/update-to-enable-tls-1-1-and-tls-1-2-as-a-default-secure-protocols-in).
- To address weak TLS usage by removing TLS 1.0 and 1.1 dependencies, see [TLS 1.2 support at Microsoft](https://cloudblogs.microsoft.com/microsoftsecure/2017/06/20/tls-1-2-support-at-microsoft/).
- [New IIS functionality](https://cloudblogs.microsoft.com/microsoftsecure/2017/09/07/new-iis-functionality-to-help-identify-weak-tls-usage/) makes it easier to find clients on [Windows Server 2012 R2](https://support.microsoft.com/help/4025335/windows-8-1-windows-server-2012-r2-update-kb4025335) and [Windows Server 2016](https://support.microsoft.com/help/4025334/windows-10-update-kb4025334) that connect to the service by using weak security protocols.
- Get more information about how to [solve the TLS 1.0 problem](https://www.microsoft.com/download/details.aspx?id=55266).
- For general information about our approach to security, go to the [Office 365 Trust Center](https://www.microsoft.com/trustcenter/cloudservices/office365).
- [Preparing for TLS 1.0/1.1 Deprecation - Office 365 Skype for Business](https://techcommunity.microsoft.com/t5/Skype-for-Business-Blog/Preparing-for-TLS-1-0-1-1-Deprecation-O365-Skype-for-Business/ba-p/222247)
- [Exchange Server TLS guidance, part 1: Getting Ready for TLS 1.2](https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-1-getting-ready-for-tls-1-2/ba-p/607649)
- [Exchange Server TLS guidance Part 2: Enabling TLS 1.2 and Identifying Clients Not Using It](https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-2-enabling-tls-1-2-and/ba-p/607761)
- [Exchange Server TLS guidance Part 3: Turning Off TLS 1.0/1.1](https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-3-turning-off-tls-1-0-1-1/ba-p/607898)
- [Enable TLS 1.1 and TLS 1.2 support in Office Online Server](/en-us/officeonlineserver/enable-tls-1-1-and-tls-1-2-support-in-office-online-server)