---
layout: Conceptual
title: Understanding Network Flows - Remote Desktop Protocol | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/understanding-remote-desktop-protocol-traffic
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Article describing Remote Desktop Protocol connectivity flows in Windows 365
author: PaulCollinge
ms.author: paulcoll
ms.service: windows-365
ms.topic: concept-article
ms.date: 2025-09-18T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
locale: en-us
document_id: 04823f82-c9cb-0286-b970-dbe3a6d3eb61
document_version_independent_id: 04823f82-c9cb-0286-b970-dbe3a6d3eb61
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/understanding-remote-desktop-protocol-traffic.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/understanding-remote-desktop-protocol-traffic
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/understanding-remote-desktop-protocol-traffic.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 779458ed-a739-b490-54a5-7c5dee5fe147
---

# Understanding Network Flows - Remote Desktop Protocol | Microsoft Learn

To ensure optimal performance and reliability in your Windows 365 deployment, it's important to understand the key connectivity requirements. These requirements fall into three main categories:

- **Remote Desktop Protocol (RDP) connectivity** – Applies equally to both the cloud environment and physical client devices.
- **Cloud service connectivity** – Covers the network requirements from the Cloud PC itself to the service.
- **Client device connectivity** – Includes the network configuration for physical endpoints accessing the service.

Proper configuration of each connectivity element is essential for delivering a seamless Windows 365 experience. This document focuses on understanding the RDP connectivity options available and how to optimize them for the highest levels of performance and reliability.

Note

RDP connectivity requires special attention. The same configuration principles apply to both cloud-hosted and physical devices.

## RDP Connectivity

RDP connectivity is a critical component of the Windows 365 experience. It enables users to connect seamlessly to their Cloud PCs and requires careful network configuration to ensure performance and reliability.

#### Characteristics of RDP Traffic

RDP traffic has several significant elements that require special consideration:

- **Latency sensitive:** RDP traffic must be delivered with minimal delay. While RDP is adept at handling challenging network conditions, optimizing for as low latency as possible helps maintain a responsive user experience.
- **Real-time:** Similar to Microsoft Teams media traffic, RDP traffic is real-time. Any delay can disrupt the user session.
- **High volume:** RDP sessions can generate substantial amounts of traffic. Routing this traffic efficiently and avoiding costly operations, such as TLS inspection, helps preserve performance and prevents overloading network devices.
- **Long-lived:** RDP connections often remain active for extended periods. Efficient routing reduces the impact on devices performing network address translation (NAT) and supports scalability.

To maintain a high-quality user experience, RDP traffic should be routed via the most direct and efficient path to Microsoft’s global infrastructure. Ensuring unnecessary inspection, filtering, or detours are avoided is essential.

Important

Failure to optimize RDP traffic can lead to degraded performance, session instability, and poor reliability for end users.

## Traditional RDP vs Windows 365 RDP

Windows 365 uses a modernized version of Remote Desktop Protocol (RDP), designed for cloud environments, and built to deliver a secure, seamless experience across diverse network conditions. This modern RDP differs significantly from the RDP used in traditional remote desktop environments.

### Traditional RDP

Traditional RDP, commonly used in on-premises environments, relies on inbound connectivity over Transmission Control Protocol (TCP) port 3389 to establish remote desktop sessions. This approach introduces security challenges as it requires opening inbound ports on the network perimeter.

### Modern RDP in Windows 365

Windows 365 uses a modern, cloud-first implementation of RDP that differs significantly from traditional models. It requires no inbound connectivity and relies on outbound traffic over the following protocols and ports, which should work in any correctly configured network:

- **TCP port 443**
- **UDP port 3478**

These connections are established from both the Cloud PC and the client device to Microsoft’s global connectivity infrastructure. Other RDP connection methods may also be available depending on the environment and are also outlined in this article.

This modern RDP model enhances security, simplifies deployment, and supports reliable remote display and input across varying network conditions.

Important

Windows 365 doesn't use traditional RDP. No inbound connectivity is required to access a Cloud PC.

