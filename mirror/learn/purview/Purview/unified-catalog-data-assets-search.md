---
layout: Conceptual
title: Search for and Manage Data Assets in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-assets-search
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-10-13T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
description: Understand how to browse and search for data assets in Microsoft Purview Unified Catalog.
locale: en-us
document_id: dfa280b5-c9a2-889b-677e-cde210a1f505
document_version_independent_id: dfa280b5-c9a2-889b-677e-cde210a1f505
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-assets-search.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-assets-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-assets-search.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: cd30af3c-35df-7b94-8e4c-a38baab5ce96
---

# Search for and Manage Data Assets in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

After data is scanned and ingested into the Microsoft Purview Data Map, data consumers need to easily find the data they need for their analytics or governance workloads. Data discovery can be time consuming because you might not know where to find the data that you want. Even after finding the data, you might have doubts about whether you can trust the data and take a dependency on it.

This article outlines how to search Microsoft Purview Unified Catalog to quickly find the data you're looking for. You can search across all data assets, or focus on governed assets that have been curated with governance metadata such as glossary terms, data products, critical data elements, or data quality scores.

## Permissions to search the Unified Catalog

Searching Unified Catalog only returns relevant data assets that you have permissions to view.

You can find a data asset in Unified Catalog when:

- [You have at least read permissions on an available Azure or Microsoft Fabric resource](data-gov-live-view#what-resources-have-live-view-available).
- [You have at least data reader permissions on a domain or collection in the Microsoft Purview Data Map where the asset is stored](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Manage permissions to these assets at the resource level and at the Microsoft Purview Data Map level, respectively. For more information on providing this access, see the links above.

To search for curated, ready-to-use data assets, [search for data products your organization has developed](unified-catalog-data-products-search).

Tip

If your Unified Catalog is well-curated, day-to-day business users shouldn't need to search the full catalog. [They should be able to find data they need in data products](unified-catalog-data-products-search), or by using the governed assets search to find curated data. For more information about setting up Unified Catalog, see [Get started with data governance](data-governance-get-started), and [plan for Unified Catalog](unified-catalog-plan).

### Permissions to search governed assets

Governed assets are visible to users with the [Global Catalog Reader role](data-governance-roles-permissions#unified-catalog-roles). Local Catalog Readers can view governed assets in the governance domain they have access to. Published governance concepts, such as glossary terms, data products, and critical data elements, are also visible to catalog readers. Draft concepts are visible only to Data Product Owners and Data Stewards.

Existing Data Map reader and curator roles aren't changed by the governed assets search experience.

## Searching the catalog

To search for data assets in Unified Catalog:

1. In the [Microsoft Purview portal](https://purview.microsoft.com), open **Unified Catalog**.
2. Under **Discovery**, select **Data assets**.
3. In the search bar, enter keywords to narrow your search, such as name, data type, classifications, and glossary terms. Search suggestions appear as you enter keywords. Your search history is also presented so you can resume a previous data exploration.
4. To complete your search, select **View search results** or select **Enter**. For full search syntax information, see keyword search syntax.

The search results page shows a list of data assets and glossary terms that match the search terms. The keyword is highlighted in the return results, so you can see where the term was found in the asset. The **Governed assets** tab displays only governed assets search results, and the **All assets** tab displays the search results in all assets in your data estate, whether they're governed or not.

Note

Search only returns items in collections where you're a data reader or curator. For more information, see [roles and permissions in collections](data-map-domains-collections-manage#add-roles-and-restrict-access).

The Microsoft Purview relevance engine sorts through all the matches and ranks them based on what it believes is useful to a user. For example, a data consumer is likely more interested in a table curated by a data steward that matches on multiple keywords than an unannotated folder. Many factors determine an asset’s relevance score. The Microsoft Purview search team constantly tunes the relevance engine to ensure the top search results have value to you.

## Keywords and keyword search syntax

Search queries consist of keywords and operators such as `AND`, `OR`, `NOT`, exact phrase quotes, field-scoped search, and parentheses for grouping. You can combine these operators to build precise queries that return exactly the assets you need.

For the full list of supported operators, field names, and detailed syntax guidance, see [Keyword search syntax](unified-catalog-data-assets-search-syntax).

## Filter results

If the top results don’t include the assets you're looking for, you can filter your results by using the filter pane to the left of the search results.

On the search results page, select **Filter** to open and close the filter pane. With the filter pane open, select a filter category, then select the checkbox next to the values you want to filter on. For some filters, you can select the ellipsis to choose **Or** or **And**.

### Available filters

You can add filters by selecting **Add filter** on the filter pane and selecting one of the following options:

- **Activity**: Refine your search to attributes created or updated within a certain timeframe.
- **Asset type**: Refine your search to specified asset types. For example: dashboards, files, glossary terms, or metamodel assets.
- **Assigned term**: Refine your search to assets with the selected terms applied.
- **Classification**: Refine your search to assets with certain classifications.
- **Collection**: Refine your search by assets in a specific collection.
- **Contact**: Refine your search to assets that have selected users listed as a contact.
- **Data source type**: Refine your search to assets from specified source types. For example: Azure Blob Storage or Power BI.
- **Endorsement**: Refine your search to assets with specified endorsements, like **Certified** or **Promoted**.
- **Label**: Refine your search to assets with specific security labels.
- **Data asset attributes**: Refine your search to assets with specified [data asset attributes](unified-catalog-attributes-data-asset). Attributes are listed under their attribute group, and use operators to help search for specific values. For example: Equals or Doesn't equal.
- **Rating**: Refine your search to only data assets with a specified rating.
- **Tags**: Refine your search to assets with selected tags.

## Search for governed assets (preview)

The governed assets search provides a focused view of data assets that are actively governed in Unified Catalog. Instead of searching across all assets, you can search only for assets that have governance metadata, such as [glossary terms](unified-catalog-glossary-terms), [data products](unified-catalog-data-products), [critical data elements](unified-catalog-critical-data-elements), or [data quality](unified-catalog-data-quality) scores. Learn more about [governed assets](data-governance-billing#what-are-governed-assets-and-how-are-you-billed).

The governed assets search is helpful because organizations have large data estates but only a small percentage of assets are curated and ready for consumption. Data consumers can use this search to find meaningful, governed data without navigating the entire data estate.

To search for governed assets:

1. In the [Microsoft Purview portal](https://purview.microsoft.com), open **Unified Catalog**.
2. Under **Discovery**, select **Data assets**.
3. Enter keywords in the search bar and select **Enter** or **View search results**.
4. On the search results page, select the **Governed assets** tab.

The search results show only assets that are governed in Unified Catalog. Each asset has a **Governed** label next to its name. Governed assets search supports semantic search, so you can use natural language queries to find assets.

### Search capabilities

Governed assets search includes the following capabilities:

- **Partial keyword match**: Enter a partial keyword, and the search returns results that match the partial term. For example, entering *cust* returns results that match *customer*.
- **Exact match with double quotes**: Use double quotes to search for an exact phrase. For example, *"customer profile"* searches for the phrase as a single unit, rather than matching *customer* and *profile* separately.
- **Search highlights**: Hover over a search result to see why it was returned. The highlight shows which attributes matched your search query, such as name, description, or term.

Note

Search isn't case sensitive, but spaces within search terms matter. Underscores and other non-space characters are treated as part of the keyword.

### Filter governed asset results

You can filter governed asset search results by using the following filters (see filter definitions):

- Asset type
- Data source type
- Classification
- Contact
- Glossary term
- Data product
- Critical data element

Note

The **Terms** filter in governed assets search uses Unified Catalog terms. After you [migrate glossary terms and enable data asset curation](unified-catalog-glossary-terms-migrate), the **Assigned term** filter is no longer available in the all data assets search, and classic terms no longer appear on asset details pages.

### View governed asset details

Select a governed asset from the search results to view its details. On the asset details page, select the **Governance** tab to see how the asset is governed. The **Governance** tab shows:

- Data products the asset is part of.
- Glossary terms linked to the asset.
- Critical data elements associated with columns in the asset.
- The latest data quality score, if a data quality run was performed on the asset.

The **Governance** tab follows existing permission models. If you have a Catalog Reader role, you see only published governance concepts. Draft concepts, such as draft glossary terms, are visible only to Data Product Owners and Data Stewards.

If an asset is deleted from Data Map, a warning icon appears next to the asset in search results. The asset continues to appear until the Data Product Owner removes it.

Note

If an asset is ungoverned (all links to data products, glossary terms, and critical data elements are removed), the asset currently still appears in governed assets search results. You have to manually delete using the delete button that will be available to such assets. APIs can also be used to automate or scale.

If an asset is deleted in data map and still governed, you have to manually remove all links to data products, glossary terms, and critical data elements first.

## Bulk edit search results

If you want to make changes to multiple assets returned by search, you can modify glossary terms, classifications, and contacts in bulk. For more information, see [How to bulk edit assets](how-to-bulk-edit-assets).

## View assets

From the search results page, select an asset to view details, such as description, attributes, schema, lineage, and classifications.

## Browse the Unified Catalog

Unified Catalog offers a browse experience that enables users to explore what data is available to them either by collection or by exploring the hierarchy of each data source in the catalog.

In Unified Catalog, go to **Discovery** &gt; **Data assets**. Under **Explore your data**, select a card for how you want to explore your data: in Azure, in Microsoft Fabric, by source type, or by collection.

You can only see the data sources you have permission to view.

## Searching Microsoft Purview in connected services

After you register your Microsoft Purview instance to an Azure Data Factory or an Azure Synapse Analytics workspace, you can search Unified Catalog directly from those services. For more information, see [Discover data in ADF using Microsoft Purview](/en-us/azure/data-factory/how-to-discover-explore-purview-data) and [Discover data in Synapse using Microsoft Purview](/en-us/azure/synapse-analytics/catalog-and-governance/how-to-discover-connect-analyze-azure-purview).

## Link glossary terms to assets and columns (preview)

You can add business context to your data by linking [glossary terms](unified-catalog-glossary-terms-create-manage) to data assets and columns.

Users need two roles in order to attach terms to assets and columns:

1. **Data Curator**: All users need to hold this role in the collection where the asset belongs. Only Data Curators can edit data assets. Learn more about this [role and collections permissions in Data Map](data-governance-roles-permissions#data-map-permissions).
2. In addition, users need either one of these roles:

    1. **Data Steward**: Users can be a Data Steward in any governance domian. These users can see published and unpublished glossary terms, and can attach both kinds of terms to assets and columns.
    2. **Global Asset Curator**: This role allows users to attach published glossary terms to assets and columns. Users with this role can only see published terms and attach published terms to assets and columns.

See [Data governance roles and permissions](data-governance-roles-permissions) for role descriptions and how to assign roles.

### Link terms to a data asset:

1. Search for an asset or column in Unified Catalog.
2. Select the data asset to open its details page.
3. Select **Edit**.
4. On the **Overview** page, at **Glossary terms**, select **Add term**.
5. Search for a term by entering keywords, or select the checkbox next to a term listed on the page. You can select multiple terms.
6. Select **Add**.
7. Select **Save**.

The terms are attached to the asset.

### Link terms to a column within an asset:

1. Search for an asset or column in Unified Catalog.
2. Select the data asset to open its details page.
3. Select **Edit**.
4. On the **Schema** page, find the row for the column you want to add a term to, and select **Add term**.
5. Search for a term by entering keywords, or select the checkbox next to a term listed on the page. You can select multiple terms.
6. Select **Add**.
7. Select **Save**.

The terms are attached to the column.