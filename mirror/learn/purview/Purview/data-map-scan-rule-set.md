---
layout: Conceptual
title: Create a scan rule set in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-scan-rule-set
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-04-23T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to create a scan rule set in Microsoft Purview Data Map to quickly scan data sources in your organization.
locale: en-us
document_id: 9a360db5-e80d-f020-8839-3dfce597f4f6
document_version_independent_id: 9a360db5-e80d-f020-8839-3dfce597f4f6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-scan-rule-set.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-scan-rule-set
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-scan-rule-set.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 80508c0d-7fd9-7d9b-7555-76d752807a36
---

# Create a scan rule set in Microsoft Purview Data Map | Microsoft Learn

In Microsoft Purview Data Map, you can create scan rule sets to customize [data source scans](data-map-scan-data-sources) in your organization.

A scan rule set is a container that groups a set of scan rules together. You can easily associate a scan rule set with a scan. For example, you might create a default scan rule set for each of your data source types, and then use these scan rule sets by default for all scans within your company. You might also want users with the right permissions to create other scan rule sets with different configurations based on business need.

## Steps to create a scan rule set

To create a scan rule set:

1. In the Microsoft Purview portal, select the **Data Map** solution.
2. Under the **Source management** section, select **Scan rule sets**, and then select **New**.
3. From the **New scan rule set** page, select the data sources that the catalog scanner supports from the **Source Type** dropdown list. You can create a scan rule set for each type of data source you intend to scan.
4. Enter a **Name** for the scan rule set. The maximum length is 63 characters, with no spaces allowed. Optionally, enter a **Description**. The maximum length is 256 characters.
5. Select a domain.

    Important

    You can only use the scan rule set in the domain where you create it.
6. Select **Continue**.

    The **Select file types** page appears. Notice that the file type options on this page vary based on the data source type that you chose on the previous page. All the file types are enabled by default.

    ![Screenshot showing the Select file types page.](media/create-a-scan-rule-set/select-file-types-page.png)

    The **Document file types** selection on this page allows you to include or exclude the following Microsoft Office file types: `.doc; .docm; .docx; .dot; .odp; .ods; .odt; .pdf; .pot; .pps; .ppsx; .ppt; .pptm; .pptx; .xlc; .xls; .xlsb; .xlsm; .xlsx; xlt`.
7. Enable or disable a file type for schema and classification by selecting or clearing its check box. If you choose a Data Lake type data source (for example, Azure Data Lake Storage Gen2 or Azure Blob), enable the file types for which you want to have schema extracted and classified.

    Important

    Deselecting a file type **doesn't** prevent ingestion. The file's information is still ingested, but its schema and classifications aren't extracted.
8. For certain data source types, you can also Create a custom file type.
9. Select **Continue**.

    The **Select classification rules** page appears. This page displays the selected **System rules** and **Custom rules**, and the total number of classification rules selected. By default, all the **System rules** check boxes are selected.
10. For the rules you want to include or exclude, select or clear the **System rules** classification rule checkboxes globally by category.

    ![Screenshot showing the Select classification rules page.](media/create-a-scan-rule-set/select-classification-rules.png)
11. You can expand the category node and select or clear individual check boxes. For example, if the rule for **Argentina.DNI Number** has high false positives, you can clear that specific check box.

    ![Screenshot showing how to select system rules.](media/create-a-scan-rule-set/select-system-rules.png)
12. Select **Create** to finish creating the scan rule set.

## Create a custom file type

Microsoft Purview supports adding a custom extension and defining a custom column delimiter in a scan rule set.

To create a custom file type:

1. Follow steps 1–5 in Steps to create a scan rule set or edit an existing scan rule set.
2. On the **Select file types** page, select **New file type** to create a new custom file type.

    ![Screenshot showing how to select New file type from the Select file types page.](media/create-a-scan-rule-set/select-new-file-type.png)
3. Enter a **File Extension** and an optional **Description**.

    ![Screenshot showing the New custom file type page.](media/create-a-scan-rule-set/new-custom-file-type-page.png)
