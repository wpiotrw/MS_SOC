---
layout: Conceptual
title: Ephemeral OS disks on Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/deploy/session-hosts/ephemeral-os-disks
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: rocolem
manager: eliotgra
ms.author: rocolem
ms.service: azure-virtual-desktop
description: Azure Virtual Desktop supports Ephemeral OS disks, enabling stateless workloads with improved performance and efficiency. These disks use local VM storage, eliminating persistence in remote Azure Storage. This architecture reduces latency for read/write operations and accelerates VM reimaging. Disk placement is controlled via the DiffDiskPlacement property, allowing configuration on either the OS cache or temp disk. Additionally, the Windows VM page file is optimized to reside on the OS disk. These enhancements make Ephemeral OS disks a strategic choice for high-performance, non-persistent virtual desktop environments.
ms.topic: article
ms.date: 2025-10-14T00:00:00.0000000Z
locale: en-us
document_id: e54301d0-47fb-7243-7328-dbf23e0cc435
document_version_independent_id: e54301d0-47fb-7243-7328-dbf23e0cc435
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/deploy/session-hosts/ephemeral-os-disks.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: ../../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: deploy/session-hosts/ephemeral-os-disks
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/deploy/session-hosts/ephemeral-os-disks.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 8a56bb74-9e32-6bd2-2409-a0e8732767f0
---

# Ephemeral OS disks on Azure Virtual Desktop - Azure Virtual Desktop | Microsoft Learn

Azure Virtual Desktop now supports [Ephemeral OS disks](/en-us/azure/virtual-machines/ephemeral-os-disks), providing several advantages for stateless workloads. Ephemeral OS disks utilize local virtual machines (VM) storage, placing the operating system on the VMs local storage, rather than remote storage which is not preserved in remote Azure Storage, enabling non-persistence for virtual machines. This setup results in lower latency for read/write operations and allows for quicker reimaging of VMs.

Ephemeral OS disks can be placed on either the VMs OS cache or the VM's temp disk. This placement is determined by the DiffDiskPlacement property, which specifies the desired location. Additionally, when provisioning a Windows VM, the page file is configured to reside on the OS Disk, further optimizing performance.

### Key Features of Ephemeral OS Disks

- Optimized for stateless workloads, as VMs using Ephemeral OS disks can't be deallocated only restarted, reimaged, or deleted.
- Provides high input/output operations per second (IOPS) and low latency by performing read/write operations directly on the VM’s local storage.
- Supported for on all images types, including Marketplace, custom images, and Azure Compute Gallery.
- Fast reset and reimage capability, allowing VMs and scale set instances to return to their original boot state.

### Limitations of Ephemeral OS Disks

The following features aren't supported with Ephemeral OS disks:

- Deallocation of VMs
- Capturing VM images
- Disk snapshots
- Azure Disk Encryption
- Azure Backup
- Azure Site Recovery
- OS Disk Swap

Note

- Ephemeral OS disks in Azure Virtual Desktop are supported only in [pooled host pools configured with session host configuration](../../deploy-azure-virtual-desktop).
- Ephemeral OS disks aren't supported with NVMe and premium SSD during preview.
- Ephemeral OS disks are only available in Azure and are not supported in Azure Government during preview.

### Size Requirements

You can choose to deploy ephemeral OS disk on temp disk, or cache on the VM. The image OS disk size should be less than or equal to the temp/cache size available on the VM size chosen.

For **OS cache placement**: Standard Windows Server images from the marketplace are 127 GiB, which means that you need a VM size that has a cache equal to or larger than 127 GiB. The Standard\_DS3\_v2 has a cache size of 127 GiB, which is large enough. In this case, the Standard\_DS3\_v2 is the smallest size in the DSv2 series that you can use with this image.

For **Temp disk placement**: Windows 11 Enterprise multi-session image from the marketplace is 127 GiB. To enable an ephemeral OS disk on temp, the temp disk size must be equal to or larger than 127 GiB. Standard\_D8s\_v3 has a temp size of 200 GiB, which can fit the 127‑GiB OS disk. Upon creation of the VM, the remaining temp disk space would be about 73 GiB.

### Dynamic Autoscaling Recommendations

When configuring host pools that include session hosts with Ephemeral OS disks, it's recommended to use [Dynamic Autoscaling](../../autoscale-create-assign-scaling-plan). For these host pools, each phase of the scaling plans should have the **Minimum percentage of active hosts (%)** set to 100%. Session hosts with Ephemeral OS disks don't support starting and deallocating. Therefore, setting the **Minimum percentage of active hosts (%)** to 100% ensures that the scaling process only creates and deletes session hosts, rather than starting and deallocating.

### Create a session host with Ephemeral OS disks

You can use the Azure portal or Azure PowerShell to configure session host with ephemeral OS disks.

# [Azure portal](#tab/portal)
To configure a session host with ephemeral OS disks using the Azure portal:

1. Sign in to the Azure portal.
2. In the search bar, enter **Azure Virtual Desktop** and select the matching service entry.
3. Select **Host pools**, then select **Create**.
4. On the **Basic** tab, complete the following information:

