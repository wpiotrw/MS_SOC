---
layout: Conceptual
title: Amazon Redshift multicloud scanning connector for Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-amazon-redshift
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This document introduces the preview for scanning Amazon Redshift in Microsoft Purview.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2023-09-15T00:00:00.0000000Z
ms.custom:
- template-how-to
- sfi-image-nochange
locale: en-us
document_id: 7dc8ef8c-9a04-0a65-1552-c663e0732ffa
document_version_independent_id: 7dc8ef8c-9a04-0a65-1552-c663e0732ffa
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-amazon-redshift.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-amazon-redshift
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-amazon-redshift.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 8e514b6a-d9a2-e9d2-a356-5df130c77721
---

# Amazon Redshift multicloud scanning connector for Microsoft Purview | Microsoft Learn

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

This document introduces the preview for scanning Amazon Redshift in Microsoft Purview.

## Supported capabilities

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

When scanning Amazon Redshift, Microsoft Purview supports extracting technical metadata including:

- Server
- Databases
- Schemas
- Tables including the columns, foreign keys and unique constraints
- Views including the columns
- Stored procedures including the parameter dataset
- Functions including the parameter dataset

When setting up scan, you can choose to scan an entire Amazon Redshift database, or scope the scan to a subset of schemas matching the given name(s) or name pattern(s).

### Known limitations

- When an object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You'll need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.
- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose). If your data source isn't publicly accessible, set up the latest [kubernetes supported self-hosted integration runtime](data-map-integration-runtime-kubernetes).

## Register

This section will enable you to register the Amazon Redshift data source for scan and data share in Purview.

### Prerequisites for register

- You'll need to be a Data Source Admin and one of the other Purview roles (for example, Data Reader or Data Share Contributor) to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

### Steps to register

It's important to register the data source in Microsoft Purview prior to setting up a scan for the data source.

1. Go to the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Select the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Navigate to the **Data Map --&gt; Sources**

    [![Screenshot that shows the link to open Microsoft Purview governance portal](media/register-scan-amazon-redshift/open-purview-studio-inline.png)](media/register-scan-amazon-redshift/open-purview-studio.png#lightbox)

    ![Screenshot that navigates to the Sources link in the Data Map](media/register-scan-amazon-redshift/sources.png)
3. Navigate to the appropriate collection under the **Sources** menu and select the **Register** icon to register a new Amazon Redshift data source.
4. Select the **Amazon Redshift** data source and select **Continue**.
5. Provide a suitable **Name** for the data source, and provide these details:

    1. Endpoint - The endpoint of your Amazon Redshift cluster. For example: `examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com`
    2. Port - The port number that you specified when you launched the cluster. The default is 5439.

    [![Screenshot that shows the register menu for Amazon Redshift.](media/register-scan-amazon-redshift/register-data-source-inline.png)](media/register-scan-amazon-redshift/register-data-source.png#lightbox)
6. The Amazon Redshift cluster is shown under the selected Collection

## Scan

Tip

To troubleshoot any issues with scanning:

1. Confirm you have properly set up **authentication for scanning**.
2. Review our [**scan troubleshooting documentation**](troubleshoot-connections).

### Authentication for a scan

Microsoft Purview supports basic authentication (username and password) for scanning Amazon Redshift.

The user should have **SELECT** permission granted for every individual system table for Microsoft Purview to query metadata from:

- svv\_external\_tables
- svv\_external\_columns
- svv\_table\_info
- information\_schema.routines
- information\_schema.parameters
- pg\_views
- pg\_database
- pg\_description

And user should have **EXECUTE** permission granted for system function for Microsoft Purview to query metadata from:

- pg\_get\_late\_binding\_view\_cols

### Create a credential

Microsoft Purview uses **Azure Key Vault** to safely store the credentials it uses to authenticate with sources.

- If you haven't set up an Azure Key Vault to store credentials, first [create an Azure Key Vault](/en-us/azure/key-vault/general/quick-create-portal) and then [follow these steps to connect your Microsoft Purview account to your Azure Key Vault.](data-map-data-scan-credentials)
- Once you have an Azure Key Vault, [store your Amazon Redshift password as a secret in the Key Vault](/en-us/azure/key-vault/secrets/quick-create-portal#add-a-secret-to-key-vault), and then [follow these steps](data-map-data-scan-credentials#create-a-new-credential)to create a credential with this information:
    - Basic authentication credential
    - Add your user name in the input field
    - Add your Key Vault connection and the name of the secret where your password is stored

### Create the scan

1. Open your **Microsoft Purview account** and select the **Open Microsoft Purview governance portal**
2. Navigate to the **Data map** --&gt; **Sources** to view the collection hierarchy
3. Select the **New Scan** icon under the **Amazon Redshift data source** registered earlier.
4. Select your integration runtime.
5. Provide these details:

    1. Name - a name for your scan
    2. Credential - choose the credential you created earlier
    3. Database - name of the database instance to scan
    4. Schema - The subset of schemas to import expressed as a semicolon separated list of schemas. For example: "schema1;schema2". All user schemas are imported if that list is empty. All system schemas and objects are ignored by default. Acceptable schema name patterns can be static names or contain wildcard %. For example: "A%;%B;%C%;D":
        - Start with A or
        - End with B or
        - Contain C or
        - Equal D

    [![Screenshot that shows the scan menu for Amazon Redshift.](media/register-scan-amazon-redshift/create-scan-inline.png)](media/register-scan-amazon-redshift/create-scan.png#lightbox)
6. Select **Test connection** to validate the settings.
7. Select **Continue**.
8. For **Scan trigger** choose whether to set up a schedule or run the scan once.
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

## Browse, search, and view assets

After successfully scanning your Amazon Redshift clusters, you can [browse the Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.