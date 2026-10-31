---
layout: Conceptual
title: Microsoft Purview Data Governance Free Version | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-free-version
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2024-09-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about which features are available using the free version of Microsoft Purview data governance solutions.
locale: en-us
document_id: 77b87ba4-0da5-ab93-f69d-dd591c4cc09e
document_version_independent_id: 77b87ba4-0da5-ab93-f69d-dd591c4cc09e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-free-version.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-free-version
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-free-version.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 69b00305-c98e-221f-df9e-af60805deab8
---

# Microsoft Purview Data Governance Free Version | Microsoft Learn

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

Microsoft Purview offers your administrators the ability to govern your data estate and your users the ability to discover data across your organization. The free version of Microsoft Purview governance solutions is an automatically available instance, ready for your users without needing to set it up. It allows your organization to try Microsoft Purview's basic capabilities and begin your governance journey.

The free version of Microsoft Purview governance solutions uses a single, organization-wide instance of Microsoft Purview that users can access to explore their Azure and Microsoft Fabric resources. Metadata for these resources is automatically inventoried and can be searched using the catalog.

Access to this version of Microsoft Purview depends on your organization's current relationship with Microsoft Purview; whether you're a new Microsoft Purview user, if you have existing accounts, or if you're already using other services like Microsoft Fabric. For more information, see, how to access the free version of Microsoft Purview governance solutions.

## Free version limitations

