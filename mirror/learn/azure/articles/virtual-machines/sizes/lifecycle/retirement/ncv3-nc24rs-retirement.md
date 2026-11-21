---
layout: Conceptual
title: NCv3 and NC24rs Retirement - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/lifecycle/retirement/ncv3-nc24rs-retirement
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
description: Migration guide for NC24rs_v3 sizes
ms.service: azure-virtual-machines
ms.topic: concept-article
ms.date: 2026-11-20T00:00:00.0000000Z
ms.subservice: sizes
locale: en-us
document_id: 9346fb9a-2e12-92a0-b9e5-e4e0e98bdb63
document_version_independent_id: e99e5e5d-0078-6fc4-c5a9-e0ae7bb75356
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/lifecycle/retirement/ncv3-nc24rs-retirement.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../../toc.json
asset_id: virtual-machines/sizes/lifecycle/retirement/ncv3-nc24rs-retirement
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/lifecycle/retirement/ncv3-nc24rs-retirement.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: d4b9b2b7-adcd-7d35-3d00-e6d11e643f13
---

# NCv3 and NC24rs Retirement - Azure Virtual Machines | Microsoft Learn

On September 30, 2025, Microsoft Azure retires the Standard\_NC24rs\_v3 virtual machine (VM) size in NCv3-series virtual machines (VMs). To avoid any disruption to your service, change the VM sizing from the Standard\_NC24rs\_v3 to the newer VM series in the same NC product line.

Note

All the NCv3-series VM sizes, including Standard\_NC24rs\_v3, retire on September 30, 2025. For retirement details and SKU migration guidance, see the [NCv3-series retirement page](/en-us/azure/virtual-machines/sizes/lifecycle/retirement/ncv3-retirement).

Microsoft recommends the Azure [NCadsH100_v5-series](/en-us/azure/virtual-machines/ncads-h100-v5?source=recommendations)VMs, which offer greater GPU memory bandwidth per GPU, improved [accelerated networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) capabilities, and larger and faster local solid state drives. These VMs are targeted for GPU accelerated midrange AI training, batch inferencing, and high-performance computing simulation workloads.

However, depending on the workload being run, regional affinity, and cost preferences, other VMs that may be migrated to from Standard\_NC24rs\_v3 include NVadsA10\_v5, NCasT4\_v3, and NVadsV710\_v5:

| Workload | Recommended SKU to Migrate to |
| --- | --- |
| High GPU compute workloads such as real-time inferencing and LLM inferencing. | NCadsH100\_v5 which has the best inference per dollar value. |
| Offline inferencing workloads where latency is not the primary concern, and there is an interest in purchasing smaller VM SKUs or reducing costs. | NCasT4\_v3 |
| Graphics, visualization, or small AI workloads where optimal performance is not a priority. | NVadsA10\_v5, NVadsV710\_v5 |

## How does the retirement of the Standard\_NC24rs\_v3 affect me?

After September 30, 2025, any remaining Standard\_NC24rs\_v3 VM subscriptions will be set to a deallocated state. They'll stop working and no longer incur billing charges. The Standard\_NC24rs\_v3 VM size will no longer be under SLA or have support included.

Note

This retirement announcement doesn't apply to NCasT4\_v3, NC\_A100\_v4, and NCadsH100\_v5 series virtual machines.

## What action do I need to take before the retirement date?

You need to resize or deallocate your Standard\_NC24rs\_v3 VM size. We recommend that you change VM sizes for these workloads from the original Standard\_NC24rs\_v3 VM size to the NCadsH100\_v5-series VMs (or an alternative).

The [NCadsH100_v5-series](/en-us/azure/virtual-machines/ncads-h100-v5?source=recommendations) is powered by NVIDIA H100 NVL GPU and 4th-generation AMD EPYC™ Genoa processors. The VMs feature up to 2 NVIDIA H100 NVL GPUs with 94GB memory each, up to 96 non-multithreaded AMD EPYC Genoa processor cores and 640 GiB of system memory. Check [Azure Regions by Product page](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/) for region availability. Visit the [Azure Virtual Machine pricing page](https://azure.microsoft.com/pricing/details/virtual-machines/) for pricing information.

## Steps to change VM size

1. Choose a series and size. Refer to the above tables for Microsoft’s recommendation. You can also file a support request if more assistance is needed.
2. [Request quota for the new target VM](/en-us/azure/azure-portal/supportability/per-vm-quota-requests)).
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