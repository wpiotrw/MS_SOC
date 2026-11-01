---
layout: Conceptual
title: Microsoft Purview Message Encryption | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ome
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-encryption
ms.date: 2025-01-10T00:00:00.0000000Z
search.appverid:
- MET150
ms.collection:
- purview-compliance
ms.custom:
- seo-marvel-apr2020
description: Learn how to send and receive encrypted email messages between people inside and outside your organization.
locale: en-us
document_id: be09a518-06e2-de7b-1279-196e7b5374dd
document_version_independent_id: be09a518-06e2-de7b-1279-196e7b5374dd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ome.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ome
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ome.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 3f7c3bf5-394c-6db3-70cc-db771b8be39d
---

# Microsoft Purview Message Encryption | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

People often use email to exchange sensitive information, such as financial data, legal contracts, confidential product information, sales reports and projections, patient health information, or customer and employee information. As a result, mailboxes can become repositories for large amounts of potentially sensitive information and information leakage can become a serious threat to your organization.

With Message encryption, your organization can send and receive encrypted email messages between people inside and outside your organization. Message encryption works with Outlook.com, Yahoo!, Gmail, and other email services. Email message encryption helps ensure that only intended recipients can view message content.

## How Message Encryption works

The rest of this article applies to Microsoft Purview Message Encryption. Office 365 Message Encryption (OME) was deprecated.

Microsoft Purview Message Encryption is an online service that's built on the Azure Rights Management service which is part of Microsoft Purview Information Protection. This service includes encryption, identity, and authorization policies to help secure your email. You can encrypt messages by using rights management templates, the [Do Not Forward option](rights-management-usage-rights#do-not-forward-option-for-emails), and the [encrypt-only option](rights-management-usage-rights#encrypt-only-option-for-emails).

