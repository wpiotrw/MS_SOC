---
layout: Conceptual
title: Technical reference details about encryption | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/technical-reference-details-about-encryption
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-11-12T00:00:00.0000000Z
audience: ITPro
ms.topic: reference
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
search.appverid:
- MET150
- MOE150
description: Learn about the various certificates, technologies, and Transport Layer Security (TLS) cipher suites used for encryption in Microsoft 365.
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: cb433e3c-42fb-682f-202b-688ca03151ae
document_version_independent_id: cb433e3c-42fb-682f-202b-688ca03151ae
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/technical-reference-details-about-encryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: technical-reference-details-about-encryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/technical-reference-details-about-encryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/e93f3d5f-c77d-4365-a7fb-c9f2234416c7
- https://authoring-docs-microsoft.poolparty.biz/devrel/0b654e73-5728-4af3-8c2e-17bfbf4c9f23
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/62e8d07a-cc62-4934-b30b-e168a571e51d
- https://authoring-docs-microsoft.poolparty.biz/devrel/11529658-843a-40bd-b2f8-5eed118be619
platformId: 7df9fccf-a8eb-b96a-0834-a82640c8d379
---

# Technical reference details about encryption | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Refer to this article for information about certificates, technologies, and TLS cipher suites used for [encryption in Microsoft 365](encryption). This article also provides details about planned deprecations.

- If you're looking for overview information, see [Encryption in Microsoft 365](encryption).
- If you're looking for setup information, see [Set up encryption in Microsoft 365 Enterprise](set-up-encryption).
- For specific information about TLS 1.1 and 1.0 deprecation, see [Disabling TLS 1.0 and 1.1 for Microsoft 365](tls-1.0-and-1.1-deprecation-for-office-365).
- For information about cipher suites supported by specific versions of Windows, see [Cipher Suites in TLS/SSL (Schannel SSP)](/en-us/windows/desktop/SecAuthN/cipher-suites-in-schannel).
- For certificate chains, see [Microsoft 365 encryption chains](encryption-office-365-certificate-chains) and [Microsoft 365 encryption chains - DOD and GCC High](encryption-office-365-certificate-chains-itar).

## Microsoft Office 365 certificate ownership and management

You don't need to purchase or maintain certificates for Office 365. Instead, Office 365 uses its own certificates.

## Current encryption standards and planned deprecations

To provide best-in-class encryption, Office 365 regularly reviews supported encryption standards. Sometimes, old standards are deprecated as they become out of date and less secure. This article describes currently supported cipher suites and other standards and details about planned deprecations.

## FIPS compliance for Microsoft 365

All cipher suites supported by Office 365 use algorithms acceptable under FIPS 140-2. Office 365 inherits FIPS validations from Windows (through Schannel). For information about Schannel, see [Cipher Suites in TLS/SSL (Schannel SSP)](/en-us/windows/desktop/SecAuthN/cipher-suites-in-schannel).

## AES256-CBC support for Microsoft 365

In late August 2023, Microsoft Purview Information Protection will begin to use Advanced Encryption Standard (AES) with 256-bit key length in Cipher Block Chaining mode (AES256-CBC). By October 2023, AES256-CBC will be the default for encryption of Microsoft 365 Apps documents and emails. You may need to take action to support this change in your organization.

### Who is impacted and what do I need to do?

Use this table to figure out if you have to take action:

| **Client applications** | **Service applications** | **Action required?** | **What do I need to do?** |
| --- | --- | --- | --- |
| Microsoft 365 Apps | Exchange Online, SharePoint Online | No | N/A |
| Office 2013, 2016, 2019, or 2021 | Exchange Online, SharePoint Online | Yes (Optional) | See Set up Office 2013, 2016, 2019, or 2021 for AES256-CBC mode. |
| Microsoft 365 Apps | Exchange Server or hybrid | Yes (Mandatory) | See Set up Exchange Server for AES256-CBC support. |
| Office 2013, 2016, 2019, or 2021 | Exchange Server or hybrid | Yes (Mandatory) | Complete Option 1 (required), and then see Set up Office 2013, 2016, 2019, or 2021 for AES256-CBC mode. |
| Microsoft 365 Apps | MIP SDK | Yes (Optional) | See Set up MIP SDK for AES256-CBC support. |
| Any | SharePoint Server | No | N/A |

#### Set up Office 2013, 2016, 2019, or 2021 for AES256-CBC mode

You need to configure Office 2013, 2016, 2019, or 2021 to use AES256-CBC mode using Group Policy, or by using the Cloud Policy service for Microsoft 365. Starting with version 16.0.16227 of Microsoft 365 Apps, CBC mode is used by default. Use the `Encryption mode for Information Rights Management (IRM)` setting under `User Configuration/Administrative Templates/Microsoft Office 2016/Security Settings`.

For example, to force CBC mode, select the group policy setting as follows:

Encryption mode for Information Rights Management (IRM): [1, Cipher Block Chaining (CBC)]

#### Set up Exchange Server for AES256-CBC support

Exchange Server doesn't support decrypting content that uses AES256-CBC. To work around this problem, you have two options.

##### Option 1

