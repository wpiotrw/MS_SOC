---
layout: Conceptual
title: Creating Virtual Machine Restore Points using PowerShell - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/virtual-machines-create-restore-points-powershell
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
author: iamwilliew
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: wwilliams
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Creating Virtual Machine Restore Points using PowerShell
ms.subservice: recovery
ms.topic: tutorial
ms.date: 2026-10-22T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-tutorial
locale: en-us
document_id: f3054a67-7e0f-b7f8-68fd-f2d03bd633ab
document_version_independent_id: 851f101b-c146-3c4e-66fe-71dcd7060688
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/virtual-machines-create-restore-points-powershell.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/virtual-machines-create-restore-points-powershell
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/virtual-machines-create-restore-points-powershell.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 458da2fa-8cb3-da06-7bc4-4f368908c0c2
---

# Creating Virtual Machine Restore Points using PowerShell - Azure Virtual Machines | Microsoft Learn

Note

We recommend that you use the Azure Az PowerShell module to interact with Azure. To get started, see [Install Azure PowerShell](/en-us/powershell/azure/install-azure-powershell). To learn how to migrate to the Az PowerShell module, see [Migrate Azure PowerShell from AzureRM to Az](/en-us/powershell/azure/migrate-from-azurerm-to-az).

You can create Virtual Machine restore points using PowerShell scripts. The [Azure PowerShell Az](/en-us/powershell/azure/new-azureps-module-az) module is used to create and manage Azure resources from the command line or in scripts.

You can protect your data and guard against extended downtime by creating [VM restore points](virtual-machines-create-restore-points#about-virtual-machine-restore-points) at regular intervals. This article shows you how to create VM restore points, and exclude disks from the restore point, using the [Az.Compute](/en-us/powershell/module/az.compute) module. Alternatively, you can create VM restore points using the [Azure CLI](virtual-machines-create-restore-points-cli) or in the [Azure portal](virtual-machines-create-restore-points-portal).

In this tutorial, you learn how to:

- Create a VM restore point collection
- Create a VM restore point
- Track the progress of Copy operation
- Restore a VM

## Prerequisites

- Learn more about the [support requirements](concepts-restore-points) and [limitations](virtual-machines-create-restore-points#limitations) before creating a restore point.

## Step 1: Create a VM restore point collection

Use the [New-AzRestorePointCollection](/en-us/powershell/module/az.compute/new-azrestorepointcollection) cmdlet to create a VM restore point collection.

```
New-AzRestorePointCollection -ResourceGroupName ExampleRG -Name ExampleRPC -VmId “/subscriptions/{SubscriptionId}/resourcegroups/ ExampleRG/providers/microsoft.compute/virtualmachines/Example-vm-1” -Location “WestEurope”
```

## Step 2: Create a VM restore point

Create a VM restore point with the [New-AzRestorePoint](/en-us/powershell/module/az.compute/new-azrestorepoint) cmdlet as shown below:

```
New-AzRestorePoint -ResourceGroupName ExampleRG -RestorePointCollectionName ExampleRPC -Name ExampleRP
```

To create a crash-consistent restore point, set `-ConsistencyMode` to `CrashConsistent`.

```azurepowershell
New-AzRestorePoint -ResourceGroupName ExampleRG -RestorePointCollectionName ExampleRPC -Name ExampleCrashConsistentRP -ConsistencyMode CrashConsistent
```

Instant Access applies only to VMs with Premium SSD v2 or Ultra Disks as data disks. It supports both application-consistent and multi-disk crash-consistent (in preview) restore points. For instructions to enable Instant Access and create a restore point, see [Create VM restore points using APIs](create-restore-points) or [Azure CLI](virtual-machines-create-restore-points-cli).

### Exclude disks from the restore point

Exclude certain disks that you do not want to be a part of the restore point with the `-DisksToExclude` parameter, as follows:

```
New-AzRestorePoint -ResourceGroupName ExampleRG -RestorePointCollectionName ExampleRPC -Name ExampleRP -DisksToExclude “/subscriptions/{SubscriptionId}/resourcegroups/ ExampleRG/providers/Microsoft.Compute/disks/example-vm-1-data_disk_1”
```

## Step 3: Track the status of the VM restore point creation

You can track the progress of the VM restore point creation using the [Get-AzRestorePoint](/en-us/powershell/module/az.compute/get-azrestorepoint) cmdlet, as follows:

```
Get-AzRestorePoint -ResourceGroupName ExampleRG -RestorePointCollectionName ExampleRPC -Name ExampleRP
```

## Restore a VM from VM restore point

To restore a VM from a VM restore point, first restore individual disks from each disk restore point. You can also use the [ARM template](https://github.com/Azure/Virtual-Machine-Restore-Points/blob/main/RestoreVMFromRestorePoint.json) to restore a full VM along with all the disks.

```
# Create Disks from disk restore points 
$restorePoint = Get-AzRestorePoint -ResourceGroupName ExampleRG -RestorePointCollectionName ExampleRPC -Name ExampleRP 

$osDiskRestorePoint = $restorePoint.SourceMetadata.StorageProfile.OsDisk.DiskRestorePoint.Id
$dataDisk1RestorePoint = $restorePoint.sourceMetadata.storageProfile.dataDisks[0].diskRestorePoint.id
$dataDisk2RestorePoint = $restorePoint.sourceMetadata.storageProfile.dataDisks[1].diskRestorePoint.id
 
New-AzDisk -DiskName “ExampleOSDisk” (New-AzDiskConfig  -Location eastus -CreateOption Restore -SourceResourceId $osDiskRestorePoint) -ResourceGroupName ExampleRg

New-AzDisk -DiskName “ExampleDataDisk1” (New-AzDiskConfig  -Location eastus -CreateOption Restore -SourceResourceId $dataDisk1RestorePoint) -ResourceGroupName ExampleRg

New-AzDisk -DiskName “ExampleDataDisk2” (New-AzDiskConfig  -Location eastus -CreateOption Restore -SourceResourceId $dataDisk2RestorePoint) -ResourceGroupName ExampleRg

```

After you create the disks, [create a new VM](windows/create-vm-specialized-portal) and [attach these restored disks](windows/attach-disk-ps#create-and-attach-a-managed-disk) to the newly created VM.