- In the free version of Microsoft Purview governance solutions, there's a limitation of 1,000 annotated assets. An annotated asset applies both to [live view](data-gov-live-view) assets that have been [curated](data-gov-classic-metadata-curation), or [custom assets added using the Microsoft Purview Data Map REST APIs](data-gov-api-create-assets). For example, if your account has 50 live view data assets, and you add descriptions and classifications to 15 of those assets, you have 15 annotated assets, and can have 985 more before you reach your limit. A description and a classification on the same asset count only as one annotated asset.
- In the free version, only [data curators](data-governance-roles-permissions#tenant-level-role-groups) are able to access any resources added to the data map using the [REST APIs](data-gov-api-create-assets).
- If your free version tenant shows three months of no activity, we have the right to clean up the account and might remove the unused resources.

## What's available in the free version

Users who have access to data stored in [supported Azure resources](data-governance-free-version#supported-data-sources) have access to its metadata in Microsoft Purview. Data readers can search for and browse this metadata and [data owners can augment the metadata to provide more context](data-gov-classic-metadata-curation).

Only a core subset of Microsoft Purview's governance solutions with limited capabilities are currently available in the free version:

- [Catalog](data-governance-free-version#catalog): Browse and search for your data assets.
- [Data Map history](data-map-history): A log of updates made to assets.

### Catalog

Users can browse and search for their data assets in Azure. You can explore your Azure assets to discover reliable data sources in their environment using [live view](data-gov-live-view) without any setup needed. The catalog automatically records data schema so users can explore data sources before accessing them. Data owners can [add metadata and information to their assets](data-gov-classic-metadata-curation), such as description, classifications, and contacts, so users have a more complete picture of their data estate.

### Supported data sources

Currently, the free version of Microsoft Purview governance solutions supports these governance data sources using [live view](data-gov-live-view):

- Azure Blob Storage
- Azure Data Lake Storage Gen 2
- Azure SQL Database
- Azure subscriptions
- Microsoft Fabric

You can annotate and curate assets that are available via [live view](data-gov-live-view), or [use our APIs to create new entities](data-gov-api-create-assets).

## Access the free version of Microsoft Purview governance solutions

The free version of Microsoft Purview governance solutions uses a single, organization-wide instance of Microsoft Purview. Access to the latest Microsoft Purview experience depends on your current relationship with Microsoft Purview; whether you're a new Microsoft Purview customer or an existing Microsoft Purview customer.

The free version of Microsoft Purview governance solutions uses the same location mappings as Microsoft 365, and maps to a location based on your Microsoft Entra ID home region. For more information, [see the FAQ.](data-governance-purview-portal-faq#how-does-microsoft-purview-choose-the-region-for-the-enterprise-version-of-microsoft-purview-)

### New Microsoft Purview customers

If you're an Azure Enterprise, Dynamics 365, Microsoft 365 Enterprise, Microsoft Fabric, Power Apps, or Power BI customer, to access the free version of Microsoft Purview governance solutions for your organization go to https://purview.microsoft.com. For more information about this access, see the [FAQ](data-governance-purview-portal-faq#how-is-access-to-the-microsoft-purview-portal-granted-if-you-re-a-dynamics-365--microsoft-365-enterprise--microsoft-fabric--power-apps--or-power-bi-user-).

If you're not an Azure Enterprise, Dynamics 365, Microsoft 365 Enterprise, Microsoft Fabric, Power Apps, or Power BI customer, we're currently making the free version of Microsoft Purview governance solutions available to organizations in batches. Go to https://purview.microsoft.com to check if it's available to your organization. If not:

- You can [create a Microsoft Purview account](create-microsoft-purview-portal) to access the **enterprise** version of Microsoft Purview.
- You can wait until the free version of Microsoft Purview governance solutions is available to your organization, and check this document for updates.

### Existing Microsoft Purview customers

If you're already using Microsoft Purview, your account is likely already upgraded to the enterprise version of Microsoft Purview.

You can check your organization's account type in the [Microsoft Purview portal](https://purview.microsoft.com) under the **Settings** gear icon, and **View all settings**.

## Permissions

Access control in the free version of Microsoft Purview governance solutions is managed at the organization/tenant level. All users are able to view data assets for sources where they have at least **Read** permissions already. For other functionality, like metadata curation, you can assign this role:

| Role | Description |
| --- | --- |
| Data Catalog Curator | Catalog curators can perform the create, read, modify, and delete actions on catalog data objects and establish relationships between objects. |

Get details about [governance roles and permissions](data-governance-roles-permissions).

## Upgrade to enterprise

The enterprise version of Microsoft Purview has access to the rest of Microsoft Purview applications and data sources. Learn how to [upgrade to the enterprise version of Microsoft Purview data governance](data-governance-free-version-upgrade-to-enterprise).

When you upgrade, all your data from the free version of Microsoft Purview governance solutions will be migrated into the enterprise version. The enterprise version will be hosted in the same location as the free version of Microsoft Purview governance solutions.

### What's in the the free and enterprise versions

Here's a brief comparison of the free and enterprise versions of Microsoft Purview data governance:

| Free | Enterprise |
| --- | --- |
| Auto discovery of Azure data sources | Collections, and glossary terms to organize your data map |
| Role group access control to platform and apps | Fine-grained, collection-level access control to platform and apps |
| Definition and manual application of classifications and terms | Automated application of classifications and terms |
| Manual descriptions, tags, and contacts | Manual and Bulk descriptions, tags, and contacts. |
| Manual creation of assets using the [data map APIs](/en-us/rest/api/purview/datamapdataplane/operation-groups) | Full use of [Microsoft Purview's REST APIs](/en-us/rest/api/purview/) |
|  | Automated scans for the hybrid data estate |
|  | Workflows |
|  | Business rules |
|  | Support for business assets and managed attributes |

Applications supported between versions of Microsoft Purview:

| Application | Free | Enterprise | Notes |
| --- | --- | --- | --- |
| [Catalog](unified-catalog-data-assets-search) | x | x | Free supports browse and search, while enterprise supports advanced search and self-service data access. |
| [Data Estate Insights](concept-insights) |  | x | Enterprise supports all available reports |
| [Data Policy](concept-policies-data-owner) |  | x |  |
| [Data Map](data-map) | x | x | [Data map history](data-map-history) is available in both the free and enterprise versions of Microsoft Purview. |

For more information about the applications available in the enterprise version of Microsoft Purview, see the [overview](data-governance-overview) article.

## Support for the free version of Microsoft Purview governance solutions

With the free version of Microsoft Purview governance solutions, you can't open support tickets for Microsoft Purview. You need to upgrade to the enterprise version of Microsoft Purview for support.