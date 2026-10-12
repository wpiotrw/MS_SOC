---
layout: Conceptual
title: ND GB300-v6 size series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nd-gb300-v6-series
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
description: Information on and specifications of the ND GB300-v6-series sizes
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-08-12T00:00:00.0000000Z
locale: en-us
document_id: f3354b38-b0fa-e29f-3ca7-60c73ee56b3b
document_version_independent_id: 1b5118b6-4623-2146-e927-01dd664321cc
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/gpu-accelerated/nd-gb300-v6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/gpu-accelerated/nd-gb300-v6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/gpu-accelerated/nd-gb300-v6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/92b2ad1c-e9f4-4efc-9995-033db4d8e4a1
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/deb7f546-d791-43c4-a74b-a8b1bcca9da4
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: b2304b6f-f86b-51c8-fcee-a5106401fe57
---

# ND GB300-v6 size series - Azure Virtual Machines | Microsoft Learn

The NDGB300v6 series is Azure’s next-generation GPU VM line purpose-built for large-scale AI, especially high-throughput inference for reasoning and agentic systems. These VMs are powered by NVIDIA GB300 NVL72 rackscale systems (Blackwell Ultra GPUs + Grace CPUs). Each ND-GB300-v6 VM has two NVIDIA Grace CPUs and four NVIDIA Blackwell B300 GPUs. The GPUs are interconnected via fifth-generation NVLINK, providing a total of 4× 1.8 TB/s NVLINK bandwidth per VM. Each GPU also has 800 Gbps InfiniBand connectivity, enabling cluster-scale performance with low latency. There are 18 VMs per rack, so effectively 72 NVIDIA Blackwell Ultra GPUs with 36 NVIDIA Grace CPUs, exposing ~37 TB of fast memory (~20TB High Bandwidth Memory, ~17TB of CPU Memory), 130 TB/s of intrarack NVLink bandwidth.

At rack scale, ND GB300 v6 delivers up to 1.44 exaFLOPS FP4 Tensor Core performance per NVL72 domain and has demonstrated ~1.1 million tokens/second LLM inference throughput per rack, which is ~27% higher than ND GB200 v6. See here for more details. Compared to GB200, GB300 provides ~1.5× FP4 compute, 50% higher HBM capacity (288 GB HBM3E per GPU vs. 192 GB), and 2x the back-end network bandwidth per GPU (800Gbps vs 400 Gbps).

The ND GB300 v6 architecture builds on the ND v6 GB200 to efficiently distribute workloads and memory demands across multiple GPUs, driving markedly higher inference throughput for long context and multimodal workloads AI and scientific applications. These instances deliver best-in-class performance for AI, ML, and analytics workloads with out-of-the-box support for frameworks like PyTorch, Tensorflow, JAX, RAPIDS, and more.

## Host specifications

| Part | Quantity^Count Units^ | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 128 vCPUs | Nvidia Grace CPU |
| Memory | 864 GiB | LPDDR5X |
| Local Storage | 4 Disks | 16 TiB (NVMe) |
| Remote Storage | 16 Disks | 80,000 IOPS 1,200 MBps |
| Network | 1 NICs | 160 Gbps Ethernet |
| Accelerators | 4 GPUs | Nvidia Blackwell Ultra GPU (288GB) |

For features supported by this series, see the Feature support section.

## Sizes in series

# [Basics](#tab/sizebasic)
vCPUs (Qty.) and Memory for each size

| Size Name | vCPUs (Qty.) | Memory (GiB) |
| --- | --- | --- |
| Standard\_ND128isr\_GB300\_v6 | 128 | 864 |
| Standard\_ND128isrG5\_GB300\_v6 | 128 | 864 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local storage](#tab/sizestoragelocal)
Local (temp) storage info for each size

| Size Name | Temp Storage Disks (Qty.) | Temp Disk Size (TB) |
| --- | --- | --- |
| Standard\_ND128isr\_GB300\_v6 | 4 | 16 |
| Standard\_ND128isrG5\_GB300\_v6 | 4 | 16 |

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
| Standard\_ND128isr\_GB300\_v6 | 16 | 80,000 | 1,200 |
| Standard\_ND128isrG5\_GB300\_v6 | 16 | 80,000 | 1,200 |

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

| Size Name | Max Front-end NICs (Qty.) | Max Front-end Bandwidth (Mbps) | Max Scale-up NICS (Qty.) | Max Scale-Up Bandwidth (TBps) | Max Scale-out NICS (Qty.) | Max Scale-Out Bandwidth (Gbps) |
| --- | --- | --- | --- | --- | --- | --- |
| Standard\_ND128isr\_GB300\_v6 | 1 | 160 | 4 | 1.8 | 4 | 4x800 |
| Standard\_ND128isrG5\_GB300\_v6 | 1 | 160 | 4 | 1.8 | 4 | 4x800 |

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
| Standard\_ND128isr\_GB300\_v6 | 4 | 288 |
| Standard\_ND128isrG5\_GB300\_v6 | 4 | 288 |

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