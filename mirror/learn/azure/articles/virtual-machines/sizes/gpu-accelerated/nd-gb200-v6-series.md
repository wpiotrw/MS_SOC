---
layout: Conceptual
title: ND GB200-v6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nd-gb200-v6-series
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
description: Information on and specifications of the ND GB200-v6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2025-03-20T00:00:00.0000000Z
locale: en-us
document_id: b0d94f7c-5b8f-96ee-cccb-6e9294555926
document_version_independent_id: 2d3ed778-a830-fb81-67a3-f824d5e9d52b
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/gpu-accelerated/nd-gb200-v6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/gpu-accelerated/nd-gb200-v6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/gpu-accelerated/nd-gb200-v6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/92b2ad1c-e9f4-4efc-9995-033db4d8e4a1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/deb7f546-d791-43c4-a74b-a8b1bcca9da4
platformId: 2146824e-9246-a567-9dcb-656725cae1f8
---

# ND GB200-v6 size series - Azure Virtual Machines | Microsoft Learn

The ND-GB200-v6 series virtual machine (VM) is a flagship addition to the Azure GPU family, delivering unmatched performance for Deep Learning training, Generative AI, and HPC workloads. These VMs leverage the NVIDIA GB200 Tensor Core GPUs, built on the Blackwell architecture, which offer significant advancements in computational power, memory bandwidth, and scalability over previous generations. Each ND-GB200-v6 VM is powered by two NVIDIA Grace CPUs and four NVIDIA Blackwell GPUs. The GPUs are interconnected via fifth-generation NVLink, providing a total of 4× 1.8 TB/s NVLink bandwidth per VM. This robust scale-up interconnect enables seamless, high-speed communication between GPUs within the VM. In addition, the VM offers a scale-out backend network with 4× 400 GB/s NVIDIA Quantum-2 CX7 InfiniBand connections per VM, ensuring high-throughput and low-latency communication when interconnecting multiple VMs. NVIDIA GB200 NVL72 connects up to 72 GPUs per rack, enabling system to operate as a single computer. This 72 GPU rack scale system comprised of groups of 18 ND GB200 v6 VMs delivering up to 1.4 Exa-FLOPS of FP4 Tensor Core throughput, 13.5 TB of shared high bandwidth memory, 130TB/s of cross sectional NVLINK bandwidth, and 28.8Tb/s scale-out networking.

With 128 vCPUs per VM supporting the overall system, the architecture is optimized to efficiently distribute workloads and memory demands for AI and scientific applications. This design enables seamless multi-GPU scaling and robust handling of large-scale models. These instances deliver best-in-class performance for AI, ML, and analytics workloads with out-of-the-box support for frameworks like TensorFlow, PyTorch, JAX, RAPIDS, and more. The scale-out InfiniBand interconnect is optimized for existing AI and HPC tools built on NVIDIA’s NCCL communication libraries, ensuring efficient distributed computing across large clusters.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 128 vCPUs | Nvidia Grace CPU |
| Memory | 900 GiB | LPDDR5X |
| Local Storage | 4 Disks | 16 TiB (NVMe) |
| Remote Storage | 16 Disks | 80,000 IOPS 1,200 MBps |
| Network | 1 NICs | 160 Gbps Ethernet |
| Accelerators | 4 GPUs | Nvidia Blackwell GPU (192 GiB) |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_ND128isr\_NDR\_GB200\_v6 | 128 | 900 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

| Size Name | Temp Storage Disks (Qty.) | Temp Disk Size (TB) |
| --- | --- | --- |
| Standard\_ND128isr\_NDR\_GB200\_v6 | 4 | 16 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- Temp disk performance depends on many factors including block size, workload patterns of read/writes, queue depth (QD), and others. Temp disk performance specifications should be viewed as best case performance numbers, assuming 4k block sizes and QD=256 for IOPS, and 256k block sizes with QD=64 for throughput. Additionally, temp disk performance often differs between read and write operations. During steady state operations, write performance is expected to be lower than read performance.
- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Remote storage](#tab/sizestorageremote)
Remote (uncached) storage info for each size

| Size Name | Max Remote Storage Disks (Qty.) | Uncached Disk IOPS | Uncached Disk Speed (MBps) |
| --- | --- | --- | --- |
| Standard\_ND128isr\_NDR\_GB200\_v6 | 316 | 80,000 | 1,200 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- Some sizes support [bursting](../../disk-bursting) to temporarily increase disk performance. Burst speeds can be maintained for up to 30 minutes at a time.
- Special Storage refers to either [Ultra Disk](../../disks-enable-ultra-ssd) or [Premium SSD v2](../../disks-deploy-premium-v2) storage.
- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly or ReadWrite. For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Network](#tab/sizenetwork)
Network interface info for each size

| Size Name | Max Front-end NICs (Qty.) | Max Front-end Bandwidth (Mbps) | Max Scale-up NICS (Qty.) | Max Scale-Up Bandwidth (Gbps) | Max Scale-out NICS (Qty.) | Max Scale-Out Bandwidth (TBps) |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_ND128isr\_NDR\_GB200\_v6 | 1 | 160 | 4 | 400 | 4 | 1.8 |

#### Networking resources

- [Virtual networks and virtual machines in Azure](/en-us/azure/virtual-network/network-overview)
- [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)

#### Table definitions

- Bandwidth is per NIC to up to 100,000 GPUs through InfiniBand
- Bandwidth is up to 72 GPUs per domain through NVLINK
- Expected network bandwidth is the maximum aggregated bandwidth allocated per VM type across all NICs, for all destinations. For more information, see [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput)
- Upper limits aren't guaranteed. Limits offer guidance for selecting the right VM type for the intended application. Actual network performance will depend on several factors including network congestion, application loads, and network settings. For information on optimizing network throughput, see [Optimize network throughput for Azure virtual machines](/en-us/azure/virtual-network/virtual-network-optimize-network-bandwidth).
- To achieve the expected network performance on Linux or Windows, you may need to select a specific version or optimize your VM. For more information, see [Bandwidth/Throughput testing (NTTTCP)](/en-us/azure/virtual-network/virtual-network-bandwidth-testing).

# [Accelerators](#tab/sizeaccelerators)
Accelerator (GPUs, FPGAs, etc.) info for each size

| Size Name | Accelerators (Qty.) | Accelerator-Memory (GB) |
| --- | --- | --- |
| Standard\_ND128isr\_NDR\_GB200\_v6 | 4 | 192 |

---

## Feature support

| Feature name | Support status |
| --- | --- |
| [Premium Storage](../../premium-storage-performance) | Supported |
| [Premium Storage caching](../../premium-storage-performance) | Supported |
| [Live Migration](../../maintenance-and-updates) | Not Supported |
| [Memory Preserving Updates](../../maintenance-and-updates) | Not Supported |
| [Generation 2 VMs](../../generation-2) | Supported |
| [Generation 1 VMs](../../generation-2) | Not Supported |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Supported |
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Not Supported |
| Service Healing | Not Supported |

## Other size information

List of all available sizes: [Sizes](../../sizes)

Pricing Calculator: [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

Information on Disk Types: [Disk Types](../../disks-types)