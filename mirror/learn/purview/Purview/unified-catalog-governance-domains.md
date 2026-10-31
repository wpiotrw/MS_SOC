---
layout: Conceptual
title: Governance Domains in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-governance-domains
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2024-04-08T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand governance domains in Microsoft Purview Unified Catalog and how they help you describe and govern your data estate.
locale: en-us
document_id: d98c5f2f-1a30-a772-35a0-d252ab87dbd9
document_version_independent_id: d98c5f2f-1a30-a772-35a0-d252ab87dbd9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-governance-domains.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-governance-domains
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-governance-domains.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 76dc4d5d-5914-8171-883d-8bba0514c1b9
---

# Governance Domains in Unified Catalog | Microsoft Learn

A governance domain in Microsoft Purview Unified Catalog provides context for your data assets and makes it easier to scale data governance practices.

Data ownership is a central aspect of data governance. Controlling access and data use are core tenets of any successful governance program. Often, IT teams store and maintain data assets even though business teams own and use the data. That creates a gap between how data should be discovered and maintained and the teams that actually use it. Unified Catalog helps bridge that gap, but business owners still need clear context about their data assets and repeatable ways to scale governance across a growing data estate.

To address these needs, Unified Catalog introduces governance domains.

## Overview and elements

At its simplest, a governance domain is a boundary that enables the common governance, ownership, and discovery of [data products](unified-catalog-data-products) and business concepts like [glossary terms](unified-catalog-glossary-terms), [objectives and key results (OKRs)](unified-catalog-okrs), or [critical data](unified-catalog-critical-data-elements). The goal is to empower a governance domain owner to manage their data products and concepts, and establish rules for their access, use, and distribution. With this goal in mind, you could establish many kinds of governance domains:

- Fundamental business areas, such as human resources, sales, finance, and supply chain.
- Overarching subject areas, such as product and parties.
- Boundaries based on organizational functions, such as customer experience, cloud supply chain, and business intelligence.

In Microsoft Purview, governance domains are flexible so your organization can build the boundaries that make the most sense for your data. But once you've created them, how do they provide context or assist with data governance?

### The parts of a governance domain: business concepts

A governance domain has a name and description, which helps users quickly understand what parts of your organization the governance domain represents. The domain also has owners who govern and maintain the domain and its assets.

Governance domains also contain the following business concepts:

- [Data products](unified-catalog-data-products): Packaged sets of data assets (tables, files, Power BI reports) grouped for discovery and reuse.
- [Glossary terms](unified-catalog-glossary-terms): Business terms that provide context and can carry access and data-handling policies that determine how data should be managed and discovered.
- [Objectives and key results (OKRs)](unified-catalog-okrs): Metrics that describe the value of your data with measurable values and goals.
- [Critical data elements (preview)](unified-catalog-critical-data-elements): Logical groupings of important columns (for example, mapping "CustID" and "CID" to a single "Customer ID" concept) that require elevated governance.

### Types of governance domains

These are the supported out-of-the-box governance domain types:

- Functional unit: Organizations or business units, such as sales, marketing, or finance.
- Line of business: Products or services being sold, such as Xbox, Office, or Azure, and different markets or subsidiaries.
- Data domain: Key organization-wide entities, such as customers or employees.
- Regulatory: Compliance-related domains such as GDPR, SOX, or HIPAA.
- Project: Collaborative programs across the organization.

## How governance domains provide business context

Governance domains provide context for your data products, which are combinations of files, tables, reports, and other assets, by defining an overarching category for them. For example, someone who needs supply delivery schedules can limit their search to the Supply Chain domain instead of scanning the entire catalog.

Each governance domain can define OKRs to describe the business value of its data products and set measurable goals. Domain owners can prioritize data products based on those goals so users understand how data supports organizational strategy.

This structure provides familiar landmarks for business users and lets domain owners tailor and scale governance as the data estate grows.

## How governance domains scale data governance

In a flat catalog, governing each asset individually is costly and unsustainable. Governance domains provide boundaries where policies can be applied broadly to data products.

The key to propagating governance policies is the use of [glossary terms](unified-catalog-glossary-terms). Glossary terms provide business-context labels that improve discovery. Glossary terms are defined within a governance domain and can be applied to any data product in that governance domain

Data owners and data stewards don't have to traverse an entire data estate to maintain governance. They can apply terms across a governance domain they understand and know that when these terms are attached to a data product, the right policies will automatically fall into place. As an example: In the Human Resources governance domain, the "Feedback Results" term denotes returned company-wide feedback queries that are considered sensitive. A designated review team evaluates access requests. A data access policy on the Feedback Results term is applied automatically to any data product labeled with that term when users request access.

Governance domain owners and data stewards define policies once and rely on terms to propagate those practices across the data estate, ensuring consistent enforcement even as new assets are added.

Governance domains use existing business context to make data more discoverable and consistently governed as it grows.