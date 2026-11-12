---
layout: Conceptual
title: Connect to and manage PostgreSQL | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-postgresql
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to PostgreSQL in Microsoft Purview, and use Microsoft Purview's features to scan and manage your PostgreSQL source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.service: purview
ms.subservice: purview-data-map
ms.topic: concept-article
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-how-to, msecd-doc-authoring-1030
locale: en-us
document_id: d7ed1630-07da-8ea7-8d2f-a23a6176af21
document_version_independent_id: d7ed1630-07da-8ea7-8d2f-a23a6176af21
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-postgresql.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-postgresql
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-postgresql.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/982661b3-cc41-45b1-b21d-18b4b6937344
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/bbee35d0-ba85-4062-b9c2-388c328eb4fa
platformId: 005b781d-051c-0be9-3ecc-ace72a7c290a
---

# Connect to and manage PostgreSQL | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register PostgreSQL, and how to authenticate and interact with PostgreSQL in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported PostgreSQL server versions are 8.x to 16.x.

When scanning PostgreSQL source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Server
    - Databases
    - Schemas
    - Tables including the columns
    - Views including the columns
- Fetching static lineage on assets relationships among tables and views.

When setting up scan, you can choose to scan an entire PostgreSQL database, or scope the scan to a subset of schemas matching the given name(s) or name pattern(s).

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

### Required permissions for scan

- The PostgreSQL user needs read access to system tables in order to access advanced metadata.
- The user must be granted CONNECT permission on the default postgres database (Command: GRANT CONNECT ON DATABASE postgres TO [user];).

## Register

This section describes how to register PostgreSQL in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Steps to register

To register a new PostgreSQL source in Microsoft Purview Unified Catalog, follow these steps:

1. Navigate to your Microsoft Purview account in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On Register sources, select **PostgreSQL**. Select **Continue**.

On the **Register sources (PostgreSQL)** screen, follow these steps:

1. Enter a **Name** that the data source will be listed within the Catalog.
2. Enter the **Server** name to connect to a PostgreSQL source. This can either be:

    - A host name used to connect to the database server. For example: `MyDatabaseServer.com`
    - An IP address. For example: `192.169.1.2`
3. Enter the **Port** used to connect to the database server (5432 by default for PostgreSQL).
4. Select a collection from the list.
5. Finish to register the data source.

    ![register sources options](media/register-scan-postgresql/register-sources.png)

## Scan

Follow the steps below to scan PostgreSQL to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Authentication for a scan

The supported authentication type for a PostgreSQL source is **Basic authentication**.

### Create and run scan

To create and run a new scan, follow these steps:

1. If your server is publicly accessible, skip to step two. Otherwise, you'll need to make sure your self-hosted integration runtime is configured:

    1. In the [Microsoft Purview governance portal](https://web.purview.azure.com/), got to the Management Center, and select **Integration runtimes**.
    2. Make sure a self-hosted integration runtime is available. If one isn't set up, use the steps mentioned in prerequisites to set up a self-hosted integration runtime.
2. In the [Microsoft Purview governance portal](https://web.purview.azure.com/), navigate to **Sources**.
3. Select the registered PostgreSQL source.
4. Select **+ New scan**.
5. Provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the Azure auto-resolved integration runtime if your server is publicly accessible, or your configured self-hosted integration runtime if it isn't publicly available.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select **Basic Authentication** while creating a credential.
        - Provide the user name used to connect to the database server in the User name input field.
        - Store the user password used to connect to the database server in the secret key.
    4. **Database**： Specify the name of the database instance to import.
    5. **Schema**: List subset of schemas to import expressed as a semicolon separated list. For example, `schema1;schema2`. All user schemas are imported if that list is empty. All system schemas (for example, SysAdmin) and objects are ignored by default.

        Acceptable schema name patterns can be static names or contain wildcard %. For example: `A%;%B;%C%;D`

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

        Usage of NOT and special characters aren't acceptable.
    6. **Maximum memory available** (applicable when using self-hosted integration runtime): Maximum memory (in GB) available on customer's VM to be used by scanning processes. This is dependent on the size of PostgreSQL source to be scanned.

        Note

        As a rule of thumb, please provide 1GB memory for every 1000 tables

        ![scan PostgreSQL](media/register-scan-postgresql/scan.png)
6. Select **Test connection** to validate the settings (available when using Azure Integration Runtime).
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

After scanning your PostgreSQL source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported PostgreSQL lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

![PostgreSQL lineage view](media/register-scan-postgresql/lineage.png)