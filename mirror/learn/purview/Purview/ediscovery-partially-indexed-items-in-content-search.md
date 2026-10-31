---
layout: Conceptual
title: Partially indexed items in Content Search | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-partially-indexed-items-in-content-search
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about unindexed items in Exchange and SharePoint that you can include in a Content search that you run in the Microsoft Purview portal.
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
- SPO160
- MOE150
- MET150
locale: en-us
document_id: f2e8d6dd-3900-6403-9f94-803cb5509e80
document_version_independent_id: f2e8d6dd-3900-6403-9f94-803cb5509e80
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-partially-indexed-items-in-content-search.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-partially-indexed-items-in-content-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-partially-indexed-items-in-content-search.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 1dae4d3e-f3a7-d00d-eb28-d34b151b9a64
---

# Partially indexed items in Content Search | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

A Content search that you run from the Microsoft Purview portal automatically includes partially indexed items in the estimated search results when you run a search. Partially indexed items are Exchange mailbox items and documents on SharePoint and OneDrive for Business sites that for some reason weren't completely indexed for search. In Exchange, a partially indexed item typically contains a file (of a file type that can't be indexed) that is attached to an email message. Here are some other reasons why items can't be indexed for search and are returned as partially indexed items when you run an eDiscovery search:

- The file type is unrecognized or unsupported for indexing.
- Messages have an attached file that can't be opened; this is the most common cause of partially indexed email items.
- The file type is supported for indexing but an indexing error occurred for a specific file.
- Too many files attached to an email message.
- A file attached to an email message is too large.
- A file is encrypted with non-Microsoft technologies.
- A file is password-protected.

Note

Most organizations have less than 1% of content by volume and less than 12% by size that is partially indexed. The reason for the difference between volume and size is that larger files have a higher probability of containing content that can't be completely indexed.

For legal investigations, your organization may be required to review partially indexed items. You can also specify whether to include partially indexed items when you export search results to a local computer or when you prepare the results for analysis with eDiscovery (Premium). For more information, see [Investigating partially indexed items in eDiscovery](ediscovery-investigating-partially-indexed-items).

## File types not indexed for search

Certain types of files, such as Bitmap (.bmp) or MP3 (.mp3) files, don't contain content that can be indexed. As a result, the search indexing servers in Exchange and SharePoint don't perform full-text indexing on these types of files. These types of files are considered to be unsupported file types. There are also file types for which full-text indexing has been disabled, either by default or by an administrator. Unsupported and disabled file types are labeled as unindexed items in Content Searches. As previously stated, partially indexed items can be included in the set of search results when you run a search, export the search results to a local computer, or prepare search results for eDiscovery (Premium).

For a list of supported and disabled file formats, see the following articles:

- **Exchange** - [File formats indexed by Exchange Search](/en-us/exchange/file-formats-indexed-by-exchange-search-exchange-2013-help)
- **Exchange** - [Get-SearchDocumentFormat](/en-us/powershell/module/exchange/get-searchdocumentformat)
- **SharePoint** - [Default crawled file name extensions and parsed file types in SharePoint](/en-us/SharePoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types)

## Messages and documents with partially indexed file types can be returned in search results

Not every email message with a partially indexed file attachment or every partially indexed SharePoint document is automatically returned as a partially indexed item. That's because other message or document properties, such as the **Subject** property in email messages and the **Title** or **Author** properties for documents are indexed and available to be searched. For example, a keyword search for "financial" will return items with a partially indexed file attachment if that keyword appears in the subject of an email message or in the file name or title of a document. However, if the keyword appears only in the body of the file, the message or document would be returned as a partially indexed item.

Similarly, messages with partially indexed file attachments and documents of a partially indexed file type are included in search results when other message or document properties, which are indexed and searchable, match the search criteria. Message properties that are indexed for search include sent and received dates, sender and recipient, the file name of an attachment, and text in the message body. Document properties indexed for search include created and modified dates. So even though a message attachment may be a partially indexed item, the message will be included in the regular search results if the value of other message or document properties matches the search criteria.

