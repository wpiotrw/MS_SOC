---
layout: Conceptual
title: Choose the right integration runtime configuration for your scenario with Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-integration-runtime-choose
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2026-05-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about the different integration runtime options and the recommended configuration when you're using Microsoft Purview.
locale: en-us
document_id: 6b76c3e8-7eb5-d9d4-4112-29fc1aea3fa3
document_version_independent_id: 6b76c3e8-7eb5-d9d4-4112-29fc1aea3fa3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-integration-runtime-choose.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-integration-runtime-choose
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-integration-runtime-choose.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f0f48fa4-6ae8-2bc7-3182-7f42fe42943c
---

# Choose the right integration runtime configuration for your scenario with Microsoft Purview | Microsoft Learn

The integration runtime (IR) is the compute infrastructure that Microsoft Purview uses to power data scan across different network environments. This article introduces the different types of integration runtime available in Microsoft Purview, and provides guidance on how to choose the right integration runtime configuration for your scenario.

## Types of integration runtimes

Purview provides the following types of integration runtimes:

- **Azure integration runtime**: The Azure integration runtime is a fully managed and elastic compute that you can use to scan Azure or non-Azure data sources. The Azure IR supports connections to data stores and compute services with publicly accessible endpoints. It's the default integration runtime that you don't need to create anything to get started.
- **Managed Virtual Network integration runtime**: You can create a Managed Virtual Network integration runtime, which resides in a Purview Managed Virtual Network. It can use private endpoints to securely connect to and scan the supported data sources. Learn more at [Managed Virtual Network and managed private endpoints](data-governance-private-endpoints-managed-virtual-network).
- **Self-hosted integration runtime**: The self-hosted integration runtime can be used to scan data sources in an on-premises network or a virtual network. You can install it on an on-premises machine or a virtual machine inside your private network. Learn more at [Create and manage self-hosted integration runtimes](data-map-integration-runtime-self-hosted).
- **Kubernetes supported self-hosted integration runtime**: This integration runtime is hosted on a Kubernetes cluster and can be used to scan data sources in an on-premises network or a virtual network. Kubernetes support improves overall performance and allows the integration runtime to scale with the job. Learn more at [Create and manage Kubernetes supported self-hosted integration runtimes](data-map-integration-runtime-kubernetes).
- **AWS integration runtime**: The AWS integration runtime is a fully managed and elastic computed hosted by Microsoft Purview in AWS. It's applicable when scanning Amazon data sources like S3, RDS.

## Choose the right integration runtime

Choose the right integration runtime for your needs. Consider your existing architecture and requirements for data integration. Also think about how to meet growing business needs and any future increase in workload.

The following considerations can help you make your decision:

1. **What data source types do you want to scan?**

    Check the supported data sources section to learn about the supported IR types for the data sources you want to scan.
