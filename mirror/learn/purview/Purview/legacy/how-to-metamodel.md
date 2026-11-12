---
layout: Conceptual
title: Manage assets and asset types with metamodel | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-metamodel
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Manage asset types with Microsoft Purview metamodel.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: evwhite
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-how-to-pattern, msecd-doc-authoring-1030
locale: en-us
document_id: 02831929-997f-828b-46bd-4458881f5aaf
document_version_independent_id: 02831929-997f-828b-46bd-4458881f5aaf
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-metamodel.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-metamodel
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-metamodel.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: c0190176-b0a4-ba2c-389e-abfdc6196172
---

# Manage assets and asset types with metamodel | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

Note

On April 22, 2024 asset types moved to be under the Microsoft Purview Data Catalog feature in the Microsoft Purview portal. Access instructions have been updated.

Metamodel is a feature in the Microsoft Purview Data Map that gives the technical data in your data map relationships and reference points to make it easier to navigate and understand in the day to day. Like adding streets and cities to a map, the metamodel orients users so they know where they're and can discover the information they need.

Create additional asset types for describing real-world things in your organization such as departments, projects, products, and lines of business. When you look at your data estate, it's often helpful to understand how your data fits into your business. Use business assets whenever you want to associate data assets to specific organizational structures, business processes, or other anything else that could be convincingly modeled as an entity.

In the example below, I describe more business context for the SalesOrderDetail table by showing that the Supply chain department (a business asset) manages the order fulfillment business process (a business asset) which uses the SalesOrderDetail table. Visualizing business context in this way can help others identify the “official” dataset that's used for a particular business purpose and understand whether data is being used compliantly.

![Screen shot showing relationships between the supply chain department, order fulfillment business process, and SalesOrderDetail table.](../media/concept-annotations/05-business-assets.png)

