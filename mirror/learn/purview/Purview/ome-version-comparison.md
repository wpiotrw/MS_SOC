---
layout: Conceptual
title: Message encryption version comparison | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ome-version-comparison
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
ms.topic: product-comparison
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
search.appverid:
- MET150
description: This article helps explain the differences between different versions of Microsoft message encryption.
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: cfb4cc94-b8f9-ab78-0c17-042d52b8247a
document_version_independent_id: cfb4cc94-b8f9-ab78-0c17-042d52b8247a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ome-version-comparison.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ome-version-comparison
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ome-version-comparison.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
platformId: 7c8b2e3a-e8ef-9cf9-f5f1-ab425a180352
---

# Message encryption version comparison | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Important

On February 28, 2021, Microsoft deprecated support for AD RMS in Exchange Online. If you've deployed a hybrid environment where your Exchange mailboxes are online and you're using IRM with Active Directory RMS on-premises, you'll need to migrate to Azure. Organizations that have deployed into the GCC Moderate environment are also affected. See "Overview of AD RMS deprecation in Exchange Online" in this article for information.

The rest of this article compares legacy Office 365 Message Encryption (OME) to Microsoft Purview Message Encryption and Microsoft Purview Advanced Message Encryption. Microsoft Purview Message Encryption is merger and newer version of both OME and Information Rights Management (IRM). Unique characteristics of deploying into GCC High are also outlined. The two can coexist in your organization. For information on how the new capabilities work, see [Office 365 Message Encryption (OME)](ome).

This article is part of a larger series of articles about message encryption. This article is intended for administrators and ITPros. If you're just looking for information on sending or receiving an encrypted message, see the list of articles in [Message encryption](ome) and locate the article that best fits your needs.

## Overview of AD RMS deprecation in Exchange Online

Exchange Online includes Information Rights Management (IRM) functionality that provides online and offline protection of email messages and attachments. By default, Exchange Online uses Azure Information Protection. However, your organization may have configured Exchange Online IRM to use on-premises Active Directory Rights Management Service (AD RMS). AD RMS support in Exchange Online is retiring. Instead, Azure Information Protection will replace AD RMS entirely.

To assess whether this deprecation impacts your organization, see [How to migrate AD RMS to Azure Rights Management in Exchange Online](/en-us/exchange/troubleshoot/administration/migrate-ad-rms-to-azure). This article provides recommendations on migration options.

## Side-by-side comparison of message encryption features and capabilities

| **Situation** | **Legacy OME** | **IRM in AD RMS** | **Microsoft Purview Message Encryption** |
| --- | --- | --- | --- |
| *Sending an encrypted mail* | Through Exchange mail flow rules | End-user initiated from Outlook desktop or Outlook on the Web; or through Exchange mail flow rules | End-user initiated from Outlook desktop, Outlook for Mac, or Outlook on the Web; through Exchange mail flow rules (also known as transport rules) and data loss prevention (DLP) |
| *Rights management template* | N/A | Do Not Forward option and custom templates | Do Not Forward option, encrypt-only option, and custom templates |
| *Recipient type* | Internal and external recipients | Internal recipients only | Internal and external recipients |
| *Experience for internal recipient* | Recipients receive an HTML message that they download and open in a web browser or mobile app | Native inline experience in Outlook clients | Native inline experience for recipients in the same organization using Outlook clients. Recipients can read message from encrypted message portal using clients other than Outlook (no download or app required). |
| *Experience for external recipient* | Recipients receive an HTML message that they download and open in a web browser or mobile app | N/A | Native inline experience for Microsoft 365 recipients. All other recipients can read message from OME portal (no download or app required). |
| *Attachment permissions* | No restrictions on attachments | Attachments are protected | Attachments are protected for the Do Not Forward option and custom templates. Admins can choose whether attachments for the encrypt-only option are protected or not. |
| *Bring your own key (BYOK) support* | None | None | BYOK supported |

## Advantages of Microsoft Purview Message Encryption over legacy OME

The new capabilities provide the following advantages:

