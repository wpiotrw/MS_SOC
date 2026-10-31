---
layout: Conceptual
title: Partially indexed items in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-ref-partially-indexed-items
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Understand partially indexed items in Data Security Investigations, including causes, file types, and how to analyze them effectively.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-02-18T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 565f788b-9a07-303c-1193-8fbc4c435b25
document_version_independent_id: 565f788b-9a07-303c-1193-8fbc4c435b25
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-ref-partially-indexed-items.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-ref-partially-indexed-items
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-ref-partially-indexed-items.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 51a13d82-e2d4-19a1-7730-db628965d597
---

# Partially indexed items in Data Security Investigations | Microsoft Learn

Data Security Investigations searches automatically include partially indexed items in the estimated search results. Partially indexed items are Exchange mailbox items and documents on SharePoint and OneDrive sites that aren't completely indexed for search. In Exchange, a partially indexed item typically contains a file (of a file type that can't be indexed) attached to an email message.

The following list describes other reasons why items can't be indexed for search and are returned as partially indexed items:

- The file type is unrecognized or unsupported for indexing.
- Messages have an attached file that can't be opened. This issue is the most common cause of partially indexed email items.
- The file type is supported for indexing but an indexing error occurred for a specific file.
- Too many files attached to an email message.
- A file attached to an email message is too large.
- A file is encrypted with non-Microsoft technologies.
- A file is password-protected.

Note

Most organizations have less than 1% of content by volume and less than 12% by size that is partially indexed. The reason for the difference between volume and size is that larger files have a higher probability of containing content that can't be fully indexed.

## File types not indexed for search

Certain types of files, such as Bitmap (.bmp) or MP3 (.mp3) files, don't contain content that can be indexed. The search indexing servers in Exchange and SharePoint don't perform full-text indexing on these types of files and they're considered as unsupported file types. There are also file types for which full-text indexing is disabled, either by default or by an administrator. Unsupported and disabled file types are labeled as unindexed items in searches.

For a list of supported and disabled file formats, see the following articles:

- **Exchange**: [File formats indexed by Exchange Search](/en-us/exchange/file-formats-indexed-by-exchange-search-exchange-2013-help)
- **Exchange**: [Get-SearchDocumentFormat](/en-us/powershell/module/exchange/get-searchdocumentformat)
- **SharePoint**: [Default crawled file name extensions and parsed file types in SharePoint](/en-us/SharePoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types)

## Messages and documents with partially indexed file types returned in search results

Not every email message with a partially indexed file attachment or every partially indexed SharePoint document is automatically returned as a partially indexed item. That's because other message or document properties, such as the **Subject** property in email messages and the **Title** or **Author** properties for documents, are indexed and available to be searched. For example, a keyword search for *financial* returns items with a partially indexed file attachment if that keyword appears in the subject of an email message or in the file name or title of a document. However, if the keyword appears only in the body of the file, the message or document is returned as a partially indexed item.

Similarly, messages with partially indexed file attachments and documents of a partially indexed file type are included in search results when other message or document properties, which are indexed and searchable, match the search criteria. Message properties that are indexed for search include sent and received dates, sender and recipient, the file name of an attachment, and text in the message body. Document properties indexed for search include created and modified dates. So even though a message attachment might be a partially indexed item, the message is included in the regular search results if the value of other message or document properties matches the search criteria.

Note

If a mailbox item is moved from a folder that is indexed to a folder that isn't indexed, a flag is set to unindex the item and the item is removed from the index and isn't searchable. Later, if that same item is moved back to a folder that is indexed, the flag isn't reset. That means the item remains unindexed, and not searchable.

To perform a deeper analysis of partially indexed items, use Microsoft Purview eDiscovery to export and review partially indexed items. For more information, see [Partially indexed items in eDiscovery](edisc-ref-partially-indexed-items).

## More information about partially indexed items

- Because message and document properties and their metadata are indexed, a keyword search might return results if that keyword appears in the indexed metadata. However, that same keyword search might not return the same item if the keyword only appears in the content of an item with an unsupported file type. In this case, the item is returned as a partially indexed item.
- Although a file type is supported for indexing and is indexed, indexing or search errors can cause a file to be returned as a partially indexed item. For example, searching a large Excel file might be partially successful (because the first 4 MB are indexed), but then fails because the file size limit is exceeded. In this case, it's possible that the same file is returned with the search results and as a partially indexed item.
- Files that are encrypted with Microsoft encryption technologies (and stored in SharePoint or OneDrive) are partially indexed.
- Email messages encrypted with S/MIME are partially indexed. This limitation includes encrypted messages with or without file attachments.
- Email messages protected using Azure Rights Management are indexed and are included in the search results if they match the search query.