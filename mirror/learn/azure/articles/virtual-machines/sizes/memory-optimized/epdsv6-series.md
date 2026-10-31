---
layout: Conceptual
title: Epdsv6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/epdsv6-series
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
ms.reviewer: mattmcinnes, tomcassidy
ms.author: noahwood
ms.update-cycle: 1095-days
description: Information on and specifications of the Epdsv6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.custom:
- build-2024
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: 9d856977-0926-3486-21fc-43d14092c5d0
document_version_independent_id: 594a6e95-aa5c-413b-9fb8-0fa3433a3f67
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/epdsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/epdsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/epdsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 3b262505-f5ea-88e5-fc19-98ab4462fd9b
---

# Epdsv6 size series - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows Client VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

The Epdsv6-series virtual machines are powered by Azure’s first-generation Cobalt 100 processor, delivering outstanding performance for memory optimized workloads. The Azure Cobalt 100 processor operates at 3.4 GHz and provides an entire physical core for each virtual machine vCPU. These virtual machines offer 8 GiB of memory per vCPU and a wide range of vCPU sizes. These VMs are best suited for memory-intensive scale-out and enterprise workloads, such as relational database servers, large databases, data analytics engines, in-memory caches, and more. Epdsv6-series virtual machines support Standard SSD, Standard HDD, and Premium SSD types. You can also attach Ultra Disk storage based on its regional availability. Disk storage is billed separately from virtual machines. For more information, [see pricing for disks](https://azure.microsoft.com/pricing/details/managed-disks/). Epdsv6-series virtual machines offer up to 96 vCPU, up to 672 GiB of RAM, and up to 5,280 GiB of fast local NVMe temporary storage.

## Host specifications

| Part | QuantityCount Units | SpecsSKU ID, Performance Units, etc. |
| --- | --- | --- |
| Processor | 2 - 96 vCores | Azure Cobalt 100 [ARM-64] |
| Memory | 16 - 672 GiB |  |
| Local Storage | 1 - 6 Disks | 110 - 880 GiB/Disk 15000 - 1800000 IOPS  90 - 8640 MBps |
| Remote Storage [Premium SSD](../../disks-types#premium-ssds) | 8 - 64 Disks | 3750 - 153600 IOPS 106 - 5000 MBps |
| Remote Storage [Premium SSD v2](../../disks-types#premium-ssd-v2) / [Ultra Disks](../../disks-types#ultra-disks) | 8 - 64 Disks | 4163 - 199987 IOPS 124 - 5850 MBps |
| Network | 2 - 8 NICs | 12500 - 60000 Mbps Interfaces: NetVSC, ConnectX, [MANA](https://aka.ms/ManaFAQ1) |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_E2pds\_v6 | 2 | 16 |
| Standard\_E4pds\_v6 | 4 | 32 |
| Standard\_E8pds\_v6 | 8 | 64 |
| Standard\_E16pds\_v6 | 16 | 128 |
| Standard\_E32pds\_v6 | 32 | 256 |
| Standard\_E48pds\_v6 | 48 | 384 |
| Standard\_E64pds\_v6 | 64 | 512 |
| Standard\_E96pds\_v6 | 96 | 672 |

Note

The Epdsv6 VM series will only work on OS images that support NVMe (i.e. NVMe drivers required for the local storage). If your current OS image doesn't have NVMe support, you’ll see an error message. NVMe support is available on the most popular OS images, and we're continuously improving OS image compatibility.

#### VM Basics resources

- [What are vCPUs (Qty.)](../../managed-disks-overview)
- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

| Size Name | Max Temp Storage Disks (Qty.) | Temp Disk Size (GiB)^1^ | Temp Disk Random Read (RR)^2^IOPS^3^ | Temp Disk Random Read (RR)^2^Throughput (MB/s)^3^ | Temp Disk Random Write (RW)^2^IOPS^3^ | Temp Disk Random Write (RW)^2^Throughput (MB/s)^3^ |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2pds\_v6 | 1 | 110 | 37500 | 90 | 15000 | 180 |
| Standard\_E4pds\_v6 | 1 | 220 | 75000 | 180 | 30000 | 360 |
| Standard\_E8pds\_v6 | 1 | 440 | 150000 | 360 | 60000 | 720 |
| Standard\_E16pds\_v6 | 2 | 440 | 300000 | 720 | 120000 | 1440 |
| Standard\_E32pds\_v6 | 4 | 440 | 600000 | 1440 | 240000 | 2880 |
| Standard\_E48pds\_v6 | 6 | 440 | 900000 | 2160 | 360000 | 4320 |
| Standard\_E64pds\_v6 | 4 | 880 | 1200000 | 2880 | 480000 | 5760 |
| Standard\_E96pds\_v6 | 6 | 880 | 1800000 | 4320 | 720000 | 8640 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- ^1^ Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1023 GiB = 1098.4 GB.
- ^2^ Temp disk speed often differs between RR (Random Read) and RW (Random Write) operations. RR operations are typically faster than RW operations. The RW speed is usually slower than the RR speed on series where only the RR speed value is listed.
- ^3^ The IOPS and throughput values shown are the combined performance across all temp disks.
- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly (R-O) or ReadWrite (R-W). For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage (Qty.) | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MB/s) | Uncached Premium SSD Burst^1^IOPS | Uncached Premium SSD Burst^1^Throughput (MB/s) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MB/s) | Uncached Burst^1^Ultra Disk and Premium SSD v2 IOPS | Uncached Burst^1^Ultra Disk and Premium SSD v2 Throughput (MB/s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2pds\_v6 | 8 | 3750 | 106 | 10000 | 1250 | 4163 | 124 | 11100 | 1463 |
| Standard\_E4pds\_v6 | 12 | 6400 | 212 | 20000 | 1250 | 8333 | 248 | 26040 | 1463 |
| Standard\_E8pds\_v6 | 24 | 12800 | 424 | 20000 | 1250 | 16666 | 496 | 26040 | 1463 |
| Standard\_E16pds\_v6 | 48 | 25600 | 848 | 40000 | 1250 | 33331 | 992 | 52080 | 1463 |
| Standard\_E32pds\_v6 | 64 | 51200 | 1696 | 80000 | 2000 | 66662 | 1984 | 104160 | 2340 |
| Standard\_E48pds\_v6 | 64 | 76800 | 2544 | 80000 | 3000 | 99994 | 2976 | 104160 | 3510 |
| Standard\_E64pds\_v6 | 64 | 102400 | 3392 | 102400 | 3392 | 133325 | 3969 | 133325 | 3969 |
| Standard\_E96pds\_v6 | 64 | 153600 | 5000 | 153600 | 5000 | 199987 | 5850 | 199987 | 5850 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- ^1^These sizes support [bursting](../../disk-bursting) to temporarily increase disk performance. Burst speeds can be maintained for up to 30 minutes at a time.
- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly or ReadWrite. For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Network](#tab/sizenetwork)
Network interface info for each size

| Size Name | Max NICs (Qty.) | Max Network Bandwidth (Mb/s) |
| --- | --- | --- |
| Standard\_E2pds\_v6 | 2 | 12500 |
| Standard\_E4pds\_v6 | 2 | 12500 |
| Standard\_E8pds\_v6 | 4 | 15000 |
| Standard\_E16pds\_v6 | 8 | 15000 |
| Standard\_E32pds\_v6 | 8 | 20000 |
| Standard\_E48pds\_v6 | 8 | 30000 |
| Standard\_E64pds\_v6 | 8 | 40000 |
| Standard\_E96pds\_v6 | 8 | 60000 |

#### Networking resources

- [Virtual networks and virtual machines in Azure](/en-us/azure/virtual-network/network-overview)
- [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)

Note

Accelerated networking is required and turned on by default on all Epdsv6 machines.

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
| [Memory Preserving Updates](../../maintenance-and-updates#live-migration) | Supported |
| [VM Generation Support](../../generation-2) | Generation 2 |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Required |
| [Ephemeral OS Disks](../../ephemeral-os-disks) | Supported |
| [Temporary local NVMe disks](../../enable-nvme-temp-faqs) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Not Supported |
| [Azure Disk Encryption for Linux VMs](../../linux/disk-encryption-linux?tabs=azcliazure,enableadecli,efacli,adedatacli#restrictions) | Not Supported |
| [Azure Disk Encryption for Windows VMs](../../windows/disk-encryption-windows#restrictions) | Not Supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)