---
layout: Conceptual
title: Connect to and manage MongoDB | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-mongodb
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
search.appverid:
- MET150
- MOE150
description: Learn how to connect to MongoDB in Microsoft Purview, and use Microsoft Purview features to scan and manage your MongoDB source.
locale: en-us
document_id: 9cdc776d-a6fe-dcd3-7a96-f2987d0f8d56
document_version_independent_id: 9cdc776d-a6fe-dcd3-7a96-f2987d0f8d56
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-mongodb.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-mongodb
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-mongodb.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: eac0ddb8-65f8-a22b-7a91-b3535b2a38c2
---

# Connect to and manage MongoDB | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register MongoDB, and how to authenticate and interact with MongoDB in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

The supported MongoDB versions are 3.6 to 7.0. You can use this connector to scan MongoDB Atlas as well.

When scanning MongoDB source, Microsoft Purview supports extracting technical metadata including:

- Server
- Databases
- Collections including the schema
- Views including the schema

During scan, Microsoft Purview retrieves and analyzes sample documents to infer the collection/view schema. The sample size is configurable.

When setting up scan, you can choose to scan one or more MongoDB databases entirely, or further scope the scan to a subset of collections matching the given names or name patterns.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- If your data source isn't publicly accessible, set up the latest self-hosted integration runtime.

    - [Choose the right integration runtime for your scenario](data-map-integration-runtime-choose):
        - **To use a self-hosted integration runtime:**
            - [Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
            - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
            - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
        - **To use a kubernetes supported self-hosted integration runtime:**
            - [Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).

## Register

This section describes how to register MongoDB in Microsoft Purview using the classic [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Steps to register

To register a new MongoDB source in Microsoft Purview Unified Catalog, do the following:

1. Navigate to your Microsoft Purview account in the classic [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On Register sources, select **MongoDB**. Select **Continue**.

On the **Register sources (MongoDB)** screen, do the following:

1. Enter a **Name** that the data source will be listed within the Catalog.
2. Enter the **server** name. Specify a name to uniquely identify your MongoDB instance in your company. For example, `host` for standalone deployment, `MyReplicaSetName` for replica set, `MyClusterName` for sharded cluster. This value is used in asset qualified name and can't be changed.
3. Select a collection from the list.
4. Finish to register the data source.

    ![register sources options](media/register-scan-mongodb/register-sources.png)

## Scan

Follow the steps below to scan MongoDB to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Authentication for a scan

The supported authentication type for a MongoDB source is **Basic authentication**.

### Create and run scan

To create and run a new scan, do the following:

1. In the Management Center, select Integration runtimes. Make sure a self-hosted integration runtime is set up. If it isn't set up, use the steps mentioned in prerequisites to create a self-hosted integration runtime.
2. Navigate to **Sources**.
3. Select the registered MongoDB source.
4. Select **+ New scan**.
5. Provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the self-hosted integration runtime used to perform scan.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select **Basic Authentication** while creating a credential.
        - Provide the user name used to connect to MongoDB in the User name input field.
        - Store the user password used to connect to MongoDB in the secret key.
    4. **Connection string**: Specify the MongoDB connection string used to connect to your MongoDB, excluding the username and password. For example, `mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017/?replicaSet=myRepl`, `mongodb+srv://mongodb0.example.com/?authSource=admin&replicaSet=myRepl`.
    5. **Databases**: Specify a list of MongoDB databases to be imported. The list can have one or more database names separated by semicolon (;), for example, `database1; database2`.
    6. **Collections**: The subset of collections to import expressed as a semicolon separated list of collections, for example, `collection1;collection2`. All collections are imported if the list is empty.​

        Acceptable collection name patterns can be static names or contain wildcard %. For example: `A%;%B;%C%;D`:

        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

        Usage of NOT and special characters aren't acceptable.
    7. **Number of sample documents**: Number of sample documents to be analyzed for schema extraction. Default is 10.
    8. **Maximum memory available** (applicable when using self-hosted integration runtime): Maximum memory (in GB) available on customer's VM to be used by scanning processes. It's dependent on the size of MongoDB source to be scanned.

        ![scan MongoDB](media/register-scan-mongodb/scan.png)
6. Select **Test connection** to validate the configurations.

    Note

    After you select **Test connection**, this message might appear: "The legacy MongoDB connector is deprecated." If you get this message, it doesn't affect the scan. You can skip the test connection and continue scanning Mongo DB in Microsoft Purview.
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