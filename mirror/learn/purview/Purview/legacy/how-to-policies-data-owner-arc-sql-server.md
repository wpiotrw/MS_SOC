---
layout: Conceptual
title: Grant read access to data assets in SQL Server 2022 using Data owner policies (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-policies-data-owner-arc-sql-server
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use Microsoft Purview Data owner policies to manage access to SQL Server 2022 (Azure Arc enabled) so users or groups in your enterprise can read data assets.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: vlrodrig
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: references_regions, event-tier1-build-2022, msecd-doc-authoring-1030
locale: en-us
document_id: a1590c36-d242-671b-4552-4422dbcc6f95
document_version_independent_id: a1590c36-d242-671b-4552-4422dbcc6f95
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-policies-data-owner-arc-sql-server.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-policies-data-owner-arc-sql-server
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-policies-data-owner-arc-sql-server.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 0621e1fb-c5b6-285c-01e1-7f7cc9655eea
---

# Grant read access to data assets in SQL Server 2022 using Data owner policies (preview) | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

[Data owner policies](../concept-policies-data-owner) are a type of Microsoft Purview access policies. They allow you to manage access to user data in sources that have been registered for *Data Policy Enforcement* in Microsoft Purview. These policies can be authored directly in the Microsoft Purview governance portal, and after publishing, they get enforced by the data source.

This guide covers how a data owner can delegate authoring policies in Microsoft Purview to enable access to Azure Arc-enabled SQL Server. The following actions are currently enabled: *Read*. This action is only supported for policies at server level. *Modify* is not supported at this point.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- A new or existing Microsoft Purview account. [Follow this quickstart guide to create one](../create-microsoft-purview-portal).

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

## Microsoft Purview configuration

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

    [![Screenshot that shows the section in the Azure portal for adding a role assignment.](../media/how-to-policies-data-owner-authoring-generic/assign-iam-permissions.png)](../media/how-to-policies-data-owner-authoring-generic/assign-iam-permissions.png#lightbox)

    Note

    The *IAM Owner* role for a data resource can be inherited from a parent resource group, a subscription, or a subscription management group. Check which Microsoft Entra users, groups, and service principals hold or are inheriting the *IAM Owner* role for the resource.
- You also need to have the Microsoft Purview *Data source admin* role for the collection or a parent collection (if inheritance is enabled). For more information, see the [guide on managing Microsoft Purview role assignments](../data-gov-classic-permissions#assign-permissions-to-your-users).

    The following screenshot shows how to assign the *Data source admin* role at the root collection level.

    [![Screenshot that shows selections for assigning the Data source admin role at the root collection level.](../media/how-to-policies-data-owner-authoring-generic/assign-purview-permissions.png)](../media/how-to-policies-data-owner-authoring-generic/assign-purview-permissions.png#lightbox)

#### Configure Microsoft Purview permissions to create, update, or delete access policies

To create, update or delete policies, you need to get the *Policy author* role in Microsoft Purview at *root collection level*:

- The *Policy author* role can create, update, and delete DevOps and Data Owner policies.
- The *Policy author* role can delete self-service access policies.

For more information about managing Microsoft Purview role assignments, see [Create and manage collections in the Microsoft Purview Data Map](../data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Note

Policy author role must be configured at the root collection level.

In addition, to easily search Microsoft Entra users or groups when creating or updating the subject of a policy, you can greatly benefit from getting the [Directory Readers](/en-us/azure/active-directory/roles/permissions-reference#directory-readers) permission in Microsoft Entra ID. This is a common permission for users in an Azure tenant. Without the Directory Reader permission, the Policy Author will have to type the complete username or email for all the principals included in the subject of a data policy.

#### Configure Microsoft Purview permissions for publishing Data Owner policies

Data Owner policies allow for checks and balances if you assign the Microsoft Purview *Policy author* and *Data source admin* roles to different people in the organization. Before a Data owner policy takes effect, a second person (*Data source admin*) must review it and explicitly approve it by publishing it. This does not apply to DevOps or Self-service access policies as publishing is automatic for them when those policies are created or updated.

To publish a Data owner policy you need to get the *Data source admin* role in Microsoft Purview at *root collection level*.

For more information about managing Microsoft Purview role assignments, see [Create and manage collections in the Microsoft Purview Data Map](../data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Note

To publish Data owner policies, the Data source admin role must be configured at the root collection level.

#### Delegate access provisioning responsibility to roles in Microsoft Purview

After a resource has been enabled for **Data policy enforcement**, any Microsoft Purview user with the *Policy author* role at the root collection level can provision access to that data source from Microsoft Purview.

Note

Any Microsoft Purview root *Collection admin* can assign new users to root *Policy author* roles. Any *Collection admin* can assign new users to a *Data source admin* role under the collection. Minimize and carefully vet the users who hold Microsoft Purview *Collection admin*, *Data source admin*, or *Policy author* roles.

If a Microsoft Purview account with published policies is deleted, such policies will stop being enforced within an amount of time that depends on the specific data source. This change can have implications on both security and data access availability. The Contributor and Owner roles in IAM can delete Microsoft Purview accounts. You can check these permissions by going to the **Access control (IAM)** section for your Microsoft Purview account and selecting **Role Assignments**. You can also use a lock to prevent the Microsoft Purview account from being deleted through [Resource Manager locks](/en-us/azure/azure-resource-manager/management/lock-resources).

### Register data sources in Microsoft Purview

Register each data source with Microsoft Purview to later define access policies.

1. Sign in to Microsoft Purview Studio.
2. Navigate to the **Data map** feature on the left pane, select **Sources**, then select **Register**. Type "Azure Arc" in the search box and select **SQL Server on Azure Arc**. Then select **Continue**.

    ![Screenshot shows how to select a source for registration.](../media/how-to-policies-data-owner-sql/select-arc-sql-server-for-registration.png)
3. Enter a **Name** for this registration. It is best practice to make the name of the registration the same as the server name in the next step.
4. Select an **Azure subscription**, **Server name** and **Server endpoint**.
5. **Select a collection** to put this registration in.
6. Enable Data Policy Enforcement. Data Policy Enforcement needs certain permissions and can affect the security of your data, as it delegates to certain Microsoft Purview roles to manage access to the data sources. **Go through the secure practices related to Data Policy Enforcement in this guide**: [How to enable Data Policy Enforcement](../how-to-enable-data-policy-enforcement)
7. Select **Register** or **Apply** at the bottom.

Once your data source has the **Data policy enforcement** toggle *Enabled*, it will look like this picture.

![Screenshot shows how to register a data source for policy.](../media/how-to-policies-data-owner-sql/enable-policy-enforcement-arc-sql.png)

## Enable policies in Azure Arc-enabled SQL Server

This section describes the steps to configure SQL Server on Azure Arc to use Microsoft Purview. Execute these steps after you enable the *Data policy enforcement* option for this data source in the Microsoft Purview account.

1. Sign in to the Azure portal through [this link](https://portal.azure.com/#view/Microsoft_Azure_HybridCompute/AzureArcCenterBlade/%7E/overview)
2. Navigate to **SQL servers** on the left pane. You'll see a list of SQL Server instances on Azure Arc.
3. Select the SQL Server instance that you want to configure.
4. Go to **Microsoft Entra ID** on the left pane.
5. Scroll down to **Microsoft Purview access policies**.
6. Select the button to **Check for Microsoft Purview Governance**. Wait while the request is processed. While that happens, this message will be displayed at the top of the page. You might need to scroll up to see it.

    ![Screenshot that shows Arc-SQL agent is processing a request](../media/how-to-policies-data-owner-sql/arc-sql-processing-request.png)
7. At the bottom of the page, confirm that the Microsoft Purview Governance Status shows `Governed`. Note that **it may take up to 30 minutes** for the correct status to be reflected. Continue doing a browser refresh until that happens.
8. Confirm that the Microsoft Purview Endpoint points to the Microsoft Purview account where you registered this data source and enabled the *data policy enforcement*

## Create and publish a Data owner policy

Execute the steps in the **Create a new policy** and **Publish a policy** sections of the [data-owner policy authoring tutorial](../how-to-policies-data-owner-authoring-generic#create-a-new-policy). The result will be a data owner policy similar to the example:

**Example: Read policy**. This policy assigns the Microsoft Entra principal 'sg-Finance' to the *SQL Data reader* action, in the scope of SQL server *DESKTOP-xxx*. This policy has also been published to that server. Note that policies related to this action are not supported below server level.

![Screenshot shows a sample data owner policy giving Data Reader access to an Azure SQL Database.](../media/how-to-policies-data-owner-sql/data-owner-policy-example-arc-sql-server-data-reader.png)

Note

- Given that scan is not currently available for this data source, data reader policies can only be created at server level. Use the **Data sources** box instead of the Asset box when authoring the **data resources** part of the policy.
- There is a know issue with SQL Server Management Studio that prevents right-clicking on a table and choosing option “Select Top 1000 rows”.

Important

- Publish is a background operation. It can take up to **5 minutes** for the changes to be reflected in this data source.
- Changing a policy does not require a new publish operation. The changes will be picked up with the next pull.

## Unpublish a data owner policy

Follow this link for the steps to [unpublish a data owner policy in Microsoft Purview](../how-to-policies-data-owner-authoring-generic#unpublish-a-policy).

## Update or delete a data owner policy

Follow this link for the steps to [update or delete a data owner policy in Microsoft Purview](../how-to-policies-data-owner-authoring-generic#update-or-delete-a-policy).

## Test the policy

After the policy is published and has been communicated to the data source, any of the Microsoft Entra users in the Subject should be able to connect and execute a query that targets the assets to which the policy granted access. To test, use SSMS or any SQL client and try to query. For example, attempt access to a SQL table you have provided read access to.

If you require additional troubleshooting, see the Next steps section in this guide.

## Role definition detail

This section contains a reference of how relevant Microsoft Purview data policy roles map to specific actions in SQL data sources.

| Microsoft Purview policy role definition | Data source specific actions |
| --- | --- |
|  |  |
| *Read* | Microsoft.Sql/sqlservers/Connect |
|  | Microsoft.Sql/sqlservers/databases/Connect |
|  | Microsoft.Sql/Sqlservers/Databases/Schemas/Tables/Rows |
|  | Microsoft.Sql/Sqlservers/Databases/Schemas/Views/Rows |
|  |  |