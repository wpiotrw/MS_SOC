---
layout: Conceptual
title: Azure Arc overview - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/overview
breadcrumb_path: ../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.service: azure-arc
description: Learn about what Azure Arc is and how it helps customers enable management and governance of their hybrid resources with other Azure services and features.
ms.date: 2025-08-26T00:00:00.0000000Z
ai-usage: ai-assisted
ms.topic: overview
author: davidsmatlak
ms.author: davidsmatlak
locale: en-us
document_id: 6c0c36de-1d68-dad7-3218-d3e33fb8145b
document_version_independent_id: 32a28486-8028-b727-c742-437f6505e720
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/overview.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 183da6f4-0dd8-236e-5e69-be87767e63e7
---

# Azure Arc overview - Azure Arc | Microsoft Learn

Today, companies struggle to control and govern increasingly complex environments that extend across data centers, multiple clouds, and edge. Each environment and cloud possesses its own set of management tools, and new DevOps and ITOps operational models can be hard to implement across resources.

Azure Arc simplifies governance and management by delivering a consistent multicloud and on-premises management platform.

Azure Arc provides a centralized, unified way to:

- Manage your entire environment together by projecting your existing non-Azure and/or on-premises resources into Azure Resource Manager.
- Manage virtual machines, Kubernetes clusters, and databases as if they are running in Azure.
- Use familiar Azure services and management capabilities, regardless of where your resources live.
- Continue using traditional ITOps while introducing DevOps practices to support new cloud native patterns in your environment.
- Configure custom locations as an abstraction layer on top of Azure Arc-enabled Kubernetes clusters and cluster extensions.

[![Diagram showing the Azure Arc management control plane.](media/overview/azure-arc-control-plane.png)](media/overview/azure-arc-control-plane.png#lightbox)

*To download architecture diagrams in high resolution, visit [Jumpstart Gems](https://aka.ms/JumpstartGems_Docs).*

Currently, Azure Arc allows you to manage the following resource types hosted outside of Azure:

- [Servers](servers/overview) and virtual machines: Manage Windows and Linux physical servers and virtual machines hosted outside of Azure. Provision, resize, delete, and manage virtual machines based on [Azure Local](/en-us/azure/azure-local/manage/azure-arc-vm-management-overview) and on [VMware vCenter](vmware-vsphere/overview) or [System Center Virtual Machine Manager](system-center-virtual-machine-manager/overview) managed on-premises environments.
- [Kubernetes clusters](kubernetes/overview): Attach and configure Kubernetes clusters running anywhere, with multiple supported distributions.
- [Azure data services](data/overview): Run SQL Managed Instance on-premises, at the edge, and in public clouds using Kubernetes and the infrastructure of your choice.
- [SQL Server](/en-us/sql/sql-server/azure-arc/overview): Extend Azure services to SQL Server instances hosted outside of Azure.

Note

For more information regarding the different services Azure Arc offers, see [Choosing the right Azure Arc service for machines](/en-us/azure/azure-arc/choose-service).

### Indirectly connected mode

As of September, 2025 indirectly connected mode is retired.

## Key features and benefits

Some of the key scenarios that Azure Arc supports are:

- Implement consistent inventory, management, governance, and security for servers across your environment.
- Configure [Azure VM extensions](servers/manage-vm-extensions) to use Azure management services to monitor, secure, and update your servers.
- Manage and govern Kubernetes clusters at scale.
- [Use GitOps to deploy configurations](kubernetes/conceptual-gitops-flux2) across one or more clusters from Git repositories.
- Zero-touch compliance and configuration for Kubernetes clusters using Azure Policy.
- Run [Azure data services](kubernetes/custom-locations) on any Kubernetes environment as if it runs in Azure (specifically Azure SQL Managed Instance, with benefits such as upgrades, updates, security, and monitoring). Use elastic scale and apply updates without any application downtime, even without continuous connection to Azure.
- Create [custom locations](kubernetes/custom-locations) on top of your [Azure Arc-enabled Kubernetes](kubernetes/overview) clusters, using them as target locations for deploying Azure services instances. Deploy your Azure service cluster extensions for [Azure Arc-enabled data services](data/create-data-controller-direct-azure-portal), [Azure Container Apps on Azure Arc](/en-us/azure/container-apps/azure-arc-overview), and [Event Grid on Kubernetes](/en-us/azure/event-grid/kubernetes/overview).
- Perform virtual machine lifecycle and management operations on [Azure Local](/en-us/azure/azure-local/manage/azure-arc-vm-management-overview) and on-premises environments managed by [VMware vCenter](vmware-vsphere/overview) and [System Center Virtual Machine Manager (SCVMM)](system-center-virtual-machine-manager/overview) through interactive and non-interactive methods. Empower developers and application teams to self-serve VM operations on-demand using Azure role-based access control (RBAC).
- A unified experience viewing your Azure Arc-enabled resources, whether you are using the Azure portal, the Azure CLI, Azure PowerShell, or Azure REST API.

## Pricing

Below is pricing information for the features available today with Azure Arc.

### Azure Arc-enabled servers

The following Azure Arc control plane functionality is offered at no extra cost:

- Resource organization through Azure management groups and tags
- Searching and indexing through Azure Resource Graph
- Access and security through Azure Role-based access control (RBAC)
- Environments and automation through templates and extensions

Any Azure service that is used on Azure Arc-enabled servers, such as Microsoft Defender for Cloud or Azure Monitor, will be charged as per the pricing for that service. For more information, see the [Azure pricing page](https://azure.microsoft.com/pricing/).

### Azure Arc-enabled VMware vSphere and System Center Virtual Machine Manager

The following Azure Arc-enabled VMware vSphere and System Center Virtual Machine Manager (SCVMM) capabilities are offered at no extra cost:

- All the Azure Arc control plane functionalities that are offered at no extra cost with Azure Arc-enabled servers.
- Discovery and single pane of glass inventory view of your VMware vCenter and SCVMM managed estate (VMs, templates, networks, datastores, clouds/clusters/hosts/resource pools).
- Lifecycle (create, resize, update, and delete) and power cycle (start, stop, and restart) operations of VMs, including the ability to delegate self-service access for these operations using Azure role-based access control (RBAC).
- Management of VMs using Azure portal, CLI, REST APIs, SDKs, and automation through Infrastructure as Code (IaC) templates such as ARM, Terraform, and Bicep.

Any Azure service that is used on Azure Arc-enabled VMware vSphere and SCVMM VMs, such as Microsoft Defender for Cloud or Azure Monitor, will be charged as per the pricing for that service. For more information, see the [Azure pricing page](https://azure.microsoft.com/pricing/).

### Azure Arc-enabled Kubernetes

Any Azure service that is used on Azure Arc-enabled Kubernetes, such as Microsoft Defender for Cloud or Azure Monitor, will be charged as per the pricing for that service.

For more information on pricing for configurations on top of Azure Arc-enabled Kubernetes, see the [Azure pricing page](https://azure.microsoft.com/pricing/).

### Azure Arc-enabled data services

For information, see the [Azure pricing page](https://azure.microsoft.com/pricing/).

## Azure Arc and the adaptive cloud approach

Azure Arc is a key part of Microsoft’s [adaptive cloud](https://azure.microsoft.com/solutions/adaptive-cloud) approach. This approach helps organizations run and manage apps and services across many environments, including Azure, other cloud providers, on-premises datacenters, and edge locations. Azure Arc supports this approach by extending Azure’s management, security, and governance tools to resources outside Azure. This ability makes it easier to keep operations consistent and secure, no matter where your workloads run.