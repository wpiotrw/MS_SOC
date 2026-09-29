---
layout: Conceptual
title: Enable shared disks for Azure managed disks - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-shared-enable
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
description: Configure an Azure managed disk as a shared disk so that you can attach it to multiple virtual machines.
ms.topic: how-to
ms.date: 2026-09-17T00:00:00.0000000Z
ms.custom: devx-track-azurecli, devx-track-azurepowershell
locale: en-us
document_id: 4adcc7c9-6709-7f9e-4ec8-63dec6d78293
document_version_independent_id: 151f998f-898f-6b49-dfeb-ae29040d1af1
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/disks-shared-enable.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurepowershell
toc_rel: toc.json
asset_id: virtual-machines/disks-shared-enable
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/disks-shared-enable.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/96f6b0a2-2fd7-4de1-936d-89ad6e0eb7cc
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/ef8b0a5a-ba0a-4ec0-8636-48246ccd954f
platformId: a3b9c835-5d67-bd64-f5b3-1eed339363ac
---

# Enable shared disks for Azure managed disks - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

This article explains how to enable the shared disks feature for Azure managed disks. With Azure shared disks, you can attach a managed disk to multiple virtual machines (VMs) simultaneously, enabling the deployment or migration of clustered applications to Azure.

If you're looking for conceptual information on managed disks that have shared disks enabled, see [Azure shared disks](disks-shared).

## Prerequisites

The scripts and commands in this article require either:

- Version 6.0.0 or newer of the Azure PowerShell module.

Or

- The latest version of the Azure CLI.

## Limitations

### General limitations

Shared disks have general limitations that apply to all shared disks, regardless of disk type. They also have more limitations that only apply to specific types of shared disks. The following list is the list of general limitations:

- Currently, only Ultra Disks, Premium SSD v2, Premium SSD, and Standard SSDs can be used as a shared disk
- Shared disks can be attached to individual Virtual Machine Scale Sets but can't be defined in the Virtual Machine Scale Set models or automatically deployed
- Write accelerator isn't supported for shared disks
- Host caching isn't supported for shared disks

Each managed disk that has shared disks enabled are also subject to the following limitations, organized by disk type:

### Ultra Disks

Ultra Disks have their own separate list of limitations, unrelated to shared disks. For Ultra Disk limitations, refer to [Using Azure Ultra Disks](/en-us/azure/virtual-machines/disks-enable-ultra-ssd).

When sharing Ultra Disks, they have the following additional limitations:

- Only basic disks can be used with some versions of Windows Server Failover Cluster, for details see [Failover clustering hardware requirements and storage options](/en-us/windows-server/failover-clustering/clustering-requirements).
- Can't be shared across availability zones.

### Premium SSD v2

