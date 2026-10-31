---
layout: Conceptual
title: Manage domains and collections in Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-domains-collections-manage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-06-25T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to create and manage domains and collections within Microsoft Purview Data Map.
locale: en-us
document_id: 130ce1b1-4927-3016-df8a-983a7cb2da01
document_version_independent_id: 130ce1b1-4927-3016-df8a-983a7cb2da01
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-domains-collections-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-domains-collections-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-domains-collections-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 558eccab-c47e-0eb7-dae6-f4c5a98d3c3c
---

# Manage domains and collections in Data Map | Microsoft Learn

Important

These features are only available if you're using the [Microsoft Purview portal](portal).

If you're using the classic governance experience (https://web.purview.azure.com/), see the [classic create and manage collections](data-map-collections-manage-classic) article instead.

Use domains and collections in Microsoft Purview Data Map to organize assets and sources by your business's flow. Use these tools to manage access across the Microsoft Purview portal. This article takes you through the creation and management of domains and collections. It also covers steps about how to register sources and add assets into your collections.

For more information, see [domains and the structure of Data Map](data-map-domains).

## Prerequisites

- A Microsoft Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- Your own [Microsoft Entra tenant](/en-us/azure/active-directory/fundamentals/active-directory-access-create-new-tenant).
- A Microsoft Purview account using the [Microsoft Purview portal](portal) experience.
- You need to be a **Microsoft Purview administrator** within the Microsoft Purview portal to manage domains. To check or set these roles, see our permissions documentation.

## Permissions to manage domains and collections

