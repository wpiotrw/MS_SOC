---
layout: Conceptual
title: Metadata and lineage from Azure Synapse Analytics into Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-lineage-azure-synapse-analytics
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
description: This article describes how to connect Azure Synapse Analytics and Microsoft Purview to track data lineage.
locale: en-us
document_id: 97a004a1-de8c-3917-4be2-3cbd152a45b8
document_version_independent_id: 97a004a1-de8c-3917-4be2-3cbd152a45b8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-lineage-azure-synapse-analytics.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-lineage-azure-synapse-analytics
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-lineage-azure-synapse-analytics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bad69977-db6a-44f3-b752-d2bee7de49ca
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31d7aff-61be-45e2-a324-a578cf0c3360
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 28ecd01c-cf4d-281d-bc0b-cf90a04bf0a7
---

# Metadata and lineage from Azure Synapse Analytics into Microsoft Purview | Microsoft Learn

This article explains the steps required for connecting an Azure Synapse workspace with a Microsoft Purview account to track [data lineage](data-gov-classic-lineage) and [ingest data sources](data-map-scan-ingestion#ingestion). The article also explains details of the activity coverage scope and supported lineage capabilities.

When you connect Azure Synapse Analytics to Microsoft Purview, whenever a supported pipeline activity is run, metadata about the activity's source data, output data, and the activity will be automatically [ingested](data-map-scan-ingestion#ingestion) into the Microsoft Purview Data Map.

If a data source has already been scanned and exists in the data map, the ingestion process will add the lineage information from Azure Synapse Analytics to that existing source. If the source or output doesn't exist in the data map and is supported by Azure Synapse Analytics lineage Microsoft Purview will automatically add their metadata from Synapse Analytics into the data map under the default domain root collection.

This can be an excellent way to monitor your data estate as users move and transform information using Azure Synapse Analytics.

## Supported Azure Synapse capabilities

Currently, Microsoft Purview captures runtime lineage from the following Azure Synapse pipeline activities:

- [Copy Data](/en-us/azure/data-factory/copy-activity-overview?context=/azure/synapse-analytics/context/context)
- [Data Flow](/en-us/azure/data-factory/concepts-data-flow-overview?context=/azure/synapse-analytics/context/context)

Important

Microsoft Purview drops lineage if the source or destination uses an unsupported data storage system.

### Copy activity support

| Data store | Supported |
| --- | --- |
| Azure Blob Storage | Yes |
| Azure Cognitive Search | Yes |
| Azure Cosmos DB for NoSQL \* | Yes |
| Azure Cosmos DB for MongoDB \* | Yes |
| Azure Data Explorer \* | Yes |
| Azure Data Lake Storage Gen1 | Yes |
| Azure Data Lake Storage Gen2 | Yes |
| Azure Database for MariaDB \* | Yes |
| Azure Database for MySQL \* | Yes |
| Azure Database for PostgreSQL \* | Yes |
| Azure Files | Yes |
| Azure SQL Database \* | Yes |
| Azure SQL Managed Instance \* | Yes |
| Azure Synapse Analytics \* | Yes |
| Azure Dedicated SQL pool (formerly SQL DW) \* | Yes |
| Azure Table Storage | Yes |
| Amazon S3 | Yes |
| Hive \* | Yes |
| Oracle \* | Yes |
| SAP Table *(when connecting to SAP ECC or SAP S/4HANA)* | Yes |
| SQL Server \* | Yes |
| Teradata \* | Yes |

*\* Microsoft Purview currently doesn't support query or stored procedure for lineage or scanning. Lineage is limited to table and view sources only.*

If you use Self-hosted Integration Runtime, note the minimal version with lineage support for:

- Any use case: version 5.9.7885.3 or later
- Copying data from Oracle: version 5.10 or later
- Copying data into Azure Synapse Analytics via COPY command or PolyBase: version 5.10 or later

#### Limitations on copy activity lineage

Currently, if you use the following copy activity features, the lineage is not yet supported:

- Copy data into Azure Data Lake Storage Gen1 using Binary format.
- Compression setting for Binary, delimited text, Excel, JSON, and XML files.
- Source partition options for Azure SQL Database, Azure SQL Managed Instance, Azure Synapse Analytics, SQL Server, and SAP Table.
- Copy data to file-based sink with setting of max rows per file.
- Column level lineage is not currently supported by copy activity when source/sink is [resource set](data-map-resource-sets).

In additional to lineage, the data asset schema (shown in Asset -&gt; Schema tab) is reported for the following connectors:

- CSV and Parquet files on Azure Blob, Azure Files, ADLS Gen1, ADLS Gen2, and Amazon S3
- Azure Data Explorer, Azure SQL Database, Azure SQL Managed Instance, Azure Synapse Analytics, SQL Server, Teradata

### Data Flow support

| Data store | Supported |
| --- | --- |
| Azure Blob Storage | Yes |
| Azure Cosmos DB for NoSQL \* | Yes |
| Azure Data Lake Storage Gen1 | Yes |
| Azure Data Lake Storage Gen2 | Yes |
| Azure Database for MySQL \* | Yes |
| Azure Database for PostgreSQL \* | Yes |
| Azure SQL Database \* | Yes |
| Azure SQL Managed Instance \* | Yes |
| Azure Synapse Analytics \* | Yes |
| Azure Dedicated SQL pool (formerly SQL DW) \* | Yes |

*\* Microsoft Purview currently doesn't support query or stored procedure for lineage or scanning. Lineage is limited to table and view sources only.*

#### Limitations on data flow lineage

- Data flow lineage may generate folder level [resource set](data-map-resource-sets) without visibility on the involved files.
- Column level lineage is not currently supported when source/sink is [resource set](data-map-resource-sets).
- For the lineage of data flow activity, Microsoft Purview only supports showing the source and sink involved. The detailed lineage for data flow transformation isn't supported yet.
- Lineage is not supported when [flowlets](/en-us/azure/data-factory/concepts-data-flow-flowlet) are part of the dataflow.
- Currently Purview doesn't support lineage reporting for Synapse tables (LakeHouse DB/Workspace DB)

## Access secured Microsoft Purview account

If your Microsoft Purview account is protected by firewall, learn how to let Azure Synapse [access a secured Microsoft Purview account](/en-us/azure/synapse-analytics/catalog-and-governance/how-to-access-secured-purview-account) through Microsoft Purview private endpoints.

## Bring Azure Synapse lineage into Microsoft Purview

### Step 1: Connect Azure Synapse workspace to your Microsoft Purview account

You can connect an Azure Synapse workspace to Microsoft Purview, and the connection enables Azure Synapse to push lineage information to Microsoft Purview. Follow the steps in [Connect Synapse workspace to Microsoft Purview](/en-us/azure/synapse-analytics/catalog-and-governance/quickstart-connect-azure-purview). Multiple Azure Synapse workspaces can connect to a single Microsoft Purview account for holistic lineage tracking.

### Step 2: Run pipeline in Azure Synapse workspace

You can create pipelines with Copy activity in Azure Synapse workspace. You don't need any other configuration for lineage data capture. The lineage data will automatically be captured during the activities execution.

### Step 3: Monitor lineage reporting status

After you run the Azure Synapse pipeline, in the Synapse pipeline monitoring view, you can check the lineage reporting status by selecting the following **Lineage status** button. The same information is also available in the activity output JSON -&gt; `reportLineageToPurvew` section.

![Monitor the lineage reporting status in pipeline monitoring view.](media/data-factory-purview/monitor-lineage-reporting-status.png)

### Step 4: View lineage information in your Microsoft Purview account

In your Microsoft Purview account, you can browse assets and choose type "Azure Synapse Analytics". You can also search Unified Catalog using keywords.

![Browse the Azure Synapse assets in Microsoft Purview.](media/how-to-lineage-azure-synapse-analytics/browse-azure-synapse-assets.png)

Select the Synapse account -&gt; pipeline -&gt; activity, you can view the lineage information.

[![Browse the Azure Synapse pipeline lineage in Microsoft Purview.](media/how-to-lineage-azure-synapse-analytics/browse-azure-synapse-pipeline-lineage.png)](media/how-to-lineage-azure-synapse-analytics/browse-azure-synapse-pipeline-lineage.png#lightbox)

## Monitor the Azure Synapse Analytics links

In Microsoft Purview governance portal, you can [monitor the Azure Synapse Analytics links](data-map-scan-run-monitor-population#monitor-links).