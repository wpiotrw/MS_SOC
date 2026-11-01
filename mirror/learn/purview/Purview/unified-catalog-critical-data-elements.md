---
layout: Conceptual
title: Critical Data Elements in Unified Catalog (Preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-critical-data-elements
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-04-20T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to create and manage critical data elements (preview) in governance domains in Microsoft Purview Unified Catalog.
locale: en-us
document_id: c4dd2a1c-8728-aa6b-2e90-2d11c3ca1667
document_version_independent_id: c4dd2a1c-8728-aa6b-2e90-2d11c3ca1667
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-critical-data-elements.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-critical-data-elements
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-critical-data-elements.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: f449b812-6f41-6105-1466-9e35022ab6b2
---

# Critical Data Elements in Unified Catalog (Preview) | Microsoft Learn

Not all data elements have the same importance or sensitivity. Dedicating resources to manage the quality of all data indiscriminately can be impractical and costly. Critical data elements are a logical grouping of important columns across tables in your data sources that you can use to focus your efforts.

These columns should be critical pieces of information that are necessary for decision making and so need to be governed with the highest care. For example, a "Customer ID" critical data element can map "CustID" from one table and "CID" from another table into the same logical container. Users can match this value across data assets to make connections, and when data producers create a new asset, they can use this element as a blueprint to provide quality information in the correct format.

Critical data elements (preview) in Microsoft Purview Unified Catalog are created within governance domains and can have policies set to manage these important pieces of information. When you create a critical data element, your organization can allocate resources strategically, focusing governance effort on areas that have the most significant effect on the business.

## Prerequisites

- You must be using [Microsoft Purview Unified Catalog](unified-catalog).
- To create critical data elements and add columns to them, you must have data steward and data product owner permissions. For more information, see [governance roles and permissions](data-governance-roles-permissions#governance-domain-level-permissions).
- To access data assets in the data map, you need at least data reader permissions on the collection where the asset is housed. For more information about data map permissions, see [Data Map permissions](data-gov-classic-permissions#roles).

## Access critical data

Critical data is defined in governance domains. To see critical data in Unified Catalog:

1. In Unified Catalog, select **Catalog management**, then select **Governance domains**. You see a list of all the governance domains you have access to based on your permissions.
2. Select the governance domain where you want to see your critical data.
3. On the **Details** tab, find the **Critical data elements** card and select **View all**.
4. The **Critical data elements (preview)** page lists all of your critical data elements. Select a name to view its details.

You can also view a list of all critical data elements:

1. In Unified Catalog, under **Discovery**, select **Enterprise glossary**.
2. Select the **Critical data elements** tab.
3. Select the name of a critical data element to open its details page.

### Filter your view by custom attribute

Use [business concept attributes](unified-catalog-attributes-business-concept) as a filter when exploring critical data elements.

1. On the **Critical data elements (preview)** page, select **Add filter**.
2. At **Filter**, select an attribute name from the dropdown list.
3. At **Operator**, select a condition, such as **Equals** or **Starts with**, which varies based on the kinds of values allowed by the attribute.
4. At **Value**, enter your value.
5. Select **Apply**.

### Critical data element details

Select the name of a critical data element to view its details page. You can create and manage access policies for the critical data element by selecting **Manage policies**.

### Overview

On the **Overview** tab, you see a description and:

- **Columns**: All data columns mapped from your assets to this critical data element. You can add columns.
- **Associated data products**: An automatically generated list of data products that have assets associated with your critical data element. 
    Note

    The list of associated data products only refreshes when you add or remove columns.

### Custom attributes

Under **Custom attributes**, you can see any [custom attribute groups and attributes](unified-catalog-attributes-business-concept) within groups, and the values set for each attribute. Only attributes with values are shown by default, but you can toggle **Show attributes without a value** on to view all attributes.

## Create critical data

Note

To create and upload critical data elements, you need the [Data Steward role](data-governance-roles-permissions#governance-domain-level-permissions).

There are two ways you can create critical data elements:

1. Individually
2. In bulk, by importing a formatted CSV file (preview)

### Create a single critical data element

1. In Unified Catalog, select **Catalog management**, then select **Governance domains**.
2. You see a list of all the governance domains you have access to based on your permissions. Select the governance domain where you want to add critical data.
3. On the **Details** tab, find the **Critical data elements** card and select **View all**.
4. Select **New critical data element**.
5. On the **Basic details** page, enter a name for your critical data. If you use a name that already exists, you'll see a warning during the creation process. While duplicating names isn't recommended, you won't be blocked from using a duplicate name.
6. Add a description, owner, and select an expected data type. Then select **Next**.
7. On the **Custom attributes** page, you can set values for all [custom attributes](unified-catalog-attributes-business-concept) defined by your admin in the **Custom attributes** section of the catalog. If the attribute is marked as required, you need to fill out all values on this page before you can complete the process.
8. When done, select **Create**.

You see your critical data in the list of critical data elements.

Note

- Ensure your [governance domain is published](unified-catalog-governance-domains-create-manage#manage-governance-domains) before you publish your critical data element.
- Other users can't see this critical data as a filter in the data product search until its status is set to **Published**.

### Bulk import critical data elements (preview)

You can import multiple critical data elements at once into a governance domain by uploading a formatted CSV file. During the bulk import process, you download a sample CSV file containing a header row. You fill out the file according to the instructions below, then reupload it. The critical data elements then appear in the governance domain in a draft state.

The bulk import process can't be used to edit or update critical data elements.

Note

- You must download the sample CSV (.csv) file and reupload it according to the following instructions. The file must have at least one row of data, not including the header row.
- The CSV file can only include 1,000 rows; more rows cause an upload error. If you need to import more critical data elements, fill out and upload a separate CSV file.
- Special characters are allowed in all fields.
- Each critical data element name must be unique; duplicate names aren't supported for import.

Follow these steps to import critical data elements in bulk to a governance domain:

1. In Unified Catalog, select **Catalog management**, then select **Governance domains**.
2. Select the name of the governance domain you want to add critical data elements to.
3. On the **Details** tab of the governance domain's details page, find the **Critical data elements (preview)** card and select **View all**.
4. On the **Critical data elements (preview)** page, select **Import**.
5. On the **Import** flyout pane, select **Download a sample CSV file**.
6. Open the downloaded file. Fill out the worksheet as described below to avoid upload errors.

    - **Column A - name** (required): Enter the critical data element name. Every name must be unique; there can't be multiple rows with the same name. Maximum length is 256 characters.
    - **Column B - description** (required): Enter a description for the critical data element. Maximum length is 10,000 characters.
    - **Column C - owners** (required): Enter a valid email address that belongs to the same tenant that you're importing from. You can add multiple email addresses separated with a semicolon; for example: `owner1@contoso.com;owner2@econtoso.com`. Groups without email aren't supported.
    - **Column D - data type** (required): Enter one of the possible values: number, text, date/time, Boolean.
7. **Column E and onward**: These are [custom attributes](unified-catalog-attributes-business-concept), which differ by governance domain based on how they're defined and scoped. Note these formatting requirements for specific entry types: - **Multiselect options**: Enter the objects inside square brackets and in quotes; for example, `["a"]`, or `["a", "b"]`. - **Single select options**: Enter the raw value; for example, `a1`, `b2`. - **Booleans**: Enter `true` or `false`; can be upper or lowercase. - **String or rich text**: Use regular text; don't add quotes unless you want quotes reflected in the attribute. - **Numeric - short, int, long, double, float, bit, byte**: Don't add quotes, just enter the number.
8. After formatting your CSV file, save it locally. Return to the **Import** flyout pane, select **Browse**, then find and select your CSV file to upload it.
9. On the **Import** flyout pane, select **OK** to start the import process.

If there's a problem with the CSV file, an error message appears on the **Import** pane explaining the error so you can fix the CSV file and reupload it.

If there are no problems with the file, the import process begins. Depending on the size of the CSV file, it might take some time to complete the import process. If the file is small, the import happens immediately and you see a success message. Larger files take longer for the import process to complete.

Check the status by returning to the governance domain details page. On the **Details** tab, select **Monitoring** to view the status of your bulk import jobs, including any errors, on the **Monitoring** page.

## Add columns

After you create your critical data, you can add data columns to map critical columns from your assets to this logical concept.

1. Select your critical data element from the list of critical data elements in your governance domain.
2. Select the **+ Add column** button.
3. Search for your data sources by using keywords and filters, and select a data source.
4. In that data source, select any relevant column.
5. Select **Add**.
6. You should now see all your columns mapped to your critical data element.
7. Repeat for any number of data sources and columns.

    Below the columns you add, you also see the list of data products that are associated with the assets you add to your critical data element.

## Remove column

To remove a column from a critical data element, select the ellipsis **...** button in the row where the column is listed, and select **Remove**.

If you can't find the column you want to remove, select the **View all columns** button to see the full list of columns.

## Update and edit critical data

Note

To edit a critical data element, you need the [data steward role](data-governance-roles-permissions#governance-domain-level-permissions).

1. On the critical data's details page, select **Edit**.
2. On the **Basic details** page, you can edit the name, description, owner, and expected data type. If you change the name to one that already exists, you'll see a warning about the duplication but you can proceed to use the duplicate name.
3. On the **Custom attributes** page, you can set values for all [custom attributes](unified-catalog-attributes-business-concept) defined by your admin in the **Custom attributes** section of the catalog. If the attribute is marked as required, you need to fill out all values on this page before you can complete the process.
4. Select **Save** to save your changes.

To update the status of your critical data element, select the **Status** button to change between: **Draft**, **Published**, and **Expired**.

## Manage related terms

You can link your critical data elements to related glossary terms.

1. Select the governance domain where your critical data element resides.
2. Select the **Critical data elements** button.
3. Search or browse for the critical data element and select it.
4. To link your critical data element to a glossary term, select the **+ Add term** button.
5. Search for the term, or terms, you want to link and select them.
6. To add your selected terms, select **Add**.
7. To remove a related term, select the term, then select the **...** ellipsis button, and then the **Remove** button.

## Delete critical data

To delete a critical data element, you need to unpublish it and delete all columns within it, and any links to glossary terms. You can then select the **Delete** button and proceed with deleting the critical data element.

## Remove data that's deleted from Data Map and metadata sync from Data Map (preview)

If the parent data asset of a column in a critical data element is deleted in Data Map, a banner appears in the critical data element to inform you of the asset deletion. However, the column still appears in the critical data element until you remove it.

Open the critical data element to view the list of columns. Columns with a caution symbol on its row have been deleted from Data Map due to their parent data asset deletion. To remove the deleted column from your critical data element, select ellipsis (...) in the row, then select **Remove**.

When you open the asset detail page from assets in a critical data element, the metadata is retrieved from the Data map. Metadata changes in Data map are now reflected in Unified Catalog after they're updated in Data map or initiated by selecting the refresh button.

For metadata represented within parent assets, such as columns within tables and views, the changes may not appear immediately. However, in all cases, metadata changes are reflected in Unified Catalog within 24 hours.

## Manage access policies

To manage access policies for critical data, you need [data steward](data-governance-roles-permissions) permissions.

1. On your governance domain's page, select your critical data elements.
2. Select a critical data element.
3. Select **Manage policies**.
4. From the policy configuration window, you're able to create and manage access policies for your critical data elements.
5. For more information about setting up access policies, see [the documentation about managing access policies](unified-catalog-data-product-access-policies#set-up-data-product-access-policies).

    These policies apply to all associated data products in your critical data element.