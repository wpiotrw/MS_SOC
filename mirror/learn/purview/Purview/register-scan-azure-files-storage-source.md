---
layout: Conceptual
title: Connect to and manage Azure Files in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-files-storage-source
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
description: Learn how to connect to Azure Files in Microsoft Purview, and use Microsoft Purview features to scan and manage your Azure Files source.
locale: en-us
document_id: f19296d3-c88a-0e01-f8f3-e59b8c7abd3c
document_version_independent_id: f19296d3-c88a-0e01-f8f3-e59b8c7abd3c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-files-storage-source.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-files-storage-source
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-files-storage-source.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/01a89bec-e73f-4ce0-a00a-ae34ad62e5fe
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/50038ab9-5431-4515-9dfc-c24291ef4fce
platformId: c294f80b-0193-5345-8862-2e6dcf3845e3
---

# Connect to and manage Azure Files in Microsoft Purview | Microsoft Learn

This article outlines how to register Azure Files, and how to authenticate and interact with Azure Files in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

Azure Files supports full and incremental scans to capture the metadata and classifications, based on system default and custom classification rules.

For file types such as .csv, .tsv, .psv, and .ssv, the schema is extracted when the following logics are in place:

1. First row values are nonempty.
2. First row values are unique.
3. First row values are not a date or a number.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You'll need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

## Register

This section describes how to register Azure Files in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Authentication for registration

Currently there's only one way to set up authentication for Azure file shares:

- Account Key

#### Account Key to register

When authentication method selected is **Account Key**, you need to get your access key and store in the key vault:

1. Navigate to your storage account
2. Select **Security + networking &gt; Access keys**
3. Copy your *key* and save it somewhere for the next steps
4. Navigate to your key vault
5. Select **Objects &gt; Secrets**
6. Select **+ Generate/Import** and enter the **Name** and **Value** as the *key* from your storage account
7. Select **Create** to complete
8. If your key vault isn't connected to Microsoft Purview yet, you'll need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
9. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) using the key to set up your scan

### Steps to register

To register a new Azure Files account in Microsoft Purview Unified Catalog, follow these steps:

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On **Register sources**, select **Azure Files**
5. Select **Continue**

![register new data source](media/register-scan-azure-files/register-sources.png)

On the **Register sources (Azure Files)** screen, follow these steps:

1. Enter a **Name** that the data source will be listed with in the Catalog.
2. Choose your Azure subscription to filter down Azure Storage Accounts.
3. Select an Azure Storage Account.
4. Select a collection from the list.
5. Select **Register** to register the data source.

![register sources options](media/register-scan-azure-files/azure-file-register-source.png)

## Scan

Follow the steps below to scan Azure Files to automatically identify assets and classify your data. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion)

### Create and run scan

To create and run a new scan, follow these steps:

1. Select the **Data Map** tab on the left pane in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select the Azure Files source that you registered.
3. Select **New scan**
4. Choose either the Azure integration runtime if your source is publicly accessible, a [managed virtual network integration runtime](data-governance-private-endpoints-managed-virtual-network) if using a managed virtual network, or a self-hosted integration runtime if your source is in a private virtual network. For more information about which integration runtime to use, see the [choose the right integration runtime configuration article.](data-map-integration-runtime-choose#choose-the-right-integration-runtime)
5. Select the account key credential to connect to your data source.

    ![Set up scan](media/register-scan-azure-files/set-up-scan-azure-file.png)
6. You can scope your scan to specific databases by choosing the appropriate items in the list.

    ![Scope your scan](media/register-scan-azure-files/azure-file-scope-your-scan.png)
7. Then select a scan rule set. You can choose between the system default, existing custom rule sets, or create a new rule set inline.

    ![Scan rule set](media/register-scan-azure-files/azure-file-scan-rule-set.png)
8. Choose your scan trigger. You can set up a schedule to reoccur, or run the scan once.

    ![trigger](media/register-scan-azure-files/trigger-scan.png)
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