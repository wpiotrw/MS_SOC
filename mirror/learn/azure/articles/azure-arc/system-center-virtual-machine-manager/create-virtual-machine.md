---
layout: Conceptual
title: Create a virtual machine on System Center Virtual Machine Manager using Azure Arc - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/create-virtual-machine
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
description: This article helps you create a SCVMM-managed on-premises virtual machine using Azure portal.
ms.date: 2026-09-24T00:00:00.0000000Z
ms.topic: how-to
ms.services: azure-arc
ms.subservice: azure-arc-scvmm
keywords: VMM, Arc, Azure
ms.custom:
- build-2025
locale: en-us
document_id: b477db4d-6df5-8ae1-7938-84dc141f2888
document_version_independent_id: b2d5ef5a-f250-d07f-43cb-d79726f61f07
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/system-center-virtual-machine-manager/create-virtual-machine.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/system-center-virtual-machine-manager/create-virtual-machine
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/system-center-virtual-machine-manager/create-virtual-machine.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/c89972e1-0a93-4ce3-b588-9c24d08ca424
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b2144970-2aee-47fb-9df2-af491ca710ec
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 86951dcb-bd46-0282-60ae-56e20beb7bf0
---

# Create a virtual machine on System Center Virtual Machine Manager using Azure Arc - Azure Arc | Microsoft Learn

Note

Azure Arc-enabled SCVMM retires in September 2029. If you're using Azure Arc-enabled SCVMM, transition to [Azure Arc-enabled Servers](/en-us/azure/azure-arc/servers/overview) or contact arc-vmm-feedback@microsoft.com. For more information, see the [transition guidance](transition-guidance).

After your administrator connects an SCVMM management server to Azure, enables VMM resources such as VMM clouds, VM templates, and VM networks in Azure, and gives you the required permissions on those resources, you can create a new SCVMM managed virtual machine in Azure.

In this article, you learn how to create a new SCVMM managed virtual machine from Azure Arc portal. To explore non-portal methods such as Azure CLI, PowerShell, REST APIs, SDKs, and Infrastructure-as-Code mechanisms, see the **Reference** section of this documentation.

## Prerequisites

- An Azure subscription and resource group where you have *Azure Arc SCVMM VM Contributor* role.
- A cloud resource on which you have *Azure Arc SCVMM Private Cloud Resource User* role.
- A virtual machine template resource on which you have *Azure Arc SCVMM Private Cloud Resource User* role.
- A virtual network resource on which you have *Azure Arc SCVMM Private Cloud Resource User* role.

## Create a VM in Azure portal

1. Go to Azure portal.
2. Start creating a new VM by using one of the following methods:

    - Select **Azure Arc** as the service. Under **Host environments**, select **SCVMM management servers**. Search for and select your SCVMM management server. Under **SCVMM inventory**, select **Virtual machines** and select **Add**.

        ![Screenshot of Add screen.](media/create-virtual-machine/add.png)

    Or

    - Select **Azure Arc** as the service. Under **Azure Arc resources**, select **Machine**. Select **Add/Create** and select **Create a machine in a connected host environment**.

        ![Screenshot of create a machine screen.](media/create-virtual-machine/create-machine.png)
3. When **Create an Azure Arc virtual machine** opens, under **Basics** &gt; **Project details**, select the **Subscription** and **Resource group** where you want to deploy the VM.
4. Under **Instance details**, enter the following information:

    - **Virtual machine name** - Specify the name of the virtual machine.
    - **Custom location** - Select the custom location that your administrator shares with you.
    - **Virtual machine kind** - Select **System Center Virtual Machine Manager**.
    - **Cloud** - Select the target VMM private cloud.
    - **Availability set** - (Optional) Use availability sets to identify virtual machines that you want VMM to keep on separate hosts for improved continuity of service.

        ![Screenshot of machines screen.](media/create-virtual-machine/machines.png)
5. Under **Template details**, enter the following information:

    - **Template** - Choose the VM template for deployment.
    - **Override template defaults** - Select the checkbox to override the default CPU cores and memory on the VM templates.
    - Specify computer name for the VM if the VM template has computer name associated with it.

        ![Screenshot of template details screen.](media/create-virtual-machine/template-details.png)
6. Keep the **Enable Guest Management** checkbox selected to automatically install Azure connected machine agent immediately after the creation of the VM. [Azure connected machine agent (Arc agent)](../servers/agent-overview) is required if you're planning to use Azure management services to govern, patch, monitor, and secure your VM through Azure.
7. Under **Administrator account**, enter the following information and select **Next : Disks &gt;**.

    - Username
    - Password
    - Confirm password

    ![Screenshot of administrator account screen.](media/create-virtual-machine/admin-account.png)
8. Under **Disks**, you can optionally change the disks configured in the template. You can add more disks or update existing disks.

    ![Screenshot of Disks tab screen.](media/create-virtual-machine/disks.png)
9. Under **Networking**, you can optionally change the network interfaces configured in the template. You can add Network interface cards (NICs) or update the existing NICs. You can also change the network that this NIC attaches to, if you have appropriate permissions to the network resource.

    ![Screenshot of Networking tab screen.](media/create-virtual-machine/networking.png)
10. Under **Advanced**, enable processor compatibility mode if required.

    ![Screenshot of Advanced tab screen.](media/create-virtual-machine/advanced.png)
11. Under **Tags**, you can optionally add tags to the VM resource.

    ![Screenshot of Tags tab screen.](media/create-virtual-machine/tags.png)
12. Under **Review + create**, review all the properties and select **Create**. The VM is created in a few minutes.