---
layout: Conceptual
title: Edsv6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/edsv6-series
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
author: mattmcinnes
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: mattmcinnes
ms.update-cycle: 1095-days
description: Information on and specifications of the Edsv6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: 72e52406-6217-d8e0-9d86-d1e29f2cfcd4
document_version_independent_id: 52ad97be-554f-0cea-8e44-bec07cd6354b
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/edsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/edsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/edsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/92b2ad1c-e9f4-4efc-9995-033db4d8e4a1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/deb7f546-d791-43c4-a74b-a8b1bcca9da4
platformId: d6c84a09-e369-80c4-5379-d02ca76e5526
---

# Edsv6 size series - Azure Virtual Machines | Microsoft Learn

Edsv6-series virtual machines run on the 5th Generation Intel® Xeon® Platinum 8573C (Emerald Rapids) processor reaching an all-core turbo clock speed of 3.0 GHz. This new processor features [Intel® Turbo Boost Technology](https://www.intel.com/content/www/us/en/architecture-and-technology/turbo-boost/turbo-boost-technology.html), [Intel® Advanced-Vector Extensions 512 (Intel® AVX-512)](https://www.intel.com/content/www/us/en/architecture-and-technology/avx-512-overview.html), and [Intel® Advanced Matrix Extensions](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html). These virtual machines offer up to 192 vCPU and 1,832 GiB of RAM and fast, local SSD storage up to 6x1760 GiB. Edsv6-series virtual machines are ideal for memory-intensive workloads such as relational database servers, large databases, data analytics engines, in-memory caches, and more.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 192 vCPUs | Intel Xeon Platinum 8573C (Emerald Rapids) [x86-64] |
| Memory | 16 - 1024 GiB |  |
| Local Storage | 1 - 4 Disks | 110 - 1760 GiB 37500 - 2400000 IOPS 180 - 11520 MBps |
| Remote Storage [Premium SSD](../../disks-types#premium-ssds) | 8 - 64 Disks | 3750 - 360000 IOPS 106 - 17280 MBps |
| Remote Storage [Premium SSD v2](../../disks-types#premium-ssd-v2) / [Ultra Disks](../../disks-types#ultra-disks) | 8 - 64 Disks | 4167 - 400000 IOPS 124 - 12000 MBps |
| Network | 2 - 8 NICs | 12500 - 54000 Mbps Interfaces: NetVSC, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GB) |
| --- | --- | --- |
| Standard\_E2ds\_v6 | 2 | 16 |
| Standard\_E4ds\_v6 | 4 | 32 |
| Standard\_E8ds\_v6 | 8 | 64 |
| Standard\_E16ds\_v6 | 16 | 128 |
| Standard\_E20ds\_v6 | 20 | 160 |
| Standard\_E32ds\_v6 | 32 | 256 |
| Standard\_E48ds\_v6 | 48 | 384 |
| Standard\_E64ds\_v6 | 64 | 512 |
| Standard\_E96ds\_v6 | 96 | 768 |
| Standard\_E128ds\_v6 | 128 | 1024 |
| Standard\_E192ids\_v6 | 192 | 1832 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

| Size Name | Max Temp Storage Disks (Qty.) | Temp Disk Size (GiB) | Temp Disk Random Read (RR)^1^IOPS | Temp Disk Random Read (RR)^1^Throughput (MB/s) | Temp Disk Random Write (RW)^1^IOPS | Temp Disk Random Write (RW)^1^Throughput (MB/s) |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2ds\_v6 | 1 | 110 | 37500 | 180 | 15000 | 90 |
| Standard\_E4ds\_v6 | 1 | 220 | 75000 | 360 | 30000 | 180 |
| Standard\_E8ds\_v6 | 1 | 440 | 150000 | 720 | 60000 | 360 |
| Standard\_E16ds\_v6 | 2 | 440 | 300000 | 1440 | 120000 | 720 |
| Standard\_E20ds\_v6 | 2 | 550 | 375000 | 1800 | 150000 | 900 |
| Standard\_E32ds\_v6 | 4 | 440 | 600000 | 2880 | 240000 | 1440 |
| Standard\_E48ds\_v6 | 6 | 440 | 900000 | 4320 | 360000 | 2160 |
| Standard\_E64ds\_v6 | 4 | 880 | 1200000 | 5760 | 480000 | 2880 |
| Standard\_E96ds\_v6 | 6 | 880 | 1800000 | 8640 | 720000 | 4320 |
| Standard\_E128ds\_v6 | 4 | 1760 | 2400000 | 11520 | 960000 | 5760 |
| Standard\_E192ids\_v6 | 6 | 1760 | 3600000 | 17280 | 1440000 | 8640 |

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
| Standard\_E2ds\_v6 | 8 | 3750 | 106 | 40000 | 1250 | 4167 | 124 | 44444 | 1463 |
| Standard\_E4ds\_v6 | 12 | 6400 | 212 | 40000 | 1250 | 8333 | 248 | 52083 | 1463 |
| Standard\_E8ds\_v6 | 24 | 12800 | 424 | 40000 | 1250 | 16667 | 496 | 52083 | 1463 |
| Standard\_E16ds\_v6 | 48 | 25600 | 848 | 40000 | 1250 | 33333 | 992 | 52083 | 1463 |
| Standard\_E20ds\_v6 | 48 | 32000 | 1060 | 64000 | 1600 | 41667 | 1240 | 83333 | 1872 |
| Standard\_E32ds\_v6 | 64 | 51200 | 1696 | 80000 | 1696 | 66667 | 1984 | 104167 | 1984 |
| Standard\_E48ds\_v6 | 64 | 76800 | 2544 | 80000 | 2544 | 100000 | 2976 | 104167 | 2976 |
| Standard\_E64ds\_v6 | 64 | 102400 | 3392 | 102400 | 3392 | 133333 | 3969 | 133333 | 3969 |
| Standard\_E96ds\_v6 | 64 | 153600 | 5088 | 153600 | 5088 | 200000 | 5953 | 200000 | 5953 |
| Standard\_E128ds\_v6 | 64 | 204800 | 6782 | 204800 | 6782 | 266667 | 7935 | 266667 | 7935 |
| Standard\_E128ds\_v6 | 64 | 204800 | 6782 | 204800 | 6782 | 266667 | 7935 | 266667 | 7935 |
| Standard\_E192ids\_v6 | 64 | 260000 | 12000 | 260000 | 12000 | 400000 | 12000 | 400000 | 12000 |

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
| Standard\_E2ds\_v6 | 2 | 12500 |
| Standard\_E4ds\_v6 | 2 | 12500 |
| Standard\_E8ds\_v6 | 4 | 12500 |
| Standard\_E16ds\_v6 | 8 | 12500 |
| Standard\_E20ds\_v6 | 8 | 12500 |
| Standard\_E32ds\_v6 | 8 | 16000 |
| Standard\_E48ds\_v6 | 8 | 24000 |
| Standard\_E64ds\_v6 | 8 | 30000 |
| Standard\_E96ds\_v6 | 8 | 41000 |
| Standard\_E128ds\_v6 | 8 | 54000 |
| Standard\_E192ids\_v6 | 8 | 200000 |

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
| [Live Migration](../../maintenance-and-updates#live-migration) | Supported |
| [Memory Preserving Updates](../../maintenance-and-updates) | Supported |
| [Generation 2 VMs](../../generation-2) | Supported |
| [Generation 1 VMs](../../generation-2) | Not Supported |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Required |
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Supported |
| [Temporary local NVMe disks](../../enable-nvme-temp-faqs) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Supported |
| [Azure Disk Encryption for Linux VMs](../../linux/disk-encryption-linux#restrictions) | Not Supported |
| [Azure Disk Encryption for Windows VMs](../../windows/disk-encryption-windows#restrictions) | Not Supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)