---
layout: Conceptual
title: Azure Dedicated Host SKU Lifecycle - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/dedicated-hosts/sku-lifecycle
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
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
description: Learn about the Azure Dedicated Host SKU lifecycle, including retired and retiring SKUs, their recommended replacements, and how to modernize to newer SKUs.
author: vamckMS
ms.author: vakavuru
ms.service: azure-dedicated-host
ms.topic: concept-article
ms.date: 2026-09-25T00:00:00.0000000Z
locale: en-us
document_id: e08632ee-8e5b-34a8-0c36-2189141b142c
document_version_independent_id: 28a1edd8-038d-7efa-dc82-35c60a84f697
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/dedicated-hosts/sku-lifecycle.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/dedicated-hosts/sku-lifecycle
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/dedicated-hosts/sku-lifecycle.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a48df08f-c196-4114-998c-7d0528e51d7a
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7853f9c-f51c-437c-a7f2-85bda0416f2e
platformId: bdc2f58a-d9af-5444-8e14-b725142fb17d
---

# Azure Dedicated Host SKU Lifecycle - Azure Virtual Machines | Microsoft Learn

A Dedicated Host SKU is a combination of a virtual machine (VM) series and a specific Intel or AMD-based physical server. Like standard VM sizes, Dedicated Host SKUs follow the [VM lifecycle](../sizes/lifecycle/lifecycle-overview) stages: *Current*, *Extended*, *End of Life*, and *Retired*. As the underlying hardware ages and newer hardware becomes available, older Dedicated Host SKUs are announced for retirement and eventually retired. Plan to modernize to a Current or Extended Dedicated Host SKU before the retirement date.

This article lists retired and retiring Dedicated Host SKUs with their recommended replacements, and describes the actions to take when a SKU is announced for retirement.

Note

No currently available Dedicated Host SKUs are planned for retirement. Dedicated Host SKU retirements are announced 12 months before the retirement date.

## Retired and retiring Dedicated Host SKUs

Warning

SKUs with *Retirement Status* listed as *Retired* are **no longer available** and can't be provisioned.

Retired Dedicated Host SKUs run on older hardware that's no longer supported. SKUs with *Retirement Status* listed as *Announced* are still available until the *Planned Retirement Date*. Retired SKUs are kept in the following table as a historical record.

| SKU name | Retirement Status | Retirement Announcement | Planned Retirement Date | Recommended replacement |
| --- | --- | --- | --- | --- |
| Dsv3-Type1 | **Retired** | 03/15/22 | 06/30/23 | Dsv3-Type3 or Dsv3-Type4 |
| Dsv3-Type2 | **Retired** | 03/15/22 | 06/30/23 | Dsv3-Type3 or Dsv3-Type4 |
| Esv3-Type1 | **Retired** | 03/15/22 | 06/30/23 | Esv3-Type3 or Esv3-Type4 |
| Esv3-Type2 | **Retired** | 03/15/22 | 06/30/23 | Esv3-Type3 or Esv3-Type4 |

For retired and retiring VM size series, see [VM size series retirements, capacity growth restrictions, and modernization guidance](../sizes/lifecycle/retirements-and-capacity-restrictions).

## What actions should you take?

When a Dedicated Host SKU is announced for retirement, modernize to a newer SKU before the retirement date. For manually placed VMs, you need to create a Dedicated Host of a newer SKU, stop the VMs on your existing Dedicated Host, reassign them to the new host, start the VMs, and delete the old host. For automatically placed VMs or for Virtual Machine Scale Sets, you need to create a Dedicated Host of a newer SKU, stop the VMs or Virtual Machine Scale Set, delete the old host, and then start the VMs or Virtual Machine Scale Set.

Refer to the [Azure Dedicated Host Modernization Guide](modernization-guide) for more detailed instructions. We recommend moving to a Current or Extended Dedicated Host SKU for your VM family.

If you have any questions, contact us through customer support.

## FAQs

### Will modernization result in downtime?

Yes, you would have to stop/deallocate your VMs or Virtual Machine Scale Sets before moving them to the target host.

### When will other Dedicated Host SKUs retire?

No currently available Dedicated Host SKUs are planned for retirement. We'll announce Dedicated Host SKU retirements 12 months in advance of the official retirement date of a given Dedicated Host SKU.

### What happens to my Azure Reservation?

You need to [exchange your reservation](/en-us/azure/cost-management-billing/reservations/exchange-and-refund-azure-reservations#how-to-exchange-or-refund-an-existing-reservation) through the Azure portal to match the new Dedicated Host SKU.

### What would happen to my host if I do not modernize before the retirement date?

After the retirement date, any dedicated host running on a retired SKU will be set to 'Host Pending Deallocate' state before eventually deallocating the host. For more assistance, please reach out to Azure support.

### What will happen to my VMs if a Host is automatically deallocated?

If the underlying host is deallocated the VMs that were running on the host would be either in failed or stopped state but not deleted.

You could stop/deallocate the VM or virtual machine scale set and dissociate the VM or virtual machine scale set from the host/host group (depending on explicit vs implicit placement) and then you would be able to either create a new host (of the same VM family) and allocate VMs on the host/host group or run the VMs on multitenant infrastructure.

Refer to the [Azure Dedicated Host Modernization Guide](modernization-guide) for more detailed instructions.