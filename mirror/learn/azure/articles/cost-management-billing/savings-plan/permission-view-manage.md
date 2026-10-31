---
layout: Conceptual
title: Permissions to view and manage savings plans - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/permission-view-manage
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/748a4eaa-0e25-ec11-b6e6-000d3a4f07b8
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
learn_banner_products:
- azure
description: Learn how savings plan permissions work and how to view and manage your savings plan in the Azure portal.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.custom: devx-track-azurepowershell
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: dfbc1d67-0ce5-39a4-3ee1-eadaee8b2789
document_version_independent_id: 5c4e332a-3c56-1d11-adc9-2faee3cf5b05
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/permission-view-manage.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/permission-view-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/permission-view-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: 03aa1910-14a8-e29c-dad7-129322e1b42b
---

# Permissions to view and manage savings plans - Microsoft Cost Management | Microsoft Learn

This article explains how savings plan permissions work and how users can view and manage savings plans in the Azure portal.

## Who can manage a savings plan by default

Two authorization methods control a user's ability to view and manage savings plans and delegate permissions: billing admin roles and savings plan role-based access control (RBAC) roles.

## Billing admin roles

Use built-in billing admin roles to view and manage savings plans and delegate permissions. To learn more about Microsoft Customer Agreement and Enterprise Agreement billing roles, see [Understand Microsoft Customer Agreement administrative roles in Azure](../manage/understand-mca-roles) and [Managing Azure Enterprise Agreement roles](../manage/understand-ea-roles), respectively.

### Billing admin roles required for savings plan actions

- View savings plans:
    - **Microsoft Customer Agreement**: Users with billing profile reader or above
    - **Enterprise Agreement**: Users with enterprise administrator (read only) or above
    - **Microsoft Partner Agreement**: Not supported
- Manage savings plans (achieved by delegating permissions for the full billing profile/enrollment):
    - **Microsoft Customer Agreement**: Users with billing profile contributor or above
    - **Enterprise Agreement**: Users with Enterprise Agreement administrator or above
    - **Microsoft Partner Agreement**: Not supported
- Delegate savings plan permissions:
    - **Microsoft Customer Agreement**: Users with billing profile contributor or above
    - **Enterprise Agreement**: Users with Enterprise Agreement purchaser or above
    - **Microsoft Partner Agreement**: Not supported

### View and manage savings plans as a billing admin

If you're a billing role user, follow these steps to view and manage all savings plans and savings plan transactions in the Azure portal.

