---
layout: Conceptual
title: Email encryption in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/email-encryption
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
ms.topic: overview
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MOE150
- MET150
ms.assetid: c0d87cbe-6d65-4c03-88ad-5216ea5564e8
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
description: Compare Microsoft 365 encryption options including Microsoft Purview Message Encryption, S/MIME, Information Rights Management (IRM), and learn about Transport Layer Security (TLS).
locale: en-us
document_id: 72721a30-cac7-6c89-aa47-a3f8145155c8
document_version_independent_id: 72721a30-cac7-6c89-aa47-a3f8145155c8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/email-encryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: email-encryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/email-encryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 91a47e96-8dd1-fbc8-66f6-9755108984cb
---

# Email encryption in Microsoft 365 | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

This article compares encryption options in Microsoft 365 including Microsoft Purview Message Encryption, S/MIME, Information Rights Management (IRM), and introduces Transport Layer Security (TLS).

Microsoft 365 delivers multiple encryption options to help you meet your business needs for email security. This article presents three ways to encrypt email in Office 365. If you want to learn more about all security features in Office 365, visit the [Office 365 Trust Center](https://go.microsoft.com/fwlink/p/?LinkID=282470). This article introduces the three types of encryption available for Microsoft 365 administrators to help secure email in Office 365:

- Microsoft Purview Message Encryption.
- Secure/Multipurpose Internet Mail Extensions (S/MIME).
- Information Rights Management (IRM).

## How Microsoft 365 uses email encryption

Encryption is the process by which information is encoded so that only an authorized recipient can decode and consume the information. Microsoft 365 uses encryption in two ways: in the service, and as a customer control. In the service, encryption is used in Microsoft 365 by default; you don't have to configure anything. For example, Microsoft 365 uses Transport Layer Security (TLS) to encrypt the connection, or session, between two servers.

Here's how email encryption typically works:

- A message is encrypted, or transformed from plain text into unreadable ciphertext, either on the sender's machine, or by a central server while the message is in transit.
- The message remains in ciphertext while it's in transit in order to protect it from being read in case the message is intercepted.
- Once the message is received by the recipient, the message is transformed back into readable plain text in one of two ways:

    - The recipient's machine uses a key to decrypt the message, or
    - A central server decrypts the message on behalf of the recipient, after validating the recipient's identity.

For more information on how Microsoft 365 secures communication between servers, such as between organizations within Microsoft 365 or between Microsoft 365 and a trusted business partner outside of Microsoft 365, see [How Exchange Online uses TLS to secure email connections in Office 365](exchange-online-uses-tls-to-secure-email-connections).

## Comparing email encryption options available in Office 365

| Email encryption technology | - | - | - |
| --- | --- | --- | --- |
| What is it? | Message encryption is a service built on the Azure Rights Management service that lets you send encrypted email to people inside or outside your organization, regardless of the destination email address (Gmail, Yahoo! Mail, Outlook.com, etc.).  As an admin, you can set up transport rules that define the conditions for encryption. When a user sends a message that matches a rule, encryption is applied automatically.  To view encrypted messages, recipients can either get a one-time passcode, sign in with a Microsoft account, or sign in with a work or school account associated with Office 365. Recipients can also send encrypted replies. They don't need a Microsoft 365 subscription to view encrypted messages or send encrypted replies. | IRM is an encryption solution that also applies usage restrictions to email messages. It helps prevent sensitive information from being printed, forwarded, or copied by unauthorized people.  IRM capabilities in Microsoft 365 use the Azure Rights Management service. | S/MIME is a certificate-based encryption solution that allows you to both encrypt and digitally sign a message. The message encryption helps ensure that only the intended recipient can open and read the message. A digital signature helps the recipient validate the identity of the sender.  Both digital signatures and message encryption are made possible through the use of unique digital certificates that contain the keys for verifying digital signatures and encrypting or decrypting messages.  To use S/MIME, you must have public keys on file for each recipient. Recipients have to maintain their own private keys, which must remain secure. If a recipient's private keys are compromised, the recipient needs to get a new private key and redistribute public keys to all potential senders. |
| What does it do? | OME:  Encrypts messages sent to internal or external recipients.  Allows users to send encrypted messages to any email address, including Outlook.com, Yahoo! Mail, and Gmail.  Allows you, as an admin, to customize the email viewing portal to reflect your organization's brand.  Microsoft securely manages and stores the keys, so you don't have to.  No special client side software is needed as long as the encrypted message (sent as an HTML attachment) can be opened in a browser. | IRM:  Uses encryption and usage restrictions to provide online and offline protection for email messages and attachments.  Gives you, as an admin, the ability to set up transport rules or Outlook protection rules to automatically apply IRM to select messages.  Lets users manually apply templates in Outlook or Outlook on the web (formerly known as Outlook Web App). | S/MIME addresses sender authentication with digital signatures, and message confidentiality with encryption. |
| What does it not do? | OME doesn't let you apply usage restrictions to messages. For example, you can't use it to stop a recipient from forwarding or printing an encrypted message. | Some applications may not support IRM emails on all devices. | S/MIME doesn't allow encrypted messages to be scanned for malware, spam, or policies. |
| Recommendations and example scenarios | We recommend using OME when you want to send sensitive business information to people outside your organization, whether they're consumers or other businesses. For example:  A bank employee sending credit card statements to customers  A doctor's office sending medical records to a patient  An attorney sending confidential legal information to another attorney | We recommend using IRM when you want to apply usage restrictions as well as encryption. For example:  A manager sending confidential details to her team about a new product applies the "Do Not Forward" option.  An executive needs to share a bid proposal with another company, which includes an attachment from a partner who is using Office 365, and require both the email and the attachment to be protected. | We recommend using S/MIME when either your organization or the recipient's organization requires true peer-to-peer encryption.  S/MIME is most commonly used in the following scenarios:  Government agencies communicating with other government agencies  A business communicating with a government agency |
|  |  |  |  |

Don't apply multiple email encryption technologies to the same email message. Some email clients, such as Outlook for Mac, Outlook for iOS, and Outlook for Android, aren't able to open messages with multiple email encryption technologies applied.

## What encryption options are available for my Microsoft 365 subscription?

For information about email encryption options for your Microsoft 365 subscription see the [Exchange Online service description](/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-service-description). Here, you can find information about the following encryption features:

- The Azure Rights Management service, including both IRM capabilities and Microsoft Purview Message Encryption
- S/MIME
- TLS
- Encryption of data at rest (through BitLocker, service encryption, and DKM)

You can also use third-party encryption tools with Microsoft 365, for example, PGP (Pretty Good Privacy). Microsoft 365 does not support PGP/MIME and you can only use PGP/Inline to send and receive PGP-encrypted emails.

## What about encryption for data at rest?

"Data at rest" refers to data that isn't actively in transit. In Microsoft 365, email data at rest is encrypted using BitLocker Drive Encryption. BitLocker encrypts the hard drives in Microsoft data centers to provide enhanced protection against unauthorized access. To learn more, see [BitLocker Overview](/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831713%28v=ws.11%29).

## More information about email encryption options

For more information about the email encryption options in this article as well as TLS, see these articles:

### Microsoft Purview Message Encryption

[Message encryption](ome)

### IRM

[Information Rights Management in Exchange Online](information-rights-management-in-exchange-online)

[Learn about the Azure Rights Management encryption service](azure-rights-management-learn-about)

### S/MIME

[S/MIME for message signing and encryption](/en-us/Exchange/policy-and-compliance/smime/smime)

[Understanding S/MIME](/en-us/previous-versions/tn-archive/aa995740%28v=exchg.65%29)

[Understanding Public Key Cryptography](/en-us/previous-versions/tn-archive/aa998077%28v=exchg.65%29)

### TLS

[Configure custom mail flow by using connectors](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow)

[How Exchange Online uses TLS to secure email connections](exchange-online-uses-tls-to-secure-email-connections)

[Disabling TLS 1.0 and 1.1 for Microsoft 365](tls-1.0-and-1.1-deprecation-for-office-365)