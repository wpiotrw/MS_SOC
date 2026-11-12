---
layout: Conceptual
title: Data Products in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-products
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
description: Learn about data products in Microsoft Purview Unified Catalog and how they help you describe and govern your data estate.
locale: en-us
document_id: 0e2a65a7-4aeb-57ae-a9d8-b99acbd2e339
document_version_independent_id: 0e2a65a7-4aeb-57ae-a9d8-b99acbd2e339
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-products.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-products
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-products.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: fdbf8d45-0dc0-6b3e-fe70-9d3adb16723b
---

# Data Products in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

A data product is a group of data assets, such as tables, files, and Power BI reports, with a defined use case that you can share with other users.

In Microsoft Purview, data governance isn't only a way to make sure your data is secure and compliant, but it's also a tool to accelerate your data's business value. Cataloging data in your estate makes it possible to better manage data for right use, but it also provides a complete picture of your data landscape. Now that there's a list of every available data asset, users no longer have to rely on networking or team knowledge to find what they need; they can search the catalog themselves. But giving every user a raw list of all available data is overwhelming and not inherently useful. Even with good descriptions, tagging, and glossary terms, it can be hard to know what you're looking for. And for a complete data visualization you probably need several data assets, and not just one. As Microsoft Purview Unified Catalog grows, context needs to grow alongside it to make it easier for your users to find and request access to the data they need.

To provide scalable data context and access management, Microsoft Purview is introducing the data product.

## What's a data product?

A data product is a business concept with a name, description, owners, and most importantly a list of associated data assets. The data product provides context for these assets, grouping them under a use case for data consumers. A governance domain can house many data products but a data product is managed by a single [governance domain](unified-catalog-governance-domains) and can be discovered across many domains.

A successful data product makes it easy for data consumers to recognize valuable data using their day-to-day language, and at the same time streamlines ownership responsibilities for those data assets. Let's explore what that looks like.

## Scalable data context

As an example, a data scientist creates a set of data assets for their data model to consume and they want others to be able to use the same dataset.

Without data products, the data scientist can use Unified Catalog to add a glossary term to all the relevant data assets. A user might not know which glossary term to search, so it might be best to add a description to each data asset to make it more relevant in searches for similar information. But both additions don't guarantee that other users see all the associated data assets. They might group in other assets that aren't as relevant, or miss a critical data piece, and spend time repeating research the original data scientist already performed.

With a data product, a data scientist can create a data product that lists all the assets used to create their data model. The description provides a full use case, with examples or suggestions on how to use the data. The data scientist is now a data product owner and they've improved their data consumer's search experience by helping them get everything they need in this one data product.

## Scalable data governance

Data products streamline governance for data assets. Using the same example of a data scientist who creates a set of data assets:

Without data products, if a user wants access to the data assets for the data set, they must request access to each data asset individually. A data owner might know that these assets are used for machine learning models, but if they make any changes to policies around their security and use cases, they must update each asset individually.

With data products, a user finds the data product and requests access to the data product. After approval, they get access to all the associated data assets. If a data owner puts more approval or data use policies in place around datasets for machine learning, they only need to apply the new policies to the data product. The policies automatically trickle down to the assets.

Data products are also associated with business health controls and [OKRs](unified-catalog-okrs). These controls allow data owners to assess data health and prioritize assets that need attention. They also help assess which data assets provide business value. This support not only helps progress towards complete data governance in your estate but also encourages developing business value from your data. Assets are no longer abstract but tied to real use cases and business objectives that your team can focus on.

### Data access policies

Data security and access is the core tenant of successful data governance. But to implement data governance and successfully drive data use (and therefore value), the data access process needs to be secure, convenient, and customizable to all scenarios across your data estate. Some data should be widely useable and accessible, and some needs to be under rigorous approval and monitoring to ensure right use.

Each data product has an access policy that determines how users request access, the terms of use for the data, and who should approve access to the data. Each of these access policies is customizable for appropriate use and will evolve to cover more use cases in the future. All users need to do is select **Request Access** inside a data product. They automatically go through the process to agree to terms of use and get approval from correct parties.

For more information about access for data products, see [the article on managing Unified Catalog access policies in Microsoft Purview.](unified-catalog-data-product-access-policies)