---
layout: Conceptual
title: Azure Private Link with Azure Virtual Desktop - Azure - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/private-link-overview
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: PaulCollinge
manager: eliotgra
ms.author: paulcoll
ms.service: azure-virtual-desktop
description: Learn about using Private Link with Azure Virtual Desktop to privately connect to your remote resources.
ms.topic: article
ms.date: 2023-12-08T00:00:00.0000000Z
locale: en-us
document_id: 6ead4e6e-7507-e771-09ea-412cac1afd92
document_version_independent_id: 6ead4e6e-7507-e771-09ea-412cac1afd92
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/private-link-overview.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: private-link-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/private-link-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/16cd61cd-9ecf-429b-b494-91576c41f8e4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/c4bdb33a-5524-4b66-b162-03f5621d7902
platformId: 02b83ed3-f6a7-8fea-9bed-b98d9ca52c6a
---

# Azure Private Link with Azure Virtual Desktop - Azure - Azure Virtual Desktop | Microsoft Learn

You can use [Azure Private Link](/en-us/azure/private-link/private-link-overview) with Azure Virtual Desktop to privately connect to your remote resources. By creating a [private endpoint](/en-us/azure/private-link/private-endpoint-overview), traffic between your virtual network and the service remains on the Microsoft network, so you no longer need to expose your service to the public internet. You also use a VPN or ExpressRoute for your users with the Remote Desktop client to connect to the virtual network. Keeping traffic within the Microsoft network improves security and keeps your data safe. This article describes how Private Link can help you secure your Azure Virtual Desktop environment.

## How does Private Link work with Azure Virtual Desktop?

Azure Virtual Desktop has three workflows with three corresponding resource types to use with private endpoints. These workflows are:

1. **Initial feed discovery**: lets the client discover all workspaces assigned to a user. To enable this process, you must create a single private endpoint to the *global* sub-resource to any workspace. However, you can only create one private endpoint in your entire Azure Virtual Desktop deployment. This endpoint creates Domain Name System (DNS) entries and private IP routes for the global fully qualified domain name (FQDN) needed for initial feed discovery. This connection becomes a single, shared route for all clients to use.
2. **Feed download**: the client downloads all connection details for a specific user for the workspaces that host their application groups. You create a private endpoint for the *feed* sub-resource for each workspace you want to use with Private Link.
3. **Connections to host pools**: every connection to a host pool has two sides - clients and session hosts. You need to create a private endpoint for the *connection* sub-resource for each host pool you want to use with Private Link.

The following high-level diagram shows how Private Link securely connects a local client to the Azure Virtual Desktop service. For more detailed information about client connections, see Client connection sequence. ![A high-level diagram that shows Private Link connecting a local client to the Azure Virtual Desktop.](media/private-link-overview/pl-with-shortpath-architecture.png)

### Supported scenarios

When adding Private Link with Azure Virtual Desktop, you have the following supported scenarios to connect to Azure Virtual Desktop. Which scenario you choose depends on your requirements. You can either share these private endpoints across your network topology or you can isolate your virtual networks so that each has their own private endpoint to the host pool or workspace.

1. All parts of the connection - initial feed discovery, feed download, and remote session connections for clients and session hosts - use private routes. You need the following private endpoints:

    | Purpose | Resource type | Target sub-resource | Endpoint quantity |
    | --- | --- | --- | --- |
    | Connections to host pools | Microsoft.DesktopVirtualization/hostpools | connection | One per host pool |
    | Feed download | Microsoft.DesktopVirtualization/workspaces | feed | One per workspace |
    | Initial feed discovery | Microsoft.DesktopVirtualization/workspaces | global | **Only one for all your Azure Virtual Desktop deployments** |
2. Feed download and remote session connections for clients and session hosts use private routes, but initial feed discovery uses public routes. You need the following private endpoints. The endpoint for initial feed discovery isn't required.

    | Purpose | Resource type | Target sub-resource | Endpoint quantity |
    | --- | --- | --- | --- |
    | Connections to host pools | Microsoft.DesktopVirtualization/hostpools | connection | One per host pool |
    | Feed download | Microsoft.DesktopVirtualization/workspaces | feed | One per workspace |
