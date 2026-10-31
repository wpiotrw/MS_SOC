---
layout: Conceptual
title: Data Governance Roles and Permissions in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-roles-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-04-24T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand the roles and permissions needed to use Microsoft Purview data governance solutions, Unified Catalog and Data Map.
ms.custom: sfi-ga-nochange
locale: en-us
document_id: d85171cc-07ef-1fc6-b283-55855f1cd329
document_version_independent_id: d85171cc-07ef-1fc6-b283-55855f1cd329
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-roles-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-roles-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-roles-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 26678339-3379-c8e0-f997-6a9ea29436f3
---

# Data Governance Roles and Permissions in Microsoft Purview | Microsoft Learn

Important

This article covers Microsoft Purview data governance permissions in the new [Microsoft Purview portal](purview-portal) using Microsoft Purview Unified Catalog.

- If you're using the classic Data Catalog, see [governance permissions for the classic Data Catalog](data-gov-classic-catalog-roles-permissions).
- For data governance permissions in the [classic Microsoft Purview portal](use-microsoft-purview-governance-portal), see [permissions in the classic Microsoft Purview governance portal](data-gov-classic-permissions).

Microsoft Purview data governance has two solutions in the Microsoft Purview Portal: Data Map and Unified Catalog. These solutions use tenant/organizational-level permissions, existing data access permissions, and domain/collection permissions to provide users access to governance tools and data assets.

The kind of permissions available to use depends on your Microsoft Purview account type.

## Check your account type

