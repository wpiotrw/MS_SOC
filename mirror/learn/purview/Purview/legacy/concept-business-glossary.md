---
layout: Conceptual
title: Understand business glossary features in the classic Microsoft Purview governance portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-business-glossary
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article explains what business glossary is in the classic Microsoft Purview governance portal.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: evwhite
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: concept-article
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: c4b78aa2-a1ea-c267-344d-69b5595b34e2
document_version_independent_id: c4b78aa2-a1ea-c267-344d-69b5595b34e2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-business-glossary.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-business-glossary
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-business-glossary.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9293d16c-0308-5a16-a81a-6d73f5419fd6
---

# Understand business glossary features in the classic Microsoft Purview governance portal | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Tip

Microsoft Purview has a new experience! If you're a new Microsoft Purview customer, or if you want more information, see our [article on the new portal](../purview-portal) or the article about our new [data governance experience](../unified-catalog) and our new [glossary terms](../unified-catalog-glossary-terms-create-manage).

A **glossary** provides vocabulary for business users. It consists of business terms that can be related to each other and allows them to be categorized so that they can be understood in different contexts. These terms can be then mapped to assets like a database, tables, columns etc. This helps in abstracting the technical jargon associated with the data repositories and allows the business user to discover and work with data in the vocabulary that is more familiar to them.

You can find Microsoft Purview's classic glossaries in the [classic Microsoft Purview governance portal](https://purview.microsoft.com/) in the Data Catalog under **Business Glossary**.

![Screenshot of the Data Catalog page in the Microsoft Purview portal](../media/concept-business-glossary/glossary-location.png)

A **business glossary** is a collection of terms. Each term represents an object in an organization and it's highly likely that there are multiple terms representing the same object. A customer could also be referred to as client, purchaser, or buyer. These multiple terms have a relationship with each other. The relationship between these terms could be:

- synonyms - different terms with the same definition
- related - different name with similar definition

The same term can also imply multiple business objects. It's important that each term is well-defined and clearly understood within the organization.

## Relationships between terms

Microsoft Purview supports these out-of-the-box relationships for terms:

- Parent/child term
- Acronym
- Synonyms
- Related terms

**Relationship definitions in the glossary are bi-directional:** Every relationship between terms is a two-way relationship. This means that if term A is related to term B, then term B is also related to term A.

Anytime you populate a relationship in one direction, Purview automatically adds the reverse relationship for you. For example, if you add term A as a synonym for term B, Purview automatically adds term B as a synonym for term A.

## Glossary vs classification vs sensitivity labels

While glossary terms, classifications and labels are annotations to a data asset, each one of them has a different meaning in the context of catalog.

### Glossary

As stated above, Business glossary term defines the business vocabulary for an organization and helps in bridging the gap between various departments in your company.

### Classifications

Classifications are annotations that can be assigned to entities. The flexibility of classifications enables you to use them for multiple scenarios such as:

- understanding the nature of data stored in the data assets
- defining access control policies

Microsoft Purview has more than 200 system classifiers today and you can define your own classifiers in catalog. As part of the scanning process, we automatically detect these classifications and apply them to data assets and schemas. However, you can override them at any point of time. The human overrides are never replaced by automated scans.

### Sensitivity labels

Sensitivity labels are a type of annotation that allows you to classify and protect your organization's data, without hindering productivity and collaboration. Sensitivity labels are used to identify the categories of classification types within your organizational data, and group the policies that you wish to apply to each category. Microsoft Purview makes use of the same sensitive information types as Microsoft 365, which allows you to stretch your existing security policies and protection across your entire content and data estate. The same labels can be shared across Microsoft Office products and data assets in Microsoft Purview.

For more information about sensitivity labels, see: [Learn about sensitivity labels](../sensitivity-labels)