Premium SSD v2 managed disks have their own separate list of limitations, unrelated to shared disks. For these limitations, see [Premium SSD v2 limitations](/en-us/azure/virtual-machines/disks-types#premium-ssd-v2-limitations).

When sharing Premium SSD v2 disks, they have the following additional limitation:

- Only basic disks can be used with some versions of Windows Server Failover Cluster, for details see [Failover clustering hardware requirements and storage options](/en-us/windows-server/failover-clustering/clustering-requirements).
- Can't be shared across availability zones.

### Premium SSD

- Can only be enabled on data disks, not OS disks.
- Host caching isn't available for Premium SSDs with `maxShares>1`.
- Disk bursting isn't available for Premium SSDs with `maxShares>1`.
- When using Availability sets or Virtual Machine Scale Sets with Azure shared disks, [storage fault domain alignment](/en-us/azure/virtual-machines/availability) with virtual machine fault domain isn't enforced for the shared data disk.
- When using [proximity placement groups (PPG)](/en-us/azure/virtual-machines/windows/proximity-placement-groups), all virtual machines sharing a disk must be part of the same PPG.
- Only basic disks can be used with some versions of Windows Server Failover Cluster, for details see [Failover clustering hardware requirements and storage options](/en-us/windows-server/failover-clustering/clustering-requirements).
- Azure Site Recovery is supported in [certain scenarios](/en-us/azure/site-recovery/shared-disk-support-matrix).
- Azure Backup is available through [Azure Disk Backup](/en-us/azure/backup/disk-backup-overview).
- Only [server-side encryption](/en-us/azure/virtual-machines/disk-encryption) is supported, [Azure Disk Encryption](/en-us/azure/virtual-machines/disk-encryption-overview) isn't currently supported.
- Can only be shared across availability zones if using [Zone-redundant storage for managed disks](/en-us/azure/virtual-machines/disks-redundancy#zone-redundant-storage-for-managed-disks).

### Standard SSDs

- Can only be enabled on data disks, not OS disks.
- Host caching isn't available for Standard SSDs with `maxShares>1`.
- When using Availability sets and Virtual Machine Scale Sets with Azure shared disks, [storage fault domain alignment](/en-us/azure/virtual-machines/availability) with virtual machine fault domain isn't enforced for the shared data disk.
- When using [proximity placement groups (PPG)](/en-us/azure/virtual-machines/windows/proximity-placement-groups), all virtual machines sharing a disk must be part of the same PPG.
- Only basic disks can be used with some versions of Windows Server Failover Cluster, for details see [Failover clustering hardware requirements and storage options](/en-us/windows-server/failover-clustering/clustering-requirements).
- Azure Site Recovery is supported in [certain scenarios](/en-us/azure/site-recovery/shared-disk-support-matrix).
- Azure Backup is available through [Azure Disk Backup](/en-us/azure/backup/disk-backup-overview).
- Only [server-side encryption](/en-us/azure/virtual-machines/disk-encryption) is supported, [Azure Disk Encryption](/en-us/azure/virtual-machines/disk-encryption-overview) isn't currently supported.
- Can only be shared across availability zones if using [Zone-redundant storage for managed disks](/en-us/azure/virtual-machines/disks-redundancy#zone-redundant-storage-for-managed-disks).

## Supported operating systems

Shared disks support several operating systems. For the supported operating systems, see the [Windows](disks-shared#sample-windows-shared-disk-workloads) and [Linux](disks-shared#sample-linux-shared-disk-workloads) sections of the conceptual article.

## Disk sizes

For now, only Ultra Disks, Premium SSD v2, Premium SSD, and Standard SSDs can enable shared disks. Different disk sizes may have a different `maxShares` limit, which you can't exceed when setting the `maxShares` value.

For each disk, you can define a `maxShares` value that represents the maximum number of nodes that can simultaneously share the disk. For example, if you plan to set up a 2-node failover cluster, you would set `maxShares=2`. The maximum value is an upper bound. Nodes can join or leave the cluster (mount or unmount the disk) as long as the number of nodes is lower than the specified `maxShares` value.

Note

The `maxShares` value can only be set or edited when the disk is detached from all nodes.

### Premium SSD ranges

The following table illustrates the allowed maximum values for `maxShares` by Premium SSD sizes:

| Disk sizes | maxShares limit |
| --- | --- |
| P1,P2,P3,P4,P6,P10,P15,P20 | 3 |
| P30, P40, P50 | 5 |
| P60, P70, P80 | 10 |

The IOPS and bandwidth limits for a disk aren't affected by the `maxShares` value. For example, the max IOPS of a P15 disk is 1100 whether maxShares = 1 or maxShares &gt; 1.

### Standard SSD ranges

The following table illustrates the allowed maximum values for `maxShares` by Standard SSD sizes:

| Disk sizes | maxShares limit |
| --- | --- |
| E1,E2,E3,E4,E6,E10,E15,E20 | 3 |
| E30, E40, E50 | 5 |
| E60, E70, E80 | 10 |

The IOPS and bandwidth limits for a disk aren't affected by the `maxShares` value. For example, the max IOPS of a E15 disk is 500 whether maxShares = 1 or maxShares &gt; 1.

### Ultra Disk ranges

The minimum `maxShares` value is 1, while the maximum `maxShares` value is 15. There are no size restrictions on Ultra Disks, any size Ultra Disk can use any value for `maxShares`, up to and including the maximum value.

### Premium SSD v2 ranges

The minimum `maxShares` value is 1, while the maximum `maxShares` value is 15. There are no size restrictions on Premium SSD v2, any size Premium SSD v2 can use any value for `maxShares`, up to and including the maximum value.

## Deploy a Premium SSD as a shared disk

To deploy a managed disk with the shared disk feature enabled, set the `maxShares` property to a value greater than 1. This setting makes the disk shareable across multiple VMs.

Important

Host caching isn't supported for shared disks.

The value of `maxShares` can only be set or changed when a disk is unmounted from all VMs. See the Disk sizes for the allowed values for `maxShares`.

# [Azure portal](#tab/azure-portal)
1. Sign in to the Azure portal.
2. Search for and select **Disks**.
3. Select **+ Create** to create a new managed disk.
4. On the **Basics** pane, select a **Region**, and then select **Change size**.

    [![Screenshot of the Create a managed disk Basics pane with Region set to West US, Availability zone set to None, and Change size highlighted.](media/disks-shared-enable/create-shared-disk-basics-pane.png)](media/disks-shared-enable/create-shared-disk-basics-pane.png#lightbox)
5. Select the Premium SSD size and SKU that you want and select **OK**.

    [![Screenshot of the Disk SKU list with Premium SSD under locally redundant storage and zone-redundant storage highlighted.](media/disks-shared-enable/select-premium-shared-disk.png)](media/disks-shared-enable/select-premium-shared-disk.png#lightbox)
6. Proceed through the deployment until you get to the **Advanced** pane.
7. For **Enable shared disk**, select **Yes**, and then select a value for **Max shares**.

    [![Screenshot of the shared disk settings with Enable shared disk set to Yes and Max shares set to 2.](media/disks-shared-enable/enable-premium-shared-disk.png)](media/disks-shared-enable/enable-premium-shared-disk.png#lightbox)
8. Select **Review + create**.

# [Azure CLI](#tab/azure-cli)
Use the following Azure CLI command to create a Premium SSD as a shared disk.

```azurecli
az disk create -g myResourceGroup -n mySharedDisk --size-gb 1024 -l westcentralus --sku Premium_LRS --max-shares 2
```

# [Azure PowerShell](#tab/azure-powershell)
Use the following Azure PowerShell commands to create a Premium SSD as a shared disk.

```azurepowershell
$dataDiskConfig = New-AzDiskConfig -Location 'WestCentralUS' -DiskSizeGB 1024 -AccountType Premium_LRS -CreateOption Empty -MaxSharesCount 2

New-AzDisk -ResourceGroupName 'myResourceGroup' -DiskName 'mySharedDisk' -Disk $dataDiskConfig
```

# [Resource Manager template](#tab/azure-resource-manager)
Before using the following template, replace `[parameters('dataDiskName')]`, `[resourceGroup().location]`, `[parameters('dataDiskSizeGB')]`, and `[parameters('maxShares')]` with your own values.

```rest
{ 
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "dataDiskName": {
      "type": "string",
      "defaultValue": "mySharedDisk"
    },
    "dataDiskSizeGB": {
      "type": "int",
      "defaultValue": 1024
    },
    "maxShares": {
      "type": "int",
      "defaultValue": 2
    }
  },
  "resources": [
    {
      "type": "Microsoft.Compute/disks",
      "name": "[parameters('dataDiskName')]",
      "location": "[resourceGroup().location]",
      "apiVersion": "2019-07-01",
      "sku": {
        "name": "Premium_LRS"
      },
      "properties": {
        "creationData": {
          "createOption": "Empty"
        },
        "diskSizeGB": "[parameters('dataDiskSizeGB')]",
        "maxShares": "[parameters('maxShares')]"
      }
    }
  ] 
}
```

---

## Deploy a Standard SSD as a shared disk

To deploy a managed disk with the shared disk feature enabled, set the `maxShares` property to a value greater than 1. This setting makes the disk shareable across multiple VMs.

Important

Host caching isn't supported for shared disks.

The value of `maxShares` can only be set or changed when a disk is unmounted from all VMs. See the Disk sizes for the allowed values for `maxShares`.

# [Azure portal](#tab/azure-portal)
1. Sign in to the Azure portal.
2. Search for and select **Disks**.
3. Select **+ Create** to create a new managed disk.
4. On the **Basics** pane, select a **Region**, and then select **Change size**.

    [![Screenshot of the Create a managed disk Basics pane with Region set to West US, Availability zone set to None, and Change size highlighted.](media/disks-shared-enable/create-shared-disk-basics-pane.png)](media/disks-shared-enable/create-shared-disk-basics-pane.png#lightbox)
5. Select the Standard SSD size and SKU that you want and select **OK**.

    [![Screenshot of the Disk SKU list with Standard SSD under locally redundant storage and zone-redundant storage highlighted.](media/disks-shared-enable/select-standard-ssd-shared-disk.png)](media/disks-shared-enable/select-standard-ssd-shared-disk.png#lightbox)
6. Proceed through the deployment until you get to the **Advanced** pane.
7. For **Enable shared disk**, select **Yes**, and then select a value for **Max shares**.

    [![Screenshot of the shared disk settings with Enable shared disk set to Yes and Max shares set to 2.](media/disks-shared-enable/enable-premium-shared-disk.png)](media/disks-shared-enable/enable-premium-shared-disk.png#lightbox)
8. Select **Review + create**.

# [Azure CLI](#tab/azure-cli)
Use the following Azure CLI command to create a Standard SSD as a shared disk.

```azurecli
az disk create -g myResourceGroup -n mySharedDisk --size-gb 1024 -l westcentralus --sku StandardSSD_LRS --max-shares 2
```

# [Azure PowerShell](#tab/azure-powershell)
Use the following Azure PowerShell commands to create a Standard SSD as a shared disk.

```azurepowershell
$dataDiskConfig = New-AzDiskConfig -Location 'WestCentralUS' -DiskSizeGB 1024 -AccountType StandardSSD_LRS -CreateOption Empty -MaxSharesCount 2

New-AzDisk -ResourceGroupName 'myResourceGroup' -DiskName 'mySharedDisk' -Disk $dataDiskConfig
```

# [Resource Manager template](#tab/azure-resource-manager)
Before using the following template, replace the default values for the `dataDiskName`, `dataDiskSizeGB`, and `maxShares` parameters with your own values.

```rest
{ 
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "dataDiskName": {
      "type": "string",
      "defaultValue": "mySharedDisk"
    },
    "dataDiskSizeGB": {
      "type": "int",
      "defaultValue": 1024
    },
    "maxShares": {
      "type": "int",
      "defaultValue": 2
    }
  },
  "resources": [
    {
      "type": "Microsoft.Compute/disks",
      "name": "[parameters('dataDiskName')]",
      "location": "[resourceGroup().location]",
      "apiVersion": "2019-07-01",
      "sku": {
        "name": "StandardSSD_LRS"
      },
      "properties": {
        "creationData": {
          "createOption": "Empty"
        },
        "diskSizeGB": "[parameters('dataDiskSizeGB')]",
        "maxShares": "[parameters('maxShares')]"
      }
    }
  ] 
}
```

---

## Deploy an Ultra Disk as a shared disk

To deploy a managed disk with the shared disk feature enabled, change the `maxShares` parameter to a value greater than 1. This makes the disk shareable across multiple VMs.

Important

The value of `maxShares` can only be set or changed when a disk is unmounted from all VMs. See the Disk sizes for the allowed values for `maxShares`.

# [Azure portal](#tab/azure-portal)
1. Sign in to the Azure portal.
2. Search for and select **Disks**.
3. Select **+ Create** to create a new managed disk.
4. On the **Basics** pane, select **Change size**.
5. Select Ultra Disk for the **Disk SKU**.

    [![Screenshot of the Disk SKU list with Ultra Disk under locally redundant storage selected.](media/disks-shared-enable/select-ultra-shared-disk.png)](media/disks-shared-enable/select-ultra-shared-disk.png#lightbox)
6. Select the disk size that you want and select **OK**.
7. Proceed through the deployment until you get to the **Advanced** pane.
8. For **Enable shared disk**, select **Yes**, and then select a value for **Max shares**.
9. Select **Review + create**.

    [![Screenshot of the Advanced pane with Enable shared disk set to Yes, Max shares set to 2, Ultra Disk performance values, and logical sector size set to 4096 bytes.](media/disks-shared-enable/enable-ultra-shared-disk.png)](media/disks-shared-enable/enable-ultra-shared-disk.png#lightbox)

# [Azure CLI](#tab/azure-cli)
##### Regional disk example

The following Azure CLI commands create a regional Ultra Disk as a shared disk, update its performance settings, and show its properties.

```azurecli
#Creating an Ultra shared Disk 
az disk create -g rg1 -n clidisk --size-gb 1024 -l westus --sku UltraSSD_LRS --max-shares 5 --disk-iops-read-write 2000 --disk-mbps-read-write 200 --disk-iops-read-only 100 --disk-mbps-read-only 1

#Updating an Ultra shared Disk 
az disk update -g rg1 -n clidisk --disk-iops-read-write 3000 --disk-mbps-read-write 300 --set diskIopsReadOnly=100 --set diskMbpsReadOnly=1

#Show shared disk properties:
az disk show -g rg1 -n clidisk
```

##### Zonal disk example

The following Azure CLI commands create an Ultra Disk as a shared disk in availability zone 1, update its performance settings, and show its properties.

```azurecli
#Creating an Ultra shared Disk 
az disk create -g rg1 -n clidisk --size-gb 1024 -l westus --sku UltraSSD_LRS --max-shares 5 --disk-iops-read-write 2000 --disk-mbps-read-write 200 --disk-iops-read-only 100 --disk-mbps-read-only 1 --zone 1

#Updating an Ultra shared Disk 
az disk update -g rg1 -n clidisk --disk-iops-read-write 3000 --disk-mbps-read-write 300 --set diskIopsReadOnly=100 --set diskMbpsReadOnly=1

#Show shared disk properties:
az disk show -g rg1 -n clidisk
```

# [Azure PowerShell](#tab/azure-powershell)
##### Regional disk example

The following Azure PowerShell commands create a regional Ultra Disk as a shared disk.

```azurepowershell
$datadiskconfig = New-AzDiskConfig -Location 'WestCentralUS' -DiskSizeGB 1024 -AccountType UltraSSD_LRS -CreateOption Empty -DiskIOPSReadWrite 2000 -DiskMBpsReadWrite 200 -DiskIOPSReadOnly 100 -DiskMBpsReadOnly 1 -MaxSharesCount 5

New-AzDisk -ResourceGroupName 'myResourceGroup' -DiskName 'mySharedDisk' -Disk $datadiskconfig
```

##### Zonal disk example

The following Azure PowerShell commands create an Ultra Disk as a shared disk in availability zone 1.

```azurepowershell
$datadiskconfig = New-AzDiskConfig -Location 'WestCentralUS' -DiskSizeGB 1024 -AccountType UltraSSD_LRS -CreateOption Empty -DiskIOPSReadWrite 2000 -DiskMBpsReadWrite 200 -DiskIOPSReadOnly 100 -DiskMBpsReadOnly 1 -MaxSharesCount 5 -Zone 1

New-AzDisk -ResourceGroupName 'myResourceGroup' -DiskName 'mySharedDisk' -Disk $datadiskconfig
```

# [Resource Manager template](#tab/azure-resource-manager)
##### Regional disk example

Before using the following template, replace the default values for the `diskName`, `location`, `dataDiskSizeGB`, `maxShares`, `diskIOPSReadWrite`, `diskMBpsReadWrite`, `diskIOPSReadOnly`, and `diskMBpsReadOnly` parameters with your own values.

```rest
{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "diskName": {
      "type": "string",
      "defaultValue": "uShared30"
    },
    "location": {
        "type": "string",
        "defaultValue": "westus",
        "metadata": {
                "description": "Location for all resources."
        }
    },
    "dataDiskSizeGB": {
      "type": "int",
      "defaultValue": 1024
    },
    "maxShares": {
      "type": "int",
      "defaultValue": 2
    },
    "diskIOPSReadWrite": {
      "type": "int",
      "defaultValue": 2048
    },
    "diskMBpsReadWrite": {
      "type": "int",
      "defaultValue": 20
    },    
    "diskIOPSReadOnly": {
      "type": "int",
      "defaultValue": 100
    },
    "diskMBpsReadOnly": {
      "type": "int",
      "defaultValue": 1
    } 
  }, 
  "resources": [
    {
        "type": "Microsoft.Compute/disks",
        "name": "[parameters('diskName')]",
        "location": "[parameters('location')]",
        "apiVersion": "2019-07-01",
        "sku": {
            "name": "UltraSSD_LRS"
        },
        "properties": {
            "creationData": {
                "createOption": "Empty"
            },
            "diskSizeGB": "[parameters('dataDiskSizeGB')]",
            "maxShares": "[parameters('maxShares')]",
            "diskIOPSReadWrite": "[parameters('diskIOPSReadWrite')]",
            "diskMBpsReadWrite": "[parameters('diskMBpsReadWrite')]",
            "diskIOPSReadOnly": "[parameters('diskIOPSReadOnly')]",
            "diskMBpsReadOnly": "[parameters('diskMBpsReadOnly')]"
        }
    }
  ]
}
```

##### Zonal disk example

Before using the following template, replace the default values for the `diskName`, `location`, `dataDiskSizeGB`, `maxShares`, `diskIOPSReadWrite`, `diskMBpsReadWrite`, `diskIOPSReadOnly`, `diskMBpsReadOnly`, and `zone` parameters with your own values.

```rest
{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "diskName": {
      "type": "string",
      "defaultValue": "uShared30"
    },
    "location": {
        "type": "string",
        "defaultValue": "westus",
        "metadata": {
                "description": "Location for all resources."
        }
    },
    "dataDiskSizeGB": {
      "type": "int",
      "defaultValue": 1024
    },
    "maxShares": {
      "type": "int",
      "defaultValue": 2
    },
    "diskIOPSReadWrite": {
      "type": "int",
      "defaultValue": 2048
    },
    "diskMBpsReadWrite": {
      "type": "int",
      "defaultValue": 20
    },    
    "diskIOPSReadOnly": {
      "type": "int",
      "defaultValue": 100
    },
    "diskMBpsReadOnly": {
      "type": "int",
      "defaultValue": 1
    },"zone": {	"type": "int",	"allowedValues": [		1,		2,		3	],  "metadata": {		"description": "Zone to deploy to."	}} 
  }, 
  "resources": [
    {
        "type": "Microsoft.Compute/disks",
        "name": "[parameters('diskName')]",
        "location": "[parameters('location')]",	"zones": ["[parameters('zone')]"],
        "apiVersion": "2019-07-01",
        "sku": {
            "name": "UltraSSD_LRS"
        },
        "properties": {
            "creationData": {
                "createOption": "Empty"
            },
            "diskSizeGB": "[parameters('dataDiskSizeGB')]",
            "maxShares": "[parameters('maxShares')]",
            "diskIOPSReadWrite": "[parameters('diskIOPSReadWrite')]",
            "diskMBpsReadWrite": "[parameters('diskMBpsReadWrite')]",
            "diskIOPSReadOnly": "[parameters('diskIOPSReadOnly')]",
            "diskMBpsReadOnly": "[parameters('diskMBpsReadOnly')]"
        }
    }
  ]
}
```

---

## Share an existing disk

To share an existing disk or update how many VMs can mount it, set the `maxShares` parameter by using either Azure PowerShell or Azure CLI. To disable sharing, set `maxShares` to 1.

Important

Host caching isn't supported for shared disks.

The value of `maxShares` can only be set or changed when a disk is unmounted from all VMs. See the Disk sizes for the allowed values for `maxShares`. Before detaching a disk, record the LUN ID for when you reattach it.

### Azure PowerShell

The following Azure PowerShell commands update the sharing configuration of an existing disk.

```azurepowershell
$datadiskconfig = Get-AzDisk -DiskName "mySharedDisk"
$datadiskconfig.maxShares = 3

Update-AzDisk -ResourceGroupName 'myResourceGroup' -DiskName 'mySharedDisk' -Disk $datadiskconfig
```

### Azure CLI

The following Azure CLI command updates the sharing configuration of an existing disk.

```azurecli
#Modifying a disk to enable or modify sharing configuration

az disk update --name mySharedDisk --max-shares 5 --resource-group myResourceGroup
```

## Use Azure shared disks with your VMs

After you deploy a shared disk with `maxShares > 1`, you can mount the disk to one or more of your VMs.

Note

Host caching isn't supported for shared disks.

If you're deploying an Ultra Disk, make sure it matches the necessary requirements. See [Using Azure Ultra Disks](disks-enable-ultra-ssd) for details.

The following Azure PowerShell commands create a VM and attach the shared disk as a data disk.

```azurepowershell

$resourceGroup = "myResourceGroup"
$location = "WestCentralUS"

$vm = New-AzVm -ResourceGroupName $resourceGroup -Name "myVM" -Location $location -VirtualNetworkName "myVnet" -SubnetName "mySubnet" -SecurityGroupName "myNetworkSecurityGroup" -PublicIpAddressName "myPublicIpAddress"

$dataDisk = Get-AzDisk -ResourceGroupName $resourceGroup -DiskName "mySharedDisk"

$vm = Add-AzVMDataDisk -VM $vm -Name "mySharedDisk" -CreateOption Attach -ManagedDiskId $dataDisk.Id -Lun 0

update-AzVm -VM $vm -ResourceGroupName $resourceGroup
```

## Supported SCSI persistent reservation commands

After you mount the shared disk to your VMs in your cluster, you can establish quorum and read/write to the disk by using Small Computer System Interface (SCSI) persistent reservation (PR) commands.

The following SCSI persistent reservation commands are available when using Azure shared disks:

- `PR_REGISTER_KEY`
- `PR_REGISTER_AND_IGNORE`
- `PR_GET_CONFIGURATION`
- `PR_RESERVE`
- `PR_PREEMPT_RESERVATION`
- `PR_CLEAR_RESERVATION`
- `PR_RELEASE_RESERVATION`

When you use `PR_RESERVE`, `PR_PREEMPT_RESERVATION`, or `PR_RELEASE_RESERVATION`, provide one of the following persistent reservation types:

- `PR_NONE`
- `PR_WRITE_EXCLUSIVE`
- `PR_EXCLUSIVE_ACCESS`
- `PR_WRITE_EXCLUSIVE_REGISTRANTS_ONLY`
- `PR_EXCLUSIVE_ACCESS_REGISTRANTS_ONLY`
- `PR_WRITE_EXCLUSIVE_ALL_REGISTRANTS`
- `PR_EXCLUSIVE_ACCESS_ALL_REGISTRANTS`

You also need to provide a persistent reservation key when you use `PR_RESERVE`, `PR_REGISTER_AND_IGNORE`, `PR_REGISTER_KEY`, `PR_PREEMPT_RESERVATION`, `PR_CLEAR_RESERVATION`, or `PR_RELEASE_RESERVATION`.