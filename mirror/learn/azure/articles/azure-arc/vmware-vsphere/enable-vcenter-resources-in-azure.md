---
layout: Conceptual
title: Onboard your VMware vCenter resources in Azure - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/vmware-vsphere/enable-vcenter-resources-in-azure
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
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
author: Jeronika-MS
learn_banner_products:
- azure
ms.author: v-gajeronika
ms.service: azure-arc
description: Learn how to browse your vCenter inventory and represent a subset of your VMware vCenter resources in Azure to enable self-service.
ms.topic: how-to
ms.date: 2026-10-06T00:00:00.0000000Z
ms.subservice: vmware-vsphere-azure-arc
ms.reviewer: v-gajeronika
locale: en-us
document_id: 95b2aca5-62f5-60fa-6aa5-59036dc4894c
document_version_independent_id: f91b656c-b51a-ff57-b105-2c8fa5f315b7
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/vmware-vsphere/enable-vcenter-resources-in-azure.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/vmware-vsphere/enable-vcenter-resources-in-azure
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/vmware-vsphere/enable-vcenter-resources-in-azure.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: 281a3fdf-c03a-1036-2821-233227c19999
---

# Onboard your VMware vCenter resources in Azure - Azure Arc | Microsoft Learn

After you connect your VMware vCenter to Azure, you can browse your vCenter inventory from the Azure portal.

[![Screenshot of where to browse your VMware Inventory from the Azure portal.](media/enable-vcenter-resources/browse-vmware-inventory.png)](media/enable-vcenter-resources/browse-vmware-inventory.png#lightbox)

To view all the connected vCenters, visit the VMware vCenter blade in Azure Arc center. From there, you can browse your virtual machines (VMs), resource pools, templates, networks, and datastores. From the inventory of your vCenter resources, you can select and onboard one or more resources in Azure through Azure Arc. When you onboard a vCenter resource in Azure, it creates an Azure resource that represents your vCenter resource. You can use this Azure resource to assign permissions or conduct management operations.

## Onboard resource pools, clusters, hosts, datastores, networks, and VM templates in Azure

In this section, you onboard resource pools, networks, and other non-VM resources in Azure.

Note

Onboarding a VMware vSphere resource on Azure Arc is a read-only operation on vCenter. That is, it doesn't make changes to your resource in vCenter.

Note

To onboard VM templates, VMware tools must be installed on them. If not installed, the **Manage Arc onboarding** option is grayed out.

1. From your browser, go to the vCenters blade on [Azure Arc Center](https://portal.azure.com/#blade/Microsoft_Azure_HybridCompute/AzureArcCenterBlade/overview) and navigate to your inventory resources blade.
2. Select the resource or resources you want to onboard and then select **Manage Arc onboarding**.
3. Select your Azure Subscription and Resource Group and then select **Onboard**.

    This starts a deployment and creates a resource in Azure, creating representations for your VMware vSphere resources. It allows you to manage who can access those resources through Azure role-based access control (RBAC) granularly.
4. Repeat these steps for one or more network, resource pool, and VM template resources.

## Onboard existing virtual machines in Azure

1. From your browser, go to the vCenters blade on [Azure Arc Center](https://portal.azure.com/#blade/Microsoft_Azure_HybridCompute/AzureArcCenterBlade/overview) and navigate to your vCenter.

    [![Screenshot of how to enable an existing virtual machine in the Azure portal.](media/enable-vcenter-resources/onboard-virtual-machines.png)](media/enable-vcenter-resources/onboard-virtual-machines.png#lightbox)
2. Go to the VM inventory resource blade, select the VMs you want to onboard, and then select **Manage Arc onboarding**.
3. Select your Azure subscription and resource group.
4. Select **Arc agent with virtual hardware management** and then provide the Administrator username and password of the VM. For Linux VMs, there's an option to use SSH key-based authentication.

    The Arc agent is the [Azure Arc connected machine agent](../servers/agent-overview). For information about the prerequisites for installing the Arc agent, see [Connected Machine agent prerequisites](../servers/prerequisites).

    Alternatively, you can choose not to install this agent by selecting **Virtual hardware management only**.
5. Select **Onboard** to start the deployment of the VM represented in Azure.

For information about the capabilities enabled by the Arc agent, see [supported operations](../servers/cloud-native/overview).

Note

Moving VMware vCenter resources between resource groups and subscriptions isn't currently supported.