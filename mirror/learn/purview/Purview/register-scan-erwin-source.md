---
layout: Conceptual
title: Connect to and manage erwin Mart servers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-erwin-source
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to erwin Mart servers in Microsoft Purview, and use Microsoft Purview's features to scan and manage your erwin Mart server source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2023-04-20T00:00:00.0000000Z
ms.custom:
- template-how-to
- ignite-fall-2021
- sfi-image-nochange
locale: en-us
document_id: 4745a9d5-9d38-8302-ef1b-c1bab547aca2
document_version_independent_id: 4745a9d5-9d38-8302-ef1b-c1bab547aca2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-erwin-source.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-erwin-source
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-erwin-source.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 3489330a-7344-a6d3-3db8-b840c04e3a9a
---

# Connect to and manage erwin Mart servers | Microsoft Learn

This article outlines how to register erwin Mart servers, and how to authenticate and interact with erwin Mart Servers in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported erwin Mart versions are 9.x to 2021.

When scanning erwin Mart source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Mart
    - Libraries
    - Models
    - Entities including the attributes, foreign keys, indexes, index members, candidate keys, and triggers
    - Default values
    - Synonyms
    - Sequences
    - Domains
    - Subject areas
    - Relationships
    - Validation rules including the valid values
    - ER diagrams
    - Views including the attributes
    - Stored procedures including the parameters
    - Schemas
    - Subtype relationships
    - View relationship
    - User defined properties
- Fetching static lineage on assets relationships among entities, views and stored procedures.

When setting up scan, you can choose to scan an entire erwin Mart server, or scope the scan to a list of models matching the given name(s).

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- Set up the latest [self-hosted integration runtime](https://go.microsoft.com/fwlink/?linkid=2246619). For more information, see [the create and configure a self-hosted integration runtime guide](data-map-integration-runtime-self-hosted).

    Important

    Make sure to install the self-hosted integration runtime and the Erwin Data Modeler software on the same machine where erwin Mart instance is running.

    - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
    - Ensure Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the self-hosted integration runtime machine. If you don't have this update installed, [you can download it here](/en-us/cpp/windows/latest-supported-vc-redist).

## Register

This section describes how to register erwin Mart servers in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

The only supported authentication for an erwin Mart source is **Server Authentication** in the form of username and password.

### Steps to register

1. Navigate to your Microsoft Purview account in the [Microsoft Purview governance portal](https://web.purview.azure.com/).
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On Register sources, select **erwin**. Select **Continue.**![register erwin source](media/register-scan-erwin-source/register-sources.png)

On the Register sources (erwin) screen, do the following:

1. Enter a **Name** that the data source will be listed within the Catalog.
2. Enter the erwin Mart **Server name.** This is the network host name used to connect to the erwin Mart server. For example, localhost
3. Enter the **Port** number used when connecting to erwin Mart. By default, this value is 18170.
4. Enter the **Application name**

    Note

    The above details can be found by navigating to your erwin Data Modeler. Select Mart -&gt; Connect to see details related to server name, port and application name.

    ![find erwin details](media/register-scan-erwin-source/erwin-details.png)
5. Select a collection from the list.
6. Finish to register the data source.

    ![register source](media/register-scan-erwin-source/register-erwin.png)

## Scan

Follow the steps below to scan erwin Mart servers to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion)

### Create and run scan

To create and run a new scan, do the following:

1. In the Management Center, select Integration runtimes. Make sure a self-hosted integration runtime is set up on the VM where erwin Mart instance is running. If it isn't set up, use the steps mentioned [here](data-map-integration-runtime-self-hosted) to set up a self-hosted integration runtime.
2. Navigate to **Sources**.
3. Select the registered **erwin** Mart.
4. Select **+ New scan**.
5. Provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the configured self-hosted integration runtime.
    3. **Server name, Port** and **Application name** are auto populated based on the values entered during registration.
    4. **Credential:** Select the credential configured to connect to your erwin Mart server. While creating a credential, make sure to:

        - Select **Basic Authentication** as the Authentication method
        - Provide your erwin Mart server's username in the User name field.
        - Save your user password for server authentication in the key vault's secret.

        To understand more on credentials, refer to the link [here](data-map-data-scan-credentials).
    5. **Use Internet Information Services (IIS)** - Select True or False to notify if Microsoft Internet Information Services (IIS) must be used when connecting to the erwin Mart server. By default this value is set to False.
    6. **Use Secure Sockets Layer (SSL)** - Select True or False to Notify if Secure Sockets Layer (SSL) must be used when connecting to the erwin Mart server. By default, this value is set to False.

        Note

        This parameter is only applicable for erwin Mart version 9.1 or later.
    7. **Models** - Scope your scan by providing a semicolon separated list of erwin model locator strings. For example, mart://Mart/Samples/eMovies;mart://Mart/Erwin\_Tutorial/AP\_Physical
    8. **Maximum memory available**: Maximum memory (in GB) available on customer's VM to be used by scanning processes. This is dependent on the size of erwin Mart to be scanned.

    ![trigger scan](media/register-scan-erwin-source/setup-scan.png)
6. Select **Test connection.**
7. Select **Continue**.
8. Choose your **scan trigger**. You can set up a schedule or ran the scan once.
9. Review your scan and select **Save and Run**.

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

After scanning your erwin source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported erwin lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

![erwin lineage view](media/register-scan-erwin-source/lineage.png)