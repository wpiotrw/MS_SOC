---
layout: Conceptual
title: Lookup activity - Microsoft Fabric | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fabric/data-factory/lookup-activity
breadcrumb_path: /fabric/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Fabric
show_latex: false
feedback_system: Standard
feedback_help_link_url: https://community.fabric.microsoft.com/datafactory
feedback_help_link_type: ask-the-community
feedback_product_url: https://ideas.fabric.microsoft.com/?forum=ea587140-44f9-ed11-8849-000d3a4ef41d
ms.service: fabric
author: whhender
ms.author: whhender
ms.subservice: data-factory
search.app:
- fabric-datafactory-docs
description: Learn how to add a lookup activity to a pipeline and use it to look up data from a data source.
ms.reviewer: xupxhou
ms.topic: how-to
ms.custom: pipelines
ms.date: 2026-01-20T00:00:00.0000000Z
locale: en-us
document_id: 9040a4a8-cdcd-acfd-2c9c-b284f2f0b281
document_version_independent_id: 9040a4a8-cdcd-acfd-2c9c-b284f2f0b281
original_content_git_url: https://github.com/MicrosoftDocs/fabric-docs-pr/blob/live/docs/data-factory/lookup-activity.md
site_name: Docs
depot_name: MSDN.fabric-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fabric-docs/{branchName}{pdfName}
asset_id: data-factory/lookup-activity
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/data-factory/lookup-activity.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/655f39c4-21c5-49d3-8367-a1f9c1a0b930
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://authoring-docs-microsoft.poolparty.biz/devrel/d30b39f7-a405-488d-84ef-d6d5296ad372
platformId: 7d2ac670-b126-1f00-af4d-14bab3ed3d39
---

# Lookup activity - Microsoft Fabric | Microsoft Learn

The Fabric Lookup activity can retrieve a dataset from any of the data sources supported by Microsoft Fabric. You can use it to dynamically determine which objects to operate on in a subsequent activity, instead of hard coding the object name. Some object examples are files and tables.

Lookup activity reads and returns the content of a configuration file or table. It also returns the result of executing a query or stored procedure. The output can be a singleton value or an array of attributes, which can be consumed in a subsequent copy, transformation, or control flow activities like ForEach activity.

## Prerequisites

To get started, you must complete the following prerequisites:

- You must have access to a Microsoft Fabric tenant with a provisioned [capacity](/en-us/fabric/enterprise/plan-capacity). You can [try Fabric with a free trial](../fundamentals/fabric-trial).
- A Fabric [workspace](../fundamentals/create-workspaces) assigned to that capacity.

## Add a lookup activity to a pipeline with UI

To use a Lookup activity in a pipeline, complete the following steps:

### Creating the activity

1. Create a new pipeline in your workspace.
2. Search for Lookup in the pipeline **Activities** pane, and select it to add it to the pipeline canvas.

    ![Screenshot of the Fabric UI with the Activities pane and Lookup activity highlighted.](media/lookup-activity/add-lookup-activity-to-pipeline.png)
3. Select the new Lookup activity on the canvas if it isn't already selected.

    ![Screenshot showing the General settings tab of the Lookup activity.](media/lookup-activity/lookup-activity-general-settings.png)

