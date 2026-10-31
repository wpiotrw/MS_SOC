---
layout: Conceptual
title: Asset management in the Microsoft Purview Data Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/classic-catalog-asset-details
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: View relevant information and take action on assets in the Microsoft Purview Data Catalog.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2025-02-24T00:00:00.0000000Z
locale: en-us
document_id: 9de80a66-0a03-0b0f-da66-a3215ce618da
document_version_independent_id: 9de80a66-0a03-0b0f-da66-a3215ce618da
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/classic-catalog-asset-details.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/classic-catalog-asset-details
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/classic-catalog-asset-details.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: 911f6807-2035-856e-42b0-02260524b7a3
---

# Asset management in the Microsoft Purview Data Catalog | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This article discusses how assets are displayed in the Microsoft Purview Data Catalog, and all the features and details available to them. It describes how you can view relevant information or take action on assets in your catalog.

## Prerequisites

- Set up your data sources and scan the assets into your catalog.
- *Or* Use the Microsoft Purview Atlas APIs to ingest assets into the catalog.

## Discover assets

You can discover your assets in the Microsoft Purview Data Catalog by either:

- [Browsing the data catalog](../unified-catalog-data-assets-search#browse-the-unified-catalog)
- [Searching the data catalog](../unified-catalog-data-assets-search)

Once you've discovered an asset, select it to view the asset details page, which contains all the asset details, and more actions you can take.

## Edit assets

To edit an asset, other than adding a rating, you will need the [data curator](../data-gov-classic-permissions) role on the collection where the asset is housed.

To edit assets you can either:

- Select multiple assets in the catalog to [bulk edit assets](../how-to-bulk-edit-assets)
- Select a single asset and select the **Edit** button at the top of the asset details page

![Screenshot of the edit asset window in the Microsoft Purview Data Catalog.](../media/catalog-asset-details/edit-asset.png)

When you're editing an asset you can manage nearly all its information including:

- Overview: Manually update name, description, classification, and glossary terms.
- Schema: Manually update column name, classification, glossary terms, data types, and description.
- Lineage: Manually add lineage connections to other resources.
- Contacts: Add experts and owners users can contact for more information on this resource.

#### Scan behavior after editing assets

Microsoft Purview works to reflect the truth of the source system whenever possible. For example, if you edit a column and later it's deleted from the source table. A scan will remove the column metadata from the asset in Microsoft Purview.

Both column-level and asset-level updates such as adding a description, glossary term or classification don't impact scan updates. Scans will update new columns and classifications regardless if these changes are made.

## Delete asset

If you're a data curator on the collection containing an asset, you can delete an asset by selecting the delete icon under the name of the asset.

Important

Deleting the asset using the delete button will also delete all the child assets under the hierarchy. For example, if you attempt to delete a storage account asset in your catalog, all the assets under it - containers, folders and files - will also be deleted together.

Any asset you delete using the delete button is permanently deleted in Microsoft Purview. However, if you run a **full scan** on the source from which the asset was ingested into the catalog, then the asset is reingested and you can discover it using the Microsoft Purview Data Catalog.

When you run an incremental scan on the source, the **deleted asset won't get re-ingested** into the catalog unless the asset is modified by an end user since the previous run of the scan. For example, say you manually delete a SQL table from the Microsoft Purview Data Map. Later, a data engineer adds a new column to the source table. When Microsoft Purview scans the database, the table will be reingested into the data map and be discoverable in the data catalog.

## Asset details page

At the top of the asset details page there are several tabs:

![Asset details tabs](../media/catalog-asset-details/asset-tabs.png)

- **Overview** - An asset's basic details like description, classification, hierarchy, and glossary terms.
- **Properties** - The technical metadata and relationships discovered in the data source.
- **Schema** - The schema of the asset including column names, data types, column level classifications, terms, and descriptions are represented in the schema tab.
- **Lineage** - This tab contains lineage graph details for assets where it's available.
- **Contacts** - Every asset can have an assigned owner and expert that can be viewed and managed from the contacts tab.
- **Related** - This tab lets you navigate through the technical hierarchy of assets that are related to the current asset you're viewing.

Tip

You can information on all these tabs by editing the asset.

## Asset overview

The overview section of the asset details gives a summarized view of an asset. The sections that follow explains the different parts of the overview page.

![Screenshot that shows the asset details overview page.](../media/catalog-asset-details/asset-detail-overview.png)

### Asset description

An asset description gives a synopsis of what the asset represents. You can add or update an asset description by editing the asset.

#### Adding rich text to a description

Microsoft Purview enables users to add rich formatting to asset descriptions such as adding bolding, underlining, or italicizing text. Users can also create tables, bulleted lists, or hyperlinks to external resources.

![Screenshot that shows the rich text editor.](../media/catalog-asset-details/rich-text-editor.png)

Below are the rich text formatting options:

| Name | Description | Shortcut key |
| --- | --- | --- |
| Bold | Make your text bold. Adding the '\*' character around text will also bold it. | Ctrl+B |
| Italic | Italicize your text. Adding the '\_' character around text will also italicize it. | Ctrl+I |
| Underline | Underline your text. | Ctrl+U |
| Bullets | Create a bulleted list. Adding the '-' character before text will also create a bulleted list. |  |
| Numbering | Create a numbered list Adding the '1' character before text will also create a bulleted list. |  |
| Heading | Add a formatted heading |  |
| Font size | Change the size of your text. The default size is 12. |  |
| Decrease indent | Move your paragraph closer to the margin. |  |
| Increase indent | Move your paragraph farther away from the margin. |  |
| Add hyperlink | Create a link in your document for quick access to web pages and files. |  |
| Remove hyperlink | Change a link to plain text. |  |
| Quote | Add quote text |  |
| Add table | Add a table to your content. |  |
| Edit table | Insert or delete a column or row from a table |  |
| Clear formatting | Remove all formatting from a selection of text, leaving only the normal, unformatted text. |  |
| Undo | Undo changes you made to the content. | Ctrl+Z |
| Redo | Redo changes you made to the content. | Ctrl+Y |

Note

Updating a description with the rich text editor updates the `userDescription` field of an entity. If you have already added an asset description before the release of this feature, that description is stored in the `description` field. When overwriting a plain text description with rich text, the entity model will persist both `userDescription` and `description`. The asset details overview page will only show `userDescription`. The `description` field can't be edited in the Microsoft Purview studio user experience.

### Classifications

Classifications identify the kind of data being represented by an asset or column such as "ABA routing number", "Email Address", or "U.S. Passport number". These attributes can be assigned during scans or added manually. For a full list of classifications, see the [supported classifications in Data Map](../data-map-classification-supported-list). You can see classifications assigned both to the asset and columns in the schema from the overview page.which you can also view as part of the schema.

### Glossary terms

Glossary terms are a managed vocabulary for business terms that can be used to categorize and relate assets across your organization. For more information, see the [business glossary page](../concept-business-glossary). You can view the assigned glossary terms for an asset in the overview section. If you're a data curator on the asset, you can add or remove a glossary term on an asset by editing the asset.

### Collection hierarchy

In Microsoft Purview, collections organize assets and data sources. They also manage access across the Microsoft Purview governance portal. You can view an assets containing collection under the **Collection path** section.

### Asset hierarchy

You can view the full asset hierarchy within the overview tab. As an example: if you navigate to a SQL table, then you can see the schema, database, and the server the table belongs to.

## Asset actions

Below are a list of actions you can take from an asset details page. Actions available to you vary depending on your permissions and the type of asset you're looking at. Available actions are generally available on the global actions bar.

![Screenshot that shows actions available on the asset details page.](../media/catalog-asset-details/asset-details-actions.png)

### Request access to data

If a [self-service data access workflow](../how-to-workflow-self-service-data-access-hybrid) has been created, you can request access to a desired asset directly from the asset details page! To learn more about Microsoft Purview's data policy applications, see [how to enable data policy enforcement](../how-to-enable-data-policy-enforcement).

### Open in Power BI

Microsoft Purview makes it easy to work with useful data you find the data catalog. You can open certain assets in Power BI Desktop from the asset details page. Power BI Desktop integration is supported for the following sources.

- Azure Blob Storage
- Azure Cosmos DB
- Azure Data Lake Storage Gen2
- Azure Dedicated SQL pool (formerly SQL DW)
- Azure SQL Database
- Azure SQL Managed Instance
- Azure Synapse Analytics
- Azure Database for MySQL
- Azure Database for PostgreSQL
- Oracle DB
- SQL Server
- Teradata

## Ratings

Assets can be rated by all users with read access, or better, to that asset in Microsoft Purview. Ratings allow users to give an asset a rating from 1 to 5 stars, and leave a comment about the asset.

These ratings can be seen by all users with read access, and rating can be [added as a filter](../unified-catalog-data-assets-search#filter-results) when [searching the data catalog](../unified-catalog-data-assets-search) so users can find assets with a certain rating.

### View ratings

1. [Search](../unified-catalog-data-assets-search) or [browse](../unified-catalog-data-assets-search#browse-the-unified-catalog) for your asset in Microsoft Purview and select it.
2. In the header of the asset you can see a rating, which will show an aggregate star rating of the asset, and the number of reviews. ![Screenshot of a rating in the header of an asset.](../media/catalog-asset-details/view-rating-aggregate.png)
3. To see a percentage breakdown of the ratings, select the rating.
4. To see specific ratings and their comments, or to add your own rating, select **Open ratings**. ![Screenshot of a selected rating in the header of an asset showing the percentage breakdown.](../media/catalog-asset-details/open-rating-details.png)

### Add a rating to an asset

1. [Search](../unified-catalog-data-assets-search) or [browse](../unified-catalog-data-assets-search#browse-the-unified-catalog) for your asset in Microsoft Purview and select it.
2. Select the ratings button in the asset's header.
3. Select the **Open ratings** button. ![Screenshot that shows the ratings button selected, and the open ratings button highlighted.](../media/catalog-asset-details/open-ratings.png)
4. Choose a star rating, add a comment, and select **Submit**. ![Screenshot of a rating, showing five start selected and a comment about the quality of the data.](../media/catalog-asset-details/rate-asset.png)

### Edit or delete your rating

1. Select the ratings button in the asset's header.
2. Select the **Open ratings** button.
3. Under **My rating** select the ellipsis button in your rating. ![Screenshot of the user's rating, shown under the My rating menu, with the ellipsis button selected.](../media/catalog-asset-details/edit-rating.png)
4. To delete your rating, select **Delete rating**.
5. To edit your rating, select **Edit rating**, then update your score and comment and select **Submit**.

## Tags

Asset can be tagged by users with data curator permissions or better, and any users with reader permissions on these assets in Microsoft Purview can see these tags. Users can add tags [as a filter](../unified-catalog-data-assets-search#filter-results) when [searching the data catalog](../unified-catalog-data-assets-search), so users can see all assets with certain tags.

Note

Tag limitations:

- An asset can only have up to 50 tags
- Tags can only be 50 characters
- Allowed characters: numbers, letters, -, and \_

Use tags when you want to quickly label your data assets without the need for consistency or control. Tags are simple keywords or phrases that can be applied to data assets to provide informal metadata. They’re useful for categorizing data assets, making them easier to discover and understand. They're also a great way to see how your data consumers describe your data so you can incorporate this language into your business glossary over time.

In the following example, a few assets with Q4 Revenue so users can easily find the data assets to use for a new report with this information. Searching the keyword returns all data with that tag applied:

![Screen shot showing Microsoft Purview search results showing assets tagged with Q4_Revenue.](../media/concept-annotations/01-tag.png)

### Add a tag to an asset

If you have [data curator](../data-gov-classic-permissions) permissions Microsoft Purview, you can add a tag to an asset by:

1. [Search](../unified-catalog-data-assets-search) or [browse](../unified-catalog-data-assets-search#browse-the-unified-catalog) for your asset in Microsoft Purview and select it.
2. Select the **+ Add Tag** button under the asset's name. ![Screenshot that shows the new tag button highlighted on an asset detail page.](../media/catalog-asset-details/add-new-tag.png)
3. Select an existing available tag, or input a new tag.

### Remove a tag from an asset

If you have [data curator](../data-gov-classic-permissions) permissions Microsoft Purview, you can remove a tag from an asset by:

1. [Search](../unified-catalog-data-assets-search) or [browse](../unified-catalog-data-assets-search#browse-the-unified-catalog) for your asset in Microsoft Purview and select it.
2. Select the **X** button next to an existing tag under the asset's name. ![Screenshot that shows the remove tag button highlighted next to an existing page.](../media/catalog-asset-details/remove-tag.png)
3. Confirm the removal of the tag.

## Duplicate assets

If you notice duplicate assets in your Microsoft Purview Data Catalog, review the [asset normalization](../data-gov-classic-asset-normalization) documentation. Microsoft Purview normalizes assets to prevent duplication, but not all possible scenarios are covered.

Compare the fully qualified asset names for duplicate assets, and update ingestion points to resolve capitalization or character differences. Then, delete the duplicated asset in your catalog.