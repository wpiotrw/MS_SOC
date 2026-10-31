---
layout: Conceptual
title: Limits in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-ref-limits
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the feature area and individual item limits for eDiscovery.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-08T00:00:00.0000000Z
audience: Admin
ms.topic: reference
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
ai-usage: ai-assisted
locale: en-us
document_id: df77475f-92e4-05da-1bad-b8eb71bc8c20
document_version_independent_id: df77475f-92e4-05da-1bad-b8eb71bc8c20
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-ref-limits.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-ref-limits
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-ref-limits.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 3f7bf42b-b5e0-f708-53db-172f09525594
---

# Limits in eDiscovery | Microsoft Learn

This article describes the limits in Microsoft Purview eDiscovery.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Case limits

The following table lists the limits for cases in eDiscovery.

| Description of limit | eDiscovery feature support | Premium eDiscovery feature support |
| --- | --- | --- |
| Maximum number of cases for an organization. | 10,000 | 50,000 |

## Case and review set limits

The following table lists the limits for cases and review sets in eDiscovery with premium feature support.

Tip

Want to try premium eDiscovery features? See the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Microsoft 365 Enterprise E5 licensing.

| Description of limit | Premium eDiscovery feature support |
| --- | --- |
| Total number of documents that you can add to a case (for all review sets in a case). | 40 million |
| Total file size per load set. This limit includes loading non-Office 365 content into a review set. | 1 TB |
| Maximum size per review set. | 1 TB |
| Maximum number of load sets per case. | 200 |
| Maximum number of review sets per case. | 100 |
| Maximum number of tag groups per case. | 1,000 |
| Maximum number of unique tags per case. | 1,000 |
| Maximum number of tagged documents per case. | Unlimited |

## Export limits

Note

When exporting large individual items (5 GB or greater), configure the export job to include only one large item per export. This configuration reduces the likelihood of performance-related issues during the export.

The following table lists the limits when exporting the results of a search.

| Description of limit | eDiscovery feature support | Premium eDiscovery feature support |
| --- | --- | --- |
| Export report total items for one report | 1 million | 1 million |
| Export report total locations for one report | 500,000 | 500,000 |
| Export results maximum number locations for one export | 100,000 | 100,000 |
| Export results maximum number of items for one export | 500,000 | 500,000 |
| Maximum amount of exportable data from a single search. | 2 TB^1^ | 5 TB |
| Maximum an organization can export in a single day.^2^ | 2 TB | 5 TB |
| Maximum number of exports or reports displayed in Content Search or eDiscovery cases. | 1,000 | 2,000 |
| Maximum size of individual file supported for export | 5 GB | 5 GB |
| Maximum size of PST file that can be exported. | 10 GB^3^ | 10 GB |
| Maximum size per export package. | 40 GB | 40 GB |
| Rate at which content from mailboxes are exported | 2 GB per hour per mailbox^4^ | 2 GB per hour per mailbox^4^ |

Note

^1^If the search results are larger than 200 GB, consider using date ranges or other types of filters to decrease the total size of the search results.

^2^ The system resets this limit daily at 12:00 AM UTC.

^3^ The export process automatically splits search results larger than 10 GB into multiple PST files, even if you select the option to export results into a single PST.

^4^ If an export runs for seven days without completing, the system automatically cancels it. To prevent this issue, divide your export into smaller batches.

## Hold limits

Tip

For better performance, limit each case to no more than 1,000 searches, holds, or exports. To spread this activity across more cases, consider updates to your organization processes and workflows.

The following table lists the limits for holds associated with an eDiscovery case.

| Description of limit | eDiscovery feature support | Premium eDiscovery feature support |
| --- | --- | --- |
| Maximum number of hold policies for an organization. | 10,000 | 20,000 |
| Maximum number of hold policies within a single case | 100 | 200 |
| Maximum number of mailboxes expanded from a single distribution list when used as a hold data source.^1^ | 100 | 100 |
| Maximum number of mailboxes in a single case hold. This limit includes the combined total of user mailboxes, and the mailboxes associated with Microsoft 365 Groups, Microsoft Teams, and Viva Engage Groups. | 1,000 | 2,000 |
| Maximum number of policies applied to a specific location | 100 | 100 |
| Maximum number of sites in a single case hold. This limit includes the combined total of OneDrive sites, SharePoint sites, and the sites associated with Microsoft 365 Groups, Microsoft Teams, and Viva Engage Groups.^2^ | 1,000 | 2,000 |

Note

^1^ You can't add distribution lists with more than 100 members directly as a hold data source. Expand the distribution list membership (for example, in Outlook) and then use the [bulk import data sources](edisc-data-sources#bulk-import-data-sources-to-a-case) feature to import the individual user mailboxes as data sources for the hold. You can also split the distribution list into smaller groups of 100 or fewer members before adding them.

