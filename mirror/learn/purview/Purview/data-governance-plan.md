---
layout: Conceptual
title: Plan for data governance with Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-plan
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2025-02-19T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about planning for data governance using Microsoft Purview solutions Unified Catalog and Data Map.
locale: en-us
document_id: 8ff6aa70-a04f-dacb-5c59-fcd36fccc899
document_version_independent_id: 8ff6aa70-a04f-dacb-5c59-fcd36fccc899
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-plan.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: df980667-bec0-2b34-ed83-3488d2880a07
---

# Plan for data governance with Microsoft Purview | Microsoft Learn

Before you get started with data governance, your information technology and data management teams should review important planning activities and considerations. Thoroughly understanding and planning for deployment helps ensure that your implementation and use of features in Microsoft Purview Unified Catalog and Microsoft Purview Data Map go smoothly and align with best practices.

Note

Check to see [which regions are supported](unified-catalog-regions) for Microsoft Purview data governance solutions.

## Relationship between Unified Catalog and Data Map

The Data Map is the technical layer of Microsoft Purview that stores the data about the assets. Data sources are scanned to create the inventory of what assets are available in the different data sources across your organization's data estate.

The Unified Catalog is the business-friendly layer where data stewards curate data, and data consumers find the right data to use. The Unified Catalog is powered by the asset inventory in the Data Map to create a marketplace of data products, ensuring consumers can find the right data and use it responsibly.

Important

As you work with Data Map and Unified Catalog, keep these points in mind:

- All data in Data Map and Unified Catalog is **metadata**, not the underlying data itself.
- None of the permissions or roles in Data Map or Unified Catalog provide access to underlying data itself.

## Who to involve in data governance

When you start your data governance planning with data owners, data stewards, and other business users with expertise, you ensure that the Unified Catalog has all of the information needed to build new value with data. IT teams are critical organizational partners in data use, and help to ensure the right data sources are prioritized for onboarding to the Microsoft Purview Data Map.

Your organization's data office will oversee the creation of the catalog with company-wide standards, and help build bridges between teams to provide the best governance framework. Having both the data publishing teams and the data consumers included in the process of building out the catalog will provide the most value from the data, and build the collaboration to include all of the experts across your organization.

Tip

For the best success, **involve all parties early**. This approach is important because the practice of data governance isn't done by a single person, and no one knows everything about the data, the business, and what it means to use that data responsibly.

## Where to start

You can start building your data governance practice with Microsoft Purview in many ways. How you start depends on your business strategy and who's doing the work. You don't realize the full value of Microsoft Purview for data governance until you complete all key tasks. The tabs below provide guidance based on your situation or preferred approach.

# [New to Microsoft Purview or data governance](#tab/new)
If you're new to data governance or to Microsoft Purview, we suggest starting with the stakeholders who are most passionate about data governance, or have the need to create a data catalog. Typically, business intelligence teams or data lake teams can be a good place to start because they have experts on the data and have invested in building data that others can use.

When you're ready to get started, complete the tasks outlined in [Getting started with data governance](data-governance-get-started) in the following order:

1. Create a governance domain (Unified Catalog).
2. Add a domain owner who is accountable for that domain (Unified Catalog).
3. Add the experts for that part of business to build business concepts (Unified Catalog).
4. Create a collection (Data Map).
5. Add a data source administrator from the data platform to onboard first (Microsoft Purview settings).
6. Register and scan the data source (Data Map).
7. Build out the data products for the most important and frequently used data in that source in the governance domain (Unified Catalog).

# [Technical staff ready to start working with data](#tab/it-data)
If you're in the IT department and want to start working with your data, follow the tasks outlined in [Getting started with data governance](data-governance-get-started) in the following order:

1. Create a collection for your data sources (Data Map).
2. Register and scan your data (Data Map).
3. Create a governance domain aligned to the area of the business or data domain that your data sources support (Unified Catalog).
4. Curate the data assets, ensuring that data lineage is added where possible and that users can understand how you created the asset and what it contains (Unified Catalog).
5. Create data products from the most requested data, including details on how to use that data effectively (Unified Catalog).
6. Run some basic data quality rules to show the data assets are good to use (Unified Catalog).
7. Publish your data products and advertise the data you support with your business stakeholders to gain their support in completing the governance domain (Unified Catalog).
8. Add the assets to your data products (Unified Catalog).

Tip

Check out best practices, API tutorials, and other resources in the **Technical reference** section of **Data governance solutions** articles.

# [Data stewards who want to first plan a strategy](#tab/stewards-strategy)
If you're a data steward or owner, and want to start by considering what's in your organization and how it should be organized, follow the tasks outlined in [Getting started with data governance](data-governance-get-started) in the following order:

1. Create a governance domain for the data you're accountable for (Unified Catalog).
2. Create the glossary terms, critical data elements, and objectives and key results to give context to what your area of the business cares about (Unified Catalog).
3. Create some data products for what you want to start governing, to ensure your business has the best data to meet your needs (Unified Catalog).
4. Collaborate with your technical and data teams to show what you want to do with the data and find what data fits your data products.
5. Create a collection for your technical partner (Data Map).
6. Have your technical partners register and scan the data source (Data Map).
7. Add the recommended assets to your data product to showcase in the Unified Catalog.

---

## Permissions hierarchy

Before you start assigning roles and permissions to users in your organization, it's helpful to understand the relationship between the primary data governance solutions, Unified Catalog and Data Map, and the permissions granted by the roles for each solution.

![Data governance permissions heirarchy.](media/datagov-perms-heirarchy.png)

- **Tenant, or organization**: Users who own the Microsoft Purview instance and need access to maintain its permissions and information.
- **Data Map**: Grants permissions to create and administrate technical domains and collections.
- **Unified Catalog**: Grants users permission to create governance domains or access data estate health.
- **Governance domain**: Grants permissions for objects within a governance domain, such as glossary terms or data products.

When you're ready to start assigning roles and permissions, [Data governance roles and permissions](data-governance-roles-permissions) gives detailed instructions. To guide you through the process, we recommend beginning with [Getting started with data governance](data-governance-get-started).