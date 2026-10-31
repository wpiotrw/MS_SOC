---
layout: Conceptual
title: Create a collection in classic Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-collections-create-classic
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
description: Learn how to create a collection and add permissions, register sources, and register assets to collections in the classic Data Map experience.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 3ec7ac87-7eb2-8302-e15c-2b25c2ba29f7
document_version_independent_id: 3ec7ac87-7eb2-8302-e15c-2b25c2ba29f7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-collections-create-classic.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-collections-create-classic
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-collections-create-classic.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 27110b47-8942-a731-f519-46b7b7c6e360
---

# Create a collection in classic Microsoft Purview Data Map | Microsoft Learn

Collections are the Microsoft Purview Data Map's tool to manage ownership and access control across assets, sources, and information. They also organize your sources and assets into categories that are customized to match your management experience with your data. This guide takes you through setting up your first collection and collection admin to prepare your Microsoft Purview environment for your organization.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- Your own [Microsoft Entra tenant](/en-us/azure/active-directory/fundamentals/active-directory-access-create-new-tenant).
- An active [Microsoft Purview account](create-microsoft-purview-portal).

## Check permissions

In order to create and manage collections in Data Map, you need to be a **Collection Admin** within the classic Microsoft Purview governance portal. We can check these permissions in the [governance portal](use-microsoft-purview-governance-portal). You can find the governance portal by:

- Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
- Open the [Azure portal](https://portal.azure.com), search for and select the Microsoft Purview account you want to use to receive the share. Open the classic [Microsoft Purview governance portal](https://web.purview.azure.com/).

1. Select Data Map &gt; Collections from the left pane to open collection management page.

    ![Screenshot of the classic Microsoft Purview governance portal opened to the Data Map, with the Collections tab selected.](media/quickstart-create-collection/find-collections.png)
2. Select your root collection. This is the top collection in your collection list and will have the same name as your Microsoft Purview account. In our example below, it's called ContosoPurview.

    ![Screenshot of the classic Microsoft Purview governance portal window, opened to the Data Map, with the root collection highlighted.](media/quickstart-create-collection/select-root-collection.png)
3. Select role assignments in the collection window.

    ![Screenshot of the classic Microsoft Purview governance portal window, opened to the Data Map, with the role assignments tab highlighted.](media/quickstart-create-collection/role-assignments.png)
4. To create a collection, you need to be in the collection admin list under role assignments. If you created the account, you should be listed as a collection admin under the root collection already. If not, you need to contact the collection admin to grant you permission.

    ![Screenshot of the classic Microsoft Purview governance portal window, opened to the Data Map, with the collection admin section highlighted.](media/quickstart-create-collection/collection-admins.png)

## Create a collection in the portal

To create your collection, start in the classic [Microsoft Purview governance portal](use-microsoft-purview-governance-portal). You can find the portal by:

- Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
- Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Select the classic [**Microsoft Purview governance portal**](https://web.purview.azure.com/) button.

1. Select Data Map &gt; Collections from the left pane to open collection management page.

    ![Screenshot of the classic Microsoft Purview governance portal window, opened to the Data Map, with the Collections tab selected.](media/quickstart-create-collection/find-collections.png)
2. Select **+ Add a collection**.

    ![Screenshot of the classic Microsoft Purview governance portal window, opened to the Data Map, with the Collections tab selected and Add a Collection highlighted.](media/quickstart-create-collection/select-add-collection.png)
3. In the right panel, enter the collection name, description, and search for users to add them as collection admins.

    ![Screenshot of the classic Microsoft Purview governance portal window, showing the new collection window, with a display name and collection admins selected, and the create button highlighted.](media/quickstart-create-collection/create-collection.png)
4. Select **Create**. The collection information displays on the page.

    ![Screenshot of the classic Microsoft Purview governance portal window, showing the newly created collection window.](media/quickstart-create-collection/created-collection.png)

## Assign permissions to collection

Now that you have a collection, you can assign permissions to this collection to manage your users access to the classic Microsoft Purview governance portal.

### Roles

All assigned roles apply to sources, assets, and other objects within the collection where the role is applied.

- **Collection admins** - can edit a collection, its details, manage access in the collection, and add subcollections.
- **Data source admins** - can manage data sources and data scans.
- **Data curators** - can create, read, modify, and delete actions on catalog data objects.
- **Data readers** - can access but not modify catalog data objects.

### Assign permissions

1. Select **Role assignments** tab to see all the roles in a collection.

    ![Screenshot of the classic Microsoft Purview governance portal collection window, with the role assignments tab highlighted.](media/quickstart-create-collection/select-role-assignments.png)
2. Select **Edit role assignments** or the person icon to edit each role member.

    ![Screenshot of the classic Microsoft Purview governance portal collection window, with the edit role assignments dropdown list selected.](media/quickstart-create-collection/edit-role-assignments.png)
3. Type in the textbox to search for users you want to add to the role member. Select **OK** to save the change.