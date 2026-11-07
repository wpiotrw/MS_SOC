---
layout: Conceptual
title: Zone resilience for Azure VMs (Preview) - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/zone-resilience
breadcrumb_path: ../breadcrumb/azure-compute/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/94/azure-virtual-machines/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ec2f1827-be25-ec11-b6e6-000d3a4f0f1c
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: AjKundnani
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: ajkundna
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Learn how zone resilience for Azure VMs uses ZRS managed disks for customer-initiated failover to another availability zone.
ms.topic: concept-article
ms.date: 2026-10-20T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 06e52f22-c09c-1595-7208-8779765e83a3
document_version_independent_id: b1a8e49b-586e-f239-6b8b-4cb824bc3d1d
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/zone-resilience.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/zone-resilience
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/zone-resilience.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/089c8ba6-d135-43ff-bfaf-b8197fb72fb9
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/32516e21-6665-416f-be21-413febe47d91
platformId: af75caf3-b19a-86b6-a3ca-715183b60808
---

# Zone resilience for Azure VMs (Preview) - Azure Virtual Machines | Microsoft Learn

Zone resilience for Azure VMs lets you initiate failover of an eligible zonal Azure virtual machine (VM) to another availability zone in the same region. Failover changes the zone placement of the existing VM without creating a replacement. The VM retains its resource ID and VM ID, attached network interface (NIC) and its IP configuration, supported zone-redundant storage (ZRS) managed disks, and other supported resource settings. The zone placement changes; the supported configuration remains associated with the VM.

