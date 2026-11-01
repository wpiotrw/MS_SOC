---
layout: Conceptual
title: Connect to and manage Azure Arc-enabled SQL Server | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-arc-enabled-sql-server
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide describes how to connect to Azure Arc-enabled SQL Server in Microsoft Purview, and use Microsoft Purview features to scan and manage your Azure Arc-enabled SQL Server source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: shjia
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2024-03-21T00:00:00.0000000Z
ms.custom:
- template-how-to
- sfi-image-nochange
locale: en-us
document_id: 010714f6-f8d5-191b-8aa4-146ef3dfbf6b
document_version_independent_id: 010714f6-f8d5-191b-8aa4-146ef3dfbf6b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-arc-enabled-sql-server.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-arc-enabled-sql-server
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-arc-enabled-sql-server.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: 91e31d2d-f3d7-bae1-d38f-30f12e2225bf
---

# Connect to and manage Azure Arc-enabled SQL Server | Microsoft Learn

This article shows how to register an Azure Arc-enabled SQL Server instance. It also shows how to authenticate and interact with Azure Arc-enabled SQL Server in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes (preview) | Yes (preview) | Yes (preview) |

The supported SQL Server versions are 2012 and later. SQL Server Express LocalDB isn't supported.

When you're scanning Azure Arc-enabled SQL Server, Microsoft Purview supports extracting the following technical metadata:

- Instances
- Databases
- Schemas
- Tables, including the columns
- Views, including the columns

When you're setting up a scan, you can choose to specify the database name to scan one database. You can further scope the scan by selecting tables and views as needed. The whole Azure Arc-enabled SQL Server instance will be scanned if you don't provide a database name.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. See [Access control in the Microsoft Purview governance portal](data-gov-classic-permissions) for details.
- [Set up the right integration runtime for your scenario](data-map-integration-runtime-choose):

    - **To use a self-hosted integration runtime:**[Follow the article to create and configure a self-hosted integration runtime](data-map-integration-runtime-self-hosted).
    - **To use a kubernetes supported self-hosted integration runtime:**[Follow the article to create and configure a kubernetes supported integration runtime](data-map-integration-runtime-kubernetes). (SQL authentication only.)

## Networking

If your Microsoft Purview instance has disabled all public network access, to access your Arc-Enabled SQL Server, the virtual machine must be added to the virtual network that is connected to your Microsoft Purview instance.

## Register

This section describes how to register an Azure Arc-enabled SQL Server instance in Microsoft Purview by using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Authentication for registration

There are two ways to set up authentication for scanning Azure Arc-enabled SQL Server with a self-hosted integration runtime:

- SQL Server authentication
- Windows authentication - Not supported by a Kubernetes SHIR.

To configure authentication for the SQL Server deployment:

1. In SQL Server Management Studio (SSMS), go to **Server Properties**, and then select **Security** on the left pane.
2. Under **Server authentication**:

    - For Windows authentication, select either **Windows Authentication mode** or **SQL Server and Windows Authentication mode**.
    - For SQL Server authentication, select **SQL Server and Windows Authentication mode**.

    ![Screenshot that shows the Security page of the Server Properties window, with options for selecting authentication mode.](media/register-scan-azure-arc-enabled-sql-server/enable-sql-server-authentication.png)

A change to the server authentication requires you to restart the SQL Server instance and SQL Server Agent. In SSMS, go to the SQL Server instance and select **Restart** on the right-click options pane.

#### Create a new login and user

If you want to create a new login and user to scan your SQL Server instance, use the following steps.

The account must have access to the master database, because `sys.databases` is in the master database. The Microsoft Purview scanner needs to enumerate `sys.databases` in order to find all the SQL databases on the server.

Note

