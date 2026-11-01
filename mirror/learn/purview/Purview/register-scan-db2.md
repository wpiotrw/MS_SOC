---
layout: Conceptual
title: Connect to and manage Db2 in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-db2
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
description: Learn how to connect to Db2 in Microsoft Purview, and use Microsoft Purview features to scan and manage your Db2 source.
locale: en-us
document_id: 971e2f97-a427-70b6-01d5-40347b343d8b
document_version_independent_id: 971e2f97-a427-70b6-01d5-40347b343d8b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-db2.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-db2
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-db2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 464b0eb6-1286-1578-ae12-f8b7b3ec1d50
---

# Connect to and manage Db2 in Microsoft Purview | Microsoft Learn

This article outlines how to register Db2, and how to authenticate and interact with Db2 in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported IBM Db2 versions are Db2 for LUW 9.7 to 11.x. Db2 for z/OS (mainframe) and iSeries (AS/400) aren't supported.

When you scan an IBM Db2 source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Server
    - Databases
    - Schemas
    - Tables including the columns, foreign keys, indexes, and constraints
    - Views including the columns
    - Triggers
- Fetching static lineage on assets relationships among tables and views.

You can scan an entire Db2 database, or scope the scan to a subset matching the given names or name patterns.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

When object is deleted from the data source, currently the subsequent scan won't remove the corresponding asset in Microsoft Purview.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose):

    - **To use a self-hosted integration runtime:**
        - [Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
        - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
        - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
        - Download the [Db2 JDBC driver](https://www.ibm.com/support/pages/db2-jdbc-driver-versions-and-downloads) on the machine where your self-hosted integration runtime is running. Note down the folder path so you can use it to set up the scan.
    - **To use a kubernetes supported self-hosted integration runtime:**
        - [Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).
        - Download the [Db2 JDBC driver](https://www.ibm.com/support/pages/db2-jdbc-driver-versions-and-downloads) on the machine where your self-hosted integration runtime is running. Note down the folder path so you can use it to set up the scan.

    Note

    The driver should be accessible by the self-hosted integration runtime. By default, self-hosted integration runtime uses [local service account "NT SERVICE\DIAHostService"](data-map-integration-runtime-self-hosted#service-account-for-self-hosted-integration-runtime). Make sure it has "Read and execute" and "List folder contents" permission to the driver folder.
- The Db2 user must have the CONNECT permission. Microsoft Purview connects to the syscat tables in IBM Db2 environment when importing metadata.

## Register

This section describes how to register Db2 in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Steps to register

To register a new Db2 source in Microsoft Purview Unified Catalog, do the following steps:

1. Navigate to your Microsoft Purview account in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On Register sources, select **Db2**. Select **Continue**.

On the **Register sources (Db2)** screen, do the following steps:

1. Enter a **Name** that the data source is within the Catalog.
2. Enter the **Server** name to connect to a Db2 source. This name can either be:

    - A host name used to connect to the database server. For example: `MyDatabaseServer.com`
    - An IP address. For example: `192.169.1.2`
3. Enter the **Port** used to connect to the database server (446 by default for Db2).
4. Select a collection from the list.
5. Finish to register the data source.

    ![register sources options](media/register-scan-db2/register-sources.png)

## Scan

Follow the steps to scan Db2 to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Authentication for a scan

The supported authentication type for a Db2 source is **Basic authentication**.

### Create and run scan

To create and run a new scan, follow these steps:

1. In the Management Center, select Integration runtimes. Make sure a self-hosted integration runtime is set up. If it isn't set up, use the steps mentioned in prerequisites to create a self-hosted integration runtime.
2. Navigate to **Sources**.
3. Select the registered Db2 source.
4. Select **+ New scan**.
5. Provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the configured self-hosted integration runtime
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select **Basic Authentication** while creating a credential.
        - Provide the user name used to connect to the database server in the User name input field.
        - Store the user password used to connect to the database server in the secret key.
    4. **Database**: The name of the database instance to import.
    5. **Schema**: List subset of schemas to import expressed as a semicolon separated list. For example, `schema1;schema2`. All user schemas are imported if that list is empty. All system schemas (for example, SysAdmin) and objects are ignored by default.

        Acceptable schema name patterns can be static names or contain wildcard %. For example: `A%;%B;%C%;D`

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

        Usage of NOT and special characters aren't acceptable.
    6. **Driver location**: Specify the path to the JDBC driver location in your machine where self-host integration runtime is running. For example, `D:\Drivers\Db2`.

        1. For Kubernetes-supported self-hosted integration runtime: `./drivers/Db2`. It's the path to valid JAR folder location. The value must be a valid relative file path. Please refer to the documentation to [set up a scan with external drivers](data-map-integration-runtime-kubernetes#set-up-a-scan-with-external-drivers) for uploading drivers in advance.
    7. **Maximum memory available**: Maximum memory (in GB) available on customer's VM to be used by scanning processes. The memory needed is dependent on the size of Db2 source to be scanned.

        Note

        As a thumb rule, please provide 1GB memory for every 1000 tables

        ![scan Db2](media/register-scan-db2/scan.png)
6. Select **Continue**.
7. Choose your **scan trigger**. You can set up a schedule or ran the scan once.
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

## Lineage

After scanning your Db2 source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported Db2 lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).