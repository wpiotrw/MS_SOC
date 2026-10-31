---
layout: Conceptual
title: Build search queries for collections | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-building-search-queries
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use keywords and conditions to narrow the scope of the search when searching for data using eDiscovery (Premium) in Microsoft Purview.
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
ms.custom: seo-marvel-mar2020
locale: en-us
document_id: fd79a87b-86a8-9cb4-3a45-23cd9e35fcd8
document_version_independent_id: fd79a87b-86a8-9cb4-3a45-23cd9e35fcd8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-building-search-queries.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-building-search-queries
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-building-search-queries.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: dc0e6e15-64d7-3583-a44c-e31bcc911f6e
---

# Build search queries for collections | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When configuring the search query when creating a [collection](ediscovery-collections) in an eDiscovery (Premium) case, you can use keywords to find specific content and conditions to narrow the scope of the search to return items that are most relevant to your legal investigation.

If you prefer to build a search query with the Keyword Query Language (KeyQL) editor, Query builder, or the Natural Language Query tools, see:

- [Use the KeyQL editor to build search queries](ediscovery-kql-editor)
- [Use the query builder to build search queries](ediscovery-query-builder)
- [Use the Natural Language Query builder to build search queries (preview)](ediscovery-natural-language-query)

## Keyword searches

Type a keyword query in the **Keywords** box in the search query. You can specify keywords, email message properties, such as sent and received dates, or document properties, such as file names or the date that a document was last changed. You can use more complex queries that use a Boolean operator, such as **AND**, **OR**, **NOT**, and **NEAR**. You can also search for sensitive information (such as social security numbers) in documents in SharePoint and OneDrive (not in email messages), or search for documents that have been shared externally. If you leave the **Keywords** box empty, all content located in the specified content locations is in the search results.

## Keyword list

Alternatively, you can select the **Show keyword list** check box and the type a keyword or keyword phrase in each row. The keywords in each row are connected by a logical operator (which is represented as *c:s* in the search query syntax) that is similar in functionality to the **OR** operator in the search query that's created. This means items that contain any keyword in any row are in the search results. You can add up to 180 rows in the keyword list in eDiscovery (Premium) search queries.

Why use the keyword list? You can get statistics that show how many items match each keyword in the keyword list. This can help you quickly identify the keywords that are the most (and least) effective. You can also use a keyword phrase (surrounded by parentheses) in a row in the keywords list. For more information about search statistics, see [Collection statistics and reports](ediscovery-collection-statistics-reports)

## Conditions

You can add search conditions to narrow the scope of a search and return a more refined set of results by selecting **Add condition**.

Each condition adds a clause to the search query that is created and run when you start the search. A condition is logically connected to the keyword query specified in the keyword box by a logical operator (which is represented as *c:c* in the search query syntax) that is similar in functionality to the **AND** operator. That means items have to satisfy both the keyword query and one or more conditions to be included in the search results. This is how conditions help to narrow your results.

For a list and description of conditions that you can use in a search query, see the "Search conditions" section in [Keyword queries and search conditions](ediscovery-keyword-queries-and-search-conditions#search-conditions).