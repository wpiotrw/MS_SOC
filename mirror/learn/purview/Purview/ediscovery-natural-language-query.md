---
layout: Conceptual
title: Use the Natural Language Query builder to create search queries (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-natural-language-query
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the Natural Language Query builder to narrow the scope of the search when searching for data using eDiscovery (Premium) in Microsoft Purview.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
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
document_id: d24fe152-bec8-f142-8337-c1e1cfbb29b0
document_version_independent_id: d24fe152-bec8-f142-8337-c1e1cfbb29b0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-natural-language-query.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-natural-language-query
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-natural-language-query.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b42fc5d9-27fd-ed13-1a41-ccd03afb3511
---

# Use the Natural Language Query builder to create search queries (preview) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

The Natural Language Query (preview) builder option in collection search tool allows you to use natural language and [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot) to quickly generate a Keyword Query Language (KeyQL) statement when you build search queries in Microsoft Purview eDiscovery (Premium).

Use the Natural Language Query (preview) builder to construct complex queries with additional functionality, including AND, OR, and grouping of conditions, all while using natural language prompts. This feature helps you build queries more easily using predefined prompts for example scenarios and allows you to refine and enhance custom prompts for more accurate search queries.

## Prerequisites to use the Natural Language Query (preview) builder

You must have Microsoft Security Copilot to use the Natural Language Query (preview) builder. For Security Copilot guidance, see the following:

- [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview)
- [Get started with Microsoft Security Copilot](/en-us/copilot/security/get-started-security-copilot)

Microsoft Purview eDiscovery capabilities are included with Microsoft Purview. For more information, see [Subscriptions and licensing](ediscovery-overview#subscriptions-and-licensing).

For information about permissions you need to use the Natural Language Query (preview) builder, see [Understand authentication in Microsoft Security Copilot](/en-us/copilot/security/authentication).

## Displaying the Natural Language Query (preview) builder

When you create or edit an eDiscovery search for a collection in eDiscovery (Premium), the option to display and use the Natural Language Query builder is located on the **Search query** page in the collections workflow. Select **Natural Language Query** to display and use the query builder.

## Using the Natural Language Query (preview) builder

After you've selected data sources for a search query, you can create a customized KeyQL search query from a natural language prompt using Security Copilot. You can also choose to use prompt suggestions as a starting point to create and refine KeyQL queries for common or custom search scenarios.

After you've selected data sources for a search query, you can create a customized KeyQL search query from a natural language prompt using Microsoft Security Copilot. You can also choose to use prompt suggestions as a starting point to create and refine KeyQL queries for common or custom search scenarios.

1. In the **Natural language prompt**pane, choose one of the following options:
    - Enter your search query question. You can include user, data source, and other content details as applicable.
    - Select **View prompts**to select one of the following prompt suggestions:
        - *Find all emails containing the words budget and finance and have attachments*
        - *Search all chats in the month of January 2020 that contain the word 'financial year'*
        - *Search for files of type .docx that contain the words confidential and budget*
2. Review the natural language prompt. To refine the prompt with Copilot, select **Refine**.
3. When the prompt is finalized, select **Generate KeyQL**.
4. Review the KeyQL query in the **Keyword Query Language (KeyQL) result** pane. If you need to refine the KeyQL query results, you can update the prompt in the **Natural language prompt** pane and select **Generate KeyQL** again. 1. When the KeyQL results are finalized, select **Copy KeyQL**.
5. Paste the KeyQL results in the query field on the **Keyword query language (KeyQL)** tab. You can close **Draft a query with Copilot**.
6. Select **Next**.
7. On the **Review your collection** page, you can review and update the collection selection, data sources, and conditions that you configured on the previous pages. Select **Edit** for any of the selections and update if needed.
8. Select **Submit** to create the collection estimate. A page is displayed confirming that the collection was created.