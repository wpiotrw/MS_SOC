---
layout: Conceptual
title: Tutorial - Manage Azure disks with the Azure CLI - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-disks
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
author: roygara
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: rogarana
ms.update-cycle: 365-days
description: In this tutorial, you learn how to use the Azure CLI to create and manage Azure disks for virtual machines
ms.service: azure-disk-storage
ms.topic: tutorial
ms.date: 2026-09-21T00:00:00.0000000Z
ms.custom: mvc, devx-track-azurecli, linux-related-content
ai-usage: ai-assisted
locale: en-us
document_id: 3ab24f5b-50fd-37cc-e031-34301147953d
document_version_independent_id: c2bc2467-8743-491c-c84c-f6983772f4da
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/linux/tutorial-manage-disks.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli
toc_rel: ../toc.json
asset_id: virtual-machines/linux/tutorial-manage-disks
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/linux/tutorial-manage-disks.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/cdc80360-921e-4b45-947f-2719acf06f23
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/539badf0-028a-4e3e-bda6-770b2552b4d8
platformId: 6bd8545b-e0ef-13b7-27bf-19baff29e529
---

# Tutorial - Manage Azure disks with the Azure CLI - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Flexible scale sets

Azure virtual machines (VMs) use disks to store the operating system, applications, and data. When you create a VM, it is important to choose a disk size and configuration appropriate to the expected workload. This tutorial shows you how to deploy and manage VM disks. You learn about:

- OS disks and temporary disks
- Data disks
- Disk types and performance options
- Disk performance
- Attaching and preparing data disks
- Disk snapshots

## Default Azure disks

When an Azure virtual machine is created, two disks are automatically attached to the virtual machine.

