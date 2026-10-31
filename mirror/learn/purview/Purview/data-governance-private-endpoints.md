---
layout: Conceptual
title: Private endpoints for governance solutions in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-private-endpoints
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
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand how you can use private endpoints to secure access to governance solutions in the Microsoft Purview portal.
locale: en-us
document_id: 8a2659a0-4357-1702-47d7-a6a779abe90f
document_version_independent_id: 8a2659a0-4357-1702-47d7-a6a779abe90f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-private-endpoints.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-private-endpoints
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-private-endpoints.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: dad23b6c-b807-6283-1e6a-35623cd5857c
---

# Private endpoints for governance solutions in Microsoft Purview | Microsoft Learn

Important

This article covers private endpoints for governance solutions in the [Microsoft Purview portal](https://purview.microsoft.com/). If you're using the [classic governance portal](https://web.purview.azure.com), follow the [documentation for private endpoints in the classic portal](data-gov-classic-private-link).

You can use private links to secure access to Microsoft Purview Unified Catalog and Data Map, and secure data traffic between Microsoft Purview and your private networks. Azure Private links and Azure Networking private endpoints are used to route traffic across Microsoft's infrastructure, instead of using the internet. To learn more about Azure Private Link in general, see: [What is Azure Private Link](/en-us/azure/private-link/private-link-overview)?

A private endpoint is a single, directional technology that lets clients initiate connections to a given service, but doesn't allow the service to initiate a connection into the customer network. For multitenant services, this model provides link identifiers to prevent access to other customers' resources hosted within the same service. When you use private endpoints, only a limited set of other PaaS resources can be accessed from services using the integration.

You can deploy an *ingestion* private endpoint if you need to scan Azure IaaS and PaaS data sources inside Azure virtual networks and on-premises data sources through a private connection. This method ensures network isolation for your metadata flowing from the data sources to Microsoft Purview Data Map.

You can deploy a *platform* private endpoint to allow only client calls to the Microsoft Purview governance portal that originates from within the private network and connect to the Microsoft Purview governance portal using a private network connectivity.

Important

Private endpoints ensure that your organization's user traffic and resources within Azure, follow your organization's configured private link network path, and you can configure Microsoft Purview to deny all request from outside that network path.

However, for external sources private endpoints do not manage all network traffic. You to configure traffic isolation from non-Azure based infrastructure, like on-premises infrastructure, you need to configure ExpressRoute, or virtual private networks, and use integration runtimes to further secure your data sources.

## Prerequisites

Before deploying private endpoints for your Microsoft Purview governance resources and the Microsoft Purview portal, ensure you meet the following prerequisites:

1. An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
2. To configure private endpoints, you need to be a [Microsoft Purview admin](data-governance-roles-permissions#tenant-level-role-groups) and have permissions in Azure to create and configure resources like virtual machines (VMs) and virtual networks (VNets).
3. Currently, Azure Data Factory, Azure Machine Learning, and Azure Synapse connections aren't supported with the platform private endpoint, and might not work after switching.

## Deployment checklist

Following the instructions further in this guide, you can deploy these private endpoints for an existing Microsoft Purview account:

1. Choose an appropriate Azure virtual network and a subnet to deploy Microsoft Purview private endpoints. Select one of the following options:
    - Deploy a new virtual network in your Azure subscription.
    - Locate an existing Azure virtual network and a subnet in your Azure subscription.
2. Define an appropriate [DNS name resolution method](data-gov-classic-private-link-name-resolution#deployment-options), so you can access Microsoft Purview account and scan data sources using a private network.
3. Create a platform private endpoint.
4. Enable ingestion private endpoints
5. Disable public access for Microsoft Purview.
6. Enable access to Microsoft Entra ID if your private network has network security group rules set to deny for all public internet traffic.
7. Deploy and register a Self-hosted integration runtime inside the same virtual network or a peered virtual network where Microsoft Purview account and ingestion private endpoints are deployed.
8. After completing this guide, adjust DNS configurations if needed.

## Create a virtual network

Tip

These instructions will create a basic virtual network. For more information about virtual network options and features, see the [virtual network documentation](/en-us/azure/virtual-network/quick-create-portal).

The next step is to create a virtual network and subnet. The number of IP address your subnet will need is made up of the number of capacities on your tenant plus three. For example, if you're creating a subnet for a tenant with seven capacities, you'll need 10 IP addresses.

Replace the sample parameters in the following table with your own to create a virtual network and subnet.

| Parameter | Value |
| --- | --- |
| `<resource-group-name>` | myResourceGroup |
| `<virtual-network-name>` | myVirtualNetwork |
| `<region-name>` | Central US |
| `<address-space>` | 10.0.0.0/16 |
| `<subnet-name>` | mySubnet |
| `<subnet-address-range>` | 10.0.0.0/24 |

1. Open the [Azure portal](https://portal.azure.com).
2. Select **Create a resource &gt; Networking &gt; Virtual network** or search for **Virtual network** in the search box.
3. In **Create virtual network**, enter or select the following information in the **Basics** tab:

    | Settings | Value |
    | --- | --- |
    | **Project details** |  |
    | Subscription | Select your Azure Subscription |
    | Resource group | Select **Create new**, enter `<resource-group-name>`, then select **OK**, or select an existing `<resource-group-name>` based on parameters. |
    | **Instance details** |  |
    | Name | Enter `<virtual-network-name>` |
4. Select the **IP addresses** tab and enter the subnet address range.
5. Select **Review + create** &gt; **Create**.

## Define a DNS name resolution method

Follow this article to select and deploy a DNS name resolution method that bets fits your organization's needs: [Configure DNS Name Resolution for private endpoints](data-gov-classic-private-link-name-resolution#deployment-options).

## Create a platform private endpoint

The next step is to create the platform private endpoint for Microsoft Purview.

1. Open the [Azure portal](https://portal.azure.com).
2. Select **Create a resource &gt; Networking &gt; Private Link**.
3. In **Private Link Center - Overview**, under the option to **Build a private connection to a service**, select **Create private endpoint**.
4. In the **Create a private endpoint - Basics** tab, enter or select the following information:

    | Settings | Value |
    | --- | --- |
    | **Project details** |  |
    | Subscription | Select your Azure Subscription |
    | Resource group | Select **myResourceGroup**. You created this in the previous section |
    | **Instance details** |  |
    | Name | Enter *myPrivateEndpoint*. If this name is taken, create a unique name. |
    | Network Interface Name | Filled automatically by the instance name. |
    | Region | Selected automatically based on your resource group. |
5. Once that information is complete, select **Next: Resource** and in the **Create a private endpoint - Resource** page, enter or select the following information:

    | Settings | Value |
    | --- | --- |
    | Connection method | Select connect to an Azure resource in my directory |
    | Subscription | Select your subscription |
    | Resource type | Select **Microsoft.Purview/accounts** |
    | Resource | Select your Microsoft Purview resource |
    | Target subresource | Platform |
6. Once that information is properly input, select **Next: Virtual Network** and enter or select the following information:

    | Settings | Value |
    | --- | --- |
    | **NETWORKING** |  |
    | Virtual network | Select the virtual network you created earlier. |
    | Subnet | Select the subnet you created earlier. |
    | **PRIVATE IP configuration** | Select **Dynamically allocate IP address**. |
7. Select **Next: DNS** and enter the following information:

    | Settings | Value |
    | --- | --- |
    | Integrate with private DNS zone | Select **Yes** |
    | Subscription | Select your subscription where your DNS zone is configured. |
    | Resource group | Select the resource group where your DNS zone is configured. |
8. Select **Next: Tags** and on the tags page you can optionally add any tags your organization is using in Azure.
9. Select **Next: Review + create** which displays the **Review + create** page where Azure validates your configuration. When you see the **Validation passed** message, select **Create**.

## Enable *ingestion* private endpoint

1. Go to the [Azure portal](https://portal.azure.com), search for and then select your Microsoft Purview account.
2. From your Microsoft Purview account, under **Settings** select **Networking**, and then select **Ingestion private endpoint connections**.
3. Under Ingestion private endpoint connections, select **+ New** to create a new ingestion private endpoint.
4. Fill in the basic information, selecting your existing virtual network and a subnet details. Optionally, select **Private DNS integration** to use Azure Private DNS Zones. Select correct Azure Private DNS Zones from each list.

    Note

    You can also use your existing Azure Private DNS zones or create DNS records in your DNS Servers manually. For more information, see [Configure DNS Name Resolution for private endpoints](data-gov-classic-private-link-name-resolution).
5. Select **Create** to finish the setup.

## Disable public access for Microsoft Purview

To cut off access to the Microsoft Purview account completely from the public internet, follow these steps. This setting applies to both private endpoint and ingestion private endpoint connections.

1. From the [Azure portal](https://portal.azure.com), go to the Microsoft Purview account, and under **Settings**, select **Networking**.
2. Go to the **Firewall** tab, and ensure that the toggle is set to **Disable from all networks**.

## Enable access to Microsoft Entra ID

Note

If your VM, VPN gateway, or virtual network peering gateway has public internet access, it can access the Microsoft Purview governance portal and the Microsoft Purview account enabled with private endpoints. For this reason, you don't have to follow the rest of the instructions. If your private network has network security group rules set to deny all public internet traffic, you'll need to add some rules to enable Microsoft Entra ID access. Follow the instructions to do so.

These instructions are provided for accessing Microsoft Purview securely from an Azure VM. Similar steps must be followed if you're using VPN or other virtual network peering gateways.

1. Go to your VM in the Azure portal, and under **Settings**, select **Networking**. Then select **Outbound port rules** &gt; **Add outbound port rule**.
2. On the **Add outbound security rule** pane:

    1. Under **Destination**, select **Service Tag**.
    2. Under **Destination service tag**, select **AzureActiveDirectory**.
    3. Under **Destination port ranges**, select \*.
    4. Under **Action**, select **Allow**.
    5. Under **Priority**, the value should be higher than the rule that denied all internet traffic.

    Create the rule.
3. Follow the same steps to create another rule to allow the **AzureResourceManager** service tag. If you need to access the Azure portal, you can also add a rule for the **AzurePortal** service tag.
4. Connect to the VM and open the browser. Go to the browser console by selecting Ctrl+Shift+J, and switch to the network tab to monitor network requests. Enter web.purview.azure.com in the URL box, and try to sign in by using your Microsoft Entra credentials. Sign-in will probably fail, and on the **Network** tab on the console, you can see Microsoft Entra ID trying to access aadcdn.msauth.net but getting blocked.
5. In this case, open a command prompt on the VM, ping aadcdn.msauth.net, get its IP, and then add an outbound port rule for the IP in the VM's network security rules. Set the **Destination** to **IP Addresses** and set **Destination IP addresses** to the aadcdn IP. Because of Azure Load Balancer and Azure Traffic Manager, the Microsoft Entra Content Delivery Network IP might be dynamic. After you get its IP, it's better to add it into the VM's host file to force the browser to visit that IP to get the Microsoft Entra Content Delivery Network.
6. After the new rule is created, go back to the VM and try to sign in by using your Microsoft Entra credentials again. If sign-in succeeds, then the Microsoft Purview governance portal is ready to use. But in some cases, Microsoft Entra ID redirects to other domains to sign in based on a customer's account type. For example, for a live.com account, Microsoft Entra ID redirects to live.com to sign in, and then those requests are blocked again. For Microsoft employee accounts, Microsoft Entra ID accesses msft.sts.microsoft.com for sign-in information.

    Check the networking requests on the browser **Networking** tab to see which domain's requests are getting blocked, redo the previous step to get its IP, and add outbound port rules in the network security group to allow requests for that IP. If possible, add the URL and IP to the VM's host file to fix the DNS resolution. If you know the exact sign-in domain's IP ranges, you can also directly add them into networking rules.
7. Now your Microsoft Entra sign-in should be successful. The Microsoft Purview governance portal will load successfully, but listing all the Microsoft Purview accounts won't work because it can only access a specific Microsoft Purview account. Enter `web.purview.azure.com/resource/{PurviewAccountName}` to directly visit the Microsoft Purview account that you successfully set up a private endpoint for.

## Deploy self-hosted integration runtime (IR) and scan your data sources

Once you deploy ingestion private endpoints for your Microsoft Purview, you need to setup and register at least one self-hosted integration runtime (IR):

- All on-premises source types like Microsoft SQL Server, Oracle, SAP, and others are currently supported only via self-hosted IR-based scans. The self-hosted IR must run within your private network and then be peered with your virtual network in Azure.
- For all Azure source types like Azure Blob Storage and Azure SQL Database, you must explicitly choose to run the scan by using a self-hosted integration runtime that is deployed in the same virtual network or a peered virtual network where Microsoft Purview account and ingestion private endpoints are deployed.

Follow the steps in [Create and manage a self-hosted integration runtime](data-map-integration-runtime-self-hosted) to set up a self-hosted IR. Then set up your scan on the Azure source by choosing that self-hosted IR in the **Connect via integration runtime** dropdown list to ensure network isolation.

Important

Make sure you download and install the latest version of self-hosted integration runtime from [Microsoft download center](https://go.microsoft.com/fwlink/?linkid=2246619).

## Test your private connection

To test your new private endpoints, you can create a virtual machine within your private virtual network and access your platform private endpoint to ensure it's working.

1. Create a virtual machine (VM).
2. Connect to a VM using Remote Desktop (RDP).
3. Access Microsoft Purview privately from the virtual machine.

## Create a virtual machine (VM)

The next step is to create a VM.

1. On the upper-left side of the screen in your Azure portal, select **Create a resource &gt; Compute &gt; Virtual Machine**.
2. In the **Basics** tab, enter or select the following information:

    | Settings | Value |
    | --- | --- |
    | **Project details** |  |
    | Subscription | Select your Azure Subscription |
    | Resource group | Select **myResourceGroup** which you created in the previous section |
    | **Instance details** |  |
    | VM name | Enter **myVM** |
    | Region | Select **West US** |
    | Availability options | Leave the default **No infrastructure redundancy required** |
    | Image | Select **Windows 10 Pro** |
    | Size | Leave the default **Standard DS1 v2** |
    | ADMINISTRATOR ACCOUNT |  |
    | Username | Enter a username of your choosing |
    | Password | Enter a password of your choosing. The password must be at least 12 characters long and meet the [defined complexity requirements](/en-us/azure/virtual-machines/windows/faq#what-are-the-password-requirements-when-creating-a-vm) |
    | Confirm password | Reenter password |
    | INBOUND PORT RULES |  |
    | Public inbound ports | Leave the default **None** |
    | LICENSING |  |
    | I have an eligible Windows 10/11 license | Check the box |
3. Select **Next: Disks**.
4. In the **Disks** tab, leave the defaults and select **Next: Networking**.
5. In the **Networking** tab, select the following information:

    | Settings | Value |
    | --- | --- |
    | Virtual network | Leave the default **MyVirtualNetwork** |
    | Address space | Leave the default **10.0.0.0/24** |
    | Subnet | Leave the default **mySubnet (10.0.0.0/24)** |
    | Public IP | Leave the default **(new) myVM-ip** |
    | Public inbound ports | Select **Allow selected** |
    | Select inbound ports | Select **RDP** |
6. Select **Review + create**. You're taken to the **Review + create** page where Azure validates your configuration.
7. When you see the **Validation passed** message, select **Create**.

### Connect to a VM using Remote Desktop (RDP)

After you create your VM, called **myVM**, connect to it from the internet using the following steps:

1. In the portal's search bar, enter *myVM*.
2. Select the **Connect** button, and choose **RDP** from the dropdown menu.
3. Enter an IP address, then select **Download RDP File**. Azure creates a Remote Desktop Protocol (.rdp) file and downloads it to your computer.
4. Open the *.rdp* file to start Remote Desktop Connection, then select **Connect**.
5. Enter the username and password you specified when creating the VM in the previous step.
6. Select **OK**.
7. You might receive a certificate warning during the sign-in process. If you receive a certificate warning, select **Yes** or **Continue**.

### Access Microsoft Purview privately from the VM

The next step is to access Microsoft Purview privately, from the virtual machine you created in the previous step, using the following steps:

1. In the Remote Desktop of myVM, open PowerShell.
2. Enter `nslookup <tenant-object-id>-api.purview-service.microsoft.com`.
3. You receive a response similar to the following message:

    ```
    Server:  UnKnown
    Address:  168.63.129.16
    
    Non-authoritative answer:
    Name:    <tenantid>-api.purview-service.microsoft.com
    Address:  10.5.0.4
    ```
4. Open the browser and go to https://purview.microsoft.com to access Microsoft Purview privately.

## Completion of private endpoint configuration

Once you've followed the steps in the previous sections and the private link is successfully configured, your organization implements private links based on the following configuration selections, whether the selection is set upon initial configuration or later changed.

If Azure Private Link is properly configured and **Block public Internet access** is **enabled**:

- Microsoft Purview is only accessible for your organization from private endpoints, and isn't accessible from the public Internet.
- Traffic from the virtual network targeting endpoints and scenarios that support private links are transported through the private link.
- Traffic from the virtual network targeting endpoints and scenarios that don't\* support private links will be blocked by the service, and won't work.
- There could be scenarios that don't support private links, which therefore will be blocked at the service when **Block public Internet access** is enabled.

If Azure Private Link is properly configured and **Block public Internet access** is **disabled**:

- Traffic from the public Internet will be allowed by Microsoft Purview services
- Traffic from the virtual network targeting endpoints and scenarios that support private links are transported through the private link.
- Traffic from the virtual network targeting endpoints and scenarios that don't\* support private links are transported through the public Internet, and will be allowed by Microsoft Purview services.
- If the virtual network is configured to block public Internet access, scenarios that don't support private links will be blocked by the virtual network, and won't work.'