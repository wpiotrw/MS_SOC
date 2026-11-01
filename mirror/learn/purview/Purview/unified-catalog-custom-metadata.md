---
layout: Conceptual
title: Custom metadata (preview) in Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-custom-metadata
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2025-07-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
ai.usage: ai-assisted
description: Learn about the different types of custom metadata (preview) in Microsoft Purview Unified Catalog and how to apply it to your data assets and business concepts.
locale: en-us
document_id: 43d07fbe-ebc8-a20b-b08f-b9efe75290cd
document_version_independent_id: 43d07fbe-ebc8-a20b-b08f-b9efe75290cd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-custom-metadata.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-custom-metadata
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-custom-metadata.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f35f8d20-6a39-e7ff-3049-f06fe3d7d127
---

# Custom metadata (preview) in Microsoft Purview Unified Catalog | Microsoft Learn

Custom metadata plays a crucial role in data governance by providing you with the flexibility to add user-defined context to describe and organize your data. In Microsoft Purview Unified Catalog, you can define and apply organization specific business attributes to your data assets and business concepts that foster better organization, accessibility, and utilization of your data. The benefits of using custom metadata include:

- **Enhanced data discovery**: Custom metadata simplifies the search and retrieval of data by allowing users to apply specific tags, which are **attributes** in Unified Catalog, that make datasets easier to locate.
- **Help with compliance**: Organizations can use custom attributes to track regulatory requirements or flag sensitive data to help ensure adherence to legal and industry standards.
- **Streamlined communication**: Custom metadata facilitates better collaboration among teams by providing clear descriptions and classifications of data assets.
- **Optimized data utilization**: By categorizing data assets effectively, organizations can prioritize the use of high-value data for analytics and decision-making.

## Custom metadata usage scenarios

Here are some examples of how you can use custom metadata to help achieve better data governance and compliance:

**Example 1: Healthcare industry**

A hospital's data catalog includes patient records, medical research, and operational data. By implementing custom metadata, administrators add attributes such as "Patient Age Group," "Disease Category," and "Research Priority Level" to the datasets. This approach enables the hospital to segment data effectively for clinical studies, prioritize urgent cases, and comply with healthcare regulations like HIPAA.

**Example 2: Financial services**

A financial institution uses custom metadata to govern its risk assessment data. Attributes like "Risk Rating," "Investment Sector," and "Regulatory Compliance Status" help ensure that analysts can quickly identify high-risk investments, provide insights into sector-specific trends, and maintain legal compliance with financial regulations.

**Example 3: Academic institutions**

Universities use custom metadata to manage their research databases. Attributes like "Research Field," "Funding Source," and "Publication Status" enable academic departments to track progress, allocate resources effectively, and collaborate across institutions.

**Example 4: AI and compliance**

Organizations can include AI and compliance related attributes to define various data product types. AI-related attributes might cover aspects such as algorithm transparency, explainability, and model performance metrics, while compliance attributes might address regulatory requirements, data privacy, and ethical considerations. By incorporating these factors, organizations can ensure their data products are robust, compliant with laws and standards, and aligned with responsible AI practices.

**Example 5: Tracking translations**

Language can be a pivotal attribute to describe and discover glossary terms in different languages. By incorporating multilingual capabilities into metadata attributes, organizations can ensure seamless communication and understanding across diverse linguistic groups. This approach not only facilitates global collaboration but also enhances accessibility, enabling users to interact with data in their preferred language while maintaining consistency and clarity in terminology usage.

## Types of custom metadata: attributes

Currently, you can use two types of custom metadata:

1. [Business concept attributes](unified-catalog-attributes-business-concept): Attributes you create and apply to business concepts, such as governance domains, data products, critical data elements, glossary terms, and objectives and key results.
2. [Data asset attributes](unified-catalog-attributes-data-asset): Attributes you create and apply to data assets.

You can find, create, and manage your custom metadata at **Unified Catalog** &gt; **Catalog management** &gt; **Custom metadata (preview)**.

Each type of attribute appears on its own tab on the **Custom metadata (preview)** page. The attribute list on each tab is organized by attribute group, and each attribute is nested within its group.

## Get started

- [Create business concept attributes](unified-catalog-attributes-business-concept)
- [Create data asset attributes](unified-catalog-attributes-data-asset)