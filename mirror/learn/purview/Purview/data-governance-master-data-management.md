---
layout: Conceptual
title: Master Data Management in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-master-data-management
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-04-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about Microsoft Purview's master data management strategies for helping organizations build a comprehensive data governance framework.
locale: en-us
document_id: 1db4464d-ecc1-972b-ef7c-500837528ab4
document_version_independent_id: 1db4464d-ecc1-972b-ef7c-500837528ab4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-master-data-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-master-data-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-master-data-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 0b0dbe60-e1c5-fc65-82ca-cc2e76720bfe
---

# Master Data Management in Microsoft Purview | Microsoft Learn

Master data management (MDM) serves as a foundational element to build comprehensive data governance framework. Master data management creates a source of truth for your data, so you can check your key assets against this source of truth to confirm your data is trustworthy. You do this by creating a deduplicated set of master data records, a golden standard by which to measure your data. The standardization process you use to create this set of master data records differs across organizations, and Microsoft Purview integrates with partner solutions to offer helpful strategies.

## Partner MDM integration with Microsoft Purview

Microsoft Purview integrates with various MDM solutions to empower data product owners to create and publish golden records that represent the authoritative version of master data assets. These integrations operate bi-directionally, enabling MDM systems to access metadata from Microsoft Purview and connect with the source systems to unify, cleanse, and standardize data, thereby creating master data assets. Later, the metadata of these master data assets is published back to Microsoft Purview in Unified Catalog, where it can be curated as a [data product](unified-catalog-data-products).

Conversely, the creation of golden data assets for master data products is facilitated within the integrated MDM solution, applying its capabilities for data management and governance. This collaborative approach ensures that organizations can use the full potential of master data for analytics and insights while maintaining data integrity and compliance.

### Partner solutions and integration instructions

**CluedIn**

- [Master data management with CluedIn](https://www.cluedin.com/product/microsoft-purview-mdm-integration)
- [Microsoft Purview and CluedIn integration](data-governance-master-data-management-cluedin)

**Profisee**

- [Master data management with Profisee](https://profisee.com/solutions/microsoft-enterprise/)
- [Microsoft Purview and Profisee integration](data-governance-master-data-management-profisee)

**Reltio**

- [Master data management with Reltio](https://learn.reltio.com/reltio-integration-for-microsoft-purview)
- [Microsoft Purview and Reltio integration](data-governance-master-data-management-reltio)

**Semarchy**

- [Master data management with Semarchy](https://www.semarchy.com/doc/semarchy-xdm/xdm/latest/Install/azure/purview/integrate-xdm-with-purview.html)
- [Microsoft Purview and Semarchy integration](data-governance-master-data-management-semarchy)

## Data flow and integration steps

Here's a step-by-step guide on how to accomplish the tasks mentioned using Microsoft Purview and a partner MDM application:

1. [Register](data-map-data-sources-register-manage#register-a-new-source) and [scan](data-map-scan-data-sources) a data source in your Microsoft Purview Data Map.
2. [Create a data product](unified-catalog-data-products-create-manage#create-data-products) to use as your master data product.
3. [Create a glossary term](unified-catalog-glossary-terms-create-manage#create-glossary-terms) and [link it to your data product](unified-catalog-glossary-terms-create-manage#link-terms-to-data-products-assets-and-critical-data-elements-preview).
4. Curate the master data product:
    1. Within the master data product, review the existing data assets and determine which ones are relevant to include.
    2. Add details description, use cases, etc., to ensure that the master data product contains the most relevant and up-to-date information.
5. The master data management application receives signal and pulls metadata:
    1. Configure your master data management application to listen for signals or events indicating changes in the Microsoft Purview metadata. This process is slightly different depending on which application you're using.
    2. When a signal is received, the MDM application pulls the required metadata related to the master data product and associated data assets from Microsoft Purview.
6. The master data management application connects data sources and copies data to create master dataset:
    1. Configure the MDM application to connect to the relevant data sources where the data assets are located.
    2. Copy the data from these sources to the MDM application's storage environment.
7. Unify, clean, and standardize the data
    1. Within the MDM application, unify, clean, and standardize the copied data to ensure consistency and accuracy.
    2. Apply data governance rules and transformations as needed to prepare the data for creating the master data asset.
8. Create a master data asset of Golden Records
    1. Utilize the MDM application's capabilities to create a master data asset comprised of golden records that represent the consolidated and standardized view of the data.
    2. Ensure that the master data asset meets the defined criteria and quality standards.
9. Publish the metadata to Microsoft Purview and [link the new data asset to your data product](unified-catalog-glossary-terms-create-manage#link-terms-to-data-products-assets-and-critical-data-elements-preview).

By following these steps, you can seamlessly integrate with a partner MDM solution to manage glossary terms, curate master data products, synchronize metadata, and create and publish master data assets. This integration helps maintain data consistency, quality, and governance across your organization's data landscape

## Where to find master data assets in Unified Catalog

Master data assets are found on a data product's details page of data produts. On the details page, locate the **Data assets** section. Each MDM asset is listed on a card labeled with the name of the MDM solution provider, such as Profisee or Semarchy. Learn more about [searching for and browsing data products](unified-catalog-data-products-search).