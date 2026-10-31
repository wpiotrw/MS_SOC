---
layout: Conceptual
title: Domains in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-domains
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-04-23T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand domains and how you can use them to organize Microsoft Purview Data Map and your data governance efforts.
locale: en-us
document_id: 6560029b-d435-351f-1ef6-eb1c91e3721a
document_version_independent_id: 6560029b-d435-351f-1ef6-eb1c91e3721a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-domains.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-domains
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-domains.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 7b164825-c80e-9317-04b4-892ab4531540
---

# Domains in Microsoft Purview Data Map | Microsoft Learn

Tip

This article covers domains in the Microsoft Purview Data Map. For governance domains in Microsoft Purview Unified Catalog, see the [governance domains article.](unified-catalog-governance-domains)

A domain is a construct that you use to distribute organizational responsibility in your instance of Purview Data Map. Domains provide structure in Data Map so that domain administrators can maintain the isolation of collections, data sources, scans, and assigned roles for access control. Previously, only collections filled this role, but we're introducing domains as top-level nodes above the rest of the hierarchy to address a few other scenarios:

- Decentralize and distribute responsibility by assigning roles at the domain level.
- Create the possibility for hard logical separations within your Data Map.
- Replace multiple accounts within a tenant to multiple domains within a single Microsoft Purview resource.

Domains also serve as the container for collections and assets.

Note

Domains are only available to Microsoft Purview accounts using [a tenant-level account](account-upgrades) (https://purview.microsoft.com).

## Default domain

Every Microsoft Purview Data Map starts with a default domain.

When an account is [upgraded to the new experience](account-upgrades#new-experience-for-existing-customers), the primary account's root collection becomes the default domain.

If you haven't [upgraded to the new experience](account-upgrades#new-experience-for-existing-customers) yet, take these points into consideration when choosing which account to elevate as your default domain:

- **Data Assets**: Choose the account with the most valuable or frequently used data assets, as this will become the default domain after the upgrade.
- **Account Usage**: Evaluate how each account is currently being used and its role within your organization. Accounts that are considered "production" would be most viable to select for this purpose.
- **Permissions and Access Controls**: Consider the existing permissions and access controls for each account, as they'll be carried over to the upgraded environment (as an isolated Domain). The permissions are applied in the new environment exactly as they are in the original environment. No more permissions are granted.

For more information about the new experience, see our guide on [governance in the new Microsoft Purview experience](account-upgrades).

## Custom domains

You can also create up to four more custom domains in your Data Map to better organize and govern your assets in Data Map. Get more information on [how to create and manage domains](data-map-domains-collections-manage#custom-domains).

## Domain level roles

Alongside [all the permissions you can assign at a collection level](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections), a new role can be assigned at the domain level to manage domains, collections, and glossaries:

- Domain admin - Can assign permissions within a domain and manage its resources.

For more information, see [how to assign permissions in collections and on a domain level](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

## Data Map structure

Capabilities and responsibilities are distributed between these three new levels in Data Map's structure: tenant/organization level, domain level, and collection level.

- Tenant level - Classifications, search, browse, metamodel, managed attributes, integration runtimes, lineage, workflows, insights, private endpoints.
- Domain level - Credentials, term templates, custom scan rule sets, advanced resource sets, pattern rules, policies, assets.
- Collection level - Data sources, scans, assets.

Important

Data sources and assets can't be duplicated in a tenant.

Domains don't change permissions in Microsoft Purview. Search and browse across a tenant are still managed by the level a user's assigned permissions. In Unified Catalog, a user only has access to metadata if they have [data-level access](data-gov-live-view#live-view-permissions) or [collection-level access](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

For more information, see [permissions for Microsoft Purview Data Map and Unified Catalog](data-governance-roles-permissions).