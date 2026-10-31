---
layout: Conceptual
title: Partially indexed items in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-ref-partially-indexed-items
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about unindexed items in Exchange and SharePoint that you can include in searches in eDiscovery.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-23T00:00:00.0000000Z
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
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1015
locale: en-us
document_id: d2abe153-1557-84dd-4a43-fe31ae6e7f08
document_version_independent_id: d2abe153-1557-84dd-4a43-fe31ae6e7f08
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-ref-partially-indexed-items.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-ref-partially-indexed-items
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-ref-partially-indexed-items.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 017f88db-2088-84b5-284b-46c1fe336d55
---

# Partially indexed items in eDiscovery | Microsoft Learn

When you select **Include partially indexed items**, eDiscovery searches automatically include partially indexed items in the estimated search results. Partially indexed items are Exchange mailbox items and documents on SharePoint and OneDrive sites that weren't completely indexed for search. In Exchange, a partially indexed item typically contains a file (of a file type that can't be indexed) attached to an email message.

The following reasons explain why items can't be indexed for search and are returned as partially indexed items:

- The file type is unrecognized or unsupported for indexing.
- Messages have an attached file that can't be opened; this issue is the most common cause of partially indexed email items.
- The file type is supported for indexing but an indexing error occurred for a specific file.
- Too many files attached to an email message.
- A file attached to an email message is too large.
- A file is encrypted with non-Microsoft technologies.
- A file attached to an email message is encrypted with a Microsoft Purview sensitivity label that applies encryption. Exchange doesn't index the attachment content, even though the attachment can be decrypted during export.
- A file is password-protected.

Note

Most organizations have less than 1% of content by volume and less than 12% by size that is partially indexed. The reason for the difference between volume and size is that larger files have a higher probability of containing content that can't be completely indexed.

For legal investigations, your organization might be required to review partially indexed items. You can specify whether to include partially indexed items when you export search results or when you add search results to a review set.

## File types not indexed for search

Certain types of files, such as Bitmap (.bmp) or MP3 (.mp3) files, don't contain content that can be indexed. The search indexing servers in Exchange and SharePoint don't perform full-text indexing on these types of files. These file types are considered unsupported file types. There are also file types for which full-text indexing is disabled, either by default or by an administrator. Unsupported and disabled file types are labeled as unindexed items in searches.

For a list of supported and disabled file formats, see the following articles:

- **Exchange**: [File formats indexed by Exchange Search](/en-us/exchange/file-formats-indexed-by-exchange-search-exchange-2013-help?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json)
- **Exchange**: [Get-SearchDocumentFormat](/en-us/powershell/module/exchange/get-searchdocumentformat)
- **SharePoint**: [Default crawled file name extensions and parsed file types in SharePoint](/en-us/SharePoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json)

## Messages and documents with partially indexed file types returned in search results

Not every email message with a partially indexed file attachment or every partially indexed SharePoint document is automatically returned as a partially indexed item. That's because other message or document properties, such as the **Subject** property in email messages and the **Title** or **Author** properties for documents, are indexed and available to be searched. For example, a keyword search for *financial* returns items with a partially indexed file attachment if that keyword appears in the subject of an email message or in the file name or title of a document. However, if the keyword appears only in the body of the file, the message or document is returned as a partially indexed item.

Similarly, messages with partially indexed file attachments and documents of a partially indexed file type are included in search results when other message or document properties, which are indexed and searchable, match the search criteria. Message properties that are indexed for search include sent and received dates, sender and recipient, the file name of an attachment, and text in the message body. Document properties indexed for search include created and modified dates. So even though a message attachment might be a partially indexed item, the message is included in the regular search results if the value of other message or document properties matches the search criteria.

For a list of email and document properties that you can search for by using eDiscovery tools in the Microsoft Purview portal, see [Keyword queries and search conditions for eDiscovery](edisc-keyword-query-language).

Note

If you move a mailbox item from a folder that is indexed to a folder that isn't indexed, a flag is set to unindex the item. The item is removed from the index and isn't searchable. Later, if you move that same item back to a folder that is indexed, the flag isn't reset. That means the item remains unindexed, and not searchable.

## Partially indexed items included in search results

Your organization might need to identify and analyze partially indexed items to determine what they are, what they contain, and whether they're relevant to a specific investigation. If you select **Include partially indexed items**, the partially indexed items in the content locations that you search are automatically included with the estimated search results. Depending on the specific setting you select, you can control whether to include partially indexed items in locations with indexed search hits, partially indexed items in locations without indexed search hits, or both. You can also include these partially indexed items when you export search results or add items to review sets.

Keep the following points in mind about partially indexed items:

- When you run an eDiscovery search, the total number and size of partially indexed Exchange items (returned by the search query) appear in the [search statistics view](edisc-search-results#statistics-dashboard), and they're labeled as **partially indexed items**. Statistics about partially indexed items don't include partially indexed items in SharePoint sites or OneDrive accounts.
- If you export results from a search of specific content locations or all content locations in your organization, only the unindexed items from content locations that contain items that match the search criteria are exported. In other words, if no search results are found in a mailbox or site, then any unindexed items in that mailbox or site aren't exported. The reason for this behavior is that exporting partially indexed items from many locations in the organization might increase the likelihood of export errors and increase the time it takes to export and download the search results.

    To export partially indexed items from all content locations for a search, configure the search to return all items (by removing any keywords from the search query) and then export only partially indexed items when you export the search results (by selecting **partially indexed items** under Select items to include in your [export options](edisc-search-export)).
- If you choose to include all mailbox items in the search results, or if a search query doesn't specify any keywords or only specifies a date range, partially indexed items might not be copied to the PST file that contains the partially indexed items. This behavior occurs because all items, including any partially indexed items, are automatically included in the regular search results.
- You can't preview partially indexed items. To view partially indexed items returned by the search, you need to export the search results.

    Additionally, when you export search results and include partially indexed items in the export, partially indexed items from SharePoint items are exported to a folder named **Uncrawlable**. When you export partially indexed Exchange items, they're exported differently depending on whether the partially indexed items matched the search query and the configuration of the export settings.
- The following table shows the export behavior of indexed and partially indexed items and whether each is included for the different export configuration settings.

    | **Export configuration** | **Indexed items that match search query** | **Partially indexed items that match search query** | **Partially indexed items that don't match search query** |
    | --- | --- | --- | --- |
    | Export only indexed items | Exported | Exported (included with the indexed items exported) | Not exported |
    | Export only partially indexed items | Not exported | Exported (as partially indexed items) | Exported (as partially indexed items) |
    | Export indexed and partially indexed items | Exported | Exported (included with the indexed items exported) | Exported (as partially indexed items) |

## Locations and the "in locations without search hits" option

When you include partially indexed items in an export (or add them to a review set), you can also choose to **exclude partially indexed items in locations without search hits**. Understanding what *location* means in this option determines what your export contains.

A **location** in eDiscovery is one of:

- A single **Exchange Online mailbox**, or
- A single **SharePoint Online site** or **OneDrive for Business site**.

A location is **not** a folder, a URL prefix, a SharePoint document library, or any subset of a mailbox or site defined by a Kusto Query Language (KQL) condition. The smallest unit the partial-index location filter operates on is the entire mailbox or the entire site.

### What the option does

| Setting | Behavior |
| --- | --- |
| *Exclude partially indexed items in locations without search hits* (selected) | Partially indexed items are returned only from mailboxes and sites where at least one item also matched your search query. Mailboxes and sites with zero indexed matches contribute zero partially indexed items. |
| *Exclude partially indexed items in locations without search hits* (cleared) | Partially indexed items are returned from every selected mailbox and site, regardless of whether the indexed query matched anything in that mailbox or site. |

### KQL conditions don't constrain partially indexed items

Partially indexed items are returned based on the **location's index state**, not on whether the item matches your KQL query. If your query uses a path, URL, file-name pattern, or other property restriction (for example, `DocumentLink:"https://contoso.sharepoint.com/sites/Finance/Subfolder/*"`), partially indexed items from **anywhere** in the matched site can still appear in your export. They aren't evaluated against the restriction.

If you need to filter partially indexed items by KQL, select **Perform advanced indexing on partially indexed items** at export time. Advanced indexing re-indexes the items so your KQL conditions apply to them.

### Single-location searches

If your scope is a single mailbox or a single site, the *Exclude partially indexed items in locations without search hits* option has **no effect**:

- If the location returns at least one indexed hit, it's considered responsive, and all of its partially indexed items are included.
- If the location returns no indexed hits, no items of any kind are exported from that location.

For single-location scopes, expect the location's full set of partially indexed items whenever you include partially indexed items at export, or use advanced indexing to apply your KQL conditions.

### Example

A SharePoint search scoped to a single site uses the query `DocumentLink:"https://contoso.sharepoint.com/sites/Project/Subfolder/*"` and includes partially indexed items at export. Two outcomes are guaranteed:

1. **Indexed items** in the export are limited to the `Subfolder/*` path (the KQL condition applies).
2. **Partially indexed items** in the export include every partially indexed item across the entire `sites/Project` site, not just `Subfolder/*` (KQL doesn't apply to partially indexed items, and the location is the whole site).

To restrict partially indexed items to the same subfolder, enable **Perform advanced indexing on partially indexed items**.

## Search-time and export-time settings are independent

eDiscovery search and export are separate jobs. The partially indexed item choices you make on each are independent:

| Where you set it | What it controls |
| --- | --- |
| Search query (search-time *Include partially indexed items*) | The statistics and preview returned by the search. It doesn't carry into a subsequent export. |
| Export dialog (export-time *Include partially indexed items*, *Exclude … in locations without search hits*, *Perform advanced indexing*) | The contents of the export package. These are the authoritative settings for what is exported. |

If you set partial-index inclusion at search but clear it at export, the export contains no partially indexed items, regardless of what your search statistics showed. If you clear it at search but set it at export, the export contains partially indexed items according to the export-dialog settings. Always confirm partial-index behavior at the export step.

## Date ranges and excluding partially indexed items

In eDiscovery searches, you can't use a date range to exclude partially indexed items from results in a search query. The search statistics include partially indexed items that fall outside of a date range, and you include them when you export partially indexed items. In eDiscovery with premium feature support, you can add partially indexed items to a review set and then filter them in a review set before export. Alternatively, use the advanced indexing capability (a premium eDiscovery feature) to ensure these partially indexed items are reindexed to compare to the date range specified and to avoid a large volume of data getting exported.

For more information about indexing limits for email messages, see [Limits in eDiscovery](edisc-ref-limits#indexing-limits-for-email-messages).

## Assess partially indexed items in your organization

After you run an eDiscovery search, you can see the total number and size of partially indexed items in the locations that you searched in the search result statistics. The detailed statistics for the search show this information.

A few factors affect the number of partially indexed items that appear in the search results:

- If an item is partially indexed and matches the search query, the item is included in both the count and size of search result items and partially indexed items. However, when you export the results of that same search, the item is included only with set of search results and isn't included as a partially indexed item.
- The detailed statistics for the search *don't* include partially indexed items located in SharePoint and OneDrive sites in the estimate of partially indexed items. However, when you export the results of an eDiscovery search, you can include partially indexed items in the export. For example, if you only search sites, the estimated number of partially indexed items is zero.

To understand your organization's exposure to partially indexed items, run a search for all content in all mailboxes or a representative subset of mailboxes by using a blank keyword query.

In the following example, there are 1,629,904 (146.46 GB) fully indexed items and 10,025 (10.27 GB) partially indexed items.

You can determine the percentage of partially indexed items by using the following calculations.

**To calculate the ratio of partially indexed items in your organization:**

`(Total number of partially indexed items/Total number of items) x 100`

`(10025/1629904) x 100 = 0.62%`

By using the search results from the previous example, 0.62% of all mailbox items are partially indexed.

**To calculate the percentage of the size of partially indexed items in your organization:**

`(Size of all partially indexed items/Size of all items) x 100`

`(10.27 GB/146.46 GB) x 100 = 7.0%`

In the previous example, 7% of the total size of mailbox items comes from partially indexed items. Most customers have less than 1% of content by volume and less than 12% of content by size that is partially indexed.

For additional assessment of what types of content make up partially indexed items for your organization, select **Partially indexed items** to include in your export item report or overall export for further investigation.

## More information about partially indexed items

- Because message and document properties and their metadata are indexed, a keyword search might return results if that keyword appears in the indexed metadata. However, that same keyword search might not return the same item if the keyword only appears in the content of an item with an unsupported file type. In this case, the item is returned as a partially indexed item.
- If a partially indexed item matches the search query criteria, it's included in the search results. However, it's not included with partially indexed items when you export search results.
- Although a file type is supported for indexing and is indexed, indexing or search errors can cause a file to be returned as a partially indexed item. For example, searching a large Excel file might be partially successful (because the first 4 MB are indexed), but then fails because the file size limit is exceeded. In this case, it's possible that the same file is returned with the search results and as a partially indexed item.
- Files that are encrypted with [Microsoft encryption technologies](encryption), including Microsoft Purview sensitivity labels that apply encryption, behave differently depending on location:

    - Email attachments: Exchange doesn't index encrypted attachments. Keyword searches don't match content inside these attachments, and they're returned as partially indexed items. However, if the email message itself matches the search criteria (for example, the subject or sender), the message is included in the search results. You can decrypt encrypted attachments during preview and export.
    - SharePoint folders and OneDrive files: Files encrypted with Microsoft encryption technologies are partially indexed.
    - To ensure encrypted attachments are captured, include partially indexed items when exporting search results or adding results to a review set. Use review sets to analyze the decrypted content after collection.
- Email messages encrypted with S/MIME are partially indexed. This limitation includes encrypted messages with or without file attachments.
- Email messages protected using Azure Rights Management are indexed and are included in the search results if they match the search query. Rights-protected email messages are decrypted and can be previewed and exported. This functionality requires that you're assigned the RMS Decrypt role, which is assigned by default to the eDiscovery Manager role group.
- Don't use query-based holds to address encrypted or partially indexed items. Query-based hold with queries that include conditions beyond dates, participants, or item types - such as keywords or paths - might not be applicable for these items. There's a risk that the hold won't be applied as intended. To ensure coverage, limit query-based hold conditions for date ranges, participants, and item types only or apply a location-based hold. For more information, see [Create an eDiscovery hold](edisc-hold-create).