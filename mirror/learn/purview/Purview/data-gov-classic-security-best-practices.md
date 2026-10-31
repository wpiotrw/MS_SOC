---
layout: Conceptual
title: Microsoft Purview classic data governance best practices for security | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-security-best-practices
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-05-20T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Discover best practices for common security requirements for classic Microsoft Purview data governance solutions..
locale: en-us
document_id: 4a400931-20ff-c04c-75d3-b9159a48800c
document_version_independent_id: 4a400931-20ff-c04c-75d3-b9159a48800c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-security-best-practices.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-security-best-practices
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-security-best-practices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 00169288-49e4-084a-3e81-74bf6a8a1e7a
---

# Microsoft Purview classic data governance best practices for security | Microsoft Learn

This article provides best practices for common security requirements for classic Microsoft Purview governance solutions. The security strategy described follows the layered defense-in-depth approach.

Note

These best practices cover security for Microsoft Purview data governance solutions. Learn more about [Microsoft Purview in general](/en-us/purview/purview), or about [risk and compliance solutions](purview-compliance) specifically.

![Screenshot that shows defense in depth in Microsoft Purview.](media/concept-best-practices/security-defense-in-depth.png)

Before applying these recommendations to your environment, you should consult your security team as some may not be applicable to your security requirements.

## Network security

You can enable the following network security capabilities for the Microsoft Purview data map:

