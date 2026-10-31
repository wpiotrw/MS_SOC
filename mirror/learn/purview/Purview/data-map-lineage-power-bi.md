---
layout: Conceptual
title: Metadata and lineage from Power BI into Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-lineage-power-bi
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article describes the data lineage extraction from Power BI source into Microsoft Purview.
ms.custom: sfi-image-nochange
locale: en-us
document_id: a49b9d74-05d0-18bb-e440-a10551607e29
document_version_independent_id: a49b9d74-05d0-18bb-e440-a10551607e29
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-lineage-power-bi.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-lineage-power-bi
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-lineage-power-bi.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 0ca8e70b-ae98-168e-ad65-a7c89952bb85
---

# Metadata and lineage from Power BI into Microsoft Purview | Microsoft Learn

This article elaborates on the data lineage for Power BI sources in Microsoft Purview.

## Prerequisites

To see data lineage in Microsoft Purview for Power BI, you must first [register and scan your Power BI source](register-scan-power-bi-tenant).

## Common scenarios

After a Power BI source has been scanned, lineage information for your current data assets, and data assets referenced by Power BI, will automatically be added in the Microsoft Purview Unified Catalog.

1. Data consumers can perform root cause analysis of a report or dashboard from Microsoft Purview. For any data discrepancy in a report, users can easily identify the upstream datasets and contact their owners if necessary.
2. Data producers can see the downstream reports or dashboards consuming their dataset. Before making any changes to their datasets, the data owners can make informed decisions.
3. Users can search by name, endorsement status, sensitivity label, owner, description, and other business facets to return the relevant Power BI artifacts.

## Power BI artifacts in Microsoft Purview

Once the [scan of your Power BI](register-scan-power-bi-tenant) is complete, following Power BI artifacts will be inventoried in Microsoft Purview:

- Workspaces
- Dashboards
- Reports
- Datasets
- Dataflows
- Datamarts

[![Screenshot showing how Overview tab is rendered for Power BI assets.](media/how-to-lineage-powerbi/powerbi-overview.png)](media/how-to-lineage-powerbi/powerbi-overview.png#lightbox)

## Lineage of Power BI artifacts in Microsoft Purview

Users can search for a Power BI artifact by name, description, or other details to see relevant results. Under the asset overview and properties tabs, the basic details such as description, classification are shown. Under the lineage tab, asset relationships are shown with the upstream and downstream dependencies.

Microsoft Purview captures lineage among Power BI artifacts (for example: Dataflow -&gt; Dataset -&gt; Report -&gt; Dashboard) and external data assets.

Note

For lineage between Power BI artifacts and external data assets, currently the supported source types are:

- Azure SQL Database
- Azure Blob Storage
- Azure Data Lake Store Gen1
- Azure Data Lake Store Gen2

[![Screenshot showing how lineage is rendered for Power BI.](media/how-to-lineage-powerbi/powerbi-lineage.png)](media/how-to-lineage-powerbi/powerbi-lineage.png#lightbox)

In addition, column level lineage (Power BI subartifact lineage) and transformation inside of Power BI datasets (except for Dataflows) are captured when using Azure SQL Database as source. For measures, you can further select column -&gt; Properties -&gt; expression to see the transformation details.

Note

Column level lineage and transformations (except for Dataflows) are supported when using Azure SQL Database as source. Other sources are currently not supported.

[![Screenshot showing how Power BI subartifacts lineage is rendered.](media/how-to-lineage-powerbi/power-bi-lineage-subartifacts.png)](media/how-to-lineage-powerbi/power-bi-lineage-subartifacts.png#lightbox)

## Known limitations

- Microsoft Purview leverages the scanner API to retrieve the metadata and lineage. Learn about some API limitations from [Metadata scanning - Considerations and limitations](/en-us/power-bi/enterprise/service-admin-metadata-scanning#considerations-and-limitations).
- In case you have the dataset table connected to another dataset table, when the middle dataset disables the "Enable load" option inside the Power BI desktop, and the lineage can't be extracted.
- For lineage between Power BI artifacts and external data assets:
    - Currently the supported source types are Azure SQL Database, Azure Blob Storage, Azure Data Lake Store Gen1 and Azure Data Lake Store Gen2.
    - Column level lineage and transformations (except for Power BI Dataflows) are only supported when using Azure SQL Database as source. Other sources are currently not supported.
    - Lineage is not captured when you use dynamic M query parameters in Power BI, e.g. pass server/database names as parameter values.
    - Limited information is currently shown for data sources where the Power BI Dataflow is created. For example, for a SQL server source of Power BI dataset, only server/database name is captured.
    - Note due to the following limitations, if you have such scenarios and scan both Power BI and the data sources that Power BI artifacts connect to, currently you may see duplicate assets in the catalog.
        - The source object names in assets and fully qualified names follow the case used in Power BI settings/queries, which may not align with the object case in original data source.
        - When Power BI references SQL views, they are currently captured as SQL table assets.
        - When Power BI references Azure Dedicated SQL pool (formerly SQL DW) sources, it's currently listed as Azure SQL Database assets. (Lineage between Power BI artifacts and external Azure Dedicated SQL pools isn't currently supported.)
- For Power BI subartifact lineage:
    - Some measures aren't shown in the subartifact lineage, for example, `COUNTROWS`.
    - In the lineage graph, when selecting a measure that is derived by columns using the COUNT function, the underlying column isn't selected automatically. Check the measure expression in the column properties tab to identify the underlying column.
    - If you scanned your Power BI source before subartifact lineage was supported, you may see a database asset along with the new table assets in the lineage graph, which isn't removed.
- Currently for the same data asset in Azure SQL Database which has UTF-8 characters in name, the full qualified name generated from scanning Power BI may be different with the fully qualified name generated from scanning Azure SQL Database as the former will go through additional encoding, and it may introduce duplicate Azure SQL data assets.