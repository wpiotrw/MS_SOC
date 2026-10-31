---
layout: Conceptual
title: Microsoft Purview private endpoints and managed virtual networks frequently for using the classic governance portal FAQ | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-private-link-faq
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article answers frequently asked questions about Microsoft Purview private endpoints and managed virtunal networks when using the classic governance portal.
locale: en-us
document_id: a058fd67-97a4-0ad1-d0ae-bb4e93d53595
document_version_independent_id: a058fd67-97a4-0ad1-d0ae-bb4e93d53595
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-private-link-faq.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-private-link-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-private-link-faq.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: dba3373c-3448-7946-0b64-7595647d2619
---

# Microsoft Purview private endpoints and managed virtual networks frequently for using the classic governance portal FAQ | Microsoft Learn

Important

This article covers private endpoints for the classic Microsoft Purview governance portal (https://web.purview.azure.com). If you're using the new Microsoft Purview portal (https://purview.microsoft.com/), follow the [documentation for private endpoints in the Microsoft Purview portal](data-governance-private-endpoints).

This article answers common questions that customers and field teams often ask about Microsoft Purview network configurations by using [Azure Private Link](/en-us/azure/private-link/private-link-overview) or [Microsoft Purview Managed VNets](data-governance-private-endpoints-managed-virtual-network). It's intended to clarify questions about Microsoft Purview firewall settings, private endpoints, DNS configuration, and related configurations.

To set up Microsoft Purview by using Private Link, see [Use private endpoints for your Microsoft Purview account](data-gov-classic-private-link). To configure Managed VNets for a Microsoft Purview account, see [Use a Managed virtual network with your Microsoft Purview account](data-governance-private-endpoints-managed-virtual-network).

## When should I use a self-hosted integration runtime, Managed virtual network IR, or Azure IR?

Learn more from [Choose the right integration runtime configuration for your scenario](data-map-integration-runtime-choose).

## Can I use both self-hosted integration runtime and Managed virtual network IR inside a Microsoft Purview account?

Yes. You can use one or all of the runtime options in a single Microsoft Purview account: Azure IR, Managed virtual network IR, and self-hosted integration runtime. You can use only one runtime option in a single scan.

## What's the purpose of deploying the Microsoft Purview account private endpoint?

The Microsoft Purview account private endpoint is used to add another layer of security by enabling scenarios where only client calls that originate from within the virtual network are allowed to access the account. This private endpoint is also a prerequisite for the portal private endpoint.

## What's the purpose of deploying the Microsoft Purview portal private endpoint?

The Microsoft Purview portal private endpoint provides private connectivity to the classic Microsoft Purview governance portal.

## What's the purpose of deploying the Microsoft Purview ingestion private endpoints?

Microsoft Purview can scan data sources in Azure or an on-premises environment by using ingestion private endpoints. Three other private endpoint resources are deployed and linked to Microsoft Purview managed or configured resources when ingestion private endpoints are created:

- If you're using a [managed Event Hubs for kafka notifications](data-map-kafa-notifications), **namespace** is linked to a Microsoft Purview configured Event Hubs namespace.
- If your account was created before December 15, 2023:
    - **Blob** is linked to a Microsoft Purview managed storage account.
    - **Queue** is linked to a Microsoft Purview managed storage account.
- If your account was created after December 15, 2023 (or deployed using API version 2023-05-01-preview onwards):
    - **Blob** is linked to a Microsoft Purview ingestion storage.
    - **Queue** is linked to a Microsoft Purview ingestion storage.

## Can I scan a data source through a public endpoint if a private endpoint is enabled on my Microsoft Purview account?

Yes. Data sources that aren't connected through a private endpoint can be scanned by using a public endpoint while Microsoft Purview is configured to use a private endpoint.

## Can I scan a data source through a service endpoint if a private endpoint is enabled?

Yes. Data sources that aren't connected through a private endpoint can be scanned by using a service endpoint while Microsoft Purview is configured to use a private endpoint. Learn more from [Choose the right integration runtime configuration for your scenario](data-map-integration-runtime-choose).

## Can I access the classic Microsoft Purview governance portal from a public network if Public network access is set to Deny in Microsoft Purview account networking?

No. Connecting to Microsoft Purview from a public endpoint where **Public network access** is set to **Deny** results in the following error message:

"Not authorized to access this Microsoft Purview account. This Microsoft Purview account is behind a private endpoint. Access the account from a client in the same virtual network (virtual network) that has been configured for the Microsoft Purview account's private endpoint."

In this case, to open the classic Microsoft Purview governance portal, either use a machine that's deployed in the same virtual network as the Microsoft Purview portal private endpoint or use a VM that's connected to your CorpNet in which hybrid connectivity is allowed.

## Is it possible to restrict access to the Microsoft Purview managed storage account or ingestion storage account and Event Hubs namespace (for private endpoint ingestion only) but keep portal access enabled for users across the web?

Note

Your account only has a managed storage account if it was created before December 15, 2023 (or deployed using API version previous to 2023-05-01-preview). Your account only has an associated Event Hubs namespace if it is [configured for kafka notifications](data-map-kafa-notifications) or was created before December 15, 2022.

Yes. You can configure Microsoft Purview firewall setting to Disabled for ingestion only (Preview). By choosing this option, public network access to your Microsoft Purview account through API and classic Microsoft Purview governance portal is allowed, however public network access is set to disabled on your Microsoft Purview account's Managed storage account. You also need to confirm your [Event Hubs network settings](data-map-kafa-notifications#event-hubs-networking) allow communication.

## If public network access is set to Allow, does it mean the managed storage account or ingestion storage account and Event Hubs namespace are accessible by anyone?

Note

Your account only has a managed storage account if it was created before December 15, 2023 (or deployed using API version previous to 2023-05-01-preview). Your account only has an associated Event Hubs namespace if it is [configured for kafka notifications](data-map-kafa-notifications) or was created before December 15, 2022.

No. As protected resources, access to the Microsoft Purview managed storage account and any Event Hubs namespace is restricted to Microsoft Purview only using RBAC authentication schemes. These resources are deployed with a deny assignment to all principals, which prevents any applications, users, or groups from gaining access to them.

To read more about Azure deny assignment, see [Understand Azure deny assignments](/en-us/azure/role-based-access-control/deny-assignments).

## What private DNS zones are required for Microsoft Purview for a private endpoint?

For Microsoft Purview *account*, *portal*, and *platform* private endpoints:

- `privatelink.purview.azure.com` - for the classic Microsoft Purview governance portal.
- `privatelink.purview-service.microsoft.com` - for the Microsoft Purview portal.

For Microsoft Purview *ingestion* private endpoints:

- `privatelink.blob.core.windows.net`
- `privatelink.queue.core.windows.net`
- `privatelink.servicebus.windows.net`

## Do I have to use a dedicated virtual network and dedicated subnet when I deploy Microsoft Purview private endpoints?

No. However, `PrivateEndpointNetworkPolicies` must be disabled in the destination subnet before you deploy the private endpoints. Consider deploying Microsoft Purview into a virtual network that has network connectivity to data source virtual networks through virtual network Peering and access to an on-premises network if you plan to scan data sources cross-premises.

Read more about [Disable network policies for private endpoints](/en-us/azure/private-link/disable-private-endpoint-network-policy).

## Can I deploy Microsoft Purview private endpoints and use existing private DNS zones in my subscription to register the A records?

Yes. Your private endpoint DNS zones can be centralized in a hub or data management subscription for all internal DNS zones required for Microsoft Purview and all data source records. We recommend this method to allow Microsoft Purview to resolve data sources by using their private endpoint internal IP addresses.

You're also required to set up a [virtual network link](/en-us/azure/dns/private-dns-virtual-network-links) for virtual networks for the existing private DNS zone.

## What are the outbound ports and firewall requirements for virtual machines with self-hosted integration runtime for Microsoft Purview when you use a private endpoint?

The VMs in which self-hosted integration runtime is deployed must have outbound access to Azure endpoints and a Microsoft Purview private IP address through port 443.

## Do I need to enable outbound internet access from the virtual machine running self-hosted integration runtime if a private endpoint is enabled?

No. However, it's expected that the virtual machine running self-hosted integration runtime can connect to your instance of Microsoft Purview through an internal IP address by using port 443. Use common troubleshooting tools for name resolution and connectivity testing, such as nslookup.exe and Test-NetConnection.

## Do I still need to deploy private endpoints for my Microsoft Purview account if I'm using Managed virtual network?

At least one account and portal private endpoints are required, if public access in Microsoft Purview account is set to **deny**. At least one account, portal and ingestion private endpoint are required, if public access in Microsoft Purview account is set to **deny** and you're planning to scan more data sources using a self-hosted integration runtime.

## What inbound and outbound communications are allowed through public endpoint for Microsoft Purview Managed VNets?

No inbound communication is allowed into a Managed virtual network from public network. All ports are opened for outbound communications. In Microsoft Purview, a Managed virtual network can be used to privately connect to Azure data sources to extract metadata during scan.

## Why do I receive the following error message when I try to launch the classic Microsoft Purview governance portal from my machine?

"This Microsoft Purview account is behind a private endpoint. Access the account from a client in the same virtual network (virtual network) that has been configured for the Microsoft Purview account's private endpoint."

It's likely your Microsoft Purview account is deployed by using Private Link and public access is disabled on your Microsoft Purview account. As a result, you have to browse the clssic Microsoft Purview governance portal from a virtual machine that has internal network connectivity to Microsoft Purview.

If you're connecting from a VM behind a hybrid network or using a jump machine connected to your virtual network, use common troubleshooting tools for name resolution and connectivity testing, such as nslookup.exe and Test-NetConnection.

1. Validate if you can resolve the following addresses through your Microsoft Purview account's private IP addresses.

    - `Web.Purview.Azure.com`
    - `<YourPurviewAccountName>.Purview.Azure.com`
2. Verify network connectivity to your Microsoft Purview account by using the following PowerShell command:

    ```powershell
    Test-NetConnection -ComputerName <YourPurviewAccountName>.Purview.Azure.com -Port 443
    ```
3. Verify your cross-premises DNS configuration if you use your own DNS resolution infrastructure.

For more information about DNS settings for private endpoints, see [Azure private endpoint DNS configuration](/en-us/azure/private-link/private-endpoint-dns).

## Can I move private endpoints associated with Microsoft Purview account or its managed resources to another Azure subscription or resource group?

No. Move operations for Account, Portal, or Ingestion private endpoints aren't supported. For more information, see [Move networking resources to new resource group or subscription](/en-us/azure/azure-resource-manager/management/move-limitations/networking-move-limitations#private-endpoints).

## Can I create multiple managed virtual networks in different regions?

Yes. You can create multiple managed virtual networks across different regions in a single Microsoft Purview instance so you can access data sources available in different regions. This feature provides the ability to:

- Create multiple managed virtual networks (five maximum) across different regions within a single Microsoft Purview instance.
- Network isolation within your own organization to address potential data residency or scan performance concerns.