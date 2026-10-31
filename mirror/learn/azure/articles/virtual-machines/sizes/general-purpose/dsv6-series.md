---
layout: Conceptual
title: Dsv6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dsv6-series
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
ms.author: mattmcinnes
ms.update-cycle: 1095-days
description: Information on and specifications of the Dsv6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: ffc7aa5f-3547-633c-66fe-190644cf2c8b
document_version_independent_id: d3af4769-0798-2985-c3c8-93515b5cf0d0
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/general-purpose/dsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/general-purpose/dsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/general-purpose/dsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: a9427fd5-74d7-38f5-2271-3a6559cae4ff
---

# Dsv6 size series - Azure Virtual Machines | Microsoft Learn

Dsv6-series virtual machines run on the 5th Generation Intel® Xeon® Platinum 8573C (Emerald Rapids) processor reaching an all-core turbo clock speed of 3.0 GHz. This new processor features [Intel® Turbo Boost Technology](https://www.intel.com/content/www/us/en/architecture-and-technology/turbo-boost/turbo-boost-technology.html), [Intel® Advanced-Vector Extensions 512 (Intel® AVX-512)](https://www.intel.com/content/www/us/en/architecture-and-technology/avx-512-overview.html), and [Intel® Advanced Matrix Extensions](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html). These virtual machines offer up to 192 vCPU and 768 GiB of RAM. Dsv6-series virtual machines provide a better performance for most general-purpose workloads compared to the prior generation (for example, increased scalability, upgraded CPU, elevated memory bandwidth, faster remote storage access).

Dsv6-series virtual machines don't have any temporary storage thus lowering the price of entry. You can attach Standard SSDs, Standard HDDs, Premium SSDs, and Premium SSD v2 storage to these virtual machines. You can also attach Ultra Disk storage based on its regional availability. Disk storage is billed separately from virtual machines.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 192 vCPUs | Intel Xeon Platinum 8573C (Emerald Rapids) [x86-64] |
| Memory | 8 - 768 GiB |  |
| Local Storage | None |  |
| Remote Storage | 8 - 64 Disks | 4,000 - 400,000 IOPS 106 - 12,000 MBps Disk Types: [Standard SDD/HDD](../../disks-types#standard-ssds), [Premium SSD](../../disks-types#premium-ssds), [Premium SSD v2](../../disks-types#premium-ssd-v2), [Ultra Disk](../../disks-types#ultra-disks) |
| Remote Storage | 8 - 64 Disks | 4,000 - 400,000 IOPS 124 - 12,000 MBps |
| Network | 2 - 8 NICs | 12,500 - 82,000 Mbps Interfaces: NetVSC, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_D2s\_v6 | 2 | 8 |
| Standard\_D4s\_v6 | 4 | 16 |
| Standard\_D8s\_v6 | 8 | 32 |
| Standard\_D16s\_v6 | 16 | 64 |
| Standard\_D32s\_v6 | 32 | 128 |
| Standard\_D48s\_v6 | 48 | 192 |
| Standard\_D64s\_v6 | 64 | 256 |
| Standard\_D96s\_v6 | 96 | 384 |
| Standard\_D128s\_v6 | 128 | 512 |
| Standard\_D192s\_v6 | 192 | 768 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

Note

No local storage present in this series.

For frequently asked questions, see [Azure VM sizes with no local temp disk](../../azure-vms-no-temp-disk).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage Disks (Qty.) | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MBps) | Uncached Premium SSD Burst IOPS | Uncached Premium SSD Burst Throughput (MBps) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MBps) | Uncached Burst Ultra Disk and Premium SSD v2 IOPS | Uncached Burst Ultra Disk and Premium SSD v2 Throughput (MBps) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_D2s\_v6 | 8 | 3,750 | 106 | 40,000 | 1,250 | 4,167 | 124 | 44,444 | 1,463 |
| Standard\_D4s\_v6 | 12 | 6,400 | 212 | 40,000 | 1,250 | 8,333 | 248 | 52,083 | 1,463 |
| Standard\_D8s\_v6 | 24 | 12,800 | 424 | 40,000 | 1,250 | 16,667 | 496 | 52,083 | 1,463 |
| Standard\_D16s\_v6 | 48 | 25,600 | 848 | 40,000 | 1,250 | 33,333 | 992 | 52,083 | 1,463 |
| Standard\_D32s\_v6 | 64 | 51,200 | 1,696 | 80,000 | 1,696 | 66,667 | 1,984 | 104,167 | 1,984 |
| Standard\_D48s\_v6 | 64 | 76,800 | 2,544 | 80,000 | 2,544 | 100,000 | 2,976 | 104,167 | 2,976 |
| Standard\_D64s\_v6 | 64 | 102,400 | 3,392 | 102,400 | 3,392 | 133,333 | 3,969 | 133,333 | 3,969 |
| Standard\_D96s\_v6 | 64 | 153,600 | 5,088 | 153,600 | 5,088 | 200,000 | 5,953 | 200,000 | 5,953 |
| Standard\_D128s\_v6 | 64 | 204,800 | 6,782 | 204,800 | 6,782 | 266,667 | 7,935 | 266,667 | 7,935 |
| Standard\_D192s\_v6 | 64 | 260,000 | 12,000 | 260,000 | 12,000 | 400,400 | 12,000 | 400,400 | 12,000 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- Some sizes support [bursting](../../disk-bursting) to temporarily increase disk performance. Burst speeds can be maintained for up to 30 minutes at a time.
- Storage capacity is shown in units of GiB or 1,024^3 bytes. When you compare disks measured in GB (1,000^3 bytes) to disks measured in GiB (1,024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1,023 GiB = 1,098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly or ReadWrite. For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Network](#tab/sizenetwork)
Network interface info for each size

| Size Name | Max NICs (Qty.) | Max Network Bandwidth (Mbps) |
| --- | --- | --- |
| Standard\_D2s\_v6 | 2 | 12,500 |
| Standard\_D4s\_v6 | 2 | 12,500 |
| Standard\_D8s\_v6 | 4 | 12,500 |
| Standard\_D16s\_v6 | 8 | 12,500 |
| Standard\_D32s\_v6 | 8 | 16,000 |
| Standard\_D48s\_v6 | 8 | 24,000 |
| Standard\_D64s\_v6 | 8 | 30,000 |
| Standard\_D96s\_v6 | 8 | 41,000 |
| Standard\_D128s\_v6 | 8 | 54,000 |
| Standard\_D192s\_v6 | 8 | 82,000 |

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
| [Live Migration](../../maintenance-and-updates) | Supported |
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