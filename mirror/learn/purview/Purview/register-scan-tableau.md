---
layout: Conceptual
title: Connect to and manage Tableau | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-tableau
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to use Microsoft Purview to scan and manage your Tableau Server.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2023-11-17T00:00:00.0000000Z
ms.custom: template-how-to
locale: en-us
document_id: aa42dde8-dd59-909f-9243-e2f6ea0c3771
document_version_independent_id: aa42dde8-dd59-909f-9243-e2f6ea0c3771
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-tableau.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-tableau
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-tableau.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 14dd0c74-8f8a-149a-a30e-12a7e1048dcd
---

# Connect to and manage Tableau | Microsoft Learn

This article outlines how to register Tableau, and how to authenticate and interact with Tableau in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported Tableau Server version is 8.x to 2023.x.

When scanning Tableau, Microsoft Purview supports extracting technical metadata including:

- Server
- Projects
- Workbooks
- Dashboards
- Data sources
- Stories
- Worksheets and the fields/axes
- Workbook data sources
- Tables and the columns

When setting up scan, you can choose to scan an entire Tableau server, or if you have multiple sites installed, to scope the scan to a given site.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

- Currently, scan isn't supported if your Tableau server doesn’t allow access from public network.
- When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- You must have an Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- You must have an active [Microsoft Purview account](create-microsoft-purview-portal).
- You need an Azure Key Vault, and to [grant Microsoft Purview permissions to access secrets](data-map-data-scan-credentials#grant-microsoft-purview-access-to-your-azure-key-vault).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose). If your data source isn't publicly accessible, set up the latest [kubernetes supported self-hosted integration runtime](data-map-integration-runtime-kubernetes).

### Required permissions for scan

Microsoft Purview supports basic authentication (username and password) for scanning Tableau server.

The user account must be licensed as "Interactor" (renamed to "Explorer" in the latest versions) on the Tableau server, and must have 'View' and 'Download' rights for all of the Workbooks, Data Sources and Projects that are about to import. It is preferable to use an account that has "Site Administrator" security role.

## Register

This section describes how to register a Tableau server in Microsoft Purview by using [the Microsoft Purview governance portal](https://web.purview.azure.com/).

1. Go to your Microsoft Purview account.
2. Select **Data Map** on the left pane.
3. Select **Register**.
4. In **Register sources**, select **Tableau** &gt; **Continue**.
5. On the **Register sources (Tableau)** screen, do the following:

    1. For **Name**, enter a name that Microsoft Purview will list as the data source.
    2. For **Host**, enter the URL of your Tableau server. If SSL is used, the URL must start by https and possibly end with a custom port if the SSL default port of 443 is not used.
    3. Select a collection from the list.

    ![Screenshot of registering a Tableau server source.](media/register-scan-tableau/register-sources.png)
6. Select **Register**.

## Scan

Tip

To troubleshoot any issues with scanning:

1. Confirm you have followed all **prerequisites**.
2. Review our [**scan troubleshooting documentation**](troubleshoot-connections).

Use the following steps to scan Tableau server to automatically identify assets. For more information about scanning in general, see [Scans and ingestion in Microsoft Purview](data-map-scan-ingestion).

1. Go to **Sources**.
2. Select the registered Tableau source.
3. Select **+ New scan**.
4. Provide the following details:

    1. **Name**: Enter a name for the scan.
    2. **Connect via integration runtime**: Choose the default Azure integration runtime, Managed VNet IR, or a Kubernetes supported self-hosted integration runtime you created.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select **Basic Authentication** while creating a credential.
        - Provide the user name used to connect to Tableau server in the User name input field.
        - Store the user password used to connect to Tableau server in the secret key.

        For more information, see [Credentials for source authentication in Microsoft Purview](data-map-data-scan-credentials).
    4. **Site**: Site is only required when connecting to an online Tableau server with multiple sites installed. The value is case sensitive, and must not contain any space as it is used in the URL to connect to Tableau.
5. Click **Test connection** to validate the settings.

    ![Screenshot of setting up a Tableau server scan.](media/register-scan-tableau/scan.png)
6. Select **Continue**.
7. For **Scan trigger**, choose whether to set up a schedule or run the scan once.
8. Review your scan and select **Save and Run**.

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

## Browse, search, and view assets

After successfully scanning your Tableau server, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.