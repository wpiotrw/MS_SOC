---
layout: Conceptual
title: How the Azure Rights Management service works—technical details | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/rights-management-how-does-it-work
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Breaking down how the Azure Rights Management encryption service works—the cryptographic controls that it uses, and step-by-step diagrams of how this process works.
ms.custom: sfi-image-nochange, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: f9c71e8b-17ad-82ed-ef6a-ff78d65ebecc
document_version_independent_id: f9c71e8b-17ad-82ed-ef6a-ff78d65ebecc
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/rights-management-how-does-it-work.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: rights-management-how-does-it-work
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/rights-management-how-does-it-work.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 83b27e6f-7394-a683-a49b-34cc651f0e42
---

# How the Azure Rights Management service works—technical details | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following information if you want to understand, in-depth, how [the Azure Rights Management service](azure-rights-management-learn-about) works. You don't need to know this level of information to configure or apply the encryption settings to protect your data.

Note

When the Azure Rights Management service was available as a standalone product rather than part of Microsoft Purview Information Protection, it was often abbreviated to *Azure RMS*. You see this abbreviation in the pictures in this article.

An important concept to understand about the Azure Rights Management service is that this service doesn't see or store your data as part of the encryption process. Information that you encrypt is never sent to or stored in Azure, unless you explicitly store it in Azure or use another cloud service that stores it in Azure. The Azure Rights Management service simply makes the data in an item unreadable to anyone other than authorized users and services:

- The data is encrypted at the application level and includes a policy that defines the authorized use for that item.
- When an encrypted item is used by a legitimate user or it's processed by an authorized service, the data in the item is decrypted and the rights that are defined in the policy are enforced.

At a high level, you can see how this process works in the following picture. A document containing the secret formula is encrypted, and then successfully opened by an authorized user or service. The document is encrypted by a content key (the green key in this picture). The content key is unique for each document and is placed in the file header where it's encrypted by your Azure Rights Management tenant root key (the red key in this picture). Your tenant key can be generated and managed by Microsoft, or you can generate and manage your own tenant key.

Throughout the encrypted process when the Azure Rights Management service is encrypting and decrypting, authorizing, and enforcing restrictions, the secret formula is never sent to Azure.

![How the Azure Rights Management service encrypts a file](media/rights-management-secret-formula.png)

For a detailed description of what’s happening, see the Walkthrough of how the service works: First use, content encryption, content consumption section in this article.

For details about the algorithms and key lengths that the service uses, see Cryptographic controls: Algorithms and key lengths.

## Cryptographic controls: Algorithms and key lengths

Even if you don't need to know in detail how this technology works, you might be asked about the cryptographic controls that it uses. For example, to confirm that the encryption is industry-standard.

| Cryptographic controls | Use in the Azure Rights Management service |
| --- | --- |
| Algorithm: AESKey length: 128 bits and 256 bits [1] | Content encryption |
| Algorithm: RSAKey length: 2048 bits [2] | Key encryption |
| SHA-256 | Certificate signing |

**Footnote 1:** 256 bits is used by the [Microsoft Purview Information Protection client](information-protection-client) in the following scenarios:

- Generic encryption (.pfile).
- Native encryption for PDF documents when the document has been encrypted with the ISO standard for PDF encryption, or the resulting encrypted document has a .ppdf file name extension.
- Native encryption for text or image files (such as .ptxt or .pjpg).

**Footnote 2:** 2048 bits is the key length when the Azure Rights Management service is activated. 1024 bits is supported for the following optional scenarios:

- During a migration from on-premises if the Active Directory Rights Management Services (AD RMS) cluster is running in Cryptographic Mode 1.
- For archived keys that were created on-premises before the migration, so that content that was previously encrypted by AD RMS can continue to be opened by the Azure Rights Management service post migration.

### How the cryptographic keys are stored and secured

For each document or email that is protected by the Azure Rights Management service, the service creates a single AES key (the "content key"), and that key is embedded to the document, and persists through editions of the document.

The content key is encrypted with the organization’s RSA key (the "Azure Rights Management tenant key") as part of the policy in the document, and the policy is also signed by the author of the document. This tenant key is common to all documents and emails that are protected by the Azure Rights Management service for the organization and the tenant key can only be changed by an administrator for the service if the organization is using a tenant key that is customer-managed (known as "bring your own key", or BYOK).

