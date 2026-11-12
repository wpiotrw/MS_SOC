---
layout: Conceptual
title: Connect to and manage Oracle in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-oracle-source
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to connect to Oracle in Microsoft Purview, and how to use Microsoft Purview features to scan and manage your Oracle source.
locale: en-us
document_id: 652134c5-0c96-a708-0c40-e25284fd068d
document_version_independent_id: 652134c5-0c96-a708-0c40-e25284fd068d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-oracle-source.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-oracle-source
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-oracle-source.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 134f8513-163e-e4da-22bb-94bc65b2553c
---

# Connect to and manage Oracle in Microsoft Purview | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register Oracle, and how to authenticate and interact with Oracle in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported Oracle server versions are 6i to 19c. Oracle proxy server isn't supported when scanning Oracle source.

When scanning Oracle source, Microsoft Purview supports:

- Extracting technical metadata, including:

    - Server
    - Schemas
    - Packages
    - Tables including the columns, foreign keys, indexes, triggers, and unique constraints
    - Views including the columns and triggers
    - Stored procedures including the parameter dataset and result set
    - Functions including the parameter dataset
    - Sequences
    - Synonyms
    - Types including the type attributes
- Fetching static lineage on assets relationships among tables and views.
- Stored procedure lineage.

When setting up scan, you can choose to scan an entire Oracle server, or scope the scan to a subset of schemas matching one or more given names or name patterns.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

