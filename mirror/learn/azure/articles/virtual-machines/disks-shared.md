---
layout: Conceptual
title: Share an Azure managed disk across VMs - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-shared
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
description: Learn how Azure shared disks let you share Azure managed disks across multiple Linux and Windows virtual machines.
ms.custom: linux-related-content
ms.topic: concept-article
ms.date: 2026-10-13T00:00:00.0000000Z
locale: en-us
document_id: bb821041-48aa-bb12-17af-6fec35719311
document_version_independent_id: dce2e4b0-f05f-09e8-7045-295f9064e3de
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/disks-shared.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/disks-shared
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/disks-shared.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 833aed18-acdc-a602-4dcc-121b386f2ba3
---

# Share an Azure managed disk across VMs - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

Azure shared disks is a feature for Azure managed disks that allows you to attach a managed disk to multiple virtual machines (VMs) simultaneously. This capability enables you to deploy new or migrate existing clustered applications to Azure without modifying your architecture. Shared disks ensure high availability for clustered applications, as other VMs in the cluster retain full access to the disk if one VM fails.

Shared disks require a cluster manager, like Windows Server Failover Cluster (WSFC), or Pacemaker, that handles cluster node communication and write locking. Shared managed disks don't natively offer a fully managed file system that can be accessed using SMB/NFS.

## How it works

