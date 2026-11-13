---
layout: Conceptual
title: Deploy a Premium SSD v2 managed disk - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-deploy-premium-v2
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
author: roygara
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: rogarana
ms.update-cycle: 365-days
ms.service: azure-disk-storage
description: Learn how to deploy zonal and nonzonal Premium SSD v2 managed disks and review their regional availability.
ms.date: 2026-08-11T00:00:00.0000000Z
ms.topic: how-to
ai-usage: ai-assisted
ms.custom:
- references_regions
- devx-track-azurecli
- devx-track-azurepowershell
- innovation-engine
- sfi-ropc-nochange\portal
- portal
locale: en-us
document_id: 6c5c02c7-b0f1-0632-9140-a0fd9418a2c9
document_version_independent_id: a08e9f6b-7124-797e-b93d-3e5fa5d1a59a
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/disks-deploy-premium-v2.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli
toc_rel: toc.json
asset_id: virtual-machines/disks-deploy-premium-v2
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/disks-deploy-premium-v2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/089c8ba6-d135-43ff-bfaf-b8197fb72fb9
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/32516e21-6665-416f-be21-413febe47d91
platformId: b628582e-ef9b-822a-8fef-d8926ff61dc4
---

# Deploy a Premium SSD v2 managed disk - Azure Virtual Machines | Microsoft Learn