^2^ Higher premium limits (for example, 2,000 sites) apply only when the case has premium eDiscovery features enabled. Check that premium features are enabled in [case settings](edisc-settings-cases). Use separate hold policies for Exchange mailboxes and for SharePoint and OneDrive sites instead of combining them in one policy.

To view a list of more than 1,000 cases, holds, searches, or exports, use the corresponding Security & Compliance PowerShell cmdlet:

- [Get-ComplianceCase](/en-us/powershell/module/exchange/get-compliancecase)
- [Get-CaseHoldPolicy](/en-us/powershell/module/exchange/get-caseholdpolicy)
- [Get-ComplianceSearch](/en-us/powershell/module/exchange/get-compliancesearch)
- [Get-ComplianceSearchAction](/en-us/powershell/module/exchange/get-compliancesearchaction)

## Indexing limits

The following table lists the indexing limits in eDiscovery with premium feature support.

Tip

Want to try premium eDiscovery features? See the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Microsoft 365 Enterprise E5 licensing.

| Description of limit | Premium eDiscovery feature support |
| --- | --- |
| Maximum number of characters extracted from a single file.^1^ | 10 million |
| Maximum size of a single file.^1^ | 150 MB |
| Maximum depth of embedded items in a document.^1^ | 25 |
| Maximum size of files processed by Optical Character Recognition (OCR).^1^ | 24 MB |
| Maximum Advanced indexing throughput | 2 GB per hour |

Note

^1^ If an item exceeds a single file limit, the process returns an error.

## Indexing limits for email messages

The following table describes the indexing limits that might cause an email message to appear as an unindexed item or a partially indexed item in the results of a search.

| Indexing limit | Maximum value | Description |
| --- | --- | --- |
| Maximum attachment size ^1^ | 150 MB | The maximum size of an email attachment that the indexing service parses. The indexing service doesn't parse any attachment that's larger than this limit. It marks the message with the attachment as partially indexed. |
| Maximum number of attachments | 250 | The maximum number of files attached to an email message that the indexing service parses. If a message has more than 250 attachments, the indexing service parses and indexes the first 250 attachments. It marks the message as partially indexed because it didn't parse the extra attachments. |
| Maximum attachment depth | 30 | The maximum number of nested attachments that the indexing service parses. For example, if an email message has another message attached to it and the attached message has an attached Word document, the indexing service indexes the Word document and the attached message. This behavior continues for up to 30 nested attachments. |
| Maximum number of attached images | 0 | The parser skips an image that's attached to an email message and doesn't index it. |
| Maximum time spent parsing an item | 30 seconds | The indexing service spends a maximum of 30 seconds parsing an item for indexing. If the parsing time exceeds 30 seconds, the indexing service marks the item as partially indexed. |
| Maximum parser output | 2 million characters | The maximum amount of text output from the parser that's indexed. For example, if the parser extracted 8 million characters from a document, the indexing service indexes only the first 2 million characters. |
| Maximum annotation tokens | 2 million | When the indexing service indexes an email message, it annotates each word with different processing instructions that specify how to index that word. Each set of processing instructions is called an annotation token. To maintain the quality of service in Microsoft 365, there's a limit of 2 million annotation tokens for an email message. |
| Maximum body size in index | 67 million characters | The total number of characters in the body of an email message and all its attachments. When the indexing service indexes an email message, it concatenates all text in the body of the message and in all attachments into a single string. The maximum size of this string that is indexed is 67 million characters. |
| Maximum unique tokens in body | 1 million | Tokens result from extracting text from content, removing punctuation and spaces, and then dividing it into words (called tokens) that the indexing service stores in the index. For example, the phrase `"cat, mouse, bird, dog, dog"` contains five tokens, but only four of these are unique tokens. There's a limit of 1 million unique tokens per email message, which helps prevent the index from getting too large with random tokens. |

Note

^1^ Parsing is the process where the indexing service extracts text from the attachment, removes unnecessary characters like punctuation and spaces, and then divides the text into words (in a process called tokenization) that it stores in the index.

## Process limits

The following table lists the process limits in eDiscovery.

| Description of limit | eDiscovery feature support | Premium eDiscovery feature support |
| --- | --- | --- |
| Maximum number of concurrent processes in your organization. | 50 | 200 |
| Maximum number of concurrent processes a single user can start at one time. | 25 | 50 |
| Maximum number of concurrent tenant-wide processes (for example, tenant-wide searches) in your organization. | 5 | 50 |
| Maximum number of concurrent tenant-wide processes (for example, tenant-wide searches) that a single user can start at one time. | 5 | 25 |
| Maximum number of jobs per day in your organization. ^1^ | 500 | 1,000 |
| Maximum duration the process runs before it's canceled. | 7 days | 7 days |