## RDP Connectivity Methods in Windows 365

Windows 365 supports multiple RDP connectivity methods to ensure reliable performance, even in challenging network conditions. These methods can be divided into public and private network connectivity options.

### Public Network Connectivity methods

Windows 365 supports the following public connectivity options. These methods are the default for the service:

- **TCP-based Reverse Connect:** This is the primary method for all connections. It uses outbound RDP over TCP port 443 to establish the session.
- **Relayed UDP-based RDP Shortpath:** This method uses outbound RDP over UDP port 3478 and connects through Microsoft’s relay infrastructure for improved media performance.
- **Direct UDP-based RDP Shortpath:** This option establishes a direct, one-to-one connection over UDP, reducing latency and improving responsiveness. This method uses a STUN server to try to find a workable direct connectivity path between the user and their Cloud PC

### Private Network Connectivity method

1. **Direct UDP over Private Networks** Enables a one-to-one UDP connection over a private network. This method is applicable only for deployments using Azure Network Connection (ANC). This method may technically be feasible via VPN links but is unlikely to be selected as a transport option by Windows 365 due to low performance.

Note

Microsoft automatically selects the most optimal method based on network conditions and deployment type. No manual configuration is required for most scenarios. Windows 365 supports multiple RDP connectivity methods to ensure reliable performance, even in challenging network conditions.

## Public Network RDP Connectivity

### TCP-based Reverse Connect

Reverse Connect is the default method used for RDP connections in Windows 365. It initiates outbound connectivity over TCP port 443 and doesn't require a listener on either the client or Cloud PC side. This approach simplifies deployment and enhances security by eliminating the need for inbound connections and is used on every connection regardless of the eventual method used.

#### How Reverse Connect Works

1. **RD Agent Installation:** During provisioning, the RD Agent is installed on the Cloud PC to manage connectivity.
2. **Persistent Signaling Session:** On startup, the RD Agent establishes a persistent, outbound TLS-encrypted signaling session to the Windows 365 infrastructure. This process is automatic and requires no manual configuration.
3. **User Login:** On the physical client device, the user logs in using a supported client, such as the Windows App.
4. **Authentication:** Microsoft Entra ID authenticates the user and returns a token that enumerates the user's available resources.
5. **Token Validation:** The client passes the token to the feed subscription service, which validates it.
6. **Resource Enumeration:** The service returns a list of available Cloud PCs for the user in the form of digitally signed connection configurations.
7. **Connection Configuration Storage:** The client stores these configurations as `.rdp` files for each resource.
8. **Connection Initiation:** When the user selects a Cloud PC, the client connects to Azure Front Door (AFD) via an anycast listener. The nearest AFD node is automatically selected based on network egress.
9. **Gateway Selection:** AFD evaluates latency to all available gateways and selects the one with the lowest latency and fewest active connections.
10. **Secure Gateway Connection:** The client connects to the selected gateway using a secure TLS 1.3 connection. The gateway validates the request and contacts the broker.
11. **Broker Orchestration:** The broker identifies the target Cloud PC and uses the existing signaling channel to initiate the session.
12. **Cloud PC Connection:** The Remote Desktop stack on the Cloud PC initiates an outbound TLS 1.3 connection to the same gateway instance.
13. **Data Relay:** Once both endpoints are connected, the gateway relays data between them and forms the base Reverse Connect transport using a nested tunnel and the highest mutually supported TLS version (up to TLS 1.3).
14. **RDP Handshake** The client begins the RDP handshake to establish the session.

![Diagram showing TCP-based RDP Connection flow.](media/understanding-remote-desktop-protocol-traffic/rdp-reverse-connect-tcp.png)

*Diagram 1: Reverse Connect RDP over TCP port 443*

### Direct UDP-based RDP Shortpath (Using STUN)

Windows 365 also uses UDP based RDP connectivity to improve session performance, reliability, and throughput. Once a TCP based Reverse Connect session is established, Windows 365 attempts to upgrade the transport to UDP using one of two methods:

