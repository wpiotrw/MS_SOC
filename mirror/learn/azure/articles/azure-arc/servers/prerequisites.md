---
layout: Conceptual
title: Connected Machine agent prerequisites - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/prerequisites
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
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Learn about the prerequisites for installing the Connected Machine agent for Azure Arc-enabled servers.
ms.date: 2026-09-11T00:00:00.0000000Z
ms.topic: concept-article
ms.custom: devx-track-azurepowershell
locale: en-us
document_id: a4d7411a-32db-b1a7-09b6-88fde6daccf9
document_version_independent_id: 89123a10-c752-74ca-adf8-69ed618e15a7
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/prerequisites.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
interactive_type: azurepowershell,azurecli
toc_rel: toc.json
asset_id: azure-arc/servers/prerequisites
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/prerequisites.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 5e0f7616-b98f-0912-eede-9d9a7735c4fa
---

# Connected Machine agent prerequisites - Azure Arc | Microsoft Learn

This article outlines the technical prerequisites, supported environments, and specifications required for successfully onboarding physical and virtual servers to Azure Arc-enabled servers. Administrators and engineers planning to implement Azure Arc in their environments should review this information. Some [onboarding methods](deployment-options) may have more requirements.

## Supported environments

Azure Arc-enabled servers support the installation of the Connected Machine agent on physical servers and virtual machines hosted outside of Azure, including on platforms like:

- VMware (including Azure VMware Solution)
- Azure Local
- Other cloud environments

Note

You shouldn't install Azure Arc on virtual machines hosted in Azure, Azure Stack Hub, or Azure Stack Edge, as they already have similar capabilities. You can [use an Azure VM to simulate an on-premises environment](plan-evaluate-on-azure-virtual-machine) for testing purposes only.

### Cloned and golden image considerations

Take extra care when using Azure Arc on systems that are:

- Cloned
- Restored from backup as a second instance of the server
- Used to create a "golden image" from which other virtual machines are created

