---
layout: Conceptual
title: ECedsv6-series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/ecedsv6-series
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
author: michamcr
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mmcrey
ms.author: mmcrey
ms.update-cycle: 1095-days
description: Specifications for Azure Confidential Computing's ECedsv6-series confidential virtual machines.
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.custom:
- ignite-2023
ms.topic: concept-article
ms.date: 2026-02-15T00:00:00.0000000Z
locale: en-us
document_id: 3e0e5537-03e9-f7cb-5c13-6a6f2a8d595c
document_version_independent_id: 18bf4fe9-1ae3-f351-1161-9b68be33b8d7
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/ecedsv6-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/ecedsv6-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/ecedsv6-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/92b2ad1c-e9f4-4efc-9995-033db4d8e4a1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/deb7f546-d791-43c4-a74b-a8b1bcca9da4
platformId: 92b49b16-f32a-983d-2073-157a9aac9122
---

# ECedsv6-series - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs

The ECedsv6-series are [Azure confidential VMs](/en-us/azure/confidential-computing/confidential-vm-overview) that help protect the confidentiality and integrity of code and data while it's being processed. Organizations can use these VMs to seamlessly bring confidential workloads to the cloud without any code changes to the application. These machines are powered by Intel® 5th Generation Xeon® Scalable processors reaching an all-core turbo clock speed of 3.0 GHz and [Intel® AMX](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html) for AI acceleration.

By using [Intel® Trust Domain Extensions (TDX)](https://www.intel.com/content/www/us/en/developer/tools/trust-domain-extensions/overview.html), these VMs are hardened from the cloud virtualized environment by denying the hypervisor, other host management code, and administrators access to the VM memory and state. It helps to protect VMs against a broad range of sophisticated [hardware and software attacks](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-trust-domain-extensions.html).

The ECedsv6 offer a balance of memory to vCPU performance that's suitable most production workloads. This series is designed for memory-intensive applications, large relational database servers, business intelligence applications, and critical applications that process sensitive and regulated data.

## Host specifications

| Part | Quantity min - max | Specs^SKU ID, Performance Units, etc.^ |
| --- | --- | --- |
| Processor | 2 - 64 vCPUs | Intel Xeon Platinum 8573C (Emerald Rapids) [x86-64] |
| Memory | 16 - 512 GiB |  |
| Local Storage | 110 - 3,520 GiB | Temp SSD |
| Remote Storage | 8 - 64 Disks | 3,750 - 102,400 IOPS 106 - 3,392 MBps |
| Network | 2 - 8 NICs | 7,000 - 25,000 Mbps |
| Accelerators | None |  |

## Sizes in series

# [Basics](#tab/sizebasic)
This table shows the number of vCPUs and amount of memory for each ECedsv6-series size.

| Size Name | vCPUs | Memory (GiB) |
| --- | --- | --- |
| Standard\_EC2eds\_v6 | 2 | 16 |
| Standard\_EC4eds\_v6 | 4 | 32 |
| Standard\_EC8eds\_v6 | 8 | 64 |
| Standard\_EC16eds\_v6 | 16 | 128 |
| Standard\_EC32eds\_v6 | 32 | 256 |
| Standard\_EC48eds\_v6 | 48 | 384 |
| Standard\_EC64eds\_v6 | 64 | 512 |

#### VM Basics resources

- [Check vCPU quotas](../../quotas)

# [Local storage](#tab/sizestoragelocal)
Each size offers local (temp) storage. Disk size is per disk, while IOPS and bandwidth limits are aggregate across all temp disks.

| Size Name | Temp Storage Disks | Size per Temp Disk (GiB) | Aggregate Temp Disk Random Read IOPS | Aggregate Temp Disk Bandwidth Limit (MiB/s) |
| --- | --- | --- | --- | --- |
| Standard\_EC2eds\_v6 | 1 | 110 | 37,500 | 280 |
| Standard\_EC4eds\_v6 | 1 | 220 | 75,000 | 560 |
| Standard\_EC8eds\_v6 | 1 | 440 | 150,000 | 1,120 |
| Standard\_EC16eds\_v6 | 2 | 440 | 300,000 | 2,240 |
| Standard\_EC32eds\_v6 | 4 | 440 | 600,000 | 4,480 |
| Standard\_EC48eds\_v6 | 6 | 440 | 900,000 | 6,720 |
| Standard\_EC64eds\_v6 | 4 | 880 | 1,200,000 | 8,576 |

#### Storage resources

- [Introduction to Azure managed disks](../../managed-disks-overview)
- [Azure managed disk types](../../disks-types)
- [Share an Azure managed disk](../../disks-shared)

#### Table definitions

- Total local temporary storage is calculated by multiplying the max number of storage disks by the temp disk size. For example, for the Standard\_DC128eds\_v6, the total local temporary storage capacity is `4 x 1,760 GiB = 7,040 GiB`.
- Storage capacity is shown in units of GiB or 1,024^3 bytes. When you compare disks measured in GB (1,000^3 bytes) to disks measured in GiB (1,024^3), remember that capacity numbers given in GiB can appear smaller. For example, 1,023 GiB = 1,098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps, where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to ReadOnly or ReadWrite. For uncached data disk operation, the host cache mode is set to None.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).

