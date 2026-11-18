---
layout: Conceptual
title: About Azure Spot Virtual Machines - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms
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
author: mattmcinnes
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: mattmcinnes
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Learn about Azure Spot Virtual Machines to save on costs.
ms.subservice: azure-spot-vm
ms.topic: overview
ms.date: 2026-11-06T00:00:00.0000000Z
locale: en-us
document_id: fb6d504c-6e94-a353-3465-832330efab44
document_version_independent_id: 79c70736-63a0-b023-5336-e16cb4f9d217
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/spot-vms.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/spot-vms
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/spot-vms.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 88f1a85d-0610-a33d-c915-ac23b0c8c08d
---

# About Azure Spot Virtual Machines - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

Using Azure Spot Virtual Machines allows you to take advantage of our unused capacity at a significant cost savings. At any point in time when Azure needs the capacity back, the Azure infrastructure will evict Azure Spot Virtual Machines. Therefore, Azure Spot Virtual Machines are great for workloads that can handle interruptions like batch processing jobs, dev/test environments, large compute workloads, and more.

The amount of available capacity can vary based on size, region, time of day, and more. When you deploy Azure Spot Virtual Machines, Azure allocates the VMs if there's capacity available, but there's no SLA for these VMs. An Azure Spot Virtual Machine offers no high availability guarantees. At any point when Azure needs the capacity back, the Azure infrastructure evicts Azure Spot Virtual Machines with 30 seconds' notice.

Azure [Spot Plus (Public Preview)](spot-plus-public-preview-azure-compute-technical) is an enhanced tier of Azure Spot Virtual Machines for interruption-tolerant workloads. It's designed to deliver better runtimes, improved eviction and rebalance signals, while remaining evictable when Azure needs the capacity.

