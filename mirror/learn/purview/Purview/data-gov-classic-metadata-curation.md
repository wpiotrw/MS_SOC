---
layout: Conceptual
title: Metadata curation in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-metadata-curation
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: jife
ms.date: 2024-06-11T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about metadata curation in Microsoft Purview Data Map.
locale: en-us
document_id: 23eecd12-7786-dcf3-8c36-0327d0125b58
document_version_independent_id: 23eecd12-7786-dcf3-8c36-0327d0125b58
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-metadata-curation.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-metadata-curation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-metadata-curation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 29f19fbc-1aa2-7a6e-d10e-0306575a76f3
---

# Metadata curation in Microsoft Purview Data Map | Microsoft Learn

This article describes how users can update and curate the metadata of an asset in the Microsoft Purview Data Map. Data assets in the map automatically have technical metadata like name and schema, but users can also add other information like descriptions and contacts. This extra information allows other users to better understand data assets so they can discover, govern, and use them.

## Who can update metadata?

- Users who have the [owner role](/en-us/azure/role-based-access-control/built-in-roles) or write permissions on available, live Azure resources can access and edit those resources in free and enterprise account types. For more information about data owner metadata curation, see the data owner curation section on this page.
- Users who have [data curator](data-gov-classic-permissions) permissions on a collection in a Microsoft Purview account can edit the metadata details for all data assets in that collection. This is only available in the [enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise).
- Users who are using the classic Microsoft Purview Unified Catalog and have been assigned to the [the data curator role group](data-governance-roles-permissions#tenant-level-role-groups) can edit the metadata details for all data assets in a Microsoft Purview account. For more information, see the role group curation section on this page.

## Data owner curation

If a user is a data owner on an available, live Azure resource, they're able to access and manage that asset's metadata in Microsoft Purview. In this case, a 'data owner' isn't limited to users who have the Azure RBAC [owner role](/en-us/azure/role-based-access-control/built-in-roles) on a resource. It also applies to users who have certain write permissions on the available Azure resources. The permissions needed are listed in the supported live sources section.

With those permissions, data owners able to update these aspects of a data asset:

- Description
- Contacts
- Column descriptions

Tip

Any of these updates are tracked by Microsoft Purview and can be viewed in [Data Map history](data-map-history).

## Role group curation

If a user has been added to the [data curator role group](data-governance-roles-permissions#tenant-level-role-groups) in the classic Microsoft Purview Unified Catalog, they're able to access and manage asset metadata in Microsoft Purview depending on the version of Microsoft Purview they're using.

With the free version of Microsoft Purview governance solutions you can update these aspects:

- Display name
- Description
- Contacts
- Column descriptions
- Column names
- Column data types
- Source classifications
- Column classifications

With the enterprise version of Microsoft Purview, after [extending live view](data-gov-live-view#extend-live-view-permissions), or [registering](data-map-data-sources-register-manage#register-a-new-source) and [scanning](data-map-scan-data-sources) an asset, you can edit all the other aspects of that asset, including adding glossary terms.

Tip

Any of these updates are tracked by Microsoft Purview and can be viewed in [Data Map history](data-map-history).

## Collection-level role curation

If a user has been given the [data curator role on a collection in Data Map](data-map-collections-manage-classic#add-role-assignments), they're able to access and manage metadata for any assets in that collection.

Note

A user can only be assigned [the data curator role on a collection](data-map-collections-manage-classic#add-role-assignments) in the [enterprise version of Microsoft Purview.](data-governance-free-version-upgrade-to-enterprise)

With the data curator role, a user can update aspects of their data assets depending on the kind of asset it is.

If an asset is only available as a [live view asset](data-gov-live-view) you can edit:

- Display name
- Description
- Contacts
- Column descriptions
- Column names
- Column data types
- Source classifications
- Column classifications

Once an asset has had [live view extended](data-gov-live-view#extend-live-view-permissions) for all users, or if an asset has been [registered](data-map-data-sources-register-manage#register-a-new-source) and [scanned](data-map-scan-data-sources), you can edit all the other aspects of an asset, including adding glossary terms.

### How to edit assets

1. [In the Microsoft Purview portal](https://purview.microsoft.com/) (or the classic [Microsoft Purview governance portal](https://web.purview.azure.com/resource/)) [search](/en-us/purview/how-to-search-catalog) or [browse](unified-catalog-data-assets-search#browse-the-unified-catalog) for a data source or asset.
2. Select the asset to view details.

    ![Screenshot of a data source showing the view details menu for both the source and one of its data assets.](media/metadata-curation/view-details.png)
3. Select **Edit**.

    ![Screenshot of a data source details view with the edit button highlighted.](media/metadata-curation/select-edit.png)
4. Make any changes to the metadata, and select **Save** when you're finished.

    ![Screenshot of a data source details edit with a description added and the save button highlighted.](media/metadata-curation/change-and-save.png)

For more information about editing assets, including rich text editing for descriptions, see the [manage assets in the Unified Catalog article]classic-catalog-asset-details.md).

### Supported live sources

| Data source | Owner permission |
| --- | --- |
| Azure SQL Database | "Microsoft.Sql/servers/write", "Microsoft.Sql/servers/databases/write", "Microsoft.Authorization/roleAssignments/write" |
| Azure Blob Storage | "Microsoft.Storage/storageAccounts/write", "Microsoft.Authorization/roleAssignments/write" |
| Azure Data Lake Storage Gen2 | "Microsoft.Storage/storageAccounts/write", "Microsoft.Authorization/roleAssignments/write" |

## Limitations

These are the current limitations for metadata curation in Microsoft Purview:

- When a user in the data curator role group edits a live mode asset for the first time, it will not work. If you edit a second time with a different edit than the first attempt, then it works.