Azure Premium SSD v2 is designed for I/O-intensive enterprise workloads that require submillisecond disk latency, high IOPS, and high throughput at a low cost. Premium SSD v2 is suited for workloads such as SQL Server, Oracle, MariaDB, SAP, Cassandra, MongoDB, big data and analytics, and gaming on virtual machines or stateful containers. For conceptual information on Premium SSD v2, see [Premium SSD v2](/en-us/azure/virtual-machines/disks-types#premium-ssd-v2).

You can deploy Premium SSD v2 disks as zonal resources or as [nonzonal resources](/en-us/azure/reliability/availability-zones-zonal-resource-resiliency#resource-deployment-types). Use a zonal disk when your workload runs in an availability zone. Use a nonzonal disk for a nonzonal VM or in a region without availability zones.

Premium SSD v2 disks support a 4k physical sector size by default, but you can configure them to use a 512E sector size. While most applications are compatible with 4k sector sizes, some require 512-byte sector sizes. Oracle Database, for example, requires release 12.2 or later to support 4k native disks.

## Premium SSD v2 limitations

- Premium SSD v2 disks can't be used as an OS disk or with [Azure Compute Gallery](/en-us/azure/virtual-machines/azure-compute-gallery).
- Premium SSD v2 doesn't support host caching.
- In most regions that support availability zones, you can only attach Premium SSD v2 disks to zonal VMs. When you create a new VM, specify the availability zone you want before adding Premium SSD v2 disks to your configuration.
    - In a subset of regions that support availability zones, you can attach [nonzonal](/en-us/azure/reliability/availability-zones-zonal-resource-resiliency#resource-deployment-types) Premium SSD v2 disks to nonzonal VMs, which have [extra limitations](/en-us/azure/virtual-machines/disks-deploy-premium-v2#limitations-for-nonzonal-disks-in-regions-with-availability-zones).

## Regional availability

### Zonal disks

Currently only available in the following regions:

| *Three Availability Zones* |
| --- |
| Austria East  Australia East  Brazil South  Canada Central  Central India  China North 3  East Asia  North Europe, West Europe  France Central  Germany West Central  Indonesia Central  Israel Central  Italy North  Japan East, Japan West  Korea Central  Malaysia West  Mexico Central  New Zealand North  Norway East  Poland Central  South African North  Southeast Asia  Spain Central  Sweden Central  Switzerland North  UAE North  UK South  Central US, East US, East US 2, South Central US, West US 2, West US 3  US Gov Virginia |

To learn when support for particular regions was added, see either [Azure Updates](https://azure.microsoft.com/updates/?query=disk%20storage) or [What's new for Azure Disk Storage](/en-us/azure/virtual-machines/disks-whats-new).

### Nonzonal disks

Azure supports nonzonal (regional) Premium SSD v2 deployments in the following regions. A nonzonal disk isn't explicitly assigned to an availability zone.

| *Regions without availability zones* | *Regions with availability zones* |
| --- | --- |
| - Australia Central 2  - Australia Southeast  - Brazil Southeast  - Canada East  - Germany North  - North Central US  - Norway West  - South India  - Switzerland West  - Taiwan North  - UK West  - US Gov Arizona  - West Central US  - West US | - Australia East  - Austria East  - Brazil South  - Canada Central  - Central India  - Central US  - East Asia  - East US  - East US 2  - France Central  - Germany West Central  - India South Central  - Indonesia Central  - Italy North  - Japan East  - Japan West  - Korea Central  - Malaysia West  - Mexico Central  - New Zealand North  - North Europe  - Norway East  - Poland Central  - South Africa North  - South Central US  - Spain Central  - South African North  - Southeast Asia  - Sweden Central  - Switzerland North  - UK South  - West Europe  - West US 2  - West US 3 |

To learn when support for particular regions was added, see either [Azure Updates](https://azure.microsoft.com/updates/?query=disk%20storage) or [What's new for Azure Disk Storage](/en-us/azure/virtual-machines/disks-whats-new).

## Prerequisites

- Install either the latest [Azure CLI](/en-us/cli/azure/install-azure-cli) or the latest [Azure PowerShell module](/en-us/powershell/azure/install-azure-powershell).

## Determine region availability programmatically

Because not every region and zone supports Premium SSD v2 disks, use the Azure CLI or PowerShell to check region and zone support.

For nonzonal deployments, also check the [nonzonal regional availability list](/en-us/azure/virtual-machines/disks-deploy-premium-v2?tabs=azure-cli#nonzonal-disks).

# [Azure CLI](#tab/azure-cli)
To find the regions and zones that support Premium SSD v2 disks, replace `yourSubscriptionId` with your subscription, and then run the [az vm list-skus](/en-us/cli/azure/vm#az-vm-list-skus) command:

```azurecli
az login

subscriptionId="<yourSubscriptionId>"

az account set --subscription $subscriptionId

az vm list-skus --resource-type disks --query "[?name=='PremiumV2_LRS'].{Region:locationInfo[0].location, Zones:locationInfo[0].zones}" 
```

# [PowerShell](#tab/azure-powershell)
To find the regions and zones that support Premium SSD v2 disks, replace `yourSubscriptionId` with your subscription, and then run the [Get-AzComputeResourceSku](/en-us/powershell/module/az.compute/get-azcomputeresourcesku) command:

```powershell
Connect-AzAccount

$subscriptionId="yourSubscriptionId"

Set-AzContext -Subscription $subscriptionId

Get-AzComputeResourceSku | where {$_.ResourceType -eq 'disks' -and $_.Name -eq 'Premiumv2_LRS'} 
```

# [Azure portal](#tab/portal)
To programmatically determine the regions and zones you can deploy to, use either Azure CLI or Azure PowerShell.

---

After you identify a supported region and zone, choose the deployment type that matches your VM.

## Deploy a zonal Premium SSD v2

Zonal Premium SSD v2 disks are available in select regions with availability zones.

# [Azure CLI](#tab/azure-cli)
Create a Premium SSD v2 in an availability zone by using the [az disk create](/en-us/cli/azure/disk#az-disk-create) command. Then create a VM in the same region and availability zone that supports Premium Storage and attach the disk to it by using the [az vm create](/en-us/cli/azure/vm#az-vm-create) command.

The following script creates a Premium SSD v2 with a 4k sector size. To deploy one with a 512 sector size, update the `$logicalSectorSize` parameter. Replace the values of all the variables with your own, then run the following script:

```azurecli
## Initialize variables
diskName="yourDiskName"
resourceGroupName="yourResourceGroupName"
region="yourRegionName"
zone="yourZoneNumber"
##Replace 4096 with 512 to deploy a disk with 512 sector size
logicalSectorSize=4096
vmName="yourVMName"
vmImage="Win2016Datacenter"
adminPassword="yourAdminPassword"
adminUserName="yourAdminUserName"
vmSize="Standard_D4s_v3"

## Create a Premium SSD v2
az disk create -n $diskName -g $resourceGroupName \
--size-gb 100 \
--disk-iops-read-write 5000 \
--disk-mbps-read-write 150 \
--location $region \
--zone $zone \
--sku PremiumV2_LRS \
--logical-sector-size $logicalSectorSize

## Create the VM
az vm create -n $vmName -g $resourceGroupName \
--image $vmImage \
--zone $zone \
--authentication-type password --admin-password $adminPassword --admin-username $adminUserName \
--size $vmSize \
--location $region \
--attach-data-disks $diskName
```

# [PowerShell](#tab/azure-powershell)
Create a Premium SSD v2 in an availability zone by using [New-AzDiskConfig](/en-us/powershell/module/az.compute/new-azdiskconfig) and [New-AzDisk](/en-us/powershell/module/az.compute/new-azdisk). Then create a VM in the same region and availability zone. Use [Add-AzVMDataDisk](/en-us/powershell/module/az.compute/add-azvmdatadisk) to add the disk to the VM configuration, and then use [Update-AzVM](/en-us/powershell/module/az.compute/update-azvm) to apply the change in Azure.

The following script creates a Premium SSD v2 with a 4k sector size. To deploy one with a 512 sector size, update the `$logicalSectorSize` parameter. Replace the values of all the variables with your own, then run the following script:

```powershell
# Initialize variables
$resourceGroupName = "yourResourceGroupName"
$region = "useast"
$zone = "yourZoneNumber"
$diskName = "yourDiskName"
$diskSizeInGiB = 100
$diskIOPS = 5000
$diskThroughputInMBPS = 150
#To use a 512 sector size, replace 4096 with 512
$logicalSectorSize=4096
$lun = 1
$vmName = "yourVMName"
$vmImage = "Win2016Datacenter"
$vmSize = "Standard_D4s_v3"
$vmAdminUser = "yourAdminUserName"
$vmAdminPassword = ConvertTo-SecureString "yourAdminUserPassword" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ($vmAdminUser, $vmAdminPassword);

# Create a Premium SSD v2
$diskconfig = New-AzDiskConfig `
-Location $region `
-Zone $zone `
-DiskSizeGB $diskSizeInGiB `
-DiskIOPSReadWrite $diskIOPS `
-DiskMBpsReadWrite $diskThroughputInMBPS `
-AccountType PremiumV2_LRS `
-LogicalSectorSize $logicalSectorSize `
-CreateOption Empty

New-AzDisk `
-ResourceGroupName $resourceGroupName `
-DiskName $diskName `
-Disk $diskconfig

# Create the VM
New-AzVm `
    -ResourceGroupName $resourceGroupName `
    -Name $vmName `
    -Location $region `
    -Zone $zone `
    -Image $vmImage `
    -Size $vmSize `
    -Credential $credential

# Attach the disk to the VM
$vm = Get-AzVM -ResourceGroupName $resourceGroupName -Name $vmName
$disk = Get-AzDisk -ResourceGroupName $resourceGroupName -Name $diskName
$vm = Add-AzVMDataDisk -VM $vm -Name $diskName -CreateOption Attach -ManagedDiskId $disk.Id -Lun $lun
Update-AzVM -VM $vm -ResourceGroupName $resourceGroupName
```

# [Azure portal](#tab/portal)
1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Navigate to **Virtual machines** and follow the normal VM creation process.
3. On the **Basics** page, select a supported region and set **Availability options** to **Availability zone**.

    For a zonal deployment, create a zonal VM or Virtual Machine Scale Set, and specify the availability zone you want before adding Premium SSD v2 disks to your configuration.
4. Select one or more of the zones.
5. Fill in the rest of the values on the page as you like.

    [![Screenshot of the basics page, region and availability options and zones highlighted.](media/disks-deploy-premium-v2/premv2-portal-deploy.png)](media/disks-deploy-premium-v2/premv2-portal-deploy.png#lightbox)
6. Proceed to the **Disks** page.
7. Under **Data disks** select **Create and attach a new disk**.

    [![Screenshot highlighting create and attach a new disk on the disk page.](media/disks-deploy-premium-v2/premv2-create-data-disk.png)](media/disks-deploy-premium-v2/premv2-create-data-disk.png#lightbox)
8. Select the **Disk SKU** and select **Premium SSD v2**.

    [![Screenshot selecting Premium SSD v2 SKU.](media/disks-deploy-premium-v2/premv2-select.png)](media/disks-deploy-premium-v2/premv2-select.png#lightbox)
9. Select whether you'd like to deploy a 4k or 512 logical sector size.

    [![Screenshot of deployment logical sector size deployment options.](media/disks-deploy-premium-v2/premv2-sector-size.png)](media/disks-deploy-premium-v2/premv2-sector-size.png#lightbox)
10. Proceed through the rest of the VM deployment, making any choices that you desire.

You've now deployed a VM with a Premium SSD v2.

---

## Deploy a nonzonal Premium SSD v2

Deploy a nonzonal disk for a nonzonal VM in a supported region, including regions with and without availability zones.

## Additional limitations for nonzonal disks in regions with availability zones

When you attach a nonzonal Premium SSD v2 disk to a nonzonal VM in a region with availability zones, Azure runs a background copy to align the disk with the VM's availability zone and optimize latency. The copy can take up to 24 hours.

The following additional limitations apply during the background copy:

- You can't attach a nonzonal disk created from a snapshot, including an [instant access snapshot](/en-us/azure/virtual-machines/disks-instant-access-snapshots), to a nonzonal VM until the copy finishes. To check the copy status, see [Performance impact of background copy](/en-us/azure/virtual-machines/scripts/create-managed-disk-from-snapshot#performance-impact---background-copy-process).
- You can't resize the disk or change its customer-managed key.

Only one background copy can run on a nonzonal disk at a time. While a background copy is in progress, attaching the disk to a running nonzonal VM might fail. Restarting a stopped or deallocated nonzonal VM with the disk attached might also fail because the restart can trigger a second background copy.

# [Azure CLI](#tab/azure-cli)
Create a nonzonal Premium SSD v2 disk by using the [az disk create](/en-us/cli/azure/disk#az-disk-create) command. Then create a nonzonal VM in the same region that supports Premium Storage and attach the disk by using the [az vm create](/en-us/cli/azure/vm#az-vm-create) command.

The following script creates a Premium SSD v2 disk with a 4k sector size. To create a disk with a 512E sector size, change the `logicalSectorSize` value to `512`. Replace the variable values with your own before you run the script.

```azurecli
## Initialize variables
diskName="yourDiskName"
resourceGroupName="yourResourceGroupName"
region="yourRegionName"
logicalSectorSize=4096
vmName="yourVMName"
vmImage="Win2016Datacenter"
adminPassword="yourAdminPassword"
adminUserName="yourAdminUserName"
vmSize="Standard_D4s_v3"

## Create a Premium SSD v2 disk
az disk create -n $diskName -g $resourceGroupName \
--size-gb 100 \
--disk-iops-read-write 5000 \
--disk-mbps-read-write 150 \
--location $region \
--sku PremiumV2_LRS \
--logical-sector-size $logicalSectorSize

## Create the VM and attach the disk
az vm create -n $vmName -g $resourceGroupName \
--image $vmImage \
--authentication-type password --admin-password $adminPassword --admin-username $adminUserName \
--size $vmSize \
--location $region \
--attach-data-disks $diskName
```

# [PowerShell](#tab/azure-powershell)
Create a nonzonal Premium SSD v2 disk by using [New-AzDiskConfig](/en-us/powershell/module/az.compute/new-azdiskconfig) and [New-AzDisk](/en-us/powershell/module/az.compute/new-azdisk). Then create a nonzonal VM in the same region, add the disk to the VM configuration with [Add-AzVMDataDisk](/en-us/powershell/module/az.compute/add-azvmdatadisk), and apply the updated configuration with [Update-AzVM](/en-us/powershell/module/az.compute/update-azvm).

The following script creates a Premium SSD v2 disk with a 4k sector size. To create a disk with a 512E sector size, change the `$logicalSectorSize` value to `512`. Replace the variable values with your own before you run the script.

```powershell
# Initialize variables
$resourceGroupName = "yourResourceGroupName"
$region = "useast"
$diskName = "yourDiskName"
$diskSizeInGiB = 100
$diskIOPS = 5000
$diskThroughputInMBPS = 150
$logicalSectorSize = 4096
$lun = 1
$vmName = "yourVMName"
$vmImage = "Win2016Datacenter"
$vmSize = "Standard_D4s_v3"
$vmAdminUser = "yourAdminUserName"
$vmAdminPassword = ConvertTo-SecureString "yourAdminUserPassword" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ($vmAdminUser, $vmAdminPassword)

# Create a Premium SSD v2 disk
$diskConfig = New-AzDiskConfig `
    -Location $region `
    -DiskSizeGB $diskSizeInGiB `
    -DiskIOPSReadWrite $diskIOPS `
    -DiskMBpsReadWrite $diskThroughputInMBPS `
    -AccountType PremiumV2_LRS `
    -LogicalSectorSize $logicalSectorSize `
    -CreateOption Empty

New-AzDisk `
    -ResourceGroupName $resourceGroupName `
    -DiskName $diskName `
    -Disk $diskConfig

# Create the VM
New-AzVm `
    -ResourceGroupName $resourceGroupName `
    -Name $vmName `
    -Location $region `
    -Image $vmImage `
    -Size $vmSize `
    -Credential $credential

# Attach the disk to the VM
$vm = Get-AzVM -ResourceGroupName $resourceGroupName -Name $vmName
$disk = Get-AzDisk -ResourceGroupName $resourceGroupName -Name $diskName
$vm = Add-AzVMDataDisk -VM $vm -Name $diskName -CreateOption Attach -ManagedDiskId $disk.Id -Lun $lun
Update-AzVM -VM $vm -ResourceGroupName $resourceGroupName
```

# [Azure portal](#tab/portal)
1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Go to **Disks**, and create a disk.
3. Select a supported region.
4. Select **Change size**, select **Premium SSD v2**, and then select **OK**.
5. Set **Availability zone** to **No infrastructure redundancy required**.
6. On the **Advanced** tab, select a 4k or 512E logical sector size.
7. Complete the remaining settings, and then create the disk.
8. Attach the disk to a new or existing VM.

---

## Adjust disk performance

You can adjust the performance of a Premium SSD v2 four times within a 24 hour period. Creating a disk counts as one of these times, so for the first 24 hours after creating a Premium SSD v2 you can only adjust its performance up to three times.

For conceptual information on adjusting disk performance, see [Premium SSD v2 performance](/en-us/azure/virtual-machines/disks-types#premium-ssd-v2-performance).

# [Azure CLI](#tab/azure-cli)
Use the [az disk update](/en-us/cli/azure/disk#az-disk-update) command to change the performance configuration of your Premium SSD v2. For example, you can use the `disk-iops-read-write` parameter to adjust the max IOPS limit, and the `disk-mbps-read-write` parameter to adjust the max throughput limit of your Premium SSD v2.

The following command adjusts the performance of your disk. Update the values in the command, and then run it:

```azurecli
subscriptionId="<yourSubscriptionId>"
resourceGroupName="<yourResourceGroupName>"
diskName="<yourDiskName>"

az disk update --subscription $subscriptionId --resource-group $resourceGroupName --name $diskName --disk-iops-read-write=5000 --disk-mbps-read-write=200
```

# [PowerShell](#tab/azure-powershell)
Use the [New-AzDiskUpdateConfig](/en-us/powershell/module/az.compute/new-azdiskupdateconfig) command to define your new performance configuration values for your Premium SSD v2 disks, and then use the [Update-AzDisk](/en-us/powershell/module/az.compute/update-azdisk) command to apply your configuration changes to your disk. For example, you can use the `DiskIOPSReadWrite` parameter to adjust the max IOPS limit, and the `DiskMBpsReadWrite` parameter to adjust the max throughput limit of your Premium SSD v2.

The following command adjusts the performance of your disk. Update the values in the command, and then run it:

```azurepowershell
$resourceGroupName = "<yourResourceGroupName>"
$diskName = "<yourDiskName>"
$diskUpdateConfig = New-AzDiskUpdateConfig -DiskIOPSReadWrite 5000 -DiskMBpsReadWrite 200

Update-AzDisk -ResourceGroupName $resourceGroupName -DiskName $diskName -DiskUpdate $diskUpdateConfig
```

# [Azure portal](#tab/portal)
1. Navigate to the disk you'd like to modify in the [Azure portal](https://portal.azure.com/).
2. Select **Size + Performance**
3. Set the values for **Disk IOPS** or **Disk throughput (MB/s)** or both, to meet your needs, then select **Save**.

---