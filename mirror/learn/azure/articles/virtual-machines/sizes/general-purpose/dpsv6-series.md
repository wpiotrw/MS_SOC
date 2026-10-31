---
layout: Conceptual
title: Dpsv6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dpsv6-series
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
ms.reviewer: mattmcinnes, tomvcassidy
ms.author: noahwood
ms.update-cycle: 1095-days
description: Information on and specifications of the Dpsv6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.custom:
- build-2024
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: 20c32ff2-b6a4-2f5b-cae1-db7199af27cc
document_version_independent_id: 79868284-95b9-b4bb-c25d-d3fe1e65647e
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/general-purpose/dpsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/general-purpose/dpsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/general-purpose/dpsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 5be51956-3a31-3797-d9da-a23d0c34b826
---

# Dpsv6 size series - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows Client VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

The Dpsv6-series virtual machines are powered by Azure's first-generation Cobalt 100 processor, delivering outstanding performance for general-purpose workloads. The Azure Cobalt 100 processor operates at 3.4 GHz and provides an entire physical core for each virtual machine vCPU. These virtual machines offer 4 GiB of memory per vCPU and a wide range of vCPU sizes. These VMs meet the requirements of most scale-out enterprise workloads such as web and application servers, small to medium databases, caches, and more. Dpsv6-series virtual machines support Standard SSD, Standard HDD, and Premium SSD types. You can also attach Ultra Disk storage based on its regional availability. Disk storage is billed separately from virtual machines. For more information, [see pricing for disks](https://azure.microsoft.com/pricing/details/managed-disks/). Dpsv6-series virtual machines offer up to 96 vCPU and 384 GiB of RAM. These VMs come without local disk, providing a better value proposition for workloads that don't require local temporary storage.

## Host specifications

| Part | QuantityCount Units | SpecsSKU ID, Performance Units, etc. |
| --- | --- | --- |
| Processor | 2 - 96 vCPUs | Azure Cobalt 100 [Arm64] |
| Memory | 8 - 384 GiB |  |
| Local Storage | None |  |
| Remote Storage | 8 - 64 Disks | 4,000 - 200,000 IOPS 106 - 5,850 MBps Disk Types: [Standard SDD/HDD](../../disks-types#standard-ssds), [Premium SSD](../../disks-types#premium-ssds), [Premium SSD v2](../../disks-types#premium-ssd-v2), [Ultra Disk](../../disks-types#ultra-disks) |
| Network | 2 - 8 NICs | 12,500 - 60,000 Mbps Interfaces: NetVSC, ConnectX, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_D2ps\_v6 | 2 | 8 |
| Standard\_D4ps\_v6 | 4 | 16 |
| Standard\_D8ps\_v6 | 8 | 32 |
| Standard\_D16ps\_v6 | 16 | 64 |
| Standard\_D32ps\_v6 | 32 | 128 |
| Standard\_D48ps\_v6 | 48 | 192 |
| Standard\_D64ps\_v6 | 64 | 256 |
| Standard\_D96ps\_v6 | 96 | 384 |

#### VM Basics resources

- [What are vCPUs (Qty.)](../../managed-disks-overview)
- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

Note

No local storage present in this series. For similar sizes with local storage, see the [Dpdsv6-series](dpdsv6-series).

For frequently asked questions, see [Azure VM sizes with no local temp disk](../../azure-vms-no-temp-disk).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage (Qty.) | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MBps) | Uncached Premium SSD Burst IOPS | Uncached Premium SSD Burst Throughput (MBps) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MBps) | Uncached Burst Ultra Disk and Premium SSD v2 IOPS | Uncached Burst Ultra Disk and Premium SSD v2 Throughput (MBps) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_D2ps\_v6 | 8 | 3,750 | 106 | 10,000 | 1,250 | 4,163 | 124 | 11,100 | 1,463 |
| Standard\_D4ps\_v6 | 12 | 6,400 | 212 | 20,000 | 1,250 | 8,333 | 248 | 26,040 | 1,463 |
| Standard\_D8ps\_v6 | 24 | 12,800 | 424 | 20,000 | 1,250 | 16,666 | 496 | 26,040 | 1,463 |
| Standard\_D16ps\_v6 | 48 | 25,600 | 848 | 40,000 | 1,250 | 33,331 | 992 | 52,080 | 1,463 |
| Standard\_D32ps\_v6 | 64 | 51,200 | 1,696 | 80,000 | 2,000 | 66,662 | 1,984 | 104,160 | 2,340 |
| Standard\_D48ps\_v6 | 64 | 76,800 | 2,544 | 80,000 | 3,000 | 99,994 | 2,976 | 104,160 | 3,510 |
| Standard\_D64ps\_v6 | 64 | 102,400 | 3,392 | 102,400 | 3,392 | 133,325 | 3,969 | 133,325 | 3,969 |
| Standard\_D96ps\_v6 | 64 | 153,600 | 5,000 | 153,600 | 5,000 | 199,987 | 5,850 | 199,987 | 5,850 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- These sizes support [bursting](../../disk-bursting) to temporarily increase disk performance. Burst speeds can be maintained for up to 30 minutes at a time.
- Storage capacity is shown in units of GiB or 1,024^3 bytes. When you compare disks measured in GB (1,000^3 bytes) to disks measured in GiB (1,024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1,023 GiB = 1,098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly or ReadWrite. For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Network](#tab/sizenetwork)
Network interface info for each size

| Size Name | Max NICs (Qty.) | Max Network Bandwidth (Mbps) |
| --- | --- | --- |
| Standard\_D2ps\_v6 | 2 | 12,500 |
| Standard\_D4ps\_v6 | 2 | 12,500 |
| Standard\_D8ps\_v6 | 4 | 15,000 |
| Standard\_D16ps\_v6 | 8 | 15,000 |
| Standard\_D32ps\_v6 | 8 | 20,000 |
| Standard\_D48ps\_v6 | 8 | 30,000 |
| Standard\_D64ps\_v6 | 8 | 40,000 |
| Standard\_D96ps\_v6 | 8 | 60,000 |

#### Networking resources

- [Virtual networks and virtual machines in Azure](/en-us/azure/virtual-network/network-overview)
- [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)

Note

Accelerated networking is required and turned on by default on all Dpsv6 machines.

#### Table definitions

- Expected network bandwidth is the maximum aggregated bandwidth allocated per VM type across all NICs, for all destinations. For more information, see [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)
- Upper limits aren't guaranteed. Limits offer guidance for selecting the right VM type for the intended application. Actual network performance will depend on several factors including network congestion, application loads, and network settings. For information on optimizing network throughput, see [Optimize network throughput for Azure virtual machines](/en-us/azure/virtual-network/virtual-network-optimize-network-bandwidth).
- To achieve the expected network performance on Linux or Windows, you may need to select a specific version or optimize your VM. For more information, see [Bandwidth/Throughput testing (NTTTCP)](/en-us/azure/virtual-network/virtual-network-bandwidth-testing).

# [Accelerators](#tab/sizeaccelerators)
Accelerator (GPUs, FPGAs, etc.) info for each size

Note

No accelerators are present in this series.

---

## Feature Support

| Feature name | Support status |
| --- | --- |
| [Premium Storage](../../premium-storage-performance) | Supported |
| [Premium Storage caching](../../premium-storage-performance) | Supported |
| [Live Migration](../../maintenance-and-updates#live-migration) | Supported |
| [Memory Preserving Updates](../../maintenance-and-updates) | Supported |
| [VM Generation Support](../../generation-2) | Generation 2 |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Required |
| [Ephemeral OS Disks](../../ephemeral-os-disks) | Not supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Not supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)