---
layout: Conceptual
title: Tutorial to provision access for Azure Storage | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/tutorial-data-owner-policies-storage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This tutorial describes how a data owner can create access policies for Azure Storage resources.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jife
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: tutorial
ms.date: 2025-02-26T00:00:00.0000000Z
ms.custom: sfi-image-nochange
locale: en-us
document_id: 3a043493-2873-3015-ae58-c7e7003cf293
document_version_independent_id: 3a043493-2873-3015-ae58-c7e7003cf293
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/tutorial-data-owner-policies-storage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/tutorial-data-owner-policies-storage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/tutorial-data-owner-policies-storage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9d76f87e-5ed2-e87c-6388-30def0edeb91
---

# Tutorial to provision access for Azure Storage | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

[Policies](../concept-policies-data-owner) in Microsoft Purview allow you to enable access to data sources that have been registered to a collection. This tutorial describes how a data owner can use Microsoft Purview to enable access to datasets in Azure Storage through Microsoft Purview.

In this tutorial, you learn how to:

- Prepare your Azure environment
- Configure permissions to allow Microsoft Purview to connect to your resources
- Register your Azure Storage resource for Data Policy Enforcement
- Create and publish a policy for your resource group or subscription

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- A new or existing Microsoft Purview account. [Follow this quickstart guide to create one](../create-microsoft-purview-portal).

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

## Configuration

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

### Register the data sources in Microsoft Purview for Data Policy Enforcement

Your Azure Storage account needs to be registered in Microsoft Purview to later define access policies, and during registration we'll enable Data Policy Enforcement. **Data Policy Enforcement** is an available feature in Microsoft Purview that allows users to manage access to a resource from within Microsoft Purview. This allows you to centralize data discovery and access management, however it's a feature that directly impacts your data security.

Warning

Before enabling Data Policy Enforcement for any of your resources, read through our [**Data Policy Enforcement article**](../how-to-enable-data-policy-enforcement).

This article includes Data Policy Enforcement best practices to help you ensure that your information is secure.

To register your resource and enable Data Policy Enforcement, follow these steps:

Note

You need to be an owner of the subscription or resource group to be able to add a managed identity on an Azure resource.

