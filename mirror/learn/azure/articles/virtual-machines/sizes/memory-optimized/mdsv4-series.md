---
layout: Conceptual
title: Mdsv4 Medium Memory size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/mdsv4-series
breadcrumb_path: ../../../breadcrumb/azure-compute/toc.json
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
author: chiefabel7
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: abelw
ms.update-cycle: 1095-days
description: Information on and specifications of the Mdsv4-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-09-03T00:00:00.0000000Z
locale: en-us
document_id: 3fc4c615-65e0-4f4d-0072-88e45065686b
document_version_independent_id: 6fa51bdd-b024-6545-9a49-a84489a61775
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/mdsv4-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/mdsv4-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/mdsv4-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/0811fd70-54cc-4b30-9df4-d821a6be00ca
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/e026b98e-678e-4406-bc80-b3daea608acc
platformId: 67a05e58-f665-b81d-a2b4-6406368bee4b
---

# Mdsv4 Medium Memory size series - Azure Virtual Machines | Microsoft Learn

The Memory and storage optimized Mdsv4 Medium Memory VM series are based on the 6th generation Intel® Xeon® Scalable processors and deliver higher remote disk storage performance. These new VM sizes offer up to 4 TB of RAM and up to 225,000 IOPS and 5.5 GBps throughput to remote disk storage with NVMe interface by using Ultra Disk and Premium SSD v2, and provides 50% networking performance improvements over previous generations.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 16 - 256 vCPUs | Intel Xeon 6th gen Scalable (Granite Rapids) [x86-64] |
| Memory | 256 - 3892 GiB |  |
| Local Storage | 1 - 2 | 550 - 4400 GiB 125,000 - 2,000,000 IOPS700 - 11,200 MBps |
| Remote Storage | 64 Disks | 20,000 - 225,000 IOPS 400 - 5,500 MBps |
| Network | 8 NICs | 4,500 - 50,000 Mbps Interfaces: NetVSC, MANA |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series (NVMe)

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_M16lds\_v4 | 16 | 256 |
| Standard\_M32lds\_v4 | 32 | 512 |
| Standard\_M48lds\_v4 | 48 | 768 |
| Standard\_M64lds\_v4 | 64 | 1024 |
| Standard\_M96lds\_v4 | 96 | 1536 |
| Standard\_M128lds\_v4 | 128 | 1944 |
| Standard\_M192lds\_v4 | 192 | 3072 |
| Standard\_M256lds\_v4 | 256 | 3892 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage information for each size:

| Size Name | Max Temp Storage Disks (Qty.) | Temp Disk Size (GiB) | Max Temp Disk Random Read (RR)^1^IOPS | Max Temp Disk Sequential Read Throughput (MBps) | Temp Disk Random Write IOPS | Temp Disk Sequential Write Throughput (MBps) |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_M16lds\_v4 | 1 | 550 | 125,000 | 700 | 62,500 | 350 |
| Standard\_M32lds\_v4 | 1 | 1100 | 250,000 | 1,400 | 125,000 | 700 |
| Standard\_M48lds\_v4 | 1 | 1650 | 375,000 | 2,100 | 187,500 | 1,050 |
| Standard\_M64lds\_v4 | 2 | 1100 | 500,000 | 2,800 | 250,000 | 1,400 |
| Standard\_M96lds\_v4 | 2 | 1650 | 750,000 | 4,200 | 375,000 | 2,100 |
| Standard\_M128lds\_v4 | 2 | 2200 | 1,000,000 | 5,600 | 500,000 | 2,800 |
| Standard\_M192lds\_v4 | 2 | 3300 | 1,500,000 | 8,400 | 750,000 | 4,200 |
| Standard\_M256lds\_v4 | 2 | 4400 | 2,000,000 | 11,200 | 1,000,000 | 5,600 |

#### Table definitions

- Total local temporary storage is calculated by multiplying the max number of storage disks by the temp disk size. For example, for the Standard\_M256lds\_v4, the total local temporary storage capacity is 2 x 6000 GiB = 12000 GiB.
- Temp disk performance depends on many factors including block size, workload patterns of read/writes, queue depth (QD), and others. Temp disk performance specifications represent best case performance numbers, assuming 4k block sizes and QD=256 for IOPS, and 256k block sizes with QD=64 for throughput. Read performance specs assume 100% reads, and write performance specs assume 100% writes. Write performance is heavily impacted by how many blocks are in use on a device. Temp disk write performance specs assume a device has a clean slate to enable the best performance. During steady state operations, write performance is expected to be lower than the published specs.
- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3), remember that capacity numbers given in GiB might appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](/en-us/azure/virtual-machines/disks-performance).
- NVMe temp disks are presented as raw NVMe devices that you need to initialize and format before use. For more details on how to format and initialize drives, refer to the [NVMe Temp Disk FAQ](/en-us/azure/virtual-machines/enable-nvme-temp-faqs).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage information for each size:

