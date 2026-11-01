---
layout: Conceptual
title: Data Quality for Azure Synapse in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-azure-synapse
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2025-02-13T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Get step-by-step guidance to configure data quality scans for Microsoft Azure Synapse serverless and Azure Synapse data warehouse in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 7a9d7803-9eb9-19fa-f153-5fd15ed2115d
document_version_independent_id: 7a9d7803-9eb9-19fa-f153-5fd15ed2115d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-azure-synapse.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-azure-synapse
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-azure-synapse.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bad69977-db6a-44f3-b752-d2bee7de49ca
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31d7aff-61be-45e2-a324-a578cf0c3360
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
platformId: d20d16dd-6e32-73df-c558-7c006e9b01fa
---

# Data Quality for Azure Synapse in Unified Catalog | Microsoft Learn

This article explains how to configure data quality scans for Azure Synapse Analytics assets in Microsoft Purview Unified Catalog. You'll learn how to set up Data Map scans, create connections, and run data profiling and quality scans for both Synapse dedicated data warehouse and Synapse serverless SQL pools.

Microsoft Azure Synapse Analytics is an enterprise analytics service that accelerates time to insight across data warehouses and big data systems. For more details, see the [Azure Synapse Analytics documentation](/en-us/azure/synapse-analytics/overview-what-is).

The following example shows a Synapse workspace with a Dedicated Synapse Data Warehouse (DWH) table called **EMPLOYEE** and a Serverless Database (SQL\_ON\_DEMAND) with a **SynapseSalesDelta** table.

![Screenshot of synapse analytics workspace.](media/synapse-dq/synapse-databae-example.png)

After you scan Azure Synapse assets, the scanned assets appear in Microsoft Purview. The following example shows an Employee table on a Synapse Analytics Dedicated instance.

## Set up data quality for Azure Synapse Analytics dedicated SQL pool

To configure data quality for a Synapse dedicated SQL pool, set up a Data Map scan, create a connection, and then run profiling and data quality scans.

### Set up Data Map scan for Synapse dedicated SQL