Zone failover is customer-initiated. See Limitations. For high availability across zones, [deploy multiple VMs across availability zones](disks-high-availability#deploy-vms-and-disks-across-three-availability-zones) and distribute traffic between them.

Important

Zone resilience for Azure VMs is in preview. Use this preview only for evaluation and testing with nonproduction VMs. Don't use it for production VMs. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

Because ZRS synchronously replicates managed disk data across availability zones, zone resilience provides a near-zero recovery point objective (RPO) for data committed to supported ZRS disks.

## How zone failover works

For an eligible VM affected by a zone failure, the failover workflow moves the VM to a healthy zone in the same region. See Limitations.

Important

Zone resilience for Azure VMs is in preview. Use this preview only for evaluation and testing with nonproduction VMs. Don't use it for production VMs. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

![Diagram of Customer-initiated zone failover: confirm impact, force-deallocate, change zones, start, and verify the VM.](media/zone-resilience/zone-recovery-workflow.png)

 Confirm the VM is affected and select a healthy zone in the same region. Force-deallocate the VM, which stops the workload. Update the zone placement of the existing VM and reuse its supported ZRS disks. Start the VM in the target zone, subject to available capacity. Verify the VM, disks, network, and workload before restoring traffic.

The workload is unavailable while the VM is deallocated and started in the target zone. Active requests, in-memory data, and runtime state aren't preserved.

The target zone must support the VM size and have enough capacity when you start the VM.

## Requirements

Before you enable zone resilience for Azure VMs, confirm that your configuration meets these requirements:

| Resource | Requirement |
| --- | --- |
| VM placement | Use a new or existing VM deployed in a specific availability zone. |
| OS disk | Use a Premium SSD ZRS or Standard SSD ZRS managed disk. |
| Data disks | Use Premium SSD ZRS or Standard SSD ZRS for every attached data disk. |
| Private IP address | Use a static or dynamic private IP address. |
| Public IP address | If used, configure a zone-redundant Standard SKU public IP address. |
| Network appliance | If used, configure a zone-redundant Standard SKU load balancer or supported gateway. |
| Management tool | Use the Azure portal, Azure CLI version 2.87.0 or later, Azure PowerShell with zone movement and force deallocation support, or Compute REST API version `2026-03-01`. |

For current ZRS disk types and regional availability, see [Redundancy options for managed disks](disks-redundancy#zone-redundant-storage-for-managed-disks). To create ZRS disks, see [Deploy a managed disk that uses zone-redundant storage](disks-deploy-zrs).

## Limitations

Important

Zone resilience for Azure VMs is in preview. Use this preview only for evaluation and testing with nonproduction VMs. Don't use it for production VMs. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

The following limitations result from the requirement to use ZRS managed disks:

- Locally redundant storage (LRS) OS and data disks aren't supported. Every attached OS and data disk must use Premium SSD ZRS or Standard SSD ZRS.
- Ephemeral OS disks aren't supported because they use local VM storage.
- Premium SSD v2, Ultra Disks, and Standard HDD managed disks aren't supported because these disk types don't offer ZRS. See [ZRS limitations](disks-redundancy#zrs-limitations).
- Data disks that use write acceleration aren't supported.

To prepare a zone VM with LRS disks, follow [Convert a disk from LRS to ZRS](disks-migrate-lrs-zrs#zonal-migration) to create ZRS disks from snapshots of the OS and data disks. You can't change a zone LRS disk's redundancy in place, but you can keep the existing VM if its disks meet the [OS disk swap requirements](linux/os-disk-swap#os-disk-swap-requirements). Swap in the ZRS OS disk, then detach the LRS data disks and attach the corresponding ZRS disks. Plan for downtime, and confirm the OS and every attached data disk use a supported ZRS type before you enable zone movement. The [regional disk conversion](disks-migrate-lrs-zrs#regional-migration) procedure doesn't apply to zone disks.

The following limitations apply to zone movement and its supported VM configurations:

- Failover is limited to another availability zone in the same region. It doesn't protect against a regional outage or an outage that affects multiple zones.
- Failover can fail when the VM size has insufficient capacity in the target zone.
- VM scale sets, availability set VMs, and Spot VMs aren't supported.
- Azure Site Recovery isn't supported for VMs with zone resilience enabled.
- On-demand capacity reservations, dedicated hosts, and proximity placement groups aren't supported.
- The feature doesn't provide automatic failover, application-level consistency, traffic failover, recovery plans, or failback orchestration.

## Prepare a VM for zone failover

Create a VM that meets every requirement before you enable zone movement. Enablement must occur while the source availability zone is healthy.

1. In the [Azure portal](https://portal.azure.com/), create a VM in a specific availability zone.
2. On the **Disks** tab, select **Premium SSD ZRS** or **Standard SSD ZRS** for the OS disk and every data disk.
3. Configure only supported zone-redundant Standard SKU network resources.
4. Create the VM.

## Enable zone movement

Enable zone movement when you create a VM or on an eligible existing zonal VM. You must deallocate an existing VM before you can enable zone movement; a new VM doesn't need a separate deallocation step. Enable zone movement while the source zone is healthy.

# [Azure portal](#tab/azure-portal-enable)
To enable zone movement when you create a VM:

1. Sign in to the [Azure portal](https://portal.azure.com/), and start creating a VM.
2. On the **Basics** tab, select a region that supports availability zones. Set **Availability options** to **Availability zone**, and select a specific **Availability zone**.
3. Under **Availability zone**, select **Protect VM from zonal-failure with Zone resilience (Preview)**.
4. In the **Zone resilience (Preview)** pane, select **Enable Zone resilience (Preview)**. Review the configuration requirements, and select **Save**.

    [![Screenshot of the VM creation page with the zone resilience link, enable checkbox, and Save button highlighted.](media/zone-resilience/zone-resilience-enable-new-vm.png)](media/zone-resilience/zone-resilience-enable-new-vm.png#lightbox)
5. On the **Disks** tab, confirm that the OS disk and every data disk use **Premium SSD ZRS** or **Standard SSD ZRS**. Configure supported network resources and the remaining VM settings.
6. Select **Review + create**, and then select **Create** after validation succeeds.

To enable zone movement on an eligible existing zonal VM:

1. In the Azure portal, open the VM, and select **Overview**.
2. Select **Stop**, confirm the operation, and wait until the VM status is **Stopped (deallocated)**. Stopping the VM interrupts the workload.
3. On **Overview**, under **Availability + scaling**, select the current value of **Zone Resilience (Preview)**.
4. In the **Zone resilience (Preview)** pane, select **Enable Zone resilience (Preview)**, review the configuration requirements, and select **Save**.

    [![Screenshot of an existing VM overview and the zone resilience pane with the enable checkbox highlighted.](media/zone-resilience/zone-resilience-enable-existing-vm.png)](media/zone-resilience/zone-resilience-enable-existing-vm.png#lightbox)
5. After the update succeeds, select **Start** on **Overview**.
6. Confirm that **Zone Resilience (Preview)** shows **Enabled**.

# [Azure CLI](#tab/azure-cli-enable)
Use Azure CLI 2.87.0 or later. Confirm your installed version with `az version`. This version introduces zone movement and force deallocation support; see the [Azure CLI release notes](/en-us/cli/azure/release-notes-azure-cli#june-02-2026).

To create a zonal Linux VM with a ZRS OS disk and zone movement enabled, run [az vm create](/en-us/cli/azure/vm#az-vm-create). This example doesn't create a public IP address. Add supported zone-redundant network resources for your workload.

```azurecli
az vm create \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>" \
  --location "<region>" \
  --zone "<source-zone>" \
  --image Ubuntu2204 \
  --size "<vm-size>" \
  --admin-username azureuser \
  --generate-ssh-keys \
  --storage-sku Premium_ZRS \
  --public-ip-address "" \
  --zone-movement true
```

To enable zone movement on an eligible existing zonal VM, deallocate it first:

```azurecli
az vm deallocate \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>"
```

After the VM is deallocated, run [az vm update](/en-us/cli/azure/vm#az-vm-update):

```azurecli
az vm update \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>" \
  --zone-movement true
```

When the update succeeds, start the VM:

```azurecli
az vm start \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>"
```

Confirm that zone movement is enabled:

```azurecli
az vm show \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>" \
  --query resiliencyProfile.zoneMovement.isEnabled \
  --output tsv
```

The command returns `true`.

# [Azure PowerShell](#tab/azure-powershell-enable)
Use a version of Az.Compute that includes [Set-AzVMZoneMovement](/en-us/powershell/module/az.compute/set-azvmzonemovement) and supports `Stop-AzVM -ForceDeallocate`. Confirm that the zone movement cmdlet is available with `Get-Command Set-AzVMZoneMovement`, and check the deallocation parameters with `Get-Command Stop-AzVM -Syntax`.

For a new VM, pass the `PSVirtualMachine` configuration from `New-AzVMConfig` through `Set-AzVMZoneMovement -IsEnabled $true` before you call `New-AzVM`. Configure the required zone, ZRS disks, and network resources on the VM configuration.

To enable zone movement on an eligible existing zonal VM, use [Get-AzVM](/en-us/powershell/module/az.compute/get-azvm), [Set-AzVMZoneMovement](/en-us/powershell/module/az.compute/set-azvmzonemovement), and [Update-AzVM](/en-us/powershell/module/az.compute/update-azvm):

```azurepowershell
$resourceGroupName = "<resource-group-name>"
$vmName = "<vm-name>"

Stop-AzVM `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName `
  -Force
```

After the VM is deallocated, enable zone movement:

```azurepowershell
$vm = Get-AzVM `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName

$vm = Set-AzVMZoneMovement -VM $vm -IsEnabled $true

Update-AzVM `
  -ResourceGroupName $resourceGroupName `
  -VM $vm
```

After the update succeeds, start the VM:

```azurepowershell
Start-AzVM `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName
```

Confirm that zone movement is enabled:

```azurepowershell
$vm = Get-AzVM `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName

$vm.ResiliencyProfile.ZoneMovement.IsEnabled
```

The command returns `True`.

# [Bicep](#tab/bicep-enable)
To create a new zonal VM with a Premium SSD ZRS OS disk and zone movement enabled, add the following VM resource excerpt to a complete Bicep template. Define `vmName` and `location` in that template, and include the other VM properties required for your deployment. You don't need to deallocate the VM when creating it.

```bicep
@description('Availability zone for the virtual machine.')
@allowed([
  '1'
  '2'
  '3'
])
param availabilityZone string = '1'

resource vm 'Microsoft.Compute/virtualMachines@2026-03-01' = {
  name: vmName
  location: location
  zones: [
    availabilityZone
  ]
  properties: {
    storageProfile: {
      osDisk: {
        name: '${vmName}-osdisk'
        createOption: 'FromImage'
        caching: 'ReadWrite'
        deleteOption: 'Delete'
        managedDisk: {
          storageAccountType: 'Premium_ZRS'
        }
      }
      dataDisks: []
    }
    resiliencyProfile: {
      zoneMovement: {
        isEnabled: true
      }
    }
  }
}
```

Next, deploy the complete template from a local file named `enable-zone-movement.bicep`:

```azurecli
az deployment group create \
  --resource-group "<resource-group-name>" \
  --template-file "./enable-zone-movement.bicep" \
  --parameters vmName="<vm-name>" availabilityZone="<source-zone>"
```

Wait for deployment to succeed before you initiate a zone move.

For an eligible existing zonal VM, set `zoneMovement.isEnabled` to `true` in its complete Bicep definition while the source zone is healthy. Preserve its current zone, disks, network interfaces, and other settings. Don't use the new-VM excerpt's `osDisk.createOption: 'FromImage'` to update an existing VM.

Deallocate the existing VM:

```azurecli
az vm deallocate \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>"
```

After the VM is deallocated, deploy its complete Bicep template:

```azurecli
az deployment group create \
  --resource-group "<resource-group-name>" \
  --template-file "./enable-existing-zone-movement.bicep" \
  --parameters vmName="<vm-name>"
```

When the deployment succeeds, start the VM:

```azurecli
az vm start \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>"
```

---

## Fail over a VM to another zone

Important

Zone resilience for Azure VMs is in preview. Use this preview only for evaluation and testing with nonproduction VMs. Don't use it for production VMs. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

See Limitations. For eligible nonproduction VMs, first confirm that an availability zone failure affects the VM. Monitor individual VM health with [Azure Resource Health](/en-us/azure/service-health/resource-health-overview), and monitor broader service issues with [Azure Service Health](/en-us/azure/service-health/overview).

Choose a target zone that supports your VM size and has sufficient capacity.

Warning

Force deallocation stops the VM and discards its in-memory state. Start failover only after you confirm the impact on your workload and its dependencies.

Use Azure CLI to orchestrate failover. With the Azure portal, Azure PowerShell, or Bicep, perform each failover operation in order.

# [Azure portal](#tab/azure-portal-recover)
Use the portal when the VM is already deallocated or can be stopped normally. If normal deallocation can't complete, use the Azure CLI, Azure PowerShell, or Bicep procedure for force deallocation.

1. In the [Azure portal](https://portal.azure.com/), open the VM, and select **Overview**.
2. If the VM isn't already deallocated, select **Stop**, confirm the operation, and wait until its status is **Stopped (deallocated)**. Don't continue if deallocation fails.
3. Under **Availability + scaling**, next to **Availability zone**, select **(edit)**.

    [![Screenshot of the VM overview with the edit link next to Availability zone highlighted.](media/zone-resilience/zone-resilience-edit-availability-zone.png)](media/zone-resilience/zone-resilience-edit-availability-zone.png#lightbox)
4. On the **Availability Zones** tab, select the target **Availability zone**, and select **Apply**.

    [![Screenshot of the Availability Zones tab with the deallocated status, target zone selector, and Apply button highlighted.](media/zone-resilience/zone-resilience-apply-availability-zone.png)](media/zone-resilience/zone-resilience-apply-availability-zone.png#lightbox)
5. Wait for the update to succeed, and confirm that **Availability zone** reports the target zone. If the update fails, review the error and VM state before continuing.
6. Return to **Overview**, and select **Start**.
7. Complete the checks in Verify failover succeeded before restoring traffic.

The VM remains deallocated after you apply the zone change. Start the VM in target zone post zone change operation completes successfully to resume normal operations by selecting **Start** in the Azure portal.

# [Azure CLI](#tab/azure-cli-recover)
Run [az vm update](/en-us/cli/azure/vm#az-vm-update) with the target zone:

```azurecli
az vm update \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>" \
  --zone "<target-zone>"
```

The command force deallocates the VM, updates its availability zone, and starts the VM in the target zone. The command waits for each operation to finish. If the zone update fails, Azure CLI attempts to restart the VM before it returns the update error.

Note

Don't deallocate the VM separately. Azure CLI handles deallocation as part of the zone update.

# [Azure PowerShell](#tab/azure-powershell-recover)
Azure PowerShell doesn't provide a single cmdlet that orchestrates zone failover. Run the following cmdlets in order, and wait for each cmdlet to finish before you continue:

```azurepowershell
$resourceGroupName = "<resource-group-name>"
$vmName = "<vm-name>"
$targetZone = "<target-zone>"

Stop-AzVM `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName `
  -ForceDeallocate `
  -Force

$vm = Get-AzVM `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName

$vm.Zones = [string[]]@($targetZone)

Update-AzVM `
  -ResourceGroupName $resourceGroupName `
  -VM $vm

Start-AzVM `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName
```

`Stop-AzVM -ForceDeallocate` releases or isolates the source-zone resources. Setting `Zones` and calling `Update-AzVM` changes the VM placement. `Start-AzVM` then starts the VM in the target zone.

Important

Unlike the Azure CLI failover command, this PowerShell sequence isn't transactional. If `Update-AzVM` fails, review the error and the VM state before you run `Start-AzVM`.

# [Bicep](#tab/bicep-recover)
Bicep updates the VM's zone placement, but doesn't deallocate or start the VM. Run the following steps in order, waiting for each command to finish before continuing.

1. Force-deallocate the existing VM.

    ```azurecli
    az vm deallocate \
      --resource-group "<resource-group-name>" \
      --name "<vm-name>" \
      --force-deallocate
    ```
2. In a complete Bicep definition of the **existing** VM, set `zones` to the healthy target zone:

    ```bicep
    @description('Healthy target zone in the VM region.')
    param targetZone string
    
    resource vm 'Microsoft.Compute/virtualMachines@2026-03-01' = {
      name: vmName
      location: location
      zones: [
        targetZone
      ]
      properties: {
        resiliencyProfile: {
          zoneMovement: {
            isEnabled: true
          }
        }
      }
    }
    ```

    This example is an excerpt, not a deployable VM definition. Keep the existing VM's full configuration, disk attachments, and network interfaces in your Bicep file. Don't reuse a new-VM template with `osDisk.createOption: 'FromImage'` to update an existing VM.

    Deploy the complete file after force-deallocation succeeds.

    ```azurecli
    az deployment group create \
      --resource-group "<resource-group-name>" \
      --template-file "./move-vm-zone.bicep" \
      --parameters vmName="<vm-name>" targetZone="<target-zone>"
    ```
3. After the deployment succeeds and the VM reports the target zone, start it.

    ```azurecli
    az vm start \
      --resource-group "<resource-group-name>" \
      --name "<vm-name>"
    ```

If the deployment fails, inspect the error and VM state before starting the VM. Verify the disks, network configuration, and workload before restoring traffic.

---

## Verify failover succeeded

After failover finishes, verify the VM and the workload before you restore traffic:

1. Confirm that the VM power state is **Running**.
2. Confirm that the VM reports the selected target availability zone.
3. Confirm that the expected OS and data disks are attached.
4. Confirm that the NIC, subnet, network security group, load balancer, and public IP associations are correct for your configuration.
5. Confirm that VM extensions and management settings are present and healthy.
6. Connect to the VM and verify operating system and application health.
7. Run workload-specific data consistency checks.
8. Restore traffic only after your health checks succeed.

Use the Azure portal, Azure CLI, or Azure PowerShell to check the VM state and zone:

# [Azure portal](#tab/azure-portal-verify)
1. In the [Azure portal](https://portal.azure.com/), open the VM, and select **Overview**.
2. Confirm that **Status** is **Running**.
3. Under **Availability + scaling**, confirm that **Availability zone** is the target zone and **Zone Resilience (Preview)** is **Enabled**.

# [Azure CLI](#tab/azure-cli-verify)
```azurecli
az vm show \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>" \
  --show-details \
  --query "{zone:zones[0], zoneMovementEnabled:resiliencyProfile.zoneMovement.isEnabled, powerState:powerState}" \
  --output table
```

Confirm that `zone` is the target zone, `zoneMovementEnabled` is `true`, and `powerState` is `VM running`.

# [Azure PowerShell](#tab/azure-powershell-verify)
```azurepowershell
$vm = Get-AzVM `
    -ResourceGroupName "<resource-group-name>" `
    -Name "<vm-name>" `
    -Status

$vm.Zones
$vm.ResiliencyProfile.ZoneMovement.IsEnabled
$vm.Statuses | Select-Object Code, DisplayStatus
```

Confirm that `Zones` contains the target zone, `IsEnabled` is `True`, and the power state is **VM running**.

---

## Troubleshoot failover

Match the error identifier or its message to the operation you attempted:

| Error identifier | When it occurs | What to do |
| --- | --- | --- |
| `ZoneMovementUpdateRequiresDeallocatedVM` | Enabling or disabling zone movement on a VM that isn't deallocated. | Deallocate the VM, retry the enable or disable update, and start the VM after it succeeds. |
| `OperationNotAllowedForNonZRSDisks` | The OS disk or an attached data disk doesn't use supported ZRS storage. | Use Premium SSD ZRS or Standard SSD ZRS for every disk before enabling zone movement. |
| `ForceDeallocateVMNotAllowedForNonResilientVM` | Force deallocation was requested for a VM without zone movement enabled. | If the source zone is healthy, deallocate normally and enable zone movement before retrying. If the source zone is unavailable, contact Azure support. |
| `OperationNotAllowedOnNullCurrentPowerStateForZonePatch` | A zone update was attempted before the affected VM reached **Deallocated**. | Force-deallocate the enabled VM, confirm it reaches **Deallocated**, and retry the zone update. |
| `OperationNotAllowedForNonZonalVM` | A zone update was requested for a regional VM without a pinned zone. | Confirm that the VM is zonal. This zone-update workflow applies only to zonal VMs. |
| `VMZoneMigrationNotCompleted` | The VM was started before zone migration finished or after migration failed. | Wait for the zone update to succeed, then retry the start. If the error persists, open an Azure support request. |

If the VM can't start because the target zone lacks capacity, select another supported zone. If the VM starts but the workload is unhealthy, complete the checks in Verify failover succeeded before restoring traffic. For other errors, review Azure service health and the operation details. If failover remains blocked, open an Azure support request.

## Disable zone movement

You must deallocate the VM before you disable zone movement. Deallocation interrupts the workload. Complete each operation before continuing, and start the VM only after the update succeeds:

# [Azure portal](#tab/azure-portal-disable)
1. In the [Azure portal](https://portal.azure.com/), open the VM, and select **Overview**.
2. Select **Stop**, confirm the operation, and wait until the VM status is **Stopped (deallocated)**.
3. Under **Availability + scaling**, select **Enabled** next to **Zone Resilience (Preview)**.
4. In the **Zone resilience (Preview)** pane, clear **Enable Zone resilience (Preview)**, and select **Save**.
5. After the update succeeds, confirm that **Zone Resilience (Preview)** shows **Disabled**, and select **Start**.

# [Azure CLI](#tab/azure-cli-disable)
```azurecli
az vm deallocate \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>"
```

Deallocate the VM, and then disable zone movement:

```azurecli
az vm update \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>" \
  --zone-movement false
```

After the update succeeds, start the VM:

```azurecli
az vm start \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>"
```

# [Azure PowerShell](#tab/azure-powershell-disable)
```azurepowershell
$resourceGroupName = "<resource-group-name>"
$vmName = "<vm-name>"

Stop-AzVM `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName `
  -Force
```

After the VM is deallocated, disable zone movement:

```azurepowershell
$vm = Get-AzVM `
    -ResourceGroupName $resourceGroupName `
    -Name $vmName

$vm = Set-AzVMZoneMovement -VM $vm -IsEnabled $false

Update-AzVM `
    -ResourceGroupName $resourceGroupName `
    -VM $vm
```

After the update succeeds, start the VM:

```azurepowershell
Start-AzVM `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName
```

# [Bicep](#tab/bicep-disable)
In the complete Bicep definition of the existing VM, set `zoneMovement.isEnabled` to `false`. The following resource block is an excerpt. Keep the VM's current zone, disks, network interfaces, and other configuration in the deployed template.

```bicep
resource vm 'Microsoft.Compute/virtualMachines@2026-03-01' = {
  name: vmName
  location: location
  properties: {
    resiliencyProfile: {
      zoneMovement: {
        isEnabled: false
      }
    }
  }
}
```

Deallocate the VM:

```azurecli
az vm deallocate \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>"
```

When the VM is deallocated, deploy the complete template from a local file named `disable-zone-movement.bicep`:

```azurecli
az deployment group create \
  --resource-group "<resource-group-name>" \
  --template-file "./disable-zone-movement.bicep" \
  --parameters vmName="<vm-name>"
```

After the deployment succeeds, start the VM:

```azurecli
az vm start \
  --resource-group "<resource-group-name>" \
  --name "<vm-name>"
```

---

## Frequently asked questions

### Does failover happen automatically or keep the workload running?

No. You must initiate failover for a VM with zone resilience enabled. The workload is unavailable while the VM is force-deallocated and started in the target zone. Zone resilience doesn't provide automatic failover, uninterrupted service, or application-level recovery orchestration. For high availability across zones, [deploy multiple VMs across availability zones](disks-high-availability#deploy-vms-and-disks-across-three-availability-zones) and distribute traffic between them.

### What data does the near-zero RPO cover?

The near-zero RPO applies to data committed to supported ZRS disks. It doesn't apply to active requests, in-memory data, temporary disks, or application state that isn't written to those disks.

### When should I use zone resilience instead of Azure Site Recovery for zonal failover?

Important

Zone resilience for Azure VMs is in preview. Use this preview only for evaluation and testing with nonproduction VMs. Don't use it for production VMs. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

See Limitations. Both options support customer-initiated failover to another zone in the same region, but they use different disk and VM recovery models:

| Decision factor | Zone resilience for Azure VMs (Preview) | Azure Site Recovery zone-to-zone disaster recovery |
| --- | --- | --- |
| Managed disks | Requires Premium SSD ZRS or Standard SSD ZRS for the OS disk and every data disk. Data committed to these disks has a near-zero RPO. | Supports eligible LRS disks through replication. ZRS-managed disks aren't supported for zone-to-zone disaster recovery. There's no defined RPO SLA. |
| Failover model | Changes the zone of the existing VM and reuses its supported disks and configuration. | Replicates the VM before an outage and creates a recovery VM in a different resource group during failover. Supports failback. |
| Choose this option when | You need to retain the existing VM resource and its supported configuration, and you can use ZRS disks. | You need zone-to-zone disaster recovery for a VM with supported LRS disks in a supported region, and you can set up replication in advance. |

For supported regions, disk restrictions, and networking behavior for Azure Site Recovery, see [Enable Azure VM disaster recovery between availability zones](/en-us/azure/site-recovery/azure-to-azure-how-to-enable-zone-to-zone-disaster-recovery) and the [Azure Site Recovery support matrix](/en-us/azure/site-recovery/azure-to-azure-support-matrix#replicated-machines-storage).

### Which advanced capabilities aren't supported?

Zone resilience doesn't provide application-level consistency, traffic failover, recovery plans, or failback orchestration. Azure Site Recovery, on-demand capacity reservations, dedicated hosts, and proximity placement groups aren't supported for VMs with zone resilience enabled. Review Limitations before you enable the feature.

## Cost

Important

There's no feature charge for zone resilience for Azure VMs during preview. It will be a paid feature at general availability. Pricing details will be published with the general availability release.

Standard charges apply for VMs, ZRS managed disks, and network resources. For managed disk pricing, see [Azure managed disks pricing](https://azure.microsoft.com/pricing/details/managed-disks/).