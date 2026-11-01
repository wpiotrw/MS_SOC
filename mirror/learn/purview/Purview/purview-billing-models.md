---
layout: Conceptual
title: Learn about Microsoft Purview billing models | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-billing-models
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
description: Learn about how the two Microsoft Purview billing models complement each other and the pay-as-you-go billing model that's used to extend Microsoft Purview controls beyond Microsoft 365 based assets.
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-01-05T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-portal
audience: ITPro
ms.topic: concept-article
ms.collection:
- purview-compliance
- essentials-get-started
ms.custom:
- admindeeplinkCOMPLIANCE
- intro-overview
locale: en-us
document_id: 10de6e26-a996-aedc-b70c-919e00ad0a20
document_version_independent_id: 10de6e26-a996-aedc-b70c-919e00ad0a20
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-billing-models.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-billing-models
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-billing-models.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 59a16ed3-3154-ffc5-ba00-56028c6af05b
---

# Learn about Microsoft Purview billing models | Microsoft Learn

[Microsoft Purview](purview) offers a set of integrated solutions that help customers secure and govern their data. It's composed of data security and data governance solutions for:

- Microsoft 365 and non-Microsoft 365 workloads and data systems.
- Microsoft 365 and non-Microsoft 365 endpoints.
- Compliance solutions for data used with Generative AI applications.

Microsoft Purview supports two complementary billing models to support this diverse environment:

- Per-user license for Microsoft 365 and Windows/macOS endpoint sources
- Pay-as-you-go model for non-Microsoft 365 data sources and certain other capabilities

This article takes you through:

- An overview of the two billing models.
- Links to information on the solution specific capabilities.

Note

The pay-as-you-go billing model builds on the per-user licensing model. The two are complementary, not mutually exclusive.

## Per-user licensing model

The per-user licensing model is the familiar Microsoft 365 E3/E5/A5/F5/G5 model. It remains unchanged. This licensing model enables you to apply Microsoft Purview controls and protections to Microsoft 365 and Windows/macOS endpoint-based assets. It's described in the [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description).

## Pay-as-you-go billing model

The pay-as-you-go billing model is a consumption billing model. It extends Microsoft Purview data security, data governance, and data risk and compliance protection capabilities beyond Microsoft 365 and Windows/macOS environments to non-Microsoft 365 locations. The billing mechanisms are Azure based, so you must associate your Microsoft 365 tenant with an active Azure subscription. It also protects data moving through networks, DataOps, application architectures, and AI apps and agents, as well as certain other user-agnostic capabilities.

In the pay-as-you-go model, you're charged based on your usage of various pay-as-you-go features, based on the unit of consumption for the feature. An Azure bill is generated at the end of the month for the total number of pay-as-you-go charges across all Microsoft solutions.

Note

For guidance on how to associate a Microsoft 365 tenant to an Azure subscription, see [Enable Microsoft Purview pay-as-you-go features for new customers](purview-payg-subscription-based-enablement).

## Capabilities that use the pay-as-you-go billing model

Note

Some Microsoft Purview solutions use the per-user licensing model. Some require the per-user licensing model to be enabled before you can use the pay-as-you-go billing model. Some are pay-as-you-go only and don't require a per-user license.

### Data Security and Data Governance

The pay-as-you-go billing model extends Microsoft Purview data security and governance capabilities beyond Microsoft 365 and Windows/macOS to environments like:

- Amazon Web Services (AWS)
- Microsoft Entra IDLS
- Azure SQL
- Box
- Dropbox
- Google Drive
- Microsoft Fabric

For details on data governance assets, see [Microsoft Purview data governance billing](data-governance-billing).

### Data security capabilities

