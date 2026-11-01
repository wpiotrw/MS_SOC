---
layout: Conceptual
title: Connect to and manage Azure SQL Managed Instance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-sql-managed-instance
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to Azure SQL Managed Instance in Microsoft Purview, and how to use Microsoft Purview's features to scan and manage your Azure SQL Managed Instance source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: shjia
ms.service: purview
ms.subservice: purview-data-map
ms.topic: tutorial
ms.date: 2024-06-06T00:00:00.0000000Z
ms.custom: template-how-to, ignite-fall-2021
locale: en-us
document_id: 308ca7da-7174-f911-fa30-5f1322a56a40
document_version_independent_id: 308ca7da-7174-f911-fa30-5f1322a56a40
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-sql-managed-instance.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-sql-managed-instance
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-sql-managed-instance.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/768b4698-4866-4946-8059-08ef5f568fcb
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/48a90357-592c-4146-a92b-4c2dcc560cbf
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 04c22821-9259-ff1e-40ce-fd117638502f
---

# Connect to and manage Azure SQL Managed Instance | Microsoft Learn

This article outlines how to register and Azure SQL Managed Instance, as well as how to authenticate and interact with the Azure SQL Managed Instance in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You'll need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.
- [Configure public endpoint in Azure SQL Managed Instance](/en-us/azure/azure-sql/managed-instance/public-endpoint-configure)

    Note

    We now support scanning Azure SQL Managed Instances over the private connection using Microsoft Purview ingestion private endpoints and a self-hosted integration runtime VM. For more information related to prerequisites, see [Connect to your Microsoft Purview and scan data sources privately and securely](data-gov-classic-private-link-end-to-end)

## Register

This section describes how to register an Azure SQL Managed Instance in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Authentication for registration

If you need to create new authentication, you need to [authorize database access to SQL Database SQL Managed Instance](/en-us/azure/azure-sql/database/logins-create-manage). There are three authentication methods that Microsoft Purview supports today:

- System or user assigned managed identity
- Service Principal
- SQL authentication

#### System or user assigned managed identity to register

Note

If you're using Private Endpoints to connect to Microsoft Purview, managed identity isn't supported.

