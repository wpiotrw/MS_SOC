---
layout: Conceptual
title: Governance roles and permissions for classic Microsoft Purview Data Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-catalog-roles-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2024-05-23T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how governance permissions and access are managed in the free and enterprise versions of Microsoft Purview accounts using the classic Microsoft Purview Data Catalog.
ms.custom: sfi-ga-nochange
locale: en-us
document_id: a5fea7c5-c44a-6ae7-27d2-d4b0ae8ed2ba
document_version_independent_id: a5fea7c5-c44a-6ae7-27d2-d4b0ae8ed2ba
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-catalog-roles-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-catalog-roles-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-catalog-roles-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: e47e4096-fdf8-40f5-5282-928281fe1db5
---

# Governance roles and permissions for classic Microsoft Purview Data Catalog | Microsoft Learn

Important

This article explains governance permissions in the [free](data-governance-free-version) and [enterprise](data-governance-free-version-upgrade-to-enterprise) versions of Microsoft Purview data governance solutions using the classic Microsoft Purview Data Catalog.

- For permissions using the [new Microsoft Purview Unified Catalog](unified-catalog), see the [data governance permissions article.](data-governance-roles-permissions)
- For general permissions in the [Microsoft Purview portal](purview-portal) see [permissions in the portal](purview-permissions).
- For classic data governance permissions, see the [permissions in the Microsoft Purview governance portal article.](data-gov-classic-permissions)

