---
layout: Conceptual
title: Microsoft Purview and Semarchy Master Data Management (MDM) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-master-data-management-semarchy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2024-07-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to deploy the Microsoft Purview and Semarchy integration as a master data management (MDM) solution for your data estate governance..
locale: en-us
document_id: 3938a58b-36b9-bd87-a6a9-7982784b54c7
document_version_independent_id: 3938a58b-36b9-bd87-a6a9-7982784b54c7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-master-data-management-semarchy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-master-data-management-semarchy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-master-data-management-semarchy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/d6f38669-3d05-40f2-afd8-e49f7dd20884
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/55265cca-de9b-48dc-a77a-9047cc39a575
platformId: c7f53960-1c9b-dbf6-01bc-463b101359f5
---

# Microsoft Purview and Semarchy Master Data Management (MDM) | Microsoft Learn

Modern organizations generate large quantities of data, often from numerous, disparate sources. The Semarchy Data Platform is the intelligent data hub for data integration, master data management (MDM), reference data management (RDM), application data management (ADM), data integration, quality, and governance. Semarchy Data Management (xDM) brings extreme agility for defining and implementing data management applications and releasing them to production.

This architecture demonstrates how to include Master Data Management (MDM) into the Azure ecosystem to enable quality, validation, matching, deduplication, authoring, curation, and collaboration for your critical data assets.

## Architecture

The following architecture illustrates the Semarchy xDM architecture and data flow.

![Screenshot of MDM architecture.](media/semarchy-mdm/mdm-semarchy-architecture.png)

## Data Flow

Metadata and data flow include the following steps:

- **Source data integration** from identified source systems:

    - This integration uses Azure Data Factory, Semarchy xDI (Semarchy’s data integration component), or your integration solution.
    - semarchy xDM exposes SQL or REST endpoints for batch and real-time integration.
    - Incoming data can be profiled with Semarchy xDM Discovery and reviewed to help define the master data model structure and rules.
    - At any time, the REST endpoints can also be used by applications to interact (read/write) with the master data managed in xDM, and use xDM as their master data backend.
- **Automatic Data Certification**

    - Data undergoes enrichment, standardization, and quality validation through a combination of rules, plugins, AI models (including Azure Machine Learning and Azure OpenAI), and third-party services. Semarchy xDM supports these automated quality processes with data recycling and incorporates user corrections to ensure optimal data quality.
    - Matching, merging, and survivorship processes are automatically carried out by combining sophisticated automation with informed user decisions, to produce accurate, and reliable consolidated golden records.
    - Golden records produced by the certification process feature complete lineage to the source systems, user change tracking, and optional historization. This guarantees data integrity, traceability, and comprehensive historical record tracking.
- **Customized Data Management Applications** are available for users to:

    - Authenticate via Microsoft Entra ID.
    - Browse and search certified data with complete traceability through each certification stage, alongside comprehensive historization.
    - Manage and curate data. Users can:
        - Author and import new data.
        - Review and fix errors.
        - Manually match and merge records with override options
        - Perform soft or hard deletes as necessary.
    - Collaborate with Data-Driven Workflows.
- **Golden data distribution** to consumer operational and analytical applications such as Azure Synapse Analytics, Power BI, Azure Machine Learning, and Azure OpenAI, ensures uninterrupted integration and usage across platforms:

    - This integration uses Azure Data Factory, Semarchy xDI, or your integration solution.
    - Semarchy xDM provides built-in SQL and REST endpoints, and Data Notifications for event-based propagation in Azure Service Bus.
- **Synchronize xDM metadata** with Microsoft Purview to gain comprehensive visibility and lineage of the entire master data flow.

## Components

This architecture involves the following components.

**Core Components**

- Semarchy xDM is a no-code platform that allows data teams to quickly develop customized master data management solutions, offering a wide range of capabilities for complex data ecosystems.
- Azure Database for SQL Server and PostgreSQL are fully managed databases as a service with built-in capabilities, such as high availability and intelligence. They store both the Semarchy metadata and master data hubs managed in xDM. Data processing is performed in the database layer, guaranteeing the best performance and scalability.
- Microsoft Entra ID, for user authentication and single sign-on to the Semarchy platform.
- Azure Key Vault is a cloud service that provides secure storage for secrets. You can use it to encrypt, decrypt, and store secrets (passwords, for example) used in xDM.

**AI Components**

- **Azure Machine Learning** is a cloud service for accelerating and managing machine learning (ML) projects. Semarchy xDM can use customized Azure Machine Learning models in the data hub certification processes.
- **Azure OpenAI** is a suite of AI services providing access to OpenAI's powerful language models. Semarchy xDM includes built-in plug-ins using these language models to enrich and certify data, for example for content generation, summarization, or translation.

**Governance Components**

