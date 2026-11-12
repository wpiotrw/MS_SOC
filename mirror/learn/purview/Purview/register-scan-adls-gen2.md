---
layout: Conceptual
title: Discover and govern Azure Data Lake Storage (ADLS) Gen2 in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-adls-gen2
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
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand the process to register an Azure Data Lake Storage Gen2 data source in Microsoft Purview, with instructions to authenticate and interact with the Azure Data Lake Storage Gen2 source.
ms.custom: sfi-image-nochange, msecd-doc-authoring-1030
locale: en-us
document_id: c0948062-c921-c19d-b804-dd878ed0ffb5
document_version_independent_id: c0948062-c921-c19d-b804-dd878ed0ffb5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-adls-gen2.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-adls-gen2
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-adls-gen2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5c1f3bfc-fced-4ad1-b4e6-b7200832734d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/5017978e-5a12-4c31-bdfd-1880eb1a780b
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: be9555b3-c5c0-1a81-030e-da93cf2345ec
---

# Discover and govern Azure Data Lake Storage (ADLS) Gen2 in Microsoft Purview | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines the process to register and govern an Azure Data Lake Storage (ADLS Gen2) data source in Microsoft Purview, including instructions to authenticate and interact with the ADLS Gen2 source.

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

When scanning Azure Data Lake Storage Gen2 source, Microsoft Purview supports extracting technical metadata including:

- Storage account
- Data Lake Storage Gen2 Service
- File system (container)
- Folders
- Files
- Resource sets

