---
layout: Conceptual
title: Create a virtual machine on VMware vSphere using Azure Arc - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/vmware-vsphere/create-virtual-machine
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
description: This article helps you create a virtual machine using Azure portal.
ms.date: 2026-10-08T00:00:00.0000000Z
ms.topic: how-to
ms.services: azure-arc
ms.subservice: vmware-vsphere-azure-arc
ms.reviewer: v-gajeronika
keywords: VMware, Arc, Azure
locale: en-us
document_id: 7ed7e20d-c86a-fa59-a60c-6327fd30796d
document_version_independent_id: d8fe635c-0b49-5880-fe4e-912ecd667b3b
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/vmware-vsphere/create-virtual-machine.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/vmware-vsphere/create-virtual-machine
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/vmware-vsphere/create-virtual-machine.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: b7201396-8011-64f4-0969-61c6ea9c843c
---

# Create a virtual machine on VMware vSphere using Azure Arc - Azure Arc | Microsoft Learn

After your administrator connects a VMware vCenter server to Azure, enables vCenter resources such as resource pools, clusters, hosts, VM templates, and VM networks in Azure, and gives you the required permissions on those resources, you can create a new VMware vCenter managed virtual machine.

In this article, you learn how to create a new VMware vCenter managed virtual machine from Azure Arc portal. To explore non-portal methods such as Azure CLI, PowerShell, REST APIs, SDKs, and Infrastructure-as-Code mechanisms, see the **Reference** section of this documentation.

## Prerequisites

- An Azure subscription and resource group where you have *Azure Arc VMware VM Contributor* role.
- A resource pool, cluster, or host resource where you have *Azure Arc VMware Private Cloud Resource User* role.
- A virtual machine template resource where you have *Azure Arc VMware Private Cloud Resource User* role.
- A virtual network resource where you have *Azure Arc VMware Private Cloud Resource User* role.
- A datastore resource where you have *Azure Arc VMware Private Cloud Resource User* role.

## Create a VM in Azure portal

1. Go to [Azure portal](https://portal.azure.com/).
2. Start creating a new VM by using one of the following two methods:

    - Select **Azure Arc** as the service. Under **Host environments**, select **VMware vCenters**. Search and select your VMware vCenters. Select **Virtual machines** under **vCenter inventory** from the left blade and select **Add**.

        [![Screenshot of Add screen.](media/create-virtual-machine/add.png)](media/create-virtual-machine/add.png#lightbox)

    Or

    - Select **Azure Arc** as the service. Under **Azure Arc resources**, select **Machine**. Select **Add/Create** and select **Create a machine in a connected host environment** from the dropdown.

        [![Screenshot of create a machine screen.](media/create-virtual-machine/create-machine.png)](media/create-virtual-machine/create-machine.png#lightbox)
3. When **Create an Azure Arc virtual machine** opens, under **Basics** &gt; **Project details**, select the **Subscription** and **Resource group** where you want to deploy the VM.
4. Under **Instance details**, enter the following information:

    - **Virtual machine name** - Specify the name of the virtual machine.
    - **Custom location** - Select the custom location that your administrator shares with you.
    - **Virtual machine kind** - Select **VMware**.
    - **Resource pool/cluster/host** - Select a resource pool, cluster, or host from the dropdown menu.
    - **Datastore** - Select a datastore from the dropdown menu.

        [![Screenshot of machines screen.](media/create-virtual-machine/machines.png)](media/create-virtual-machine/machines.png#lightbox)
5. Under **Template details**, enter the following information:

    - **Template** - Choose the VM template for deployment.
    - **Override template defaults** - Select the checkbox to override the default CPU cores and memory on the VM templates.
    - Specify computer name for the VM if the VM template has computer name associated with it.
6. Keep the **Arc agent with virtual hardware management** option selected to automatically install Azure connected machine agent immediately after the creation of the VM. [Azure connected machine agent (Arc agent)](../servers/agent-overview) is required if you're planning to use Azure management services to govern, patch, monitor, and secure your VM through Azure. Select the **Virtual hardware management only** option if you plan to install the Arc agent manually later or if you plan to use only Azure-based VM CRUD capabilities without consuming Azure services.
7. Under **Administrator account**, enter the following information:

    - Username
    - Password
    - Confirm password

    [![Screenshot of Arc onboarding choice screen.](media/create-virtual-machine/manage-arc-onboarding.png)](media/create-virtual-machine/manage-arc-onboarding.png#lightbox)

    If you're creating a Linux virtual machine, you have an option to use an SSH key as the authentication method.
8. If you chose to install the Arc agent, choose the **Connectivity method** for the Arc agent to connect to Azure. The available options are Public endpoint, Proxy server, and Private endpoint.

    - To connect the Arc agent through a proxy, provide the proxy server details.
    - To connect Arc agent through a private endpoint, follow these steps to set up Azure private link and provide the same details.
9. Under **Disks**, you can optionally change the disks configured in the template. You can add more disks or update existing disks.

    [![Screenshot of Disks tab screen.](media/create-virtual-machine/disks.png)](media/create-virtual-machine/disks.png#lightbox)
10. Under **Networking**, you can optionally change the network interfaces configured in the template. You can add Network interface cards (NICs) or update the existing NICs. You can also change the network that this NIC attaches to, provided you have appropriate permissions to the network resource.

    [![Screenshot of Networking tab screen.](media/create-virtual-machine/networking.png)](media/create-virtual-machine/networking.png#lightbox)
11. Under **Advanced**, customize the guest operating system settings of the VM as required.

    [![Screenshot of Advanced tab screen.](media/create-virtual-machine/advanced.png)](media/create-virtual-machine/advanced.png#lightbox)
12. Under **Tags**, you can optionally add tags to the VM resource.

    [![Screenshot of Tags tab screen.](media/create-virtual-machine/tags.png)](media/create-virtual-machine/tags.png#lightbox)
13. Under **Review + create**, review all the properties and select **Create**. The portal creates the VM in a few minutes.