---
layout: Conceptual
title: Analyze data in a review set in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-analyzing-data-in-review-set
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the tools available to organize document sets when analyzing an Microsoft Purview eDiscovery (Premium) case.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
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
document_id: 6de6112f-2bb2-d4ec-155b-69450caa1c15
document_version_independent_id: 6de6112f-2bb2-d4ec-155b-69450caa1c15
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-analyzing-data-in-review-set.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-analyzing-data-in-review-set
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-analyzing-data-in-review-set.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 3f9feb89-deca-5efe-5218-3d24de9d28dd
---

# Analyze data in a review set in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When the number of collected documents is large, it can be difficult to review them all. Microsoft Purview eDiscovery (Premium) provides a number of tools to analyze the documents to reduce the volume of documents to be reviewed without any loss in information, and to help you organize the documents in a coherent manner. To learn more about these capabilities, see:

- [Near duplicate detection](ediscovery-near-duplicate-detection)
- [Email threading](ediscovery-email-threading)
- [Themes](ediscovery-themes)

## Run analytics for a review set

To analyze data in a review set:

1. Configure analytics settings for your case. For more information, see [Configure search and analytics settings](ediscovery-configure-search-and-analytics-settings).
2. Open the review set you want to analyze.
3. Select **Analytics** &gt; **Run document & email analytics**.

    ![Select Run document &amp; email analytics from the Analytics dropdown list](media/runanalytics1.png)

You can check the progress of analysis on the **Jobs** tab of the case.

After analysis is completed, you can view the analytics report, run queries within your review set on outputs of the analysis (see [Query within your review set](ediscovery-review-set-search), and see related documents of a given document (see [Reviewing data in review set](ediscovery-review-set-search).

## Using the For Review filter query

After running analytics for the review set, you can use an automatically generated filter query (called *For Review*) that filters your review to exclude immaterial, duplicate, or non-inclusive items. This leaves you with only the items that are representative, unique, and inclusive in the review set.

To apply the **For Review** filter query to a review set, select the **Saved filter queries** dropdown list, and then select **[AutoGen] For Review**.

![Select For Review from the Saved filter queries dropdown list](media/forreviewfilterquery1.png)

Here's the syntax for the **For Review** filter query:

`(((FileClass="Email") AND (IsInclusive="True") AND (MarkAsRepresentative="Unique")) OR ((FileClass="Attachment") AND (MarkAsRepresentative="Unique")) OR ((FileClass="Document") AND (MarkAsRepresentative="Unique")) OR ((FileClass="Conversation") AND (MarkAsRepresentative="Unique")) OR ((FileClass="Attachment" OR FileClass="Conversation" OR FileClass="Document" OR FileClass="Email") AND NOT (Exists:MarkAsRepresentative)))`

The following list describes the result of the filter query in terms of what content is displayed after you apply it to the review set.

- **Email**: Displays items that are marked as both **Inclusive** and **Representative**. An email is marked as IsInclusive True when it contains all the unique content from a thread, including all previous replies. It ensures that only the most comprehensive email in a thread is reviewed, which is essential for understanding the full context of the conversation without having to review each individual reply. An email is MarkedAsRepresentative Unique when it is the single representative copy among duplicates.
- **Attachments**: Filters out duplicate attachments in the review set. Only attachments that are unique in the review set are displayed.
- **Documents**: Filters out duplicate documents. Only documents that are unique in the review set are displayed.
- **Teams conversations**: Filter out duplicate Teams (and Viva Engage) conversations. Only conversations that are unique in the review set are displayed.
- **Other**: Any emails, attachments, documents and conversations in the review set where MarkedAsRepresentative field contains no value. This means analytics was not able to generate a value for it, so the reviewer should review them and assess themselves.

For more information about inclusive types and document uniqueness, see [Email threading in eDiscovery (Premium)](ediscovery-email-threading).

## Analytics report

To view the analytics report for a review set:

1. Open the review set.
2. Select **Analytics** &gt; **Show reports**.

The **Analytics** report has seven components from the analysis:

- **Target population:** The number of email messages, attachments, and loose documents found in the review set.
- **Documents (excluding attachments):** The number of loose documents that are pivots, unique near duplicates of a pivot, or an exact duplicate of another document.
- **Emails:** The number of email messages that are marked as *inclusive* vs not.
- **Attachments:** The number of email attachments that are unique or duplicates of another email attachment in the review set.
- **Number documents by file type:** The number of files, identified by file extension.
- **Documents by source:** A summary of content by its original data source.
- **Documents aggregated by process:** A summary of content by review set processes.