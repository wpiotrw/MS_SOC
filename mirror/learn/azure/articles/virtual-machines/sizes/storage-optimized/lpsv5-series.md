---
layout: Conceptual
title: Lpsv5 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/storage-optimized/lpsv5-series
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
author: noahwood28
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: noahwood
ms.update-cycle: 1095-days
description: Information on and specifications of the Lpsv5-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-11-07T00:00:00.0000000Z
ai-usage: ai-generated
locale: en-us
document_id: d74acdae-dddd-ea15-9c72-f36fcb2afca1
document_version_independent_id: 598014b3-dab0-5249-4392-e43ee6b0a1a7
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/storage-optimized/lpsv5-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/storage-optimized/lpsv5-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/storage-optimized/lpsv5-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 325d37f4-3fe3-7b56-69cb-0e42fff284ab
---

# Lpsv5 size series - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows Client VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

The Lpsv5-series virtual machines feature high-throughput, low-latency local NVMe storage. These VMs are powered by Azure's second-generation Cobalt 200 processor, which is based on the Arm Neoverse V3 architecture and provides an entire physical core for each virtual machine vCPU. Cobalt 200 supports the [Processor Mode](../../vm-processor-mode) feature, running at up to 3.6 GHz in Opportunistic mode and at 3.2 GHz in Deterministic mode. The Lpsv5-series VMs are available in sizes from 1 to 128 vCPUs, with 8 GiB of memory per vCPU and up to 23,040 GB (6 x 3,840 GB) of local NVMe temporary storage.

Lpsv5-series VMs are well suited for scale-up or scale-out storage workloads that need a balance of SSD capacity, compute, and memory. These workloads include data preprocessing and staging, relational and NoSQL databases with local storage requirements, big data analytics, and search and indexing engines.

