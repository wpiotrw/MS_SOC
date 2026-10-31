---
layout: Conceptual
title: Decryption in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-decryption
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how eDiscovery handles encrypted documents attached to email messages and stored in SharePoint and OneDrive.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-28T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 6b32571f-7e8f-5b74-fed6-e88b4558eaae
document_version_independent_id: 6b32571f-7e8f-5b74-fed6-e88b4558eaae
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-decryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-decryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-decryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 62cd2fea-0d99-8b11-4dc9-ec9420c5204a
---

# Decryption in eDiscovery | Microsoft Learn

Encryption is an important part of your file protection and information protection strategy. Organizations of all types use encryption technology to protect sensitive content within their organization and ensure that only the right people have access to that content.

To run common eDiscovery tasks on encrypted content, eDiscovery managers need to decrypt email message content when they [export](edisc-search-export) it from eDiscovery cases. Content encrypted with Microsoft encryption technologies isn't available for review until after export.

To make it easier to manage encrypted content in the eDiscovery workflow, eDiscovery tools now incorporate the decryption of encrypted files attached to email messages and sent in Exchange Online.^1^ Additionally, encrypted documents stored in SharePoint and OneDrive are decrypted when premium eDiscovery features are enabled.^2^

Before this capability, only the content of an email message protected by rights management (and not attached files) was decrypted. Encrypted documents in SharePoint and OneDrive couldn't be decrypted during the eDiscovery workflow. Now, files that are encrypted with a Microsoft encryption technology and located on a SharePoint or OneDrive account are searchable and decrypted when the search results are prepared for preview, [added to a review set](edisc-search-add-to-review-set), and exported. Additionally, encrypted documents in SharePoint and OneDrive that are attached to an email message (as a copy) are searchable. This decryption capability allows eDiscovery managers to view the content of encrypted email attachments and site documents when previewing search results, and [review them](edisc-review-set-view) after they're added to a review set when premium eDiscovery features are enabled.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Requirements for decryption in eDiscovery

