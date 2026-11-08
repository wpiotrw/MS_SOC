---
layout: Conceptual
title: Estimate the cost of creating a Virtual Machine in the Azure portal (Preview) - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/estimated-vm-create-cost-card
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
author: iamwilliew
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: wwilliams
ms.update-cycle: 180-days
ms.service: azure-virtual-machines
description: Use the Azure portal Virtual Machine creation flow cost card to estimate the final cost of your Virtual Machine.
ms.topic: concept-article
ms.date: 2026-11-02T00:00:00.0000000Z
ms.custom: portal
locale: en-us
document_id: 98c9e8ea-8c7f-758d-5f06-2c3e13b3fcb9
document_version_independent_id: af985a4f-37b6-16d4-87b7-600acc75ce99
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/estimated-vm-create-cost-card.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/estimated-vm-create-cost-card
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/estimated-vm-create-cost-card.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 046dc90a-5278-4ff0-0175-26d7b92d20b5
---

# Estimate the cost of creating a Virtual Machine in the Azure portal (Preview) - Azure Virtual Machines | Microsoft Learn

Azure virtual machines (VM) can be created through the [Azure portal](https://portal.azure.com/). This method provides a browser-based user interface to create VMs and their associated resources. As you create VMs in the Azure portal and configure them through the different tabs during the creation process, the cost card reflects the pricing estimations based on your selections.

Important

The estimated cost card feature for virtual machines in the Azure portal is currently in preview. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability.

The cost displayed in this card doesn't reflect usage and other costs incurred on the VMs beyond the creation of the resources. The final price of your VMs may factor in other respective networking, storage, and extra costs that pertain to the usage and application of the VMs.

Note

Costs reflected in the card are estimates only. Pricing may vary depending on your Microsoft agreement, date of purchase, subscription type, usage costs, licensing, and currency exchange rates. Total costs may include other resource costs, licensing, and subscription implications. The costs indicated on the card may vary across regions, subscription types, sizes, and images.

## Prerequisites

Currently, the estimated cost card feature for VMs in the Azure portal is limited to Pay-as-you-go customers. This feature isn't available or visible for other subscription types and other discount plans, such as the Savings Plan and Reserved Instances.

If your subscription has policy restrictions for specific users, those users aren't able to view the cost card unless those restrictions are lifted. If your subscription has policy restrictions to not show costs, cost card will not be shown unless those restrictions are lifted.

## Cost card

The following sections reflect the various tabs during the VM creation process in the Azure portal. The listed resources and features are included in the estimated cost card. For further pricing information, refer to their respective pricing pages linked in the following tables.

Costs associated with selecting existing resources during the VM creation process are only reflected in the cost card if those resources may incur extra charges.

### Basics

| Resource or feature | Notes |
| --- | --- |
| [Image and Size (Windows)](https://azure.microsoft.com/pricing/details/virtual-machines/windows/) | Estimates of VM size and Windows based image are displayed. |
| [Image and Size (Linux)](https://azure.microsoft.com/pricing/details/virtual-machines/linux/) | Estimates of VM size and Linux based image are displayed. |
| [Spot](https://azure.microsoft.com/pricing/spot-advisor/) | If selected, the discounted Spot price is shown. |
| [Azure Hybrid Benefit (AHB) licensing](https://azure.microsoft.com/pricing/hybrid-benefit/) | If selected, the AHB discounts are applied and shown. |

### Disks

| Resource or feature | Notes |
| --- | --- |
| [OS Disk](https://azure.microsoft.com/pricing/details/managed-disks/) | Estimate for using the selected disk to host the selected operating system is displayed. |
| [Ultra Disk Reservation charge](https://azure.microsoft.com/pricing/details/managed-disks/) | A reservation charge is only imposed if Ultra Disk compatibility is enabled on the VM without attaching an Ultra Disk. |
| [Data Disk](https://azure.microsoft.com/pricing/details/managed-disks/) | Estimate for using the selected disk, to store and access data, is displayed. A disk share estimate is displayed if enabled and other charges apply. Transaction and bursting costs aren't included in the estimate. |

### Networking

| Resource or feature | Notes |
| --- | --- |
| [Public IP](https://azure.microsoft.com/pricing/details/ip-addresses/) | Estimated cost of running a public IP Address. A Standard Public IP is selected when a new IP is created as part of the default selection. |
| [VM Data transfer](https://azure.microsoft.com/pricing/details/bandwidth/) | Estimated cost is based on inter-region data transfer routed via Microsoft Premium Global Network. |
| [Azure Load Balancer](https://azure.microsoft.com/pricing/details/load-balancer/) | A new Standard Azure Load Balancer estimate includes the cost of one rule and estimated data processed. For an existing Azure load balancer, the estimate includes only the estimated data transfer and Azure assumes rules already exist. |
| [Azure Application Gateway](https://azure.microsoft.com/pricing/details/application-gateway/) | A new Application Gateway v2 estimate includes Fixed, Capacity units and estimate outbound data transfer costs. For this estimate, one capacity unit consumption is assumed. For an existing Azure Application gateway, only the outbound data transfer estimate is displayed. Azure assumes that other fixed costs are already paid for. |

### Management

| Resource or feature | Notes |
| --- | --- |
| [Azure Backup](https://azure.microsoft.com/pricing/details/backup/) | Monthly average backup cost is based on the operating system disk size of the VM that needs backup, the backup policy selected, and estimated moderate daily data churn. Storage consumed by Azure Backup grows incrementally over a period; the monthly cost of Azure Back also increases as consumption grows. Azure models the growth of consumed storage over a year, aggregates it and uses the average monthly consumption to propose the estimate. |
| [Azure Site Recovery](https://azure.microsoft.com/pricing/details/site-recovery/) | Estimate for recovering a VM to Azure. |

### Monitoring

| Resource or feature | Notes |
| --- | --- |
| [Alerts](https://azure.microsoft.com/pricing/details/monitor/) | Estimate for the selected alerting rules. |
| [Boot Diagnostics](https://azure.microsoft.com/pricing/details/storage/blobs/) | Estimate for enabling boot diagnostics can vary based the storage account and number of transactions performed. If enabled, a charged is incurred. However, due to the variability in consumption, the charge isn't included in the estimate. |

### Advanced

| Resource or feature | Notes |
| --- | --- |
| [Azure Dedicated Host](https://azure.microsoft.com/pricing/details/virtual-machines/dedicated-host/) | Adding an existing Azure Dedicated Host deducts the cost of the VM size as the host had been prepaid for. |