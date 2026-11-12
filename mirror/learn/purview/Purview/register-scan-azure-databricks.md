---
layout: Conceptual
title: Connect to and manage Azure Databricks in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-databricks
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to connect to Azure Databricks in Microsoft Purview, and how to use Microsoft Purview to scan and manage your Azure Databricks source..
locale: en-us
document_id: f990def2-f24a-5fc6-1ed2-ea1afd62b38a
document_version_independent_id: f990def2-f24a-5fc6-1ed2-ea1afd62b38a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-databricks.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-databricks
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-databricks.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/545d40c6-c50c-444b-b422-1c707eeab28e
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b908d601-32e8-445a-b044-a507b5d1689e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 8d1f95fd-b78b-59de-8364-be671c8cdcba
---

# Connect to and manage Azure Databricks in Microsoft Purview | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register Azure Databricks, and how to authenticate and interact with Azure Databricks in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

Note

This connector brings metadata from Azure Databricks workspace-scoped Hive metastore. To scan metadata in [Azure Databricks Unity Catalog](/en-us/azure/databricks/data-governance/unity-catalog/), refer to [Azure Databricks Unity Catalog connector](register-scan-azure-databricks-unity-catalog).

When scanning Azure Databricks Hive metastore, Microsoft Purview supports:

- Extracting technical metadata, including:

    - Azure Databricks workspace
    - Hive server
    - Databases
    - Tables including the columns, foreign keys, unique constraints, and storage description
    - Views including the columns and storage description
- Fetching relationship between external tables and Azure Data Lake Storage Gen2/Azure Blob assets (external locations).
- Fetching static lineage between tables and views based on the view definition.

When setting up scan, you can choose to scan the entire Hive metastore, or scope the scan to a subset of schemas.

Compared to scanning via generic [Hive Metastore connector](register-scan-hive-metastore-source) if you use it to scan Azure Databricks earlier:

- You can directly set up scan for Azure Databricks workspaces without direct HMS access. It uses Databricks personal access token for authentication and connects to a cluster to perform scan.
- The Databricks workspace info is captured.
- The relationship between tables and storage assets is captured.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

When you delete an object from the data source, the subsequent scan doesn't automatically remove the corresponding asset in Purview.

## Prerequisites