For a list of email and document properties that you can search for by using eDiscovery tools in the Microsoft Purview portal, see [Keyword queries and search conditions for eDiscovery](ediscovery-keyword-queries-and-search-conditions).

Note

If a mailbox item is moved from a folder that is indexed to a folder that is not indexed, a flag is set to unindex the item and the item is removed from the index and will not be searchable. Later, if that same item is moved back to a folder that is indexed, the flag is not reset. That means the item will remain unindexed, and not searchable.

## Partially indexed items included in the search results

Your organization might be required to identify and perform additional analysis on partially indexed items to determine what they are, what they contain, and whether they're relevant to a specific investigation. As previously explained, the partially indexed items in the content locations that are searched are automatically included with the estimated search results. You have the option to include these partially indexed items when you export search results or prepare the search results for eDiscovery (Premium).

Keep the following in mind about partially indexed items:

- When you run an eDiscovery search, the total number and size of partially indexed Exchange items (returned by the search query) are displayed in the search statistics on the flyout page, and labeled as **unindexed items**. Statistics about partially indexed items displayed on the flyout page don't include partially indexed items in SharePoint sites or OneDrive accounts.
- If the search that you're exporting results from was a search of specific content locations or all content locations in your organization, only the unindexed items from content locations that contain items that match the search criteria will be exported. In other words, if no search results are found in a mailbox or site, then any unindexed items in that mailbox or site won't be exported. The reason for this is that exporting partially indexed items from lots of locations in the organization might increase the likelihood of export errors and increase the time it takes to export and download the search results.

    To export partially indexed items from all content locations for a search, configure the search to return all items (by removing any keywords from the search query) and then export only partially indexed items when you export the search results (by selecting **Only items that have an unrecognized format, are encrypted, or weren't indexed for other reasons** under **Output options**).
- If you choose to include all mailbox items in the search results, or if a search query doesn't specify any keywords or only specifies a date range, partially indexed items might not be copied to the PST file that contains the partially indexed items. This is because all items, including any partially indexed items, will be automatically included in the regular search results.
- Partially indexed items aren't available to be previewed. You have to export the search results to view partially indexed items returned by the search.

    Additionally, when you export search results and include partially indexed items in the export, partially indexed items from SharePoint items are exported to a folder named **Uncrawlable**. When you export partially indexed Exchange items, they're exported differently depending if the partially indexed items matched the search query and the configuration of the export settings.
- The following table shows the export behavior of indexed and partially indexed items and whether or not each is included for the different export configuration settings.

    | **Export configuration** | **Indexed items that match search query** | **Partially indexed items that match search query** | **Partially indexed items that don't match search query** |
    | --- | --- | --- | --- |
    | Export only indexed items | Exported | Exported (included with the indexed items exported) | Not exported |
    | Export only partially indexed items | Not exported | Exported (as partially indexed items) | Exported (as partially indexed items) |
    | Export indexed and partially indexed items | Exported | Exported (included with the indexed items exported) | Exported (as partially indexed items) |
    |  |  |  |  |

## Date ranges and excluding partially indexed items

In Content search and Microsoft Purview eDiscovery, you can't use a date range to exclude partially indexed items from being returned by a search query. In other words, partially indexed items that fall outside of a date range are still included as partially indexed items in the search statistics and when you export partially indexed items. In eDiscovery (Premium), partially indexed items can be collected and then filtered in a review set prior to export.

## Indexing limits for messages

The following table describes the indexing limits that might result in an email message being returned as a partially indexed item in an eDiscovery search in Microsoft 365.

For a list of indexing limits for SharePoint documents, see [Search limits for SharePoint Online](/en-us/sharepoint/search-limits).

| **Indexing limit** | **Maximum value** | **Description** |
| --- | --- | --- |
| Maximum attachment size (excluding Excel files) | 150 MB | The maximum size of an email attachment that will parse for indexing. Any attachment that's larger than this limit won't be parsed for indexing, and the message with the attachment will be marked as partially indexed. **Note:** Parsing is the process where the indexing service extracts text from the attachment, removes unnecessary characters like punctuation and spaces, and then divides the text into words (in a process called tokenization), that are then stored in the index. |
| Maximum size of Excel files | 4 MB | The maximum size of an Excel file located on a site or attached to an email message that will be parsed for indexing. Any Excel file that's larger than this limit won't be parsed, and the file or the email the message with the file attachment will be marked as unindexed. |
| Maximum number of attachments | 250 | The maximum number of files attached to an email message that will be parsed for indexing. If a message has more than 250 attachments, the first 250 attachments are parsed and indexed, and the message is marked as partially indexed because it had additional attachments that weren't parsed. |
| Maximum attachment depth | 30 | The maximum number of nested attachments that are parsed. For example, if an email message has another message attached to it and the attached message has an attached Word document, the Word document and the attached message will be indexed. This behavior will continue for up to 30 nested attachments. |
| Maximum number of attached images | 0 | An image that's attached to an email message is skipped by the parser and isn't indexed. |
| Maximum time spent parsing an item | 30 seconds | A maximum of 30 seconds is spent parsing an item for indexing. If the parsing time exceeds 30 seconds, the item is marked as partially indexed. |
| Maximum parser output | 2 million characters | The maximum amount of text output from the parser that's indexed. For example, if the parser extracted 8 million characters from a document, only the first 2 million characters are indexed. |
| Maximum annotation tokens | 2 million | When an email message is indexed, each word is annotated with different processing instructions that specify how that word should be indexed. Each set of processing instructions is called an annotation token. To maintain the quality of service in Office 365, there's a limit of 2 million annotation tokens for an email message. |
| Maximum body size in index | 67 million characters | The total number of characters in the body of an email message and all its attachments. When an email message is indexed, all text in the body of the message and in all attachments is concatenated into a single string. The maximum size of this string that is indexed is 67 million characters. |
| Maximum unique tokens in body | 1 million | As previously explained, tokens are the result of extracting text from content, removing punctuation and spaces, and then dividing it into words (called tokens) that are stored in the index. For example, the phrase `"cat, mouse, bird, dog, dog"` contains 5 tokens. But only 4 of these are unique tokens. There's a limit of 1 million unique tokens per email message, which helps prevent the index from getting too large with random tokens. |
|  |  |  |

## More information about partially indexed items

- As previously stated, because message and document properties and their metadata are indexed, a keyword search might return results if that keyword appears in the indexed metadata. However, that same keyword search might not return the same item if the keyword only appears in the content of an item with an unsupported file type. In this case, the item would be returned as a partially indexed item.
- If a partially indexed item is included in the search results because it matched the search query criteria, it isn't included with partially indexed items when you export search results.
- Although a file type is supported for indexing and is indexed, there can be indexing or search errors that will cause a file to be returned as a partially indexed item. For example, searching a large Excel file might be partially successful (because the first 4 MB are indexed), but then fails because the file size limit is exceeded. In this case, it's possible that the same file is returned with the search results and as a partially indexed item.
- Files that are encrypted with [Microsoft encryption technologies](encryption) and are attached to an email message that matches the criteria of a search can be previewed and will be decrypted when exported. At this time, files that are encrypted with Microsoft encryption technologies (and stored in SharePoint or OneDrive for Business) are partially indexed.
- Email messages encrypted with S/MIME are partially indexed. This includes encrypted messages with or without file attachments.
- Email messages protected using Azure Rights Management are indexed and will be included in the search results if they match the search query. Rights-protected email messages are decrypted and can be previewed and exported. This functionality requires that you're assigned the RMS Decrypt role, which is assigned by default to the eDiscover Manager role group.
- If you create a query-based hold that's associated with an eDiscovery case, all partially indexed items are placed on hold. This includes partially indexed items that don't match the search query criteria for the hold. For more information about creating query-based eDiscovery holds, see [Create an eDiscovery hold](ediscovery-create-holds).