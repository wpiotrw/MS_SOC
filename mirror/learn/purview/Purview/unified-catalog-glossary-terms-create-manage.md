---
layout: Conceptual
title: Create and Manage Glossary Terms in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-glossary-terms-create-manage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-05-20T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to create and manage glossary terms in Microsoft Purview Unified Catalog.
locale: en-us
document_id: d383c877-ae67-bd1c-f2e5-daa915f4f8d4
document_version_independent_id: d383c877-ae67-bd1c-f2e5-daa915f4f8d4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-glossary-terms-create-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-glossary-terms-create-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-glossary-terms-create-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 1c74f45b-ad38-0b3b-2464-41f525e0744d
---

# Create and Manage Glossary Terms in Unified Catalog | Microsoft Learn

[Glossary terms](unified-catalog-glossary-terms) in Microsoft Purview Unified Catalog provide a vocabulary for business users. These terms allow users to discover and work with data in the vocabulary that is more familiar to them, rather than using abstract technical jargon inherited from data sources.

Use business terms to define a shared vocabulary for your organization. By creating terms, identifying their synonyms, acronyms, related terms, and more, you can create a flexible controlled taxonomy organized in a hierarchical way. Glossaries of terms help bridge the communication gap between various departments in your company by providing consistent definitions for concepts, metrics, and other important elements across the organization.

This article describes how to manage glossary terms in Microsoft Purview. It explains how to create a glossary term in a [governance domain](unified-catalog-governance-domains), and how to link glossary terms to data products, data assets, columns, and critical data elements.

## Prerequisites

