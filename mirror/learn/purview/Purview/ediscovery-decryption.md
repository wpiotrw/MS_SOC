---
layout: Conceptual
title: Decryption in Microsoft Purview eDiscovery tools | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-decryption
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about how Microsoft 365 eDiscovery tools handle encrypted documents attached to email messages and stored in SharePoint Online and OneDrive for Business.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
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
ms.custom:
- seo-marvel-apr2020
locale: en-us
document_id: 05f81cbb-97fe-bcb7-0308-0c25c483caf3
document_version_independent_id: 05f81cbb-97fe-bcb7-0308-0c25c483caf3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-decryption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-decryption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-decryption.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 16dcc903-f3b1-8d33-9e5d-d3ca21ba4154
---

# Decryption in Microsoft Purview eDiscovery tools | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Encryption is an important part of your file protection and information protection strategy. Organizations of all types use encryption technology to protect sensitive content within their organization and ensure that only the right people have access to that content.

To run common eDiscovery tasks on encrypted content, eDiscovery managers are required to decrypt email message content when exported from content searches, Microsoft Purview eDiscovery (Standard) cases, and Microsoft Purview eDiscovery (Premium) cases. Content encrypted with Microsoft encryption technologies wasn't available for review until after export.

To make it easier to manage encrypted content in the eDiscovery workflow, Microsoft Purview eDiscovery tools now incorporate the decryption of encrypted files attached to email messages and sent in Exchange Online.^1^ Additionally, encrypted documents stored in SharePoint Online and OneDrive for Business are decrypted in eDiscovery (Premium)^2^.

Prior to this new capability, only the content of an email message protected by rights management (and not attached files) were decrypted. Encrypted documents in SharePoint and OneDrive couldn't be decrypted during the eDiscovery workflow. Now, files that are encrypted with a Microsoft encryption technology is located on a SharePoint or OneDrive account are searchable and decrypted when the search results are prepared for preview, added to a review set in eDiscovery (Premium), and exported. Additionally, encrypted documents in SharePoint and OneDrive that are attached to an email message (as a copy) are searchable. This decryption capability allows eDiscovery managers to view the content of encrypted email attachments and site documents when previewing search results, and review them after they've been added to a review set in eDiscovery (Premium).

## Requirements for decryption in eDiscovery