This tenant key is protected in Microsoft’s online services, in a highly controlled environment and under close monitoring. When you use a customer-managed tenant key (BYOK), this security is enhanced by the use of an array of high-end hardware security modules (HSMs) in each Azure region, without the ability for the keys to be extracted, exported, or shared under any circumstances. For more information about the tenant key and BYOK, see [Managing the root key for your Azure Rights Management service](rights-management-tenant-key).

Licenses and certificates that are sent to a Windows device are encrypted with the client's device private key. This private key is created the first time a user on the device uses the Azure Rights Management service. This private key, in turn, is encrypted with DPAPI on the client, which protects these secrets by using a key derived from the user’s password. On mobile devices, the keys are used only one time, so because they aren't stored on the clients, these keys don’t need to be encrypted on the device.

## Walkthrough of how the service works: First use, content encryption, content consumption

To understand in more detail how the Azure Rights Management service works, let's walk through a typical flow after [the Azure Rights Management service is activated](activate-rights-management-service) and when a user first uses the Rights Management service from their Windows computer (a process sometimes known as **initializing the user environment** or bootstrapping), **encrypts content** (a document or email), and then **consumes** (opens and uses) content that has been encrypted by somebody else.

After the user environment is initialized, that user can then encrypt documents or consume encrypted documents on that computer.

Note

If this user moves to another Windows computer, or another user uses this same Windows computer, the initialization process is repeated.

### Initializing the user environment

Before a user can encrypt content or consume encrypted content on a Windows computer, the user environment must be prepared on the device. This is a one-time process and happens automatically without user intervention when a user tries to encrypt or consume encrypted content:

![Client activation flow for the Azure Rights Management service - step 1, authenticating the client](media/rights-management-authenticate-user.png)

**What's happening in step 1**: The client for the Azure Rights Management service that runs on the computer first connects to the service, and the service authenticates the user by using their Microsoft Entra account.

When the user’s account is federated with Microsoft Entra ID, this authentication is automatic and the user isn't prompted for credentials.

![Client activation for the Azure Rights Management service - step 2, certificates are downloaded to the client](media/rights-management-certificates-downloaded.png)

**What's happening in step 2**: After the user is authenticated, the connection is automatically redirected to the organization’s tenant, which issues certificates that let the user authenticate to the Azure Rights Management service in order to consume encrypted content and to encrypt content offline.

One of these certificates is the rights account certificate. This certificate, often abbreviated as RAC, authenticates the user to Microsoft Entra ID and is valid for 31 days. The certificate is automatically renewed by the client, providing the user account is still in Microsoft Entra ID and the account is enabled. This certificate isn't configurable by an administrator.

A copy of this certificate is stored in Azure so that if the user moves to another device, the certificates are created by using the same keys.

### Content encryption

When a user encrypts a document, the client for the Azure Rights Management service takes the following actions on an unencrypted document:

![Document encryption by the Azure Rights Management service - step 1, document is encrypted](media/rights-management-document-encrypted.png)

**What's happening in step 1**: The client creates a random key (the content key) and encrypts the document using this key with the AES symmetric encryption algorithm.

![Document encryption by the Azure Rights Management service - step 2, policy is created](media/rights-management-policy-created.png)

**What's happening in step 2**: The client then creates a certificate that includes a policy for the document that includes the [usage rights](/en-us/purview/rights-management-usage-rights) for users or groups, and other restrictions, such as an expiration date. These settings can be defined with sensitivity label encryption settings that an administrator previously configured, or specified at the time the content is encrypted (sometimes referred to as "user-defined permissions" or an "ad hoc policy").

The main Microsoft Entra attribute used to identify the selected users and groups is the Microsoft Entra **ProxyAddresses** attribute, which stores all the email addresses for a user or group. However, if a user account doesn't have any values in the AD ProxyAddresses attribute, the user's **UserPrincipalName** value is used instead.

The client then uses the organization’s key that was obtained when the user environment was initialized and uses this key to encrypt the policy and the symmetric content key. The client also signs the policy with the user’s certificate that was obtained when the user environment was initialized.

![Document encryption by the Azure Rights Management service - step 3, policy is embedded in the document](media/rights-management-policy-embedded.png)

**What's happening in step 3**: Finally, the client embeds the policy into a file with the body of the document encrypted previously, which together comprise an encrypted document.

