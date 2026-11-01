---
layout: Conceptual
title: Connect to and manage an Azure Database for PostgreSQL | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-postgresql
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to an Azure Database for PostgreSQL single server in Microsoft Purview, and use Microsoft Purview's features to scan and manage your Azure Database for PostgreSQL source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: shjia
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2026-03-13T00:00:00.0000000Z
ms.custom: template-how-to, ignite-fall-2021
locale: en-us
document_id: 1bdb53ed-7b8c-b719-0a27-c93ad910cdf1
document_version_independent_id: 1bdb53ed-7b8c-b719-0a27-c93ad910cdf1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-postgresql.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-postgresql
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-postgresql.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9527be-7cdf-4bdd-8574-272df09987d3
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e87f9e59-cf8f-4272-9365-9d20f2c3efe5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: d4424d1b-0fc2-6df7-276e-31f248978728
---

# Connect to and manage an Azure Database for PostgreSQL | Microsoft Learn

This article outlines how to register an Azure Database for PostgreSQL deployed with single server deployment option, and how to authenticate and interact with an Azure Database for PostgreSQL in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

Important

Microsoft Purview only supports single server deployment option for Azure Database for PostgreSQL. Versions 8.x to 12.x.

> 
> **Azure Database for PostgreSQL single server retired in March 2025. We are working on bringing support for Azure Database for PostgreSQL Flex server.**

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You'll need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

## Register

This section describes how to register an Azure Database for PostgreSQL in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Authentication for registration

Currently, to be able to manage and interact with an Azure Database for PostgreSQL single server, only SQL Authentication is supported.

#### SQL Authentication

Connecting to an Azure Database for PostgreSQL database requires the fully qualified server name and login credentials. You can follow the instructions in [CONNECT AND QUERY](/en-us/azure/postgresql/connect-python) to create a login for your Azure Database for PostgreSQL if you don't have this available. You'll need **username** and **password** for the next steps.

1. If you don't have an Azure Key vault already, follow [this guide to create an Azure Key Vault](/en-us/azure/key-vault/certificates/quick-create-portal).
2. Navigate to your key vault in the Azure portal
3. Select **Settings &gt; Secrets**
4. Select **+ Generate/Import** and enter the **Name** and **Value** as the *password* from your Azure PostgreSQL Database
5. Select **Create** to complete
6. If your key vault isn't connected to Microsoft Purview yet, you'll need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
7. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) of type SQL authentication using the **username** and **password** to set up your scan

### Steps to register

To register a new Azure Database for PostgreSQL in Microsoft Purview Unified Catalog, do the following:

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On **Register sources**, select **Azure Database for PostgreSQL**. Select **Continue**.

![register new data source](media/register-scan-azure-postgresql/01-register-azure-postgres.png)

On the **Register sources Azure Database for PostgreSQL** screen, do the following:

1. Enter a **Name** for your data source. This will be the display name for this data source in your Catalog.
2. Select **From Azure subscription**, select the appropriate subscription from the **Azure subscription** drop-down box and the appropriate server from the **Server name** drop-down box.
3. Select **Register** to register the data source.

![register sources options](media/register-scan-azure-postgresql/02-register-source-azure-postgres.png)

## Scan

Follow the steps below to scan an Azure Database for PostgreSQL database to automatically identify assets and classify your data. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion)

### Create and run scan

To create and run a new scan, do the following:

1. Select the **Data Map** tab on the left pane in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select the Azure Database for PostgreSQL source that you registered.
3. Select **New scan**
4. Choose either the Azure integration runtime if your source is publicly accessible, a [managed virtual network integration runtime](data-governance-private-endpoints-managed-virtual-network) if using a managed virtual network, or a self-hosted integration runtime if your source is in a private virtual network. For more information about which integration runtime to use, see the [choose the right integration runtime configuration article.](data-map-integration-runtime-choose#choose-the-right-integration-runtime)
5. Select the credential to connect to your data source.

    ![Set up scan](media/register-scan-azure-postgresql/03-azure-postgres-scan.png)
6. You can scope your scan to specific folders or subfolders by choosing the appropriate items in the list.

    ![Scope your scan](media/register-scan-azure-postgresql/04-scope-scan.png)
7. Then select a scan rule set. You can choose between the system default, existing custom rule sets, or create a new rule set inline.

    ![Scan rule set](media/register-scan-azure-postgresql/05-scan-rule-set.png)
8. Choose your scan trigger. You can set up a schedule or run the scan once.

    ![trigger scan](media/register-scan-azure-postgresql/06-trigger-scan.png)
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