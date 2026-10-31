---
layout: Conceptual
title: Ebdsv6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/ebdsv6-series
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
author: bansal-misha
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: mishabansal
ms.update-cycle: 1095-days
description: Information on and specifications of the Ebdsv6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: ea27c752-c7ed-669e-2ab5-acbecb053426
document_version_independent_id: 1fe51899-60cc-87c3-cb50-9ea0fa9e4c98
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/ebdsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/ebdsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/ebdsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/92b2ad1c-e9f4-4efc-9995-033db4d8e4a1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/deb7f546-d791-43c4-a74b-a8b1bcca9da4
platformId: 7936705b-1732-555b-3878-48ec5c9d8a6e
---

# Ebdsv6 size series - Azure Virtual Machines | Microsoft Learn

The Ebdsv6-series virtual machines run on the fifth Generation Intel® Xeon® Platinum 8573C (Emerald Rapids) processor and deliver higher remote storage performance compared to the previous generation. The Ebdsv6-series is ideal for storage throughput intensive workloads. These virtual machines offer up to 800,000 IOPS and 14,000 MBps of remote disk storage performance. Additionally, the Ebsv6 VM series offer up to 192vCPU and 1,832 GiB of RAM providing larger processing power to consolidate workloads. Refer to the Premium SSD, Premium SSD v2, and Ultra Disks to attain published disk performance.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 192 vCPUs | Intel Xeon Platinum 8573C (Emerald Rapids) [x86-64] |
| Memory | 16 - 1832 GiB |  |
| Local Storage | 1 - 6 Disks | 110 - 1760 GiB  37500 - 3600000 IOPS 180 - 17280 MBps |
| Remote Storage | 8 - 64 Disks | 8800 - 800000 IOPS  253 - 14000 MBps |
| Network | 2 - 8 NICs | 12500 - 200000 Mbps Interfaces: NetVSC, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GB) |
| --- | --- | --- |
| Standard\_E2bds\_v6 | 2 | 16 |
| Standard\_E4bds\_v6 | 4 | 32 |
| Standard\_E8bds\_v6 | 8 | 64 |
| Standard\_E16bds\_v6 | 16 | 128 |
| Standard\_E32bds\_v6 | 32 | 256 |
| Standard\_E48bds\_v6 | 48 | 384 |
| Standard\_E64bds\_v6 | 64 | 512 |
| Standard\_E96bds\_v6 | 96 | 768 |
| Standard\_E128bds\_v6 | 128 | 1024 |
| Standard\_E192ibds\_v6 | 192 | 1832 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

| Size Name | Max Temp Storage Disks (Qty.) | Temp Disk Size (GiB) | Temp Disk Random Read (RR)^1^IOPS | Temp Disk Random Read (RR)^1^Throughput (MB/s) | Temp Disk Random Write (RW)^1^IOPS | Temp Disk Random Write (RW)^1^Throughput (MB/s) |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2bds\_v6 | 1 | 110 | 37500 | 180 | 15000 | 90 |
| Standard\_E4bds\_v6 | 1 | 220 | 75000 | 360 | 30000 | 180 |
| Standard\_E8bds\_v6 | 1 | 440 | 150000 | 720 | 60000 | 360 |
| Standard\_E16bds\_v6 | 2 | 440 | 300000 | 1440 | 120000 | 720 |
| Standard\_E32bds\_v6 | 4 | 440 | 600000 | 2880 | 240000 | 1440 |
| Standard\_E48bds\_v6 | 6 | 440 | 900000 | 4320 | 360000 | 2160 |
| Standard\_E64bds\_v6 | 4 | 880 | 1200000 | 5760 | 480000 | 2880 |
| Standard\_E96bds\_v6 | 6 | 880 | 1800000 | 8640 | 720000 | 4320 |
| Standard\_E128bds\_v6 | 4 | 1760 | 2400000 | 11520 | 960000 | 5760 |
| Standard\_E192ibds\_v6 | 6 | 1760 | 3600000 | 17280 | 1440000 | 8640 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- ^1^Temp disk speed often differs between RR (Random Read) and RW (Random Write) operations. RR operations are typically faster than RW operations. The RW speed is usually slower than the RR speed on series where only the RR speed value is listed.
- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Remote storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage Disks (Qty.) | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MB/s) | Uncached Premium SSD Burst^1^IOPS | Uncached Premium SSD Burst^1^Throughput (MB/s) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MB/s) | Uncached Burst^1^Ultra Disk and Premium SSD v2 IOPS | Uncached Burst^1^Ultra Disk and Premium SSD v2 Throughput (MB/s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2bds\_v6 | 8 | 8800 | 253 | 30000 | 1200 | 13200 | 330 | 45000 | 1565 |
| Standard\_E4bds\_v6 | 12 | 17600 | 506 | 35000 | 1200 | 23540 | 660 | 46813 | 1565 |
| Standard\_E8bds\_v6 | 24 | 36300 | 1023 | 44000 | 1500 | 48620 | 1320 | 58933 | 1935 |
| Standard\_E16bds\_v6 | 48 | 72600 | 1980 | 77000 | 2500 | 97240 | 2530 | 103133 | 3194 |
| Standard\_E32bds\_v6 | 64 | 143000 | 4070 | 154000 | 5000 | 191620 | 5280 | 206360 | 6486 |
| Standard\_E48bds\_v6 | 64 | 209000 | 6160 | 220000 | 7000 | 278630 | 8030 | 293295 | 9124 |
| Standard\_E64bds\_v6 | 64 | 242000 | 6600 | 253000 | 8000 | 324280 | 8580 | 339020 | 10400 |
| Standard\_E96bds\_v6 | 64 | 286000 | 8250 | 286000 | 10000 | 429000 | 9900 | 429000 | 12000 |
| Standard\_E128bds\_v6 | 64 | 330000 | 10000 | 350000 | 11500 | 500000 | 12000 | 530303 | 13800 |
| Standard\_E192ibds\_v6 | 64 | 400000 | 14000 | 400000 | 14000 | 800000 | 14000 | 800000 | 14000 |

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
| Standard\_E2bds\_v6 | 2 | 12500 |
| Standard\_E4bds\_v6 | 2 | 12500 |
| Standard\_E8bds\_v6 | 4 | 12500 |
| Standard\_E16bds\_v6 | 8 | 12500 |
| Standard\_E32bds\_v6 | 8 | 16000 |
| Standard\_E48bds\_v6 | 8 | 24000 |
| Standard\_E64bds\_v6 | 8 | 30000 |
| Standard\_E96bds\_v6 | 8 | 41000 |
| Standard\_E128bds\_v6 | 8 | 54000 |
| Standard\_E192ibds\_v6 | 8 | 200000 |

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
| [Live Migration](../../maintenance-and-updates) | Not Supported |
| [Memory Preserving Updates](../../maintenance-and-updates) | Supported |
| [Generation 2 VMs](../../generation-2) | Supported |
| [Generation 1 VMs](../../generation-2) | Not Supported |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Required |
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Supported |
| [Azure Disk Encryption for Linux VMs](../../linux/disk-encryption-linux#restrictions) | Not Supported |
| [Azure Disk Encryption for Windows VMs](../../windows/disk-encryption-windows#restrictions) | Not Supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)