---
layout: Conceptual
title: Create and manage business concept attributes (preview) in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-attributes-business-concept
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
description: Learn how to create and manage custom attributes for business concepts in Microsoft Purview Unified Catalog.
locale: en-us
document_id: d7288a2f-dff1-e478-53f5-32ce7c903532
document_version_independent_id: d7288a2f-dff1-e478-53f5-32ce7c903532
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-attributes-business-concept.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-attributes-business-concept
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-attributes-business-concept.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b7f0f64c-286e-1ec9-dd93-68ba65df7470
---

# Create and manage business concept attributes (preview) in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Business concept attributes are a type of user-defined [custom metadata](unified-catalog-custom-metadata) in Microsoft Purview Unified Catalog. You can create and apply these attributes to your organization's [business concepts](data-governance-get-started#business-concepts) for better organization, governance, and discovery.

You create and manage business concept attributes in the **Custom metadata (preview)** area of **Unified Catalog** &gt; **Catalog management**.

## Workflow and tasks by role

Creating and managing business concept attributes involves three basic steps. Each step involves certain user roles and functions in your organization:

1. Admins create and maintain the attributes and attribute group definitions.
2. Data stewards and data product owners update the values for business concept attributes defined by their admins.
3. Data consumers or catalog readers use business concept attributes to filter their view of published business concepts.

Use this table to guide you to relevant tasks depending on your role in the organization. See [Data governance roles and permissions](data-governance-roles-permissions) for role descriptions and how to assign roles.

| Role | Task |
| --- | --- |
| Admins - Governance Domain Creators and Data Curators | Create attribute groupsCreate attributesSet the scope for an attribute groupEdit groups to add attributesRequire values for attributesExpire attributes and attribute groups |
| Data StewardsData Product Owners | Edit attributesAdd values to attributesUse attributes as filters for viewing business conceptsDelete attribute values |
| Catalog readers (local and global) | Use attributes as filters for viewing business concepts |

## Know before you start

Before you start creating attributes, review these sections:

- Understand attributes and groups
- Field types for attribute values
- Scope settings for attribute groups

Note

As you start planning your attribute strategy, keep in mind that after you create a business concept attribute, you can only make limited edits. Also, you can't delete attributes and attribute groups; you can only expire them.

### Understand attributes and groups