Users can then encrypt email messages and various attachments by using these options. For a full list of supported attachment types, see ["File types covered by IRM policies when they're attached to messages" in Introduction to IRM for email messages](https://support.office.com/article/bb643d33-4a3f-4ac7-9770-fd50d95f58dc#FileTypesforIRM).

As an administrator, you can also define Exchange mail flow rules (also known as transport rules) to apply this protection. For example, you can create a rule that requires the encryption of all messages addressed to a specific recipient, or that contains specific words in the subject line, and also specify that recipients can't copy or print the contents of the message.

Message encryption provides a unified sender experience whether you're sending mail inside your organization or to recipients outside of Microsoft 365. In addition, recipients who receive a protected email message sent to a Microsoft 365 account in Outlook 2016 or Outlook on the web, don't have to take any other action to view the message. It works seamlessly. Recipients using other email clients and email service providers also have an improved experience. For information, see [Learn about protected messages in Microsoft 365](https://support.microsoft.com/office/2baf3ac7-12db-40a4-8af7-1852204b4b67) and [How do I open a protected message](https://support.microsoft.com/office/1157a286-8ecc-4b1e-ac43-2a608fbf3098).

For a detailed list of the differences between the previous version of OME and Microsoft Purview Message Encryption, see [Compare versions of message encryption](ome-version-comparison).

When someone sends an email message that matches an encryption mail flow rule, the message is encrypted before it's sent. All Microsoft 365 end users that use Outlook clients to read mail receive native, first-class reading experiences for encrypted and rights-protected mail even if they're not in the same organization as the sender. Supported Outlook clients include Outlook desktop, Outlook Mac, Outlook mobile on iOS and Android, and Outlook on the web (formerly known as Outlook Web App).

Recipients of encrypted messages who receive encrypted or rights-protected mail sent to their Gmail and Yahoo accounts receive a wrapper mail that directs them to the encrypted message portal where they can easily authenticate using a Microsoft account, Gmail, or Yahoo credentials.

End users that read encrypted or rights-protected mail on clients other than Outlook also use the encrypted message portal to view encrypted and rights-protected messages that they receive.

If the sender of the protected mail is in GCC High and the recipient is outside of GCC High, including commercial users, Outlook.com users, and users of other email providers such as Gmail, the recipient receives a wrapper mail. The wrapper mail directs the recipient to the encrypted message portal where the recipient is able to read and reply to the message. Otherwise, if the sender and recipient are both in the GCC High environment, even if they're not in the same organization, then recipients that use Outlook clients to read mail receive native, first-class reading experiences for encrypted and rights-protected mail. For more information about the different experience in GCC High, see [Compare versions of OME](ome-version-comparison).

For more information about size limits for messages and attachments that you can encrypt using OME, see [Exchange Online Limits](/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits).

## How Microsoft Purview Advanced Message Encryption works on top of Microsoft Purview Message Encryption

Microsoft Purview Advanced Message Encryption lets you create multiple branding templates so you can fine-tune control over recipient mail and create custom branding experiences to support a diverse organizational structure.

Advanced Message Encryption in Microsoft 365 helps you meet compliance obligations that require more flexible control over external recipient's access to encrypted emails. With Advanced Message Encryption, as an administrator, you can control sensitive emails shared outside the organization with automatic policies that detect sensitive information types (for example, personal data, Financial or Health IDs) or keywords to enhance protection by expiring access through a secure web portal to encrypted emails. As an admin you can further control encrypted emails accessed through a web portal by revoking access to an email anytime.

Message revocation and expiration only work for emails that your users send to recipients outside your organization. In addition, the recipients must access the email through the web portal. To ensure the recipient uses the portal to receive email, you set up a custom branding template that applies the wrapper. Then, you apply the branding template in a mail flow rule. For more information about Advanced Message Encryption, see [Advanced Message Encryption](ome-advanced-message-encryption).

## Defining rules for Microsoft Purview Message Encryption

One way to enable Microsoft Purview Message Encryption is for Exchange Online administrators to define mail flow rules. These rules determine under what conditions email messages should be encrypted. When an encryption action is set for a rule, any messages that match the rule conditions are encrypted before they're sent.

Mail flow rules are flexible, letting you combine conditions so you can meet specific security requirements in a single rule. For example, you can create a rule to encrypt all messages that contain specified keywords and are addressed to external recipients. Microsoft Purview Message Encryption also encrypts replies from recipients of encrypted email.

For more information about how to create mail flow rules to take advantage of Microsoft Purview Message Encryption, see [Define mail flow rules to encrypt email messages](define-mail-flow-rules-to-encrypt-email).

## Get started with the Microsoft Purview Message Encryption

If you're ready to get started using Microsoft Purview Message Encryption within your organization, see [Set up Microsoft Purview Message Encryption](set-up-new-message-encryption-capabilities).

## Sending, viewing, and replying to encrypted email messages

With Microsoft Purview Message Encryption, users can send encrypted email from Outlook and Outlook on the web. Additionally, admins can set up mail flow rules in Microsoft 365 to automatically encrypt emails based on keyword matching or other conditions.

Recipients of encrypted messages who are in organizations will be able to read those messages seamlessly in any version Outlook, including Outlook for PC, Outlook for Mac, Outlook on the web, Outlook for iOS, and Outlook for Android. Users that receive encrypted messages on other email clients can view the messages in the encrypted message portal.

For detailed guidance about how to send and view encrypted messages, take a look at these articles.

| Read this article... | If you are... |
| --- | --- |
| [Learn about protected messages in Microsoft 365](https://support.microsoft.com/office/2baf3ac7-12db-40a4-8af7-1852204b4b67) | An end user that wants to learn more about how encrypted messages work and what options are available to you. |
| [How do I open a protected message?](https://support.microsoft.com/office/1157a286-8ecc-4b1e-ac43-2a608fbf3098) | An end user that wants to read a protected message that was sent to you. This article includes information about reading messages in several versions of Outlook and from different email accounts, including those accounts outside of Microsoft 365 such as gmail and Yahoo! accounts. |
| [Send, view, and reply to encrypted messages in Outlook](https://support.microsoft.com/office/eaa43495-9bbb-4fca-922a-df90dee51980) | An end user that wants to send, view, or reply to an encrypted message from Outlook. Even if you're not a member of an organization, you still receive notification of encrypted messages sent to you in Outlook. Use this article for instructions on how to view and reply to encrypted messages sent from Office 365. |
| [Send a digitally signed or encrypted message for Mac](https://support.microsoft.com/office/a18ecf7f-a7ac-4edd-b02e-687b05eff547) | An end user that wants to send, view, or reply to encrypted messages using Outlook for Mac. This article also covers using encryption methods other than OME, such as S/MIME. |
| [View encrypted messages on your Android device](https://support.microsoft.com/article/83d60f17-2305-407a-a762-7d518401fdeb) | An end user who has received a message encrypted with Office 365 Message Encryption on your Android device, you can use the free OME Viewer app to view the message and send an encrypted reply. This article explains how. |
| [View encrypted messages on your iPhone or iPad](https://support.microsoft.com/office/4d631321-0d26-4bcc-a483-d294dd0b1caf) | An end user who has received a message encrypted with Office 365 Message Encryption on your iPhone or iPad, you can use the free OME Viewer app to view the message and send an encrypted reply. This article explains how. |