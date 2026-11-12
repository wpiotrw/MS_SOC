---
layout: Conceptual
title: Data asset attributes in Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-attributes-data-asset
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to apply business context to data assets using data asset attributes in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 62725ed6-864b-8a39-f724-0046ad0e2fb4
document_version_independent_id: 62725ed6-864b-8a39-f724-0046ad0e2fb4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-attributes-data-asset.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-attributes-data-asset
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-attributes-data-asset.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 7e079c20-21fd-5627-19f5-e858467a6a34
---

# Data asset attributes in Microsoft Purview Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Data asset attributes are a type of [custom metadata](unified-catalog-custom-metadata) in Microsoft Purview Unified Catalog that you can create and apply to your organization's data assets. These user-defined attributes provide a business or organization level context to an asset, helping data consumers understand the role an asset plays in the organization.

## Prerequisites

To create a **data asset attribute**, you must hold the [Data Curator role in the Data Map](data-map-collections-manage-classic#roles).

## Manage attributes on the Custom metadata (preview) page

Note

Data asset attributes were previously called "managed attributes" and were located under **Catalog management** &gt; **Classic types**.

The **Custom metadata (preview)** area under **Unified Catalog** &gt; **Catalog management** is where you create and manage two types of attributes:

1. Data asset attributes
2. Business concept attributes

The **Data asset attributes** tab is where you find all of your data asset attributes nested within each attribute group.

The **Business concept attributes** tab lists all of your attributes nested within each attribute group. Learn [how to work with business concept attributes](unified-catalog-attributes-business-concept).

## Know before you start

Before you start creating attributes, review these sections:

- Understand attributes and groups
- Attribute field types
- Learn when you can mark an attribute as required

### Understand attributes and groups

- **Data asset attributes:** A set of user-defined attributes that provide a business or organization level context to a data asset. Each attribute has a name and a value. For example, "Department" is an attribute name and "Finance" is its value.
- **Attribute group:** A grouping of data asset attributes that makes it easier to organize and consume them.

### Attribute field types

Data asset attributes can include several types of values, such as text-based descriptions, numerical identifiers, or date-based identifiers.

During the attribute creation process, you can choose from the following field type options:

- Text
- Single choice: When you select this type, a **Choices** field appears, where you enter a name for the choice and can add more choices.
- Multiple choice: When you select this type, a **Choices** field appears, where you enter a name for the choice and can add more choices.
- Date
- Boolean
- Byte
- Double
- Float
- Integer
- Long
- Short

## Create and edit attribute groups

You must connect all data asset attributes to an attribute group. You might want to develop a grouping strategy ahead of time, then create one or more attribute groups before creating the attributes you assign to the groups. Alternatively, you can create an attribute group at the point in the attribute creation process where you assign a group to the attribute.

As you develop a grouping strategy, consider which attributes in a group you want to mark as required. **You can only set attributes to be required when you create an attribute group first, and then add assets *while you're in the process of creating the group*.**

### Create an attribute group

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Unified Catalog**.
2. Under **Catalog management**, select **Custom metadata**.
3. On the **Data asset attributes** tab, select **New**, then select **New attribute group**.
4. On the **New attribute group** flyout pane, enter an **Attribute group name** and an optional description. You can't change a group name after you create the group.
5. You can create a new data asset attribute at this stage by selecting **New attribute**. This is the **only** stage at which you can mark an attribute as required.
6. When done, select **Create**.

The group is now listed on the **Data asset attributes** tab of the **Custom metadata (preview)** page.

### View and edit an attribute group

Find the name of an attribute group on the **Data asset attributes** tab, hover over its row, and select the **Edit** pencil icon. A flyout pane appears, which contains all the details of the attribute group, including a list of all attributes in the group.

Add a new attribute to the group by selecting **New attribute**.

You can't edit an attribute group name after you create the group.

## Mark an attribute as required

When you create a data asset attribute as part of a data asset attribute group, you can make it required by selecting **Mark as required**. Marking an attribute as required means that a value must be provided for this attribute. When you edit a data asset, you must fill out the required attribute before you can close the editor.

Important

- You can only select **Mark as required** when you create an attribute during the process of creating an attribute group. You can't mark the attribute as required when creating just an attribute on its own.
- If an existing attribute isn't marked as required, you can't mark it as required during the editing process.
- Once you select **Mark as required** and create the attribute, you can't unselect it during the editing process.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Unified Catalog**.
2. Under **Catalog management**, select **Custom metadata**.
3. On the **Data asset attributes** tab, select **New**, then select **New attribute group**.
4. Select **New** and select **New attribute**.
5. Fill out your attribute details, and select **Mark as required**.
6. Select **Apply** and finish adding other attributes to complete your attribute group.

## Create data asset attributes

1. In the [Microsoft Purview portal](purview-portal), under **Solutions**, select **Unified Catalog**.
2. Under **Catalog management**, select **Custom metadata**, then select the **Data asset attributes** tab.
3. Select **New**, then select **New attribute**.
4. On the **New attribute** flyout pane, enter an **Attribute name** and an optional description.

    Note

    You can create more than one attribute with the same name and link them to different attribute groups. Providing a detailed description for identically named attributes can help avoid confusion or the misapplication of attributes.
5. Select **Mark as required** if you want to require a value for the attribute. This option is only available when creating an attribute during the process of creating an attribute group (learn more).
6. At **Attribute group**, select a group name from the dropdown list.

    - You can create a new attribute group at this step by selecting **New**, then follow the steps to create an attribute group.
    - If you're creating the attribute at the same time as you're creating the group, the **Attribute group** selector doesn't show; the attribute is automatically associated to the group you're creating.
7. At **Field type**, select an attribute field type.
8. At **Applicable asset types**, select one or more data asset types that the attribute can be applied to. For example, if you select "Azure SQL Table" for an attribute, it applies to Azure SQL Table assets, but not Azure Synapse Analytics Dedicated Table assets. When done, select **Apply**.
9. Select **Create**.

These attributes are automatically applied to the specified resources without a value. You need to apply a value for each asset.

## Edit a data asset attribute

After you create a data asset attribute, you can't change its name, the attribute group it belongs to, or the field type. To edit other details, such as the description or to mark the attribute as expired, follow these steps:

- On the **Data asset attributes** tab of the **Custom metadata (preview)** page, hover over the attribute name and select the **Edit** pencil icon.
- Make your edits, then select **Update**.

## Add a value to a data asset attribute

After you create a data asset attribute, you need to add a value for each of your assets. To add values to your assets, follow these steps:

1. [Search for your data asset](unified-catalog-data-assets-search).
2. On the **Overview** tab of the asset's details page, see the **Data asset attributes** section with all attributes that have values. (You can see attributes without values by using the **Show attributes without a value** toggle.)
3. Select **Edit**.
4. Under **Data asset attributes**, add values for each of your attributes.
5. If any attributes are **Required**, you can't save until you add a value for that attribute.

## Expire a data asset attribute or attribute group

You can't delete a data asset attribute or a data asset attribute group. You can only expire them. When you expire an attribute or attribute group, you can't apply them to other data assets, and you can't reactivate them.

- **When you expire an attribute**: Any data assets that had the attribute applied continue to show that attribute.
- **When you expire an attribute group**: All the attributes within the group are also expired. Any data assets that had an attribute within this group applied to it continue to show that attribute.

To expire an attribute or attribute group:

1. On the **Data assets attributes** tab of the **Custom metadata (preview)** page, find the attribute or attribute group you want to expire and select the **Edit** pencil icon.
2. On the **Edit attribute** or **Edit attribute group** pane, select the **Mark as expired** checkbox.
3. Select **Update**.

## Create data asset attributes using APIs

You can programmatically create and apply data asset attributes by using the business metadata APIs in Apache Atlas 2.2. For more information, see the [Use Atlas 2.2 APIs](data-gov-api-atlas-2-2) tutorial.

## Best practices for using data asset attributes

Use data asset attributes to extend the fields available for an asset in the Microsoft Purview Unified Catalog. Data asset attributes are key-value pairs that add structured metadata to your catalog. When Microsoft Purview scans data, it adds technical information about the data, such as data type and classification. If you want to add more fields, you need to define data asset attributes.

For example, a data asset attribute lets a user tag tables with the department that publishes them. Use data asset attributes when you want to make sure assets are always tagged in exactly the same way with this information. The user also wants to filter by the publisher field when they search for data.

The data asset attribute in this example helps users quickly find all data published by a team, but it doesn't help someone understand the definition of a publisher or what it means if the team is the publisher of the data. For any information that needs a business explanation, use [glossary terms](unified-catalog-glossary-terms).