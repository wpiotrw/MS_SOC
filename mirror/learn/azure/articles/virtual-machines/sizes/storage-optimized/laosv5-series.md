---
layout: Conceptual
title: Laosv5 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/storage-optimized/laosv5-series
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
description: Information on and specifications of the Laosv5-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-08-18T00:00:00.0000000Z
locale: en-us
document_id: 5549f90a-2bc0-832c-9482-71a116cbd06b
document_version_independent_id: e22a7e57-192c-66f3-e4ec-b09376800cad
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/storage-optimized/laosv5-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/storage-optimized/laosv5-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/storage-optimized/laosv5-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/0811fd70-54cc-4b30-9df4-d821a6be00ca
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/e026b98e-678e-4406-bc80-b3daea608acc
platformId: 3a2802a4-f2e6-85de-c734-b43068b8398b
---

# Laosv5 size series - Azure Virtual Machines | Microsoft Learn

The Laosv5-series of Azure Virtual Machines (VMs) features high-throughput, low latency, directly mapped local NVMe storage. These VMs utilize AMD's fifth Generation EPYC™ 9005 processors that can achieve a boosted maximum frequency of 4.5 GHz. The Laosv5-series VMs are available in sizes from 2 to 160 vCPUs, with 8 GiB of memory allocated per vCPU and 720 GB of local NVMe temp disk capacity allocated per vCPU, with up to 138 TB (9x15.36 TB) of local temp disk capacity available on the largest size.

These VMs are perfect for distributed, scale-out workloads that require high amounts of local storage capacity per vCPU and the ability to move that data quickly over the network or to an Azure remote storage backend. Workloads like storage caching layers, Elasticsearch, distributed file systems, big data analytics, relational and NoSQL databases, and data warehouses all benefit from the dense storage capabilities of Laosv5 VMs.

