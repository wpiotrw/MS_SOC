---
layout: Conceptual
title: Investigating partially indexed items in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-investigating-partially-indexed-items
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to manage partially indexed items (also called unindexed items) from Exchange, SharePoint, and OneDrive for Business within your organization.
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
- sfi-image-nochange
locale: en-us
document_id: 3f9b74c1-390b-6298-0edf-eb64286aaabd
document_version_independent_id: 3f9b74c1-390b-6298-0edf-eb64286aaabd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-investigating-partially-indexed-items.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-investigating-partially-indexed-items
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-investigating-partially-indexed-items.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 5fe8bd3f-a11f-c641-f845-2882730beed8
---

# Investigating partially indexed items in eDiscovery | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

An eDiscovery search that you run from the Microsoft Purview portal automatically includes partially indexed items in the estimated search results when you run a search. Partially indexed items are Exchange mailbox items and documents on SharePoint and OneDrive for Business sites that for some reason weren't completely indexed for search. Most email messages and site documents are successfully indexed because they fall within the indexing limits for email messages. However, some items may exceed these indexing limits, and will be partially indexed. Here are other reasons why items can't be indexed for search and are returned as partially indexed items when you run an eDiscovery search:

- Email messages have an attached file that can't be opened; this is the most common cause of partially indexed email items.
- Too many files attached to an email message.
- A file attached to an email message is too large.
- The file type is supported for indexing but an indexing error occurred for a specific file.

Although it varies, most organizations customers have less than 1% of content by volume and less than 12% of content by size that is partially indexed. The reason for the difference between the volume versus size is that larger files have a higher probability of containing content that can't be completely indexed.

For more information about partially index items in Content search, see [Investigating partially indexed items in Content search](ediscovery-partially-indexed-items-in-content-search).

## Why does the partially indexed item count change for a search?

After you run an eDiscovery search, the total number and size of partially indexed items in the locations that were searched are listed in the search result statistics that are displayed in the detailed statistics for the search. Note these are called *unindexed items* in the search statistics. Here are a few things that will affect the number of partially indexed items that are returned in the search results:

- If an item is partially indexed and matches the search query, it's included in both the count (and size) of search result items and partially indexed items. However, when the results of that same search are exported, the item is included only with set of search results; it's not included as a partially indexed item.
- Partially indexed items located in SharePoint and OneDrive sites *aren't* included in the estimate of partially indexed items that's displayed in the detailed statistics for the search. However, partially indexed items can be exported when you export the results of an eDiscovery search. For example, if you only search sites, the estimated number partially indexed items will be zero.

## Calculating the ratio of partially indexed items in your organization

To understand your organization's exposure to partially indexed items, you can run a search for all content in all mailboxes (by using a blank keyword query). In the following example, there are 1,629,904 (146.46 GB) fully indexed items and 10,025 (10.27 GB) partially indexed items.

![Example of search statistics showing partially indexed items.](media/partiallyindexeditemstest.png)

You can determine the percentage of partially indexed items by using the following calculations.

**To calculate the ratio of partially indexed items in your organization:**

`(Total number of partially indexed items/Total number of items) x 100`

`(10025/1629904) x 100 = 0.62%`

By using the search results from the previous example, 0.62% of all mailboxes items are partially indexed.

**To calculate the percentage of the size of partially indexed items in your organization:**

`(Size of all partially indexed items/Size of all items) x 100`

`(10.27 GB/146.46 GB) x 100 = 7.0%`

So in the previous example, 7% of the total size of mailbox items are from partially indexed items. As previously stated, most organizations customers have less than 1% of content by volume and less than 12% of content by size that is partially indexed.

## Working with partially indexed items

In cases when you need to examine partially indexed items to validate that they don't contain relevant information, you can export a content search report that contains information about partially indexed items. When you export a content search report, be sure to choose one of the export options that includes partially indexed items.

![Choose the second or third option to export partially indexed items.](media/partiallyindexeditemsexportoptions.png)

When you export eDiscovery search results or a search report using one of these options, the export includes a report named Unindexed Items.csv. This report includes most of the same information as the ResultsLog.csv file; however, the Unindexed Items.csv file also includes two fields related to partially indexed items: **Error Tags** and **Error Properties**. These fields contain information about the indexing error for each partially indexed item. Using the information in these two fields can help you determine whether or not the indexing error for a particular impacts your investigation.

Note

The Unindexed Items.csv file also contains fields named **Error Type** and **Error Message**. These are legacy fields that contain information that is similar to the information in the **Error Tags** and **Error Properties** fields, but with less detailed information. You can safely ignore these legacy fields.

## Errors related to partially indexed items

Error tags are made up of two pieces of information, the error and the file type. For example, in this error/file-type pair:

```text
 parseroutputsize_xls
```

`parseroutputsize` is the error and `xls` is the file type of the file the error occurred on. In cases where the file type wasn't recognized or the file type didn't apply to the error, you will see the value `noformat` in place of the file type.

The following is a list of indexing errors and a description of the possible cause of the error.

| Error tag | Description |
| --- | --- |
| `attachmentcount` | An email message had too many attachments, and some of these attachments weren't processed. |
| `attachmentdepth` | The content retriever and document parser found too many levels of attachments nested inside other attachments. Some of these attachments weren't processed. |
| `attachmentrms` | An attachment failed decoding because it was RMS-protected. |
| `attachmentsize` | A file attached to an email message was too large and couldn't be processed. |
| `indexingtruncated` | When writing the processed email message to the index, one of the indexable properties was too large and was truncated. The truncated properties are listed in Error Properties field. |
| `invalidunicode` | An email message contained text that couldn't be processed as valid Unicode. Indexing for this item may be incomplete. |
| `parserencrypted` | The content of attachment or email message is encrypted, and Microsoft 365 couldn't decode the content. |
| `parsererror` | An unknown error occurred during parsing. This typically results from a software bug or a service crash. |
| `parserinputsize` | An attachment was too large for the parser to handle, and the parsing of that attachment didn't happen or wasn't completed. |
| `parsermalformed` | An attachment was malformed and couldn't be handled by the parser. This result can be due to old file formats, files created by incompatible software, or viruses pretending to be something other than claimed. |
| `parseroutputsize` | The output from the parsing of an attachment was too large and had to be truncated. |
| `parserunknowntype` | An attachment had a file type that Microsoft 365 couldn't detect. |
| `parserunsupportedtype` | An attachment had a file type that Office 365 could detect, but parsing that file type isn't supported. |
| `propertytoobig` | The value of an email property in Exchange Store was too large to be retrieved and the message couldn't be processed. This typically only happens to the body property of an email message. |
| `retrieverrms` | The content retriever failed to decode an RMS-protected message. |
| `wordbreakertruncated` | Too many words were identified in the document during indexing. Processing of the property stopped when reaching the limit, and the property is truncated. |

Error fields describe which fields are affected by the processing error listed in the Error Tags field. If you're searching a property such as `subject` or `participants`, errors in the body of the message won't impact the results of your search. This can be useful when determining exactly which partially indexed items you might need to further investigate.