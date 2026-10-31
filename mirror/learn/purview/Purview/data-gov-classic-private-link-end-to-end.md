---
layout: Conceptual
title: Deploy private endpoints for your Microsoft Purview account for using classic governance and scan data sources privately and securely  | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-private-link-end-to-end
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
description: This article describes how you can set up a private endpoint to connect to your Microsoft Purview account and scan data sources from restricted network for an end to end isolation for classic governance portal.
locale: en-us
document_id: 613cb0df-4319-01d2-ebba-58b1617b143a
document_version_independent_id: 613cb0df-4319-01d2-ebba-58b1617b143a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-private-link-end-to-end.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-private-link-end-to-end
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-private-link-end-to-end.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: a34705a0-1b55-547e-826d-cf16dc17634d
---

# Deploy private endpoints for your Microsoft Purview account for using classic governance and scan data sources privately and securely  | Microsoft Learn

Important

This article covers private endpoints for the classic Microsoft Purview governance portal (https://web.purview.azure.com). If you're using the new Microsoft Purview portal (https://purview.microsoft.com/), follow the [documentation for private endpoints in the Microsoft Purview portal](data-governance-private-endpoints).

In this guide, you'll learn how to deploy *account*, \_portal, and *ingestion* private endpoints for your Microsoft Purview account to access purview account and scan data sources using a self-hosted integration runtime securely and privately, enabling end-to-end network isolation.=

The Microsoft Purview *account* private endpoint is used to add another layer of security by enabling scenarios where only client calls that originate from within the virtual network are allowed to access the Microsoft Purview account. This private endpoint is also a prerequisite for the portal private endpoint.

The Microsoft Purview *portal* private endpoint is required to enable connectivity to [the classic Microsoft Purview governance portal](https://web.purview.azure.com/resource/) using a private network.

Microsoft Purview can scan data sources in Azure or an on-premises environment by using *ingestion* private endpoints. Depending on your accounts deployment date and configuration, up to three private endpoint resources are required to be deployed and linked to Microsoft Purview configured resources when ingestion private endpoint is deployed:

- If you're using a [managed Event Hubs for kafka notifications](data-map-kafa-notifications), a namespace private endpoint is linked to a Microsoft Purview configured Event Hubs namespace.
- If your account was created before December 15, 2023:

    - Blob private endpoint is linked to a Microsoft Purview managed storage account.
    - Queue private endpoint is linked to a Microsoft Purview managed storage account.
- If your account was created after December 15, 2023 (or deployed using API version 2023-05-01-preview onwards):

    - Blob private endpoint is linked to a Microsoft Purview ingestion storage.
    - Queue private endpoint is linked to a Microsoft Purview ingestion storage.

    ![Diagram that shows Microsoft Purview and Private Link architecture.](media/catalog-private-link/purview-private-link-architecture.png)

## Deployment checklist

Following the instructions further in this guide, you can deploy these private endpoints for an existing Microsoft Purview account:

1. Choose an appropriate Azure virtual network and a subnet to deploy Microsoft Purview private endpoints. Select one of the following options:

    - Deploy a [new virtual network](/en-us/azure/virtual-network/quick-create-portal) in your Azure subscription.
    - Locate an existing Azure virtual network and a subnet in your Azure subscription.
2. Define an appropriate [DNS name resolution method](data-gov-classic-private-link-name-resolution#deployment-options), so you can access Microsoft Purview account and scan data sources using private network. You can use any of the following options:

    - Deploy new Azure DNS zones using the steps explained further in this guide.
    - Add required DNS records to existing Azure DNS zones using the steps explained further in this guide.
    - After completing the steps in this guide, add required DNS A records in your existing DNS servers manually.
3. Deploy private endpoints for an existing Microsoft Purview account.
4. Enable access to Microsoft Entra ID if your private network has network security group rules set to deny for all public internet traffic.
5. Deploy and register Self-hosted integration runtime inside the same virtual network or a peered virtual network where Microsoft Purview account and ingestion private endpoints are deployed.
6. After completing this guide, adjust DNS configurations if needed.
7. Validate your network and name resolution between management machine, self-hosted IR VM and data sources to Microsoft Purview.

    Note

    If you [configure your own Event Hubs namespace](data-map-kafa-notifications) or [enable a managed Event Hubs namespace](data-map-kafa-notifications#create-a-managed-namespace) after deploying your ingestion private endpoint, you'll need to redeploy the ingestion private endpoint.

## Enable *account* and *portal* private endpoint

1. Go to the [Azure portal](https://portal.azure.com), and then select your Microsoft Purview account, and under **Settings** select **Networking**, and then select **Private endpoint connections**.

    ![Screenshot that shows creating an account private endpoint.](media/catalog-private-link/purview-pe-add-to-existing.png)
2. Select **+ Private endpoint** to create a new private endpoint.
3. Fill in the basic information.
4. On the **Resource** tab, for **Resource type**, select **Microsoft.Purview/accounts**.
5. For **Resource**, select the Microsoft Purview account, and for **Target sub-resource**, select **account**.
6. On the **Configuration** tab, select the virtual network and optionally, select Azure Private DNS zone to create a new Azure DNS Zone.

    Note

    For DNS configuration, you can also use your existing Azure Private DNS Zones from the dropdown list or add the required DNS records to your DNS Servers manually later. For more information, see [Configure DNS Name Resolution for private endpoints](data-gov-classic-private-link-name-resolution)
7. Go to the summary page, and select **Create** to create the account private endpoint.
8. Repeat steps 2 through 7 to create the portal private endpoint. Make sure you select **portal** for **Target sub-resource**.

## Deploy *ingestion* private endpoint

Ingestion private endpoints are deployed from the Azure portal for all Microsoft Purview instances, regardless of whether you're using the Microsoft Purview portal or the classic governance portal.

1. Go to the [Azure portal](https://portal.azure.com), and then search for and select your Microsoft Purview account.
2. From your Microsoft Purview account, under **Settings** select **Networking**, and then select **Ingestion private endpoint connections**.
3. Under Ingestion private endpoint connections, select **+ New** to create a new ingestion private endpoint.

    ![Screenshot that shows add private endpoint to existing account.](media/catalog-private-link/purview-pe-add-ingestion-to-existing.png)
4. Fill in the basic information, selecting your existing virtual network and a subnet details. Optionally, select **Private DNS integration** to use Azure Private DNS Zones. Select correct Azure Private DNS Zones from each list.

    Note

    You can also use your existing Azure Private DNS zones or create DNS records in your DNS Servers manually later. For more information, see [Configure DNS Name Resolution for private endpoints](data-gov-classic-private-link-name-resolution)
5. Select **Create** to create the private endpoint.
6. If you don't have one already, you need to deploy a self-hosted integration runtime to connect to the sources with private endpoints.

## Configure networking for Event Hubs namespace

If you've [configured an Event Hubs to send/receive events to/from Microsoft Purview's Apache Atlas Kafka topics](data-map-kafa-notifications), you need to confirm your [Event Hubs network settings](data-map-kafa-notifications#event-hubs-networking) allow communication.

### Deploy self-hosted integration runtime (IR) and scan your data sources

Once you deploy ingestion private endpoints for your Microsoft Purview, you need to setup and register at least one self-hosted integration runtime (IR):

- All on-premises source types like Microsoft SQL Server, Oracle, SAP, and others are currently supported only via self-hosted IR-based scans. The self-hosted IR must run within your private network and then be peered with your virtual network in Azure.
- For all Azure source types like Azure Blob Storage and Azure SQL Database, you must explicitly choose to run the scan by using a self-hosted integration runtime that is deployed in the same virtual network or a peered virtual network where Microsoft Purview account and ingestion private endpoints are deployed.

Follow the steps in [Create and manage a self-hosted integration runtime](data-map-integration-runtime-self-hosted) to set up a self-hosted IR. Then set up your scan on the Azure source by choosing that self-hosted IR in the **Connect via integration runtime** dropdown list to ensure network isolation.

![Screenshot that shows running an Azure scan by using self-hosted IR.](media/catalog-private-link/shir-for-azure.png)

Important

Make sure you download and install the latest version of self-hosted integration runtime from [Microsoft download center](https://go.microsoft.com/fwlink/?linkid=2246619).

## Enable access to Microsoft Entra ID

Note

If your VM, VPN gateway, or VNet Peering gateway has public internet access, it can access the classic Microsoft Purview governance portal and the Microsoft Purview account enabled with private endpoints. For this reason, you don't have to follow the rest of the instructions. If your private network has network security group rules set to deny all public internet traffic, you'll need to add some rules to enable Microsoft Entra ID access. Follow the instructions to do so.

These instructions are provided for accessing Microsoft Purview securely from an Azure VM. Similar steps must be followed if you're using VPN or other virtual network Peering gateways.

1. Go to your virtual machine in the Azure portal, and under **Networking**, select **Network settings**.
2. Select **+ Create port rule**
3. Select **Outbound port rule**

    ![Screenshot that shows adding an outbound rule.](media/catalog-private-link/outbound-rule-add.png)
4. On the **Add outbound security rule** pane:

    1. Under **Destination**, select **Service Tag**.
    2. Under **Destination service tag**, select **AzureActiveDirectory**.
    3. Under **Destination port ranges**, select \*.
    4. Under **Action**, select **Allow**.
    5. Under **Priority**, the value should be higher than the rule that denied all internet traffic.

    Create the rule.

    ![Screenshot that shows adding outbound rule details.](media/catalog-private-link/outbound-rule-details.png)
5. Follow the same steps to create another rule to allow the **AzureResourceManager** service tag. If you need to access the Azure portal, you can also add a rule for the **AzurePortal** service tag.
6. Connect to the VM and open the browser. Go to the browser console by selecting Ctrl+Shift+J, and switch to the network tab to monitor network requests. Enter web.purview.azure.com in the URL box, and try to sign in by using your Microsoft Entra credentials. Sign-in will probably fail, and on the **Network** tab on the console, you can see Microsoft Entra ID trying to access aadcdn.msauth.net but getting blocked.

    ![Screenshot that shows sign-in fail details.](media/catalog-private-link/login-fail.png)
7. In this case, open a command prompt on the VM, ping aadcdn.msauth.net, get its IP, and then add an outbound port rule for the IP in the VM's network security rules. Set the **Destination** to **IP Addresses** and set **Destination IP addresses** to the aadcdn IP. Because of Azure Load Balancer and Azure Traffic Manager, the Microsoft Entra Content Delivery Network IP might be dynamic. After you get its IP, it's better to add it into the VM's host file to force the browser to visit that IP to get the Microsoft Entra Content Delivery Network.

    ![Screenshot that shows the test ping.](media/catalog-private-link/ping.png)

    ![Screenshot that shows the Microsoft Entra Content Delivery Network rule.](media/catalog-private-link/aadcdn-rule.png)
8. After the new rule is created, go back to the VM and try to sign in by using your Microsoft Entra credentials again. If signin succeeds, then the classic Microsoft Purview governance portal is ready to use. But in some cases, Microsoft Entra ID redirects to other domains to sign in based on a customer's account type. For example, for a live.com account, Microsoft Entra ID redirects to live.com to sign in, and then those requests are blocked again. For Microsoft employee accounts, Microsoft Entra ID accesses msft.sts.microsoft.com for sign-in information.

    Check the networking requests on the browser **Networking** tab to see which domain's requests are getting blocked, redo the previous step to get its IP, and add outbound port rules in the network security group to allow requests for that IP. If possible, add the URL and IP to the VM's host file to fix the DNS resolution. If you know the exact sign-in domain's IP ranges, you can also directly add them into networking rules.
9. Now your Microsoft Entra sign-in should be successful. The classic Microsoft Purview governance portal will load successfully, but listing all the Microsoft Purview accounts won't work because it can only access a specific Microsoft Purview account. Enter `web.purview.azure.com/resource/{PurviewAccountName}` to directly visit the Microsoft Purview account that you successfully set up a private endpoint for.

## Firewalls to restrict public access

To cut off access to the Microsoft Purview account completely from the public internet, follow these steps. This setting applies to both private endpoint and ingestion private endpoint connections.

1. From the [Azure portal](https://portal.azure.com), go to the Microsoft Purview account, and under **Settings**, select **Networking**.
2. Go to the **Firewall** tab, and ensure that the toggle is set to **Disable from all networks**.

    ![Screenshot that shows private endpoint firewall settings.](media/catalog-private-link/purview-firewall-private.png)