# [Remote storage](#tab/sizestorageremote)
Remote (uncached) storage available for each size.

| Size Name | Max Remote Storage Disks | Uncached Premium SSD IOPS | Uncached Premium SSD Throughput (MBps) |
| --- | --- | --- | --- |
| Standard\_EC2eds\_v6 | 8 | 3,750 | 106 |
| Standard\_EC4eds\_v6 | 12 | 6,400 | 212 |
| Standard\_EC8eds\_v6 | 24 | 12,800 | 424 |
| Standard\_EC16eds\_v6 | 48 | 25,600 | 848 |
| Standard\_EC32eds\_v6 | 64 | 51,200 | 1,696 |
| Standard\_EC48eds\_v6 | 64 | 76,800 | 2,544 |
| Standard\_EC64eds\_v6 | 64 | 102,400 | 3,392 |

# [Network](#tab/sizenetwork)
Network interface information for each size.

| Size Name | Max NICs | Max Network Bandwidth (Mbps) |
| --- | --- | --- |
| Standard\_EC2eds\_v6 | 2 | 7,000 |
| Standard\_EC4eds\_v6 | 2 | 7,000 |
| Standard\_EC8eds\_v6 | 4 | 7,000 |
| Standard\_EC16eds\_v6 | 8 | 7,000 |
| Standard\_EC32eds\_v6 | 8 | 9,000 |
| Standard\_EC48eds\_v6 | 8 | 12,500 |
| Standard\_EC64eds\_v6 | 8 | 25,000 |

---

Note

Some [pricing differences based on your encryption settings](/en-us/azure/confidential-computing/confidential-vm-overview#encryption-pricing-differences) exist for confidential VMs.

## Feature support

| Feature name | Support status |
| --- | --- |
| [Premium Storage](../../premium-storage-performance) | Supported |
| [Premium Storage caching](../../premium-storage-performance) | Supported |
| [Live Migration](../../maintenance-and-updates) | Coming Soon |
| [Memory Preserving Updates](../../maintenance-and-updates) | Not Supported |
| [Generation 2 VMs](../../generation-2) | Supported |
| [Generation 1 VMs](../../generation-2) | Not Supported |
| [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) | Not Supported |
| [Ephemeral OS Disk](../../ephemeral-os-disks) | Not Supported |
| [Nested Virtualization](/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization) | Not Supported |

## Size table definitions

- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to **ReadOnly** or **ReadWrite**. For uncached data disk operation, the host cache mode is set to **None**.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).
- **Expected network bandwidth** is the maximum aggregated bandwidth allocated per VM type across all NICs, for all destinations. For more information, see [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput).

    Upper limits aren't guaranteed. Limits offer guidance for selecting the right VM type for the intended application. Actual network performance will depend on several factors including network congestion, application loads, and network settings. For information on optimizing network throughput, see [Optimize network throughput for Azure virtual machines](/en-us/azure/virtual-network/virtual-network-optimize-network-bandwidth). To achieve the expected network performance on Linux or Windows, you may need to select a specific version or optimize your VM. For more information, see [Bandwidth/Throughput testing (NTTTCP)](/en-us/azure/virtual-network/virtual-network-bandwidth-testing).