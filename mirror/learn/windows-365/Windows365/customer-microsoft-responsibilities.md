---
layout: Conceptual
title: Microsoft and customer responsibilities for Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/customer-microsoft-responsibilities
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn the responsibilities of Microsoft and customers for Windows 365.
keywords: 
author: ErikjeMS
ms.author: hinallur
manager: dougeby
ms.date: 2025-04-16T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: shupadhyaya
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: a1c80379-6d13-80e1-dc47-0f4a636a51b9
document_version_independent_id: a1c80379-6d13-80e1-dc47-0f4a636a51b9
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/customer-microsoft-responsibilities.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: customer-microsoft-responsibilities
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/customer-microsoft-responsibilities.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: f6206041-98f0-a40d-e77e-4d5f16ed464c
---

# Microsoft and customer responsibilities for Windows 365 | Microsoft Learn

Windows 365 follows a shared responsibility model like the [rest of the online services in the Microsoft Cloud](/en-us/compliance/assurance/assurance-risk-assessment-guide). The responsibilities for managing Windows 365 are clearly divided between Microsoft and the customer:

- Microsoft is responsible for the security and compliance of the cloud infrastructure.
- Customers are responsible for managing and configuring security and compliance in the cloud according to their specific needs and risk tolerance.

For more information, see [Windows 365 service description service responsibility section](/en-us/office365/servicedescriptions/windows-365-service-description/windows-365-service-description?branch=main#service-responsibility).

If a service incident occurs, Microsoft might temporarily adjust infrastructure, networking, or other managed components to restore or maintain the stability and availability of the Windows 365 service. These adjustments ensure reliable operation and uninterrupted user access.

This document applies only to Windows 365 and doesn't apply to any other Microsoft online services or products, including the Windows operating system. This document doesn't supersede any product terms or the service level agreement (SLA) for Windows 365. For more information, see the [Windows 365 Service Description](/en-us/office365/servicedescriptions/windows-365-service-description/windows-365-service-description) and [SLA](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services).

## Microsoft responsibilities

**Change management**: Microsoft manages all service infrastructure updates and changes in accordance with SOC 2 and ISO 27001 standards.

**Gallery image**: Production and publication of gallery images on a monthly basis.

**Intune enrollment**: Microsoft makes sure that Cloud PCs are automatically enrolled in Microsoft Intune. An exception to this automatic enrollment is when the customer uses Windows 365 Business and doesn't choose automatic enrollment or lacks the required licensing.

**Network connectivity**:

For Microsoft-hosted networks, Microsoft manages:

- Network connectivity for Windows 365, including Azure Networking and on-site infrastructure configurations (like firewalls, proxies, and other settings).
- Network security and Remote Desktop Protocol (RDP) connectivity, ensuring a stable connection.
- Microsoft manages the core network infrastructure.

**Security and compliance**: Microsoft manages risks related to fraud, abuse, and malicious activity as explained in the [Product Use Rights](/en-us/legal/windows-365/windows-365-app-license-terms) and the [Microsoft Online Services Agreement](https://www.microsoft.com/servicesagreement/).

**Service critical components**: Microsoft deploys, manages, and maintains the critical components needed to reliably deliver Windows 365, as outlined in the Service Description and SLA. These components include: Service agents: RD-Agent, Azure Agent, CMD Agent.

**Service-level commitments**: Microsoft makes sure Windows 365 availability and performance as defined in the SLA.

## Customer responsibilities

**Change management**: Integrating and testing Microsoft’s service changes within the organization's IT environment.

**Licensing**: Assignment and managing Windows 365 licenses to end users.

**Network connectivity**:

For Azure network connections (ANC), customers manage:

- Security, network configurations, firewalls, VPNs, routing, proxies, and any other network components under their control.
- Proper configuration of their virtual network, as any misconfigurations can affect connectivity to their Cloud PCs.

In both ANC and Microsoft-hosted networks, customers are responsible for any operating system-level networking configurations or network security controls they apply. These configurations and controls include third-party agents such as VPNs, custom proxies, or traffic inspection tools that can affect network connectivity.

**Ongoing configurations**: Managing configurations like time zone redirection, USB redirection, and location redirection.

**Operating system and application management**: Installing updates, configuring settings, and managing OS and application lifecycles running on their Cloud PCs. This responsibility excludes the service-critical components that are Microsoft responsibilities.

**Gallery images (third-party applications)**: For gallery images that include third-party applications or developer tools, customers are responsible for managing and maintaining those applications.

Preinstalled applications might not be managed through Microsoft Intune unless customers configure appropriate management policies. Customers who require Intune-based management should uninstall and redeploy applications using their own management workflows.

Customers are responsible for:

- Monitoring and remediating application security vulnerabilities.
- Installing security and software updates.
- Configuring application settings.
- Ensuring applications meet organizational security and compliance requirements.
- Managing antivirus and endpoint protection requirements.
- Redeploying or customizing applications as needed.

**Security and compliance**: Customers implementing endpoint security policies, antivirus protection, regulatory compliance measures, and monitoring security threats to the Cloud PC's operating system.

**User management and authentication**: Managing user accounts, access permissions, and identity security.

## Shared responsibilities

For shared responsibilities, such as network connectivity and security, customers must understand their role and take appropriate action when needed. This clear division promotes efficient operation and security of the Windows 365 environment.

Microsoft deploys some configurations and components during the initial provisioning of a Cloud PC. After deployment, customers are responsible for their ongoing management and configuration. Examples of such configurations and components include:

- Microsoft 365 Apps.
- Multimedia redirection plug-in.
- Windows operating system configurations, such as disabling port 3389, or enabling security features like Hypervisor-protected Code Integrity (HVCI) and Credential Guard through supported management tools.

**Network connectivity**:

For Microsoft-hosted networks, Microsoft manages:

- Network connectivity for Windows 365, including Azure Networking and on-site infrastructure configurations (like firewalls, proxies, and other settings).
- Network security and Remote Desktop Protocol (RDP) connectivity, ensuring a stable connection.
- Microsoft manages the core network infrastructure.

For Azure network connections (ANC), customers manage:

- Security, network configurations, firewalls, VPNs, routing, proxies, and any other network components under their control.
- Proper configuration of their virtual network, as any misconfigurations can affect connectivity to their Cloud PCs.

In both ANC and Microsoft-hosted networks, customers are responsible for any operating system-level networking configurations or network security controls they apply. These configurations and controls include third-party agents such as VPNs, custom proxies, or traffic inspection tools that can affect network connectivity.

**Security and monitoring**: Microsoft secures the cloud infrastructure. Customers manage Windows client OS and application security running in the cloud.

**Support and troubleshooting**: Microsoft provides platform-level support. Customers handle OS-level issues, application troubleshooting, and user-related concerns.