2. **What’s the network access control on your data source?**

    Different data sources have different network firewall settings to protect them from random access over the internet. These settings apply to on-premises, cloud, and SaaS data stores. The following table lists some common firewall options. Choose the supported IR type according to your scenario.

    | Data source firewall | Azure IR | [Managed Virtual Network IR](data-governance-private-endpoints-managed-virtual-network) | [SHIR](data-map-integration-runtime-self-hosted) | [Kubernetes supported SHIR](data-map-integration-runtime-kubernetes) |
    | --- | --- | --- | --- | --- |
    | Allow public access | ✓ | ✓ | ✓ | ✓ |
    | Allow [Azure service](/en-us/azure/azure-sql/database/network-access-controls-overview) or [trusted service](/en-us/azure/storage/common/storage-network-security#exceptions) | ✓ | ✓ | ✓ | ✓ |
    | Allow access from specific Azure virtual network |  | ✓ (with managed private endpoint support) | ✓ | ✓ |
    | Allow specific IP / IP range |  |  | ✓ | ✓ |
    | Other on-premises or private network access |  |  | ✓ | ✓ |
3. **What’s the firewall setting of your Microsoft Purview?**

    Purview provides different network firewall options. Learn more from [Configure Microsoft Purview firewall](data-gov-classic-firewall). Choose the supported IR type according to your scenario.

    | Purview firewall | Azure IR | [Managed Virtual Network IR](data-governance-private-endpoints-managed-virtual-network) | [SHIR](data-map-integration-runtime-self-hosted) | [Kubernetes supported SHIR](data-map-integration-runtime-kubernetes) |
    | --- | --- | --- | --- | --- |
    | Enabled from all networks | ✓ | ✓ | ✓ | ✓ |
    | Disabled from all networks |  | ✓ (managed private endpoint required) | ✓ (need to create private endpoint from your network) | ✓ (need to create private endpoint from your network) |
4. **What level of security do you require during data transmission?**

    The integration runtime location defines the location of its back-end compute and where the scan operations are performed. For data residency consideration:

    - When you use Azure IR, Purview automatically detects the data source's location and uses the IR in that region. If Purview can't detect the region, it uses the Purview account's region.
    - When you use Managed Virtual Network IR, it runs in the region you configure for the managed virtual network.
    - When you use SHIR, you can fully decide the location in your on-premises or Azure virtual machines.

        To protect against, for example, man-in-the-middle attacks during data transmission, use a private endpoint and private link to ensure data security.
    - You can create managed private endpoints to your data stores when using Managed Virtual Network IR. The Purview service maintains the private endpoints within the managed virtual network.
    - You can also create private endpoints in your virtual network and the SHIR can use them to access data stores.
5. **What level of maintenance are you able to provide?**

    Maintaining infrastructure, servers, and equipment is one of the important tasks of the IT department of an enterprise. It usually takes much time and effort.

    - When using Azure IR and Managed Virtual Network IR, you don't need to worry about maintenance such as updates, patches, and versions. The Purview service takes care of all the maintenance efforts.
    - Because the SHIR is installed on your machines and the Kubernetes supported SHIR is on your Kubernetes clusters, you need to manage the maintenance.
        - The SHIR supports autoupdate to automatically get the latest version whenever there's' an update. Learn more from [Self-hosted integration runtime autoupdate and expiration](data-map-integration-runtime-self-hosted#autoupdate-version-vs-latest-version).
        - Currently, the [Kubernetes supported self-hosted integration runtime](data-map-integration-runtime-kubernetes) only supports manual updates.
6. **Performance and scalability**

    Use the fully managed and autoscaled Azure IR, Managed Virtual Network IR, or the Kubernetes-supported self-hosted integration runtime whenever applicable. By using elasticity, they can provide you with better performance and scalability, especially when scanning large-scale data systems.

## Hibernation of managed virtual network integration runtime

If the integration runtime is inactive (no scans on the integration runtime for more than 90 days), your Managed Virtual Network Integration Runtime automatically goes into hibernation. Its status shows as **Hibernated** when you select the integration runtime.

**What this change means for you**

1. When you run Test Connection on a hibernated integration runtime, the test connection fails. You see a message to try Test Connection after 15 minutes. By this time, your Managed Virtual Network returns to a normal state. After this, you can run your Test Connections and Scans normally.
2. When you run a scan directly by using **Run scan now** or **Edit Scan** options without running a Test Connection first from a hibernated Integration Runtime, or you run a scan through API, you see a message that this scan takes up to 15 extra minutes. This extra time is for the hibernated Integration Runtime to wake up and the scan process to begin. You see your scan status as **Queued\_Waking Up IR** instead of **Queued** state that you see in case of normal scan. After the first scan, you can run all your following scans normally.

## Supported data sources

The following table shows all the data sources that Purview scan supports, and the supported integration runtime types.

| Category | Supported data store | Azure IR/AWS IR | [Managed Virtual Network IR](data-governance-private-endpoints-managed-virtual-network) | [SHIR](data-map-integration-runtime-self-hosted) | [Kubernetes SHIR](data-map-integration-runtime-kubernetes) |
| --- | --- | --- | --- | --- | --- |
| Azure | [Multiple sources](register-scan-azure-multiple-sources) | ✓ |  |  |  |
|  | [Azure Blob Storage](register-scan-azure-blob-storage-source) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
|  | [Azure Cosmos DB (API for NoSQL)](register-scan-azure-cosmos-database) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
|  | [Azure Data Explorer](register-scan-azure-data-explorer) | ✓ | ✓ (v2 only) | ✓ | ✓ |
|  | [Azure Data Lake Storage Gen1](register-scan-adls-gen1) | ✓ | ✓ (v2 only) | ✓ |  |
|  | [Azure Data Lake Storage Gen2](register-scan-adls-gen2) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
|  | [Azure Database for MySQL](register-scan-azure-mysql-database) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
|  | [Azure Database for PostgreSQL](register-scan-azure-postgresql) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
|  | [Azure Databricks Hive Metastore](register-scan-azure-databricks) |  |  | ✓ | ✓ |
|  | [Azure Databricks Unity Catalog](register-scan-azure-databricks-unity-catalog) | ✓ | ✓ (v2 only, including managed private endpoint) |  | ✓ |
|  | [Azure Dedicated SQL pool (formerly SQL DW)](register-scan-azure-synapse-analytics) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
|  | [Azure Files](register-scan-azure-files-storage-source) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
|  | [Azure SQL Database](register-scan-azure-sql-database) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
|  | [Azure SQL Managed Instance](register-scan-azure-sql-managed-instance) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
|  | [Azure Synapse Analytics (Workspace)](register-scan-synapse-workspace) | ✓ | ✓ (including managed private endpoint) | ✓ | ✓ |
| Database | [Amazon RDS](register-scan-amazon-rds) | ✓ |  |  | ✓ |
|  | [Amazon Redshift](register-scan-amazon-redshift) | ✓ |  |  | ✓ |
|  | [Cassandra](register-scan-cassandra-source) | ✓ | ✓ (v2 only) | ✓ | ✓ |
|  | [Db2](register-scan-db2) |  |  | ✓ | ✓ |
|  | [Google BigQuery](register-scan-google-bigquery-source) |  |  | ✓ | ✓ |
|  | [Hive Metastore Database](register-scan-hive-metastore-source) |  |  | ✓ | ✓ |
|  | [MongoDB](register-scan-mongodb) |  |  | ✓ | ✓ |
|  | [MySQL](register-scan-mysql) | ✓ | ✓ (v2 only) | ✓ | ✓ |
|  | [Oracle](register-scan-oracle-source) |  |  | ✓ |  |
|  | [PostgreSQL](register-scan-postgresql) | ✓ | ✓ (v2 only) | ✓ | ✓ |
|  | [SAP Business Warehouse](register-scan-sap-bw) |  |  | ✓ | ✓ |
|  | [SAP HANA](register-scan-sap-hana) |  |  | ✓ | ✓ |
|  | [Snowflake](register-scan-snowflake) | ✓ | ✓ (v2 only, including managed private endpoint) | ✓ |  |
|  | [SQL Server](register-scan-on-premises-sql-server) |  |  | ✓ | ✓ |
|  | [SQL Server on Azure-Arc](register-scan-azure-arc-enabled-sql-server) |  |  | ✓ | ✓ |
|  | [Teradata](register-scan-teradata-source) |  |  | ✓ |  |
| File | [Amazon S3](register-scan-amazon-s3) | ✓ |  |  |  |
|  | [HDFS](register-scan-hdfs) |  |  | ✓ | ✓ |
| Services and apps | [Dataverse](register-scan-dataverse) | ✓ | ✓ (v2 only) |  | ✓ |
|  | [Erwin](register-scan-erwin-source) |  |  | ✓ |  |
|  | [Looker](register-scan-looker-source) | ✓ | ✓ (v2 only) | ✓ | ✓ |
|  | [Fabric](register-scan-fabric-tenant) | ✓ | ✓ (v2 only) | ✓ | ✓ |
|  | [Power BI](register-scan-power-bi-tenant) | ✓ | ✓ (v2 only) | ✓ | ✓ |
|  | [Qlik Sense](register-scan-qlik-sense) | ✓ | ✓ (v2 only) |  | ✓ |
|  | [Salesforce](register-scan-salesforce) | ✓ | ✓ (v2 only) | ✓ | ✓ |
|  | [SAP ECC](register-scan-sapecc-source) |  |  | ✓ | ✓ |
|  | [SAP S/4HANA](register-scan-saps4hana-source) |  |  | ✓ | ✓ |
|  | [Tableau](register-scan-tableau) | ✓ | ✓ (v2 only) |  | ✓ |