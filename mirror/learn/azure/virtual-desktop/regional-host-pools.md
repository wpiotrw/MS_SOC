---
layout: Conceptual
title: Regional Host Pools - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/regional-host-pools
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: TomHickling
manager: eliotgra
ms.author: thhickli
ms.service: azure-virtual-desktop
description: A guide to regional host pools
ms.topic: article
ms.date: 2025-10-17T00:00:00.0000000Z
locale: en-us
document_id: 19913212-2ade-fb7f-7068-c459c4e56b58
document_version_independent_id: 19913212-2ade-fb7f-7068-c459c4e56b58
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/regional-host-pools.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: regional-host-pools
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/regional-host-pools.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 19fa899a-05f8-7a5d-6903-3cc01836a253
---

# Regional Host Pools - Azure Virtual Desktop | Microsoft Learn

Azure Virtual Desktop now supports Regional host pools. These are new host pools where the metadata is stored in a more resilient manner that reduces the impact of any future database or Azure region outages. These host pools use a new and different set of backend infrastructure, and as such will coexist side by side with the existing "geographical" host pools. At a future date the ability to create new geographical host pools will be deprecated. During this coexistence period, both types of host pools aren't interoperable.

### What are Regional host pools?

Regional host pools are a new type of host pool that uses a different set of underlying infrastructure provided by the Azure Virtual Desktop service. This infrastructure removes cross-region dependencies thereby reducing the impact of any Azure region or Azure Virtual Desktop database outages. They increase the resiliency and availability of customer connectivity to the session hosts running end user workloads. There are no functional differences between the two types of host pool.

Note

Errors and checkpoints are not being reported into Log Analytics for regional session hosts.

### What are the benefits of Regional host pools?

The main benefits of the new regional host pools are the increased resiliency inherent in the underlying infrastructure architecture. As well as the control provided allowing you to define your data sovereignty requirements by aligning your host pool metadata with each of the Azure regions supported. We strongly recommend that when this service becomes generally available that you create all new host pools as regional host pools to take full advantage of these benefits. As well as consider transitioning your existing geographical host pools over to regional.

### Where can you use Regional host pools?

Two regions are currently supported: East US 2 and Central US. When this service reaches general availability, it commences a gradual rolling deployment across multiple Azure regions. See [Data Locations for Azure Virtual Desktop](/en-us/azure/virtual-desktop/data-locations) for available regions supporting Regional databases.

### Limitations of Regional host pools

As the metadata for new regional host pools exists within a separate set of infrastructure, Azure Virtual Desktop objects have a new -DeploymentScope parameter with values of either "geographical" or "regional", and only objects with the same deployment scope can be associated together. For example, it will not be possible to join new regional application groups to existing geographical workspaces or vice versa. Only objects of the same deployment scope can be associated together. Application groups created in regional host pools will automatically be regional, and only regional application groups can be associated with regional workspaces. Likewise, geographic application groups can only be associated with geographical objects.

### Create a regional host pool

##### PowerShell

