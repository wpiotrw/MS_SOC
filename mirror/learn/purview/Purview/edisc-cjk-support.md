---
layout: Conceptual
title: Double-byte character language support in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-cjk-support
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how eDiscovery supports a double-byte character set in Chinese, Japanese, and Korean (CJK) languages.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-29T00:00:00.0000000Z
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
document_id: 791fb145-53c3-914d-26a9-a6def1d21110
document_version_independent_id: 791fb145-53c3-914d-26a9-a6def1d21110
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-cjk-support.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-cjk-support
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-cjk-support.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: a7775466-2114-bdba-a675-d6bbb146f29b
---

# Double-byte character language support in eDiscovery | Microsoft Learn

eDiscovery supports double-byte character set languages (these include Simplified Chinese, Traditional Chinese, Japanese, and Korean, which are collectively known as *CJK* languages) for the following scenarios in a review set:

- When you [search for data](edisc-review-set-search).
- When you [tag documents](edisc-review-set-tagging).
- When you [analyze case data](edisc-review-set-analytics) using near duplicate detection, email threading, and themes analytics.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Limitations for CJK characters

The following features for CJK characters aren't currently supported in eDiscovery:

- Detecting CJK characters in file metadata.
- Filtering, sorting, or searching by document languages in a review set.
- Optical Character Recognition (OCR) for image files.
- Email files (such as \*.eml and \*.msg) in [Annotate view](edisc-review-set-view#use-annotate-view).
- Search hit highlighting in [Text view](edisc-review-set-view#use-plain-text-view).
- [Query-based holds](edisc-hold-manage) for cases.
- The [Relevance module](ediscovery-predictive-coding-overview) used to analyze data.

## Search for items containing CJK characters

You can use CJK characters when searching for content in eDiscovery. CJK characters are supported for all search operators and [search conditions](edisc-condition-builder), including the Boolean operators **AND**, **OR**, **NOT**, and **NEAR**.

If you're certain that content locations or items contain CJK characters, but searches don't return any results, select the query language-country/region icon ![Query language-country/region icon in eDiscovery.](media/8d4b60c8-e1f1-40f9-88ae-ee2a7eca0886.png) and select the corresponding language-country/region culture code value for the search. The default language/region is neutral.

When searching for phrases in CJK languages, break the phrase into individual words or characters and combine them using the AND operator. CJK phrases aren't natively recognized as single searchable units, so this approach helps to ensure more accurate search results. For example, instead of searching for `(SubjectTitle:Teamsのチャットメッセージ)`, use `(SubjectTitle:Teams) AND (SubjectTitle:の) AND (SubjectTitle:チャット) AND (SubjectTitle:メッセージ)`.

## Search multiple languages at the same time

How you search multiple languages at the same time depends on your search scenario.

- When you [query data in a review set](edisc-review-set-search) with premium eDiscovery features enabled, you can search for multiple languages. For review set queries, you don't need to specify a document language. eDiscovery automatically detects document languages when you add content to a review set. This detection helps you optimize your query results in a review set.
- When you [create a search to collect data](edisc-search-query), create separate searches for each language you're targeting. For example, if you're searching for a document that contains both Chinese and Korean, select Chinese for your first search and select Korean for your second search.

## Changing your display language to Chinese, Japanese, or Korean

For information about how to change display language and time zone, see [How to set language and region settings for Office 365](/en-us/office365/troubleshoot/access-management/set-language-and-region?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).