Lpsv5-series virtual machines support Standard SSD, Standard HDD, and Premium SSD remote disk types. You can also attach Premium SSD v2 and Ultra Disk storage. Remote disk storage is billed separately from virtual machines. For more information, see [pricing for disks](https://azure.microsoft.com/pricing/details/managed-disks/).

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 1 - 128 vCPUs | Azure Cobalt 200 [Arm64] |
| Memory | 8 - 1,024 GiB |  |
| Local Storage | 1 - 6 Disks | 240 - 3,840 GB 75,000 - 7,200,000 IOPS 380 - 36,000 MBps |
| Remote Storage | 4 - 64 Disks | 2,000 - 320,000 IOPS 60 - 8,770 MBps Disk Types: [Standard SSD/HDD](../../disks-types#standard-ssds), [Premium SSD](../../disks-types#premium-ssds), [Premium SSD v2](../../disks-types#premium-ssd-v2), [Ultra Disk](../../disks-types#ultra-disks) |
| Network | 2 - 15 NICs | 12,500 - 85,000 Mbps Interfaces: NetVSC, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_L1ps\_v5 | 1 | 8 |
| Standard\_L2ps\_v5 | 2 | 16 |
| Standard\_L4ps\_v5 | 4 | 32 |
| Standard\_L8ps\_v5 | 8 | 64 |
| Standard\_L16ps\_v5 | 16 | 128 |
| Standard\_L32ps\_v5 | 32 | 256 |
| Standard\_L48ps\_v5 | 48 | 384 |
| Standard\_L64ps\_v5 | 64 | 512 |
| Standard\_L96ps\_v5 | 96 | 768 |
| Standard\_L128ps\_v5 | 128 | 1,024 |

Note

This VM series will only work on OS images that support NVMe. If your current OS image doesn't have NVMe support, you'll see an error message. [NVMe](../../enable-nvme-interface) support is available on the most popular OS images, and we're continuously improving OS image compatibility.

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

| Size Name | Temp Storage Disks (Qty.) | Temp Disk Size (GB) | Temp Disk Random Read IOPS | Temp Disk Sequential Read Throughput (MBps) | Temp Disk Random Write IOPS | Temp Disk Sequential Write Throughput (MBps) |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_L1ps\_v5 | 1 | 240 | 75,000 | 380 | 37,500 | 190 |
| Standard\_L2ps\_v5 | 1 | 480 | 150,000 | 750 | 75,000 | 380 |
| Standard\_L4ps\_v5 | 2 | 480 | 300,000 | 1,500 | 150,000 | 750 |
| Standard\_L8ps\_v5 | 4 | 480 | 600,000 | 3,000 | 300,000 | 1,500 |
| Standard\_L16ps\_v5 | 1 | 3,840 | 1,200,000 | 6,000 | 600,000 | 3,000 |
| Standard\_L32ps\_v5 | 2 | 3,840 | 2,400,000 | 12,000 | 1,200,000 | 6,000 |
| Standard\_L48ps\_v5 | 3 | 3,840 | 3,600,000 | 18,000 | 1,800,000 | 9,000 |
| Standard\_L64ps\_v5 | 4 | 3,840 | 4,800,000 | 24,000 | 2,400,000 | 12,000 |
| Standard\_L96ps\_v5 | 6 | 3,840 | 7,200,000 | 36,000 | 3,600,000 | 18,000 |
| Standard\_L128ps\_v5 | 6 | 3,840 | 7,200,000 | 36,000 | 3,600,000 | 18,000 |

#### Storage resources

- [NVMe Overview](../../nvme-overview)
- [FAQ for temp NVMe disks](../../enable-nvme-temp-faqs)

#### Table definitions

- Total local temporary storage is calculated by multiplying the max number of storage disks with the temp disk size. For example, for the Standard\_L128ps\_v5, the total local temporary storage capacity is `6 x 3,840 GB = 23,040 GB`.
- Temp disk performance depends on many factors including block size, workload patterns of read/writes, queue depth (QD), and others. Temp disk performance specifications should be viewed as best case performance numbers, assuming 4k block sizes and QD=256 for IOPS, and 256k block sizes with QD=64 for throughput. Read performance specs assume 100% reads, and write performance specs assume 100% writes. Additionally, write performance is heavily impacted by how many blocks in use on a device. Temp disk write performance specs assume a device has a clean slate to enable the best performance. During steady state operations, write performance is expected to be lower than the published specs.
- NVMe temp disks are presented as raw NVMe devices that need to be initialized and formatted before use. For more details on how to format and initialize drives, refer to the [NVMe Temp Disk FAQ](../../enable-nvme-temp-faqs).
- The IOPS and throughput values shown are the combined performance across all temp disks.
- Local storage capacity is shown in units of GB or 1,000^3 bytes. When you compare disks measured in GB (1,000^3 bytes) to disks measured in GiB (1,024^3) remember that capacity numbers given in GiB might appear smaller. For example, 1,023 GiB = 1,098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly (R-O) or ReadWrite (R-W). For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage Disks (Qty.) | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MBps) | Uncached Premium SSD Burst IOPS | Uncached Premium SSD Burst Throughput (MBps) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MBps) | Uncached Burst Ultra Disk and Premium SSD v2 IOPS | Uncached Burst Ultra Disk and Premium SSD v2 Throughput (MBps) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_L1ps\_v5 | 4 | 2,000 | 60 | 22,500 | 710 | 2,500 | 70 | 28,130 | 820 |
| Standard\_L2ps\_v5 | 8 | 4,000 | 120 | 45,000 | 1,410 | 5,000 | 140 | 56,250 | 1,640 |
| Standard\_L4ps\_v5 | 12 | 8,000 | 240 | 45,000 | 1,410 | 10,000 | 270 | 56,250 | 1,640 |
| Standard\_L8ps\_v5 | 24 | 16,000 | 470 | 45,000 | 1,410 | 20,000 | 550 | 56,250 | 1,640 |
| Standard\_L16ps\_v5 | 48 | 32,000 | 940 | 75,000 | 1,410 | 40,000 | 1,100 | 93,750 | 1,640 |
| Standard\_L32ps\_v5 | 64 | 64,000 | 1,890 | 100,000 | 1,920 | 80,000 | 2,190 | 125,000 | 2,230 |
| Standard\_L48ps\_v5 | 64 | 96,000 | 2,830 | 160,000 | 2,870 | 120,000 | 3,290 | 200,000 | 3,340 |
| Standard\_L64ps\_v5 | 64 | 128,000 | 3,780 | 160,000 | 3,830 | 160,000 | 4,380 | 200,000 | 4,450 |
| Standard\_L96ps\_v5 | 64 | 192,000 | 5,660 | 192,000 | 5,660 | 240,000 | 6,580 | 240,000 | 6,580 |
| Standard\_L128ps\_v5 | 64 | 204,800 | 7,550 | 204,800 | 7,550 | 320,000 | 8,770 | 320,000 | 8,770 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- These sizes support [bursting](../../disk-bursting) to temporarily increase disk performance. Burst speeds can be maintained for up to 30 minutes at a time.
- Storage capacity is shown in units of GiB or 1,024^3 bytes. When you compare disks measured in GB (1,000^3 bytes) to disks measured in GiB (1,024^3) remember that capacity numbers given in GiB might appear smaller. For example, 1,023 GiB = 1,098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly or ReadWrite. For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Network](#tab/sizenetwork)
Network interface info for each size

| Size Name | Max NICs (Qty.) | Max Network Bandwidth (Mbps) |
| --- | --- | --- |
| Standard\_L1ps\_v5 | 2 | 12,500 |
| Standard\_L2ps\_v5 | 3 | 16,000 |
| Standard\_L4ps\_v5 | 4 | 25,000 |
| Standard\_L8ps\_v5 | 4 | 25,000 |
| Standard\_L16ps\_v5 | 8 | 25,000 |
| Standard\_L32ps\_v5 | 8 | 25,000 |
| Standard\_L48ps\_v5 | 8 | 35,000 |
| Standard\_L64ps\_v5 | 15 | 45,000 |
| Standard\_L96ps\_v5 | 15 | 70,000 |
| Standard\_L128ps\_v5 | 15 | 85,000 |

#### Networking resources

- [Virtual networks and virtual machines in Azure](/en-us/azure/virtual-network/network-overview)
- [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)

Note

Accelerated networking is required and turned on by default on all Lpsv5 machines.

#### Table definitions

- Expected network bandwidth is the maximum aggregated bandwidth allocated per VM type across all NICs, for all destinations. For more information, see [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)
- Upper limits aren't guaranteed. Limits offer guidance for selecting the right VM type for the intended application. Actual network performance will depend on several factors including network congestion, application loads, and network settings. For information on optimizing network throughput, see [Optimize network throughput for Azure virtual machines](/en-us/azure/virtual-network/virtual-network-optimize-network-bandwidth).
- To achieve the expected network performance on Linux or Windows, you might need to select a specific version or optimize your VM. For more information, see [Bandwidth/Throughput testing (NTTTCP)](/en-us/azure/virtual-network/virtual-network-bandwidth-testing).

# [Accelerators](#tab/sizeaccelerators)
Accelerator (GPUs, FPGAs, etc.) info for each size

Note

No accelerators are present in this series.

---

## Feature support

| Feature name | Support status |
| --- | --- |
| [Premium Storage](../../premium-storage-performance) | Supported |
| [Premium Storage caching](../../premium-storage-performance) | Supported |
| [Live Migration](../../maintenance-and-updates#live-migration) | Not Supported |
| [Memory Preserving Updates](../../maintenance-and-updates) | Supported |
| [Generation 2 VMs](../../generation-2) | Supported |
| [Generation 1 VMs](../../generation-2) | Not Supported |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Required |
| [Ephemeral OS Disks](../../ephemeral-os-disks) | Supported |
| [Temporary local NVMe disks](../../enable-nvme-temp-faqs) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Not Supported |
| [Azure Disk Encryption for Linux VMs](../../linux/disk-encryption-linux#restrictions) | Not Supported |
| [Azure Disk Encryption for Windows VMs](../../windows/disk-encryption-windows#restrictions) | Not Supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)