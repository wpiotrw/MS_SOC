---
layout: Conceptual
title: Check Azure data sources to register and scan in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-data-sources-check-azure-readiness
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: In this tutorial, you'll verify the readiness of your Azure data sources before you register and scan them in Microsoft Purview.
ms.custom: sfi-image-nochange
locale: en-us
document_id: a9eee132-a06b-4c8c-9ffa-382c5c61fd37
document_version_independent_id: a9eee132-a06b-4c8c-9ffa-382c5c61fd37
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-data-sources-check-azure-readiness.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-data-sources-check-azure-readiness
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-data-sources-check-azure-readiness.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 8ab830cf-c851-a701-a28b-7641f76efc14
---

# Check Azure data sources to register and scan in Microsoft Purview | Microsoft Learn

To scan data sources, Microsoft Purview requires access to them. It uses credentials to obtain this access. A *credential* is the authentication information that Microsoft Purview can use to authenticate to your registered data sources. There are a few ways to set up the credentials for Microsoft Purview, including:

- The managed identity assigned to the Microsoft Purview account.
- Secrets stored in Azure Key Vault.
- Service principals.

In this two-part tutorial series, we'll help you verify and configure required Azure role assignments and network access for various Azure data sources across your Azure subscriptions at scale. You can then register and scan your Azure data sources in Microsoft Purview.

