---
layout: Conceptual
title: Connect to Azure Cosmos DB for SQL API in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-cosmos-database
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.date: 2025-05-21T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand the process to register an Azure Cosmos DB instance in Microsoft Purview, including instructions to authenticate and interact with the Azure Cosmos DB database.
ms.custom: sfi-image-nochange
locale: en-us
document_id: b7b09dc8-2e11-b9fc-155b-bb97761799de
document_version_independent_id: b7b09dc8-2e11-b9fc-155b-bb97761799de
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-cosmos-database.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-cosmos-database
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-cosmos-database.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cd668c2f-f5b3-4573-8ad1-019570e3e2db
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/cc82e69d-afbe-4554-9f4c-6705fc860c42
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
platformId: c64099db-c923-83cb-eb9a-cb253e45b115
---

# Connect to Azure Cosmos DB for SQL API in Microsoft Purview | Microsoft Learn

This article outlines the process to register and scan Azure Cosmos DB for SQL API instance in Microsoft Purview, including instructions to authenticate and interact with the Azure Cosmos DB database source

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You will need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

## Register

This section will enable you to register the Azure Cosmos DB for SQL API instance and set up an appropriate authentication mechanism to ensure successful scanning of the data source.

### Steps to register

It is important to register the data source in Microsoft Purview prior to setting up a scan for the data source.

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Select the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Navigate to the **Data Map --&gt; Collections**

    ![Screenshot that navigates to the Sources link in the Data Map](media/register-scan-azure-cosmos-database/register-cosmos-db-open-purview-studio.png)
3. Create the [Collection hierarchy](data-map-collections-create-classic) using the **Collections** menu and assign permissions to individual subcollections, as required

    ![Screenshot that shows the collection menu to create collection hierarchy](media/register-scan-azure-cosmos-database/register-cosmos-db-collections.png)
4. Navigate to the appropriate collection under the **Sources** menu and select the **Register** icon to register a new Azure Cosmos DB database

    ![Screenshot that shows the collection used to register the data source](media/register-scan-azure-cosmos-database/register-cosmos-db-register-data-source.png)
5. Select the **Azure Cosmos DB for SQL API** data source and select **Continue**

    ![Screenshot that allows selection of the data source](media/register-scan-azure-cosmos-database/register-cosmos-db-select-data-source.png)
6. Provide a suitable **Name** for the data source, select the relevant **Azure subscription**, **Cosmos DB account name** and the **collection** and select **Apply**

    ![Screenshot that shows the details to be entered in order to register the data source](media/register-scan-azure-cosmos-database/register-cosmos-db-data-source-details.png)
7. The *Azure Cosmos DB database* storage account will be shown under the selected Collection

    ![Screenshot that shows the data source mapped to the collection to initiate scanning](media/register-scan-azure-cosmos-database/register-cosmos-db-collection-mapping.png)

## Scan

### Authentication for a scan

In order to have access to scan the data source, an authentication method in the Azure Cosmos DB database Storage account needs to be configured.

There is only one way to set up authentication for Azure Cosmos DB Database:

**Account Key** - Secrets can be created inside an Azure Key Vault to store credentials in order to enable access for Microsoft Purview to scan data sources securely using the secrets. A secret can be a storage account key, SQL login password or a password.

Note

You need to deploy an *Azure key vault* resource in your subscription and assign *Microsoft Purview account’s* MSI with required access permission to secrets inside *Azure key vault*.

#### Using Account Key for scanning

You need to get your access key and store in the key vault:

1. Navigate to your Azure Cosmos DB database storage account
2. Select **Settings &gt; Keys**

    ![Screenshot that shows the access keys in the storage account](media/register-scan-azure-cosmos-database/register-cosmos-db-access-keys.png)
3. Copy your *key* and save it separately for the next steps

    ![Screenshot that shows the access keys to be copied](media/register-scan-azure-cosmos-database/register-cosmos-db-key.png)
4. Navigate to your key vault

    ![Screenshot that shows the key vault](media/register-scan-azure-cosmos-database/register-cosmos-db-key-vault.png)
5. Select **Settings &gt; Secrets** and select **+ Generate/Import**

    ![Screenshot that shows the key vault option to generate a secret](media/register-scan-azure-cosmos-database/register-cosmos-db-generate-secret.png)