Microsoft Purview data governance has two solutions in the Microsoft Purview portal, the Data Map and the catalog. These solutions use tenant/organizational-level permissions, existing data access permissions, and domain/collection permissions to provide users access to governance tools and data assets. The kind of permissions available to use depends on your Microsoft Purview account type. You can check your account type in the [Microsoft Purview portal](https://purview.microsoft.com) under the **Settings** card, and **Account**.

![Screenshot of the settings solution highlighted on the Microsoft Purview portal main page.](media/roles-permissions/open-settings.png)

![Screenshot of the settings page in the Microsoft Purview portal.](media/roles-permissions/check-your-account-type.png)

| Account Type | Tenant/Organization permissions | Data access permissions | Domain and collection permissions |
| --- | --- | --- | --- |
| Free | x | x |  |
| Enterprise | x | x | x |

For more information about each permission type, see these guides:

- Tenant/organization permissions - assigned at the organizational level, they provide general and administrative permissions.
- Domain and collection level permissions - permissions in the Microsoft Purview Data Map that grant access to data assets in Microsoft Purview.
- Data access permissions - permissions users already have on their Azure data sources.

For more information about permission based on account type, see these guides:

- Free
- Enterprise

Important

For users newly created in Microsoft Entra ID, it could take some time for permissions to propagate even after correct permissions have been applied.

## Tenant level role groups

Assigned at the organizational level, tenant level role groups provide general, and administrative permissions for both the Microsoft Purview Data Map and classic Data Catalog. If you're managing your Microsoft Purview account or your organization's data governance strategy, you probably need one or several of these roles.

The currently available governance tenant-level role groups are:

| Role group | Description | Account type availability |
| --- | --- | --- |
| Purview administrator | Create, edit, and delete domains and perform role assignments. | Free and enterprise accounts |
| Data Source Administrators | Manage data sources and data scans in the Microsoft Purview Data Map. | Enterprise accounts |
| Data Catalog Curators | Perform create, read, modify, and delete actions on catalog data objects and establish relationships between objects in the classic Data Catalog. | Enterprise accounts |
| Data Estate Insights Readers | Provides read-only access to all insights reports across platforms and providers in the classic Data Catalog. | Enterprise accounts |
| Data Estate Insights Admins | Provides admin access to all insights reports across platforms and providers in the classic Data Catalog. | Enterprise accounts |

For a full list of all available roles and role groups, not just for data governance, see [roles, and role groups in the Microsoft Defender XDR and Microsoft Purview portals.](/en-us/microsoft-365/security/office-365-security/scc-permissions)

### How to assign and manage role groups

Note

Users must hold the [role management role](/en-us/microsoft-365/security/office-365-security/scc-permissions#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance) or the Global Administrator role for the organization in order to assign roles.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

To assign and manage roles in Microsoft Purview, follow the [permissions in Microsoft Purview guide.](purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group)

## Permissions to search the classic Data Catalog

No specific permissions are needed in the catalog to be able to search it. However, searching the catalog will only return relevant data assets that you have permissions to view in the Data Map.

Users can find a data asset in the catalog when:

- [The user has at least read permissions on an available Azure or Microsoft Fabric resource](data-gov-live-view#what-resources-have-live-view-available)
- The user has data reader permissions on a domain or collection in the Microsoft Purview Data Map where the asset is stored

Permissions to these assets are managed at the [resource level](data-gov-live-view#what-resources-have-live-view-available) and at the Data Map level.

## Domain and collection permissions

Domains and collections are tools that the Microsoft Purview Data Map uses to group assets, sources, and other artifacts into a hierarchy for discoverability and to manage access control within the Microsoft Purview Data Map.

### Domain and collection roles

The Microsoft Purview Data Map uses a set of predefined roles to control who can access what within the account. These roles are currently:

- **Domain admin** ([domain](data-map-domains) level only) - Can assign permissions within a domain and manage its resources.
- **Collection administrator** - a role for users that will need to assign roles to other users in the Microsoft Purview governance portal or manage collections. Collection admins can add users to roles on collections where they're admins. They can also edit collections, their details, and add subcollections. A collection administrator on the [root collection](data-governance-glossary) also automatically has permission to the Microsoft Purview governance portal. If your **root collection administrator** ever needs to be changed, you can [follow the steps in the section below](data-gov-classic-permissions#administrator-change).
- **Data curators** - a role that provides access to the Microsoft Purview Unified Catalog to manage assets, configure custom classifications, create and manage glossary terms, and view data estate insights. Data curators can create, read, modify, move, and delete assets. They can also apply annotations to assets.
- **Data readers** - a role that provides read-only access to data assets, classifications, classification rules, collections and glossary terms.
- **Data source administrator** - a role that allows a user to manage data sources and scans. If a user is granted only to **Data source admin** role on a given data source, they can run new scans using an existing scan rule. To create new scan rules, the user must be also granted as either **Data reader** or **Data curator** roles.
- **Insights reader** - a role that provides read-only access to insights reports for collections where the insights reader also has at least the **Data reader** role. For more information, see [insights permissions.](insights-permissions)
- **Policy author** - a role that allows a user to view, update, and delete Microsoft Purview policies through the Data policy app within Microsoft Purview.
- **Workflow administrator** - a role that allows a user to access the workflow authoring page in the Microsoft Purview governance portal, and publish workflows on collections where they have access permissions. Workflow administrator only has access to authoring, and so will need at least Data reader permission on a collection to be able to access the Purview governance portal.

Note

At this time, Microsoft Purview policy author role is not sufficient to create policies. The Microsoft Purview data source admin role is also required.

Important

The user that created the account is automatically assigned domain admin on the default domain and collection admin on the root collection.

### Add role assignments

1. Open the Microsoft Purview Data Map.
2. Select the domain or collection where you want to add your role assignment.
3. Select the **Role assignments** tab to see all the roles in a collection or a domain. Only a collection admin or domain admin can manage role assignments.

    ![Screenshot of Microsoft Purview governance portal collection window, with the role assignments tab highlighted.](media/include-manage-domain-collection-roles/select-role-assignments.png)
4. Select **Edit role assignments** or the person icon to edit each role member.

    ![Screenshot of Microsoft Purview governance portal collection window, with the edit role assignments dropdown list selected.](media/include-manage-domain-collection-roles/edit-role-assignments.png)
5. Type in the textbox to search for users you want to add to the role member. Select **X** to remove members you don't want to add.

    ![Screenshot of Microsoft Purview governance portal collection admin window with the search bar highlighted.](media/include-manage-domain-collection-roles/search-user-permissions.png)
6. Select **OK** to save your changes, and you'll see the new users reflected in the role assignments list.

### Remove role assignments

1. Select **X** button next to a user's name to remove a role assignment.

    ![Screenshot of Microsoft Purview governance portal collection window, with the role assignments tab selected, and the x button beside one of the names highlighted.](media/include-manage-domain-collection-roles/remove-role-assignment.png)
2. Select **Confirm** if you're sure to remove the user.

    ![Screenshot of a confirmation pop-up, with the confirm button highlighted.](media/include-manage-domain-collection-roles/confirm-remove.png)

### Restrict inheritance

Collection permissions are inherited automatically from the parent collection. You can restrict inheritance from a parent collection at any time, using the restrict inherited permissions option.

Note

Currently permissions from the default domain cannot be restricted. Any permissions assigned at the default domain will be inherited by the domain's direct subcollections.

Once you restrict inheritance, you'll need to add users directly to the restricted collection to grant them access.

1. Navigate to the collection where you want to restrict inheritance and select the **Role assignments** tab.
2. Select **Restrict inherited permissions** and select **Restrict access** in the popup dialog to remove inherited permissions from this collection and any subcollections. Collection admin permissions won't be affected.

    ![Screenshot of Microsoft Purview governance portal collection window, with the role assignments tab selected, and the restrict inherited permissions slide button highlighted.](media/include-manage-domain-collection-roles/restrict-access-inheritance.png)
3. After restriction, inherited members are removed from the roles expect for collection admin.
4. Select the **Restrict inherited permissions** toggle button again to revert.

    ![Screenshot of Microsoft Purview governance portal collection window, with the role assignments tab selected, and the unrestrict inherited permissions slide button highlighted.](media/include-manage-domain-collection-roles/remove-restriction.png)

Tip

For more detailed information about the roles available in collections see [the who should be assigned what roles table](data-gov-classic-permissions#who-should-be-assigned-to-what-role) or the [collections example](data-gov-classic-permissions#a-collections-example).

## Data access permissions

Data access permissions are permissions users already have on their Azure data sources. These existing permissions also grant permission to access and manage the metadata for those sources, depending on the level of permissions:

- Reader permissions
- Owner permissions

Currently, these features are only available for some Azure sources:

| Data source | Reader permission |
| --- | --- |
| Azure SQL Database | [Reader role in Azure](/en-us/azure/role-based-access-control/built-in-roles#general) |
| Azure Blob Storage | [Reader role in Azure](/en-us/azure/role-based-access-control/built-in-roles#general) |
| Azure Data Lake Storage Gen2 | [Reader role in Azure](/en-us/azure/role-based-access-control/built-in-roles#general) |
| Azure Subscription | Read permission on subscription |

The reader role contains enough permissions, but if you're building a custom role, your users need to have these actions included:

| Data source | Reader permission |
| --- | --- |
| Azure SQL Database | "Microsoft.Sql/servers/read", "Microsoft.Sql/servers/databases/read", "Microsoft.Sql/servers/databases/schemas/read", "Microsoft.Sql/servers/databases/schemas/tables/read", "Microsoft.Sql/servers/databases/schemas/tables/columns/read" |
| Azure Blob Storage | "Microsoft.Storage/storageAccounts/read", "Microsoft.Storage/storageAccounts/blobServices/read", "Microsoft.Storage/storageAccounts/blobServices/containers/read" |
| Azure Data Lake Storage Gen2 | "Microsoft.Storage/storageAccounts/read", "Microsoft.Storage/storageAccounts/blobServices/read", "Microsoft.Storage/storageAccounts/blobServices/containers/read" |
| Azure Subscription | "Microsoft.Resources/subscriptions/resourceGroups/read" |

### Reader permissions

Users who have at least the [reader role](/en-us/azure/role-based-access-control/built-in-roles) on available Azure resources are also able to access those resources metadata in the free and enterprise account types.

Users can search and browse for assets from these sources in the classic Data Catalog and view their metadata.

These are the permissions needed on the resources for users to be considered readers:

| Data source | Reader permission |
| --- | --- |
| Azure SQL Database | [Reader role in Azure](/en-us/azure/role-based-access-control/built-in-roles#general) |
| Azure Blob Storage | [Reader role in Azure](/en-us/azure/role-based-access-control/built-in-roles#general) |
| Azure Data Lake Storage Gen2 | [Reader role in Azure](/en-us/azure/role-based-access-control/built-in-roles#general) |
| Azure Subscription | Read permission on subscription |

### Owner permissions

Users who have the [owner role](/en-us/azure/role-based-access-control/built-in-roles) or write permissions on [available Azure resources](data-gov-classic-metadata-curation#supported-live-sources) can access and edit metadata for those resources in free and enterprise account types.

Owning users can search and browse for assets from these sources in the catalog and view metadata. Users can also update and manage the metadata for those resources. Learn more about [metadata curation](data-gov-classic-metadata-curation).

These are the permissions needed on the resources for users to be considered owners:

| Data source | Owner permission |
| --- | --- |
| Azure SQL Database | "Microsoft.Sql/servers/write", "Microsoft.Sql/servers/databases/write", "Microsoft.Authorization/roleAssignments/write" |
| Azure Blob Storage | "Microsoft.Storage/storageAccounts/write", "Microsoft.Authorization/roleAssignments/write" |
| Azure Data Lake Storage Gen2 | "Microsoft.Storage/storageAccounts/write", "Microsoft.Authorization/roleAssignments/write" |

## Permissions in the free version

All users are able to view data assets for available sources where they have at least **Read** permissions already. Owning users are able to manage the metadata for [available assets](data-gov-classic-metadata-curation#supported-live-sources) where they have at least **Owner/Write** permissions already. For more information, see the data access permissions section.

Extra permissions can also be assigned using tenant level role groups.

Important

For users newly created in Microsoft Entra ID, it may take some time for permissions to propagate even after correct permissions have been applied.

## Permissions in enterprise version of Microsoft Purview

All users are able to view data assets for available sources where they have at least **Read** permissions already. Owning users are able to manage the metadata for assets where they have at least **Owner/Write** permissions already. For more information, see the data access permissions section.

Extra permissions can also be assigned using tenant level role groups.

Permissions can also be assigned in the Microsoft Purview Data Map so users can browse assets in the Data Map or classic Data Catalog search that they don't already have data access to.