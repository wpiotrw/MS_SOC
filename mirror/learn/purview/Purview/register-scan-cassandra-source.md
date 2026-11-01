---
layout: Conceptual
title: Connect to and manage Cassandra | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-cassandra-source
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to Cassandra in Microsoft Purview, and use Microsoft Purview's features to scan and manage your Cassandra source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2024-06-19T00:00:00.0000000Z
ms.custom: template-how-to, ignite-fall-2021
locale: en-us
document_id: 54470ac3-8456-9ac6-7a5b-52e8d699a452
document_version_independent_id: 54470ac3-8456-9ac6-7a5b-52e8d699a452
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-cassandra-source.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-cassandra-source
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-cassandra-source.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c92c5bc4-094e-8d84-3de1-531bd72cc060
---

# Connect to and manage Cassandra | Microsoft Learn

This article outlines how to register Cassandra, and how to authenticate and interact with Cassandra in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported Cassandra server versions are 3.*x* or 4.*x*.

When scanning Cassandra source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Cluster
    - Keyspaces
    - Tables including the columns and indexes
    - Materialized views including the columns
- Fetching static lineage on assets relationships among tables and materialized views.

When setting up scan, you can choose to scan an entire Cassandra instance, or scope the scan to a subset of keyspaces matching the given name(s) or name pattern(s).

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).

Note

**If your data store is not publicly accessible** (if your data store limits access from on-premises network, private network or specific IPs, etc.), **you will need to configure a self hosted integration runtime to connect to it**.

- If your data source isn't publicly accessible, set up the latest self-hosted integration runtime.
    - [Choose the right integration runtime for your scenario](data-map-integration-runtime-choose):
        - **To use a self-hosted integration runtime:**
            - [Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
            - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
            - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
        - **To use a kubernetes supported self-hosted integration runtime:**
            - [Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).

## Register

This section describes how to register Cassandra in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Steps to register

To register a new Cassandra server in Microsoft Purview Unified Catalog:

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left pane.
3. Select **Register**.
4. On the **Register sources** screen, select **Cassandra**, and then select **Continue**:

    ![Screenshot that shows the Register sources screen.](media/register-scan-cassandra-source/register-sources.png)
5. On the **Register sources (Cassandra)** screen:

    1. Enter a **Name**. The data source will use this name in the catalog.
    2. In the **Host** box, enter the server address where the Cassandra server is running. For example, 20.190.193.10.
    3. In the **Port** box, enter the port used by the Cassandra server.
    4. Select a collection from the list. ![Screenshot that shows the Register sources (Cassandra) screen.](media/register-scan-cassandra-source/configure-sources.png)
    5. Select **Register**.

## Scan

Follow the steps below to scan Cassandra to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion)

### Create and run scan

To create and run a new scan:

1. If your server is publicly accessible, skip to step two. Otherwise, you'll need to make sure your self-hosted integration runtime is configured:

    1. In the [Microsoft Purview governance portal](https://web.purview.azure.com/), got to the Management Center, and select **Integration runtimes**.
    2. Make sure a self-hosted integration runtime is available. If one isn't set up, use the steps mentioned in prerequisites to set up a self-hosted integration runtime.
2. In the [Microsoft Purview governance portal](https://web.purview.azure.com/), navigate to **Sources**.
3. Select the registered Cassandra server.
4. Select **New scan**.
5. Provide the following details.

    1. **Name**: Specify a name for the scan.
    2. **Connect via integration runtime**: Select the Azure auto-resolved integration runtime if your server is publicly accessible, or your configured self-hosted integration runtime if it isn't publicly available.
    3. **Credential**: When you configure the Cassandra credentials, be sure to:

        - Select **Basic Authentication** as the authentication method.
        - In the **User name** box, provide the name of the user you're making the connection for.
        - In the key vault's secret, save the password of the Cassandra user you're making the connection for.

        For more information, see [Credentials for source authentication in Microsoft Purview](data-map-data-scan-credentials).
    4. **Keyspaces**: Specify a list of Cassandra keyspaces to import. Multiple keyspaces must be separated with semicolons. For example, `keyspace1;keyspace2`. When the list is empty, all available keyspaces are imported.
    5. **Use Secure Sockets Layer(SSL)**: Select **True** or **False** to specify whether to use Secure Sockets Layer (SSL) when connecting to the Cassandra server. By default, this option is set to **False**.
    6. **Maximum memory available** (applicable when using self-hosted integration runtime): Specify the maximum memory (in GB) available on your VM to be used for scanning processes. This value depends on the size of Cassandra server to be scanned. ![scan Cassandra source](media/register-scan-cassandra-source/scan.png)
6. Select **Test connection** to validate the settings.
7. Select **Continue**.
8. Select a **scan trigger**. You can set up a schedule or run the scan once.
9. Review your scan, and then select **Save and Run**.

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

## Lineage

After scanning your Cassandra source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported Cassandra lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

![Cassandra lineage view](media/register-scan-cassandra-source/lineage.png)