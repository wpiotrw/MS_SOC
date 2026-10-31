---
layout: FAQ
title: Double Key Encryption FAQ | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/double-key-encryption-faq
summary: >
  <p>&quot;Have questions about how Double Key Encryption works that we didn't cover elsewhere? Check for an answer here.&quot;</p>
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article contains frequently asked questions and answers about Microsoft Purview Double Key Encryption.
author: kreagle
ms.author: k-reagle
manager: laurawi
ms.date: 2025-01-10T00:00:00.0000000Z
audience: Admin
ms.topic: faq
ms.service: purview
ms.subservice: purview-encryption
ms.reviewer: laurawi
ms.collection:
- purview-compliance
locale: en-us
document_id: f0442f4b-8ffe-22c6-51a2-980d6bce0e54
document_version_independent_id: f0442f4b-8ffe-22c6-51a2-980d6bce0e54
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/double-key-encryption-faq.yml
site_name: Docs
depot_name: MSDN.Purview
page_type: faq
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: double-key-encryption-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/double-key-encryption-faq.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19e6356c-ba1e-4d22-9557-6222c183f04d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e93f3d5f-c77d-4365-a7fb-c9f2234416c7
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/01e6eca5-e701-4cd9-a21f-56c9258f473e
- https://authoring-docs-microsoft.poolparty.biz/devrel/62e8d07a-cc62-4934-b30b-e168a571e51d
platformId: f0d65c2c-ea1a-5047-5886-3164b413ef74
---

# Double Key Encryption FAQ | Microsoft Learn

"Have questions about how Double Key Encryption works that we didn't cover elsewhere? Check for an answer here."

## What Microsoft 365 Apps can I use with DKE?

You can use DKE labels to protect documents using the desktop versions of Word, Excel, PowerPoint, and Outlook on Windows. To ensure that you're using a supported version of Office apps, see the [capabilities tables](sensitivity-labels-versions) and the row **Double Key Encryption (DKE)**.

## Can I use Double Key Encryption with Microsoft Office built-in sensitivity labeling?

Yes! Use can use built-in sensitivity labeling with Office apps. For information, see the [capabilities tables](sensitivity-labels-versions) and the row **Double Key Encryption (DKE)**. While you can use the information protection client to protect documents with Double Key Encryption for now, this method will be deprecated in the future.

## How is Double Key Encryption different from the existing hold your own key (HYOK) solution?

Double Key Encryption encrypts your data with two keys. Your encryption key is in your control and the second key is stored in Microsoft Azure, allowing you to move your encrypted data to the cloud. HYOK protects your content with only one key and the key is always on premises.

## Can Double Key Encrypted documents be shared externally?

You can share Double Key Encrypted documents with users on a separate tenant as long as those users:

- Have the required permission to access your key in your Double Key Encryption service.
- Have the required permission to access your key in Microsoft Azure.

## What happens to documents that are protected with HYOK?

Deploying Double Key Encryption doesn't affect your existing HYOK setup. However, we recommend that you start using Double Key Encryption in parallel with HYOK.

## Can I run Double Key Encryption in my non-Microsoft air-gapped environment?

DKE doesn't support these environments because the service requires access to Microsoft Azure.

## Where can I store Double Key Encrypted documents?

You can store Double Key Encrypted documents on-premises or in the cloud. In the cloud, you can move encrypted content to SharePoint Online and OneDrive for Business. You can't view the encrypted documents online in Office Web Apps.

## What regions and languages is Double Key Encryption available in? Is Double Key Encryption available worldwide?

DKE labels are localized to the same languages as other sensitivity labels in Microsoft Purview Information Protection. Double Key Encryption is available worldwide.

## Can I convert a non-DKE label to a DKE label?

No. You can’t add DKE to a label after you create it. Instead, you must choose **Use Double Key Encryption** and provide the URL of your Double Key Encryption service when you create the label.

## How do I roll my DKE keys?

For instructions on rolling (also called rotating or rekeying) the key you store in Azure, see [Operations for your tenant key](rights-management-tenant-key#operations-for-your-tenant-key). See [Tenant and key settings](double-key-encryption-setup#tenant-and-key-settings) for information on creating a new key for the DKE service. When you create a key, you set up a name and a GUID. Then, if you rotate a key, you keep the old record with the name and GUID but add a new record with the same name but different GUID. The new key gets set as active so that the public key API starts returning it for new encryption. Both keys are available for decryption so that new content and old content can be decrypted.

## Why can't I access Double Key Encrypted documents?

The right to view DKE-protected content requires users to authenticate to endpoints managed by your organization. If users in your organization can't view DKE-protected content, review the [key access settings](double-key-encryption-setup#key-access-settings) configuration.

## What kind of mutual transport layer security (mTLS) is supported with the DKE service on Office Desktop Apps on Windows?

- Before 2402: No mTLS support.
- After 2402: The apps don’t support sending the client certification. Instead the desktop apps send the request with `WINHTTP_NO_CLIENT_CERT_CONTEXT`. For more information, see [SSL in WinHTTP - Win32 apps](/en-us/windows/win32/winhttp/ssl-in-winhttp#optional-client-ssl-certificates).