6. Enter the **Name** and **Value** as the *key* from your storage account and Select **Create** to complete

    ![Screenshot that shows the key vault option to enter the secret values](media/register-scan-azure-cosmos-database/register-cosmos-db-key-vault-options.png)
7. If your key vault is not connected to Microsoft Purview yet, you will need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
8. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) using the key to set up your scan.

### Creating the scan

1. Open your **Microsoft Purview account** and select the **Open Microsoft Purview governance portal**
2. Navigate to the **Data map** --&gt; **Sources** to view the collection hierarchy
3. Select the **New Scan** icon under the **Azure Cosmos database** registered earlier

    ![Screenshot that shows the screen to create a new scan](media/register-scan-azure-cosmos-database/register-cosmos-db-create-scan.png)
4. Provide a **Name** for the scan.
5. Choose either the Azure integration runtime if your source is publicly accessible, a [managed virtual network integration runtime](data-governance-private-endpoints-managed-virtual-network) if using a managed virtual network, or a self-hosted integration runtime if your source is in a private virtual network. For more information about which integration runtime to use, see the [choose the right integration runtime configuration article.](data-map-integration-runtime-choose#choose-the-right-integration-runtime)
6. Choose the appropriate collection for the scan and select **+ New** under **Credential**

    ![Screenshot that shows the Account Key option for scanning](media/register-scan-azure-cosmos-database/register-cosmos-db-acct-key-option.png)
7. Select the appropriate **Key vault connection** and the **Secret name** that was used while creating the *Account Key*. Choose **Authentication method** as *Account Key*

    ![Screenshot that shows the account key options](media/register-scan-azure-cosmos-database/register-cosmos-db-acct-key-details.png)
8. Select **Test connection**. On a successful connection, select **Continue**

    ![Screenshot that shows Test Connection success](media/register-scan-azure-cosmos-database/register-cosmos-db-test-connection.png)

### Scoping and running the scan

1. You can scope your scan to specific folders and subfolders by choosing the appropriate items in the list.

    ![Scope your scan](media/register-scan-azure-cosmos-database/register-cosmos-db-scope-scan.png)
2. Then select a scan rule set. You can choose between the system default, existing custom rule sets, or create a new rule set inline.

    ![Scan rule set](media/register-scan-azure-cosmos-database/register-cosmos-db-scan-rule-set.png)

    ![New Scan rule](media/register-scan-azure-cosmos-database/register-cosmos-db-new-scan-rule-set.png)
3. You can select the **classification rules** to be included in the scan rule

    ![Scan rule set classification rules](media/register-scan-azure-cosmos-database/register-cosmos-db-classification.png)

    ![Scan rule set selection](media/register-scan-azure-cosmos-database/register-cosmos-db-select-scan-rule-set.png)
4. Choose your scan trigger. You can set up a schedule or run the scan once.

    ![scan trigger](media/register-scan-azure-cosmos-database/register-cosmos-db-scan-trigger.png)
5. Review your scan and select **Save and run**.

    ![review scan](media/register-scan-azure-cosmos-database/register-cosmos-db-review-scan.png)

### Viewing Scan

1. Navigate to the *data source* in the *Collection* and select **View Details** to check the status of the scan

    ![view scan](media/register-scan-azure-cosmos-database/register-cosmos-db-view-scan.png)
2. The scan details indicate the progress of the scan in the **Last run status** and the number of assets *scanned* and *classified*

    ![view scan details](media/register-scan-azure-cosmos-database/register-cosmos-db-last-run-status.png)
3. The **Last run status** will be updated to **In progress** and then **Completed** once the entire scan has run successfully

    ![view scan in progress](media/register-scan-azure-cosmos-database/register-cosmos-db-scan-in-progress.png)

    ![view scan completed](media/register-scan-azure-cosmos-database/register-cosmos-db-scan-completed.png)

### Managing Scan

Scans can be managed or run again on completion.

1. Select the **Scan name** to manage the scan

    ![manage scan](media/register-scan-azure-cosmos-database/register-cosmos-db-manage-scan.png)
2. You can *run the scan* again, *edit the scan*, *delete the scan*

    ![manage scan options](media/register-scan-azure-cosmos-database/register-cosmos-db-manage-scan-options.png)
3. You can run a *Full Scan* again

    ![full scan](media/register-scan-azure-cosmos-database/register-cosmos-db-full-scan.png)