Note

^1^This limit resets daily at 00:00 UTC.

## Purge limits

The following table lists the purge limits in eDiscovery.

| Description of limit | eDiscovery feature support | Premium eDiscovery feature support |
| --- | --- | --- |
| Items per location in Exchange | 10 | 100 |
| Items per location in Teams | N/A | 100 |
| Total locations per purge | 50,000 | 100,000 |

## Review set download limits

The following table lists the review set download limits in eDiscovery with premium feature support.

Tip

Want to try premium eDiscovery features? See the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Microsoft 365 Enterprise E5 licensing.

| Description of limit | Premium eDiscovery feature support |
| --- | --- |
| Total file size or maximum number of documents downloaded from a review set.^1^ | 3 MB or 50 documents |

Note

^1^ This limit applies to downloading selected documents from a review set. It doesn't apply to exported documents from a review set. For more information about exporting documents from a review set, see [Export items from a review set in eDiscovery](edisc-review-set-export).

## Review set export limits

The following table lists the limits when exporting documents from a review set in eDiscovery with premium feature support.

Tip

Want to try premium eDiscovery features? See the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Microsoft 365 Enterprise E5 licensing.

| Description of limit | Premium eDiscovery feature support |
| --- | --- |
| Maximum size of a single export. | 5 million documents or 500 GB, whichever is smaller. |

## Review set limits

The following table lists the review set limits in eDiscovery with premium feature support.

Tip

Want to try premium eDiscovery features? See the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Microsoft 365 Enterprise E5 licensing.

| Description of limit | Premium eDiscovery feature support |
| --- | --- |
| Maximum number of items displayed per page in a review set.^1^ | 1,000 |
| Add to review set processing | To optimize performance during the *Add to review set* process, the system allocates up to one minute to process each item. If processing isn't completed within one minute, the item might be added to the review set without fully extracting its child items.^2^ |

Note

^1^Use default or custom filters to adjust the displayed items in a review set as needed.

