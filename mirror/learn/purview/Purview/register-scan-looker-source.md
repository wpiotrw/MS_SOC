---
layout: Conceptual
title: Connect to and manage Looker | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-looker-source
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to  Looker  in Microsoft Purview, and use Microsoft Purview's features to scan and manage your Looker source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2023-08-22T00:00:00.0000000Z
ms.custom: template-how-to, ignite-fall-2021
locale: en-us
document_id: 962337e3-5c90-f767-75cd-a1f8fcedea3b
document_version_independent_id: 962337e3-5c90-f767-75cd-a1f8fcedea3b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-looker-source.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-looker-source
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-looker-source.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f51462b7-d679-e48a-df7b-f63b6e77beee
---

# Connect to and manage Looker | Microsoft Learn

This article outlines how to register Looker, and how to authenticate and interact with Looker in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported Looker server version is 7.2.

When scanning Looker source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Server
    - Folders
    - Projects
    - Models
    - Dashboards
    - Looks
    - Explore diagrams including the joins
    - Views including the dimensions, measures, parameters, and filters
    - Layouts including the chart layouts, table layouts, text, and fields
- Fetching static lineage on assets relationships among views and layouts.

When setting up scan, you can choose to scan an entire Looker server, or scope the scan to a subset of Looker projects matching the given name(s).

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

This section describes how to register Looker in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Authentication for registration

An API3 key is required to connect to the Looker server. The API3 key consists in a public client\_id and a private client\_secret and follows an OAuth2 authentication pattern.

### Steps to register

To register a new Looker server in Microsoft Purview Unified Catalog, follow these steps:

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left navigation.
3. Select **Register.**
4. On Register sources, select **Looker**. Select **Continue.**

![register looker source](media/register-scan-looker-source/register-sources.png)

On the Register sources (Looker) screen, follow these steps:

1. Enter a **Name** that the data source will be listed within the Catalog.
2. Enter the Looker API URL in the **Server API URL** field. The default port for API requests is port 19999. Also, all Looker API endpoints require an HTTPS connection. For example: 'https://azurepurview.cloud.looker.com'
3. Select a collection from the list.
4. Finish to register the data source.

    ![scan looker source](media/register-scan-looker-source/scan-source.png)

## Scan

Follow the steps below to scan Looker to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion)

### Create and run scan

To create and run a new scan, follow these steps:

1. If your server is publicly accessible, skip to step two. Otherwise, you'll need to make sure your self-hosted integration runtime is configured:

    1. In the [Microsoft Purview governance portal](https://web.purview.azure.com/), got to the Management Center, and select **Integration runtimes**.
    2. Make sure a self-hosted integration runtime is available. If one isn't set up, use the steps mentioned in prerequisites to set up a self-hosted integration runtime.
2. In the [Microsoft Purview governance portal](https://web.purview.azure.com/), navigate to **Sources**.
3. Select the registered **Looker** server.
4. Select **+ New scan**.
5. Provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the Azure auto-resolved integration runtime if your server is publicly accessible, or your configured self-hosted integration runtime if it isn't publicly available.
    3. **Server API URL** is auto populated based on the value entered during registration.
    4. **Credential:** While configuring Looker credential, make sure to:

        - Select **Basic Authentication** as the Authentication method
        - Provide your Looker API3 key's client ID in the User name field
        - Save your Looker API3 key's client secret in the key vault's secret.

        To access client ID and client secret, navigate to Looker -&gt;Admin -&gt; Users -&gt; Select **Edit** on a user -&gt; Select **EditKeys** -&gt; Use the Client ID and Client Secret or create a new one.

        ![get looker details](media/register-scan-looker-source/looker-details.png)

        To understand more on credentials, refer to the link [here](data-map-data-scan-credentials)
    5. **Model filter** - Scope your scan by providing a semicolon separated list of Looker models. This option is used to select looks and dashboards by their parent model.
    6. **Maximum memory available** (applicable when using self-hosted integration runtime): Maximum memory (in GB) available on customer's VM to be used by scanning processes. This is dependent on the size of erwin Mart to be scanned.

        ![trigger scan](media/register-scan-looker-source/setup-scan.png)
6. Select **Test connection** to validate the settings.
7. Select **Continue**.
8. Choose your **scan trigger**. You can set up a schedule or ran the scan once.
9. Review your scan and select on **Save and Run**.

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

After scanning your Looker source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported Looker lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

![Looker lineage view](media/register-scan-looker-source/lineage.png)