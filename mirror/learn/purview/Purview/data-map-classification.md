---
layout: Conceptual
title: Data classification in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-classification
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2024-04-17T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand the concepts behind data classification in Microsoft Purview Data Map.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 4a3fbb61-2373-0f9c-6a76-7b7dac7ee935
document_version_independent_id: 4a3fbb61-2373-0f9c-6a76-7b7dac7ee935
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-classification.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-classification
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-classification.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: cf34a8e8-65b6-dc14-154a-ac87c8426d96
---

# Data classification in Microsoft Purview Data Map | Microsoft Learn

Data classification in Microsoft Purview Data Map is a way of categorizing data assets by assigning unique logical tags or classes to the data assets. Classification is based on the business context of the data. For example, you might classify assets by *Passport Number*, *Driver's License Number*, *Credit Card Number*, *SWIFT Code*, *Person’s Name*, and so on.

When you classify data assets, you make them easier to understand, search, and govern. Classifying data assets also helps you understand the risks associated with them. This in turn can help you implement measures to protect sensitive or important data from ungoverned proliferation and unauthorized access across the data estate.

Data Map provides an automated classification capability while you scan your data sources. You get more than 200+ built-in system classifications and the ability to create custom classifications for your data. You can classify assets automatically when they're ingested as part of a configured scan, or you can edit them manually in the Microsoft Purview governance portal after they're scanned and ingested.

## Uses of classification

Classification is the process of organizing data into *logical categories* that make the data easy to retrieve, sort, and identify for future use. This can be important for data governance. Among other reasons, classifying data assets is important because it helps you:

- Narrow down the search for data assets that you're interested in.
- Organize and understand the variety of data classes that are important in your organization and where they're stored.
- Understand the risks associated with your most important data assets and then take appropriate measures to mitigate them.

Following image shows classification applied while scanning on the *Customer* table in Azure SQL Database.

[![Screenshot that shows the classification of the 'Customers' table in Azure SQL Database.](media/concept-classification/classification-customers-example-1.png)](media/concept-classification/classification-customers-example-1.png#lightbox)

## Types of classification

The Microsoft Purview governance portal supports both system and custom classifications.

- **System classifications**: 200+ system classifications supported are out of the box. See the full [list of available system classifications](data-map-classification-supported-list).

    In the example in the preceding image, *Person’s Name* is a system classification. System classification has the thunderbolt icon along with classification name. Hovering over the classification itself provides more details on the type of classification, and more details on how it was applied
- **Custom classifications**: You can create custom classifications when you want to classify assets based on a pattern or a specific column name that's unavailable as a system classification. Custom classification rules can be based on a *regular expression* pattern or *dictionary*.

    Let's say that the *Employee ID* column follows the EMPLOYEE{GUID} pattern (for example, EMPLOYEE9c55c474-9996-420c-a285-0d0fc23f1f55). You can create your own custom classification by using a regular expression, such as `\^Employee\[A-Za-z0-9\]{8}-\[A-Za-z0-9\]{4}-\[A-Za-z0-9\]{4}-\[A-Za-z0-9\]{4}-\[A-Za-z0-9\]{12}\$`.

Note

Sensitivity labels are different from classifications. Sensitivity labels categorize assets in the context of data security and privacy, such as *Highly Confidential*, *Restricted*, *Public*, and so on. To use sensitivity labels in the Microsoft Purview Data Map, you'll need at least one Microsoft 365 license or account within the same Microsoft Entra tenant as your Microsoft Purview Data Map. For more information about the differences between sensitivity labels and classifications, see [sensitivity labels in the Microsoft Purview governance portal FAQ](data-map-sensitivity-labels-faq#what-is-the-difference-between-classifications-and-sensitivity-labels).