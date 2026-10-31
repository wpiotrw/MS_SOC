---
layout: Conceptual
title: Create and manage credentials for scans in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-data-scan-credentials
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2025-10-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about the steps to create and manage credentials in Microsoft Purview Data Map.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 2e770eec-b123-a120-5362-aef92254408e
document_version_independent_id: 2e770eec-b123-a120-5362-aef92254408e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-data-scan-credentials.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-data-scan-credentials
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-data-scan-credentials.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 3cb2f1ad-d552-66d9-6763-0d6df002f68a
---

# Create and manage credentials for scans in Microsoft Purview Data Map | Microsoft Learn

This article describes how you can create credentials in Microsoft Purview Data Map. These saved credentials let you quickly reuse and apply saved authentication information to your data source scans.

## Prerequisites

- A Microsoft Azure Key Vault. To learn how to create one, see [Quickstart: Create a key vault using the Azure portal](/en-us/azure/key-vault/general/quick-create-portal).

## Introduction

A credential is authentication information that Microsoft Purview can use to authenticate to your registered data sources. A credential object can be created for various types of authentication scenarios, such as Basic Authentication requiring username/password. Credential capture specific information required to authenticate, based on the chosen type of authentication method. Credentials use your existing Key Vault secrets for retrieving sensitive authentication information during the Credential creation process.

In Microsoft Purview, there are few options to use as authentication method to scan data sources such as the following options. Learn from each [data source article](data-map-data-sources) for its supported authentication.

- Microsoft Purview system-assigned managed identity
- User-assigned managed identity (preview)
- Account Key (using Key Vault)
- SQL Authentication (using Key Vault)
- Service Principal (using Key Vault)
- Consumer Key (using Key Vault)
- And more

Before creating any credentials, consider your data source types and networking requirements to decide which authentication method you need for your scenario.

## Use Microsoft Purview system-assigned managed identity to set up scans

If you're using the Microsoft Purview system-assigned managed identity (SAMI) to set up scans, you won't need to create a credential and link your key vault to Microsoft Purview to store them. For detailed instructions on adding the Microsoft Purview SAMI to have access to scan your data sources, refer to the data source-specific authentication sections below:

- [Azure Blob Storage](register-scan-azure-blob-storage-source#authentication-for-a-scan)
- [Azure Data Lake Storage Gen1](register-scan-adls-gen1#authentication-for-a-scan)
- [Azure Data Lake Storage Gen2](register-scan-adls-gen2#authentication-for-a-scan)
- [Azure SQL Database](register-scan-azure-sql-database)
- [Azure SQL Managed Instance](register-scan-azure-sql-managed-instance#authentication-for-registration)
- [Azure Synapse Workspace](register-scan-synapse-workspace#register)
- [Azure Synapse dedicated SQL pools (formerly SQL DW)](register-scan-azure-synapse-analytics#authentication-for-registration)

## Grant Microsoft Purview access to your Azure Key Vault

To give Microsoft Purview access to your Azure Key Vault, there are two things you need to confirm:

- Firewall access to the Azure Key Vault
- Microsoft Purview permissions on the Azure Key Vault

### Firewall access to Azure Key Vault

If your Azure Key Vault has disabled public network access, you have two options to allow access for Microsoft Purview.

- Trusted Microsoft services
- Private endpoint connections

#### Trusted Microsoft services

Microsoft Purview is listed as one of [Azure Key Vault's trusted services](/en-us/azure/key-vault/general/overview-vnet-service-endpoints#trusted-services), so if public network access is disabled on your Azure Key Vault you can enable access only to trusted Microsoft services, and Microsoft Purview will be included.

You can enable this setting in your Azure Key Vault under the **Networking** tab.

At the bottom of the page, under Exception, enable the **Allow trusted Microsoft services to bypass this firewall** feature.

![Azure Key Vault networking page with the Allow trusted Microsoft services to bypass this firewall feature enabled.](media/manage-credentials/trusted-keyvault-services.png)

#### Private endpoint connections

To connect to Azure Key Vault with private endpoints, follow [Azure Key Vault's private endpoint documentation](/en-us/azure/key-vault/general/private-link-service).

Note

Private endpoint connection option is supported when using Azure integration runtime in [managed virtual network](data-governance-private-endpoints-managed-virtual-network) to scan the data sources. For self-hosted integration runtime, you need to enable trusted Microsoft services.

### Microsoft Purview permissions on the Azure Key Vault

Currently Azure Key Vault supports two permission models:

- Option 1 - Access Policies
- Option 2 - Role-based Access Control

Before assigning access to the Microsoft Purview system-assigned managed identity (SAMI), first identify your Azure Key Vault permission model from Key Vault resource **Access Policies** in the menu. Follow steps below based on relevant the permission model.

![Azure Key Vault Permission Model](media/manage-credentials/akv-permission-model.png)

#### Option 1 - Assign access using Key Vault Access Policy

Follow these steps only if permission model in your Azure Key Vault resource is set to **Vault Access Policy**:

1. Navigate to your Azure Key Vault.
2. Select the **Access policies** page.
3. Select **Add Access Policy**.

    ![Add Microsoft Purview managed identity to AKV](media/manage-credentials/add-msi-to-akv-2.png)
4. In the **Secrets permissions** dropdown, select **Get** and **List** permissions.
5. For **Select principal**, choose the Microsoft Purview system managed identity. You can search for the Microsoft Purview SAMI using either the Microsoft Purview instance name **or** the managed identity application ID. We don't currently support compound identities (managed identity name + application ID).

    ![Add access policy](media/manage-credentials/add-access-policy.png)
6. Select **Add**.
7. Select **Save** to save the Access policy.

    ![Save access policy](media/manage-credentials/save-access-policy.png)

#### Option 2 - Assign access using Key Vault Azure role-based access control

Follow these steps only if permission model in your Azure Key Vault resource is set to **Azure role-based access control**:

1. Navigate to your Azure Key Vault.
2. Select **Access Control (IAM)** from the left navigation menu.
3. Select **+ Add**.
4. Set the **Role** to **Key Vault Secrets User** and enter your Microsoft Purview account name under **Select** input box. Then, select Save to give this role assignment to your Microsoft Purview account.

    ![Azure Key Vault RBAC](media/manage-credentials/akv-add-rbac.png)

## Create Azure Key Vaults connections in your Microsoft Purview account

Before you can create a Credential, first associate one or more of your existing Azure Key Vault instances with your Microsoft Purview account.

1. If you're using the [classic Microsoft Purview portal](use-microsoft-purview-governance-portal), navigate to the **Management Center** in the studio and then navigate to **Credentials**. If you're using the new [Microsoft Purview portal](purview-portal), open **Data Map**, select **Source management**, then select **Credentials**.
2. From the **Credentials** page, select **Manage Key Vault connections**.

    ![Manage Azure Key Vault connections](media/manage-credentials/manage-kv-connections.png)
3. Select **+ New** from the Manage Key Vault connections page.
4. Provide the required information, then select **Create**.
5. Confirm that your Key Vault has been successfully associated with your Microsoft Purview account as shown in this example:

    ![View Azure Key Vault connections to confirm.](media/manage-credentials/view-kv-connections.png)

## Create a new credential

These credential types are supported in Microsoft Purview:

- Basic authentication: You add the **password** as a secret in key vault.
- Service Principal: You add the **service principal key** as a secret in key vault.
- SQL authentication: You add the **password** as a secret in key vault.
- Windows authentication: You add the **password** as a secret in key vault.
- Account Key: You add the **account key** as a secret in key vault.
- Role ARN: For an Amazon S3 data source, add your **role ARN** in AWS.
- Consumer Key: For Salesforce data sources, you can add the **password** and the **consumer secret** in key vault.
- User-assigned managed identity (preview): You can add user-assigned managed identity credentials. For more information, see the create a user-assigned managed identity section below.

For more information, see [Add a secret to Key Vault](/en-us/azure/key-vault/secrets/quick-create-portal#add-a-secret-to-key-vault) and [Create a new AWS role for Microsoft Purview](register-scan-amazon-s3#create-a-new-aws-role-for-microsoft-purview).

After storing your secrets in the key vault:

1. Provide 'Reader access' to the user at the Azure subscription level.
2. In Microsoft Purview, go to the Credentials page.
3. Create your new Credential by selecting **+ New**.
4. Provide the required information. Select the **Authentication method** and a **Key Vault connection** from which to select a secret from.
5. Once all the details have been filled in, select **Create**.
6. Verify that your new credential shows up in the list view and is ready to use.

    ![View credential](media/manage-credentials/view-credentials.png)

## Manage your key vault connections

1. Search for Key Vault connections by entering a name in the search box.
2. Delete one or more Key Vault connections by selecting the checkbox next to the Key Vault's name, then selecting **Delete**.

## Manage your credentials

1. Search/find Credentials by name.
2. Select and make updates to an existing Credential.
3. Delete one or more Credentials.

## Create a user-assigned managed identity

User-assigned managed identities (UAMI) enable Azure resources to authenticate directly with other resources using Microsoft Entra authentication, without the need to manage those credentials. They allow you to authenticate and assign access just like you would with a system assigned managed identity, Microsoft Entra user, Microsoft Entra group, or service principal. User-assigned managed identities are created as their own resource (rather than being connected to a preexisting resource). For more information about managed identities, see the [managed identities for Azure resources documentation](/en-us/azure/active-directory/managed-identities-azure-resources/overview).

The following steps explain how to create a UAMI for Microsoft Purview to use.

### Supported data sources for UAMI

- [Azure Data Lake Gen 1](register-scan-adls-gen1)
- [Azure Data Lake Gen 2](register-scan-adls-gen2)
- [Azure SQL Database](register-scan-azure-sql-database)
- [Azure SQL Managed Instance](register-scan-azure-sql-managed-instance)
- [Azure SQL Dedicated SQL pools](register-scan-azure-synapse-analytics)
- [Azure Blob Storage](register-scan-azure-blob-storage-source)

### Create a user-assigned managed identity

1. In the [Azure portal](https://portal.azure.com/), navigate to your Microsoft Purview account.
2. In the **Managed identities** section on the left menu, select the **+ Add** button to add user assigned managed identities.

    ![Screenshot showing managed identity screen in the Azure portal with user-assigned and add highlighted.](media/manage-credentials/create-new-managed-identity.png)
3. After finishing the setup, go back to your Microsoft Purview account in the Azure portal. If the managed identity is successfully deployed, you'll see the Microsoft Purview account's status as **Succeeded**.

    ![Screenshot the Microsoft Purview account in the Azure portal with Status highlighted under the overview tab and essentials menu.](media/manage-credentials/status-successful.png)
4. Once the managed identity is successfully deployed, navigate to the classic [Microsoft Purview governance portal](https://web.purview.azure.com/) by selecting **Open Microsoft Purview governance portal**.
5. In the classic [Microsoft Purview governance portal](https://web.purview.azure.com/), navigate to the Management Center in the studio and then navigate to the Credentials section.
6. Create a user-assigned managed identity by selecting **+New**.
7. Select the Managed identity authentication method from the **Authentication method** dropdown list, and make a selection from the **User assigned managed identities** dropdown list.

    Note

    If the portal was open during creation of your user assigned managed identity, you need to refresh the Microsoft Purview portal to load the settings finished in the Azure portal.
8. When done filling in all the information, select **Create**.

### Delete a user-assigned managed identity

1. In the [Azure portal](https://portal.azure.com/) navigate to your Microsoft Purview account.
2. In the **Managed identities** section on the left menu, select the identity you want to delete.
3. Select the **Remove** button.
4. Once the managed identity is successfully removed, navigate to the classic [Microsoft Purview governance portal](https://web.purview.azure.com/) by selecting **Open Microsoft Purview governance portal**.
5. Navigate to the Management Center in the studio and then navigate to the Credentials section.
6. Select the identity you want to delete, and then select the **Delete** button.

Note

If you have deleted a user-assigned managed identity in the Azure portal, you need to delete the original identity and create a new one in the Microsoft Purview portal.