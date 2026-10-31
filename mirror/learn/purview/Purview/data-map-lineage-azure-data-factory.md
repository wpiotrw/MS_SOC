---
layout: Conceptual
title: Connect Azure Data Factory to Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-lineage-azure-data-factory
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2026-02-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article describes how to connect Azure Data Factory and Microsoft Purview to track data lineage.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 534b3fb1-35c5-5e3a-654d-b2cb5a3a8335
document_version_independent_id: 534b3fb1-35c5-5e3a-654d-b2cb5a3a8335
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-lineage-azure-data-factory.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-lineage-azure-data-factory
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-lineage-azure-data-factory.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/655f39c4-21c5-49d3-8367-a1f9c1a0b930
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d30b39f7-a405-488d-84ef-d6d5296ad372
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c862c1e6-e701-a751-95bb-fcf9d681b6dc
---

# Connect Azure Data Factory to Microsoft Purview | Microsoft Learn

This article explains the steps required for connecting an Azure Data Factory account with a Microsoft Purview account to track [data lineage](data-gov-classic-lineage) and [ingest data sources](data-map-scan-ingestion#ingestion). The article also explains details of the activity coverage scope and supported lineage patterns.

When you connect an Azure Data Factory to Microsoft Purview, whenever a supported Azure Data Factory activity runs, it automatically [ingests](data-map-scan-ingestion#ingestion) metadata about the activity's source data, output data, and the activity into Microsoft Purview Data Map.

If a data source is already scanned and exists in Data Map, the ingestion process adds the lineage information from Azure Data Factory to that existing source. If the source or output doesn't exist in Data Map and is supported by Azure Data Factory lineage, Microsoft Purview automatically adds their metadata from Azure Data Factory into Data Map under the root collection.

This connection is an excellent way to monitor your data estate as users move and transform information by using Azure Data Factory.

## View existing Data Factory connections

Multiple Azure Data Factorys can connect to a single Purview to push lineage information. The current limit allows you to connect up to 10 Azure Data Factory accounts at a time from the Microsoft Purview management center. To show the list of Azure Data Factory accounts connected to your Microsoft Purview account, follow these steps:

1. Select **Management** on the left navigation pane.
2. Under **Lineage connections**, select **Data Factory**.
3. The Data Factory connection list appears.

    [![Screen shot showing a data factory connection list.](media/how-to-link-azure-data-factory/data-factory-connection.png)](media/how-to-link-azure-data-factory/data-factory-connection.png#lightbox)
4. Notice the various values for connection **Status**:

    - **Connected**: The Data Factory is connected to the Microsoft Purview account.
    - **Disconnected**: The Data Factory has access to the catalog, but it's connected to another catalog. As a result, data lineage won't be reported to the catalog automatically.
    - **Unknown**: The current user doesn't have access to the Data Factory, so the connection status is unknown.

Note

To view the Data Factory connections, you need to be assigned the following role. Role inheritance from management group isn't supported. **Collection admins** role on the root collection.

## Create new Azure Data Factory connection

Note

To add or remove the Azure Data Factory connections, you need to be assigned the following role. Role inheritance from management group is not supported. **Collection admins** role on the root collection.

Also, you need to be the Azure Data Factory's "Owner" or "Contributor".

Your Azure Data Factory needs to have system assigned managed identity enabled.

Follow the steps below to connect an existing Azure Data Factory to your Microsoft Purview account. You can also [connect Data Factory to Microsoft Purview account from ADF](/en-us/azure/data-factory/connect-data-factory-to-azure-purview).

1. Select **Management** on the left navigation pane.
2. Under **Lineage connections**, select **Data Factory**.
3. On the **Data Factory connection** page, select **New**.
4. Select your Azure Data Factory account from the list and select **OK**. You can also filter by subscription name to limit your list.

    Some Azure Data Factory instances might be disabled if the Azure Data Factory is already connected to the current Purview account, or the Azure Data Factory doesn't have a managed identity. A warning message is displayed if any of the selected Azure Data Factorys are already connected to other Microsoft Purview account. When you select **OK**, the Azure Data Factory connection with the other Microsoft Purview account is disconnected. No other confirmations are required.

    ![Screenshot showing warning to disconnect Azure Data Factory.](media/how-to-link-azure-data-factory/warning-for-disconnect-factory.png)

Note

You can add up to 10 Azure Data Factory accounts at once. To add more than 10 Azure Data Factory accounts, add them in multiple batches.

### How authentication works

Azure Data Factory uses its managed identity to authenticate lineage push operations from Microsoft Purview. When you connect your Azure Data Factory to Purview in the UI, it adds the role assignment automatically.

Grant the Azure Data Factory's managed identity the **Data Curator** role on Microsoft Purview **root collection**. To learn more, see [Access control in Microsoft Purview](data-gov-classic-permissions) and [Add roles and restrict access through collections](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

### Remove Data Factory connections

Important

Even if the Data Factory connection is removed, any ongoing ingestion won't be canceled. Azure Data Factory lineage ingestion is an asynchronous operation.

To remove an Azure Data Factory connection, complete the following steps:

1. On the **Data Factory connection** page, select the **Remove** button next to one or more Azure Data Factory connections.
2. Select **Confirm** in the popup to delete the selected Azure Data Factory connections.

    [![Screenshot showing how to select data factories to remove connection.](media/how-to-link-azure-data-factory/remove-data-factory-connection.png)](media/how-to-link-azure-data-factory/remove-data-factory-connection.png#lightbox)

## Monitor the Azure Data Factory links

In Microsoft Purview portal, you can [monitor the Data Factory links](data-map-scan-run-monitor-population#monitor-links).

## Supported Azure Data Factory activities

Microsoft Purview captures runtime lineage from the following Azure Data Factory activities:

- [Copy Data](/en-us/azure/data-factory/copy-activity-overview)
- [Data Flow](/en-us/azure/data-factory/concepts-data-flow-overview)
- [Execute SSIS Package](/en-us/azure/data-factory/how-to-invoke-ssis-package-ssis-activity)

Important

Microsoft Purview drops lineage if the source or destination uses an unsupported data storage system.

The integration between Azure Data Factory and Microsoft Purview supports only a subset of the data systems that Azure Data Factory supports. For more information, see the following sections.

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

### Execute SSIS Package support

Refer to [supported data stores](data-map-lineage-sql-server-integration-services#supported-data-stores).

## Access secured Microsoft Purview account

If a firewall protects your Microsoft Purview account, learn how to let Azure Data Factory [access a secured Microsoft Purview account](/en-us/azure/data-factory/how-to-access-secured-purview-account) through Microsoft Purview private endpoints.

## Bring Azure Data Factory lineage into Microsoft Purview

For an end-to-end walkthrough, see the [Tutorial: Push Data Factory lineage data to Microsoft Purview](/en-us/azure/data-factory/turorial-push-lineage-to-purview).

## Supported lineage patterns

Microsoft Purview supports several patterns of lineage. The generated lineage data depends on the type of source and sink used in the Azure Data Factory activities. Although Azure Data Factory supports over 80 sources and sinks, Microsoft Purview supports only a subset. For the supported sources and sinks, see Supported Azure Data Factory activities.

To configure Azure Data Factory to send lineage information, see [Get started with lineage](data-gov-classic-lineage-user-guide#get-started-with-lineage).

You can find information in the lineage view by using the following methods:

- In the **Lineage** tab, hover on shapes to preview additional information about the asset in the tooltip.
- Select the node or edge to see the asset type it belongs to or to switch assets.
- The **Lineage** tab displays columns of a dataset on the left side. For more information about column-level lineage, see [Dataset column lineage](data-gov-classic-lineage-user-guide#dataset-column-lineage).

### Data lineage for 1:1 operations

The most common pattern for capturing data lineage moves data from a single input dataset to a single output dataset, with a process in between.

An example of this pattern includes the following components:

- 1 source/input: *Customer* (SQL Table)
- 1 sink/output: *Customer1.csv* (Azure Blob)
- 1 process: *CopyCustomerInfo1#Customer1.csv* (Data Factory Copy activity)

![Screenshot showing the lineage for a one to one Data Factory Copy operation.](media/how-to-link-azure-data-factory/adf-copy-lineage.png)

### Data movement with 1:1 lineage and wildcard support

Another common scenario for capturing lineage is using a wildcard to copy files from a single input dataset to a single output dataset. The wildcard allows the copy activity to match multiple files for copying by using a common portion of the file name. Microsoft Purview captures file-level lineage for each individual file copied by the corresponding copy activity.

An example of this pattern includes the following components:

- Source/input: *CustomerCall\*.csv* (ADLS Gen2 path)
- Sink/output: *CustomerCall\*.csv* (Azure blob file)
- 1 process: *CopyGen2ToBlob#CustomerCall.csv* (Data Factory Copy activity)

[![Screenshot showing lineage for a one to one Copy operation with wildcard support.](media/how-to-link-azure-data-factory/adf-copy-lineage-wildcard.png)](media/how-to-link-azure-data-factory/adf-copy-lineage-wildcard.png#lightbox)

### Data movement with n:1 lineage

You can use Data Flow activities to perform data operations like merge, join, and so on. You can use more than one source dataset to produce a target dataset. In this example, Microsoft Purview captures file-level lineage for individual input files to a SQL table that is part of a Data Flow activity.

An example of this pattern includes the following components:

- 2 sources/inputs: *Customer.csv*, *Sales.parquet* (ADLS Gen2 Path)
- 1 sink/output: *Company data* (Azure SQL table)
- 1 process: *DataFlowBlobsToSQL* (Data Factory Data Flow activity)

[![Screenshot showing the lineage for an n to one A D F Data Flow operation.](media/how-to-link-azure-data-factory/adf-data-flow-lineage.png)](media/how-to-link-azure-data-factory/adf-data-flow-lineage.png#lightbox)

### Lineage for resource sets

A resource set is a logical object in the catalog that represents many partition files in the underlying storage. For more information, see [Understanding Resource sets](data-map-resource-sets). When Microsoft Purview captures lineage from Azure Data Factory, it applies the rules to normalize the individual partition files and create a single logical object.

In the following example, an Azure Data Lake Gen2 resource set is produced from an Azure Blob:

- 1 source/input: *Employee\_management.csv* (Azure Blob)
- 1 sink/output: *Employee\_management.csv* (Azure Data Lake Gen 2)
- 1 process: *CopyBlobToAdlsGen2\_RS* (Azure Data Factory Copy activity)

[![Screenshot showing the lineage for a resource set.](media/how-to-link-azure-data-factory/adf-resource-set-lineage.png)](media/how-to-link-azure-data-factory/adf-resource-set-lineage.png#lightbox)