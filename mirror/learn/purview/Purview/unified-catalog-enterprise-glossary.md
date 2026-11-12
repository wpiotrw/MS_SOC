---
layout: Conceptual
title: Enterprise Glossary in Unified Catalog (Preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-enterprise-glossary
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
description: Learn how to use the enterprise glossary (preview) in Microsoft Purview Unified Catalog to quickly find published business concepts.
locale: en-us
document_id: 7407f391-56ea-dc11-02d2-47d9849cc4ee
document_version_independent_id: 7407f391-56ea-dc11-02d2-47d9849cc4ee
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-enterprise-glossary.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-enterprise-glossary
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-enterprise-glossary.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 36abbacb-8ba0-6776-d20e-30dda27187b8
---

# Enterprise Glossary in Unified Catalog (Preview) | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article helps you understand the Enterprise glossary (preview) area of Microsoft Purview Unified Catalog, where you can browse and search for published business concepts, such as [governance domains](unified-catalog-governance-domains), [glossary terms](unified-catalog-glossary-terms), [critical data elements](unified-catalog-critical-data-elements), and [objectives and key results (OKRs)](unified-catalog-okrs).

As a consumer of the catalog, you can discover data products through the search experience and through the enterprise glossary experience that links different business concepts to data products. This experience has three tabs for glossary terms, critical data elements, and OKRs, and gives you a consolidated view of all the published concepts within. Once you find the concept you're looking for, you can view the related data products and request access to the ones you need.

## Prerequisites

To browse the enterprise glossary, you need a [catalog reader role](data-governance-roles-permissions#catalog-level-permissions).

## Search for business concepts in the catalog

You can browse and search for published business concepts within Unified Catalog.

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), open **Unified Catalog**.
2. Under **Discovery**, select **Enterprise glossary**.
3. Select the **Governance domains**, **Glossary terms**, **Critical data elements**, or **OKRs** tab to learn more about published concepts under each concept. 
    Note

    - You can visualize any parent/child relationships in a tree-like hierarchy within the **Glossary terms** tab by selecting **Tree** in the views drop-down.
    - The list view displays all published glossary terms but the tree visualization doesn't display terms with unpublished parents.

Search for any concept by name in the search bar. You can sort the results in ascending or descending alphabetical order, and filter results by governance domain, owner, or any other available filter.

Select a published concept to view its related concepts, such as data products.

## Filter your view by custom attributes

Use [business concept attributes](unified-catalog-attributes-business-concept) as a filter when browsing and searching for business concepts.

1. In the Enterprise glossary, select the tab for the concept you want to search. If you're searching in a governance domain, select **View all** on a business concept card.
2. Select **Add filter**.
3. At **Filter**, select an attribute name from the dropdown list.
4. At **Operator**, select a condition, such as **Equals** or **Starts with**, which varies based on the kinds of values allowed by the attribute.
5. At **Value**, enter your value.
6. Select **Apply**.