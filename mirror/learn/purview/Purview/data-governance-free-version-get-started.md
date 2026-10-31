---
layout: Conceptual
title: Get Started with Free Version of Microsoft Purview Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-free-version-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2024-06-05T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article describes how you and your users can make the best use of the free version of Microsoft Purview governance solutions to get started on your data governance journey.
locale: en-us
document_id: 480f7c0a-9435-40bb-d5d5-2adc6944c8e3
document_version_independent_id: 480f7c0a-9435-40bb-d5d5-2adc6944c8e3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-free-version-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-free-version-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-free-version-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a2f4ebad-9739-0755-12f9-9fd859a2336d
---

# Get Started with Free Version of Microsoft Purview Governance | Microsoft Learn

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

The free version of Microsoft Purview governance solutions provides an automatically available Microsoft Purview instance, ready for your users without setup. It allows your organization to try Microsoft Purview's basic governance capabilities and begin your governance journey. This article offers some best practices to help you quickly get started with Microsoft Purview data governance solutions, the Data Map, and the catalog.

Access to this version of Microsoft Purview depends on your organization's current relationship with Microsoft Purview; whether you're a new Microsoft Purview user, if you have existing accounts, or if you're using other services like Microsoft Fabric. For more information, see [how to access the free version of Microsoft Purview governance solutions.](data-governance-free-version#access-the-free-version-of-microsoft-purview-governance-solutions).

## How to start your governance journey

The free version of Microsoft Purview governance solutions lets you get started on your governance journey even as you begin planning. [Once your organization has access to the free version of Microsoft Purview governance solutions](data-governance-free-version#access-the-free-version-of-microsoft-purview-governance-solutions), use this guide to build your governance experience.

1. [Explore the Microsoft Purview portal](purview-portal#get-started-with-the-portal).
2. See what metadata for [supported Azure sources](data-governance-free-version#supported-data-sources) is already available in the catalog.
3. [Search](unified-catalog-data-assets-search) or [browse](unified-catalog-data-assets-search#browse-the-unified-catalog) the catalog to understand your initial assets.
4. Engage your [data owners](data-gov-live-view#data-owners), and add [data curators](data-governance-roles-permissions#tenant-level-role-groups) to manage metadata in your environment.
5. Work with your data owners and curators to [augment the metadata for existing data sources](data-gov-classic-metadata-curation). This gives your users more context and information about their data sources.
6. Add your other critical Azure resources to the data map using our [REST APIs](data-gov-api-create-assets).

    Important

    Only [data curators](data-governance-roles-permissions#tenant-level-role-groups) will be able to access any resources added to the data map using the [REST APIs](data-gov-api-create-assets). In order for other users to be able to access, [upgrade to the enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise).
7. Engage your users to discover your users to access your resources in the catalog.

## When you're ready to expand

Once you've added and curated your critical Azure resources in the Microsoft Purview portal, if you're looking for [more governance features](data-governance-free-version#whats-in-the-the-free-and-enterprise-versions), you're ready to [upgrade to the enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise).

When you upgrade, all the information you have and have added to the free version of Microsoft Purview governance solutions will be available in the enterprise version of Microsoft Purview within minutes, so you can get started using all of the enterprise features right away. Here's some steps you can take to prepare your environment for upgrade.

1. Review our [deployment best practices](deployment-best-practices#identify-objectives-and-goals) to start the right conversations in your organization.
2. Consider your [network architecture](concept-best-practices-network) for Microsoft Purview.
3. Plan your [collections architecture for your data map](data-gov-best-practices-domains-collections).
4. [Upgrade to the enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise).
5. Review the [scanning best practices](data-map-scanning-best-practices) and [classification best practices](data-gov-best-practices-classification).

Tip

If you used the [REST APIs](data-gov-api-create-assets) to add sources and assets in the free version of Microsoft Purview governance solutions that you can now scan in the enterprise version, Microsoft Purview will [normalize](data-gov-classic-asset-normalization) the newly scanned information and add it to your existing resources.