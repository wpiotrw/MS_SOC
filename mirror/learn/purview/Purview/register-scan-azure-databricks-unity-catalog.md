---
layout: Conceptual
title: Connect to and manage Azure Databricks Unity Catalog in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-databricks-unity-catalog
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2026-05-19T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to use Microsoft Purview to scan and manage your Azure Databricks Unity Catalog.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 4b5f81de-b1bf-3528-f216-17a1acf8571f
document_version_independent_id: 4b5f81de-b1bf-3528-f216-17a1acf8571f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-databricks-unity-catalog.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-databricks-unity-catalog
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-databricks-unity-catalog.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/545d40c6-c50c-444b-b422-1c707eeab28e
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b908d601-32e8-445a-b044-a507b5d1689e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: dad34276-c59a-d3eb-720e-14b2bc6f0c55
---

# Connect to and manage Azure Databricks Unity Catalog in Microsoft Purview | Microsoft Learn

This article outlines how to register Azure Databricks, and how to authenticate and interact with Azure Databricks Unity Catalog in Microsoft Purview. For more information about Microsoft Purview, see the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | No |

When scanning Azure Databricks Unity Catalog, Microsoft Purview supports:

- Extracting technical metadata, including:

    - Metastore
    - Catalogs
    - Schemas
    - Tables, including the columns. Purview supports external tables metadata, but lineage isn't supported.
    - Views, including the columns
    - Tags from Unity Catalog (tags that represent labels, classification equivalent in Unity Catalog are scanned in Microsoft Purview in properties)
- Fetching lineage on assets relationships between tables, views, and columns during notebook runs.

When setting up a scan, you can choose to scan the entire Unity Catalog, or scope the scan to a subset of catalogs.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

Note

This connector brings metadata from Azure Databricks Unity Catalog. To scan Azure Databricks workspace-scoped metadata, see [Azure Databricks Hive Metastore connector](register-scan-azure-databricks).

### Known limitations

