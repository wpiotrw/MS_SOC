---
layout: Conceptual
title: Classic Assets Report in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-assets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2024-04-07T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to view and use Microsoft Purview Data Estate Insights asset reporting on your data.
locale: en-us
document_id: a9c4c45e-a083-695b-48e4-d80e53bb4f5c
document_version_independent_id: a9c4c45e-a083-695b-48e4-d80e53bb4f5c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-reports-classic-assets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-reports-classic-assets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-reports-classic-assets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 19dab2ff-9f7c-7585-f8c3-d0cf0e0074c2
---

# Classic Assets Report in Unified Catalog | Microsoft Learn

This article describes how to access, view, and filter data asset insight reports for your data.

In this article, you learn how to:

- View data estate insights from your Microsoft Purview account.
- Get a bird's eye view of your data.
- Drill down for more asset count details.

## Prerequisites

Before getting started with Microsoft Purview Data Estate Insights, make sure that you've completed the following steps:

- Set up a storage resource and populated the account with data.
- Set up and completed a scan your storage source. For more information to create and complete a scan, see [Manage data sources in Microsoft Purview](data-map-data-sources-register-manage).
- Permissions depending on your current experience:
    - [If using the classic Microsoft Purview Catalog](use-microsoft-purview-governance-portal), you need the [data curator role or insight reader role](data-gov-classic-permissions#roles).
    - [If using the new Microsoft Purview Unified Catalog](unified-catalog), you need [data health reader](data-governance-roles-permissions#unified-catalog-permissions) permissions.

## Understand your asset inventory in Data Estate Insights

In Microsoft Purview Data Estate Insights, you can get an overview of the assets that you scanned into the Data Map. You can also view key gaps that governance stakeholders can close for better governance of the data estate.

1. Open the Microsoft Purview portal.
2. If you're using the [classic Microsoft Purview portal](use-microsoft-purview-governance-portal), select **Data estate insights**. If you're using the [new Microsoft Purview portal](purview-portal) open **Unified Catalog**, select **Health Management**, then select **Reports**.
3. Select the **Classic assets** report.
4. The **Assets Summary** report provides several high-level KPIs, with these graphs:

    - **Unclassified assets**: Assets with no system or custom classification on the entity or its columns.
    - **Unassigned data owner**: Assets that have the owner attribute within "Contacts" tab as blank.
    - **Net new assets in last 30 days**: Assets that you added to the Purview account, via data scan or Atlas API pushes.
    - **Deleted assets in last 30 days**: Assets that you deleted from the Purview account, as a result of deletion from data sources.

    [![Screenshot of the insights assets summary graphs, showing the four main KPI charts.](media/asset-insights/asset-insights-summary-report-small.png)](media/asset-insights/asset-insights-summary-report.png#lightbox)
5. Below these KPIs, you can also view your data asset distribution by collection.

    [![Screenshot of the insights assets by collection section, showing all a graphic that summarizes number of assets by collection.](media/asset-insights/assets-by-collection-small.png)](media/asset-insights/assets-by-collection.png#lightbox)
6. Using filters you can drill down to assets within a specific collection or classification category.

    ![Screenshot of the insights assets by collection section, with the filter at the top selected, showing available collections.](media/asset-insights/filter.png)

    Note

    ***Each classification filter has some common values:***

    - **Applied**: Any filter value is applied
    - **Not Applied**: No filter value is applied. For example, if you pick a classification filter with value as "Not Applied", the graph shows all assets with no classification.
    - **All**: Filter values are cleared. Meaning the graph shows all assets, with or without classification.
    - **Specific**: You pick a specific classification from the filter, and only that classification is shown.
7. To learn more about which specific assets are shown in the graph, select **View details**.

    ![Screenshot of the insights assets by collection section, with the view-details button at the bottom highlighted.](media/asset-insights/view-details.png)

    ![Screenshot of the asset details view screen, which is still within the Data Estate Insights application.](media/asset-insights/details-view.png)
8. You can select any collection to view the collection's asset list.

    ![Screenshot of the asset details view screen, with one of the collections highlighted.](media/asset-insights/select-collection.png)

    ![Screenshot of the asset list screen, showing all assets within the selected collection.](media/asset-insights/asset-list.png)
9. You can also select an asset to edit without leaving the Data Estate Insights App.

    ![Screenshot of the asset list screen, with an asset selected for editing and the asset edit screen open within the Data Estate Insights application.](media/asset-insights/edit-asset.png)

### File-based source types

The next graphs in asset insights show a distribution of file-based source types. The first graph, **Size trend (GB) of file type within source types**, shows top file type size trends over the last 30 days.

1. Pick your source type to view the file type within the source.
2. Select **View details** to see the current data size, change in size, current asset count, and change in asset count.

    Note

    If the scan runs only once in the last 30 days, or any catalog change such as classification addition or removal happens only once in 30 days, then the change information appears blank.
3. See the top folders with change top asset counts when you select source type.
4. Select the path to see the asset list.

The second graph in file-based source types is **Files not associated with a resource set**. If you expect that all files should roll up into a resource set, this graph can help you understand which assets aren't rolled up. Missing assets can be an indication of the wrong file-pattern in the folder. You can select **View details** below the graph for more information.

[![View file based assets](media/asset-insights/file-based-assets-inline.png)](media/asset-insights/file-based-assets.png#lightbox)