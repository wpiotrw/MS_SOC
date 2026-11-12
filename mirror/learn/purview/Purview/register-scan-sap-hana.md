---
layout: Conceptual
title: Connect to and manage SAP HANA | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-sap-hana
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to SAP HANA in Microsoft Purview, and how to use Microsoft Purview to scan and manage your SAP HANA source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-how-to, msecd-doc-authoring-1030
locale: en-us
document_id: 256c04b2-f4fc-044e-33a4-9e6a86d304ab
document_version_independent_id: 256c04b2-f4fc-044e-33a4-9e6a86d304ab
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-sap-hana.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-sap-hana
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-sap-hana.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a990abc9-acfe-e9ba-a771-156fe5d2106f
---

# Connect to and manage SAP HANA | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register SAP HANA, and how to authenticate and interact with SAP HANA in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

When scanning SAP HANA source, Microsoft Purview supports extracting technical metadata including:

- Server
- Databases
- Schemas
- Tables, including the columns, foreign keys, indexes, and unique constraints.
- Views, including the columns.
- Calculation views. These are scanned as a part of \_SIS\_BIC schema. For scoped scan scenarios, this schema needs to be included.
- Stored procedures including the parameter dataset and result set.
- Functions, including the parameter dataset.
- Sequences
- Synonyms

When setting up scan, you can choose to scan an entire SAP HANA database, or scope the scan to a subset of schemas matching the given names or name patterns.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- You must have an Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- You must have an active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose):

    - **To use a self-hosted integration runtime:**
        - [Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
        - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
        - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
        - Download the SAP HANA JDBC driver [(JAR ngdbc)](https://mvnrepository.com/artifact/com.sap.cloud.db.jdbc/ngdbc) on the machine where your self-hosted integration runtime is running. Note down the folder path that you'll use to set up the scan.
    - **To use a kubernetes supported self-hosted integration runtime:**
        - [Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).
        - Download the SAP HANA JDBC driver [(JAR ngdbc)](https://mvnrepository.com/artifact/com.sap.cloud.db.jdbc/ngdbc) on the machine where your self-hosted integration runtime is running. Note down the folder path that you'll use to set up the scan.

    Note

    The driver should be accessible by the self-hosted integration runtime. By default, self-hosted integration runtime uses [local service account "NT SERVICE\DIAHostService"](data-map-integration-runtime-self-hosted#service-account-for-self-hosted-integration-runtime). Make sure it has "Read and execute" and "List folder contents" permission to the driver folder.

### Required permissions for scan

Microsoft Purview supports basic authentication (username and password) for scanning SAP HANA.

The SAP HANA user you specified must have the permission to select metadata of the schemas you want to import.

```sql
CREATE USER <user> PASSWORD <password> NO FORCE_FIRST_PASSWORD_CHANGE;
GRANT SELECT METADATA ON SCHEMA <schema1> TO <user>;
GRANT SELECT METADATA ON SCHEMA <schema2> TO <user>;
```

And the user must have the permission to select on system table \_SYS\_REPO.ACTIVE\_OBJECT and on system schemas \_SYS\_BI and \_SYS\_BIC.

```sql
GRANT SELECT ON _SYS_REPO.ACTIVE_OBJECT TO <user>;
GRANT SELECT ON SCHEMA _SYS_BI TO <user>;
GRANT SELECT ON SCHEMA _SYS_BIC TO <user>;
```

## Register

This section describes how to register an SAP HANA in Microsoft Purview by using the [classic Microsoft Purview governance portal](https://web.purview.azure.com/).

1. Open the classic Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Select the [classic Microsoft Purview governance portal](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left pane.
3. Select **Register**.
4. In **Register sources**, select **SAP HANA** &gt; **Continue**.
5. On the **Register sources (SAP HANA)** screen, do the following:

    1. For **Name**, enter a name that Microsoft Purview will list as the data source.
    2. For **Server**, enter the host name or IP address used to connect to an SAP HANA source. For example, `MyDatabaseServer.com` or `192.169.1.2`.
    3. For **Port**, enter the port number used to connect to the database server (39013 by default for SAP HANA).
    4. Select a collection from the list.

    ![Screenshot that shows boxes for registering SAP HANA sources.](media/register-scan-sap-hana/configure-sources.png)
6. Select **Finish**.

## Scan

Use the following steps to scan SAP HANA databases to automatically identify assets. For more information about scanning in general, see [Scans and ingestion in Microsoft Purview](data-map-scan-ingestion).

### Authentication for a scan

The supported authentication type for an SAP HANA source is **Basic authentication**.

### Create and run scan

1. In the Management Center, select integration runtimes. Make sure that a self-hosted integration runtime is set up. If it isn't set up, use the steps in in prerequisites.
2. Go to **Sources**.
3. Select the registered SAP HANA source.
4. Select **+ New scan**.
5. Provide the following details:

    1. **Name**: Enter a name for the scan.
    2. **Connect via integration runtime**: Select the configured self-hosted integration runtime.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select **Basic Authentication** while creating a credential.
        - Provide the user name used to connect to the database server in the User name input field.
        - Store the user password used to connect to the database server in the secret key.

        For more information, see [Credentials for source authentication in Microsoft Purview](data-map-data-scan-credentials).
    4. **Database**: Specify the name of the database instance to import.
    5. **Schema**: List subset of schemas to import expressed as a semicolon separated list. For example, `schema1; schema2`. All user schemas are imported if that list is empty. All system schemas and objects are ignored by default.

        Acceptable schema name patterns that use SQL `LIKE` expression syntax include the percent sign (%). For example, `A%; %B; %C%; D` means:

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

        Usage of NOT and special characters aren't acceptable.
    6. **Driver location**: Specify the path to the JDBC driver location in your machine where self-host integration runtime is running. For example: `D:\Drivers\SAPHANA`.

        1. For self-hosted integration runtime on a local machine: `D:\Drivers\SAPHANA`. It's the path to valid JAR folder location. The value must be a valid absolute file path and doesn't contain space. Make sure the driver is accessible by the self-hosted integration runtime; learn more from prerequisites section.
        2. For Kubernetes-supported self-hosted integration runtime: `./drivers/SAPHANA`. It's the path to valid JAR folder location. The value must be a valid relative file path. Refer to the documentation to [set up a scan with external drivers](data-map-integration-runtime-kubernetes#set-up-a-scan-with-external-drivers) for uploading drivers in advance.
    7. **Maximum memory available**: Maximum memory (in gigabytes) available on the customer's machine for the scanning processes to use. This value is dependent on the size of SAP HANA database to be scanned.

    ![Screenshot that shows boxes for scan details.](media/register-scan-sap-hana/scan.png)
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