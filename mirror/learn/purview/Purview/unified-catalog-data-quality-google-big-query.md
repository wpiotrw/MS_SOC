---
layout: Conceptual
title: Set Up Data Quality for Google BigQuery (Preview) in Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-google-big-query
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2024-08-12T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Get step-by-step guidance to configure data quality scans for Google BigQuery (preview) in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 12efd97e-c6f5-0c88-64ae-b0e2ebb23bbf
document_version_independent_id: 12efd97e-c6f5-0c88-64ae-b0e2ebb23bbf
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-google-big-query.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-google-big-query
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-google-big-query.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 88db7eca-5031-d644-5a0d-9c5dff2bae15
---

# Set Up Data Quality for Google BigQuery (Preview) in Microsoft Purview Unified Catalog | Microsoft Learn

This article provides step-by-step guidance to register, scan, and configure data quality for Google BigQuery sources in Microsoft Purview Unified Catalog.

## Supported capabilities

When scanning a Google BigQuery source, Microsoft Purview supports:

- Extracting technical metadata including:
    - Projects and datasets.
    - Tables including the columns.
    - Views including the columns.
- Fetching static lineage on assets relationships among tables and views.

When setting up a scan, you can choose to scan an entire Google BigQuery project. You can also scope the scan to a subset of datasets matching the given names or name patterns.

## Known limitations

Be aware of the following limitations when scanning Google BigQuery sources:

- Microsoft Purview only supports scanning Google BigQuery datasets in a US multiregional location. If a dataset is in another location (for example, "us-east1" or "EU"), the scan completes but no assets appear in Microsoft Purview.
- When you delete an object from the data source, the subsequent scan doesn't automatically remove the corresponding asset in Microsoft Purview.

## Configure Data Map scan to catalog Google BigQuery data in Microsoft Purview

### Register a Google BigQuery project

To register a Google BigQuery project in Microsoft Purview, complete the following steps:

1. In the Microsoft Purview portal, select **Data Map**, then select **Register**.
2. At **Register sources**, select **Google BigQuery**, then select **Continue**.
3. Enter a **Name** for the data source that appears in the catalog.
4. Enter the **ProjectID**. The ProjectID should be a fully qualified project ID. For example, `mydomain.com: myProject`.
5. Select a collection from the list.
6. Select **Register**.

### Set up a Data Map scan for Google BigQuery project

To configure a Data Map scan for the registered Google BigQuery project, follow these steps:

1. Make sure a self-hosted integration runtime is set up. If the runtime isn't set up, use the steps in [Google BigQuery connection prerequisites](register-scan-google-bigquery-source#prerequisites).
2. Navigate to **Sources**.
3. Select the registered BigQuery project.
4. Select **New scan**.
5. Enter these details:

    - **Name**: The name of the scan.
    - **Connect via integration runtime**: Select the configured self-hosted integration runtime.
    - **Credential**: While configuring BigQuery credential, make sure to:
        - Select **Basic Authentication** as the authentication method.
        - Provide the email ID of the service account in the **User name** field. For example, `xyz\@developer.gserviceaccount.com`.
        - Store the service account private key as a Key Vault secret (see the following steps).
    - **JDBC driver location**: Specify the path to the JDBC (Java Database Connectivity) driver on the machine where the self-hosted integration runtime is running. For example: `D:\Drivers\GoogleBigQuery`.
    - **Datasets to import**: Specify a list of BigQuery datasets to import. For example, `dataset1`; `dataset2`. When the list is empty, all available datasets are imported.
    - **Maximum memory (in GB)**: The required memory value depends on the size of the Google BigQuery project being scanned.

    **Create a service account private key:**

    1. In the Google Cloud console navigation menu, select **IAM & Admin** &gt; **Service Accounts**, then select a project.
    2. Select the email address of the service account that you want to create a key for.
    3. Select the **Keys** tab.
    4. Select **Add key** &gt; **Create new key**.
    5. Choose JSON format.
    6. Copy the entire JSON key file and store it as the value of a Key Vault secret.
6. Select **Test connection**.
7. Select **Continue**.
8. Choose your scan trigger. You can set up a schedule or run the scan once.
9. Review your scan and select **Save and Run**.

Once scanned, the data assets in Google BigQuery project are available in the Unified Catalog search. For more information, see [how to connect and manage Google BigQuery in Microsoft Purview](register-scan-google-bigquery-source).

Important

Deleting your scan doesn't delete catalog assets created from previous scans.

### Set up connection to Google BigQuery project for data quality scan

The scanned assets are now ready for cataloging and governance. Associate the scanned assets to the data products in a governance domain to set up a data quality scan.

Important

Data quality stewards need **read only** access to Google BigQuery to set up a data quality connection. Virtual network and private endpoint aren't supported for Google BigQuery data source yet for data quality scanning service.

1. In Unified Catalog, go to **Health management** &gt; **Data quality**. Select a governance domain to open its details page, then select **Manage** to create a connection.
2. Set up the connection:

    - Add connection name and description.
    - Select source type **Google BigQuery**.
    - Add **Project ID**, **Dataset name**, and **Table name**.
    - Enter details at **Service account private key**:
        - Add the Microsoft Azure subscription.
        - Add the Microsoft Azure Key Vault connection.
        - Enter the **Secret name**.
        - Enter the **Secret version**.
3. Test the connection to make sure the data source connection is successfully configured.

    ![Screenshot that shows how to set up google BigQuery connection.](media/dq-connectors/dq-google-big-query-connection-setup-1.png)

    ![Screenshot that shows how to configure connection for google BigQuery.](media/dq-connectors/dq-google-big-query-connection-setup-2.png)

## Profiling and data quality scanning for data in Google BigQuery

After you set up the connection, you can profile your data, create and apply rules, and run a data quality scan for your data in Google BigQuery. Follow the step-by-step guidelines in the following articles:

- [How to configure and run data profiling of your data](unified-catalog-data-quality-profiling)
- [How to configure and run data quality scan](unified-catalog-data-quality-scan)