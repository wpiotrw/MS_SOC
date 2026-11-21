---
layout: Conceptual
title: Copy snapshot of managed disk to subscription (Windows) - PowerShell - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/scripts/virtual-machines-powershell-sample-copy-snapshot-to-same-or-different-subscription
breadcrumb_path: ../../breadcrumb/azure-compute/toc.json
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
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
description: Azure PowerShell Script Sample -  Copy (move) snapshot of a managed disk to same or different subscription
author: ushnaarshadkhan
ms.custom: devx-track-azurepowershell
ms.service: azure-disk-storage
ms.topic: sample
ms.tgt_pltfrm: vm-windows
ms.date: 2023-03-01T00:00:00.0000000Z
ms.author: uarshadkhan
locale: en-us
document_id: 1e095220-1139-ac0f-cde1-06867e7a4358
document_version_independent_id: 357c559a-ccfd-eb07-01e1-6e7e002c5066
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/scripts/virtual-machines-powershell-sample-copy-snapshot-to-same-or-different-subscription.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/scripts/virtual-machines-powershell-sample-copy-snapshot-to-same-or-different-subscription
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/scripts/virtual-machines-powershell-sample-copy-snapshot-to-same-or-different-subscription.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/f7db5823-dfbf-4e94-9016-c24311b90d7e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/a5ab72d9-1367-4994-84a6-d9964cd9936d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
platformId: 0325f7aa-9ba3-484a-1251-dbf8c6f042a0
---

# Copy snapshot of managed disk to subscription (Windows) - PowerShell - Azure Virtual Machines | Microsoft Learn

This script copies a snapshot of a managed disk to same or different subscription. Use this script for the following scenarios:

1. Migrate a snapshot in Premium storage (Premium\_LRS) to Standard storage (Standard\_LRS or Standard\_ZRS) to reduce your cost.
2. Migrate a snapshot from locally redundant storage (Premium\_LRS, Standard\_LRS) to zone redundant storage (Standard\_ZRS) to benefit from the higher reliability of ZRS storage.
3. Move a snapshot to different subscription in the same region for longer retention.

If needed, install the Azure PowerShell module using the instructions found in the [Azure PowerShell guide](/en-us/powershell/azure/), and then run `Connect-AzAccount` to create a connection with Azure. Also, you need to have an SSH public key named `id_rsa.pub` in the .ssh directory of your user profile.

If you don't have an Azure account, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

## Sample script

```powershell
#Provide the subscription Id of the subscription where snapshot exists
$sourceSubscriptionId='yourSourceSubscriptionId'

#Provide the name of your resource group where snapshot exists
$sourceResourceGroupName='yourResourceGroupName'

#Provide the name of the snapshot
$snapshotName='yourSnapshotName'

#Set the context to the subscription Id where snapshot exists
Select-AzSubscription -SubscriptionId $sourceSubscriptionId

#Get the source snapshot
$snapshot= Get-AzSnapshot -ResourceGroupName $sourceResourceGroupName -Name $snapshotName

#Provide the subscription Id of the subscription where snapshot will be copied to
#If snapshot is copied to the same subscription then you can skip this step
$targetSubscriptionId='yourTargetSubscriptionId'

#Name of the resource group where snapshot will be copied to
$targetResourceGroupName='yourTargetResourceGroupName'

#Set the context to the subscription Id where snapshot will be copied to
#If snapshot is copied to the same subscription then you can skip this step
Select-AzSubscription -SubscriptionId $targetSubscriptionId

#We recommend you to store your snapshots in Standard storage to reduce cost. Please use Standard_ZRS in regions where zone redundant storage (ZRS) is available, otherwise use Standard_LRS
#Please check out the availability of ZRS here: https://docs.microsoft.com/en-us/Az.Storage/common/storage-redundancy-zrs#support-coverage-and-regional-availability
$snapshotConfig = New-AzSnapshotConfig -SourceResourceId $snapshot.Id -Location $snapshot.Location -CreateOption Copy -SkuName Standard_LRS

#Create a new snapshot in the target subscription and resource group
New-AzSnapshot -Snapshot $snapshotConfig -SnapshotName $snapshotName -ResourceGroupName $targetResourceGroupName 
```

## Script explanation

This script uses following commands to create a snapshot in the target subscription using the Id of the source snapshot. Each command in the table links to command specific documentation.

| Command | Notes |
| --- | --- |
| [New-AzSnapshotConfig](/en-us/powershell/module/az.compute/new-azsnapshotconfig) | Creates snapshot configuration that is used for snapshot creation. It includes the resource Id of the parent snapshot and location that is same as the parent snapshot. |
| [New-AzSnapshot](/en-us/powershell/module/az.compute/new-azsnapshot) | Creates a snapshot using snapshot configuration, snapshot name, and resource group name passed as parameters. |