- **Direct RDP Shortpath:** Establishes a one-to-one UDP connection using STUN to facilitate.
- **Relayed RDP Shortpath:** Uses TURN to relay UDP traffic via a known IP and port.

#### How Direct UDP Shortpath Works

1. **Initial TCP Connection:** The RDP session begins over a TCP-based Reverse Connect transport via the gateway as described in this document.
2. **UDP Socket Creation:** If RDP Shortpath is enabled on the Cloud PC (enabled by default), the service creates UDP sockets on all viable network interfaces.
3. **STUN Discovery:** The Cloud PC attempts to connect to a Windows 365 STUN server on UDP port 3478. This temporary connection identifies the external IP address and port of the NAT device. No RDP traffic is routed through the STUN server.
4. **Candidate Exchange:** The Cloud PC shares its candidate IP and port information with the client via the established TCP session. The client also sends its own candidate list.
5. **Connection Attempt:** Both endpoints attempt to establish a direct UDP connection simultaneously. Because both initiate outbound traffic, this method often succeeds even through restrictive firewalls with a supported NAT type in place.
6. **Transport Evaluation:** If the direct connection is successful and determined to be the fastest path, all dynamic virtual channels, such as graphics, input, and device redirection, switch to the new UDP transport.
7. **Move to TURN:** If STUN-based connectivity isn't possible to establish, the system attempts to connect to TURN servers on UDP port 3478. This enables relayed UDP connectivity, which has a higher success rate across varied network conditions due to its ability to work on any NAT type and known IP subnet & port.

Note

This connectivity method doesn't traverse the STUN server. The STUN server is only used during the initial connection phase to identify the NAT configuration on both sides and enable a one-to-one connection.

UDP-based RDP Shortpath improves performance and reliability. It automatically attempts after TCP-based Reverse Connect and requires no manual configuration other than traffic optimization.

![Diagram showing RDP Shortpath using STUN for direct connectivity.](media/understanding-remote-desktop-protocol-traffic/rdp-shortpath-stun.png)

*Diagram 2: RDP Connectivity with RDP Shortpath using STUN*

## Known challenges with Direct RDP Shortpath (Using STUN)

Direct RDP Shortpath relies on STUN to establish a one-to-one UDP connection. While this method offers significant performance benefits over TCP based RDP connectivity, it may not succeed in certain network environments due to limitations in NAT behavior and firewall configurations. For this model of connectivity to be successful, the NAT type on the networks of both the physical device, and the Cloud PC need to be of a supported type.

It's also often challenging to identify the IP addresses required for this type of connectivity in advance, such as when configuring a VPN or Secure Web Gateway (SWG) bypass for remote users.

#### Scenarios Where Direct RDP Shortpath May Fail

Direct connectivity may not work in the following conditions, many of which are common in enterprise networks:

- **Double NAT:** For example, traffic routed through a Secure Web Gateway (SWG) or proxy applies Network Address Translation (NAT) twice, once on Azure egress and again at the VPN or SWG endpoint.
- **Internet proxies or inspection devices:** Routing through proxies or devices that inspect traffic can interfere with STUN-based connectivity. Bypass of these devices can be difficult due to lack of prior knowledge of NAT IP information.
- **Symmetric NAT:** Common in enterprise networks, symmetric NAT on either the Cloud PC or client side prevents successful STUN negotiation. Azure NAT Gateway uses this NAT type as do many other common enterprise NAT devices.
- **Restricted UDP access:** Networks that block or limit UDP traffic, or restrict access to specific ports or IP ranges, prevents direct connectivity and is common in enterprise networks. Working round this limitation is difficult due to the lack of prior knowledge of the ports and IP addresses used for the connection.
- **Carrier Grade NAT (CGN):** When multiple networks share a public IP address, STUN can't establish a unique path.

Due to these limitations, treat this method as a best-effort approach and avoid investing significant effort in making it work. Instead, prioritize optimizing relayed UDP via TURN, which functions reliably in almost all network conditions.