- Ability to use the encrypt-only option (which enables secure collaboration), Do Not Forward option, and custom restrictions.
- Senders can send mail encrypted with the new capabilities manually from Outlook Desktop, Outlook for Mac and Outlook on the web clients.
- Microsoft 365 recipients get to use an inline experience in supported Outlook clients. Alternatively, admins can choose to show Microsoft 365 recipients a branded experience.
- Accounts outside of Microsoft 365, such as Gmail, Yahoo, and Microsoft accounts, are federated with the OME portal, which provides a better user experience for these recipients. All other identities use a one-time pass code to access encrypted messages.
- Admins can customize branding, and create multiple branding templates.
- Admins can revoke emails encrypted with the new capabilities.
- The new capabilities provide detailed usage reports through the Microsoft Purview portal.

## Microsoft Purview Advanced Message Encryption capabilities

Microsoft Purview Advanced Message Encryption offers more capabilities on top of Microsoft Purview Message Encryption. You must have Microsoft Purview Message Encryption set up in your organization in order to use Advanced Message Encryption. Also, in order to use these capabilities, recipients must view and reply to secure mail through the Microsoft Purview Message Encryption Portal. The advanced capabilities include:

- Message revocation
- Message expiration
- Multiple branding templates
- Encrypted message portal activity logs

For information on using Advanced Message Encryption, see [Microsoft Purview Advanced Message Encryption](ome-advanced-message-encryption).

## Unique characteristics of Microsoft Purview Message Encryption in a GCC High deployment

If you plan to use Microsoft Purview Message Encryption in a GCC High environment, there are some unique characteristics regarding the recipient experience.

### Encrypted email between GCC High and GCC High recipients

Senders can manually encrypt emails in Outlook for PC and Mac and Outlook on the web, or organizations can set up a policy to encrypt emails using Exchange mail flow rules.

Recipients inside GCC High receive the same inline reading experience in Outlook for PC and Mac and Outlook on the web as all other users.

### Encrypted email between GCC High and Non-GCC High recipients

Senders inside GCC High can send encrypted email outside of the GCC High boundary and vice versa.

All recipients outside GCC High, including commercial Microsoft 365 users, Outlook.com users, and other users of other email providers such as Gmail and Yahoo, receive a wrapper mail. This wrapper mail redirects the recipient to the Microsoft Purview Message Encryption Portal where the recipient can read and reply to the message. This is also true for senders outside GCC High sending OME encrypted mail to GCC High.

## Coexistence of legacy OME and Microsoft Purview Message Encryption in the same tenant

You can use both legacy OME and Microsoft Purview Message Encryption in the same tenant. As an administrator, you do this by choosing which version of message encryption you want to use when you create your mail flow rules.

- To specify the legacy version of OME, use the Exchange mail flow rule action **Apply the previous version of OME**.
- To specify Microsoft Purview Message Encryption, use the Exchange mail flow rule action **Apply Office 365 Message Encryption and rights protection**.

Users can manually send mail that is encrypted with Microsoft Purview Message Encryption from Outlook Desktop, Outlook for Mac, and Outlook on the web.

## Migrate from legacy OME to Microsoft Purview Message Encryption

Even though both versions can coexist, we highly recommend that you edit your old mail flow rules that use the rule action **Apply the previous version of OME** to use Microsoft Purview Message Encryption. Update these rules to use the mail flow rule action **Apply Office 365 Message Encryption and rights protection**, select "Encrypt" in the RMS template list. For instructions, see [Define mail flow rules to encrypt email messages](define-mail-flow-rules-to-encrypt-email).

## Get started with OME

Typically, Microsoft Purview Message Encryption is automatically enabled for your organization. For more information about Microsoft Purview Message Encryption within your organization, see [Set up Microsoft Purview Message Encryption](set-up-new-message-encryption-capabilities).

The legacy version of OME is automatically enabled for your organization if you have enabled Azure Information Protection. In the past, legacy OME worked even if Azure Information Protection wasn't enabled. This is no longer the case.

To start using legacy OME, if you have enabled Azure Information Protection, configure mail flow rules that use the rule action **Apply the previous version of OME**. For instructions, see [Define mail flow rules to encrypt email messages](define-mail-flow-rules-to-encrypt-email).