This document can be stored anywhere or shared by using any method, and the policy always stays with the encrypted document.

### Content consumption

When a user wants to consume an encrypted document, the client starts by requesting access to the Azure Rights Management service:

![Consumption by the Azure Rights Management service - step 1, user is authenticated and gets the list of rights](media/rights-management-authenticated-rights.png)

**What's happening in step 1**: The authenticated user sends the document policy and the user’s certificates to the Azure Rights Management service. The service decrypts and evaluates the policy, and builds a list of rights (if any) the user has for the document. To identify the user, the Microsoft Entra ProxyAddresses attribute is used for the user's account and groups to which the user is a member. For performance reasons, group membership is [cached](rights-management-users-groups#group-membership-caching). If the user account hasn't any values for the Microsoft Entra ProxyAddresses attribute, the value in the Microsoft Entra UserPrincipalName is used instead.

![Document consumption with the Azure Rights Management service - step 2, use license is returned to the client](media/rights-management-use-license.png)

**What's happening in step 2**: The service then extracts the AES content key from the decrypted policy. This key is then encrypted with the user’s public RSA key that was obtained with the request.

The re-encrypted content key is then embedded into an encrypted use license with the list of user rights, which is then returned to the client.

![Document consumption with the Azure Rights Management service - step 3, document is decrypted and rights are enforced](media/rights-management-decrypted-enforced.png)

**What's happening in step 3**: Finally, the client takes the encrypted use license and decrypts it with its own user private key. This lets the client decrypt the document’s body as it is needed and render it on the screen.

The client also decrypts the rights list and passes them to the application, which enforces those rights in the application’s user interface.

Note

When users who are external to your organization consume content that you have encrypted, the consumption flow is the same. What changes for this scenario, is how the user is authenticated. For more information, see [When I share an encrypted document with somebody outside my company, how does that user get authenticated?](azure-rights-management-learn-about#when-i-share-an-encrypted-document-with-somebody-outside-my-company-how-does-that-user-get-authenticated)

### Variations

The preceding walkthroughs cover the standard scenarios but there are some variations:

- **Email encryption**: When Exchange Online and Microsoft Purview Message Encryption is used to encrypt email messages, authentication for consumption can also use federation with a social identity provider or by using a one-time passcode. Then, the process flows are very similar, except that content consumption happens service-side in a web browser session over a temporarily cached copy of the outbound email.
- **Mobile devices**: When mobile devices encrypt or consume files with the Azure Rights Management service, the process flows are simpler. Mobile devices don’t first go through the user initialization process because instead, each transaction (to encrypt or consume content) is independent. As with Windows computers, mobile devices connect to the Azure Rights Management service and authenticate. To encrypt content, mobile devices submit a policy and the Azure Rights Management service sends them a publishing license and symmetric key to encrypt the document. To consume encrypted content, when mobile devices connect to the Azure Rights Management service and authenticate, they send the document policy to the Azure Rights Management service and request a use license to consume the document. In response, the Azure Rights Management service sends the necessary keys and restrictions to the mobile devices. Both processes use TLS to protect the key exchange and other communications.
- **Rights Management connector**: When the Azure Rights Management service is used with the Rights Management connector, the process flows remain the same. The only difference is that the connector acts as a relay between the on-premises services (such as Exchange Server and SharePoint Server) and the Azure Rights Management service. The connector itself doesn't perform any operations, such as the initialization of the user environment, or encryption or decryption. It simply relays the communication that would usually go to an AD RMS server, handling the translation between the protocols that are used on each side. This scenario lets you use the Azure Rights Management service with on-premises services.
- **Generic encryption (.pfile)**: When the Azure Rights Management service generically encrypts a file, the flow is basically the same for content encryption except that the client creates a policy that grants all rights. When the file is consumed, it's decrypted before it's passed to the target application. This scenario lets you encrypt all files, even if they don’t natively support the Azure Rights Management service.
- **Microsoft accounts**: The Azure Rights Management service can authorize email addresses for consumption when they're authenticated with a Microsoft account. However, not all applications can open encrypted content when a Microsoft account is used for authentication. [Supported scenarios for opening protected documents](/en-us/previous-versions/azure/information-protection/secure-collaboration-documents#supported-scenarios-for-opening-protected-documents).