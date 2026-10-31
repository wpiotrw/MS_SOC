---
layout: Conceptual
title: Learn about data governance with Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
keywords: Microsoft Purview, data governance, Unified Catalog, Data Map
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: jife
ms.date: 2025-02-19T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how Microsoft Purview solutions Unified Catalog and Data Map can deliver a modern data governance experience for your organization.
locale: en-us
document_id: 8ff102f0-a830-e7fc-586e-7d62ea5f428d
document_version_independent_id: 8ff102f0-a830-e7fc-586e-7d62ea5f428d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 911e4cf2-c6c4-7ce7-727d-c682f2c02279
---

# Learn about data governance with Microsoft Purview | Microsoft Learn

Data governance ensures that the data you use in your business operations, reports, and analysis is discoverable, accurate, trusted, and protected. With ever-evolving regulations combined with the proliferation of AI and regulations for AI, data governance is as critical as data security.

Managing the quality of your data in the era of AI is essential. When your AI systems ingest trusted, high-quality data, you get accurate insights for making sound business decisions. But managing data quality is time-consuming. Data professionals often spend most of their time simply finding, cleaning, and organizing data, instead of using the data that's clean and trusted.

Microsoft Purview data governance solutions, Unified Catalog and Data Map, deliver a modern data governance experience to provide comprehensive visibility, data confidence, and responsible innovation by streamlining metadata from disparate catalogs and sources. With Unified Catalog at the center of your day-to-day operations, your organization can experience comprehensive visibility, data confidence, and responsible innovation to help you achieve greater business value in the era of AI.

## Data governance solutions

Microsoft Purview data governance involves two primary solutions:

- [Data Map](data-map)
- [Unified Catalog](unified-catalog)

Use Data Map to scan all your assets and multicloud sources to capture metadata. Unified Catalog is a searchable catalog of your scanned data where you curate, grant access to, and improve the health of your data. The catalog is a software as a service (SaaS) experience based on a single-tenant model, providing end-to-end capabilities for curating data, managing data quality and health, and granting users in your organization access to data. With a user-friendly and modern experience, Unified Catalog helps organizations achieve greater business value in the era of AI through high-quality data.

For an overview, check out [this video](https://www.youtube.com/watch?v=eGo9mJldifo) explaining Microsoft Purview data governance capabilities, how to set up for success, and the day-to-day management experience.

Important

As you work with Data Map and Unified Catalog, keep these points in mind:

- All data in Data Map and Unified Catalog is **metadata**, not the underlying data itself.
- None of the permissions or roles in Data Map or Unified Catalog provide access to underlying data itself.

## Federated approach to data governance

A federated approach to data governance is a middle ground between a centralized and a decentralized approach. An organization's central data office sets the rules, while individuals in various roles and departments who use the data and understand its function are entrusted to govern that data appropriately. The federated model ensures that there's centralized oversight and helps unlock business innovation by facilitating how users request access to the data they need.

![Data governance federated approach.](media/datagov-federated-approach.png)

### User-friendly tools for data professionals

An effective system of data governance empowers your organization's data professionals to easily manage, discover, and access data. Microsoft Purview data governance solutions are built for each role performed in your organization. Business domain experts can accelerate data value while your data office and stewards provide the standards for consistent operations and can maintain commonalities.

- **Central data office**: Establishes and ensures governance policies, active metadata, compliance, and insights into overall governance health.
- **Data consumers**: Quickly find and use relevant, trusted datasets through streamlined access request workflow.
- **Data owners**: Register data assets for use, manage classifications and access, and ensure high quality standards.
- **Data stewards**: Ensure data quality, seamless data discovery, glossary, consistency, and lineage. Work with central data office.

## Key capabilities

#### Comprehensive visibility

Simplify visibility across disparate catalogs, data sources, data management, and data security with these capabilities:

- Unified Catalog, providing AI-enabled recommendations for data quality and data curation.
- Data products within the Unified Catalog, which are groups of assets with a use case that you can share with data consumers.
- Actionable oversight that helps you analyze and track data health while ensuring users have access to the data they need.

#### Data confidence

Maintain confidence in your organization's data with built-in data quality and data lineage capabilities aligned to industry standards and policies:

- Governance domains of data products and business concepts for easier access and use. Use governance controls across your data estate to complement the domains set up in other technical catalogs. Establish accountability for the area of your data estate.
- Data lineage helps you easily see the relationship between the data products and any assets associated with them to identify the root cause of quality issues.
- Data quality experiences built-in to empower data owners to oversee the quality of their data ecosystem and facilitate actions for improvement.

#### Responsible innovation

Responsibly unlock business value with easier data discovery and actionable insights with these capabilities:

- Role-based access controls to ensure the right people have access to the right data through reader and owner level rights.
- Simplified access and discovery by searching on business context and natural language, with help from Security Copilot.
- Quick access to analytics with Purview Analytics in OneLake, so you can export data from Unified Catalog and import it into OneLake for business users running analytics in Microsoft Fabric.

Tip

Visit [Learn about Unified Catalog](unified-catalog) for detailed information about features and how to get started using the catalog.

## Workflow at a glance

Your organization can take different approaches to start building a data governance practice. The following steps outline the process for setting up data governance with Microsoft Purview:

1. Assign a user in your organization the Data Governance Administrator role. This role grants permissions to assign roles to other users in your organization for key governance tasks and data curation.
2. Use Data Map to scan your data assets and multicloud sources to capture metadata.
3. In Unified Catalog, build governance domains and curate data products.
4. Connect your data with business concepts, such as objectives and key results (OKRs) and glossary terms.
5. Improve data quality and remove data issues to improve data health.

Tip

We've mapped out suggested paths to help you get started depending on your situation at [Plan for data governance](data-governance-plan).

## Billing

Before you get started, review [billing for Microsoft Purview data governance solutions](data-governance-billing).

## Getting started

If you're ready to begin, use these resources to get started:

- Learn how to [plan for data governance](data-governance-plan).
- Visit [Get started](data-governance-get-started) to view detailed instructions with links to deeper technical content.
- Review the [roles and permissions](data-governance-roles-permissions) needed for users in your organization who play a role in data governance.