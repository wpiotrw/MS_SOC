---
layout: Conceptual
title: CJK/Double Byte support for eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-cjk-support
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how Microsoft Purview eDiscovery (Premium) in Microsoft 365 supports Chinese, Japanese, and Korean (CJK) languages, which use a double-byte character set.
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
document_id: 838a8f74-01bf-1738-d6db-28205b63f19f
document_version_independent_id: 838a8f74-01bf-1738-d6db-28205b63f19f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-cjk-support.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-cjk-support
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-cjk-support.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 336ebff3-80ff-6c5e-1278-3a3078db0734
---

# CJK/Double Byte support for eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Microsoft Purview eDiscovery (Premium) supports double-byte character set languages (these include Simplified Chinese, Traditional Chinese, Japanese, and Korean, which are collectively known as *CJK* languages) for the following advanced scenarios in a review set:

- When you [query the data in a review set](ediscovery-review-set-search).
- When you [tag documents in a review set](ediscovery-tagging-documents).
- When you [analyze case data in a review set](ediscovery-analyzing-data-in-review-set) by using near duplicate detection, email threading, and themes analytics.

## Frequently asked questions

**How do I create a search to collect items that contains CJK characters?**

You can use CJK characters for [keyword searches](ediscovery-building-search-queries#keyword-searches), [keyword queries and search conditions](ediscovery-keyword-queries-and-search-conditions) when searching for content in eDiscovery (Premium). Searching for CJK characters is also supported when searching for content in Microsoft Purview eDiscovery (Standard) and Content Search.

We provide CJK support for all [search operators](ediscovery-keyword-queries-and-search-conditions#search-operators) and [search conditions](ediscovery-keyword-queries-and-search-conditions#search-conditions), including the boolean operators **AND**, **OR**, **NOT**, and **NEAR**.

If you're certain that content locations or items contain CJK characters, but searches aren't returning any results, select the query language-country/region icon ![Query language-country/region icon in Content search.](media/8d4b60c8-e1f1-40f9-88ae-ee2a7eca0886.png) and select the corresponding language-country/region culture code value for the search. The default language/region is neutral.

**Can I search for multiple languages at once?**

It depends on your search scenario.

- When you [query data in a review set](ediscovery-review-set-search) in eDiscovery (Premium), you can search for multiple languages.
- When you [create a search to collect data](ediscovery-create-draft-collection), create separate collections for each language you're targeting. For example, if you are searching for a document that contains both Chinese and Korean, select Chinese for your first collection and select Korean for your second collection.

**I don't see the query language-country/region icon to select a language for queries in a review set. How can I specify a query language in a review set search?**

For review set queries, you don't need to specify a document language. eDiscovery (Premium) automatically detects document languages when you add content to a review set. This helps you optimize your query results in a review set.

**Can I see detected languages in [file metadata](ediscovery-view-documents-in-review-set#metadata-view)?**

No, you can't see detected languages in file metadata.

**Can I filter by document languages in a review set**?

No, you can't filter, sort, or search by document languages in a review set.

**Will this CJK release for review set scenarios affect any of my existing searches and review sets?**

No, none of your existing searches and review sets will change. You don't need to reindex existing data, and search results for English text will be the same.

**How do I change my display language to Chinese, Japanese, or Korean?**

For information about how to change display language and time zone, see [How to set language and region settings for Office 365](/en-us/office365/troubleshoot/access-management/set-language-and-region).

## Limits

- OCR doesn't support CJK characters from image files
- Email files (such as \*.eml and \*.msg) in [Annotate view](ediscovery-view-documents-in-review-set#annotate-view) aren't supported for CJK languages.
- Search hit highlighting in [Text view](ediscovery-view-documents-in-review-set#plain-text-view) isn't supported for CJK languages.
- The [Relevance module](ediscovery-predictive-coding-overview) used to analyze data doesn't support CJK languages.
- [Query-based holds](ediscovery-managing-holds#view-noncustodial-holds) aren't supported for CJK languages.