Customers using Exchange Online with the Azure Rights Management Connector service deployed will be opted out of the AES256-CBC publishing change in both Exchange Online and SharePoint Online.

To move to AES256-CBC mode, complete these steps:

1. Install the hotfix on your Exchange Servers when it becomes available. For the most recent information about ship dates, see the [Microsoft 365 product roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=117576).
2. If you're using Exchange Server with the Azure Rights Management Connector Service, you'll need to run the GenConnectorConfig.ps1 script on each Exchange server. For more information, see [Configure servers for the Rights Management connector](/en-us/azure/information-protection/configure-servers-rms-connector).

Once your organization has installed the patch across all of your Exchange Servers, open a support case and request these services to be enabled for AES256-CBC publishing.

##### Option 2

This option gives you some extra time before you need to patch all of your Exchange servers. Use this option if you're unable to complete the steps in option 1 when the hotfix becomes available. Instead, deploy group policy or client settings that force Microsoft 365 clients to keep using AES128-ECB mode. Deploy this setting using Group Policy, or by using the Cloud Policy service for Microsoft 365. You can configure Office and Microsoft 365 Apps for Windows to use ECB or CBC mode with the `Encryption mode for Information Rights Management (IRM)` setting under `User Configuration/Administrative Templates/Microsoft Office 2016/Security Settings`. Starting with version 16.0.16327 of Microsoft 365 Apps, CBC mode is used by default.

For example, to force EBC mode for Windows clients, set the group policy setting as follows:

Encryption mode for Information Rights Management (IRM): [2, Electronic Codebook (ECB)]

To configure settings for Office for Mac clients, see [Set suite-wide preferences for Office for Mac](/en-us/deployoffice/mac/preferences-office).

As soon as you can, complete the steps in option 1.

#### Set up MIP SDK for AES256-CBC support

Update to MIP SDK 1.13 or later. If you choose to update to MIP SDK 1.13, you'll need to configure a setting to force AES256-CBC. For more information, see the [MIP SDK Version 1.13.158 Critical Update](/en-us/information-protection/develop/version-release-history). Later versions of the MIP SDK will protect Microsoft 365 files and email with AES256-CBC by default.

## Versions of TLS supported by Microsoft 365

TLS, and SSL that came before TLS, are cryptographic protocols that secure communication over a network by using security certificates to encrypt a connection between computers. All Microsoft 365 support TLS version 1.2 (TLS 1.2). Support for TLS version 1.3 (TLS 1.3) is being rolled out throughout the service by the various applications and services. Exchange Online now supports TLS 1.3 for all email submissions and server communications with third-parties on the internet for worldwide customers. There is no timeline for TLS 1.3 for Exchange Online operated by 21Vianet.

Important

Be aware that TLS versions deprecate, and that deprecated versions *should not be used* where newer versions are available. If your legacy services do not require TLS 1.0 or 1.1 you should disable them.

## Deprecations

- Cipher suites: We are constantly reviewing our supported cipher suite list. We have stop supporting weak SHA1 message authentication, and the non-forward-secrecy RSA key exchange algorithm in the past. The current list of supported ciphers can be seen here: TLS cipher suites supported by Microsoft 365.
- TLS 1.0 and TLS 1.1 versions: Support for these TLS versions ended on October 31, 2018 with their removal from the service completed since 2022. All connections with Microsoft 365 now use at least TLS 1.2 to communicate. One exception is the SMTP AUTH client submission protocol in Exchange Online which offers an opt-in endpoint for customers with legacy devices that still need TLS 1.0 or TLS 1.1.
- 3DES algorithm: Support for this encryption algorithm ended on October 31, 2018. Microsoft 365 removed the cipher suite using it, TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA cipher suite, from the service from February 28, 2019. For a list of supported ciphers, see TLS cipher suites supported by Microsoft 365.
- SHA-1 certificates: Support in Microsoft 365 for communications where the other third-party provides SHA-1 certificates ended from June 2016. SHA-2 (Secure Hash Algorithm 2) or stronger hashing algorithms are now needed in the certificate chain.

## TLS cipher suites supported by Microsoft 365

TLS uses *cipher suites*, collections of encryption algorithms, to establish secure connections. Microsoft 365 supports the cipher suites listed in the following table. The table lists the cipher suites in order of strength, with the strongest cipher suite listed first.

Microsoft 365 responds to a connection request by first attempting to connect using the most secure cipher suite. If the connection doesn't work, Microsoft 365 tries the second most secure cipher suite in the list, and so on. The service continues down the list until the connection is accepted. Likewise, when Microsoft 365 requests a connection, the receiving service chooses whether to use TLS and which cipher suite to use.

| Cipher suite name | TLS protocol version |
| --- | --- |
| TLS\_AES\_256\_GCM\_SHA384 | 1.3 |
| TLS\_AES\_128\_GCM\_SHA256 | 1.3 |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 | 1.2 |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 | 1.2 |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 | 1.2 |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | 1.2 |

Note

Legacy TLS cipher suites may appear in external security scans of Exchange Online endpoints due to compatibility requirements for legacy SMTP AUTH client submission protocol. These cipher suites are retained for specific opt-in legacy TLS scenarios and aren't used for standard SMTP connections, which negotiate the strongest mutually supported TLS version and cipher suite.