If two agents use the same source ID, you'll encounter inconsistent behaviors when both agents try to act as one Azure resource. The best practice for these situations is to use an automation tool or script to onboard the server to Azure Arc after it's cloned, restored from backup, or created from a golden image. For more information about cloning machines to use as Arc-enabled servers, see [Cloning guidelines](agent-overview#cloning-guidelines).

Note

For more information on using Azure Arc-enabled servers in VMware environments, see the [VMware FAQ](vmware-faq).

## Supported operating systems

Azure Arc supports Windows and Linux operating systems as listed in the table. If an OS version isn't listed, it's not supported by Azure Arc.

x86-64 (64-bit) architecture is fully supported, while only some features may be supported on Arm64. The Azure Connected Machine agent doesn't run on 32-bit architectures.

| Operating system | Version | x86-64 | ARM64 | End of new agent version support | Notes |
| --- | --- | --- | --- | --- | --- |
| AlmaLinux | 8 | ✅ | ✅ | May 2029 |  |
| AlmaLinux | 9 | ✅ | ❌ | August 2032 |  |
| Amazon Linux | 2 | ⚠️ | ⚠️ | November 2026 | New arc agent version support ends November 2026 |
| Amazon Linux | 2023 | ✅ | ✅ | August 2027 |  |
| Azure Linux (CBL-Mariner) | 3.0 | ⚠️ | ⚠️ | November 2026 | New arc agent version support ends November 2026 |
| Azure Local |  |  |  |  |  |
| Debian | 11 | ⚠️ | ❌ | November 2026 | New arc agent version support ends November 2026 |
| Debian | 12 | ⚠️ | ⚠️ | November 2026 | New arc agent version support ends November 2026 |
| Debian | 13 | ✅ | ❌ | — |  |
| Oracle Linux | 7 | ⚠️ | ❌ | November 2026 | New arc agent version support ends November 2026 |
| Oracle Linux | 8 | ✅ | ✅ | August 2029 |  |
| Oracle Linux | 9 | ✅ | ❌ | August 2032 |  |
| Oracle Linux | 10 | ✅ | ❌ | — |  |
| Red Hat Enterprise Linux (RHEL) | 7 | ⚠️ | ❌ | November 2026 | New arc agent version support ends November 2026 |
| Red Hat Enterprise Linux (RHEL) | 8 | ✅ | ❌ | August 2029 |  |
| Red Hat Enterprise Linux (RHEL) | 9 | ✅ | ❌ | August 2032 |  |
| Red Hat Enterprise Linux (RHEL) | 10 | ✅ | ❌ | August 2035 |  |
| Rocky Linux | 8 | ✅ | ❌ | August 2029 |  |
| Rocky Linux | 9 | ✅ | ❌ | August 2032 |  |
| SUSE Linux Enterprise Server (SLES) | 12 SP5 | ⚠️ | ❌ | November 2026 | New arc agent version support ends November 2026 |
| SUSE Linux Enterprise Server (SLES) | 15 SP3 | ⚠️ | ⚠️ | November 2026 | New arc agent version support ends November 2026 |
| SUSE Linux Enterprise Server (SLES) | 15 SP4 | ⚠️ | ⚠️ | November 2026 | New arc agent version support ends November 2026 |
| SUSE Linux Enterprise Server (SLES) | 15 SP5 | ⚠️ | ⚠️ | November 2026 | New arc agent version support ends November 2026 |
| SUSE Linux Enterprise Server (SLES) | 15 SP6 | ⚠️ | ⚠️ | November 2026 | New arc agent version support ends November 2026 |
| SUSE Linux Enterprise Server (SLES) | 15 SP7 | ✅ | ✅ | August 2031 |  |
| Ubuntu | 18.04 | ⚠️ | ❌ | November 2026 | New arc agent version support ends November 2026 |
| Ubuntu | 20.04 | ⚠️ | ⚠️ | November 2026 | New arc agent version support ends November 2026 |
| Ubuntu | 22.04 | ✅ | ✅ | May 2027 |  |
| Ubuntu | 24.04 | ✅ | ✅ | May 2029 |  |
| Ubuntu | 26.04 | ✅ | ❌ | — |  |
| Windows Client | 10 | ✅ | ❌ | — | see client operating system guidance |
| Windows Client | 11 | ✅ | ❌ | — | see client operating system guidance |
| Windows IoT Enterprise | 10 (22H2) | ✅ | ❌ | — | see client operating system guidance |
| Windows IoT Enterprise | 11 | ✅ | ❌ | — | see client operating system guidance |
| Windows IoT Enterprise LTSC | 10 (2021) | ✅ | ❌ | — | see client operating system guidance |
| Windows IoT Enterprise LTSC | 11 (2024) | ✅ | ❌ | — | see client operating system guidance |
| Windows Server | 2012 | ⚠️ | ❌ | November 2026 | New arc agent version support ends November 2026 |
| Windows Server | 2012 R2 | ⚠️ | ❌ | November 2026 | New arc agent version support ends November 2026 |
| Windows Server | 2016 | ✅ | ❌ | February 2030 |  |
| Windows Server | 2019 | ✅ | ❌ | — |  |
| Windows Server | 2022 | ✅ | ❌ | — |  |
| Windows Server | 2025 | ✅ | ❌ | — |  |

Important

The expected end of Azure Arc support for Windows Server 2012 and Windows Server 2012 R2 doesn't extend the ESU period. ESUs for these versions end on October 13, 2026. The October 13, 2026 security update is the final update provided through ESUs.

For Windows Server, both Desktop and Server Core experiences are supported. Azure Editions are supported on Azure Local.

The Azure Connected Machine agent isn't tested on operating systems hardened by the Center for Information Security (CIS) Benchmark.

### Azure Connected Machine Agent OS support and deprecation

When an operating system version reaches the date listed in the **End of new agent version support** column, Microsoft stops releasing new versions of the Azure Connected Machine Agent for that operating system version. In accordance with the [Azure Connected Machine Agent release and support policy](/en-us/azure/azure-arc/servers/agent-release-notes), Microsoft continues to support and service the final compatible agent version for **12 months after the final agent release**.

Customers should upgrade to a supported operating system version before the servicing period ends to continue receiving Azure Connected Machine Agent updates.

Azure Connected Machine Agent support follows Microsoft's support lifecycle for the agent and is independent of extended support programs offered by operating system vendors. Participation in an extended security or support offering doesn't extend or otherwise change Microsoft's support timeline for the Azure Connected Machine Agent.

### Arm64 architecture support

Not all features, virtual machine extensions, and services are supported on Arm64 at this point. For full details on Arm64 compatibility or to check if other services are supported, refer to the documentation for the service you wish to use. The following are a few features known to be supported on Arm64:

- RunCommand
- CustomScriptExtension
- Azure Monitor Agent

Note

Machine configuration isn't compatible with Arm64 at this time.

## Client operating systems

The Azure Arc service and Azure Connected Machine Agent are supported on Windows 10 and 11 client operating systems only when using those computers in a server-like environment. That is, the computer should always be:

- Connected to the internet
- Connected to a power source
- Powered on

For example, a computer running Windows 11 that's responsible for digital signage, point-of-sale solutions, and general back office management tasks is a good candidate for Azure Arc. End-user productivity machines that may go offline for long periods of time shouldn't use Azure Arc. Consider using [Microsoft Intune](/en-us/mem/intune) or [Microsoft Configuration Manager](/en-us/mem/configmgr) for those scenarios.

## Short-lived servers and virtual desktop infrastructure

Microsoft doesn't recommend running Azure Arc on short-lived (ephemeral) servers or virtual desktop infrastructure (VDI) VMs. Azure Arc is designed for long-term management of servers and isn't optimized for scenarios where you are regularly creating and deleting servers. For example, Azure Arc doesn't know if the agent is offline due to planned system maintenance or because the VM was deleted, so it doesn't automatically clean up server resources that stopped sending heartbeats. As a result, you could encounter a conflict if you recreate a deleted VM with the same name and there's an existing Azure Arc resource with the same name.

[Azure Virtual Desktop on Azure Local](/en-us/azure/virtual-desktop/azure-local-overview) doesn't use short-lived VMs and supports running Azure Arc on the desktop VMs.

## Software and system requirements

This section details the software requirements for the Azure Connected Machine agent.

### Linux operating system requirements

- systemd
- wget (to download the installation script)
- openssl
- gnupg (Debian-based systems only)

## Local user logon right for Windows systems

The Azure Hybrid Instance Metadata Service runs under a low-privileged virtual account, `NT SERVICE\himds`. This account needs the "log on as a service" right in Windows to run. In most cases, there's nothing you need to do, because this right is granted to virtual accounts by default. However, if your organization uses Group Policy to customize this setting, you'll need to add `NT SERVICE\himds` to the list of accounts allowed to log on as a service.

You can check the current policy on your machine by opening the Local Group Policy Editor (`gpedit.msc`) from the Start menu and navigating to the following policy item:

Computer Configuration &gt; Windows Settings &gt; Security Settings &gt; Local Policies &gt; User Rights Assignment &gt; Log on as a service

Check if any of `NT SERVICE\ALL SERVICES`, `NT SERVICE\himds`, or `S-1-5-80-4215458991-2034252225-2287069555-1155419622-2701885083` (the static security identifier for NT SERVICE\himds) are in the list. If none are in the list, you'll need to work with your Group Policy administrator to add `NT SERVICE\himds` to any policies that configure user rights assignments on your servers. The Group Policy administrator needs to make the change on a computer with the Azure Connected Machine agent installed so the object picker resolves the identity correctly. The agent doesn't need to be configured or connected to Azure to make this change.

![Screen capture of the Local Group Policy Editor showing which users have permissions to log on as a service.](media/prerequisites/arc-server-user-rights-assignment.png)

## Required permissions

You'll need the following Azure built-in roles for different aspects of managing connected machines:

- To onboard machines, you must have the [Azure Connected Machine Onboarding](/en-us/azure/role-based-access-control/built-in-roles#azure-connected-machine-onboarding) or [Contributor](/en-us/azure/role-based-access-control/built-in-roles#contributor) role for the resource group where you're managing the servers.
- To read, modify, and delete a machine, you must have the [Azure Connected Machine Resource Administrator](/en-us/azure/role-based-access-control/built-in-roles#azure-connected-machine-resource-administrator) role for the resource group.
- To select a resource group from the drop-down list when using the **Generate script** method, you'll also need the [Reader](/en-us/azure/role-based-access-control/built-in-roles#reader) role for that resource group (or another role that includes **Reader** access).
- When associating a Private Link Scope with an Arc Server, you must have Microsoft.HybridCompute/privateLinkScopes/read permission on the Private Link Scope Resource.

## Azure resource providers

The following [Azure resource providers](/en-us/azure/azure-resource-manager/management/resource-providers-and-types) must be registered in your subscription to use Azure Arc-enabled servers:

- **Microsoft.HybridCompute**
- **Microsoft.GuestConfiguration**
- **Microsoft.HybridConnectivity**
- **Microsoft.AzureArcData** (if you plan to Arc-enable SQL Servers)
- **Microsoft.Compute** (for Azure Update Manager and automatic extension upgrades)

You can register the resource providers using the following commands:

Azure PowerShell:

```azurepowershell
Connect-AzAccount
Set-AzContext -SubscriptionId [subscription you want to onboard]
Register-AzResourceProvider -ProviderNamespace Microsoft.HybridCompute
Register-AzResourceProvider -ProviderNamespace Microsoft.GuestConfiguration
Register-AzResourceProvider -ProviderNamespace Microsoft.HybridConnectivity
Register-AzResourceProvider -ProviderNamespace Microsoft.AzureArcData
```

Azure CLI:

```azurecli
az account set --subscription "{Your Subscription Name}"
az provider register --namespace 'Microsoft.HybridCompute'
az provider register --namespace 'Microsoft.GuestConfiguration'
az provider register --namespace 'Microsoft.HybridConnectivity'
az provider register --namespace 'Microsoft.AzureArcData'
```

You can also register the resource providers in the [Azure portal](/en-us/azure/azure-resource-manager/management/resource-providers-and-types#azure-portal).