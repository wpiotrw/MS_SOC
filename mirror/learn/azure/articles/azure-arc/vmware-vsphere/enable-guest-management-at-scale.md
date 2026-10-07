---
layout: Conceptual
title: Install Arc agent at scale for your VMware VMs - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/vmware-vsphere/enable-guest-management-at-scale
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
description: Learn how to install Arc agent at scale for Arc enabled VMware vSphere VMs.
ms.topic: how-to
ms.date: 2026-10-06T00:00:00.0000000Z
ms.subservice: vmware-vsphere-azure-arc
ms.reviewer: v-gajeronika
locale: en-us
document_id: e2a3fc9a-ba63-7c31-4f5c-032be4edd35f
document_version_independent_id: 08fa07bf-48b0-c104-d1db-6f91c9bf913d
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/vmware-vsphere/enable-guest-management-at-scale.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
interactive_type: azurecli
toc_rel: toc.json
asset_id: azure-arc/vmware-vsphere/enable-guest-management-at-scale
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/vmware-vsphere/enable-guest-management-at-scale.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: 10d1d624-18ca-b34b-18e6-921a39e7d1ef
---

# Install Arc agent at scale for your VMware VMs - Azure Arc | Microsoft Learn

In this article, you learn how to install Azure connected machine agents in VMware VMs at-scale through Azure Arc enabled VMware vSphere experiences. Installing these agents is a prerequisite to use Azure services for securing, patching, and monitoring your VMs. By using these agents, you can leverage Azure Arc benefits such as Extended Security Updates, pay-as-you-go licensing for Windows Server and SQL servers, and Software Attestation benefits.

You can install Arc agents on VMware VMs through multiple methods. Choose the method that fits your deployment preferences:

- Azure portal
- Programmatic methods such as Azure CLI, Azure PowerShell, Azure REST APIs, Azure SDKs, Terraform, Bicep, and ARM templates. The reference section of this documentation repository has information on the exact syntax.
- Out-of-band methods such as using a Service Principal, System Center Configuration Manager script, System Center Configuration Manager custom task sequence, Group policy, and Ansible playbook.

## Prerequisites

Before you install Arc agents at scale for VMware VMs, ensure the following conditions are met:

- You are onboarded to Azure Arc enabled VMware vSphere with the vCenter Azure resource in a *Connected* state and its associated Azure Arc resource bridge is in a *Running* state.
- You have the *Azure Arc VMware VM Contributor* role or a custom Azure role with permissions to install Arc agents on the target machines.
- All the target machines are:

    - Powered on.
    - Running a [supported operating system](../servers/prerequisites#supported-operating-systems).
    - VMware tools are installed on the machines. If you don't install VMware tools, the portal disables the option to install Arc agent. 
        Note

        Use the out-of-band methods to install Arc agents if VMware tools aren't installed.
    - Able to connect through the firewall to communicate over the internet, and [these URLs](../servers/network-requirements#urls) aren't blocked.

    Note

    If you're using a Linux VM, the account must not prompt for login on sudo commands. To override the prompt, from a terminal, run `sudo visudo`, and add `<username> ALL=(ALL) NOPASSWD:ALL` at the end of the file. Ensure you replace `<username>`. If your VM template has these changes incorporated, you don't need to make this change for the VM created from that template.

## Install Arc agents

# [Azure portal](#tab/azure-portal)
This method works only if VMware tools are installed on the target machines. If VMware tools aren't installed, the portal grays out the **Arc agent with virtual hardware management** option under **Manage Arc onboarding**. You can install Arc agents by using out-of-band methods.

An administrator can install agents for multiple machines from the Azure portal if the machines share the same administrator credentials.

1. Go to **Azure Arc center** and select **vCenter resource**. Navigate to the virtual machines inventory.
2. Select all the target machines and choose **Manage Arc onboarding** option.
3. Select **Arc agent with virtual hardware management** radio button to install Arc agents on the selected machines. By using this option, you can use Azure services such as Azure Update Manager, Azure Monitor, Microsoft Defender for Cloud, Azure Policy, Azure Automation, Change Tracking and Inventory, and more to secure, govern, patch, and monitor your virtual machines.
4. Based on your organization's network policies, choose the connectivity method for the Arc agents that runs in your VMware VMs to connect to Azure. The available options are Public endpoint, Proxy server, and Private endpoint.

    - To connect the Arc agent through a proxy, provide the proxy server details.
    - To connect the Arc agent through a private endpoint, follow these [steps](../servers/private-link-security) to set up Azure private link.

    Note

    Private endpoint connectivity is only available for Arc agent to Azure communications. For Arc resource bridge to Azure connectivity, Azure private link isn't supported.
5. Enter the administrator username and password for the machine. For Windows VMs, the account must be part of the local administrators group. For Linux VMs, it must be a root account. These credentials aren't persisted in Azure. They're used to install the Azure Arc agent and then discarded. Alternatively, for Linux VMs, you can use SSH key-based authentication method.
6. Select **Onboard** to start the installation of the Arc agent in the specified machines. Once installation is complete, the Arc agent status column will switch to Enabled for the machines with Arc agent running. You can start using Azure services for these machines.

# [Auto Arc-enablement script](#tab/ercenablement-script)
This method works only if VMware tools are installed on the target machines. If VMware tools aren't installed, you can install Arc agents by using out-of-band methods.

You can automate Arc agent installation by using a helper script that uses the AzCLI command. To onboard VMs to Azure Arc at scale, download this [helper script](https://aka.ms/arcvmwarebatchenable). In a single ARM deployment, the helper script can onboard up to 400 VMs.

### Features of the script

- Creates a log file (vmware-batch.log) for tracking its operations.
- Generates a list of Azure portal links to all the deployments created (`all-deployments-<timestamp>.txt`).
- Creates ARM deployment files (`vmw-dep-<timestamp>-<batch>.json`).
- Onboards up to 200 VMs in a single ARM deployment if you're installing the Arc agent, otherwise it onboards up to 400 VMs.
- Supports running as a cron job to onboard all the VMs in a vCenter.
- Allows for service principal authentication to Azure for automation.

Before running this script, install Azure CLI and the `connectedvmware` extension.

### Prerequisites

Before running this script, install:

- Azure CLI from [here](/en-us/cli/azure/install-azure-cli).
- The `connectedvmware` extension for Azure CLI: Install it by running `az extension add --name connectedvmware`.

### Usage

1. Download the script to your local machine.
2. Open a PowerShell terminal and go to the directory containing the script.
3. Run the following command to allow the script to run, as it's an unsigned script. If you close the session before you complete all the steps, run this command again for the new session: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.
4. Run the script with the required parameters. For example, `.\arcvmware-batch-enablement.ps1 -VCenterId "<vCenterId>" -EnableGuestManagement -VMCountPerDeployment 3 -DryRun`. Replace `<vCenterId>` with the ARM ID of your vCenter.

### Parameters

- `VCenterId`: The ARM ID of the vCenter where the VMs are located.
- `EnableGuestManagement`: If you specify this switch, the script installs Arc agents on the VMs.
- `VMCountPerDeployment`: The number of VMs to onboard per ARM deployment. The maximum value is 200 if you are installing Arc agent, otherwise it's 400.
- `DryRun`: If you specify this switch, the script only creates the ARM deployment files. Otherwise, the script also deploys the ARM deployments.

### Running as a Cron Job

You can set up this script to run as a cron job by using the Windows Task Scheduler. Here's a sample script to create a scheduled task:

```azurecli
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-File "C:\Path\To\vmware-batch-enable.ps1" -VCenterId "<vCenterId>" -EnableGuestManagement -VMCountPerDeployment 3 -DryRun' 
$trigger = New-ScheduledTaskTrigger -Daily -At 3am 
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "EnableVMs" 
```

Replace `<vCenterId>` with the ARM ID of your vCenter.

To unregister the task, run the following command:

```azurecli
Unregister-ScheduledTask -TaskName "EnableVMs"
```

# [Out-of-band methods](#tab/Out-of-band)
You can install Arc agents directly on machines without relying on VMware tools or APIs. By using the out-of-band approach, first onboard the machines as Arc-enabled Server resources with the resource type `Microsoft.HybridCompute/machines`. After that, select the **Arc agent with virtual hardware management** option under **Manage Arc onboarding** to update the machine's `Kind` property as `VMware`, which enables virtual lifecycle operations.

1. **Connect the machines as Arc-enabled Server resources:** Install Arc agents by using Arc-enabled Server scripts.

    To install Arc agents at scale, use any of the following automation approaches:

    - [Install Arc agents at scale by using a Service Principal](../servers/onboard-service-principal).
    - [Install Arc agents at scale by using Configuration Manager script](../servers/onboard-configuration-manager-powershell).
    - [Install Arc agents at scale with a Configuration Manager custom task sequence](../servers/onboard-configuration-manager-custom-task).
    - [Install Arc agents at scale by using Group policy](../servers/onboard-group-policy-powershell).
    - [Install Arc agents at scale by using Ansible playbook](../servers/onboard-ansible-playbooks).
2. **Link Arc-enabled Server resources to the vCenter:** The following commands update the `Kind` property of Hybrid Compute machines to **VMware**. When you link the machines to vCenter, it enables virtual lifecycle operations and power cycle operations (start, stop, and other actions) on the machines.

    - The following command scans all the Arc for Server machines that belong to the vCenter in the specified subscription. It links the machines with that vCenter.

        ```azurecli
        az connectedvmware vm create-from-machines --subscription contoso-sub --vcenter-id /subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/allhands-demo/providers/microsoft.connectedvmwarevsphere/VCenters/ContosovCentervcenters/contoso-vcenter
        ```
    - The following command scans all the Arc for Server machines that belong to the vCenter in the specified resource group. It links the machines with that vCenter.

        ```azurecli
        az connectedvmware vm create-from-machines --resource-group contoso-rg --vcenter-id /subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/allhands-demo/providers/microsoft.connectedvmwarevsphere/VCenters/ContosovCentervcenters/contoso-vcenter
        ```
    - Use the following command to link an individual Arc for Server resource to vCenter.

        ```azurecli
        az connectedvmware vm create-from-machines --resource-group contoso-rg --name contoso-vm --vcenter-id /subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/allhands-demo/providers/microsoft.connectedvmwarevsphere/VCenters/ContosovCentervcenters/contoso-vcenter
        ```

---