- **Permissions**: You need to be assigned the *RMS Decrypt* role to preview, review, and export files encrypted with Microsoft encryption technologies. You also need this role to review and query encrypted files that are added to a review set in eDiscovery. The Microsoft Purview portal assigns this role by default to the eDiscovery Manager role group. For more information about the RMS Decrypt role, see [Assign eDiscovery permissions](edisc-permissions#rms-decrypt).
- **Run the Inbox Repair tool on exported PST files**: After you export PST files, run the Inbox Repair tool (ScanPST.exe) to diagnose and repair any errors in the PST files.

## Supported encryption technologies

For Exchange, eDiscovery tools support items encrypted with Microsoft encryption technologies. These technologies are Azure Rights Management (Azure RMS)^1^ and Microsoft Purview Information Protection (specifically sensitivity labels). For more information about Microsoft encryption technologies, see [Encryption](encryption) and the various [email encryption](email-encryption#comparing-email-encryption-options-available-in-office-365) options available. Content encrypted by S/MIME or third-party encryption technologies isn't supported. For example, previewing or exporting content encrypted with non-Microsoft technologies isn't supported.

Note

Microsoft eDiscovery tools don't support the decryption of email messages sent with a [Microsoft Purview Message Encryption custom branding template](add-your-organization-brand-to-encrypted-messages). When you use an OME custom branding template, email messages are delivered to the encrypted message portal instead of the recipient's mailbox. Therefore, you can't use eDiscovery tools to search for encrypted messages because those messages are never received by the recipient's mailbox.

For SharePoint, content labeled with *SharePoint online service* is decrypted. Items labeled or encrypted in the client before uploading to SharePoint, legacy document library RMS templates or settings, and S/MIME or other standards aren't supported.^2^.

## eDiscovery activities that support encrypted items

The following table identifies the supported tasks that you can perform in eDiscovery tools on encrypted files attached to email messages and encrypted documents in SharePoint and OneDrive. You can perform these supported tasks on encrypted files that match the criteria of a search. A value of `N/A` indicates the functionality isn't available in eDiscovery.

| eDiscovery task | eDiscovery | Premium features enabled |
| --- | --- | --- |
| Search for content in encrypted files in sites and email attachments^1^ | No | Yes |
| Preview encrypted files attached to email | No | Yes^2^ |
| Preview encrypted documents in SharePoint and OneDrive | No | Yes |
| Review encrypted files in a review set | N/A | Yes |
| Export encrypted files attached to email | Yes | Yes |
| Export encrypted documents in SharePoint and OneDrive | No | Yes |
|  |  |  |

## Supported decryption

The following table describes the decryption that eDiscovery supports for email, email with attachments, and files hosted by SharePoint.

| Item type | Task | eDiscovery | Premium features enabled |
| --- | --- | --- | --- |
| Encrypted email | Search | Yes | Yes |
| Encrypted email | Decryption to .pst | No | Yes |
| Encrypted email | Decryption to file | No | Yes |
| Encrypted mail and attachment | Search | No | Yes (with Advanced indexing)^3^ |
| Encrypted mail and attachment | Decryption to .pst | No | Yes |
| Encrypted mail and attachment | Decryption to file | No | Yes |
| File in SharePoint with MIP label | Search | No | Yes |
| File in SharePoint with MIP label | Decryption | No | Yes |
| File in SharePoint with other encryption^4^ | Search, Decryption | No | No |

Important

eDiscovery doesn't support legacy encryption protocols.

## Decryption limitations with email and attachments

Important

Decryption and searchability are distinct. Email attachments encrypted with sensitivity labels are decrypted during preview and export, but the content in those attachments isn't indexed for search. Keyword searches don't match content inside these attachments. To ensure these attachments are captured, include partially indexed items in your collection and use review sets to analyze decrypted content. For more information, see [Partially indexed items](edisc-ref-partially-indexed-items).

eDiscovery support for decryption of email messages and attachments is subject to the following limitations:

- Decryption isn't supported when the email or attachment encryption is applied in an external organization. eDiscovery only supports decryption for email and attachments that your organization encrypts.
- When decrypting emails or attachments, the owner of the mailbox must have access to view the encrypted content. Decryption isn't supported if the owner sends or forwards the emails or attachments to other recipients who can't view the encrypted content. Changes in the owner's groups or other organization permissions might also affect decryption support.
- PDFs generated from MIP-labeled Word documents (for example, a .docx file encrypted with a sensitivity label and then saved as .pdf) can only be decrypted when [PDF encryption is enabled](/en-us/powershell/module/exchangepowershell/set-irmconfiguration?view=exchange-ps#-enablepdfencryption). PDF encryption and decryption control of the tenant is configured by running the following cmdlet:

    `Set-IRMConfiguration -EnablePdfEncryption $true`

If you don't set the configuration to *True*, eDiscovery doesn't decrypt the PDF generated from MIP labeled document.

## Decryption limitations with sensitivity labels in SharePoint and OneDrive

eDiscovery doesn't support encrypted files in SharePoint and OneDrive when a sensitivity label that applies encryption is configured with the following setting:

- User access to the document has an expiration setting that is set to a value other than **Never**.

For more information about these settings, see the "Configure encryption settings" section in [Restrict access to content by using sensitivity labels to apply encryption](encryption-sensitivity-labels#configure-encryption-settings).

An eDiscovery search might return documents encrypted with the previous settings. This result might happen when a document property (such as the title, author, or modified date) matches the search criteria. Although these documents might be included in search results, you can't preview or review them. These documents remain encrypted when they're exported with premium eDiscovery features enabled.

Files in SharePoint with sensitivity labels configured for user-defined permissions are supported for eDiscovery decryption. For more information, see [Learn more about support for labels configured for user-defined permissions.](sensitivity-labels-sharepoint-onedrive-files#support-for-labels-configured-for-user-defined-permissions)

Important

Decryption is supported for files that are locally encrypted and then uploaded to SharePoint or OneDrive as long as the user is signed in to a Microsoft 365 client when encrypting the file. For example, local files that are encrypted by the Microsoft Purview Information Protection client and then uploaded to Microsoft 365. If the encryption applied locally isn't by a user signed in to the Microsoft 365 client, the file isn't supported for decryption.

## Decryption scope for nested and container files

eDiscovery decryption applies to root-level items only, such as files stored directly in SharePoint or OneDrive, direct email attachments, and the email messages themselves. If an encrypted file is nested inside a container format, eDiscovery doesn't recursively decrypt it.

For example:

- A MIP-labeled encrypted .pptx file stored directly in a SharePoint document library is decrypted as expected.
- The same MIP-labeled encrypted .pptx file inside a .zip archive stored in SharePoint isn't decrypted. The .zip archive is collected and processed, but encrypted files within the archive aren't decrypted.
- An encrypted attachment on an email message is decrypted. However, if that email message is attached as a nested .msg file inside another email, encrypted attachments within the nested .msg file aren't decrypted.

This behavior applies to all container formats, including .zip archives and .msg files that contain encrypted items as nested content. Sensitivity label metadata for nested items might also not be available because label information is read from source-level properties of the root item.

## Decrypting RMS-protected email messages and encrypted file attachments by using premium eDiscovery features

When you export rights-protected (RMS-protected) email messages that are included in the results of a search, the export process decrypts these messages. Members of the eDiscovery Manager role group have this decryption capability by default because the RMS Decrypt management role is assigned to this role group by default.

Keep the following things in mind when exporting encrypted email messages and attachments:

- To enable decryption of RMS-protected messages when you export them, you must export the search results as individual messages.
- Attachments encrypted separately from an email can be decrypted if the attachments are Microsoft 365 documents. For example, if a user encrypts a Word document and then attaches it to an email message that isn't encrypted, this attachment is decrypted.
- Attachments encrypted as part of the encryption of the associated email message are decrypted. For example, if a user creates an email message, attaches an unencrypted Word document, and then encrypts the message (including the attachment), this attachment is decrypted.
- The **ResultsLog** report identifies messages that are decrypted. This report contains a column named **Decode Status**, and a value of **Decoded** identifies the messages that are decrypted.
- In addition to decrypting file attachments when exporting search results, you can also preview the decrypted file when previewing search results. You can only view the rights-protected email message after you export it.
- To prevent someone from decrypting RMS-protected messages and encrypted file attachments, create a custom role group by copying the built-in eDiscovery Manager role group, then remove the RMS Decrypt management role from the custom role group. Add the person you don't want to decrypt messages as a member of the custom role group.

## Notes

^1^ When you enable premium eDiscovery features, you can only transparently decrypt content encrypted with RMS keys hosted in Microsoft 365. Double Key Encryption (DKE), Hold Your Own Key (HYOK), on-premises RMS, and similar options aren't supported. For more information, see [Key types for the service](rights-management-tenant-key#key-types-for-the-service).

^2^ Email attachment decryption is supported only for Microsoft 365 documents (Microsoft Word, Excel, PowerPoint, etc.) and PDF files if [PDF decryption is enabled](/en-us/powershell/module/exchangepowershell/set-irmconfiguration?view=exchange-ps#-enablepdfencryption). Encrypted email messages attached as attachments aren't supported.

^3^ eDiscovery can decrypt and index encrypted files located on a local computer that a user copies to an email message as long as the encryption was applied when the user was signed in to a Microsoft 365 client. When you enable premium eDiscovery features, you need to advanced index encrypted email and attachments in recipient mailbox to decrypt them.

^4^ You can only decrypt items labeled in SharePoint or uploaded to SharePoint after integration with sensitivity labels are enabled. These items must have labels with admin-defined permissions and have no expiration. You can't decrypt all other encrypted files in SharePoint. For more information, see [Enable sensitivity labels for files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).

You can't decrypt other documents, including:

- Files encrypted in the client and uploaded before sensitivity labels were integrated with SharePoint.
- Documents encrypted with legacy RMS templates and not labeled.
- Documents with user-defined permissions or with expiration settings (SMIME or other standards).