Learn more about RDP shortpath [here](/en-us/windows-365/enterprise/rdp-shortpath-public-networks).

Tip

Use the [avdnettest tool](/en-us/troubleshoot/azure/virtual-desktop/troubleshoot-rdp-shortpath) to check the NAT type used in your network environment.

#### Use of Relayed RDP Shortpath

Because of these limitations, Direct RDP Shortpath is a best-effort connectivity model. If it can't be established, Windows 365 automatically reverts to Relayed RDP Shortpath, which uses TURN servers and has a significantly higher success rate. This method works reliably because the subnet and port requirements for outbound traffic are known in advance and therefore can be opened and easily optimized.

Note

Relayed RDP Shortpath ensures consistent connectivity across a wider range of network conditions and also requires no inbound access.

## Relayed UDP-based RDP Shortpath (Using TURN)

Relayed RDP Shortpath provides a reliable method for UDP-based RDP connectivity when direct Shortpath isn't possible. This method uses globally distributed TURN servers within Microsoft’s infrastructure to relay RDP traffic between the client and Cloud PC. This connectivity model works automatically and doesn't require any configuration other than optimization of the required traffic. It's essential that this connectivity method is configured and optimized within your network environments.

#### Key Benefits

- **Bypasses NAT limitations:** Unlike STUN-based direct connections, TURN relays aren't affected by double NAT, symmetric NAT, or firewall restrictions.
- **Global reach:** TURN servers are deployed in over [47 regions worldwide](/en-us/azure/virtual-desktop/rdp-shortpath?tabs=public-networks), allowing traffic to be relayed through a location close to the user for optimal performance.
- **Predictable configuration:** Relayed traffic uses known IP subnets and ports, enabling firewall and network optimization, including proxy, Secure Web Gateway (SWG), and VPN bypass.

#### How Relayed RDP Shortpath Works

- **TCP-based Reverse Connect:** The RDP session begins over TCP port 443 using the Reverse Connect method.
- **Direct RDP Shortpath Attempt:** The system attempts to establish a direct UDP connection using STUN.
- **Configure TURN connectivity:** If direct connectivity fails, both the client and Cloud PC attempt outbound connections to the TURN infrastructure on UDP port 3478, specifically targeting the dedicated 51.5.0.0/16 subnet.
- **Transport Evaluation:** If the relayed connection is successful and determined to be the fastest path, all dynamic virtual channels such as graphics, input, and device redirection, switch to the new transport.
- **TCP Persistence:** If no UDP method succeeds, the RDP session continues over the existing TCP connection.
- **RDP Multipath:** With RDP Multipath multiple UDP connections are established to allow for seamless continued connectivity if issues occur on the active path.

![Diagram comparing all public RDP connection options: TCP, STUN, and TURN.](media/understanding-remote-desktop-protocol-traffic/all-public-rdp-options.png)

*Diagram 3: All Public RDP options*

Note

Relayed RDP Shortpath is automatically enabled and requires no manual configuration. It ensures consistent connectivity across a wide range of network environments. More information on RDP shortpath for public networks can be found [here](/en-us/azure/virtual-desktop/rdp-shortpath?tabs=public-networks).

## Private Network RDP Connectivity

#### RDP Shortpath for Managed Networks

Windows 365 supports a fourth RDP connectivity method for managed, private networks. This option is available only in specific deployment scenarios and offers direct UDP connectivity between the client device and the Cloud PC.

Important

This method isn't required for achieving high-performance connectivity to the service. The primary and default methods are the public methods described in this article.

#### Availability Conditions

RDP Shortpath for managed networks is supported only when:

- The deployment uses Azure Network Connection (ANC). This method of connectivity isn't available for Microsoft-hosted network deployments.
- There's **direct line-of-sight** between the physical device and the Cloud PC, via ExpressRoute or Site-to-Site VPN.
- The network path allows traffic to traverse successfully. Firewall rules must permit the required ports, protocols, and IP ranges.