| Parameter | Value/Description |
| --- | --- |
| **Subscription** | In the dropdown list, select the subscription where you want to create the host pool. |
| **Resource group** | Select an existing resource group, or select **Create new** and enter a name. |
| **Host pool name** | Enter a name for the host pool, such as **hp01**. |
| **Location** | Select the Azure region where you want to create your host pool. |
| **Deployment scope** | Select Regional to store the host pool's metadata in a regional database within the Azure region you selected for Location, or Geographical to store it in the geographical database serving that region. Geographical is the default. This option only appears when the region you select for Location supports regional host pools. Deployment scope can't be changed after the host pool is created. |
| **Validation environment** | Select **Yes** to create a host pool that is used as a [validation environment](../../configure-validation-environment).Select **No** (*default*) to create a host pool that isn't used as a validation environment. |
| **Preferred app group type** | Select the [preferred application group type](../../terminology#application-groups) for this host pool: **Desktop** or **RemoteApp**. A desktop application group is created automatically when you use the Azure portal. |
| **Host pool type** | Select **Pooled**. Pooled is the only host pool type supported with session host configuration and ephemeral OS disks. |

Once you complete this tab, select Next: **Session hosts**.

1. On the **Session hosts** tab, complete the following information, which is captured in a session host configuration and used to create session hosts.

| Parameter | Value/Description |
| --- | --- |
| **Number of session hosts** | Select the number of session hosts you would like to create. |
| **Resource group** | This value defaults to the resource group that you chose to contain your host pool on the **Basics** tab, but you can select an alternative. |
| **Name prefix** | Enter a name prefix for your session hosts, such as **hp01-sh**.Each session host has a suffix of a hyphen and then a sequential number added to the end, such as **hp01-sh-0**.This name prefix can be a maximum of 11 characters and is used in the computer name in the operating system. The prefix and the suffix combined can be a maximum of 15 characters. Session host names must be unique. |
| **Virtual machine type** | Select **Azure virtual machine**. |
| **Virtual machine location** | Select the Azure region where you want to deploy your session hosts. This value must be the same region that contains your virtual network. |
| **Availability options** | Select one or more [availability zones](/en-us/azure/reliability/availability-zones-overview) in which to deploy your virtual machine. |
| **Security type** | Select from **Standard**, [Trusted launch virtual machines](/en-us/azure/virtual-machines/trusted-launch), or [Confidential virtual machines](/en-us/azure/confidential-computing/confidential-vm-overview).- If you select **Trusted launch virtual machines**, options for **secure boot** and **vTPM** are automatically selected.- If you select **Confidential virtual machines**, options for **secure boot**, **vTPM**, and **integrity monitoring** are automatically selected. You can't opt out of vTPM when using a confidential VM. |
| **Image** | Select the OS image that you want to use from the list, or select **See all images** to see more. The full list includes any images that you created and stored as an [Azure Compute Gallery shared image](/en-us/azure/virtual-machines/shared-image-galleries) or a [managed image](/en-us/azure/virtual-machines/windows/capture-image-resource). |
| **Virtual machine size** | Select a size. If you want to use a different size, select **Change size**, and then select from the list. |
| **OS disk type** | Select the disk type to use for your session hosts. During preview, only **Standard SSD** is supported and is automatically selected once ephemeral OS disks are configured. |
| **Ephemeral OS disk** | Image value must be configured to select ephemeral OS disk. If the selected virtual machine size doesn’t have a temporary disk or cache equal to or greater than the image size, you won’t be able to configure an ephemeral OS disk. |
| **Boot Diagnostics** | Select whether you want to enable [boot diagnostics](/en-us/azure/virtual-machines/boot-diagnostics). |
| **Network and security** |  |
| **Virtual network** | Select your virtual network. An option to select a subnet appears. |
| **Subnet** | Select a subnet from your virtual network. |
| **Network security group** | Select whether you want to use a network security group (NSG).- **None** doesn't create a new NSG.- **Basic** creates a new NSG for the VM network adapter.- **Advanced** enables you to select an existing NSG.You don't need to open inbound ports to connect to Azure Virtual Desktop. Learn more at [Understanding Azure Virtual Desktop network connectivity](../../network-connectivity). |
| **Public inbound ports** | You can select a port to allow from the list. Azure Virtual Desktop doesn't require public inbound ports, so we recommend that you select **No**. |
| **Domain to join** |  |
| **Select which directory you would like to join** | Select from **Microsoft Entra ID** or **Active Directory**, and complete the relevant parameters for the selected option. |
| **Virtual Machine Administrator account** | Select the key vault and secret for the username and password for the local administrator account of the new session host VMs. The username and password must meet the [requirements for Windows VMs in Azure](/en-us/azure/virtual-machines/windows/faq#what-are-the-password-requirements-when-creating-a-vm-). |
| **Custom configuration** |  |
| **Custom configuration script URL** | If you want to run a PowerShell script during deployment, you can enter the URL here. |

1. Once you complete this tab, select **Next** to continue configuring your Workspace and other optional configuration or select **Review + Create**.
2. On the Review + create tab, ensure validation passes and review the information that is during deployment.
3. Select Create to create the host pool.
4. Once the host pool and session host are created, go to Overview page of the host pool. Select Total machines under Virtual machines. Select the created session host and click the session host name under Name. You're brought to the session host’s Priorities page, where under Disk, you can confirm that the session host is configured with an ephemeral OS disk.

### Schedule an update and edit a session host configuration to configure Ephemeral OS disks

Using session host update, you can schedule an update to your host pool to enable ephemeral OS disks. Session host update uses the current session host configuration defined for the host pool. Before scheduling an update, configure the session host update settings to enable ephemeral OS disks—otherwise, session hosts are redeployed using the existing configuration values. Learn how to [schedule an update and edit a session host configuration](../../session-host-update-configure).

### Next Steps

Check out the [frequently asked questions on ephemeral OS disk](/en-us/azure/virtual-machines/ephemeral-os-disks-faq).

---