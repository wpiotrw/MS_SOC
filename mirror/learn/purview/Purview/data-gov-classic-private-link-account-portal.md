---
layout: Conceptual
title: Connect privately and securely to your Microsoft Purview account to use the classic governance portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-private-link-account-portal
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
description: This article describes how you can set up a private endpoint to connect to your Microsoft Purview account from restricted network for classic data governance.
locale: en-us
document_id: 5a296cad-27e8-acc4-c5aa-2161cad23aa7
document_version_independent_id: 5a296cad-27e8-acc4-c5aa-2161cad23aa7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-private-link-account-portal.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-private-link-account-portal
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-private-link-account-portal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 76772cf6-696c-fd06-0fc7-b20bfae2c6a0
---

# Connect privately and securely to your Microsoft Purview account to use the classic governance portal | Microsoft Learn

Important

This article covers private endpoints for the classic Microsoft Purview governance portal (https://web.purview.azure.com). If you're using the new Microsoft Purview portal (https://purview.microsoft.com/), follow the [documentation for private endpoints in the Microsoft Purview portal](data-governance-private-endpoints).

In this guide, you'll learn how to deploy private endpoints for your Microsoft Purview account to allow you to connect to your Microsoft Purview account only from VNets and private networks. To achieve this goal, you need to deploy *account* and *portal* private endpoints for your Microsoft Purview account.

Important

Microsoft Purview instances using the [new Microsoft Purview portal](data-governance-purview-portal) can only use [ingestion private endpoints](data-gov-classic-private-link-end-to-end#deploy-ingestion-private-endpoint).

The Microsoft Purview *account* private endpoint is used to add another layer of security by enabling scenarios where only client calls that originate from within the virtual network are allowed to access the Microsoft Purview account. This private endpoint is also a prerequisite for the portal private endpoint.

The Microsoft Purview *portal* private endpoint is required to enable connectivity to the [classic Microsoft Purview governance portal](https://web.purview.azure.com/resource/) using a private network.

Note

If you only create *account* and *portal* private endpoints, you won't be able to run any scans. To enable scanning on a private network, you will also need to [create an ingestion private endpoint](data-gov-classic-private-link-end-to-end).

![Diagram that shows Microsoft Purview and Private Link architecture.](media/catalog-private-link/purview-private-link-account-portal.png)

For more information about Azure Private Link service, see [private links and private endpoints](/en-us/azure/private-link/private-endpoint-overview) to learn more.

## Deployment checklist

Using this guide, you can deploy these private endpoints for an existing Microsoft Purview account:

1. Choose an appropriate Azure virtual network and a subnet to deploy Microsoft Purview private endpoints. Select one of the following options:

    - Deploy a [new virtual network](/en-us/azure/virtual-network/quick-create-portal) in your Azure subscription.
    - Locate an existing Azure virtual network and a subnet in your Azure subscription.
2. Define an appropriate [DNS name resolution method](data-gov-classic-private-link-name-resolution#deployment-options), so Microsoft Purview account and web portal can be accessible through private IP addresses. You can use any of the following options:

    - Deploy new Azure DNS zones using the steps explained further in this guide.
    - Add required DNS records to existing Azure DNS zones using the steps explained further in this guide.
    - After completing the steps in this guide, add required DNS A records in your existing DNS servers manually.
3. Deploy account and portal private endpoints for an existing Microsoft Purview account.
4. Enable access to Microsoft Entra ID if your private network has network security group rules set to deny for all public internet traffic.
5. After completing this guide, adjust DNS configurations if needed.
6. Validate your network and name resolution from management machine to Microsoft Purview.

## Enable *account* and *portal* private endpoint

There are two ways you can add Microsoft Purview *account* and *portal* private endpoints for an existing Microsoft Purview account:

- Use the Azure portal (Microsoft Purview account).
- Use the Private Link Center.

### Use the Azure portal (Microsoft Purview account)

1. Go to the [Azure portal](https://portal.azure.com), and then select your Microsoft Purview account, and under **Settings** select **Networking**, and then select **Private endpoint connections**.

    ![Screenshot that shows creating an account private endpoint.](media/catalog-private-link/purview-pe-add-to-existing.png)
2. Select **+ Private endpoint** to create a new private endpoint.
3. Fill in the basic information.
4. On the **Resource** tab, for **Resource type**, select **Microsoft.Purview/accounts**.
5. For **Resource**, select the Microsoft Purview account, and for **Target sub-resource**, select **account**.
6. On the **Configuration** tab, select the virtual network and optionally, select Azure Private DNS zone to create a new Azure DNS Zone.

    Note

    For DNS configuration, you can also use your existing Azure Private DNS Zones from the dropdown list or add the required DNS records to your DNS Servers manually later. For more information, see [Configure DNS Name Resolution for private endpoints](data-gov-classic-private-link-name-resolution)
7. Go to the summary page, and select **Create** to create the portal private endpoint.
8. Follow the same steps when you select **portal** for **Target sub-resource**.

### Use the Private Link Center

1. Go to the [Azure portal](https://portal.azure.com).
2. In the search bar at the top of the page, search for **private link** and go to the **Private Link** pane by selecting the first option.
3. Select **+ Add**, and fill in the basic details.

    ![Screenshot that shows creating private endpoints from the Private Link Center.](media/catalog-private-link/private-link-center.png)
4. For **Resource**, select the already created Microsoft Purview account. For **Target sub-resource**, select **account**.
5. On the **Configuration** tab, select the virtual network and private DNS zone. Go to the summary page, and select **Create** to create the account private endpoint.

Note

Follow the same steps when you select **portal** for **Target sub-resource**.

## Enable access to Microsoft Entra ID

Note

If your VM, VPN gateway, or VNet Peering gateway has public internet access, it can access the Microsoft Purview portal and the Microsoft Purview account enabled with private endpoints. For this reason, you don't have to follow the rest of the instructions. If your private network has network security group rules set to deny all public internet traffic, you'll need to add some rules to enable Microsoft Entra ID access. Follow the instructions to do so.

These instructions are provided for accessing Microsoft Purview securely from an Azure VM. Similar steps must be followed if you're using VPN or other virtual network Peering gateways.

1. Go to your VM in the Azure portal, and under **Settings**, select **Networking**. Then select **Outbound port rules**, **Add outbound port rule**.

    ![Screenshot that shows adding an outbound rule.](media/catalog-private-link/outbound-rule-add.png)
2. On the **Add outbound security rule** pane:

    1. Under **Destination**, select **Service Tag**.
    2. Under **Destination service tag**, select **AzureActiveDirectory**.
    3. Under **Destination port ranges**, select \*.
    4. Under **Action**, select **Allow**.
    5. Under **Priority**, the value should be higher than the rule that denied all internet traffic.

    Create the rule.

    ![Screenshot that shows adding outbound rule details.](media/catalog-private-link/outbound-rule-details.png)
3. Follow the same steps to create another rule to allow the **AzureResourceManager** service tag. If you need to access the Azure portal, you can also add a rule for the **AzurePortal** service tag.
4. Connect to the VM and open the browser. Go to the browser console by selecting Ctrl+Shift+J, and switch to the network tab to monitor network requests. Enter web.purview.azure.com in the URL box, and try to sign in by using your Microsoft Entra credentials. Sign-in will probably fail, and on the **Network** tab on the console, you can see Microsoft Entra ID trying to access aadcdn.msauth.net but getting blocked.

    ![Screenshot that shows sign-in fail details.](media/catalog-private-link/login-fail.png)
5. In this case, open a command prompt on the VM, ping aadcdn.msauth.net, get its IP, and then add an outbound port rule for the IP in the VM's network security rules. Set the **Destination** to **IP Addresses** and set **Destination IP addresses** to the aadcdn IP. Because of Azure Load Balancer and Azure Traffic Manager, the Microsoft Entra Content Delivery Network IP might be dynamic. After you get its IP, it's better to add it into the VM's host file to force the browser to visit that IP to get the Microsoft Entra Content Delivery Network.

    ![Screenshot that shows the test ping.](media/catalog-private-link/ping.png)

    ![Screenshot that shows the Microsoft Entra Content Delivery Network rule.](media/catalog-private-link/aadcdn-rule.png)
6. After the new rule is created, go back to the VM and try to sign in by using your Microsoft Entra credentials again. If sign-in succeeds, then the Microsoft Purview portal is ready to use. But in some cases, Microsoft Entra ID redirects to other domains to sign in based on a customer's account type. For example, for a live.com account, Microsoft Entra ID redirects to live.com to sign in, and then those requests are blocked again. For Microsoft employee accounts, Microsoft Entra ID accesses msft.sts.microsoft.com for sign-in information.

    Check the networking requests on the browser **Networking** tab to see which domain's requests are getting blocked, redo the previous step to get its IP, and add outbound port rules in the network security group to allow requests for that IP. If possible, add the URL and IP to the VM's host file to fix the DNS resolution. If you know the exact sign-in domain's IP ranges, you can also directly add them into networking rules.
7. Now your Microsoft Entra sign-in should be successful. The Microsoft Purview portal will load successfully, but listing all the Microsoft Purview accounts won't work because it can only access a specific Microsoft Purview account. Enter `web.purview.azure.com/resource/{PurviewAccountName}` to directly visit the Microsoft Purview account that you successfully set up a private endpoint for.