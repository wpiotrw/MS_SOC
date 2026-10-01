---
layout: Conceptual
title: Grant RBAC Access to Reservations by Using PowerShell - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/manage-reservations-rbac-powershell
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/f54500da-fd24-ec11-b6e6-000d3a4f07b8
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
description: Learn how to delegate access management for Azure reservations by using PowerShell.
author: pri-mittal
ms.reviewer: primittal
ms.service: cost-management-billing
ms.subservice: reservations
ms.custom: devx-track-azurepowershell
ms.topic: how-to
ms.date: 2026-09-30T00:00:00.0000000Z
ms.author: primittal
service.tree.id: cf90d1aa-e8ca-47a9-a6d0-bc69c7db1d52
locale: en-us
document_id: c00952f4-d8be-ca41-8b06-cb2d906f769a
document_version_independent_id: 8933231f-bbfe-4bd2-7b49-0ff9ef4a7069
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/reservations/manage-reservations-rbac-powershell.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/reservations/manage-reservations-rbac-powershell
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/reservations/manage-reservations-rbac-powershell.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
- https://authoring-docs-microsoft.poolparty.biz/devrel/f7db5823-dfbf-4e94-9016-c24311b90d7e
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/a5ab72d9-1367-4994-84a6-d9964cd9936d
platformId: e2ce800a-eb0f-a28a-5128-20c07ff20505
---

# Grant RBAC Access to Reservations by Using PowerShell - Microsoft Cost Management | Microsoft Learn

This article shows you how to grant role-based access control (RBAC) access to Azure reservations by using Azure PowerShell. To view and manage RBAC access in the Azure portal, see [Permissions to view and manage Azure reservations](view-reservations).

Note

We recommend that you use the Azure Az PowerShell module to interact with Azure. To get started, see [Install Azure PowerShell](/en-us/powershell/azure/install-azure-powershell). To learn how to migrate to the Az PowerShell module, see [Migrate Azure PowerShell from AzureRM to Az](/en-us/powershell/azure/migrate-from-azurerm-to-az).

## Grant access by using PowerShell

The following user types can delegate access management for all reservation orders that they can access:

- Users that have owner access for reservations orders
- Users with elevated access
- [User Access Administrators](../../role-based-access-control/built-in-roles#user-access-administrator)

When you grant access by using PowerShell, you can't view the roles in the Azure portal. Instead, you can view roles by using the `get-AzRoleAssignment` command in the following section.

## Assign the owner role for all reservations

Use the following PowerShell script to give a user RBAC access to all reservation orders in their Microsoft Entra tenant (directory).

```azurepowershell

Import-Module Az.Accounts
Import-Module Az.Resources
 
Connect-AzAccount -Tenant <TenantId>
 
$response = Invoke-AzRestMethod -Path /providers/Microsoft.Capacity/reservations?api-version=2020-06-01 -Method GET
 
$responseJSON = $response.Content | ConvertFrom-JSON
 
$reservationObjects = $responseJSON.value
 
foreach ($reservation in $reservationObjects)
{
  $reservationOrderId = $reservation.id.substring(0, 84)
  Write-Host "Assigning Owner role assignment to "$reservationOrderId
  New-AzRoleAssignment -Scope $reservationOrderId -ObjectId <ObjectId> -RoleDefinitionName Owner
}
```

When you use the PowerShell script to assign the ownership role and it runs successfully, a success message isn't returned.

### Parameters

The `-ObjectId` parameter is the Microsoft Entra `ObjectId` of the user, group, or service principal.

- **Type**: String
- **Aliases**: `Id`, `PrincipalId`
- **Position**: Named
- **Default value**: None
- **Accept pipeline input**: True
- **Accept wildcard characters**: False

The `-TenantId` parameter is the tenant's unique identifier.

- **Type**: String
- **Position**: 5
- **Default value**: None
- **Accept pipeline input**: False
- **Accept wildcard characters**: False

## Grant tenant-level access

You need [User Access Administrator](../../role-based-access-control/built-in-roles#user-access-administrator) rights before you can grant users or groups the following roles at the tenant level:

- Reservations Administrator
- Reservations Contributor
- Reservations Reader

To get User Access Administrator rights at the tenant level, follow the steps to [elevate access](../../role-based-access-control/elevate-access-global-admin).

### Add a Reservations Administrator role, Reservations Contributor role, or Reservations Reader role at the tenant level

Only users with the Global Administrator role can assign these roles from the [Azure portal](https://portal.azure.com).

1. Sign in to the Azure portal and go to **Reservations**.
2. Select a reservation that you can access.
3. At the top of the page, select **Role Assignment**.
4. Select the **Roles** tab.
5. To make modifications, add a user as a Reservations Administrator, Reservations Contributor, or Reservations Reader by using access control.

### Add a Reservations Administrator role at the tenant level by using an Azure PowerShell script

Use the following Azure PowerShell script to add a Reservations Administrator role at the tenant level.

```azurepowershell
Import-Module Az.Accounts
Import-Module Az.Resources
Connect-AzAccount -Tenant <TenantId>
New-AzRoleAssignment -Scope "/providers/Microsoft.Capacity" -PrincipalId <ObjectId> -RoleDefinitionName "Reservations Administrator"
```

#### Parameters

The `-ObjectId` parameter is the Microsoft Entra `ObjectId` of the user, group, or service principal.

- **Type**: String
- **Aliases**: `Id`, `PrincipalId`
- **Position**: Named
- **Default value**: None
- **Accept pipeline input**: True
- **Accept wildcard characters**: False

The `-TenantId` parameter is the tenant's unique identifier.

- **Type**: String
- **Position**: 5
- **Default value**: None
- **Accept pipeline input**: False
- **Accept wildcard characters**: False

### Add a Reservations Contributor role at the tenant level by using an Azure PowerShell script

Use the following Azure PowerShell script to add a Reservations Contributor role at the tenant level.

```azurepowershell
Import-Module Az.Accounts
Import-Module Az.Resources
Connect-AzAccount -Tenant <TenantId>
New-AzRoleAssignment -Scope "/providers/Microsoft.Capacity" -PrincipalId <ObjectId> -RoleDefinitionName "Reservations Contributor"
```

#### Parameters

The `-ObjectId` parameter is the Microsoft Entra `ObjectId` of the user, group, or service principal.

- **Type**: String
- **Aliases**: `Id`, `PrincipalId`
- **Position**: Named
- **Default value**: None
- **Accept pipeline input**: True
- **Accept wildcard characters**: False

The `-TenantId` parameter is the tenant's unique identifier.

- **Type**: String
- **Position**: 5
- **Default value**: None
- **Accept pipeline input**: False
- **Accept wildcard characters**: False

### Assign a Reservations Reader role at the tenant level by using an Azure PowerShell script

Use the following Azure PowerShell script to assign the Reservations Reader role at the tenant level.

```azurepowershell

Import-Module Az.Accounts
Import-Module Az.Resources

Connect-AzAccount -Tenant <TenantId>

New-AzRoleAssignment -Scope "/providers/Microsoft.Capacity" -PrincipalId <ObjectId> -RoleDefinitionName "Reservations Reader"
```

#### Parameters

The `-ObjectId` parameter is the Microsoft Entra `ObjectId` of the user, group, or service principal.

- **Type**: String
- **Aliases**: `Id`, `PrincipalId`
- **Position**: Named
- **Default value**: None
- **Accept pipeline input**: True
- **Accept wildcard characters**: False

The `-TenantId` parameter is the tenant's unique identifier.

- **Type**: String
- **Position**: 5
- **Default value**: None
- **Accept pipeline input**: False
- **Accept wildcard characters**: False