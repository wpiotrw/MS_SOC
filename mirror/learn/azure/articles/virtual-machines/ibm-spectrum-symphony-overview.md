---
layout: Conceptual
title: What is IBM Spectrum Symphony on Azure? - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/ibm-spectrum-symphony-overview
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
author: rayoef
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: rayoflores
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Learn how IBM Spectrum Symphony integrates with Azure Compute Fleet to extend enterprise HPC workload orchestration to Azure compute capacity.
ms.subservice: hpc
ms.topic: overview
ms.date: 2026-09-22T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 72bee729-9411-080d-990e-36ed583dd355
document_version_independent_id: 01ef23d4-2bec-a424-3d08-a95b3c3e9047
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/ibm-spectrum-symphony-overview.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/ibm-spectrum-symphony-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/ibm-spectrum-symphony-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 57431083-4518-f114-3d6f-78ab12b60721
---

# What is IBM Spectrum Symphony on Azure? - Azure Virtual Machines | Microsoft Learn

IBM Spectrum Symphony integrates with Azure Compute Fleet to extend enterprise high-performance computing (HPC) workload orchestration environments to Azure. The integration dynamically provisions Azure compute capacity as workload demand changes while maintaining your existing Symphony workload policies, queues, service-level objectives, and operational processes.

## How the integration works

The IBM Spectrum Symphony Provider Plugin for Microsoft Azure Compute Fleet connects IBM Symphony Host Factory to Azure Compute Fleet. The plugin translates Symphony resource requirements into Azure Compute Fleet requests. Symphony schedules and orchestrates workloads, while Azure Compute Fleet provides access to eligible compute capacity.

![Diagram that shows IBM Spectrum Symphony connected to Azure Compute Fleet.](media/ibm-spectrum-symphony/architecture.svg)

 IBM Spectrum Symphony sends job, policy, and resource-demand information to Host Factory. The Azure resource connector translates the demand into an Azure Compute Fleet Launch mode request. Azure Compute Fleet selects eligible Spot and pay-as-you-go VMs. The provisioned VMs join the Symphony cluster as execution hosts. Symphony manages the workloads and execution-host lifecycle, while Azure provides the compute capacity.

The integration uses the following flow:

1. IBM Spectrum Symphony evaluates queued jobs, workload priorities, policies, and resource demand.
2. Host Factory sends the resource requirements to the Azure resource connector.
3. The resource connector translates the requirements into an Azure Compute Fleet API request.
4. Azure Compute Fleet selects eligible virtual machine (VM) types and a mix of Spot and pay-as-you-go capacity.
5. The provisioned VMs join the Symphony cluster as execution hosts and run queued jobs.
6. As demand decreases, Symphony can release the Azure resources.

Symphony manages the workload and its policies. Azure Compute Fleet manages access to the underlying compute capacity.

The provider uses [Azure Compute Fleet Launch mode](/en-us/azure/azure-compute-fleet/launch-mode). Launch mode provisions VMs in a single request and then hands off their lifecycle to Symphony. The fleet resource is deleted automatically after provisioning, but the VMs continue to run until Symphony releases them.

## Key capabilities

The integration provides the following capabilities:

- **Dynamic scaling:** Provision and scale Azure compute capacity as workload demand changes.
- **Policy-driven elasticity:** Maintain existing workload priorities and service-level objectives when you extend workloads to Azure.
- **Flexible VM selection:** Provision across eligible Azure VM families based on workload requirements.
- **Flexible purchasing:** Combine [Azure Spot Virtual Machines](spot-vms) and pay-as-you-go VMs.
- **Hybrid orchestration:** Extend an existing Symphony environment to Azure without replacing your workload orchestration processes.
- **Workload-based provisioning:** Select capacity based on attributes such as virtual CPU (vCPU), memory, and storage.

Azure Compute Fleet can use multiple VM types and allocation strategies to optimize for cost, capacity, or both. This flexibility increases the range of eligible capacity compared to requesting a single VM size.

## Workload scenarios

Use the integration for compute-intensive and data-intensive distributed applications that benefit from elastic batch capacity. Example scenarios include:

- Electronic design automation.
- Engineering analysis.
- Financial risk calculations.
- Scientific computing.

## Considerations

Before you use the integration, consider the following factors:

- Subscription, region, and VM family determine the standard Azure VM and vCPU quotas that apply. Azure Compute Fleet doesn't increase these quotas.
- Spot VMs can be evicted when Azure needs the capacity or when the price exceeds the maximum price you set. Design workloads to tolerate interruptions.
- Available VM types and capacity vary by Azure region.
- Your IBM Spectrum Symphony licensing and support terms apply to the Symphony environment and provider plugin.