3. Only remote session connections for clients and session hosts use private routes, but initial feed discovery and feed download use public routes. You need the following private endpoint(s). Endpoints to workspaces aren't required.

    | Purpose | Resource type | Target sub-resource | Endpoint quantity |
    | --- | --- | --- | --- |
    | Connections to host pools | Microsoft.DesktopVirtualization/hostpools | connection | One per host pool |
4. Both clients and session host VMs use public routes. Private Link isn't used in this scenario.

Important

- If you create a private endpoint for initial feed discovery, the workspace used for the global sub-resource governs the shared Fully Qualified Domain Name (FQDN), facilitating the initial discovery of feeds across all workspaces. You should create a separate workspace that is only used for this purpose and doesn't have any application groups registered to it. Deleting this workspace will cause all feed discovery processes to stop working.
- You can't control access to the workspace used for the initial feed discovery (global sub-resource). If you configure this workspace to only allow private access, the setting is ignored. This workspace is always accessible from public routes.
- IP address allocations are subject to change as the demand for IP addresses increases. During capacity expansions, additional addresses are needed for private endpoints. It's important you consider potential address space exhaustion and ensure sufficient headroom for growth. For more information on determining the appropriate network configuration for private endpoints in either a hub or a spoke topology, see [Decision tree for Private Link deployment](/en-us/azure/architecture/networking/guide/private-link-hub-spoke-network#decision-tree-for-private-link-deployment).

### UDP with Private Link (Opt‑in)

Azure Virtual Desktop supports UDP traffic with Private Link only when you opt in from the Azure portal host pool **Networking** page. If you do not opt in, UDP traffic over Private Link is blocked.

**How to opt in (portal):**

1. In the Azure portal, open your **Azure Virtual Desktop** host pool.
2. Select **Networking -&gt; Public access.**
3. Under **Public access**, choose the radio button **Enable public access for end users, use private access for session hosts***or***Disable public access and use private access**. The UDP opt‑in checkbox appears for these selections.
4. Select **Allow Direct UDP network path over Private Link** to enable UDP‑based transports (for example, [RDP Shortpath for managed networks](/en-us/azure/virtual-desktop/rdp-shortpath?tabs=managed-networks)).

\*\* **Important configuration requirement** After you enable the UDP opt‑in checkbox, **disable RDP Shortpath for public networks options** in the **RDP Shortpath** tab:

Turn off **RDP Shortpath for public networks (via STUN)** and **RDP Shortpath for public networks (via TURN)**.

The portal blocks **Save** if those public Shortpath options remain enabled and shows a **Configuration Error** until you disable them.

Important

The UDP opt-in checkbox is **mandatory** for enabling RDP Shortpath with Private link. If the checkbox is not checked, RDP Shortpath will be blocked for Private Link connections.

### Configuration outcomes

You configure settings on the relevant Azure Virtual Desktop workspaces and host pools to set public or private access. For connections to a workspace, except the workspace used for initial feed discovery (global sub-resource), the following table details the outcome of each scenario:

| Configuration | Outcome |
| --- | --- |
| Public access **enabled** from all networks | Workspace feed requests are **allowed** from *public* routes.Workspace feed requests are **allowed** from *private* routes. |
| Public access **disabled** from all networks | Workspace feed requests are **denied** from *public* routes.Workspace feed requests are **allowed** from *private* routes. |

With the [reverse connect transport](network-connectivity#reverse-connect-transport), there are two network connections for connections to host pools: the client to the gateway, and the session host to the gateway. In addition to enabling or disabling public access for both connections, you can also choose to enable public access for clients connecting to the gateway and only allow private access for session hosts connecting to the gateway. The following table details the outcome of each scenario:

| Configuration | Outcome |
| --- | --- |
| Public access **enabled** from all networks | Remote sessions are **allowed** when either the client or session host is using a *public* route.Remote sessions are **allowed** when either the client or session host is using a *private* route. |
| Public access **disabled** from all networks | Remote sessions are **denied** when either the client or session host is using a *public* route.Remote sessions are **allowed** when both the client and session host are using a *private* route. |
| Public access **enabled** for client networks, but **disabled** for session host networks | Remote sessions are **denied** if the session host is using a *public* route, regardless of the route the client is using.Remote sessions are **allowed** as long as the session host is using a *private* route, regardless of the route the client is using. |

## Client connection sequence

When a user connects to Azure Virtual Desktop over Private Link, and Azure Virtual Desktop is configured to only allow client connections from private routes, the connection sequence is as follows:

1. With a supported client, a user subscribes to a workspace. The user's device queries DNS for the address `rdweb.wvd.microsoft.com` (or the corresponding address for other Azure environments).
2. Your private DNS zone for **privatelink-global.wvd.microsoft.com** returns the private IP address for the initial feed discovery (global sub-resource). If you're not using a private endpoint for initial feed discovery, a public IP address is returned.
3. For each workspace in the feed, a DNS query is made for the address `<workspaceId>.privatelink.wvd.microsoft.com`.
4. Your private DNS zone for **privatelink.wvd.microsoft.com** returns the private IP address for the workspace feed download, and downloads the feed using TCP port 443.
5. When connecting to a remote session, the `.rdp` file that comes from the workspace feed download contains the address for the Azure Virtual Desktop gateway service with the lowest latency for the user's device. A DNS query is made to an address in the format `<hostpoolId>.afdfp-rdgateway.wvd.microsoft.com`.
6. Your private DNS zone for **privatelink.wvd.microsoft.com** returns the private IP address for the Azure Virtual Desktop gateway service to use for the host pool providing the remote session. Orchestration through the virtual network and the private endpoint uses TCP port 443.
7. Following orchestration, the network traffic between the client, Azure Virtual Desktop gateway service, and session host is transferred over to a port in the TCP dynamic port range of 1 - 65535.

Important

If you intend to restrict network ports from either the user client devices or your session host VMs to the private endpoints, you will need to allow traffic across the entire TCP dynamic port range of 1 - 65535 to the private endpoint for the host pool resource using the *connection* sub-resource. The entire TCP dynamic port range is needed because Azure private networking internally maps these ports to the appropriate gateway that was selected during client orchestration. If you restrict ports to the private endpoint, your users may not be able to connect to Azure Virtual Desktop.

## Known issues and limitations

Private Link with Azure Virtual Desktop has the following limitations:

- Before you use Private Link for Azure Virtual Desktop, you need to [enable Private Link with Azure Virtual Desktop](private-link-setup#enable-private-link-with-azure-virtual-desktop-on-a-subscription) on each Azure subscription you want to Private Link with Azure Virtual Desktop.
- All [Remote Desktop clients to connect to Azure Virtual Desktop](/en-us/previous-versions/remote-desktop-client/overview) can be used with Private Link. If you're using the [Remote Desktop client for Windows](users/connect-windows) on a private network without internet access and you're subscribed to both public and private feeds, you aren't able to access your feed.
- After you've changed a private endpoint to a host pool, you must restart the *Remote Desktop Agent Loader* (*RDAgentBootLoader*) service on each session host in the host pool. You also need to restart this service whenever you change a host pool's network configuration. Instead of restarting the service, you can restart each session host.
- Early in the preview of Private Link with Azure Virtual Desktop, the private endpoint for the initial feed discovery (for the *global* sub-resource) shared the private DNS zone name of `privatelink.wvd.microsoft.com` with other private endpoints for workspaces and host pools. In this configuration, users are unable to establish private endpoints exclusively for host pools and workspaces. Starting September 1, 2023, sharing the private DNS zone in this configuration will no longer be supported. You need to create a new private endpoint for the *global* sub-resource to use the private DNS zone name of `privatelink-global.wvd.microsoft.com`. For the steps to do this, see [Initial feed discovery](private-link-setup#initial-feed-discovery).