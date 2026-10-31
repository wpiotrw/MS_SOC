---
layout: Conceptual
title: Endsv6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/endsv6-series
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
description: Information on and specifications of the Endsv6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: ab88eca6-ebfe-a1fd-fc27-48b24d5cc3ae
document_version_independent_id: 66be8ae1-46cb-db1b-45f2-bd77b336bd8c
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/endsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/endsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/endsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 7f23a7a7-4c2a-a213-91ce-a3b45fe07bac
---

# Endsv6 size series - Azure Virtual Machines | Microsoft Learn

Endsv6-series virtual machines run on the 5th Generation Intel® Xeon® Platinum 8573C (Emerald Rapids) processor reaching an all- core turbo clock speed of up to 3.0 GHz. These virtual machines offer up to 128 vCPU and 1024 GiB of RAM. Endsv6-series virtual machines are ideal for memory-intensive enterprise applications and applications that benefit from low latency, high-speed local storage.

Network Optimized VMs enhance accelerated networking by providing hardware acceleration of initial connection setup for certain traffic types, a task previously performed in software. These enhancements reduce the end-to-end latency for initially establishing a connection or initial packet flow, and allow a VM to scale up the number of connections it manages more quickly, subject to application constraints.

Endsv6 VMs offer up to 200 Gbps network bandwidth, 15 vNICs and up to 400k Connection per Second (CPS). Both series also include up to 128 vCPU and 1024 GiB of RAM.

Both series provide up to 3x improvement in NW BW/vCPU than the current generation Intel Ev6 VMs. This series will be relevant for workloads such as network virtual appliances, large-scale e-commerce applications, express route, application gateway, and more that requires the ability to handle a high number of user connections and data transfers. They're also suited for media processing tasks that involve transferring large amounts of data quickly, and other applications that benefit from high NW BW/vCPU and CPS & flow limit configurations.

The Endsv6 series comes with a local disk. We recommend choosing Premium SSD, Premium SSD v2, or Ultra Disks to attain the published disk performance.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 128 vCPUs | Intel Xeon Platinum 8573C (Emerald Rapids) [x86-64] |
| Memory | 16 - 1024 GiB |  |
| Local Storage | 1 - 4 Disks | 110 - 1760 GiB 37500 - 2400000 180 - 11520 MBps |
| Remote Storage | 8 - 64 Disks | 3750 - 204800 IOPS 106 - 6782 MBps |
| Network | 4 - 15 NICs | 25000 - 200000 Mbps Interfaces: NetVSC, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GB) |
| --- | --- | --- |
| Standard\_E2nds\_v6 | 2 | 16 |
| Standard\_E4nds\_v6 | 4 | 32 |
| Standard\_E8nds\_v6 | 8 | 64 |
| Standard\_E16nds\_v6 | 16 | 128 |
| Standard\_E32nds\_v6 | 32 | 256 |
| Standard\_E48nds\_v6 | 48 | 384 |
| Standard\_E64nds\_v6 | 64 | 512 |
| Standard\_E96nds\_v6 | 96 | 768 |
| Standard\_E128nds\_v6 | 128 | 1024 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local storage](#tab/sizestoragelocal)
| Size Name | Max Temp Storage Disks (Qty.) | Temp Disk Size (GiB) | Temp Disk Random Read (RR)1 IOPS | Temp Disk Random Read (RR)1 Throughput (MB/s) | Temp Disk Random Write (RW)1 IOPS | Temp Disk Random Write (RW)1 Throughput (MB/s) |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2nds\_v6 | 1 | 110 | 37500 | 180 | 15000 | 90 |
| Standard\_E4nds\_v6 | 1 | 220 | 75000 | 360 | 30000 | 180 |
| Standard\_E8nds\_v6 | 1 | 440 | 150000 | 720 | 60000 | 360 |
| Standard\_E16nds\_v6 | 2 | 440 | 300000 | 1440 | 120000 | 720 |
| Standard\_E32nds\_v6 | 4 | 440 | 600000 | 2880 | 240000 | 1440 |
| Standard\_E48nds\_v6 | 6 | 440 | 900000 | 4320 | 360000 | 2160 |
| Standard\_E64nds\_v6 | 4 | 880 | 1200000 | 5760 | 480000 | 2880 |
| Standard\_E96nds\_v6 | 6 | 880 | 1800000 | 8640 | 720000 | 4320 |
| Standard\_E128nds\_v6 | 4 | 1760 | 2400000 | 11520 | 960000 | 5760 |

# [Remote storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage Disks (Qty.) | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MB/s) | Uncached Premium SSD Burst^1^IOPS | Uncached Premium Uncached Premium SSD Burst^1^Throughput (MB/s) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MB/s) | Uncached Burst^1^Ultra Disk and Premium SSD v2 IOPS | Uncached Burst^1^Ultra Disk and Premium SSD v2 Throughput (MB/s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2nds\_v6 | 8 | 3750 | 106 | 40000 | 1250 | 4167 | 124 | 44444 | 1463 |
| Standard\_E4nds\_v6 | 12 | 6400 | 212 | 40000 | 1250 | 8333 | 248 | 52083 | 1463 |
| Standard\_E8nds\_v6 | 24 | 12800 | 424 | 40000 | 1250 | 16667 | 496 | 52083 | 1463 |
| Standard\_E16nds\_v6 | 48 | 25600 | 848 | 40000 | 1250 | 33333 | 992 | 52083 | 1463 |
| Standard\_E32nds\_v6 | 64 | 51200 | 1696 | 80000 | 1696 | 66667 | 1984 | 104167 | 1984 |
| Standard\_E48nds\_v6 | 64 | 76800 | 2544 | 80000 | 2544 | 1000000 | 2976 | 104167 | 2976 |
| Standard\_E64nds\_v6 | 64 | 76800 | 2544 | 102400 | 3392 | 133333 | 3969 | 133333 | 3969 |
| Standard\_E96nds\_v6 | 64 | 153600 | 5088 | 153600 | 5088 | 200000 | 5953 | 200000 | 5953 |
| Standard\_E128nds\_v6 | 64 | 204800 | 6782 | 204800 | 6782 | 266667 | 7935 | 266667 | 7935 |

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
| Standard\_E2nds\_v6 | 4 | 25000 |
| Standard\_E4nds\_v6 | 4 | 30000 |
| Standard\_E8nds\_v6 | 8 | 40000 |
| Standard\_E16nds\_v6 | 8 | 50000 |
| Standard\_E32nds\_v6 | 8 | 50000 |
| Standard\_E48nds\_v6 | 8 | 75000 |
| Standard\_E64nds\_v6 | 8 | 100000 |
| Standard\_E96nds\_v6 | 15 | 150000 |
| Standard\_E128nds\_v6 | 15 | 200000 |

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
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Supported |
| [Temporary local NVMe disks](../../enable-nvme-temp-faqs) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)