| Solution | Applies to | Unit of Measure | Details |
| --- | --- | --- | --- |
| [Data Security Investigations](data-security-investigations) | Data storage meter based on the storage associated each investigation | Number of gigabytes of stored data for all investigations/month  Number of Data Security Investigations security compute units consumed | Learn more about [billing for Data Security Investigations](data-security-investigations-billing) |
| [Information Protection](sensitivity-labels) | Sensitivity labels that you apply to non-Microsoft 365 data sources | Number of assets in scope of protection policy/day | Refer to details below on how assets are defined and calculated |
| [Insider Risk Management](insider-risk-management) | Detect risky behavior for non-Microsoft 365 locations when using Cloud and generative AI policy indicators | Data Security processing unit as measured on a daily basis | Learn more about [Insider Risk Management policy indicators](insider-risk-management-settings-policy-indicators) |

### Data governance capabilities

| Solution | Applies | Unit of Measure | Details |
| --- | --- | --- | --- |
| [Unified Catalog data curation](unified-catalog) | Applies when you actively curate and manage the technical assets in Microsoft Purview Unified Catalog | Number of unique assets governed/day | [Learn more about data governance billing](data-governance-billing) |
| [Unified Catalog data health management](unified-catalog-data-health-management) | Applies when you manage data quality and take health management actions | Number of data governance processing units (DGPUs) consumed | [Learn more about data governance billing](data-governance-billing) |

