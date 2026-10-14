---
layout: Conceptual
title: Windows 365 Cloud PC Connectivity Requirements | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/understanding-network-connectivity-flows-cloud-side
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to configure Windows 365 Cloud PC connectivity for optimal performance, including Microsoft-hosted and Azure Network Connection options.
author: PaulCollinge
ms.author: paulcoll
ms.service: windows-365
ms.topic: article
ms.date: 2025-11-21T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
locale: en-us
document_id: 081abf88-c991-7f4e-d72e-b93cbe851f11
document_version_independent_id: 081abf88-c991-7f4e-d72e-b93cbe851f11
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/understanding-network-connectivity-flows-cloud-side.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/understanding-network-connectivity-flows-cloud-side
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/understanding-network-connectivity-flows-cloud-side.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 1486e805-eb88-5190-c068-d524bbc2b214
---

# Windows 365 Cloud PC Connectivity Requirements | Microsoft Learn

This document focuses on the connectivity and optimization required on the Windows 365 side to ensure successful provisioning and operation of your Cloud PCs.

## Introduction

Understanding Windows 365 connectivity requirements is critical for achieving optimal performance and reliability in your organization’s deployment.

Service connectivity requirements fall into three areas:

- [RDP connectivity](/en-us/windows-365/enterprise/understanding-remote-desktop-protocol-traffic)
- **Cloud-side service connectivity (this document)**
- **Physical client connectivity**

## Deployment Options

Windows 365 offers two deployment models for cloud network connectivity. The technical effort varies significantly between them. For details, see the [Deployment Options](/en-us/windows-365/enterprise/windows-365-network-deployment-options) documentation.

**Microsoft Hosted Network** is the recommended option due to:

- **Automatic configuration**: Microsoft provides all underlying network connectivity.
- **Managed infrastructure**: Microsoft handles maintenance, upgrades, and security.
- **Secure by design**: No inbound connectivity or cross-Cloud PC traffic.
- **Low complexity**: Minimal customer-side dependencies enable rapid deployment.
- **High flexibility**: Ideal for quick setup or business continuity scenarios.
- **Lower Cost:** The underlying network infrastructure is provided for you by Microsoft.

Choosing this option vastly simplifies connectivity configuration and operation, and should be the default choice unless the Azure Network Connection (ANC) model is required.

**Azure Network Connection (ANC).** ANC requires full network configuration and maintenance on the customer side:

- **Customer-managed network**: Configure routing, rules, and security in your own VNet, within your own Azure subscription.
- **Ongoing maintenance**: Beyond Azure defaults, your network team manages updates and general maintenance.
- **Security responsibility**: Your team secures the network.
- **Azure network expertise required**: Azure networking skills required to deploy and operate the underlying network.
- **Longer deployment times**: Higher overhead and lower flexibility.
- **Network costs:** Network elements, including bandwidth and firewalls, are billed to your Azure subscription.

There are two elements to understand when configuring connectivity on the Cloud PC side, and these elements differ depending on the deployment option chosen:

- **Underlying network requirements**: The configuration to the underlying network which the Cloud PC's virtual network card sits in.
- **Cloud PC configuration**: The network configuration applied to the Cloud PC itself, such as Proxy, VPN, or Secure Web Gateway (SWG) settings and software.

## Microsoft Hosted Network Connectivity Requirements

#### Underlying network requirements:

No configuration is required because Microsoft fully manages the infrastructure on your behalf.

#### Cloud PC configuration:

VPN and Secure Web Gateway (SWG) software can affect traffic flow and divert it from a direct path via the underlying network. Follow these guidelines to ensure high performance and reliability:

1. [Optimize RDP](/en-us/windows-365/enterprise/optimization-of-rdp) traffic by bypassing VPN/SWG tunnels and routing directly to Microsoft’s backbone.
2. Bypass other [required endpoints](/en-us/windows-365/enterprise/requirements-network) from VPN/SWG tunnels for direct service access where possible.
3. Ensure endpoints remain accessible if traffic is inadvertently routed through VPN/SWG, for example by ensuring they're allowed and not inspected through the SWG solution.
4. Configure pre-logon or machine tunnels to bypass required endpoints. Failure to do so impacts Cloud PC availability as connectivity is required before a user logs on to their Cloud PC.
5. Consider bypassing VPN/SWGs for other Microsoft 365 traffic that benefits from Direct Routing such as [Microsoft 365 traffic](/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges). Microsoft's network provides a high bandwidth low latency path to these services.

In the following example, we see a Microsoft Hosted Network deployed Cloud PC with Secure Web Gateway software installed.

- Path 1, shown as a dashed green line, sends RDP and other key endpoints directly to Microsoft’s network, bypassing the SWG tunnel. This direct route improves performance and reliability by avoiding the traffic hairpinning through the SWG.
- Path 2, shown as a solid blue line, sends all other traffic through the SWG tunnel or private access solution when needed. Microsoft’s high-speed network peers directly with the internet to reach external services.

![Screenshot of the ANC with optimized RDP and local Azure Firewall default path.](media/understanding-network-connectivity-flows-cloud-side/microsoft-hosted-network-rdp-optimized.png)

*Diagram 1: ANC with optimized RDP and local Azure Firewall default path.*

