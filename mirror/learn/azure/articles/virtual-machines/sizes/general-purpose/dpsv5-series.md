---
layout: Conceptual
title: Dpsv5 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dpsv5-series
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
description: Information on and specifications of the Dpsv5-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: aa8bca0c-449b-3e08-5395-cd3d42121427
document_version_independent_id: 091696f9-8ec8-4b81-d92a-2014cb8da2b7
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/general-purpose/dpsv5-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/general-purpose/dpsv5-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/general-purpose/dpsv5-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: db218ec4-98ee-0349-f5ba-ac127662d4cd
---

# Dpsv5 size series - Azure Virtual Machines | Microsoft Learn

The Dpsv5-series and Dpdsv5-series virtual machines are based on the Arm architecture, delivering outstanding price-performance for general-purpose workloads. These virtual machines feature the Ampere® Altra® Arm-based processor operating at 3.0 GHz, which provides an entire physical core for each virtual machine vCPU. These virtual machines offer a range of vCPU sizes, up to 4 GiB of memory per vCPU, and temporary storage options able to meet the requirements of scale-out and most enterprise workloads such as web and application servers, small to medium databases, caches, and more.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 64 vCPUs | Ampere Altra [Arm64] |
| Memory | 8 - 208 GiB |  |
| Local Storage | None |  |
| Remote Storage | 4 - 32 Disks | 4,000 - 80,000 IOPS 85 - 1,735 MBps Disk Types: [Standard SDD/HDD](../../disks-types#standard-ssds), [Premium SSD](../../disks-types#premium-ssds) |
| Network | 2 - 8 NICs | 12,500 - 40,000 Mbps Interfaces: NetVSC, ConnectX |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_D2ps\_v5 | 2 | 8 |
| Standard\_D4ps\_v5 | 4 | 16 |
| Standard\_D8ps\_v5 | 8 | 32 |
| Standard\_D16ps\_v5 | 16 | 64 |
| Standard\_D32ps\_v5 | 32 | 128 |
| Standard\_D48ps\_v5 | 48 | 192 |
| Standard\_D64ps\_v5 | 64 | 208 |

#### VM Basics resources

- [What are vCPUs](../../managed-disks-overview)
- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

Note

No local storage present in this series. For similar sizes with local storage, see the [Dpdsv6-series](dpdsv6-series).

For frequently asked questions, see [Azure VM sizes with no local temp disk](../../azure-vms-no-temp-disk).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage Disks (Qty.) | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MBps) | Uncached Premium SSD Burst IOPS | Uncached Premium SSD Burst Throughput (MBps) |
| --- | --- | --- | --- | --- | --- |
| Standard\_D2ps\_v5 | 4 | 3,750 | 85 | 10,000 | 1,200 |
| Standard\_D4ps\_v5 | 8 | 6,400 | 145 | 20,000 | 1,200 |
| Standard\_D8ps\_v5 | 16 | 12,800 | 290 | 20,000 | 1,200 |
| Standard\_D16ps\_v5 | 32 | 25,600 | 600 | 40,000 | 1,200 |
| Standard\_D32ps\_v5 | 32 | 51,200 | 865 | 80,000 | 2,000 |
| Standard\_D48ps\_v5 | 32 | 76,800 | 1,315 | 80,000 | 3,000 |
| Standard\_D64ps\_v5 | 32 | 80,000 | 1,735 | 80,000 | 3,000 |

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
| Standard\_D2ps\_v5 | 2 | 12,500 |
| Standard\_D4ps\_v5 | 2 | 12,500 |
| Standard\_D8ps\_v5 | 4 | 12,500 |
| Standard\_D16ps\_v5 | 4 | 12,500 |
| Standard\_D32ps\_v5 | 8 | 16,000 |
| Standard\_D48ps\_v5 | 8 | 24,000 |
| Standard\_D64ps\_v5 | 8 | 40,000 |

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
| [VM Generation Support](../../generation-2) | Generation 2 |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Required |
| [Ephemeral OS Disks](../../ephemeral-os-disks) | Not supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Not supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)