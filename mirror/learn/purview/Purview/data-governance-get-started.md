---
layout: Conceptual
title: Get started with data governance in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2026-04-24T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Get detailed setup steps to build a fully integrated data governance plan with Microsoft Purview Unified Catalog and Data Map.
locale: en-us
document_id: 12042d23-8925-96a7-11bd-acd1736f9df2
document_version_independent_id: 12042d23-8925-96a7-11bd-acd1736f9df2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/54918a83-0404-4863-9c91-715186c1f582
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b26f5f7a-0913-4a95-8337-ed7543902f2d
platformId: 1c5acf9b-e0c1-ea45-bf7b-d23bc2952fc1
---

# Get started with data governance in Microsoft Purview | Microsoft Learn

This article takes you through technical steps to get started building your data governance solution in Microsoft Purview and integrating data governance with your day-to-day business operations.

You might find it helpful to review [Plan for Unified Catalog](unified-catalog-plan) as an orientation to the material below. For a step-by-step illustration of how to set up your environment, visit the [sample setup walkthrough](data-governance-setup-sample).

## Prerequisites

1. You need a Microsoft Purview Enterprise instance, either by:
    1. [Upgrading an existing account to the new experience](data-governance-purview-portal#how-to-use-the-new-experience)
    2. [Upgrading from the free version of Microsoft Purview to enterprise](data-governance-free-version-upgrade-to-enterprise)
2. Get your data sources [registered](data-map-data-sources-register-manage) and [scanned](data-map-scan-ingestion#scanning) in Microsoft Purview. View the [list of supported data sources](data-map-data-sources).

## Data Governance Administrator role

The Data Governance Administrator role delegates the first level of access for Microsoft Purview Unified Catalog users. Granting this role to a user in your organization is your first step as you get started. Find details on [how to assign roles for data governance](data-governance-roles-permissions).

## Business concepts

Business concepts are elements in Unified Catalog that help you organize and understand your data in ways that make sense to the data consumers and curators in your organization. When we refer to business concepts in Unified Catalog, we're talking about these five elements:

1. [Governance domains](unified-catalog-governance-domains)
2. [Data products](unified-catalog-data-products)
3. [Critical data elements (preview)](unified-catalog-critical-data-elements)
4. [Glossary terms](unified-catalog-glossary-terms)
5. [Objectives and key results (OKRs)](unified-catalog-okrs)

The [Plan for Unified Catalog](unified-catalog-plan) article has detailed guidance to help you understand these concepts and how to start working with them. As a starting point, it's helpful to have a good understanding of **governance domains** and **data products**:

- **Governance domain**: A boundary that enables the common governance, ownership, and discovery of data products and other business concepts. The goal is to empower a governance domain owner to manage their data products, and establish rules for their access, usage, and distribution. Here are some examples of how you could set up your governance domains:

    - Corporate or business areas, such as human resources, sales, and finance.
    - Overarching subject areas, such as product or parties.
    - Regulatory domains, such as SOX, PCI, or anti-money laundering.
    - Boundaries based on organizational functions, such as customer experience, cloud supply chain, or business intelligence.
- **Data product**: A group of data assets, such as tables, files, or Microsoft Power BI reports, that are packaged together with a proper use case to be shared to data consumers in the organization. A governance domain can house many data products, but a data product is managed by a single governance domain and can be discovered across many governance domains.

Once you set up governance domains and data products, you can further curate your data by:

- [Connecting to the other business concepts](data-governance-get-started#connect-your-data-with-business-concepts).
- [Creating and applying attributes to your business concepts.](unified-catalog-plan#create-and-apply-custom-metadata)

## Basic setup steps

1. [Assign users to the Data Governance Administrator role](data-governance-roles-permissions#tenant-level-role-groups) - Gives the admin permissions to grant users [application-level-permissions](data-governance-roles-permissions#catalog-level-permissions) like governance domain creation.
2. Build governance domains:
    1. [Assign users the governance domain creator role](data-governance-roles-permissions#how-to-assign-catalog-level-roles)
    2. [Create at least one governance domain](unified-catalog-governance-domains-create-manage#create-governance-domains)
        Tip

        Use [our guide](unified-catalog-plan#create-governance-domains) to strategize your governance domain structure.
    3. [Assign at least one governance domain owner](data-governance-roles-permissions#how-to-assign-governance-domain-roles) on each governance domain. This user is the point of support and decision authority for data being consumed in this governance domain.
3. [Register your data sources](data-map-data-sources-register-manage) in Microsoft Purview Data Map, and then [scan the data sources](data-map-scan-ingestion) to capture metadata.
4. Build data products:
    1. [Assign data product owners](data-governance-roles-permissions#how-to-assign-catalog-level-roles) to create data products in your governance domains. These should be business and data experts who can pair data with day-to-day scenarios in their governance domain.
    2. [Create at least one data product in your governance domains](unified-catalog-data-products-create-manage#create-data-products). 
        Tip

        Use [our guide](unified-catalog-plan#create-data-products) for tips on how to build good data products.
5. Assign users [catalog reader permissions in your governance domains](data-governance-roles-permissions#how-to-assign-governance-domain-roles) so they can view and explore your data products in the Unified Catalog.

## Connect your data with business concepts

[**Glossary terms**](unified-catalog-glossary-terms) provide vocabulary for business users. These terms let users discover and work with data in the vocabulary that's familiar to them, instead of using abstract technical terminology inherited from physical data sources.

[**Objectives and key results (OKRs)**](unified-catalog-okrs) are the goals or desired outcomes of a governance domain; for example, 10% rise in sales or 3% reduction in support cases. Objectives should relate to everything an organization does and should define how they're achieving their outcomes.

[**Health management actions**](unified-catalog-data-health-management-actions-page) give you and your users steps to improve data health and governance across your data estate. These actions correspond to the checks made to calculate a data product’s data governance health control score. Addressing these actions raises your health score and promotes an overall more usable and discoverable Unified Catalog. Understanding the value of your data products improves the trust others take in that data and helps with prioritizing which data to focus on improving first.

#### Connect action steps

1. [Assign users data steward permission in your governance domains to create and manage glossary terms](data-governance-roles-permissions#how-to-assign-governance-domain-roles). These users should be data and business experts. They increase the value of data products by curating the information and attaching glossary terms to make the data understandable.
2. [Create at least one OKR in your governance domain.](unified-catalog-okrs-create-manage#create-okrs)
    1. [Link your OKR to a data product to connect your data to your business goals.](data-governance-roles-permissions#how-to-assign-governance-domain-roles)
3. [Assign users data health reader permissions in Unified Catalog](data-governance-roles-permissions#how-to-assign-catalog-level-roles). These users monitor Unified Catalog use and current governance scores, and take actions to build trust in your data products.
4. [Publish some glossary terms in your governance domain.](unified-catalog-glossary-terms-create-manage#create-glossary-terms)
    1. [Link a glossary term to a data product to improve discoverability.](unified-catalog-glossary-terms-create-manage#link-terms-to-data-products-assets-and-critical-data-elements-preview)
5. [Assign users data steward permission in your governance domains to create and manage OKRs](data-governance-roles-permissions#how-to-assign-governance-domain-roles). These users should be business strategy experts to ensure business leaders appreciate the value of their data, and the importance of data governance. They drive prioritization and strategize how teams build, maintain, and govern their data to create insights.
6. [Review your health controls](unified-catalog-controls) to get a baseline for your current health management.
7. [Review health actions](unified-catalog-data-health-management-actions-page) to start considering next steps for your data governance journey.
8. [Create custom metadata and apply attributes to your business concepts.](unified-catalog-plan#create-and-apply-custom-metadata)

## Improve data quality and remove data issues

[**Data quality**](unified-catalog-data-quality) measures the quality of data in an organization. It uses data quality rules that you configure and define in Unified Catalog.

[**Data quality rules**](unified-catalog-data-quality-rules) describe the state of the data with dimensions like accuracy, completeness, conformity, consistency, timeliness, and uniqueness. Each rule produces a score that describes how close the data is to its desired state.

[**Data profiling**](unified-catalog-data-quality-profiling) examines the data available in your data sources. It collects statistics and information, and assesses the quality level of the data according to a defined set of goals. If data is of poor quality or managed in structures that can't be integrated to meet the needs of the organization, it can affect business processes and decision-making.

#### Quality action steps

1. [Assign users(s) data quality steward permissions](data-governance-roles-permissions#how-to-assign-catalog-level-roles) to use all data quality features.
2. [Set up a data source connection to prepare your source for data quality assessment](unified-catalog-data-quality-supported-sources-connection).
3. [Configure and run data profiling for an asset in your data source.](unified-catalog-data-quality-profiling)
    1. When profiling is complete, browse the results for each column in the data asset to understand your data's current structure and state.
4. [Set up data quality rules](unified-catalog-data-quality-rules) based on the profiling results, and apply them to your data asset.
5. [Configure and run a data quality scan](unified-catalog-data-quality-scan) on a data product to assess the quality of all supported assets in the data product.
6. [Review your scan results](unified-catalog-data-quality-scores) to evaluate your data product's current data quality.

## Weekly planning

The following is a reference example to assist with planning the new Microsoft Purview data governance solution areas, scenarios, tasks, and personas with key stakeholders.

### Week 1-2

| Area | Scenario | Task | Description/Outcomes | Persona |
| --- | --- | --- | --- | --- |
| Data management | Catalog setup | Set up first governance domain | Identify governance domain scope, usage, and owners. Assign accountability to governance domain owner, define and create your first governance domain, description, and assign data owners. Capture feedback on establishing the governance domain. | Governance domain owner |
|  | Catalog curation | Create data products in the governance domain | Identify scope of data to manage, publish, and owners. Create data products, descriptions, use cases, assign ownership, and create and assign glossary terms to help increase usability for data consumers. Map data assets to data products, create access policies for data consumers to attest to when requesting access – capture feedback (ease of use for business unit to manage, understand, and own curation) | Data product owner/data steward |
|  | Publication | Publish the governance domain and data products | Publish the governance domain and associated data products to make available for discovery, understanding, and access through the Unified Catalog experience. Assign data consumers permissions to access and view the first governance domain by adding them to the Global Catalog reader role and capture feedback with publication. | Governance domain owner and data product owner |
|  | Operations | Data governance and management operations | Assess operational tasks, stakeholders, processes, and procedures to enable data governance and management. Evaluate against current state data governance policies, practice, and culture to identify potential areas for improvement or change. | Data governance office |

### Week 2-3

| Area | Scenario | Task | Description/Outcomes | Persona |
| --- | --- | --- | --- | --- |
| Data discovery, understanding, and access | Discover and access | Unified Catalog product search | Exercise the Unified Catalog product search experience to help data consumers and users discover and understand data products that are curated and developed for a specific business purpose. Assess data product metadata to determine proper usage, data quality, and applicability to data consumer business outcomes, and then request access. Assess ease of use to data products the user recently reviewed, and data products subscribed to – capture feedback on full data consumer experience. | Data consumer |
| Data management | Access management | Access request management | Review access requests for data products in the first governance domain and approve or reject. Engage with IT owners for approvals (as appropriate) to data assets. | Data product owner |
|  | Catalog curation | Review data product discoverability | Review discoverability and usability of published data products along with data consumer feedback to inform semantic knowledge improvement opportunities (for example, glossary terms, attention to attention items in the action center, etc.). | Data product owner/data steward |

### Week 3-4

| Area | Scenario | Task | Description/Outcomes | Persona |
| --- | --- | --- | --- | --- |
| Data management | Data quality | Improve data quality and reduce data issues | Assess top-level data quality by the first governance domain, and evaluate and set up data quality for associated data assets by data product (via connections). Use data quality profiling data to inform quality rules and dimensions to establish key data assets in the data product. Run data quality scans (ad-hoc or scheduled), monitor data quality activity and scans, and set up alerts to be informed of changes with data asset health (via target thresholds). Capture feedback on overall data quality experience. | Data quality steward |
|  | Operations | Data governance and management operations | Assess operational tasks, stakeholders, processes, and procedures to enable data quality in the context of data governance and management. Evaluate against current state data governance policies, practice, and culture to identify potential areas for improvement or change. | Data governance office |

### Week 4-5

| Area | Scenario | Task | Description/Outcomes | Persona |
| --- | --- | --- | --- | --- |
| Health management | Reports | Manage data governance | Review the controls with business data domain owners and set up regular review of reporting on those controls. The goal of the meeting is to review issues and prioritize solutions or data products that are needed to meet business needs. | Data governance office |
|  | Health actions | Improve data governance | Take actions based on the controls to improve data governance and ensure standards are met. | Data stewards/data product owners |

## Unified Catalog overview page

The **Overview page** in Unified Catalog helps users in an organization get started with their data governance journey, understand, and navigate the different steps outlined in this document, using step by step instructions and video demos.

## Resources

- [Sample setup walkthrough for data governance using Unified Catalog](data-governance-setup-sample)
- [Data governance roles and permissions](data-governance-roles-permissions)