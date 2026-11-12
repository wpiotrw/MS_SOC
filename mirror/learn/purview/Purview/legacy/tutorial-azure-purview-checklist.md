---
layout: Conceptual
title: Prerequisites to successfully deploy a Microsoft Purview (formerly Azure Purview) account | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/tutorial-azure-purview-checklist
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This tutorial lists a prerequisite checklist to deploy a Microsoft Purview (formerly Azure Purview) account.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: zeinam
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: tutorial
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 772703a0-cda9-56ac-90a2-80b398ea956f
document_version_independent_id: 772703a0-cda9-56ac-90a2-80b398ea956f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/tutorial-azure-purview-checklist.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/tutorial-azure-purview-checklist
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/tutorial-azure-purview-checklist.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: d9237af6-171d-2158-5a6a-d0ab250cb12e
---

# Prerequisites to successfully deploy a Microsoft Purview (formerly Azure Purview) account | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Tip

Microsoft Purview has a new experience! If you're a new Microsoft Purview customer, or if you want more information, see our [article on the new portal](../purview-portal) or the article about our new [data governance experience](../unified-catalog).

If you're planning on deploying Microsoft Purview governance solutions in your organization, use [our new portal](../purview-portal) and check out our [data governance quickstart](../data-governance-get-started) and [best practices](../unified-catalog-plan).

This article lists prerequisites that help you get started quickly on planning and deployment for your Microsoft Purview (formerly Azure Purview) account.

If you're creating a plan to deploy Microsoft Purview, and also want to consider best practices as you develop your deployment strategy, then use [our deployment best practices guide](../deployment-best-practices) to get started.

If you're looking for a strictly technical deployment guide, this deployment checklist is for you.

