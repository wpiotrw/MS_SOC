---
layout: Conceptual
title: Azure Virtual Desktop Hybrid Overview - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/hybrid-overview
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: SteveD-MSFT
manager: eliotgra
ms.author: stdowns
ms.service: azure-virtual-desktop
description: An overview of Microsoft's Azure Virtual Desktop Hybrid capability. This feature enables deploying virtual desktops and applications on-premises while managing them from a cloud-native service.
ms.topic: overview
ms.date: 2026-06-09T00:00:00.0000000Z
locale: en-us
document_id: ef85a86e-0401-1268-7cd3-5cc87944d8a2
document_version_independent_id: ef85a86e-0401-1268-7cd3-5cc87944d8a2
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/hybrid-overview.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: hybrid-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/hybrid-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
platformId: dd43b92e-0bc2-f8fc-8978-b353f6f5a81f
---

# Azure Virtual Desktop Hybrid Overview - Azure Virtual Desktop | Microsoft Learn

**Azure Virtual Desktop Hybrid** extends cloud-native desktop virtualization to existing on-premises infrastructure. The Azure Virtual Desktop service remains in Azure while applications and desktops are hosted on-premises. Session hosts must be [Azure Arc-enabled](/en-us/azure/azure-arc/servers/overview). The Azure Arc extension installs the AVD components and registers the device with a host pool.

## How it works

Azure Virtual Desktop Hybrid uses Azure Arc to deploy AVD components and register your on-premises machines with Azure Virtual Desktop in Azure.

At a high level:

1. You deploy a Windows virtual machine or headless physical device on your on-premises infrastructure.
2. You install the [Azure Arc connected machine agent](/en-us/azure/azure-arc/servers/agent-overview) on the machine, which registers it with Azure as an Arc-enabled server.
3. You run the [Azure Virtual Desktop Arc extension](/en-us/azure/virtual-desktop/deploy-azure-virtual-desktop-hybrid) on the Arc-enabled machine. The extension installs the AVD software and registers the machine with Azure Virtual Desktop.
4. Users connect to the session host using [Windows App](/en-us/windows-app/overview), the same way they connect to any Azure Virtual Desktop session host.

Microsoft manages the Azure Virtual Desktop service in Azure. You manage the on-premises machines, networking, and hosting infrastructure.

## Key capabilities

- **Cloud-managed service:** Microsoft hosts and manages the Azure Virtual Desktop service in Azure. You control and maintain the on-premises session hosts.
- **Use your existing infrastructure:** Use your current datacenter resources to host virtual desktops and remote apps. You can run Azure Virtual Desktop session hosts on your preferred on-premises hypervisor that supports Windows virtual machines.
- **Consistent user experience:**[Windows App](/en-us/windows-app/overview) provides a consistent user experience across Azure Virtual Desktop, Azure Virtual Desktop Hybrid, and Windows 365.

## Supported operating systems and licensing

Azure Virtual Desktop Hybrid supports the following operating systems. Licensing consists of user entitlement and Azure Virtual Desktop Hybrid service user license.

### Operating system support and user entitlement

Users must be licensed for a supported operating system to access Azure Virtual Desktop Hybrid.

| Operating System | Licensing method | Details |
| --- | --- | --- |
| [Windows Server 2025](/en-us/lifecycle/products/windows-server-2025)[Windows Server 2022](/en-us/lifecycle/products/windows-server-2022)[Windows Server 2019](/en-us/lifecycle/products/windows-server-2019)[Windows Server 2016](/en-us/lifecycle/products/windows-server-2016) | Remote Desktop Services (RDS) Client Access License (CAL) with Software Assurance (per-user or per-device)RDS User Subscription Licenses. | Supported on virtual machines and headless physical servers. |
| [Windows 11 Enterprise](/en-us/lifecycle/products/windows-11-enterprise-and-education)[Windows 10 Enterprise](/en-us/lifecycle/products/windows-10-enterprise-and-education) | Microsoft 365 E3, E5, A3, A5, F3, Business Premium, Student Use BenefitWindows Enterprise E3, E5Windows Education A3, A5Windows VDA per user[Per-user access pricing](/en-us/azure/virtual-desktop/licensing#licensing-recommendations-for-working-with-external-identities) by enrolling an Azure subscription. (External commercial purposes only) | Supported on virtual machines. Physical devices are only supported when used as dedicated, headless session hosts (rack-mounted or similar). Laptops and personal PCs aren't supported. |
| [Windows 11 Enterprise multi-session](/en-us/lifecycle/products/windows-11-enterprise-and-education)[Windows 10 Enterprise multi-session](/en-us/lifecycle/products/windows-10-enterprise-and-education) | Not supported on Azure Virtual Desktop Hybrid. | Not Supported |

## Session host deployment and power management

Azure Virtual Desktop Hybrid doesn't provision or manage virtual machine state, so the following capabilities aren't supported:

- Power management
- Autoscale
- Start VM on Connect
- Session Host Configuration

Organizations are responsible for deploying and managing their on-premises session hosts using hypervisor tools, scripts, partner solutions, or other tools.