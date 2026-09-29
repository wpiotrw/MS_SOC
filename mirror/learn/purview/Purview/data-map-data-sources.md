---
layout: Conceptual
title: Data sources that connect to Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-data-sources
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.date: 2026-07-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about the data sources and file types that can connect to Microsoft Purview Data Map.
locale: en-us
document_id: 54b8544c-fc06-7da0-1d87-55a4e47a8e9e
document_version_independent_id: 54b8544c-fc06-7da0-1d87-55a4e47a8e9e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-data-sources.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-data-sources
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-data-sources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/bad69977-db6a-44f3-b752-d2bee7de49ca
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31d7aff-61be-45e2-a324-a578cf0c3360
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 05669664-73ef-9333-9632-0a8b9ad15b11
---

# Data sources that connect to Microsoft Purview Data Map | Microsoft Learn

This article lists the supported data sources, file types, and scanning concepts in Microsoft Purview Data Map.

## Data source listing by type

The tables below show all data sources that have technical metadata available in Microsoft Purview Data Map, along with other supported capabilities. Select a data source name in the **Data source** column for instructions on connecting that source to Data Map.

- Microsoft Azure
- Database
- File
- Services and apps

### Azure

Azure resources are only available in the same tenant as your Microsoft Purview account, unless noted otherwise on each data source's page.

