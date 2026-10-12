---
layout: Conceptual
title: NVv3 series retirement - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/lifecycle/retirement/nvv3-series-retirement
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
description: 'This article contains the details of the NVv3-series retirement. '
ms.service: azure-virtual-machines
ms.topic: how-to
ms.date: 2025-06-13T00:00:00.0000000Z
locale: en-us
document_id: 6497d14d-b5e1-9dc2-7627-6b697d6b636e
document_version_independent_id: 8133f047-2880-b7a7-3cd1-4e82fb2ff850
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/lifecycle/retirement/nvv3-series-retirement.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../../toc.json
asset_id: virtual-machines/sizes/lifecycle/retirement/nvv3-series-retirement
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/lifecycle/retirement/nvv3-series-retirement.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: f43aa265-2ff9-a765-853b-587e86891455
---

# NVv3 series retirement - Azure Virtual Machines | Microsoft Learn

Note

If you're currently using NVv3-series Azure VMs in the Azure UAE North region, you can continue using the NVv3-series VMs beyond the general retirement date of September 30, 2026 until the extension date of January 31, 2027. Customers in the Azure UAE North region must migrate off the NVv3-series VMs by January 31, 2027.

Note

1-year and 3-year RI purchases for the NVv3-series ended November 2, 2025.

On September 30, 2026, Microsoft Azure retired the Standard\_NV12s\_v3, Standard\_NV12hs\_v3, Standard\_NV24s\_v3, Standard\_NV24ms\_v3, Standard\_NV32ms\_v3, and Standard\_NV48s\_v3 virtual machines (VMs) in the NVv3-series virtual machines (VMs). To avoid unplanned disruption, customers who were using these VM sizes were required to migrate to supported VM series prior to the retirement date using the migration guidance below.

Microsoft is recommending the Azure [NVadsA10_v5-series](/en-us/azure/virtual-machines/sizes/gpu-accelerated/nvadsa10v5-series?tabs=sizebasic) VMs, which offer greater GPU memory bandwidth per GPU. With the NVadsA10\_v5-series VMs, Azure introduces VMs with partial NVIDIA GPUs and each VM instance comes with a GRID license. This license gives you the flexibility to use an NV instance as a virtual workstation for a single user or 25 concurrent users can connect to the VM for a virtual application scenario. These VMs are targeted for GPU accelerated graphics applications, virtual desktops, visualizations, or small AI workloads.

Depending on the workload being run, regional affinity, and cost preferences, other VMs that may be migrated to from the NVv3-series VMs include [NCasT4_v3](/en-us/azure/virtual-machines/sizes/gpu-accelerated/ncast4v3-series?tabs=sizebasic) and [NC_RTXPRO6000BSE_v6](/en-us/azure/virtual-machines/sizes/gpu-accelerated/nc-rtxpro6000-bse-v6-series?tabs=sizestoragelocalgp%2Csizebasicco):

| Workload | Recommended SKU to Migrate to |
| --- | --- |
| GPU accelerated graphics applications, virtual desktops, visualizations, or small AI workloads. | NVadsA10\_v5, NC\_RTXPRO6000BSE\_v6 |
| Offline inferencing workloads where latency is not a primary concern, and there is an interest in purchasing smaller VM SKUs or reducing costs. | NCasT4\_v3 |

## How does the retirement of the NVv3-series virtual machines affect me?

**After September 30th, 2026, any remaining NVv3-series virtual machines (VMs) will be set to a deallocated state. They'll stop working and no longer incur billing charges. NVv3 will no longer be under SLA or have support included.**

Note

This retirement only impacts the virtual machine sizes in the NVv3-series powered by NVIDIA Tesla M60 GPUs. For NVv4-series virtual machines, see the [NVv4-series virtual machines retirement guide](/en-us/azure/virtual-machines/sizes/lifecycle/retirement/nvv4-retirement). This retirement announcement doesn't apply to NVadsA10\_v5 or NVadsV710\_v5 series virtual machines.

## What action did I need to take before the retirement date?

You needed to resize or deallocate your NVv3-series VMs. Change the VM size for these workloads from the original NVv3-series VMs to the NVadsA10\_v5-series VMs (or an alternative).

The [NVadsA10_v5-series](/en-us/azure/virtual-machines/sizes/gpu-accelerated/nvadsa10v5-series?tabs=sizebasic) is powered by NVIDIA A10 GPUs and AMD EPYC™ 74F3V(Milan) processors. The VMs feature up to 2 NVIDIA A10 GPUs with 24GB memory each, up to 72 non-multithreaded AMD EPYC 74F3V processor cores and 880 GiB of system memory. Check [Azure Regions by Product page](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/) for region availability. Visit the [Azure Virtual Machine pricing page](https://azure.microsoft.com/pricing/details/virtual-machines/) for pricing information.

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