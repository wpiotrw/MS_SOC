---
layout: Conceptual
title: Connect to and manage Salesforce in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-salesforce
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
description: Learn how to connect to Salesforce in Microsoft Purview with Data Map, and use Data Map features to scan and manage your Salesforce source.
locale: en-us
document_id: 0f83975c-71cf-1082-fb37-8a0d26532ce0
document_version_independent_id: 0f83975c-71cf-1082-fb37-8a0d26532ce0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-salesforce.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-salesforce
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-salesforce.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: ab484cce-19a5-e189-fcc9-f21bb00f21b7
---

# Connect to and manage Salesforce in Microsoft Purview | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register Salesforce, and how to authenticate and interact with Salesforce in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

When scanning Salesforce source, Microsoft Purview supports extracting technical metadata including:

- Organization
- Objects including the fields, foreign keys, and unique\_constraints

When setting up scan, you can choose to scan an entire Salesforce organization, or scope the scan to a subset of objects matching the given names or name patterns.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- A Salesforce connected app, which will be used to access your Salesforce information.
    - If you need to create a connected app, you can follow the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm&amp;type=5).
    - You'll need to [enable OAuth for your Salesforce application](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_api_integration.htm&amp;type=5).

Note

**If your data store is not publicly accessible** (if your data store limits access from on-premises network, private network or specific IPs, etc.), **you will need to configure a self hosted integration runtime to connect to it**.

- If your data source isn't publicly accessible, set up the latest self-hosted integration runtime.
    - [Choose the right integration runtime for your scenario](data-map-integration-runtime-choose):
        - **To use a self-hosted integration runtime:**
            - [Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
            - Ensure [JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) is installed on the machine where the self-hosted integration runtime is installed. Restart the machine after you newly install the JDK for it to take effect.
            - Ensure that Visual C++ Redistributable (version Visual Studio 2012 Update 4 or newer) is installed on the machine where the self-hosted integration runtime is running. If you don't have this update installed, [download it now](/en-us/cpp/windows/latest-supported-vc-redist).
            - Ensure the self-hosted integration runtime machine's IP is within the [trusted IP ranges for your organization](https://help.salesforce.com/s/articleView?id=sf.security_networkaccess.htm&amp;type=5) set on Salesforce.
        - **To use a kubernetes supported self-hosted integration runtime:**
            - [Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes).
            - Ensure the self-hosted integration runtime machine's IP is within the [trusted IP ranges for your organization](https://help.salesforce.com/s/articleView?id=sf.security_networkaccess.htm&amp;type=5) set on Salesforce.

### Required permissions for scan

If users will be submitting Salesforce Documents, certain security settings must be configured to allow this access on Standard Objects and Custom Objects. To configure permissions:

- Within Salesforce, select Setup and then select Manage Users.
- Under the Manage Users tree select Profiles.
- Once the Profiles appear on the right, select which Profile you want to edit and select the Edit link next to the corresponding profile.

For Standard Objects, ensure that the "Documents" section has the Read permissions selected. For Custom Objects, ensure that the Read permissions selected for each custom objects.

## Register

This section describes how to register Salesforce in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Steps to register

To register a new Salesforce source in Microsoft Purview Unified Catalog, follow these steps:

1. Navigate to your Microsoft Purview account in the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select **Data Map** on the left navigation.
3. Select **Register**
4. On Register sources, select **Salesforce**. Select **Continue**.

On the **Register sources (Salesforce)** screen, follow these steps:

1. Enter a **Name** that the data source will be listed within the Catalog.
2. Enter the Salesforce sign in endpoint URL as **Domain URL**. For example, `https://login.salesforce.com`. You can use your company's instance URL (such as `https://na30.salesforce.com`) or My Domain URL (such as `https://myCompanyName.my.salesforce.com/`) or Sandbox URL (such as `https://myCompanyName.sandbox.my.salesforce.com/`).
3. Select a collection from the list.
4. Finish to register the data source.

    ![register sources options](media/register-scan-salesforce/register-sources.png)

## Scan

Follow these steps to scan Salesforce to automatically identify assets. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

Microsoft Purview uses Salesforce REST API version 41.0 to extract metadata, including REST requests like 'Describe Global' URI (/v41.0/sobjects/),'sObject Basic Information' URI (/v41.0/sobjects/sObject/), and 'SOQL Query' URI (/v41.0/query?).

### Authentication for a scan

The supported authentication type for a Salesforce source is **Consumer key authentication**.

### Create and run scan

To create and run a new scan, follow these steps:

1. If your server is publicly accessible, skip to step two. Otherwise, you'll need to make sure your self-hosted integration runtime is configured:

    1. In the [Microsoft Purview governance portal](https://web.purview.azure.com/), got to the Management Center, and select **Integration runtimes**.
    2. Make sure a self-hosted integration runtime is available. If one isn't set up, use the steps mentioned in prerequisites to set up a self-hosted integration runtime.
2. In the [Microsoft Purview governance portal](https://web.purview.azure.com/), navigate to **Sources**.
3. Select the registered Salesforce source.
4. Select **+ New scan**.
5. Provide the below details:

    1. **Name**: The name of the scan
    2. **Connect via integration runtime**: Select the Azure autoresolved integration runtime if your server is publicly accessible, or your configured self-hosted integration runtime if it isn't publicly available.
    3. **Credential**: Select the credential to connect to your data source. Make sure to:

        - Select **Consumer key** while creating a credential.
        - Provide the username of the user that the connected app is imitating in the User name input field.
        - Store the password of the user that the connected app is imitating in an Azure Key Vault secret.
            - If your self-hosted integration runtime machine's IP is within the [trusted IP ranges for your organization](https://help.salesforce.com/s/articleView?id=sf.security_networkaccess.htm&amp;type=5) set on Salesforce, provide just the password of the user.
            - Otherwise, **concatenate the password and security token as the value of the secret**. The security token is an automatically generated key that must be added to the end of the password when logging in to Salesforce from an untrusted network. Learn more about how to [get or reset a security token](https://help.salesforce.com/apex/HTViewHelpDoc?id=user_security_token.htm).
        - Provide the consumer key from the connected app definition. You can find it on the connected app's Manage Connected Apps page or from the connected app's definition.
        - Stored the consumer secret from the connected app definition in an Azure Key Vault secret. You can find it along with consumer key.
    4. **Objects**: Provide a list of object names to scope your scan. For example, `object1; object2`. An empty list means it's retrieving all available objects. You can specify object names as a wildcard pattern. For example, `topic?`, `*topic*`, or `topic_?,*topic*`.
    5. **Maximum memory available** (applicable when using self-hosted integration runtime): Maximum memory (in GB) available on customer's VM to be used by scanning processes. This is dependent on the size of Salesforce source to be scanned.

        Note

        As a rule of thumb, please provide 1GB memory for every 1000 tables

        ![scan Salesforce](media/register-scan-salesforce/scan.png)
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