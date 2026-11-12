---
layout: Conceptual
title: Create and Manage Data Products in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-products-create-manage
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
description: Learn how to create and manage data products and manage data assets in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 353cd96e-f133-9240-41d5-a5008d935a60
document_version_independent_id: 353cd96e-f133-9240-41d5-a5008d935a60
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-products-create-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-products-create-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-products-create-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: a1e17e9d-324d-7d0c-49b8-8f4f4a859727
---

# Create and Manage Data Products in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

A [data product](unified-catalog-data-products) in Microsoft Purview Unified Catalog is a set of information with a defined use case that you share with other users. For example, a data product can be a sales report, an ML model, or a data model and its associated tables. A data product is a logical grouping of related physical assets that you create for a specific purpose.

It can be hard to find the value of data presented by itself, but data already associated with a purpose is easier to find and use. Data products in Unified Catalog provide practical context for your users and for intelligence systems, to help users identify what data is useful to them.

To create data products for your organization and ensure those products have enough definition to be useful to your user base, follow these instructions.

## Prerequisites

- To view data products, users need [catalog reader permissions](data-governance-roles-permissions).
- To manage or edit data products, users need [data product owner](data-governance-roles-permissions) permissions.

## View data products

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), open **Unified Catalog**.
2. Under **Catalog management**, select **Data product**. You see a list of all the data products you have access to based on your permissions. You can scroll, sort, filter, and search through these data products to find the ones you're looking for.
3. Select a **Data product name** from the list to view more details on the data project's details page.

### Filter your view by custom attribute

You can use [business concept attributes](unified-catalog-attributes-business-concept) as a filter when exploring data products.

1. Under **Catalog management**, select **Data products**.
2. Select **Add filter**.
3. At **Filter**, select an attribute name from the dropdown list.
4. At **Operator**, select a condition, such as **Equals** or **Starts with**, which varies based on the kinds of values allowed by the attribute.
5. At **Value**, enter your value.
6. Select **Apply**.

### Details

The **Details** tab on the data product detail page provides a description and use cases. Here you find the governance domain, update frequency, status, owner, subscribers, terms of use, aggregate [data quality](unified-catalog-data-quality) score, [health actions](unified-catalog-data-health-management-actions-page), and documentation.

1. You see a list of all the data products you have access to based on your permissions.
2. You can scroll, sort, filter, and search through these data products to find the ones you're looking for.
3. For more details about a specific data product, select that data product.
4. On the data product's detail page, you can view the governance domain, update frequency, status, owner, subscribers, terms of use, aggregate [data quality](unified-catalog-data-quality) score, [health actions](unified-catalog-data-quality-actions), and documentation.

### Custom attributes

Under **Custom attributes**, you can see any [custom attribute groups and attributes](unified-catalog-attributes-business-concept) within groups, and the values set for each attribute. Only attributes with values are shown by default, but you can toggle **Show attributes without a value** on to view all attributes.

### Data observability