Run the [Microsoft Purview data sources readiness checklist](https://github.com/Azure/Purview-Samples/tree/master/Data-Source-Readiness) script after you deploy your Microsoft Purview account and before you register and scan your Azure data sources.

In part 1 of this tutorial series, you'll:

- Locate your data sources and prepare a list of data source subscriptions.
- Run the readiness checklist script to find any missing role-based access control (RBAC) or network configurations across your data sources in Azure.
- In the output report, review missing network configurations and role assignments required by Microsoft Purview Managed Identity (MSI).
- Share the report with data Azure subscription owners so they can take suggested actions.

## Prerequisites

- Azure subscriptions where your data sources are located. If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- A [Microsoft Purview account](create-microsoft-purview-portal).
- An Azure Key Vault resource in each subscription that has data sources like Azure SQL Database, Azure Synapse Analytics, or Azure SQL Managed Instance.
- The [Microsoft Purview data sources readiness checklist](https://github.com/Azure/Purview-Samples/tree/master/Data-Source-Readiness) script.

Note

The Microsoft Purview data sources readiness checklist is available only for Windows. This readiness checklist script is currently supported for Microsoft Purview MSI.

## Prepare Azure subscriptions list for data sources

Before running the script, create a .csv file (for example, C:\temp\Subscriptions.csv) with four columns:

| Column name | Description | Example |
| --- | --- | --- |
| `SubscriptionId` | Azure subscription IDs for your data sources. | aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e |
| `KeyVaultName` | Name of existing key vault that’s deployed in the data source subscription. | ContosoDevKeyVault |
| `SecretNameSQLUserName` | Name of an existing Azure Key Vault secret that contains a Microsoft Entra user name that can sign in to Azure Synapse, Azure SQL Database, or Azure SQL Managed Instance by using Microsoft Entra authentication. | ContosoDevSQLAdmin |
| `SecretNameSQLPassword` | Name of an existing Azure Key Vault secret that contains a Microsoft Entra user password that can sign in to Azure Synapse, Azure SQL Database, or Azure SQL Managed Instance by using Microsoft Entra authentication. | ContosoDevSQLPassword |

**Sample .csv file:**

[![Screenshot that shows a sample subscription list.](media/tutorial-data-sources-readiness/subscriptions-input.png)](media/tutorial-data-sources-readiness/subscriptions-input.png#lightbox)

Note

You can update the file name and path in the code, if you need to.

## Run the script and install the required PowerShell modules

Follow these steps to run the script from your Windows computer:

1. [Download the Microsoft Purview data sources readiness checklist](https://github.com/Azure/Purview-Samples/tree/master/Data-Source-Readiness) script to the location of your choice.
2. On your computer, enter **PowerShell** in the search box on the Windows taskbar. In the search list, select and hold (or right-click) **Windows PowerShell** and then select **Run as administrator**.
3. In the PowerShell window, enter the following command. (Replace `<path-to-script>` with the folder path of the extracted script file.)

    ```powershell
    dir -Path <path-to-script> | Unblock-File
    ```
4. Enter the following command to install the Azure cmdlets:

    ```powershell
    Install-Module -Name Az -AllowClobber -Scope CurrentUser
    ```
5. If you see the prompt *NuGet provider is required to continue*, enter **Y**, and then select **Enter**.
6. If you see the prompt *Untrusted repository*, enter **A**, and then select **Enter**.
7. Repeat the previous steps to install the `Az.Synapse` and `AzureAD` modules.

It might take up to a minute for PowerShell to install the required modules.

## Collect other data needed to run the script

Before you run the PowerShell script to verify the readiness of data source subscriptions, obtain the values of the following arguments to use in the scripts:

- `AzureDataType`: Choose any of the following options as your data-source type to check the readiness for the data type across your subscriptions:

    - `BlobStorage`
    - `AzureSQLMI`
    - `AzureSQLDB`
    - `ADLSGen2`
    - `ADLSGen1`
    - `Synapse`
    - `All`
- `PurviewAccount`: Your existing Microsoft Purview account resource name.
- `PurviewSub`: Subscription ID where the Microsoft Purview account is deployed.

## Verify your permissions

Make sure your user has the following roles and permissions:

| Role or permission | Scope |
| --- | --- |
| **Global Reader** | Microsoft Entra tenant |
| **Reader** | Azure subscriptions where your Azure data sources are located |
| **Reader** | Subscription where your Microsoft Purview account was created |
| **SQL Admin** (Microsoft Entra authentication) | Azure Synapse dedicated pools, Azure SQL Database instances, Azure SQL managed instances |
| Access to your Azure key vault | Access to get/list key vault's secret or Azure Key Vault secret user |

## Run the client-side readiness script

Run the script by completing these steps:

1. Use the following command to go to the script's folder. Replace `<path-to-script>` with the folder path of the extracted file.

    ```powershell
    cd <path-to-script>
    ```
2. Run the following command to set the execution policy for the local computer. Enter **A** for *Yes to All* when you're prompted to change the execution policy.

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy Unrestricted
    ```
3. Run the script with the following parameters. Replace the `DataType`, `PurviewName`, and `SubscriptionID` placeholders.

    ```powershell
    .\purview-data-sources-readiness-checklist.ps1 -AzureDataType <DataType> -PurviewAccount <PurviewName> -PurviewSub <SubscriptionID>
    ```

    When you run the command, a pop-up window might appear twice prompting you to sign in to Azure and Microsoft Entra ID by using your Microsoft Entra credentials.

It can take several minutes to create the report, depending on the number of Azure subscriptions and resources in the environment.

After the process completes, review the output report, which demonstrates the detected missing configurations in your Azure subscriptions or resources. The results can appear as *Passed*, *Not Passed*, or *Awareness*. You can share the results with the corresponding subscription admins in your organization so they can configure the required settings.

## More information

### What data sources are supported by the script?

Currently, the following data sources are supported by the script:

- Azure Blob Storage (BlobStorage)
- Azure Data Lake Storage Gen2 (ADLSGen2)
- Azure Data Lake Storage Gen1 (ADLSGen1)
- Azure SQL Database (AzureSQLDB)
- Azure SQL Managed Instance (AzureSQLMI)
- Azure Synapse (Synapse) dedicated pool

You can choose all or any of these data sources as the input parameter when you run the script.

### What checks are included in the results?

#### Azure Blob Storage (BlobStorage)

- RBAC. Check whether Microsoft Purview MSI is assigned the **Storage Blob Data Reader** role in each of the subscriptions below the selected scope.
- RBAC. Check whether Microsoft Purview MSI is assigned the **Reader** role on the selected scope.
- Service endpoint. Check whether service endpoint is on, and check whether **Allow trusted Microsoft services to access this storage account** is enabled.
- Networking: Check whether private endpoint is created for storage and enabled for Blob Storage.

#### Azure Data Lake Storage Gen2 (ADLSGen2)

- RBAC. Check whether Microsoft Purview MSI is assigned the **Storage Blob Data Reader** role in each of the subscriptions below the selected scope.
- RBAC. Check whether Microsoft Purview MSI is assigned the **Reader** role on the selected scope.
- Service endpoint. Check whether service endpoint is on, and check whether **Allow trusted Microsoft services to access this storage account** is enabled.
- Networking: Check whether private endpoint is created for storage and enabled for Blob Storage.

#### Azure Data Lake Storage Gen1 (ADLSGen1)

- Networking. Check whether service endpoint is on, and check whether **Allow all Azure services to access this Data Lake Storage Gen1 account** is enabled.
- Permissions. Check whether Microsoft Purview MSI has Read/Execute permissions.

#### Azure SQL Database (AzureSQLDB)

- SQL Server instances:

    - Network. Check whether public endpoint or private endpoint is enabled.
    - Firewall. Check whether **Allow Azure services and resources to access this server** is enabled.
    - Microsoft Entra administration. Check whether Azure SQL Server has Microsoft Entra authentication.
    - Microsoft Entra administration. Populate the Azure SQL Server Microsoft Entra admin user or group.
- SQL databases:

    - SQL role. Check whether Microsoft Purview MSI is assigned the **db\_datareader** role.

#### Azure SQL Managed Instance (AzureSQLMI)

- SQL Managed Instance servers:

    - Network. Check whether public endpoint or private endpoint is enabled.
    - ProxyOverride. Check whether Azure SQL Managed Instance is configured as Proxy or Redirect.
    - Networking. Check whether NSG has an inbound rule to allow AzureCloud over required ports:
        - Redirect: 1433 and 11000-11999 or
        - Proxy: 3342
    - Microsoft Entra administration. Check whether Azure SQL Server has Microsoft Entra authentication.
    - Microsoft Entra administration. Populate the Azure SQL Server Microsoft Entra admin user or group.
- SQL databases:

    - SQL role. Check whether Microsoft Purview MSI is assigned the **db\_datareader** role.

#### Azure Synapse (Synapse) dedicated pool

- RBAC. Check whether Microsoft Purview MSI is assigned the **Storage Blob Data Reader** role in each of the subscriptions below the selected scope.
- RBAC. Check whether Microsoft Purview MSI is assigned the **Reader** role on the selected scope.
- SQL Server instances (dedicated pools):

    - Network: Check whether public endpoint or private endpoint is enabled.
    - Firewall: Check whether **Allow Azure services and resources to access this server** is enabled.
    - Microsoft Entra administration: Check whether Azure SQL Server has Microsoft Entra authentication.
    - Microsoft Entra administration: Populate the Azure SQL Server Microsoft Entra admin user or group.
- SQL databases:

    - SQL role. Check whether Microsoft Purview MSI is assigned the **db\_datareader** role.