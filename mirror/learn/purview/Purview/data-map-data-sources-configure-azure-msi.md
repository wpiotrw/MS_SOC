---
layout: Conceptual
title: Configure access to data sources for Microsoft Purview MSI at scale | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-data-sources-configure-azure-msi
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
description: In this tutorial, learn how to configure Azure MSI settings on your Azure data source subscriptions.
locale: en-us
document_id: ba687b9e-f998-f2e2-1c0b-785dccc4c6b9
document_version_independent_id: ba687b9e-f998-f2e2-1c0b-785dccc4c6b9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-data-sources-configure-azure-msi.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-data-sources-configure-azure-msi
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-data-sources-configure-azure-msi.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 271e0940-e6aa-cc3b-2ce1-c327a3876c0a
---

# Configure access to data sources for Microsoft Purview MSI at scale | Microsoft Learn

To scan data sources, Microsoft Purview requires access to them. This tutorial is intended for Azure subscription owners and Microsoft Purview Data Source Administrators. It will help you identify required access and set up required authentication and network rules for Microsoft Purview across Azure data sources.

In part 2 of this tutorial series, you'll:

- Locate your data sources and prepare a list of data source subscriptions.
- Run a script to configure any missing role-based access control (RBAC) or required network configurations across your data sources in Azure.
- Review the output report.

## Prerequisites