- **Permissions**: You have to be assigned the *RMS Decrypt* role to preview, review, and export files encrypted with Microsoft encryption technologies. You also have to be assigned this role to review and query encrypted files that are added to a review set in eDiscovery (Premium). This role is assigned by default to the eDiscovery Manager role group on the **Permissions** page in the Microsoft Purview portal. For more information about the RMS Decrypt role, see [Assign eDiscovery permissions](ediscovery-assign-permissions#rms-decrypt-role).
- **Run the Inbox Repair tool on exported PST files**: After you've exported PST files, we recommend that you run the Inbox Repair tool (ScanPST.exe) to diagnose and repair any errors in the PST files.

## Supported encryption technologies

For Exchange, Microsoft Purview eDiscovery tools support items encrypted with Microsoft encryption technologies. These technologies are Azure Rights Management (Azure RMS)^3^ and Microsoft Purview Information Protection (specifically sensitivity labels). For more information about Microsoft encryption technologies, see [Encryption](encryption) and the various [email encryption](email-encryption#comparing-email-encryption-options-available-in-office-365) options available. Content encrypted by S/MIME or third-party encryption technologies isn't supported. For example, previewing or exporting content encrypted with non-Microsoft technologies isn't supported.

Note

The decryption of email messages sent with an [Microsoft Purview Message Encryption custom branding template](add-your-organization-brand-to-encrypted-messages) is not supported by Microsoft eDiscovery tools. When using an OME custom branding template, email messages are delivered to the OME portal instead of the recipient's mailbox. Therefore, you won't be able to use eDiscovery tools to search for encrypted messages because those messages are never received by the recipient's mailbox.

For SharePoint, content labeled with SharePoint online service are decrypted. Items labeled or encrypted in the client before uploading to SharePoint, legacy document library RMS templates or settings and S/MIME or other standards aren't supported^2^.

## eDiscovery activities that support encrypted items

The following table identifies the supported tasks that can be performed in Microsoft Purview eDiscovery tools on encrypted files attached to email messages and encrypted documents in SharePoint and OneDrive. These supported tasks can be performed on encrypted files that match the criteria of a search. A value of `N/A` indicates the functionality isn't available in the corresponding eDiscovery tool.

| eDiscovery task | Content search | eDiscovery (Standard) | eDiscovery (Premium) |
| --- | --- | --- | --- |
| Search for content in encrypted files in sites and email attachments^1^ | No | No | Yes |
| Preview encrypted files attached to email | No | No | Yes |
| Preview encrypted documents in SharePoint and OneDrive | No | No | Yes |
| Review encrypted files in a review set | N/A | N/A | Yes |
| Export encrypted files attached to email | Yes | Yes | Yes |
| Export encrypted documents in SharePoint and OneDrive | No | No | Yes |
|  |  |  |  |

## Supported decryption

The following table describes the decryption supported by eDiscovery (Standard) and eDiscovery (Premium) for email, email with attachments, and files hosted by SharePoint.

| **Item type** | **Task** | **eDiscovery (Standard)** | **eDiscovery (Premium)** |
| --- | --- | --- | --- |
| Encrypted email | Search | Yes | Yes |
| Encrypted email | Decryption to .pst | No | Yes |
| Encrypted email | Decryption to file | Yes | Yes |
| Encrypted mail and attachment | Search | No | Yes (with Advanced indexing)^1^ |
| Encrypted mail and attachment | Decryption to .pst | No | Yes |
| Encrypted mail and attachment | Decryption to file | No | Yes |
| File in SharePoint with MIP label | Search | No | Yes |
| File in SharePoint with MIP label | Decryption | No | Yes |
| File in SharePoint with other encryption^2^ | Search, Decryption | No | No |
|  |  |  |  |

Important

eDiscovery (Standard) doesn't support legacy encryption protocols.

## Decryption limitations with email and attachments

eDiscovery support for decryption of email messages and attachments is subject to the following limitations:

- Decryption isn't supported when the email or attachment encryption is applied in an external organization. eDiscovery only supports decryption for email and attachments that are encrypted in your organization.
- When decrypting emails or attachments, the owner of the mailbox where the emails and attachments are included in eDiscovery activities must have access to view the encrypted content. Decryption for emails or attachments isn't supported if they're sent or forwarded other recipients that can't view the encrypted content. Changes in the owner's groups or other organization permissions may also affect decryption support.

## Decryption limitations with sensitivity labels in SharePoint and OneDrive

eDiscovery doesn't support encrypted files in SharePoint and OneDrive when a sensitivity label that applied the encryption is configured with either of the following settings:

- Users can assign permissions when they manually apply the label to a document. This is sometimes referred to as *user-defined permissions*.
- User access to the document has an expiration setting that is set to a value other than **Never**.

For more information about these settings, see the "Configure encryption settings" section in [Restrict access to content by using sensitivity labels to apply encryption](encryption-sensitivity-labels#configure-encryption-settings).

Documents encrypted with the previous settings can still be returned by an eDiscovery search. This result may happen when a document property (such as the title, author, or modified date) matches the search criteria. Although these documents might be included in search results, they can't be previewed or reviewed. These documents will also remain encrypted when they're exported in eDiscovery (Premium).

Important

Decryption isn't supported for files that are locally encrypted and then uploaded to SharePoint or OneDrive. For example, local files that are encrypted by the Microsoft Purview Information Protection client and then uploaded to Microsoft 365 aren't supported. Only files that are encrypted in the SharePoint or OneDrive service are supported for decryption.

## Notes

^1^ Encrypted files located on a local computer and copied to an email message aren't decrypted and indexed for eDiscovery. For eDiscovery (Premium), encrypted email and attachments in recipient mailbox needs to be advanced indexed to be decrypted. For more information about Advanced indexing, see [Advanced indexing of custodian data](ediscovery-indexing-custodian-data).

^2^ Only items labeled in SharePoint (or uploaded to SharePoint after integration with sensitivity labels are enabled) and that have labels with admin-defined permissions and no expiration are decrypted. All other encrypted files in SharePoint aren't decrypted. For more information, see [Enable sensitivity labels for files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).

Other documents aren't decrypted, including:

- Files encrypted in the client and uploaded before sensitivity labels were integrated with SharePoint Online.
- Documents encrypted with legacy RMS templates and not labeled.
- Documents with user-defined permissions or with expiration settings (SMIME or other standards).

^3^ Only content encrypted with RMS keys hosted in Microsoft 365 is transparently decrypted by eDiscovery (Premium). Double Key Encryption (DKE), Hold Your Own Key (HYOK), on-premises RMS, etc. aren't supported. For more information, see [Key types for the service](rights-management-tenant-key#key-types-for-the-service).