The **Data observability** (preview) tab provides a more detailed view into data health and lineage. This view requires a [brief setup process](unified-catalog-observability-setup). Get details about the [observability view for governance domains](unified-catalog-observability-views#data-product-data-observability).

## Create data products

Note

To create, edit, and manage data products, users need the [Data Product Owner role](data-governance-roles-permissions). You can only create data products in governance domains where you have data product owner access.

There are two ways you can create data products:

1. Individually, by creating one term at a time.
2. In bulk, by importing a formatted CSV file (preview).

### Create a single data product

1. In Unified Catalog, select **Catalog management**, select **Data products**, and then select **New data product**.
2. On **Basic details**, enter a **Name** and **Description**. If you use a name that already exists, you'll see a warning during the creation process. While duplicating names isn't recommended, you won't be blocked from using a duplicate name. The description should be a business narrative about the data, where it came from, and why you captured it. The goal is for a new user to understand the basics of when, what, why, and how the data came into existence. Provide clarity about the meaning of the specific data to the business. The description is limited to 10,000 characters.
3. Select a **Type** from the dropdown menu. Get details about data product types.
4. Make an optional selection from the **Audience** dropdown list.
5. Enter the **Owner** and any other owners for the data product.
6. Select **Next**.
7. On **Business details**, select the [governance domain](unified-catalog-governance-domains) your data product should be associated with.
8. Enter a **Use case**. The use case describes what the data is used for today and how a user can effectively apply it to their own scenario. Add information about what filters or dimensions are available, which asset contains the view that's easiest to parse, or any other details that can accelerate the usage of the data. If the data is only appropriate for specific purposes, include these details so users don't request access for data that they won't be approved for or won't help them to achieve their goals.
9. If you decide to mark the data product as **Endorsed**, select the **Mark as Endorsed** box. Learn more about endorsing a data product.
10. Select **Next**.
11. On the **Custom attributes** page, you can set values for all [custom attributes](unified-catalog-attributes-business-concept) defined by your admin in the **Custom attributes** section of the catalog. If the attribute is marked as required, you need to fill out all values on this page before you can complete the process.
12. Select **Create**.

You arrive at the new data product's details page. This is where you can make other edits to the data product, which is currently in a **draft** state.

Important

Other users can't see the data product yet. To make it visible to other users, you need to add data assets, [create an access policy](unified-catalog-data-product-access-policies), and then publish the data product.

### Bulk import data products (preview)

You can create many data products at once and import them into a governance domain by uploading a formatted CSV file. During the bulk import process, you download a sample CSV file containing a header row. You fill out the file according to the instructions in this article, and then reupload it. The data products appear in the governance domain in a draft state.

You can't use the bulk import process to edit or update data products.

Note

- You must download the sample CSV (.csv) file and reupload it according to the following instructions. The file must have at least one row of data, not including the header row.
- The CSV file can only include 1,000 rows. More rows cause an upload error. If you need to import more data products, fill out and upload a separate CSV file.
- Special characters are allowed in all fields.
- Each data product name must be unique. Duplicate names aren't supported for import.

To import data products in bulk to a governance domain, follow these steps:

1. In Unified Catalog, select **Catalog management**, then select **Governance domains**.
2. Select the name of the governance domain where you want to add data products.
3. On the **Details** tab of the governance domain's details page, find the **Data products** card and select **View all**.
4. On the **Data products** page, select **Import**.
5. On the **Import** flyout pane, select **Download a sample CSV file**.
6. Open the downloaded file. Fill out the worksheet as described in this article to avoid upload errors.

    - **Column A - name** (required): Enter the data product name. Every name must be unique; you can't have multiple rows with the same name. Maximum length is 256 characters.
    - **Column B - owners** (required): Enter a valid email address that belongs to the same tenant that you're importing from. You can add multiple email addresses separated by a semicolon. For example: `owner1@contoso.com;owner2@econtoso.com`. Groups without email aren't supported.
    - **Column C - type** (required): Enter a data product type; see list of types.
    - **Column D - audience**: Enter one of these allowed values to describe the intended audience for the data product:

        - BI engineer
        - Business analyst
        - Business user
        - Data analyst
        - Data engineer
        - Data scientist
        - Executive
        - Software engineer
    - **Column E - endorsed**: Enter **True** or **False**. Endorsed is a signal of confidence to data consumers that the data product meets the organization’s quality and governance expectations. It shows as a label on the data product for data consumers.
    - **Column F - description** (required): Enter a description for the data product. Maximum length is 500,000 characters.
    - **Column G - business use** (required): This entry shows in the **Use case** area of the data product. Enter a description of what the data is used for today and how a user can effectively apply it to their own scenario.
    - **Column H and onward**: These columns are for [custom attributes](unified-catalog-attributes-business-concept), which differ by governance domain based on how they're defined and scoped. Note these formatting requirements for specific entry types:

        - **Multiselect options**: Enter the objects inside square brackets and in quotes. For example, `["a"]`, or `["a", "b"]`.
        - **Single select options**: Enter the raw value. For example, `a1`, `b2`.
        - **Booleans**: Enter `true` or `false`. You can use upper or lowercase.
        - **String or rich text**: Use regular text; don't add quotes unless you want quotes reflected in the attribute.
        - **Numeric - short, int, long, double, float, bit, byte**: Don't add quotes. Just enter the number.
7. After formatting your CSV file, save it locally. Return to the **Import** flyout pane, select **Browse**, and then find and select your CSV file to upload it.
8. On the **Import** flyout pane, select **OK** to start the import process.

If there's a problem with the CSV file, an error message appears on the **Import** pane explaining the error so you can fix the CSV file and reupload it.

If there are no problems with the file, the import process begins. Depending on the size of the CSV file, it might take some time to complete the import process. If the file is small, the import happens immediately and you see a success message. Larger files take longer for the import process to complete.

Check the status by returning to the governance domain details page. On the **Details** tab, select **Monitoring** to view the status of your bulk import jobs, including any errors, on the **Monitoring** page.

## Data product types

When you create a data product, you can optionally identify it as one of the following types. These types help identify the kinds of users that might want to use the data product, and you can use them to filter data products in a search.

- **Analytics model**: Data that's transformed from raw data to help build analytics from, and might be distinct fact and dimension tables.
- **Business system/Application**: A common set of consumable tables from a specific source, or available in a certain application that you consume together.
- **Dashboards/Reports**: Data visualizations that you use to make decisions and view common metrics. They might or might not include the data used to power the visualization.
- **Dataset**: An individual asset or group of assets used as a common data product type to make data discoverable for specific use cases.
- **Master and reference data**: Highly reusable data that you should consistently reference and highly control due to its common use and greater importance to the health of the data estate.
- **ML training data**: Data approved for use as training a new model. It's typically not production data and is desensitized to prevent potential risks.
- **ML testing data**: Data built to specifically test ML models for edge cases, fairness, and potential harms.
- **Model types**: Typically used for AI models and analytical or semantic models used with AI.
- **Operational**: A data product that you use for data quality, or to operate a portion of the data estate but not planned for high consumption or governance. It could be an investigatory data product of transitory data assets or data used to run a process, but isn't modeled or consolidated for analytical purposes.
- **Semantic model**: A group of related data tables and their relationships and meanings for interpretation and reuse.
- **Transactional data**: Data from an originating source that might have limited use cases, but is required for engineering scenarios or system-to-system integrations. It's not typically used for most business data consumption, but it could be important for governance and control scenarios.

## Managing data products

Data product owners can view and modify the properties of a data product by following these steps:

1. In Unified Catalog, select **Catalog management**, and then select **Data products**.
2. Select the data product to open its details page.
3. Select **Edit**.

From the data product page, you can:

- Edit details about the data product.
- Update frequency.
- Change the data product's status.
- Manage data product access policies.
- Add or remove associated data assets.
- Remove data assets that are deleted from Data Map (preview).
- Manage associated terms or OKRs.
- Manage terms of use.
- Manage associated documentation.
- Endorse a data product.
- [Edit values for custom attributes](unified-catalog-attributes-business-concept).

## Edit data product

To edit a data product, you need [data product owner](data-governance-roles-permissions) permissions. You can only edit a data product when it's in **Draft** status.

1. On your data product page, select the **Edit** button.
2. On the **Basic details** page, update the name, description, type, and owners. If you change the name to one that already exists, you'll see a warning about the duplication but you can proceed to use the duplicate name.
3. Select **Save**.
4. On the **Business details** page, update use cases and endorsement status.
5. Select **Save**.
6. On the **Custom attributes** page, you can set values for all [custom attributes](unified-catalog-attributes-business-concept) defined by your admin in the **Custom attributes** section of the catalog. If the attribute is marked as required, you need to fill out all values on this page before you can complete the process.
7. To save your changes, select **Save**.

### Update contacts

When you add owners to data products during the creation or editing process, the owners automatically appear in the **Contacts** section. You can customize the label by selecting the pencil icon in each contact card.

### Update frequency

Use the update frequency to show how regularly you manage a data product. This indicator isn't currently automated.

1. To edit the update frequency, select the **Update frequency** attribute on the right side of the page.
2. Select the update frequency you expect for your data product.
3. Select **Done**.

## Publish, draft, and expire

To publish a drafted data product, select **Publish** on the data product's details page. Before you can publish, you need to add data assets to your data product and [set up a data access policy](unified-catalog-data-product-access-policies) so users can request access to your data product.

Note

Ensure your [governance domain is published](unified-catalog-governance-domains-create-manage#manage-governance-domains) before you publish your data products.

After completing the requirements, you can publish your data product, which makes the data product available for users in Unified Catalog.

You can also set a previously published data product to a draft by **unpublishing** it:

1. Select the **Unpublish** button in the data product.
2. Select **Set to draft** which allows only stewards, governance domain owners, and data product owners to view and manage it.

You can also set your data product to **Expired**:

1. Select the **Unpublish** button in the data product.
2. Select **Set to expired** which makes it visible only to stewards, governance domain owners, and data product owners.

## Manage data product access policies

To manage access policies, you need [data product owner or data steward](data-governance-roles-permissions) permissions.

1. If your data product is published, first unpublish it to manage policies.
2. On your data product page, select **Manage policies**.
3. From the policy configuration window, you can create and manage your data product's access policy. Learn how to [set up data product access policies](unified-catalog-data-product-access-policies#set-up-data-product-access-policies).

## Add and remove data assets

A data product groups together data assets. Grouping assets in this way makes it easier to discover them. To add or remove data assets from a data product, see the following sections.

### Add data assets

Note

When you add data assets, the search only shows assets that the [governance domain is scoped for](unified-catalog-governance-domains-create-manage#data-estate-mappings), or that the [user has access to in Microsoft Purview Data Map](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

To add data assets to a data product:

1. In Unified Catalog, select **Catalog management**, and then select **Data products**.
2. Select the data product you want to add assets to.
3. Select **Add data assets** under the description and use cases.
4. Search for your data assets by using keywords or filters. To add filters, select **Add filter**.
5. Select any assets you want to add to the data product.
6. Select **Selected assets** to edit your selected asset list.
7. When you're done selecting assets, select **Add**.

You see your newly added assets in your data product.

### Remove data assets

Tip

Collaborate with your data quality team to perform necessary cleanup work, as described in the following section, before removing data assets and deleting data products.

Before you can remove a data asset from a data product, you must remove all data quality rules and previous data quality scans from the asset. For more information, see [deleting data quality history](unified-catalog-data-quality-scan#delete-previous-data-quality-scans-and-history).

Although data quality stewards might not be involved in creating data products, they're the subject matter experts in data quality rules and scans. Only users holding the Data Quality Steward role can remove data quality rules and scans, so data product owners should work with data quality stewards to get rules and scans removed before the asset in question can be removed from the data product.

Follow these steps to remove a data asset:

1. In Unified Catalog, select **Catalog management**, and then select **Data products**.
2. Select the data product you want to remove assets from.
3. If the assets you want to remove are on the front page, select the ellipsis (...) on the data asset's card, and then select **Remove**.
4. If you don't see the assets on the main product page, select **View all data assets**. There you can search and filter the assets. To remove them, select their ellipsis button and select **Remove**.

    Note

    The remove action is unavailable if the data asset has data quality rules running on it or failed data quality run history. You need the Data Quality Steward role to resolve these issues before the asset can be removed.

## Remove assets that are deleted from Data Map and metadata sync from Data Map (preview)

If you delete a data asset in a data product in Data Map, a banner appears in the data product to inform you of the asset deletion. However, the asset still appears in the data product until you remove it.

Open the data product and select **View all data assets** to view the list of assets. Assets with a caution symbol on its row are deleted from Data Map. To remove the deleted asset from your data product, select ellipsis (...) in the row, and then select **Remove**.

When you open the asset detail page from assets in a data product, the metadata is retrieved from the Data map. Metadata changes in Data Map are now reflected in Unified Catalog after they're updated in Data Map or initiated by selecting the refresh button.

For metadata represented within parent assets, such as columns within tables and views, the changes may not appear immediately. However, in all cases, metadata changes are reflected in Unified Catalog within 24 hours.

## Manage linked resources

Link [glossary terms](unified-catalog-glossary-terms) and [OKRs](unified-catalog-okrs) directly to your data products to improve understanding, apply policies, and associate your data products with your business goals.

When you map assets in your data product to critical data elements, the system automatically adds [critical data elements](unified-catalog-critical-data-elements).

### Add linked resources

1. On the data products page, select the data product you want to add terms or OKRs to.
2. Under **Glossary terms** or **OKRs**, select the **+** button next to the listing of those items.
3. Search for your terms or OKRs by using keywords, governance domain, or filters by selecting **Filter**.
4. Select any terms or OKRs you want to add to the data product.
5. Select the **Add** button.
6. You can now see the term or OKR in the list for your data products.

### Remove linked resources

1. On the data products page, select the data product you want to remove terms or OKRs from.
2. Under **Glossary terms** or **OKRs**, find the item you want to remove, and select its ellipsis button.
3. Select **Remove**.

Note

The system automatically adds critical data elements based on the assets in your data product. For more information, see [managing critical data elements](unified-catalog-critical-data-elements).

## Terms of use

1. On the data products page, select the data product you want to manage terms of use for.
2. Select the **Terms of use** attribute, on the right side of the page.
3. To add more terms of use:
    1. Select **+ Add link**.
    2. Choose a particular data asset to link the use to (optional).
    3. Enter a friendly name for the terms.
    4. Enter the link to the terms of use.
    5. Select **Create**.
    6. Select **Done**.
4. To remove any terms of use:
    1. Hover over the term you want to remove.
    2. Select the trashcan **remove** button.
5. When you're finished, select **Done**.

## Documentation

1. On the data products page, select the data product you want to manage documentation for.
2. Select the **Documentation** attribute on the right side of the page.
3. To add documentation:
    1. Select **Add link**.
    2. Choose a particular data asset to link the documentation to (optional).
    3. Enter a friendly name for the documentation.
    4. Enter the link to the documentation.
    5. Select **Create**.
    6. Select **Done**.
4. To remove documentation:
    1. Hover over the documentation you want to remove.
    2. Select the trashcan **Remove** button.
5. When you're finished, select **Done**.

## Endorse a data product

As a Unified Catalog grows in size, it's important for data consumers to understand what data they can trust. Data consumers need to know if a data product meets their organization's quality standards and can be regarded as reliable.

Data product owners can now set the **Endorsed** flag for their data products to indicate that they certified their data products, and build confidence in the quality of their data product.

To endorse a data product, you need [data product owner](data-governance-roles-permissions) permissions.

1. On your data product page, select **Edit**.
2. Select **Details**.
3. Select the **Mark as 'Endorsed'** checkbox.
4. Select **Save**.

## Delete data products

Plan carefully before deleting a data product, as the process requires several steps.

1. First, unpublish the data product.

    1. Also, remove links to all related business concepts and remove any data assets within the data product.
    2. If any assets have data quality rules running on them or failed data quality run history, [delete the data quality history](unified-catalog-data-quality-scan#delete-previous-data-quality-scans-and-history).
2. Then, inform subscribers of the data product about the upcoming deletion and [delete their access request to the data product](unified-catalog-data-product-access-policies#delete-access-requests).
3. When you complete all tasks, select **Delete** on the data product's page to delete the data product.