- You must have an Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- You must have an active [Microsoft Purview account](create-microsoft-purview-portal).
- You need an Azure Key Vault, and to [grant Microsoft Purview permissions to access secrets](data-map-data-scan-credentials#grant-microsoft-purview-access-to-your-azure-key-vault).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- Set up the latest [self-hosted integration runtime](https://go.microsoft.com/fwlink/?linkid=2246619). For more information, see [Create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted). The minimal supported self-hosted Integration Runtime version is 5.20.8227.2.

    - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
    - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
- In your Azure Databricks workspace:

    - [Generate a personal access token](/en-us/azure/databricks/dev-tools/auth#--azure-databricks-personal-access-tokens), and store it as a secret in Azure Key Vault.
    - [Create a cluster](/en-us/azure/databricks/clusters/create-cluster). Note the cluster ID - you can find it in Azure Databricks workspace -&gt; Compute -&gt; your cluster -&gt; Tags -&gt; Automatically added tags -&gt; `ClusterId`.
    - Make sure the user has the following [permissions](/en-us/azure/databricks/security/access-control/cluster-acl) so as to connect to the Azure Databricks cluster:

        - **Can Attach To** permission to connect to the running cluster.
        - **Can Restart** permission to automatically trigger the cluster to start if its state is terminated when connecting.

## Register

This section describes how to register an Azure Databricks workspace in Microsoft Purview by using [the Microsoft Purview governance portal](https://web.purview.azure.com/).

1. Go to your Microsoft Purview account.
2. Select **Data Map** on the left pane.
3. Select **Register**.
4. In **Register sources**, select **Azure Databricks** &gt; **Continue**.
5. On the **Register sources (Azure Databricks)** screen, complete the following steps:

    1. For **Name**, enter a name that Microsoft Purview lists as the data source.
    2. For **Azure subscription** and **Databricks workspace name**, select the subscription and workspace that you want to scan from the dropdown. The Databricks workspace URL is automatically populated.
    3. Select a collection from the list.

    ![Screenshot of registering Azure Databricks source.](media/register-scan-azure-databricks/configure-sources.png)
6. Select **Finish**.

## Scan

Tip

To troubleshoot any issues with scanning:

1. Confirm you followed all **prerequisites**.
2. Review the [**scan troubleshooting documentation**](troubleshoot-connections).

Use the following steps to scan Azure Databricks to automatically identify assets. For more information about scanning in general, see [Scans and ingestion in Microsoft Purview](data-map-scan-ingestion).

1. In the Management Center, select integration runtimes. Make sure that a self-hosted integration runtime is set up. If it isn't set up, use the steps in [Create and manage a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
2. Go to **Sources**.
3. Select the registered Azure Databricks.
4. Select **+ New scan**.
5. Provide the following details:

    1. **Name**: Enter a name for the scan.
    2. **Extraction method:** Indicate to extract metadata from Hive Metastore or Unity Catalog. Select **Hive Metastore**.
    3. **Connect via integration runtime**: Select the configured self-hosted integration runtime.
    4. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select **Access Token Authentication** while creating a credential.
        - Provide secret name of the personal access token that you created in Prerequisites in the appropriate box.

        For more information, see [Credentials for source authentication in Microsoft Purview](data-map-data-scan-credentials).
    5. **Cluster ID**: Specify the cluster ID that Microsoft Purview connects to and powers the scan. You can find it in Azure Databricks workspace -&gt; Compute -&gt; your cluster -&gt; Tags -&gt; Automatically added tags -&gt; `ClusterId`.

        1. **Mount points**: Provide the mount point and Azure Storage source location string when you have external storage manually mounted to Databricks. Use the format `/mnt/<path>=abfss://<container>@<adls_gen2_storage_account>.dfs.core.windows.net/;/mnt/<path>=wasbs://<container>@<blob_storage_account>.blob.core.windows.net`. It's used to capture the relationship between tables and the corresponding storage assets in Microsoft Purview. This setting is optional. If you don't specify it, the relationship isn't retrieved.

        You can get the list of mount points in your Databricks workspace by running the following Python command in a notebook:

        ```
        dbutils.fs.mounts()
        ```

        It prints all the mount points like below:

        ```
        [MountInfo(mountPoint='/databricks-datasets', source='databricks-datasets', encryptionType=''),
        MountInfo(mountPoint='/mnt/ADLS2', source='abfss://samplelocation1@azurestorage1.dfs.core.windows.net/', encryptionType=''),
        MountInfo(mountPoint='/databricks/mlflow-tracking', source='databricks/mlflow-tracking', encryptionType=''), 
        MountInfo(mountPoint='/mnt/Blob', source='wasbs://samplelocation2@azurestorage2.blob.core.windows.net', encryptionType=''),
        MountInfo(mountPoint='/databricks-results', source='databricks-results', encryptionType=''),
        MountInfo(mountPoint='/databricks/mlflow-registry', source='databricks/mlflow-registry', encryptionType=''), MountInfo(mountPoint='/', source='DatabricksRoot', encryptionType='')]  
        ```

        In this example, specify the following as mount points:

        `/mnt/ADLS2=abfss://samplelocation1@azurestorage1.dfs.core.windows.net/;/mnt/Blob=wasbs://samplelocation2@azurestorage2.blob.core.windows.net`
    6. **Schema**: The subset of schemas to import expressed as a semicolon separated list of schemas. For example, `schema1;schema2`. All user schemas are imported if that list is empty. All system schemas and objects are ignored by default.

        Acceptable schema name patterns can be static names or contain wildcard %. For example: `A%;%B;%C%;D`

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

        Usage of NOT and special characters aren't acceptable.

        Note

        This schema filter is supported on Self-hosted Integration Runtime version 5.32.8597.1 and above.
    7. **Maximum memory available**: Maximum memory (in gigabytes) available on the customer's machine for the scanning processes to use. This value is dependent on the size of Azure Databricks to be scanned.

        Note

        As a thumb rule, please provide 1GB memory for every 1000 tables.

    ![Screenshot of setting up Azure Databricks scan.](media/register-scan-azure-databricks/scan.png)
6. Select **Continue**.
7. For **Scan trigger**, choose whether to set up a schedule or run the scan once.
8. Review your scan and select **Save and Run**.

Once the scan successfully completes, see how to browse and search Azure Databricks assets.

### View your scans and scan runs

To view existing scans:

1. Go to the Microsoft Purview portal. On the left pane, select **Data map**.
2. Select the data source. You can view a list of existing scans on that data source under **Recent scans**, or you can view all scans on the **Scans** tab.
3. Select the scan that has results you want to view. The pane shows you all the previous scan runs, along with the status and metrics for each scan run.
4. Select the run ID to check the [scan run details](data-map-scan-run-monitor-population#scan-run-details).

### Manage your scans

To edit, cancel, or delete a scan:

1. Go to the Microsoft Purview portal. On the left pane, select **Data Map**.
2. Select the data source. You can view a list of existing scans on that data source under **Recent scans**, or you can view all scans on the **Scans** tab.
3. Select the scan that you want to manage. You can then:

    - Edit the scan by selecting **Edit scan**.
    - Cancel an in-progress scan by selecting **Cancel scan run**.
    - Delete your scan by selecting **Delete scan**.

Note

- Deleting your scan does not delete catalog assets created from previous scans.

## Browse and search assets

After scanning your Azure Databricks, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

From the Databricks workspace asset, you can find the associated Hive Metastore and the tables/views, reversed applies too.

![Screenshot of browsing assets by source type.](media/register-scan-azure-databricks/browse-by-source-type.png)

![Screenshot of navigating to Azure Databricks source asset details.](media/register-scan-azure-databricks/switch-to-source-asset.png)

![Screenshot of finding the associated Hive Metastore with Azure Databricks source.](media/register-scan-azure-databricks/associated-hive-metastore.png)

## Lineage

Refer to the supported capabilities section on the supported Azure Databricks scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

Go to the Hive table/view asset -&gt; lineage tab, you can see the asset relationship when applicable. For relationship between table and external storage assets, you see Hive table asset and the storage asset are directly connected bi-directionally, as they mutually impact each other. If you use mount point in create table statement, you need to provide the mount point information in scan settings to extract such relationship.

![Screenshot that shows Azure Databricks lineage example.](media/register-scan-azure-databricks/lineage.png)