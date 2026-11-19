---
layout: Conceptual
title: Msv4 Medium Memory size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/msv4-series
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
description: Information on and specifications of the Msv4-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-09-03T00:00:00.0000000Z
locale: en-us
document_id: 2339a645-6d24-6de1-d624-6e937ec11721
document_version_independent_id: 310aa20a-18f4-e542-25ae-241272bb350b
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/msv4-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/msv4-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/msv4-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/0811fd70-54cc-4b30-9df4-d821a6be00ca
- https://authoring-docs-microsoft.poolparty.biz/devrel/92b2ad1c-e9f4-4efc-9995-033db4d8e4a1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/e026b98e-678e-4406-bc80-b3daea608acc
- https://authoring-docs-microsoft.poolparty.biz/devrel/deb7f546-d791-43c4-a74b-a8b1bcca9da4
platformId: cec42a3d-1c8f-fe2e-0684-4358af768f64
---

# Msv4 Medium Memory size series - Azure Virtual Machines | Microsoft Learn

The memory-and-storage-optimized Msv4 Medium Memory VM series are based on the 6th generation Intel® Xeon® Scalable processors and deliver higher remote disk storage performance. These new VM sizes offer up to 4 TB of RAM and up to 225,000 IOPS and 5.5 GBps throughput to remote disk storage with NVMe interface by using Ultra Disk and Premium SSD v2, and provide 50% networking performance improvements over previous generations.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 16 - 256 vCPUs | Intel Xeon 6th gen Scalable (Granite Rapids) [x86-64] |
| Memory | 256 - 3892 GiB |  |
| Local Storage | None |  |
| Remote Storage | 64 Disks | 20,000 - 225,000 IOPS 4000 - 5,500 MBps |
| Network | 8 NICs | 4,500 - 50,000 Mbps Interfaces: NetVSC, MANA |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series (NVMe)

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_M16ls\_v4 | 16 | 256 |
| Standard\_M32ls\_v4 | 32 | 512 |
| Standard\_M48ls\_v4 | 48 | 768 |
| Standard\_M64ls\_v4 | 64 | 1024 |
| Standard\_M96ls\_v4 | 96 | 1536 |
| Standard\_M128ls\_v4 | 128 | 1944 |
| Standard\_M192ls\_v4 | 192 | 3072 |
| Standard\_M256ls\_v4 | 256 | 3892 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage information for each size:

Note

This series doesn't have local storage.

For frequently asked questions, see [Azure VM sizes with no local temp disk](../../azure-vms-no-temp-disk).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage information for each size:

| Size Name | Max Remote Storage Disks (Qty.) | Max Uncached Premium SSD IOPS | Max Uncached Ultra Disk and Premium SSD v2 IOPS | Max Uncached Premium SSD Throughput (MB/s) | Max Uncached Ultra Disk and Premium SSD v2 Throughput (MB/s) |
| --- | --- | --- | --- | --- | --- |
| Standard\_M16ls\_v4 | 64 | 20,000 | 20,000 | 400 | 400 |
| Standard\_M32ls\_v4 | 64 | 40,000 | 40,000 | 800 | 800 |
| Standard\_M48ls\_v4 | 64 | 65,000 | 65,000 | 1,600 | 1,600 |
| Standard\_M64ls\_v4 | 64 | 80,000 | 80,000 | 1,600 | 1,600 |
| Standard\_M96ls\_v4 | 64 | 120,000 | 120,000 | 3,200 | 3,200 |
| Standard\_M128ls\_v4 | 64 | 160,000 | 160,000 | 4,000 | 4,000 |
| Standard\_M192ls\_v4 | 64 | 200,000 | 200,000 | 4,750 | 4,750 |
| Standard\_M256ls\_v4 | 64 | 225,000 | 225,000 | 5,500 | 5,500 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3), remember that capacity numbers given in GiB might appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- IOPS and MBps listed here refer to uncached mode for data disks.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](/en-us/azure/virtual-machines/disks-performance).
- IOPS spec is defined using common small random block sizes like 4KiB or 8KiB. Maximum IOPS is defined as "up-to" and measured using 4KiB random reads workloads.
- TPUT spec is defined using common large sequential block sizes like 128KiB or 1024KiB. Maximum TPUT is defined as "up-to" and measured using 128KiB sequential reads workloads.

# [Network](#tab/sizenetwork)
Network interface information for each size:

| Size Name | Max NICs (Qty.) | Max Network Bandwidth (Mb/s) |
| --- | --- | --- |
| Standard\_M16ls\_v4 | 8 | 4,500 |
| Standard\_M32ls\_v4 | 8 | 8,000 |
| Standard\_M48ls\_v4 | 8 | 16,000 |
| Standard\_M64ls\_v4 | 8 | 16,000 |
| Standard\_M96ls\_v4 | 8 | 30,000 |
| Standard\_M128ls\_v4 | 8 | 30,000 |
| Standard\_M192ls\_v4 | 8 | 50,000 |
| Standard\_M256ls\_v4 | 8 | 50,000 |

#### Networking resources

- [Virtual networks and virtual machines in Azure](/en-us/azure/virtual-network/network-overview)
- [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)

#### Table definitions

- Expected network bandwidth is the maximum aggregated bandwidth allocated per VM type across all NICs, for all destinations. For more information, see [Virtual machine network bandwidth](/en-us/articles/virtual-network/virtual-machine-network-throughput).
- Upper limits aren't guaranteed. Limits offer guidance for selecting the right VM type for the intended application. Actual network performance will depend on several factors including network congestion, application loads, and network settings. For information on optimizing network throughput, see [Optimize network throughput for Azure virtual machines](/en-us/articles/virtual-network/virtual-network-optimize-network-bandwidth).
- To achieve the expected network performance on Linux or Windows, you might need to select a specific version or optimize your VM. For more information, see [Bandwidth/Throughput testing (NTTTCP)](/en-us/support/azure/virtual-network/virtual-network-bandwidth-testing).

# [Accelerators](#tab/sizeaccelerators)
Accelerator (GPUs, FPGAs, etc.) info for each size

Note

This series doesn't include any accelerators.

---

## Feature support

| Feature name | Support status |
| --- | --- |
| [Premium Storage](../../premium-storage-performance) | Supported |
| [Premium Storage caching](../../premium-storage-performance) | Supported |
| [Live Migration](../../maintenance-and-updates) | Limited Support |
| [Memory Preserving Updates](../../maintenance-and-updates) | Not Supported |
| [Generation 2 VMs](../../generation-2) | Supported |
| [Generation 1 VMs](../../generation-2) | Not Supported |
| [Accelerated Networking](/en-us/azure/virtual-network/create-virtual-machine-accelerated-networking) | Supported |
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Not Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Not Supported |
| [Hibernation](../../hibernate-resume) | Not Supported |
| [Write Accelerator](/en-us/azure/virtual-machines/how-to-enable-write-accelerator) | Not Supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)