To manage domains, and permissions in domains, a user needs to be a [Purview administrator](data-governance-roles-permissions#tenant-level-role-groups) or a [domain admin](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

To manage collections, a user needs the Domain Administrator or Collection Administrator role in the Microsoft Purview portal. To check these permissions in the Microsoft Purview portal:

1. In the Microsoft Purview portal, open **Data Map**, then select **Domains** to open the domains management page.
2. Select your default domain, which is currently the only available domain.
3. Select the **Role assignments** tab.
4. Search under these roles for your user:
    - Domain administrators: To be able to manage the domain or permissions in it.
    - Collection administrators: To be able to create or manage collections in the domain.

Tip

If you don't have either of the needed permissions, contact the domain administrator to grant you permission.

## Default domain

Every Microsoft Purview Data Map starts with a default domain.

When an account is [upgraded to the new experience](account-upgrades#new-experience-for-existing-customers), the primary account's root collection becomes the default domain.

If you haven't [upgraded to the new experience](account-upgrades#new-experience-for-existing-customers) yet, take these points into consideration when choosing which account to elevate as your default domain:

- **Data Assets**: Choose the account with the most valuable or frequently used data assets, as this will become the default domain after the upgrade.
- **Account Usage**: Evaluate how each account is currently being used and its role within your organization. Accounts that are considered "production" would be most viable to select for this purpose.
- **Permissions and Access Controls**: Consider the existing permissions and access controls for each account, as they'll be carried over to the upgraded environment (as an isolated Domain). The permissions are applied in the new environment exactly as they are in the original environment. No more permissions are granted.

For more information about the new experience, see our guide on [governance in the new Microsoft Purview experience](account-upgrades).

## Custom domains

You can create up to four custom domains in your Data Map.

### Create custom domains

1. In **Data Map**, select **Domains**.
2. Select **New domain**.
3. On the **New domain** pane, enter a name for the domain, a description, and assign one or more domain administrators.
4. Select **Create**.

### Edit custom domains

You can modify the description or the administrators of your custom domains by editing them.

1. In **Data Map**, select **Domains**.
2. Select the domain you want to edit. On its details page, select **Edit**.

### Delete custom domains

Important

- Before you delete a custom domain, remove everything under it first. This list includes subcollections, data sources, scans, assets, glossaries, terms, credentials, Azure Key Vaults, and other related resources.
- You can't delete default domains.

To remove a domain, you need to have either Microsoft Purview administrator or domain administrator permissions.

1. In **Data Map**, select **Domains**.
2. Select the domain you want to delete.
3. Select the **Delete** button and confirm the deletion.

## Collection management

### Create a collection

You need to be a collection administrator or domain administrator within a domain order to create a collection. If you're not sure, see how to check permissions.

1. In **Data Map**, select **Domains**.
2. Use the dropdown next to your default domain to select your default domain, or select an existing collection where you want to make a child collection.
3. Select **+ New collection**. Only domain and collection admins can manage collections.
4. In the new collection window, enter the collection display name and description. If needed, you can also add users or groups as collection admins to the new collection.
5. Select **Create**.
6. The new collection's information appears in the collection list under your domain, and you're taken to your collection's detail page.

### Edit a collection

1. Select **Edit** either from the collection detail page, or from the collection's dropdown list.
2. Make changes, then select **Save**.

### View collections

1. On the **Domains** page in Data Map, select the arrow next to the collection's name to expand or collapse the collection hierarchy. Select the collection name to navigate.
2. Enter a name in the **Filter by name** box to filter collections.
3. Select **Refresh** in collection detail page to reload the single collection.

### Delete a collection

You need to be a domain administrator or a collection administrator to delete a collection. If you're not sure, check permissions. You can delete a collection only if it has no child collections, assets, data sources, or scans associated with it.

1. On the collection's details page, select **Delete**.
2. A confirmation window appears. Select **Confirm** to continue the deletion.
3. Verify deletion of the collection from your Data Map.

### Move registered sources between collections

You can move registered sources from one collection to another collection you have access to. For steps, see [Manage data sources](data-map-data-sources-register-manage#move-sources-between-collections).

## Add roles and restrict access

Since you manage permissions through domains and collections in Data Map, it's important to understand the roles and the permissions they give to your users.

You assign and inherit roles in domains and collections the same way. When you grant a user permissions on a domain or collection, they get access to sources and assets associated with that collection, and they inherit permissions to its subcollections. Inheritance can be restricted, but it's allowed by default.

The following guide discusses the roles, how to manage them, and permissions inheritance.

### Roles

All assigned roles apply to sources, assets, and other objects within the domain or collection where you apply the role.

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

## Register and scan source in a domain or collection

Important

Every source has its own prerequisites and information for registration and scanning. For detailed information, see [registration and scanning steps](data-map-data-sources) for each data source.

1. In the Microsoft Purview portal, open **Data Map**.
2. Select **Data sources** from the left pane to open the data sources map page.
3. Select **Register** or the register icon on a domain or collection node to register a data source. Only data source admins can register sources.
4. Enter the data source name and other source information.
5. Select a domain.
6. Select a collection. To register the resource in the domain, choose the **Select domain only** option. All assets under this source belong to the domain or collection you select.

    ![Screenshot of the Register data source page, showing a domain selected a Select domain only selected for the collection.](media/how-to-create-and-manage-domains-collections/register-source.png)
7. The created data source is put under the selected domain or collection. Select **View details** to see the data source.

    ![Screenshot of the data map Microsoft Purview portal window with the newly added source card highlighted.](media/how-to-create-and-manage-domains-collections/see-registered-source.png)
8. Select **New scan** to create scan under the data source.

    ![Screenshot of a source Microsoft Purview portal window with the new scan button highlighted.](media/how-to-create-and-manage-domains-collections/new-scan.png)
9. When creating a scan, you can select a collection and all assets scanned are included in that collection. Collections listed in a scan are subcollections of the data source collection.

    ![Screenshot of a new scan window with the collection dropdown highlighted.](media/how-to-create-and-manage-domains-collections/scan-under-collection.png)
10. After your scan, you see the data sources linked to the collection or domain on their data sources card.

## Add assets to collection and domains

Assets and sources are also associated with domains and collections. During a scan, if you associate the scan with a domain or collection, the assets are automatically added to that resource. You can also manually move the assets to any subcollections if you have the write permissions on those subcollections.

1. Check the domain and collection information in asset details. You can find information in the **Collection path** section on right-top corner of the asset details page.

    ![Screenshot of Microsoft Purview portal asset window, with the collection path highlighted.](media/how-to-create-and-manage-domains-collections/collection-path.png)
2. Select the ellipsis button on the right-top corner of the **Collection path** section.

    ![Screenshot of Microsoft Purview portal asset window with the collection path highlighted and the ellipsis button next to collection path selected.](media/how-to-create-and-manage-domains-collections/move-asset.png)
3. Select the **Move to another collection** button.
4. In the right side panel, choose the target collection you want move to. You can only see the collections where you have write permissions. You can only add the asset to the subcollections of the data source collection.

    ![Screenshot of Microsoft Purview portal pop-up window with the select a collection dropdown menu highlighted.](media/how-to-create-and-manage-domains-collections/move-select-collection.png)
5. Select **Move** button on the bottom of the window to move the asset.

## Rename collections

1. In Data Map, navigate to the collection that you want to rename.
2. Select **Edit** either from the collection detail page, or from the collection's dropdown menu.
3. Enter a new friendly name and select **Save**.

## Move collections

1. In the Microsoft Purview portal, go to the collection that you want to move to a different parent collection.
2. Select the ellipsis button in the upper-right corner of the collection path section and select **Move to another collection**.
3. From the **Select parent collection** dropdown list, select a new parent for the collection and select **OK**.

## Best practices

- [Domains and collections architecture best practices](data-gov-best-practices-domains-collections)
- [Data Map domains and governance domains best practices](data-gov-best-practices-domains-and-gov-domains)