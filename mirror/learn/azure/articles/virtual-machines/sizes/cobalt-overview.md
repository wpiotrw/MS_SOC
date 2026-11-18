---
layout: Conceptual
title: Azure Cobalt processor-based Virtual Machines - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview
breadcrumb_path: ../../breadcrumb/azure-compute/toc.json
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
ms.reviewer: mattmcinnes
ms.author: noahwood
ms.update-cycle: 1095-days
ms.subservice: sizes
description: An overview of Azure Cobalt processor-based Virtual Machines.
ms.service: azure-virtual-machines
ms.topic: concept-article
ms.workload: infrastructure-services
ms.date: 2026-11-09T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 8d00ada3-a0bb-a9ab-aaa1-9bbd4de6e06e
document_version_independent_id: 8d47b0ea-d8e6-cefa-37c5-b33536bcb16b
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/cobalt-overview.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/sizes/cobalt-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/cobalt-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 98d23ef0-34b5-87b2-6f2e-44765c70574d
---

# Azure Cobalt processor-based Virtual Machines - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

Azure Cobalt processor-based virtual machines (VMs) use Microsoft's custom-designed Arm64 processors for cloud-native workloads. The portfolio includes Cobalt 200-based and Cobalt 100-based VM series, with options for general-purpose, memory-optimized, and storage-optimized workloads.

## Azure Cobalt processors

### Cobalt 200

Cobalt 200-based Virtual Machines (VMs) are powered by Azure's second-generation Cobalt 200 processor. They build on Cobalt 100's strengths and deliver up to 50% higher CPU performance for a wide range of scale-out and cloud-native workloads, including data analytics, web and application servers, open-source databases, caches, and microservices. Cobalt 200 VMs also deliver outstanding performance for agentic AI workloads, such as agent runtimes, sandboxes, tool execution, retrieval, and orchestration.

The Cobalt 200 processor is based on Arm's Neoverse V3 core and offers a full physical core per vCPU. Cobalt 200 supports [Processor Mode](../vm-processor-mode), with frequencies up to 3.6 GHz in Opportunistic mode and 3.2 GHz in Deterministic mode.

Cobalt 200 also expands the Cobalt portfolio beyond general purpose and memory optimized VMs. It brings Cobalt to storage optimized L-series VMs (Lpsv5) for workloads like NoSQL databases, big data analytics, and search and indexing engines. It also brings Cobalt to high-memory M-series VMs (Mpsv4) for workloads like large in-memory databases and ERP systems.

### Cobalt 100

Cobalt 100-based Virtual Machines (VMs) are powered by Azure's first-generation Cobalt 100 processor. These VMs offer an attractive option for a wide range of scale-out and cloud-native Linux-based workloads, including data analytics, web and application servers, open-source databases, caches, and more. These VMs utilize Microsoft's first 64-bit Arm-based CPU, which was fully designed by Microsoft. The Cobalt 100 processor, based on the Arm's Neoverse N2 design, aims to enhance performance and power efficiency for broad range of workloads. Operating at 3.4 GHz, the Azure Cobalt 100 processor provides an entire physical core for each virtual machine vCPU.

## List of VM series by family

The following section lists the VM series powered by Cobalt 200 and Cobalt 100 processors. To find detailed information on a series, including specifications and recommended workloads, check out the links in the *Series* column.

### Cobalt 200-based VMs

| Family | Memory Ratio | Series |
| --- | --- | --- |
| General purpose - D family | 2 GiB: 1 vCPU | [Dplsv7-series](general-purpose/dplsv7-series), [Dpldsv7-series](general-purpose/dpldsv7-series) |
| General purpose - D family | 4 GiB: 1 vCPU | [Dpsv7-series](general-purpose/dpsv7-series), [Dpdsv7-series](general-purpose/dpdsv7-series) |
| Memory optimized - E family | 8 GiB: 1 vCPU | [Epsv7-series](memory-optimized/epsv7-series), [Epdsv7-series](memory-optimized/epdsv7-series) |
| Memory optimized - M family | 16 GiB: 1 vCPU | [Mpsv4-series](memory-optimized/mpsv4-series), [Mpdsv4-series](memory-optimized/mpdsv4-series) |
| Storage optimized - L family | 8 GiB: 1 vCPU | [Lpsv5-series](storage-optimized/lpsv5-series) |

### Cobalt 100-based VMs

| Family | Memory Ratio | Series |
| --- | --- | --- |
| General Purpose | 2 GiB: 1 vCPU | [Dplsv6-series](general-purpose/dplsv6-series), [Dpldsv6-series](general-purpose/dpldsv6-series) |
| General Purpose | 4 GiB: 1 vCPU | [Dpsv6-series](general-purpose/dpsv6-series), [Dpdsv6-series](general-purpose/dpdsv6-series) |
| Memory Optimized | 8 GiB: 1 vCPU | [Epsv6-series](memory-optimized/epsv6-series), [Epdsv6-series](memory-optimized/epdsv6-series) |

To learn how to deploy these VMs for cloud-native applications on AKS, check out [Azure Kubernetes Service (AKS) demo on Cobalt 100 VMs](https://aka.ms/C100-VM-deploy-demo).

To find the most up-to-date regional availability, visit the Virtual Machines section at the bottom of the [Product Availability by Region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table) page.

## Guest OS Support for Cobalt 100 VMs

The following section lists the Guest OS support for Cobalt 100 VMs.

### Guest OS Support

| Guest OS | Version |
| --- | --- |
| AlmaLinux | 8+ |
| Azure Linux | 3 |
| Debian | 11+ |
| Flatcar | N/A |
| Kali Linux | N/A |
| QNX Neutrino RTOS | 7.1 |
| Red Hat Enterprise Linux (RHEL) | 8.6+ |
| SUSE Linux Enterprise Server (SLES) | 15 SP4+ |
| Ubuntu | 20.04+ |
| Windows 11 Client | N/A |

To find the most up-to-date Guest OS support, visit [Azure portal](https://portal.azure.com/#create/Microsoft.VirtualMachine). Under "Instance Details," select "See all images," then click the "Image Type" filter to select "Arm64."