| No. | Prerequisite / Action | Required permission | More guidance and recommendations |
| --- | --- | --- | --- |
| 1 | Microsoft Entra tenant | N/A | An [Microsoft Entra tenant](/en-us/azure/active-directory/fundamentals/active-directory-access-create-new-tenant) should be associated with your subscription. <br>- *Information Protection Administrator* role is required, if you plan to [extend Microsoft 365 Sensitivity Labels to the Microsoft Purview Data Map for files and db columns](../data-map-sensitivity-labels)<br>- *Power BI Administrator* role is required, if you're planning to [scan Power BI tenants](../register-scan-power-bi-tenant). |
| 2 | An active Azure Subscription | *Subscription Owner* | An Azure subscription is needed to deploy Microsoft Purview and its managed resources. If you don't have an Azure subscription, create a [free subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin. |
| 3 | Define whether you plan to deploy a Microsoft Purview with a managed event hub | N/A | You can choose to deploy configure an existing Event Hubs namespace during Microsoft Purview account creation, see [Microsoft Purview account creation](../create-microsoft-purview-portal). With this managed namespace you can publish messages to the event hub kafka topic ATLAS\_HOOK and Microsoft Purview will consume and process it. Microsoft Purview will notify entity changes to the event hub kafka topic ATLAS\_ENTITIES and user can consume and process it. You can enable or disable this feature any time after account creation. |
| 4 | Register the following resource providers: <br>- Microsoft.Storage<br>- Microsoft.EventHub (optional)<br>- Microsoft.Purview | *Subscription Owner* or custom role to register Azure resource providers (*/register/action*) | [Register required Azure Resource Providers](/en-us/azure/azure-resource-manager/management/resource-providers-and-types) in the Azure Subscription that is designated for Microsoft Purview Account. Review [Azure resource provider operations](/en-us/azure/role-based-access-control/resource-provider-operations). |
| 5 | Update Azure Policy to allow deployment of the following resources in your Azure subscription: <br>- Microsoft Purview<br>- Azure Storage | *Subscription Owner* | Use this step if an existing Azure Policy prevents deploying such Azure resources. If a blocking policy exists and needs to remain in place, follow our [Microsoft Purview exception tag guide](../data-gov-azure-policy-exclusion) and follow the steps to create an exception for Microsoft Purview accounts. |
| 6 | Define your network security requirements. | Network and Security architects. | - Review [Microsoft Purview network architecture and best practices](../concept-best-practices-network) to define what scenario is more relevant to your network requirements.<br>- If private network is needed, use [Microsoft Purview Managed IR](../data-governance-private-endpoints-managed-virtual-network) to scan Azure data sources when possible to reduce complexity and administrative overhead. |
| 7 | An Azure Virtual Network and Subnets for Microsoft Purview private endpoints. | *Network Contributor* to create or update Azure virtual network. | Use this step if you're planning to deploy [private endpoint connectivity with Microsoft Purview](../data-gov-classic-private-link): <br>- Private endpoints for **Ingestion**.<br>- Private endpoint for Microsoft Purview **Account**.<br>- Private endpoint for Microsoft Purview **Portal**.<br><br> Deploy [Azure Virtual Network](/en-us/azure/virtual-network/quick-create-portal) if you need one. |
| 8 | Deploy private endpoint for Azure data sources. | *Network Contributor* to set up private endpoints for each data source. | Perform this step, if you're planning to use [Private Endpoint for Ingestion](../data-gov-classic-private-link-end-to-end). |
| 9 | Define whether to deploy new or use existing Azure Private DNS Zones. | Required [Azure Private DNS Zones](../data-gov-classic-private-link-name-resolution) can be created automatically during Purview Account deployment using Subscription Owner / Contributor role | Use this step if you're planning to use Private Endpoint connectivity with Microsoft Purview. Required DNS Zones for Private Endpoint: <br>- privatelink.purview.azure.com<br>- privatelink.purview-service.microsoft.com<br>- privatelink.purviewstudio.azure.com<br>- privatelink.blob.core.windows.net<br>- privatelink.queue.core.windows.net<br>- privatelink.servicebus.windows.net |
| 10 | A management machine in your CorpNet or inside Azure virtual network to launch the Microsoft Purview governance portal. | N/A | Use this step if you're planning to set **Allow Public Network** to **deny** on your Microsoft Purview Account. |
| 11 | Deploy a Microsoft Purview Account | Subscription Owner / Contributor | Purview account is deployed with one Capacity Unit and will scale up based [on demand](../data-map). |
| 12 | Deploy a Managed Integration Runtime and Managed private endpoints for Azure data sources. | *Data source admin* to set up Managed virtual network inside Microsoft Purview. *Network Contributor* to approve managed private endpoint for each Azure data source. | Perform this step if you're planning to use [Managed virtual network](../data-governance-private-endpoints-managed-virtual-network). within your Microsoft Purview account for scanning purposes. |
| 13 | Deploy Self-hosted integration runtime VMs inside your network. | Azure: *Virtual Machine Contributor* On-premises: Application owner | Use this step if you're planning to perform any scans using [Self-hosted Integration Runtime](../data-map-integration-runtime-self-hosted). |
| 14 | Create a Self-hosted integration runtime inside Microsoft Purview. | Data curator  VM Administrator or application owner | Use this step if you're planning to use Self-hosted Integration Runtime instead of Managed Integration Runtime or Azure Integration Runtime. [download](https://www.microsoft.com/en-us/download/details.aspx?id=105539) |
| 15 | Register your Self-hosted integration runtime | Virtual machine administrator | Use this step if you have **on-premises** or **VM-based data sources** (for example, SQL Server).  Use this step are using **Private Endpoint** to scan to **any** data sources. |
| 16 | Grant Azure RBAC **Reader** role to **Microsoft Purview MSI** at data sources' Subscriptions | *Subscription owner* or *User Access Administrator* | Use this step if you're planning to register [multiple](../register-scan-azure-multiple-sources) or **any** of the following data sources: <br>- [Azure Blob Storage](../register-scan-azure-blob-storage-source)<br>- [Azure Data Lake Storage Gen1](../register-scan-adls-gen1)<br>- [Azure Data Lake Storage Gen2](../register-scan-adls-gen2)<br>- [Azure SQL Database](../register-scan-azure-sql-database)<br>- [Azure SQL Managed Instance](../register-scan-azure-sql-managed-instance)<br>- [Azure Synapse Analytics](../register-scan-synapse-workspace) |
| 17 | Grant Azure RBAC **Storage Blob Data Reader** role to **Microsoft Purview MSI** at data sources Subscriptions. | *Subscription owner* or *User Access Administrator* | **Skip** this step if you're using Private Endpoint to connect to data sources. Use this step if you have these data sources:<br>- [Azure Blob Storage](../register-scan-azure-blob-storage-source#using-a-system-or-user-assigned-managed-identity-for-scanning)<br>- [Azure Data Lake Storage Gen2](../register-scan-adls-gen2#using-a-system-or-user-assigned-managed-identity-for-scanning) |
| 18 | Enable network connectivity to allow AzureServices to access data sources:  for example, Enable "**Allow trusted Microsoft services to access this storage account**". | *Owner* or *Contributor* at Data source | Use this step if **Service Endpoint** is used in your data sources. (Don't use this step if Private Endpoint is used) |
| 19 | Enable **Microsoft Entra authentication** on **Azure SQL Servers**, **Azure SQL Managed Instance** and **Azure Synapse Analytics** | Azure SQL Server Contributor | Use this step if you have **Azure SQL DB** or **Azure SQL Managed Instance** or **Azure Synapse Analytics** as data source. |
| 20 | Grant **Microsoft Purview MSI** account with **db\_datareader** role to Azure SQL databases and Azure SQL Managed Instance databases | Azure SQL Administrator | Use this step if you have **Azure SQL DB** or **Azure SQL Managed Instance** as data source. **Skip** this step if you're using **Private Endpoint** to connect to data sources. |
| 21 | Grant Azure RBAC **Storage Blob Data Reader** to **Synapse SQL Server** for staging Storage Accounts | Owner or User Access Administrator at data source | Use this step if you have **Azure Synapse Analytics** as data sources. **Skip** this step if you're using Private Endpoint to connect to data sources. |
| 22 | Grant Azure RBAC **Reader** role to **Microsoft Purview MSI** at **Synapse workspace** resources | Owner or User Access Administrator at data source | Use this step if you have **Azure Synapse Analytics** as data sources. **Skip** this step if you're using Private Endpoint to connect to data sources. |
| 23 | Grant Azure **Purview MSI account** with **db\_datareader** role | Azure SQL Administrator | Use this step if you have **Azure Synapse Analytics (Dedicated SQL databases)**. **Skip** this step if you're using **Private Endpoint** to connect to data sources. |
| 24 | Grant **Microsoft Purview MSI** account with **sysadmin** role | Azure SQL Administrator | Use this step if you have Azure Synapse Analytics (Serverless SQL databases). **Skip** this step if you're using **Private Endpoint** to connect to data sources. |
| 25 | Create an app registration or service principal inside your Microsoft Entra tenant | Microsoft Entra ID *Application Administrator* | Use this step if you're planning to perform a scan on a data source using Delegated Author [Service Principal](../data-map-service-principal). |
| 26 | Create an **Azure Key Vault** and a **Secret** to save data source credentials or service principal secret. | *Contributor* or *Key Vault Administrator* | Use this step if you have **on-premises** or **VM-based data sources** (for example, SQL Server).  Use this step are using **ingestion private endpoints** to scan a data source. |
| 27 | Grant Key **Vault Access Policy** to Microsoft Purview MSI: **Secret: get/list** | *Key Vault Administrator* | Use this step if you have **on-premises** / **VM-based data sources** (for example, SQL Server)  Use this step if **Key Vault Permission Model** is set to [Vault Access Policy](/en-us/azure/key-vault/general/assign-access-policy). |
| 28 | Grant **Key Vault RBAC role** Key Vault Secrets User to Microsoft Purview MSI. | *Owner* or *User Access Administrator* | Use this step if you have **on-premises** or **VM-based data sources** (for example, SQL Server)  Use this step if **Key Vault Permission Model** is set to [Azure role-based access control](/en-us/azure/key-vault/general/rbac-guide). |
| 29 | Create a new connection to Azure Key Vault from the Microsoft Purview governance portal | *Data source admin* | Use this step if you're planning to use any of the following [authentication options](../data-map-data-scan-credentials#create-a-new-credential) to scan a data source in Microsoft Purview: <br>- Account key<br>- Basic Authentication<br>- Delegated Auth<br>- SQL Authentication<br>- Service Principal<br>- Consumer Key |
| 30 | Deploy a private endpoint for Power BI tenant | *Power BI Administrator* *Network contributor* | Use this step if you're planning to register a Power BI tenant as data source and your Microsoft Purview account is set to **deny public access**.  For more information, see [How to configure private endpoints for accessing Power BI](/en-us/power-bi/enterprise/service-security-private-links). |
| 31 | Connect Azure Data Factory to Microsoft Purview from Azure Data Factory Portal. **Manage** -&gt; **Microsoft Purview**. Select **Connect to a Purview account**.  Validate if Azure resource tag **catalogUri** exists in ADF Azure resource. | Azure Data Factory Contributor / Data curator | Use this step if you have **Azure Data Factory**. |
| 32 | Verify if you have at least one **Microsoft 365 required license** in your Microsoft Entra tenant to use sensitivity labels in Microsoft Purview. | Microsoft Entra ID *Global Reader* | Perform this step if you're planning to extend **sensitivity labels to Microsoft Purview Data Map** For more information, see [licensing requirements to use sensitivity labels on files and database columns in Microsoft Purview](../data-map-sensitivity-labels-faq) |
| 33 | Consent "**Extend labeling to assets in Microsoft Purview Data Map**" | Compliance Administrator  Azure Information Protection Administrator | Use this step if you're interested in extending sensitivity labels to your data in the data map.  For more information, see [Labeling in the Microsoft Purview Data Map](../data-map-sensitivity-labels). |
| 34 | Create new collections and assign roles in Microsoft Purview | *Collection admin* | [Create a collection and assign permissions in Microsoft Purview](../data-map-collections-create-classic). |
| 36 | Govern Data Sources in Microsoft Purview | *Data Source admin* *Data Reader* or *Data Curator* | For more information, see [supported data sources and file types](../data-map-data-sources) |
| 35 | Grant access to data roles in the organization | *Collection admin* | Provide access to other teams to use Microsoft Purview: <br>- Data curator<br>- Data reader<br>- Collection admin<br>- Data source admin<br>- Policy Author<br>- Workflow admin<br><br> For more information, see [Access control in Microsoft Purview](../data-gov-classic-permissions). |