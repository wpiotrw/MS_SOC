---
layout: Conceptual
title: Dadsv6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dadsv6-series
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
description: Information on and specifications of the Dadsv6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-03-10T00:00:00.0000000Z
locale: en-us
document_id: 348803c6-4e7d-16ee-95dd-aa034a56f68b
document_version_independent_id: 366a7832-95bc-76f1-497f-34b05c08799a
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/general-purpose/dadsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/general-purpose/dadsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/general-purpose/dadsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 34d2698e-b0e3-432e-27ae-eaa3392e2a37
---

# Dadsv6 size series - Azure Virtual Machines | Microsoft Learn

Dadsv6-series VMs utilize AMD's 4th Generation EPYC™ 9004 processors that can achieve a boosted maximum frequency of 3.7GHz. These virtual machines offer up to 96 vCPU and 384 GiB of RAM. The Dadsv6-series sizes offer a combination of vCPU, memory and fast local NVMe temporary storage for most production workloads. Dadsv6-series virtual machines support Standard SSD, Standard HDD, and Premium SSD types. You can also attach Ultra Disk storage based on its regional availability. Disk storage is billed separately from virtual machines.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 96 vCPUs | AMD EPYC 9004 (Genoa) [x86-64] |
| Memory | 8 - 384 GiB |  |
| Local Storage | 1 - 6 Disks | 110 - 880 GiB 38,000 - 1,800,000 IOPS 180 - 8,640 MBps |
| Remote Storage | 4 - 32 Disks | 4,000 - 175,000 IOPS 90 - 4,320 MBps Disk Types: [Standard SDD/HDD](../../disks-types#standard-ssds), [Premium SSD](../../disks-types#premium-ssds), [Premium SSD v2](../../disks-types#premium-ssd-v2) |
| Network | 2 - 8 NICs | 12,500 - 40,000 Mbps Interfaces: NetVSC, ConnectX |
| Accelerators | None |  |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_D2ads\_v6 | 2 | 8 |
| Standard\_D4ads\_v6 | 4 | 16 |
| Standard\_D8ads\_v6 | 8 | 32 |
| Standard\_D16ads\_v6 | 16 | 64 |
| Standard\_D32ads\_v6 | 32 | 128 |
| Standard\_D48ads\_v6 | 48 | 192 |
| Standard\_D64ads\_v6 | 64 | 256 |
| Standard\_D96ads\_v6 | 96 | 384 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local Storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

| Size Name | Temp Storage Disks (Qty.) | Temp Disk Size (GiB) | Temp Disk Random Read IOPS | Temp Disk Sequential Read Throughput (MBps) |
| --- | --- | --- | --- | --- |
| Standard\_D2ads\_v6 | 1 | 110 | 37,500 | 180 |
| Standard\_D4ads\_v6 | 1 | 220 | 75,000 | 360 |
| Standard\_D8ads\_v6 | 1 | 440 | 150,000 | 720 |
| Standard\_D16ads\_v6 | 2 | 440 | 300,000 | 1,440 |
| Standard\_D32ads\_v6 | 4 | 440 | 600,000 | 2,880 |
| Standard\_D48ads\_v6 | 6 | 440 | 900,000 | 4,320 |
| Standard\_D64ads\_v6 | 4 | 880 | 1,200,000 | 5,760 |
| Standard\_D96ads\_v6 | 6 | 880 | 1,800,000 | 8,640 |

#### Storage resources

- [NVMe Overview](/en-us/azure/virtual-machines/nvme-overview)
- [FAQ for temp NVMe disks](/en-us/azure/virtual-machines/enable-nvme-temp-faqs)

#### Table definitions

- Total local temporary storage is calculated by multiplying the max number of storage disks with the temp disk size. For example, for the Standard\_D96ads\_v6, the total local temporary storage capacity is `6 x 880 GiB = 5,280 GiB`.
- Temp disk performance depends on many factors including block size, workload patterns of read/writes, queue depth (QD), and others. Temp disk performance specifications should be viewed as best case performance numbers, assuming 4k block sizes and QD=256 for IOPS, and 256k block sizes with QD=64 for throughput. Read performance specs assume 100% reads, and write performance specs assume 100% writes. Additionally, write performance is heavily impacted by how many blocks in use on a device. Temp disk write performance specs assume a device has a clean slate to enable the best performance. During steady state operations, write performance is expected to be lower than the published specs.
- NVMe temp disks are presented as raw NVMe devices that need to be initialized and formatted before use. For more details on how to format and initialize drives, refer to the [NVMe Temp Disk FAQ](/en-us/azure/virtual-machines/enable-nvme-temp-faqs).
- The IOPS and throughput values shown are the combined performance across all temp disks.
- Storage capacity is shown in units of GiB or 1,024^3 bytes. When you compare disks measured in GB (1,000^3 bytes) to disks measured in GiB (1,024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1,023 GiB = 1,098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Remote Storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage Disks (Qty.) | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MBps) | Uncached Premium SSD Burst IOPS | Uncached Premium SSD Burst Throughput (MBps) | Uncached Ultra Disk and Premium SSD v2 IOPS | Uncached Ultra Disk and Premium SSD v2 Throughput (MBps) | Uncached Burst Ultra Disk and Premium SSD v2 IOPS | Uncached Burst Ultra Disk and Premium SSD v2 Throughput (MBps) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_D2ads\_v6 | 4 | 4,000 | 90 | 20,000 | 1,250 | 4,000 | 90 | 20,000 | 1,250 |
| Standard\_D4ads\_v6 | 8 | 7,600 | 180 | 20,000 | 1,250 | 7,600 | 180 | 20,000 | 1,250 |
| Standard\_D8ads\_v6 | 16 | 15,200 | 360 | 20,000 | 1,250 | 15,200 | 360 | 20,000 | 1,250 |
| Standard\_D16ads\_v6 | 32 | 30,400 | 720 | 40,000 | 1,250 | 30,400 | 720 | 40,000 | 1,250 |
| Standard\_D32ads\_v6 | 32 | 57,600 | 1,440 | 80,000 | 1,700 | 57,600 | 1,440 | 80,000 | 1,700 |
| Standard\_D48ads\_v6 | 32 | 86,400 | 2,160 | 90,000 | 2,550 | 86,400 | 2,160 | 90,000 | 2,550 |
| Standard\_D64ads\_v6 | 32 | 115,200 | 2,880 | 120,000 | 3,400 | 115,200 | 2,880 | 120,000 | 3,400 |
| Standard\_D96ads\_v6 | 32 | 175,000 | 4,320 | 175,000 | 5,090 | 175,000 | 4,320 | 175,000 | 5,090 |

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
| Standard\_D2ads\_v6 | 2 | 12,500 |
| Standard\_D4ads\_v6 | 2 | 12,500 |
| Standard\_D8ads\_v6 | 4 | 12,500 |
| Standard\_D16ads\_v6 | 8 | 16,000 |
| Standard\_D32ads\_v6 | 8 | 20,000 |
| Standard\_D48ads\_v6 | 8 | 28,000 |
| Standard\_D64ads\_v6 | 8 | 36,000 |
| Standard\_D96ads\_v6 | 8 | 40,000 |

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
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Supported |
| [Temporary local NVMe disks](../../enable-nvme-temp-faqs) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Supported |
| [Azure Disk Encryption for Linux VMs](../../linux/disk-encryption-linux?tabs=azcliazure,enableadecli,efacli,adedatacli#restrictions) | Not Supported |
| [Azure Disk Encryption for Windows VMs](../../windows/disk-encryption-windows#restrictions) | Not Supported |

Note

This VM series will only work on OS images that support NVMe. If your current OS image doesn't have NVMe support, you'll see an error message. [NVMe](../../enable-nvme-interface) support is available on the most popular OS images, and we're continuously improving OS image compatibility.

Some Azure services refer to this VM family as **Dadv6** rather than **Dadsv6**. This naming inconsistency doesn't affect VM capabilities, including Premium Storage support.

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)