- Currently, the Oracle service name isn't captured in the metadata or hierarchy.
- When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.
- Stored procedures directly under a schema or not within a package aren't supported.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- [The enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise) or an active Microsoft Purview account using the [classic governance portal](use-microsoft-purview-governance-portal).
- You need to be a Data Source Administrator and Data Reader to register a source in the Microsoft Purview Data Map. Get details about [domain and collection permissions](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).
- Set up the latest [self-hosted integration runtime](https://go.microsoft.com/fwlink/?linkid=2246619). For more information, see [the create and configure a self-hosted integration runtime guide](data-map-integration-runtime-self-hosted).

    - Ensure OpenJDK 8 with OJDBC driver 8 is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you install the JDK for it to take effect.

        - Ensure Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the self-hosted integration runtime machine. If you don't have this update installed, [you can download it here](/en-us/cpp/windows/latest-supported-vc-redist).
        - Download the [Oracle JDBC driver](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html) on the machine where your self-hosted integration runtime is running. Note down the folder path that you'll use to set up the scan.

            Note

            The driver should be accessible by the self-hosted integration runtime. By default, self-hosted integration runtime uses [local service account "NT SERVICE\DIAHostService"](data-map-integration-runtime-self-hosted#service-account-for-self-hosted-integration-runtime). Make sure it has "Read and execute" and "List folder contents" permission to the driver folder.

### Required permissions for scan

Microsoft Purview supports basic authentication (username and password) for scanning Oracle. The Oracle user must have read access to system tables in order to access advanced metadata and classification.

The user should have permission to create a session and role SELECT\_CATALOG\_ROLE assigned. Alternatively, the user could have SELECT permission granted for every individual system table that this connector queries metadata from:

```sql
grant create session to [user];
grant select on all_users to [user];
grant select on dba_objects to [user];
grant select on dba_tab_comments to [user];
grant select on dba_external_locations to [user];
grant select on dba_directories to [user];
grant select on dba_mviews to [user];
grant select on dba_clu_columns to [user];
grant select on dba_tab_columns to [user];
grant select on dba_col_comments to [user];
grant select on dba_constraints to [user];
grant select on dba_cons_columns to [user];
grant select on dba_indexes to [user];
grant select on dba_ind_columns to [user];
grant select on dba_procedures to [user];
grant select on dba_synonyms to [user];
grant select on dba_views to [user];
grant select on dba_source to [user];
grant select on dba_triggers to [user];
grant select on dba_arguments to [user];
grant select on dba_sequences to [user];
grant select on dba_dependencies to [user];
grant select on dba_type_attrs to [user];
grant select on V_$INSTANCE to [user];
grant select on v_$database to [user];
```

For classification, the user must have reader (SELECT) permissions on the relevant tables.

*For Individual Tables* Use the following SQL command to grant access to a specific table:

```sql
GRANT SELECT ON [table_name] TO [purview_user];
```

*For All Tables at Once* To grant access across all tables in the database, use:

```sql
GRANT SELECT ANY TABLE TO [purview_user];
```

## Register

This section describes how to register Oracle in Microsoft Purview using the Microsoft Purview portal.

### Steps to register

To register a new Oracle source in your data map, do the following:

1. Accessing the Microsoft Purview Data Map depends on which portal experience you're using.

    - If you're using the Microsoft Purview portal, navigate directly to the portal (https://purview.microsoft.com) and select the **Data Map** solution.
    - If you're using the classic Microsoft Purview governance portal, navigate directly to the portal (https://web.purview.azure.com), select your Microsoft Purview account, and select **Data map** from the left menu.
2. Select **Data sources**
3. Select **Register**
4. On Register sources, select **Oracle**. Select **Continue**.

    ![Screenshot of the register sources menu in the Microsoft Purview Data Map.](media/register-scan-oracle-source/register-sources.png)

On the **Register sources (Oracle)** screen, do the following:

1. Enter a **Name** that the data source will be listed within the Catalog.
2. Enter the **Host** name to connect to an Oracle source. This can either be:

    - A host name used to connect to the database server. For example: `MyDatabaseServer.com`
    - An IP address. For example: `192.169.1.2`
3. Enter the **Port number** used to connect to the database server (1521 by default for Oracle).
4. Enter the **Oracle service name** (not Oracle UID) used to connect to the database server.
5. Select a collection from the list.
6. Finish to register the data source.

    ![Screenshot of the register Oracle sources options.](media/register-scan-oracle-source/register-sources-2-expanded.png)

## Scan

Follow the steps below to scan Oracle and automatically classify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

Tip

To troubleshoot any issues with scanning:

1. Confirm you have followed all **prerequisites**.
2. Review our [**scan troubleshooting documentation**](troubleshoot-connections).

### Create and run scan

To create and run a new scan, do the following:

1. Under **Source management** in the data map, select **Integration runtimes**. Make sure a self-hosted integration runtime is set up. If it isn't set up, use the steps mentioned [here](data-map-integration-runtime-self-hosted) to create a self-hosted integration runtime.
2. Navigate to **Sources**.
3. Select the registered Oracle source.
4. Select **+ New scan**.
5. Provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the configured self-hosted integration runtime
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select Basic Authentication while creating a credential.
        - Provide the user name used to connect to the database server in the User name input field.
        - Store the user password used to connect to the database server in the secret key.
    4. **Schema**: List subset of schemas to import expressed as a semicolon separated list in **case-sensitive** manner. For example, `schema1;schema2`. All user schemas are imported if that list is empty. All system schemas (for example, SysAdmin) and objects are ignored by default.

        Acceptable schema name patterns can be static names or contain wildcard %. For example: `A%;%B;%C%;D`

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

        Usage of NOT and special characters aren't acceptable.
    5. **Driver location**: Specify the path to the JDBC driver location in your machine where self-host integration runtime is running. For example: `D:\Drivers\Oracle`.

        1. For self-hosted integration runtime on a local machine: `D:\Drivers\Oracle`. It's the path to valid JAR folder location. The value must be a valid absolute file path and doesn't contain space. Make sure the driver is accessible by the self-hosted integration runtime; learn more at prerequisites.
    6. **Stored procedure details**: Controls the number of details imported from stored procedures:

        - Signature: The name and parameters of stored procedures.
        - Code, signature: The name, parameters, and code of stored procedures.
        - Lineage, code, signature: The name, parameters and code of stored procedures, and the data lineage derived from the code.
        - None: Stored procedure details aren't included.
    7. **Maximum memory available**: Maximum memory (in GB) available on customer's VM to be used by scanning processes. This is dependent on the size of Oracle source to be scanned.

        Note

        As a rule of thumb, please provide 1GB memory for every 1000 tables

        ![Screenshot of the Oracle scan settings page.](media/register-scan-oracle-source/scan.png)
6. Select **Test connection**.

    Note

    Use the "Test connection" button in the scan setup UI to test the connection. The "Test Connection" in self-hosted integration runtime configuration manager UI -&gt; Diagnostics tab does not fully validate the connectivity.
7. Select **Continue**.
8. Select a **scan rule set** for classification. You can choose between the system default, existing custom rule sets, or [create a new rule set](data-map-scan-rule-set) inline.
9. Choose your **scan trigger**. You can set up a schedule or ran the scan once.
10. Review your scan and select **Save and Run**.

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

After scanning your Oracle source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported Oracle lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

![Oracle lineage view](media/register-scan-oracle-source/lineage.png)