- Azure subscriptions where your data sources are located. If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- An [Microsoft Purview account](create-microsoft-purview-portal).
- An Azure Key Vault resource in each subscription that has data sources like Azure SQL Database, Azure Synapse Analytics, or Azure SQL Managed Instance.
- The [Microsoft Purview MSI Configuration](https://github.com/Azure/Purview-Samples/tree/master/Data-Source-MSI-Configuration) script.

Note

The Microsoft Purview MSI Configuration script is available only for Windows. This script is currently supported for Microsoft Purview Managed Identity (MSI).

Important

We strongly recommend that you test and verify all the changes the script performs in your Azure environment before you deploy it into your production environment.

## Prepare Azure subscriptions list for data sources

Before you run the script, create a .csv file (for example, "C:\temp\Subscriptions.csv) with four columns:

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

1. [Download Microsoft Purview MSI Configuration](https://github.com/Azure/Purview-Samples/tree/master/Data-Source-MSI-Configuration) script to the location of your choice.
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

At a minimum, you need the following permissions to run the script in your Azure environment:

| Role | Scope | Why is it needed? |
| --- | --- | --- |
| **Global Reader** | Microsoft Entra tenant | To read Azure SQL Admin user group membership and Microsoft Purview MSI |
| **Application Administrator** | Microsoft Entra tenant | To assign the **Directory Reader** role to Azure SQL managed instances |
| **Contributor** | Subscription or resource group where your Microsoft Purview account is created | To read the Microsoft Purview account resource and create a Key Vault resource and secret |
| **Owner or User Access Administrator** | Management group or subscription where your Azure data sources are located | To assign RBAC |
| **Contributor** | Management group or subscription where your Azure data sources are located | To set up network configuration |
| **SQL Admin** (Microsoft Entra authentication) | Azure SQL Server instances or Azure SQL managed instances | To assign the **db\_datareader** role to Microsoft Purview |
| Access to your Azure key vault | Access to get/list Key Vault secret for Azure SQL Database, Azure SQL Managed Instance, or Azure Synapse authentication |  |

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
    .\purview-msi-configuration.ps1 -AzureDataType <DataType> -PurviewAccount <PurviewName> -PurviewSub <SubscriptionID>
    ```

    When you run the command, a pop-up window might appear twice prompting you to sign in to Azure and Microsoft Entra ID by using your Microsoft Entra credentials.

It can take several minutes to create the report, depending on the number of Azure subscriptions and resources in the environment.

You might be prompted to sign in to your Azure SQL Server instances if the credentials in the key vault don't match. You can provide the credentials or select **Enter** to skip the specific server.

After the process completes, view the output report to review the changes.

## More information

### What data sources are supported by the script?

Currently, the following data sources are supported by the script:

- Azure Blob Storage (BlobStorage)
- Azure Data Lake Storage Gen2 (ADLSGen2)
- Azure Data Lake Storage Gen1 (ADLSGen1)
- Azure SQL Database (AzureSQLDB)
- Azure SQL Managed Instance (AzureSQLMI)
- Azure Synapse (Synapse) dedicated pool

You can choose all or any of these data sources as input parameter when you run the script.

### What configurations are included in the script?

This script can help you automatically complete the following tasks:

#### Azure Blob Storage (BlobStorage)

- RBAC. Assign the Azure RBAC **Reader** role to Microsoft Purview MSI on the selected scope. Verify the assignment.
- RBAC. Assign the Azure RBAC **Storage Blob Data Reader** role to Microsoft Purview MSI in each of the subscriptions below the selected scope. Verify the assignments.
- Networking. Report whether private endpoint is created for storage and enabled for Blob Storage.
- Service endpoint. If private endpoint is off, check whether service endpoint is on, and enable **Allow trusted Microsoft services to access this storage account**.

#### Azure Data Lake Storage Gen2 (ADLSGen2)

- RBAC. Assign the Azure RBAC **Reader** role to Microsoft Purview MSI on the selected scope. Verify the assignment.
- RBAC. Assign the Azure RBAC **Storage Blob Data Reader** role to Microsoft Purview MSI in each of the subscriptions below the selected scope. Verify the assignments.
- Networking. Report whether private endpoint is created for storage and enabled for Blob Storage.
- Service endpoint. If private endpoint is off, check whether service endpoint is on, and enable **Allow trusted Microsoft services to access this storage account**.

#### Azure Data Lake Storage Gen1 (ADLSGen1)

- Networking. Verify that service endpoint is on, and enable **Allow all Azure services to access this Data Lake Storage Gen1 account** on Data Lake Storage.
- Permissions. Assign Read/Execute access to Microsoft Purview MSI. Verify the access.

#### Azure SQL Database (AzureSQLDB)

- SQL Server instances:

    - Network. Report whether public endpoint or private endpoint is enabled.
    - Firewall. If private endpoint is off, verify firewall rules and enable **Allow Azure services and resources to access this server**.
    - Microsoft Entra administration. Enable Microsoft Entra authentication for Azure SQL Database.
- SQL databases:

    - SQL role. Assign the **db\_datareader** role to Microsoft Purview MSI.

#### Azure SQL Managed Instance (AzureSQLMI)

- SQL Managed Instance servers:

    - Network. Verify that public endpoint or private endpoint is on. Report if public endpoint is off.
    - ProxyOverride. Verify that Azure SQL Managed Instance is configured as Proxy or Redirect.
    - Networking. Update NSG rules to allow AzureCloud inbound access to SQL Server instances over required ports:

        - Redirect: 1433 and 11000-11999

        or

        - Proxy: 3342

        Verify this access.
    - Microsoft Entra administration. Enable Microsoft Entra authentication for Azure SQL Managed Instance.
- SQL databases:

    - SQL role. Assign the **db\_datareader** role to Microsoft Purview MSI.

#### Azure Synapse (Synapse) dedicated pool

- RBAC. Assign the Azure RBAC **Reader** role to Microsoft Purview MSI on the selected scope. Verify the assignment.
- RBAC. Assign the Azure RBAC **Storage Blob Data Reader** role to Microsoft Purview MSI in each of the subscriptions below the selected scope. Verify the assignments.
- SQL Server instances (dedicated pools):

    - Network. Report whether public endpoint or private endpoint is on.
    - Firewall. If private endpoint is off, verify firewall rules and enable **Allow Azure services and resources to access this server**.
    - Microsoft Entra administration. Enable Microsoft Entra authentication for Azure SQL Database.
- SQL databases:

    - SQL role. Assign the **db\_datareader** role to Microsoft Purview MSI.