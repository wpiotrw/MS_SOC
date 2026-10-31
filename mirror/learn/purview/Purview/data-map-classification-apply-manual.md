---
layout: Conceptual
title: Manually apply classifications on assets in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-classification-apply-manual
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2022-12-30T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how Microsoft Purview solutions can deliver a modern data governance experience for your organization.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 5755f8ae-1957-379d-1f36-1d7eba7a9bba
document_version_independent_id: 5755f8ae-1957-379d-1f36-1d7eba7a9bba
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-classification-apply-manual.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-classification-apply-manual
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-classification-apply-manual.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b9127c15-bc9f-9773-4c2e-5d21933871cf
---

# Manually apply classifications on assets in Microsoft Purview Data Map | Microsoft Learn

This article discusses how to manually apply classifications on assets in Microsoft Purview Data Map.

[Classifications](data-map-classification) are logical labels to help you and your team identify the kinds of data you have across your data estate. For example: if files or tables contain credit card numbers, or addresses.

Microsoft Purview [automatically applies classifications to some assets during the scanning process](data-map-classification-apply-auto), but there are some scenarios when you may want to manually apply more classifications. For example, Microsoft Purview doesn't automatically apply classifications to table assets (only their columns), or you might want to apply custom classifications, or add classifications to assets grouped a [resource set](data-map-resource-sets).

Note

Some custom classifications can be [automatically applied](data-map-classification-apply-auto) after setting up a [custom classification rule](data-map-classification-custom#custom-classification-rules).

Follow the steps in this article to manually apply classifications to file, table, and column assets.

## Manually apply classification to a file asset

1. [Search](unified-catalog-data-assets-search) or [browse](unified-catalog-data-assets-search#browse-the-unified-catalog) Microsoft Purview Unified Catalog for the file you're interested in and navigate to the asset detail page.

    [![Screenshot showing the asset detail page.](media/apply-classifications/asset-detail-page.png)](media/apply-classifications/asset-detail-page.png#lightbox)
2. On the **Overview** tab, view the **Classifications** section to see if there are any existing classifications. Select **Edit**.
3. From the **Classifications** drop-down list, select the specific classifications you're interested in. In our example, we're adding **Credit Card Number**, which is a system classification and **CustomerAccountID**, which is a custom classification.

    [![Screenshot showing how to select classifications to add to an asset.](media/apply-classifications/select-classifications.png)](media/apply-classifications/select-classifications.png#lightbox)
4. Select **Save**.
5. On the **Overview** tab, confirm that the classifications you selected appear under the **Classifications** section.

    [![Screenshot showing how to confirm classifications were added to an asset.](media/apply-classifications/confirm-classifications.png)](media/apply-classifications/confirm-classifications.png#lightbox)

## Manually apply classification to a table asset

When Microsoft Purview scans your data sources, it doesn't automatically assign classifications to table assets (only on columns). For a table asset to have classifications, you must add them manually:

To add a classification to a table asset:

1. [Search](unified-catalog-data-assets-search) or [browse](unified-catalog-data-assets-search#browse-the-unified-catalog) Unified Catalog for the table asset that you're interested in. For example, **Customer** table.
2. Confirm that no classifications are assigned to the table. Select **Edit**.

    [![Screenshot showing how to view and edit the classifications of a table asset.](media/apply-classifications/select-edit-from-table-asset.png)](media/apply-classifications/select-edit-from-table-asset.png#lightbox)
3. From the **Classifications** drop-down list, select one or more classifications. This example uses a custom classification named **CustomerInfo**, but you can select any classifications for this step.

    [![Screenshot showing how to select classifications to add to a table asset.](media/apply-classifications/select-classifications-in-table.png)](media/apply-classifications/select-classifications-in-table.png#lightbox)
4. Select **Save** to save the classifications.
5. On the **Overview** page, verify that Microsoft Purview added your new classifications.

    [![Screenshot showing how to verify that classifications were added to a table asset.](media/apply-classifications/verify-classifications-added-to-table.png)](media/apply-classifications/verify-classifications-added-to-table.png#lightbox)

## Manually add classification to a column asset

Microsoft Purview automatically scans and adds classifications to all column assets. However, if you want to change the classification, you can do so at the column level:

1. [Search](unified-catalog-data-assets-search) or [browse](unified-catalog-data-assets-search#browse-the-unified-catalog) Unified Catalog for the table asset that contains the column you want to update.
2. Select **Edit** from the **Overview** tab.
3. Select the **Schema** tab.

    [![Screenshot showing how to edit the schema of a column.](media/apply-classifications/edit-column-schema.png)](media/apply-classifications/edit-column-schema.png#lightbox)
4. Identify the columns you're interested in and select **Add a classification**. This example adds a **Common Passwords** classification to the **PasswordHash** column.

    [![Screenshot showing how to add a classification to a column.](media/apply-classifications/add-classification-to-column.png)](media/apply-classifications/add-classification-to-column.png#lightbox)
5. Select **Save**.
6. Select the **Schema** tab and confirm that the classification has been added to the column.

    [![Screenshot showing how to confirm that a classification was added to a column schema.](media/apply-classifications/confirm-classification-added.png)](media/apply-classifications/confirm-classification-added.png#lightbox)

## View classification details

Microsoft Purview captures important details like who applied a classification and when it was applied. To view the details, hover over the classification to revel the Classification details card. The classification details card shows the following information:

- Classification name - Name of the classification applied on the asset or column.
- Applied by - Who applied the classification. Possible values are scan and user name.
- Applied time - Local timestamp when the classification was applied via scan or manually.
- Classification type - System or custom.

Users with Data Curator role can see more details for classifications that were applied automatically through a scan. These details include sample count that the scanner read to classify the data, and distinct data count in the sample that the scanner found.

## Impact of rescanning on existing classifications

Classification tags are automatically applied the first time based on sampling your data and matching those samples against predefined RegEx patterns or dictionaries. Subsequent rescans can preserve, remove, or incrementally add classification tags depending on several factors:

- A scan run doesn't remove classification tags that were manually applied.
- A scan run doesn't reapply classification tags that were manually removed.
- A later run of a scan that continues to use the same scan rule can update the classification tags.
- For a scan run, classification tags from the previous scans can get removed or retained based on the criteria listed in this table:

    | File type | File size | Classification tags from previous scan will be: |
    | --- | --- | --- |
    | File types with no size (for example, SQL) | All | Retained |
    | .doc, .docm, .docx, .dot, .odp, .ods, .odt, .pdf, .pot, .pps, .ppsx, .ppt, .pptm, .pptx, .txt, .xlc, .xls, .xlsb, .xlsm, .xlsx, .xlt | &gt;20 MB | Retained |
    | .doc, .docm, .docx, .dot, .odp, .ods, .odt, .pdf, .pot, .pps, .ppsx, .ppt, .pptm, .pptx, .txt, .xlc, .xls, .xlsb, .xlsm, .xlsx, .xlt | &lt;20 MB | Removed |
    | GZ | &gt;400 KB | Retained |
    | GZ | &lt;400 KB | Removed |
    | Files with no extension or structured file types | &gt; 1 MB | Retained |
    | Files with no extension or structured file types | &lt; 1 MB | Removed |