---
layout: Conceptual
title: Configure DNS Name Resolution for private endpoints for classic Microsoft Purview data governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-private-link-name-resolution
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
description: This article describes an overview of how you can use a private end point for your Microsoft Purview account when using classic data governance.
locale: en-us
document_id: 5b60349d-6b21-e136-1ed2-f14126bbf13e
document_version_independent_id: 5b60349d-6b21-e136-1ed2-f14126bbf13e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-private-link-name-resolution.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-private-link-name-resolution
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-private-link-name-resolution.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 057c1134-e194-4d2e-9e64-70c64aad0ae4
---

# Configure DNS Name Resolution for private endpoints for classic Microsoft Purview data governance | Microsoft Learn

Important

This article covers private endpoints for the classic Microsoft Purview governance portal (https://web.purview.azure.com). If you're using the new Microsoft Purview portal (https://purview.microsoft.com/), follow the [documentation for private endpoints in the Microsoft Purview portal](data-governance-private-endpoints).

## Conceptual overview

Accurate name resolution is a critical requirement when setting up private endpoints for your Microsoft Purview accounts.

You might need to enable internal name resolution in your DNS settings to resolve the private endpoint IP addresses to the fully qualified domain name (FQDN) from data sources and your management machine to Microsoft Purview account and self-hosted integration runtime, depending on scenarios that you're deploying.

Tip

When you deploy your DNS Zones, don't use specific IP addresses. IP addresses for Azure resources are not static, and building your DNS Zones with static IP addresses will eventually cause errors.

## Deployment options

Use any of the following options to set up internal name resolution when using private endpoints for your Microsoft Purview account:

- Deploy new Azure Private DNS Zones in your Azure environment part of private endpoint deployment. (Default option)
- Use existing Azure Private DNS Zones. Use this option if you're using a private endpoint in a hub-and-spoke model from a different subscription or even within the same subscription.
- Use your own DNS Servers if you don't use DNS forwarders and instead you manage A records directly in your on-premises DNS servers.

Tip

- Classic Microsoft Purview governance portal (https://web.purview.azure.com): *account*, *portal*, and *ingestion* private endpoints are supported.
- New Microsoft Purview portal (https://purview.microsoft.com/): *platform* and *ingestion* private endpoints are supported.

## Option 1 - Deploy new Azure Private DNS Zones

### Deploy new Azure Private DNS Zones

To enable internal name resolution, you can deploy the required Azure DNS Zones inside your Azure subscription where Microsoft Purview account is deployed.

![Screenshot that shows DNS Zones.](media/catalog-private-link/purview-pe-dns-zones.png)

When you create ingestion, portal and account private endpoints, the DNS CNAME resource records for Microsoft Purview is automatically updated to an alias in few subdomains with the prefix `privatelink`:

- By default, during the deployment of *account* or *platform* private endpoints for your Microsoft Purview account, we also create a [private DNS zone](/en-us/azure/dns/private-dns-overview) that corresponds to the `privatelink` subdomain for Microsoft Purview as `privatelink.purview.azure.com` for the classic Microsoft Purview governance portal and `privatelink.purview-service.microsoft.com` for the Microsoft Purview portal, including DNS A resource records for the private endpoints.
- During the deployment of *portal* private endpoint for your Microsoft Purview account, we also create a new private DNS zone that corresponds to the `privatelink` subdomain for Microsoft Purview as `privatelink.purviewstudio.azure.com` including DNS A resource records for *Web*.
- If you enable ingestion private endpoints, other DNS zones are required for managed or configured resources.

The following table shows an example of Azure Private DNS zones and DNS A Records that are deployed as part of configuration of private endpoint for a Microsoft Purview account if you enable *Private DNS integration* during the deployment:

| Private endpoint | Private endpoint associated to | Portal availability | DNS Zone (new) | A Record (example) |
| --- | --- | --- | --- | --- |
| Account | Microsoft Purview | `privatelink.purview.azure.com` | Contoso-Purview |  |
| Platform | Microsoft Purview | `privatelink.purview-service.microsoft.com` | Contoso-Purview |  |
| Portal | Microsoft Purview | `privatelink.purviewstudio.azure.com` | Web |  |
| Platform | Microsoft Purview | `privatelink.purview-service.microsoft.com` | Web |  |
| Ingestion | Microsoft Purview ingestion - Blob\* | `privatelink.blob.core.windows.net` | ingestioneus2eastusksqky |  |
| Ingestion | Microsoft Purview ingestion - Blob\* | `privatelink.blob.storage.azure.net` | ingestioneus2eastusksqky |  |
| Ingestion | Microsoft Purview ingestion - Queue\* | `privatelink.queue.core.windows.net` | ingestioneus2eastusksqky |  |
| Ingestion | Microsoft Purview ingestion - Queue\* | `privatelink.queue.storage.azure.net` | ingestioneus2eastusksqky |  |
| Ingestion | Microsoft Purview configured Event Hubs - Event Hubs\*\* | `privatelink.servicebus.windows.net` | atlas-12345678-1234-1234-abcd-123456789abc |  |

Note

\*If your account was created before December 15, 2023, the endpoint is deployed to your managed storage account. If it was created after November 10 (or deployed using API version 2023-05-01-preview onwards), it points to the ingestion storage.

\*\*Your account only has an associated Event Hubs namespace if it is [configured for kafka notifications](data-map-kafa-notifications) or created before December 15, 2022.

### Validate virtual network links on Azure Private DNS Zones

Once the private endpoint deployment is completed, make sure there's a [Virtual network link](/en-us/azure/dns/private-dns-virtual-network-links) on all corresponding Azure Private DNS zones to Azure virtual network where private endpoint was deployed.

![Screenshot that shows virtual network links on DNS Zone.](media/catalog-private-link/purview-name-resolution-link.png)

For more information, see [Azure private endpoint DNS configuration](/en-us/azure/private-link/private-endpoint-dns).

### Verify internal name resolution

When you resolve the Microsoft Purview endpoint URL from outside the virtual network with the private endpoint, it resolves to the public endpoint of Microsoft Purview. When resolved from the virtual network hosting the private endpoint, the Microsoft Purview endpoint URL resolves to the private endpoint's IP address.

As an example, if a Microsoft Purview account name is 'Contoso-Purview', when it's resolved from outside the virtual network that hosts the private endpoint, it will be:

| Name | Type | Value |
| --- | --- | --- |
| `Contoso-Purview.purview.azure.com` | CNAME | `Contoso-Purview.privatelink.purview.azure.com` |
| `Contoso-Purview.privatelink.purview.azure.com` | CNAME | &lt;Microsoft Purview public endpoint&gt; |
| &lt;Microsoft Purview public endpoint&gt; | A | &lt;Microsoft Purview public IP address&gt; |
| `Web.purview.azure.com` | CNAME | &lt;Microsoft Purview governance portal public endpoint&gt; |

The DNS resource records for Contoso-Purview, when resolved in the virtual network hosting the private endpoint, will be:

| Name | Type | Value |
| --- | --- | --- |
| `Contoso-Purview.purview.azure.com` | CNAME | `Contoso-Purview.privatelink.purview.azure.com` |
| `Contoso-Purview.privatelink.purview.azure.com` | A | &lt;Microsoft Purview account private endpoint IP address&gt; |
| `Web.purview.azure.com` | CNAME | &lt;Microsoft Purview portal private endpoint IP address&gt; |

## Option 2 - Use existing Azure Private DNS Zones

### Use existing Azure Private DNS Zones

During the deployment of Microsoft Purview private endpoints, you can choose *Private DNS integration* using existing Azure Private DNS zones. This is common case for organizations where private endpoint is used for other services in Azure. In this case, during the deployment of private endpoints, make sure you select the existing DNS zones instead of creating new ones.

This scenario also applies if your organization uses a central or hub subscription for all Azure Private DNS Zones.

The following list shows the required Azure DNS zones and A records for Microsoft Purview private endpoints:

Important

Update all names with `Contoso-Purview`,`ingestioneus2eastusksqky` and `atlas-12345678-1234-1234-abcd-123456789abc` with corresponding Azure resources name in your environment.

- `Contoso-Purview` is the name of your Microsoft Purview account.
- You only need the endpoints associated with the portal you're using:
    - Classic Microsoft Purview governance portal (https://web.purview.azure.com): *account*, *portal*, and *ingestion* private endpoints are supported.
    - New Microsoft Purview portal (https://purview.microsoft.com/): *platform* and *ingestion* private endpoints are supported.
- If your account is [configured for kafka notifications](data-map-kafa-notifications) or was created before December 15, 2022, `atlas-12345678-1234-1234-abcd-123456789abc` is your Event Hubs namespace.
- If your account was created **before** December 15, 2023, for `ingestioneus2eastusksqky` use the name of your Microsoft Purview managed storage account.
- If your account was created **after** December 15, 2023 (or deployed using API version 2023-05-01-preview onwards), leave `ingestioneus2eastusksqky` as is.

| Private endpoint | Private endpoint associated to | Portal availability | DNS Zone (existing) | A Record (example) |
| --- | --- | --- | --- | --- |
| Account | Microsoft Purview | `privatelink.purview.azure.com` | Contoso-Purview |  |
| Platform | Microsoft Purview | `privatelink.purview-service.microsoft.com` | Contoso-Purview |  |
| Portal | Microsoft Purview | `privatelink.purviewstudio.azure.com` | Web |  |
| Ingestion | Microsoft Purview ingestion - Blob\* | `privatelink.blob.core.windows.net` | ingestioneus2eastusksqky |  |
| Ingestion | Microsoft Purview ingestion - Blob\* | `privatelink.blob.storage.azure.net` | ingestioneus2eastusksqky |  |
| Ingestion | Microsoft Purview ingestion - Queue\* | `privatelink.queue.core.windows.net` | ingestioneus2eastusksqky |  |
| Ingestion | Microsoft Purview ingestion - Queue\* | `privatelink.queue.storage.azure.net` | ingestioneus2eastusksqky |  |
| Ingestion | Microsoft Purview configured Event Hubs\*\* | `privatelink.servicebus.windows.net` | atlas-12345678-1234-1234-abcd-123456789abc |  |

[![Diagram that shows Microsoft Purview name resolution](media/catalog-private-link/purview-name-resolution-diagram.png)](media/catalog-private-link/purview-name-resolution-diagram.png#lightbox)

Note

\*If your account was created before December 15, 2023, the endpoint is deployed to your managed storage account. If it was created after November 10 (or deployed using API version 2023-05-01-preview onwards), it points to the ingestion storage. \*\*Your account only has an associated Event Hubs namespace if it is [configured for kafka notifications](data-map-kafa-notifications) or created before December 15, 2022.

For more information, see [Virtual network workloads without custom DNS server](/en-us/azure/private-link/private-endpoint-dns#virtual-network-workloads-without-custom-dns-server) and [On-premises workloads using a DNS forwarder](/en-us/azure/private-link/private-endpoint-dns#on-premises-workloads-using-a-dns-forwarder) scenarios in [Azure Private Endpoint DNS configuration](/en-us/azure/private-link/private-endpoint-dns).

### Verify virtual network links on Azure Private DNS Zones

Once the private endpoint deployment is completed, make sure there's a [Virtual network link](/en-us/azure/dns/private-dns-virtual-network-links) on all corresponding Azure Private DNS zones to Azure virtual network where private endpoint was deployed.

![Screenshot that shows virtual network links on DNS Zone.](media/catalog-private-link/purview-name-resolution-link.png)

For more information, see [Azure private endpoint DNS configuration](/en-us/azure/private-link/private-endpoint-dns).

### Configure DNS Forwarders if custom DNS is used

Additionally it's required to validate your DNS configurations on Azure virtual network where self-hosted integration runtime VM or management PC is located.

![Diagram that shows Azure virtual network custom DNS](media/catalog-private-link/purview-pe-custom-dns.png)

- If it's configured to *Default*, no further action is required in this step.
- If custom DNS server is used, you should add corresponding DNS forwarders inside your DNS servers for the following zones:

    - Purview.azure.com
    - purviewstudio.azure.com
    - Blob.core.windows.net
    - Queue.core.windows.net
    - Blob.storage.azure.net
    - Queue.storage.azure.net
    - Servicebus.windows.net

### Verify internal name resolution

When you resolve the Microsoft Purview endpoint URL from outside the virtual network with the private endpoint, it resolves to the public endpoint of Microsoft Purview. When resolved from the virtual network hosting the private endpoint, the Microsoft Purview endpoint URL resolves to the private endpoint's IP address.

As an example, if a Microsoft Purview account name is 'Contoso-Purview', when it's resolved from outside the virtual network that hosts the private endpoint, it will be:

| Name | Type | Value |
| --- | --- | --- |
| `Contoso-Purview.purview.azure.com` | CNAME | `Contoso-Purview.privatelink.purview.azure.com` |
| `Contoso-Purview.privatelink.purview.azure.com` | CNAME | &lt;Microsoft Purview public endpoint&gt; |
| &lt;Microsoft Purview public endpoint&gt; | A | &lt;Microsoft Purview public IP address&gt; |
| `Web.purview.azure.com` | CNAME | &lt;Microsoft Purview governance portal public endpoint&gt; |

The DNS resource records for Contoso-Purview, when resolved in the virtual network hosting the private endpoint, will be:

| Name | Type | Value |
| --- | --- | --- |
| `Contoso-Purview.purview.azure.com` | CNAME | `Contoso-Purview.privatelink.purview.azure.com` |
| `Contoso-Purview.privatelink.purview.azure.com` | A | &lt;Microsoft Purview account private endpoint IP address&gt; |
| `Web.purview.azure.com` | CNAME | &lt;Microsoft Purview portal private endpoint IP address&gt; |

## Option 3 - Use your own DNS Servers

If you don't use DNS forwarders and instead you manage A records directly in your on-premises DNS servers to resolve the endpoints through their private IP addresses, you might need to create the following A records in your DNS servers.

Important

Update all names with `Contoso-Purview`,`ingestioneus2eastusksqky` and `atlas-12345678-1234-1234-abcd-123456789abc` with corresponding Azure resources name in your environment.

- `Contoso-Purview` is the name of your Microsoft Purview account.
- You only need the endpoints associated with the portal you're using:
    - Classic Microsoft Purview governance portal (https://web.purview.azure.com): *account*, *portal*, and *ingestion* private endpoints are supported.
    - New Microsoft Purview portal (https://purview.microsoft.com/): *platform* and *ingestion* private endpoints are supported.
- If your account is [configured for kafka notifications](data-map-kafa-notifications) or was created before December 15, 2022, `atlas-12345678-1234-1234-abcd-123456789abc` is your Event Hubs namespace.
- If your account was created **before** December 15, 2023, for `ingestioneus2eastusksqky` use the name of your Microsoft Purview managed storage account.
- If your account was created **after** December 15, 2023 (or deployed using API version 2023-05-01-preview onwards), leave `ingestioneus2eastusksqky` as is.

| Name | Type | Value | Portal availability |
| --- | --- | --- | --- |
| `web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `ingestioneus2eastusksqky.blob.core.windows.net`, `ingestioneus2eastusksqky.blob.storage.azure.net` | A | &lt;blob-ingestion private endpoint IP address of Microsoft Purview&gt; | Classic and new portals |
| `ingestioneus2eastusksqky.queue.core.windows.net`, `ingestioneus2eastusksqky.queue.storage.azure.net` | A | &lt;queue-ingestion private endpoint IP address of Microsoft Purview&gt; | Classic and new portals |
| `atlas-12345678-1234-1234-abcd-123456789abc.servicebus.windows.net` | A | &lt;namespace-ingestion private endpoint IP address of Microsoft Purview&gt; | Classic and new portals |
| `Contoso-Purview.Purview.azure.com` | A | &lt;account/platform private endpoint IP address of Microsoft Purview&gt; | Classic and new portals |
| `Contoso-Purview.scan.Purview.azure.com` | A | &lt;account/platform private endpoint IP address of Microsoft Purview&gt; | Classic and new portals |
| `Contoso-Purview.catalog.Purview.azure.com` | A | &lt;account/platform private endpoint IP address of Microsoft Purview&gt; | Classic and new portals |
| `Contoso-Purview.proxy.purview.azure.com` | A | &lt;account/platform private endpoint IP address of Microsoft Purview&gt; | Classic and new portals |
| `Contoso-Purview.guardian.purview.azure.com` | A | &lt;account/platform private endpoint IP address of Microsoft Purview&gt; | Classic and new portals |
| `gateway.purview.azure.com` | A | &lt;account/platform private endpoint IP address of Microsoft Purview&gt; | Classic and new portals |
| `insight.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `manifest.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `cdn.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `hub.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `catalog.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `cseo.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `datascan.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `datashare.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `datasource.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `policy.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `sensitivity.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `web.privatelink.purviewstudio.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |
| `workflow.prod.ext.web.purview.azure.com` | A | &lt;portal private endpoint IP address of Microsoft Purview&gt; | Classic portal |

## Verify and DNS test name resolution and connectivity

1. If you're using Azure Private DNS Zones, make sure the following DNS Zones and the corresponding A records are created in your Azure Subscription:

    | Private endpoint | Private endpoint associated to | Portal availability | DNS Zone (existing) | A Record (example) |
    | --- | --- | --- | --- | --- |
    | Account | Microsoft Purview | Classic portal | `privatelink.purview.azure.com` | Contoso-Purview |
    | Platform | Microsoft Purview | New portal | `privatelink.purview-service.microsoft.com` | Contoso-Purview |
    | Portal | Microsoft Purview | Classic portal | `privatelink.purviewstudio.azure.com` | Web |
    | Ingestion | Microsoft Purview ingestion - Blob\* | Classic and new portals | `privatelink.blob.core.windows.net`,`privatelink.blob.storage.azure.net` | ingestioneus2eastusksqky |
    | Ingestion | Microsoft Purview ingestion - Queue\* | Classic and new portals | `privatelink.queue.core.windows.net`,`privatelink.queue.storage.azure.net` | ingestioneus2eastusksqky |
    | Ingestion | Event Hubs\*\* | Classic and new portals | `privatelink.servicebus.windows.net` | atlas-12345678-1234-1234-abcd-123456789abc |

    Note

    \*If your account was created before December 15, 2023, the endpoint is deployed to your managed storage account. If it was created after November 10 (or deployed using API version 2023-05-01-preview onwards), it points to the ingestion storage. \*\*Your account only has an associated Event Hubs namespace if it is [configured for kafka notifications](data-map-kafa-notifications) or created before December 15, 2022.
2. Create [Virtual network links](/en-us/azure/dns/private-dns-virtual-network-links) in your Azure Private DNS Zones for your Azure Virtual Networks to allow internal name resolution.
3. From your management PC and self-hosted integration runtime VM, test name resolution and network connectivity to your Microsoft Purview account using tools such as Nslookup.exe and PowerShell

To test name resolution you need to resolve the following FQDNs through their private IP addresses: (Instead of Contoso-Purview, ingestioneus2eastusksqky or atlas-12345678-1234-1234-abcd-123456789abc, use the hostname associated with your purview account name and managed or configured resources names)

- `Contoso-Purview.purview.azure.com`
- `web.purview.azure.com`
- `ingestioneus2eastusksqky.blob.core.windows.net`
- `ingestioneus2eastusksqky.queue.core.windows.net`
- `atlas-12345678-1234-1234-abcd-123456789abc.servicebus.windows.net`

To test network connectivity, from self-hosted integration runtime VM you can launch PowerShell console and test connectivity using `Test-NetConnection`. You must resolve each endpoint by their private endpoint and obtain TcpTestSucceeded as True. (Instead of Contoso-Purview, ingestioneus2eastusksqky or atlas-12345678-1234-1234-abcd-123456789abc, use the hostname associated with your purview account name and managed or configured resources names)

- `Test-NetConnection -ComputerName Contoso-Purview.purview.azure.com -port 443`
- `Test-NetConnection -ComputerName web.purview.azure.com -port 443`
- `Test-NetConnection -ComputerName ingestioneus2eastusksqky.blob.core.windows.net -port 443`
- `Test-NetConnection -ComputerName ingestioneus2eastusksqky.queue.core.windows.net -port 443`
- `Test-NetConnection -ComputerName atlas-12345678-1234-1234-abcd-123456789abc.servicebus.windows.net -port 443`

The following example shows Microsoft Purview DNS name resolution from outside the virtual network or when an Azure private endpoint isn't configured.

![Screenshot that shows Microsoft Purview name resolution from outside CorpNet.](media/catalog-private-link/purview-name-resolution-external.png)

The following example shows Microsoft Purview DNS name resolution from inside the virtual network.

![Screenshot that shows Microsoft Purview name resolution from inside CorpNet.](media/catalog-private-link/purview-name-resolution-private-link.png)

Note

The values in these images are examples. Use the information in the article to correctly configure your DNS Zones.