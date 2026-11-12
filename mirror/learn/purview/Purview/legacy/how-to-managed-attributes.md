---
layout: Conceptual
title: Managed attributes in classic Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-managed-attributes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Apply business context to assets using managed attributes in the classic Microsoft Purview governance portal.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 5db655e9-fc5f-1910-4fd0-d1affb92f664
document_version_independent_id: 5db655e9-fc5f-1910-4fd0-d1affb92f664
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-managed-attributes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-managed-attributes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-managed-attributes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c2f42550-2cfe-341e-c7b3-8cc723269cfa
---

# Managed attributes in classic Microsoft Purview Data Map | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Managed attributes are user-defined attributes that provide a business or organization level context to an asset. When applied to assets, managed attributes enable data consumers using the data catalog to gain context on the role an asset plays in a business.

## Terminology

Important

Attributes for data assets are referred to by different names, depending on which portal you're using.

- In the Microsoft Purview portal, https://purview.microsoft.com, they're called **Data asset attributes**.
- In the classic Microsoft Purview governance portal, https://web.purview.azure.com, they're called **Managed attributes**.

This article explains working with **Managed attributes** in the classic governance portal (although the process for working with data asset attributes in the Microsoft Purview portal is the same).

- **Managed attribute:** A set of user-defined attributes that provide a business or organization level context to an asset. A managed attribute has a name and a value. For example, 'Department' is an attribute name and 'Finance' is its value.
- **Attribute group:** A grouping of managed attributes that allow for easier organization and consumption.

## Create managed attributes

1. Access managed attributes by following the steps corresponding to the portal you're using:

    - In the [Microsoft Purview portal](../purview-portal) (https://purview.microsoft.com):
        1. Under **Solutions**, select **Unified Catalog**.
        2. Under **Catalog management**, select **Custom metadata**, then select the **Data asset attributes** tab.
    - In the [classic Microsoft Purview governance portal](use-microsoft-purview-governance-portal) (https://web.purview.azure.com):
        1. Open **Data Map**.
        2. Under the **Annotation management**, select **Managed attributes**.
2. Select **New**, then select either **New attribute** or **New attribute group**.
3. To create an attribute group, enter a name and a description.
4. Managed attributes have a name, attribute group, data type, and associated asset types. They also have a required flag that can only be enabled when created as part of creating a new attribute group. Associated asset types are the data asset types you can apply the attribute to. For example, if you select "Azure SQL Table" for an attribute, it will be applied to Azure SQL Table assets, but not Azure Synapse Dedicated Table assets.
5. Select **Create** to save your attribute.

These attributes will be automatically applied to the specified resources without a value. You'll need to apply a value for each asset.

## Required managed attributes

When you create a managed attribute as part of a managed attribute group, you can add the **required** flag. The required flag means that a value must be provided for this managed attribute. When you edit a data asset, the required attribute must be filled out before you can close the editor.

Important

- You can only add the **required** flag when you create an attribute during the process of creating an attribute group. You can't add the **required** flag while creating a new attribute outside of an attribute group.
- If an existing attribute doesn't have the **required** flag, you can't add it during the editing process.
- Once you add the **required** flag, you can't remove it from the attribute.

1. Open Data Map and navigate to **Managed attributes** in the **Annotation management** section.
2. Select **New** and select **Attribute group**.
3. Select **New attribute**.
4. Fill out your attribute details, and select **Mark as required**.
5. Select **Apply** and finish adding other attributes to complete your attribute group.

## Add value for managed attribute

Once a managed attribute has been created, you'll need to add a value for each of your assets. You can add values to your assets by:

1. [Search for your data asset](../unified-catalog-data-assets-search).
2. On the overview for your asset, see the **Managed attributes** section with all attributes that have values. (You can see attributes without values by using the **Show attributes without a value** toggle.)
3. Select the **Edit** button.
4. Under **Managed attributes**, add values for each of your attributes.
5. If any attributes are **Required**, you won't be able to save until you add a value for that attribute.

## Expiring managed attributes

In the managed attribute management experience, managed attributes can't be deleted, only expired. Expired attributes can't be applied to any assets and are, by default, hidden in the user experience. By default, expired managed attributes aren't removed from an asset. If an asset has an expired managed attribute applied, it can only be removed, not edited.

Both attribute groups and individual managed attributes can be expired. To mark an attribute group or managed attribute as expired, select the **Edit** icon.

![Screenshot that shows how to edit an attribute group.](../media/how-to-managed-attributes/expire-attribute-group.png)

Select **Mark as expired** and confirm your change. Once expired, attribute groups and managed attributes can't be reactivated.

![Screenshot that shows the edit an attribute group window.](../media/how-to-managed-attributes/mark-as-expired.png)

## Create managed attributes using APIs

Managed attributes can be programmatically created and applied using the business metadata APIs in Apache Atlas 2.2. For more information, see the [Use Atlas 2.2 APIs](../data-gov-api-atlas-2-2) tutorial.

## Searching by managed attributes

Once you have created managed attributes, you can refine your [data catalog searches](../unified-catalog-data-assets-search) using these attributes.

1. In a data catalog search, to refine by a managed attribute, first select **Add filter** at the top of the search.

    ![Screenshot showing the add filter button highlighted on a search in the Data Catalog.](../media/how-to-managed-attributes/add-filter.png)
2. Select the drop-down, scroll to your list of managed attributes, and select one.

    ![Screenshot showing the filter dropdown with the list of added managed attributes highlighted.](../media/how-to-managed-attributes/select-managed-attributes.png)
3. Select your operator, which will be different based on the kinds of values allowed by the attribute. In this example, we've selected Cost Center, which is a text value, so we can compare Cost Center with the text we'll enter.

    ![Screenshot showing the filter operator dropdown with the available operators highlighted.](../media/how-to-managed-attributes/select-operator.png)
4. Enter your values, and the search runs with your new filter.

## Best practices for using managed attributes

Use managed attributes to extend the fields available for an asset in the Microsoft Purview Data Catalog. Managed attributes are key-value pairs that add structured metadata to your data catalog. When Microsoft Purview scans data, it adds technical information about the data like data type, classification, etc. If you want to add more fields, you need to define managed attributes.

In the following example, a managed attribute lets me tag tables with the department that publishes them. I use a managed attribute because I want to make sure assets are always tagged in exactly the same way with this information. I also want to filter by the publisher field when I search for data.

![Screen shot showing an asset detail page with a managed attribute key-value pair of publisher: supply chain.](../media/concept-annotations/02-managed-attribute.png)

The managed attribute in this example helps people quickly find all data published by the supply chain team, but doesn't help someone understand the definition of a publisher or what it means if supply chain is the publisher of the data. For any information that needs a business explanation, use [terms](../unified-catalog-glossary-terms).

## Known limitations

Below are the known limitations of the managed attribute feature as it currently exists in Microsoft Purview.

- Managed attributes can only be expired.
- Managed attributes can't be applied via the bulk edit experience.
- After creating an attribute group, you can't edit the name of the attribute group.
- After creating a managed attribute, you can't update the attribute name, attribute group, or the field type.
- A managed attribute can only be marked as required during the creation of an attribute group.