## Azure Network Connection (ANC) Connectivity Requirements

To maintain reliability and performance for ANC deployments, ensure the following best-practice configurations are in place. As the underlying network in this deployment option is fully within your own Azure subscription, there are a considerable number of requirements to ensure are in place. See [this document](/en-us/windows-365/enterprise/create-azure-network-connection) for guidance on how to initially create an ANC.

#### Underlying network requirements:

1. **Allocate [sufficient IP space](/en-us/windows-365/enterprise/create-azure-network-connection):** Twice the maximum Cloud PC count is recommended. Keep at least 50% free for disaster recovery scenarios where all Cloud PCs may need to be reprovisioned.
2. **Configure DNS:** Use Azure DNS or a reachable custom DNS server. Ensure robust name resolution, using multiple DNS servers is recommended for redundancy and high availability.
3. **Disable TLS inspection:** Traffic to **[required endpoints](/en-us/windows-365/enterprise/requirements-network)** must not be inspected; TLS interception breaks critical flows.
4. **Use ExpressRoute or site-to-site VPN only for on-premises traffic:** Scale circuits for Windows 365 load. Use local Azure breakout for all other traffic where possible.
5. **Route [required endpoints](/en-us/windows-365/enterprise/requirements-network) to an egress in Azure:** Avoid routing via on-premises as doing so provides an inefficient path, which may lead to performance or reliability issues. Use [FQDN tags](/en-us/windows-365/enterprise/azure-firewall-windows-365) to automate rules if using Azure Firewall.
6. **Apply FQDN-based rules on any Network Virtual Appliance (NVA) used:** Many endpoints can't be represented as IP ranges; configure rules accordingly.
7. **Use NAT Gateway instead of an NVA such as Azure Firewall for critical, long-lived outbound traffic such as [RDP](/en-us/windows-365/enterprise/understanding-remote-desktop-protocol-traffic) and VPN/SWG traffic:** A NAT Gateway provides the most optimized path for this critical traffic, and avoids issues caused by load on the firewall or scale-in causing dropped connections.
8. **Configure [User Defined Routes](/en-us/azure/virtual-network/virtual-networks-udr-overview) (UDRs) for Direct Routing of RDP traffic:** Use the `WindowsVirtualDesktop` service tag to direct RDP traffic to the NAT Gateway
9. **Assign multiple public IPs to the NAT gateway:** Multiple IPs distribute traffic across the IP addresses used, and prevents DDoS protection triggers.
10. **Verify [Network Security Groups](/en-us/azure/virtual-network/network-security-groups-overview) (NSGs):** Ensure they don't block required endpoints.
11. **No inbound connectivity required:** All traffic is outbound.
12. **Run [ANC health check](/en-us/troubleshoot/windows-365/health-checks):** Validate configuration and remediate issues before provisioning Cloud PCs.

![remote-desktop-protocol-optimized-azure-network](media/understanding-network-connectivity-flows-cloud-side/remote-desktop-protocol-optimized-in-azure-network-new.png)

*Diagram 2: ANC with optimized RDP and local Azure Firewall default path.*

This diagram shows three main routes configured from the Azure virtual network (VNet):

**Default route (0.0.0.0/0 User Defined Route UDR)** Sends all traffic to the Azure Firewall’s private IP, which becomes the default path. The firewall allows approved traffic to Microsoft’s network and the internet as required. Use this path for other [Windows 365 service endpoints](/en-us/windows-365/enterprise/requirements-network?tabs=enterprise%2Cent) that don’t require special handling.

1. **Optimized route for RDP traffic** A more specific UDR sends the `WindowsVirtualDesktop` service tag to '**Internet'**, which in this example uses a NAT Gateway. This path is optimized for RDP and should also be used for long-lived or latency-sensitive traffic that doesn’t need to traverse the firewall. 'Internet' doesn't mean this traffic reaches the public internet for Microsoft hosted endpoints.
2. **On-premises route** The ExpressRoute Gateway provides a more specific route for on-premises traffic, for example, anything in the `10.0.0.0/8` range.

See the document [Use Azure Firewall to manage and secure Windows 365 environments](/en-us/windows-365/enterprise/azure-firewall-windows-365) for more detail.

#### Cloud PC Configuration

As is the case with Microsoft Hosted Network deployments, even if the underlying network is correctly configured, changes to network connectivity on the Cloud PC itself can impact deployment and performance and reliability. Ensure the following steps are also followed for ANC deployments.

1. [Optimize RDP](/en-us/windows-365/enterprise/optimization-of-rdp) traffic by bypassing VPN/SWG tunnels and routing directly to Microsoft’s backbone via the ANC network.
2. Bypass [required endpoints](/en-us/windows-365/enterprise/requirements-network) from VPN/SWG tunnels for direct service access.
3. Ensure endpoints remain accessible if traffic is inadvertently routed through VPN/SWG. For example, ensure endpoints are added to allow lists.
4. Configure pre-logon or machine tunnels to bypass required endpoints. Failure to do so impacts Cloud PC availability.
5. Consider bypassing VPN/SWGs for other Microsoft 365 traffic that benefits from direct routing such as [Microsoft 365 traffic](/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges).