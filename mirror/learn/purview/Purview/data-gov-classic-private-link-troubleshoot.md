---
layout: Conceptual
title: Troubleshooting private endpoint configuration for Microsoft Purview accounts for using classic Microsoft Purview governance portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-private-link-troubleshoot
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
description: This article describes how to troubleshoot problems with your Microsoft Purview account related to private endpoints configurations for using the classic governance portal.
locale: en-us
document_id: 15cb81ec-dd55-ce4c-0ba8-98c135f53aa6
document_version_independent_id: 15cb81ec-dd55-ce4c-0ba8-98c135f53aa6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-private-link-troubleshoot.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-private-link-troubleshoot
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-private-link-troubleshoot.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 2436f6b4-e7b0-edc5-ed60-db78261ebdb9
---

# Troubleshooting private endpoint configuration for Microsoft Purview accounts for using classic Microsoft Purview governance portal | Microsoft Learn

Important

This article covers private endpoints for the classic Microsoft Purview governance portal (https://web.purview.azure.com). If you're using the new Microsoft Purview portal (https://purview.microsoft.com/), follow the [documentation for private endpoints in the Microsoft Purview portal](data-governance-private-endpoints).

This article summarizes known limitations related to using private endpoints for Microsoft Purview and provides a list of steps and solutions for troubleshooting some of the most common relevant issues.

## Known limitations

- We currently don't support ingestion private endpoints that work with your AWS sources.
- Scanning Azure Multiple Sources using self-hosted integration runtime isn't supported.
- Using Azure integration runtime to scan data sources behind private endpoint isn't supported.
- The ingestion private endpoints can be created via the classic Microsoft Purview governance portal experience described in the steps [here](data-gov-classic-private-link-end-to-end#deploy-ingestion-private-endpoint). They can't be created from the Private Link Center.
- Creating a DNS record for ingestion private endpoints inside existing Azure DNS Zones, while the Azure Private DNS Zones are located in a different subscription than the private endpoints isn't supported via the classic Microsoft Purview governance portal experience. A record can be added manually in the destination DNS Zones in the other subscription.
- If you [configure your own Event Hubs namespace](data-map-kafa-notifications) or [enable a managed Event Hubs namespace](data-map-kafa-notifications#create-a-managed-namespace) after deploying an ingestion private endpoint, you'll need to redeploy the ingestion private endpoint.
- Self-hosted integration runtime machine must be deployed in the same virtual network or a peered virtual network where Microsoft Purview account and ingestion private endpoints are deployed.
- For limitation related to Private Link service, see [Azure Private Link limits](/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#private-link-limits).
- Currently, Microsoft Purview instances using the [new Microsoft Purview portal](data-governance-purview-portal) can only use [ingestion private endpoints](data-gov-classic-private-link-end-to-end#deploy-ingestion-private-endpoint).

## Recommended troubleshooting steps

1. Once you deploy private endpoints for your Microsoft Purview account, review your Azure environment to make sure private endpoint resources are deployed successfully. Depending on your scenario, one or more of the following Azure private endpoints must be deployed in your Azure subscription:

    | Private endpoint | Private endpoint assigned to | Example |
    | --- | --- | --- |
    | Account | Microsoft Purview Account | mypurview-private-account |
    | Portal | Microsoft Purview Account | mypurview-private-portal |
    | Ingestion | Storage (Blob)\* | mypurview-ingestion-blob |
    | Ingestion | Storage (Queue)\* | mypurview-ingestion-queue |
    | Ingestion | Event Hubs Namespace\*\* | mypurview-ingestion-namespace |

    Note

    \*If your account was created before December 15, 2023, the endpoint is deployed to your managed storage account. If it was created after November 10 (or deployed using API version 2023-05-01-preview onwards), it points to the ingestion storage.

    \*\*Your account only has an associated Event Hubs namespace if it is [configured for kafka notifications](data-map-kafa-notifications) or created before December 15, 2022.
2. If portal private endpoint is deployed, make sure you also deploy account private endpoint.
3. If portal private endpoint is deployed, and public network access is set to deny in your Microsoft Purview account, make sure you launch the [classic Microsoft Purview governance portal](https://web.purview.azure.com/resource/) from internal network. 

    - To verify the correct name resolution, you can use a **NSlookup.exe** command line tool to query `web.purview.azure.com`. The result must return a private IP address that belongs to portal private endpoint.
    - To verify network connectivity, you can use any network test tools to test outbound connectivity to `web.purview.azure.com` endpoint to port **443**. The connection must be successful.
4. If Azure Private DNS Zones are used, make sure the required Azure DNS Zones are deployed and there's DNS (A) record for each private endpoint.
5. Test network connectivity and name resolution from management machine to Microsoft Purview endpoint and purview web url. If account and portal private endpoints are deployed, the endpoints must be resolved through private IP addresses.

    ```powershell
    Test-NetConnection -ComputerName web.purview.azure.com -Port 443
    ```

    Example of successful outbound connection through private IP address:

    ```
    ComputerName     : web.purview.azure.com
    RemoteAddress    : 10.9.1.7
    RemotePort       : 443
    InterfaceAlias   : Ethernet 2
    SourceAddress    : 10.9.0.10
    TcpTestSucceeded : True
    ```

    ```powershell
    Test-NetConnection -ComputerName purview-test01.purview.azure.com -Port 443
    ```

    Example of successful outbound connection through private IP address:

    ```
    ComputerName     : purview-test01.purview.azure.com
    RemoteAddress    : 10.9.1.8
    RemotePort       : 443
    InterfaceAlias   : Ethernet 2
    SourceAddress    : 10.9.0.10
    TcpTestSucceeded : True
    ```
6. If you've created your Microsoft Purview account after 18 August 2021, make sure you download and install the latest version of self-hosted integration runtime from [Microsoft download center](https://go.microsoft.com/fwlink/?linkid=2246619).
7. From self-hosted integration runtime VM, test network connectivity and name resolution to Microsoft Purview endpoint.
8. From self-hosted integration runtime, test network connectivity and name resolution to Microsoft Purview managed resources such as blob queue, and secondary resources like Event Hubs through port 443 and private IP addresses. (If either are needed, replace the managed storage account and Event Hubs namespace with corresponding resource names).

    ```powershell
    Test-NetConnection -ComputerName `scansoutdeastasiaocvseab`.blob.core.windows.net -Port 443
    ```

    Example of successful outbound connection to managed blob storage through private IP address:

    ```
    ComputerName     : scansoutdeastasiaocvseab.blob.core.windows.net
    RemoteAddress    : 10.15.1.6
    RemotePort       : 443
    InterfaceAlias   : Ethernet 2
    SourceAddress    : 10.15.0.4
    TcpTestSucceeded : True
    ```

    ```powershell
    Test-NetConnection -ComputerName `scansoutdeastasiaocvseab`.queue.core.windows.net -Port 443
    ```

    Example of successful outbound connection to managed queue storage through private IP address:

    ```
    ComputerName     : scansoutdeastasiaocvseab.blob.core.windows.net
    RemoteAddress    : 10.15.1.5
    RemotePort       : 443
    InterfaceAlias   : Ethernet 2
    SourceAddress    : 10.15.0.4
    TcpTestSucceeded : True
    ```

    ```powershell
    Test-NetConnection -ComputerName `Atlas-1225cae9-d651-4039-86a0-b43231a17a4b`.servicebus.windows.net -Port 443
    ```

    Example of successful outbound connection to Event Hubs namespace through private IP address:

    ```
    ComputerName     : Atlas-1225cae9-d651-4039-86a0-b43231a17a4b.servicebus.windows.net
    RemoteAddress    : 10.15.1.4
    RemotePort       : 443
    InterfaceAlias   : Ethernet 2
    SourceAddress    : 10.15.0.4
    TcpTestSucceeded : True
    ```
9. From the network where data source is located, test network connectivity and name resolution to Microsoft Purview endpoint and managed or configured resources endpoints.
10. If data sources are located in on-premises network, review your DNS forwarder configuration. Test name resolution from within the same network where data sources are located to self-hosted integration runtime, Microsoft Purview endpoints and managed or configured resources. It's expected to obtain a valid private IP address from DNS query for each endpoint.

    For more information, see [Virtual network workloads without custom DNS server](/en-us/azure/private-link/private-endpoint-dns#virtual-network-workloads-without-custom-dns-server) and [On-premises workloads using a DNS forwarder](/en-us/azure/private-link/private-endpoint-dns#on-premises-workloads-using-a-dns-forwarder) scenarios in [Azure Private Endpoint DNS configuration](/en-us/azure/private-link/private-endpoint-dns).
11. If management machine and self-hosted integration runtime VMs are deployed in on-premises network and you have set up DNS forwarder in your environment, verify DNS and network settings in your environment.
12. If ingestion private endpoint is used, make sure self-hosted integration runtime is registered successfully inside Microsoft Purview account and shows as running both inside the self-hosted integration runtime VM and in the [classic Microsoft Purview governance portal](https://web.purview.azure.com/resource/) .

## Common errors and messages

### Issue

You could receive the following error message when running a scan:

`Internal system error. Please contact support with correlationId:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx System Error, contact support.`

### Cause

This can be an indication of issues related to connectivity or name resolution between the VM running self-hosted integration runtime and Microsoft Purview's managed storage account or configured Event Hubs.

### Resolution

Validate if name resolution is successful between the VM running the Self-Hosted Integration Runtime and the Microsoft Purview managed blob queue or configured Event Hubs through port 443 and private IP addresses (step 8 above.)

### Issue

You could receive the following error message when running a new scan:

`message: Unable to setup config overrides for this scan. Exception:'Type=Microsoft.WindowsAzure.Storage.StorageException,Message=The remote server returned an error: (404) Not Found.,Source=Microsoft.WindowsAzure.Storage,StackTrace= at Microsoft.WindowsAzure.Storage.Core.Executor.Executor.EndExecuteAsync[T](IAsyncResult result)`

### Cause

This can be an indication of running an older version of self-hosted integration runtime. You'll need to use the self-hosted integration runtime version 5.9.7885.3 or greater.

### Resolution

Upgrade self-hosted integration runtime to 5.9.7885.3.

### Issue

Microsoft Purview account with private endpoint deployment failed with Azure Policy validation error during the deployment.

### Cause

This error suggests that there might be an existing Azure Policy Assignment on your Azure subscription that is preventing the deployment of any of the required Azure resources.

### Resolution

Review your existing Azure Policy Assignments and make sure deployment of the following Azure resources are allowed in your Azure subscription.

Note

Depending on your scenario, you may need to deploy one or more of the following Azure resource types:

- Microsoft Purview (Microsoft.Purview/Accounts)
- Private Endpoint (Microsoft.Network/privateEndpoints)
- Private DNS Zones (Microsoft.Network/privateDnsZones)
- Event Hub Name Space (Microsoft.EventHub/namespaces)
- Storage Account (Microsoft.Storage/storageAccounts)

### Issue

Not authorized to access this Microsoft Purview account. This Microsoft Purview account is behind a private endpoint. Access the account from a client in the same virtual network (virtual network) that has been configured for the Microsoft Purview account's private endpoint.

### Cause

User is trying to connect to Microsoft Purview from a public endpoint or using Microsoft Purview public endpoints where **Public network access** is set to **Deny**.

### Resolution

In this case, to open the classic Microsoft Purview governance portal, either use a machine that is deployed in the same virtual network as the classic Microsoft Purview governance portal private endpoint or use a VM that is connected to your CorpNet in which hybrid connectivity is allowed.

### Issue

You could receive the following error message when scanning a SQL server, using a self-hosted integration runtime:

`Message=This implementation is not part of the Windows Platform FIPS validated cryptographic algorithms`

### Cause

Self-hosted integration runtime machine has enabled the FIPS mode. Federal Information Processing Standards (FIPS) defines a certain set of cryptographic algorithms that are allowed to be used. When FIPS mode is enabled on the machine, some cryptographic classes that the invoked processes depend on are blocked in some scenarios.

### Resolution

Disable FIPS mode on self-hosted integration server.