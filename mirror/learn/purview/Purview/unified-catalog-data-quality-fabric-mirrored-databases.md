---
layout: Conceptual
title: Data Quality for Fabric Mirrored Databases in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-fabric-mirrored-databases
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Get step-by-step guidance on configuring data quality scans for a Microsoft Fabric mirrored data asset in Microsoft Purview.
locale: en-us
document_id: b56a3925-1f48-3032-32b1-5975c51154c2
document_version_independent_id: b56a3925-1f48-3032-32b1-5975c51154c2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-fabric-mirrored-databases.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-fabric-mirrored-databases
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-fabric-mirrored-databases.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 71094fb1-7b45-675a-750d-fcffb7bdabe4
---

# Data Quality for Fabric Mirrored Databases in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article explains how to configure data quality scans in Microsoft Purview for data assets that are mirrored from external sources into Microsoft Fabric.

Mirroring in Fabric is a low-cost, low-latency solution that replicates data from sources like Azure SQL Database, Azure Cosmos DB, and Snowflake into Fabric's OneLake. For more information, see the [Fabric mirroring documentation](/en-us/fabric/mirroring/overview).

## Configure data quality for a Fabric mirrored database

To set up data quality for a Fabric mirrored database, complete the following steps:

Note

Before you begin, make sure you have:

- A [Microsoft Fabric workspace](/en-us/fabric/get-started/create-workspaces) with mirroring enabled.
- A Lakehouse in your Fabric workspace (or permissions to create one).
- Access to [Microsoft Purview Data Map](data-map-scan-data-sources) with service principal authentication configured.

1. [Enable mirroring in your Fabric tenant](/en-us/fabric/mirroring/overview). A Power BI administrator can enable mirroring for the entire organization or for specific security groups in the Power BI admin portal. You can replicate an entire database or individual tables.
2. After enabling mirroring and initiating replication, [confirm that replication completes successfully](/en-us/fabric/mirroring/monitor).
3. [Open the SQL analytics endpoint](/en-us/fabric/data-engineering/navigate-lakehouse-explorer#access-a-lakehouses-sql-analytics-endpoint).

    [![Screenshot to navigate sql end point.](media/data-quality-self-help/go-to-sql-end-point.png)](media/data-quality-self-help/go-to-sql-end-point.png#lightbox)
4. On the **Reporting** tab, select **Automatically update semantic model**.

    [![Automatically update semantic model.](media/data-quality-self-help/update-semantic-model.png)](media/data-quality-self-help/update-semantic-model.png#lightbox)
5. Create a Lakehouse in your Fabric workspace if you don't have one created.
6. Create a Fabric shortcut from your mirrored database to the lakehouse.
7. Go to Microsoft Purview Data Map and [run a Data Map scan](data-map-scan-data-sources) on the lakehouse you created in the previous step. Use service principal authentication.

    ![Use service principal for datamap scan.](media/data-quality-self-help/datamap-servicepriciple.png)
8. When the scan is completed, [associate the discovered Lakehouse table assets with a data product](unified-catalog-data-products-create-manage#add-data-assets). Make sure to select the **Lakehouse tables** to associate to your [data product](unified-catalog-data-products-create-manage).
9. After associating the Lakehouse tables with your target data product in Unified Catalog, you can profile and measure the data quality of all mirrored tables as Lakehouse tables in Microsoft Purview.
10. In the **Data quality** area of **Health management** in Unified Catalog, [run a data quality scan](unified-catalog-data-quality-scan) or [profile your data](unified-catalog-data-quality-profiling) as usual.

Important

- Use service principal for Data Map scans, and use a managed identity for data quality scans.
- Select the mirrored database instead of individual tables.
- Update the semantic model every time when you add new table to the mirrored database.
- If your mirrored database tables aren't available in the Fabric Lakehouse, contact Fabric support.
- Data quality scanning is supported only for Lakehouse Delta, Iceberg, and Parquet file formats.