4. Make one of the following selections for **File contents within** to specify the type of file contents within your file:

    - Select **Custom Delimiter** and enter your own **Custom delimiter** (single character only).
    - Select **System File Type** and choose a system file type (for example XML) from the **System file type** drop-down list.
5. Select **Create** to save the custom file.

    The system returns to the **Select file types** page and inserts the new custom file type as a new tile.

    ![Screenshot showing the new custom file type tile on the Select file types page.](media/create-a-scan-rule-set/new-custom-file-type-tile.png)
6. Select **Edit** in the new file type tile if you want to change or delete it.
7. Select **Continue** to finish configuring the scan rule set.

## Ignore patterns

Microsoft Purview supports defining regular expressions (regex) to exclude assets during scanning. During scanning, Purview compares the asset's URL against these regular expressions. Microsoft Purview ignores all assets that match any of the regexes.

The **Ignore patterns** pane prepopulates one regex for spark transaction files. You can remove the preexisting pattern if it isn't required. You can define up to 10 ignore patterns.

![Screenshot showing the ignore patterns blade with four defined regular expressions. The first is the prepopulated spark transaction regex, the second is \\.txt$, the third is \\.csv$, and finally .folderB/.*.](media/create-a-scan-rule-set/ignore-patterns-blade.png)

In the preceding example:

- Regexes 2 and 3 ignore all files ending with .txt and .csv during scanning.
- Regex 4 ignores /folderB/ and all its contents during scanning.

Here are some more tips you can use to ignore patterns:

- While processing the regex, Microsoft Purview adds $ to the regex by default.
- To understand what URL the scanning agent compares with your regular expression, browse through Microsoft Purview Unified Catalog, find the asset you want to ignore in the future, and see its fully qualified name (FQN) in the **Overview** tab.

    ![Screenshot showing the fully qualified name on an asset's overview tab.](media/create-a-scan-rule-set/fully-qualified-name.png)

## System scan rule sets

System scan rule sets are Microsoft-defined scan rule sets that are automatically created for each Microsoft Purview catalog. Each system scan rule set is associated with a specific data source type. When you create a scan, you can associate it with a system scan rule set. Every time Microsoft makes an update to these system rule sets, you can update them in your catalog, and apply the update to all the associated scans.

1. To view the list of system scan rule sets, select **Scan rule sets** in the **Management Center** and choose the **System** tab.

    [![Screenshot showing the list of system scan rule sets.](media/create-a-scan-rule-set/system-scan-rule-sets.jpg)](media/create-a-scan-rule-set/system-scan-rule-sets.jpg#lightbox)
2. Each system scan rule set has a **Name**, **Source type**, and a **Version**. If you select the version number of a scan rule set in the **Version** column, you see the rules associated with the current version and the previous versions (if any).

    [![Screenshot showing a system scan rule set page.](media/create-a-scan-rule-set/system-scan-rule-set-page.jpg)](media/create-a-scan-rule-set/system-scan-rule-set-page.jpg#lightbox)
3. If an update is available for a system scan rule set, you can select **Update** in the **Version** column. In the system scan rule page, choose a version from the **Select a new version to update** drop-down list. The page provides a list of system classification rules associated with the new version and current version.

    [![Screenshot showing how to change the version of a system scan rule set.](media/create-a-scan-rule-set/system-scan-rule-set-version.jpg)](media/create-a-scan-rule-set/system-scan-rule-set-version.jpg#lightbox)

### Associate a scan with a system scan rule set

When you [create a scan](data-map-scan-data-sources), choose to associate it with a system scan rule set as follows:

1. On the **Select a scan rule set** page, select the system scan rule set.

    [![Screenshot showing how to select a system scan rule set for a scan.](media/create-a-scan-rule-set/set-system-scan-rule-set.jpg)](media/create-a-scan-rule-set/set-system-scan-rule-set.jpg#lightbox)
2. Select **Continue**, and then select **Save and Run**.