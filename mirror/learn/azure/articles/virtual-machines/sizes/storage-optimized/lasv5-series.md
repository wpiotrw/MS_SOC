---
layout: Conceptual
title: Lasv5 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/storage-optimized/lasv5-series
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
author: zhousarah
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: 
ms.author: zhousarah
ms.update-cycle: 1095-days
description: Information on and specifications of the Lasv5-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-08-18T00:00:00.0000000Z
locale: en-us
document_id: b75cf19f-757a-53d6-bd49-2bb9a0da21b8
document_version_independent_id: 9d09f957-7c69-31d1-9b12-369015d40d1c
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/storage-optimized/lasv5-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/storage-optimized/lasv5-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/storage-optimized/lasv5-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/0811fd70-54cc-4b30-9df4-d821a6be00ca
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/e026b98e-678e-4406-bc80-b3daea608acc
platformId: 78dffc21-58ad-50a8-1a4d-b74cc6da9dff
---

# Lasv5 size series - Azure Virtual Machines | Microsoft Learn

The Lasv5-series of Azure Virtual Machines (VMs) features high-throughput, low latency, directly mapped local NVMe storage. These VMs utilize AMD's fifth Generation EPYC™ 9005 processors that can achieve a boosted maximum frequency of 4.5 GHz. The Lasv5-series VMs are available in sizes from 2 to 160 vCPUs, with 8 GiB of memory allocated per vCPU and 240 GB of local NVMe temp disk capacity allocated per vCPU, with up to 30.7 TB (8x3.84 TB) of local temp disk capacity available on the largest size.

Lasv5-series VMs are well suited for scale-up or scale-out storage workloads that need a balance of SSD capacity, compute, and memory. These VMs are perfect for big data, relational, NoSQL databases, data analytics, and data warehousing workloads. Examples include Cassandra, MongoDB, Cloudera, Spark, Elastic Search, Redis, and other data-intensive applications.

