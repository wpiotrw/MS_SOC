---
layout: Conceptual
title: Use the portal to deploy Azure Spot Virtual Machines - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/spot-portal
breadcrumb_path: ../breadcrumb/azure-compute/toc.json
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
author: kaza-sriram
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: prkazasr
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: How to use the Portal to deploy Spot Virtual Machines
ms.subservice: azure-spot-vm
ms.topic: how-to
ms.date: 2026-02-28T00:00:00.0000000Z
locale: en-us
document_id: a898e9f6-fbea-5053-ced3-43e9becf8d06
document_version_independent_id: 8103753d-6476-c75f-765e-d70e33a98cff
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/spot-portal.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/spot-portal
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/spot-portal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 3a1f7932-bd39-1664-632a-f9eba8498d31
---

# Use the portal to deploy Azure Spot Virtual Machines - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Uniform scale sets

By using [Azure Spot Virtual Machines](spot-vms), you can take advantage of unused capacity at a significant cost savings. At any point when Azure needs the capacity back, the Azure infrastructure evicts Azure Spot Virtual Machines. Therefore, Azure Spot Virtual Machines are great for workloads that can handle interruptions like batch processing jobs, dev/test environments, large compute workloads, and more. [Spot Plus (Public Preview)](spot-plus-public-preview-azure-compute-technical) is an enhanced tier of Azure Spot Virtual Machines for interruption-tolerant workloads. It's designed to deliver better runtimes and improved eviction and rebalance signals, while remaining evictable when Azure needs the capacity.

Pricing for Azure Spot Virtual Machines is variable, based on region and SKU. For more information, see VM pricing for [Linux](https://azure.microsoft.com/pricing/details/virtual-machines/linux/) and [Windows](https://azure.microsoft.com/pricing/details/virtual-machines/windows/). For more information about setting the max price, see [Azure Spot Virtual Machines - Pricing](spot-vms#pricing).

You have option to set a max price you are willing to pay, per hour, for the VM. The max price for an Azure Spot Virtual Machine can be set in US dollars (USD), using up to 5 decimal places. For example, the value `0.05701`would be a max price of $0.05701 USD per hour. If you set the max price to be `-1`, the VM won't be evicted based on price. The price for the VM will be the current price for spot or the price for a standard VM, which ever is less, as long as there is capacity and quota available.

When the VM is evicted, you have the option to either delete the VM and the underlying disk or deallocate the VM so that it can be restarted later.

## Create the VM

When you are deploying a VM, you can choose to use an Azure spot instance.

On the **Basics** tab, in the **Instance details** section, select **Run with Azure Spot discount** to choose a Spot variant.

![Screenshot of the Basics tab with the Run with Azure Spot discount option.](media/spot-portal/spot-plus-pricing-tier-selection.png)

After you choose the Spot variant, the section expands and you can choose your [eviction type and eviction policy](spot-vms#eviction-policy).

![Screenshot of the expanded Spot configuration with eviction type and eviction policy options.](media/spot-portal/spot-plus-eviction-settings.png)

Select **View pricing history and compare prices in nearby regions** to compare the pricing and eviction rates with other similar regions. Currently, this feature is available for **Spot** only.

In this example, the Canada Central region is less expensive and has a lower eviction rate than the East US region.

![Screenshot of the region options with the difference in pricing and eviction rates.](media/spot-portal/pricing.png)

You can change the region by selecting the choice that works the best for you and then selecting **OK**.

## Simulate an eviction

You can [simulate an eviction](/en-us/rest/api/compute/virtualmachines/simulateeviction) of an Azure Spot Virtual Machine, to testing how well your application will respond to a sudden eviction.

Replace the following with your information:

- `subscriptionId`
- `resourceGroupName`
- `vmName`

```rest
POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/simulateEviction?api-version=2020-06-01
```

`Response Code: 204` means the simulated eviction was successful.