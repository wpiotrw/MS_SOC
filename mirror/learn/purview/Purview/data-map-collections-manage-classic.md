---
layout: Conceptual
title: Manage domains and collections in Data Map (classic) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-collections-manage-classic
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article explains how to create and manage collections within the classic Microsoft Purview Data Map.
ms.custom: sfi-image-nochange
locale: en-us
document_id: e476ebab-bce0-1f50-f99c-7fab3a63aa4d
document_version_independent_id: e476ebab-bce0-1f50-f99c-7fab3a63aa4d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-collections-manage-classic.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-collections-manage-classic
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-collections-manage-classic.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 64b2172f-26b9-4b53-fdef-f71955463788
---

# Manage domains and collections in Data Map (classic) | Microsoft Learn

Tip

If you're using the new [Microsoft Purview portal experience](portal), refer instead to [how to create and manage domains and collections](data-map-domains-collections-manage).

Collections in the Microsoft Purview Data Map can be used to organize assets and sources by your business's flow. They're also the tool used to manage access across the classic Microsoft Purview governance portal. This guide will take you through the creation and management of these collections, as well as cover steps about how to register sources and add assets into your collections.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- Your own [Microsoft Entra tenant](/en-us/azure/active-directory/fundamentals/active-directory-access-create-new-tenant).
- An active [Microsoft Purview (formerly Azure Purview) account](create-microsoft-purview-portal).

### Check permissions

In order to create and manage collections in the Data Map, you'll need to be a **Collection Admin** within the classic Microsoft Purview governance portal. We can check these permissions in the classic [Microsoft Purview governance portal](https://web.purview.azure.com/resource/). You can find the portal by:

- Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
- Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**Microsoft Purview governance portal**](https://web.purview.azure.com/) button.

1. Select Data Map &gt; Collections from the left pane to open collection management page.

    ![Screenshot of Microsoft Purview governance portal window, opened to the Data Map, with the Collections tab selected.](media/how-to-create-and-manage-collections/find-collections.png)
2. Select your root collection. This is the top collection in your collection list and will have the same name as your account. In the following example, it's called Contoso Microsoft Purview. Alternatively, if collections already exist you can select any collection where you want to create a subcollection.

    ![Screenshot of Microsoft Purview governance portal window, opened to the Data Map, with the root collection highlighted.](media/how-to-create-and-manage-collections/select-root-collection.png)
3. Select **Role assignments** in the collection window.

    ![Screenshot of Microsoft Purview governance portal window, opened to the Data Map, with the role assignments tab highlighted.](media/how-to-create-and-manage-collections/role-assignments.png)
4. To create a collection, you'll need to be in the collection admin list under role assignments. If you created the account, you should be listed as a collection admin under the root collection already. If not, you'll need to contact the collection admin to grant your permission.

    ![Screenshot of Microsoft Purview governance portal window, opened to the Data Map, with the collection admin section highlighted.](media/how-to-create-and-manage-collections/collection-admins.png)

## Collection management

### Create a collection

You'll need to be a collection admin in order to create a collection. If you aren't sure, follow the guide above to check permissions.

1. Select Data Map &gt; Collections from the left pane to open collection management page.

    ![Screenshot of Microsoft Purview governance portal window, opened to the Data Map, with the Collections tab selected and open.](media/how-to-create-and-manage-collections/find-collections.png)
2. Select **+ Add a collection**. Again, note that only collection admins can manage collections.

    ![Screenshot of Microsoft Purview governance portal window, showing the new collection window, with the 'Add a collection' button highlighted.](media/how-to-create-and-manage-collections/select-add-a-collection.png)
3. In the right panel, enter the collection name and description. If needed you can also add users or groups as collection admins to the new collection.
4. Select **Create**.

    ![Screenshot of Microsoft Purview governance portal window, showing the new collection window, with a display name and collection admins selected, and the create button highlighted.](media/how-to-create-and-manage-collections/create-collection.png)
5. The new collection's information will reflect on the page.

    ![Screenshot of Microsoft Purview governance portal window, showing the newly created collection window.](media/how-to-create-and-manage-collections/created-collection.png)

### Edit a collection

1. Select **Edit** either from the collection detail page, or from the collection's dropdown menu.

    ![Screenshot of Microsoft Purview governance portal window, open to collection window, with the 'edit' button highlighted both in the selected collection window, and under the ellipsis button next to the name of the collection.](media/how-to-create-and-manage-collections/edit-collection.png)
2. Currently collection description and collection admins can be edited. Make any changes, then select **Save** to save your change.

    ![Screenshot of Microsoft Purview governance portal window with the edit collection window open, a description added to the collection, and the save button highlighted.](media/how-to-create-and-manage-collections/edit-description.png)

### View Collections

1. Select the triangle icon beside the collection's name to expand or collapse the collection hierarchy. Select the collection names to navigate.

    ![Screenshot of Microsoft Purview governance portal collection window, with the button next to the collection name highlighted.](media/how-to-create-and-manage-collections/subcollection-menu.png)
2. Type in the filter box at the top of the list to filter collections.

    ![Screenshot of Microsoft Purview governance portal collection window, with the filter above the collections highlighted.](media/how-to-create-and-manage-collections/filter-collections.png)
3. Select **Refresh** in Root collection's contextual menu to reload the collection list.

    ![Screenshot of Microsoft Purview governance portal collection window, with the button next to the Resource name selected, and the refresh button highlighted.](media/how-to-create-and-manage-collections/refresh-collections.png)
4. Select **Refresh** in collection detail page to reload the single collection.

    ![Screenshot of Microsoft Purview governance portal collection window, with the refresh button under the collection window highlighted.](media/how-to-create-and-manage-collections/refresh-single-collection.png)

### Delete a collection

You'll need to be a collection admin in order to delete a collection. If you aren't sure, follow the guide above to check permissions. Collection can be deleted only if no child collections, assets, data sources or scans are associated with it.

1. Select **Delete** from the collection detail page.

    ![Screenshot of Microsoft Purview governance portal window to delete a collection](media/how-to-create-and-manage-collections/delete-collections.png)
2. Select **Confirm** when prompted, **Are you sure you want to delete this collection?**

    ![Screenshot of Microsoft Purview governance portal window showing confirmation message to delete a collection](media/how-to-create-and-manage-collections/delete-collection-confirmation.png)
3. Verify deletion of the collection from your Data Map.

### Move registered sources between collections

You can move registered sources from one collection to another you have access to. For steps, see [Manage data sources](data-map-data-sources-register-manage#move-sources-between-collections).

## Add roles and restrict access through collections

Since permissions are managed through collections in Data Map, it's important to understand the roles and what permissions they'll give your users. A user granted permissions on a collection will have access to sources and assets associated with that collection, and inherit permissions to subcollections. Inheritance can be restricted, but is allowed by default.

The following guide will discuss the roles, how to manage them, and permissions inheritance.

### Roles

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

## Register source to a collection

1. Select **Register** or register icon on collection node to register a data source. Only a data source admin can register sources.

    ![Screenshot of the data map Microsoft Purview governance portal window with the register button highlighted both at the top of the page and under a collection.](media/how-to-create-and-manage-collections/register-by-collection.png)
2. Fill in the data source name, and other source information. It lists all the collections where you have scan permission on the bottom of the form. You can select one collection. All assets under this source will belong to the collection you select.

    ![Screenshot of the source registration window.](media/how-to-create-and-manage-collections/register-source.png)
3. The created data source will be put under the selected collection. Select **View details** to see the data source.

    ![Screenshot of the data map Microsoft Purview governance portal window with the newly added source card highlighted.](media/how-to-create-and-manage-collections/see-registered-source.png)
4. Select **New scan** to create scan under the data source.

    ![Screenshot of a source Microsoft Purview governance portal window with the new scan button highlighted.](media/how-to-create-and-manage-collections/new-scan.png)
5. Similarly, at the bottom of the form, you can select a collection, and all assets scanned will be included in the collection. The collections listed here are restricted to subcollections of the data source collection.

    ![Screenshot of a new scan window with the collection dropdown highlighted.](media/how-to-create-and-manage-collections/scan-under-collection.png)
6. Back in the collection window, you'll see the data sources linked to the collection on the sources card.

    ![Screenshot of the data map Microsoft Purview governance portal window with the newly added source card highlighted in the map.](media/how-to-create-and-manage-collections/source-under-collection.png)

## Add assets to collections

Assets and sources are also associated with collections. During a scan, if the scan was associated with a collection the assets will be automatically added to that collection, but can also be manually added to any subcollections.

1. Check the collection information in asset details. You can find collection information in the **Collection path** section on right-top corner of the asset details page.

    ![Screenshot of Microsoft Purview governance portal asset window, with the collection path highlighted.](media/how-to-create-and-manage-collections/collection-path.png)
2. Permissions in asset details page:

    1. Check the collection-based permission model by following the add roles and restricting access on collections guide above.
    2. If you don't have read permission on a collection, the assets under that collection won't be listed in search results. If you get the direct URL of one asset and open it, you'll see the no access page. Contact your collection admin to grant you the access. You can select the **Refresh** button to check the permission again.

        ![Screenshot of Microsoft Purview governance portal asset window where the user has no permissions, and has no access to information or options.](media/how-to-create-and-manage-collections/no-access.png)
    3. If you have the read permission to one collection but don't have the write permission, you can browse the asset details page, but the following operations are disabled:

        - Edit the asset. The **Edit** button will be disabled.
        - Delete the asset. The **Delete** button will be disabled.
        - Move asset to another collection. The ellipsis button on the right-top corner of Collection path section will be hidden.
    4. The assets in **Hierarchy** section are also affected by permissions. Assets without read permission will be grayed.

        ![Screenshot of Microsoft Purview governance portal hierarchy window where the user has only read permissions, and has no access to options.](media/how-to-create-and-manage-collections/hierarchy-permissions.png)

### Move asset to another collection

1. Select the ellipsis button on the right-top corner of Collection path section.

    ![Screenshot of Microsoft Purview governance portal asset window with the collection path highlighted and the ellipsis button next to collection path selected.](media/how-to-create-and-manage-collections/move-asset.png)
2. Select the **Move to another collection** button.
3. In the right side panel, choose the target collection you want move to. You can only see the collections where you have write permissions. The asset can also only be added to the subcollections of the data source collection.

    ![Screenshot of Microsoft Purview governance portal pop-up window with the select a collection dropdown menu highlighted.](media/how-to-create-and-manage-collections/move-select-collection.png)
4. Select **Move** button on the bottom of the window to move the asset.

## Search and browse by collections

### Search by collection

1. In the classic Microsoft Purview governance portal, the search bar is located at the top of the portal window.

    ![Screenshot showing the location of the classic Microsoft Purview governance portal search bar.](media/how-to-create-and-manage-collections/purview-search-bar.png)
2. When you select the search bar, you can see your recent search history and recently accessed assets. Select **View all** to see all of the recently viewed assets.

    ![Screenshot showing the search bar before any keywords have been entered](media/how-to-create-and-manage-collections/search-no-keywords.png)
3. Enter in keywords that help identify your asset such as its name, data type, classifications, and glossary terms. As you enter in keywords relating to your desired asset, the classic Microsoft Purview governance portal displays suggestions on what to search and potential asset matches. To complete your search, select **View search results** or press **Enter**.

    ![Screenshot showing the search bar as a user enters in keywords](media/how-to-create-and-manage-collections/search-keywords.png)
4. The search results page shows a list of assets that match the keywords provided in order of relevance. There are various factors that can affect the relevance score of an asset. You can filter down the list more by selecting specific collections, data stores, classifications, contacts, labels, and glossary terms that apply to the asset you're looking for.

    ![Screenshot showing the results of a search](media/how-to-create-and-manage-collections/search-results.png)
5. Select your desired asset to view the asset details page where you can view properties including schema, lineage, and asset owners.

    ![Screenshot showing search results with collections.](media/how-to-create-and-manage-collections/search-by-collection.png)

### Browse by collection

1. You can browse data assets, by selecting the **Browse assets** on the homepage.

    ![Screenshot of the catalog Microsoft Purview governance portal window with the browse assets button highlighted.](media/how-to-create-and-manage-collections/browse-by-collection.png)
2. On the Browse asset page, select **By collection** pivot. Collections are listed with hierarchical table view. To further explore assets in each collection, select the corresponding collection name.

    ![Screenshot of the asset Microsoft Purview governance portal window with the by collection tab selected.](media/how-to-create-and-manage-collections/by-collection-view.png)
3. On the next page, the search results of the assets under selected collection will be shown. You can narrow the results by selecting the facet filters. Or you can see the assets under other collections by selecting the sub/related collection names.

    ![Screenshot of the catalog Microsoft Purview governance portal window with the by collection tab selected.](media/how-to-create-and-manage-collections/search-results-by-collection.png)
4. To view the details of an asset, select the asset name in the search result. Or you can check the assets and bulk edit them.

    ![Screenshot of the catalog Microsoft Purview governance portal window with the by collection tab selected and asset check boxes highlighted.](media/how-to-create-and-manage-collections/view-asset-details.png)

## Rename collections (preview)

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

1. In the classic Microsoft Purview governance portal, navigate to the collection that you want to rename.
2. Select **Edit** either from the collection detail page, or from the collection's dropdown menu.

    ![Screenshot of Microsoft Purview governance portal window to edit and rename a collection, open to collection window, with the 'edit' button highlighted both in the selected collection window, and under the ellipsis button next to the name of the collection.](media/how-to-create-and-manage-collections/edit-rename-collection.png)
3. Provide a new friendly name and select **Save** to save your change.

    ![Screenshot of Microsoft Purview governance portal window with the rename collection window open.](media/how-to-create-and-manage-collections/rename-collection.png)

## Move collections (preview)

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

1. In the classic Microsoft Purview governance portal, navigate to the collection that you want to move to a different parent collection.
2. Select the ellipsis button on the right-top corner of collection path section and select **Move to another collection**.

    ![Screenshot of Microsoft Purview governance portal window to move a collection, open to collection window, ellipsis and move to another collection highlighted.](media/how-to-create-and-manage-collections/move-collection.png)
3. From **Select parent collection** dropdown list, select a new parent for the collection and select **OK**.

    ![Screenshot of Microsoft Purview governance portal window with the move collection window open.](media/how-to-create-and-manage-collections/move-collection-new-parent.png)