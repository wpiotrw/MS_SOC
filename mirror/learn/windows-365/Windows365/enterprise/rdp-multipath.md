---
layout: Conceptual
title: Use RDP Multipath with Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/rdp-multipath
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to use RDP Multipath Windows 365 Cloud PCs.
author: ridalwan
ms.author: ridalwan
ms.service: windows-365
ms.topic: how-to
ms.date: 2025-07-10T00:00:00.0000000Z
ms.reviewer: ridalwan
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: 1a763fdd-45ad-1bf0-b809-79a54f781b77
document_version_independent_id: 1a763fdd-45ad-1bf0-b809-79a54f781b77
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/rdp-multipath.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/rdp-multipath
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/rdp-multipath.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
platformId: 8c14b9d2-6bdd-d5a3-2d69-aa73835e691d
---

# Use RDP Multipath with Windows 365 | Microsoft Learn

## Overview

Remote Desktop Protocol (RDP) Multipath improves session resiliency by establishing multiple transport paths between the Windows App and your Cloud PC. By continuously monitoring these paths and automatically transitioning traffic when network conditions change, RDP Multipath helps reduce session interruptions and maintain a more reliable remote desktop experience.

RDP Multipath provides the following benefits:

- **Improved session resiliency** – Multiple transport paths help maintain connectivity during transient network issues and reduce the likelihood of session interruptions
- **Automatic path selection and failover** – RDP Multipath continuously evaluates available transport paths and automatically uses the most reliable path.
- **Support for UDP and TCP connectivity scenarios** – Users can benefit from RDP Multipath across a variety of network environments, including networks where UDP connectivity is restricted.
- **Seamless integration** – No additional configuration is required beyond ensuring your environment meets the prerequisites and is configured to use RDP Shortpath.

RDP Multipath automatically maintains multiple transport paths between the Windows App and your Cloud PC. If the active transport path becomes unavailable or degraded, traffic can transition to an alternate path to help maintain session continuity. If all transport paths are lost, such as during a local network outage, the connection attempts to recover once network connectivity is restored. 

Important

- If all paths fail example due to a local network outage, the system attempts to reconnect once connectivity is restored.

### How does this work?

The following diagram illustrates how RDP Multipath works with Windows 365 cloud PC. In this user scenario, the primary active transport path is UDP via STUN, supplemented by redundant UDP connections through a TURN server.

When UDP‑based RDP Shortpath connectivity is available, UDP remains the preferred transport protocol for optimal performance and reliability. In addition to maintaining redundant UDP paths, Windows 365 Cloud PC can establish redundant TCP standby transport paths to improve overall session resiliency.

![RDP Multipath with Redundant UDP and Websocket network paths](media/rdp-multipath/rdp-multipath-with-redundant-udp-and-websocket-network-paths.png)

### Availability

RDP Multipath is available for Windows 365 across the following Azure environments:

| Environment | Redundant UDP transport paths | Redundant TCP transport paths |
| --- | --- | --- |
| Azure public cloud | Generally available | Generally available |
| Azure Government | Generally available | Phased GA rollout started |

Note

RDP Multipath with redundant TCP transport paths is being enabled in Azure Government through a phased, quality-driven rollout. Until the rollout is complete, redundant TCP transport paths might not be consistently available across all Cloud PCs.

### Requirements

RDP Multipath works automatically when the following prerequisites are met:

- Microsoft recommends configuring RDP Shortpath as the primary transport protocol to maximize the resiliency benefits of RDP Multipath. For more information, see [Configure RDP Shortpath](/en-us/azure/virtual-desktop/rdp-shortpath?tabs=public-networks).
- Windows App for Windows:

    - Connections must be from a local Windows device using [Windows App, version 2.0.559.0](/en-us/windows-app/whats-new?tabs=windows) or later, which is the minimum supported version for RDP Multipath. This version enables RDP Multipath with multiple UDP transport paths.
    - To take advantage of the latest RDP Multipath enhancements, including support for **multiple UDP transport paths and redundant TCP transport paths**, connections must use [Windows App Version 2.0.1069.0](/en-us/windows-app/whats-new?tabs=windows) or later
