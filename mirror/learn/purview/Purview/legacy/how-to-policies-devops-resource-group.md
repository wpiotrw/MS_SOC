---
layout: Conceptual
title: Manage access to entire resource groups or subscriptions for monitoring system health and performance using Microsoft Purview DevOps policies, a type of RBAC policies. | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-policies-devops-resource-group
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use Microsoft Purview DevOps policies to provision access to all data sources inside a resource group or subscription, so IT operations personnel can monitor performance, health and audit security, while limiting the insider threat.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: vlrodrig
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 663912e2-25f6-ca27-8507-c01caddeedf2
document_version_independent_id: 663912e2-25f6-ca27-8507-c01caddeedf2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-policies-devops-resource-group.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-policies-devops-resource-group
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-policies-devops-resource-group.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 3e641a22-9449-4e2c-2dda-b550bf423e7b
---

# Manage access to entire resource groups or subscriptions for monitoring system health and performance using Microsoft Purview DevOps policies, a type of RBAC policies. | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

[DevOps policies](../concept-policies-devops) are a type of Microsoft Purview access policies. They allow you to manage access to system metadata on data sources that have been registered for *Data policy enforcement* in Microsoft Purview. These policies are configured directly in the Microsoft Purview governance portal, and after they're saved, they get automatically published and then enforced by the data source. Microsoft Purview policies only manage access for Microsoft Entra principals.

This how-to guide covers how to register an entire resource group or subscription and then create a single policy that will provision access to **all** data sources in that resource group or subscription. That single policy will cover all existing data sources and any data sources that are created afterwards. And provisioning access to its system metadata (DMVs and DMFs) using the DevOps policies actions *SQL Performance Monitoring* or *SQL Security Auditing*.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- A new or existing Microsoft Purview account. [Follow this quickstart guide to create one](../create-microsoft-purview-portal).

**Only these data sources are enabled for access policies on resource group or subscription**. Follow the **Prerequisites** section that is specific to the data sources in these guides:

- [DevOps policies on an Azure SQL Database](../how-to-policies-devops-azure-sql-db#prerequisites)
- [DevOps policies on an Azure Arc-enabled SQL Server](../how-to-policies-devops-arc-sql-server#prerequisites)

## Microsoft Purview Configuration

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

### Register the subscription or resource group for Data Policy Enforcement

The subscription or resource group needs to be registered with Microsoft Purview before you can create access policies. To register your subscription or resource group, follow the **Prerequisites** and **Register** sections of this guide:

- [Register multiple sources in Microsoft Purview](../register-scan-azure-multiple-sources#prerequisites)

After you've registered your resources, you'll need to enable the Data Policy Enforcement option. Data Policy Enforcement needs certain permissions and can affect the security of your data, as it delegates to certain Microsoft Purview roles to manage access to the data sources. **Go through the secure practices related to Data Policy Enforcement in this guide**: [How to enable Data Policy Enforcement](../how-to-enable-data-policy-enforcement)

In the end, your resource will have the **Data Policy Enforcement** toggle **Enabled**, as shown in the screenshot:

![Screenshot shows how to register a resource group or subscription for policy by toggling the enable tab in the resource editor.](../media/how-to-policies-data-owner-resource-group/enable-policy-enforcement-resource-group.png)

## Create a new DevOps policy

Follow this link for the steps to [create a new DevOps policy in Microsoft Purview](../how-to-policies-devops-authoring-generic#create-a-new-devops-policy).

## List DevOps policies

Follow this link for the steps to [list DevOps policies in Microsoft Purview](../how-to-policies-devops-authoring-generic#list-devops-policies).

## Update a DevOps policy

Follow this link for the steps to [update a DevOps policies in Microsoft Purview](../how-to-policies-devops-authoring-generic#update-a-devops-policy).

## Delete a DevOps policy

Follow this link for the steps to [delete a DevOps policies in Microsoft Purview](../how-to-policies-devops-authoring-generic#delete-a-devops-policy).

## Test the DevOps policy

See how to [test the policy you created.](../how-to-policies-devops-authoring-generic#test-the-devops-policy)

## Role definition detail

See the [mapping of DevOps role to data source actions.](../how-to-policies-devops-authoring-generic#role-definition-detail)