Lasv5-series VMs support Standard SSD, Standard HDD, and Premium SSD remote disk types. You can also attach Ultra Disk storage based on its regional availability. Remote Disk storage is billed separately from virtual machines. For more information, see pricing for disks.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, and other details^ |
| --- | --- | --- |
| Processor | 2 - 160 vCPUs | AMD EPYC 9005 (Turin) [x86-64] |
| Memory | 16 - 1,280 GiB |  |
| Local Storage | 1 - 8 Disks | 480 - 3,840 GB 150,000 - 9,600,000 IOPS 750 - 48,000 MBps |
| Remote Storage | 10 - 64 Disks | 4,000 - 400,000 IOPS 118 - 12,000 MBps Disk Types: [Standard SDD/HDD](../../disks-types#standard-ssds), [Premium SSD](../../disks-types#premium-ssds), [Premium SSD v2](../../disks-types#premium-ssd-v2) |
| Network | 2 - 15 NICs | 16,000 - 200,000 Mbps Interfaces: NetVSC, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs and memory for each size.

| Size Name | vCPUs | Memory (GiB) |
| --- | --- | --- |
| Standard\_L2as\_v5 | 2 | 16 |
| Standard\_L4as\_v5 | 4 | 32 |
| Standard\_L8as\_v5 | 8 | 64 |
| Standard\_L16as\_v5 | 16 | 128 |
| Standard\_L32as\_v5 | 32 | 256 |
| Standard\_L48as\_v5 | 48 | 384 |
| Standard\_L64as\_v5 | 64 | 512 |
| Standard\_L80as\_v5 | 80 | 640 |
| Standard\_L96as\_v5 | 96 | 768 |
| Standard\_L128as\_v5 | 128 | 1,024 |
| Standard\_L160ias\_v5 | 160 | 1,280 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage information for each size.

| Size Name | Temp Storage Disks | Temp Disk Size (GB) | Temp Disk Random Read IOPS | Temp Disk Sequential Read Throughput (MBps) | Temp Disk Random Write IOPS | Temp Disk Sequential Write Throughput (MBps) |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_L2as\_v5 | 1 | 480 | 150,000 | 750 | 75,000 | 375 |
| Standard\_L4as\_v5 | 1 | 960 | 300,000 | 1,500 | 150,000 | 750 |
| Standard\_L8as\_v5 | 1 | 1,920 | 600,000 | 3,000 | 300,000 | 1,500 |
| Standard\_L16as\_v5 | 1 | 3,840 | 1,200,000 | 6,000 | 600,000 | 3,000 |
| Standard\_L32as\_v5 | 2 | 3,840 | 2,400,000 | 12,000 | 1,200,000 | 6,000 |
| Standard\_L48as\_v5 | 3 | 3,840 | 3,600,000 | 18,000 | 1,800,000 | 9,000 |
| Standard\_L64as\_v5 | 4 | 3,840 | 4,800,000 | 24,000 | 2,400,000 | 12,000 |
| Standard\_L80as\_v5 | 5 | 3,840 | 6,000,000 | 30,000 | 3,000,000 | 15,000 |
| Standard\_L96as\_v5 | 6 | 3,840 | 7,200,000 | 36,000 | 3,600,000 | 18,000 |
| Standard\_L128as\_v5 | 8 | 3,840 | 9,600,000 | 48,000 | 4,800,000 | 24,000 |
| Standard\_L160ias\_v5 | 8 | 3,840 | 9,600,000 | 48,000 | 4,800,000 | 24,000 |

#### Storage resources

- [NVMe Overview](/en-us/azure/virtual-machines/nvme-overview)
- [FAQ for temp NVMe disks](/en-us/azure/virtual-machines/enable-nvme-temp-faqs)

#### Table definitions

- Temp disk performance depends on many factors, including block size, workload patterns of read and write operations, queue depth (QD), and others. View temp disk performance specifications as best-case performance numbers, assuming 4 KB block sizes and QD=256 for IOPS, and 256 KB block sizes with QD=64 for throughput. Write performance is heavily impacted by how many blocks are in use on a device. Temp disk write performance specifications assume a device has a clean slate to enable the best performance. During steady-state operations, write performance is lower than the published specifications.
- For Lasv5 and Lasv4, temp disk refers to the NVMe local data disks used by the VM. While Lsv3 and Lasv3 have NVMe local data disks and a SCSI local temp disk, Lasv5 and Lasv4 only have NVMe local temp disks. There's no SCSI local temp disk on Lasv5.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps, where MBps = 10^6 bytes/sec.
- To learn how to get the best local storage performance for your VMs, see the [NVMe Temp Disk FAQ](/en-us/azure/virtual-machines/enable-nvme-temp-faqs).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage information for each size. | Size Name | Max Remote Storage Disks | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MBps) | Uncached Premium SSD Burst IOPS | Uncached Premium SSD Burst Throughput (MBps) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MBps) | Uncached Burst Ultra Disk and Premium SSD v2 IOPS | Uncached Burst Ultra Disk and Premium SSD v2 Throughput (MBps) | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Standard\_L2as\_v5 | 4 | 4,000 | 118 | 44,000 | 1,413 | 4,400 | 137 | 48,400 | 1,653 | | Standard\_L4as\_v5 | 8 | 8,000 | 234 | 47,200 | 1,413 | 8,800 | 274 | 52,083 | 1,653 | | Standard\_L8as\_v5 | 16 | 16,000 | 468 | 47,200 | 1,413 | 17,600 | 548 | 52,083 | 1,653 | | Standard\_L16as\_v5 | 32 | 32,000 | 936 | 72,700 | 1,413 | 35,200 | 1,096 | 80,000 | 1,653 | | Standard\_L32as\_v5 | 32 | 64,000 | 1,872 | 94,400 | 1,916 | 70,400 | 2,191 | 104,167 | 2,242 | | Standard\_L48as\_v5 | 32 | 96,000 | 2,808 | 99,000 | 2,875 | 105,600 | 3,291 | 108,900 | 3,363 | | Standard\_L64as\_v5 | 32 | 128,000 | 3,744 | 132,000 | 3,833 | 140,800 | 4,382 | 145,200 | 4,485 | | Standard\_L80as\_v5 | 32 | 160,000 | 4,704 | 162,500 | 4,791 | 176,000 | 5,478 | 178,475 | 5,577 | | Standard\_L96as\_v5 | 32 | 192,000 | 5,664 | 192,500 | 5,749 | 211,200 | 6,574 | 211,750 | 6,669 | | Standard\_L128as\_v5 | 32 | 204,800 | 7,488 | 225,280 | 7,664 | 281,600 | 8,765 | 310,886 | 8,967 | | Standard\_L160ias\_v5 | 32 | 260,000 | 12,000 | 260,000 | 12,000 | 400,000 | 12,000 | 400,000 | 12,000 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- Some sizes support [bursting](../../disk-bursting) to temporarily increase disk performance. Burst speeds can be maintained for up to 30 minutes at a time.
- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3), remember that capacity numbers given in GiB might appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps, where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly or ReadWrite. For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Network](#tab/sizenetwork)
Network interface information for each size.

| Size Name | Max NICs | Max Network Bandwidth (Mbps) |
| --- | --- | --- |
| Standard\_L2as\_v5 | 2 | 16,000 |
| Standard\_L4as\_v5 | 2 | 16,000 |
| Standard\_L8as\_v5 | 4 | 25,000 |
| Standard\_L16as\_v5 | 8 | 25,000 |
| Standard\_L32as\_v5 | 8 | 25,000 |
| Standard\_L48as\_v5 | 8 | 35,000 |
| Standard\_L64as\_v5 | 8 | 45,000 |
| Standard\_L80as\_v5 | 8 | 57,500 |
| Standard\_L96as\_v5 | 8 | 70,000 |
| Standard\_L128as\_v5 | 15 | 75,000 |
| Standard\_L160ias\_v5 | 15 | 200,000 |

#### Networking resources

- [Virtual networks and virtual machines in Azure](/en-us/azure/virtual-network/network-overview)
- [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)

#### Table definitions

- Expected network bandwidth is the maximum aggregated bandwidth allocated per VM type across all NICs, for all destinations. For more information, see [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput).
- Upper limits aren't guaranteed. Limits offer guidance for selecting the right VM type for the intended application. Actual network performance depends on several factors including network congestion, application loads, and network settings. For information on optimizing network throughput, see [Optimize network throughput for Azure virtual machines](/en-us/azure/virtual-network/virtual-network-optimize-network-bandwidth).
- To achieve the expected network performance on Linux or Windows, you might need to select a specific version or optimize your VM. For more information, see [Bandwidth/Throughput testing (NTTTCP)](/en-us/azure/virtual-network/virtual-network-bandwidth-testing).

# [Accelerators](#tab/sizeaccelerators)
Accelerator (GPUs, FPGAs, and other accelerators) information for each size.

Note

This series doesn't include any accelerators.

---

## Feature support

| Feature name | Support status |
| --- | --- |
| [Premium Storage](../../premium-storage-performance) | Supported |
| [Premium Storage caching](../../premium-storage-performance) | Supported |
| [Live Migration](../../maintenance-and-updates) | Not Supported |
| [Memory Preserving Updates](../../maintenance-and-updates) | Supported |
| [Generation 2 VMs](../../generation-2) | Supported |
| [Generation 1 VMs](../../generation-2) | Not Supported |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Supported |
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Supported |

Note

This VM series works only on OS images that support NVMe. If your current OS image doesn't support NVMe, you see an error message. [NVMe](/en-us/azure/virtual-machines/enable-nvme-interface) support is available on the most popular OS images, and Microsoft is continuously improving OS image compatibility.

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)