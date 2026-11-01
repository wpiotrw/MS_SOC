---
layout: Conceptual
title: Discover and govern Azure SQL database in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-sql-database
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: athenadsouza
ms.date: 2026-07-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to register, authenticate with, and interact with an Azure SQL database in Microsoft Purview.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 9f660a0b-a260-4076-bd66-b758a914fad5
document_version_independent_id: 9f660a0b-a260-4076-bd66-b758a914fad5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-sql-database.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-sql-database
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-sql-database.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab7faaf-d791-4a26-96a2-3b11738538e7
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/302e28b0-1f09-4811-9a9b-2a72e0770581
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 98c83759-b0c1-d535-043c-6ac06ec2cbd6
---

# Discover and govern Azure SQL database in Microsoft Purview | Microsoft Learn

This article outlines the process to register an Azure SQL database source in Microsoft Purview. It includes instructions to authenticate and interact with the SQL database.

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

When you're scanning Azure SQL Database, Microsoft Purview supports extracting technical metadata from these sources:

- Server
- Database
- Schemas
- Tables, including columns
- Views, including columns
- Stored procedures (with lineage extraction enabled)\*
- Stored procedure runs (with lineage extraction enabled)\*

When you're setting up a scan, you can further scope it after providing the database name by selecting tables and views as needed.

\* Stored procedure lineage extraction scan has some limitations. Refer to the Known limitations section on this page for details.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

For stored procedures (SP) lineage extraction:

- SP lineage extraction scan isn't supported if your logical server in Azure disables public access or doesn't allow Azure services to access it.
- SP lineage extraction scan is currently not supported if your stored procedures contain an INSERT or a DROP query.
- SP lineage extraction scan isn't supported if your Microsoft Purview account disables public access.

    - SP lineage extraction scan is scheduled to run every six hours by default. The frequency can't be changed.
    - Lineage is captured only when the stored procedure execution transfers data from one table to another. And it's not supported for temporary tables.
    - Lineage extraction isn't supported for functions or triggers.
    - Due to the following limitations, you could see duplicate assets in the catalog if you have scenarios such as:
        - The object names in assets and fully qualified names follow the case used in stored procedure statements, which might not align with the object case in original data source.
        - When SQL views are referenced in stored procedures, they're currently captured as SQL tables.

For scanned assets:

- For a full scan, instead of INT and NUMERIC data type, DECIMAL is displayed as a data type for SQL asset properties. If length of the field is MAX, it is displayed as zero (0).
- For **nchar** data type, column length is displayed in character count.

Note

Lineage is also supported if Azure SQL tables or views are used as a source/sink in [Azure Data Factory Copy and Data Flow activities](data-map-lineage-azure-data-factory).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- Data Source Administrator and Data Reader permissions, so you can register a source and manage it in the Microsoft Purview governance portal. For details, see [Access control in the Microsoft Purview governance portal](data-gov-classic-permissions).

## Register the data source

Before you scan, it's important to register the data source in Microsoft Purview:

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Select the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Navigate to the **Data Map**.

    ![Screenshot that shows the area for opening a Microsoft Purview governance portal.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-open-purview-studio.png)
3. Create the [collection hierarchy](data-map-collections-create-classic) by going to **Collections** and then selecting **Add a collection**. Assign permissions to individual subcollections as required.

    ![Screenshot that shows selections for assigning access control permissions to the collection hierarchy.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-collections.png)
