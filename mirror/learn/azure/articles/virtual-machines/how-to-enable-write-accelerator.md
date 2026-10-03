---
layout: Conceptual
title: Azure Write Accelerator - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/how-to-enable-write-accelerator
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
description: Learn how to enable and use Write Accelerator
ms.topic: how-to
ms.date: 2026-09-21T00:00:00.0000000Z
ms.custom: devx-track-azurepowershell, devx-track-azurecli
ai-usage: ai-assisted
locale: en-us
document_id: 7e05b681-ee07-2f70-ee7a-78fa6b1eb1e5
document_version_independent_id: b4977afa-66fe-3c8d-db4d-2b842fc96138
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/how-to-enable-write-accelerator.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurepowershell
toc_rel: toc.json
asset_id: virtual-machines/how-to-enable-write-accelerator
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/how-to-enable-write-accelerator.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 8eeff73a-6bca-c000-6556-86f82eea4823
---

# Azure Write Accelerator - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

Write Accelerator is a disk capability for M-series virtual machines (VMs) on Premium SSD managed disks. As the name states, the purpose of the functionality is to improve the I/O latency of writes against Premium SSDs. Write Accelerator is ideally suited where log file updates are required to persist to disk in a highly performant manner for modern databases.

Write Accelerator is generally available for M-series VMs in the Public Cloud.

## Prerequisites

