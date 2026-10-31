---
layout: Conceptual
title: Dnlsv6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/dnlsv6-series
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
author: iamwilliew
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: wwilliams
ms.update-cycle: 1095-days
description: Information on and specifications of the Dnlsv6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: 29edc501-3956-951d-af27-6e1ed79a3d48
document_version_independent_id: 11005bfa-69eb-81e8-17cc-22be17796029
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/dnlsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/dnlsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/dnlsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 46fbd343-6732-a2df-6c06-9ee985310dac
---

# Dnlsv6 size series - Azure Virtual Machines | Microsoft Learn

Dnlsv6-series virtual machines run on 5th Generation Intel® Xeon® Platinum 8573C (Emerald Rapids) CPU processor reaching an all- core turbo clock speed of up to 3.0 GHz. These virtual machines offer up to 128 vCPU and 256 GiB of RAM. These VM sizes can reduce costs when running non-memory intensive applications. Dnlsv6-series virtual machines, an extension of our standard Dlsv6-series, provide better networking performance for most general-purpose workloads.

Network Optimized VMs enhance accelerated networking by providing hardware acceleration of initial connection setup for certain traffic types, a task previously performed in software. These enhancements reduce the end-to-end latency for initially establishing a connection or initial packet flow, and allow a VM to scale up the number of connections it manages more quickly, subject to application constraints.

The new Network Optimized sizes make use of enhancements provided by Azure Boost to deliver increased network bandwidth per vCPU, a greater number of vNICs, and improved connection setup performance. The Dnlsv6 offers up to 200 Gbps network bandwidth, 15 vNICs and up to 400k Connection per Second (CPS).

These VM sizes are relevant for workloads such as network virtual appliances, large-scale e-commerce applications that require the ability to handle a high number of user connections, and data transfers and media processing tasks that involve transferring large amounts of data quickly. Other applications will also benefit from increased network connection setup performance.

Dnlsv6-series virtual machines don't have any temporary storage, thus lowering the price of entry. You can attach Standard SSD, Standard HDD, and Premium SSD types. You can also attach Ultra Disk storage based on its regional availability. Disk storage is billed separately from virtual machines.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 128 vCPUs | Intel Xeon Platinum 8573C (Emerald Rapids) [x86-64] |
| Memory | 4 - 256 GiB |  |
| Local Storage | None |  |
| Remote Storage [Premium SSD](../../disks-types#premium-ssds) | 8 - 64 Disks | 3750 - 204800 IOPS 106 - 6782 MBps |
| Remote Storage [Premium SSD v2](../../disks-types#premium-ssd-v2) / [Ultra Disks](../../disks-types#ultra-disks) | 8 - 64 Disks | 4167 - 266667 IOPS 124 - 7935 MBps |
| Network | 4 - 15 NICs | 25000 - 200000 Mbps Interfaces: NetVSC, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GB) |
| --- | --- | --- |
| Standard\_D2nls\_v6 | 2 | 4 |
| Standard\_D4nls\_v6 | 4 | 8 |
| Standard\_D8nls\_v6 | 8 | 16 |
| Standard\_D16nls\_v6 | 16 | 32 |
| Standard\_D32nls\_v6 | 32 | 64 |
| Standard\_D48nls\_v6 | 48 | 96 |
| Standard\_D64nls\_v6 | 64 | 128 |
| Standard\_D96nls\_v6 | 96 | 192 |
| Standard\_D128nls\_v6 | 128 | 256 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local storage](#tab/sizestoragelocal)
Note

No local storage present in this series.

For frequently asked questions, see [Azure VM sizes with no local temp disk](../../azure-vms-no-temp-disk).

# [Remote storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage Disks (Qty.) | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MB/s) | Uncached Premium SSD Burst^1^IOPS | Uncached Premium Uncached Premium SSD Burst^1^Throughput (MB/s) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MB/s) | Uncached Burst^1^Ultra Disk and Premium SSD v2 IOPS | Uncached Burst^1^Ultra Disk and Premium SSD v2 Throughput (MB/s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_D2nls\_v6 | 8 | 3750 | 106 | 40000 | 1250 | 4167 | 124 | 44444 | 1463 |
| Standard\_D4nls\_v6 | 12 | 6400 | 212 | 40000 | 1250 | 8333 | 248 | 52083 | 1463 |
| Standard\_D8nls\_v6 | 24 | 12800 | 424 | 40000 | 1250 | 16667 | 496 | 52083 | 1463 |
| Standard\_D16nls\_v6 | 48 | 25600 | 848 | 40000 | 1250 | 33333 | 992 | 52083 | 1463 |
| Standard\_D32nls\_v6 | 64 | 51200 | 1696 | 80000 | 1696 | 66667 | 1984 | 104167 | 1984 |
| Standard\_D48nls\_v6 | 64 | 76800 | 2544 | 80000 | 2544 | 100000 | 2976 | 104167 | 2976 |
| Standard\_D64nls\_v6 | 64 | 102400 | 3392 | 102400 | 3392 | 133333 | 3969 | 133333 | 3969 |
| Standard\_D96nls\_v6 | 64 | 153600 | 5088 | 153600 | 5088 | 200000 | 5953 | 200000 | 5953 |
| Standard\_D128nls\_v6 | 64 | 204800 | 6782 | 204800 | 6782 | 266667 | 7935 | 266667 | 7935 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- ^1^Some sizes support [bursting](../../disk-bursting) to temporarily increase disk performance. Burst speeds can be maintained for up to 30 minutes at a time.
- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly or ReadWrite. For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Network](#tab/sizenetwork)
Network interface info for each size

| Size Name | Max NICs (Qty.) | Max Network Bandwidth (Mb/s) |
| --- | --- | --- |
| Standard\_D2nls\_v6 | 4 | 25000 |
| Standard\_D4nls\_v6 | 4 | 30000 |
| Standard\_D8nls\_v6 | 8 | 40000 |
| Standard\_D16nls\_v6 | 8 | 50000 |
| Standard\_D32nls\_v6 | 8 | 50000 |
| Standard\_D48nls\_v6 | 8 | 75000 |
| Standard\_D64nls\_v6 | 8 | 100000 |
| Standard\_D96nls\_v6 | 15 | 150000 |
| Standard\_D128nls\_v6 | 15 | 200000 |

#### Networking resources

- [Virtual networks and virtual machines in Azure](/en-us/azure/virtual-network/network-overview)
- [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)

#### Table definitions

- Expected network bandwidth is the maximum aggregated bandwidth allocated per VM type across all NICs, for all destinations. For more information, see [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)
- Upper limits aren't guaranteed. Limits offer guidance for selecting the right VM type for the intended application. Actual network performance will depend on several factors including network congestion, application loads, and network settings. For information on optimizing network throughput, see [Optimize network throughput for Azure virtual machines](/en-us/azure/virtual-network/virtual-network-optimize-network-bandwidth).
- To achieve the expected network performance on Linux or Windows, you may need to select a specific version or optimize your VM. For more information, see [Bandwidth/Throughput testing (NTTTCP)](/en-us/azure/virtual-network/virtual-network-bandwidth-testing).

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
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Not Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)