Refer to the [**General** settings](activity-overview#general-settings) guidance to configure the **General** settings tab.

### Lookup settings

Select the **Settings** tab, select an existing connection from the **Connection** dropdown, or create a new connection, and specify its configuration details.

![Screenshot showing the Lookup activity settings tab highlighting the tab, and where to choose a new connection.](media/lookup-activity/lookup-activity-settings.png)

The example in the previous image shows a Lakehouse connection, but each connection type has its own configuration details specific to the data source selected.

The **Preview data** button in the Lookup activity settings to view a sample of the data returned by your query.

![Screenshot showing the Lookup activity preview of selected data.](media/lookup-activity/lookup-activity-preview-data.png)

Preview data helps you:

- Validate that your Lakehouse table or query returns the expected columns and values
- Confirm whether the result is a **single row** or **multiple rows**
- Understand the output shape (`firstRow` vs `value`) before referencing it in [expressions](expression-language)

## Use the Lookup activity output

After the Lookup activity runs, it returns the results of your query in the **Output** tab (which should be the same data in the Preview data view). You can reference this output in downstream activities to drive dynamic, metadata‑driven pipelines.

![Screenshot showing the Lookup activity output after running.](media/lookup-activity/lookup-activity-output.png)

You'll be able to use the output of the Lookup activity via the [expression](expression-language) builder in subsequent activities.

The Lookup output is commonly used to:

- Control branching logic (for example, **If Condition** or **Switch**)
- Loop over rows using a **ForEach** activity

![Screenshot showing how to use the output of the Lookup activity.](media/lookup-activity/lookup-activity-output-expression.png)

This example showcases an If Condition activity using the Lookup activity's output.

## Supported capabilities

- The Lookup activity can return up to 5,000 rows; if the result set contains more records, the first 5,000 rows are returned.
- The Lookup activity output supports up to 4 MB in size; activity fails if the size exceeds the limit.
- The longest duration for Lookup activity before timeout is 24 hours.

Note

When you use query or stored procedure to look up data, make sure to return one and exact one result set. Otherwise, Lookup activity fails.

The following data sources are supported for Lookup activity.

| Category | Data store |
| --- | --- |
| **Azure** | [Azure Blob Storage](connector-azure-blob-storage-overview) |
|  | [Azure Cosmos DB for NoSQL](connector-azure-cosmosdb-for-nosql-overview) |
|  | [Azure Databricks](connector-azure-databricks-overview) |
|  | [Azure Data Explorer](connector-azure-data-explorer-overview) |
|  | [Azure Database for MySQL](connector-azure-database-for-mysql-overview) |
|  | [Azure Database for PostgreSQL](connector-azure-database-for-postgresql-overview) |
|  | [Azure Data Lake Storage Gen2](connector-azure-data-lake-storage-gen2-overview) |
|  | [Azure Files](connector-azure-files-overview) |
|  | [Azure SQL database](connector-azure-sql-database-overview) |
|  | [Azure SQL Managed Instance](connector-azure-sql-managed-instance-overview) |
|  | [Azure Synapse Analytics](connector-azure-synapse-analytics-overview) |
|  | [Azure Table Storage](connector-azure-table-storage-overview) |
| **Database** | [Amazon RDS for Oracle](connector-amazon-rds-for-oracle-overview) |
|  | [Amazon RDS for SQL Server](connector-amazon-rds-for-sql-server-overview) |
|  | [Amazon Redshift](connector-amazon-redshift-overview) |
|  | [IBM Db2 database](connector-ibm-db2-database-overview) |
|  | [Google BigQuery](connector-google-bigquery-overview) |
|  | [Greenplum for Pipeline](connector-greenplum-for-pipeline-overview) |
|  | [Informix For Pipeline](connector-informix-for-pipeline-overview) |
|  | [MariaDB](connector-mariadb-overview) |
|  | [Microsoft Access](connector-microsoft-access-overview) |
|  | [MySQL database](connector-mysql-database-overview) |
|  | [Oracle database](connector-oracle-database-overview) |
|  | [PostgreSQL database](connector-postgresql-overview) |
|  | [Presto](connector-presto-overview) |
|  | [SAP BW Open Hub Application Server](connector-sap-bw-open-hub-application-server-overview) |
|  | [SAP BW Open Hub Message Server](connector-sap-bw-open-hub-message-server-overview) |
|  | [SAP HANA database](connector-sap-hana-overview) |
|  | [SAP Table Application Server](connector-sap-table-application-server-overview) |
|  | [SAP Table Message Server](connector-sap-table-message-server-overview) |
|  | [Snowflake](connector-snowflake-overview) |
|  | [SQL Server database](connector-sql-server-database-overview) |
|  | [Teradata database](connector-teradata-database-overview) |
|  | [Vertica](connector-vertica-overview) |
| **File** | [Amazon S3](connector-amazon-s3-overview) |
|  | [Amazon S3 Compatible](connector-amazon-s3-compatible-overview) |
|  | [Folder](connector-folder-overview) |
|  | [FTP](connector-ftp-overview) |
|  | [Google Cloud Storage](connector-google-cloud-storage-overview) |
|  | [Hdfs for Pipeline](connector-hdfs-for-pipeline-overview) |
|  | [Oracle Cloud Storage](connector-oracle-cloud-storage-overview) |
|  | [SFTP](connector-sftp-overview) |
| **Generic protocol** | [HTTP](connector-http-overview) |
|  | [OData](connector-odata-overview) |
|  | [ODBC](connector-odbc-overview) |
| **Microsoft Fabric** | [Lakehouse](connector-lakehouse-overview) |
|  | [Data Warehouse](connector-data-warehouse-overview) |
|  | [KQL Database](connector-kql-database-overview) |
|  | [SQL database](connector-sql-database-overview) |
| **NoSQL** | [Cassandra](connector-cassandra-overview) |
| **Services and apps** | [Dataverse](connector-dataverse-overview) |
|  | Dynamics 365 |
|  | [Dynamics AX](connector-dynamics-ax-overview) |
|  | [Dynamics CRM](connector-dynamics-crm-overview) |
|  | [Salesforce objects](connector-salesforce-objects-overview) |
|  | [Salesforce Service Cloud](connector-salesforce-service-cloud-overview) |
|  | [ServiceNow](connector-servicenow-overview) |
|  | [SharePoint Online List](connector-sharepoint-online-list-overview) |

## Save and run or schedule the pipeline

Switch to the **Home** tab at the top of the pipeline editor and select the save button to save your pipeline. Select **Run** to run it directly or **Schedule** to schedule runs at specific times or intervals. For more information on pipeline runs, see: [schedule pipeline runs](pipeline-runs).

![Screenshot showing the Home tab in the pipeline editor with the tab name, Save, Run, and Schedule buttons highlighted.](includes/media/save-run-schedule-pipeline/save-run-schedule-pipeline.png)

After running, you can monitor the pipeline execution and view run history from the **Output** tab below the canvas.