Laosv5-series VMs support Standard SSD, Standard HDD, and Premium SSD remote disk types. You can also attach Ultra Disk storage based on its regional availability. Remote Disk storage is billed separately from virtual machines. For more information, see pricing for disks.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 160 vCPUs | AMD EPYC 9005 (Turin) [x86-64] |
| Memory | 16 - 1,040 GiB |  |
| Local Storage | 1 - 9 Disks | 1,440 - 15,360 GB 215,625 - 20,700,000 IOPS 1,220 - 117,000 MBps |
| Remote Storage | 10 - 64 Disks | 4,400 - 400,000 IOPS 150 - 12,000 MBps Disk Types: [Standard SDD/HDD](../../disks-types#standard-ssds), [Premium SSD](../../disks-types#premium-ssds), [Premium SSD v2](../../disks-types#premium-ssd-v2) |
| Network | 3 - 15 NICs | 25,000 - 200,000 Mbps Interfaces: NetVSC, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs and memory for each size.

| Size Name | vCPUs | Memory (GiB) |
| --- | --- | --- |
| Standard\_L2aos\_v5 | 2 | 16 |
| Standard\_L4aos\_v5 | 4 | 32 |
| Standard\_L8aos\_v5 | 8 | 64 |
| Standard\_L12aos\_v5 | 12 | 96 |
| Standard\_L16aos\_v5 | 16 | 128 |
| Standard\_L24aos\_v5 | 24 | 192 |
| Standard\_L32aos\_v5 | 32 | 256 |
| Standard\_L48aos\_v5 | 48 | 384 |
| Standard\_L64aos\_v5 | 64 | 512 |
| Standard\_L96aos\_v5 | 96 | 768 |
| Standard\_L128aos\_v5 | 128 | 1,024 |
| Standard\_L160iaos\_v5 | 160 | 1,040 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage information for each size.

| Size Name | Temp Storage Disks | Temp Disk Size (GB) | Temp Disk Random Read IOPS | Temp Disk Sequential Read Throughput (MBps) | Temp Disk Random Write IOPS | Temp Disk Sequential Write Throughput (MBps) |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_L2aos\_v5 | 1 | 1,440 | 215,625 | 1,220 | 107,813 | 565 |
| Standard\_L4aos\_v5 | 1 | 2,880 | 431,250 | 2,440 | 215,625 | 1,125 |
| Standard\_L8aos\_v5 | 1 | 5,760 | 862,500 | 4,875 | 431,250 | 2,250 |
| Standard\_L12aos\_v5 | 1 | 8,640 | 1,293,750 | 7,315 | 646,875 | 3,375 |
| Standard\_L16aos\_v5 | 1 | 11,520 | 1,725,000 | 9,750 | 862,500 | 4,500 |
| Standard\_L24aos\_v5 | 2 | 8,640 | 2,587,500 | 14,625 | 1,293,750 | 6,750 |
| Standard\_L32aos\_v5 | 2 | 11,520 | 3,450,000 | 19,500 | 1,725,000 | 9,000 |
| Standard\_L48aos\_v5 | 3 | 11,520 | 5,175,000 | 29,250 | 2,587,500 | 13,500 |
| Standard\_L64aos\_v5 | 3 | 15,360 | 6,900,000 | 39,000 | 3,450,000 | 18,000 |
| Standard\_L96aos\_v5 | 9 | 11,520 | 10,350,000 | 58,500 | 5,175,000 | 27,000 |
| Standard\_L128aos\_v5 | 6 | 15,360 | 13,800,000 | 78,000 | 6,900,000 | 36,000 |
| Standard\_L160iaos\_v5 | 9 | 15,360 | 20,700,000 | 117,000 | 10,350,000 | 54,000 |

#### Storage resources

- [NVMe Overview](/en-us/azure/virtual-machines/nvme-overview)
- [FAQ for temp NVMe disks](/en-us/azure/virtual-machines/enable-nvme-temp-faqs)

#### Table definitions

- Temp disk performance depends on many factors, including block size, workload patterns of read and write operations, queue depth (QD), and others. View temp disk performance specifications as best-case performance numbers, assuming 4 KB block sizes and QD=256 for IOPS, and 256 KB block sizes with QD=64 for throughput. Write performance is heavily impacted by how many blocks are in use on a device. Temp disk write performance specifications assume a device has a clean slate to enable the best performance. During steady-state operations, write performance is lower than the published specifications.
- For Laosv5 and Laosv4, temp disk refers to the NVMe local data disks used by the VM. While Lsv3 and Lasv3 have NVMe local data disks and a SCSI local temp disk, Laosv5 and Laosv4 only have NVMe local temp disks. There's no SCSI local temp disk on Laosv5.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps, where MBps = 10^6 bytes/sec.
- To learn how to get the best local storage performance for your VMs, see the [NVMe Temp Disk FAQ](/en-us/azure/virtual-machines/enable-nvme-temp-faqs).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage information for each size.

| Size Name | Max Remote Storage Disks | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MBps) | Uncached Premium SSD Burst IOPS | Uncached Premium SSD Burst Throughput (MBps) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MBps) | Uncached Burst Ultra Disk and Premium SSD v2 IOPS | Uncached Burst Ultra Disk and Premium SSD v2 Throughput (MBps) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_L2aos\_v5 | 4 | 4,400 | 150 | 44,000 | 1,413 | 5,000 | 170 | 50,000 | 1,600 |
| Standard\_L4aos\_v5 | 8 | 8,800 | 300 | 47,200 | 1,413 | 10,000 | 340 | 53,636 | 1,600 |
| Standard\_L8aos\_v5 | 16 | 17,600 | 600 | 47,200 | 1,413 | 20,000 | 680 | 53,636 | 1,600 |
| Standard\_L12aos\_v5 | 32 | 26,400 | 900 | 47,200 | 1,413 | 30,000 | 1,020 | 53,636 | 1,600 |
| Standard\_L16aos\_v5 | 32 | 35,200 | 1,200 | 72,700 | 1,413 | 40,000 | 1,360 | 82,613 | 1,600 |
| Standard\_L24aos\_v5 | 32 | 52,800 | 1,800 | 72,700 | 1,916 | 60,000 | 2,040 | 82,613 | 2,170 |
| Standard\_L32aos\_v5 | 32 | 70,400 | 2,400 | 94,400 | 2,875 | 80,000 | 2,720 | 107,272 | 3,258 |
| Standard\_L48aos\_v5 | 32 | 105,600 | 3,600 | 132,000 | 5,749 | 120,000 | 4,080 | 150,000 | 6,515 |
| Standard\_L64aos\_v5 | 32 | 140,800 | 4,800 | 192,500 | 5,749 | 160,000 | 5,440 | 218,750 | 6,515 |
| Standard\_L96aos\_v5 | 32 | 211,200 | 7,200 | 220,000 | 7,664 | 240,000 | 8,160 | 250,000 | 8,685 |
| Standard\_L128aos\_v5 | 64 | 260,000 | 9,600 | 260,000 | 10,588 | 320,000 | 10,880 | 320,000 | 12,000 |
| Standard\_L160iaos\_v5 | 64 | 260,000 | 12,000 | 260,000 | 12,000 | 400,000 | 12,000 | 400,000 | 12,000 |

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
| Standard\_L2aos\_v5 | 2 | 25,000 |
| Standard\_L4aos\_v5 | 2 | 25,000 |
| Standard\_L8aos\_v5 | 4 | 25,000 |
| Standard\_L12aos\_v5 | 6 | 25,000 |
| Standard\_L16aos\_v5 | 8 | 25,000 |
| Standard\_L24aos\_v5 | 8 | 37,500 |
| Standard\_L32aos\_v5 | 8 | 50,000 |
| Standard\_L48aos\_v5 | 8 | 75,000 |
| Standard\_L64aos\_v5 | 8 | 100,000 |
| Standard\_L96aos\_v5 | 8 | 150,000 |
| Standard\_L128aos\_v5 | 8 | 150,000 |
| Standard\_L160iaos\_v5 | 8 | 200,000 |

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