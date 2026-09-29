---
layout: Conceptual
title: Configure Ultra Disks for Azure virtual machines - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-enable-ultra-ssd
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
description: Learn how to check Ultra Disk availability, deploy and attach Ultra Disks, configure 512-byte sectors, and adjust performance for Azure virtual machines.
ms.topic: how-to
ms.date: 2026-09-18T00:00:00.0000000Z
ms.custom: references_regions, devx-track-azurecli, devx-track-azurepowershell, devx-track-arm-template, portal
locale: en-us
document_id: a4c7ec02-cc18-3f20-704e-79f148f136e8
document_version_independent_id: beb667ae-5d75-c979-f621-c75e21453b6a
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/disks-enable-ultra-ssd.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli
toc_rel: toc.json
asset_id: virtual-machines/disks-enable-ultra-ssd
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/disks-enable-ultra-ssd.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 54a7369b-3ad8-0bb7-9162-d2c6e6393711
---

# Configure Ultra Disks for Azure virtual machines - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

This article explains how to check Ultra Disk availability, deploy a VM with an Ultra Disk, configure an Ultra Disk with a 512-byte sector size, attach an Ultra Disk to an existing VM, and adjust Ultra Disk performance. For conceptual information about Ultra Disks, see [What disk types are available in Azure?](disks-types#ultra-disks)

Azure Ultra Disks offer high throughput, high IOPS, and consistent low latency disk storage for Azure IaaS virtual machines (VMs). This new offering provides top of the line performance at the same availability levels as our existing disks offerings. One major benefit of Ultra Disks is the ability to dynamically change the performance of the SSD along with your workloads without the need to restart your VMs. Ultra Disks are suited for data-intensive workloads such as SAP HANA, top tier databases, and transaction-heavy workloads.

## GA scope and limitations

The following list contains Ultra Disk's limitations:

- Ultra Disks can't be used as an OS disk or with Azure Compute Gallery.
- Currently, Ultra Disks only support Single VM and Availability zone infrastructure options as locally redundant storage (LRS). Ultra Disks don't support zone redundant storage (ZRS).
- Ultra Disks don't support availability sets.
- Ultra Disks don't support disk caching.

Ultra Disks support a 4k physical sector size by default but also supports a 512E sector size. Most applications are compatible with 4k sector sizes, but some require 512-byte sector sizes. Oracle Database, for example, requires release 12.2 or later in order to support 4k native disks. For older versions of Oracle DB, 512-byte sector size is required.

The following table outlines the regions Ultra Disks are available in, and their corresponding availability options.

Note

If a region in the following list lacks availability zones that support Ultra Disks, then a VM in that region must be deployed without infrastructure redundancy to attach an Ultra Disk.

| Redundancy options | Regions |
| --- | --- |
| **Regional** | Australia CentralAustralia Central 2Australia SoutheastBrazil SoutheastCanada EastKorea SouthNorth Central USNorway WestTaiwan NorthUAE CentralUK WestUS Gov ArizonaUS Gov TexasWest US |
| **One availability zone** | Brazil SouthCentral IndiaEast AsiaKorea CentralUS Gov Virginia |
| **Two availability zones** | Germany West CentralJapan WestQatar CentralSouth Central USSpain Central |
| **Three availability zones** | Australia EastAustria EastCanada CentralCentral USChina North 3East USEast US 2France CentralIndonesia CentralItaly NorthJapan EastMalaysia WestNew Zealand NorthNorth EuropePoland CentralSouth Africa NorthSoutheast AsiaSweden CentralSwitzerland NorthUAE NorthUK SouthWest EuropeWest US 2West US 3 |

Not every VM size is available in every supported region with Ultra Disks. The following table lists VM series that are compatible with Ultra Disks.

| VM Type | Sizes | Description |
| --- | --- | --- |
| General purpose | [DSv3-series](/en-us/azure/virtual-machines/sizes/general-purpose/dsv3-series?tabs=sizebasic), [Ddsv4-series](/en-us/azure/virtual-machines/sizes/general-purpose/ddsv4-series?tabs=sizestorageremote), [Dsv4-series](/en-us/azure/virtual-machines/sizes/general-purpose/dsv4-series?tabs=sizebasic), [Dasv4-series](/en-us/azure/virtual-machines/sizes/general-purpose/dasv4-series?tabs=sizestorageremote), [Dsv5-series](/en-us/azure/virtual-machines/sizes/general-purpose/dsv5-series?tabs=sizestorageremote), [Ddsv5-series](/en-us/azure/virtual-machines/sizes/general-purpose/ddsv5-series?tabs=sizestorageremote), [Dasv5-series](/en-us/azure/virtual-machines/sizes/general-purpose/dasv5-series?tabs=sizestorageremote), [Dplsv6-series](/en-us/azure/virtual-machines/sizes/general-purpose/dplsv6-series?tabs=sizestorageremote), [Dpldsv6-series](/en-us/azure/virtual-machines/sizes/general-purpose/dpldsv6-series?tabs=sizestorageremote), [Dpsv6-series](/en-us/azure/virtual-machines/sizes/general-purpose/dpsv6-series?tabs=sizestorageremote), [Dpdsv6-series](/en-us/azure/virtual-machines/sizes/general-purpose/dpdsv6-series?tabs=sizestorageremote) | Balanced CPU-to-memory ratio. Ideal for testing and development, small to medium databases, and low to medium traffic web servers. |
| Compute optimized | [FSv2-series](/en-us/azure/virtual-machines/fsv2-series), [Famsv6-series](/en-us/azure/virtual-machines/sizes/compute-optimized/famsv6-series?tabs=sizestorageremote) | High CPU-to-memory ratio. Good for medium traffic web servers, network appliances, batch processes, and application servers. |
| Memory optimized | [ESv3-series](/en-us/azure/virtual-machines/ev3-esv3-series#esv3-series), [Easv4-series](/en-us/azure/virtual-machines/sizes/memory-optimized/easv4-series?tabs=sizestorageremote), [Edsv4-series](/en-us/azure/virtual-machines/sizes/memory-optimized/edsv4-series?tabs=sizestorageremote), [Esv4-series](/en-us/azure/virtual-machines/sizes/memory-optimized/esv4-series?tabs=sizestorageremote), [Esv5-series](/en-us/azure/virtual-machines/sizes/memory-optimized/esv5-series?tabs=sizestorageremote), [Edsv5-series](/en-us/azure/virtual-machines/sizes/memory-optimized/edsv5-series?tabs=sizestorageremote), [Easv5-series](/en-us/azure/virtual-machines/easv5-eadsv5-series#easv5-series), [Ebsv5 series](/en-us/azure/virtual-machines/ebdsv5-ebsv5-series#ebsv5-series), [Ebdsv5 series](/en-us/azure/virtual-machines/ebdsv5-ebsv5-series#ebdsv5-series), [M-series](/en-us/azure/virtual-machines/sizes/memory-optimized/m-series?tabs=sizestorageremote), [Mv2-series](/en-us/azure/virtual-machines/sizes/memory-optimized/mv2-series?tabs=sizestorageremote), [Msv2](/en-us/azure/virtual-machines/sizes/memory-optimized/msv2-mm-series?tabs=sizestorageremote), [Mdsv2-series](/en-us/azure/virtual-machines/sizes/memory-optimized/mdsv2-mm-series?tabs=sizestorageremote), [Mbsv3](/en-us/azure/virtual-machines/sizes/memory-optimized/mbsv3-series?tabs=sizestorageremote), [Mbdsv3-series](/en-us/azure/virtual-machines/sizes/memory-optimized/mbdsv3-series?tabs=sizestorageremote), [Epsv6-series](/en-us/azure/virtual-machines/sizes/memory-optimized/epsv6-series?tabs=sizebasic), [Epdsv6-series](/en-us/azure/virtual-machines/sizes/memory-optimized/epdsv6-series?tabs=sizebasic) | High memory-to-CPU ratio. Great for relational database servers, medium to large caches, and in-memory analytics. |
| Storage optimized | [LSv2-series](/en-us/azure/virtual-machines/lsv2-series), [Lsv3-series](/en-us/azure/virtual-machines/lsv3-series), [Lasv3-series](/en-us/azure/virtual-machines/lasv3-series) | High disk throughput and IO ideal for Big Data, SQL, NoSQL databases, data warehousing, and large transactional databases. |
| GPU optimized | [NCv3-series](/en-us/azure/virtual-machines/ncv3-series), [NCasT4_v3-series](/en-us/azure/virtual-machines/nct4-v3-series), [ND-series](/en-us/azure/virtual-machines/nd-series), [NDv2-series](/en-us/azure/virtual-machines/ndv2-series), [NVv3-series](/en-us/azure/virtual-machines/nvv3-series), [NVv4-series](/en-us/azure/virtual-machines/nvv4-series), [NVadsA10 v5-series](/en-us/azure/virtual-machines/nva10v5-series) | Specialized virtual machines targeted for heavy graphic rendering and video editing, as well as model training and inferencing (ND) with deep learning. Available with single or multiple GPUs. |
| Performance optimized | [HC-series](/en-us/azure/virtual-machines/hc-series), [HBv2-series](/en-us/azure/virtual-machines/hbv2-series) | The fastest and most powerful CPU virtual machines with optional high-throughput network interfaces (RDMA). |

## Determine VM size and region availability

### VMs using availability zones

To use Ultra Disks, you need to determine which availability zone you are in. Not every region supports every VM size with Ultra Disks. To determine if your region, zone, and VM size support Ultra Disks, run either of the following commands, make sure to replace the **region**, **vmSize**, and **subscriptionId** values first:

#### Azure CLI

Use [`az vm list-skus`](/en-us/cli/azure/vm#az-vm-list-skus) to check Ultra Disk availability for a VM size, region, and subscription.

```azurecli
subscriptionId="<yourSubID>"
# Example value is southeastasia
region="<yourLocation>"
# Example value is Standard_E64s_v3
vmSize="<yourVMSize>"

az vm list-skus --resource-type virtualMachines --location $region --query "[?name=='$vmSize'].locationInfo[0].zoneDetails[0].Name" --subscription $subscriptionId
```

#### Azure PowerShell

Use [`Get-AzComputeResourceSku`](/en-us/powershell/module/az.compute/get-azcomputeresourcesku) to check Ultra Disk availability for a VM size and region.

```powershell
# Example value is southeastasia
$region = "<yourLocation>"
# Example value is Standard_E64s_v3
$vmSize = "<yourVMSize>"
$sku = (Get-AzComputeResourceSku | where {$_.Locations -icontains($region) -and ($_.Name -eq $vmSize) -and $_.LocationInfo[0].ZoneDetails.Count -gt 0})
if($sku){$sku[0].LocationInfo[0].ZoneDetails} Else {Write-host "$vmSize is not supported with Ultra Disk in $region region"}
```

The response will be similar to the form below, where X is the zone to use for deploying in your chosen region. X could be either 1, 2, or 3.

Preserve the **Zones** value, it represents your availability zone and you'll need it in order to deploy an Ultra Disk.

| ResourceType | Name | Location | Zones | Restriction | Capability | Value |
| --- | --- | --- | --- | --- | --- | --- |
| disks | UltraSSD\_LRS | eastus2 | X |  |  |  |

Note

If there was no response from the command, then the selected VM size is not supported with Ultra Disks in the selected region.

Now that you know which zone to deploy to, follow the deployment steps in this article to either deploy a VM with an Ultra Disk attached or attach an Ultra Disk to an existing VM.

### VMs with no redundancy options

Ultra Disks deployed in select regions must be deployed without any redundancy options for now. However, not every VM size that supports Ultra Disks are necessarily in these regions. To determine which VM sizes support Ultra Disks, use either of the following code snippets. Make sure to replace the `vmSize`, `region`, and `subscriptionId` values first:

#### Azure CLI

```azurecli
subscriptionId="<yourSubID>"
# Example value is westus
region="<yourLocation>"
# Example value is Standard_E64s_v3
vmSize="<yourVMSize>"

az vm list-skus --resource-type virtualMachines --location $region --query "[?name=='$vmSize'].capabilities" --subscription $subscriptionId
```

#### Azure PowerShell

```powershell
# Example value is westus
$region = "<yourLocation>"
# Example value is Standard_E64s_v3
$vmSize = "<yourVMSize>"
(Get-AzComputeResourceSku | where {$_.Locations -icontains($region) -and ($_.Name -eq $vmSize) })[0].Capabilities
```

The response will be similar to the following form, `UltraSSDAvailable   True` indicates whether the VM size supports Ultra Disks in this region.

```
Name                                         Value
----                                         -----
MaxResourceVolumeMB                          884736
OSVhdSizeMB                                  1047552
vCPUs                                        64
HyperVGenerations                            V1,V2
MemoryGB                                     432
MaxDataDiskCount                             32
LowPriorityCapable                           True
PremiumIO                                    True
VMDeploymentTypes                            IaaS
vCPUsAvailable                               64
ACUs                                         160
vCPUsPerCore                                 2
CombinedTempDiskAndCachedIOPS                128000
CombinedTempDiskAndCachedReadBytesPerSecond  1073741824
CombinedTempDiskAndCachedWriteBytesPerSecond 1073741824
CachedDiskBytes                              1717986918400
UncachedDiskIOPS                             80000
UncachedDiskBytesPerSecond                   1258291200
EphemeralOSDiskSupported                     True
AcceleratedNetworkingEnabled                 True
RdmaEnabled                                  False
MaxNetworkInterfaces                         8
UltraSSDAvailable                            True
```

## Deploy a VM with Ultra Disks by using Azure Resource Manager

First, determine the VM size to deploy. For a list of supported VM sizes, see the GA scope and limitations section.

If you would like to create a VM with multiple Ultra Disks, refer to the sample [Create a VM with multiple Ultra Disks](https://aka.ms/ultradiskArmTemplate).

If you intend to use your own template, make sure that **apiVersion** for `Microsoft.Compute/virtualMachines` and `Microsoft.Compute/Disks` is set as `2018-06-01` (or later).

Set the disk sku to **UltraSSD\_LRS**, then set the disk capacity, IOPS, availability zone, and throughput in MBps to create an Ultra Disk.

Once the VM is provisioned, you can partition and format the data disks and configure them for your workloads.

## Deploy a VM with an Ultra Disk

# [Portal](#tab/azure-portal)
This section covers deploying a virtual machine equipped with an Ultra Disk as a data disk. It assumes you have familiarity with deploying a virtual machine, if you don't, see our [Quickstart: Create a Windows virtual machine in the Azure portal](windows/quick-create-portal).

1. Sign in to the [Azure portal](https://portal.azure.com/) and navigate to deploy a virtual machine (VM).
2. Make sure to choose a supported VM size and region.
3. Select **Availability zone** in **Availability options**.
4. Fill in the remaining entries with selections of your choice.
5. Select **Disks**.

    [![Screenshot of the Create a virtual machine Basics pane with Availability options set to Availability zone and Availability zone set to Zone 3.](media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-vm-create.png)](media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-vm-create.png#lightbox)
6. On the Disks blade, select **Yes** for **Enable Ultra Disk compatibility**.
7. Select **Create and attach a new disk** to attach an Ultra Disk now.

    [![Screenshot of the virtual machine Disks pane with Enable Ultra Disk compatibility selected and Create and attach a new disk highlighted.](media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-vm-disk-enable.png)](media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-vm-disk-enable.png#lightbox)
8. On the **Create a new disk** blade, enter a name, then select **Change size**.

    [![Screenshot of the Create a new disk pane with a 1,024-GiB Premium SSD LRS selected and Change size highlighted.](media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-create-disk.png)](media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-create-disk.png#lightbox)
9. Change the **Disk SKU** to **Ultra Disk**.
10. Change the values of **Custom disk size (GiB)**, **Disk IOPS**, and **Disk throughput** to ones of your choice.
11. Select **OK** in both blades.

    [![Screenshot of the Select a disk size pane with the Ultra Disk SKU and custom disk size, IOPS, and throughput settings highlighted.](media/virtual-machines-disks-getting-started-ultra-ssd/new-select-ultra-disk-size.png)](media/virtual-machines-disks-getting-started-ultra-ssd/new-select-ultra-disk-size.png#lightbox)
12. Continue with the VM deployment, the same as you would deploy any other VM.

# [Azure CLI](#tab/azure-cli)
First, determine the VM size to deploy. See the GA scope and limitations section for a list of supported VM sizes.

You must create a VM that is capable of using Ultra Disks, in order to attach an Ultra Disk.

Set the variables to your own values. Set `zone` to the availability zone that you got from Determine VM size and region availability. Then run the following Azure CLI commands to create an Ultra-enabled VM with an attached Ultra Disk:

```azurecli
subscriptionId="<yourSubscriptionID>"
rgName="<yourResourceGroupName>"
vmName="<yourVMName>"
diskName="<yourDiskName>"
region="<yourLocation>"
zone="<yourAvailabilityZone>"
user="<yourAdminUsername>"
password="<yourAdminPassword>"

az disk create --subscription $subscriptionId -n $diskName -g $rgName --size-gb 1024 --location $region --zone $zone --sku UltraSSD_LRS --disk-iops-read-write 8192 --disk-mbps-read-write 400
az vm create --subscription $subscriptionId -n $vmName -g $rgName --image Win2016Datacenter --ultra-ssd-enabled true --zone $zone --authentication-type password --admin-password $password --admin-username $user --size Standard_D4s_v3 --location $region --attach-data-disks $diskName
```

Use [`az vm show`](/en-us/cli/azure/vm#az-vm-show) to confirm that `ultraSSDEnabled` is `true` and the Ultra Disk appears in the VM's data disks:

```azurecli
az vm show -g <yourResourceGroupName> -n <yourVMName> --query "{ultraSSDEnabled:additionalCapabilities.ultraSSDEnabled,dataDisks:storageProfile.dataDisks[].name}"
```

# [Azure PowerShell](#tab/azure-powershell)
First, determine the VM size to deploy. See the GA scope and limitations section for a list of supported VM sizes.

To use Ultra Disks, you must create a VM that can use Ultra Disks. Set the variables to your own values. Set `$zone` to the availability zone that you got from Determine VM size and region availability. Then run the following [New-AzVM](/en-us/powershell/module/az.compute/new-azvm) command to create an Ultra-enabled VM:

```powershell
$rgName = "<yourResourceGroup>"
$vmName = "<yourVMName>"
$region = "<yourLocation>"
$zone = "<yourAvailabilityZone>"

New-AzVM `
    -ResourceGroupName $rgName `
    -Name $vmName `
    -Location $region `
    -Image "Win2016Datacenter" `
    -EnableUltraSSD `
    -Size "Standard_D4s_v3" `
    -Zone $zone
```

### Create and attach the disk

Once your VM has been deployed, you can create and attach an Ultra Disk to it, use the following script:

```powershell
# Set parameters and select subscription
$subscriptionId = "<yourSubscriptionID>"
$rgName = "<yourResourceGroup>"
$vmName = "<yourVMName>"
$diskName = "<yourDiskName>"
$region = "<yourLocation>"
$zone = "<yourAvailabilityZone>"
$lun = 1
Connect-AzAccount -SubscriptionId $subscriptionId

# Create the disk
$diskConfig = New-AzDiskConfig `
    -Location $region `
    -DiskSizeGB 8 `
    -DiskIOPSReadWrite 1000 `
    -DiskMBpsReadWrite 100 `
    -AccountType UltraSSD_LRS `
    -CreateOption Empty `
    -Zone $zone

New-AzDisk `
    -ResourceGroupName $rgName `
    -DiskName $diskName `
    -Disk $diskConfig

# Add disk to VM
$vm = Get-AzVM -ResourceGroupName $rgName -Name $vmName
$disk = Get-AzDisk -ResourceGroupName $rgName -Name $diskName
$vm = Add-AzVMDataDisk -VM $vm -Name $diskName -CreateOption Attach -ManagedDiskId $disk.Id -Lun $lun
Update-AzVM -VM $vm -ResourceGroupName $rgName
```

Use [`Get-AzVM`](/en-us/powershell/module/az.compute/get-azvm) to confirm that Ultra Disk compatibility is enabled and the Ultra Disk appears in the VM's data disks:

```powershell
$vm = Get-AzVM -ResourceGroupName '<yourResourceGroup>' -Name '<yourVMName>'
$vm.AdditionalCapabilities.UltraSSDEnabled
$vm.StorageProfile.DataDisks | Select-Object Name, Lun
```

---

## Deploy an Ultra Disk with a 512-byte sector size

# [Portal](#tab/azure-portal)
1. Sign in to the [Azure portal](https://portal.azure.com/), then search for and select **Disks**.
2. Select **+ New** to create a new disk.
3. Select a region that supports Ultra Disks and select an availability zone, fill in the rest of the values as you desire.
4. Select **Change size**.

    [![Screenshot of the Create a managed disk Basics pane with Region set to West US 2, Availability zone set to 1, and Change size highlighted.](media/virtual-machines-disks-getting-started-ultra-ssd/create-managed-disk-basics-workflow.png)](media/virtual-machines-disks-getting-started-ultra-ssd/create-managed-disk-basics-workflow.png#lightbox)
5. For **Disk SKU** select **Ultra Disk**, then fill in the values for the desired performance and select **OK**.

    [![Screenshot of the Select a disk size pane with Ultra Disk selected, custom disk size set to 1,024 GiB, disk IOPS set to 2,048, and disk throughput set to 8 MB/s.](media/virtual-machines-disks-getting-started-ultra-ssd/select-disk-size-ultra.png)](media/virtual-machines-disks-getting-started-ultra-ssd/select-disk-size-ultra.png#lightbox)
6. On the **Basics** blade, select the **Advanced** tab.
7. Select **512** for **Logical sector size**, then select **Review + Create**.

    [![Screenshot of the Create a managed disk Advanced pane with Logical sector size set to 512 bytes.](media/virtual-machines-disks-getting-started-ultra-ssd/select-different-sector-size-ultra.png)](media/virtual-machines-disks-getting-started-ultra-ssd/select-different-sector-size-ultra.png#lightbox)

# [Azure CLI](#tab/azure-cli)
First, determine the VM size to deploy. See the GA scope and limitations section for a list of supported VM sizes.

You must create a VM that is capable of using Ultra Disks in order to attach an Ultra Disk.

Set the variables to your own values. Set `zone` to the availability zone that you got from Determine VM size and region availability. Then run the following Azure CLI commands to create a VM with an Ultra Disk that has a 512-byte sector size.

```azurecli
subscriptionId="<yourSubscriptionID>"
rgName="<yourResourceGroupName>"
vmName="<yourVMName>"
diskName="<yourDiskName>"
region="<yourLocation>"
zone="<yourAvailabilityZone>"
user="<yourAdminUsername>"
password="<yourAdminPassword>"

# Create an Ultra Disk with 512-byte sector size
az disk create --subscription $subscriptionId -n $diskName -g $rgName --size-gb 1024 --location $region --zone $zone --sku UltraSSD_LRS --disk-iops-read-write 8192 --disk-mbps-read-write 400 --logical-sector-size 512
az vm create --subscription $subscriptionId -n $vmName -g $rgName --image Win2016Datacenter --ultra-ssd-enabled true --zone $zone --authentication-type password --admin-password $password --admin-username $user --size Standard_D4s_v3 --location $region --attach-data-disks $diskName
```

Use [`az disk show`](/en-us/cli/azure/disk#az-disk-show) to confirm that `provisioningState` is `Succeeded` and `logicalSectorSize` is `512`:

```azurecli
az disk show -g <yourResourceGroupName> -n <yourDiskName> --query "{provisioningState:provisioningState,logicalSectorSize:logicalSectorSize}"
```

# [Azure PowerShell](#tab/azure-powershell)
First, determine the VM size to deploy. See the GA scope and limitations section for a list of supported VM sizes.

To use Ultra Disks, you must create a VM that can use Ultra Disks. Set the variables to your own values. Set `$zone` to the availability zone that you got from Determine VM size and region availability. Then run the following [New-AzVM](/en-us/powershell/module/az.compute/new-azvm) command to create an Ultra-enabled VM:

```powershell
$rgName = "<yourResourceGroup>"
$vmName = "<yourVMName>"
$region = "<yourLocation>"
$zone = "<yourAvailabilityZone>"

New-AzVM `
    -ResourceGroupName $rgName `
    -Name $vmName `
    -Location $region `
    -Image "Win2016Datacenter" `
    -EnableUltraSSD `
    -Size "Standard_D4s_v3" `
    -Zone $zone
```

To create and attach an Ultra Disk that has a 512-byte sector size, you can use the following script:

```powershell
# Set parameters and select subscription
$subscriptionId = "<yourSubscriptionID>"
$rgName = "<yourResourceGroup>"
$vmName = "<yourVMName>"
$diskName = "<yourDiskName>"
$region = "<yourLocation>"
$zone = "<yourAvailabilityZone>"
$lun = 1
Connect-AzAccount -SubscriptionId $subscriptionId

# Create the disk
$diskConfig = New-AzDiskConfig `
    -Location $region `
    -DiskSizeGB 8 `
    -DiskIOPSReadWrite 1000 `
    -DiskMBpsReadWrite 100 `
    -LogicalSectorSize 512 `
    -AccountType UltraSSD_LRS `
    -CreateOption Empty `
    -Zone $zone

New-AzDisk `
    -ResourceGroupName $rgName `
    -DiskName $diskName `
    -Disk $diskConfig

# Add disk to VM
$vm = Get-AzVM -ResourceGroupName $rgName -Name $vmName
$disk = Get-AzDisk -ResourceGroupName $rgName -Name $diskName
$vm = Add-AzVMDataDisk -VM $vm -Name $diskName -CreateOption Attach -ManagedDiskId $disk.Id -Lun $lun
Update-AzVM -VM $vm -ResourceGroupName $rgName
```

Use [`Get-AzDisk`](/en-us/powershell/module/az.compute/get-azdisk) to confirm that `ProvisioningState` is `Succeeded` and `LogicalSectorSize` is `512`:

```powershell
Get-AzDisk -ResourceGroupName '<yourResourceGroup>' -DiskName '<yourDiskName>' |
    Select-Object ProvisioningState, LogicalSectorSize
```

---

## Attach an Ultra Disk

### Additional limitations for regional Ultra Disks in regions with availability zones

When you attach a regional Ultra Disk to a regional VM in a region with availability zones, Azure might run a background copy to align the disk with the VM's availability zone and optimize latency. The copy can take up to 24 hours.

The following additional limitations apply during the background copy:

- You can't attach a nonzonal disk created from a snapshot, including an [instant access snapshot](disks-instant-access-snapshots), to a nonzonal VM in a region with availability zones until the copy finishes. To check the copy status, see [Performance impact of background copy](scripts/create-managed-disk-from-snapshot#performance-impact---background-copy-process).
- You can't resize the disk or change its customer-managed key.

Only one background copy can run on a nonzonal disk at a time. While a background copy is in progress, attaching the disk to a running nonzonal VM might fail. Restarting a stopped or deallocated nonzonal VM with the disk attached might also fail because the restart can trigger a second background copy.

# [Portal](#tab/azure-portal)
Alternatively, if your existing VM is in a region/availability zone that is capable of using Ultra Disks, you can make use of Ultra Disks without having to create a new VM. By enabling Ultra Disks on your existing VM, then attaching them as data disks. To enable Ultra Disk compatibility, you must stop the VM. After you stop the VM, you can enable compatibility, then restart the VM. Once compatibility is enabled, you can attach an Ultra Disk:

1. Navigate to your VM and stop it, wait for it to deallocate.
2. Once your VM has been deallocated, select **Disks**.
3. Select **Additional settings**.

    [![Screenshot of the virtual machine Disks toolbar with Additional settings highlighted.](media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-disk-additional-settings.png)](media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-disk-additional-settings.png#lightbox)
4. Select **Yes** for **Enable Ultra Disk compatibility**.

    [![Screenshot of the Ultra disk settings with Enable Ultra disk compatibility set to Yes.](media/virtual-machines-disks-getting-started-ultra-ssd/enable-ultra-disks-existing-vm.png)](media/virtual-machines-disks-getting-started-ultra-ssd/enable-ultra-disks-existing-vm.png#lightbox)
5. Select **Save**.
6. Select **Create and attach a new disk** and fill in a name for your new disk.
7. For **Storage type** select **Ultra Disk**.
8. Change the values of **Size (GiB)**, **Max IOPS**, and **Max throughput** to ones of your choice.
9. After you're returned to your disk's blade, select **Save**.

    [![Screenshot of the virtual machine Disks pane with a 4-GiB Ultra Disk data disk configured for 120 IOPS and 25 MB/s throughput, and Save highlighted.](media/virtual-machines-disks-getting-started-ultra-ssd/new-create-ultra-disk-existing-vm.png)](media/virtual-machines-disks-getting-started-ultra-ssd/new-create-ultra-disk-existing-vm.png#lightbox)
10. Start your VM again.

# [Azure CLI](#tab/azure-cli)
Alternatively, if your existing VM is in a region/availability zone that is capable of using Ultra Disks, you can make use of Ultra Disks without having to create a new VM.

### Enable Ultra Disk compatibility on an existing VM with Azure CLI

If your VM meets the requirements outlined in GA scope and limitations and is in the appropriate zone for your account, then you can enable Ultra Disk compatibility on your VM.

To enable Ultra Disk compatibility, you must stop the VM. After you stop the VM, you can enable compatibility, then restart the VM. Once compatibility is enabled, you can attach an Ultra Disk:

```azurecli
rgName="<yourResourceGroupName>"
vmName="<yourVMName>"

az vm deallocate -n $vmName -g $rgName
az vm update -n $vmName -g $rgName --ultra-ssd-enabled true
az vm start -n $vmName -g $rgName
```

### Create an Ultra Disk with Azure CLI

Now that you have a VM that is capable of attaching Ultra Disks, you can create and attach an Ultra Disk to it.

```azurecli
subscriptionId="<yourSubscriptionID>"
rgName="<yourResourceGroupName>"
vmName="<yourVMName>"
diskName="<yourDiskName>"
region="<yourLocation>"
zone="<yourAvailabilityZone>"

# Create an Ultra Disk
az disk create \
--subscription $subscriptionId \
-n $diskName \
-g $rgName \
--size-gb 4 \
--location $region \
--zone $zone \
--sku UltraSSD_LRS \
--disk-iops-read-write 1000 \
--disk-mbps-read-write 50
```

### Attach the Ultra Disk with Azure CLI

```azurecli
subscriptionId="<yourSubscriptionID>"
rgName="<yourResourceGroupName>"
vmName="<yourVMName>"
diskName="<yourDiskName>"

az vm disk attach -g $rgName --vm-name $vmName --disk $diskName --subscription $subscriptionId
```

Use `az vm show` to confirm that the Ultra Disk appears in the VM's data disks:

```azurecli
az vm show -g <yourResourceGroupName> -n <yourVMName> --query "storageProfile.dataDisks[].name"
```

# [Azure PowerShell](#tab/azure-powershell)
Alternatively, if your existing VM is in a region/availability zone that is capable of using Ultra Disks, you can make use of Ultra Disks without having to create a new VM.

### Enable Ultra Disk compatibility on an existing VM with Azure PowerShell

If your VM meets the requirements outlined in GA scope and limitations and is in the appropriate zone for your account, then you can enable Ultra Disk compatibility on your VM.

To enable Ultra Disk compatibility, you must stop the VM. After you stop the VM, you can enable compatibility, then restart the VM. Once compatibility is enabled, you can attach an Ultra Disk:

```powershell
$rgName = "<yourResourceGroup>"
$vmName = "<yourVMName>"

# Stop the VM
Stop-AzVM -Name $vmName -ResourceGroupName $rgName
# Enable Ultra Disk compatibility
$vm = Get-AzVM -name $vmName -ResourceGroupName $rgName
Update-AzVM -ResourceGroupName $rgName -VM $vm -UltraSSDEnabled $True
# Start the VM
Start-AzVM -Name $vmName -ResourceGroupName $rgName
```

### Create and attach an Ultra Disk with Azure PowerShell

Now that you have a VM that is capable of using Ultra Disks, you can create and attach an Ultra Disk to it:

```powershell
# Set parameters and select subscription
$subscriptionId = "<yourSubscriptionID>"
$rgName = "<yourResourceGroup>"
$vmName = "<yourVMName>"
$diskName = "<yourDiskName>"
$region = "<yourLocation>"
$zone = "<yourAvailabilityZone>"
$lun = 1
Connect-AzAccount -SubscriptionId $subscriptionId

# Create the disk
$diskConfig = New-AzDiskConfig `
    -Location $region `
    -DiskSizeGB 8 `
    -DiskIOPSReadWrite 1000 `
    -DiskMBpsReadWrite 100 `
    -AccountType UltraSSD_LRS `
    -CreateOption Empty `
    -zone $zone

New-AzDisk `
    -ResourceGroupName $rgName `
    -DiskName $diskName `
    -Disk $diskConfig

# Add disk to VM
$vm = Get-AzVM -ResourceGroupName $rgName -Name $vmName
$disk = Get-AzDisk -ResourceGroupName $rgName -Name $diskName
$vm = Add-AzVMDataDisk -VM $vm -Name $diskName -CreateOption Attach -ManagedDiskId $disk.Id -Lun $lun
Update-AzVM -VM $vm -ResourceGroupName $rgName
```

Use `Get-AzVM` to confirm that the Ultra Disk appears in the VM's data disks:

```powershell
(Get-AzVM -ResourceGroupName '<yourResourceGroup>' -Name '<yourVMName>').StorageProfile.DataDisks |
    Select-Object Name, Lun
```

---

## Adjust the performance of an Ultra Disk

# [Portal](#tab/azure-portal)
Ultra Disks offer a unique capability that allows you to adjust their performance. You can adjust the performance of an Ultra Disk four times within a 24 hour period.

1. Navigate to your VM and select **Disks**.
2. Select the Ultra Disk you'd like to modify the performance of.

    [![Screenshot of the virtual machine Data disks list with the Ultra Disk named ultra-disk-name highlighted at LUN 0.](media/virtual-machines-disks-getting-started-ultra-ssd/select-ultra-disk-to-modify.png)](media/virtual-machines-disks-getting-started-ultra-ssd/select-ultra-disk-to-modify.png#lightbox)
3. Select **Size + performance** and then make your modifications.
4. Select **Save**.

    [![Screenshot of the Ultra Disk Size + performance pane with custom disk size set to 32 GiB, disk IOPS set to 125, and disk throughput set to 25 MB/s.](media/virtual-machines-disks-getting-started-ultra-ssd/modify-ultra-disk-performance.png)](media/virtual-machines-disks-getting-started-ultra-ssd/modify-ultra-disk-performance.png#lightbox)

# [Azure CLI](#tab/azure-cli)
Ultra Disks offer a unique capability that allows you to adjust their performance. You can adjust the performance of an Ultra Disk four times within a 24 hour period. The following command depicts how to use this feature:

```azurecli
subscriptionId="<yourSubscriptionID>"
rgName="<yourResourceGroupName>"
diskName="<yourDiskName>"

az disk update --subscription $subscriptionId --resource-group $rgName --name $diskName --disk-iops-read-write=5000 --disk-mbps-read-write=200
```

Use `az disk show` to confirm that `diskIOPSReadWrite` is `5000` and `diskMBpsReadWrite` is `200`:

```azurecli
az disk show -g <yourResourceGroupName> -n <yourDiskName> --query "{diskIOPSReadWrite:diskIOPSReadWrite,diskMBpsReadWrite:diskMBpsReadWrite}"
```

# [Azure PowerShell](#tab/azure-powershell)
Ultra Disks have a unique capability that allows you to adjust their performance. You can adjust the performance of an Ultra Disk four times within a 24 hour period. The following command is an example that adjusts the performance without having to detach the disk:

```powershell
$rgName = "<yourResourceGroup>"
$diskName = "<yourDiskName>"

$diskUpdateConfig = New-AzDiskUpdateConfig -DiskMBpsReadWrite 2000
Update-AzDisk -ResourceGroupName $rgName -DiskName $diskName -DiskUpdate $diskUpdateConfig
```

Use `Get-AzDisk` to confirm that `DiskMBpsReadWrite` is `2000`:

```powershell
(Get-AzDisk -ResourceGroupName '<yourResourceGroup>' -DiskName '<yourDiskName>').DiskMBpsReadWrite
```

---