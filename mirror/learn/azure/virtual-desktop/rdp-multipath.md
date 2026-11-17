---
layout: Conceptual
title: Use DS Multipath to improve Azure Virtual Desktop connections - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/rdp-multipath
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: cawerner
manager: eliotgra
ms.author: cawerner
ms.service: azure-virtual-desktop
description: Learn how DS Multipath enhances remote connections to an Azure Virtual Desktop session by intelligently managing multiple network paths.
ms.topic: how-to
ms.date: 2026-10-23T00:00:00.0000000Z
locale: en-us
document_id: 12f15fbe-4cd6-872f-2bc9-d461cfaaf15d
document_version_independent_id: 12f15fbe-4cd6-872f-2bc9-d461cfaaf15d
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/rdp-multipath.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: rdp-multipath
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/rdp-multipath.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: f0fb3d84-7a29-4898-30e1-2f3c02e363c0
---

# Use DS Multipath to improve Azure Virtual Desktop connections - Azure Virtual Desktop | Microsoft Learn

Direct Stream (DS) Multipath improves session stability by continuously monitoring multiple network paths and dynamically selecting the most reliable one. This intelligent switching mechanism helps reduce the likelihood of disconnections and contributes to a smoother and more consistent user experience across different network conditions.

It offers several key benefits:

- **Seamless integration**: No configuration changes are needed beyond ensuring your environment supports [DS Shortpath](/en-us/azure/virtual-desktop/rdp-shortpath?tabs=public-networks).
- **Intelligent path management**: ICE discovers and evaluates multiple Direct Stream (DS) Shortpath routes using User Datagram Protocol (UDP) over STUN (Simple Traversal Underneath NAT) and TURN (Traversal Using Relays around NAT) protocols.
- **Enhanced reliability**: Backup paths remain on standby. If the active path becomes unstable or fails, DS Multipath automatically switches to the next best path, reducing session drops and interruptions.

DS Multipath uses multiple network paths to improve connection reliability. These paths can include combinations of UDP-based STUN or TURN connections when UDP connectivity is available, along with redundant TCP-based Reverse Connect paths established using Rendezvous. If the main transport path becomes degraded or fails, the system automatically switches to a backup available UDP or TCP transport path. If all paths are lost—such as during a network outage—the system attempts to reconnect once network connectivity is restored. 

The following diagram illustrates how DS Multipath works with Azure Virtual Desktop. In this user scenario, the primary active transport path is UDP via STUN, supplemented by redundant UDP connections through a TURN server.

When UDP‑based DS Shortpath connectivity is available, UDP remains the preferred transport protocol for optimal performance and reliability. In addition to maintaining redundant UDP paths, Azure Virtual Desktop can establish redundant TCP standby transport paths to improve overall session resiliency.

![Diagram that shows RDP Multipath network paths.](media/rdp-multipath/image.png)

## Availability

DS Multipath capabilities are available across the following Azure environments:

| Environment | Multiple UDP transport paths | Redundant TCP transport paths |
| --- | --- | --- |
| Azure public cloud | Generally available | Generally available |
| Azure Government | Generally available | Generally available |

## Prerequisites

DS Multipath works automatically when the following prerequisites are met:

- Microsoft recommends configuring DS Shortpath as the primary transport protocol to maximize the resiliency benefits of DS Multipath. For more information, see [Configure DS Shortpath](/en-us/azure/virtual-desktop/rdp-shortpath?tabs=public-networks).
- Windows App for Windows:

    - Connections must be from a local Windows device using [Windows App, version 2.0.559.0](/en-us/windows-app/whats-new?tabs=windows) or later, which is the minimum supported version for DS Multipath. This version enables DS Multipath with multiple UDP transport paths.
    - To take advantage of the latest DS Multipath enhancements, including support for **multiple UDP transport paths and redundant TCP transport paths**, connections must use [Windows App Version 2.0.1069.0](/en-us/windows-app/whats-new?tabs=windows) or later
- Windows App for macOS Beta: DS Multipath with multiple UDP transport paths is supported with Windows App for macOS [Beta version 11.3.8 (3048)](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/udp%20test).
- Other platforms aren't currently supported.

## Required network endpoints for DS transport

To support DS connectivity using UDP-based DS Shortpath and DS Multipath, as well as TCP-based connections over Reverse Connect, ensure outbound connectivity to the following endpoints:

# [Azure cloud](#tab/azure)
| # | DS method | FQDN | IP address | Protocol/port | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | TCP-based DS | `*.wvd.microsoft.com` | `40.64.144.0/20` | TCP 443 | TCP-based DS connection. The initial connection to every session host or Cloud PC uses this connection. |
| 2 | UDP-based DS via TURN | N/A | `51.5.0.0/16` | UDP 3478 | Relayed UDP-based DS connection using TURN servers. This method works when direct connectivity isn't possible. |
| 3 | UDP-based DS using STUN | N/A | `51.5.0.0/16` | UDP 1024-65535Default: 49152-65535 | Direct one-to-one UDP connection between the user device and the session host or Cloud PC. |

# [Azure for US Government](#tab/azure-government)
Important

DS Shortpath connectivity through the endpoints listed in this tab is currently available in public preview for Azure Government. Availability is limited to designated validation rings during the preview.

| # | DS method | FQDN | IP address | Protocol/port | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | TCP-based DS | N/A | `20.159.80.0/24` | TCP 443 | TCP-based DS connection. The initial connection to every session host or Cloud PC uses this connection. |
| 2 | UDP-based DS via TURN | N/A | `20.140.236.0/22` | UDP 3478 | Relayed UDP-based DS connection using TURN servers. |
| 3 | UDP-based DS using STUN | N/A | `20.140.236.0/22` | UDP 1024-65535Default: 49152-65535 | Direct one-to-one UDP connection between the user device and the session host. |

### Port scaling considerations

When using DS Multipath, customers should plan firewall and network capacity with **per‑user port scaling** in mind.

Each active user session can establish **up to five outbound transport paths**:

- **Up to three UDP ports** for UDP‑based DS Shortpath and Multipath connections (for example, primary and redundant UDP paths discovered through STUN or TURN).
- **Up to two TCP ports** for TCP‑based DS connections over Reverse Connect, including redundant TCP transport paths when available.

Ensure that firewall rules, NAT capacity, and port exhaustion limits are configured to accommodate the expected number of concurrent user sessions and their associated transport paths at scale.

Important

Microsoft recommends using **Windows App version 2.0.1069.0 or later and configuring DS Shortpath** as the primary transport protocol for the best DS Multipath experience. With Windows App version 2.0.559.0 or later, users benefit from DS Multipath with multiple UDP transport paths. With Windows App version 2.0.1069.0 or later, users gain the additional resiliency benefits of redundant TCP transport paths. If UDP connectivity is unavailable or restricted by network policy, DS Multipath can continue to provide resiliency through redundant TCP transport paths.

## Verify DS Multipath connectivity

There are two ways to verify that DS Multipath is being used for a connection:

- Users can check the connection status of a remote session from the connection bar, which shows DS Multipath is enabled, as shown in the following example screenshot:

    ![A screenshot of connection information showing that RDP Multipath is enabled.](media/rdp-multipath/rdp-multipath-connection-bar.png)
- Azure Virtual Desktop administrators can view connection reliability information in Azure Virtual Desktop Insights. For more information, see the [connection reliability use case for Azure Virtual Desktop Insights](insights-use-cases#connection-reliability).

---