#### Connection Methods

This connectivity can be established in one of two ways:

1. **RDP Shortpath Listener:** When configured, the Cloud PC listens on UDP port 3390 for incoming connections.
2. **ICE/STUN Discovery:** If the listener method isn't viable, ICE/STUN is used to discover available IP addresses and negotiate a dynamic port. The port range is configurable if needed.

Once the UDP connection is successfully established, the TCP-based public path is dropped, and the session continues over the private network.

For more detail see [RDP Shortpath for private networks documentation](/en-us/windows-365/enterprise/rdp-shortpath-private-networks)

![Diagram showing RDP Shortpath for managed or private networks.](media/understanding-remote-desktop-protocol-traffic/rdp-shortpath-managed-networks.png)

*Diagram 4: RDP Shortpath for Private Networks*

Note

This method provides direct connectivity in managed network environments but requires specific configuration and network conditions. The public TCP based method is still required initially to establish this type of connectivity.

## RDP Multipath

RDP Multipath is an innovative connectivity enhancement for Windows 365 that improves session reliability and performance by intelligently managing multiple network paths. It builds on RDP Shortpath and uses Interactive Connectivity Establishment (ICE) to discover and evaluate multiple UDP routes in real time, including those using STUN and TURN protocols.

This feature ensures that if the active path becomes unstable or fails, the system automatically switches to a backup path, without interrupting the user session. Multipath routing is especially beneficial in environments with fluctuating network conditions, offering a smoother and more resilient remote desktop experience.

For full details, visit the [RDP Multipath documentation](/en-us/windows-365/enterprise/rdp-multipath).

## RDP Connection method summary

The following table is a summary of the RDP methods available to securely connect to your Cloud PC.

Ensure you check the [Network Requirements page](/en-us/windows-365/enterprise/requirements-network) for the full connectivity requirements.

| RDP Method | Protocol/Port | FQDN | IP | Public/Private Network Method | Notes |
| --- | --- | --- | --- | --- | --- |
| TCP RDP (Reverse Connect) | TCP/443 | \*.wvd.microsoft.com | 40.64.144.0/20 covers the RDP connection element within this domain but not everything that resolves to it | Public | TCP based RDP relayed via Microsoft's global RDP gateway infrastructure - Initial connection method used in all cases. |
| Indirect UDP RDP (RDP via TURN) | UDP/3478 | n/a | 51.5.0.0/16 | Public | UDP based RDP relayed via Microsoft's global TURN infrastructure. Works in any network scenario if necessary endpoints are accessible. |
| Direct RDP using STUN | UDP/1024-65535 (Default 49152-65535) | n/a | 51.5.0.0/16 for STUN element. Public IP of NAT used on either side of connection | Public | Not possible in all network scenarios. Requires open access to any public IP if NAT IP isn't known in advance. |
| RDP Shortpath for managed networks | UDP/3390 (Configurable) | n/a | Private IPs of physical client and Cloud PC | Private | Requires direct line of sight between physical device and Cloud PC. Only possible with ANC deployments. |
| RDP Shortpath for managed networks using ICE/STUN | UDP/1024-65535 (Default 49152-65535) | n/a | 51.5.0.0/16 for STUN then private IP of physical device and Cloud PC | Private | Requires access to STUN server range and also direct line of sight between physical device and Cloud PC. Only possible with ANC deployments |

Important

The IP subnet 40.64.144.0/20 is used only for the TCP based RDP connection. The domain.wvd.microsoft.com also includes traffic that does not resolve to this subnet. Because of this, use the IP range for bypass and optimization rules. At the same time, make sure that \*.wvd.microsoft.com continues to use a path that does not depend on IP matching, such as a proxy, so that all required traffic can reach the service.

## Detecting which RDP transport is used.

For more detail on how to detect which transport method is in use for a particular connection see the article ‘[Verify RDP Shortpath is working’](/en-us/azure/virtual-desktop/configure-rdp-shortpath?tabs=intune%2Cportal%2Cconnection-information)