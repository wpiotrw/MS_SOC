---
layout: Conceptual
title: Governance Domain and Data Map Domain Recommendations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-best-practices-domains-and-gov-domains
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2025-03-26T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Find best practices for using governance domains in Microsoft Purview Unified Catalog and platform domains in Microsoft Purview Data Map.
locale: en-us
document_id: 37838188-07fb-9829-4268-499a5c52ab37
document_version_independent_id: 37838188-07fb-9829-4268-499a5c52ab37
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-best-practices-domains-and-gov-domains.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-best-practices-domains-and-gov-domains
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-best-practices-domains-and-gov-domains.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: b290e9f7-ccb1-228e-cf32-a9abcab70ec5
---

# Governance Domain and Data Map Domain Recommendations | Microsoft Learn

Important

- Domains in Data Map are limitied to 5 total.
- Collections are limited to 1000 across all platform domains. (One domain can have 1000 collections; 5 plaform domains would have 200 collections each if spread evenly.)
- Data sources are registered in one collection in one domain.
- Assets from a scanned data source must be scanned in the same domain as the data source.
- Merging an account will create a domain.
- Fabric domains likey don't map to domains, as the number of Fabric domains will exceed the 5 domains limit.

## General recommendations

[![Diagram of a logical mapping of Azure Purview constructs to the new Microsoft Purview construct model.](media/concept-best-practices-domains-and-gov-domains/datamap-and-gov-domains.jpg)](media/concept-best-practices-domains-and-gov-domains/datamap-and-gov-domains.jpg#lightbox)

- If true separation is required separate tenants are needed to enable different implementations of Microsoft Purview. Creating separate tenants isn't a likely solution for most organizations, but in some regulatory environments could be needed.
- Many organizations already have a SaaS model for deployment they can follow from Microsoft 365 or PBI/Fabric. Following that pattern within the organization can help resolve the SaaS deployment concerns.

### Collections and domains

- Using collections offer access segmentation for most needs to different users to get only the access required to Data Map.
- Use collections for technical separation along IT teams and enable onboarding, the governance domains can be used for the business team separations and logical concept boundaries (glossary terms and data products).
- For data sources that don't have production and nonproduction separate resources, data sources that have both requires the use of collections for testing because each data source is registered to one domain and one collection.

### Domains and governance domains

- Use dev, test, production governance domains (Finance.dev, Finance.prod, etc.) to separate testing with concepts and consumption experience. When testing isn't needed or shouldn't be made visible to consumers of the catalog, you can expire or repurpose the governance domain for production if concepts are ready for production.
- Plan to segment billing with governance domains not collections or platform domains.
- Governance domains can be mapped to platform domains and collections to build a logical relationship between the governance domains and the parts of Data Map that house their data assets.

## Domain recommendations

### Nonrecommended uses of the domains in Data Map

- Isolation of geo-residency segmentation.
- Domains don't scale to create boundaries along geo-residency segmentation needs.
- Domains don't enable separate storage locations for metadata.
- Business continuity and disaster recovery scenarios aren't recommended because if one domain is down all others are down.
- Metadata would need to be downloaded to an alternate source.
- Business unit isolation is best handled with Governance domains.
- Billing separation would follow the practice of using Governance domains.

### Recommended uses of the domains in Data Map

- Lifecycle Management (Development, test, Quality Assurance, Production), most customers have nonproduction and production resources, which are intended to be kept separate from production resources. Separation can be achieved with either domains or collections. When there's nonproduction and production data in the same resource, the customer has to use collections.