| Size Name | Max Remote Storage Disks (Qty.) | Max Uncached Premium SSD IOPS | Max Uncached Ultra Disk and Premium SSD v2 IOPS | Max Uncached Premium SSD Throughput (MB/s) | Max Uncached Ultra Disk and Premium SSD v2 Throughput (MB/s) |
| --- | --- | --- | --- | --- | --- |
| Standard\_M16lds\_v4 | 64 | 20,000 | 20,000 | 400 | 400 |
| Standard\_M32lds\_v4 | 64 | 40,000 | 40,000 | 800 | 800 |
| Standard\_M48lds\_v4 | 64 | 65,000 | 65,000 | 1,600 | 1,600 |
| Standard\_M64lds\_v4 | 64 | 80,000 | 80,000 | 1,600 | 1,600 |
| Standard\_M96lds\_v4 | 64 | 120,000 | 120,000 | 3,200 | 3,200 |
| Standard\_M128lds\_v4 | 64 | 160,000 | 160,000 | 4,000 | 4,000 |
| Standard\_M192lds\_v4 | 64 | 200,000 | 200,000 | 4,750 | 4,750 |
| Standard\_M256lds\_v4 | 64 | 225,000 | 225,000 | 5,500 | 5,500 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3), remember that capacity numbers given in GiB might appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- IOPS and MBps listed here refer to uncached mode for data disks.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](/en-us/azure/virtual-machines/disks-performance).
- The IOPS specification uses common small random block sizes like 4 KiB or 8 KiB. Maximum IOPS is defined as "up-to" and measured by using 4 KiB random reads workloads.
- The TPUT specification uses common large sequential block sizes like 128 KiB or 1024 KiB. Maximum TPUT is defined as "up-to" and measured by using 128 KiB sequential reads workloads.

# [Network](#tab/sizenetwork)
Network interface information for each size:

| Size Name | Max NICs (Qty.) | Max Network Bandwidth (Mb/s) |
| --- | --- | --- |
| Standard\_M16lds\_v4 | 8 | 4,500 |
| Standard\_M32lds\_v4 | 8 | 8,000 |
| Standard\_M48lds\_v4 | 8 | 16,000 |
| Standard\_M64lds\_v4 | 8 | 16,000 |
| Standard\_M96lds\_v4 | 8 | 30,000 |
| Standard\_M128lds\_v4 | 8 | 30,000 |
| Standard\_M192lds\_v4 | 8 | 50,000 |
| Standard\_M256lds\_v4 | 8 | 50,000 |

#### Networking resources

- [Virtual networks and virtual machines in Azure](/en-us/azure/virtual-network/network-overview)
- [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)

#### Table definitions

- Expected network bandwidth is the maximum aggregated bandwidth allocated per VM type across all NICs, for all destinations. For more information, see [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput).
- Upper limits aren't guaranteed. Limits offer guidance for selecting the right VM type for the intended application. Actual network performance depends on several factors including network congestion, application loads, and network settings. For information on optimizing network throughput, see [Optimize network throughput for Azure virtual machines](/en-us/azure/virtual-network/virtual-network-optimize-network-bandwidth).
- To achieve the expected network performance on Linux or Windows, you might need to select a specific version or optimize your VM. For more information, see [Bandwidth/Throughput testing (NTTTCP)](/en-us/azure/virtual-network/virtual-network-bandwidth-testing).

# [Accelerators](#tab/sizeaccelerators)
Accelerator (GPUs, FPGAs, etc.) info for each size

Note

This series doesn't include any accelerators.

---

## Feature support

| Feature name | Support status |
| --- | --- |
| [Premium Storage](../../premium-storage-performance) | Supported |
| [Premium Storage caching](../../premium-storage-performance) | Supported |
| [Live Migration](../../maintenance-and-updates) | Limited Support |
| [Memory Preserving Updates](../../maintenance-and-updates) | Not Supported |
| [Generation 2 VMs](../../generation-2) | Supported |
| [Generation 1 VMs](../../generation-2) | Not Supported |
| [Accelerated Networking](/en-us/azure/virtual-network/create-virtual-machine-accelerated-networking) | Supported |
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Not Supported |
| [Hibernation](../../hibernate-resume) | Not Supported |
| [Write Accelerator](/en-us/azure/virtual-machines/how-to-enable-write-accelerator) | Not Supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)