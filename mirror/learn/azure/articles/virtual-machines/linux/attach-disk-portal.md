---
layout: Conceptual
title: Use the portal to attach a data disk to a Linux VM - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/attach-disk-portal
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
description: Use the portal to attach new or existing data disk to a Linux virtual machine.
ms.date: 2026-09-21T00:00:00.0000000Z
ms.service: azure-disk-storage
ms.topic: how-to
ms.collection: linux
ai-usage: ai-assisted
ms.custom:
- linux-related-content
- ge-structured-content-pilot
locale: en-us
document_id: 6fde1939-787d-2aa5-4b29-d303f8ed49cb
document_version_independent_id: c2838cb5-c34c-e0ff-b280-b86f29453cad
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/linux/attach-disk-portal.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/linux/attach-disk-portal
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/linux/attach-disk-portal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: cf37f054-1cc1-1505-c7ee-6bf3a356b030
---

# Use the portal to attach a data disk to a Linux VM - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Flexible scale sets

This article shows you how to attach both new and existing disks to a Linux virtual machine through the Azure portal. You can also [attach a data disk to a Windows VM in the Azure portal](/en-us/azure/virtual-machines/windows/attach-managed-disk-portal).

## Find the Linux VM in the Azure portal

Follow these steps:

1. Go to the [Azure portal](https://portal.azure.com/) to find the VM. Search for and select **Virtual machines**.
2. Select the VM you'd like to attach the disk to from the list.
3. In the **Virtual machines** page, under **Settings**, select **Disks**.

## Attach a new managed data disk in the Azure portal

Follow these steps:

1. On the **Disks** pane, under **Data disks**, select **Create and attach a new disk**.
2. Enter a name for your managed disk. Review the default settings, and update the **Storage type**, **Size (GiB)**, **Encryption** and **Host caching** as necessary.

    [![Screenshot of the Azure portal Data disks pane showing the LUN, disk name, storage type, size, encryption, and host caching settings for a new managed disk.](media/attach-disk-portal/create-new-md.png)](media/attach-disk-portal/create-new-md.png#lightbox)
3. When you're done, select **Save** at the top of the page to create the managed disk and update the VM configuration.

## Attach an existing managed data disk in the Azure portal

Follow these steps:

1. On the **Disks** pane, under **Data disks**, select **Attach existing disks**.
2. Select the drop-down menu for **Disk name** and select a disk from the list of available managed disks.
3. Select **Save** to attach the existing managed disk and update the VM configuration.

## Connect to the Linux VM to mount the new disk

To partition, format, and mount your new disk so your Linux VM can use it, SSH into your VM. For more information, see [How to use SSH with Linux on Azure](mac-create-ssh-keys). The following example connects to a VM with the public IP address of *10.123.123.25* with the username *azureuser*:

```bash
ssh azureuser@10.123.123.25
```

## Find the attached data disk in Linux

Azure Linux VMs can expose managed disks through SCSI or NVMe controllers. Select the controller type that your VM uses. For details about the controller types, see [SCSI to NVMe conversion](/en-us/azure/virtual-machines/nvme-linux#scsi-vs-nvme).

# [SCSI](#tab/scsi)
Use `lsblk` to list disks on a VM with a SCSI controller:

```bash
lsblk -o NAME,HCTL,SIZE,MOUNTPOINT | grep -i "sd"
```

The output is similar to the following example:

```output
sda     0:0:0:0      30G
├─sda1             29.9G /
├─sda14               4M
└─sda15             106M /boot/efi
sdb     1:0:1:0      14G
└─sdb1               14G /mnt
sdc     3:0:0:0       4G
```

In this example, the disk that you added is `sdc`. It uses LUN 0 and has a capacity of 4 GiB.

For a more complex example, here's what multiple data disks look like in the portal:

![Screenshot of three Azure managed data disks: a 4-GiB Premium SSD at LUN 0, a 16-GiB Premium SSD at LUN 1, and a 32-GiB Standard HDD at LUN 2.](media/attach-disk-portal/find-disk.png)

In the image, you can see three data disks: 4 GiB on LUN 0, 16 GiB on LUN 1, and 32 GiB on LUN 2.

From the output of `lsblk`, you can see that the 4-GiB disk at LUN 0 is `sdc`, the 16-GiB disk at LUN 1 is `sdd`, and the 32-GiB disk at LUN 2 is `sde`.

```output
sda     0:0:0:0      30G
├─sda1             29.9G /
├─sda14               4M
└─sda15             106M /boot/efi
sdb     1:0:1:0      14G
└─sdb1               14G /mnt
sdc     3:0:0:0       4G
sdd     3:0:0:1      16G
sde     3:0:0:2      32G
```

# [NVMe](#tab/nvme)
Use `azure-nvme-id` from the [azure-vm-utils](azure-virtual-machine-utilities) package to identify disks exposed through an NVMe controller and their LUNs. If the package isn't installed, follow the installation guidance in the azure-vm-utils article before you run the command.

```bash
sudo azure-nvme-id
```

The output is similar to the following example:

```output
/dev/nvme0n1: type=os
/dev/nvme0n2: type=data, lun=0
/dev/nvme1n1: type=local, index=1, name=nvme-50G-1
```

In this example, `/dev/nvme0n2` is the managed data disk at LUN 0.

---

## Prepare a new empty data disk in Linux

Important

If you're using an existing disk that contains data, skip to mounting the disk. The following instructions delete data on the disk. Verify that you identified the correct disk before you format it.

If you're attaching a new disk, you need to partition the disk.

Use the `parted` utility to partition a data disk and `mkfs.xfs` to format the partition with the XFS file system.

- Use the latest version of `parted` that's available for your distribution.
- If the disk size is 2 tebibytes (TiB) or larger, you must use GPT partitioning. If disk size is under 2 TiB, then you can use either MBR or GPT partitioning.

# [SCSI](#tab/scsi)
The following example uses `parted` on `/dev/sdc`, which is where the first data disk typically is on most VMs. Replace `sdc` with the correct option for your disk. The example formats the partition by using the [XFS](https://xfs.wiki.kernel.org/) file system.

```bash
sudo parted /dev/sdc --script mklabel gpt mkpart xfspart xfs 0% 100%
sudo partprobe /dev/sdc
sudo mkfs.xfs /dev/sdc1
```

# [NVMe](#tab/nvme)
The following example uses `parted` on `/dev/nvme0n2`. Replace `nvme0n2` with the managed data disk that you identified with `azure-nvme-id`.

```bash
sudo parted /dev/nvme0n2 --script mklabel gpt mkpart xfspart xfs 0% 100%
sudo partprobe /dev/nvme0n2
sudo mkfs.xfs /dev/nvme0n2p1
```

---

Use the [`partprobe`](https://linux.die.net/man/8/partprobe) utility to ensure the kernel recognizes the new partition table. If you don't use `partprobe`, the `blkid` or `lsblk` commands might not return the UUID for the new file system right away.

## Mount the data disk in Linux

Create a directory to mount the file system by using `mkdir`:

```bash
sudo mkdir /datadrive
```

Use `mount` to mount the file system.

# [SCSI](#tab/scsi)
Replace `/dev/sdc1` with the partition for the data disk that you identified on the VM with a SCSI controller.

```bash
sudo mount /dev/sdc1 /datadrive
```

# [NVMe](#tab/nvme)
Replace `/dev/nvme0n2p1` with the partition for the data disk that you identified on the VM with an NVMe controller.

```bash
sudo mount /dev/nvme0n2p1 /datadrive
```

---

Add the drive to the */etc/fstab* file to ensure the drive is automatically added after a reboot.

Ensure that the UUID (Universally Unique Identifier) is used in */etc/fstab* to refer to the drive rather than a device name, such as */dev/sdc1* or */dev/nvme0n2p1*. If the OS detects a disk error during boot, using the UUID avoids the incorrect disk being mounted to a given location. Remaining data disks would then be assigned those same device IDs. To find the UUID of the new drive, use the `blkid` utility.

```bash
sudo blkid
```

The following output is from a VM with a SCSI controller. On a VM with an NVMe controller, the managed data disk partition appears as an NVMe path such as `/dev/nvme0n2p1` instead of `/dev/sdc1`.

```output
/dev/sda1: LABEL="cloudimg-rootfs" UUID="11111111-1b1b-1c1c-1d1d-1e1e1e1e1e1e" TYPE="ext4" PARTUUID="1a1b1c1d-11aa-1234-1a1a1a1a1a1a"
/dev/sda15: LABEL="UEFI" UUID="BCD7-96A6" TYPE="vfat" PARTUUID="1e1g1cg1h-11aa-1234-1u1u1a1a1u1u"
/dev/sdb1: UUID="22222222-2b2b-2c2c-2d2d-2e2e2e2e2e2e" TYPE="ext4" PARTUUID="1a2b3c4d-01"
/dev/sda14: PARTUUID="2e2g2cg2h-11aa-1234-1u1u1a1a1u1u"
/dev/sdc1: UUID="33333333-3b3b-3c3c-3d3d-3e3e3e3e3e3e" TYPE="xfs" PARTLABEL="xfspart" PARTUUID="c1c2c3c4-1234-cdef-asdf3456ghjk"
```

## Configure automatic mounting in /etc/fstab

Note

Improperly editing the **/etc/fstab** file could result in an unbootable system. If unsure, refer to the distribution's documentation for information on how to properly edit this file. You should create a backup of the **/etc/fstab** file is created before editing.

Next, open the **/etc/fstab** file in a text editor. Add a line to the end of the file, using the UUID value for the partition that you created in the previous steps, and the mount point of `/datadrive`. If you used the example from this article, the new line would look like the following sample.

```config
UUID=33333333-3b3b-3c3c-3d3d-3e3e3e3e3e3e   /datadrive   xfs   defaults,nofail   1   2
```

When you're done editing the file, save and close the editor.

Note

Later removing a data disk without editing fstab could cause the VM to fail to boot. Most distributions provide either the *nofail* and/or *nobootwait* fstab options. These options allow a system to boot even if the disk fails to mount at boot time. Consult your distribution's documentation for more information on these parameters.

The *nofail* option ensures that the VM starts even if the file system is corrupt or the disk doesn't exist at boot time. Without this option, you might encounter behavior as described in [Cannot SSH to Linux VM due to FSTAB errors](/en-us/archive/blogs/linuxonazure/cannot-ssh-to-linux-vm-after-adding-data-disk-to-etcfstab-and-rebooting)

## Verify the mounted data disk in Linux

Use `lsblk` again to verify that the data disk is mounted at `/datadrive`.

# [SCSI](#tab/scsi)
```bash
lsblk -o NAME,HCTL,SIZE,MOUNTPOINT | grep -i "sd"
```

```output
sda     0:0:0:0      30G
├─sda1             29.9G /
├─sda14               4M
└─sda15             106M /boot/efi
sdb     1:0:1:0      14G
└─sdb1               14G /mnt
sdc     3:0:0:0       4G
└─sdc1                4G /datadrive
```

# [NVMe](#tab/nvme)
```bash
lsblk -o NAME,TYPE,SIZE,MOUNTPOINT | grep nvme
```

```output
nvme0n1       disk    30G
├─nvme0n1p1   part  29.9G /
├─nvme0n1p14  part     4M
└─nvme0n1p15  part   106M /boot/efi
nvme0n2       disk     4G
└─nvme0n2p1   part     4G /datadrive
```

---

## TRIM/UNMAP support for Linux in Azure

Some Linux kernels support TRIM/UNMAP operations to discard unused blocks on the disk. This feature is primarily useful to inform Azure that deleted pages are no longer valid and can be discarded. This feature can save money on disks that are billed based on the amount of consumed storage, such as unmanaged standard disks and disk snapshots.

There are two ways to enable TRIM support in your Linux VM. As usual, consult your distribution for the recommended approach:

1. Use the `discard` mount option in */etc/fstab*, for example:

    ```config
    UUID=33333333-3b3b-3c3c-3d3d-3e3e3e3e3e3e   /datadrive   xfs   defaults,discard   1   2
    ```
2. In some cases, the `discard` option may have performance implications. Alternatively, you can run the `fstrim` command manually from the command line, or add it to your crontab to run regularly:

    **Ubuntu**

    ```bash
    sudo apt-get install util-linux
    sudo fstrim /datadrive
    ```

    **RHEL**

    ```bash
    sudo yum install util-linux
    sudo fstrim /datadrive
    ```

    **SUSE**

    ```bash
    sudo zypper install util-linux
    sudo fstrim /datadrive
    ```