---
layout: Conceptual
title: Encryption in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/encryption
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-12-06T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
- MOE150
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
description: With Microsoft 365, your content is encrypted at rest and in transit with the strongest encryption, protocols, and technologies available. Get an overview of encryption in Microsoft 365.
locale: en-us
document_id: be54dcb7-50bd-2b97-a3ff-687022e48337
document_version_independent_id: be54dcb7-50bd-2b97-a3ff-687022e48337
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/encryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: encryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/encryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: e5fc9e17-64ff-5334-1820-1206503938d0
---

# Encryption in Microsoft 365 | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Encryption is an important part of your file protection and information protection strategy. This article provides an overview of encryption for Microsoft 365. Get help with encryption tasks like how to set up encryption for your organization and how to password-protect Microsoft 365 documents.

- For information about certificates and technologies like TLS, see [Technical reference details about encryption in Microsoft 365](technical-reference-details-about-encryption).
- For an overview of how to configure or set up encryption for your organization, see [Set up encryption in Microsoft 365 Enterprise](set-up-encryption).

## What is encryption, and how does it work in Microsoft 365?

The encryption process encodes your data (referred to as plaintext) into ciphertext. Unlike plaintext, ciphertext can't be used by people or computers unless and until the ciphertext is decrypted. Decryption requires an encryption key that only authorized users have. Encryption helps ensure that only authorized recipients can decrypt your content. Content includes files, email messages, calendar entries, and so on.

Encryption by itself doesn't prevent content interception. Encryption is part of a larger information protection strategy for your organization. By using encryption, you help ensure that only authorized parties can use the encrypted data.

You can have multiple layers of encryption in place at the same time. For example, you can encrypt email messages and also the communication channels through which your email flows. With Microsoft 365, your data is encrypted at rest and in transit, using several strong encryption protocols, and technologies that include Transport Layer Security/Secure Sockets Layer (TLS/SSL), Internet Protocol Security (IPSec), and Advanced Encryption Standard (AES).

## Encryption for data at rest and data in transit

**Examples of data at rest** include files that you uploaded to a SharePoint library, Project Online data, documents that you uploaded in a Skype for Business meeting, email messages, and attachments that you stored in folders in your mailbox, and files you uploaded to OneDrive.

**Examples of data in transit** include mail messages that are in the process of being delivered, or conversations that are taking place in an online meeting. In Microsoft 365, data is in transit whenever a user's device is communicating with a Microsoft server, or when a Microsoft server is communicating with another server.

With Microsoft 365, multiple layers and kinds of encryption work together to secure your data. The following table includes some examples, with links to additional information.

| **Kinds of Content** | **Encryption Technologies** | **Resources to learn more** |
| --- | --- | --- |
| Files on a device. These files can include email messages saved in a folder, documents saved on a computer, tablet, or phone, or data saved to the Microsoft cloud. | BitLocker in Microsoft data centers. BitLocker can also be used on client machines, such as Windows computers and tabletsDistributed Key Manager (DKM) in Microsoft data centersCustomer Key for Microsoft 365 | [Windows IT Center: BitLocker](/en-us/windows/device-security/bitlocker/bitlocker-overview)[Microsoft Trust Center: Encryption](https://www.microsoft.com/TrustCenter/Security/Encryption)[Cloud security controls series: Encrypting Data at Rest](https://blogs.microsoft.com/microsoftsecure/2015/09/10/cloud-security-controls-series-encrypting-data-at-rest)[How Exchange Online secures your email secrets](exchange-online-secures-email-secrets)[Service encryption with Microsoft Purview Customer Key](customer-key-overview) |
| Files in transit between users. These files can include Microsoft 365 documents or SharePoint list items shared between users. | TLS for files in transit | [Data Encryption in OneDrive and SharePoint](data-encryption-in-odb-and-spo)[Skype for Business Online: Security and Archiving](/en-us/office365/servicedescriptions/skype-for-business-online-service-description/skype-for-business-online-features) |
| Email in transit between recipients. This email includes email hosted by Exchange Online. | Microsoft Purview Message Encryption with the Azure Rights Management service, S/MIME, and TLS for email in transit | [Message Encryption](ome)[Email encryption in Microsoft 365](email-encryption)[How Exchange Online uses TLS to secure email connections in Microsoft 365](exchange-online-uses-tls-to-secure-email-connections) |
| Chats, messages, and files in transit between recipients using Microsoft Teams. | Teams uses TLS and MTLS to encrypt instant messages. Media traffic is encrypted using Secure RTP (SRTP). Teams uses FIPS (Federal Information Processing Standard) compliant algorithms for encryption key exchanges. | [Encryption for Teams](/en-us/microsoftteams/teams-security-guide#encryption-for-teams) |

## Microsoft 365 Crypto Update

In late August 2023, Microsoft Purview Information Protection began to use Advanced Encryption Standard (AES) with 256-bit key length in Cipher Block Chaining mode (AES256-CBC). By October 2023, AES256-CBC became the default for encryption of Microsoft 365 Apps documents and emails. You might need to take action to support this change in your organization. For more information, see [Technical reference details about encryption](technical-reference-details-about-encryption).

## What if I need more control over encryption to meet security and compliance requirements?

Microsoft 365 provides Microsoft-managed solutions for volume encryption, file encryption, and mailbox encryption in Microsoft 365. In addition, Microsoft provides encryption solutions that you can manage and control. These encryption solutions are built on Azure.

To learn more, see the following resources:

- [Learn about the Azure Rights Management encryption service](azure-rights-management-learn-about)
- [Set up Information Rights Management (IRM) in SharePoint admin center](set-up-irm-in-sp-admin-center)
- [Overview of Customer Key](customer-key-overview)
- [Double Key Encryption](double-key-encryption)

## How do I...

| **To do this task** | **See these resources** |
| --- | --- |
| Set up encryption for my organization | [Set up encryption in Microsoft 365 Enterprise](set-up-encryption) |
| View details about certificates, technologies, and TLS cipher suites | [Technical details about encryption](technical-reference-details-about-encryption) |
| Work with encrypted messages on a mobile device | [View encrypted messages on your Android device](https://support.office.com/article/83d60f17-2305-407a-a762-7d518401fdeb)[View encrypted messages on your iPhone or iPad](https://support.microsoft.com/en-us/office/view-protected-messages-on-your-iphone-or-ipad-4d631321-0d26-4bcc-a483-d294dd0b1caf) |
| Encrypt a document using password protection. (Password protection isn't supported in a browser. Use desktop versions of Word, Excel, and PowerPoint for password protection.) | [Add or remove protection in your document, workbook, or presentation](https://support.office.com/article/05084cc3-300d-4c1a-8416-38d3e37d6826). Choose an **Add protection** section, and then see **Encrypt with Password**. |
| Remove encryption from a document | [Add or remove protection in your document, workbook, or presentation](https://support.office.com/article/05084cc3-300d-4c1a-8416-38d3e37d6826). Choose a **Remove protection** section, and then see **Remove password encryption**. |