---
layout: Conceptual
title: Overview of the Azure Arc-enabled System Center Virtual Machine Manager - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/overview
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
description: This article provides a detailed overview of the Azure Arc-enabled System Center Virtual Machine Manager.
ms.date: 2026-09-24T00:00:00.0000000Z
ms.topic: overview
ms.services: azure-arc
ms.subservice: azure-arc-scvmm
ms.reviewer: v-gajeronika
keywords: VMM, Arc, Azure, System Center
locale: en-us
document_id: 4ca156c4-ca77-1aef-3248-a6ba6ad84959
document_version_independent_id: ad9a9713-d502-677a-d295-9b91519b1583
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/system-center-virtual-machine-manager/overview.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/system-center-virtual-machine-manager/overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/system-center-virtual-machine-manager/overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/c89972e1-0a93-4ce3-b588-9c24d08ca424
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b2144970-2aee-47fb-9df2-af491ca710ec
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 2648d95b-338d-4fa2-a96a-01e3ae52cd56
---

# Overview of the Azure Arc-enabled System Center Virtual Machine Manager - Azure Arc | Microsoft Learn

Note

Azure Arc-enabled SCVMM retires in September 2029. If you're using Azure Arc-enabled SCVMM, transition to [Azure Arc-enabled Servers](/en-us/azure/azure-arc/servers/overview) or contact arc-vmm-feedback@microsoft.com. For more information, see the [transition guidance](transition-guidance).

Azure Arc-enabled System Center Virtual Machine Manager (SCVMM) empowers System Center customers to connect their VMM environment to Azure and perform VM self-service operations from Azure portal. By extending the Azure control plane to SCVMM managed infrastructure, Azure Arc-enabled SCVMM enables you to use Azure security, governance, and management capabilities consistently across your System Center managed estate and Azure.

By using Azure Arc-enabled SCVMM, you can manage your hybrid environment consistently and perform self-service VM operations through Azure portal. For Microsoft Azure Pack customers, this solution is intended as an alternative to perform VM self-service operations.

Azure Arc-enabled SCVMM allows you to:

- Perform various VM lifecycle operations such as start, stop, pause, and delete VMs on SCVMM managed VMs directly from Azure.
- Empower developers and application teams to self-serve VM operations on demand by using [Azure role-based access control (RBAC)](/en-us/azure/role-based-access-control/overview).
- Browse your VMM resources (VMs, templates, VM networks, and storage) in Azure, providing you with a single pane view for your infrastructure across both environments.
- Discover and onboard existing SCVMM managed VMs to Azure.
- Install the Azure Connected Machine agent at scale on SCVMM VMs to [govern, protect, configure, and monitor them](../servers/overview#supported-cloud-operations).
- Build automation and self-service pipelines by using Python, Java, JavaScript, Go, and .NET SDKs; Terraform, ARM, and Bicep templates; Azure REST APIs, CLI, and PowerShell.
- Leverage Azure Arc benefits such as [Windows Server management](/en-us/azure/azure-arc/servers/windows-server-management-overview?tabs=portal) for VMs with Software Assurance licenses, and pay-as-you-go billing for [Extended Security Updates](/en-us/azure/azure-arc/system-center-virtual-machine-manager/deliver-esus-for-system-center-virtual-machine-manager-vms) for Windows Server and SQL Server VMs.

For updates on the capabilities and enhancements of Azure Arc, see the [Tech Community blog](https://techcommunity.microsoft.com/category/azure/blog/azurearcblog) for Azure Arc.

## How does it work?

To Azure Arc-enable an SCVMM management server, deploy [Azure Arc resource bridge](../resource-bridge/overview) in the VMM environment. Azure Arc resource bridge is a virtual appliance that connects VMM management server to Azure. By using Azure Arc resource bridge, you can represent the SCVMM resources (clouds, VMs, templates, and more) in Azure and perform various operations on them.

## Architecture

The following image shows the architecture for the Azure Arc-enabled SCVMM:

[![Screenshot of Arc enabled SCVMM - architecture.](media/architecture/azure-arc-scvmm-architecture.png)](media/architecture/azure-arc-scvmm-architecture.png#lightbox)

*To download architecture diagrams in high resolution, visit [Jumpstart Gems](https://aka.ms/JumpstartGems_Docs).*

## How is Azure Arc-enabled SCVMM different from Azure Arc-enabled servers

- Azure Arc-enabled servers interact on the guest operating system level, with no awareness of the underlying infrastructure fabric and the virtualization platform that they're running on. Since Azure Arc-enabled servers also support bare-metal machines, a host hypervisor might not exist in some cases.
- Azure Arc-enabled SCVMM is a superset of Azure Arc-enabled servers that extends management capabilities beyond the guest operating system to the VM itself. This extension provides lifecycle management and CRUD (Create, Read, Update, and Delete) operations on an SCVMM VM. The Azure portal exposes these lifecycle management capabilities, and they look and feel just like a regular Azure VM. Azure Arc-enabled SCVMM also provides guest operating system management by using the same components as Azure Arc-enabled servers.

You can start with either option and add the other one later without any disruption. Both options provide the same consistent experience.

Note

For guidance on choosing the right Azure Arc service for your virtual machines, see [Choose the right Azure Arc service for machines](../choose-service).

### Supported scenarios

Azure Arc-enabled SCVMM supports the following scenarios:

- SCVMM administrators can connect a VMM instance to Azure and browse the SCVMM virtual machine inventory in Azure.
- Administrators can use the Azure portal to browse SCVMM inventory and register SCVMM cloud, virtual machines, VM networks, and VM templates into Azure.
- Administrators can provide app teams/developers fine-grained permissions on those SCVMM resources through Azure RBAC.
- App teams can use Azure interfaces (portal, CLI, PowerShell, SDKs, Terraform, Bicep, ARM templates, or REST API) to manage the lifecycle of on-premises VMs they use for deploying their applications (CRUD, Start/Stop/Restart).
- Administrators can install Azure Connected Machine agent on SCVMM-managed VMs at-scale and can perform the following actions:

    - **Govern**:
        - Assign [Azure machine configurations](/en-us/azure/governance/machine-configuration/overview) to audit settings inside the machine.
    - **Protect**:
        - Protect non-Azure servers with [Microsoft Defender for Endpoint](/en-us/microsoft-365/security/defender-endpoint), included through [Microsoft Defender for Cloud](/en-us/azure/security-center/defender-for-servers-introduction), for threat detection, for vulnerability management, and to proactively monitor for potential security threats. Microsoft Defender for Cloud presents the alerts and remediation suggestions from the threats detected.
        - Use [Microsoft Sentinel](/en-us/azure/azure-arc/servers/scenario-onboard-azure-sentinel) to collect security-related events and correlate them with other data sources.
    - **Configure**:
        - Use [Azure Automation](/en-us/azure/automation/extension-based-hybrid-runbook-worker-install?tabs=windows) for frequent and time-consuming management tasks using PowerShell and Python [runbooks](/en-us/azure/automation/automation-runbook-execution). Assess configuration changes for installed software, Microsoft services, Windows registry and files, and Linux daemons using the Azure Monitor agent for [change tracking and inventory](/en-us/azure/automation/change-tracking/overview-monitoring-agent?tabs=win-az-vm).
        - Use [Azure Update Manager](/en-us/azure/update-manager/overview) to manage operating system updates for Windows and Linux servers. Automate onboarding and configuration of a set of Azure services when you use [Azure Automanage](/en-us/azure/automanage/automanage-arc).
        - Perform post-deployment configuration and automation tasks using supported [Arc-enabled servers VM extensions](/en-us/azure/azure-arc/servers/manage-vm-extensions) for non-Azure Windows or Linux machine.
    - **Monitor**:
        - Monitor operating system performance and discover application components to monitor processes and dependencies with other resources using [VM insights](/en-us/azure/azure-monitor/vm/vminsights-overview).
        - Collect other log data, such as performance data and events, from the operating system or workloads running on the machine with the [Azure Monitor Agent](/en-us/azure/azure-monitor/agents/azure-monitor-agent-overview). This data is stored in a [Log Analytics workspace](/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview).

    Log data collected and stored in a Log Analytics workspace from the hybrid machine contains properties specific to the machine, such as a Resource ID, to support [resource-context](/en-us/azure/azure-monitor/logs/manage-access#access-mode) log access.

    Watch this video to learn more about Azure monitoring, security, and update services across hybrid and multicloud environments.
- Administrators can install the Azure Connected Machine agent at scale and leverage Azure Arc benefits such as [Windows Server management](/en-us/azure/azure-arc/servers/windows-server-management-overview?tabs=portal) for VMs with Software Assurance licenses, and pay-as-you-go billing for [Extended Security Updates](/en-us/azure/azure-arc/system-center-virtual-machine-manager/deliver-esus-for-system-center-virtual-machine-manager-vms) for Windows Server and SQL Server VMs.

### Unsupported scenarios

Azure Arc-enabled SCVMM doesn't support:

- Azure-based management of VMware vCenter VMs managed by SCVMM. To onboard VMware VMs to Azure Arc, use [Azure Arc-enabled VMware vSphere](/en-us/azure/azure-arc/vmware-vsphere/overview).
- Azure-based management of Azure Local VMs managed by SCVMM. To onboard Azure Local VMs to Azure Arc, use [Azure Arc VM management capabilities of Azure Local](/en-us/azure/azure-local/manage/azure-arc-vm-management-overview).

### Supported VMM versions

Azure Arc-enabled SCVMM works with VMM 2025, 2022, and 2019 versions. It supports SCVMM management servers with a maximum of 15,000 VMs.

### Supported regions

For the most up-to-date information about regional availability of Azure Arc-enabled SCVMM, see [Product Availability by Region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).

## Data residency

Azure Arc-enabled SCVMM stores customer data. By default, customer data stays within the region the customer deploys the service instance in. For regions with data residency requirements, customer data is always kept within the same region.