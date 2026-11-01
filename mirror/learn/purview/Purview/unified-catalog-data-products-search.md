---
layout: Conceptual
title: Search for Data Products in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-products-search
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-05-21T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
ai-usage: ai-assisted
description: Learn how to search for data products and view data assets in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 60aa2fe0-a0b7-90f0-bba9-d96046ce3e8e
document_version_independent_id: 60aa2fe0-a0b7-90f0-bba9-d96046ce3e8e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-products-search.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-products-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-products-search.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 381cdd53-6f66-25e2-3a00-4bce39d781a5
---

# Search for Data Products in Unified Catalog | Microsoft Learn

This article outlines how to search and browse Microsoft Purview Unified Catalog to find data products.

## Prerequisites

To search for data products, you need a [Catalog Reader role](data-governance-roles-permissions#unified-catalog-roles).

## How to search

You can search for data products by using keywords or natural language (preview). To find data products that best fit your business needs, use **Search with natural language (preview)**. Searching with natural language supports data products created in English, French, and Spanish languages, and search terms in the corresponding languages.

The data product search is based on these attributes:

- Data product name, description, and business use.
- Name and description of associated governance domain, glossary terms, CDEs, and OKRs.
- Name and description of contained data assets.

To search for data products in Unified Catalog, select **Discovery**, then select **Data products**.

In the search bar, search by keywords, partial keywords, or natural language search:

- **Partial keyword match**: Enter a partial keyword, and the search returns results that match the partial term. For example, entering *cust* returns results that match *customer*.
- **Exact match with double quotes**: Use double quotes to search for an exact phrase. For example, *"customer profile"* searches for the phrase as a single unit, rather than matching *customer* and *profile* separately.
- **Natural language (preview)**: Select the magnifying glass icon at the end of the search bar, then enter a description of the data you need to find, then press **Enter**. Examples:

    - *I need three years of North American revenue data from finance department to analyze sales trends.*
    - *Find certified master data for customer accounts, which includes customer ID, name, and address.*
    - *I'm working on improving customer satisfaction. Show me Power BI reports of customer rating and feedback.*

A list of search results appears. Select a data product to view its details page. Hover over a search result to see why it was returned. The highlight shows which attributes matched your search query, such as name, description, or term.

You can filter search results by governance domain, data product type, owner, glossary terms, or critical data elements.

Note

Search isn't case sensitive, but spaces within search terms matter. Underscores and other non-space characters are treated as part of the keyword.

## Explore data products by governance domain

You can browse data products in Unified Catalog by governance domain.

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), go to **Discovery** &gt; **Data products**.
2. Select a governed domain under **Explore data products by governance domain**, or select **Explore all** to navigate to a governance domain.
3. When you select a governance domain, a list of its data products appears. Select a data product name from the list to view that product's details page.

## Explore data products by filtering on custom attributes

When you explore data products by governance domains, you can filter your view by [business concept attributes](unified-catalog-attributes-business-concept).

1. In Unified Catalog, go to **Discovery** &gt; **Data products**.
2. Select **Explore all**. You arrive at the **Explore data products by governance domain** page.
3. Select **Add filter**.
4. At **Filter**, select an attribute name from the dropdown list.
5. At **Operator**, select a condition, such as **Equals** or **Starts with**, which varies based on the kinds of values allowed by the attribute.
6. At **Value**, enter your value.
7. Select **Apply**.

## View data product details

A data product details page contains a description, use case, terms of use, and contacts. The page lists the glossary terms, critical data elements (CDE), and data assets that are associated to the data product. Select an asset, term, or CDE to display a flyout with a **View details** button for further details.

## View data asset details

Select a data asset from the data product details page to view a flyout pane with more information. Select **View details** on the flyout pane to open the details page for the data asset.

The data asset details page includes a description and owner, lists the data asset columns, and displays lineage information. The page also lists other data products that contain the data asset.