- In Microsoft Purview, Databricks notebook names appear as numeric IDs instead of readable names. This limitation exists because Databricks doesn't expose notebook names in the Unity Catalog system table.
- You might encounter errors if scan results from Azure Databricks exceed 1 MB and Azure Databricks-managed blob storage denies public network access. To prevent this problem, ensure that Microsoft Purview has access to the internal DBFS storage location of the Azure Databricks workspace being scanned. To learn more, see [Cloud fetch in JDBC](/en-us/azure/databricks/integrations/jdbc/capability#cloud-fetch-in-jdbc).
- Incremental scan is available only for the *Azure Databricks Unity Catalog* data source.
- Scoped scan is available only for the Unity Catalog option under *Azure Databricks* data source.
- You can add managed private endpoints only for the Unity Catalog option under *Azure Databricks* data source.
- When you delete an object from the data source, the subsequent scan doesn't automatically remove the corresponding asset in Microsoft Purview.
- Lineage information isn't available in Azure Databricks workspaces in the China region. This limitation exists because Azure Databricks system tables aren't supported in this region. Microsoft Purview uses these tables to extract lineage, so it can't retrieve lineage in this region.
- Set the Databricks table column comment to an empty string if you don't want the column description displayed in Microsoft Purview.
- Lineage for external isn't supported.
- Tags aren't currently supported for scans done using a Kubernetes SHIR option.

For more information about other limitations related to native Azure Databricks lineage, see [Azure Databricks documentation](/en-us/azure/databricks/data-governance/unity-catalog/data-lineage#limitations).

## Prerequisites

- You must have an Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- You must have an active [Microsoft Purview account](create-microsoft-purview-portal).
- You need an Azure Key Vault, and to [grant Microsoft Purview permissions to access secrets](data-map-data-scan-credentials#grant-microsoft-purview-access-to-your-azure-key-vault).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the classic Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- To scan Azure Databricks Unity Catalog, Microsoft Purview connects to a SQL Warehouse in your workspace, and uses a Personal Access Token for authentication. You need to have an Azure Databricks workspace that is [Unity Catalog enabled](/en-us/azure/databricks/data-governance/unity-catalog/enable-workspaces) and attached to the metastore you want to scan. In your Azure Databricks workspace:

    - [Create a SQL Warehouse](/en-us/azure/databricks/sql/admin/sql-endpoints). You can use the autocreated Starter warehouse as well if applicable.
    - Note down the HTTP path. You can find it in Azure Databricks workspace &gt; SQL Warehouses &gt; your warehouse &gt; Connection details &gt; HTTP path.
    - Make sure the user has the **Can Use** permission so they can connect to the Azure Databricks SQL warehouse. Learn more at [SQL warehouse access control](/en-us/azure/databricks/security/access-control/sql-endpoint-acl).
    - The SQL warehouse in Azure Databricks must be running to establish a connection with Microsoft Purview before setting up the scan in Microsoft Purview.
- To fetch lineage from Azure Databricks using Microsoft Purview, the following prerequisites must be in place:

    - Enable the system schema: The system schema **system.access** must be enabled in your Unity Catalog. This requirement exists because lineage information is stored in system tables, and enabling this schema allows access to those tables. [Learn more about monitoring usage with system tables](/en-us/azure/databricks/administration-guide/system-tables/).
    - User privileges:

        - The user account you use for scanning needs to have SELECT privileges on the following system tables:

            - system.access.table\_lineage
            - system.access.column\_lineage

            These permissions are required because lineage data is read directly from the system tables, and without the necessary access, Microsoft Purview can't retrieve the lineage information.

            The user account you use for scanning also needs to have these permissions:

            - USE CATALOG on system
            - USE SCHEMA on system.access
- If your Azure Databricks workspace doesn’t allow access from public network or if your Microsoft Purview account doesn’t enable access from all networks, you can use the [Managed Virtual Network Integration Runtime](data-governance-private-endpoints-managed-virtual-network) or a [kubernetes supported self-hosted integration runtime](data-map-integration-runtime-kubernetes) to scan. You can set up a managed private endpoint for Azure Databricks as needed to establish private connectivity.

## Data source setup (Azure Databricks vs. Azure Databricks Unity Catalog)

You can set up an Azure Databricks Unity Catalog connection to Microsoft Purview through two sources:

- Azure Databricks (old source)
- Azure Databricks Unity Catalog

#### Differences in capabilities between data sources

The capabilities of the Azure Databricks Unity Catalog connector differ based on the source used for the connection, as outlined in the following table:

| Capability | Old source | New source |
| --- | --- | --- |
| **Source name** | Azure Databricks | Azure Databricks Unity Catalog |
| **Source support** | Hive & Unity Catalog | Unity Catalog |
| **Authentication: Personal Access Token** | Supported | Supported |
| **Authentication: Service Principal** | No | Supported |
| **Authentication: Managed Identity** | No | Supported (system managed identity) |
| **Integration Runtime: Azure IR** | Supported | Supported |
| **Integration Runtime: Managed Virtual Network IR** | Supported | Yes\*\* |
| **Integration Runtime: Kubernetes Self-Hosted IR** | Supported | Supported |
| **Scoped scan** | Yes - catalog level | No |
| **Incremental scan** | No | Yes |
| **Lineage** | Supported | Supported |

\*\*Scanning Azure Databricks Unity Catalog is supported through Managed Virtual Network Integration Runtime. However, Managed Private Endpoint isn't supported in this case.

#### Which source should I use?

Choose either source based on your organization’s needs, or use both in parallel. Switching between sources or using both simultaneously **doesn't cause asset duplication** in Microsoft Purview. This flexibility allows you to start with the option that best fits your current setup and adjust over time as needed.

## Authentication for a scan

To scan Azure Databricks Unity Catalog, use personal access tokens, managed identities, or service principal authentication methods.

# [System assigned managed identity](#tab/MI)
#### If you use a system assigned managed identity

##### In Azure Databricks

1. Go to **Settings** &gt; **Workspace admin** &gt; **Identity and access**.
2. Select **Add service principal**.
3. Select **Add new**.
4. Select **Microsoft Entra ID managed**. Enter the **Application ID** for Microsoft Purview. You can find the Application ID under Microsoft Purview account resource details in the Azure portal.

    ![Find the Microsoft Entra application ID](media/register-scan-azure-databricks-unity-catalog/image1.png)

##### In Microsoft Purview

1. Select the system-assigned managed identity under **Credential**.

# [Personal access token](#tab/PAT)
#### If you're using a personal access token

1. [Generate a personal access token](/en-us/azure/databricks/dev-tools/auth#--azure-databricks-personal-access-tokens), and store it as a secret in Azure Key Vault.
2. While setting up a scan, select **+ New** under **Credential** and register the credential.
3. Select the appropriate credential under **Credential** during scan setup.

# [Service Principal](#tab/SP)
#### If you're using a service principal

1. [Set up service principal authentication for Azure Databricks](/en-us/azure/databricks/dev-tools/auth/azure-sp).
2. Select **+ New** under **Credential**.
3. Select the appropriate **Key vault connection** and the **Secret name** that you used while creating the *Service Principal*.

---

- For all the objects that you want to bring into Microsoft Purview, the user or service principal needs to have at least **SELECT** privilege on tables/views, **USE CATALOG** on the object’s catalog, and **USE SCHEMA** on the object’s schema.

    - To scan all the objects in a Unity Catalog metastore, use a user or service principal with metastore admin role. For more information, see [Manage privileges in Unity Catalog](/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/) and [Unity Catalog privileges and securable objects](/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/privileges).

        - For classification, the user also needs to have **SELECT** privilege on the tables/views to retrieve sample data.

## Register

This section describes how to register an Azure Databricks workspace in Microsoft Purview by using the [classic Microsoft Purview governance portal](https://web.purview.azure.com/).

1. Go to your Microsoft Purview account.
2. Select **Data Map** on the left pane.
3. Select **Register**.
4. In **Register sources**, select **Azure Databricks Unity Catalog** &gt; **Continue**.
5. On the **Register sources (Azure Databricks Unity Catalog)** screen, complete the following steps:
6. For **Name**, enter a name that Microsoft Purview will list as the data source.

    1. For **Metastore ID**, enter the metastore ID for the Azure Databricks Unity Catalog metastore that you want to scan.
    2. Select a collection from the list.

![Screenshot of registering Azure Databricks Unity Catalog source.](media/register-scan-azure-databricks-unity-catalog/register.png)

1. Select **Finish**.

## Scan

Tip

To troubleshoot any problems with scanning:

1. Confirm you meet all **prerequisites**.
2. Review the [**scan troubleshooting documentation**](troubleshoot-connections).

Use the following steps to scan Azure Databricks and automatically identify assets. For more information about scanning, see [Scans and ingestion in Microsoft Purview](data-map-scan-ingestion).

1. Go to **Sources**.
2. Select the registered Azure Databricks.
3. Select **+ New scan**.
4. Provide the following details:

    1. **Name**: Enter a name for the scan.
    2. **Connect via integration runtime**: Choose the default Azure integration runtime, Managed Virtual Network IR, or a Kubernetes supported self-hosted integration runtime you created.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select **Access Token**, **Managed Identity**, or **Service Principal**.
        - You can create a new Access Token or Service Principal credential while registering a scan. For more information, see [Credentials for source authentication in Microsoft Purview](data-map-data-scan-credentials).
    4. **Workspace URL:** Provide the URL for the workspace that you want to scan.

        1. **HTTP path:** Specify the Databricks SQL Warehouse’s HTTP path that Microsoft Purview connects to and performs the scan; for example, `/sql/1.0/endpoints/xxxxxxxxxxxxxxxx`. You can find it in Azure Databricks workspace -&gt; SQL Warehouses -&gt; your warehouse -&gt; Connection details -&gt; HTTP path.
    5. **Lineage extraction:** Toggle lineage extraction to **On** to fetch lineage of the scanned assets.
5. Select **Test connection** to validate the settings.

    ![Screenshot of setting up Azure Databricks Unity Catalog scan.](media/register-scan-azure-databricks-unity-catalog/image.png)
6. Select **Continue**.
7. On the **Scope your scan** page, select one or more catalogs on which you want to limit your scan. Use **Advanced mode** (preview) to select specific item paths to include or exclude from the scan.

    ![Advanced mode for scan scope](media/register-scan-azure-databricks-unity-catalog/advanced-mode-scope.png)
8. For **Scan trigger**, choose whether to set up a schedule or run the scan once.
9. Review your scan and select **Save and Run**.

After the scan finishes successfully, see how to browse and search assets.

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

After scanning your Azure Databricks, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details and lineage.

When you browse by source types, you see two entries for **Azure Databricks Unity Catalog** and **Azure Databricks**. The **Azure Databricks Unity Catalog** entry contains the Unity Catalog artifacts, including the metastore and its catalogs, schemas, tables, and views. The **Azure Databricks** entry contains the workspace artifacts.

![Screenshot of browsing assets by source type.](media/register-scan-azure-databricks/unity-catalog-browse-by-source-type.png)

From the Azure Databricks workspace asset, you can find the associated Unity Catalog under the **Properties** tab. The association also works in reverse.

![Screenshot of finding the associated Unity Catalog with Azure Databricks source.](media/register-scan-azure-databricks/associated-unity-catalog.png)

### Lineage

When you browse a particular Azure Databricks asset, you can see the notebooks that have captured lineage.

Go to the asset and select the lineage tab. You can see the lineage on the Azure Databricks Notebook asset or table/view asset when applicable.

![Screenshot of browsing notebooks present in the associated Azure Databricks Unity Catalog workspace asset.](media/register-scan-azure-databricks-unity-catalog/azuredatabricksuc-notebooks.png)

![Screenshot of notebook lineage present in the associated Azure Databricks Unity Catalog workspace asset.](media/register-scan-azure-databricks-unity-catalog/azuredatabricksuc-notebook-lineage.png)

#### Supported lineage scenarios

- Lineage is supported for tables and views when they're connected via Databricks notebooks within the Unity Catalog.
- Lineage appears only for objects scanned through Microsoft Purview. All related assets must be scanned to form a complete lineage graph. Ensure all Databricks workspaces with relevant notebooks are included in Microsoft Purview scans.

#### Lineage limitations

- When you execute notebooks through Databricks jobs, column-level lineage might not be captured.
- Microsoft Purview shows only partial lineage if you don't scan all objects involved in a data flow. For example, if a notebook in Workspace A writes data to a table in Workspace B, but you only scan Workspace A by using Microsoft Purview, the lineage shows the notebook but not the destination table, resulting in incomplete lineage.
- If an external service triggers a notebook (for example, Azure Data Factory [ADF] pipeline calling a Databricks job), the lineage in Microsoft Purview doesn't reflect that dependency.
    - In this case, lineage between ADF datasets and Databricks assets isn't shown.
    - Only lineage built within Databricks notebooks is captured.

#### Lineage is missing scenario

Lineage extraction is passive; Microsoft Purview only ingests what Unity Catalog system table logs and makes accessible.

- Refer to the preceding sections to ensure that your lineage scenario is supported.
- Validate that Unity Catalog lineage system tables (`system.access.table_lineage`, `system.access.column_lineage`) are populated correctly.
- Raise a support ticket if you still encounter problems.

Refer to the supported capabilities section for supported Databricks Unity Catalog lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

## Frequently asked questions (FAQ)

### Does Microsoft Purview capture column-level lineage from Unity Catalog?

Microsoft Purview captures lineage at both the Unity Catalog table and view level, and at the column level.

### Why don't I see column-level lineage?

Column-level lineage appears when you run your notebook from a cluster. SQL warehouses don't generate column-level lineage.

### How do I fix a timeout error?

Your scan might not finish if your workspace contains a large number of assets. To fix this problem, scope your scan to a few catalogs at a time. This approach reduces the number of assets in each scan and helps your scans complete.

### Why didn't Microsoft Purview fetch the lineage after I ran my notebook?

After you run your notebook, Databricks might take a few minutes to update the lineage information in its system tables. Microsoft Purview can fetch the lineage after the system tables are updated.