1. From the [Azure portal](https://portal.azure.com), find the Azure Blob storage account that you would like to register.

    [![Screenshot that shows the storage account](../media/tutorial-data-owner-policies-storage/register-blob-storage-acct.png)](../media/tutorial-data-owner-policies-storage/register-blob-storage-acct.png#lightbox)
2. Select **Access Control (IAM)** in the left navigation and then select **+ Add** --&gt; **Add role assignment**.

    [![Screenshot that shows the access control for the storage account](../media/tutorial-data-owner-policies-storage/register-blob-access-control.png)](../media/tutorial-data-owner-policies-storage/register-blob-access-control.png#lightbox)
3. Set the **Role** to **Storage Blob Data Reader** and enter your *Microsoft Purview account name* under the **Select** input box. Then, select **Save** to give this role assignment to your Microsoft Purview account.

    [![Screenshot that shows the details to assign permissions for the Microsoft Purview account](../media/tutorial-data-owner-policies-storage/register-blob-assign-permissions.png)](../media/tutorial-data-owner-policies-storage/register-blob-assign-permissions.png#lightbox)
4. If you have a firewall enabled on your Storage account, follow these steps as well:

    1. Go into your Azure Storage account in [Azure portal](https://portal.azure.com).
    2. Navigate to **Security + networking &gt; Networking**.
    3. Choose **Selected Networks** under **Allow access from**.
    4. In the **Exceptions** section, select **Allow trusted Microsoft services to access this storage account** and select **Save**.

        [![Screenshot that shows the exceptions to allow trusted Microsoft services to access the storage account.](../media/tutorial-data-owner-policies-storage/register-blob-permission.png)](../media/tutorial-data-owner-policies-storage/register-blob-permission.png#lightbox)
5. Once you have set up authentication for your storage account, go to the [Microsoft Purview governance portal](https://web.purview.azure.com/).
6. Select **Data Map** on the left menu.

    ![Screenshot that shows the far left menu in the Microsoft Purview governance portal open with Data Map highlighted.](../media/tutorial-data-owner-policies-storage/select-data-map.png)
7. Select **Register**.

    ![Screenshot that shows the Microsoft Purview governance portal Data Map sources, with the register button highlighted at the top.](../media/tutorial-data-owner-policies-storage/select-register.png)
8. On **Register sources**, select **Azure Blob Storage**.

    ![Screenshot that shows the tile for Azure Multiple on the screen for registering multiple sources.](../media/tutorial-data-owner-policies-storage/select-azure-blob-storage.png)
9. Select **Continue**.
10. On the **Register sources (Azure)** screen, do the following:

    1. In the **Name** box, enter a friendly name that the data source will be listed with in the catalog.
    2. In the **Subscription** dropdown list boxes, select the subscription where your storage account is housed. Then select your storage account under **Storage account name**. In **Select a collection** select the collection where you'd like to register your Azure Storage account.

        [![Screenshot that shows the boxes for selecting a storage account.](../media/tutorial-data-owner-policies-storage/enable-policy-enforcement-storage.png)](../media/tutorial-data-owner-policies-storage/enable-policy-enforcement-storage.png#lightbox)
    3. In the **Select a collection** box, select a collection or create a new one (optional).
    4. Set the *Data Policy Enforcement* toggle to **Enabled**, as shown in the image below.

        [![Screenshot that shows Data Policy Enforcement toggle set to active on the registered resource page.](../media/tutorial-data-owner-policies-storage/enable-policy-enforcement-storage.png)](../media/tutorial-data-owner-policies-storage/enable-policy-enforcement-storage.png#lightbox)

        Tip

        If the Data Policy Enforcement toggle is greyed out and unable to be selected:

        1. Confirm you have followed all prerequisites to enable Data Policy Enforcement across your resources.
        2. Confirm that you have selected a storage account to be registered.
        3. It may be that this resource is already registered in another Microsoft Purview account. Hover over it to know the name of the Microsoft Purview account that has registered the data resource.first. Only one Microsoft Purview account can register a resource for Data Policy Enforcement at at time.
    5. Select **Register** to register the resource group or subscription with Microsoft Purview with Data Policy Enforcement enabled.

Tip

For more information about Data Policy Enforcement, including best practices or known issues, see our [Data Policy Enforcement article](../how-to-enable-data-policy-enforcement).

## Create a data owner policy

1. Sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Navigate to the **Data policy** feature using the left side panel. Then select **Data policies**.
3. Select the **New Policy** button in the policy page.

    [![Data owner can access the Policy functionality in Microsoft Purview when it wants to create policies.](../media/how-to-policies-data-owner-authoring-generic/policy-onboard-guide-1.png)](../media/how-to-policies-data-owner-authoring-generic/policy-onboard-guide-1.png#lightbox)
4. The new policy page will appear. Enter the policy **Name** and **Description**.
5. To add a policy statement to the new policy, select the **New policy statement** button. This will bring up the policy statement builder.

    [![Data owner can create a new policy statement.](../media/how-to-policies-data-owner-authoring-generic/create-new-policy.png)](../media/how-to-policies-data-owner-authoring-generic/create-new-policy.png#lightbox)
6. Select the **Effect** button and choose *Allow* from the drop-down list.
7. Select the **Action** button and choose *Read* or *Modify* from the drop-down list.
8. Select the **Data Resources** button to bring up the window to enter Data resource information, which will open to the right.
9. Under the **Data Resources** Panel do one of two things depending on the granularity of the policy:

    - To create a broad policy statement that covers an entire data source, resource group, or subscription that was previously registered, use the **Data sources** box and select its **Type**.
    - To create a fine-grained policy, use the **Assets** box instead. Enter the **Data Source Type** and the **Name** of a previously registered and scanned data source. See example in the image.

    [![Screenshot showing the policy editor, with Data Resources selected, and Data source Type highlighted in the data resources menu.](../media/how-to-policies-data-owner-authoring-generic/select-data-source-type.png)](../media/how-to-policies-data-owner-authoring-generic/select-data-source-type.png#lightbox)
10. Select the **Continue** button and traverse the hierarchy to select and underlying data-object (for example: folder, file, etc.). Select **Recursive** to apply the policy from that point in the hierarchy down to any child data-objects. Then select the **Add** button. This will take you back to the policy editor.

    ![Screenshot showing the Select asset menu, and the Add button highlighted.](../media/how-to-policies-data-owner-authoring-generic/select-asset.png)
11. Select the **Subjects** button and enter the subject identity as a principal, group, or MSI. Then select the **OK** button. This will take you back to the policy editor

    ![Screenshot showing the Subject menu, with a subject select from the search and the OK button highlighted at the bottom.](../media/how-to-policies-data-owner-authoring-generic/select-subject.png)
12. Select the **Save** button to save the policy.

    [![Screenshot showing a sample data owner policy giving access to an Azure Storage account.](../media/tutorial-data-owner-policies-storage/data-owner-policy-example-storage.png)](../media/tutorial-data-owner-policies-storage/data-owner-policy-example-storage.png#lightbox)

## Publish a data owner policy

1. Sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Navigate to the **Data policy** feature using the left side panel. Then select **Data policies**.

    ![Screenshot showing the Microsoft Purview governance portal with the leftmost menu open, Policy Management highlighted, and Data Policies selected on the next page.](../media/how-to-policies-data-owner-authoring-generic/policy-onboard-guide-2.png)
3. The Policy portal will present the list of existing policies in Microsoft Purview. Locate the policy that needs to be published. Select the **Publish** button on the right top corner of the page.

    [![Screenshot showing the policy editing menu with the Publish button highlighted in the top right of the page.](../media/how-to-policies-data-owner-authoring-generic/publish-policy.png)](../media/how-to-policies-data-owner-authoring-generic/publish-policy.png#lightbox)
4. A list of data sources is displayed. You can enter a name to filter the list. Then, select each data source where this policy is to be published and then select the **Publish** button.

    ![Screenshot showing with Policy publish menu with a data resource selected and the publish button highlighted.](../media/how-to-policies-data-owner-authoring-generic/select-data-sources-publish-policy.png)

Important

- Publish is a background operation. It can take up to **2 hours** for the changes to be reflected in Storage account(s).

## Clean up resources

To delete a policy in Microsoft Purview, follow these steps:

1. Sign in to the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Navigate to the **Data policy** feature using the left side panel. Then select **Data policies**.

    ![Screenshot showing the leftmost menu open, Policy Management highlighted, and Data Policies selected on the next page.](../media/how-to-policies-data-owner-authoring-generic/policy-onboard-guide-2.png)
3. The Policy portal will present the list of existing policies in Microsoft Purview. Select the policy that needs to be updated.
4. The policy details page will appear, including Edit and Delete options. Select the **Edit** button, which brings up the policy statement builder. Now, any parts of the statements in this policy can be updated. To delete the policy, use the **Delete** button.

    ![Screenshot showing an open policy with the Edit button highlighted in the top menu on the page.](../media/how-to-policies-data-owner-authoring-generic/edit-policy.png)