- **Business concept attributes**: [Business concepts](data-governance-get-started#business-concepts), such as governance domains and glossary terms, help you organize and understand your data in ways that make sense for your organization. You define an attribute as metadata that you apply to your business concepts to better describe your organization's unique needs.
- **Attribute groups**: A category by which you group attributes, so you can organize and consume them more easily.

### Field types for attribute values

Business concept attributes can include several types of values, such as text-based descriptions, numerical identifiers, or date-based identifiers. During the attribute creation process, you can choose from the following field type options:

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
- Rich text
- Short

For more information, see Add values to attributes.

### Scope setting for attribute groups

The **Scope** setting for attribute groups lets you apply attributes to a broad array of governance domains and business concepts in Unified Catalog.

When you create an attribute group, the **Scope** settings let you select all or some [governance domains](unified-catalog-governance-domains), [business concepts](unified-catalog-plan#know-your-data-with-business-concepts), and [data product types](unified-catalog-data-products-create-manage#data-product-types). Setting a scope means that every attribute in that group applies to the governance domains, business concepts, and data products that you select for that group.

Scope defaults to all governance domains and business concepts during the attribute group creation process. If you need to narrow the scope, select each dropdown within **Scope** and set it to the desired scope.

When creating or editing an attribute, you can accept the **Inherit Group Scope** setting, which applies the group scope to the attribute, or you can override the inherited setting and select individual governance domains and business concepts as the scope for that particular attribute within the group.

## Create and edit attribute groups

You must connect all business concept attributes to an attribute group. You might want to develop a grouping strategy ahead of time, then create one or more attribute groups before creating the attributes you'll assign to the groups. Alternatively, you can create an attribute group at the point in the attribute creation process where you assign a group to the attribute.

Note

When you apply an attribute group to a business concept, you add all attributes in that group to the business concept.

### Create an attribute group

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Unified Catalog** with an account that has a role in a [tenant level role group](data-governance-roles-permissions#tenant-level-role-groups).
2. Under **Catalog management**, select **Custom metadata**.
3. On the **Business concept attributes** tab, select **New**, then select **New attribute group**.
4. On the **New attribute group** flyout pane, enter an **Attribute group name** and an optional description.
5. Select **New attribute** to create a new business concept attribute at this stage. This is the **only** stage at which you can mark an attribute as required.
6. Under **Scope**, select the **Governance Domains**, **Business Concepts**, and **Data product types** that apply to the group and all attributes assigned to the group. All values are checked by default, so be sure to uncheck any values you don't want. Get more details on scope settings.
7. When done, select **Create**.

The group now appears on the **Business concept attributes** tab of the **Custom metadata (preview)** page.

### View and edit an attribute group

Find the name of an attribute group on the **Business concept attributes** tab, hover over its row, and select the **Edit** pencil icon. A flyout pane appears, which contains all the details of the attribute group, including a list of all attributes in the group.

Add a new attribute to the group by selecting **New attribute**.

To change the scope of an attribute in the group or edit any details of the attribute, select the attribute name, make edits on the **Edit attribute** flyout pane, then select **Apply**.

## Mark an attribute as required

When you create a business concept attribute as part of a business concept attribute group, you can make the attribute required by selecting **Mark as required**. Marking as required means that a value must be provided for the attribute. When a business concept is created or edited, the value for the required attribute must be filled out before you can complete the creation or editing process.

Important

- You can only select **Mark as required** when you create an attribute during the process of creating an attribute group. You can't mark the attribute as required when creating just an attribute on its own.
- If an existing attribute isn't marked as required, you can't mark it as required during the editing process.
- Once you select **Mark as required** and create the attribute, you can't unselect it during the editing process.

## Create attributes

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Unified Catalog** with an account that has the [Data Steward role](data-governance-roles-permissions#unified-catalog-roles).
2. Under **Catalog management**, select **Custom metadata**.
3. On the **Business concept attributes** tab, select **New**, then select **New attribute**.

    ![Custom metadata create business concept attribute.](media/unified-catalog-metadata-create.png)
4. On the **New attribute** pane, enter an **Attribute name** and an optional description.

    Note

    You can create more than one attribute with the same name and link them to different attribute groups. Providing a detailed description for identically named attributes can help avoid confusion or the misapplication of attributes.
5. Select **Mark as required** if you want to require a value for the attribute. This option is only available when creating an attribute during the process of creating an attribute group (learn more).
6. At **Attribute group**, select a group name from the dropdown list.

    - You can create a new attribute group at this step by selecting **New**, then follow the steps to create an attribute group.
    - If you're creating the attribute at the same time as you're creating the group, the **Attribute group** selector doesn't show; the attribute is automatically associated to the group you're creating.
7. At **Field type**, select an attribute field type.
8. The **Inherit Group Scope** toggle is on by default, which means that the attribute has the same scope as the group to which you assign it.

    To override scope inheritance, toggle off the switch. Then select the individual governance domains, business concepts, and data product types that you want the attribute to apply to. Get details on scope settings. ![Custom metadata attribute scope setting.](media/unified-catalog-metadata-scope.png)
9. When done, select **Create**.

Your attribute now appears on the list of attributes on the **Business concept attributes** tab, nested under its group.

## Edit attributes

An admin can edit attribute groups and attributes. You can update the description, the scope, or set an attribute or group as expired. When you edit an attribute group, you can add attributes to it.

To make edits, follow these steps:

1. Find the attribute or group from the list on the **Custom metadata** page.
2. Hover over the name and select the **Edit** pencil icon.
3. Make your edits, then select **Update**.

## Add values to attributes

Data stewards and data product owners can set and update values for attributes that admins define. You don't need to fill in the values when you create the business concept. However, if an attribute is marked as required, then whenever a user creates or edits an attribute, they must fill in the values before they can complete the attribute editing process.

## Delete attribute values

Attributes that are expired display a trash can icon next to them when you view them on a business concept's **Custom attributes** page. To delete an attribute value:

- Open the business concept details page and select **Edit**.
- On the **Custom attributes** page, find the attribute you want to delete (expired attributes appear as grayed out).
- Select the trash can icon next to the attribute. The attribute is removed from the view.
- Select **Save**.

## Expire an attribute or attribute group

You can't delete a business concept attribute or a business concept attribute group. You can only expire them. When you expire an attribute or attribute group, you can't apply them to other business concepts, and you can't reactivate them.

- **When you expire an attribute**: Any business concepts that had the attribute applied continue to show that attribute.
- **When you expire an attribute group**: All the attributes within the group are also expired. Any business concepts that had an attribute within this group applied continue to show that attribute.

To expire an attribute or attribute group:

1. On the **Business concept attributes** tab of the **Custom metadata (preview)** page, find the attribute or attribute group you want to expire and select the **Edit** pencil icon.
2. On the **Edit attribute** or **Edit attribute group** pane, select the **Mark as expired** checkbox.
3. Select **Update**.

## View attributes and use as filters

You can view attributes and use them as filters in various ways:

- List view of all attributes on the Custom metadata (preview) page.
- Displayed on a business concept's details page
- As a filter when exploring business concepts.
- As a filter for exploring data products.

### On the Custom metadata (preview) page

The **Unified Catalog** &gt; **Catalog management** &gt; **Custom metadata** page lists business concept attributes on the **Business concept attributes** tab. The list is organized by group name. Use the arrow next to the group name to expand or collapse the list of attributes under a group.

### On a business concept details page

You can view details about attributes on the details pages for all business concepts and data products:

- [Governance domains](unified-catalog-governance-domains-create-manage#access-governance-domains)
- [Data products](unified-catalog-data-products-create-manage#view-data-products)
- [Critical data elements](unified-catalog-critical-data-elements#access-critical-data)
- [Glossary terms](unified-catalog-glossary-terms-create-manage#access-glossary-terms)
- [Objectives and key results (OKRs)](unified-catalog-okrs-create-manage#access-okrs)

### Filters for viewing business concepts

Use business concept attributes as filters when browsing and searching for business concepts.

1. Go to **Unified Catalog** &gt; **Discovery** &gt; **Enterprise glossary**.
2. Select the tab of the business concept you want to search in. If you're searching in a governance domain, select **View all** on a business concept card.
3. Select **Add filter**.
4. At **Filter**, select an attribute name from the dropdown list.
5. At **Operator**, select a condition, such as **Equals** or **Starts with**, which varies based on the kinds of values allowed by the attribute.
6. At **Value**, enter your value.
7. Select **Apply**.

### Filter for exploring data products

When you explore data products by governance domains, you can filter your view by data asset attributes.

1. In Unified Catalog, go to **Discovery** &gt; **Data products**.
2. Select **Explore all**. You arrive at the **Explore data products by governance domain** page.
3. Select **Add filter**.
4. At **Filter**, select an attribute name from the dropdown list.
5. At **Operator**, select a condition, such as **Equals** or **Starts with**, which varies based on the kinds of values allowed by the attribute.
6. At **Value**, enter your value.
7. Select **Apply**.