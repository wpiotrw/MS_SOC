---
layout: Conceptual
title: Connect to and manage Qlik Sense | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-qlik-sense
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to use Microsoft Purview to scan and manage your Qlik Sense.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2024-06-04T00:00:00.0000000Z
ms.custom: template-how-to
locale: en-us
document_id: 982348f0-95e0-5902-c71e-fe3f8a930de4
document_version_independent_id: 982348f0-95e0-5902-c71e-fe3f8a930de4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-qlik-sense.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-qlik-sense
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-qlik-sense.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 61b82962-482f-3f01-39f0-bae7941a98a2
---

# Connect to and manage Qlik Sense | Microsoft Learn

This article outlines how to register Qlik Sense, and how to authenticate and interact with Qlik Sense in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | No |

The supported Qlik Sense version is 11.11 to 14.x.

When scanning Qlik Sense, Microsoft Purview supports extracting technical metadata including:

- Server
- Folders
- Streams
- Applications
- Stories
- Dimensions
- Measures
- Expressions
- QVD (QlikView Data)
- Tables and the columns
- Sheets and the lists, charts, report tables, pivot tables, axes, text boxes, text fields

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

- When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.

## Prerequisites

- You must have an Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- You must have an active [Microsoft Purview account](create-microsoft-purview-portal).
- You need an Azure Key Vault, and to [grant Microsoft Purview permissions to access secrets](data-map-data-scan-credentials#grant-microsoft-purview-access-to-your-azure-key-vault).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](catalog-permissions).
- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose). If your data source isn't publicly accessible, set up the latest [kubernetes supported self-hosted integration runtime](data-map-integration-runtime-kubernetes).

### Required permissions for scan

Microsoft Purview extracts metadata via Qlik Engine API (JSON over WebSocket). It supports **Qlik Sense certificate authentication** for scanning Qlik Sense. Make sure:

- User account must have read access granted.
- This may be accomplished by creating security rules for a specific application and user.
- Another alternative is if the application is published to a specific stream and the user has rights to read from this stream.

The user must have appropriate permissions:

- Read all application objects (especially script).
- Read all data connections (or at least data connections specified in application).

### Create Qlik Sense certificate

You need to export the certificate from Qlik Sense. Learn more from [Exporting certificates through the QMC](https://help.qlik.com/en-US/sense-admin/May2024/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Administer_QSEoW/Managing_QSEoW/export-certificates.htm).

1. Launch Qlik Management Console (QMC): https://your\_QPS\_server\_name/qmc.
2. Under **CONFIGURE SYSTEM**, click **Certificates**.
3. Enter the machine name, and optionally input the certificate password or leave it empty.
4. Keep the export file format as "Windows format".
5. Note the location where the certificate will be exported to, and then click Export certificates.
6. In File Explorer, navigate to where the certificate was exported to, e.g. `C:\ProgramData\Qlik\Sense\Repository\Exported Certificates`.

Next, store the **client.pfx** certificate you exported in your Azure Key Vault. You can choose to store it as a certificate or as a secret.

- To store it as a certificate, follow the steps in [Tutorial: Import a certificate in Azure Key Vault](/en-us/azure/key-vault/certificates/tutorial-import-certificate). If your certificate is protected by a password, note after imported in Key Vault, its associated password isn't saved. The password is required only once during the import operation.
- To store it as a secret, you can convert the content of client.pfx to Base64 format using https://www.base64encode.org/, and put the resulted string as secret value. If your certificate is protected by a password, also save the password as another secret.

## Register

This section describes how to register a Qlik Sense server in Microsoft Purview by using [the Microsoft Purview governance portal](https://web.purview.azure.com/).

1. Go to your Microsoft Purview account.
2. Select **Data Map** on the left pane.
3. Select **Register**.
4. In **Register sources**, select **Qlik Sense** &gt; **Continue**.
5. On the **Register sources (Qlik Sense)** screen, do the following:

    1. For **Name**, enter a name that Microsoft Purview will list as the data source.
    2. For **Server URL**, enter the URL of your Qlik Sense server. In order to use the Qlik Engine API, you need to open a WebSocket to the engine using one of the following URIs: `wss://server.domain.com:4747/app/` or `wss://server.domain.com[/virtual proxy]/app/`.
    3. Select a collection from the list.

    ![Screenshot of registering a Qlik Sense source.](media/register-scan-qlik-sense/register-sources.png)
6. Select **Register**.

## Scan

Tip

To troubleshoot any issues with scanning:

1. Confirm you have followed all **prerequisites**.
2. Review our [**scan troubleshooting documentation**](troubleshoot-connections).

Use the following steps to scan Qlik Sense server to automatically identify assets. For more information about scanning in general, see [Scans and ingestion in Microsoft Purview](data-map-scan-ingestion).

1. Go to **Sources**.
2. Select the registered Qlik Sense source.
3. Select **+ New scan**.
4. Provide the following details:

    1. **Name**: Enter a name for the scan.
    2. **Connect via integration runtime**: Choose the proper type of integration runtime. Learn more from [Choose the right integration runtime configuration for your scenario](data-map-integration-runtime-choose).
    3. **Credential**: Select the credential to connect to your data source. Follow the steps to Create Qlik Sense certificate and store it in Azure Key Vault. When creating the credential, make sure to:

        - Select **Qlik Sense certificate Authentication** while creating a credential.
        - Specify the user name.
        - Specify the user directory. See the "Users" page in the Qlik Management Console (https://your\_QPS\_server\_name/qmc).
        - For the certificate, specify the Key Vault certificate or secret name.
        - If your certificate is protected by a password and you store the certificate as a Key Vault secret, also specify the Key Vault secret name for the password.

        For more information, see [Credentials for source authentication in Microsoft Purview](data-map-data-scan-credentials).
    4. **Server data folder**: The network shared location of Qlik Sense Server's Qlik View Data (QVD) folder, e.g. `\\QlikSense\qliksenseshare`. If specified, Microsoft Purview tries to access the network shared location and scan the QVD files.
5. Click **Test connection** to validate the settings.

    ![Screenshot of setting up a Qlik Sense scan.](media/register-scan-qlik-sense/scan.png)
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

## Browse, search, and view assets

After successfully scanning your Qlik Sense server, you can [browse Unified Catalog](unified-catalog-data-assets-search#browse-the-unified-catalog) or [search Unified Catalog](unified-catalog-data-assets-search) to view the asset details.