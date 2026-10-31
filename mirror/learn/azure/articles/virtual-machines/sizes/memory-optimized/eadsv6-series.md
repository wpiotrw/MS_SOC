---
layout: Conceptual
title: Eadsv6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/eadsv6-series
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
description: Information on and specifications of the Eadsv6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: d6ac5567-7fb4-ae58-33b4-248e869a39d8
document_version_independent_id: de4d5f8f-ad1c-7fd7-91a9-915d04c72011
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/eadsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/eadsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/eadsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/92b2ad1c-e9f4-4efc-9995-033db4d8e4a1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/deb7f546-d791-43c4-a74b-a8b1bcca9da4
platformId: e28a529d-bbd1-01a7-bfc6-41e94dbd21fc
---

# Eadsv6 size series - Azure Virtual Machines | Microsoft Learn

Eadsv6-series VMs utilize AMD's fourth Generation EPYC™ 9004 processors that can achieve a boosted maximum frequency of 3.7 GHz. These virtual machines offer up to 96 vCPU and 672 GiB of RAM. The Eadsv6-series sizes offer a combination of vCPU, memory, and fast local NVMe temporary storage that is ideal for memory-intensive enterprise applications. Eadsv6-series virtual machines support Standard SSD, Standard HDD, and Premium SSD types. You can also attach Ultra Disk storage based on its regional availability. Disk storage is billed separately from virtual machines.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 96 vCPUs | AMD EPYC 9004 (Genoa) [x86-64] |
| Memory | 16 - 672 GiB |  |
| Local Storage | 1 - 6 Disks | 110 - 880 GiB 37500 - 1800000 IOPS 180 - 8640 MBps |
| Remote Storage [Premium SSD](../../disks-types#premium-ssds) | 4 - 32 Disks | 4000 - 175000 IOPS 90 - 4320 MBps |
| Remote Storage [Premium SSD v2](../../disks-types#premium-ssd-v2) / [Ultra Disks](../../disks-types#ultra-disks) | 4 - 32 Disks | 4000 - 175000 IOPS 90 - 4320 MBps |
| Network | 2 - 8 NICs | 12500 - 40000 Mbps Interfaces: NetVSC, ConnectX |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GB) |
| --- | --- | --- |
| Standard\_E2ads\_v6 | 2 | 16 |
| Standard\_E4ads\_v6 | 4 | 32 |
| Standard\_E8ads\_v6 | 8 | 64 |
| Standard\_E16ads\_v6 | 16 | 128 |
| Standard\_E20ads\_v6 | 20 | 160 |
| Standard\_E32ads\_v6 | 32 | 256 |
| Standard\_E48ads\_v6 | 48 | 384 |
| Standard\_E64ads\_v6 | 64 | 512 |
| Standard\_E96ads\_v6 | 96 | 672 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

| Size Name | Max Temp Storage Disks (Qty.) | Temp Disk Size (GiB) | Temp Disk Random Read (RR)^1^IOPS | Temp Disk Random Read (RR)^1^Throughput (MB/s) |
| --- | --- | --- | --- | --- |
| Standard\_E2ads\_v6 | 1 | 110 | 37500 | 180 |
| Standard\_E4ads\_v6 | 1 | 220 | 75000 | 360 |
| Standard\_E8ads\_v6 | 1 | 440 | 150000 | 720 |
| Standard\_E16ads\_v6 | 2 | 440 | 300000 | 1440 |
| Standard\_E20ads\_v6 | 2 | 550 | 375000 | 1800 |
| Standard\_E32ads\_v6 | 4 | 440 | 600000 | 2880 |
| Standard\_E48ads\_v6 | 6 | 440 | 900000 | 4320 |
| Standard\_E64ads\_v6 | 4 | 880 | 1200000 | 5760 |
| Standard\_E96ads\_v6 | 6 | 880 | 1800000 | 8640 |

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
| Standard\_E2ads\_v6 | 4 | 4000 | 90 | 20000 | 1250 | 4000 | 90 | 20000 | 1250 |
| Standard\_E4ads\_v6 | 8 | 7600 | 180 | 20000 | 1250 | 7600 | 180 | 20000 | 1250 |
| Standard\_E8ads\_v6 | 16 | 15200 | 360 | 20000 | 1250 | 15200 | 360 | 20000 | 1250 |
| Standard\_E16ads\_v6 | 32 | 30400 | 720 | 40000 | 1250 | 30400 | 720 | 40000 | 1250 |
| Standard\_E20ads\_v6 | 32 | 38000 | 900 | 64000 | 1600 | 38000 | 900 | 64000 | 1600 |
| Standard\_E32ads\_v6 | 32 | 57600 | 1440 | 80000 | 1700 | 57600 | 1440 | 80000 | 1700 |
| Standard\_E48ads\_v6 | 32 | 86400 | 2160 | 90000 | 2550 | 86400 | 2160 | 90000 | 2550 |
| Standard\_E64ads\_v6 | 32 | 115200 | 2880 | 120000 | 3400 | 115200 | 2880 | 120000 | 3400 |
| Standard\_E96ads\_v6 | 32 | 175000 | 4320 | 175000 | 5090 | 175000 | 4320 | 175000 | 5090 |

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
| Standard\_E2ads\_v6 | 2 | 12500 |
| Standard\_E4ads\_v6 | 2 | 12500 |
| Standard\_E8ads\_v6 | 4 | 12500 |
| Standard\_E16ads\_v6 | 8 | 16000 |
| Standard\_E20ads\_v6 | 8 | 16000 |
| Standard\_E32ads\_v6 | 8 | 20000 |
| Standard\_E48ads\_v6 | 8 | 28000 |
| Standard\_E64ads\_v6 | 8 | 36000 |
| Standard\_E96ads\_v6 | 8 | 40000 |

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
| [Memory Preserving Updates](../../maintenance-and-updates#live-migration) | Supported |
| [Generation 2 VMs](../../generation-2) | Supported |
| [Generation 1 VMs](../../generation-2) | Not Supported |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Required |
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Supported |
| [Temporary local NVMe disks](../../enable-nvme-temp-faqs) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Supported |
| [Azure Disk Encryption for Linux VMs](../../linux/disk-encryption-linux?tabs=azcliazure,enableadecli,efacli,adedatacli#restrictions) | Not Supported |
| [Azure Disk Encryption for Windows VMs](../../windows/disk-encryption-windows#restrictions) | Not Supported |

Note

This VM series will only work on OS images that support NVMe. If your current OS image doesn't have NVMe support, you’ll see an error message. [NVMe](../../enable-nvme-interface) support is available on the most popular OS images, and we're continuously improving OS image compatibility.

Some Azure services may refer to this VM family as **Eadv6** rather than **Eadsv6**. This is a known naming inconsistency and does not affect VM capabilities, including Premium Storage support.

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)