- **Microsoft Purview** is a data governance solution that provides broad visibility into on-premises and cloud data estates. Semarchy xDM integrates with Microsoft Purview to provide insights into Semarchy Data Hubs as data products and end-to-end master data lineage.

**Source and Consumer Systems** Among others, this architecture includes the following systems from which you collect master data to be managed in Semarchy xDM, or to which you send golden data produced by Semarchy xDM.

- **Azure Synapse Analytics** is a fast, flexible, and trusted cloud data warehouse that uses a massively parallel processing architecture. Semarchy Data Hubs act as providers of certified metadata for Azure Synapse.
- **Power BI** is a business analytics suite that delivers insights throughout your organization. You can use Power BI to build dashboards and reports on top of Semarchy Discovery metrics and the Semarchy Data Hubs.

## Scenario Details

Data-driven initiatives, such as digital transformation, business intelligence, or AI projects require accurate and trustable data. Master Data Management is an essential step to deliver this clean, accurate data.

A common use case for an MDM solution is to consolidate master data from multiple sources while allowing collaborative authoring and stewardship of this master data to serve analytical and operational applications with golden data.

## Design data applications

Semarchy xDM Data Management Applications provide all users with a customized experience to access and manage their data. Through these applications, master data records are displayed in fully customizable interfaces, supporting data management, authoring, and stewardship operations. Users with different roles and personas collaborate in Data-Driven Workflows to manage data. The power of Semarchy xDM lies in the flexibility in the design of your data applications, allowing them to adapt to your domains, organization, and business needs.

## Integrate and certify master data

Data curated in external source systems, such as Customer Relationship Management (CRM), Enterprise Resource Planning (ERP), or other systems (known as the publishers) is pushed to Semarchy xDM’s data hubs via an integration layer, such as Azure Data Factory or Semarchy xDI.

As data changes appear in the data hub, through data loads or authoring, it passes through the entire certification process, during which it's enriched, standardized, validated for data quality, and then matched and merged the records.

## Consume data from the hub

Data can be pushed to or consumed from Semarchy xDM using REST API endpoints, or through SQL. Changes made to the data through the data hub can also be propagated in real-time to downstream systems using data notifications.

## Considerations

The Semarchy Data Platform has several features that address the issues of reliability, security, cost optimization, operational excellence, and performance efficiency. More information about architectural excellence can be found at [Microsoft Azure Well-Architected Framework pillars](/en-us/azure/well-architected/pillars).

## Reliability

Reliability ensures your application fulfills the promises you make to your customers. Find guidance on [Reliability](/en-us/azure/well-architected/reliability/).

Semarchy xDM runs natively on Azure Kubernetes Service and Azure SQL Database, which offers out-of-the-box capabilities to support high availability.

## Security

Security shields against intentional attacks and misuse of your valuable data and systems. Find guidance on [Security](/en-us/azure/well-architected/security/).

Semarchy xDM authenticates users via its identity management layer that supports role mapping, lookup, and profile synchronization. It provides native support for multiple IDPs, including Microsoft Entra ID. It also includes advanced security features such as fine-grained privileges to secure access and operations.

## Performance Efficiency

Performance efficiency is the capability of your system to scale and effectively meet user needs. Find guidance on [Performance Efficiency](/en-us/azure/well-architected/performance-efficiency/).

Semarchy xDM runs natively on Azure Kubernetes Service and Azure SQL Database. You can configure Azure Kubernetes Service to scale up and out. You can deploy and configure Azure SQL Database to balance performance, scalability, and costs.

## Cost Optimization

Cost optimization involves finding ways to reduce unnecessary expenses and enhance operational efficiency. Find guidance on [Cost Optimization](/en-us/azure/well-architected/cost-optimization/).

Running costs consist of the Semarchy software subscription license and Azure consumption. Contact Semarchy for more information.

## Deploy this scenario

To deploy this scenario:

1. Deploy Semarchy xDM using Azure Kubernetes Services.
2. Configure Secrets Management to use Azure Key Vault.
3. Configure Authentication with Microsoft Entra ID.
4. Design and deploy your customized master data model in xDM
5. Integrate your data into xDM using Azure Data Factory.

## Contributors to this document

- David Cox
- Cedric Blanc
- François-Xavier Nicolas (FX)

## Reference document

- [Deploy Semarchy xDM](https://www.semarchy.com/doc/semarchy-xdm/xdm/latest/Install/azure/aks/install-on-aks.html)
- [Copy Secrets Management](https://www.semarchy.com/doc/semarchy-xdm/xdm/latest/Install/secrets-management/kms-configuration.html#_azure_kms)
- [Configure Authentication with Microsoft Entra ID](https://www.semarchy.com/doc/semarchy-xdm/xdm/latest/Install/azure/configure-authentication-in-azure.html)
- [Integrate your data into xDM using Azure Data Factory](https://www.semarchy.com/doc/semarchy-xdm/xdm/latest/Integrate/overview.html)