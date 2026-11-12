---
layout: Conceptual
title: Connect to and manage Azure Database for MySQL | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-mysql-database
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to Azure Database for MySQL in Microsoft Purview, and use Microsoft Purview's features to scan and manage your Azure Database for MySQL source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: shjia
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-how-to, ignite-fall-2021, fasttrack-edit, msecd-doc-authoring-1030
locale: en-us
document_id: d315acda-ad26-665f-d6de-c39e58b2ed8c
document_version_independent_id: d315acda-ad26-665f-d6de-c39e58b2ed8c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-mysql-database.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-mysql-database
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-mysql-database.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/4c3c562b-e580-487f-8ab7-ed723105d8cf
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/c5148132-a95f-467e-b31c-8786a8264397
platformId: 2991c127-341a-96c8-4958-55d1b3cc32fc
---

# Connect to and manage Azure Database for MySQL | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register a database in Azure Database for MySQL, and how to authenticate and interact with Azure Database for MySQL in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes* | Yes |

\* Microsoft Purview relies on UPDATE\_TIME metadata from Azure Database for MySQL for incremental scans. In some cases, this field might not persist in the database and a full scan is performed. For more information, see [The INFORMATION_SCHEMA TABLES Table](https://dev.mysql.com/doc/refman/5.7/en/information-schema-tables-table.html) for MySQL.

Important

Microsoft Purview only supports single server deployment option for Azure Database for MySQL.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You'll need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

## Register

This section describes how to register an Azure Database for MySQL in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Authentication for registration

You'll need **username** and **password** for the next steps.

Follow the instructions in [CREATE DATABASES AND USERS](/en-us/azure/mysql/howto-create-users) to create a login for your Azure Database for MySQL.

1. Navigate to your key vault in the Azure portal
2. Select **Settings &gt; Secrets**
3. Select **+ Generate/Import** and enter the **Name** and **Value** as the *password* from your Azure SQL Database
4. Select **Create** to complete
5. If your key vault isn't connected to Microsoft Purview yet, you'll need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
6. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) of type SQL authentication using the **username** and **password** to set up your scan.

### Steps to register

To register a new Azure Database for MySQL in Microsoft Purview Unified Catalog, do the following:

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left navigation.
3. Select **Register**.
4. On **Register sources**, select **Azure Database for MySQL**. Select **Continue**.

![register new data source](media/register-scan-azure-mysql/01-register-azure-mysql-data-source.png)

On the **Register sources (Azure Database for MySQL)** screen, do the following:

1. Enter a **Name** for your data source. This will be the display name for this data source in your Catalog.
2. Select **From Azure subscription**, select the appropriate subscription from the **Azure subscription** drop-down box and the appropriate server from the **Server name** drop-down box.
3. Select **Register** to register the data source.

![register sources options](media/register-scan-azure-mysql/02-register-azure-mysql-name-connection.png)

## Scan

Follow the steps below to scan Azure Database for MySQL to automatically identify assets and classify your data. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion)

### Create and run scan

To create and run a new scan, do the following:

1. Select the **Data Map** tab on the left pane in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select the Azure Database for MySQL source that you registered.
3. Select **New scan**
4. Choose either the Azure integration runtime if your source is publicly accessible, a [managed virtual network integration runtime](data-governance-private-endpoints-managed-virtual-network) if using a managed virtual network, or a self-hosted integration runtime if your source is in a private virtual network. For more information about which integration runtime to use, see the [choose the right integration runtime configuration article.](data-map-integration-runtime-choose#choose-the-right-integration-runtime)
5. Select the credential to connect to your data source and check your connection to make sure your credential is properly configured.

    ![Set up scan](media/register-scan-azure-mysql/03-new-scan-azure-mysql-connection-credential.png)
6. You can scope your scan to specific folders or subfolders by choosing the appropriate items in the list.

    ![Scope your scan](media/register-scan-azure-mysql/04-scope-azure-mysql-scan.png)
7. Then select a scan rule set. You can choose between the system default, existing custom rule sets, or create a new rule set inline.

    ![Scan rule set](media/register-scan-azure-mysql/05-scan-rule-set.png)
8. Choose your scan trigger. You can set up a schedule or run the scan once.

    ![trigger](media/register-scan-azure-mysql/06-trigger-scan.png)
9. Review your scan and select **Save and run**.--&gt;

![review your scan](media/register-scan-azure-mysql/07-review-your-scan.png)

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