Check whether your organization has the free or enterprise type of account. To check your account type, go to the [Microsoft Purview portal](https://purview.microsoft.com), select the **Settings** card. Under **Account**, view your **Account type**.

![Screenshot of the settings page in the Microsoft Purview portal.](media/roles-permissions/check-your-account-type.png)

Important

For users newly created in Microsoft Entra ID, it might take some time for permissions to propagate even after correct permissions are applied.

## Permissions in the enterprise version

All users can view data assets for available sources where they have at least **Read** permissions. Users who are owners can manage the metadata for assets where they have at least **Owner/Write** permissions. Learn more about [Microsoft Azure roles](/en-us/azure/role-based-access-control/built-in-roles).

### Permissions types

- Tenant/organization permissions: Assigned at the organizational level, these permissions provide general and administrative permissions.
- Unified Catalog permissions: These permissions allow users to browse Unified Catalog and build out their data governance solutions.
- Data Map domain and collection level permissions: Permissions in Data Map that grant access to data assets in Microsoft Purview.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Tenant level role groups

Assigned at the organizational level, tenant level role groups provide general and administrative permissions for both Microsoft Purview Data Map and Unified Catalog. If you're managing your Microsoft Purview account or your organization's data governance strategy, you probably need to belong to one or more of these role groups:

- Purview Administrators
- Data Source Administrators
- Data Governance

For more information, see descriptions of these roles.

For a full list of all available roles and role groups, not just for data governance, see [roles, and role groups in the Microsoft Defender XDR and Microsoft Purview portals](/en-us/microsoft-365/security/office-365-security/scc-permissions).

### How to assign and manage role groups

A user must hold the [*Role management* role](/en-us/microsoft-365/security/office-365-security/scc-permissions) in order to add users or groups to a Microsoft Purview role group. For instructions on assigning and managing roles in Microsoft Purview, see [permissions in Microsoft Purview](purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group).

## Unified Catalog permissions

Three levels of permissions grant users access to information in Unified Catalog:

1. Data governance tenant level: A tenant/organizational-level role group that has the Data Governance Admin role. That role delegates the first level of access for Governance Domain Creators. (This role isn't surfaced in Unified Catalog, but affects your ability to assign permissions in Unified Catalog.)
2. Catalog level permissions: Permissions that grant ownership to governance domains and access to health management.
3. Governance domain level permissions: Permissions to access and manage resources inside specific governance domains.

#### Permissions to search the full Unified Catalog

You don't need specific permissions in Unified Catalog to search the Unified Catalog. However, searching Unified Catalog only returns relevant data assets that you have permissions to view in Data Map. Users can find a data asset in Unified Catalog when:

- They [search data products](unified-catalog-data-products-search) in a governance domain where they have catalog reader permissions.
- They have data reader permissions on a domain or collection in Data Map where the asset is stored.
- They have at least [Read permissions on an available Azure or Microsoft Fabric resource](data-gov-live-view#what-resources-have-live-view-available). 
    Important

    Users who already have **Read** permissions in Azure might have access to assets in Unified Catalog that you didn't intend for them to have. If you don't want them to have such access, you need to [remove their permissions](/en-us/azure/role-based-access-control/role-assignments-remove).

You manage permissions to these assets at the resource level and at the Data Map level.

If your catalog is well-curated, day-to-day business users shouldn't need to search the full catalog. They should be able to find the data they need in data products. For more information about setting up the Unified Catalog, see [get started with data governance](data-governance-get-started), and [plan for Unified Catalog](unified-catalog-plan).

### Catalog level permissions

Catalog level permissions provide high-level access within Unified Catalog and include these roles:

- Governance Domain Creator
- Global Catalog Reader
- Data Health Owner
- Data Health Reader

For more information, see descriptions of these roles.

#### How to assign catalog level roles

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) using credentials for an admin account that is assigned the *Data Governance* role.
2. Go to **Settings** and select **Unified Catalog**.
3. Select **Roles and permissions**.
4. Select **Governance Domain Creators** or another role, then select the add user icon.
5. Search for the user you want to add, then select the user.
6. Select **Save**.

### Governance domain level permissions

Governance domain permissions provide access within a specific [governance domain](unified-catalog-governance-domains). Grant these permissions to data experts and business users so they can read and manage objects within the governance domain. Only a user with the **Governance domain owner** role can grant governance domain permissions.

See the list of these roles and descriptions.

Tip

A user in your organization who runs data governance or Unified Catalog should hold the **Governance domain owner** role. This role is essential for building entities such as governance domains, data products, and glossary terms. Assign at least two people as governance domain owners.

#### How to assign governance domain roles

A user needs to be a Governance Domain Owner in the governance domain to assign governance domain roles. Data Governance Administrators or Governance Domain Creators assign this role.

Assign governance domain roles under the **Roles** tab in a governance domain. For instructions on assigning roles, see [how to manage governance domains](unified-catalog-governance-domains-create-manage#roles).

## Unified Catalog roles

Important

Be sure you understand the difference between the two Catalog Reader roles:

**Global Catalog Reader** allows users to access published business concepts from published governance domains.

**Local Catalog Reader** greatly reduces access to governance domains. When you assign users to this role within a governance domain:

- Only those users have reader access to published concepts within that governance domain.
- A user with this role can also hold other roles, such as Data Product Owner or Data Steward, that let them view published business concepts from other governance domains.

The **Local Catalog Reader** role is helpful when, for example, you need to limit access to a governance domain to meet regulatory or legal requirements. However, overuse of this role hinders a [federated approach to data governance](data-governance-overview#federated-approach-to-data-governance).

Note

[Data observability](unified-catalog-observability) uses the same roles as the rest of the Unified Catalog. Catalog Readers can't access the broader Data Observability explorer view in data estate health and they can only view published concepts. The Data Steward, Data Product Owners, Governance Domain Owners, and Governance Domain Creators have access to data observability views in both the concepts that they can view and the data health management view that enables broader exploration and view across the full data estate.

| Permission level | Role | Description |
| --- | --- | --- |
| **Tenant** | Data Governance role group | Grants access to data governance roles within Microsoft Purview. |
|  | Data Source Administrators role group | Manage data sources and data scans in the Microsoft Purview Data Map. |
|  | Purview Administrators role group | Create, edit, and delete domains and perform role assignments. |
| **Catalog** | Data Governance Administrator | Delegates the first level of access for Governance Domain Creators and other catalog level permissions. |
|  | Data Health Owner | Can create, update, and read artifacts in the **Health management** area of Unified Catalog. |
|  | Data Health Reader | Can read artifacts in the **Health management** area of Unified Catalog. |
|  | Global Asset Curator | Can add published glossary terms to data assets and columns. |
|  | Global Catalog Reader | Can read published artifacts across governance domains that don't have a Local Catalog Reader specified. |
|  | Governance Domain Creator | Can create domains and delegate governance domain owner (or remains governance domain owner by default). |
| **Governance domain** | Data Product Owner\* | Can create, update, and read data products only within their governance domain. Can read and build relationships with concepts in governance domains. |
|  | Data Profile Reader | Has access to browse data profile insights and can drill down the profiling results to browse the statistics in column level. This is a sub-role that requires the user to also hold the **Governance Domain Reader***and* either the **Global Catalog Reader** or **Local Catalog Reader** roles. |
|  | Data Profile Steward | Can run data profiling jobs and access profiling insight details. This role can also browse through all data quality insights and can monitor profiling jobs. This role can't create rules and can't run data quality scanning. This is a sub-role that requires the user to also hold the **Governance Domain Reader***and***Data Product Owner** roles. |
|  | Data Quality Metadata Reader | Can browse data quality insights (except profiling results column level insight), data quality rule definition, and rule level scores. This role can't access error records and can't run profiling and data quality scanning jobs. This is a sub-role that requires the user to also hold the **Governance Domain Reader***and* either the **Global Catalog Reader** or **Local Catalog Reader** roles. |
|  | Data Quality Reader | Can browse all data quality insights and data quality rules definitions. This role can't run data quality scanning and data profiling jobs, and can't access data profiling column level insight. This is a sub-role that requires the user to also hold the **Governance Domain Reader***and* either the **Global Catalog Reader** or **Local Catalog Reader** roles. |
|  | Data Quality Steward | Can use data quality features like data quality rule management, data quality scanning, browsing data quality insights, data quality scheduling, job monitoring, and configuring thresholds and alerts. This is a sub-role that requires the user to also hold the **Governance Domain Reader***and***Data Product Owner** roles. |
|  | Data Steward\* | Can create, update, and read artifacts and policies within their governance domain. Can also read artifacts from other governance domains. |
|  | Governance Domain Owner | Can delegate all other governance domain permissions, configure domain level data quality scan alerts, set up domain level schedule for data quality scanning job, and set domain level access policies. |
|  | Governance Domain Reader | Can read governance domain metadata for published domains they're added to. |
|  | Local Catalog Reader | Can read published concepts only in the governance domain they're granted access to. Because this role greatly limits the scope of who can access and manage data, it's recommended to limit use of this role so that you can better utilize a [federated approach to data governance](data-governance-overview#federated-approach-to-data-governance). |

\*To be able to add data assets to a data product, Data Product Owners and Data Stewards also need Data Map permissions to read those data assets in Data Map.

## Data Map permissions

Data Map uses a set of predefined roles to control who can access what within the account. [Domains and collections](data-map-domains-collections-manage) are tools used by Data Map to group assets, sources, and other artifacts into a hierarchy for discoverability, and to manage access control within Data Map.

Find a [description of each role and learn how to add roles and restrict access through collections](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

For more detailed information about the roles available in collections, see [who should be assigned what roles](data-gov-classic-permissions#who-should-be-assigned-to-what-role) or the [collections example](data-gov-classic-permissions#a-collections-example).

Tip

If you're a data steward or data product owner for Unified Catalog, it's a good idea to have Data Map permissions as well.

## Data asset lifecycle example

To understand how permissions work between Data Map and Unified Catalog, review the table below on the full lifecycle of an Azure SQL table in the environment:

| Step | Role | Permission level |
| --- | --- | --- |
| 1. The Azure SQL Database is registered in Data Map | Data Source Administrator | Data Map |
| 2. The Azure SQL Database is scanned in Data Map | Data Curator or Data Source Administrator | Data Map |
| 3. The Azure SQL table is curated and certified | Data Curator | Data Map |
| 4. A governance domain is created in the Microsoft Purview Account | Governance Domain Creator | Catalog |
| 5. A data product is created in the governance domain | Governance Domain Owner and/or Data Product Owner | Governance domain |
| 6. The Azure SQL table is added as an asset to the data product | Data Product Owner and/or Steward | Governance domain |
| 7. An access policy is added to the data product | Data Product Owner and/or Steward | Governance domain |
| 8. A user searches Unified Catalog, looking for data assets that match their needs | Asset permissions or data reader permission | [Asset permissions](data-gov-live-view#what-resources-have-live-view-available) or Data Map permissions |
| 9. A user searches data products, looking for a product that matches their needs | Global Catalog Reader | Catalog |
| 10. A user requests access to the resources in the data product | Global Catalog Reader | Catalog |
| 11. A user views Data Health Insights to track the health of their Data Catalog | Data Health Reader | Catalog |
| 12. A user wants to develop a new report to track data health progress in their catalog | Data Health Owner | Catalog |