^2^Use the [items.csv process report](edisc-process-report-use#items-csv-report) to review any items that encountered this processing limit after the *Add to review set* process is completed.

## Search limits

The following table lists the search limits for Exchange mailboxes and SharePoint sites in eDiscovery with premium feature support.

| Description of limit | eDiscovery feature support | Premium eDiscovery feature support |
| --- | --- | --- |
| Maximum recommended number of locations specified for a single targeted search.^1^ | 1,000 | 1,000 |
| Maximum number of locations for a single tenant-wide search, export from search, or add to review set process (organization-wide "All people and groups" source).^1^ | 500,000 | 500,000 |
| Maximum number of Sensitive Information Types per search query.^2^ | 20 | 20 |
| Maximum number of participants per search query.^2^ | 25 | 50 |
| Maximum number of characters for a search query (including operators and conditions).^3, 5^ | 10,000 | 10,000 |
| Minimum number of alpha characters for prefix wildcards; for example, `one*` or `set*`. | 3 | 3 |
| Maximum variants returned when using prefix wildcard to search for an exact phrase or when using a prefix wildcard and the NEAR Boolean operator.^4^ | 10,000 | 10,000 |
| Maximum number of operators in a query.^5^ | 100 | 100 |
| Maximum number of keyword segments in a query for tenant wide search. ^6^ | 5 | 5 |
| Maximum number of keyword segments in a query for targeted search. ^6^ | 20 | 100 |

Note

^1^ The 1,000 location limit applies only to targeted searches you manually specify individual mailboxes or sites. It includes the combined total of user mailboxes, and the mailboxes associated with Microsoft 365 Groups, Microsoft Teams, and Viva Engage Groups. Tenant-wide processes that use the organization-wide "All people and groups" source support up to 500,000 locations and aren't subject to the 1,000 targeted search limit. The 500,000 tenant-wide location limit applies to tenant-wide search, tenant-wide export from search, and tenant-wide add to review set processes. ^2^ Including more than 20 Sensitive Information Types or 25 participants might result in search query timeouts. ^3^ When searching SharePoint and OneDrive locations, characters in the URLs of searched sites count against this limit. The total number of characters consists of:

- All characters in both the *Users* and *Filters* fields.
- All search permissions filters that apply to the user.
- The characters from any location properties in the search, including *ExchangeLocation*, *PublicFolderLocation*, *SharePointLocation*, *ExchangeLocationExclusion*, *PublicFolderLocationExclusion*, *SharePointLocationExclusion*, and *OneDriveLocationExclusion*. For example, including all SharePoint sites and OneDrive accounts in the search counts as six characters, as the word `ALL` appears for both the *SharePointLocation* and *OneDriveLocation* field.

^4^ For non-phrase queries (a keyword value that doesn't use double quotation marks) the system uses a special prefix index. This index tells the system that a word occurs in a document, but not where it occurs in the document. To do a phrase query (a keyword value with double quotation marks), the system needs to compare the position within the document for the words in the phrase. This comparison means that the system can't use the prefix index for phrase queries. In this case, the system internally expands the query with all possible words that the prefix expands to. For example, `time*` can expand to "time OR timer OR times OR timex OR time boxed OR ...". The limit of 10,000 is the maximum number of variants the word can expand to, not the number of documents matching the query. There's no upper limit for non-phrase terms. ^5^ A search query can include a maximum of 100 operators and up to 10,000 characters. An operator is Boolean operator such as AND, OR, or NEAR. The limit of operators and characters apply to the combined total of operator and characters in the user input search query and any search permission filters that are applied to the user running the search. As a result, users with multiple or complex permission filters, especially filters applied to the same users or groups, are more likely to reach this limit. To reduce the risk of exceeding the maximum number of operator, keep search permission filters to the minimum required to meet your organization’s business needs. For more information, see [Configure search permission filtering in eDiscovery](edisc-search-permission-filtering). ^6^ Keyword segment refers to each individual keyword or keyword phrase entered as a separate row in the Keyword condition of the condition builder. It doesn't refer to the number of words or characters within a keyword or phrase. Each keyword segment is executed as a separate search operation against the selected locations. As a result, using a large number of keyword segments can increase search duration or cause the search to time out or fail. If your scenario requires more keyword segments than supported in a single search, split the keywords across multiple searches and run them separately.

For more information about specific limits, see the following articles:

- [Exchange](/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json)
- [SharePoint](/en-us/sharepoint/search-limits?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json)

### Search sample limit

The search sample is a best effort and depends on the following factors. If you need essential data, see [export the data](edisc-search-export) or [add data to review set](edisc-search-add-to-review-set).

| Description of limit | Limit |
| --- | --- |
| Maximum item size for sample | 10 MB |
| Time spent per location during sampling | Less than 30 seconds |

### Export search and export as report limit

The following table lists limits for the **Export as report** and the **export search** results:

| Description of limit | Limit |
| --- | --- |
| Export items report only CSV report string field character limit | 255 |
| Exported results (items) | 500,000 |
| Exported results (locations) | 100,000 |
| Search export expiry | 14 days from creation |
| Total items | 1 million |
| Total locations | 500,000 |

## Search times

Microsoft collects performance information for searches run by all organizations. While the complexity of the search query can impact search times, the biggest factor that affects how long searches take is the number of mailboxes searched.

Although Microsoft doesn't provide a service level agreement for search times, the following table lists average search times for collection searches based on the number of mailboxes included in the search.

| Number of mailboxes | Average search time |
| --- | --- |
| 100 | 30 seconds |
| 1,000 | 45 seconds |
| 10,000 | 4 minutes |
| 25,000 | 10 minutes |
| 50,000 | 20 minutes |
| 100,000 | 25 minutes |

## Themes limits

The limits described in this section relate to manually defining the maximum number of themes in settings for a case in eDiscovery with premium feature support.

Tip

Want to try premium eDiscovery features? See the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Microsoft 365 Enterprise E5 licensing.

| Description of limit | Premium eDiscovery feature support |
| --- | --- |
| Minimum number for the maximum number of defined themes. | 3 |
| Maximum number of defined themes. | 10,000 |

## Viewer limits

| Description of limit | Limit |
| --- | --- |
| Maximum size of an Excel file you can view in the native viewer. | 4 MB |

## Tenant region or environment change limits

The same Microsoft 365 region and service environment store eDiscovery case data (cases, searches, holds, review sets, and exports) where you originally created it. This data doesn't move with your tenant if you later relocate the tenant to a different region or to a different service environment.

Important

If you move your Microsoft 365 tenant between regions (for example, through [Advanced Data Residency](/en-us/microsoft-365/enterprise/advanced-data-residency)), or migrate it across service environments (for example, from Microsoft 365 commercial to a Microsoft 365 Government environment such as GCC, GCC High, or DoD), you can't access eDiscovery cases and their associated data that you created **before** the move from the destination tenant. Cases created **after** the move work normally in the new location.

There's no in-place migration path for eDiscovery case data across regions or service environments. To avoid losing access to in-flight investigations, complete the following actions before the move:

- Complete or close any active investigations where possible.
- [Export](edisc-search-export) the results of any searches you want to retain.
- [Export](edisc-review-set-export) any review sets you want to retain.
- Document the membership of any case holds you need to recreate in the destination tenant.

After the move, recreate the holds, searches, and cases you still need in the destination tenant.