**Operating system disk** - The operating system (OS) disk hosts the VM operating system and can be up to 4,095 gibibytes (GiB), although many operating systems are partitioned with [master boot records (MBRs)](/en-us/windows/win32/fileio/basic-and-dynamic-disks#master-boot-record) by default. An MBR limits the usable size to 2 TiB. If you need more than 2 TiB, create and attach data disks and use them for data storage. Device names vary by VM generation and disk controller type, so don't rely on a fixed path such as */dev/sda*. OS disk caching is optimized for OS performance, so don't store application data on the OS disk. Use data disks for application and data storage.

**Temporary disk** - Temporary storage uses local storage on the same Azure host as the VM. Depending on the VM size and generation, this storage might appear as a temporary disk or local NVMe disk. It's high-performance, but nonpersistent. If the VM is moved to a new host, data on temporary storage is removed. The available size depends on the VM size.

## Data disks

To install applications and store data, additional data disks can be added. Data disks should be used in any situation where durable and responsive data storage is desired. The size of the virtual machine determines how many data disks can be attached to a VM.

## VM disk types

Azure managed disks offer five disk types:

- [Ultra Disks](../disks-types#ultra-disks)
- [Premium SSD v2](../disks-types#premium-ssd-v2)
- [Premium SSDs](../disks-types#premium-ssds)
- [Standard SSDs](../disks-types#standard-ssds)
- [Standard HDDs](../disks-types#standard-hdds)

In general, use Premium SSD v2 or Premium SSD for production workloads, Standard SSD for dev/test and less performance-sensitive workloads, and Ultra Disks for IO-intensive data workloads. Ultra Disks and Premium SSD v2 are data-disk only options and can't be used as OS disks. For detailed limits, region availability, and sizing guidance, see [Azure managed disk types](../disks-types).

## Launch Azure Cloud Shell

Azure Cloud Shell is a free interactive shell that you can use to run the steps in this article. It has common Azure tools preinstalled and configured to use with your account.

To open Cloud Shell, select **Try it** from the upper-right corner of a code block. You can also launch Cloud Shell in a separate browser tab at https://shell.azure.com. Select **Copy** to copy a code block, paste it into Cloud Shell, and press Enter to run it.

## Create and attach disks

Data disks can be created and attached at VM creation time or to an existing VM.

### Attach disk at VM creation

Create a resource group with the [az group create](/en-us/cli/azure/group#az-group-create) command.

```azurecli
az group create --name myResourceGroupDisk --location eastus
```

Create a VM by using the [az vm create](/en-us/cli/azure/vm#az-vm-create) command. The following example creates a VM named *myVM*, adds a user account named *azureuser*, and generates SSH keys if they don't already exist. The `--data-disk-sizes-gb` argument specifies extra data disks to create and attach. To create and attach more than one disk, use a space-delimited list of disk sizes. In the following example, you create a VM with two data disks, both 128 GiB. Because the disks are 128 GiB, you configure both as P10 disks, which provide a maximum of 500 IOPS per disk.

```azurecli
az vm create \
  --resource-group myResourceGroupDisk \
  --name myVM \
  --image Ubuntu2204 \
  --size Standard_DS2_v2 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --data-disk-sizes-gb 128 128
```

### Attach disk to existing VM

To create and attach a new disk to an existing virtual machine, use the [az vm disk attach](/en-us/cli/azure/vm/disk#az-vm-disk-attach) command. The following example creates a 128-GiB premium disk and attaches it to the VM created in the last step.

```azurecli
az vm disk attach \
    --resource-group myResourceGroupDisk \
    --vm-name myVM \
    --name myDataDisk \
    --size-gb 128 \
    --sku Premium_LRS \
    --new
```

## Prepare a data disk in Linux

After you attach a disk to the virtual machine, configure the operating system to use the disk. The following examples manually configure the first 128-GiB data disk that was attached when you created the VM. The VM's disk controller determines how Linux exposes the disk. You can also automate this process by using cloud-init, which is covered in a [later tutorial](tutorial-automate-vm-deployment).

Create an SSH connection with the virtual machine. Replace the example IP address with the public IP of the virtual machine.

```console
ssh azureuser@10.101.10.10
```

Verify that you identified the correct data disk before you format it. Formatting the wrong disk results in data loss.

# [SCSI](#tab/scsi)
On a VM with a SCSI controller, use `lsblk` to identify the data disk. The following examples use `/dev/sdc`. Replace `sdc` with the device name for your data disk.

```bash
lsblk -o NAME,HCTL,SIZE,MOUNTPOINT | grep -i "sd"
```

Partition the disk with `parted`, then use `partprobe` to make the operating system aware of the new partition table.

```bash
sudo parted /dev/sdc --script mklabel gpt mkpart xfspart xfs 0% 100%
sudo partprobe /dev/sdc
```

Write a file system to the partition by using the `mkfs` command.

```bash
sudo mkfs.xfs /dev/sdc1
```

Mount the new disk so that it is accessible in the operating system.

```bash
sudo mkdir /datadrive && sudo mount /dev/sdc1 /datadrive
```

The disk can now be accessed through the `/datadrive` mountpoint, which can be verified by running the `df -h` command.

```bash
df -h | grep -i "sd"
```

The output shows the new drive mounted on `/datadrive`.

```bash
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        29G  2.0G   27G   7% /
/dev/sda15      105M  3.6M  101M   4% /boot/efi
/dev/sdb1        14G   41M   13G   1% /mnt
/dev/sdc1       128G   52M  128G   1% /datadrive
```

# [NVMe](#tab/nvme)
On a VM with an NVMe controller, use `azure-nvme-id` from the [azure-vm-utils](azure-virtual-machine-utilities) package to identify the data disk. If the package isn't installed, follow the installation guidance in the azure-vm-utils article before you run the command. The following examples use `/dev/nvme0n2`. Replace `nvme0n2` with the device name for your data disk.

```bash
sudo azure-nvme-id
```

Partition the disk with `parted`, then use `partprobe` to make the operating system aware of the new partition table.

```bash
sudo parted /dev/nvme0n2 --script mklabel gpt mkpart xfspart xfs 0% 100%
sudo partprobe /dev/nvme0n2
```

Write a file system to the partition by using the `mkfs` command.

```bash
sudo mkfs.xfs /dev/nvme0n2p1
```

Mount the new disk so that it is accessible in the operating system.

```bash
sudo mkdir /datadrive && sudo mount /dev/nvme0n2p1 /datadrive
```

Verify that the data disk is mounted at `/datadrive`.

```bash
df -h | grep -i "nvme"
```

---

To ensure that the drive is remounted after a reboot, it must be added to the */etc/fstab* file. To do so, get the UUID of the disk with the `blkid` utility.

```bash
sudo -i blkid
```

The output displays the UUID of the drive. On a VM with a SCSI controller, the partition might appear as `/dev/sdc1`. On a VM with an NVMe controller, it might appear as `/dev/nvme0n2p1`.

```bash
/dev/sdc1: UUID="33333333-3b3b-3c3c-3d3d-3e3e3e3e3e3e" TYPE="xfs"
```

Note

Improperly editing the **/etc/fstab** file could result in an unbootable system. If unsure, refer to the distribution's documentation for information on how to properly edit this file. It is also recommended that a backup of the /etc/fstab file is created before editing.

Open the `/etc/fstab` file in a text editor as follows:

```bash
sudo nano /etc/fstab
```

Add a line similar to the following to the */etc/fstab* file, replacing the UUID value with your own.

```bash
UUID=33333333-3b3b-3c3c-3d3d-3e3e3e3e3e3e   /datadrive  xfs    defaults,nofail   1  2
```

When you are done editing the file, use `Ctrl+O` to write the file and `Ctrl+X` to exit the editor.

Now that the disk has been configured, close the SSH session.

```bash
exit
```

## Take a disk snapshot

When you take a disk snapshot, Azure creates a read-only, point-in-time copy of the disk. Azure VM snapshots are useful to quickly save the state of a VM before you make configuration changes. In the event of an issue or error, you can restore a VM by using a snapshot. When a VM has more than one disk, a snapshot is taken of each disk independently. To take application-consistent backups, consider stopping the VM before you take disk snapshots. Alternatively, use [Azure Backup](/en-us/azure/backup/), which supports automated backups while the VM is running.

### Create snapshot

Before you create a snapshot, you need the ID or name of the disk. Use [az vm show](/en-us/cli/azure/vm#az-vm-show) to show the disk ID. In this example, the disk ID is stored in a variable so that it can be used in a later step.

```azurecli
osdiskid=$(az vm show \
   -g myResourceGroupDisk \
   -n myVM \
   --query "storageProfile.osDisk.managedDisk.id" \
   -o tsv)
```

Now that you have the ID, use [az snapshot create](/en-us/cli/azure/snapshot#az-snapshot-create) to create a snapshot of the disk.

```azurecli
az snapshot create \
    --resource-group myResourceGroupDisk \
    --source "$osdiskid" \
    --name osDisk-backup
```

### Create disk from snapshot

This snapshot can then be converted into a disk using [az disk create](/en-us/cli/azure/disk#az-disk-create), which can be used to recreate the virtual machine.

```azurecli
az disk create \
   --resource-group myResourceGroupDisk \
   --name mySnapshotDisk \
   --source osDisk-backup
```

### Restore virtual machine from snapshot

Before you delete the VM, use [az vm show](/en-us/cli/azure/vm#az-vm-show) to store the resource IDs of all its data disks in the `dataDiskIds` variable.

```azurecli
dataDiskIds=$(az vm show \
   --resource-group myResourceGroupDisk \
   --name myVM \
   --query "storageProfile.dataDisks[].managedDisk.id" \
   --output tsv)
```

To demonstrate virtual machine recovery, delete the existing virtual machine using [az vm delete](/en-us/cli/azure/vm#az-vm-delete).

```azurecli
az vm delete \
--resource-group myResourceGroupDisk \
--name myVM
```

Create a new virtual machine from the snapshot disk.

```azurecli
az vm create \
    --resource-group myResourceGroupDisk \
    --name myVM \
    --attach-os-disk mySnapshotDisk \
    --os-type linux
```

### Reattach data disks

All data disks need to be reattached to the virtual machine.

Use [az vm disk attach](/en-us/cli/azure/vm/disk#az-vm-disk-attach) with each resource ID to reattach all the data disks.

```azurecli
for dataDiskId in $dataDiskIds; do
   az vm disk attach \
      --resource-group myResourceGroupDisk \
      --vm-name myVM \
      --name "$dataDiskId"
done
```