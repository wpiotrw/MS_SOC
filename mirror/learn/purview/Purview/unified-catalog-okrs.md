---
layout: Conceptual
title: Objectives and Key Results (OKRs) in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-okrs
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
description: Learn how objectives and key results (OKRs) in Microsoft Purview Unified Catalog help you describe and govern your data estate.
locale: en-us
document_id: af7851f9-d043-5c8e-5d85-e191447e7ff7
document_version_independent_id: af7851f9-d043-5c8e-5d85-e191447e7ff7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-okrs.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-okrs
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-okrs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c0439c36-80e3-415f-8e4c-6951e3f1b136
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/2812d699-d85f-4a7f-839d-44e218b35d24
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 6628f6bd-469d-22ef-93a4-c81cec0f0fb1
---

# Objectives and Key Results (OKRs) in Unified Catalog | Microsoft Learn

Objectives and key results (OKRs) (preview) in Microsoft Purview Unified Catalog are trackable business objectives tied to [governance domains](unified-catalog-governance-domains) and [data products](unified-catalog-data-products) to emphasize the value of business data.

Data governance is an important practice that organizations often overlook unless they have strict compliance requirements. While organizations seem to understand the value of data, they don't always recognize the role data governance plays in promoting healthy, useful data. As data estates become overgrown with ungoverned information, valuable data gets neglected.

OKRs link data products directly to real business objectives to bridge the gap between the business and the data estate. Data governance isn't just an IT task or engineering best practice, it's a critical part of value generation. To make use of your data, you need to maintain your data estate, and you can share the work among the experts who know the data best.

## What is an OKR

An OKR is the goal or desired outcome of a governance domain; for example, a 10% raise in sales or a 3% reduction in support cases. Objectives should relate to everything an organization does and should define how they achieve their outcomes.

### Parts of an OKR

Unified Catalog OKRs have several parts:

- Owners: The users responsible for maintaining the objective.
- Definition: An overarching description of your objective, which can be as broad as “Increase sales,” or as specific as "Use marketing campaigns to increase sales in the first quarter."
- Target date: When you expect to achieve your goal.
- Key results: The measurable, time-bound goals associated with your objective. These should be how you track progress toward your objective.

### Owner

These users are responsible for maintaining a business objective. They could be the leaders of the business and should have knowledge of how the business functions and where it's headed. Multiple owners are encouraged to provide a complete perspective on the business and to support each other in owning the objective.

### Definition

Good objectives are specific and achievable in a time frame. The definition is a high-level text description of the mission or current goal of the team or process, and why it matters. The description itself should be succinct, but it isn't enough on its own. It requires a way to measure the goal's achievement and progress, which are the key results.

### Target date

The target date is when you expect to meet the goal. This date helps drive progress toward the goal and encourages achievable goals, since you must complete them within a specific time frame.

### Key results

Key results show how you measure progress toward your objective. Your objective might have several key results that roll up to your overall goals.

A good metric for goals and objectives uses the SMART acronym:

- **S**pecific
- **M**easurable
- **A**chievable
- **R**ealistic
- **T**ime-bound

To tie your objectives to real results, key results have several features:

- Result: A statement that encompasses the specific, measurable result you expect.
- Progress status: Is your progress on track, behind, or at risk? This status helps your business identify and prioritize issues.
- Progress amount: Where do you stand in relation to your goal? You need to use specific numbers or percentages to represent this amount.
- Goal amount: What's your goal? You need to use specific numbers or percentages to represent this amount.
- Maximum amount: What's the maximum achievable?

You can edit these values so business users and owners can update their goals and results over time. These values are also converted to graphics, so business owners can see at a glance how their organization is progressing toward their goals and where there might be blockages.

### Related data products

You can connect an OKR to all data products that are relevant to that objective. It can be the data used to measure that OKR, or the data used to investigate new business opportunities. Data consumers can use this connection to see all data related directly to their business objectives, and business owners can track the health of the data directly associated with their goals.

## How OKRs generate business value

Data governance directly supports these business objectives. After all, data helps you both track and achieve these objectives. You can also use data to uncover new areas for improvement and to guide which objectives need prioritization. OKRs help to directly tie data to its business value.

For example: Your marketing team develops an email campaign results [data product](unified-catalog-data-products) that they use to track the effectiveness of their email marketing campaigns. Your marketing [governance domain](unified-catalog-governance-domains) has a "Customer Response" OKR, with the goal of at least 20% customer response to email, telephone, and mail campaigns sent out. A business owner connects the "Customer Response" OKR to the email campaign results data product and creates an "Email Campaign Response" key result to measure the current percentage of customer response. When the marketing team tracks their quarterly progress, their objectives directly tie to the data they use to track that information. They're directly aware of the health and value of the data associated with their OKRs and naturally encouraged to invest in the health of the data.

This approach not only encourages your users to focus on their objectives but also promotes health, security, right use, and data discovery directly related to your business objectives. Your business and your data estate grow together naturally to support your goals.