You can run all the following steps by using [this code](https://github.com/Azure/Purview-Samples/blob/master/TSQL-Code-Permissions/grant-access-to-on-prem-sql-databases.sql).

1. Go to SSMS, connect to the server, and then select **Security** on the left pane.
2. Select and hold (or right-click) **Login**, and then select **New login**. If Windows authentication is applied, select **Windows authentication**. If SQL Server authentication is applied, select **SQL Server authentication**.

    ![Screenshot that shows selections for creating a new login and user.](media/register-scan-azure-arc-enabled-sql-server/create-new-login-user.png)
3. Select **Server Roles** on the left pane, and ensure that a public role is assigned.
4. Select **User Mapping** on the left pane, select all the databases in the map, and then select the **db\_datareader** database role.

    ![Screenshot that shows user mapping.](media/register-scan-azure-arc-enabled-sql-server/user-mapping.png)
5. Select **OK** to save.
6. If SQL Server authentication is applied, you must change your password as soon as you create a new login:

    1. Select and hold (or right-click) the user that you created, and then select **Properties**.
    2. Enter a new password and confirm it.
    3. Select the **Specify old password** checkbox and enter the old password.
    4. Select **OK**.

    ![Screenshot that shows selections for changing a password.](media/register-scan-azure-arc-enabled-sql-server/change-password.png)

#### Store your SQL Server login password in a key vault and create a credential in Microsoft Purview

1. Go to your key vault in the Azure portal. Select **Settings** &gt; **Secrets**.
2. Select **+ Generate/Import**. For **Name** and **Value**, enter the password from your SQL Server login.
3. Select **Create**.
4. If your key vault isn't connected to Microsoft Purview yet, [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account).
5. [Create a new credential](data-map-data-scan-credentials#create-a-new-credential) by using the username and password to set up your scan.

    Be sure to select the right authentication method when you're creating a new credential. If Windows authentication is applied, select **Windows authentication**. If SQL Server authentication is applied, select **SQL Server authentication**.

### Steps to register

1. Go to your Microsoft Purview account.
2. Under **Sources and scanning** on the left pane, select **Integration runtimes**. Make sure that a self-hosted integration runtime is set up. If it isn't set up, [follow the steps to create a self-hosted integration runtime](data-map-integration-runtime-self-hosted) for scanning on an on-premises or Azure virtual machine that has access to your on-premises network.
3. Select **Data Map** on the left pane.
4. Select **Register**.
5. Select **Azure Arc-enabled SQL Server**, and then select **Continue**.

    ![Screenshot that shows selecting a SQL data source.](media/register-scan-azure-arc-enabled-sql-server/set-up-azure-arc-enabled-sql-data-source.png)
6. Provide a friendly name, which is a short name that you can use to identify your server. Also provide the server endpoint.
7. Select **Finish** to register the data source.

## Scan

Use the following steps to scan Azure Arc-enabled SQL Server instances to automatically identify assets and classify your data. For more information about scanning in general, see [Scans and ingestion in Microsoft Purview](data-map-scan-ingestion).

To create and run a new scan:

1. In the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), select the **Data Map** tab on the left pane.
2. Select the Azure Arc-enabled SQL Server source that you registered.
3. Select **New scan**.
4. Select the credential to connect to your data source. Credentials are grouped and listed under the authentication methods.

    ![Screenshot that shows selecting a credential for a scan.](media/register-scan-azure-arc-enabled-sql-server/azure-arc-enabled-sql-set-up-scan-win-auth.png)
5. You can scope your scan to specific tables by choosing the appropriate items in the list.

    ![Screenshot that shows selected assets for scoping a scan.](media/register-scan-azure-arc-enabled-sql-server/azure-arc-enabled-sql-scope-your-scan.png)
6. Select a scan rule set. You can choose between the system default, existing custom rule sets, or creation of a new rule set inline.

    ![Screenshot that shows selecting a scan rule set.](media/register-scan-azure-arc-enabled-sql-server/azure-arc-enabled-sql-scan-rule-set.png)
7. Choose your scan trigger. You can set up a schedule or run the scan once.

    ![Screenshot that shows setting up a recurring scan trigger.](media/register-scan-azure-arc-enabled-sql-server/trigger-scan.png)
8. Review your scan, and then select **Save and run**.

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

## Access policy

### Supported policies

The following types of policies are supported on this data resource from Microsoft Purview:

- [DevOps policies](concept-policies-devops)
- [Data Owner policies](concept-policies-data-owner) (preview)

### Access policy prerequisites on Azure Arc-enabled SQL Server

- Get [SQL Server on-premises version 2022](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) and install it. Versions 2022 or more recent are supported on both Windows and Linux. You can try the free Developer edition.
- Configure your [permissions](/en-us/azure/azure-arc/servers/prerequisites#required-permissions) and then [register a list of resource providers](/en-us/azure/azure-arc/servers/prerequisites#azure-resource-providers) in the subscription you'll use to onboard the SQL Server instance to Azure Arc.
- Complete prerequisites and onboard the [SQL Server instance with Azure Arc](/en-us/sql/sql-server/azure-arc/deployment-options). A simple configuration for Windows SQL Server is [here](/en-us/sql/sql-server/azure-arc/connect-with-installer). An alternate configuration for Linux SQL Server is [here](/en-us/azure/azure-arc/servers/onboard-portal#install-and-validate-the-agent-on-linux).
- Enable [Microsoft Entra authentication in SQL Server](/en-us/sql/relational-databases/security/authentication-access/azure-ad-authentication-sql-server-setup-tutorial). For a simpler setup, complete the [prerequisites](/en-us/sql/relational-databases/security/authentication-access/azure-ad-authentication-sql-server-automation-setup-tutorial#preparation-before-setting-the-azure-ad-admin) and process outlined in [this article](/en-us/sql/relational-databases/security/authentication-access/azure-ad-authentication-sql-server-automation-setup-tutorial#setting-up-azure-ad-admin-using-the-azure-portal).
- Remember to [grant application permissions and grant admin consent](/en-us/sql/relational-databases/security/authentication-access/azure-ad-authentication-sql-server-setup-tutorial#grant-application-permissions)
- You need to configure a Microsoft Entra admin for the SQL Server instance, but it isn't necessary to set up other Microsoft Entra logins or users. You'll grant access to those users by using Microsoft Purview policies.

#### Region support

Data policy enforcement is available in all Microsoft Purview regions except:

- West US2
- East Asia
- US Gov Virginia
- China North 3

#### Security considerations for Azure Arc-enabled SQL Server

- The server admin can turn off the Microsoft Purview policy enforcement.
- Azure Arc admin and server admin permissions provide the ability to change the Azure Resource Manager path of the server. Because mappings in Microsoft Purview use Resource Manager paths, it can lead to wrong policy enforcements.
- A SQL Server admin (database admin) can gain the power of a server admin and can tamper with the cached policies from Microsoft Purview.
- The recommended configuration is to create a separate app registration for each SQL server instance. This configuration prevents the second SQL Server instance from reading the policies meant for the first SQL Server instance, in case a rogue admin in the second SQL Server instance tampers with the Resource Manager path.

#### Verify the prerequisites

1. Sign in to the Azure portal through [this link](https://portal.azure.com/#view/Microsoft_Azure_HybridCompute/AzureArcCenterBlade/%7E/overview)
2. Navigate to **SQL servers** on the left pane. You'll see a list of SQL Server instances on Azure Arc.
3. Select the SQL Server instance that you want to configure.
4. Go to **Microsoft Entra ID** on the left pane.
5. Ensure that Microsoft Entra authentication is configured with an admin login. If not, refer to the access policy prerequisites section in this guide.
6. Ensure that a certificate has been provided to for SQL Server to authenticate to Azure. If not, refer to the access policy prerequisites section in this guide.
7. Ensure that an app registration has been entered to create a trust relationship between SQL Server and Microsoft Entra ID. If not, refer to the access policy prerequisites section in this guide.
8. If you made any changes, select the **Save** button to save the configuration and wait until the operation completes successfully. This could take a few minutes. The message *"Saved successfully"* will be displayed at the top of the page in green background. You might need to scroll up to see it.

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

### Register the data source and enable Data policy enforcement

Before you can create policies, you must register the Azure Arc-enabled SQL Server data source with Microsoft Purview:

1. Sign in to Microsoft Purview Studio.
2. Go to **Data map** on the left pane, select **Sources**, and then select **Register**. Enter **Azure Arc** in the search box and select **SQL Server on Azure Arc**. Then select **Continue**.

    ![Screenshot that shows selecting a source for registration.](media/how-to-policies-data-owner-sql/select-arc-sql-server-for-registration.png)
3. For **Name**, enter a name for this registration. It's best practice to make the name of the registration the same as the server name in the next step.
4. Select values for **Azure subscription**, **Server name**, and **Server endpoint**.
5. For **Select a collection**, choose a collection to put this registration in.
6. Enable **Data policy enforcement**. **Data policy enforcement** needs certain permissions and can affect the security of your data, because it delegates to certain Microsoft Purview roles to manage access to the data sources. Go through the secure practices related to **Data policy enforcement** in this guide: [Enable Data policy enforcement on your Microsoft Purview sources](how-to-enable-data-policy-enforcement).
7. Upon enabling Data Policy Enforcement, Microsoft Purview will automatically capture the **Application ID** of the App Registration related to this Azure Arc-enabled SQL Server if one has been configured. Come back to this screen and hit the refresh button on the side of it to refresh, in case the association between the Azure Arc-enabled SQL Server and the App Registration changes in the future.
8. Select **Register** or **Apply**.

![Screenshot that shows selections for registering a data source for a policy.](media/how-to-policies-data-owner-sql/enable-policy-enforcement-arc-sql.png)

### Enable policies in Azure Arc-enabled SQL Server

This section describes the steps to configure SQL Server on Azure Arc to use Microsoft Purview. Execute these steps after you enable the *Data policy enforcement* option for this data source in the Microsoft Purview account.

1. Sign in to the Azure portal through [this link](https://portal.azure.com/#view/Microsoft_Azure_HybridCompute/AzureArcCenterBlade/%7E/overview)
2. Navigate to **SQL servers** on the left pane. You'll see a list of SQL Server instances on Azure Arc.
3. Select the SQL Server instance that you want to configure.
4. Go to **Microsoft Entra ID** on the left pane.
5. Scroll down to **Microsoft Purview access policies**.
6. Select the button to **Check for Microsoft Purview Governance**. Wait while the request is processed. While that happens, this message will be displayed at the top of the page. You might need to scroll up to see it.

    ![Screenshot that shows Arc-SQL agent is processing a request](media/how-to-policies-data-owner-sql/arc-sql-processing-request.png)
7. At the bottom of the page, confirm that the Microsoft Purview Governance Status shows `Governed`. Note that **it may take up to 30 minutes** for the correct status to be reflected. Continue doing a browser refresh until that happens.
8. Confirm that the Microsoft Purview Endpoint points to the Microsoft Purview account where you registered this data source and enabled the *data policy enforcement*

### Create a policy

To create an access policy for Azure Arc-enabled SQL Server, follow these guides:

- [Provision access to system health, performance and audit information in SQL Server 2022](how-to-policies-devops-arc-sql-server#create-a-new-devops-policy)
- [Provision read/modify access on a single SQL Server 2022](how-to-policies-data-owner-arc-sql-server#create-and-publish-a-data-owner-policy)

To create policies that cover all data sources inside a resource group or Azure subscription, see [Discover and govern multiple Azure sources in Microsoft Purview](register-scan-azure-multiple-sources#policies).