---
layout: Conceptual
title: Connect to and manage Teradata | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-teradata-source
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to Teradata in Microsoft Purview, and use Microsoft Purview's features to scan and manage your Teradata source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2023-04-20T00:00:00.0000000Z
ms.custom: template-how-to, ignite-fall-2021
locale: en-us
document_id: 6acb965c-21aa-4ab6-4f0d-d74835592614
document_version_independent_id: 6acb965c-21aa-4ab6-4f0d-d74835592614
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-teradata-source.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-teradata-source
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-teradata-source.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9f096ad3-0bc8-48a4-25e1-2ae68b811737
---

# Connect to and manage Teradata | Microsoft Learn

This article outlines how to register Teradata, and how to authenticate and interact with Teradata in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported Teradata database versions are 12.x to 17.x.

When scanning Teradata source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Server
    - Databases
    - Tables including the columns, foreign keys, indexes, and constraints
    - Views including the columns
    - Stored procedures including the parameter dataset and result set
    - Functions including the parameter dataset
- Fetching static lineage on assets relationships among tables and views.

When setting up scan, you can choose to scan an entire Teradata server, or scope the scan to a subset of databases matching the given name(s) or name pattern(s).

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

### Required permissions for scan

Microsoft Purview supports basic authentication (username and password) for scanning Teradata. The user should have SELECT permission granted for every individual system table listed below:

```sql
grant select on dbc.tvm to [user]; 
grant select on dbc.dbase to [user]; 
grant select on dbc.tvfields to [user]; 
grant select on dbc.udtinfo to [user]; 
grant select on dbc.idcol to [user]; 
grant select on dbc.udfinfo to [user];
```

To retrieve data types of view columns, Microsoft Purview issues a prepare statement for `select * from <view>` for each of the view queries and parse the metadata that contains the data type details for better performance. It requires the SELECT data permission on views. If the permission is missing, view column data types will be skipped.

For classification, user also needs to have read permission on the tables/views to retrieve sample data.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- Set up the latest [self-hosted integration runtime](https://go.microsoft.com/fwlink/?linkid=2246619). For more information, see [the create and configure a self-hosted integration runtime guide](data-map-integration-runtime-self-hosted).

    - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
    - Ensure Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the self-hosted integration runtime machine. If you don't have this update installed, [you can download it here](/en-us/cpp/windows/latest-supported-vc-redist).
    - Download the [Teradata JDBC driver](https://downloads.teradata.com/) on the machine where your self-hosted integration runtime is running. Note down the folder path which you will use to set up the scan.

        Note

        The driver should be accessible by the self-hosted integration runtime. By default, self-hosted integration runtime uses [local service account "NT SERVICE\DIAHostService"](data-map-integration-runtime-self-hosted#service-account-for-self-hosted-integration-runtime). Make sure it has "Read and execute" and "List folder contents" permission to the driver folder.

## Register

This section describes how to register Teradata in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Steps to register

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On Register sources, select **Teradata**. Select **Continue**

    ![register Teradata options](media/register-scan-teradata-source/register-sources.png)

On the **Register sources (Teradata)** screen, do the following:

1. Enter a **Name** that the data source will be listed with in the Catalog.
2. Enter the **Host** name to connect to a Teradata source. It can also be an IP address of the server.
3. Select a collection from the list.
4. Finish to register the data source.

    ![register Teradata](media/register-scan-teradata-source/register-sources-2.png)

## Scan

Follow the steps below to scan Teradata to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Create and run scan

1. In the Management Center, select **Integration runtimes**. Make sure a self-hosted integration runtime is set up. If it isn't set up, use the steps mentioned [here](data-map-integration-runtime-self-hosted) to set up a self-hosted integration runtime
2. Select the **Data Map** tab on the left pane in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
3. Select the registered Teradata source.
4. Select **New scan**
5. Provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the configured self-hosted integration runtime.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select Basic Authentication while creating a credential.
        - Provide a user name to connect to database server in the User name input field
        - Store the database server password in the secret key.

        To understand more on credentials, refer to the link [here](data-map-data-scan-credentials)
    4. **Schema**: List subset of databases to import expressed as a semicolon separated list. For Example: `schema1;schema2`. All user databases are imported if that list is empty. All system databases (for example, SysAdmin) and objects are ignored by default.

        Acceptable database name patterns can be static names or contain wildcard %. For example: `A%;%B;%C%;D`

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

        Usage of NOT and special characters aren't acceptable
    5. **Driver location**: Specify the path to the JDBC driver location in your machine where self-host integration runtime is running. For example: `D:\Drivers\Teradata`.

        1. For self-hosted integration runtime on a local machine: `D:\Drivers\Teradata`. It's the path to valid JAR folder location. The value must be a valid absolute file path and doesn't contain space. Make sure the driver is accessible by the self-hosted integration runtime;; learn more from prerequisites section.
    6. **Stored procedure details**: Controls the number of details imported from stored procedures:

        - Signature: The name and parameters of stored procedures.
        - Code, signature: The name, parameters and code of stored procedures.
        - Lineage, code, signature: The name, parameters and code of stored procedures, and the data lineage derived from the code.
        - None: Stored procedure details aren't included.
    7. **Maximum memory available:** Maximum memory (in GB) available on customer's VM to be used by scanning processes. This is dependent on the size of Teradata source to be scanned.

        Note

        As a rule of thumb, please provide 2GB memory for every 1000 tables

        ![setup scan](media/register-scan-teradata-source/setup-scan.png)
6. Select **Continue**.
7. Select a **scan rule set** for classification. You can choose between the system default, existing custom rule sets, or [create a new rule set](data-map-scan-rule-set) inline.
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

After scanning your Teradata source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported Teradata lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

![Teradata lineage view](media/register-scan-teradata-source/lineage.png)