The new DeploymentScope parameter has been added to the [5.4.5-preview version of the Az.DesktopVirtualization module](https://powershellgallery.com/packages/Az.DesktopVirtualization/5.4.5-preview). Once installed you just need to add the -DeploymentScope parameter to your PowerShell commands. When creating a new regional host pool your command would include:

`New-AzWvdHostPool -DeploymentScope Regional....`

If you're deploying a normal geographical host pool use the value of Geographical in place of Regional. This parameter isn't required, so if this is not set the deployment defaults to Geographical.

##### Azure portal

There's only one new step required to create a new regional host pool. A new field called Deployment Scope (Preview) has been introduced. This parameter controls whether the Azure Virtual Desktop objects being created are geographical or regional. This drop-down box has two options: geographical or regional. Selecting geographical will create existing geographical host pools. Selecting regional creates new regional host pools. This dropdown box is only active if you have selected an Azure region that also has the new regional infrastructure present, currently only East US 2, and Central US during preview.

![Screenshot of regional host pools setting in the Intune portal.](media/regional-host-pools/image.png)

To create a regional host pool using the Azure portal:

1. Sign in to the Azure portal.
2. In the search bar, enter **Azure Virtual Desktop** and select the matching service entry.
3. Select **Host pools**, then select **Create**.
4. On the **Basic** tab, complete the following information:

| Parameter | Value/Description |
| --- | --- |
| **Subscription** | In the dropdown list, select the subscription where you want to create the host pool. |
| **Resource group** | Select an existing resource group, or select **Create new** and enter a name. |
| **Host pool name** | Enter a name for the host pool, such as **hp01**. |
| **Location** | Select the Azure region where you want to create your host pool. During the preview only East US 2 and Central US support regional host pools. Select either of these regions. When selecting any other region the Deployment Scope field is not shown. |
| **Deployment scope** | Select Regional to create a regional host pool. This drop-down box is only active when selecting either East US 2 or Central US. Selecting geographical will result in a normal geographical host pool. |
| **Validation environment** | Select whether you want this host pool to be a validation host pool or not. |
| **Preferred app group type** | Select the [preferred application group type](terminology#application-groups) for this host pool: **Desktop** or **RemoteApp**. A desktop application group is created automatically when you use the Azure portal. |
| **Host pool type** | Select whether you want your host pool to be **Pooled** or **Personal**.If you select **Pooled**, two new options appear for **Load balancing algorithm** and **Max session limit**.<br><br>Expand this section for the pooled options.<br>- For **Load balancing algorithm**, choose either **breadth-first** or **depth-first**, based on your usage pattern.- For **Max session limit**, enter the maximum number of users that you want load-balanced to a single session host. For more information, see [Host pool load-balancing algorithms](host-pool-load-balancing).<br>If you select **Personal**, two new options appear for **Assignment type** and **Assign multiple desktops to a single user**.<br><br>Expand this section for the personal options.<br>For **Assignment type**, select **Automatic** for the service to assign any personal desktop not already assigned to a user, or select **Direct** to assign a specific personal desktop to a user. With the **Direct** assignment type you can also check the box to **Assign multiple desktops to a single user**. For more information, see [Assign multiple personal desktops to a single user](configure-host-pool-personal-desktop-assignment-type#assign-multiple-personal-desktops-to-a-single-user). |

Once you complete this tab, select Next: **Session hosts**.

1. On the **Session hosts** tab, complete the following information, which is captured in a session host configuration and used to create session hosts.

| Parameter | Value/Description |
| --- | --- |
| **Add virtual machines** | Select **Yes**. This action shows several new options. |
| **Resource group** | This value defaults to the resource group that you chose to contain your host pool on the **Basics** tab, but you can select an alternative. |
| **Name prefix** | Enter a name prefix for your session hosts, such as **hp01-sh**.Each session host has a suffix of a hyphen and then a sequential number added to the end, such as **hp01-sh-0**.This name prefix can be a maximum of 11 characters and is used in the computer name in the operating system. The prefix and the suffix combined can be a maximum of 15 characters. Session host names must be unique. |
| **Virtual machine type** | Select **Azure virtual machine**. |
| **Virtual machine location** | Select the Azure region where you want to deploy your session hosts. This value must be the same region that contains your virtual network. |
| **Availability options** | Select from [availability zones](/en-us/azure/reliability/availability-zones-overview), [availability set](/en-us/azure/virtual-machines/availability-set-overview), or **No infrastructure redundancy required**. If you select **availability zones** or **availability set**, complete the extra parameters that appear. |
| **Security type** | Select from **Standard**, [Trusted launch virtual machines](/en-us/azure/virtual-machines/trusted-launch), or [Confidential virtual machines](/en-us/azure/confidential-computing/confidential-vm-overview).- If you select **Trusted launch virtual machines**, options for **secure boot** and **vTPM** are automatically selected.- If you select **Confidential virtual machines**, options for **secure boot**, **vTPM**, and **integrity monitoring** are automatically selected. You can't opt out of vTPM when using a confidential VM. |
| **Image** | Select the OS image that you want to use from the list, or select **See all images** to see more. The full list includes any images that you created and stored as an [Azure Compute Gallery shared image](/en-us/azure/virtual-machines/shared-image-galleries) or a [managed image](/en-us/azure/virtual-machines/windows/capture-image-resource). |
| **Virtual machine size** | Select a size. If you want to use a different size, select **Change size**, and then select from the list. |
| **Number of VMs** | Enter the number of virtual machines that you want to deploy. You can deploy up to 400 session hosts at this point if you want (depending on your [subscription quota](/en-us/azure/quotas/view-quotas)), or you can add more later.For more information, see [Azure Virtual Desktop service limits](/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-virtual-desktop-service-limits) and [Virtual Machines limits](/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-virtual-machines-limits---azure-resource-manager). |
| **OS disk type** | Select the disk type to use for your session hosts. During preview, only **Standard SSD** is supported and is automatically selected once ephemeral OS disks are configured. |
| **OS disk size** | Select a size for the OS disk.If you enable hibernation, ensure that the OS disk is large enough to store the contents of the memory in addition to the OS and other applications. |
| **Boot Diagnostics** | Select whether you want to enable [boot diagnostics](/en-us/azure/virtual-machines/boot-diagnostics). |
| **Network and security** |  |
| **Virtual network** | Select your virtual network. An option to select a subnet appears. |
| **Subnet** | Select a subnet from your virtual network. |
| **Network security group** | Select whether you want to use a network security group (NSG).- **None** doesn't create a new NSG.- **Basic** creates a new NSG for the VM network adapter.- **Advanced** enables you to select an existing NSG.You don't need to open inbound ports to connect to Azure Virtual Desktop. Learn more at [Understanding Azure Virtual Desktop network connectivity](network-connectivity). |
| **Public inbound ports** | You can select a port to allow from the list. Azure Virtual Desktop doesn't require public inbound ports, so we recommend that you select **No**. |
| **Domain to join** |  |
| **Select which directory you would like to join** | Select from **Microsoft Entra ID** or **Active Directory**, and complete the relevant parameters for the selected option. |
| **Virtual Machine Administrator account** |  |
| **Username** | Enter a name to use as the local administrator account for the new session hosts. For more information, see [What are the username requirements when creating a VM?](/en-us/azure/virtual-machines/windows/faq#what-are-the-username-requirements-when-creating-a-vm-) |
| **Password** | Enter a password for the local administrator account. For more information, see [What are the password requirements when creating a VM?](/en-us/azure/virtual-machines/windows/faq#what-are-the-password-requirements-when-creating-a-vm-) |
| **Confirm password** | Reenter the password. |
| **Custom configuration** |  |
| **Custom configuration script URL** | If you want to run a PowerShell script during deployment, you can enter the URL here. |

1. Once you complete this tab, select **Next: Workspace &gt;** to continue configuring your Workspace and other optional configuration or select **Review + Create**.
2. On the Review + create tab, ensure validation passes and review the information that is during deployment.
3. Select Create to create the host pool.