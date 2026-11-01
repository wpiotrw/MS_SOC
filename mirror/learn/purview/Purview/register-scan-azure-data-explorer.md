---
layout: Conceptual
title: Connect to and manage Azure Data Explorer in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-data-explorer
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
description: Learn how to connect to Azure Data Explorer in Microsoft Purview, and use Microsoft Purview features to scan and manage your Azure Data Explorer source.
locale: en-us
document_id: afee38b2-471a-2a30-7659-b804679e8244
document_version_independent_id: afee38b2-471a-2a30-7659-b804679e8244
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-data-explorer.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-data-explorer
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-data-explorer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: bc28a479-e407-1487-7d7d-d80a83042f98
---

# Connect to and manage Azure Data Explorer in Microsoft Purview | Microsoft Learn

This article outlines how to register Azure Data Explorer, and how to authenticate and interact with Azure Data Explorer in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You will need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

## Register

This section describes how to register Azure Data Explorer in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Authentication for registration

There are several methods available for authentication for Azure Data Explorer:

- Service Principal
- System-assigned managed identity (SAMI)
- User-assigned managed identity (UAMI)

#### Service Principal to register

To use service principal authentication for scans, you can use an existing one or create a new one.

Note

If you have to create a new Service Principal, please follow these steps:

1. Navigate to the [Azure portal](https://portal.azure.com).
2. Select **Microsoft Entra ID** from the left-hand side menu.
3. Select **App registrations**.
4. Select **+ New application registration**.
5. Enter a name for the **application** (the service principal name).
6. Select **Accounts in this organizational directory only**.
7. For Redirect URI select **Web** and enter any URL you want; it doesn't have to be real or work.
8. Then select **Register**.

It is required to get the Service Principal's application ID and secret:

1. Navigate to your Service Principal in the [Azure portal](https://portal.azure.com)
2. Copy the values the **Application (client) ID** from **Overview** and **Client secret** from **Certificates & secrets**.
3. Navigate to your key vault
4. Select **Settings &gt; Secrets**
5. Select **+ Generate/Import** and enter the **Name** of your choice and **Value** as the **Client secret** from your Service Principal
6. Select **Create** to complete
7. If your key vault is not connected to Microsoft Purview yet, you will need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
8. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) using the Service Principal to set up your scan

#### Granting the Service Principal access to your Azure data explorer instance

1. Navigate to the Azure portal. Then navigate to your Azure data explorer instance.
2. Add the service principal to the **AllDatabasesViewer** role in the **Permissions** tab.

### System or user assigned managed identity to register

- **System-assigned managed identity** - As soon as the Microsoft Purview Account is created, a system-assigned managed identity (SAMI) is created automatically in Microsoft Entra tenant. It has the same name as your Microsoft Purview account.
- **User-assigned managed identity** (preview) - Similar to a system-managed identity, a user-assigned managed identity (UAMI) is a credential resource that can be used to allow Microsoft Purview to authenticate against Microsoft Entra ID. For more information, you can see our [User-assigned managed identity guide](data-map-data-scan-credentials#create-a-user-assigned-managed-identity).

To register using either of these managed identities, follow these steps:

1. If you would like to use a user-assigned managed identity and have not created one, follow the steps to create the identity in the [User-assigned managed identity guide](data-map-data-scan-credentials#create-a-user-assigned-managed-identity).
2. Navigate to the [Azure portal](https://portal.azure.com). Then navigate to your Azure data explorer instance.
3. Select the **Permissions** tab on the left pane.
4. Add the SAMI or UAMI to the **AllDatabasesViewer** role in the **Permissions** tab.

### Steps to register

To register a new Azure Data Explorer (Kusto) account in Microsoft Purview Unified Catalog, follow these steps:

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On **Register sources**, select **Azure Data Explorer**
5. Select **Continue**

![register new data source](media/register-scan-azure-data-explorer/register-new-data-source.png)

On the **Register sources (Azure Data Explorer (Kusto))** screen, do the following:

1. Enter a **Name** that the data source will be listed with in the Catalog.
2. Choose your Azure subscription to filter down Azure Data Explorer.
3. Select an appropriate cluster.
4. Select a collection from the list.
5. Select **Register** to register the data source.

![register sources options](media/register-scan-azure-data-explorer/register-sources.png)

## Scan

Follow the steps below to scan Azure Data Explorer to automatically identify assets and classify your data. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Create and run scan

To create and run a new scan, follow these steps:

1. Select the **Data Map** tab on the left pane in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select the Azure Data Explorer source that you registered.
3. Select **New scan**
4. Choose either the Azure integration runtime if your source is publicly accessible, a [managed virtual network integration runtime](data-governance-private-endpoints-managed-virtual-network) if using a managed virtual network, or a self-hosted integration runtime if your source is in a private virtual network. For more information about which integration runtime to use, see the [choose the right integration runtime configuration article.](data-map-integration-runtime-choose#choose-the-right-integration-runtime)
5. Select the credential to connect to your data source.

    ![Set up scan](media/register-scan-azure-data-explorer/set-up-scan-data-explorer.png)
6. You can scope your scan to specific databases by choosing the appropriate items in the list.

    ![Scope your scan](media/register-scan-azure-data-explorer/scope-your-scan-data-explorer.png)
7. Then select a scan rule set. You can choose between the system default, existing custom rule sets, or create a new rule set inline.

    ![Scan rule set](media/register-scan-azure-data-explorer/scan-rule-set-data-explorer.png)
8. Choose your scan trigger. You can set up a schedule or run the scan once.

    ![trigger](media/register-scan-azure-data-explorer/trigger-scan.png)
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