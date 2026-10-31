---
layout: Conceptual
title: Create and Manage OKRs in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-okrs-create-manage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2025-07-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to create and manage objectives and key results (ORKs) in Microsoft Purview Unified Catalog.
locale: en-us
document_id: aa7ab879-ed6a-d1ae-6bd8-f87ec3982169
document_version_independent_id: aa7ab879-ed6a-d1ae-6bd8-f87ec3982169
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-okrs-create-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-okrs-create-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-okrs-create-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 0d445544-d3ed-3c76-7dd6-2f4808098929
---

# Create and Manage OKRs in Unified Catalog | Microsoft Learn

[Objectives and key results (OKRs)](unified-catalog-okrs) in Microsoft Purview Unified Catalog are trackable business objectives tied to [governance domains](unified-catalog-governance-domains) and [data products](unified-catalog-data-products) to emphasize the value of business data.

This article describes how to manage OKRs in Microsoft Purview. It provides steps to create OKRs in a [governance domain](unified-catalog-governance-domains), create key results, and connect them to your data products.

## Prerequisites

- Any user can read published OKRs.
- To create and edit OKRs, you need the [steward role](data-governance-roles-permissions#governance-domain-level-permissions).

## Access OKRs

1. In Unified Catalog, select **Catalog management**, then select **Governance domains**.
2. Select the governance domain you'd like to see OKRs for.
3. On the **Details** tab, find the **OKRs** card and select **View all**.

The full list of OKRs for that governance domain is displayed. Select an OKR to see its detailed view, and get more information about its key results.

You can also view a list of all OKRs:

1. In Unified Catalog, under **Discovery**, select **Enterprise glossary**.
2. Select the **OKRs** tab.
3. Select the name of an OKR to open its details page.

### Filter your view by custom attribute

Use [business concept attributes](unified-catalog-attributes-business-concept) as a filter when exploring OKRs.

1. In Unified Catalog, go to **Discovery** &gt; **Enterprise glossary**.
2. On the **OKRs** tab, select **Add filter**.
3. At **Filter**, select an attribute name from the dropdown list.
4. At **Operator**, select a condition, such as **Equals** or **Starts with**, which varies based on the kinds of values allowed by the attribute.
5. At **Value**, enter your value.
6. Select **Apply**.

### Overview

The **Overview** tab shows key results, associated data products, target date, and current overall progress.

### Custom attributes

Under **Custom attributes**, you can see any [custom attribute groups and attributes](unified-catalog-attributes-business-concept) within groups, and the values set for each attribute. Only attributes with values are shown by default, but you can toggle **Show attributes without a value** on to view all attributes.

## Create OKRs

You can create OKRs directly in the Microsoft Purview portal.

1. In Unified Catalog, select **Catalog management**, then select **Governance domains**.
2. Select the governance domain you want to add an OKR to.
3. On the **Details** tab, find the **OKRs** card and select **View all**.
4. On the **OKRs** page, select **New OKR**.
5. On the **Basic details** page, at **Objective**, enter a statement describing the action you'll take and why it matters. For example: Revamp customer service to improve satisfaction and retention rates. If you use a name that already exists, you'll see a warning during the creation process. While duplicating names isn't recommended, you won't be blocked from using a duplicate name.
6. Select an owner or owners for your OKR.
7. Select a target date to meet the OKR.
8. Select **Next**.
9. On the **Custom attributes** page, you can set values for all [custom attributes](unified-catalog-attributes-business-concept) defined by your admin in the **Custom attributes** section of the catalog. If the attribute is marked as required, you need to fill out all values on this page before you can complete the process.
10. Select **Create**.

You see the details page for your new OKR, where you can edit or manage your OKR, view key results, and view linked data products.

Note

Only stewards and governance domain owners can see your OKR until you publish it.

## Key results

Key results are how you track the overall progress of an OKR. They should be specific, measurable outcomes so you and your team can accurately gauge progress or completion.

The top key results are listed on the details page. To view any others, select **View all key results**.

Select a specific key result to see its details.

### Create key result

To create a new key result for an OKR:

1. In your OKR's details page, select **Add key result**.
2. Add your key result statement - it should be a specific, measurable outcome that uses metrics. For example: Increase customer retention rate by 25%.
3. Select current progress status - on track, behind, or at risk.
4. Set progress amount as a percentage or a value.
5. Set goal amount as a percentage or a value.
6. Set the maximum allowed amount as a percentage or value.
7. Select **Create**.

Your newly created key result is now listed under key results in your OKR.

### Update key result

1. In your OKR's details page, select the key result you want to update, or select **View all key results** to see a full list of key results.
2. Select the key result you want to edit, and select the **Edit** button.
3. Edit the result, progress status, progress amount, goal amount, or maximum amount.
4. Select **Save** to save your updates.

## Data products

Add, remove, and view data product links all from within your business OKR.

### View linked data products

You can view all your linked data products from within your OKR. The details page lists the first 10 linked data products. Select **View all data products** to see and search the entire list.

### Add data product link

1. In your OKR's details page, select the **+ Link data product** button.
2. Search for the data products you want to link.
3. Select the data products you want to link.
4. Remove any selected products from the **Selected** list by selecting the **X** button next to their name.
5. To add your selected data products, select **Save**.

### Remove linked data products

To remove a linked data product:

1. Open the OKR where the data product is linked.
2. Find the data product on the details page or select **View all data products** to search for it.
3. Select the ellipsis button (**...**) next to the data product and select **Remove link**.

## Edit and manage OKRs

1. On the OKR's details page, select **Edit**.
2. On the **Basic details** page, update the objective, owner, and target date. If you change the name to one that already exists, you'll see a warning about the duplication but you can proceed to use the duplicate name.
3. Select **Save**.
4. On the **Custom attributes** page, you can set values for all [custom attributes](unified-catalog-attributes-business-concept) defined by your admin in the **Custom attributes** section of the catalog. If the attribute is marked as required, you need to fill out all values on this page before you can complete the process.
5. Select **Save**.

### Draft, publish, or close

You can publish a drafted OKR, or unpublish a previously published OKR and set it to draft or closed. Closing an OKR limits its visibility to stewards and governance domain owners.

To publish or unpublish an OKR:

Closing an OKR limits its visibility to stewards and governance domain owners. Deleted OKRs are removed from the governance domain.

1. Select the governance domain you'd like to publish or unpublish an OKR from.
2. Select the **OKRs** card.
3. Search or browse for the OKR and select it.
4. Select **Publish** if in draft state and **Unpublish** if already published.
5. You can either **Set to draft** for further edits or **Set to closed** if you don't wish to use it any longer.

Note

Ensure your [governance domain is published](unified-catalog-governance-domains-create-manage#manage-governance-domains) before you publish your OKRs.

## Delete OKRs

To delete an OKR, first unpublish it and delete any key results and links to related data products. Then select **Delete** to delete the OKR.