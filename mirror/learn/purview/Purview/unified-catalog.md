---
layout: Conceptual
title: Learn about Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2024-08-28T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Explore how you can build good data governance practices across your data estate using Microsoft Purview Unified Catalog.
locale: en-us
document_id: 662c3a79-037d-875f-15e0-321b09336167
document_version_independent_id: 662c3a79-037d-875f-15e0-321b09336167
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/54918a83-0404-4863-9c91-715186c1f582
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/b26f5f7a-0913-4a95-8337-ed7543902f2d
platformId: 35057fa9-c3cd-9a28-7100-8ed84c880702
---

# Learn about Microsoft Purview Unified Catalog | Microsoft Learn

Tip

The new Unified Catalog experience is rolling out across environments. If you don't see it yet, [check the schedule for your region](unified-catalog-regions). Make sure you've [upgraded to the enterprise version of the new Microsoft Purview experience](data-governance-free-version-upgrade-to-enterprise) in order to access the new experience when it's available in your region.

Microsoft Purview Unified Catalog provides a platform for data governance and enables you to drive business value creation in your organization.

Historically, data governance was a defense mechanism, a way to make sure your data is secure and compliant. But good data governance makes your data more visible to your users and provides many opportunities to reunite your business with the data that fuels it.

Most importantly, all of these new features are available in a single, integrated SaaS framework. Users shouldn't need to switch between applications to practice good data governance. We're working toward a solution where everything is in one place with experiences for data consumers, data stewards, and data owners.

## Data governance for the era of AI​

This era of artificial intelligence means that you have more data than ever, more ways to use it, and even more motivation to make sure you properly use and secure it. It's a task many organizations already struggle with, without the added complexity of using AI tools.

Governing data for an entire organization requires both rigor and flexibility. Clean, secure data requires consistency, but your teams' needs are unique for access and management. Because of this, use a federated governance approach: provide a centralized place to develop data safety, quality, and standards, but provide tools to create self-service access control, discoverability, and maintenance. Federated data governance spreads ownership across your business, reducing bottlenecks and encouraging participation in the life cycle of managing, governing, consuming, and applying data.

Data governance isn't just a gatekeeping function. When practiced well, it also accelerates data value creation. Your data users, stakeholders, and subject matter experts have crucial insights to the data-to day operations of your organization. Good data governance can apply that expertise to reasonably scale the practice of data governance across your entire organization, including your nontechnical functions and business users. Said another way, good data governance utilizes your whole team and matches your data with your data-to-day business functions.

The point is both to reveal your data's business value and simplify its management even as your organization and data estate grow. Here's how it can help each sector of your business:

- For organization-wide data consumers:

    - Data discovery - help you easily find the data you need
    - Secure access - facilitates safe access to your data
    - Data understanding - providing what you need to know about the data before and while you use it
- For data owners and stewards:

    - Data curation and management - helps you deliver high quality data that's easy to understand and safely access for organization-wide applications
    - Responsible data use - helps you ensure that your data is used by intended users for intended purposes
    - Impact analysis - understand action anomaly states impacting your data
- For data officers and CxO stakeholders:

    - Data value creation - maximize value creation from your data while reducing operations spend
    - Data estate standardization - create common controls across your data estate with federated accountability so your data is healthy and safe.

## Governance with the Unified Catalog

The new Unified Catalog experience lets you explore and understand your data categorized by governance domains. You can search through an AI-powered copilot and subscribe to data products that come equipped with all the data you need and the tools to safely access it. Over the last couple of years, we invested in a strong platform that has an inventory of all your data assets, their metadata, and their lineage so you can understand the topography of your data estate. Now we're providing better tools to manage it as it grows, and more points to surface that data to your business, to make use of it in the day-to-day.

Here are the tools that Unified Catalog provides to meet these data governance basics:

| Data governance principle | Catalog solution | Description |
| --- | --- | --- |
| **Data access** - quickly provide right access and enforce right use to balance safety and innovation. | Unified Catalog access policies | Provides tools to manage self-service access requests that pairs data with compliance standards and right-use requirements. |
|  | Critical data elements​ | Establish access policies on critical types of information to be applied across your data estate. |
|  | Glossary terms | Attach access policies with your business vocabulary to promote right-use. |
| **Data curation** - organizing, annotating, and publishing your data so that it's safely accessible, reusable, and protected. | Governance domains | Organize data by business concepts, to make data more accessible and distribute ownership. ​ |
|  | Data products | Group related data assets so users can easily find the full data picture. |
|  | Health actions | Take action to bring your data up to good governance standards. |
| **Data discovery** - users can find the data they need for day-to-day business and innovation. | [Search](unified-catalog-data-assets-search) & [browse](unified-catalog-data-assets-search#browse-the-unified-catalog) Unified Catalog | Search by governance domain, by data product, by keyword, or use the AI powered copilot to find what you need. ​ |
|  | Self-service access requests | Get access to all the data you need with a single request from inside Unified Catalog. ​ |
| **Data health** - data quality standards are maintained across your estate, and there's an active data lifecycle keeping your data fresh and secure. | Health management ​ | Ready-made reports provide the status of your data estate, and your data governance progress, at a glance. |
|  | Critical data elements​ | Track important information to standardize and govern use. |
|  | Data quality​ | Set quality rules from the top down to simplify distribution and provide snapshot progress tracking. |
|  | Health controls | See how your data estate measures up to governance standards. |
|  | OKRs | Map data health and governance goals to your business objectives. |
| **Data understanding** - data has quality descriptors that help users understand what the data is and how it should be used. | Data products | Provide business context for a set of data assets. |
|  | Glossary terms | Attach your day-to-day business vocabulary to your data assets. |
|  | OKRs | Link data usage directly to your business objectives. |

## Get started

Ready to get started making your information clean, valuable, and accessible to your business users? We've created a guide to take you from zero to a fully integrated Unified Catalog in [Get started with data governance](data-governance-get-started).

## Unified Catalog features

Now that you understand how Unified Catalog supports good data governance practice, and how the features promote data governance principals, explore the features in more detail:

- Governance domains: An organizational object that provides context for your data assets and makes it easier to scale data governance practices.
    - Unified Catalog access policies: Provide secure, self-service access to data products.
    - Critical data elements: Logically describe your key business data to govern them.
    - Glossary terms: Active values that provide context but also apply policies that determine how your data should be managed, governed, and made discoverable for use.
- Data products: A kit of data assets (tables, files, Microsoft Power BI reports, and more) that provides assets with a use case for ease of discovery and understanding.
- OKRs: Drive business value from your data and directly promote data governance objectives.
- Data estate health updates: Expanded features to provide new insights and encourage governance ownership.
    - Health controls: Track your governance progress with a health score.
    - Health actions: Follow these actions in your data estate to improve your governance score.
- Data quality: Set rules and get scores to get insight across your data estate.

### Governance domains

Governance domains let you explore data through business concepts, like Marketing or Finance. This approach makes data more accessible to everyone.

Governance domains offer a new way to organize your data estate. You want and need to access your entire data estate, but a single, uncategorized list is overwhelming. A governance domain is a boundary that aligns your data estate to your organization. Think of it as a mini catalog inside Unified Catalog.

Inside your governance domain are the terms that define users' day-to-day work. There are objectives and key results (OKRs) to align your organization's goals with your data. There are data products that make data discovery more straightforward for your users.

The goal of the governance domain is to organize your Unified Catalog so that it not only drives healthy data governance but also ties your data directly to its business value and your objectives.

For more information, see [the overview of governance domains](unified-catalog-governance-domains).

#### Access policies

Unified Catalog access policies let you manage access to your data products and set up a system to provide access to users who request it. Promote innovation and flexibility in your data estate by creating self-service access opportunities, while upholding security and right-use standards. All in the Unified Catalog.

For more information, see [how to create and manage Unified Catalog access policies](unified-catalog-data-product-access-policies).

#### Critical data elements

Critical data elements are a logical grouping of important pieces of information across your data estate. For example, a "Customer ID" critical data element can map "CustID" from one table and "CID" from another table into the same logical container. These groupings can make data easier to understand and promote standardization. You can attach data quality rules and access policies to these elements to further secure sensitive information across your data estate.

For more information, see [how to create and manage critical data elements](unified-catalog-critical-data-elements).

#### Glossary terms

If you use Microsoft Purview, you're familiar with glossary terms and how they provide critical business context to your data assets. We've taken them from static objects to active objects that help define how you should manage, govern, and make your data assets discoverable. Policies within these terms allow data stewards to scale governance across your entire data estate. Terms applied to data products trickle down to the data assets and automatically secure those resources with their attached policies.

For more information, see [the overview of glossary terms](unified-catalog-glossary-terms).

### Data products

Data products improve catalog organization by grouping data assets together, such as tables, files, and reports, so users can easily discover them. You no longer need to request access to 15 different tables to build a data model. When one user researches and creates a viable data product, all other users benefit from that work. They can find and request access to the data in that product and have everything they need in one place.

For more information, see [the overview of data products](unified-catalog-data-products).

### OKRs

Objectives and key results (OKRs) link data products directly to your objectives. They bridge the gap between your business and Unified Catalog. Use data to discover and track objectives in your business. Unified Catalog makes it easy to see those connections and track your goals.

For more information, see [the overview of OKRs](unified-catalog-okrs).

### New data estate health features

Health management has a few new features for you to implement to enhance your data governance strategy and management.

#### Health controls

Track your journey to complete data governance by monitoring health controls. Health controls measure your current governance practices against standards and give your data estate a score.

Learn more about [data health controls](unified-catalog-controls).

#### Health actions

Health actions are concrete steps you can take to improve data governance across your data estate. The actions are provided in a single list that can focus your data governance journey and democratize ownership. Completing these actions improves data quality and discoverability across your data estate.

Learn more about [viewing data health management actions](unified-catalog-data-health-management-actions-page).

### Data quality

Data quality enables your organization to set rules through your governance domains, data products, and the data assets themselves. These rules trickle down across your environment so you can better evaluate your data across your data estate. You get data quality scores at the asset, data product, and governance domain levels, so you have full insight into your data estate.

Get an [overview of data quality](unified-catalog-data-quality).