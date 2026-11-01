---
layout: Conceptual
title: Connect to and manage Google BigQuery projects | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-google-bigquery-source
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.date: 2023-04-20T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to connect to Google BigQuery projects in Microsoft Purview and use Microsoft Purview features to scan and manage your Google BigQuery source.
locale: en-us
document_id: a57fc61e-0249-05ae-5e86-aaf49a4d30fc
document_version_independent_id: a57fc61e-0249-05ae-5e86-aaf49a4d30fc
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-google-bigquery-source.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-google-bigquery-source
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-google-bigquery-source.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b3c3e02c-ee97-66de-95df-de367c6a0091
---

# Connect to and manage Google BigQuery projects | Microsoft Learn

This article outlines how to register Google BigQuery projects, and how to authenticate and interact with Google BigQuery in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

When scanning Google BigQuery source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Projects
    - Datasets
    - Tables including the columns
    - Views including the columns
- Fetching static lineage on assets relationships among tables and views.

When setting up scan, you can choose to scan an entire Google BigQuery project, or scope the scan to a subset of datasets matching the given name(s) or name pattern(s).

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

- Currently, Microsoft Purview only supports scanning Google BigQuery datasets in US multi-regional location. If the specified dataset is in other location e.g. us-east1 or EU, you will observe scan completes but no assets shown up in Microsoft Purview.
- When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose):

    - **To use a self-hosted integration runtime:**
        - [Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
        - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
        - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
        - Download and unzip the [BigQuery JDBC driver](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers) on the machine where your self-hosted integration runtime is running. Note down the folder path which you will use to set up the scan.
    - **To use a kubernetes supported self-hosted integration runtime:**
        - [Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).
        - Download and unzip the [BigQuery JDBC driver](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers) on the machine where your self-hosted integration runtime is running. Note down the folder path which you will use to set up the scan.

    Note

    The driver should be accessible by the self-hosted integration runtime. By default, self-hosted integration runtime uses [local service account "NT SERVICE\DIAHostService"](data-map-integration-runtime-self-hosted#service-account-for-self-hosted-integration-runtime). Make sure it has "Read and execute" and "List folder contents" permission to the driver folder.

### Required permissions for scan

The Google BigQuery service account you use for scan needs to have both BigQuery Metadata Viewer and BigQuery Job User [IAM roles](https://cloud.google.com/bigquery/docs/access-control) on the project(s) you want to scan. These permissions are required because Microsoft Purview extracts the metadata by reading the Google BigQuery database system tables (e.g. INFORMATION\_SCHEMA). And the underlying Google BigQuery JDBC driver creates a BigQuery job when it needs to read from these system tables.

Microsoft Purview uses Oauth 2.0 protocol for accessing Google BigQuery service. Set up the credential by following the instruction in Create and run scan section.

## Register

This section describes how to register a Google BigQuery project in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Steps to register

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left navigation.
3. Select **Register.**
4. On Register sources, select **Google BigQuery** . Select **Continue.**

    ![register BigQuery source](media/register-scan-google-bigquery-source/register-sources.png)

On the Register sources (Google BigQuery) screen, do the following:

1. Enter a **Name** that the data source will be listed within the Catalog.
2. Enter the **ProjectID.** This should be a fully qualified project ID. For example, mydomain.com:myProject
3. Select a collection from the list.
4. Select **Register**.

    ![configure BigQuery source](media/register-scan-google-bigquery-source/configure-sources.png)

## Scan

Follow the steps below to scan a Google BigQuery project to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Create and run scan

1. In the Management Center, select Integration runtimes. Make sure a self-hosted integration runtime is set up. If it isn't set up, use the steps mentioned in prerequisites.
2. Navigate to **Sources**.
3. Select the registered **BigQuery** project.
4. Select **+ New scan**.
5. Provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the configured self-hosted integration runtime
    3. **Credential**: While configuring BigQuery credential, make sure to:

        - Select **Basic Authentication** as the Authentication method
        - Provide the email ID of the service account in the User name field. For example, `xyz\@developer.gserviceaccount.com`
        - Follow below steps to generate the private key, copy the entire JSON key file then store it as the value of a Key Vault secret.

        To create a new private key from Google's cloud platform:

        1. In the navigation menu, select IAM & Admin -&gt; Service Accounts -&gt; Select a project -&gt;
        2. Select the email address of the service account that you want to create a key for.
        3. Select the **Keys** tab.
        4. Select the **Add key** drop-down menu, then select Create new key.
        5. Choose JSON format.

        Note

        The contents of the private key are saved in a temp file on the VM when scanning processes are running. This temp file is deleted after the scans are successfully completed. In the event of a scan failure, the system will continue to retry until success. Please make sure access is appropriately restricted on the VM where SHIR is running.

        To understand more on credentials, refer to the link [here](data-map-data-scan-credentials).
    4. **Driver location**: Specify the path to the JDBC driver location in your machine where self-host integration runtime is running. For example: `D:\Drivers\GoogleBigQuery`.

        1. For self-hosted integration runtime on a local machine: `D:\Drivers\GoogleBigQuery`. It's the path to valid JAR folder location. The value must be a valid absolute file path and doesn't contain space. Make sure the driver is accessible by the self-hosted integration runtime;; learn more from prerequisites section.
        2. For Kubernetes-supported self-hosted integration runtime: `./drivers/GoogleBigQuery`. It's the path to valid JAR folder location. The value must be a valid relative file path. Please refer to the documentation to [set up a scan with external drivers](data-map-integration-runtime-kubernetes#set-up-a-scan-with-external-drivers) for uploading drivers in advance.
    5. **Dataset**: Specify a list of BigQuery datasets to import. For example, `dataset1;dataset2`. When the list is empty, all available datasets are imported. Acceptable dataset name patterns can be static names or contain wildcard %.

        Example: `A%;%B;%C%;D`

        - Start with A or
        - end with B or
        - contain C or
        - equal D

        Usage of NOT and special characters aren't acceptable.
    6. **Maximum memory available**: Maximum memory (in GB) available on your VM to be used by scanning processes. This is dependent on the size of Google BigQuery project to be scanned.

        ![scan BigQuery source](media/register-scan-google-bigquery-source/scan.png)
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

After scanning your Google BigQuery source, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.

Go to the asset -&gt; lineage tab, you can see the asset relationship when applicable. Refer to the supported capabilities section on the supported Google BigQuery lineage scenarios. For more information about lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage user guide](data-gov-classic-lineage-user-guide).

![Google BigQuery lineage view](media/register-scan-google-bigquery-source/lineage.png)