- Any user can read published glossary terms.
- To create, edit, and manage glossary terms, you need the [Data Steward role](data-governance-roles-permissions#governance-domain-level-permissions) in the governance domain where the terms reside.
- To link glossary terms to data assets and columns, in addition to needing the Data Steward role, you also need the [Data Reader role](data-governance-roles-permissions#data-map-permissions) in the assets' collections.

## Access glossary terms

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), open **Unified Catalog**.
2. Under **Catalog management**, select **Governance domains**.
3. Select the governance domain you want to see glossary terms for.
4. On the **Glossary terms** card, select **View all**.

You see a list of all the glossary terms for that governance domain. You can search or sort through these glossary terms, filter them, or change the view between a list, a compact list, or a tree.

Note

There might be multiple pages of terms. Use the arrow buttons and the page selector to toggle between these pages.

You can also view a list of all glossary terms:

1. In Unified Catalog, under **Discovery**, select **Enterprise glossary**.
2. Select the **Glossary terms** tab.
3. Select the name of a glossary term to open its details page.

### Filter your view by custom attribute

You can use [business concept attributes](unified-catalog-attributes-business-concept) as a filter when exploring glossary terms.

1. In Unified Catalog, go to **Discovery** &gt; **Enterprise glossary**.
2. On the **Glossary terms** tab, select **Add filter**.
3. At **Filter**, select an attribute name from the dropdown list.
4. At **Operator**, select a condition, such as **Equals** or **Starts with**, which varies based on the kinds of values allowed by the attribute.
5. At **Value**, enter your value.
6. Select **Apply**.

### Glossary term details

Select a term from the list to view its details page. To create and manage access policies for the critical data element, select **Manage policies**.

### Overview

The **Overview** tab contains a description of the term.

### Custom attributes

Under **Custom attributes**, you can see any [custom attribute groups and attributes](unified-catalog-attributes-business-concept) within groups, and the values set for each attribute. Only attributes with values are shown by default, but you can toggle **Show attributes without a value** on to view all attributes.

### Related

The **Related** tab displays any related elements, such as acronyms, synonyms, and resources. It also shows you which data products, data assets, and columns the term is linked to.

### Observability

If you set up [data observability (preview)](unified-catalog-observability), the **Data observability** tab is where you see its visualizations.

## Create glossary terms

Note

To create and upload glossary terms, you need the [Data Steward role](data-governance-roles-permissions#governance-domain-level-permissions).

There are two ways you can create glossary terms:

1. Individually, by creating one term at a time.
2. In bulk, by importing a formatted CSV file (preview).

### Create a single glossary term

1. In Unified Catalog, select **Catalog management**, and then select **Governance domains**.
2. Select the name of the governance domain where you want to add a term.
3. On the **Details** tab for the domain, find the **Glossary terms** card and select **View all**.
4. Select **New term** to create a single new term.
5. On **Basic details**, enter a name and a definition for your term. If you use a name that already exists, you'll see a warning during the creation process. While duplicating names isn't recommended, you won't be blocked from using a duplicate name.. The description is limited to 10,000 characters.
6. Select an owner or several owners for the term.
7. For **Parent term**, select an existing term within the same domain as a parent term. Then select **Next**. 
    Note

    You can visualize parent and child relationships in a tree-like hierarchy within the terms list page by selecting **Tree** in the views drop-down.
8. On **Acronyms**, add any related acronyms or leave it blank, and then select **Next**.
9. On **Resources**, add any related resources, such as links to documentation or other sources that provide context for your term, or leave it blank. Then select **Next**.
10. On the **Custom attributes** page, you can set values for all [custom attributes](unified-catalog-attributes-business-concept) defined by your admin in the **Custom attributes** section of the catalog. If the attribute is marked as required, you need to fill out all values on this page before you can complete the process.
11. When done, select **Create**.

Your term is created in a draft state, where only stewards and domain owners can see it. To make it visible to all users, you need to publish the term.

You arrive at the details page for your new glossary term, where you can edit or manage your term, publish your term, or link the term to data products, data assets, columns, and critical data elements.

### Bulk import glossary terms (preview)

You can create many glossary terms at once and import them into a governance domain by uploading a formatted CSV file. During the bulk import process, you download a sample CSV file containing a header row. You fill out the file according to the instructions below, then reupload it. The terms then appear in the governance domain in a draft state.

The bulk import process can't be used to edit or update glossary terms.

Note

- You must download the sample CSV (.csv) file and reupload it according to the following instructions. The file must have at least one row of data, not including the header row.
- The CSV file can only include 1,000 rows; more rows cause an upload error. If you need to import more terms, fill out and upload a separate CSV file.
- Special characters are allowed in all fields.
- Each term name must be unique; duplicate names aren't supported for import.

Follow these steps to import glossary terms in bulk to a governance domain:

1. In Unified Catalog, select **Catalog management**, then select **Governance domains**.
2. Select the name of the governance domain you want to add glossary terms to.
3. On the **Details** tab of the governance domain's details page, find the **Glossary terms** card and select **View all**.
4. On the **Glossary terms** page, select **Import**.
5. On the **Import terms** flyout pane, select **Download a sample CSV file**.
6. Open the downloaded file. Fill out the worksheet as described below to avoid upload errors.

    - **Column A - name** (required): Enter the glossary term name. Every term name must be unique; there can't be multiple rows with the same name. Maximum length is 256 characters.
    - **Column B - description** (required): Enter a description for the term. Maximum length is 500,000 characters.
    - **Column C - owners** (required): Enter a valid email address that belongs to the same tenant that you're importing from. You can add multiple email addresses separated with a semicolon; for example: `owner1@contoso.com;owner2@econtoso.com`. Groups without email aren't supported.
    - **Column D - experts**: Enter the email address of one or more users who are considered experts of the term.
    - **Column E - acronyms**: Enter any common abbreviations or shortened versions of the term.
    - **Column F - resources**: Enter related resources, such as links to documentation or other sources that provide context for the term. Resource links must be a valid URL in this format: `https://www.contoso.com`; both `http://` and `https://` are acceptable. List multiple resources by following this example: `resourcename1|value1;resourcename2|value2`.
    - **Column G and onward**: These are [custom attributes](unified-catalog-attributes-business-concept), which differ by governance domain based on how they're defined and scoped. Note these formatting requirements for specific entry types:

        - **Multiselect options**: Enter the objects inside square brackets and in quotes; for example, `["a"]`, or `["a", "b"]`.
        - **Single select options**: Enter the raw value; for example, `a1`, `b2`.
        - **Booleans**: Enter `true` or `false`; can be upper or lowercase.
        - **String or rich text**: Use regular text; don't add quotes unless you want quotes reflected in the attribute.
        - **Numeric - short, int, long, double, float, bit, byte**: Don't add quotes, just enter the number.
7. After formatting your CSV file, save it locally. Return to the **Import terms** flyout pane, select **Browse**, then find and select your CSV file to upload it.
8. On the **Import terms** flyout pane, select **OK** to start the import process.

If there's a problem with the CSV file, an error message appears on the **Import terms** pane explaining the error so you can fix the CSV file and reupload it.

If there are no problems with the file, the import process begins. Depending on the size of the CSV file, it might take some time to complete the import process. If the file is small, the import happens immediately and you see a success message. Larger files take longer for the import process to complete.

Check the status by returning to the governance domain details page. On the **Details** tab, select **Monitoring** to view the status of your bulk import jobs, including any errors, on the **Monitoring** page.

## Publish terms

When your term is ready to use in your governance domain, publish it by following these steps:

1. Select the domain where your term resides.
2. On the **Glossary terms** card, select **View all**.
3. Search or browse for the glossary term and select it.
4. On the glossary term's details page, select **Publish**.

Note

Ensure your [governance domain is published](unified-catalog-governance-domains-create-manage#manage-governance-domains) before you publish your glossary terms.

## Manage term policies

To manage term policies, you need [data steward](data-governance-roles-permissions) permissions.

1. On your glossary term page, select **Manage policies**.
2. From the policy configuration window, create and manage your term policies. For more information, see [the documentation about managing access policies](unified-catalog-data-product-access-policies#set-up-data-product-access-policies).

## Link terms to data products, assets, and critical data elements (preview)

You can link glossary terms to data products, data assets, columns, and critical data elements to add business context to your data. Glossary terms must be in **Draft** state in order to add links; if the term is published, select **Unpublish** on the term's page to put it in **Draft** state.

Note

- When working with data assets and columns, *in addition to* needing the **Data Steward** role, you need the **Data Reader** role in the collection to which the asset or column belongs. All users with the **Catalog Reader** role can see published glossary terms associated to data assets and columns.
- You need to [enable asset curation](unified-catalog-glossary-terms-migrate) before you can attach terms to assets and columns.

1. Select the governance domain where the term you want to link resides.
2. On the **Glossary terms** card, select **View all**.
3. Search or browse for the glossary term and select it.
4. Select **Related**.
5. Depending on what you want to link it to, select any of the following options: **Add data product**, **Add data assets**, **Add column**, **Add critical data element**.
6. In the flyout pane, search for and select the items you want to link to, then select **Add**.

Tip

Your search results might span multiple pages. Check the page selector to view all pages.

You can view all your linked data products, data assets, and columns from within your glossary term. The **Related** tab lists the first 10 linked items of each type. Select **View all** to see and search the entire list.

To remove a link, select the element on the **Related** tab of the glossary term, then select **...**, then **Remove**.

## Remove assets that are deleted from Data Map and metadata sync from Data Map (preview)

If you delete a data asset in a term in Data Map, a banner appears in the term to inform you of the asset deletion. However, the asset still appears in the term until you remove it.

Open the term and select **Related** to view the list of assets. Assets with a caution symbol on its row are deleted from Data Map. To remove the deleted asset from your term, select ellipsis (...) in the row, and then select **Remove**.

When you open the asset detail page from assets in a term, the metadata is retrieved from the Data map. Metadata changes in Data map are now reflected in Unified Catalog after they're updated in Data map or initiated by selecting the refresh button.

For metadata represented within parent assets, such as columns within tables and views, the changes may not appear immediately. However, in all cases, metadata changes are reflected in Unified Catalog within 24 hours.

### Manage links to terms from data products and data assets

There are two other pathways through which you can manage links to glossary terms:

- [Within a data product](unified-catalog-data-products-create-manage#manage-linked-resources): Data Stewards can add or remove links to published and unpublished glossary terms from a data product's details page.
- [Within a data asset](unified-catalog-data-assets-search#link-glossary-terms-to-assets-and-columns-preview): Data Stewards can add or remove links to published and unpublished glossary terms residing in their governance domains. Users with the Global Asset Curator role can add published glossary terms to data assets.

## Manage related terms

Add related glossary terms from across all your governance domains to connect similar terms.

1. Select the governance domain where your term resides.
2. On the **Glossary terms** card, select **View all**.
3. Search or browse for the glossary term and select it.
4. On the glossary term's details page, select the **Related** tab.
5. To add a term, select **Add term** and choose whether to add the term as a synonym or a related term.

    Note

    You can link terms from different governance domains.
6. To remove a related term, select the **X** next to the term.

## Update contacts

When you add owners to glossary terms during the creation or editing process, you automatically add them to the **Contacts** section on the glossary term's details page. You can add experts to glossary terms as a contact type. To update contacts, edit the glossary term and at **Basic details**, enter a user name at **Owner** to add them as a contact.

## Edit glossary terms

1. Select the governance domain where you want to edit one of the terms.
2. On the **Glossary terms** card, select **View all**.
3. Search or browse for the glossary term and select it.
4. If the term is published, select **Unpublish**, and then select **Edit** to edit the name, definition, owners, or custom attributes. If you change the name to one that already exists, you'll see a warning about the duplication but you can proceed to use the duplicate name. When you're done, select **Save**.
5. To edit an owner's description, select the pencil icon on the card with the owner's name, edit the text, and then select the check mark to save.
6. To update status, select **...**, and then select the new desired status.
7. When done editing, publish the term.

### Bulk edit glossary terms (preview)

Use the bulk edit process to edit up to 50 glossary terms at one time. You can edit **Attributes**, such as owners and descriptions, and **Term relationships** by adding and removing synonyms and related terms. All glossary terms must be in **Draft** state for bulk editing.

1. Select the governance domain where you want to bulk edit terms.
2. On the **Glossary terms** card, select **View all**.
3. On the **Glossary terms** page, select **Bulk edit.**
4. Check the boxes next to the name of the **Draft** terms you want to edit, and then select **Edit items**.
5. On the **Editing terms** flyout pane, select **Select a new attribute**.
6. From the **Attribute**dropdown menu, select the attribute you want to edit:
    1. Description (required)
    2. Acronyms
    3. Owner (required)
    4. Expert
    5. Resources
    6. Parent term
7. For **Operation**, select one of these options:
    1. **Replace with**: Replace the value of the existing attribute.
    2. **Add**: Add a value to the attribute. This option isn't available for required attributes or for parent terms.
    3. **Remove**: Delete the attribute. This option isn't available for required attributes.
8. For **Replace with** and **Add** operations, enter a value at **New value**.
9. To edit more attributes, select **Select a new attribute**.
10. Expand **Term relationships**if you want to edit synonyms or related terms.
    1. Under **Synonyms** or **Related terms**, select **Select terms for operation**.
    2. Select **Add** or **Remove**.
    3. On the **Search and select** pane, check the box next to the synonyms and related terms you want to add or remove, and then select **Select**.
11. When you finish making edits, select **Save**.

Your changes are applied to all the terms you selected to edit.

Tip

You can also select **Publish** and **Unpublish** to publish draft glossary terms or unpublish published glossary terms in bulk.

## Move terms between governance domains (preview)

You can move multiple glossary terms at once from one governance domain to another domain. To move terms, you need to be a Data Steward in both the domain you're moving terms from, and in the domain you're moving the terms to. You can only move terms in a **Draft** state. If you select a parent term to move, the term's associated child terms move with it.

Use these steps to move glossary terms in bulk:

1. Select the governance domain that contains the terms you want to move out.
2. On the **Glossary terms** card, select **View all**.
3. On the **Glossary terms** page, select **Move to**.
4. Select the checkbox next to the **Draft** terms that you want to move, then select **Move items**.
5. In the **Move to** window, select the governance domain from the dropdown that you want to move the terms into.
6. Select **Move**.

The glossary terms appear in their new governance domain and are removed from their previous domain.

## Expire glossary terms

When you expire a glossary term, only Data Stewards and Governance Domain Owners can see it.

1. Select the governance domain where you want to remove or retire a term.
2. On the **Glossary terms** card, select **View all**.
3. Search or browse for the glossary term and select it.
4. Select **...**, and then select **Set to Expired**.
5. Select **Save**.

## Delete glossary terms

To delete a glossary term, first unpublish it and remove any links to related business concepts such as glossary terms, data products, data assets, columns, and critical data elements. Then select **Delete** to delete the term.

## Accessing the classic business glossary

You can still access the [classic business glossary](concept-business-glossary) by following these steps:

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), open **Unified Catalog**.
2. Select the **Catalog management** drop-down.
3. Select **Classic types**.
4. Select the **Glossaries** tab.