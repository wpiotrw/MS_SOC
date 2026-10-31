---
layout: Conceptual
title: Create and Manage Governance Domains in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-governance-domains-create-manage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-04-21T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to create and manage governance domains in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 90e5955e-b51d-88c7-d0e1-95a8135850e7
document_version_independent_id: 90e5955e-b51d-88c7-d0e1-95a8135850e7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-governance-domains-create-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-governance-domains-create-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-governance-domains-create-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: b9d267cb-ea65-d7cb-55db-423b42b9fc72
---

# Create and Manage Governance Domains in Unified Catalog | Microsoft Learn

Ownership of data is an important aspect of data governance. However, today IT infrastructure maintains and supports data without always having the full context for how data can and should be used in an organization. The use of [governance domains](unified-catalog-governance-domains) brings users and data together with a data-use driven structure. This article covers how to create and manage governance domains in Microsoft Purview Unified Catalog.

## Prerequisites

- To create a governance domain, you must have the [governance domain creator role](data-governance-roles-permissions#catalog-level-permissions).
- To assign data stewards or data product owners, you must have [governance domain owner permissions](data-governance-roles-permissions#how-to-assign-and-manage-role-groups).
- To curate data, such as adding glossary terms or objectives and key results (OKRs) to a governance domain, you must have [Data Steward permissions](data-governance-roles-permissions#governance-domain-level-permissions).
- To add data products to a governance domain, you must have [Data Product Owner permissions](data-governance-roles-permissions#governance-domain-level-permissions).

## Access governance domains

To see governance domains, you need the Global Catalog Reader role or the Local Catalog Reader role, which is a more restrictive role. For details about each role, see [Catalog level permissions](data-governance-roles-permissions#catalog-level-permissions) and [Governance domain level permissions](data-governance-roles-permissions#governance-domain-level-permissions).

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), open **Unified Catalog**.
2. Under **Catalog management**, select **Governance domains**. You see a list of all the governance domains in your organization. You can filter the governance domains by keyword.
3. Select a governance domain to see its details, roles, aggregate [data quality](unified-catalog-data-quality) score, [health actions](unified-catalog-data-health-management-actions-page), associated [data products](unified-catalog-data-products), [glossary terms](unified-catalog-glossary-terms), [OKRs](unified-catalog-okrs), and [critical data](unified-catalog-critical-data-elements).

### Details

The **Details** tab shows key information about the domain and displays all associated business concepts.

### Custom attributes

Under **Custom attributes**, you can see any [custom attribute groups and attributes](unified-catalog-attributes-business-concept) within groups, and the values set for each attribute. Only attributes with values are shown by default, but you can toggle **Show attributes without a value** on to view all attributes.

### Roles

The **Roles** tab displays the users in your organization (grouped by role) who are associated to the domain. For details, see edit roles for governance domains.

### Data estate mappings

Use the **Data estate mappings** tab to map your domain to a specific Data Map collection. For more information, see setting up data estate mappings.

### Data observability (preview)

The **Observability** (preview) tab provides a detailed view of data health and lineage. This view requires a [brief setup process](unified-catalog-observability-setup). For more information, see the [observability view for governance domains](unified-catalog-observability-views#governance-domains-data-observability).

### Monitoring

Select **Monitoring** on the **Details** page of a governance domain to view the status of bulk import jobs. The **Monitoring** page displays the status of bulk imports of glossary terms, data products, and critical data elements. The page will also list any upload errors and how to fix them.

## Edit roles

To edit the users, groups, or service principals assigned to a role:

1. Go to the governance domain where you want to edit the roles.
2. On the **Roles** tab, select the **+** button next to the role name where you want to add the user.
3. Search for users, groups, or service principals to add to the role and select them.
4. To remove users from the list, select the **X** next to their name.
5. When you're done, select **Save**.

For more information, see [roles assigned at the governance domain level](data-governance-roles-permissions#governance-domain-level-permissions).

## View your business concepts

Your governance domain has many business concepts associated with it: [data products](unified-catalog-data-products), [glossary terms](unified-catalog-glossary-terms), [OKRs](unified-catalog-okrs), and [critical data](unified-catalog-critical-data-elements).

You can find and view each of these concepts in your governance domain in the **Business concepts** area on the governance domain's **Details** tab. Select the card for each concept to view its details.

To add any of these concepts to your governance domain, see:

- [Add data products](unified-catalog-data-products-create-manage#create-data-products).
- [Add glossary terms](unified-catalog-glossary-terms-create-manage#create-glossary-terms).
- [Add OKRs](unified-catalog-okrs-create-manage#create-okrs).
- [Add critical data](unified-catalog-critical-data-elements#create-critical-data).

### Filter your view by custom attribute

You can use [business concept attributes](unified-catalog-attributes-business-concept) as a filter when exploring business concepts in a governance domain.

1. On a governance domain details page, select **View all** on a business concept card.
2. Select **Add filter**.
3. At **Filter**, select an attribute name from the dropdown list.
4. At **Operator**, select a condition, such as **Equals** or **Starts with**, which varies based on the kinds of values allowed by the attribute.
5. At **Value**, enter your value.
6. Select **Apply**.

## Create governance domains

Note

To create a governance domain, you need the [governance domain creator role.](data-governance-roles-permissions#governance-domain-level-permissions)

1. In Unified Catalog, select **Catalog management**, then select **Governance domains**.
2. Select **New Governance domain**.
3. On the **Basic details** page, enter a unique name for your governance domain and a description.
4. Select the governance domain **Type**: Functional unit, line of business, data domain, regulatory, or project. **Type** is an extra descriptor to indicate your governance domain's purpose. There aren't any behavioral differences between types.
5. Select an existing domain as a parent domain (optional). Parent/child relationships appear in a tree-like hierarchy. 
    Note

    Governance domain hierarchies in Unified Catalog can support as many as 200 domains, including a maximum of five levels of depth.
6. Select **Next**.
7. On the **Custom attributes** page, you can set values for all [custom attributes](unified-catalog-attributes-business-concept) defined by your admin in the **Custom attributes** section of the catalog. If the attribute is marked as required, you need to fill out all values on this page before you can complete the process.
8. Select **Create**.

You see your governance domain in the list of domains. Other users can't see this governance domain until you set its status to **Published**. You must also publish your domain before you can publish business concepts, like glossary terms or data products, within it.

Tip

Find [guidance on what governance domains to create in your organization](unified-catalog-plan#governance-domain-structure-models).

## Manage governance domains

Note

To edit a governance domain, you need the [governance domain owner role.](data-governance-roles-permissions#governance-domain-level-permissions)

1. On the governance domain's details page, select **Edit**.
2. You can edit the domain's name, description, owner, and status.
3. When you're done, select **Save**.

To add data products to a governance domain, see [Create and manage data products](unified-catalog-data-products-create-manage).

Note

If a governance domain becomes uneditable because the owner leaves the organization, Data Governance admins can add new governance domain owners in the **Roles** tab.

### Configure data estate mappings

You can map your governance domains to [collections in your Data Map](data-map-domains-collections-manage) to direct your data stewards and data product owners to build business concepts from data assets belonging to specific collections. This mapping is meant to be recommended guidance, as these Data Governance roles require Data Map permissions to access the data assets.

To map your governance domain to a specific Data Map collection:

1. Go to the **Data estate mappings** tab in a governance domain.
2. Use the **Select a mapping** dropdown menu to select the collection you want to associate your governance domain with.

    Note

    You can only see the [collections that you have access to in Data Map](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).
3. Select **Save**.

## Delete governance domains

To delete a governance domain, unpublish it and delete all business concepts within it, including any subdomains. Then select the **Delete** button to delete the governance domain.

## Manage domain policies

To manage domain policies, you need [data owner or data steward](data-governance-roles-permissions) permissions.

1. On your governance domain's page, select **Configure access**.
2. From the policy configuration window, you can create and manage your access policies. For more information, see [how to manage access policies](unified-catalog-data-product-access-policies#set-up-data-product-access-policies).

## Access classic experiences in the governance domain

You can access classic glossaries, business assets, or managed attributes by going to **Catalog management**, then selecting **Classic types**.

Select a tab to access your classic experiences: **Glossaries**, **Business assets**, **Asset types**, or **Managed attributes**.