- Windows App for macOS Beta: RDP Multipath with multiple UDP transport paths is supported with Windows App for macOS [Beta version 11.3.8 (3048)](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/udp%20test).
- Other platforms aren't currently supported.

Important

Microsoft recommends using **Windows App version 2.0.1069.0 or later and configuring RDP Shortpath** as the primary transport protocol for the best RDP Multipath experience. With Windows App version 2.0.559.0 or later, users benefit from RDP Multipath with multiple UDP transport paths. With Windows App version 2.0.1069.0 or later, users gain the additional resiliency benefits of redundant TCP transport paths. If UDP connectivity is unavailable or restricted by network policy, RDP Multipath can continue to provide resiliency through redundant TCP transport paths.

### Required network endpoints

The required network endpoints vary by cloud environment. Select your environment to view the applicable IP ranges and port requirements.

# [Azure cloud](#tab/azure)
| # | RDP method | FQDN | IP address | Protocol/port | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | TCP-based RDP | `*.wvd.microsoft.com` | `40.64.144.0/20` | TCP 443 | TCP-based RDP connection. The initial connection to every session host or Cloud PC uses this connection. |
| 2 | UDP-based RDP via TURN | N/A | `51.5.0.0/16` | UDP 3478 | Relayed UDP-based RDP connection using TURN servers. This method works when direct connectivity isn't possible. |
| 3 | UDP-based RDP using STUN | N/A | `51.5.0.0/16` | UDP 1024-65535Default: 49152-65535 | Direct one-to-one UDP connection between the user device and the session host or Cloud PC. |

# [Azure for US Government](#tab/azure-government)
Important

The phased GA rollout of RDP Shortpath connectivity using STUN and TURN has started for Windows 365 in Azure Government. Azure Government uses the dedicated `20.140.236.0/22` IP range for STUN and TURN connectivity. Availability will expand progressively as the phased rollout continues.

| # | RDP method | FQDN | IP address | Protocol/port | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | TCP-based RDP | N/A | `20.159.80.0/24` | TCP 443 | TCP-based RDP connection. The initial connection to every session host or Cloud PC uses this connection. |
| 2 | UDP-based RDP via TURN | N/A | `20.140.236.0/22` | UDP 3478 | Relayed UDP-based RDP connection using TURN servers. Phased rollout started. |
| 3 | UDP-based RDP using STUN | N/A | `20.140.236.0/22` | UDP 1024-65535Default: 49152-65535 | Direct one-to-one UDP connection between the user device and the session host. |

### Port scaling considerations

When using RDP Shortpath and RDP Multipath, customers should plan firewall and network capacity with **per‑user port scaling** in mind.

Each active user session can establish **up to five outbound transport paths**:

- **Up to three UDP ports** for UDP‑based RDP Shortpath and Multipath connections (for example, primary and redundant UDP paths discovered through STUN or TURN).
- **Up to two TCP ports** for TCP‑based RDP connections over Reverse Connect, including redundant TCP transport paths when available.

Ensure that firewall rules, NAT capacity, and port exhaustion limits are configured to accommodate the expected number of concurrent user sessions and their associated transport paths at scale.

Note

UDP-based connectivity remains the preferred transport protocol for optimal performance and reliability. In environments where UDP connectivity is restricted or unavailable due to firewall or proxy requirements, Windows 365 Cloud PCs connections rely on TCP-based transport over port 443.

### Verify RDP Multipath connectivity

Users can check the connection status of a remote session from the connection bar, which shows RDP Multipath is enabled, as shown in the following example screenshot:

![A screenshot of connection information showing that RDP Multipath is enabled.](media/rdp-multipath/multipath-connection-bar.png)

---