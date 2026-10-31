---
layout: Conceptual
title: Automatically Apply Classifications on Data Map Assets | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-classification-apply-auto
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2025-03-25T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to automatically apply classifications on assets in Microsoft Purview Data Map.
locale: en-us
document_id: c260f23e-97ab-7fc3-9826-88741dca7045
document_version_independent_id: c260f23e-97ab-7fc3-9826-88741dca7045
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-classification-apply-auto.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-classification-apply-auto
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-classification-apply-auto.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 2be69dc2-3edf-f599-d9b2-c9a37d5f2fee
---

# Automatically Apply Classifications on Data Map Assets | Microsoft Learn

After data sources are [registered](data-map-data-sources-register-manage#register-a-new-source) in Microsoft Purview Data Map, the next step is to [scan](data-map-scan-ingestion) the data sources. The scanning process establishes a connection to the data source, captures technical metadata, and can automatically classify data using either the [supported system classifications](data-map-classification-supported-list) or [rules for your custom classifications](data-map-classification-custom#custom-classification-rules).

For example, if you have a file named *multiple.docx* and it has a National ID number in its content, during the scanning process Data Map adds the classification **EU National Identification Number** to the file asset's detail page.

These [classifications](data-map-classification) help you and your team identify the kinds of data you have across your data estate. For example: if files or tables contain credit card numbers, or addresses. Then you can more easily search for certain kinds of information, like customer IDs, or prioritize security for sensitive data types.

Classifications can be automatically applied on file and column assets during scanning.

In this article we'll discuss:

- The steps to automatically apply classifications
- How Microsoft Purview classifies assets

## Automatically apply classifications

Note

Table assets are not automatically assigned classifications, because the classifications are assigned to their columns, but you can [manually apply classifications to table assets](data-map-classification-apply-manual#manually-apply-classification-to-a-table-asset).

After data sources are [registered](data-map-data-sources-register-manage#register-a-new-source), you can automatically classify data in that source's data assets by running a [scan](data-map-scan-ingestion).

1. Check the **Scan** section of the [source article](data-map-data-sources) for your data source to confirm any prerequisites or authentication are set up and ready for a scan.
2. Search the Microsoft Purview Data Map the registered source that has the data assets (files and columns), you want to classify.
3. Select the **New Scan** icon under the resource.

    ![Screenshot of the Microsoft Purview Data Map, with the new scan button selected under a registered source.](media/apply-classifications/new-scan.png)

    Tip

    If you don't see the New Scan button, you may not have correct permissions. To run a scan, you'll need at least [data source administrator permissions](data-gov-classic-permissions) on the collection where the source is registered.
4. Select your credential and authenticate with your source. (For more information about authenticating with your source, see the **prerequisite** and **scan** sections of your specific source [source article](data-map-data-sources).) Select **Continue**.
5. If necessary, select the assets in the source you want to scan. You can scan all assets, or a subset of folders, files, or tables depending on the source.
6. Select your scan rule set. You'll see a list of available scan rule sets and can select one, or you can choose to create a new scan rule set using the **New scan rule set** button at the top. The scan rule set will determine which classifications will be compared and applied to your data. For more information, see how Microsoft Purview classifies assets.

    ![Screenshot of the scan rule set page of the scan menu, with the new scan rule set and existing scan rule set buttons highlighted.](media/apply-classifications/select-scan-rule-set.png)

    Tip

    For more information about the options available when creating a scan rule set, start at step 4 of these [steps to create a scan rule set](data-map-scan-rule-set#steps-to-create-a-scan-rule-set).
7. Schedule your scan.
8. Save and run your scan. Applicable classifications in your scan rule set will be automatically applied to the assets you scan. You'll be able to view and manage them once the scan is complete.

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

## How Microsoft Purview classifies assets

When a data source is scanned, Microsoft Purview compares data in the asset to a list of possible classifications called a [scan rule set](data-map-scan-rule-set).

There are [system scan rule sets](data-map-scan-rule-set#system-scan-rule-sets) already available for each data source that contains every currently available system classification for that data source. Or, you can [create a custom scan rule set](data-map-scan-rule-set) to make a list of classifications tailored to your data set.

Making a custom rule sets for your data can be a good idea if your data is limited to specific kinds of information, or regions, as comparing your data to fewer classification types will speed up the scanning process. For example, if your dataset only contains European data, you could create a custom scan rule set that excludes identification for other regions.

You might also make a custom rule set if you've created [custom classifications](data-map-classification-custom#steps-to-create-a-custom-classification) and [classification rules](data-map-classification-custom#custom-classification-rules), so that your custom classifications can be automatically applied during scanning.

For more information about the available system classifications and how your data is classified, see the [list of system classifications](data-map-classification-supported-list).