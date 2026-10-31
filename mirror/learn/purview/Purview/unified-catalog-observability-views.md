---
layout: Conceptual
title: Observability Views in Microsoft Purview Unified Catalog (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-observability-views
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2026-01-08T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about observability in lineage explorer in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 2008e55e-56e2-2c88-4e4e-bc20dd9fcfec
document_version_independent_id: 2008e55e-56e2-2c88-4e4e-bc20dd9fcfec
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-observability-views.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-observability-views
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-observability-views.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: dc450233-27a9-13e3-4be7-1ffcf12c470e
---

# Observability Views in Microsoft Purview Unified Catalog (preview) | Microsoft Learn

Data observability in Microsoft Purview Unified Catalog provides specific views focused on a business concept, such as a governance domain or data product, and the user who views that concept. Each view is scoped to a specific concept and provides alternate views in a dropdown menu to help give different perspectives of the data. You can also create your own view by using saved views in the data observability experience under **Health management**.

## Saved views

When you create a saved view, you create a diagram that you can reference later or share with others. After building a diagram by providing minimal details and deciding on sharability, you can reuse the same view at any time.

To create a saved view:

1. In Unified Catalog, go to **Health management** &gt; **Data observability**.
2. Create a diagram by searching, filtering, or selecting the items you want to focus on.
3. Select **Save this view** at the top right of the screen.
4. In the **Save view**window, provide details about the view:
    1. Enter a **View name**.
    2. Enter a **Description**.
    3. At **Owner**, you can add more users. Only the view owners can manage the view.
    4. Select **Visible to everyone** if you want other users to see the view.
5. Select **Save**.

To delete saved views:

1. In **Data observability**, select **Manage saved views** from the **Save this view** dropdown.
2. On the flyout pane, select the trash can icon next to the view you want to remove.
3. Select **OK**.

Known limitations:

- Only 25 shared views can exist at one time.
- Views aren't a point in time picture; they're based on what is in the most current snapshot for the view.
- Views are either personal or shared to all users of **Data observability**. Views don't impact the permissions the user has or what they can see in the catalog.
- You can't edit views. If you need to edit a view, start from the previous saved view, make the needed changes, create a new saved view, and delete the previous view.

## Governance domains data observability

At the highest level of business concepts, the [governance domain](unified-catalog-governance-domains) provides the structure and accountability for a portion of the data estate.

1. In Unified Catalog, under **Catalog management**, select **Governance domains**.
2. Select a governance domain that you have access to, then select the **Observability** tab.
3. Select a view from the **Current view**dropdown menu:
    1. **Data Products/Assets** displays all of the data products in the domain with all of the assets mapped to each product.
    2. **Data Products** displays only the data products of the domain.
    3. **Assets** displays only the assets that are mapped to data products of that domain.
    4. **Data Product Lineage** displays the inferred lineage between data products of that domain.
    5. **Data Asset Linage** displays the lineage between the assets used in the data products of the domain.
    6. **Data Assets with Data Quality issues** displays the assets that have at least one data quality dimension that isn't healthy.
    7. **Data Products with Data Quality issues** displays the data products that have at least one data quality dimension that isn't healthy.

## Data product data observability

For [data product](unified-catalog-data-products) owners, the **Observability** tab on a product's details page provides a quick view of everything within a single data product.

1. In Unified Catalog, select a data product by going to **Catalog management** &gt; **Data products**.
2. On the data product's details page, select the **Observability** tab.
3. Select a view from the **Current View** dropdown menu:

    1. **Assets** displays the assets contained within the data product.
    2. **Data Assets with Data Quality issues** displays the assets with data quality issues that are in the data product.

## Glossary term data observability

[Glossary terms](unified-catalog-glossary-terms) can link to data and give better context to where certain topics have data available in the governance domains across the data estate.

1. On the glossary term's page, select **Observability**.
2. The default view displays the glossary term and the connections to the data products from any domain using links to that glossary term.

## Data observability in Health management

To view your entire data estate in Unified Catalog, go to **Health management**, then select **Data observability (preview)** for a custom view of data observability. This view provides a view of the entire data estate by governance domain by default, called the **Data Estate** view.

Two other views let you focus on either data assets or data products with data quality issues. The difference is that you can search for specific assets, columns, or business concepts, then add them to the diagram or add them to the diagram with lineage. Adding anything with lineage to the diagram includes all of the lineage connections from end to end for that specific asset, column, or business concept.

Other functions available for custom view:

- **Undo**: Go back a change in the diagram to the previous view.
- **Redo**: Go forward a change in the diagram to the view before a user clicked undo.
- **Scope to selection**: Focus the diagram to the single item selected on the screen.
- **Show Lineage**: Include all related items that are connected to the focus item at the same level of grain. If you're focused on a column, the diagram includes the column level lineage. If you're focused on an asset, the diagram includes asset level lineage.
- **Show non-governed assets**: Include all assets included in the lineage of an item even if they're not included in the governed assets of any domain.
- **Save Screenshot**: Download a picture of the current view for use offline.
- **Hierarchy Filter**: Select which levels of hierarchy in the concepts are shown. The hierarchy filter enables you to include deeper level of details in any currently scoped view. If the diagram is focused on data products, the hierarchy can be set to include data assets. If it has data assets, the asset schema can be added.