You can use either your Microsoft Purview system-assigned managed identity (SAMI), or a [user-assigned managed identity](data-map-data-scan-credentials#create-a-user-assigned-managed-identity) (UAMI) to authenticate. Both options allow you to assign authentication directly to Microsoft Purview, like you would for any other user, group, or service principal. The Microsoft Purview system-assigned managed identity is created automatically when the account is created and has the same name as your Microsoft Purview account. A user-assigned managed identity is a resource that can be created independently. To create one, you can follow our [user-assigned managed identity guide](data-map-data-scan-credentials#create-a-user-assigned-managed-identity).

You can find your managed identity Object ID in the Azure portal by following these steps:

For Microsoft Purview account’s system-assigned managed identity:

1. Open the Azure portal, and navigate to your Microsoft Purview account.
2. Select the **Properties** tab on the left side menu.
3. Select the **Managed identity object ID** value and copy it.

For user-assigned managed identity (preview):

1. Open the Azure portal, and navigate to your Microsoft Purview account.
2. Select the Managed identities tab on the left side menu
3. Select the user assigned managed identities, select the intended identity to view the details.
4. The object (principal) ID is displayed in the overview essential section.

Either managed identity will need permission to get metadata for the database, schemas and tables, and to query the tables for classification.

- Create a Microsoft Entra user in Azure SQL Managed Instance by following the prerequisites and tutorial on [Create contained users mapped to Microsoft Entra identities](/en-us/azure/azure-sql/database/authentication-aad-configure?tabs=azure-powershell#create-contained-users-mapped-to-azure-ad-identities)
- Assign `db_datareader` permission to the identity.

#### Service Principal to register

There are several steps to allow Microsoft Purview to use service principal to scan your Azure SQL Managed Instance.

#### Create or use an existing service principal

To use a service principal, you can use an existing one or create a new one. If you're going to use an existing service principal, skip to the next step. If you have to create a new Service Principal, follow these steps:

1. Navigate to the [Azure portal](https://portal.azure.com).
2. Select **Microsoft Entra ID** from the left-hand side menu.
3. Select **App registrations**.
4. Select **+ New application registration**.
5. Enter a name for the **application** (the service principal name).
6. Select **Accounts in this organizational directory only**.
7. For Redirect URI, select **Web** and enter any URL you want; it doesn't have to be real or work.
8. Then select **Register**.

#### Configure Microsoft Entra authentication in the database account

The service principal must have permission to get metadata for the database, schemas, and tables. It must also be able to query the tables to sample for classification.

- [Configure and manage Microsoft Entra authentication with Azure SQL](/en-us/azure/azure-sql/database/authentication-aad-configure)
- Create a Microsoft Entra user in Azure SQL Managed Instance by following the prerequisites and tutorial on [Create contained users mapped to Microsoft Entra identities](/en-us/azure/azure-sql/database/authentication-aad-configure?tabs=azure-powershell#create-contained-users-mapped-to-azure-ad-identities)
- Assign `db_datareader` permission to the identity.

#### Add service principal to key vault and Microsoft Purview's credential

It's required to get the service principal's application ID and secret:

1. Navigate to your Service Principal in the [Azure portal](https://portal.azure.com)
2. Copy the values the **Application (client) ID** from **Overview** and **Client secret** from **Certificates & secrets**.
3. Navigate to your key vault
4. Select **Settings &gt; Secrets**
5. Select **+ Generate/Import** and enter the **Name** of your choice and **Value** as the **Client secret** from your Service Principal
6. Select **Create** to complete
7. If your key vault isn't connected to Microsoft Purview yet, you'll need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
8. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) using the Service Principal to set up your scan.

#### SQL authentication to register

Note

Only the server-level principal login (created by the provisioning process) or members of the `loginmanager` database role in the master database can create new logins. It takes about **15 minutes** after granting permission, the Microsoft Purview account should have the appropriate permissions to be able to scan the resource(s).

You can follow the instructions in [CREATE LOGIN](/en-us/sql/t-sql/statements/create-login-transact-sql?view=azuresqldb-current&amp;preserve-view=true#examples-1) to create a login for Azure SQL Managed Instance if you don't have this login available. You'll need **username** and **password** for the next steps.

1. Navigate to your key vault in the Azure portal
2. Select **Settings &gt; Secrets**
3. Select **+ Generate/Import** and enter the **Name** and **Value** as the *password* from your Azure SQL Managed Instance
4. Select **Create** to complete
5. If your key vault isn't connected to Microsoft Purview yet, you'll need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
6. Finally, [create a new credential](data-map-data-scan-credentials#create-a-new-credential) using the **username** and **password** to set up your scan.

### Steps to register

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Select the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Navigate to the **Data Map**.
3. Select **Register**
4. Select **Azure SQL Managed Instance** and then **Continue**.
5. Select **From Azure subscription**, select the appropriate subscription from the **Azure subscription** drop-down box and the appropriate server from the **Server name** drop-down box.
6. Provide the **public endpoint fully qualified domain name** and **port number**. Then select **Register** to register the data source.

    ![Screenshot of register sources screen, with Name, subscription, server name, and endpoint filled out.](media/register-scan-azure-sql-managed-instance/add-azure-sql-database-managed-instance.png)

    For Example: `foobar.public.123.database.windows.net,3342`

## Scan

Follow the steps below to scan an Azure SQL Managed Instance to automatically identify assets and classify your data. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Create and run scan

To create and run a new scan, complete the following steps:

1. Select the **Data Map** tab on the left pane in the Microsoft Purview governance portal.
2. Select the Azure SQL Managed Instance source that you registered.
3. Select **New scan**
4. Choose either the Azure integration runtime if your source is publicly accessible, a [managed virtual network integration runtime](data-governance-private-endpoints-managed-virtual-network) if using a managed virtual network, or a standard or kubernetes supported self-hosted integration runtime if your source is in a private virtual network. For more information about which integration runtime to use, see the [choose the right integration runtime configuration article.](data-map-integration-runtime-choose#choose-the-right-integration-runtime)
5. Select the credential to connect to your data source.

    ![Screenshot of new scan window, with the Purview MSI selected as the credential, but a service principal, or SQL authentication also available.](media/register-scan-azure-sql-managed-instance/set-up-scan-sql-mi.png)
6. You can scope your scan to specific tables by choosing the appropriate items in the list.

    ![Screenshot of the scope your scan window, with a subset of tables selected for scanning.](media/register-scan-azure-sql-managed-instance/scope-your-scan.png)
7. Then select a scan rule set. You can choose between the system default, existing custom rule sets, or create a new rule set inline.

    ![Screenshot of scan rule set window, with the system default scan rule set selected.](media/register-scan-azure-sql-managed-instance/scan-rule-set.png)
8. Choose your scan trigger. You can set up a schedule or run the scan once.

    ![Screenshot of the set scan trigger window, with the recurring tab selected.](media/register-scan-azure-sql-managed-instance/trigger-scan.png)
9. Review your scan and select **Save and run**.

If you're having trouble connecting to your data source, or running your scan, you scan see our [troubleshooting guide for scans and connections.](troubleshoot-connections)

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

## Set up access policies

The following types of Microsoft Purview policies are supported on this data resource:

- [DevOps policies](concept-policies-devops)

### Access policy prerequisites on Azure SQL MI

- Create a new Azure SQL MI or use an existing one in one of the currently available regions for this feature. You can follow [this guide](/en-us/azure/azure-sql/managed-instance/instance-create-quickstart?view=azuresql&amp;preserve-view=true) to create a new Azure SQL MI.

#### Region support

All [Microsoft Purview regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=purview) are supported.

Enforcement of Microsoft Purview policies is available only in the following regions for Azure SQL MI:

Public cloud:

- East US
- East US2
- South Central US
- West Central US
- West US3
- Canada Central
- Brazil South
- West Europe
- North Europe
- France Central
- UK South
- South Africa North
- Central India
- South East Asia
- East Asia
- Australia East

## Azure SQL MI configuration

This section explains how you can set up Azure SQL MI to honor policies from Microsoft Purview. Check first whether Azure SQL MI is configured for public or private endpoint. This [guide](/en-us/azure/azure-sql/managed-instance/public-endpoint-configure?view=azuresql-mi&amp;tabs=azure-portal&amp;preserve-view=true) explains how to do so.

### Configuration for SQL MI public endpoint

If Azure SQL MI is configured for public endpoint, follow these steps:

- Configure a Microsoft Entra Admin. In Azure portal navigate to the Azure SQL MI then navigate to Microsoft Entra ID on the side menu (formerly called Active Directory admin). Set an Admin name and then select **Save**.
- Then navigate to Identity on the side menu. Under System assigned managed identity check status to *On* and then select **Save**. See screenshot:

    [![Screenshot shows how to assign system managed identity to Azure SQL MI.](media/how-to-policies-data-owner-sql/assign-identity-azure-sql-mi.png)](media/how-to-policies-data-owner-sql/assign-identity-azure-sql-mi.png#lightbox)

### Configuration for SQL MI private endpoint

If Azure SQL MI is configured to use private endpoint, execute the same steps outlined in the configuration for public endpoint, and in addition, do the following:

- Navigate to the [Network Security Group (NSG)](/en-us/azure/virtual-network/network-security-groups-overview) associated to your Azure SQL MI.
- Add an outbound security rule similar to the one in the following screenshot. *Destination = Service Tag, Destination service tag = MicrosoftPurviewPolicyDistribution, Service = HTTPS, Action = Allow.* Ensure also that this rule's priority is lower than the one for the *deny\_all\_outbound* rule.

    ![Screenshot shows how to configure outbound security rule to Purview](media/how-to-policies-data-owner-sql/nsg-outbound-rule-azure-sql-mi.png)

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

#### Register the data sources in Microsoft Purview

The Azure SQL Managed Instance data source needs to be registered first with Microsoft Purview, before you can create access policies. You can follow the "Prerequisites" and "Register the data source" sections in this guide:

[Register and scan Azure SQL MI](register-scan-azure-sql-managed-instance#register)

After you've registered your resources, you'll need to enable data policy enforcement (formerly Data Use Management). Data policy enforcement needs certain permissions and can affect the security of your data, as it delegates to certain Microsoft Purview roles the ability to manage access to data sources. **Go through the secure practices related to data policy enforcement in this guide**: [How to enable data policy enforcement](how-to-enable-data-policy-enforcement)

Once your data source has the **Data policy enforcement** toggle *Enabled*, it will look like this screenshot. This will enable the access policies to be used with the given data source ![Screenshot shows how to enable policy enforcement.](media/how-to-policies-data-owner-sql/enable-policy-enforcement-azure-sql-mi.png)

Return to the Azure portal for Azure SQL Database to verify it's now governed by Microsoft Purview:

1. Sign in to the Azure portal through [this link](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Sql%2Fservers).
2. Select the Azure SQL Server that you want to configure.
3. Go to **Microsoft Entra ID** on the left pane.
4. Scroll down to **Microsoft Purview access policies**.
5. Select the button to **Check for Microsoft Purview Governance**. Wait while the request is processed, which could take a few minutes.

    [![Screenshot that shows Azure SQL is governed by Microsoft Purview.](media/how-to-policies-data-owner-sql/check-governed-status-azure-sql-db.png)](media/how-to-policies-data-owner-sql/check-governed-status-azure-sql-db.png#lightbox)
6. Confirm that the Microsoft Purview Governance Status shows **Governed**. Note that **it could take a few minutes** after you enable *Data policy enforcement* in Microsoft Purview for the correct status to be reflected.

Note

If you disable data policy enforcement for this Azure SQL Database data source in Microsoft Purview, select **Check for Microsoft Purview Governance** for the Microsoft Purview Governance Status to be updated to **Not Governed**. This step must be done for the impacted data source each time data policy enforcement status is changed for an existing or new access policy in Microsoft Purview. Before you enable *Data policy enforcement* for the data source in another Microsoft Purview account, ensure that the Purview Governance Status shows as **Not Governed**. Then repeat the steps above with the new Microsoft Purview account.

### Create a policy

To create access policies for Azure SQL MI, follow these guides:

- To create a DevOps policy on a single Azure SQL MI see [Provision access to system health, performance and audit information in Azure SQL MI](how-to-policies-devops-azure-sql-mi#create-a-new-devops-policy).
- To create policies that cover all data sources inside a resource group or Azure subscription, see [Discover and govern multiple Azure sources in Microsoft Purview](register-scan-azure-multiple-sources#policies).