[![YouTube video about Spot VMs and reducing operational costs of stateless workloads.](media/spot-vms/azure-spot-virtual-machines-thumbnail.jpg)](https://youtu.be/GFRA91FTqAE)

## Eviction policy

Spot VMs can be stopped if Azure needs capacity for other pay-as-you-go workloads or when the price of the spot instance exceeds the maximum price that you have set. When creating an Azure Spot Virtual Machine, you can set the eviction policy to *Deallocate* (default) or *Delete*.

The *Deallocate* policy moves your VM to the stopped-deallocated state, allowing you to redeploy it later. However, there's no guarantee that the allocation will succeed. The deallocated VMs will count against your quota and you'll be charged storage costs for the underlying disks.

If you would like your VM to be deleted when it's evicted, you can set the eviction policy to *delete*. The evicted VMs are deleted together with their underlying disks, so you'll not continue to be charged for the storage.

You can opt in to receive in-VM notifications through [Azure Scheduled Events](linux/scheduled-events). These are delivered on a best effort basis up to 30 seconds prior to the eviction.

| Option | Outcome |
| --- | --- |
| Max price is set to &gt;= the current price. | VM is deployed if capacity and quota are available. |
| Max price is set to &lt; the current price. | The VM isn't deployed. You'll get an error message that the max price needs to be &gt;= current price. |
| Restarting a stopped/deallocated VM if the max price is &gt;= the current price | If there's capacity and quota, then the VM is deployed. |
| Restarting a stopped/deallocated VM if the max price is &lt; the current price | You'll get an error message that the max price needs to be &gt;= current price. |
| Price for the VM has gone up and is now &gt; the max price. | The VM gets evicted. Azure will attempt scheduled event delivery up to 30 seconds before actual eviction. |
| After eviction, the price for the VM goes back to being &lt; the max price. | The VM won't be automatically restarted. You can restart the VM yourself, and it will be charged at the current price. |
| If the max price is set to `-1` | The VM won't be evicted for pricing reasons. The max price will be the current price, up to the price for standard VMs. You'll never be charged above the standard price. |
| Changing the max price | You need to deallocate the VM to change the max price. Deallocate the VM, set a new max price, then update the VM. |

Tip

Check out our [Azure Virtual Machine Spot Eviction](/en-us/azure/architecture/guide/spot/spot-eviction) guide to learn how to create a reliable interruptible workload in Azure.

## Limitations

The following VM sizes aren't supported for Azure Spot Virtual Machines:

- B-series
- Promo versions of any size (like Dv2, NV, NC, H promo sizes)

Azure Spot Virtual Machines can be deployed to any region, except Microsoft Azure operated by 21Vianet.

The following [offer types](https://azure.microsoft.com/support/legal/offer-details/) are currently supported:

- Enterprise Agreement
- Pay-as-you-go offer code (003P)
- Sponsored (0036P and 0136P) - not available in Fairfax
- For Cloud Service Provider (CSP), see the [Partner Center](/en-us/partner-center/azure-plan-get-started) or contact your partner directly.

## Pricing

Pricing for Azure Spot Virtual Machines is variable, based on region and SKU. For more information, see VM pricing for [Linux](https://azure.microsoft.com/pricing/details/virtual-machines/linux/) and [Windows](https://azure.microsoft.com/pricing/details/virtual-machines/windows/).

You can also query pricing information by using the [Azure retail prices API](/en-us/rest/api/cost-management/retail-prices/azure-retail-prices) to query for information about Spot pricing (not Spot Plus). The `meterName` and `skuName` both contain `Spot`.

For other ways to query pricing information, see Spot & Spot Plus Pricing ARG.

With variable pricing, you have option to set a max price, in US dollars (USD), using up to five decimal places. For example, the value `0.98765`would be a max price of $0.98765 USD per hour. If you set the max price to be `-1`, the VM won't be evicted based on price. The price for the VM will be the current price for spot or the price for a standard VM, which ever is less, as long as there's capacity and quota available.

## Pricing and eviction history

### Portal

You can see historical pricing and eviction rates per size in a region in the portal while you are creating the VM. After selecting the checkbox to **Run with Azure Spot discount**, a link will appear under the size selection of the VM titled **View pricing history and compare prices in nearby regions**. By selecting that link you will be able to see a table or graph of spot pricing for the specified VM size. The pricing and eviction rates in the following images are only examples.

Tip

Eviction rates are quoted *per hour*. For example, an eviction rate of 10% means a VM has a 10% chance of being evicted within the next hour, based on historical eviction data of the last 7 days.

**Chart**:

![Screenshot of the region options with the difference in pricing and eviction rates as a chart.](../reusable-content/ce-skilling/azure/media/virtual-machines/spot-chart.png)

**Table**:

![Screenshot of the region options with the difference in pricing and eviction rates as a table.](../reusable-content/ce-skilling/azure/media/virtual-machines/spot-table.png)

### Azure Resource Graph

You can programmatically access relevant Spot VM SKU data through [Azure Resource Graph](/en-us/azure/governance/resource-graph/overview). Get pricing history in the last 90 days and eviction rates for the last 28 trailing days to identify SKUs that better meet your specific needs.

Key benefits:

- Query Spot eviction rates and the last few months of Spot prices programmatically through ARM or the [ARG Explorer in Azure portal](/en-us/azure/governance/resource-graph/first-query-portal)
- Create a custom query to extract the specific data relevant to your scenario with the ability to filter across a variety of parameters, such as SKU and region
- Easily compare data across multiple regions and SKUs
- Find a different Spot SKU or region with a lower price and/or eviction rate

Try out the following sample queries for Spot pricing history and eviction rates using the [ARG Explorer in Azure portal](/en-us/azure/governance/resource-graph/first-query-portal). Spot pricing history and eviction rates data are available in the `SpotResources` table. 

**Spot and Spot Plus pricing sample query (history available only for Spot)**:

```sql
SpotResources 
| where type =~ 'microsoft.compute/skuspotpricehistory/ostype/location' 
| where sku.name in~ ('standard_d2s_v4', 'standard_d4s_v4') 
| where properties.osType =~ 'linux' 
| where location in~ ('eastus', 'southcentralus') 
| project skuName = tostring(sku.name), osType = tostring(properties.osType), location, latestSpotPriceUSD = todouble(properties.spotPrices[0].priceUSD), latestSpotPlusPriceUSD = todouble(properties.spotPlusPrices[0].priceUSD)
| order by latestSpotPriceUSD asc 
```

**Spot eviction rates sample query**:

```sql
SpotResources 
| where type =~ 'microsoft.compute/skuspotevictionrate/location' 
| where sku.name in~ ('standard_d2s_v4', 'standard_d4s_v4') 
| where location in~ ('eastus', 'southcentralus') 
| project skuName = tostring(sku.name), location, spotEvictionRate = tostring(properties.evictionRate) 
| order by skuName asc, location asc
```

Alternatively, try out the [ARG REST API](/en-us/rest/api/azure-resourcegraph/) to get the pricing history and eviction rate history data.

## Frequently asked questions

**Q:** Once created, is an Azure Spot Virtual Machine the same as regular standard VM?

**A:** Yes, except there's no SLA for Azure Spot Virtual Machines and they can be evicted at any time.

**Q:** What to do when you get evicted, but still need capacity?

**A:** We recommend you use standard VMs instead of Azure Spot Virtual Machines if you need capacity right away.

**Q:** How is quota managed for Azure Spot Virtual Machines?

**A:** Azure Spot Virtual Machines will have a separate quota pool. Spot quota will be shared between VMs and scale-set instances. For more information, see [Azure subscription and service limits, quotas, and constraints](/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits).

**Q:** Can I request for additional quota for Azure Spot Virtual Machines?

**A:** Yes, you'll be able to submit the request to increase your quota for Azure Spot Virtual Machines through the [standard quota request process](/en-us/azure/azure-portal/supportability/per-vm-quota-requests).

**Q:** Where can I post questions?

**A:** You can post and tag your question with `azure-spot` at [Q&A](/en-us/answers/topics/azure-spot.html).

**Q:** How can I change the max price for a spot VM?

**A:** Before you can change the max price, you need to deallocate the VM. Then you can change the max price in the portal, from the **Configuration** section for the VM.

**Q:** Can I convert existing VMs to Spot VMs?

**A:** No, setting the Spot flag is only supported at creation time.

**Q:** Can I convert Spot VMs to Standard VMs?

**A:** No, Spot VMs cannot be directly converted to Standard VMs.