- Only supported with [Premium SSD managed disks](/en-us/azure/virtual-machines/disks-types#premium-ssds)
- Only supported by M-series VMs

## Plan to use Write Accelerator

Write Accelerator should be used for the volumes that contain the transaction log or redo logs of a DBMS. You shouldn't use Write Accelerator for the data volumes of a DBMS as the feature is optimized to be used against log disks.

Important

Enabling Write Accelerator for the operating system disk of the VM reboots the VM.

To enable Write Accelerator to an existing Azure disk that isn't part of a volume build out of multiple disks with Windows disk or volume managers, Windows Storage Spaces, Windows Scale-out file server (SOFS), Linux LVM, or MDADM, the workload accessing the Azure disk needs to be shut down. Database applications using the Azure disk must be shut down.

To enable or disable Write Accelerator for an existing volume that is built out of multiple Azure Premium SSDs and striped using Windows disk or volume managers, Windows Storage Spaces, Windows Scale-out file server (SOFS), Linux LVM or MDADM, all disks building the volume must be enabled or disabled for Write Accelerator in separate steps. Shut down the VM Before enabling or disabling Write Accelerator in such a configuration.

Enabling Write Accelerator for OS disks shouldn't be necessary for SAP-related VM configurations.

### Write Accelerator restrictions

When using Write Accelerator for an Azure disk/VHD, these restrictions apply:

- Set disk caching to `None` or `ReadOnly`. Other caching modes aren't supported.
- Snapshots are currently supported for only Write Accelerator-enabled data disks, and not the OS disk. During backup, the Azure Backup service automatically backs up and protects Write Accelerator-enabled data disks attached to the VM.
- Only smaller I/O sizes (&lt;=64 KiB) are taking the accelerated path. In workload situations where data is getting bulk loaded or where the transaction log buffers of the different DBMS are filled to a larger degree before getting persisted to the storage, chances are that the I/O written to disk is not taking the accelerated path.

There are limits of Azure Premium SSDs per VM that can be supported by Write Accelerator. The current limits are:

| VM SKU | Number of Write Accelerator disks | Write Accelerator Disk IOPS per VM |
| --- | --- | --- |
| M416ms\_v2, M416s\_8\_v2, M416s\_v2 | 16 | 20000 |
| M208ms\_v2, M208s\_v2 | 8 | 10000 |
| M192ids\_v2, M192idms\_v2, M192is\_v2, M192ims\_v2, | 16 | 20000 |
| M128ms, M128s, M128ds\_v2, M128dms\_v2, M128s\_v2, M128ms\_v2 | 16 | 20000 |
| M64ms, M64ls, M64s, M64ds\_v2, M64dms\_v2, M64s\_v2, M64ms\_v2 | 8 | 10000 |
| M32ms, M32ls, M32ts, M32s, M32dms\_v2, M32ms\_v2 | 4 | 5000 |
| M16ms, M16s | 2 | 2500 |
| M8ms, M8s | 1 | 1250 |
| Standard\_M12s\_v3, Standard\_M12ds\_v3 | 1 | 5000 |
| Standard\_M24s\_v3, Standard\_M24ds\_v3 | 2 | 5000 |
| Standard\_M48s\_1\_v3, Standard\_M48ds\_1\_v3 | 4 | 5000 |
| Standard\_M96s\_1\_v3, Standard\_M96ds\_1\_v3, Standard\_M96s\_2\_v3, Standard\_M96ds\_2\_v3 | 8 | 10000 |
| Standard\_M176s\_3\_v3, Standard\_M176ds\_3\_v3, Standard\_M176s\_4\_v3, Standard\_M176ds\_4\_v3 | 16 | 20000 |

The IOPS limits are per VM, not per disk. All Write Accelerator disks share the same IOPS limit per VM. Attached disks can't exceed the Write Accelerator IOPS limit for a VM. For example, even though the attached disks can do 30,000 IOPS, the system doesn't allow the disks to go above 20,000 IOPS for M416ms\_v2.

## Enable Write Accelerator with Azure PowerShell

The Azure PowerShell module from version 5.5.0 include the changes to the relevant cmdlets to enable or disable Write Accelerator for specific Azure Premium SSDs. In order to enable or deploy disks supported by Write Accelerator, the following PowerShell commands got changed, and extended to accept a parameter for Write Accelerator.

A new switch parameter, **-WriteAccelerator** has been added to the following cmdlets:

- [Set-AzVMOsDisk](/en-us/powershell/module/az.compute/set-azvmosdisk)
- [Add-AzVMDataDisk](/en-us/powershell/module/az.compute/Add-AzVMDataDisk)
- [Set-AzVMDataDisk](/en-us/powershell/module/az.compute/Set-AzVMDataDisk)
- [Add-AzVmssDataDisk](/en-us/powershell/module/az.compute/Add-AzVmssDataDisk)

Note

If you enable Write Accelerator on virtual machine scale sets that use Flexible orchestration mode, enable it on each individual instance.

Not giving the parameter sets the property to false and will deploy disks that have no support by Write Accelerator.

A new switch parameter, **-OsDiskWriteAccelerator** was added to the following cmdlets:

- [Set-AzVmssStorageProfile](/en-us/powershell/module/az.compute/Set-AzVmssStorageProfile)

Not specifying the parameter sets the property to false by default, returning disks that don't use Write Accelerator.

A new optional Boolean (non-nullable) parameter, **-OsDiskWriteAccelerator** was added to the following cmdlets:

- [Update-AzVM](/en-us/powershell/module/az.compute/Update-AzVM)
- [Update-AzVmss](/en-us/powershell/module/az.compute/Update-AzVmss)

Specify either `$true` or `$false` to control support of Azure Write Accelerator with the disks.

Examples of commands could look like:

```azurepowershell
New-AzVMConfig | Set-AzVMOsDisk | Add-AzVMDataDisk -Name "datadisk1" | Add-AzVMDataDisk -Name "logdisk1" -WriteAccelerator | New-AzVM

Get-AzVM | Update-AzVM -OsDiskWriteAccelerator $true

New-AzVmssConfig | Set-AzVmssStorageProfile -OsDiskWriteAccelerator | Add-AzVmssDataDisk -Name "datadisk1" -WriteAccelerator:$false | Add-AzVmssDataDisk -Name "logdisk1" -WriteAccelerator | New-AzVmss

Get-AzVmss | Update-AzVmss -OsDiskWriteAccelerator:$false
```

Two main scenarios can be scripted as shown in the following sections.

### Add a new disk with Write Accelerator by using PowerShell

You can use this script to add a new disk to your VM. The disk created with this script uses Write Accelerator.

Replace `myVM`, `myWAVMs`, `log001`, size of the disk, and LunID of the disk with values appropriate for your specific deployment.

```azurepowershell
# Specify your VM Name
$vmName="myVM"
#Specify your Resource Group
$rgName = "myWAVMs"
#data disk name
$datadiskname = "log001"
#LUN Id
$lunid=8
#size
$size=1023
#Pulls the VM info for later
$vm=Get-AzVM -ResourceGroupName $rgname -Name $vmname
#add a new VM data disk
Add-AzVMDataDisk -CreateOption empty -DiskSizeInGB $size -Name $vmname-$datadiskname -VM $vm -Caching None -WriteAccelerator:$true -lun $lunid
#Updates the VM with the disk config - does not require a reboot
Update-AzVM -ResourceGroupName $rgname -VM $vm
```

### Enable Write Accelerator on an existing Azure disk by using PowerShell

You can use this script to enable Write Accelerator on an existing disk. Replace `myVM`, `myWAVMs`, and `test-log001` with values appropriate for your specific deployment. The script adds Write Accelerator to an existing disk where the value for **$newstatus** is set to '$true'. Using the value '$false' will disable Write Accelerator on a given disk.

```azurepowershell
#Specify your VM Name
$vmName="myVM"
#Specify your Resource Group
$rgName = "myWAVMs"
#data disk name
$datadiskname = "test-log001"
#new Write Accelerator status ($true for enabled, $false for disabled)
$newstatus = $true
#Pulls the VM info for later
$vm=Get-AzVM -ResourceGroupName $rgname -Name $vmname
#add a new VM data disk
Set-AzVMDataDisk -VM $vm -Name $datadiskname -Caching None -WriteAccelerator:$newstatus
#Updates the VM with the disk config - does not require a reboot
Update-AzVM -ResourceGroupName $rgname -VM $vm
```

Note

Executing the script above will detach the disk specified, enable Write Accelerator against the disk, and then attach the disk again

## Enable Write Accelerator in the Azure portal

You can enable Write Accelerator via the portal where you specify your disk caching settings:

![Screenshot of the Azure portal Disks page showing data disk Host caching options set to Read-only plus Write Accelerator and None plus Write Accelerator.](media/virtual-machines-common-how-to-enable-write-accelerator/wa_scrnsht.png)

## Enable Write Accelerator with the Azure CLI

You can use the [Azure CLI](/en-us/cli/azure/) to enable Write Accelerator.

Set the resource group, VM, disk, and disk LUN values for the following examples:

```azurecli
rgName="myResourceGroup"
vmName="myVM"
diskName="myDataDisk"
diskLun=1
```

- To enable Write Accelerator on an existing attached disk, use [az vm update](/en-us/cli/azure/vm#az-vm-update). The `--write-accelerator` value maps the disk LUN to `true`:

```azurecli
az vm update \
  --resource-group $rgName \
  --name $vmName \
  --write-accelerator "${diskLun}=true"
```

- To attach an existing disk with Write Accelerator enabled, use [az vm disk attach](/en-us/cli/azure/vm/disk#az-vm-disk-attach):

```azurecli
az vm disk attach \
  --resource-group $rgName \
  --vm-name $vmName \
  --name $diskName \
  --enable-write-accelerator
```

- To disable Write Accelerator on an attached disk, set its LUN to `false`:

```azurecli
az vm update \
  --resource-group $rgName \
  --name $vmName \
  --write-accelerator "${diskLun}=false"
```

## Enable Write Accelerator with the REST API

To deploy through Azure REST API, you need to install the Azure armclient.

### Install armclient

To run armclient, you need to install it through Chocolatey. You can install it through cmd.exe or PowerShell. Use elevated rights for these commands (“Run as Administrator”).

Using cmd.exe, run the following command:

```cmd
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

Using PowerShell, run the following command:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

Now install armclient by using the following command in either cmd.exe or PowerShell:

```console
choco install armclient
```

### Get your current VM configuration

To change the attributes of your disk configuration, first retrieve the current VM configuration in a JSON file. Replace `subscription-ID`, `resource-group`, `vm-name`, and `filename.json` with your values.

```console
armclient GET /subscriptions/subscription-ID/resourceGroups/resource-group/providers/Microsoft.Compute/virtualMachines/vm-name?api-version=2017-12-01 > filename.json
```

The output could look like:

```output
{
  "properties": {
    "vmId": "2444c93e-f8bb-4a20-af2d-1658d9dbbbcb",
    "hardwareProfile": {
      "vmSize": "Standard_M64s"
    },
    "storageProfile": {
      "imageReference": {
        "publisher": "SUSE",
        "offer": "SLES-SAP",
        "sku": "12-SP3",
        "version": "latest"
      },
      "osDisk": {
        "osType": "Linux",
        "name": "mylittlesap_OsDisk_1_754a1b8bb390468e9b4c429b81cc5f5a",
        "createOption": "FromImage",
        "caching": "ReadWrite",
        "managedDisk": {
          "storageAccountType": "Premium_LRS",
          "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Compute/disks/mylittlesap_OsDisk_1_754a1b8bb390468e9b4c429b81cc5f5a"
        },
        "diskSizeGB": 30
      },
      "dataDisks": [
        {
          "lun": 0,
          "name": "data1",
          "createOption": "Attach",
          "caching": "None",
          "managedDisk": {
            "storageAccountType": "Premium_LRS",
            "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Compute/disks/data1"
          },
          "diskSizeGB": 1023
        },
        {
          "lun": 1,
          "name": "log1",
          "createOption": "Attach",
          "caching": "None",
          "managedDisk": {
            "storageAccountType": "Premium_LRS",
            "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Compute/disks/data2"
          },
          "diskSizeGB": 1023
        }
      ]
    },
    "osProfile": {
      "computerName": "mylittlesapVM",
      "adminUsername": "pl",
      "linuxConfiguration": {
        "disablePasswordAuthentication": false
      },
      "secrets": []
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Network/networkInterfaces/mylittlesap518"
        }
      ]
    },
    "diagnosticsProfile": {
      "bootDiagnostics": {
        "enabled": true,
        "storageUri": "https://mylittlesapdiag895.blob.core.windows.net/"
      }
    },
    "provisioningState": "Succeeded"
  },
  "type": "Microsoft.Compute/virtualMachines",
  "location": "westeurope",
  "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Compute/virtualMachines/mylittlesapVM",
  "name": "mylittlesapVM"

```

### Enable Write Accelerator in the VM configuration

In `filename.json`, find the data disk that you want to update. The following example adds `writeAcceleratorEnabled: true` to the disk named `log1` after its `caching` property.

```JSON
        {
          "lun": 1,
          "name": "log1",
          "createOption": "Attach",
          "caching": "None",
          "writeAcceleratorEnabled": true,
          "managedDisk": {
            "storageAccountType": "Premium_LRS",
            "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Compute/disks/data2"
          },
          "diskSizeGB": 1023
        }
```

### Apply and verify the VM configuration

Apply the updated JSON file to the VM. Replace `subscription-ID`, `resource-group`, `vm-name`, and `filename.json` with the same values that you used to retrieve the configuration.

```console
armclient PUT /subscriptions/subscription-ID/resourceGroups/resource-group/providers/Microsoft.Compute/virtualMachines/vm-name?api-version=2017-12-01 @filename.json
```

In the response, verify that the target data disk contains `"writeAcceleratorEnabled": true`. The following output shows Write Accelerator enabled for the disk named `log1`.

```output
{
  "properties": {
    "vmId": "2444c93e-f8bb-4a20-af2d-1658d9dbbbcb",
    "hardwareProfile": {
      "vmSize": "Standard_M64s"
    },
    "storageProfile": {
      "imageReference": {
        "publisher": "SUSE",
        "offer": "SLES-SAP",
        "sku": "12-SP3",
        "version": "latest"
      },
      "osDisk": {
        "osType": "Linux",
        "name": "mylittlesap_OsDisk_1_754a1b8bb390468e9b4c429b81cc5f5a",
        "createOption": "FromImage",
        "caching": "ReadWrite",
        "managedDisk": {
          "storageAccountType": "Premium_LRS",
          "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Compute/disks/mylittlesap_OsDisk_1_754a1b8bb390468e9b4c429b81cc5f5a"
        },
        "diskSizeGB": 30
      },
      "dataDisks": [
        {
          "lun": 0,
          "name": "data1",
          "createOption": "Attach",
          "caching": "None",
          "managedDisk": {
            "storageAccountType": "Premium_LRS",
            "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Compute/disks/data1"
          },
          "diskSizeGB": 1023
        },
        {
          "lun": 1,
          "name": "log1",
          "createOption": "Attach",
          "caching": "None",
          "writeAcceleratorEnabled": true,
          "managedDisk": {
            "storageAccountType": "Premium_LRS",
            "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Compute/disks/data2"
          },
          "diskSizeGB": 1023
        }
      ]
    },
    "osProfile": {
      "computerName": "mylittlesapVM",
      "adminUsername": "pl",
      "linuxConfiguration": {
        "disablePasswordAuthentication": false
      },
      "secrets": []
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Network/networkInterfaces/mylittlesap518"
        }
      ]
    },
    "diagnosticsProfile": {
      "bootDiagnostics": {
        "enabled": true,
        "storageUri": "https://mylittlesapdiag895.blob.core.windows.net/"
      }
    },
    "provisioningState": "Succeeded"
  },
  "type": "Microsoft.Compute/virtualMachines",
  "location": "westeurope",
  "id": "/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/mylittlesap/providers/Microsoft.Compute/virtualMachines/mylittlesapVM",
  "name": "mylittlesapVM"
```

Once you've made this change, the drive should be supported by Write Accelerator.