- Enable [end-to-end network isolation](data-gov-classic-private-link-end-to-end) using Private Link Service.
- Use [Microsoft Purview Firewall](data-gov-classic-private-link-end-to-end#firewalls-to-restrict-public-access) to disable Public access.
- Deploy Network Security Group (NSG) rules for subnets where Azure data sources private endpoints, Microsoft Purview private endpoints and self-hosted runtime VMs are deployed.
- Implement Microsoft Purview with private endpoints managed by a Network Virtual Appliance, such as [Azure Firewall](/en-us/azure/firewall/overview) for network inspection and network filtering.

[![Screenshot that shows Microsoft Purview account in a network.](media/concept-best-practices/security-networking.png)](media/concept-best-practices/security-networking.png#lightbox)

For more information, see [Best practices related to connectivity to Azure PaaS Services](/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/connectivity-to-azure-paas-services).

### Deploy private endpoints for Microsoft Purview accounts

If you need to use Microsoft Purview from inside your private network, it's recommended to use Azure Private Link Service with your Microsoft Purview accounts for partial or [end-to-end isolation](data-gov-classic-private-link-end-to-end) to connect to Microsoft Purview governance portal, access Microsoft Purview endpoints and to scan data sources.

The Microsoft Purview *account* private endpoint is used to add another layer of security, so only client calls that are originated from within the virtual network are allowed to access the Microsoft Purview account. This private endpoint is also a prerequisite for the portal private endpoint.

The Microsoft Purview *portal* private endpoint is required to enable connectivity to Microsoft Purview governance portal using a private network.

Microsoft Purview can scan data sources in Azure or an on-premises environment by using ingestion private endpoints.

For more information, see [Microsoft Purview network architecture and best practices](concept-best-practices-network).

### Block public access using Microsoft Purview firewall

You can disable Microsoft Purview Public access to cut off access to the Microsoft Purview account completely from the public internet. In this case, you should consider the following requirements:

- Microsoft Purview must be deployed based on [end-to-end network isolation scenario](data-gov-classic-private-link-end-to-end).
- To access Microsoft Purview governance portal and Microsoft Purview endpoints, you need to use a management machine that is connected to private network to access Microsoft Purview through private network.
- Review [known limitations](data-gov-classic-private-link-troubleshoot).

For more information, see [Firewalls to restrict public access](data-gov-classic-private-link-end-to-end#firewalls-to-restrict-public-access).

### Use Network Security Groups

You can use an Azure network security group to filter network traffic to and from Azure resources in an Azure virtual network. A network security group contains [security rules](/en-us/azure/virtual-network/network-security-groups-overview#security-rules) that allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources. For each rule, you can specify source and destination, port, and protocol.

Network Security Groups can be applied to network interface or Azure virtual networks subnets, where Microsoft Purview private endpoints, self-hosted integration runtime VMs and Azure data sources are deployed.

For more information, see [apply NSG rules for private endpoints](/en-us/azure/private-link/disable-private-endpoint-network-policy).

The following NSG rules are required on **data sources** for Microsoft Purview scanning:

| Direction | Source | Source port range | Destination | Destination port | Protocol | Action |
| --- | --- | --- | --- | --- | --- | --- |
| Inbound | Self-hosted integration runtime VMs' private IP addresses or subnets | \* | Data Sources private IP addresses or Subnets | 443 | Any | Allow |

The following NSG rules are required on from the **management machines** to access Microsoft Purview governance portal:

| Direction | Source | Source port range | Destination | Destination port | Protocol | Action |
| --- | --- | --- | --- | --- | --- | --- |
| Outbound | Management machines' private IP addresses or subnets | \* | Microsoft Purview account and portal private endpoint IP addresses or subnets | 443 | Any | Allow |
| Outbound | Management machines' private IP addresses or subnets | \* | Service tag: `AzureCloud` | 443 | Any | Allow |

The following NSG rules are required on **self-hosted integration runtime VMs** for Microsoft Purview scanning and metadata ingestion:

Important

Consider adding additional rules with relevant Service Tags, based on your data source types.

| Direction | Source | Source port range | Destination | Destination port | Protocol | Action |
| --- | --- | --- | --- | --- | --- | --- |
| Outbound | Self-hosted integration runtime VMs' private IP addresses or subnets | \* | Data Sources private IP addresses or subnets | 443 | Any | Allow |
| Outbound | Self-hosted integration runtime VMs' private IP addresses or subnets | \* | Microsoft Purview account and ingestion private endpoint IP addresses or Subnets | 443 | Any | Allow |
| Outbound | Self-hosted integration runtime VMs' private IP addresses or subnets | \* | Service tag: `Servicebus` | 443 | Any | Allow |
| Outbound | Self-hosted integration runtime VMs' private IP addresses or subnets | \* | Service tag: `Storage` | 443 | Any | Allow |
| Outbound | Self-hosted integration runtime VMs' private IP addresses or subnets | \* | Service tag: `AzureActiveDirectory` | 443 | Any | Allow |
| Outbound | Self-hosted integration runtime VMs' private IP addresses or subnets | \* | Service tag: `DataFactory` | 443 | Any | Allow |
| Outbound | Self-hosted integration runtime VMs' private IP addresses or subnets | \* | Service tag: `KeyVault` | 443 | Any | Allow |

The following NSG rules are required on for **Microsoft Purview account, portal and ingestion private endpoints**:

| Direction | Source | Source port range | Destination | Destination port | Protocol | Action |
| --- | --- | --- | --- | --- | --- | --- |
| Inbound | Self-hosted integration runtime VMs' private IP addresses or subnets | \* | Microsoft Purview account and ingestion private endpoint IP addresses or subnets | 443 | Any | Allow |
| Inbound | Management machines' private IP addresses or subnets | \* | Microsoft Purview account and ingestion private endpoint IP addresses or subnets | 443 | Any | Allow |

For more information, see [Self-hosted integration runtime networking requirements](data-map-integration-runtime-self-hosted#networking-requirements).

## Access management

Identity and Access Management provides the basis of a large percentage of security assurance. It enables access based on identity authentication and authorization controls in cloud services. These controls protect data and resources and decide which requests should be permitted.

Related to roles and access management in Microsoft Purview, you can apply the following security best practices:

- Define roles and responsibilities to manage Microsoft Purview in control plane and data plane:
    - Define roles and tasks required to deploy and manage Microsoft Purview inside an Azure subscription.
    - Define roles and task needed to perform data management and governance using Microsoft Purview.
- Assign roles to Microsoft Entra groups instead of assigning roles to individual users.
- Use Azure [Active Directory Entitlement Management](/en-us/azure/active-directory/governance/entitlement-management-overview) to map user access to Microsoft Entra groups using Access Packages.
- Enforce multifactor authentication for Microsoft Purview users, especially, for users with privileged roles such as collection admins, data source admins or data curators.

### Manage a Microsoft Purview account in control plane and data plane

Control plane refers to all operations related to Azure deployment and management of Microsoft Purview inside Azure Resource Manager.

Data plane refers to all operations, related to interacting with Microsoft Purview inside Data Map and Unified Catalog.

You can assign control plane and data plane roles to users, security groups and service principals from your Microsoft Entra tenant that is associated to Microsoft Purview instance's Azure subscription.

Examples of control plane operations and data plane operations:

| Task | Scope | Recommended role | What roles to use? |
| --- | --- | --- | --- |
| Deploy a Microsoft Purview account | Control plane | Azure subscription owner or contributor | Azure RBAC roles |
| Set up a Private Endpoint for Microsoft Purview | Control plane | Contributor | Azure RBAC roles |
| Delete a Microsoft Purview account | Control plane | Contributor | Azure RBAC roles |
| Add or manage a [self-hosted integration runtime (SHIR)](data-map-integration-runtime-self-hosted) | Control plane | Data source administrator | Microsoft Purview roles |
| View Microsoft Purview metrics to get current capacity units | Control plane | Reader | Azure RBAC roles |
| Create a collection | Data plane | Collection Admin | Microsoft Purview roles |
| Register a data source | Data plane | Collection Admin | Microsoft Purview roles |
| Scan a SQL Server | Data plane | Data source admin and data reader or data curator | Microsoft Purview roles |
| Search inside Microsoft Purview Unified Catalog | Data plane | Data source admin and data reader or data curator | Microsoft Purview roles |

Microsoft Purview plane roles are defined and managed inside Microsoft Purview instance in Microsoft Purview collections. For more information, see [Access control in Microsoft Purview](data-gov-classic-permissions#roles).

Follow [Microsoft Purview Data Governance roles](data-governance-roles-permissions) for guidance on users' roles and permissions to manage in Unified Catalog.

Follow [Azure role-based access recommendations](/en-us/azure/role-based-access-control/best-practices) for Azure control plane tasks.

### Authentication and authorization

To gain access to Microsoft Purview, users must be authenticated and authorized. Authentication is the process of proving the user is who they claim to be. Authorization refers to controlling access inside Microsoft Purview assigned on collections.

We use Microsoft Entra ID to provide authentication and authorization mechanisms for Microsoft Purview inside Collections. You can assign Microsoft Purview roles to the following security principals from your Microsoft Entra tenant that is associated with Azure subscription where your Microsoft Purview instance is hosted:

- Users and guest users (if they're already added into your Microsoft Entra tenant)
- Security groups
- Managed Identities
- Service Principals

Microsoft Purview fine-grained roles can be assigned to a flexible Collections hierarchy inside the Microsoft Purview instance.

[![Screenshot that shows Microsoft Purview access management.](media/concept-best-practices/security-access-management.png)](media/concept-best-practices/security-access-management.png#lightbox)

### Define Least Privilege model

As a general rule, restrict access based on the [need to know](https://en.wikipedia.org/wiki/Need_to_know) and [least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) security principles is imperative for organizations that want to enforce security policies for data access.

In Microsoft Purview, data sources, assets and scans can be organized using [Microsoft Purview Collections](data-map-collections-create-classic). Collections are hierarchical grouping of metadata in Microsoft Purview, but at the same time they provide a mechanism to manage access across Microsoft Purview. Roles in Microsoft Purview can be assigned to a collection based on your collection's hierarchy.

Use [Microsoft Purview collections](data-gov-best-practices-domains-collections#define-a-hierarchy) to implement your organization's metadata hierarchy for centralized or delegated management and governance hierarchy based on least privileged model.

Follow least privilege access model when assigning roles inside Microsoft Purview collections by segregating duties within your team and grant only the amount of access to users that they need to perform their jobs.

For more information how to assign least privilege access model in Microsoft Purview, based on Microsoft Purview collection hierarchy, see [Access control in Microsoft Purview](data-gov-classic-permissions#assign-permissions-to-your-users).

### Lower exposure of privileged accounts

Securing privileged access is a critical first step to protecting business assets. Minimizing the number of people who have access to secure information or resources, reduces the chance of a malicious user getting access, or an authorized user inadvertently affecting a sensitive resource.

Reduce the number of users with write access inside your Microsoft Purview instance. Keep the number of collection admins and data curator roles minimum at root collection.

### Use multifactor authentication and conditional access

[Microsoft Entra multifactor authentication](/en-us/azure/active-directory/authentication/concept-mfa-howitworks) provides another layer of security and authentication. For more security, we recommend enforcing [conditional access policies](/en-us/azure/active-directory/conditional-access/overview) for all privileged accounts.

By using Microsoft Entra Conditional Access policies, apply Microsoft Entra multifactor authentication at sign-in for all individual users who are assigned to Microsoft Purview roles with modify access inside your Microsoft Purview instances: Collection Admin, Data Source Admin, Data Curator.

Enable multifactor authentication for your admin accounts and ensure that admin account users have registered for MFA.

You can define your Conditional Access policies by selecting Microsoft Purview as a Cloud App.

### Prevent accidental deletion of Microsoft Purview accounts

In Azure, you can apply [resource locks](/en-us/azure/azure-resource-manager/management/lock-resources) to an Azure subscription, a resource group, or a resource to prevent accidental deletion or modification for critical resources.

Enable Azure resource lock for your Microsoft Purview accounts to prevent accidental deletion of Microsoft Purview instances in your Azure subscriptions.

Adding a `CanNotDelete` or `ReadOnly` lock to Microsoft Purview account doesn't prevent deletion or modification operations inside Microsoft Purview data plane, however, it prevents any operations in control plane, such as deleting the Microsoft Purview account, deploying a private endpoint or configuration of diagnostic settings.

For more information, see [Understand scope of locks](/en-us/azure/azure-resource-manager/management/lock-resources#understand-scope-of-locks).

Resource locks can be assigned to Microsoft Purview resource groups or resources, however, you can't assign an Azure resource lock to Microsoft Purview Managed resources or managed Resource Group.

### Implement a break glass strategy

Plan for a break glass strategy for your Microsoft Entra tenant, Azure subscription and Microsoft Purview accounts to prevent tenant-wide account lockout.

For more information about Microsoft Entra ID and Azure emergency access planning, see [Manage emergency access accounts in Microsoft Entra ID](/en-us/azure/active-directory/roles/security-emergency-access).

For more information about Microsoft Purview break glass strategy, see [Microsoft Purview collections best practices and design recommendations](data-gov-best-practices-domains-collections#design-recommendations).

## Threat protection and preventing data exfiltration

Microsoft Purview provides rich insights into the sensitivity of your data, which makes it valuable to security teams using Microsoft Defender for Cloud to manage the organization's security posture and protect against threats to their workloads. Data resources remain a popular target for malicious actors, making it crucial for security teams to identify, prioritize, and secure sensitive data resources across their cloud environments. To address this challenge, we're announcing the integration between Microsoft Defender for Cloud and Microsoft Purview in public preview.

### Integrate with Microsoft 365 and Microsoft Defender for Cloud

Often, one of the biggest challenges for security organization in a company is to identify and protect assets based on their criticality and sensitivity. Microsoft recently [announced integration between Microsoft Purview and Microsoft Defender for Cloud in Public Preview](https://techcommunity.microsoft.com/t5/azure-purview-blog/what-s-new-in-azure-purview-at-microsoft-ignite-2021/ba-p/2915954) to help overcome these challenges.

If you've extended your Microsoft 365 sensitivity labels for assets and database columns in Microsoft Purview, you can keep track of highly valuable assets using Microsoft Defender for Cloud from inventory, alerts and recommendations based on assets detected sensitivity labels.

- For recommendations, we've provided **security controls** to help you understand how important each recommendation is to your overall security posture. Microsoft Defender for Cloud includes a **secure score** value for each control to help you prioritize your security work. Learn more in [Security controls and their recommendations](/en-us/azure/defender-for-cloud/secure-score-security-controls#security-controls-and-their-recommendations).
- For alerts, we've assigned **severity labels** to each alert to help you prioritize the order in which you attend to each alert. Learn more in [How are alerts classified?](/en-us/azure/defender-for-cloud/alerts-overview#how-are-alerts-classified).

For more information, see [Integrate Microsoft Purview with Azure security products](how-to-integrate-with-azure-security-products).

## Information Protection

### Secure metadata extraction and storage

Microsoft Purview is a data governance solution in cloud. You can register and scan different data sources from various data systems from your on-premises, Azure, or multicloud environments into Microsoft Purview. While data source is registered and scanned in Microsoft Purview, the actual data and data sources stay in their original locations, only metadata is extracted from data sources and stored in Microsoft Purview Data Map, which means you don't need to move data out of the region or their original location to extract the metadata into Microsoft Purview.

If your account was created **before** December 15, 2023, then your account was deployed with a managed resource group and an Azure Storage account was deployed in that group. These resources are consumed by Microsoft Purview and can't be accessed by any other users or principals. An Azure role-based access control (RBAC) deny assignment is added automatically to this resource group when the Microsoft Purview account was deployed, and that prevents access by other users or any CRUD operations that aren't initiated by Microsoft Purview.

Accounts deployed **after** December 15, 2023 (or deployed using API version 2023-05-01-preview onwards) use an ingestion storage account which is deployed in internal Microsoft Azure subscriptions. Since these resources are not on the Microsoft Purview's Azure subscription, they can't be accessed by any other users or principals, except the Microsoft Purview account.

(If you've deployed your accounts using the API, accounts deployed using the API version 2023-05-01-preview onwards will use an ingestion storage account deployed on internal Microsoft Azure subscriptions, instead of a managed storage account deployed on your Azure subscription.)

### Where is metadata stored?

Microsoft Purview extracts only the metadata from different data source systems into [Microsoft Purview Data Map](data-map) during the scanning process.

You can deploy a Microsoft Purview account inside your Azure subscription in any [supported Azure regions](https://azure.microsoft.com/global-infrastructure/services/?products=purview&amp;regions=all).

All metadata is stored inside Data Map inside your Microsoft Purview instance. This means the metadata is stored in the same region as your Microsoft Purview instance.

### How metadata is extracted from data sources?

Microsoft Purview allows you to use any of the following options to extract metadata from data sources:

- **Azure runtime**. Metadata data is extracted and processed inside the same region as your data sources.

    1. A manual or automatic scan is initiated from the Microsoft Purview Data Map through the Azure integration runtime.
    2. The Azure integration runtime connects to the data source to extract metadata.
    3. Metadata is queued in Microsoft Purview managed or ingestion storage and stored in Azure Blob Storage.
    4. Metadata is sent to the Microsoft Purview Data Map.
- **Self-hosted integration runtime**. Metadata is extracted and processed by self-hosted integration runtime inside self-hosted integration runtime VMs' memory before they're sent to Microsoft Purview Data Map. In this case, customers have to deploy and manage one or more self-hosted integration runtime Windows-based virtual machines inside their Azure subscriptions or on-premises environments. Scanning on-premises and VM-based data sources always requires using a self-hosted integration runtime. The Azure integration runtime isn't supported for these data sources. The following steps show the communication flow at a high level when you're using a self-hosted integration runtime to scan a data source.

    1. A manual or automatic scan is triggered. Microsoft Purview connects to Azure Key Vault to retrieve the credential to access a data source.
    2. The scan is initiated from the Microsoft Purview Data Map through a self-hosted integration runtime.
    3. The self-hosted integration runtime service from the VM connects to the data source to extract metadata.
    4. Metadata is processed in VM memory for the self-hosted integration runtime. Metadata is queued in Microsoft Purview ingestion storage and then stored in Azure Blob Storage.
    5. Metadata is sent to the Microsoft Purview Data Map.

    If you need to extract metadata from data sources with sensitive data that can't leave the boundary of your on-premises network, it's highly recommended to deploy the self-hosted integration runtime VM inside your corporate network, where data sources are located, to extract and process metadata in on-premises, and send only metadata to Microsoft Purview.

    1. A manual or automatic scan is triggered. Microsoft Purview connects to Azure Key Vault to retrieve the credential to access a data source.
    2. The scan is initiated through the on-premises self-hosted integration runtime.
    3. The self-hosted integration runtime service from the VM connects to the data source to extract metadata.
    4. Metadata is processed in VM memory for the self-hosted integration runtime. Metadata is queued in Microsoft Purview ingestion storage and then stored in Azure Blob Storage. Actual data never leaves the boundary of your network.
    5. Metadata is sent to the Microsoft Purview Data Map.

### Information protection and encryption

Azure offers many mechanisms for keeping data private in rest and as it moves from one location to another. For Microsoft Purview, data is encrypted at rest using Microsoft-managed keys and when data is in transit, using Transport Layer Security (TLS) v1.2 or greater.

#### Transport Layer Security (Encryption-in-transit)

Data in transit (also known as data in motion) is encrypted in Microsoft Purview.

To add another layer of security in addition to access controls, Microsoft Purview secures customer data by encrypting data in motion with Transport Layer Security (TLS) and protect data in transit against 'out of band' attacks (such as traffic capture). It uses encryption to make sure attackers can't easily read or modify the data.

Microsoft Purview supports data encryption in transit with Transport Layer Security (TLS) v1.2 or greater.

For more information, see, [Encrypt sensitive information in transit](/en-us/security/benchmark/azure/baselines/purview-security-baseline#dp-4-encrypt-sensitive-information-in-transit).

#### Transparent data encryption (Encryption-at-rest)

Data at rest includes information that resides in persistent storage on physical media, in any digital format. The media can include files on magnetic or optical media, archived data, and data backups inside Azure regions.

To add another layer of security in addition to access controls, Microsoft Purview encrypts data at rest to protect against 'out of band' attacks (such as accessing underlying storage). It uses encryption with Microsoft-managed keys. This practice helps make sure attackers can't easily read or modify the data.

For more information, see [Encrypt sensitive data at rest](/en-us/security/benchmark/azure/baselines/purview-security-baseline#dp-5-encrypt-sensitive-data-at-rest).

### Optional Event Hubs namespace configuration

Each Microsoft Purview account can configure Event Hubs that are accessible via their Atlas Kafka endpoint. This can be enabled at creation under *Configuration*, or from the Azure portal under *Kafka configuration*. It's recommended to only enable optional managed event hub if it's used to distribute events into or outside of Microsoft Purview account Data Map. To remove this information distribution point, either don't configure these endpoints, or remove them.

To remove configured Event Hubs namespaces, you can follow these steps:

1. Search for and open your Microsoft Purview account in the [Azure portal](https://portal.azure.com).
2. Select **Kafka configuration** under settings on your Microsoft Purview account page in the Azure portal.
3. Select the Event Hubs you want to disable. (Hook hubs send messages to Microsoft Purview. Notification hubs receive notifications.)
4. Select **Remove** to save the choice and begin the disablement process. This can take several minutes to complete. ![Screenshot showing the Kafka configuration page of the Microsoft Purview account page in the Azure portal with the remove button highlighted.](media/concept-best-practices/select-remove.png)

Note

If you have an ingestion private endpoint when you disable this Event Hubs namespace, after disabling the ingestion private endpoint may show as disconnected.

For more information about configuring these Event Hubs namespaces, see: [Configure Event Hubs for Atlas Kafka topics](data-map-kafa-notifications)

## Credential management

To extract metadata from a data source system into Microsoft Purview Data Map, it's required to register and scan the data source systems in Microsoft Purview Data Map. To automate this process, we have made available [connectors](data-map-data-sources) for different data source systems in Microsoft Purview to simplify the registration and scanning process.

To connect to a data source Microsoft Purview requires a credential with read-only access to the data source system.

It's recommended prioritizing the use of the following credential options for scanning, when possible:

1. Microsoft Purview Managed Identity
2. User Assigned Managed Identity
3. Service Principals
4. Other options such as Account key, SQL Authentication, etc.

If you use any options rather than managed identities, all credentials must be stored and protected inside an [Azure key vault](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account). Microsoft Purview requires get/list access to secret on the Azure Key Vault resource.

As a general rule, you can use the following options to set up integration runtime, and credentials to scan data source systems:

| Scenario | Runtime option | Supported Credentials |
| --- | --- | --- |
| Data source is an Azure Platform as a Service, such as Azure Data Lake Storage Gen 2 or Azure SQL inside public network | Option 1: Azure Runtime | Microsoft Purview Managed Identity, Service Principal or Access Key / SQL Authentication (depending on Azure data source type) |
| Data source is an Azure Platform as a Service, such as Azure Data Lake Storage Gen 2 or Azure SQL inside public network | Option 2: Self-hosted integration runtime | Service Principal or Access Key / SQL Authentication (depending on Azure data source type) |
| Data source is an Azure Platform as a Service, such as Azure Data Lake Storage Gen 2 or Azure SQL inside private network using Azure Private Link Service | Self-hosted integration runtime | Service Principal or Access Key / SQL Authentication (depending on Azure data source type) |
| Data source is inside an Azure IaaS VM such as SQL Server | Self-hosted integration runtime deployed in Azure | SQL Authentication or Basic Authentication (depending on Azure data source type) |
| Data source is inside an on-premises system such as SQL Server or Oracle | Self-hosted integration runtime deployed in Azure or in the on-premises network | SQL Authentication or Basic Authentication (depending on Azure data source type) |
| Multicloud | Azure runtime or self-hosted integration runtime based on data source types | Supported credential options vary based on data sources types |
| Power BI tenant | Azure Runtime | Microsoft Purview Managed Identity |

Use [this guide](data-map-data-sources) to read more about each source and their supported authentication options.

## Other recommendations

### Apply security best practices for Self-hosted runtime VMs

Consider securing the deployment and management of self-hosted integration runtime VMs in Azure or your on-premises environment, if self-hosted integration runtime is used to scan data sources in Microsoft Purview.

For self-hosted integration runtime VMs deployed as virtual machines in Azure, follow [security best practices recommendations for Windows virtual machines](/en-us/azure/virtual-machines/security-recommendations).

- Lock down inbound traffic to your VMs using Network Security Groups and [Azure Defender access Just-in-Time](/en-us/azure/defender-for-cloud/just-in-time-access-usage).
- Install antivirus or antimalware.
- Deploy Azure Defender to get insights around any potential anomaly on the VMs.
- Limit the amount of software in the self-hosted integration runtime VMs. Although it isn't a mandatory requirement to have a dedicated VM for a self-hosted runtime for Microsoft Purview, we highly suggest using dedicated VMs especially for production environments.
- Monitor the VMs using [Azure Monitor for VMs](/en-us/azure/azure-monitor/vm/vminsights-overview). By using Log analytics agent, you can capture content such as performance metrics to adjust required capacity for your VMs.
- By integrating virtual machines with Microsoft Defender for Cloud, you can you prevent, detect, and respond to threats.
- Keep your machines current. You can enable Automatic Windows Update or use [Update Management in Azure Automation](/en-us/azure/automation/update-management/overview) to manage operating system level updates for the OS.
- Use multiple machines for greater resilience and availability. You can deploy and register multiple self-hosted integration runtimes to distribute the scans across multiple self-hosted integration runtime machines or deploy the self-hosted integration runtime on a Virtual Machine Scale Set for higher redundancy and scalability.
- Optionally, you can plan to enable Azure backup from your self-hosted integration runtime VMs to increase the recovery time of a self-hosted integration runtime VM if there's a VM level disaster.