To scan Azure Synapse Analytics dedicated SQL pool, see [Register and scan a Synapse workspace](register-scan-synapse-workspace). To grant the necessary managed identity permissions on the dedicated SQL instance, see [Use a managed identity for dedicated SQL databases](register-scan-synapse-workspace#use-a-managed-identity-for-dedicated-sql-databases).

![Screenshot of data map scan configuration.](media/synapse-dq/config-data-map-scan.png)

After the Data Map scan completes, the Synapse dedicated SQL assets appear in Microsoft Purview Unified Catalog. The following example shows an Employee table on a Synapse Analytics dedicated instance:

![Screenshot of data map scan result.](media/synapse-dq/synapse-data-map-scan.png)

### Set up connection to your Synapse dedicated data warehouse

After the Data Map scan completes and the dedicated SQL asset appears in Unified Catalog, the asset is ready for cataloging and governance.

Important

- Data Quality stewards need read-only access to the Synapse dedicated data warehouse to set up the data quality connection.
- If your Synapse data source is behind a private endpoint, you must first enable managed virtual networks. See [Set up managed virtual networks](unified-catalog-data-quality-managed-virtual-networks). In managed virtual network setups, you can't test the connection.

Associate the scanned asset to the data product in a governance domain. At the Data Quality tab, add a new Azure SQL Database connection and enter the database name manually.

1. In Unified Catalog, go to **Health management** &gt; **Data quality** and select a governance domain.
2. On the governance domain's details page, select **Manage**, then select **Connections**.
3. On the **Connections** page, select **New** and configure connection with the following information, as seen in the example below:

    - Add connection name and description.
    - Select source type **Azure Synapse Analytics**.
    - Select **Azure subscription**.
    - Select **Workspace name**.
    - Select **Dedicated SQL endpoint**.
    - Select **serverless SQL endpoint**.
    - Select **Endpoint type**.
    - Select **Database**.
    - Add MSI as Credential.

    [![Screenshot of how to set up data source connection.](media/synapse-dq/connectionsetup.png)](media/synapse-dq/connectionsetup.png#lightbox)
4. Test the connection. After configuring the data source connection and successfully testing it, you can proceed to configure and run data profiling and data quality scans.

### Profiling and data quality scanning for data in Synapse dedicated data warehouse

After you set up the connection, you can profile your data, create and apply rules, and run a data quality scan for your data in Synapse dedicated data warehouse.

Important

Before you run profiling or data quality scans, verify that your dedicated SQL pool configuration and concurrency limits can support these jobs. Data quality assessment jobs open connections on the dedicated SQL pool and might fail if the instance is underprovisioned or exceeds concurrency limits. Concurrency limits might lead to job termination. Higher DW limits (such as DWU 1000) provide the capacity to run the queries. For more information, see [Memory and concurrency limits](/en-us/azure/synapse-analytics/sql-data-warehouse/memory-concurrency-limits).

Use the following articles for step-by-step guidance:

- [How to configure and run data profiling of your data](unified-catalog-data-quality-profiling)
- [How to configure and run data quality scan](unified-catalog-data-quality-scan)

## Set up data quality for Azure Synapse Analytics serverless SQL pool

To configure data quality for a Synapse serverless SQL pool, set up a Data Map scan, create a connection, and then run profiling and data quality scans.

### Set up Data Map scan for Synapse serverless SQL

To scan Azure Synapse Analytics serverless SQL pool, see [Register and scan a Synapse workspace](register-scan-synapse-workspace). To grant the necessary managed identity permissions, see [Use a managed identity for dedicated SQL databases](register-scan-synapse-workspace#use-a-managed-identity-for-dedicated-sql-databases). After the Data Map scan completes, the serverless assets appear in Unified Catalog.

![Screenshot of data map scan configuration for serverless.](media/synapse-dq/synapse-serverless-datamap-scan.png)

### Set up connection to your Synapse serverless SQL pool

After the Data Map scan completes and the serverless SQL asset appears in Unified Catalog, the asset is ready for cataloging and governance.

Important

- Data Quality stewards need read-only access to the Synapse dedicated data warehouse to set up the data quality connection.
- If your Synapse data source is behind a private endpoint, you must first enable managed virtual networks. See [Set up managed virtual networks](unified-catalog-data-quality-managed-virtual-networks).
- In Synapse serverless setup, the external table points to Delta formatted data stored in ADLS Gen2.
- The Synapse connector only detects and supports **sql.azuresynapse.net**. If the Fully Qualified Name (FQN) generated by your Data Map scan contains **database.windows.net**, the Synapse connection for data quality scan will fail.

Associate the scanned asset to the data product in a governance domain. In **Data Quality**, add a new SQL Database connection and enter the database name manually.

1. In Unified Catalog, go to **Health management** &gt; **Data quality** and select a governance domain.
2. On the governance domain's details page, select **Manage**, then select **Connections**.
3. On the **Connections** page, select **New** and configure connection with the following information, as seen in the example below

    - Add connection name and description.
    - Select source type **Azure Synapse Analytics**.
    - Select **Azure subscription**.
    - Select **Workspace name**.
    - Select **Dedicated SQL endpoint**.
    - Select **serverless SQL endpoint**.
    - Select **Endpoint type**.
    - Select **Database**.
    - Add MSI as Credential.

    [![Screenshot of how to set up data source connection for synapse serverless.](media/synapse-dq/connectionsetup.png)](media/synapse-dq/connectionsetup.png#lightbox)
4. Test the connection. After configuring the data source connection and successfully testing it, you can proceed to configure and run data profiling and data quality scans.

### Profiling and data quality scanning for data in Synapse serverless

After you set up the connection, you can profile your data, create and apply rules, and run a data quality scan for your data in Synapse serverless SQL pool.

Important

Data quality assessments and profiling run on Spark in the background, where each Spark node opens a connection. For Azure Synapse serverless SQL, no concurrency limits apply. Performance depends on the Delta Parquet optimizations on your ADLS Gen2 instance. The engine works with external lakehouse sources such as Delta format tables.

Use the following articles for step-by-step guidance:

- [How to configure and run data profiling of your data](unified-catalog-data-quality-profiling)
- [How to configure and run data quality scan](unified-catalog-data-quality-scan)

### Performance and connection reference for Synapse serverless

Use the following references for serverless performance and connection details:

- [Memory and concurrency limits for Azure Synapse Analytics](/en-us/azure/synapse-analytics/sql-data-warehouse/memory-concurrency-limits)
- [Set up data source connection for data quality](unified-catalog-data-quality-supported-sources-connection)