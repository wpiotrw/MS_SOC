---
layout: Conceptual
title: NCv3-series Retirement - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/lifecycle/retirement/ncv3-retirement
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
author: sherrywangms
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: sherrywang
ms.update-cycle: 1095-days
description: Migration guide for NCv3-series virtual machines
ms.service: azure-virtual-machines
ms.topic: concept-article
ms.date: 2026-11-20T00:00:00.0000000Z
ms.subservice: sizes
locale: en-us
document_id: 476fd707-73f2-f3ba-78f3-2dd0083a230f
document_version_independent_id: 8e06c9f0-e10f-efa8-f6bb-e173208e8a7f
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/lifecycle/retirement/ncv3-retirement.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../../toc.json
asset_id: virtual-machines/sizes/lifecycle/retirement/ncv3-retirement
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/lifecycle/retirement/ncv3-retirement.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 67e7fe4a-cee7-79e4-5e72-54b7730d9956
---

# NCv3-series Retirement - Azure Virtual Machines | Microsoft Learn

This article explains the retirement timeline for Azure NCv3-series virtual machines, including regional extensions, and provides guidance on replacement VM series and resizing your VMs.

Note

If you're currently using the NCv3-series Azure VMs in either of these regions, you can disregard the general NCv3-series retirement date of September 30, 2025, and continue to use the NCv3-series Azure VMs in that region until the respective extension date:  The US Gov Virginia and US Gov Arizona regions have an extension and a retirement date of **December 31st, 2026**.  The Jio India West and China North 3 regions have an extension and a retirement date of **June 30th, 2027**.

On September 30, 2025, Microsoft Azure will retire the Standard\_NC6s\_v3, Standard\_NC12s\_v3, Standard\_NC24s\_v3, and Standard\_NC24rs\_v3 virtual machines (VMs) in NCv3-series virtual machines (VMs). To avoid any disruption to your service, we recommend that you change the VM sizing for your workloads from the current NCv3-series VMs to the newer VM series in the same NC product line.

Microsoft is recommending the Azure [NCadsH100_v5-series](/en-us/azure/virtual-machines/ncads-h100-v5?source=recommendations)VMs, which offer greater GPU memory bandwidth per GPU, improved [accelerated networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) capabilities, and larger and faster local solid state drives. These VMs are targeted for GPU accelerated midrange AI training, batch inferencing, and high-performance computing simulation workloads. For regions where NCadsH100\_v5 is not available, please migrate to the other recommended SKUs below.

Depending on the workload being run, regional affinity, and cost preferences, other VMs that may be migrated to from the NCv3-series VMs include [NVadsA10_v5](/en-us/azure/virtual-machines/sizes/gpu-accelerated/nvadsa10v5-series?tabs=sizebasic), [NCasT4_v3](/en-us/azure/virtual-machines/sizes/gpu-accelerated/ncast4v3-series?tabs=sizebasic), and [NVadsV710_v5](/en-us/azure/virtual-machines/sizes/gpu-accelerated/nvadsv710-v5-series?tabs=sizebasic):

| Workload | Recommended SKU to Migrate to |
| --- | --- |
| High GPU compute workloads such as real-time inferencing and LLM inferencing. | NCadsH100\_v5 which has the best inference per dollar value. |
| Offline inferencing workloads where latency is not the primary concern, and there is an interest in purchasing smaller VM SKUs or reducing costs. | NCasT4\_v3 |
| Graphics, visualization, or small AI workloads where optimal performance is not a priority. | NVadsA10\_v5, NVadsV710\_v5 |

## How does the retirement of the NCv3-series virtual machines affect me?

**After** **September 30th, any remaining** **NCv3-series virtual machines (VMs) subscriptions will be set to a deallocated state. They'll stop working and no longer incur billing charges. NCv3 will no longer be under SLA or have support included.**

Note

This retirement only impacts the virtual machine sizes in the original NCv3-series powered by NVIDIA V100 GPUs. This retirement announcement doesn't apply to NCasT4\_v3, NC\_A100\_v4, and NCadsH100\_v5 series virtual machines.

## What action do I need to take before the retirement date?

You need to resize or deallocate your NCv3-series VMs. We recommend that you change VM sizes for these workloads from the original NCv3-series VMs to the NCadsH100\_v5-series VMs (or an alternative).

The [NCadsH100_v5-series](/en-us/azure/virtual-machines/ncads-h100-v5?source=recommendations) is powered by NVIDIA H100 NVL GPU and 4th-generation AMD EPYC™ Genoa processors. The VMs feature up to 2 NVIDIA H100 NVL GPUs with 94GB memory each, up to 96 non-multithreaded AMD EPYC Genoa processor cores and 640 GiB of system memory. Check [Azure Regions by Product page](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/) for region availability. Visit the [Azure Virtual Machine pricing page](https://azure.microsoft.com/pricing/details/virtual-machines/) for pricing information.

## Steps to change VM size

1. Choose a series and size. Refer to the above tables for Microsoft’s recommendation. You can also file a support request if more assistance is needed.
2. [Request quota for the new target VM](/en-us/azure/azure-portal/supportability/per-vm-quota-requests).
3. [Resize the virtual machine](../../resize-vm).

## Help and support

If you have a support plan and you need technical help, create a [support request](https://portal.azure.com/).

1. Under *Issue type*, select **Technical**.
2. Under *Subscription*, select your subscription.
3. Under *Service*, click **My services**.
4. Under *Service type*, select **Virtual Machine running Windows/Linux**.
5. Under *Summary*, enter the summary of your request.
6. Under *Problem type*, select **Assistance with resizing my VM.**
7. Under *Problem subtype*, select the option that applies to you.