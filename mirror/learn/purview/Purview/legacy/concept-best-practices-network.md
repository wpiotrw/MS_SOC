---
layout: Conceptual
title: Microsoft Purview network architecture and best practices | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-best-practices-network
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article provides examples of Microsoft Purview network architecture options and describes best practices.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: zeinam
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: best-practice
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: fasttrack-edit, msecd-doc-authoring-1030
locale: en-us
document_id: d813f56d-0dd0-b4d8-7811-5357a8b47f88
document_version_independent_id: d813f56d-0dd0-b4d8-7811-5357a8b47f88
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-best-practices-network.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-best-practices-network
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-best-practices-network.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 884229b4-a53f-f80a-f013-1aeec2d8b099
---

# Microsoft Purview network architecture and best practices | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Microsoft Purview governance solutions are a platform as a service (PaaS) solutions for data governance. Microsoft Purview accounts have public endpoints that are accessible through the internet to connect to the service. However, all endpoints are secured through Microsoft Entra logins and role-based access control (RBAC).

Note

These best practices cover the network architecture for [Microsoft Purview unified governance solutions](/en-us/purview/purview#microsoft-purview-unified-data-governance-solutions). For more information about Microsoft Purview risk and compliance solutions, [go here](../purview-compliance). For more information about Microsoft Purview in general, [go here](/en-us/purview/purview).

For an added layer of security, you can create private endpoints for your Microsoft Purview account. You'll get a private IP address from your virtual network in Azure to the Microsoft Purview account and its managed resources. This address will restrict all traffic between your virtual network and the Microsoft Purview account to a private link for user interaction with the APIs and Microsoft Purview governance portal, or for scanning and ingestion.

Currently, the Microsoft Purview firewall provides access control for the public endpoint of your purview account. You can use the firewall to allow all access or to block all access through the public endpoint when using private endpoints. For more information see, [Microsoft Purview firewall options](../data-gov-classic-firewall)

Based on your network, connectivity, and security requirements, you can set up and maintain Microsoft Purview accounts to access underlying services or ingestion. Use this best practices guide to define and prepare your network environment so you can access Microsoft Purview and scan data sources from your network or cloud.

This guide covers the following network options:

- Use Azure public endpoints.
- Use private endpoints.
- Use private endpoints and allow public access on the same Microsoft Purview account.
- Use Azure public endpoints to access Microsoft Purview governance portal and private endpoints for ingestion.

This guide describes a few of the most common network architecture scenarios for Microsoft Purview. Though you're not limited to those scenarios, keep in mind the limitations of the service when you're planning networking for your Microsoft Purview accounts.

## Prerequisites

To understand which network option is best for your environment, we suggest that you perform the following actions first:

- Review your network topology and security requirements before registering and scanning any data sources in Microsoft Purview. For more information, see: [Define an Azure network topology](/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/define-an-azure-network-topology).
- Define your [network connectivity model for PaaS services](/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/connectivity-to-azure-paas-services).

## Option 1: Use public endpoints

By default, you can use Microsoft Purview accounts through the public endpoints accessible over the internet. Allow public networks in your Microsoft Purview account if you have the following requirements:

- No private connectivity is required when scanning or connecting to Microsoft Purview endpoints.
- All data sources are software-as-a-service (SaaS) applications only.
- All data sources have a public endpoint that's accessible through the internet.
- Business users require access to a Microsoft Purview account and the Microsoft Purview governance portal through the internet.

### Integration runtime options

To scan data sources while the Microsoft Purview account firewall is set to allow public access, you can use all the integration runtime types - the Azure integration runtime, [Managed VNet integration runtime](../data-governance-private-endpoints-managed-virtual-network), and a [self-hosted integration runtime](../data-map-integration-runtime-self-hosted). Learn more from [Choose the right integration runtime configuration for your scenario](../data-map-integration-runtime-choose).

Here are some best practices:

- Whenever applicable, we recommend that you use the Azure integration runtime or Managed VNet integration runtime to scan data sources, to reduce cost and administrative overhead.
- The following steps show the communication flow at a high level when you're using the Azure integration runtime to scan a data source:

    [![Screenshot that shows the connection flow between Microsoft Purview, the Azure runtime, and data sources.](../media/concept-best-practices/network-azure-runtime.png)](../media/concept-best-practices/network-azure-runtime.png#lightbox)

    Note

    This graphic only applies to Microsoft Purview accounts created after December 15, 2023 (or deployed using API version 2023-05-01-preview onwards).

    1. A manual or automatic scan is initiated from the Microsoft Purview Data Map through the Azure integration runtime.
    2. The Azure integration runtime connects to the data source to extract metadata.
    3. Metadata is queued in the Microsoft Purview ingestion storage account and stored in Azure Blob Storage temporarily.
    4. Metadata is sent to the Microsoft Purview Data Map.
- Scanning on-premises and VM-based data sources always requires using a self-hosted integration runtime. The Azure integration runtime isn't supported for these data sources. The following steps show the communication flow at a high level when you're using a self-hosted integration runtime to scan a data source. The first diagram shows a scenario where resources are within Azure or on a VM in Azure. The second diagram shows a scenario with on-premises resources. The steps between the two are the same from Microsoft Purview's perspective:

    [![Screenshot that shows the connection flow between Microsoft Purview, a self-hosted runtime, and data sources.](../media/concept-best-practices/network-self-hosted-runtime.png)](../media/concept-best-practices/network-self-hosted-runtime.png#lightbox)

    [![Screenshot that shows the connection flow between Microsoft Purview, an on-premises self-hosted runtime, and data sources in on-premises network.](../media/concept-best-practices/security-self-hosted-runtime-on-premises.png)](../media/concept-best-practices/security-self-hosted-runtime-on-premises.png#lightbox)

    1. A manual or automatic scan is triggered. Microsoft Purview connects to Azure Key Vault to retrieve the credential to access a data source.
    2. The scan is initiated from the Microsoft Purview Data Map through a self-hosted integration runtime.
    3. The self-hosted integration runtime service from the VM or on-premises machine connects to the data source to extract metadata.
    4. Metadata is processed in the machine's memory for the self-hosted integration runtime. Metadata is queued in Microsoft Purview ingestion storage and then stored in Azure Blob Storage temporarily. Actual data never leaves the boundary of your network.
    5. Metadata is sent to the Microsoft Purview Data Map.

### Authentication options

When you're scanning a data source in Microsoft Purview, you need to provide a credential. Microsoft Purview can then read the metadata of the assets from the data source by using the integration runtime. Refer to each [data source article](../data-map-data-sources) for details about the supported authentication types and the needed permissions. Authentication options and requirements vary based on the following factors:

- **Data source type**. For example, if the data source is Azure SQL Database, you need to use a login with db\_datareader access to each database. This can be a user-assigned managed identity or a Microsoft Purview managed identity. Or it can be a service principal in Microsoft Entra ID added to SQL Database as db\_datareader.

    If the data source is Azure Blob Storage, you can use a Microsoft Purview managed identity, or a service principal in Microsoft Entra ID added as a Blob Storage Data Reader role on the Azure storage account. Or use the storage account's key.
- **Authentication type**. We recommend that you use a Microsoft Purview managed identity to scan Azure data sources when possible, to reduce administrative overhead. For any other authentication types, you need to [set up credentials for source authentication inside Microsoft Purview](../data-map-data-scan-credentials):

    1. Generate a secret inside an Azure key vault.
    2. Register the key vault inside Microsoft Purview.
    3. Inside Microsoft Purview, create a new credential by using the secret saved in the key vault.
- **Runtime type that's used in the scan**. Currently, you can't use a Microsoft Purview managed identity with a self-hosted integration runtime.

### Other considerations

- If you choose to scan data sources using public endpoints, your self-hosted integration runtime VMs must have outbound access to data sources and Azure endpoints.
- Your self-hosted integration runtime VMs must have [outbound connectivity to Azure endpoints](../data-map-integration-runtime-self-hosted#networking-requirements).

## Option 2: Use private endpoints

Similar to other PaaS solutions, Microsoft Purview doesn't support deploying directly into a virtual network. So you can't use certain networking features with the offering's resources, such as network security groups, route tables, or other network-dependent appliances such as Azure Firewall. Instead, you can use private endpoints that can be enabled on your virtual network. You can then disable public internet access to securely connect to Microsoft Purview.

You must use private endpoints for your Microsoft Purview account if you have any of the following requirements:

- You need to have end-to-end network isolation for Microsoft Purview accounts and data sources.
- You need to [block public access](../data-gov-classic-private-link-end-to-end#firewalls-to-restrict-public-access) to your Microsoft Purview accounts.
- Your platform-as-a-service (PaaS) data sources are deployed with private endpoints, and you've blocked all access through the public endpoint.
- Your on-premises or infrastructure-as-a-service (IaaS) data sources can't reach public endpoints.

### Design considerations

- To connect to your Microsoft Purview account privately and securely, you need to deploy an account and a portal private endpoint. For example, this deployment is necessary if you intend to connect to Microsoft Purview through the API or use the Microsoft Purview governance portal.
- If you need to connect to the Microsoft Purview governance portal by using private endpoints, you have to deploy both account and portal private endpoints.
- To scan data sources through private connectivity, you need to configure at least one account and one ingestion private endpoint for Microsoft Purview.
- Review [DNS requirements](../data-gov-classic-private-link-name-resolution#deployment-options). If you're using a custom DNS server on your network, clients must be able to resolve the fully qualified domain name (FQDN) for the Microsoft Purview account endpoints to the private endpoint's IP address.

### Integration runtime options

To scan data sources through private connectivity, you can use [Managed VNet integration runtime](../data-governance-private-endpoints-managed-virtual-network) or [self-hosted integration runtime](../data-map-integration-runtime-self-hosted). Learn more from [Choose the right integration runtime configuration for your scenario](../data-map-integration-runtime-choose).

- Whenever applicable, we recommend that you use the Managed VNet integration runtime to scan data sources, to reduce cost and administrative overhead.
- If using self-hosted integration runtime, you need to set up and use a self-hosted integration runtime on a Windows virtual machine that's deployed inside the same or a peered virtual network where Microsoft Purview ingestion private endpoints are deployed.
- To scan on-premises data sources, you can also install a self-hosted integration runtime either on an on-premises Windows machine or on a VM inside an Azure virtual network.
- When you're using private endpoints with Microsoft Purview, you need to allow network connectivity from data sources to the self-hosted integration VM on the Azure virtual network where Microsoft Purview private endpoints are deployed.
- We recommend allowing automatic upgrade of the self-hosted integration runtime. Make sure you open required outbound rules in your Azure virtual network or on your corporate firewall to allow automatic upgrade. For more information, see [Self-hosted integration runtime networking requirements](../data-map-integration-runtime-self-hosted#networking-requirements).

### Authentication options

- Make sure that your credentials are stored in an Azure key vault and registered inside Microsoft Purview.
- You must create a credential in Microsoft Purview based on each secret that you create in the Azure key vault. You need to assign, at minimum, *get* and *list* access for secrets for Microsoft Purview on the Key Vault resource in Azure. Otherwise, the credentials won't work in the Microsoft Purview account.

### Current limitations

- Scanning multiple Azure sources by using the entire subscription or resource group through ingestion private endpoints and a self-hosted integration runtime or Managed VNet integration runtime isn't supported when you're using private endpoints for ingestion. Instead, you can register and scan data sources individually.
- For limitations related to Microsoft Purview private endpoints, see [Known limitations](../data-gov-classic-private-link-troubleshoot#known-limitations).
- For limitations related to the Private Link service, see [Azure Private Link limits](/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#private-link-limits).

### Private endpoint scenarios

#### Single virtual network, single region

In this scenario, all Azure data sources, self-hosted integration runtime VMs, and Microsoft Purview private endpoints are deployed in the same virtual network in an Azure subscription.

If on-premises data sources exist, connectivity is provided through a site-to-site VPN or Azure ExpressRoute connectivity to an Azure virtual network where Microsoft Purview private endpoints are deployed.

This architecture is suitable mainly for small organizations or for development, testing, and proof-of-concept scenarios.

[![Screenshot that shows Microsoft Purview with private endpoints in a single virtual network scenario.](../media/concept-best-practices/network-pe-single-vnet.png)](../media/concept-best-practices/network-pe-single-vnet.png#lightbox)

#### Single region, multiple virtual networks

To connect two or more virtual networks in Azure together, you can use [virtual network peering](/en-us/azure/virtual-network/virtual-network-peering-overview). Network traffic between peered virtual networks is private and is kept on the Azure backbone network.

Many customers build their network infrastructure in Azure by using the hub-and-spoke network architecture, where:

- Networking shared services (such as network virtual appliances, ExpressRoute/VPN gateways, or DNS servers) are deployed in the hub virtual network.
- Spoke virtual networks consume those shared services via virtual network peering.

In hub-and-spoke network architectures, your organization's data governance team can be provided with an Azure subscription that includes a virtual network (hub). All data services can be located in a few other subscriptions connected to the hub virtual network through a virtual network peering or a site-to-site VPN connection.

In a hub-and-spoke architecture, you can deploy Microsoft Purview and one or more self-hosted integration runtime VMs in the hub subscription and virtual network. You can register and scan data sources from other virtual networks from multiple subscriptions in the same region.

The self-hosted integration runtime VMs can be deployed inside the same Azure virtual network or a peered virtual network where the account and ingestion private endpoints are deployed.

[![Screenshot that shows Microsoft Purview with private endpoints in a scenario of multiple virtual networks.](../media/concept-best-practices/network-pe-multi-vnet.png)](../media/concept-best-practices/network-pe-multi-vnet.png#lightbox)

You can optionally deploy another self-hosted integration runtime in the spoke virtual networks.

#### Multiple regions, multiple virtual networks

If your data sources are distributed across multiple Azure regions in one or more Azure subscriptions, you can use this scenario.

For performance and cost optimization, we highly recommended deploying one or more self-hosted integration runtime VMs in each region where data sources are located.

[![Screenshot that shows Microsoft Purview with private endpoints in a scenario of multiple virtual networks and multiple regions.](../media/concept-best-practices/network-pe-multi-region.png)](../media/concept-best-practices/network-pe-multi-region.png#lightbox)

#### Scan using Managed Vnet Runtime

You can use Managed VNet Runtime to scan data sources in a private network. Learn more from [Use a Managed VNet with your Microsoft Purview account](../data-governance-private-endpoints-managed-virtual-network).

Using Managed VNet Runtime helps to minimize the administrative overhead of managing the runtime and reduce overall scan duration.

To scan any Azure data sources over private network using Managed VNet Runtime, a managed private endpoint must be deployed within Microsoft Purview Managed Virtual Network, even if the data source already has a private network in your Azure subscription.

[![Screenshot that shows Microsoft Purview with Managed VNet.](../media/concept-best-practices/network-pe-managed-vnet.png)](../media/concept-best-practices/network-pe-managed-vnet.png#lightbox)

If you need to scan on-premises data sources or additional data sources in Azure that are not supported by Managed VNet Runtime, you can deploy both Managed VNet Runtime and Self-hosted integration runtime.

[![Screenshot that shows Microsoft Purview with Managed VNet and SHIR.](../media/concept-best-practices/network-pe-managed-vnet-shir.png)](../media/concept-best-practices/network-pe-managed-vnet-shir.png#lightbox)

### If Microsoft Purview isn't available in your primary region

Microsoft Purview is an Azure platform as a service solution. You can deploy a Microsoft Purview account inside your Azure subscription in [any supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=purview&amp;regions=all).

If Microsoft Purview isn't available in your primary Azure region, consider the following factors when choosing a secondary region to deploy your Microsoft Purview account:

- Review the latency between your primary Azure region where data sources are deployed and your secondary Azure region, where Microsoft Purview account will be deployed. For more information, see [Azure network round-trip latency statistics](/en-us/azure/networking/azure-network-latency).
- Review your data residency requirements. When you scan data sources in the Microsoft Purview Data Map, information related to your metadata is ingested and stored inside your data map in the Azure region where your Microsoft Purview account is deployed. For more information, see [Where is metadata stored](../data-gov-classic-security-best-practices#where-is-metadata-stored).
- Review your network and security requirements if private network connectivity for user access or metadata ingestion is required. For more information, see [If Microsoft Purview isn't available in your primary region](../concept-best-practices-network#if-microsoft-purview-isnt-available-in-your-primary-region).

**Option 1: Deploy your Microsoft Purview account in a secondary region and deploy all private endpoints in the primary region, where your Azure data sources are located.** For this scenario:

- This is the recommended option, if Australia Southeast is the primary region for all your data sources and you have all network resources deployed in your primary region.
- Deploy a Microsoft Purview account in your secondary region (for example, Australia East).
- Deploy all Microsoft Purview private endpoints including account, portal and ingestion in your primary region (for example, Australia Southeast).
- Deploy all [Microsoft Purview self-hosted integration runtime](../ data-map-integration-runtime-self-hosted.md) VMs in your primary region (for example, Australia Southeast). This helps to reduce cross region traffic as the Data Map scans will happen in the local region where data sources are located and only metadata is ingested int your secondary region where your Microsoft Purview account is deployed.
- If you use [Microsoft Purview Managed VNets](../data-governance-private-endpoints-managed-virtual-network) for metadata ingestion, Managed VNet Runtime and all managed private endpoints will be automatically deployed in the region where your Microsoft Purview is deployed (for example, Australia East).

**Option 2: Deploy your Microsoft Purview account in a secondary region and deploy private endpoints in the primary and secondary regions.** For this scenario:

- This option is recommended if you have data sources in both primary and secondary regions and users are connected through the primary region.
- Deploy a Microsoft Purview account in your secondary region (for example, Australia East).
- Deploy Microsoft Purview governance portal private endpoint in the primary region (for example, Australia Southeast) for user access to Microsoft Purview governance portal.
- Deploy Microsoft Purview account and ingestion private endpoints in your primary region (for example, Australia southeast) to scan data sources locally in the primary region.
- Deploy Microsoft Purview account and ingestion private endpoints in your secondary region (for example, Australia East) to scan data sources locally in the secondary region.
- Deploy [Microsoft Purview self-hosted integration runtime](../ data-map-integration-runtime-self-hosted.md) VMs in both primary and secondary regions. This will help to keep data Map scan traffic in the local region and send only metadata to Microsoft Purview Data Map where is configured in your secondary region (for example, Australia East).
- If you use [Microsoft Purview Managed VNets](../data-governance-private-endpoints-managed-virtual-network) for metadata ingestion, Managed VNet Runtime and all managed private endpoints will be automatically deployed in the region where your Microsoft Purview is deployed (for example, Australia East).

### DNS configuration with private endpoints

#### Name resolution for multiple Microsoft Purview accounts

It's recommended to follow these recommendations, if your organization needs to deploy and maintain multiple Microsoft Purview accounts using private endpoints:

1. Deploy at least one *account* private endpoint for each Microsoft Purview account.
2. Deploy at least one set of *ingestion* private endpoints for each Microsoft Purview account.
3. Deploy one *portal* private endpoint for one of the Microsoft Purview accounts in your Azure environments. Create one DNS A record for *portal* private endpoint to resolve `web.purview.azure.com`. The *portal* private endpoint can be used by all purview accounts in the same Azure virtual network or virtual networks connected through VNet peering.

[![Screenshot that shows how to handle private endpoints and DNS records for multiple Microsoft Purview accounts.](../media/concept-best-practices/network-pe-dns.png)](../media/concept-best-practices/network-pe-dns.png#lightbox)

This scenario also applies if multiple Microsoft Purview accounts are deployed across multiple subscriptions and multiple VNets that are connected through VNet peering. *Portal* private endpoint mainly renders static assets related to the Microsoft Purview governance portal, thus, it's independent of Microsoft Purview account, therefore, only one *portal* private endpoint is needed to visit all Microsoft Purview accounts in the Azure environment if VNets are connected.

[![Screenshot that shows how to handle private endpoints and DNS records for multiple Microsoft Purview accounts in multiple vnets.](../media/concept-best-practices/network-pe-dns-multi-vnet.png)](../media/concept-best-practices/network-pe-dns-multi-vnet.png#lightbox)

Note

You may need to deploy separate *portal* private endpoints for each Microsoft Purview account in the scenarios where Microsoft Purview accounts are deployed in isolated network segmentations. Microsoft Purview *portal* is static contents for all customers without any customer information. Optionally, you can use public network, (without portal private endpoint) to launch `web.purview.azure.com` if your end users are allowed to launch the Internet.

## Option 3: Use both private and public endpoints

You might choose an option in which a subset of your data sources uses private endpoints, and at the same time, you need to scan either of the following:

- Other data sources that are configured with a [service endpoint](/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)
- Data sources that have a public endpoint that's accessible through the internet

If you need to scan some data sources by using an ingestion private endpoint and some data sources by using public endpoints or a service endpoint, you can:

1. Use private endpoints for your Microsoft Purview account.
2. Set **Public network access** to **Enabled from all networks** on your Microsoft Purview account.

### Integration runtime options

- To scan an Azure data source that's configured with a private endpoint, you need to set up and use a self-hosted integration runtime on a Windows virtual machine that's deployed inside the same or a peered virtual network where Microsoft Purview account and ingestion private endpoints are deployed.

    When you're using a private endpoint with Microsoft Purview, you need to allow network connectivity from data sources to a self-hosted integration VM on the Azure virtual network where Microsoft Purview private endpoints are deployed.
- To scan an Azure data source that's configured to allow a public endpoint, you can use the Azure integration runtime.
- To scan on-premises data sources, you can also install a self-hosted integration runtime on either an on-premises Windows machine or a VM inside an Azure virtual network.
- We recommend allowing automatic upgrade for a self-hosted integration runtime. Make sure you open required outbound rules in your Azure virtual network or on your corporate firewall to allow automatic upgrade. For more information, see [Self-hosted integration runtime networking requirements](../data-map-integration-runtime-self-hosted#networking-requirements).

### Authentication options

- To scan an Azure data source that's configured to allow a public endpoint, you can use any authentication option, based on the data source type.
- If you use an ingestion private endpoint to scan an Azure data source that's configured with a private endpoint:

    - You can't use a Microsoft Purview managed identity. Instead, use a service principal, an account key, or SQL authentication, based on the data source type.
    - Make sure that your credentials are stored in an Azure key vault and registered inside Microsoft Purview.
    - You must create a credential in Microsoft Purview based on each secret that you create in Azure Key Vault. At minimum, assign *get* and *list* access for secrets for Microsoft Purview on the Key Vault resource in Azure. Otherwise, the credentials won't work in the Microsoft Purview account.

## Option 4: Use private endpoints for ingestion only

You might choose this option if you need to:

- Scan all data sources using ingestion private endpoint.
- Managed resources must be configured to disable public network.
- Enable access to Microsoft Purview governance portal through public network.

To enable this option:

1. Configure ingestion private endpoint for your Microsoft Purview account.
2. Set **Public network access** to **Disabled for ingestion only (Preview)** on your [Microsoft Purview account](../data-gov-classic-firewall).

### Integration runtime options

Follow recommendation for option 2.

### Authentication options

Follow recommendation for option 2.

## Self-hosted integration runtime network and proxy recommendations

For scanning data sources across your on-premises and Azure networks, you may need to deploy and use one or multiple [self-hosted integration runtime virtual machines](../data-map-integration-runtime-self-hosted) inside an Azure VNet or an on-premises network, for any of the scenarios mentioned earlier in this document.

- To simplify management, when possible, use Azure IR and [Microsoft Purview Managed VNet IR](../data-governance-private-endpoints-managed-virtual-network) to scan data sources.
- The Self-hosted integration runtime service can communicate with Microsoft Purview through public or private network over port 443. For more information, see, [self-hosted integration runtime networking requirements](../data-map-integration-runtime-self-hosted#networking-requirements).
- One self-hosted integration runtime VM can be used to scan one or multiple data sources in Microsoft Purview, however, self-hosted integration runtime must be only registered for Microsoft Purview and can't be used for Azure Data Factory or Azure Synapse at the same time.
- You can register and use one or multiple self-hosted integration runtimes in one Microsoft Purview account. It's recommended to place at least one self-hosted integration runtime VM in each region or on-premises network where your data sources reside.
- It's recommended to define a baseline for required capacity for each self-hosted integration runtime VM and scale the VM capacity based on demand.
- It's recommended to set up network connection between self-hosted integration runtime VMs and Microsoft Purview and its managed resources through private network, when possible.
- Allow outbound connectivity to download.microsoft.com, if auto-update is enabled.
- The self-hosted integration runtime service doesn't require outbound internet connectivity, if self-hosted integration runtime VMs are deployed in an Azure VNet or in the on-premises network that is connected to Azure through an ExpressRoute or Site to Site VPN connection. In this case, the scan and metadata ingestion process can be done through private network.
- Self-hosted integration runtime can communicate Microsoft Purview and its managed resources directly or through [a proxy server](../data-map-integration-runtime-self-hosted#proxy-server-considerations). Avoid using proxy settings if self-hosted integration runtime VM is inside an Azure VNet or connected through ExpressRoute or Site to Site VPN connection.
- Review supported scenarios, if you need to use self-hosted integration runtime with [proxy setting](../data-map-integration-runtime-self-hosted#proxy-server-considerations).