1. Sign in to the [Azure portal](https://portal.azure.com) and go to **Cost Management + Billing**.
    - If you're under an Enterprise Agreement account, on the left menu, select **Billing scopes**. Then in the list of billing scopes, select one.
    - If you're under a Microsoft Customer Agreement account, on the left menu, select **Billing profiles**. In the list of billing profiles, select one.
2. On the left menu, select **Products + services** &gt; **Savings plans**. The complete list of savings plans for your Enterprise Agreement enrollment or Microsoft Customer Agreement billing profile appears.
3. Billing role users can take ownership of a savings plan with the [Savings Plan Order - Elevate REST API](/en-us/rest/api/billingbenefits/savings-plan-order/elevate) to give themselves Azure RBAC roles.

### Add billing administrators

Add a user as a billing administrator to an Enterprise Agreement or a Microsoft Customer Agreement in the Azure portal.

- **Enterprise Agreement**: Add users with the Enterprise administrator role to view and manage all savings plan orders that apply to the Enterprise Agreement. Enterprise administrators can view and manage savings plans in **Cost Management + Billing**.
    - Users with the Enterprise administrator (read-only) role can only view the savings plan from **Cost Management + Billing**.
    - Department admins and account owners can't view savings plans unless they're explicitly added to them by using **Access control (IAM)**. For more information, see [Manage Azure Enterprise roles](../manage/understand-ea-roles).
- **Microsoft Customer Agreement**: Users with the billing profile owner role or the billing profile contributor role can manage all savings plan purchases made by using the billing profile.
    - Billing profile readers and invoice managers can view all savings plans that are paid for with the billing profile. However, they can't make changes to savings plans. For more information, see [Billing profile roles and tasks](../manage/understand-mca-roles#billing-profile-roles-and-tasks).

## Savings plan RBAC roles

The savings plan lifecycle is independent of an Azure subscription. Savings plans don't inherit permissions from subscriptions after the purchase. Savings plans are a tenant-level resource with their own Azure RBAC permissions.

### Overview

There are four savings plan-specific RBAC roles:

- **Savings plan administrator**: Allows [management](manage-savings-plan) of one or more savings plans in a tenant and [delegation of RBAC roles](/en-us/azure/role-based-access-control/role-assignments-portal) to other users.
- **Savings plan purchaser**: Allows purchase of savings plans with a specified subscription.
    - Allows nonbilling admins and nonsubscription owners to purchase savings plans or perform a [reservation trade-in](reservation-trade-in).
    - Savings plan purchasing by nonbilling admins must be enabled. For more information, see [Permissions to buy a savings plan](permission-buy-savings-plan).
- **Savings plan contributor**: Allows management of one or more savings plans in a tenant but not delegation of RBAC roles to other users.
- **Savings plan reader**: Allows read-only access to one or more savings plans in a tenant.

You can scope these roles to either a specific resource entity (for example, a subscription or savings plan) or the Microsoft Entra tenant (directory). To learn more about Azure RBAC, see [What is Azure role-based access control (Azure RBAC)?](../../role-based-access-control/overview)

### Savings plan RBAC roles required for savings plan actions

- View savings plans:
    - **Tenant scope**: Users with savings plan reader or above.
    - **Savings plan scope**: Built-in reader or above.
- Manage savings plans:
    - **Tenant scope**: Users with savings plan contributor or above.
    - **Savings plan scope**: Built-in contributor or owner roles, or savings plan contributor or above.
- Delegate savings plan permissions:
    - **Tenant scope**: [User Access administrator](../../role-based-access-control/built-in-roles#general) rights are required to grant RBAC roles to all savings plans in the tenant. To gain these rights, follow [Elevate access](../../role-based-access-control/elevate-access-global-admin) steps.
    - **Savings plan scope**: Savings plan administrator or user access administrator.

In addition, users who held the subscription owner role when the subscription was used to purchase a savings plan can also view, manage, and delegate permissions for the purchased savings plan.

### View savings plans with RBAC access

If you have savings plan-specific RBAC roles (savings plan administrator, purchaser, contributor, or reader), purchased savings plans, or were added as an owner to savings plans, follow these steps to view and manage savings plans in the Azure portal.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Select **Home** &gt; **Savings plans** to list savings plans to which you have access.

### Add RBAC roles to users and groups

To learn about delegating savings plan RBAC roles, see [Delegate savings plan RBAC roles](manage-savings-plan#delegate-savings-plan-rbac-roles).

*Enterprise administrators can take ownership of a savings plan order. They can add other users to a savings plan by using***Access control (IAM)**.

## Grant access with PowerShell

Users who have owner access for savings plan orders, users with elevated access, and [user access administrators](../../role-based-access-control/built-in-roles#user-access-administrator) can delegate access management for all savings plan orders to which they have access.

Access granted by using PowerShell isn't shown in the Azure portal. Instead, you use the `get-AzRoleAssignment` command in the following section to view assigned roles.

### Assign the owner role for all savings plans

To give a user Azure RBAC access to all savings plan orders in their Microsoft Entra tenant (directory), use the following Azure PowerShell script:

```azurepowershell
Import-Module Az.Accounts
Import-Module Az.Resources

Connect-AzAccount -Tenant <TenantId>
$response = Invoke-AzRestMethod -Path /providers/Microsoft.BillingBenefits/savingsPlans?api-version=2022-11-01 -Method GET
$responseJSON = $response.Content | ConvertFrom-JSON
$savingsPlanObjects = $responseJSON.value

foreach ($savingsPlan in $savingsPlanObjects)
{
  $savingsPlanOrderId = $savingsPlan.id.substring(0, 84)
  Write-Host "Assigning Owner role assignment to "$savingsPlanOrderId
  New-AzRoleAssignment -Scope $savingsPlanOrderId -ObjectId <ObjectId> -RoleDefinitionName Owner
}
```

When the PowerShell script successfully assigns the owner role, it doesn't return a success message.

#### Parameters

- **ObjectId**: Microsoft Entra object ID of the user, group, or service principal

    - **Type**: String
    - **Aliases**: Id, PrincipalId
    - **Position**: Named
    - **Default value**: None
    - **Accept pipeline input**: True
    - **Accept wildcard characters**: False
- **TenantId**: Tenant unique identifier

    - **Type**: String
    - **Position**: 5
    - **Default value**: None
    - **Accept pipeline input**: False
    - **Accept wildcard characters**: False

### Add a savings plan administrator role at the tenant level by using Azure PowerShell script

To add a savings plan administrator role at the tenant level with PowerShell, use the following Azure PowerShell script:

```azurepowershell
Import-Module Az.Accounts
Import-Module Az.Resources
Connect-AzAccount -Tenant <TenantId>
New-AzRoleAssignment -Scope "/providers/Microsoft.BillingBenefits" -PrincipalId <ObjectId> -RoleDefinitionName "Savings plan administrator"
```

#### Parameters

- **ObjectId**: Microsoft Entra object ID of the user, group, or service principal

    - **Type**: String
    - **Aliases**: Id, PrincipalId
    - **Position**: Named
    - **Default value**: None
    - **Accept pipeline input**: True
    - **Accept wildcard characters**: False
- **TenantId**: Tenant unique identifier

    - **Type**: String
    - **Position**: 5
    - **Default value**: None
    - **Accept pipeline input**: False
    - **Accept wildcard characters**: False

### Assign a savings plan contributor role at the tenant level by using Azure PowerShell script

To assign the savings plan contributor role at the tenant level with PowerShell, use the following Azure PowerShell script:

```azurepowershell
Import-Module Az.Accounts
Import-Module Az.Resources
Connect-AzAccount -Tenant <TenantId>
New-AzRoleAssignment -Scope "/providers/Microsoft.BillingBenefits" -PrincipalId <ObjectId> -RoleDefinitionName "Savings plan contributor"
```

#### Parameters

- **ObjectId**: Microsoft Entra object ID of the user, group, or service principal

    - **Type**: String
    - **Aliases**: Id, PrincipalId
    - **Position**: Named
    - **Default value**: None
    - **Accept pipeline input**: True
    - **Accept wildcard characters**: False
- **TenantId**: Tenant unique identifier

    - **Type**: String
    - **Position**: 5
    - **Default value**: None
    - **Accept pipeline input**: False
    - **Accept wildcard characters**: False

### Assign a savings plan reader role at the tenant level by using Azure PowerShell script

To assign the savings plan reader role at the tenant level with PowerShell, use the following Azure PowerShell script:

```azurepowershell
Import-Module Az.Accounts
Import-Module Az.Resources
Connect-AzAccount -Tenant <TenantId>
New-AzRoleAssignment -Scope "/providers/Microsoft.BillingBenefits" -PrincipalId <ObjectId> -RoleDefinitionName "Savings plan reader"
```

#### Parameters

- **ObjectId**: Microsoft Entra object ID of the user, group, or service principal

    - **Type**: String
    - **Aliases**: Id, PrincipalId
    - **Position**: Named
    - **Default value**: None
    - **Accept pipeline input**: True
    - **Accept wildcard characters**: False
- **TenantId**: Tenant unique identifier

    - **Type**: String
    - **Position**: 5
    - **Default value**: None
    - **Accept pipeline input**: False
    - **Accept wildcard characters**: False