---
layout: Conceptual
title: Connect to and manage dedicated SQL pools (formerly SQL DW) in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-synapse-analytics
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
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
description: Learn how to connect to dedicated SQL pools (formerly SQL DW) in Microsoft Purview, and use Microsoft Purview features to scan and manage your dedicated SQL pools source.
locale: en-us
document_id: 158c2539-a98e-b28d-1dee-2f21bfc2e7db
document_version_independent_id: 158c2539-a98e-b28d-1dee-2f21bfc2e7db
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-synapse-analytics.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-synapse-analytics
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-synapse-analytics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/bad69977-db6a-44f3-b752-d2bee7de49ca
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31d7aff-61be-45e2-a324-a578cf0c3360
platformId: f37c5512-6838-8736-69f8-18ba3f2d6741
---

# Connect to and manage dedicated SQL pools (formerly SQL DW) in Microsoft Purview | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register dedicated SQL pools (formerly SQL DW), and how to authenticate and interact with dedicated SQL pools in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

Note

There are dedicated SQL pools (formerly SQL DW) and dedicated SQL pools in Azure Synapse workspace and you can refer to [What is the difference between dedicated SQL pools (SQL DW) and dedicated SQL pools in Azure Synapse workspaces](/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-overview-faq#what-is-the-difference-between-dedicated-sql-pools--sql-dw--and-dedicated-sql-pools-in-azure-synapse-workspaces-) for the detail difference between the two. Currently Microsoft Purview provides separate data sources for dedicated SQL pools (formerly SQL DW) and dedicated SQL pools:

- if you are looking to register and scan a dedicated SQL pool (formerly SQL DW), you can follow instructions in [Connect to and manage dedicated SQL pools in Microsoft Purview](register-scan-azure-synapse-analytics).
- if you are looking to register and scan a dedicated SQL pool (formerly SQL DW) which has enabled Azure Synapse workspace features as documented in [Enable Azure Synapse workspace features for a dedicated SQL pool (formerly SQL DW)](/en-us/azure/synapse-analytics/sql-data-warehouse/workspace-connected-create), you can also follow instructions in [Connect to and manage Azure Synapse Analytics workspaces in Microsoft Purview](register-scan-synapse-workspace).
- if you are looking to register and scan a dedicated SQL pool or a serverless SQL pool in Azure Synapse workspace, you must follow instructions in [Connect to and manage Azure Synapse Analytics workspaces in Microsoft Purview](register-scan-synapse-workspace).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

When scanning dedicated SQL pool (formerly SQL DW) source, Microsoft Purview supports extracting technical metadata including:

- Server
- Dedicated SQL pools
- Schemas
- Tables including columns
- Views including columns

When setting up the scan, you can further scope it after providing the dedicated SQL pool name by selecting tables and views as needed.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You will need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

## Register

This section describes how to register dedicated SQL pools in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Authentication for registration

There are three ways to set up authentication:

- System or user assigned managed identity (Recommended)
- Service Principal
- SQL authentication

    Note

    Only the server-level principal login (created by the provisioning process) or members of the `loginmanager` database role in the master database can create new logins. It takes about 15 minutes after granting permission, the Microsoft Purview account should have the appropriate permissions to be able to scan the resource(s).

#### System or user assigned managed identity to register

You can use either your Microsoft Purview system-assigned managed identity (SAMI), or a [User-assigned managed identity](data-map-data-scan-credentials#create-a-user-assigned-managed-identity) (UAMI) to authenticate. Both options allow you to assign authentication directly to Microsoft Purview, like you would for any other user, group, or service principal. The Microsoft Purview SAMI is created automatically when the account is created. A UAMI is a resource that can be created independently, and to create one you can follow our [user-assigned managed identity guide](data-map-data-scan-credentials#create-a-user-assigned-managed-identity). Create a Microsoft Entra user in the dedicated SQL pool using your managed identity object name by following the prerequisites and tutorial on [Create Microsoft Entra users using Microsoft Entra applications](/en-us/azure/azure-sql/database/authentication-aad-service-principal-tutorial).

Example SQL syntax to create user and grant permission:

```sql
CREATE USER [PurviewManagedIdentity] FROM EXTERNAL PROVIDER
GO

EXEC sp_addrolemember 'db_datareader', [PurviewManagedIdentity]
GO
```

The authentication must have permission to get metadata for the database, schemas, and tables. It must also be able to query the tables to sample for classification. The recommendation is to assign `db_datareader` permission to the identity.

#### Service Principal to register

To use service principal authentication for scans, you can use an existing one or create a new one.

If you need to create a new Service Principal, follow these steps:

1. Navigate to the [Azure portal](https://portal.azure.com).
2. Select **Microsoft Entra ID** from the left-hand side menu.
3. 1. Select **App registrations**.
4. Select **+ New application registration**.
5. Enter a name for the **application** (the service principal name).
6. Select **Accounts in this organizational directory only**.
7. For Redirect URI, select **Web** and enter any URL you want; it doesn't have to be real or work.
8. Then select **Register**.

It is required to get the Service Principal's application ID and secret:

1. Navigate to your Service Principal in the [Azure portal](https://portal.azure.com)
2. Copy the values the **Application (client) ID** from **Overview** and **Client secret** from **Certificates & secrets**.
3. Navigate to your key vault
4. Select **Settings &gt; Secrets**
5. Select **+ Generate/Import** and enter the **Name** of your choice and **Value** as the **Client secret** from your Service Principal
6. Select **Create** to complete
7. If your key vault is not connected to Microsoft Purview yet, you will need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
8. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) using the Service Principal to set up your scan.

##### Granting the Service Principal access

In addition, you must also create a Microsoft Entra user in the dedicated pool by following the prerequisites and tutorial on [Create Microsoft Entra users using Microsoft Entra applications](/en-us/azure/azure-sql/database/authentication-aad-service-principal-tutorial). Example SQL syntax to create user and grant permission:

```sql
CREATE USER [ServicePrincipalName] FROM EXTERNAL PROVIDER
GO

ALTER ROLE db_datareader ADD MEMBER [ServicePrincipalName]
GO
```

Note

Microsoft Purview will need the **Application (client) ID** and the **client secret** in order to scan.

#### SQL authentication to register

You can follow the instructions in [CREATE LOGIN](/en-us/sql/t-sql/statements/create-login-transact-sql?view=azure-sqldw-latest&amp;preserve-view=true#examples-1) to create a login for your dedicated SQL pool (formerly SQL DW) if you don't already have one.

When authentication method selected is **SQL Authentication**, you need to get your password and store in the key vault:

1. Get the password for your SQL login
2. Navigate to your key vault
3. Select **Settings &gt; Secrets**
4. Select **+ Generate/Import** and enter the **Name** and **Value** as the *password* for your SQL login
5. Select **Create** to complete
6. If your key vault is not connected to Microsoft Purview yet, you will need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
7. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) using the key to set up your scan.

### Steps to register

To register a new SQL dedicated pool in Microsoft Purview, complete the following steps:

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Select the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On **Register sources**, select **Azure Dedicated SQL Pool (formerly SQL DW)**.
5. Select **Continue**

On the **Register sources** screen, complete the following steps:

1. Enter a **Name** that the data source will be listed with in the Catalog.
2. Choose your Azure subscription to filter down dedicated SQL pools.
3. Select your dedicated SQL pool.
4. Select a collection from the list.
5. Select **Register** to register the data source.

## Scan

Follow the steps below to scan dedicated SQL pools to automatically identify assets and classify your data. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion)

### Create and run scan

To create and run a new scan, complete the following steps:

1. Select the **Data Map** tab on the left pane in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select the SQL dedicated pool source that you registered.
3. Select **New scan**
4. Choose either the Azure integration runtime if your source is publicly accessible, a [managed virtual network integration runtime](data-governance-private-endpoints-managed-virtual-network) if using a managed virtual network, or a self-hosted integration runtime if your source is in a private virtual network. For more information about which integration runtime to use, see the [choose the right integration runtime configuration article.](data-map-integration-runtime-choose#choose-the-right-integration-runtime)
5. Select the credential to connect to your data source.

    ![Set up scan](media/register-scan-azure-synapse-analytics/sql-dedicated-pool-set-up-scan.png)
6. You can scope your scan to specific tables by choosing the appropriate items in the list.

    ![Scope your scan](media/register-scan-azure-synapse-analytics/scope-scan.png)
7. Then select a scan rule set. You can choose between the system default, existing custom rule sets, or create a new rule set inline.

    ![Scan rule set](media/register-scan-azure-synapse-analytics/select-scan-rule-set.png)
8. Choose your scan trigger. You can set up a schedule or run the scan once.

    ![trigger](media/register-scan-azure-synapse-analytics/trigger-scan.png)
9. Review your scan and select **Save and run**.

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