This article will get you started in building a metamodel for your Microsoft Purview Data Map.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- Create a new, or use an existing Microsoft Purview account. You can [follow our quick-start guide to create one](../create-microsoft-purview-portal).
- [Data Curator role](../data-gov-classic-permissions#roles) on the collection where the data asset is housed and/or the root collection, depending on what you need. See the guide on [managing Microsoft Purview role assignments](../data-gov-classic-permissions#assign-permissions-to-your-users).
    - Create and modify asset types, modify assets - Data Curator on the collection where the data asset is housed. An asset will need to be moved to your collection after creation for you to be able to modify it.
    - Create and modify assets - Data curator on the root collection.

    Note

    Even if you are using the [new data catalog experience](../unified-catalog) these permissions are required.

## Current limitations

Note

Since this feature is in preview, available abilities are regularly updated.

- When a new asset created, you have to refresh the asset to see relationships
- You can't set relationships between two data assets in the Microsoft Purview governance portal
- The related tab only shows a "business lineage" view for business assets, not data assets

## Create and modify asset types

1. To open asset types in the Microsoft Purview Data Catalog:

    - If you're using the [new data catalog experience](../unified-catalog) in the [Microsoft Purview portal](../purview-portal) (https://purview.microsoft.com):
        1. Open the data catalog application
        2. Select the **Data management** dropdown
        3. Select **Governance domains**
        4. Select a domain where you want to add your managed attribute.
        5. Select the **Governance domains** header
        6. Select **Asset types**
    - If you're using the classic data catalog experience in the [Microsoft Purview portal](../purview-portal) (https://purview.microsoft.com):
        1. Open the data catalog application
        2. Select the **Metamodel** dropdown
        3. Select **Asset types**
    - If you're using the [classic Microsoft Purview governance portal](../use-microsoft-purview-governance-portal) (https://web.purview.azure.com):
        1. Open the Microsoft Purview Data Map
        2. Select **Asset types** under the **Metamodel** section.
2. You’ll see a list of available asset types. Predefined asset types will have unique icons. All custom assets are designated with a puzzle piece icon.
3. To create a new asset type, select **New asset type** and add a name, description, and attributes.

    [![Screenshot of the asset types page in the Microsoft Purview Data Map, with the buttons in steps 1 through 3 highlighted.](../media/how-to-metamodel/create-and-modify-metamodel-asset-types-inline.png)](../media/how-to-metamodel/create-and-modify-metamodel-asset-types.png#lightbox)
4. To define a relationship between two asset types, select **New relationship type**.
5. Give the relationship a name and define its reverse direction. Assign it to one or more pairs of assets. Select **Create** to save your new relationship type.

    ![Screenshot of the new relationship type page with a relationship defined and the create button highlighted.](../media/how-to-metamodel/create-new-relationship-type.png)
6. As you create more asset types, your canvas might get crowded with asset types. To hide an asset from the canvas, select the eye icon on the asset card.

    ![Screenshot of an asset card in the asset types canvas, the eye icon in the right corner is highlighted.](../media/how-to-metamodel/hide-asset.png)
7. To add an asset type back to the canvas, drag it from the left panel.

    ![Screenshot of the asset list to the left of the asset canvas with one item highlighted.](../media/how-to-metamodel/add-asset.png)

## Create and modify assets

1. When you’re ready to begin working with assets, navigate to your data catalog. If you're using the [classic Microsoft Purview portal](../use-microsoft-purview-governance-portal), select **Business assets**. If you're using the [new Microsoft Purview portal](../purview-portal) under **Business glossary** select **Business assets**.

    Note

    If you're using the [new data catalog experience](../unified-catalog), you'll need to switch back to the original experience to update your business assets.
2. To create a new asset, select **New asset**, select the asset type from the drop-down menu, give it a name, description, and complete any required attributes. Select **Create** to save your new asset.

    ![Screenshot of the business assets page with the new asset button highlighted.](../media/how-to-metamodel/select-new-asset.png)

    ![Screenshot of the new asset page with a name and description added and the create button highlighted.](../media/how-to-metamodel/create-new-asset.png)
3. To establish a relationship between two assets, go to the asset detail page and select **Edit &gt; Related**, and the relationship you’d like to populate.

    ![Screenshot of an asset page with the edit button highlighted.](../media/how-to-metamodel/select-edit.png)

    ![Screenshot of the edit asset page with the Related tab open and the relationships highlighted.](../media/how-to-metamodel/establish-relationships.png)
4. Select the assets or assets you’d like to link from the data catalog and select **OK**.

    ![Screenshot of the select assets page with two assets selected and the Ok button highlighted.](../media/how-to-metamodel/select-related-assets.png)
5. Save your changes. You can see the relationships you established in the asset overview.
6. In the **Related** tab of the asset you can also explore a visual representation of related assets.

    ![Screenshot of the related tab of a business asset.](../media/how-to-metamodel/visualize-related-assets.png)

    Note

    This is the experience provided by default from Atlas.

## Predefined asset types

An asset type is a template for storing a concept that’s important to your organization—anything you might want to represent in your data map alongside your physical metadata. You can create your own, but Purview also comes with a prepackaged set of business asset types you can modify to meet your needs.

| Asset Type | Description |
| --- | --- |
| Application service | A well-defined software component, especially one that implements a specific business function such as on-boarding a new customer, taking an order, or sending an invoice. |
| Business process | A set of activities that are performed in coordination in an organizational or technical environment that jointly realizes a business goal. |
| Data Domain | A category of data that is governed or explicitly managed for master data management. |
| Department | An organizational subunit that only has full recognition within the context of that organization. A department wouldn't be regarded as a legal entity in its own right. |
| Line of business | An organization subdivision focused on a single product or family of products. |
| Organization | A collection of people organized together into a community or other social, commercial, or political structure. The group has some common purpose or reason for existence that goes beyond the set of people belonging to it and can act as a unit. Organizations are often decomposable into hierarchical structures. |
| Product | Any offered product or service. |
| Project | A specific activity used to control the use of resources and associated costs so they're used appropriately in order to successfully achieve the project's goals, such as building a new capability or improving an existing capability. |
| System | An IT system including hardware and software. |