| Data source | Can automatically apply classifications | Can apply sensitivity labels to Data Map assets | Can apply policies | Data lineage | Accessible in live view |
| --- | --- | --- | --- | --- | --- |
| *Select link for connection and scanning instructions.* | *Select **Yes** for scanning instructions. Learn how [classifications are applied during scanning](data-map-classification-apply-auto).* | *Learn about [sensitivity labeling (preview)](data-map-sensitivity-labels).* | *Select **Yes** to see supported policies; for example, data owner, self-service access, or protection.* | *Select **Yes** for details.* | *Learn about [live view](data-gov-live-view).* |
| [Multiple sources](register-scan-azure-multiple-sources) | [Yes](register-scan-azure-multiple-sources#scan) | Source dependent | [Yes](register-scan-azure-multiple-sources#policies) | No | Limited |
| [Azure Blob Storage](register-scan-azure-blob-storage-source) | [Yes](register-scan-azure-blob-storage-source#scan) | Yes | [Yes](register-scan-azure-blob-storage-source#policies) (preview) | Limited\* | Yes |
| [Azure Cosmos DB for SQL API](register-scan-azure-cosmos-database) | [Yes](register-scan-azure-cosmos-database#scan) | Yes | No | No\* | No |
| [Azure Data Explorer](register-scan-azure-data-explorer) | [Yes](register-scan-azure-data-explorer#scan) | Yes | No | No\* | No |
| [Azure Data Factory](data-map-lineage-azure-data-factory) | No | No | No | [Yes](data-map-lineage-azure-data-factory) | No |
| [Azure Data Lake Storage Gen2](register-scan-adls-gen2) | [Yes](register-scan-adls-gen2#scan) | Yes | [Yes](register-scan-adls-gen2#policies) (preview) | Limited\* | Yes |
| [Azure Data Share](how-to-link-azure-data-share) | No | No | No | [Yes](how-to-link-azure-data-share) | No |
| [Azure Database for MySQL](register-scan-azure-mysql-database) | [Yes](register-scan-azure-mysql-database#scan) | Yes | No | No\* | No |
| [Azure Database for PostgreSQL](register-scan-azure-postgresql) | [Yes](register-scan-azure-postgresql#scan) | Yes | No | No\* | No |
| [Azure Databricks Hive Metastore](register-scan-azure-databricks) | [Yes](register-scan-azure-databricks#scan)\*\* | No | No | [Yes](register-scan-azure-databricks#lineage) | No |
| [Azure Databricks Unity Catalog](register-scan-azure-databricks-unity-catalog) | [Yes](register-scan-azure-databricks-unity-catalog#scan)\*\*\* | No | No | [Yes](register-scan-azure-databricks-unity-catalog#lineage) | No |
| [Azure Dedicated SQL pool (formerly SQL DW)](register-scan-azure-synapse-analytics) | [Yes](register-scan-azure-synapse-analytics#scan) | No | No | No\* | No |
| [Azure Files](register-scan-azure-files-storage-source) | [Yes](register-scan-azure-files-storage-source#scan) | Yes | No | Limited\* | No |
| [Azure Machine Learning](register-scan-azure-machine-learning) | No | No | No | [Yes](register-scan-azure-machine-learning) | No |
| [Azure SQL Database](register-scan-azure-sql-database) | [Yes](register-scan-azure-sql-database#scope-and-run-the-scan) | Yes | [Yes](register-scan-azure-sql-database#set-up-policies)^ | [Yes (Preview)](register-scan-azure-sql-database#extract-lineage-preview) | Yes |
| [Azure SQL Managed Instance](register-scan-azure-sql-managed-instance) | [Yes](register-scan-azure-sql-managed-instance#scan) | Yes | [Yes](register-scan-azure-sql-managed-instance#set-up-access-policies) | No\* | No |
| [Azure Synapse Analytics (Workspace)](register-scan-synapse-workspace) | [Yes](register-scan-synapse-workspace) | Yes | No | [Yes - Synapse pipelines](data-map-lineage-azure-synapse-analytics) | No |

\* Besides the lineage on assets within the data source, lineage is also supported if dataset is used as a source/sink in [Data Factory](data-map-lineage-azure-data-factory) or [Synapse pipeline](data-map-lineage-azure-synapse-analytics).

\*\* Classification support for only Unity Catalog in Azure Databricks data source.

\*\*\* Custom classification isn't supported for Azure Databricks Unity Catalog source.

^ Protection policies aren't supported for Azure SQL Database.

### Database

| Data source | Can automatically apply classifications | Can apply sensitivity labels to Data Map assets | Can apply policies | Data lineage | Accessible in live view |
| --- | --- | --- | --- | --- | --- |
| *Select link for connection and scanning instructions.* | *Select **Yes** for scanning instructions. Learn how [classifications are applied during scanning](data-map-classification-apply-auto).* | *Learn about [sensitivity labeling (preview)](data-map-sensitivity-labels).* | *Select **Yes** to see supported policies; for example, data owner, self-service access, or protection.* | *Select **Yes** for details.* | *Learn about [live view](data-gov-live-view).* |
| [Amazon RDS](register-scan-amazon-rds) | [Yes](register-scan-amazon-rds#scan-an-amazon-rds-database) | No | No | No | No |
| [Amazon Redshift](register-scan-amazon-redshift) | No | No | No | No | No |
| [Cassandra](register-scan-cassandra-source) | No | No | No | [Yes](register-scan-cassandra-source#lineage) | No |
| [Db2](register-scan-db2) | No | No | No | [Yes](register-scan-db2#lineage) | No |
| [Google BigQuery](register-scan-google-bigquery-source) | No | No | No | [Yes](register-scan-google-bigquery-source#lineage) | No |
| [Hive Metastore Database](register-scan-hive-metastore-source) | No | No | No | [Yes*](register-scan-hive-metastore-source#lineage) | No |
| [MongoDB](register-scan-mongodb) | No | No | No | No | No |
| [MySQL](register-scan-mysql) | No | No | No | [Yes](register-scan-mysql#lineage) | No |
| [Oracle](register-scan-oracle-source) | [Yes](register-scan-oracle-source#scan) | No | No | [Yes*](register-scan-oracle-source#lineage) | No |
| [PostgreSQL](register-scan-postgresql) | No | No | No | [Yes](register-scan-postgresql#lineage) | No |
| [SAP Business Warehouse](register-scan-sap-bw) | No | No | No | No | No |
| [SAP HANA](register-scan-sap-hana) | No | No | No | No | No |
| [Snowflake](register-scan-snowflake) | [Yes](register-scan-snowflake#scan) | Yes | No | [Yes*](register-scan-snowflake#lineage) | No |
| [SQL Server](register-scan-on-premises-sql-server) | [Yes](register-scan-on-premises-sql-server#scan) | Yes | No | No\* | No |
| [SQL Server on Azure-Arc](register-scan-azure-arc-enabled-sql-server) | [Yes](register-scan-azure-arc-enabled-sql-server#scan) | No | [Yes](register-scan-azure-arc-enabled-sql-server#access-policy) | No\* | No |
| [Teradata](register-scan-teradata-source) | [Yes](register-scan-teradata-source#scan) | No | No | [Yes*](register-scan-teradata-source#lineage) | No |

\* Besides the lineage on assets within the data source, lineage is also supported if dataset is used as a source/sink in [Data Factory](data-map-lineage-azure-data-factory) or [Synapse pipeline](data-map-lineage-azure-synapse-analytics).

### File

| Data source | Can automatically apply classifications | Can apply sensitivity labels to Data Map assets | Can apply policies | Data lineage | Accessible in live view |
| --- | --- | --- | --- | --- | --- |
| *Select link for connection and scanning instructions.* | *Select **Yes** for scanning instructions. Learn how [classifications are applied during scanning](data-map-classification-apply-auto).* | *Learn about [sensitivity labeling (preview)](data-map-sensitivity-labels).* | *Select **Yes** to see supported policies; for example, data owner, self-service access, or protection.* | *Select **Yes** for details.* | *Learn about [live view](data-gov-live-view).* |
| [Amazon S3](register-scan-amazon-s3) | [Yes](register-scan-amazon-s3#create-a-scan-for-one-or-more-amazon-s3-buckets) | No | No | Limited\* | No |
| [Hadoop Distributed File System (HDFS)](register-scan-hdfs) | [Yes](register-scan-hdfs#scan) | No | No | No | No |

\* Besides the lineage on assets within the data source, lineage is also supported if dataset is used as a source/sink in [Data Factory](data-map-lineage-azure-data-factory) or [Synapse pipeline](data-map-lineage-azure-synapse-analytics).

### Services and apps

| Data source | Can automatically apply classifications | Can apply sensitivity labels to Data Map assets | Can apply policies | Data lineage | Accessible in live view |
| --- | --- | --- | --- | --- | --- |
| *Select link for connection and scanning instructions.* | *Select **Yes** for scanning instructions. Learn how [classifications are applied during scanning](data-map-classification-apply-auto).* | *Learn about [sensitivity labeling (preview)](data-map-sensitivity-labels).* | *Select **Yes** to see supported policies; for example, data owner, self-service access, or protection.* | *Select **Yes** for details.* | *Learn about [live view](data-gov-live-view).* |
| [Airflow](data-map-lineage-airflow) | No | No | No | [Yes](data-map-lineage-airflow) | No |
| [Dataverse](register-scan-dataverse) | [Yes](register-scan-dataverse#scan) | Yes | No | No | No |
| [Erwin](register-scan-erwin-source) | No | No | No | [Yes](register-scan-erwin-source#lineage) | No |
| [Fabric](register-scan-fabric-tenant) | No | No | No | Yes | [Yes](data-gov-live-view) |
| [Looker](register-scan-looker-source) | No | No | No | [Yes](register-scan-looker-source#lineage) | No |
| [Power BI](register-scan-power-bi-tenant) | No | No | No | [Yes](data-map-lineage-power-bi) | [Yes**](data-gov-live-view) |
| [Qlik Sense](register-scan-qlik-sense) | No | No | No | No | No |
| [Salesforce](register-scan-salesforce) | No | No | No | No | No |
| [SAP ECC](register-scan-sapecc-source) | No | No | No | [Yes*](register-scan-sapecc-source#lineage) | No |
| [SAP S/4HANA](register-scan-saps4hana-source) | No | No | No | [Yes*](register-scan-saps4hana-source#lineage) | No |
| [Tableau](register-scan-tableau) | No | No | No | No | No |

\* Besides the lineage on assets within the data source, lineage is also supported if dataset is used as a source/sink in [Data Factory](data-map-lineage-azure-data-factory) or [Synapse pipeline](data-map-lineage-azure-synapse-analytics).

\*\* Power BI items in a Fabric tenant are available using live view.

Note

Currently, the Microsoft Purview Data Map can't scan an asset that has `/`, `\`, or `#` in its name. To scope your scan and avoid scanning assets that have those characters in the asset name, use the example in [Register and scan an Azure SQL Database](register-scan-azure-sql-database#create-the-scan).

Important

If you plan on using a self-hosted integration runtime, scanning some data sources requires extra setup on the self-hosted integration runtime machine. For example, JDK, Microsoft Visual C++ Redistributable, or specific driver. For your source, **[refer to each source article for prerequisite details.](data-map-data-sources)** Any requirements are listed in the **Prerequisites** section.

## Data Map scanner regions

The following list shows the Azure data source (data center) regions where the Data Map scanner runs. If your Azure data source is in a region outside of this list, the scanner runs in the region of your Microsoft Purview instance.

- Australia East
- Australia Southeast
- Brazil South
- Canada Central
- Canada East
- Central India
- China North 3
- East Asia
- East US
- East US 2
- France Central
- Germany West Central
- Japan East
- Korea Central
- North Central US
- North Europe
- Qatar Central
- South Africa North
- South Central US
- Southeast Asia
- Switzerland North
- UAE North
- UK South
- USGov Virginia
- West Central US
- West Europe
- West US
- West US 2
- West US 3

## File types supported for scanning

The file types listed in the following section support scanning, schema extraction, and classification where applicable. Additionally, Data Map supports [custom file extensions and custom parsers](data-map-scan-rule-set#create-a-custom-file-type).

**Structured file formats supported by extension include scanning, schema extraction, and asset and column level classification:**

- AVRO
- CSV
- GZIP
- JSON
- ORC
- PARQUET\*
- PSV
- SSV
- TSV
- TXT
- XML

\*For noncompressed PARQUET files, all Parquet formats are supported. For compressed PARQUET files, only snappy Parquet format is supported.

**Document file formats supported by extension include scanning and asset level classification:**

- DOC
- DOCM
- DOCX
- DOT
- ODP
- ODS
- ODT
- PDF
- POT
- PPS
- PPSX
- PPT
- PPTM
- PPTX
- XLC
- XLS
- XLSB
- XLSM
- XLSX
- XLT

Note

**Known limitations:**

- The Microsoft Purview Data Map scanner only supports schema extraction for the structured file types listed in the previous section.
- For AVRO, ORC, and PARQUET file types, the scanner doesn't support schema extraction for files that contain complex data types (for example, MAP, LIST, STRUCT).
- For noncompressed PARQUET files, all Parquet formats are supported. For compressed PARQUET files, only snappy Parquet format is supported for schema extraction and classification.
- For GZIP file types, the GZIP must be mapped to a single CSV file within. GZIP files are subject to system and custom classification rules. The scanner currently doesn't support scanning a GZIP file mapped to multiple files within, or any file type other than CSV.
- For Parquet files, if you're using a self-hosted integration runtime, you need to install the **64-bit JRE 11 (Java Runtime Environment) or OpenJDK** on your IR machine. See the [Java runtime installation guide](data-map-integration-runtime-self-hosted#java-runtime-environment-installation).
- The Delta format isn't supported. If you're scanning the Delta format directly from storage data source like Microsoft Azure Data Lake Storage Gen2, the set of Parquet files from the delta format are parsed and handled as resource set as described in [Understanding resource sets](data-map-resource-sets). The columns used for partitioning aren't recognized as part of the schema for the resource set.

- Unsupported Parquet encodings: Microsoft Purview doesn't support schema extraction for Parquet files that use run-length encoding (RLE) in Microsoft Fabric Lakehouse. Tables containing RLE-encoded columns might fail to extract schema metadata, including tables, columns, and data types. The process still discovers asset-level metadata (L1). To enable full schema extraction, re-create the affected tables by using a supported encoding format, such as dictionary or plain encoding.

**For delimited file types (CSV, PSV, SSV, TSV, TXT):**

- Delimited files with only one column can't be determined to be CSV files and have no schema.
- Data type detection isn't supported. The data type is listed as "string" for all columns.
- The only supported delimiters are comma(‘,’), semicolon(‘;’), vertical bar(‘|’), and tab(‘\t’).
- Delimited files with less than three rows can't be determined to be CSV files if they're using a custom delimiter. For example, files with ~ delimiter and less than three rows can't be determined to be CSV files.
- If a field contains double quotes, the double quotes can only appear at the beginning and end of the field and must be matched. Double quotes that appear in the middle of the field or appear at the beginning and end but aren't matched are recognized as bad data and no schema is parsed from the file. Rows that have different number of columns than the header row are judged as error rows. The numbers of error rows divided by the numbers of rows sampled must be less than 0.1.

## Schema extraction

For data sources that support schema extraction during scan, the number of columns doesn't directly truncate the asset schema.

## Nested data

Nested data is only supported for JSON content. For all system supported file types, if there's nested JSON content in a column, then the scanner parses the nested JSON data and surfaces it within the schema tab of the asset.

Nested data, or nested schema parsing, isn't supported in SQL. A column with nested data will be reported and classified as is, and subdata won't be parsed.

## Sampling data for classification

In Data Map terminology,

- L1 scan: Extracts basic information and metadata like file name, size, and fully qualified name.
- L2 scan: Extracts schema for structured file types and database tables.
- L3 scan: Extracts schema where applicable and subjects the sampled file to system and custom classification rules.

Learn more about [customizing the scan levels](data-map-scan-ingestion#customize-scan-level).

For all structured file formats, the Microsoft Purview Data Map scanner samples files in the following way:

- For structured file types, it samples the top 128 rows in each column or the first 1 MB, whichever is lower.
- For document file formats, it samples the first 20 MB of each file.
- If a document file is larger than 20 MB, the scanner doesn't perform a deep scan (subject to classification). In that case, Microsoft Purview captures only basic metadata like file name and fully qualified name.
- For **tabular data sources (SQL)**, it samples the top 128 rows.
- For **Azure Cosmos DB for NoSQL**, up to 300 distinct properties from the first 10 documents in a container are collected for the schema. For each property, the scanner samples values from up to 128 documents or the first 1 MB.
- For unstructured data formats, such as DOCX files, there's no requirement to meet a condition of eight distinct values. The presence of a single relevant keyword is sufficient for classification.

## Resource set file sampling

If a folder or group of partition files matches a system resource set policy or a customer-defined resource set policy, Data Map detects it as a *resource set*. If the scanner detects a resource set, it samples each folder it contains. For more information about resource sets, see [Resource sets in Microsoft Purview Data Map](data-map-resource-sets).

File sampling for resource sets by file types:

- **Delimited files (CSV, PSV, SSV, TSV)**: The scanner samples 1 in 100 files (L3 scan) within a folder or group of partition files that are considered as a resource set.
- **Data Lake file types (Parquet, Avro, Orc)**: The scanner samples 1 in 18,446,744,073,709,551,615 (long max) files (L3 scan) within a folder or group of partition files that are considered as a resource set.
- **Other structured file types (JSON, XML, TXT)**: The scanner samples 1 in 100 files (L3 scan) within a folder or group of partition files that are considered as a resource set.
- **SQL objects and Azure Cosmos DB entities**: The scanner L3 scans each file.
- **Document file types**: The scanner L3 scans each file. Resource set patterns don't apply to these file types.