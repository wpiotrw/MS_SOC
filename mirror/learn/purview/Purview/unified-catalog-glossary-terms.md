---
layout: Conceptual
title: Glossary Terms in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-glossary-terms
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how glossary terms in Microsoft Purview Unified Catalog help you describe and govern your data estate.
locale: en-us
document_id: 35acd184-4c31-3edd-341c-bce10ceab8ce
document_version_independent_id: 35acd184-4c31-3edd-341c-bce10ceab8ce
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-glossary-terms.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-glossary-terms
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-glossary-terms.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 390fa16f-0412-c164-9d09-41159317b99a
---

# Glossary Terms in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Glossary terms in Microsoft Purview Unified Catalog are active values that provide context. They also apply policies that determine how you manage, govern, and make your data discoverable for use.

If you already use Microsoft Purview, you're familiar with the business glossary in general. It provides a vocabulary for business users. It consists of business terms that can be related to each other and allows them to be categorized so that they can be understood in different contexts. This structure helps abstract the technical jargon associated with the data repositories and allows the business user to discover and work with data in the vocabulary that is more familiar to them. Microsoft Purview takes these terms a step further by allowing them to play an active role in data governance. Now data stewards can use terms to apply policies and scale data governance as their data estate grows.

Note

You can now bring classic glossary terms into Unified Catalog and link all of your terms to data assets and columns. Follow the instructions to [migrate glossary terms from the classic data governance experience and enable the curation of data assets (preview)](unified-catalog-glossary-terms-migrate).

## What is a glossary term?

Terms are individual concepts that define the business, processes, and systems used in an organization. You can apply them across a data estate, relating to data assets and [data products](unified-catalog-data-products) to provide business context to your users. A technically named SQL table becomes less mysterious once it's linked to your "Account" business term, since users can immediately see what aspect of the business it's related to.

Create glossary terms under [governance domains](unified-catalog-governance-domains) to impart context specific to each part of your organization. Both sales and marketing might use the same term to mean different things, and your governance domains help your team differentiate between those meanings.

After you create glossary terms, you can link them to data products, data assets, columns, and critical data elements to provide context and to provide specific data governance based on business context. It's easy to understand how a term and its definition provide business context to a data product or asset, but how do terms provide data governance? Terms are an active part of Microsoft Purview that provide data governance by now containing policies.

Policies in a business term apply specific business health goals, data governance requirements, and terms of use to any data product or asset that you apply the term to.

## How does this scale data governance?

Glossary terms were previously static terms that you applied to define a concept. But now they can be activated as objects that attach to policies that determine how you manage, govern, and make your data discoverable for use. Terms for data access and data health controls can trickle down to data products. Today, data stewards apply policies on single data objects. That's not scalable. Now a data steward can create a single term and create its policies. They might not know where to apply that term, but any time they apply the term to a data product or asset, all the associated policies are automatically applied. Active terms allow your data estate to naturally scale, and maintain security and discoverability without overburdening your data stewards.