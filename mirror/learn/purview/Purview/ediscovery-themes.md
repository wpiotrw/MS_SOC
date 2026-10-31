---
layout: Conceptual
title: Themes in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-themes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use Themes in eDiscovery (Premium) to organize review sets by finding the dominant theme in each document.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-mar2020
locale: en-us
document_id: e75ea166-564e-b717-6fe7-5a33570191a7
document_version_independent_id: e75ea166-564e-b717-6fe7-5a33570191a7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-themes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-themes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-themes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: c24c6a18-c7bf-0d8e-e2c2-bf118e4aebbd
---

# Themes in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When you create a new document, you generally start with one or more ideas that you want to convey in the document, and then compose the document using words that align with these ideas. The more prevalent an idea is, the more frequent the words that are related to that idea tend to be. This method also aligns to how readers consume documents. The important things to understand from reading a document are the main ideas that the document is trying to convey. This also includes which ideas appear where and what the relationships between the ideas are.

This process can be extended to how an eDiscovery reviewer wants to consume a set of documents in a case. They want to see which ideas are present in the review sets and which documents are talking about those ideas. If they find a particular document of interest, they want to be able to see documents that discuss similar ideas.

The **Themes** functionality in eDiscovery (Premium) attempts to mimic how humans reason about documents, by analyzing the *themes* that are discussed in a review set and assigning a theme to documents in the review set. In eDiscovery (Premium), Themes goes one step further and identifies the *dominant theme* in each review set and document. The *dominant theme* is the one that appears the most often in a document.

## How does themes work?

The **Themes** functionality analyzes documents with text in a review set to parse out common themes that appear across all the documents in the review set. eDiscovery (Premium) assigns those themes to the documents in which they appear. It also labels each theme with the words used in the documents that are representative of the theme. Because a document can contain various types of subject matter, eDiscovery (Premium) often assigns multiple themes to review sets and documents. This is referred to as the *Themes list*. The theme that appears most prominently in a review set or document is designated as its *dominant theme*.

## Configuring Themes

Themes are supported for cases and apply to all the review sets within them. You can configure the settings for themes when you create a new case or you can update the theme settings for an existing case.

## Configure Themes when creating a new case

To configure themes when you create a new case, complete the following steps:

1. In the [Microsoft Purview portal](https://compliance.microsoft.com/), navigate to **eDiscovery** &gt; **Premium**.
2. Select the **Cases** tab and open an eDiscovery (Premium) case, and then select **Create a case**.
3. On the **Name and description** page, name the case and complete the **Description**, **Number**, and **Case format** options as applicable. Select **Next** to continue.
4. On the **Members and settings** page, select **Group items by theme**. Select the following theme options as applicable:
    - **Maximum number of themes:** Specifies the maximum number of themes that can be generated when you run analytics on the data in review sets included in a case. For more information on limits, see [Limits in eDiscovery (Premium)](ediscovery-premium-limits#themes-limits).
    - **Add numeric identifiers to themes:** Numbers (that identify a theme) are included when generating themes.
    - **Automatically set maximum number of themes:** In certain situations, there may not be enough documents in a review set to produce the desired number of themes for the case. When this setting is enabled, eDiscovery (Premium) adjusts the maximum number of themes dynamically rather than attempting to enforce the maximum number of themes.
5. If you need to exclude keywords associated with themes, enter the text or regular expression needed in the **Text to ignore** field. In the **Apply to** field, select **Themes** to apply the text or regular expression to all themes.
6. Complete the other field on the **Members and settings** page as applicable, then select **Next**.
7. On the **Summary** page, review the case settings, then select **Submit** to create the case.

After a new case is created, analytics are automatically run on the data when the review sets are added to the case. Themes for the review sets are generated as part of the analytics processing.

## Configure Themes for an existing case

To configure themes for an existing case, complete the following steps:

1. In the [Microsoft Purview portal](https://compliance.microsoft.com/), navigate to **eDiscovery** &gt; **Premium**.
2. Select the **Cases** tab and open an eDiscovery (Premium) case.
3. Select the **Settings** tab, and then choose **Select** on the **Search & analytics** card.
4. On the **Search & analytics** page, select the **Themes**checkbox and configure the following options as applicable:
    - **Max number of themes:** Specifies the maximum number of themes that can be generated when you run analytics on the data in review sets included in a case. For more information on limits, see [Limits in eDiscovery (Premium)](ediscovery-premium-limits#themes-limits).
    - **Include numbers themes:** Numbers (that identify a theme) are included when generating themes.
    - **Adjust maximum number of themes dynamically:** In certain situations, there may not be enough documents in a review set to produce the desired number of themes for the case. When this setting is enabled, eDiscovery (Premium) adjusts the maximum number of themes dynamically rather than attempting to enforce the maximum number of themes.
5. If you need to exclude keywords associated with themes, select **Edit** in the **Ignore text** section. Enter the text or regular expression needed in the **Text (Regular expressions are supported)** field. In the **Apply to** field, select **Themes** to apply the text or regular expression to all themes.
6. Select **Save** to save the theme settings.
7. Navigate to the review set in the case that you want to apply the new theme settings to, and select **Analytics** &gt; **Run Document & email analytics**.
8. Select **Yes** to confirm that you want to run analytics on the review set.

After the analytics job completes, you can view the themes that were generated for the review set by filtering the documents in the review set by theme.

## Filtering documents by Theme

Filtering documents by theme can significantly save time when reviewing documents. For example, if you're looking for documents that discuss a particular topic, you can filter the documents by the dominant theme that is related to that topic. You can also filter documents by other themes in the theme list to find documents that are similar to a document that you're interested in. To display the themes for a document as a column in the document list for the review set, select **Customize columns** and select **Dominant theme** and **Themes list**.

To filter documents by theme, complete the following steps:

1. In a review set, choose **Filters** and expand the options for **Analytics & predictive coding**.
2. Select **Dominant theme** and **Themes list**, and then select **Done** to add these filters to the review set.
3. Use the conditional controls as needed to filter the documents by specific themes for each of these filters.

To filter documents by theme using [advanced filters (preview)](ediscovery-review-set-search#advanced-filters-preview), complete the following steps:

1. In a review set, choose **Select a filter** and select **Dominant theme**.
2. Select an operator to use with the **Dominant theme** and define the value to use with the operator.
3. Use an addition **Themes list** filter and the operator and values to applicable to this filter. You can configure the **AND** and **OR** operators to filter documents by a combination of the **Dominant theme** and **Themes list** values.