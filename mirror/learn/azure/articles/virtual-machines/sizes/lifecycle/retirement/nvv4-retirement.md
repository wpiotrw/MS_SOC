---
layout: Conceptual
title: NVv4 series retirement - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/lifecycle/retirement/nvv4-retirement
breadcrumb_path: ../../../../breadcrumb/azure-compute/toc.json
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
author: yangnicole-ml
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: yangnicole
ms.update-cycle: 1095-days
description: 'This article contains the details of the NVv4-series retirement. '
ms.service: azure-virtual-machines
ms.topic: how-to
ms.date: 2025-06-13T00:00:00.0000000Z
locale: en-us
document_id: 472621ce-bde1-edb8-7628-7b159c13611e
document_version_independent_id: 53c38d5f-1f2d-50a9-e35b-b3820965cb45
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/lifecycle/retirement/nvv4-retirement.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../../toc.json
asset_id: virtual-machines/sizes/lifecycle/retirement/nvv4-retirement
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/lifecycle/retirement/nvv4-retirement.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 59bcbc90-6683-11cd-e72f-95c90af695bb
---

# NVv4 series retirement - Azure Virtual Machines | Microsoft Learn

Note

There is a known resize operation error that occurs when migrating from the NVv4-series to the NVads\_V710\_v5-series. To unblock this, register your subscription ID under the Azure Feature Exposure Control (AFEC) ‘VMTempDiskResizePreview’. The AFEC is also discoverable in the portal. Then, confirm the AFEC registration status before resizing the VMs.

Note

1-year and 3-year RI purchases for the NVv4-series ended on November 2, 2025.

Note

All Compute Pre-Purchase (CPP) sales for the NVv4-series ended on June 2, 2026.

On September 30, 2026, Microsoft Azure retired the Standard\_NV4as\_v4, Standard\_NV4ahs\_v4, Standard\_NV8as\_v4, Standard\_NV8ahs\_v4, Standard\_NV16as\_v4, Standard\_NV16ahs\_v4, Standard\_NV32as\_v4, and Standard\_NV32ahs\_v4 virtual machines (VMs) in NVv4-series virtual machines (VMs). To avoid unplanned disruption, customers who were using these VM sizes were required to migrate to supported VM series prior to the retirement date using the migration guidance below.

Microsoft is recommending the Azure [NVads_V710_v5-series](/en-us/azure/virtual-machines/sizes/gpu-accelerated/nvadsv710-v5-series?tabs=sizebasic) VMs, which offer greater GPU memory bandwidth per GPU. The NVads\_V710\_v5-series VMs take advantage of the AMD Simultaneous Multithreading technology to assign dedicated vCPU threads to each VM and support NVMe for ephemeral local storage capability.

The NVads\_V710\_v5-series enables right-sizing for demanding GPU-accelerated graphics applications and cloud-based virtual desktops to provide a seamless end user experience while providing a cost-effective choice for a full range of graphics-enabled virtual desktop experiences. The VMs are also sized to deliver high-quality, interactive gaming experiences in the cloud, optimized for rendering and streaming complex graphics. In addition, the NVads\_V710\_v5-series supports small AI inference workloads such as Small Language Model (SLMs), recommendation systems, and semantic indexing, by taking advantage of the computational IP blocks in the Radeon Pro V710 GPUs.

Depending on the workload being run, regional affinity, and cost preferences, other VMs that may be migrated to from the NVv4-series VMs include [NVadsA10_v5](/en-us/azure/virtual-machines/sizes/gpu-accelerated/nvadsa10v5-series?tabs=sizebasic) and [NGads_V620](/en-us/azure/virtual-machines/sizes/gpu-accelerated/ngadsv620-series?tabs=sizebasic).

| Workload | Recommended SKU to Migrate to |
| --- | --- |
| Small AI workloads such as SLM inferencing and semantic search where optimal performance is not a priority or there is an interest in reducing costs. | NVads\_V710\_v5, NVadsA10\_v5 |
| GPU accelerated graphics applications, virtual desktops, and visualizations. | NVads\_V710\_v5, NVadsA10\_v5, NGads\_V620 |
| Gaming workloads | NGads\_V620 |

## How does the retirement of the NVv4-series virtual machines affect me?

**After** **September 30th, 2026, any remaining** **NVv4-series virtual machines (VMs) subscriptions will be set to a deallocated state. They'll stop working and no longer incur billing charges. NVv4 will no longer be under SLA or have support included.**

Note

This retirement only impacts the virtual machine sizes in the NVv4-series powered by AMD Radeon Instinct MI25 GPUs. For NVv3-series virtual machines, see the [NVv3-series virtual machines retirement guide](/en-us/azure/virtual-machines/sizes/lifecycle/retirement/nvv3-series-retirement). This retirement announcement doesn't apply to NVadsA10\_v5 or NVads\_V710\_v5 series virtual machines.

## What action did I need to take before the retirement date?

You needed to resize or deallocate your NVv4-series VMs. We recommend that you change VM sizes for these workloads from the original NVv4-series VMs to the NVads\_V710\_v5-series VMs (or an alternative).

The [NVads_V710_v5-series](/en-us/azure/virtual-machines/sizes/gpu-accelerated/nvadsv710-v5-series?tabs=sizebasic) is powered by AMD Radeon™ Pro V710 GPUs and AMD EPYC™ 9V64 F (Genoa) processors. The VMs feature up to 1 AMD Radeon™ Pro V710 GPU with 24GB memory each, up to 28 multithreaded AMD EPYC 9V64 F processor cores and 160 GiB of system memory. Check [Azure Regions by Product page](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/) for region availability. Visit the [Azure Virtual Machine pricing page](https://azure.microsoft.com/pricing/details/virtual-machines/) for pricing information.

## Steps to change VM size

1. Choose a series and size. Refer to the above tables for Microsoft’s recommendation. You can also file a support request if more assistance is needed.
2. [Request quota for the new target VM](/en-us/azure/azure-portal/supportability/per-vm-quota-requests).
3. You can [resize the virtual machine](/en-us/azure/virtual-machines/resize-vm).

## Help and support

If you have a support plan and you need technical help, create a [support request](https://portal.azure.com/).

1. Under *Issue type*, select **Technical**.
2. Under *Subscription*, select your subscription.
3. Under *Service*, click **My services**.
4. Under *Service type*, select **Virtual Machine running Windows/Linux**.
5. Under *Summary*, enter the summary of your request.
6. Under *Problem type*, select **Assistance with resizing my VM.**
7. Under *Problem subtype*, select the option that applies to you.