When setting up scan, you can choose to scan the entire ADLS Gen2 or selective folders. Learn about the supported file format [here](data-map-data-sources#file-types-supported-for-scanning).

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You'll need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.
- You need to have at least [Reader permission on the ADLS Gen 2 account](/en-us/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac) to be able to register it.

## Register

This section will enable you to register the ADLS Gen2 data source for scan and data share in Purview.

### Prerequisites for register

- You'll need to be a Data Source Admin and one of the other Purview roles (for example, Data Reader or Data Share Contributor) to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

### Steps to register

It's important to register the data source in Microsoft Purview prior to setting up a scan for the data source.

1. Go to the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Select the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Navigate to the **Data Map --&gt; Sources**

    ![Screenshot that shows the link to open Microsoft Purview governance portal](media/register-scan-adls-gen2/register-adls-gen2-open-purview-studio.png)

    ![Screenshot that navigates to the Sources link in the Data Map](media/register-scan-adls-gen2/register-adls-gen2-sources.png)
3. Create the [Collection hierarchy](data-map-collections-create-classic) using the **Collections** menu and assign permissions to individual subcollections, as required

    ![Screenshot that shows the collection menu to create collection hierarchy](media/register-scan-adls-gen2/register-adls-gen2-collections.png)
4. Navigate to the appropriate collection under the **Sources** menu and select the **Register** icon to register a new ADLS Gen2 data source

    ![Screenshot that shows the collection used to register the data source](media/register-scan-adls-gen2/register-adls-gen2-register-source.png)
5. Select the **Azure Data Lake Storage Gen2** data source and select **Continue**

    ![Screenshot that allows selection of the data source](media/register-scan-adls-gen2/register-adls-gen2-select-data-source.png)
6. Provide a suitable **Name** for the data source, select the relevant **Azure subscription**, existing **Data Lake Store account name** and the **collection** and select **Apply**. Leave the **Data Policy Enforcement** toggle on the **disabled** position until you have a chance to carefully go over this [document](how-to-policies-data-owner-storage).

    ![Screenshot that shows the details to be entered in order to register the data source](media/register-scan-adls-gen2/register-adls-gen2-data-source-details.png)
7. The ADLS Gen2 storage account will be shown under the selected Collection

    ![Screenshot that shows the data source mapped to the collection to initiate scanning](media/register-scan-adls-gen2/register-adls-gen2-data-source-collection.png)

## Scan

Tip

To troubleshoot any issues with scanning:

1. Confirm you have properly set up **authentication for scanning**
2. Review our [**scan troubleshooting documentation**](troubleshoot-connections).

### Authentication for a scan

Your Azure network may allow for communications between your Azure resources, but if you've set up firewalls, private endpoints, or virtual networks within Azure, you'll need to follow one of these configurations below.

| Networking constraints | Integration runtime type | Available credential types |
| --- | --- | --- |
| No private endpoints or firewalls | Azure IR | Managed identity (Recommended), service principal, or account key |
| Firewall enabled but no private endpoints | Azure IR | Managed identity |
| Private endpoints enabled | \*Self-Hosted IR | Service principal, account key |

Important

1. \*To use a self-hosted integration runtime, you'll first need to [choose the right one for your scenario](data-map-integration-runtime-choose), create one, and confirm your [network settings for Microsoft Purview](data-gov-classic-private-link).
2. If you use the Self-Hosted Integration runtime to scan parquet files, you need to install the **64-bit JRE 8 (Java Runtime Environment) or OpenJDK** on your IR machine. You can check our [Java Runtime Environment installation guide](data-map-integration-runtime-self-hosted#java-runtime-environment-installation).

# [System or user assigned managed identity](#tab/MI)
#### Using a system or user assigned managed identity for scanning

There are two types of managed identity you can use:

- **System-assigned managed identity (Recommended)** - As soon as the Microsoft Purview Account is created, a system-assigned managed identity (SAMI) is created automatically in Microsoft Entra tenant. Depending on the type of resource, specific RBAC role assignments are required for the Microsoft Purview system-assigned managed identity (SAMI) to perform the scans.
- **User-assigned managed identity** (preview) - Similar to a system managed identity, a user-assigned managed identity (UAMI) is a credential resource that can be used to allow Microsoft Purview to authenticate against Microsoft Entra ID. For more information, you can see our [User-assigned managed identity guide](data-map-data-scan-credentials#create-a-user-assigned-managed-identity).

It's important to give your Microsoft Purview account or user-assigned managed identity (UAMI) the permission to scan the ADLS Gen2 data source. You can add your Microsoft Purview account's system-assigned managed identity (which has the same name as your Microsoft Purview account) or UAMI at the Subscription, Resource Group, or Resource level, depending on what level scan permissions are needed.

Note

You need to be an owner of the subscription to be able to add a managed identity on an Azure resource.

1. From the [Azure portal](https://portal.azure.com), find either the subscription, resource group, or resource (for example, an Azure Data Lake Storage Gen2 storage account) that you would like to allow the catalog to scan.

    ![Screenshot that shows the storage account](media/register-scan-adls-gen2/register-adls-gen2-storage-acct.png)
2. Select **Access Control (IAM)** in the left navigation and then select **+ Add** --&gt; **Add role assignment**

    ![Screenshot that shows the access control for the storage account](media/register-scan-adls-gen2/register-adls-gen2-access-control.png)
3. Set the **Role** to **Storage Blob Data Reader** and enter your *Microsoft Purview account name* or *[user-assigned managed identity](data-map-data-scan-credentials#create-a-user-assigned-managed-identity)* under the **Select** input box. Then, select **Save** to give this role assignment to your Microsoft Purview account.

    ![Screenshot that shows the details to assign permissions for the Microsoft Purview account](media/register-scan-adls-gen2/register-adls-gen2-assign-permissions.png)

    Note

    For more details, please see steps in [Authorize access to blobs and queues using Microsoft Entra ID](/en-us/azure/storage/blobs/authorize-access-azure-active-directory)

    Note

    If you have firewall enabled for the storage account, you must use **managed identity** authentication method when setting up a scan.
4. Go into your ADLS Gen2 storage account in [Azure portal](https://portal.azure.com)
5. Navigate to **Security + networking &gt; Networking**

    ![Screenshot that shows the details to provide firewall access](media/register-scan-adls-gen2/register-adls-gen2-networking.png)
6. Choose **Selected Networks** under **Allow access from**

    ![Screenshot that shows the details to allow access to selected networks](media/register-scan-adls-gen2/register-adls-gen2-network-access.png)
7. In the **Exceptions** section, select **Allow trusted Microsoft services to access this storage account** and hit **Save**

    ![Screenshot that shows the exceptions to allow trusted Microsoft services to access the storage account](media/register-scan-adls-gen2/register-adls-gen2-permission-microsoft-services.png)

# [Account Key](#tab/AK)
#### Using Account Key for scanning

Note

If you use this option, you need to deploy an *Azure key vault* resource in your subscription and [assign *Microsoft Purview account’s* System Assigned Managed Identity (SAMI) required access permission to secrets inside *Azure key vault*.](data-map-data-scan-credentials#microsoft-purview-permissions-on-the-azure-key-vault)

When authentication method selected is **Account Key**, you need to get your access key and store in the key vault:

1. Navigate to your ADLS Gen2 storage account
2. Select **Security + networking &gt; Access keys**

    ![Screenshot that shows the access keys in the storage account](media/register-scan-adls-gen2/register-adls-gen2-access-keys.png)
3. Copy your *key* and save it separately for the next steps

    ![Screenshot that shows the access keys to be copied](media/register-scan-adls-gen2/register-adls-gen2-key.png)
4. Navigate to your key vault

    ![Screenshot that shows the key vault](media/register-scan-adls-gen2/register-adls-gen2-key-vault.png)
5. Select **Settings &gt; Secrets** and select **+ Generate/Import**![Screenshot that shows the key vault option to generate a secret](media/register-scan-adls-gen2/register-adls-gen2-generate-secret.png)
6. Enter the **Name** and **Value** as the *key* from your storage account

    ![Screenshot that shows the key vault option to enter the secret values](media/register-scan-adls-gen2/register-adls-gen2-secret-values.png)
7. Select **Create** to complete

    ![Screenshot that shows the key vault option to create a secret](media/register-scan-adls-gen2/register-adls-gen2-secret.png)
8. If your key vault isn't connected to Microsoft Purview yet, you'll need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
9. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) using the key to set up your scan

# [Service Principal](#tab/SP)
#### Using Service Principal for scanning

##### Creating a new service principal

If you need to [Create a new service principal](data-map-service-principal), it's required to register an application in your Microsoft Entra tenant and provide access to Service Principal in your data sources. Your Microsoft Entra Application Administrator can perform this operation.

##### Getting the Service Principal's Application ID

1. Copy the **Application (client) ID** present in the **Overview** of the [*Service Principal*](data-map-service-principal) already created

    ![Screenshot that shows the Application (client) ID for the Service Principal](media/register-scan-adls-gen2/register-adls-gen2-sp-appln-id.png)

##### Granting the Service Principal access to your ADLS Gen2 account

It's important to give your service principal the permission to scan the ADLS Gen2 data source. You can add access for the service principal at the Subscription, Resource Group, or Resource level, depending on what level scan permissions are needed.

Note

You need to be an owner of the subscription to be able to add a service principal on an Azure resource.

1. From the [Azure portal](https://portal.azure.com), find either the subscription, resource group, or resource (for example, an Azure Data Lake Storage Gen2 storage account) that you would like to allow the catalog to scan.

    ![Screenshot that shows the storage account](media/register-scan-adls-gen2/register-adls-gen2-storage-acct.png)
2. Select **Access Control (IAM)** in the left navigation and then select **+ Add** --&gt; **Add role assignment**

    ![Screenshot that shows the access control for the storage account](media/register-scan-adls-gen2/register-adls-gen2-access-control.png)
3. Set the **Role** to **Storage Blob Data Reader** and enter your *service principal* under **Select** input box. Then, select **Save** to give this role assignment to your Microsoft Purview account.

    ![Screenshot that shows the details to provide storage account permissions to the service principal](media/register-scan-adls-gen2/register-adls-gen2-sp-permission.png)

---

### Create the scan

1. Open your **Microsoft Purview account** and select the **Open Microsoft Purview governance portal**
2. Navigate to the **Data map** --&gt; **Sources** to view the collection hierarchy
3. Select the **New Scan** icon under the **ADLS Gen2 data source** registered earlier

    ![Screenshot that shows the screen to create a new scan](media/register-scan-adls-gen2/register-adls-gen2-new-scan.png)
4. Choose either the Azure integration runtime if your source is publicly accessible, a [managed virtual network integration runtime](data-governance-private-endpoints-managed-virtual-network) if using a managed virtual network, or a self-hosted integration runtime if your source is in a private virtual network. For more information about which integration runtime to use, see the [choose the right integration runtime configuration article.](data-map-integration-runtime-choose#choose-the-right-integration-runtime)

# [System or user assigned managed identity](#tab/MI)
#### If using a system or user assigned managed identity

1. Provide a **Name** for the scan, select the system-assigned or user-assigned managed identity under **Credential**, choose the appropriate collection for the scan, and select **Test connection**. On a successful connection, select **Continue**.

    ![Screenshot that shows the managed identity option to run the scan](media/register-scan-adls-gen2/register-adls-gen2-managed-identity.png)

# [Account Key](#tab/AK)
#### If using Account Key

1. Provide a **Name** for the scan, select the Azure IR or your Self-Hosted IR depending on your configuration, choose the appropriate collection for the scan, and select **+ New** under credential.
2. Select **Account Key** as the authentication method, then select the appropriate **Key vault connection**, and provide the name of the secret you used to store the account key. Then select **Create**

    ![Screenshot that shows the Account Key option for scanning](media/register-scan-adls-gen2/register-adls-gen2-acct-key.png)
3. Select **Test connection**. On a successful connection, select **Continue**

# [Service Principal](#tab/SP)
#### If using Service Principal

1. Provide a **Name** for the scan, select the Azure IR or your Self-Hosted IR depending on your configuration, choose the appropriate collection for the scan, and select the **+ New** under **Credential**

    ![Screenshot that shows the option for service principal to enable scanning](media/register-scan-adls-gen2/register-adls-gen2-sp-option.png)
2. Select the appropriate **Key vault connection** and the **Secret name** that was used while creating the *Service Principal*. The **Service Principal ID** is the **Application (client) ID** copied earlier.

    ![Screenshot that shows the service principal option](media/register-scan-adls-gen2/register-adls-gen2-service-principal-option.png)
3. Select **Test connection**. On a successful connection, select **Continue**

---

### Scope and run the scan

1. You can scope your scan to specific folders and subfolders by choosing the appropriate items in the list.

    ![Scope your scan](media/register-scan-adls-gen2/register-adls-gen2-scope-scan.png)
2. Then select a scan rule set. You can choose between the system default, existing custom rule sets, or create a new rule set inline.

    ![Scan rule set](media/register-scan-adls-gen2/register-adls-gen2-scan-rule-set.png)
3. If creating a new *scan rule set*, select the **file types** to be included in the scan rule.

    ![Scan rule set file types](media/register-scan-adls-gen2/register-adls-gen2-file-types.png)
4. You can select the **classification rules** to be included in the scan rule

    ![Scan rule set classification rules](media/register-scan-adls-gen2/register-adls-gen2-classification rules.png)

    ![Scan rule set selection](media/register-scan-adls-gen2/register-adls-gen2-select-scan-rule-set.png)
5. Choose your scan trigger. You can set up a schedule or run the scan once.

    ![scan trigger](media/register-scan-adls-gen2/register-adls-gen2-scan-trigger.png)
6. Review your scan and select **Save and run**.

    ![review scan](media/register-scan-adls-gen2/register-adls-gen2-review-scan.png)

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

## Data sharing

Microsoft Purview Data Sharing (preview) enables sharing of data in-place from ADLS Gen2 to ADLS Gen2. This section provides details about the ADLS Gen2 specific requirements for sharing and receiving data in-place. Refer to [How to share data](how-to-share-data) and [How to receive share](how-to-receive-share) for step by step guide on how to use data sharing.

### Storage accounts supported for in-place data sharing

The following storage accounts are supported for in-place data sharing:

- Regions: Canada Central, Canada East, UK South, UK West, Australia East, Japan East, Korea South, and South Africa North
- Redundancy options: LRS, GRS, RA-GRS
- Tiers: Hot, Cool

Only use storage accounts without production workload for the preview.

Note

Source and target storage accounts must be in the same region as each other. They don't need to be in the same region as the Microsoft Purview account.

### Storage account permissions required to share data

To add or update a storage account asset to a share, you need ONE of the following permissions:

- **Microsoft.Authorization/roleAssignments/write** - This permission is available in the *Owner* role.
- **Microsoft.Storage/storageAccounts/blobServices/containers/blobs/modifyPermissions/** - This permission is available in the *Blob Storage Data Owner* role.

### Storage account permissions required to receive shared data

To map a storage account asset in a received share, you need ONE of the following permissions:

- **Microsoft.Storage/storageAccounts/write** - This permission is available in the *Contributor* and *Owner* role.
- **Microsoft.Storage/storageAccounts/blobServices/containers/write** - This permission is available in the *Contributor*, *Owner*, *Storage Blob Data Contributor* and *Storage Blob Data Owner* role.

### Update shared data in source storage account

Updates you make to shared files or data in the shared folder from source storage account will be made available to recipient in target storage account in near real time. When you delete subfolder or files within the shared folder, they'll disappear for recipient. To delete the shared folder, file or parent folders or containers, you need to first revoke access to all your shares from the source storage account.

### Access shared data in target storage account

The target storage account enables recipient to access the shared data read-only in near real time. You can connect analytics tools such as Synapse Workspace and Databricks to the shared data to perform analytics. Cost of accessing the shared data is charged to the target storage account.

### Service limit

Source storage account can support up to 20 targets, and target storage account can support up to 100 sources. If you require an increase in limit, contact Support.

## Policies

The following types of policies are supported on this data resource from Microsoft Purview:

- [Data owner policies](concept-policies-data-owner) - a set of policy statements that allow you to grant users and groups access to data sources.
- [Self-service access policies](concept-self-service-data-access-policy) - policy that allows users to request access to data sources registered to Microsoft Purview.
- [Protection policies](data-gov-protection-policy-azure-sources) - denies access to data tagged with sensitivity labels to all users except those specified by the policy.

### Access policy pre-requisites on Azure Storage accounts

#### Region support

- All [Microsoft Purview regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=purview) are supported.
- Storage accounts in the following regions are supported without the need for additional configuration. However, zone-redundant storage (ZRS) accounts are not supported.
    - Australia Central
    - Australia East
    - Australia Southeast
    - Brazil South
    - Canada Central
    - Canada East
    - Central India
    - Central US
    - East Asia
    - East US 2
    - East US
    - France Central
    - Germany West Central
    - Japan East
    - Japan West
    - Korea Central
    - North Central US
    - North Europe
    - Norway East
    - Poland Central
    - Qatar Central
    - South Central US
    - South Africa North
    - Southeast Asia
    - South India
    - Sweden Central
    - Switzerland North
    - West Central US
    - West Europe
    - West US
    - West US 2
    - West US 3
    - UAE North
    - UK South
    - UK West
- Storage accounts in other regions in Public Cloud are supported after setting feature flag *AllowPurviewPolicyEnforcement*, as outlined in the next section. Newly created ZRS Storage accounts are supported, if created after setting the feature flag *AllowPurviewPolicyEnforcement*.

If needed, you can create a new Storage account by [following this guide](/en-us/azure/storage/common/storage-account-create).

#### Configure the subscription where the Azure Storage account resides for policies from Microsoft Purview

This step is only necessary in certain regions (see prior section). To enable Microsoft Purview to manage policies for one or more Azure Storage accounts, execute the following PowerShell commands in the subscription where you'll deploy your Azure Storage account. These PowerShell commands will enable Microsoft Purview to manage policies on all Azure Storage accounts in that subscription.

If you’re executing these commands locally, be sure to run PowerShell as an administrator. Alternatively, you can use the [Azure Cloud Shell](/en-us/azure/cloud-shell/overview) in the Azure portal: https://shell.azure.com.

```powershell
# Install the Az module
Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force
# Login into the subscription
Connect-AzAccount -Subscription <SubscriptionID>
# Register the feature
Register-AzProviderFeature -FeatureName AllowPurviewPolicyEnforcement -ProviderNamespace Microsoft.Storage
```

If the output of the last command shows *RegistrationState* as *Registered*, then your subscription is enabled for access policies. If the output is *Registering*, wait at least 10 minutes, and then retry the command. **Do not continue unless the RegistrationState shows as *Registered***.

### Configure the Microsoft Purview account for policies

#### Register the data source in Microsoft Purview

Before a policy can be created in Microsoft Purview for a data resource, you must register that data resource in Microsoft Purview Studio. You will find the instructions related to registering the data resource later in this guide.

Note

Microsoft Purview policies rely on the data resource ARM path. If a data resource is moved to a new resource group or subscription it will need to be de-registered and then registered again in Microsoft Purview.

#### Configure permissions to enable Data policy enforcement on the data source

Once a resource is registered, but before a policy can be created in Microsoft Purview for that resource, you must configure permissions. A set of permissions are needed to enable the **Data policy enforcement**. This applies to data sources, resource groups, or subscriptions. To enable *Data policy enforcement*, you must have *both* specific Identity and Access Management (IAM) privileges on the resource as well as specific Microsoft Purview privileges:

- You must have *either one* of the following IAM role combinations on the resource's Azure Resource Manager path or any parent of it (that is, using IAM permission inheritance):

    - IAM Owner
    - Both IAM Contributor and IAM User Access Administrator

    To configure Azure role-based access control (RBAC) permissions, follow [this guide](/en-us/azure/role-based-access-control/check-access). The following screenshot shows how to access the **Access Control** section in the Azure portal for the data resource to add a role assignment.

    [![Screenshot that shows the section in the Azure portal for adding a role assignment.](media/how-to-policies-data-owner-authoring-generic/assign-iam-permissions.png)](media/how-to-policies-data-owner-authoring-generic/assign-iam-permissions.png#lightbox)

    Note

    The *IAM Owner* role for a data resource can be inherited from a parent resource group, a subscription, or a subscription management group. Check which Microsoft Entra users, groups, and service principals hold or are inheriting the *IAM Owner* role for the resource.
- You also need to have the Microsoft Purview *Data source admin* role for the collection or a parent collection (if inheritance is enabled). For more information, see the [guide on managing Microsoft Purview role assignments](data-gov-classic-permissions#assign-permissions-to-your-users).

    The following screenshot shows how to assign the *Data source admin* role at the root collection level.

    [![Screenshot that shows selections for assigning the Data source admin role at the root collection level.](media/how-to-policies-data-owner-authoring-generic/assign-purview-permissions.png)](media/how-to-policies-data-owner-authoring-generic/assign-purview-permissions.png#lightbox)

#### Configure Microsoft Purview permissions to create, update, or delete access policies

To create, update or delete policies, you need to get the *Policy author* role in Microsoft Purview at *root collection level*:

- The *Policy author* role can create, update, and delete DevOps and Data Owner policies.
- The *Policy author* role can delete self-service access policies.

For more information about managing Microsoft Purview role assignments, see [Create and manage collections in the Microsoft Purview Data Map](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Note

Policy author role must be configured at the root collection level.

In addition, to easily search Microsoft Entra users or groups when creating or updating the subject of a policy, you can greatly benefit from getting the [Directory Readers](/en-us/azure/active-directory/roles/permissions-reference#directory-readers) permission in Microsoft Entra ID. This is a common permission for users in an Azure tenant. Without the Directory Reader permission, the Policy Author will have to type the complete username or email for all the principals included in the subject of a data policy.

#### Configure Microsoft Purview permissions for publishing Data Owner policies

Data Owner policies allow for checks and balances if you assign the Microsoft Purview *Policy author* and *Data source admin* roles to different people in the organization. Before a Data owner policy takes effect, a second person (*Data source admin*) must review it and explicitly approve it by publishing it. This does not apply to DevOps or Self-service access policies as publishing is automatic for them when those policies are created or updated.

To publish a Data owner policy you need to get the *Data source admin* role in Microsoft Purview at *root collection level*.

For more information about managing Microsoft Purview role assignments, see [Create and manage collections in the Microsoft Purview Data Map](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Note

To publish Data owner policies, the Data source admin role must be configured at the root collection level.

#### Delegate access provisioning responsibility to roles in Microsoft Purview

After a resource has been enabled for **Data policy enforcement**, any Microsoft Purview user with the *Policy author* role at the root collection level can provision access to that data source from Microsoft Purview.

Note

Any Microsoft Purview root *Collection admin* can assign new users to root *Policy author* roles. Any *Collection admin* can assign new users to a *Data source admin* role under the collection. Minimize and carefully vet the users who hold Microsoft Purview *Collection admin*, *Data source admin*, or *Policy author* roles.

If a Microsoft Purview account with published policies is deleted, such policies will stop being enforced within an amount of time that depends on the specific data source. This change can have implications on both security and data access availability. The Contributor and Owner roles in IAM can delete Microsoft Purview accounts. You can check these permissions by going to the **Access control (IAM)** section for your Microsoft Purview account and selecting **Role Assignments**. You can also use a lock to prevent the Microsoft Purview account from being deleted through [Resource Manager locks](/en-us/azure/azure-resource-manager/management/lock-resources).

### Register the data source in Microsoft Purview for Data Policy Enforcement

The Azure Storage resource needs to be registered first with Microsoft Purview before you can create access policies. To register your resource, follow the **Prerequisites** and **Register** sections of this guide:

- [Register Azure Data Lake Storage (ADLS) Gen2 in Microsoft Purview](register-scan-adls-gen2#prerequisites)

After you've registered the data source, you'll need to enable Data Policy Enforcement. This is a pre-requisite before you can create policies on the data source. Data Policy Enforcement can impact the security of your data, as it delegates to certain Microsoft Purview roles managing access to the data sources. **Go through the secure practices related to Data Policy Enforcement in this guide**: [How to enable Data Policy Enforcement](how-to-enable-data-policy-enforcement)

Once your data source has the **Data Policy Enforcement** option set to **Enabled**, it will look like this screenshot: ![Screenshot shows how to register a data source for policy with the option Data policy enforcement set to enable](media/how-to-policies-data-owner-storage/enable-policy-enforcement-storage.png)

### Create a policy

To create an access policy for Azure Data Lake Storage Gen2, follow this guide:

- [Provision read/modify access on a single storage account](how-to-policies-data-owner-storage#create-and-publish-a-data-owner-policy)

To create policies that cover all data sources inside a resource group or Azure subscription you can refer to [this section](register-scan-azure-multiple-sources#policies).

### Protection policy

Protection access control policies (protection policies) enable organizations to automatically protect sensitive data across data sources. Microsoft Purview already scans data assets and identifies sensitive data elements, and this new feature allows you to automatically restrict access to that data using sensitivity labels from Microsoft Purview Information Protection.

Follow this documentation to create a protection policy: [How to create a Microsoft Purview Information Protection policy.](data-gov-protection-policy#create-protection-policy)