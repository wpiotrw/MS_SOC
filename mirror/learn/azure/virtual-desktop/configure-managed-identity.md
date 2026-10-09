---
layout: Conceptual
title: Configure managed identity in Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/configure-managed-identity
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
zone_pivot_group_filename: virtual-desktop/zone-pivot-groups.json
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: ChristianMontoya
manager: eliotgra
ms.author: chrimo
ms.service: azure-virtual-desktop
description: How to configure a managed identity for host pools in Azure Virtual Desktop.
ms.topic: how-to
zone_pivot_groups: azure-virtual-desktop-managed-identity-approaches
ms.date: 2025-08-14T00:00:00.0000000Z
locale: en-us
document_id: cd385be2-1d0e-0e2f-0f94-479f6a5f43d4
document_version_independent_id: cd385be2-1d0e-0e2f-0f94-479f6a5f43d4
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/configure-managed-identity.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: configure-managed-identity
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/configure-managed-identity.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/f7db5823-dfbf-4e94-9016-c24311b90d7e
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/a5ab72d9-1367-4994-84a6-d9964cd9936d
platformId: f296cabd-4a7c-c20b-e3a4-248f9295c873
---

# Configure managed identity in Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn

Azure Virtual Desktop supports assigning permissions to [Managed identities for Azure resources](/en-us/entra/identity/managed-identities-azure-resources/overview) for features that need to perform Azure Resource Manager (ARM) operations on virtual machines, key vault, and virtual networks in the Azure subscription. The following feature can use a managed identity:

- [Autoscale](autoscale-scaling-plan).
- [Session host update](session-host-update).
- [Start VM on Connect](start-virtual-machine-connect).
- Azure Virtual Desktop for Azure Local.

Some Azure Virtual Desktop features can't use a managed identity. The features that require you [Assign Azure RBAC roles for Microsoft Entra roles to a service principal](service-principal-assign-roles?pivots=avd-service-principal) using the Azure Virtual Desktop service principal approach are:

- [App Attach](app-attach-setup) (when using Azure Files and your session hosts joined to Microsoft Entra ID).

When using a managed identity, you have two options:

- System-assigned managed identity
- User-assigned managed identity

