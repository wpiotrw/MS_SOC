---
layout: Conceptual
title: Availability options for Azure Virtual Machines - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/availability
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
author: mimckitt
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: mimckitt
ms.update-cycle: 1095-days
ms.service: azure-virtual-machines
description: Learn about the availability options for running virtual machines in Azure
ms.topic: concept-article
ms.date: 2026-10-20T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: bc927ec4-97ad-b143-acc1-06f091d01080
document_version_independent_id: 6f9d720c-b9b7-22d7-6e20-6da6c705eac6
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/availability.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/availability
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/availability.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 58440aae-1bdd-5fc8-1c1f-21fb4e70d88d
---

# Availability options for Azure Virtual Machines - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

This article provides an overview of the availability options for Azure virtual machines (VMs).

## Availability zones

[Availability zones](/en-us/azure/reliability/availability-zones-overview?context=/azure/virtual-machines/context/context) expands the level of control you have to maintain the availability of the applications and data on your VMs. An Availability Zone is a physically separate zone, within an Azure region. There are three Availability Zones per supported Azure region.

Each Availability Zone has a distinct power source, network, and cooling. By designing your solutions to use replicated VMs in zones, you can protect your apps and data from the loss of a data center. If one zone is compromised, then replicated apps and data are instantly available in another zone.

Note

Regional resources may or may not exist in an Availability zone, and there is no insight into what physical or logical zone a regional resource is in. A failure in any of the availability zones in a region has the potential to bring down a regional VM.

### Zone resilience for Azure VMs (Preview)

[Zone resilience for Azure VMs (Preview)](zone-resilience) lets you initiate failover of an eligible standalone zonal VM to another availability zone in the same region. The VM retains its resource identity and supported configuration.

As a prerequisite, the OS disk and every attached data disk must use supported ZRS managed disks, and you must enable zone resilience before an outage. For more details, refer to the [zone resilience documentation](zone-resilience#requirements).

Important

Zone resilience for Azure VMs is in preview. Use this preview only for evaluation and testing with nonproduction VMs. Don't use it for production VMs. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

Review the [preview limitations](zone-resilience#limitations) before enabling the feature.

## Virtual Machines Scale Sets

[Azure virtual machine scale sets](flexible-virtual-machine-scale-sets) let you create and manage a group of load balanced VMs. The number of VM instances can automatically increase or decrease in response to demand or a defined schedule. Scale sets provide high availability to your applications, and allow you to centrally manage, configure, and update many VMs. There is no cost for the scale set itself, you only pay for each VM instance that you create.

Virtual machines in a scale set can also be deployed into multiple availability zones, a single availability zone, or regionally. Availability zone deployment options may differ based on the [orchestration mode](../virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes?context=/azure/virtual-machines/context/context).

## Availability sets

An [availability set](availability-set-overview) is a logical grouping of VMs that allows Azure to understand how your application is built to provide for redundancy and availability. We recommended that two or more VMs are created within an availability set to provide for a highly available application and to meet the [99.95% Azure SLA](https://azure.microsoft.com/support/legal/sla/virtual-machines/). There is no cost for the Availability Set itself, you only pay for each VM instance that you create.

## Load balancer

Combine the [Azure Load Balancer](/en-us/azure/load-balancer/load-balancer-overview) with availability zones and scale sets to get the most application resiliency. The Azure Load Balancer distributes traffic between multiple virtual machines. For our Standard tier virtual machines, the Azure Load Balancer is included. Not all virtual machine tiers include the Azure Load Balancer. For more information about load balancing your virtual machines, see the Load Balancer quickstarts using the [CLI](/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-cli) or [PowerShell](/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-powershell).

## Azure Storage redundancy

Azure Storage always stores multiple copies of your data so that it is protected from planned and unplanned events, including transient hardware failures, network or power outages, and massive natural disasters. Redundancy ensures that your storage account meets its availability and durability targets even in the face of failures.

When deciding which redundancy option is best for your scenario, consider the tradeoffs between lower costs and higher availability. The factors that help determine which redundancy option you should choose include:

- How your data is replicated in the primary region
- Whether your data is replicated to a second region that is geographically distant to the primary region, to protect against regional disasters
- Whether your application requires read access to the replicated data in the secondary region if the primary region becomes unavailable for any reason

For more information, see [Azure Storage redundancy](/en-us/azure/storage/common/storage-redundancy)

## Azure Site Recovery

As an organization you need to adopt a business continuity and disaster recovery (BCDR) strategy that keeps your data safe, and your apps and workloads online, when planned and unplanned outages occur.

[Azure Site Recovery](/en-us/azure/site-recovery/site-recovery-overview) helps ensure business continuity by keeping business apps and workloads running during outages. Site Recovery replicates workloads running on physical and virtual machines (VMs) from a primary site to a secondary location. When an outage occurs at your primary site, you fail over to secondary location, and access apps from there. After the primary location is running again, you can fail back to it.

Site Recovery can manage replication for:

- Azure VMs replicating between Azure regions.
- On-premises VMs, Azure Stack VMs, and physical servers.