4. Go to the appropriate collection under **Sources**, and then select the **Register** icon to register a new SQL database.

    ![Screenshot that shows the collection that's used to register the data source.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-data-source.png)
5. Select the **Azure SQL Database** data source, and then select **Continue**.
6. For **Name**, provide a suitable name for the data source. Select relevant names for **Azure subscription**, **Server name**, and **Select a collection**, and then select **Apply**.

    ![Screenshot that shows details entered to register a data source.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-ds-details.png)
7. Confirm that the SQL database appears under the selected collection.

    ![Screenshot that shows a data source mapped to a collection to initiate scanning.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-ds-collections.png)

## Update firewall settings

If your database server has a firewall enabled, you need to update the firewall to allow access in one of the following ways:

- Allow Azure connections through the firewall. This is a straightforward option to route traffic through Azure networking, without needing to manage virtual machines.
- Install a self-hosted integration runtime on a machine in your network and give it access through the firewall. If you have a private virtual network set up within Azure, or have any other closed network set up, using a self-hosted integration runtime on a machine within that network will allow you to fully manage traffic flow and utilize your existing network.
- [Use a managed virtual network](data-governance-private-endpoints-managed-virtual-network). Setting up a managed virtual network with your Microsoft Purview account allows you to connect to Azure SQL by using the Azure integration runtime in a closed network.

For more information about the firewall, see the [Azure SQL Database firewall documentation](/en-us/azure/azure-sql/database/firewall-configure).

### Allow Azure connections

Enabling Azure connections allows Microsoft Purview to connect to the server without requiring you to update the firewall itself.

1. Go to your database account.
2. On the **Overview** page, select the server name.
3. Select **Security** &gt; **Networking**.
4. For **Allow Azure services and resources to access this server**, select **Yes**.

![Screenshot that shows selections in the Azure portal to allow Azure connections to a server.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-firewall.png)

For more information about allowing connections from inside Azure, see the [how-to guide](/en-us/azure/azure-sql/database/firewall-configure#connections-from-inside-azure).

### Install a self-hosted integration runtime

You can install a self-hosted integration runtime on a machine to connect with a resource in a private network:

1. [Choose the right integration runtime for your scenario](data-map-integration-runtime-choose)
2. Create and install your integration runtime:
    - **To use a self-hosted integration runtime:**[Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
    - **To use a kubernetes supported self-hosted integration runtime:**[Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).
3. Check your database server's networking configuration to confirm that a private endpoint is accessible to the machine that contains the self-hosted integration runtime. Add the IP address of the machine if it doesn't already have access.
4. If your logical server is behind a private endpoint or in a virtual network, you can use an [ingestion private endpoint](data-gov-classic-private-link-end-to-end#deploy-self-hosted-integration-runtime-ir-and-scan-your-data-sources) to ensure end-to-end network isolation.

## Configure authentication for a scan

To scan your data source, you need to configure an authentication method in Azure SQL Database.

Important

If you're using a [self-hosted integration runtime](data-map-integration-runtime-self-hosted) to connect to your resource, system-assigned and user-assigned managed identities won't work. You need to use service principal authentication or SQL authentication.

Microsoft Purview supports the following options:

- **System-assigned managed identity (SAMI)** (recommended). This is an identity that is associated directly with your Microsoft Purview account. It allows you to authenticate directly with other Azure resources without needing to manage a go-between user or credential set.

    The SAMI is created when your Microsoft Purview resource is created. The SAMI is managed by Azure and uses your Microsoft Purview account's name. The SAMI can't currently be used with a self-hosted integration runtime for Azure SQL.

    For more information, see the [managed identity overview](/en-us/azure/active-directory/managed-identities-azure-resources/overview).
- **User-assigned managed identity (UAMI)** (preview). Similar to a SAMI, a UAMI is a credential resource that allows Microsoft Purview to authenticate against Microsoft Entra ID.

    The UAMI is managed by users in Azure, rather than by Azure itself, which gives you more control over security. The UAMI can't currently be used with a self-hosted integration runtime for Azure SQL.

    For more information, see the [guide for user-assigned managed identities](data-map-data-scan-credentials#create-a-user-assigned-managed-identity).
- **Service principal**. A service principal is an application that can be assigned permissions like any other group or user, without being associated directly with a person. Authentication for service principals has an expiration date, so it can be useful for temporary projects.

    For more information, see the [service principal documentation](/en-us/azure/active-directory/develop/app-objects-and-service-principals).
- **SQL authentication**. Connect to the SQL database with a username and password. For more information, see the [SQL authentication documentation](/en-us/sql/relational-databases/security/choose-an-authentication-mode#connecting-through-sql-server-authentication).

    If you need to create a login, follow [this guide to query a SQL database](/en-us/azure/azure-sql/database/logins-create-manage). Use [this guide to create a login by using T-SQL](/en-us/sql/t-sql/statements/create-login-transact-sql).

    Note

    Be sure to select the **Azure SQL Database** option on the page.

For steps to authenticate with your SQL database, select your chosen method of authentication from the following tabs.

# [SQL authentication](#tab/sql-authentication)
Note

Only the server-level principal login (created by the provisioning process) or members of the `loginmanager` database role in the master database can create new logins. The Microsoft Purview account should be able to scan the resources about 15 minutes after it gets permissions.

1. You need a SQL login with at least `db_datareader` permissions to be able to access the information that Microsoft Purview needs to scan the database. You can follow the instructions in [CREATE LOGIN](/en-us/sql/t-sql/statements/create-login-transact-sql?view=azuresqldb-current&amp;preserve-view=true#examples-1) to create a login for Azure SQL Database. Save the username and password for the next steps.
2. Go to your key vault in the Azure portal.
3. Select **Settings** &gt; **Secrets**, and then select **+ Generate/Import**.

    ![Screenshot that shows the key vault option to generate a secret.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-secret.png)
4. For **Name** and **Value**, use the username and password (respectively) from your SQL database.
5. Select **Create**.
6. If your key vault isn't connected to Microsoft Purview yet, [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account).
7. [Create a new credential](data-map-data-scan-credentials#create-a-new-credential) by using the key to set up your scan.

    ![Screenshot that shows the key vault option to set up credentials.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-credentials.png)

    ![Screenshot that shows the key vault option to create a secret.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-key-vault-options.png)

# [Managed identity](#tab/managed-identity)
Important

If you're using a self-hosted integration runtime to connect to your resource, system-assigned and user-assigned managed identities won't work. You need to use SQL authentication or service principal authentication.

### Configure Microsoft Entra authentication in the database account

The managed identity needs permission to get metadata for the database, schemas, and tables. It must also be authorized to query the tables to sample for classification.

1. If you haven't already, [configure Microsoft Entra authentication with Azure SQL](/en-us/azure/azure-sql/database/authentication-aad-configure).
2. Create a Microsoft Entra user in Azure SQL Database with the exact managed identity from Microsoft Purview. Follow the steps in [Create the service principal user in Azure SQL Database](/en-us/azure/azure-sql/database/authentication-aad-service-principal-tutorial#create-the-service-principal-user-in-azure-sql-database).
3. Assign proper permission (for example: `db_datareader`) to the identity. Here's example SQL syntax to create the user and grant permission:

    ```sql
    CREATE USER [Username] FROM EXTERNAL PROVIDER
    GO
    
    EXEC sp_addrolemember 'db_datareader', [Username]
    GO
    ```

    Note

    The `[Username]` value is your managed identity name from Microsoft Purview. You can [read more about fixed-database roles and their capabilities](/en-us/sql/relational-databases/security/authentication-access/database-level-roles#fixed-database-roles).

### Configure portal authentication

It's important to give your Microsoft Purview account's system-assigned managed identity or [user-assigned managed identity](data-map-data-scan-credentials#create-a-user-assigned-managed-identity) the permission to scan the SQL database. You can add the SAMI or UAMI at the subscription, resource group, or resource level, depending on the breadth of the scan.

Note

To add a managed identity on an Azure resource, you need to be an owner of the subscription.

1. From the [Azure portal](https://portal.azure.com), find the subscription, resource group, or resource (for example, a SQL database) that the catalog should scan.
2. Select **Access control (IAM)** on the left menu, and then select **+ Add** &gt; **Add role assignment**.

    ![Screenshot that shows selections for adding a role assignment for access control.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-sql-ds.png)
3. Set **Role** to **Reader**. In the **Select** box, enter your Microsoft Purview account name or UAMI. Then, select **Save** to give this role assignment to your Microsoft Purview account.

    ![Screenshot that shows the details to assign permissions for the Microsoft Purview account.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-access-managed-identity.png)

# [Service principal](#tab/service-principal)
### Create a new service principal

If you don't have a service principal, you can follow the [service principal guide](data-map-service-principal) to create one.

Note

To create a service principal, you must register an application in your Microsoft Entra tenant. If you don't have the required access, your Microsoft Entra Application Administrator can perform this operation.

### Grant the service principal access to your SQL database

The service principal needs permission to get metadata for the database, schemas, and tables. It must also be authorized to query the tables to sample for classification.

1. If you haven't already, [configure Microsoft Entra authentication with Azure SQL](/en-us/azure/azure-sql/database/authentication-aad-configure).
2. Create a Microsoft Entra user in Azure SQL Database with your service principal. Follow the steps in [Create the service principal user in Azure SQL Database](/en-us/azure/azure-sql/database/authentication-aad-service-principal-tutorial#create-the-service-principal-user-in-azure-sql-database).
3. Assign proper permission (for example: `db_datareader`) to the identity. Here's example SQL syntax to create the user and grant permission:

    ```sql
    CREATE USER [Username] FROM EXTERNAL PROVIDER
    GO
    
    EXEC sp_addrolemember 'db_datareader', [Username]
    GO
    ```

    Note

    The `[Username]` value is your own service principal's name. You can [read more about fixed-database roles and their capabilities](/en-us/sql/relational-databases/security/authentication-access/database-level-roles#fixed-database-roles).

### Create the credential

1. Go to your key vault in the Azure portal.
2. Select **Settings** &gt; **Secrets**, and then select **+ Generate/Import**.

    ![Screenshot that shows the key vault option to generate a secret for a service principal.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-secret.png)
3. For **Name**, give the secret a name of your choice.
4. For **Value**, use the service principal's secret value. If you've already created a secret for your service principal, you can find its value in **Client credentials** on your secret's overview page.

    If you need to create a secret, you can follow the steps in the [service principal guide](data-map-service-principal#add-a-secret-to-the-client-credentials).

    ![Screenshot that shows the client credentials for a service principal.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-sp-client-credentials.png)
5. Select **Create** to create the secret.
6. If your key vault isn't connected to Microsoft Purview yet, [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account).
7. [Create a new credential](data-map-data-scan-credentials#create-a-new-credential).

    ![Screenshot that shows the key vault option to add a credential for a service principal.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-credentials.png)
8. For **Service Principal ID**, use the application (client) ID of your service principal.

    ![Screenshot that shows the application ID for a service principal.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-sp-appln-id.png)
9. For **Secret name**, use the name of the secret that you created in previous steps.

    ![Screenshot that shows the key vault option to create a secret for a service principal.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-sp-cred.png)

---

## Create the scan

1. Open your Microsoft Purview account and select **Open Microsoft Purview governance portal**.
2. Go to **Data map** &gt; **Sources** to view the collection hierarchy.
3. Select the **New Scan** icon under the SQL database that you registered earlier.

    ![Screenshot that shows the pane for creating a new scan.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-new-scan.png)

To learn more about stored procedure data lineage in Azure SQL Database, see the Extract lineage (preview) section of this article.

For scanning steps, select your method of authentication from the following tabs.

# [SQL authentication](#tab/sql-authentication)
1. For **Name**, provide a name for the scan.
2. For **Database selection method**, select **Enter manually**.
3. For **Database name** and **Credential**, enter the values that you created earlier.

    ![Screenshot that shows database and credential information for the SQL authentication option to run a scan.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-sql-auth.png)
4. For **Select a connection**, choose the appropriate collection for the scan.
5. Select **Test connection** to validate the connection. After the connection is successful, select **Continue**.

# [Managed identity](#tab/managed-identity)
1. For **Name**, provide a name for the scan.
2. Select the SAMI or UAMI under **Credential**, and choose the appropriate collection for the scan.

    ![Screenshot that shows credential and collection information for the managed identity option to run a scan.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-managed-id.png)
3. Select **Test connection**. After the connection is successful, select **Continue**.

    ![Screenshot that shows the message for a successful connection for the managed identity option to run a scan.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-test.png)

# [Service principal](#tab/service-principal)
1. For **Name**, provide a name for the scan.
2. Choose the appropriate collection for the scan, and select the credential that you created earlier under **Credential**.

    ![Screenshot that shows collection and credential information for the service principal option to enable scanning.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-sp.png)
3. Select **Test connection**. After the connection is successful, select **Continue**.

---

## Scope and run the scan

1. You can scope your scan to specific database objects by choosing the appropriate items in the list.

    ![Screenshot that shows options for scoping a scan.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-scope-scan.png)
2. Select a scan rule set. You can use the system default, choose from existing custom rule sets, or create a new rule set inline. Select **Continue** when you're finished.

    ![Screenshot that shows options for selecting a scan rule set.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-scan-rule-set.png)

    If you select **New scan rule set**, a pane opens so that you can enter the source type, the name of the rule set, and a description. Select **Continue** when you're finished.

    ![Screenshot that shows information for creating a new scan rule set.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-new-scan-rule-set.png)

    For **Select classification rules**, choose the classification rules that you want to include in the scan rule set, and then select **Create**.

    ![Screenshot that shows a list of classification rules for a scan rule set.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-classification.png)

    The new scan rule set then appears in the list of available rule sets.

    ![Screenshot that shows the selection of a new scan rule set.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-sel-scan-rule.png)
3. Choose your scan trigger. You can set up a schedule or run the scan once.
4. Review your scan, and then select **Save and run**.

### View a scan

To check the status of a scan, go to the data source in the collection, and then select **View details**.

![Screenshot that shows the button for viewing details of a scan.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-view-scan.png)

The scan details indicate the progress of the scan in **Last run status**, along with the number of assets scanned and classified. **Last run status** is updated to **In progress** and then **Completed** after the entire scan has run successfully.

![Screenshot that shows a completed status for the last scan run.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-scan-complete.png)

### Manage a scan

After you run a scan, you can use the run history to manage it:

1. Under **Recent scans**, select a scan.

    ![Screenshot that shows the selection of a recently completed scan.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-manage scan.png)
2. In the run history, you have options for running the scan again, editing it, or deleting it.

    ![Screenshot that shows options for running, editing, and deleting a scan.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-manage-scan-options.png)

    If you select **Run scan now** to rerun the scan, you can then choose either **Incremental scan** or **Full scan**.

    ![Screenshot that shows options for full or incremental scan.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-full-inc.png)

### Troubleshoot scanning

If you have problems with scanning, try these tips:

- Confirm that you followed all prerequisites.
- Check the network by confirming firewall, Azure connections, or integration runtime settings.
- Confirm that authentication is properly set up.

For more information, review [Troubleshoot your connections in Microsoft Purview](troubleshoot-connections).

## Set up policies

The following types of Microsoft Purview policies are supported on this data resource:

- [Data owner policies](concept-policies-data-owner) - a set of policy statements that allow you to grant users and groups access to data sources.
- [Self-service policies](concept-self-service-data-access-policy) - policy that allows users to request access to data sources registered to Microsoft Purview.
- [DevOps policies](concept-policies-devops) - grants access to database system metadata across multiple sources. They simplify access provisioning for IT operations and security auditing personnel. They only grant access, and don't deny access.

### Access policy prerequisites on Azure SQL Database

- Create a new Azure SQL Database instance, or use an existing one, in one of the currently available regions for this feature. You can follow [this guide to create an Azure SQL Database instance](/en-us/azure/azure-sql/database/single-database-create-quickstart).

#### Region support

All [Microsoft Purview regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=purview) are supported.

Enforcement of Microsoft Purview policies is available only in the following regions for Azure SQL Database:

Public cloud:

- East US
- East US2
- South Central US
- West Central US
- West US3
- Canada Central
- Brazil South
- West Europe
- North Europe
- France Central
- UK South
- South Africa North
- Central India
- South East Asia
- East Asia
- Australia East

Sovereign clouds:

- USGov Virginia
- China North 3

#### Configure the Azure SQL Database instance for policies from Microsoft Purview

For the logical server associated with Azure SQL Database to honor policies from Microsoft Purview, you need to configure a Microsoft Entra admin. In the Azure portal, go to the logical server that hosts the Azure SQL Database instance. On the side menu, select **Microsoft Entra ID**. Set an admin name to any Microsoft Entra user or group that you prefer, and then select **Save**.

Then, on the side menu, select **Identity**. Under **System assigned managed identity**, turn the status to **On**, and then select **Save**.

![Screenshot that shows the assignment of a system-assigned managed identity to a logical server associated with Azure SQL Database.](media/how-to-policies-data-owner-sql/assign-identity-azure-sql-db.png)

### Configure the Microsoft Purview account for policies

#### Register the data source in Microsoft Purview

Before a policy can be created in Microsoft Purview for a data resource, you must register that data resource in Microsoft Purview Studio. You will find the instructions related to registering the data resource later in this guide.

Note

Microsoft Purview policies rely on the data resource ARM path. If a data resource is moved to a new resource group or subscription it will need to be de-registered and then registered again in Microsoft Purview.

#### Configure permissions to enable Data policy enforcement on the data source

Once a resource is registered, but before a policy can be created in Microsoft Purview for that resource, you must configure permissions. A set of permissions are needed to enable the **Data policy enforcement**. This applies to data sources, resource groups, or subscriptions. To enable *Data policy enforcement*, you must have *both* specific Identity and Access Management (IAM) privileges on the resource as well as specific Microsoft Purview privileges:

- You must have *either one* of the following IAM role combinations on the resource's Azure Resource Manager path or any parent of it (that is, using IAM permission inheritance):

    - IAM Owner
    - Both IAM Contributor and IAM User Access Administrator

    To configure Azure role-based access control (RBAC) permissions, follow [this guide](/en-us/azure/role-based-access-control/check-access). The following screenshot shows how to access the **Access Control** section in the Azure portal for the data resource to add a role assignment.

    [![Screenshot that shows the section in the Azure portal for adding a role assignment.](media/how-to-policies-data-owner-authoring-generic/assign-iam-permissions.png)](media/how-to-policies-data-owner-authoring-generic/assign-iam-permissions.png#lightbox)

    Note

    The *IAM Owner* role for a data resource can be inherited from a parent resource group, a subscription, or a subscription management group. Check which Microsoft Entra users, groups, and service principals hold or are inheriting the *IAM Owner* role for the resource.
- You also need to have the Microsoft Purview *Data source admin* role for the collection or a parent collection (if inheritance is enabled). For more information, see the [guide on managing Microsoft Purview role assignments](data-gov-classic-permissions#assign-permissions-to-your-users).

    The following screenshot shows how to assign the *Data source admin* role at the root collection level.

    [![Screenshot that shows selections for assigning the Data source admin role at the root collection level.](media/how-to-policies-data-owner-authoring-generic/assign-purview-permissions.png)](media/how-to-policies-data-owner-authoring-generic/assign-purview-permissions.png#lightbox)

#### Configure Microsoft Purview permissions to create, update, or delete access policies

To create, update or delete policies, you need to get the *Policy author* role in Microsoft Purview at *root collection level*:

- The *Policy author* role can create, update, and delete DevOps and Data Owner policies.
- The *Policy author* role can delete self-service access policies.

For more information about managing Microsoft Purview role assignments, see [Create and manage collections in the Microsoft Purview Data Map](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Note

Policy author role must be configured at the root collection level.

In addition, to easily search Microsoft Entra users or groups when creating or updating the subject of a policy, you can greatly benefit from getting the [Directory Readers](/en-us/azure/active-directory/roles/permissions-reference#directory-readers) permission in Microsoft Entra ID. This is a common permission for users in an Azure tenant. Without the Directory Reader permission, the Policy Author will have to type the complete username or email for all the principals included in the subject of a data policy.

#### Configure Microsoft Purview permissions for publishing Data Owner policies

Data Owner policies allow for checks and balances if you assign the Microsoft Purview *Policy author* and *Data source admin* roles to different people in the organization. Before a Data owner policy takes effect, a second person (*Data source admin*) must review it and explicitly approve it by publishing it. This does not apply to DevOps or Self-service access policies as publishing is automatic for them when those policies are created or updated.

To publish a Data owner policy you need to get the *Data source admin* role in Microsoft Purview at *root collection level*.

For more information about managing Microsoft Purview role assignments, see [Create and manage collections in the Microsoft Purview Data Map](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Note

To publish Data owner policies, the Data source admin role must be configured at the root collection level.

#### Delegate access provisioning responsibility to roles in Microsoft Purview

After a resource has been enabled for **Data policy enforcement**, any Microsoft Purview user with the *Policy author* role at the root collection level can provision access to that data source from Microsoft Purview.

Note

Any Microsoft Purview root *Collection admin* can assign new users to root *Policy author* roles. Any *Collection admin* can assign new users to a *Data source admin* role under the collection. Minimize and carefully vet the users who hold Microsoft Purview *Collection admin*, *Data source admin*, or *Policy author* roles.

If a Microsoft Purview account with published policies is deleted, such policies will stop being enforced within an amount of time that depends on the specific data source. This change can have implications on both security and data access availability. The Contributor and Owner roles in IAM can delete Microsoft Purview accounts. You can check these permissions by going to the **Access control (IAM)** section for your Microsoft Purview account and selecting **Role Assignments**. You can also use a lock to prevent the Microsoft Purview account from being deleted through [Resource Manager locks](/en-us/azure/azure-resource-manager/management/lock-resources).

### Register the data source and enable Data policy enforcement

The Azure SQL Database resource needs to be registered with Microsoft Purview before you can create access policies. To register your resources, follow the "Prerequisites" and "Register the data source" sections in [Enable Data policy enforcement on your Microsoft Purview sources](register-scan-azure-sql-database#prerequisites).

After you register the data source, you need to enable **Data policy enforcement**. This is a prerequisite before you can create policies on the data source. **Data policy enforcement** can affect the security of your data, because it delegates to certain Microsoft Purview roles that manage access to the data sources. Go through the security practices in [Enable Data policy enforcement on your Microsoft Purview sources](how-to-enable-data-policy-enforcement).

After your data source has the **Data policy enforcement** option set to **Enabled**, it will look like this screenshot:

![Screenshot that shows the panel for registering a data source for a policy, including areas for name, server name, and data policy enforcement.](media/how-to-policies-data-owner-sql/enable-policy-enforcement-azure-sql-db.png)

Return to the Azure portal for Azure SQL Database to verify it's now governed by Microsoft Purview:

1. Sign in to the Azure portal through [this link](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Sql%2Fservers).
2. Select the Azure SQL Server that you want to configure.
3. Go to **Microsoft Entra ID** on the left pane.
4. Scroll down to **Microsoft Purview access policies**.
5. Select the button to **Check for Microsoft Purview Governance**. Wait while the request is processed, which could take a few minutes.

    [![Screenshot that shows Azure SQL is governed by Microsoft Purview.](media/how-to-policies-data-owner-sql/check-governed-status-azure-sql-db.png)](media/how-to-policies-data-owner-sql/check-governed-status-azure-sql-db.png#lightbox)
6. Confirm that the Microsoft Purview Governance Status shows **Governed**. Note that **it could take a few minutes** after you enable *Data policy enforcement* in Microsoft Purview for the correct status to be reflected.

Note

If you disable data policy enforcement for this Azure SQL Database data source in Microsoft Purview, select **Check for Microsoft Purview Governance** for the Microsoft Purview Governance Status to be updated to **Not Governed**. This step must be done for the impacted data source each time data policy enforcement status is changed for an existing or new access policy in Microsoft Purview. Before you enable *Data policy enforcement* for the data source in another Microsoft Purview account, ensure that the Purview Governance Status shows as **Not Governed**. Then repeat the steps above with the new Microsoft Purview account.

### Create an access policy

To create an access policy for Azure SQL Database, follow these guides:

- [Provision access to system health, performance, and audit information in Azure SQL Database](how-to-policies-devops-azure-sql-db#create-a-new-devops-policy). Use this guide to apply a DevOps policy on a single SQL database.
- [Provision read/modify access on a single Azure SQL Database](how-to-policies-data-owner-azure-sql-db#create-and-publish-a-data-owner-policy). Use this guide to provision access on a single SQL database account in your subscription.
- [Self-service access policies for Azure SQL Database](how-to-policies-self-service-azure-sql-db). Use this guide to allow data consumers to request access to data assets by using a self-service workflow.

To create policies that cover all data sources inside a resource group or Azure subscription, see [Discover and govern multiple Azure sources in Microsoft Purview](register-scan-azure-multiple-sources#policies).

## Extract lineage (preview)

Microsoft Purview supports lineage for views and stored procedures from Azure SQL Database. While lineage for views is supported as part of scanning, you'll need to turn on the **Lineage extraction** toggle to extract stored procedure lineage when you're setting up a scan.

Note

Lineage isn't supported using a self-hosted integration runtime or managed VNET runtime and an Azure SQL private endpoint. You need to enable Azure services to access the server under network settings for your Azure SQL Database, and your Microsoft Purview account needs to allow public access. Learn more about the known limitations in lineage extraction scan.

### Lineage for SQL DB views

SQL DB metadata scan includes lineage extraction for views. Only new scans include the view lineage extraction. Lineage is extracted at all scan levels (L1/L2/L3). In case of an incremental scan, whatever metadata is scanned as part of incremental scan, the corresponding static lineage for tables/views will be extracted.

![Screenshot that shows lineage details for SQL DB views.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-view-lineage.png)

### Prerequisites for setting up a scan with SP lineage extraction

1. Follow the steps in the Configure authentication for a scan section of this article to authorize Microsoft Purview to scan your SQL database.
2. Sign in to Azure SQL Database with your Microsoft Entra account, and assign `db_owner` permissions to the Microsoft Purview managed identity.

    Note

    The 'db\_owner' permissions is needed because lineage is based on XEvent sessions. So Microsoft Purview needs the permission to manage the XEvent sessions in SQL.

    Use the following example SQL syntax to create a user and grant permission. Replace `<purview-account>` with your account name.

    ```sql
    Create user <purview-account> FROM EXTERNAL PROVIDER
    GO
    EXEC sp_addrolemember 'db_owner', <purview-account> 
    GO
    ```
3. Run the following command on your SQL database to create a master key:

    ```sql
    Create master key
    Go
    ```
4. Ensure that **Allow Azure services and resources to access this server** is enabled under networking/firewall for your Azure SQL resource.

### Create a scan with lineage extraction turned on

1. On the pane for setting up a scan, turn on the **Enable lineage extraction** toggle.

    [![Screenshot that shows the pane for creating a new scan, with lineage extraction turned on.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-lineage-extraction.png)](media/register-scan-azure-sql-database/register-scan-azure-sql-db-lineage-extraction-expanded.png#lightbox)
2. Select your method of authentication by following the steps in the Create the scan section of this article.
3. After you successfully set up the scan, a new scan type called **Lineage extraction** will run incremental scans **every six hours** to extract lineage from Azure SQL Database. Lineage is extracted based on the stored procedure runs in the SQL database.

    [![Screenshot that shows the screen that runs lineage extraction every six hours.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-lineage-extraction-runs.png)](media/register-scan-azure-sql-database/register-scan-azure-sql-db-lineage-extraction-runs-expanded.png#lightbox)

### Search Azure SQL Database assets and view runtime lineage

You can [browse through the Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search the Unified Catalog](unified-catalog-data-assets-search) to view asset details for Azure SQL Database. The following steps describe how to view runtime lineage details:

1. Go to the **Lineage** tab for the asset. When applicable, the asset lineage appears here.

    ![Screenshot that shows lineage details from stored procedures.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-lineage.png)

    When applicable, you can further drill down to see the lineage at SQL statement level within a stored procedure, along with column level lineage. When using Self-hosted Integration Runtime for scan, retrieving the lineage drilldown information during scan is supported since version 5.25.8374.1.

    ![Screenshot that shows stored procedure lineage drilldown.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-lineage-drilldown.png)

    For information about supported Azure SQL Database lineage scenarios, refer to the Supported capabilities section of this article. For more information about lineage in general, see [Data lineage in Microsoft Purview](data-gov-classic-lineage) and [Microsoft Purview lineage user guide](data-gov-classic-lineage-user-guide).
2. Go to the stored procedure asset. On the **Properties** tab, go to **Related assets** to get the latest run details of stored procedures.

    ![Screenshot that shows run details for stored procedure properties.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-stored-procedure-properties.png)
3. Select the stored procedure hyperlink next to **Runs** to see the **Azure SQL Stored Procedure Run** overview. Go to the **Properties** tab to see enhanced runtime information from the stored procedure, such as **executedTime**, **rowCount**, and **Client Connection**.

    [![Screenshot that shows run properties for a stored procedure.](media/register-scan-azure-sql-database/register-scan-azure-sql-db-stored-procedure-run-properties.png)](media/register-scan-azure-sql-database/register-scan-azure-sql-db-stored-procedure-run-properties-expanded.png#lightbox)

### Troubleshoot lineage extraction for Stored Procedures

The following tips can help you solve problems related to lineage:

- If no lineage is captured after a successful **Lineage extraction** run, it's possible that no stored procedures have run at least once since you set up the scan.
- Lineage is captured for stored procedure runs that happen after a successful scan is set up. Lineage from past stored procedure runs isn't captured.
- If your database is processing heavy workloads with lots of stored procedure runs, lineage extraction filters only the most recent runs. Stored procedure runs early in the six-hour window, or the run instances that create heavy query load, won't be extracted. Contact support if you're missing lineage from any stored procedure runs.
- If a stored procedure contains drop or create statements, they aren't currently captured in lineage