VMs in the cluster can read or write to their attached disk based on the reservation that the clustered application chooses. VMs that use a SCSI disk controller coordinate access by using [SCSI Persistent Reservations](https://www.t10.org/members/w_spc3.htm) (SCSI PR). VMs that use an NVMe disk controller coordinate access by using NVMe reservations. Both protocols let a clustered application register each node, reserve disk access, and move the reservation to another node during failover.

Shared managed disks offer shared block storage that multiple VMs can access. A shared disk is exposed as a logical unit number (LUN) to VMs that use SCSI and as a namespace to VMs that use NVMe. In both cases, the disk appears as direct-attached storage (DAS) or a local drive to the VM. For more information about the controller interfaces, see [SCSI to NVMe conversion](/en-us/azure/virtual-machines/nvme-linux#scsi-vs-nvme).

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

### Operating system requirements

Shared disks support several operating systems. For supported operating systems, see the Windows or Linux sections.

## Billing implications

When you share a disk, your billing could be impacted in two different ways, depending on the type of disk.

For shared Premium SSDs, in addition to cost of the disk's tier, there's an extra charge that increases with each VM the SSD is mounted to. See [managed disks pricing](https://azure.microsoft.com/pricing/details/managed-disks/) for details.

Both shared Ultra Disks and shared Premium SSD v2 disks don't have an extra charge for each VM that they're mounted to. They're billed on the total IOPS and MB/s that the disk is configured for. Normally, Ultra Disks and Premium SSD v2 has two performance throttles that determine its total IOPS/MB/s. However, when configured as a shared disk, two more performance throttles are exposed, for a total of four. These two extra throttles allow for increased performance at an extra expense and each meter has a default value, which raises the performance and cost of the disk.

The four performance throttles a shared Ultra Disk and shared Premium SSD v2 have are `diskIOPSReadWrite`, `diskMBpsReadWrite`, `diskIOPSReadOnly`, and `diskMBpsReadOnly`. Each performance throttle can be configured to change the performance of your disk. The performance of shared Ultra Disks and Premium SSD v2 disks are calculated in the following ways: total provisioned IOPS (`diskIOPSReadWrite` + `diskIOPSReadOnly`) and total provisioned throughput in MB/s (`diskMBpsReadWrite` + `diskMBpsReadOnly`).

Once you've determined your total provisioned IOPS and total provisioned throughput, you can use them in the [pricing calculator](https://azure.microsoft.com/pricing/calculator/?service=managed-disks) to determine the cost of an Ultra shared disk or a Premium SSD v2 shared disk.

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

## Sample Windows shared disk workloads

Azure shared disks are supported on Windows Server 2008 and newer. Most Windows-based clustering builds on WSFC, which handles all core infrastructure for cluster node communication, allowing your applications to take advantage of parallel access patterns. WSFC enables both Cluster Shared Volumes (CSV) and non-CSV-based options depending on your version of Windows Server. For details, refer to [Create a failover cluster](/en-us/windows-server/failover-clustering/create-failover-cluster).

Some popular applications running on WSFC include:

- [Create an FCI with Azure shared disks (SQL Server on Azure VMs)](/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-azure-shared-disks-manually-configure)
    - [Migrate your failover cluster instance to SQL Server on Azure VMs with shared disks](/en-us/azure/azure-sql/migration-guides/virtual-machines/sql-server-failover-cluster-instance-to-sql-on-azure-vm)
- File servers. You can use the Scale-Out File Server features deployed on a Windows Server failover cluster, which uses shared disk in active-active mode. Cluster witness resources are stored on Azure shared disks and all file shares are simultaneously online on all nodes. For an example, see the Scale-out File Server (SoFS) [template](https://aka.ms/azure-shared-disk-sofs-template)
- SAP application servers use clustered shared disks to store SAP Central Services (ASCS for ABAP and SCS for Java) and SAP global host files. SAP ASCS/SCS [template](https://aka.ms/azure-shared-disk-sapacs-template)
- File Server for General Use (IW workload) - shared disks enable high availability for file servers in general
- Remote Desktop Server User Profile Disk (RDS UPD)

## Sample Linux shared disk workloads

Azure shared disks are supported on:

- [SUSE SLE HA 15 SP1 and above](https://www.suse.com/c/azure-shared-disks-excercise-w-sles-for-sap-or-sle-ha/)
- [Ubuntu 18.04 and above](https://discourse.ubuntu.com/t/ubuntu-high-availability-corosync-pacemaker-shared-disk-environments/14874)
- Red Hat Enterprise Linux (RHEL) ([support policy](https://access.redhat.com/articles/3444601))
    - [RHEL 7.9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/deploying_red_hat_enterprise_linux_7_on_public_cloud_platforms/configuring-rhel-high-availability-on-azure_cloud-content)
    - [RHEL 8.3 and above](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/deploying_rhel_8_on_microsoft_azure/configuring-rhel-high-availability-on-azure_cloud-content-azure)
- [Oracle Enterprise Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/availability/)

Linux clusters can use cluster managers such as [Pacemaker](https://wiki.clusterlabs.org/wiki/Pacemaker). Pacemaker builds on [Corosync](http://corosync.github.io/corosync/), enabling cluster communications for applications deployed in highly available environments. Some common clustered filesystems include [ocfs2](https://oss.oracle.com/projects/ocfs2/) and [gfs2](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/global_file_system_2/ch-overview-gfs2). You can use SCSI Persistent Reservation (SCSI PR) and STONITH Block Device (SBD) based clustering models for arbitrating access to the disk. When using SCSI PR, you can manipulate reservations and registrations by using utilities such as [fence_scsi](https://manpages.ubuntu.com/manpages/jammy/man8/fence_scsi.8.html) and [sg_persist](https://linux.die.net/man/8/sg_persist).

## Persistent reservation flow

The following diagrams illustrate common reservation patterns for clustered applications. The same flow applies whether the VMs use SCSI persistent reservations or NVMe reservations. The disk controller determines which protocol and commands the clustered application uses.

The following diagram illustrates a sample two-node clustered database application that uses reservations to enable failover from one node to the other.

![Diagram of a two-node Azure VM cluster sharing a data disk, showing registration, exclusive reservation, preemption, and database failover from VM1 to VM2.](media/virtual-machines-disks-shared-disks/shared-disk-updated-two-node-cluster-diagram.png)

The flow is as follows:

1. The clustered application running on both Azure VM1 and VM2 registers its intent to read or write to the disk.
2. The application instance on VM1 then takes exclusive reservation to write to the disk.
3. This reservation is enforced on your Azure disk and the database can now exclusively write to the disk. Any writes from the application instance on VM2 won't succeed.
4. If the application instance on VM1 goes down, the instance on VM2 can now initiate a database failover and take-over of the disk.
5. This reservation is now enforced on the Azure disk and the disk will no longer accept writes from VM1. It will only accept writes from VM2.
6. The clustered application can complete the database failover and serve requests from VM2.

The following diagram illustrates another common clustered workload consisting of multiple nodes reading data from the disk for running parallel processes, such as training of machine learning models.

![Diagram of four Azure VMs sharing a data disk, with all VMs registering and reading while VM1 reserves write access.](media/virtual-machines-disks-shared-disks/shared-disk-updated-machine-learning-trainer-model.png)

The flow is as follows:

1. The clustered application running on all VMs registers the intent to read or write to the disk.
2. The application instance on VM1 takes an exclusive reservation to write to the disk while opening up reads to the disk from other VMs.
3. This reservation is enforced on your Azure disk.
4. All nodes in the cluster can now read from the disk. Only one node writes back results to the disk, on behalf of all nodes in the cluster.

### SCSI persistent reservation flow

For VMs that use a SCSI disk controller, the clustered application performs the preceding flows by using SCSI PR register, reserve, preempt, and release operations against the shared disk LUN.

### NVMe persistent reservation flow

NVMe reservations provide the same access-coordination model for shared managed disks attached to VMs through an NVMe controller. NVMe uses namespaces instead of SCSI LUNs and uses the Reservation Register, Reservation Acquire, Reservation Release, and Reservation Report commands to manage registrations and reservations.

The following flow illustrates failover for a two-node clustered application:

1. The clustered application on VM1 and VM2 registers a unique reservation key for each VM by using the Reservation Register command.
2. The application on VM1 acquires the reservation with the required reservation type by using the Reservation Acquire command.
3. The shared disk enforces the reservation. Access from VM2 is limited by the selected reservation type.
4. If the application on VM1 goes down, the application on VM2 initiates failover. VM2 uses the Reservation Acquire command with the preempt action to replace VM1's reservation.
5. The shared disk enforces the new reservation and rejects conflicting access from VM1.
6. The clustered application completes failover and serves requests from VM2. When a reservation is no longer needed, the holder removes it by using the Reservation Release command.

### Ultra Disk and Premium SSD v2 reservation flow

Both Ultra Disks and Premium SSD v2 managed disks offer two extra throttles, giving each of them a total of four throttles. As a result, the reservation flow can use SCSI persistent reservations or NVMe reservations to coordinate disk access between clustered VMs, as described in Persistent reservation flow, or it can use the four throttles to distribute IOPS and throughput more granularly.

![Table showing read-only and read/write access for the reservation holder, registered nodes, and other nodes for each persistent reservation type.](media/virtual-machines-disks-shared-disks/ultra-reservation-table.png)

## Premium SSD performance throttles

With Premium SSD, the disk IOPS and throughput is fixed, for example, IOPS of a P30 is 5000. This value remains whether the disk is shared across 2 VMs or 5 VMs. The disk limits can be reached from a single VM or divided across two or more VMs.

## Ultra Disk and Premium SSD v2 performance throttles

Both Ultra Disks and Premium SSD v2 managed disks have the unique capability of allowing you to set your performance by exposing modifiable attributes and allowing you to modify them. By default, there are only two modifiable attributes but, shared Ultra Disks and shared Premium SSD v2 managed disks have two more attributes. Ultra Disks and Premium SSD v2 split these attributes across each attached VM. For some examples on how this distribution of capacity, IOPS, and throughput works, see the Examples section.

| Attribute | Description |
| --- | --- |
| `diskIOPSReadWrite` (Read/write disk IOPS) | The total number of IOPS allowed across all VMs mounting the shared disk with write access. |
| `diskMBpsReadWrite` (Read/write disk throughput) | The total throughput (MB/s) allowed across all VMs mounting the shared disk with write access. |
| `diskIOPSReadOnly`\* (Read-only disk IOPS) | The total number of IOPS allowed across all VMs mounting the shared disk as `ReadOnly`. |
| `diskMBpsReadOnly`\* (Read-only disk throughput) | The total throughput (MB/s) allowed across all VMs mounting the shared disk as `ReadOnly`. |

\* Applies to shared Ultra Disks and shared Premium SSD v2 managed disks only

The following formulas explain how the performance attributes can be set, since they're user modifiable:

- `diskIOPSReadWrite`(Read/write disk IOPS):
    - Has a baseline minimum IOPS of 100, for disks 100 GiB and smaller.
        - For disks larger than 100 GiB, the baseline minimum IOPS you can set increases by 1 per GiB. So the lowest you can set `diskIOPSReadWrite` for a 101 GiB disk is 101 IOPS.
    - The maximum you can set this attribute is determined by the size of your disk, the formula is 300 \* GiB, up to a maximum of 400,000.
- `diskMBpsReadWrite`(Read/write disk throughput)
    - The minimum throughput (MB/s) of this attribute is determined by your IOPS, the formula is 4 KiB per second per IOPS. So if you had 101 IOPS, the minimum MB/s you can set is 1.
    - The maximum you can set this attribute is determined by the amount of IOPS you set, the formula is 256 KiB per second per IOPS, up to a maximum of 10,000 MB/s.
- `diskIOPSReadOnly`(Read-only disk IOPS)
    - The minimum baseline IOPS for this attribute is 100. For `diskIOPSReadOnly`, the baseline doesn't increase with disk size.
    - The maximum you can set this attribute is determined by the size of your disk, the formula is 300 \* GiB, up to a maximum of 400,000.
- `diskMBpsReadOnly`(Read-only disk throughput)
    - The minimum throughput (MB/s) for this attribute is 1. For `diskMBpsReadOnly`, the baseline doesn't increase with IOPS.
    - The maximum you can set this attribute is determined by the amount of IOPS you set, the formula is 256 KiB per second per IOPS, up to a maximum of 10,000 MB/s.

### Examples

The following examples depict a few scenarios that show how the throttling can work with shared Ultra Disks, specifically.

#### Two-node cluster using Cluster Shared Volumes

The following is an example of a 2-node WSFC using clustered shared volumes. With this configuration, both VMs have simultaneous write-access to the disk, which results in the `ReadWrite` throttle being split across the two VMs and the `ReadOnly` throttle not being used.

![Diagram of a two-node Windows cluster using Cluster Shared Volumes, with read/write IOPS and throughput split equally between both VMs.](media/virtual-machines-disks-shared-disks/ultra-two-node-example.png)

#### Two-node cluster without Cluster Shared Volumes

The following is an example of a 2-node WSFC that isn't using Cluster Shared Volumes. With this configuration, only one VM has write-access to the disk. This results in the `ReadWrite` throttle being used exclusively for the primary VM and the `ReadOnly` throttle only being used by the secondary.

![Diagram of a two-node Windows failover cluster without Cluster Shared Volumes, with VM1 using the read/write throttles and VM2 using the read-only throttles.](media/virtual-machines-disks-shared-disks/ultra-two-node-no-csv.png)

#### Four node Linux cluster

The following is an example of a 4-node Linux cluster with a single writer and three scale-out readers. With this configuration, only one VM has write-access to the disk. This results in the `ReadWrite` throttle being used exclusively for the primary VM and the `ReadOnly` throttle being split by the secondary VMs.

![Diagram of a four-node Linux cluster, with VM1 using the read/write throttles and the read-only throttles split across VM2, VM3, and VM4.](media/virtual-machines-disks-shared-disks/ultra-four-node-example.png)

#### Shared Ultra Disk and Premium SSD v2 pricing

Both shared Ultra Disks and shared Premium SSD v2 managed disks are priced based on provisioned capacity, total provisioned IOPS (`diskIOPSReadWrite` + `diskIOPSReadOnly`) and total provisioned throughput in MB/s (`diskMBpsReadWrite` + `diskMBpsReadOnly`). There's no extra charge for each additional VM mount. For example, a shared Ultra Disk with the following configuration (`diskSizeGB`: 1024, `diskIOPSReadWrite`: 10000, `diskMBpsReadWrite`: 600, `diskIOPSReadOnly`: 100, `diskMBpsReadOnly`: 1) is charged with 1024 GiB, 10100 IOPS, and 601 MB/s regardless of whether it's mounted to two VMs or five VMs.