**Data governance processing units**: For more information on data governance processing units, see [Data governance processing units explained](data-governance-billing#data-governance-processing-units-explained).

### Data risk and compliance capabilities

For generative AI apps and agents, Microsoft Purview offers the following capabilities on a pay-as-you-go billing model. Microsoft 365 Copilot experiences aren't charged.

| Solution | Applies to | Unit of Measure | Details |
| --- | --- | --- | --- |
| [Audit solutions](audit-solutions-overview) | Audit logs for user interactions with non-Microsoft generative AI applications | Number of audit records processed | Learn more about [generative AI applications supported by Audit solutions](audit-copilot). |
| [Communication compliance](communication-compliance) | Detect inappropriate or risky interactions for non-Microsoft 365 AI interactions when using AI policy indicators | Number of text records scanned | Billing meters for communication compliance are broken down into two categories, standard, and premium. Learn more about the [channels](communication-compliance-channels) and [generative AI applications supported by Communication Compliance](communication-compliance-copilot) |
| [Data Lifecycle Management](data-lifecycle-management) | Retention policies for AI interactions | Number of non-Microsoft 365 Copilot or AI App interactions (prompts and responses) under a retention policy | Each non-Microsoft 365 generative AI prompt and response count as a separate interaction and is retained and deleted according to the retention policy settings you configure in Microsoft Purview. For more information on retention policies in DLM for Microsoft 365 Copilot and AI apps, see [Learn about retention for Copilot & AI apps](retention-policies-copilot) |
| [eDiscovery](edisc) | Storage of non-Microsoft 365 AI application data and usage of Microsoft Graph APIs for standard licensed tenants | Number gigabytes stored/day for storage of non-Microsoft 365 AI data. Gigabytes/export for usage of Export API by Standard licensed tenants | Learn more about [eDiscovery billing](edisc-billing) |

### Other Microsoft Purview solutions that use pay-as-you-go pricing

| Solution | Applies to | Unit of Measure | Details |
| --- | --- | --- | --- |
| [On-demand classification](on-demand-classification) | Applies when you run a scan to identify and classify sensitive content in data stored in SharePoint and OneDrive | Asset, based on the number classified per scan | Learn more about [On-demand classification](on-demand-classification) |
| [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot) | Applies for all Security Copilot functions | Security Compute Units | [Get started with Security Copilot](/en-us/copilot/security/get-started-security-copilot#security-compute-units) |
| [Network Data Security](dlp-network-data-security-learn) | Requests from an endpoint device to a website, cloud app, or generative AI app | Number of requests sent from the endpoint device to the website, cloud app, or generative AI app | Network data security only counts requests that are outbound from the device. |
| [Data Security for Gen AI Applications](/en-us/purview/ai-microsoft-purview) | Applies to classification and protection of sensitive content for non-M365 AI interactions (prompts/responses) | Number of requests or messages for non-Microsoft 365 AI interactions (prompts or responses) | Learn more about data security [for AI interactions](/en-us/purview/ai-microsoft-purview) |

## Cost estimator tools

Understand pricing and estimate your expected monthly costs for pay-as-you-go capabilities:

- [Microsoft pay-as-you-go pricing](https://azure.microsoft.com/pricing/details/purview/)
- [Estimate your costs for Microsoft Purview pay-as-you-go feature use](https://azure.microsoft.com/pricing/calculator/)

## Units of measure for pay-as-you-go capabilities

### Assets

An asset is any Microsoft 365 item that a Microsoft Purview policy protects. Some examples are a table for structured data or any file for unstructured data. You're charged for each day that a policy covers an asset. For Microsoft Data Lifecycle Management, assets include interactions (prompts and responses) between a user and a Copilot or AI App.

Here are some examples of assets for Microsoft Purview Data Security and Governance and the protection policies that you can apply to them.

| Cloud provider | Data source | Asset | Can be protected by |
| --- | --- | --- | --- |
| Azure | SQL DB | Table | Protection policy and auto-labeling policy from Microsoft Purview Information Protection |
| Azure | ADLS | File or resource set | Protection policy and auto-labeling policy from Microsoft Purview Information Protection |
| Azure | Blob | File or resource set | Protection policy and auto-labeling policy from Microsoft Purview Information Protection |
| Azure | Fabric | [Supported item types](/en-us/fabric/governance/protection-policies-overview#supported-item-types) | Protection policies from Microsoft Purview Information Protection |
| Azure | Fabric | [Supported item types](dlp-powerbi-get-started#supported-item-types) | Microsoft Purview Data Loss Prevention |

For details on data governance assets, see [Microsoft Purview data governance billing](data-governance-billing).

#### Counting assets

Assets are counted based on the number of items that are in the scope of a policy. The asset doesn't have to match a policy's conditions to be counted, it just has to be in a location that's in the scope of a policy. An asset is only counted once, regardless of how many solutions or protection policies cover it.

Here are some examples:

- **Protection policy**: A tenant has SQL server with 100 tables, and 50 of those tables are labeled **Confidential** and 20 are labeled **General**. The protection policy only applies to assets labeled with **Confidential**, so the asset count is 50.
- **Data Loss Prevention policy**: A tenant has 10 Fabric workspaces, each with 50 assets. The policy only applies to five of these Fabric workspaces. The asset count for this policy is 250.

### Processing units

A processing unit measures the amount of compute resources used to process signals from workloads that are included in pay-as-you-go.

- **Data governance processing units**: A data governance processing unit (DGPU) is a fully managed compute unit that runs compute capabilities such as data quality and data health management. Each DGPU is 60 minutes of compute time that runs across varying sets of nodes based on the workload need. For more information on data governance processing units, see [Data governance processing units explained](data-governance-billing#data-governance-processing-units-explained).
- **Data security processing units**: Microsoft Purview data security processing units represent the compute required to process user activities from non-Microsoft 365 data sources to generate insights. The number of units required can vary depending on the Purview solution and the complexity of the data being processed. [Insider risk management](insider-risk-management) is a pay-as-you-go feature that uses a processing unit based meter. It includes [pay-as-you-go indicators](insider-risk-management-settings-policy-indicators#cloud-service-indicators). For more information, see [Configure policy indicators in insider risk management](insider-risk-management-settings-policy-indicators#built-in-indicators-vs-custom-indicators).
- **Compute units**: Data Security Investigation compute units (compute units) represent the compute required to process and generate AI-based insights in Data Security Investigations. The number of units required can vary depending on the process and is a pay-as-you-go feature that uses a processing unit based meter.For more information, see [Billing in Data Security Investigations](data-security-investigations-billing).

#### Counting processing units

The number of processing units you need varies depending on the Microsoft Purview solution and the complexity of the data being processed.

For example, Insider Risk Management processes user activities corresponding to the non-Microsoft 365 indicators selected in data theft and data leak policies to generate insights, alerts, and cases. For Insider Risk Management, a processing unit represents the compute required to process 10,000 such user activities. Billing is based on the number of processing units utilized. Insider Risk Management indicators that detect activity in cloud storage apps (Box, Dropbox, Google Drive), cloud services (AWS, Azure), and Microsoft Fabric (Power BI) are billed on data security processing units.

### Data storage meter (GBs)

Microsoft Purview data storage meter is defined by a gigabyte per month storage amount billed at a specific rate for applicable solutions. The total amount of data within a solution subject to data storage meter is automatically calculated from the current amount of data in solution-related containers. For example, pay-as-you-go in [Data Security Investigations](data-security-investigations-billing) and [eDiscovery](edisc-billing) use the data storage meter.

eDiscovery also uses a storage meter defined by the gigabytes per export through Graph API for E3 eDiscovery licensed customers. Each organization receives an included amount of free storage per month, with additional usage billed at a set price per GB.

For more information about API storage and pricing, see [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/).

### Text records

Microsoft Purview text records meter is defined by text records, where one text record equals 1,000 characters. Each message converts into multiple text records based on character length. For example, pay-as-you-go in Communication Compliance uses a text records-based meter.

**1 text record = 1,000 characters**

If a message has more than 1,000 characters, it counts as one text record for each unit of 1,000 characters. For instance, if a message contains 7,500 characters, it counts as eight text records. If a message contains 500 characters, it counts as one text record.

### Counting text records for Communication Compliance Premium

Counting text records for premium is based on the type of detections that the messages are being evaluated for. If the evaluation includes the following detections, they're charged at the premium rate:

1. **Code of conduct**: Hate, self-harm, violence, sexual
2. **Risky Gen AI:** Prompt shields, protected materials

### Calculating text records for Communication Compliance Standard

If messages are evaluated positive for any other detections, such as other trainable classifiers or sensitive info types, you pay standard charges. Messages that evaluate messages for both premium and standard detections are charged only for premium detections.

### Security Compute Units (SCU)

A security compute unit (SCU) is a bundled unit of measure. It combines all the resources, like network, processor, and storage, that Microsoft Security Copilot needs to provide service into a single, billable quantity.

For more information on SCUs, see [Get started with security compute units](/en-us/copilot/security/get-started-security-copilot#security-compute-units).

#### Counting SCUs

The number of SCUs you have available is your capacity. Your available capacity consists of two types:

- **Provisioned SCUs:** These are units that you pre-allocate. You use the cost estimators to project the number of SCUs you anticipate using. Use of provisioned SCUs is measured in hourly blocks. For example, if you provision an SCU at 9:05 a.m., then deprovision it at 9:35 am, and then provision another SCU at 9:45 am, you are charged for two units within the 9:00 a.m. to 10:00 a.m. hour. To maximize usage, make SCU provisioning changes at the beginning of the hour. For more information, see [Manage usage](/en-us/copilot/security/manage-usage).
- **Overage SCUs:** These units cover unexpected spikes in usage. To manage unexpected demand spikes, you can allocate an overage amount to ensure that additional SCUs are available when you run out of provisioned units. Overage units are billed on-demand. You can set limits for overage units as unlimited or set a maximum upper amount. This approach enables predictable billing while providing the flexibility to handle both regular and unexpected usage.

### Requests

For pay-as-you-go billing, a request is each network call a device or browser makes to a website or API. This definition doesn't include the responses to the requests. Azure counts requests in the monthly pay-as-you-go bill you receive. Microsoft Purview network data security pay-as-you-go uses requests as its unit of measure. Here are some examples:

| Activity | Data type | Example |
| --- | --- | --- |
| Text sent to or shared with cloud or AI app | human readable strings transmitted inline | - submitting a form with textual information - Sending raw text or a prompt to a generative AI - the body of an email - sending JSON data to an API |
| File uploaded to or shared with cloud or AI app | Byte streams, including text based file, binary files, txt files, source code, documents, images, videos, .exe's, .pdf's, archive files | - Uploading a profile picture to social media - sending a document or PDF file as an email attachment - sharing a document with generative AI - transferring a document or .ZIP files to a cloud storage solution |