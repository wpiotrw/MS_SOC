---
layout: Conceptual
title: Connect to and manage Hive Metastore databases | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-hive-metastore-source
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to Hive Metastore databases in Microsoft Purview, and how to use Microsoft Purview to scan and manage your Hive Metastore database source.
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
document_id: 8a2aff89-e1d6-2429-89b5-0ecf553aeb79
document_version_independent_id: 8a2aff89-e1d6-2429-89b5-0ecf553aeb79
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-hive-metastore-source.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-hive-metastore-source
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-hive-metastore-source.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 1ad6d810-306b-d5e6-98e5-730a5ef4afc4
---

# Connect to and manage Hive Metastore databases | Microsoft Learn

This article outlines how to register Hive Metastore databases, and how to authenticate and interact with Hive Metastore databases in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported Hive versions are 2.x to 3.x. The supported platforms are Apache Hadoop, Cloudera, and Hortonworks. If you want to scan Azure Databricks, you're suggested to use the [Azure Databricks connector](register-scan-azure-databricks), which is more compatible and user friendly.

When scanning Hive metastore source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Server
    - Databases
    - Tables including the columns, foreign keys, unique constraints, and storage description
    - Views including the columns and storage description
- Fetching static lineage on assets relationships among tables and views.

When setting up scan, you can choose to scan an entire Hive metastore database, or scope the scan to a subset of schemas matching the given name(s) or name pattern(s).

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- You must have an Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- You must have an active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- If your data source isn't publicly accessible, set up the latest self-hosted integration runtime.

    - [Choose the right integration runtime for your scenario](data-map-integration-runtime-choose):
        - **To use a self-hosted integration runtime:**
            - [Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
            - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
            - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
            - Download the Hive Metastore database's JDBC driver on the machine where your self-hosted integration runtime is running. For example, if the database is *mssql*, download [Microsoft's JDBC driver for SQL Server](/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server). Note down the folder path that you'll use to set up the scan.
        - **To use a kubernetes supported self-hosted integration runtime:**
            - [Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).
            - Download the Hive Metastore database's JDBC driver on the machine where your self-hosted integration runtime is running. For example, if the database is *mssql*, download [Microsoft's JDBC driver for SQL Server](/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server). Note down the folder path that you'll use to set up the scan.

    Note

    The JDBC driver should be accessible by the self-hosted integration runtime. By default, self-hosted integration runtime uses [local service account "NT SERVICE\DIAHostService"](data-map-integration-runtime-self-hosted#service-account-for-self-hosted-integration-runtime). Make sure it has "Read and execute" and "List folder contents" permission to the driver folder.

## Register

This section describes how to register a Hive Metastore database in Microsoft Purview by using [the Microsoft Purview governance portal](https://web.purview.azure.com/).

The only supported authentication for a Hive Metastore database is Basic Authentication.

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left pane.
3. Select **Register**.
4. In **Register sources**, select **Hive Metastore** &gt; **Continue**.
5. On the **Register sources (Hive Metastore)** screen, do the following:

    1. For **Name**, enter a name that Microsoft Purview will list as the data source.
    2. For **Hive Cluster URL**, enter a value that you get from the Ambari URL. For example, enter **hive.azurehdinsight.net**.
    3. For **Hive Metastore Server URL**, enter a URL for the server. For example, enter **sqlserver://hive.database.windows.net**.
    4. Select a collection from the list.

    ![Screenshot that shows boxes for registering Hive sources.](media/register-scan-hive-metastore-source/configure-sources.png)
6. Select **Finish**.

## Scan

Tip

To troubleshoot any issues with scanning:

1. Confirm you have followed all **prerequisites**.
2. Review our [**scan troubleshooting documentation**](troubleshoot-connections).

Use the following steps to scan Hive Metastore databases to automatically identify assets. For more information about scanning in general, see [Scans and ingestion in Microsoft Purview](data-map-scan-ingestion).

1. In the Management Center, select integration runtimes. Make sure that a self-hosted integration runtime is set up. If it isn't set up, use the steps in prerequisites.
2. Go to **Sources**.
3. Select the registered Hive Metastore database.
4. Select **+ New scan**.
5. Provide the following details:

    1. **Name**: Enter a name for the scan.
    2. **Connect via integration runtime**: Select the configured self-hosted integration runtime.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select Basic Authentication while creating a credential.
        - Provide the Metastore username in the appropriate box.
        - Store the Metastore password in the secret key.

        For more information, see [Credentials for source authentication in Microsoft Purview](data-map-data-scan-credentials).
    4. **Metastore JDBC Driver Location**: Specify the path to the JDBC driver location in your machine where self-host integration runtime is running. For example, `D:\Drivers\HiveMetastore`.

        1. For self-hosted integration runtime on a local machine: `D:\Drivers\HiveMetastore`. It's the path to valid JAR folder location. The value must be a valid absolute file path and doesn't contain space. Make sure the driver is accessible by the self-hosted integration runtime;; learn more from prerequisites section.
        2. For Kubernetes-supported self-hosted integration runtime: `./drivers/HiveMetastore`. It's the path to valid JAR folder location. The value must be a valid relative file path. Please refer to the documentation to [set up a scan with external drivers](data-map-integration-runtime-kubernetes#set-up-a-scan-with-external-drivers) for uploading drivers in advance.
    5. **Metastore JDBC Driver Class**: Provide the class name for the connection driver. For example, enter **\com.microsoft.sqlserver.jdbc.SQLServerDriver**.
    6. **Metastore JDBC URL**: Provide the connection URL value and define the connection to the URL of the Metastore database server. For example: `jdbc:sqlserver://hive.database.windows.net;database=hive;encrypt=true;trustServerCertificate=true;create=false;loginTimeout=300`.

        Note

        When you copy the URL from *hive-site.xml*, remove `amp;` from the string or the scan will fail.

        [Download the SSL certificate](https://www.digicert.com/CACerts/BaltimoreCyberTrustRoot.crt.pem) to the self-hosted integration runtime machine, then update the path to the SSL certificate's location on your machine in the URL.

        When you enter local file paths in the scan configuration, change the Windows path separator character from a backslash (`\`) to a forward slash (`/`). For example, if you place the SSL certificate at local file path *D:\Drivers\SSLCert\BaltimoreCyberTrustRoot.crt.pem*, change the `serverSslCert` parameter value to *D:/Drivers/SSLCert/BaltimoreCyberTrustRoot.crt.pem*.

        The **Metastore JDBC URL** value will look like this example:

        `jdbc:mariadb://samplehost.mysql.database.azure.com:3306/XXXXXXXXXXXXXXXX?useSSL=true&enabledSslProtocolSuites=TLSv1,TLSv1.1,TLSv1.2&serverSslCert=D:/Drivers/SSLCert/BaltimoreCyberTrustRoot.crt.pem`
    7. **Metastore database name**: Provide the name of the Hive Metastore database.
    8. **Schema**: Specify a list of Hive schemas to import. For example: **schema1; schema2**.

        All user schemas are imported if that list is empty. All system schemas (for example, SysAdmin) and objects are ignored by default.

        Acceptable schema name patterns that use SQL `LIKE` expression syntax include the percent sign (%). For example, `A%; %B; %C%; D` means:

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

        Usage of `NOT` and special characters isn't acceptable.
    9. **Maximum memory available**: Maximum memory (in gigabytes) available on the customer's machine for the scanning processes to use. This value is dependent on the size of Hive Metastore database to be scanned.

        Note

        As a thumb rule, please provide 1GB memory for every 1000 tables.

    ![Screenshot that shows boxes for scan details.](media/register-scan-hive-metastore-source/scan.png)
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

## Lineage

After scanning your Hive Metastore source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported Hive Metastore lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).