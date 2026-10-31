---
layout: Conceptual
title: Manage data sources in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-data-sources-register-manage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-05-16T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to register new data sources, manage collections of data sources, and view sources in Microsoft Purview Data Map.
locale: en-us
document_id: 455067d6-e68c-1faa-225c-571f093febe6
document_version_independent_id: 455067d6-e68c-1faa-225c-571f093febe6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-data-sources-register-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-data-sources-register-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-data-sources-register-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: dfcc2d94-ac9d-6c88-a5c0-833cb20e9a18
---

# Manage data sources in Microsoft Purview Data Map | Microsoft Learn

In this article, you learn how to register new data sources, manage domains and collections of data sources, view sources, and move sources between collections in the Microsoft Purview Data Map.

## Register a new source

Note

To register and manage a source in Data Map, you need to be a Data Source Admin and have one of the other Data Map roles, such as Data Reader. For more information, see [assigning data governance roles and permissions](data-governance-roles-permissions).

Use the following steps to register a new source:

1. In the Microsoft Purview portal, navigate to **Data Map**, **Data sources**, and select **Register**.

    ![Screenshot of the classic Microsoft Purview governance portal.](media/manage-data-sources/purview-studio.png)
2. If you're using the classic experience, open the classic [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), go to **Data Map**, **Sources**, and select **Register**.
3. Select a source type. This example uses Azure Blob Storage. Select **Continue**.

    ![Screenshot showing selecting a data source type in the Register sources page.](media/manage-data-sources/select-source-type.png)
4. Fill out the form on the **Register sources** page. Select a name for your source and enter the relevant information. If you choose **From Azure subscription** as your account selection method, the sources in your subscription appear in a dropdown list.
5. Select **Register**.

Important

Most data sources have prerequisites to register and scan them in Microsoft Purview. For a list of all available sources, and links to source-specific instructions to register and scan, see [Data sources that connect to Data Map](data-map-data-sources).

## View sources

You can view all registered sources by going to the Microsoft Purview portal &gt; **Data Map** &gt; **Data sources**.

There are two view types:

- The map view
- The table view

### Map view

To find the map view, open Data Map and select **Data sources**. Make sure the toggle at the top of the page is set to **Map view**.

In **Map view**, you see all of your sources and collections, and you can filter by sources, domains, and collections. In the following screenshot, you see the default domain at the top called PDG. It has three collections: test, collection01, and xDM Assets. The collection xDM Assets has a PostgreSQL source registered to it. An Azure resource group source is also housed under the root domain.

[![Screenshot of the Microsoft Purview data source map view.](media/manage-data-sources/map-view-inline.png)](media/manage-data-sources/map-view-expanded.png#lightbox)

You can open and manage each of the subcollections from the map view by selecting the **+** button. You can also register a new source by selecting the register source button, or view details by selecting **View details**.

![Screenshot the map view showing the Root collection and the finance subcollection with its resource and subcollections expanded.](media/manage-data-sources/collection-options.png)

### Table view

In the table view, you see a sortable list of sources. Hover over the source for options to edit, begin a new scan, or delete.

[![Screenshot of the Microsoft Purview data source list view.](media/manage-data-sources/list-view.png)](media/manage-data-sources/list-view.png#lightbox)

## Manage collections and domains

To manage collections and domains, and assign permissions based on your collections and domains, see [Create and manage collections and domains](data-map-domains-collections-manage).

## Move sources between collections

After you register your source, you can move it to another collection that you have access to within the same domain.

Important

Data source connections that register multiple sources can't be moved between collections:

- Azure (Multiple)
- AWS account (Multiple)
- Azure Synapse Analytics (Multiple)

1. Find your source in Data Map and select it.
2. Beside the **Collection Path** list, select the ellipsis (...) button and select **Move**.

    ![Screenshot of a source, with the ellipsis and move buttons highlighted.](media/manage-data-sources/choose-to-move.png)
3. In the **Move collection** menu that appears, select your collection from the drop-down and then select **Ok**.

    ![Screenshot of the Move collection window, showing the drop-down selection of collections.](media/manage-data-sources/select-collection.png)
4. Your data source has been moved. It can take up to an hour for results to be fully seen across your Microsoft Purview environment. Your scans will move with your resource, but assets will remain in their original collection until your next scan, then they'll move to the new collection.

Note

- When a source moves to a new collection, its scans move with it, but assets don't appear in the new collection until your next scan.
- If you manually moved any assets from your source to a different collection before migrating the source, the scan doesn't take them to the new collection. They remain in the collection you moved them to.