Learn more about the [Differences between system-assigned and user-assigned managed identities](/en-us/entra/identity/managed-identities-azure-resources/overview#differences-between-system-assigned-and-user-assigned-managed-identities).

::: zone pivot="system-assigned"

## Prerequisites

To create and assign a system-assigned managed identity to a host pool, you need:

- An existing host pool.
- An Azure account assigned the [Desktop Virtualization Host Pool Contributor](rbac#desktop-virtualization-host-pool-contributor) at the scope of the host pool, or higher.
- If you want to use Azure CLI or Azure PowerShell locally, see [Use Azure CLI and Azure PowerShell with Azure Virtual Desktop](cli-powershell) to make sure you have the [desktopvirtualization](/en-us/cli/azure/desktopvirtualization) Azure CLI extension or the [Az.DesktopVirtualization](/en-us/powershell/module/az.desktopvirtualization) PowerShell module installed. Alternatively, use the [Azure Cloud Shell](/en-us/azure/cloud-shell/overview).

## Create and assign a system-assigned managed identity

Select the relevant tab for your scenario.

# [Azure portal](#tab/portal1)
Here's how to create a system-assigned managed identity with the Azure portal:

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. In the search bar, enter *Azure Virtual Desktop* and select the matching service entry
3. Select **Host pools**, then select the name of the host pool you want to configure.
4. Select **Identity**.
5. Select **Assign a Managed Identity** so that the box is checked, then select **System assigned managed identity**.
6. Select **Save** to create and assign a system-assigned managed identity.

# [Azure PowerShell](#tab/powershell1)
Here's how to create a system-assigned managed identity with Azure PowerShell. Be sure to change the `<placeholder>` values for your own.

1. Open [Azure Cloud Shell](/en-us/azure/cloud-shell/overview) in the Azure portal with the *PowerShell* terminal type, or run PowerShell on your local device.

    - If you're using Cloud Shell, make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).
    - If you're using PowerShell locally, first [sign in with Azure PowerShell](/en-us/powershell/azure/authenticate-azureps), and then make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).

1. Get the current values of the host pool:

    ```powershell
    $parameters = @{
        Name = '<HostPoolName>'
        ResourceGroupName = '<ResourceGroupName>'
    }
    
    $existingHostPool = Get-AzWvdHostPool @parameters
    ```
2. Run the `New-AzWvdHostPool` command with the same information, only changing the `IdentityType` to 'SystemAssigned'. Since this host pool already exists, this command only changes the `IdentityType` property:

    ```powershell
    $parameters = @{
        Name = $existingHostPool.Name
        ResourceGroupName = $existingHostPool.ResourceGroupName
        Location = $existingHostPool.Location
        HostPoolType = $existingHostPool.HostPoolType
        LoadBalancerType = $existingHostPool.LoadBalancerType
        PreferredAppGroupType = $existingHostPool.PreferredAppGroupType
        IdentityType = 'SystemAssigned'
    }
    
    New-AzWvdHostPool @parameters 
    ```
3. To check the changes, run this command:

    ```powershell
    $parameters = @{
        Name = '<HostPoolName>'
        ResourceGroupName = '<ResourceGroupName>'
    }
    
    Get-AzWvdHostPool @parameters | Format-Table Name, IdentityType
    ```

    The output should be similar to the following example:

    ```output
    Name        IdentityType
    ----------- ----------------
    contosohp01 SystemAssigned
    ```

---

::: zone-end

::: zone pivot="user-assigned"

## Prerequisites

To assign a user-assigned managed identity to a host pool, you need:

- An existing host pool.
- An Azure account assigned:

    1. [Desktop Virtualization Host Pool Contributor](rbac#desktop-virtualization-host-pool-contributor) at the scope of the host pool, or higher.
    2. [Managed Identity Operator](/en-us/azure/role-based-access-control/built-in-roles/identity#managed-identity-operator) at the scope of the managed identity, or higher.
- If you want to use Azure CLI or Azure PowerShell locally, see [Use Azure CLI and Azure PowerShell with Azure Virtual Desktop](cli-powershell) to make sure you have the [desktopvirtualization](/en-us/cli/azure/desktopvirtualization) Azure CLI extension or the [Az.DesktopVirtualization](/en-us/powershell/module/az.desktopvirtualization) PowerShell module installed. Alternatively, use the [Azure Cloud Shell](/en-us/azure/cloud-shell/overview).

## Assign a user-assigned managed identity

Select the relevant tab for your scenario.

# [Azure portal](#tab/portal2)
Here's how to assign a user-assigned managed identity with the Azure portal:

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. In the search bar, enter *Azure Virtual Desktop* and select the matching service entry
3. Select **Host pools**, then select the name of the host pool you want to configure.
4. Select **Identity**.
5. Select **Assign a Managed Identity** so that the box is checked, then select **User assigned managed identity**.
6. For **Subscription**, select the appropriate subscription from the drop-down menu.
7. For **Existing user assigned managed identities**, select the appropriate managed identity from the drop-down menu.
8. Select **Save** to apply the new managed identity.

# [Azure PowerShell](#tab/powershell2)
Here's how to assign a user-assigned managed identity with Azure PowerShell. Be sure to change the `<placeholder>` values for your own.

1. Open [Azure Cloud Shell](/en-us/azure/cloud-shell/overview) in the Azure portal with the *PowerShell* terminal type, or run PowerShell on your local device.

    - If you're using Cloud Shell, make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).
    - If you're using PowerShell locally, first [sign in with Azure PowerShell](/en-us/powershell/azure/authenticate-azureps), and then make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).

1. Get the current values of the host pool:

    ```powershell
    $parameters = @{
        Name = '<HostPoolName>'
        ResourceGroupName = '<HostPoolResourceGroupName>'
    }
    
    $existingHostPool = Get-AzWvdHostPool @parameters
    ```
2. Get the managed identity object that you want to assign to the host pool:

    ```powershell
    $parameters = @{
        Name = '<ManagedIdentityName>'
        ResourceGroupName = '<ManagedIdentityResourceGroupName>'
    }
    
    $managedIdentity = Get-AzUserAssignedIdentity @parameters
    ```
3. Run the `New-AzWvdHostPool` command with the same information, only changing the `IdentityType` to 'SystemAssigned'. Since this host pool already exists, this command only changes the `IdentityType` property:

    ```powershell
    $parameters = @{
        Name = $existingHostPool.Name
        ResourceGroupName = $existingHostPool.ResourceGroupName
        Location = $existingHostPool.Location
        HostPoolType = $existingHostPool.HostPoolType
        LoadBalancerType = $existingHostPool.LoadBalancerType
        PreferredAppGroupType = $existingHostPool.PreferredAppGroupType
        IdentityType = 'UserAssigned'
        IdentityUserAssignedIdentity = @{$managedIdentity.Id = @{}}
    }
    
    New-AzWvdHostPool @parameters 
    ```
4. To check the changes, run this command:

    ```powershell
    $parameters = @{
        Name = '<HostPoolName>'
        ResourceGroupName = '<ResourceGroupName>'
    }
    
    Get-AzWvdHostPool @parameters | Format-Table Name, IdentityType, IdentityUserAssignedIdentity
    ```

    The output should be similar to the following example:

    ```output
    Name        IdentityType     IdentityUserAssignedIdentity
    ----------- ---------------- ----------------------------
    contosohp01 UserAssigned   {...
    ```

---

::: zone-end

## Remove a managed identity

Removing a managed identity from a host pool has slightly different behavior, depending on the identity type of the managed identity:

- **System-assigned**: When you complete the removal, Azure automatically deletes the managed identity and all associated metadata.
- **User-assigned**: When you complete the removal, Azure removes the association between the host pool and the managed identity, but doesn't make any other changes. For example, it doesn't change any permissions assigned to the managed identity.

Important

Host pools configured with a session host configuration will **require a managed identity** in a future service update in order to add session hosts to the host pool. This replaces reliance on the Azure Virtual Desktop service principal and allows for a more secure configuration. Learn more about [using managed identities with Azure Virtual Desktop host pools](service-principal-assign-roles).

Select the relevant tab for your scenario.

# [Azure portal](#tab/portal3)
Here's how to remove a managed identity with the Azure portal:

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. In the search bar, enter *Azure Virtual Desktop* and select the matching service entry
3. Select **Host pools**, then select the name of the host pool you want to configure.
4. Select **Identity**.
5. Select the **Assign a Managed Identity** so that the box is unchecked.
6. Select **Save** to complete the removal of the managed identity.

# [Azure PowerShell](#tab/powershell3)
Here's how to remove a managed identity with Azure PowerShell. Be sure to change the `<placeholder>` values for your own.

1. Open [Azure Cloud Shell](/en-us/azure/cloud-shell/overview) in the Azure portal with the *PowerShell* terminal type, or run PowerShell on your local device.

    - If you're using Cloud Shell, make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).
    - If you're using PowerShell locally, first [sign in with Azure PowerShell](/en-us/powershell/azure/authenticate-azureps), and then make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).

1. Get the current values of the host pool:

    ```powershell
    $parameters = @{
        Name = '<HostPoolName>'
        ResourceGroupName = '<ResourceGroupName>'
    }
    
    $existingHostPool = Get-AzWvdHostPool @parameters
    ```
2. Run the `New-AzWvdHostPool` command with the same information, only changing the `IdentityType` to 'None'. Since this host pool already exists, this command only changes the `IdentityType` property:

    ```powershell
    $parameters = @{
        Name = $existingHostPool.Name
        ResourceGroupName = $existingHostPool.ResourceGroupName
        Location = $existingHostPool.Location
        HostPoolType = $existingHostPool.HostPoolType
        LoadBalancerType = $existingHostPool.LoadBalancerType
        PreferredAppGroupType = $existingHostPool.PreferredAppGroupType
        IdentityType = 'None'
    }
    
    New-AzWvdHostPool @parameters 
    ```
3. To check the changes, run this command:

    ```powershell
    $parameters = @{
        Name = '<HostPoolName>'
        ResourceGroupName = '<ResourceGroupName>'
    }
    
    Get-AzWvdHostPool @parameters | Format-Table Name, IdentityType
    ```

    The output should be similar to the following example:

    ```output
    Name        IdentityType
    ----------- ----------------
    contosohp01 None
    ```

---

## Assign managed identity to On-Premises Session hosts

Azure Virtual Desktop for Azure Local require that the managed identity is granted Reader access to the session host. These instructions will grant reader access to the resource group hosting those resources.

# [Azure portal](#tab/hybridportal)
Here's how to assign reader access to a managed identity with the Azure portal:

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. In the search bar, enter *Resource Groups* and select the matching entry
3. Select the **resource group** containing the session hosts
4. Select **Access Control (IAM)** in the left-side navigation.
5. Select **Add** and then **Add role assignment**
6. In the **Search by role name, description, permission, or ID** search box search for **Reader** and click **Next**
7. For **Assign access to** select **Managed identity**
8. For **Members** click **Select members**
9. Select the correct **Subscription**
10. In the **Managed Identity** dropdown select **Hostpool**
11. Select the correct Managed Identity for the Hostpool
12. Click **Select** and then **Next**
13. Select **Review + assign**
14. Review your selections and then select **Review + assign**

# [Azure PowerShell](#tab/hybridpowershell)
Here's how to assign reader access to a managed identity with Azure PowerShell. Be sure to change the `<placeholder>` values for your own.

1. Open [Azure Cloud Shell](/en-us/azure/cloud-shell/overview) in the Azure portal with the *PowerShell* terminal type, or run PowerShell on your local device.

    - If you're using Cloud Shell, make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).
    - If you're using PowerShell locally, first [sign in with Azure PowerShell](/en-us/powershell/azure/authenticate-azureps), and then make sure your [Azure context is set to the subscription that you want to use](/en-us/powershell/azure/context-persistence).

1. Get the managed identity object that is assigned to the host pool.

```powershell
$hostPool = Get-AzWvdHostPool -Name "<HOSTPOOL_NAME>" -ResourceGroupName "<RESOURCE_GROUP>"
$HP_PRINCIPAL_ID = $hostPool.IdentityPrincipalId
```

1. Assign reader access on the resource group to the managed identity

```powershell
New-AzRoleAssignment -ObjectId $HP_PRINCIPAL_ID -RoleDefinitionName "Reader" -ResourceGroupName "<RESOURCE_GROUP>"
```

---