---
layout: Conceptual
title: Data quality troubleshooting in Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-troubleshooting
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-02-23T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article provides a list of frequently encountered issues in Microsoft Purview Unified Catalog data quality and how to resolve them.
locale: en-us
document_id: 9d529159-9c8b-233b-aed9-31b4749b0c5f
document_version_independent_id: 9d529159-9c8b-233b-aed9-31b4749b0c5f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-troubleshooting.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-troubleshooting
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-troubleshooting.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5c1f3bfc-fced-4ad1-b4e6-b7200832734d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/5017978e-5a12-4c31-bdfd-1880eb1a780b
platformId: 8bbcf5a3-468a-05fb-f781-0c2916f4405b
---

# Data quality troubleshooting in Microsoft Purview Unified Catalog | Microsoft Learn

This article describes common questions and symptoms of errors, along with possible resolutions:

#### Why do I see an invalid source error from the scanning job?

- You might see this error for two reasons:
    - The delta table doesn't exist in the location.
    - The data in the file aren't in a valid delta format.

#### I'm setting up data quality scans for my Microsoft Fabric delta tables. I see all data assets in the data quality view, I select one asset and apply rules for data quality scanning, but the scan fails.

- Your data quality scanning might fail for several reasons:
    - The data in tables aren't in the correct delta format. Make sure that your data are in delta format.
        - The Data Map scan didn't run successfully. Rerun the Data Map scan.
        - You need to [delete any previous data quality runs for the data asset](unified-catalog-data-quality-scan#delete-previous-data-quality-scans-and-history).

#### Why do I see the error message, "No connection can be used. Try to create connection first."?

- To profile data or to run data quality scanning, you first need to configure a data source connection. This alert disappears after you [create a data source connection](unified-catalog-data-quality-supported-sources-connection).

#### Why is the total count of profiled data less than the total count in my Microsoft Azure Data Lake Storage Gen2 delta table?

- Microsoft Purview Data Quality uses a **1 million** sample size for profiling. This sample is taken **randomly**. If your delta table has more than 1 million records, the total count doesn't match.

#### Why do I see an action about data quality score missing for a data product, but I see the score in the data product when I browsed the data product view?

- When you created the action, there wasn't any data quality score for that data product. Data quality scanning ran after you created the action and the score published for the data product. Close the action once the remediation is done to avoid confusion.

#### Data quality rule creation from "Suggest rules" throws an error about a "date" column when trying to add all 30 suggested rules

- This error occurs because the schema data type is **unsupported** in the data quality schema view. You can change the **data type** to **date** by selecting the **schema management** toggle and saving it. After you change the data type, you should be able to add the rule.

#### When trying to add all suggested rules, why do I see the error "ObserverId already exists"?

- Most likely, the same or identical rule is already added to a column. When you try to add the same or identical rule to a column, the application throws this error message.

#### Why is my scheduled job skipping instead of running? I see **Skipped** for data quality scanning jobs.

- The data quality job checks and runs data quality only if there are changes since the last run. It checks the delta history. **Skipped** means there are no changes in the data since last run, and the spark run for data quality isn't performed. **Skipped** doesn't mean failed.

#### When I select profile data tab, I see number of columns preselected. Can I change the selected columns?

- Microsoft Purview Data Quality uses an AI assisted profiling solution. The Microsoft Purview Data Profiling AI selects the preselected columns. You can deselect those columns and reselect based on criticality of the columns, and select **Save and run** to run profiling.

#### Why can't I select some of the data assets from data quality asset list page to profile and scan?

- There are a few reasons:
    - Those data assets are published from unsupported data sources.
    - The file format of those data assets isn't supported.

#### Why is my profiling job failing for the supported data sources?

- Check the schema to make sure that there's no column name with spaces. The current version doesn't support column names with spaces.

#### Why can't I run data quality scanning and data profiling for CSV, TSV, and text files?

- Data Quality currently supports the Delta format of Parquet, Delta, Iceberg ORC, and Iceberg AVRO. Purview Data Quality doesn't support CSV, TSV, and text files.

#### Why don't I see the data quality freshness rule in the rule list?

- Microsoft Azure SQL tables don't support data quality freshness. If your data asset is an Azure SQL table, the freshness rule doesn't appear in the list for selection and application to the data asset.

#### Why do I see datatype Undefined for some columns of a data asset schema in a data quality schema page?

- It seems the data type for all columns isn't identified correctly. You can import the schema to resolve the issue (to update the datatype). Select the schema menu item from the data quality overview page, select the **Schema management** toggle, and select **Import schema**. After importing the schema, select the schema management toggle again to save the updated schema.
- Microsoft Azure SQL tables don't support data quality freshness. If your data asset is an Azure SQL table, the freshness rule doesn't appear in the list for selection and application to the data asset.

#### My data quality scan job failed. I see an error message 'Internal service error occurred, please retry, or contact Microsoft support.' What should I do to troubleshoot?

- Many reasons can cause the scan to fail with this error message:
    - You're not authorized to perform the current operation for the workspace that you're trying to access for the data quality scan.
    - Error code 403, meaning access to data sources is forbidden temporarily.
    - Granted access to the data source for your managed identity (MSI) expired.
        - Microsoft Purview managed identity (MSI) needs contributor access to the Fabric workspace. If you don't provide the contributor access for the Microsoft Purview MSI to the Fabric workspace, the data quality scan fails.

#### Why am I getting delta format error even though I'm using delta format?

- We support Spark 3.4 Delta 2.4. Make sure that you're using delta lake version 2.4.

#### Why am I seeing the error when I selected a reference data asset to configure **Table lookup rule**?

- You selected a data asset that isn't part linked or referred to a data product under the same governance domain. To select the right data asset:
    - Select **select reference table**, as indicated in this image:

        ![Screenshot of lookup data asset error.](media/data-quality-self-help/dq-table-lookup-error.png)
    - Cancel current selection, as shown in the following image:

        ![Screenshot of selecting correct data asset.](media/data-quality-self-help/dq-select-correct-data-asset.png)
    - After canceling the current selection, select another asset.

#### How can I configure access to data source for Microsoft Purview MSI?

- Here's [MSI configuration guide.](data-map-data-sources-configure-azure-msi) You find the details in this document.

#### All our data sources are behind the private end point (in virtual network), Can Microsoft Purview access data in virtual network for data quality scanning?

- Yes, Microsoft Purview supports Managed Virtual Network for data quality scanning. See the [Microsoft Purview managed virtual network configuration article](unified-catalog-data-quality-managed-virtual-networks).

#### Where can I find documentation about expression function to create custom rules?

- Find information and examples at [Create data quality rules](unified-catalog-data-quality-rules).

#### Why is my data quality scan for Fabric Lakehouse table failing?

- Many reasons can cause the failure:
    - Make sure that your lakehouse tables are discoverable in Data Map with schema.
    - Make sure that you're using SPN for Data Map scan and MSI for data quality scan.

        - Make sure that you configured the data quality connection with MSI.
        - Make sure that Microsoft Purview MSI has contributor access to your Fabric workspace.
        - Enable Microsoft OneLake setting: Users can access data stored in OneLake with apps external to Fabric.

        ![Screenshot for onelake setting.](media/dq-fabric/fabric_admin_setting.png)
    - Learn how to [configure data quality for Fabric Lakehouse](unified-catalog-data-quality-fabric-lakehouse).
    - Learn how to [configure a Data Map scan setup for Fabric](register-scan-fabric-tenant).

#### Why can't users enable managed virtual network (VNET) for data quality configuration on Microsoft Purview for Databricks or Synapse, or any other supported data sources?

- **Problem**: After selecting the **Enable managed Vnet** checkbox and receiving approval, no changes occur on the Microsoft Purview side. Subsequent attempts to create a connection fail with no request sent to the sources (for example, Azure Databricks, Synpase, Data Lake Storage Gen2) for approval.
- **Resolution**: This problem occurs when you delete the Managed Private Endpoint (MPE) after configuring it. Currently, if you update or delete the MPE directly from the source after initial approval, the Data Quality system can't track the MPE status change. To resolve this problem, contact Microsoft support.

#### Schema is blank or columns are missing

- Import the schema from the **Data Quality** page to ensure that all columns, including any missing ones, are properly loaded and to resolve the issue. After importing the schema, perform a hard refresh to avoid reloading cached or outdated information.
- Depending on the extent of the schema changes, you might need to remove the asset from the data asset data quality page or the data product page and then re-add it from the Data Map to fully resolve the issue.
- Rule bindings use the technical column name as the key, not just the DisplayName. If the column’s name changed, or the asset’s schema cached in data quality still references the old technical name, subsequent runs fail because the rule can’t find the column.
- Data product assets don’t auto refresh when you update metadata in Data Map (owner, description, lineage, and relevant here, schema). You need to manually refresh the asset inside catalog management so that data quality sees the latest column set.