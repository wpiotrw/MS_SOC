---
layout: Conceptual
title: How Exchange Online uses TLS to secure email connections | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/exchange-online-uses-tls-to-secure-email-connections
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-11-24T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-encryption
search.appverid:
- MET150
- MOE150
ms.assetid: 4cde0cda-3430-4dc0-b489-f2c0736c929f
ms.collection:
- purview-compliance
description: Learn how Exchange Online and Microsoft 365 use Transport Layer Security (TLS) and Forward Secrecy (FS) to secure email communications.
locale: en-us
document_id: fa5d23b6-1110-83af-b2e4-b86dc6483ebf
document_version_independent_id: fa5d23b6-1110-83af-b2e4-b86dc6483ebf
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/exchange-online-uses-tls-to-secure-email-connections.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: exchange-online-uses-tls-to-secure-email-connections
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/exchange-online-uses-tls-to-secure-email-connections.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 7350ae17-2533-78f1-fadd-3859c4156c0a
---

# How Exchange Online uses TLS to secure email connections | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Learn how Exchange Online and Microsoft 365 use Transport Layer Security (TLS) and Forward Secrecy (FS) to secure email communications.

## TLS basics for Microsoft 365 and Exchange Online

Transport Layer Security (TLS), and Secure Sockets Layer (SSL) that came before TLS, are cryptographic protocols. These protocols secure communication over a network by using security certificates to encrypt a connection between computers. TLS supersedes SSL and is often referred to as SSL 3.1. Exchange Online uses TLS to encrypt the connections between Exchange servers and the connections between Exchange servers and other servers. For example, TLS is used to encrypt the connection between Exchange Online and your on-premises Exchange servers or your recipients' mail servers. Once the connection is encrypted, all data sent through that connection is sent through the encrypted channel.

TLS doesn't encrypt the message, just the connection. So, if you forward a message that was sent through a TLS-encrypted connection to a recipient organization that doesn't support TLS encryption, that message isn't necessarily encrypted.

If you want to encrypt the message, use an encryption technology that encrypts the message contents. For example, you can use Microsoft Purview Message Encryption or S/MIME. See [Email encryption in Office 365](email-encryption) and [Message encryption](ome) for information on message encryption in Office 365.

Use TLS in situations where you want to set up a secure channel of correspondence between Microsoft and your on-premises organization or another organization, such as a partner. Exchange Online always attempts to use TLS first to secure your email but can't if the other party doesn't offer TLS security. Keep reading to find out how you can secure all mail to your on-premises servers or important partners by using *connectors*.

To provide the best-in-class encryption to our customers, Microsoft deprecated Transport Layer Security (TLS) versions 1.0 and 1.1 in [Office 365](tls-1.0-and-1.1-deprecation-for-office-365) and [Office 365 GCC](tls-1-2-in-office-365-gcc). However, you can continue to use an unencrypted SMTP connection without any TLS. We don't recommend email transmission without any encryption.

## How Exchange Online uses TLS between Exchange Online customers

Exchange Online servers always encrypt connections to other Exchange Online servers in our data centers with TLS 1.2. When you send a message to a recipient that is within your organization, Exchange Online automatically sends the message over an encrypted connection using TLS. Exchange Online also sends email that you send to other customers over encrypted connections using TLS that are secured using Forward Secrecy.

## How Microsoft 365 uses TLS between Microsoft 365 and external, trusted partners

By default, Exchange Online always uses *opportunistic TLS*. Opportunistic TLS means Exchange Online always tries to encrypt connections with the most secure version of TLS first, then works its way down the list of TLS ciphers until it finds one on which both parties can agree. Unless you configure Exchange Online to ensure that messages to that recipient must use a secure connection, then by default Exchange sends the message without encryption if the recipient's organization doesn't support TLS encryption. Opportunistic TLS is sufficient for most businesses. However, for businesses that have compliance requirements such as medical, banking, or government organizations, you can configure Exchange Online to require, or force, TLS. For instructions, see [Configure mail flow using connectors in Office 365](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow).

If you decide to configure TLS between your organization and a trusted partner organization, Exchange Online can use *forced TLS* to create trusted channels of communication. Forced TLS requires your partner organization to authenticate to Exchange Online with a security certificate to send mail to you. Your partner needs to manage their own certificates. Exchange Online uses connectors to protect messages that you send from unauthorized access before they arrive at the recipient's email provider. For information on using connectors to configure mail flow, see [Configure mail flow using connectors in Office 365](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow).

## TLS and hybrid Exchange Server deployments

If you're managing a hybrid Exchange deployment, your on-premises Exchange server needs to authenticate to Microsoft 365 using a security certificate to send mail to recipients whose mailboxes are only in Office 365. As a result, you need to manage your own security certificates for your on-premises Exchange servers. You must also securely store and maintain these server certificates. For more information about managing certificates in hybrid deployments, see [Certificate requirements for hybrid deployments](/en-us/exchange/certificate-requirements).

Note

Certificates to relay emails to Exchange Online don't need an EKU for client authentication.

## How to set up forced TLS for Exchange Online in Office 365

For Exchange Online customers, in order for forced TLS to work to secure all of your sent and received email, you need to set up more than one connector that requires TLS. You need one connector for messages sent to user mailboxes and another connector for messages sent from user mailboxes. Create these connectors in the Exchange admin center in Office 365. For instructions, see [Configure mail flow using connectors in Office 365](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow).

## TLS certificate information for Exchange Online

The certificate information used by Exchange Online is described in the following table. If your business partner is setting up forced TLS on their email server, you need to provide this information to them. For security reasons, our certificates do change from time to time. The current certificate is valid from September 24, 2020.

### Current certificate information valid from September 24, 2020

| Attribute | Value |
| --- | --- |
| Certificate authority root issuer | DigiCert CA - 1 |
| Certificate name | mail.protection.outlook.com |
| Organization | Microsoft Corporation |
| Organization unit | www.digicert.com |
| Certificate key strength | 2048 |

## Get more information about TLS, certificates, and Microsoft 365 and download certificates

[Microsoft 365 encryption chains and certificate downloads](encryption-office-365-certificate-chains)

[Microsoft 365 encryption chains and certificate downloads - DOD and GCC High](encryption-office-365-certificate-chains-itar)

For a list of supported cipher suites, see [Technical reference details about encryption](technical-reference-details-about-encryption).

[Set up connectors for secure mail flow with a partner organization](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-for-secure-mail-flow-with-a-partner)

[Connectors with enhanced email security](/en-us/previous-versions/exchange-server/exchange-150/dn942516%28v=exchg.150%29)

[Encryption in Microsoft 365](encryption)