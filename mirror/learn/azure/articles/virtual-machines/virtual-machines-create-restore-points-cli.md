---
layout: Conceptual
title: Creating Virtual Machine Restore Points using Azure CLI - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/virtual-machines-create-restore-points-cli
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
author: shsangal
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: shsangal
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Creating Virtual Machine Restore Points using Azure CLI
ms.subservice: recovery
ms.topic: tutorial
ms.date: 2026-10-22T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-tutorial, devx-track-azurecli
locale: en-us
document_id: fab2a709-16e0-d91e-1524-db4832ec2ecb
document_version_independent_id: fcefc7e9-a767-86b5-c97b-15d149ea3856
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/virtual-machines-create-restore-points-cli.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/virtual-machines-create-restore-points-cli
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/virtual-machines-create-restore-points-cli.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/089c8ba6-d135-43ff-bfaf-b8197fb72fb9
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/32516e21-6665-416f-be21-413febe47d91
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: ebc8a1a9-2584-e0b5-2bc0-d599616d2229
---

# Creating Virtual Machine Restore Points using Azure CLI - Azure Virtual Machines | Microsoft Learn

You can protect your data and guard against extended downtime by creating [VM restore points](virtual-machines-create-restore-points#about-virtual-machine-restore-points) at regular intervals. You can create VM restore points, and exclude disks while creating the restore point, using Azure CLI. Azure CLI is used to create and manage Azure resources using command line or scripts. Alternatively, you can create VM restore points using the [Azure portal](virtual-machines-create-restore-points-portal) or using [PowerShell](virtual-machines-create-restore-points-powershell).

The [az restore-point](/en-us/cli/azure/restore-point) module is used to create and manage restore points from the command line or in scripts.

In this tutorial, you learn how to:

- Create a VM restore point collection
- Create a VM restore point
- Track the progress of Copy operation
- Restore a VM

## Prerequisites

- Use the Bash environment in [Azure Cloud Shell](/en-us/azure/cloud-shell/overview). For more information, see [Get started with Azure Cloud Shell](/en-us/azure/cloud-shell/quickstart).

    [![](../reusable-content/azure-cli/media/hdi-launch-cloud-shell.png)](https://shell.azure.com)
- If you prefer to run CLI reference commands locally, [install](/en-us/cli/azure/install-azure-cli) the Azure CLI. If you're running on Windows or macOS, consider running Azure CLI in a Docker container. For more information, see [How to run the Azure CLI in a Docker container](/en-us/cli/azure/run-azure-cli-docker).

    - If you're using a local installation, sign in to the Azure CLI by using the [az login](/en-us/cli/azure/reference-index#az-login) command. To finish the authentication process, follow the steps displayed in your terminal. For other sign-in options, see [Authenticate to Azure using Azure CLI](/en-us/cli/azure/authenticate-azure-cli).
    - When you're prompted, install the Azure CLI extension on first use. For more information about extensions, see [Use and manage extensions with the Azure CLI](/en-us/cli/azure/azure-cli-extensions-overview).
    - Run [az version](/en-us/cli/azure/reference-index?#az-version) to find the version and dependent libraries that are installed. To upgrade to the latest version, run [az upgrade](/en-us/cli/azure/reference-index?#az-upgrade).

- Learn more about the [support requirements](concepts-restore-points) and [limitations](virtual-machines-create-restore-points#limitations) before creating a restore point.

## Step 1: Create a VM restore point collection

Use the [az restore-point collection create](/en-us/cli/azure/restore-point/collection#az-restore-point-collection-create) command to create a VM restore point collection, as shown below:

```
az restore-point collection create --location "norwayeast" --source-id "/subscriptions/{subscription-id}/resourceGroups/ExampleRg/providers/Microsoft.Compute/virtualMachines/ExampleVM" --tags myTag1="tagValue1" --resource-group "ExampleRg" --collection-name "ExampleRpc" 
```

### Create a VM restore point collection with instant access

Instant Access is optional and applies only to VMs with Premium SSD v2 or Ultra Disks as data disks. It supports both application-consistent and multi-disk crash-consistent (in preview) restore points. When you enable Instant Access on the restore point collection, disk restoration can begin immediately from the restore point without waiting for full hydration. This feature significantly reduces RTOs. To learn more, see [Instant Access](virtual-machines-create-restore-points#instant-access).

```
az restore-point collection create --location "norwayeast" --source-id "/subscriptions/{subscription-id}/resourceGroups/ExampleRg/providers/Microsoft.Compute/virtualMachines/ExampleVM" --tags myTag1="tagValue1" --resource-group "ExampleRg" --collection-name "ExampleRpc" --instant-access true
```

## Step 2: Create a VM restore point

Create a VM restore point with the [az restore-point create](/en-us/cli/azure/restore-point#az-restore-point-create) command as follows:

```
az restore-point create --resource-group "ExampleRg" --collection-name "ExampleRpc" --name "ExampleRp"
```

To create a crash-consistent restore point, set `--consistency-mode` to `CrashConsistent`.

### Create a VM restore point with specific instant access duration

Create a VM restore point with the [az restore-point create](/en-us/cli/azure/restore-point#az-restore-point-create) command as follows:

```
az restore-point create --resource-group "ExampleRg" --collection-name "ExampleRpc" --name "ExampleRp" --instant-access-duration "120"
```

> 
> **Note:** Instant Access duration is an optional parameter. Its an integer property set on each restore point. Specifies how long Instant Access remains active, in minutes. Valid range: 60–300 minutes. Default: 300 (5 hours).

For a multi-disk crash-consistent restore point with Instant Access (in preview), use the Instant Access-enabled collection from step 1 and specify both the consistency mode and duration:

```azurecli
az restore-point create --resource-group "ExampleRg" --collection-name "ExampleRpc" --name "ExampleCrashConsistentRp" --consistency-mode CrashConsistent --instant-access-duration 120
```

### Exclude disks when creating a restore point

Exclude the disks that you do not want to be a part of the restore point with the `--exclude-disks` parameter, as follows:

```
az restore-point create --exclude-disks "/subscriptions/{subscription-id}/resourceGroups/ExampleRg/providers/Microsoft.Compute/disks/ExampleDisk1" --resource-group "ExampleRg" --collection-name "ExampleRpc" --name "ExampleRp"
```

## Step 3: Track the status of the VM restore point creation

Use the [az restore-point show](/en-us/cli/azure/restore-point#az-restore-point-show) command to track the progress of the VM restore point creation.

```
az restore-point show --resource-group "ExampleRg" --collection-name "ExampleRpc" --name "ExampleRp"
```

If the restore point collection has Instant Access enabled, check `instantAccessState` to validate the consolidated access state across all disk restore points within the restore point.

```
az restore-point show --resource-group "ExampleRg" --collection-name "ExampleRpc" --name "ExampleRp" --instance-view --query "instanceView.statuses[1]" -o tsv
```

A value of `InstantAccess` or `AvailableWithInstantAccess` means the restore point is ready for fast disk restoration.

## Restore a VM from VM restore point

To restore a VM from a VM restore point, first restore individual disks from each disk restore point. You can also use the [ARM template](https://github.com/Azure/Virtual-Machine-Restore-Points/blob/main/RestoreVMFromRestorePoint.json) to restore a full VM along with all the disks.

```
# Create Disks from disk restore points 
$osDiskRestorePoint = az restore-point show --resource-group "ExampleRg" --collection-name "ExampleRpc" --name "ExampleRp" --query "sourceMetadata.storageProfile.dataDisks[0].diskRestorePoint.id"
$dataDisk1RestorePoint = az restore-point show --resource-group "ExampleRg" --collection-name "ExampleRpcTarget" --name "ExampleRpTarget" –query "sourceMetadata.storageProfile.dataDisks[0].diskRestorePoint.id"
$dataDisk2RestorePoint = az restore-point show --resource-group "ExampleRg" --collection-name "ExampleRpcTarget" --name "ExampleRpTarget" –query "sourceMetadata.storageProfile.dataDisks[0].diskRestorePoint.id"
 
az disk create --resource-group “ExampleRg” --name “ExampleOSDisk” --sku Premium_LRS --size-gb 128 --source $osDiskRestorePoint

az disk create --resource-group “ExampleRg” --name “ExampleDataDisk1” --sku Premium_LRS --size-gb 128 --source $dataDisk1RestorePoint

az disk create --resource-group “ExampleRg” --name “ExampleDataDisk1” --sku Premium_LRS --size-gb 128 --source $dataDisk2RestorePoint
```

Once you have created the disks, [create a new VM](scripts/create-vm-from-managed-os-disks) and [attach these restored disks](linux/add-disk#attach-an-existing-disk) to the newly created VM.

## Disable instant access for future restore points

Update a VM restore point collection with the [az restore-point collection update](/en-us/cli/azure/restore-point/collection#az-restore-point-collection-update) command as follows:

```
az restore-point collection update -g MyResourceGroup --collection-name ExampleRpc --tags myTag1="tagValue1" --instant-access false
```