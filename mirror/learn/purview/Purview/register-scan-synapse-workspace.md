---
layout: Conceptual
title: Connect to and manage Azure Synapse Analytics workspaces | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-synapse-workspace
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2026-02-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
search.appverid:
- MET150
- MOE150
description: Learn how to connect to Azure Synapse Analytics workspaces in Microsoft Purview, and how to use Microsoft Purview features to scan and manage your Azure Synapse Analytics workspace source.
locale: en-us
document_id: 38cf1d1a-5510-3f17-30ee-c8ef4922b22f
document_version_independent_id: 38cf1d1a-5510-3f17-30ee-c8ef4922b22f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-synapse-workspace.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-synapse-workspace
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-synapse-workspace.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bad69977-db6a-44f3-b752-d2bee7de49ca
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31d7aff-61be-45e2-a324-a578cf0c3360
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
platformId: 2cd01b6a-2612-9707-8ada-60c8ef36a9ad
---

# Connect to and manage Azure Synapse Analytics workspaces | Microsoft Learn

This article outlines how to register Azure Synapse Analytics workspaces. It also describes how to authenticate and interact with Azure Synapse Analytics workspaces in Microsoft Purview. Learn more about [Microsoft Purview](purview).

Note

There are dedicated SQL pools (formerly SQL DW) and dedicated SQL pools in Azure Synapse workspace. For the detailed difference between the two, see [What is the difference between dedicated SQL pools (SQL DW) and dedicated SQL pools in Azure Synapse workspaces](/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-overview-faq#what-is-the-difference-between-dedicated-sql-pools--sql-dw--and-dedicated-sql-pools-in-azure-synapse-workspaces-). Currently Microsoft Purview provides separate data sources for dedicated SQL pools (formerly SQL DW) and dedicated SQL pools:

- To register and scan a dedicated SQL pool (formerly SQL DW), see [Connect to and manage dedicated SQL pools in Microsoft Purview](register-scan-azure-synapse-analytics).
- To register and scan a dedicated SQL pool (formerly SQL DW) that has enabled Azure Synapse workspace features, as documented in [Enable Azure Synapse workspace features for a dedicated SQL pool (formerly SQL DW)](/en-us/azure/synapse-analytics/sql-data-warehouse/workspace-connected-create), see [Connect to and manage Azure Synapse Analytics workspaces in Microsoft Purview](register-scan-synapse-workspace).
- To register and scan a dedicated SQL pool or a serverless SQL pool in Azure Synapse workspace, see [Connect to and manage Azure Synapse Analytics workspaces in Microsoft Purview](register-scan-synapse-workspace).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | No |

Azure Synapse Analytics lake databases aren't currently supported. You might observe some inconsistencies in the scanned assets for these databases.

For external tables, Azure Synapse Analytics doesn't currently capture the relationship of those tables to their original files.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- Data source administrator and data reader permissions to register a source and manage it in the Microsoft Purview governance portal. For details, see [Access control in the Microsoft Purview governance portal](data-gov-classic-permissions).

## Register

The following procedure describes how to register Azure Synapse Analytics workspaces in Microsoft Purview by using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

To register an Synapse Analytics workspace, you need at least the data reader role on the Synapse Analytics workspace and be a data source administrator in Microsoft Purview.

1. Open the [Microsoft Purview governance portal](https://web.purview.azure.com) and select your Microsoft Purview account.

    Alternatively, go to the [Azure portal](https://portal.azure.com), search for and select the Microsoft Purview account, and then select the **Microsoft Purview governance portal** button.
2. On the left pane, select **Sources**.
3. Select **Register**.
4. Under **Register sources**, select **Azure Synapse Analytics (multiple)**.
5. Select **Continue**.

    ![Screenshot of a selection of sources in Microsoft Purview, including Azure Synapse Analytics.](media/register-scan-synapse-workspace/register-synapse-source.png)
6. On the **Register sources (Azure Synapse Analytics)** page, do the following:

    1. For **Name**, enter a name for the data source to be listed in Microsoft Purview Unified Catalog.
    2. Optionally, for **Azure subscription**, choose a subscription to filter down to.
    3. For **Workspace name**, select the workspace that you're working with.

        The boxes for the SQL endpoints are automatically filled in based on your workspace selection.
    4. Select a collection from the list.
    5. Select **Register** to finish registering the data source.

    ![Screenshot of the page for entering details about the Azure Synapse source.](media/register-scan-synapse-workspace/register-synapse-source-details.png)

## Scan

Use the following steps to scan Azure Synapse Analytics workspaces to automatically identify assets and classify your data. For more information about scanning in general, see [Scans and ingestion in Microsoft Purview](data-map-scan-ingestion).

1. Set up authentication for enumerating your dedicated or serverless resources. By setting up authentication, Microsoft Purview can enumerate your workspace assets and perform scans.
2. Apply permissions to scan the contents of the workspace.
3. Confirm that your network is set up to allow access for Microsoft Purview.

### Enumeration authentication

Use the following procedures to set up authentication. You must be an owner or a user access administrator to add the specified roles.

#### Authentication for enumerating dedicated SQL database resources

1. In the Azure portal, go to the Azure Synapse Analytics workspace resource.
2. On the left pane, select **Access Control (IAM)**.
3. Select the **Add** button.
4. Set the **Reader** role and enter your Microsoft Purview account name, which represents its managed service identity (MSI).
5. Select **Save** to finish assigning the role.

If you want to scan a dedicated SQL pool (formerly SQL DW) that has enabled Azure Synapse Analytics workspace features as documented in [Enable Azure Synapse workspace features for a dedicated SQL pool (formerly SQL DW)](/en-us/azure/synapse-analytics/sql-data-warehouse/workspace-connected-create), follow these additional configuration steps for the dedicated SQL pool (formerly SQL DW):

1. In the Azure portal, go to the SQL Server resource associated with the dedicated SQL pool (formerly SQL DW).
2. On the left pane, select **Access Control (IAM)**.
3. Select the **Add** button.
4. Set the **Reader** role and enter your Microsoft Purview account name, which represents its managed service identity (MSI).
5. Select **Save** to finish assigning the role.

Note

If you're planning to register and scan multiple Azure Synapse Analytics workspaces in your Microsoft Purview account, you can also assign the role from a higher level, such as a resource group or a subscription.

#### Authentication for enumerating serverless SQL Database resources

Set authentication in three places to allow Microsoft Purview to enumerate your serverless SQL Database resources.

To set authentication for the Azure Synapse Analytics workspace:

1. In the Azure portal, go to the Azure Synapse Analytics workspace resource.
2. On the left pane, select **Access Control (IAM)**.
3. Select the **Add** button.
4. Set the **Reader** role and enter your Microsoft Purview account name, which represents its MSI.
5. Select **Save** to finish assigning the role.

To set authentication for the storage account:

1. In the Azure portal, go to the resource group or subscription that contains the storage account associated with the Azure Synapse Analytics workspace.
2. On the left pane, select **Access Control (IAM)**.
3. Select the **Add** button.
4. Set the **Storage blob data reader** role and enter your Microsoft Purview account name (which represents its MSI) in the **Select** box.
5. Select **Save** to finish assigning the role.

To set authentication for the Azure Synapse Analytics serverless database:

1. Go to your Azure Synapse Analytics workspace and open Synapse Studio.
2. On the left pane, select **Data**.
3. Select the ellipsis (**...**) next to one of your databases, and then start a new SQL script.
4. Run the following command in your SQL script to add the Microsoft Purview account MSI (represented by the account name) on the serverless SQL databases:

    ```sql
    CREATE LOGIN [PurviewAccountName] FROM EXTERNAL PROVIDER;
    ```

### Apply permissions to scan the contents of the workspace

You must set up authentication on each SQL Database that you want to register and scan from your Azure Synapse Analytics workspace. For steps to apply permissions, see the following scenarios.

Important

The following steps for serverless databases *do not* apply to replicated databases. In Azure Synapse Analytics, serverless databases that are replicated from Spark databases are currently read-only. For more information, see [Operation isn't allowed for a replicated database](/en-us/azure/synapse-analytics/sql/resources-self-help-sql-on-demand#operation-isnt-allowed-for-a-replicated-database).

# [Managed identity](#tab/MI)
#### Use a managed identity for dedicated SQL databases

Important

If you use a [self-hosted integration runtime](data-map-integration-runtime-self-hosted) to connect to your resource on a private network, managed identities don't work. You need to use service principal authentication or SQL authentication.

To run the commands in the following procedure, you must be an Azure Synapse administrator on the workspace. For more information about Azure Synapse Analytics permissions, see [Set up access control for your Azure Synapse Analytics workspace](/en-us/azure/synapse-analytics/security/how-to-set-up-access-control).

1. Go to your Azure Synapse Analytics workspace.
2. Go to the **Data** section, and then look for one of your dedicated SQL databases.
3. Select the ellipsis (**...**) next to the database name, and then start a new SQL script.
4. Run the following command in your SQL script to add the Microsoft Purview account MSI (represented by the account name) as `db_datareader` on the dedicated SQL database:

    ```sql
    CREATE USER [PurviewAccountName] FROM EXTERNAL PROVIDER
    GO
    
    EXEC sp_addrolemember 'db_datareader', [PurviewAccountName]
    GO
    ```
5. Run the following command in your SQL script to verify the addition of the role:

    ```sql
    SELECT p.name AS UserName, r.name AS RoleName
    FROM sys.database_principals p
    LEFT JOIN sys.database_role_members rm ON p.principal_id = rm.member_principal_id
    LEFT JOIN sys.database_principals r ON rm.role_principal_id = r.principal_id
    WHERE p.authentication_type_desc = 'EXTERNAL'
    ORDER BY p.name;
    ```

Follow the same steps for each database that you want to scan.

#### Use a managed identity for serverless SQL databases

1. Go to your Azure Synapse Analytics workspace.
2. Go to the **Data** section, and select one of your SQL databases.
3. Select the ellipsis (**...**) next to the database name, and then start a new SQL script.
4. Run the following command in your SQL script to add the Microsoft Purview account MSI (represented by the account name) as `db_datareader` on the serverless SQL databases:

    ```sql
    CREATE USER [PurviewAccountName] FOR LOGIN [PurviewAccountName];
    ALTER ROLE db_datareader ADD MEMBER [PurviewAccountName]; 
    ```
5. Run the following command in your SQL script to verify the addition of the role:

    ```sql
    SELECT p.name AS UserName, r.name AS RoleName
    FROM sys.database_principals p
    LEFT JOIN sys.database_role_members rm ON p.principal_id = rm.member_principal_id
    LEFT JOIN sys.database_principals r ON rm.role_principal_id = r.principal_id
    WHERE p.authentication_type_desc = 'EXTERNAL'
    ORDER BY p.name;
    ```

Follow the same steps for each database that you want to scan.

#### Grant permission to use credentials for external tables

If the Synapse Analytics workspace has any external tables, you must give the Microsoft Purview managed identity References permission on the external table's scoped credentials. By using the References permission, Microsoft Purview can read data from external tables.

1. Run the following command in your SQL script to get the list of database scoped credentials:

    ```sql
    Select name, credential_identity
    from sys.database_scoped_credentials;
    ```
2. To grant access to database scoped credentials, run the following command. Replace `scoped_credential` with the name of the database scoped credential.

    ```sql
    GRANT REFERENCES ON DATABASE SCOPED CREDENTIAL::[scoped_credential] TO [PurviewAccountName];
    ```
3. To verify the permission assignment, run the following command in your SQL script:

    ```sql
    SELECT dp.permission_name, dp.grantee_principal_id, p.name AS grantee_principal_name
    FROM sys.database_permissions AS dp
    JOIN sys.database_principals AS p ON dp.grantee_principal_id = p.principal_id
    JOIN sys.database_scoped_credentials AS c ON dp.major_id = c.credential_id;
    ```

# [Service principal](#tab/SP)
#### Use a service principal for dedicated SQL databases

1. Set up a new credential of type *service principal* by following the instructions in [Credentials for source authentication in Microsoft Purview](data-map-data-scan-credentials).
2. Go to your Azure Synapse Analytics workspace.
3. Go to the **Data** section, and then look for one of your dedicated SQL databases.
4. Select the ellipsis (**...**) next to the database name, and then start a new SQL script.
5. Run the following command in your SQL script to add the service principal ID as `db_datareader` on the dedicated SQL database:

    ```sql
    CREATE USER [ServicePrincipalID] FROM EXTERNAL PROVIDER
    GO
    
    EXEC sp_addrolemember 'db_datareader', [ServicePrincipalID]
    GO
    ```

Repeat the previous steps for all dedicated SQL databases in your Azure Synapse Analytics workspace.

#### Use a service principal for serverless SQL databases

1. Go to your Azure Synapse Analytics workspace.
2. Go to the **Data** section, and then look for one of your serverless SQL databases.
3. Select the ellipsis (**...**) next to the database name, and then start a new SQL script.
4. Run the following command in your SQL script to add the service principal ID on the serverless SQL databases:

    ```sql
    CREATE LOGIN [ServicePrincipalID] FROM EXTERNAL PROVIDER;
    ```
5. Run the following command in your SQL script to add the service principal ID as `db_datareader` on each of the serverless SQL databases that you want to scan:

    ```sql
     CREATE USER [ServicePrincipalID] FOR LOGIN [ServicePrincipalID];
     ALTER ROLE db_datareader ADD MEMBER [ServicePrincipalID]; 
    ```

# [SQL authentication](#tab/SQLAuth)
#### Use SQL authentication for dedicated SQL databases

1. Set up a new credential of type *SQL authentication* by following the instructions in [Credentials for source authentication in Microsoft Purview](data-map-data-scan-credentials).
2. Go to your Azure Synapse Analytics workspace.
3. Go to the **Data** section, and then look for one of your dedicated SQL databases.
4. Select the ellipsis (**...**) next to the database name, and then start a new SQL script.
5. Run the following command in your SQL script to add the SQL authentication login name as `db_datareader` on the dedicated SQL database:

    ```sql
    CREATE USER [SQLUser] FROM LOGIN [SQLUser];
    GO
    
    EXEC sp_addrolemember 'db_datareader', [SQLUser]; 
    GO
    ```

Repeat the previous steps for all dedicated SQL databases in your Azure Synapse Analytics workspace.

#### Use SQL authentication for serverless SQL databases

1. Go to your Azure Synapse Analytics workspace.
2. Go to the **Data** section, and then look for one of your serverless SQL databases.
3. Select the ellipsis (**...**) next to the database name, and then start a new SQL script.
4. Run the following command in your SQL script to add the SQL authentication login name on the serverless SQL databases:

    ```sql
    CREATE USER [SQLUser] FROM LOGIN [SQLUser];
    GO
    ```
5. Run the following command in your SQL script to add the service principal ID as `db_datareader` on each of the serverless SQL databases that you want to scan:

    ```sql
    ALTER ROLE db_datareader ADD MEMBER [SQLUser];
    GO
    ```

---

### Set up firewall access for the Azure Synapse Analytics workspace

1. In the Azure portal, go to the Azure Synapse Analytics workspace.
2. On the left pane, select **Networking**.
3. For **Allow Azure services and resources to access this workspace**, select **ON**.
4. Select **Save**.

If you want to scan a dedicated SQL pool (formerly SQL DW) that has enabled Azure Synapse Analytics workspace features as documented in [Enable Azure Synapse workspace features for a dedicated SQL pool (formerly SQL DW)](/en-us/azure/synapse-analytics/sql-data-warehouse/workspace-connected-create), follow these additional configuration steps for the dedicated SQL pool (formerly SQL DW):

1. In the Azure portal, go to the SQL Server resource associated with the dedicated SQL pool (formerly SQL DW).
2. On the left pane, select **Networking**.
3. For **Allow Azure services and resources to access this server**, select **ON**.
4. Select **Save**.

Important

If you can't enable **Allow Azure services and resources to access this workspace** on your Azure Synapse Analytics workspaces, you'll get a serverless database enumeration failure when you set up a scan in the Microsoft Purview governance portal. In this case, you can choose the Enter manually option to specify the database names that you want to scan, and then proceed or set up a scan using an API.

### Create and run a scan

1. In the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), on the left pane, select **Data Map**.
2. Select the data source that you registered.
3. Select **View details**, and then select **New scan**. Alternatively, you can select the **Scan quick action** icon on the source tile.
4. On the **Scan** details pane, in the **Name** box, enter a name for the scan.

Note

For the integration runtime, if you're using [managed virtual network runtime](data-governance-private-endpoints-managed-virtual-network), make sure you create the required Managed Private Endpoints:

- To scan Serverless pools, create a managed private endpoint of *sqlOnDemand* (case sensitive) sub-resource type for your Synapse workspace.
- To scan Dedicated pools, create a managed private endpoint of *sql* (case sensitive) sub-resource type for your Synapse workspace.

- If you're scanning both Serverless and Dedicated pools, you must create both managed private endpoints and in the wizard select one.

1. In the **Credential** dropdown list, select the credential to connect to the resources within your data source.
2. For **Database selection method**, select **From Synapse workspace** or **Enter manually**. By default, Microsoft Purview tries to enumerate the databases under the workspace, and you can select the ones that you want to scan.

    ![Screenshot of the details pane for the Azure Synapse source scan.](media/register-scan-synapse-workspace/synapse-scan-setup.png)

    If you get an error that says Microsoft Purview failed to load the serverless databases, you can select **Enter manually** to specify the type of database (dedicated or serverless) and the corresponding database name.

    ![Screenshot of the selection for manually entering database names when setting up a scan.](media/register-scan-synapse-workspace/synapse-scan-setup-enter-manually.png)
3. Select **Test connection** to validate the settings. If you get any error, on the report page, hover over the connection status to see details.
4. Select **Continue**.
5. Select **Scan rule sets** of type **Azure Synapse SQL**. You can also create scan rule sets inline.
6. Choose your scan trigger. You can set up a schedule or run the scan once.
7. Review your scan, and then select **Save** to complete the setup.

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

### Set up a scan by using an API

Here's an example of creating a scan for a serverless database by using the Microsoft Purview REST API. Replace the placeholders in braces (`{}`) with your actual settings. To learn more, see [Scans - Create Or Update](/en-us/rest/api/purview/scanningdataplane/scans/create-or-replace).

```http
PUT https://{purview_account_name}.purview.azure.com/scan/datasources/<data_source_name>/scans/{scan_name}?api-version=2022-02-01-preview
```

In the following code, `collection_id` isn't the friendly name for the collection. It's a five-character ID. For the root collection, `collection_id` is the name of the collection. For all subcollections, it's the ID that you can find in one of these places:

- The URL in the Microsoft Purview governance portal. Select the collection, and check the URL to find where it says **collection=**. That's your ID. In the following example, the **Investment** collection has the ID **50h55c**.

    [![Screenshot of a collection ID in a URL.](media/register-scan-synapse-workspace/find-collection-id.png)](media/register-scan-synapse-workspace/find-collection-id.png#lightbox)
- You can [list child collection names](/en-us/rest/api/purview/accountdataplane/collections/list-child-collection-names) of the root collection to list the collections, and then use the name instead of the friendly name.

```json
{
    "properties":{
        "resourceTypes":{
            "AzureSynapseServerlessSql":{
                "scanRulesetName":"AzureSynapseSQL",
                "scanRulesetType":"System",
                "resourceNameFilter":{
                    "resources":[ "{serverless_database_name_1}", "{serverless_database_name_2}", ...]
                }
            }
        },
        "credential":{
            "referenceName":"{credential_name}",
            "credentialType":"SqlAuth | ServicePrincipal | ManagedIdentity (if UAMI authentication)"
        },
        "collection":{
            "referenceName":"{collection_id}",
            "type":"CollectionReference"
        },
        "connectedVia":{
            "referenceName":"{integration_runtime_name}",
            "integrationRuntimeType":"SelfHosted (if self-hosted IR) | Managed (if VNet IR)"
        }
    },
    "kind":"AzureSynapseWorkspaceCredential | AzureSynapseWorkspaceMsi (if system-assigned managed identity authentication)"
}
```

To schedule the scan, create a trigger for it after scan creation. For more information, see [Triggers - Create Trigger](/en-us/rest/api/purview/scanningdataplane/triggers/create-or-replace).

### Troubleshooting

If you have any problems with scanning:

- Confirm that you followed all prerequisites.
- Confirm that you set up enumeration authentication for your resources.
- Confirm that you set up authentication.
- Check the network by confirming firewall settings.
- Review the [scan troubleshooting documentation](troubleshoot-connections).