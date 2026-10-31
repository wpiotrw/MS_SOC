---
layout: Conceptual
title: Analyze data in a review set in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-analytics
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the tools available to analyze documents and email in review sets in Microsoft Purview eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-29T00:00:00.0000000Z
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
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 7ad139ee-acea-9c30-fb4c-46eb2dc33e0b
document_version_independent_id: 7ad139ee-acea-9c30-fb4c-46eb2dc33e0b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-analytics.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-analytics
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-analytics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: aabbf6ab-19f0-41aa-9c01-858b79459de8
---

# Analyze data in a review set in eDiscovery | Microsoft Learn

When you collect a large number of documents, it can be difficult to review them all. eDiscovery provides tools to analyze the documents so you can reduce the number of documents to review without losing any information. eDiscovery analysis tools also help you organize the documents in a coherent manner. For more information about these capabilities, see:

- [Near duplicate detection](edisc-settings-search-analytics#near-duplicate-detection)
- [Email threading](edisc-settings-search-analytics#email-threading)
- [Themes](edisc-settings-search-analytics#themes)

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Run analytics for a review set

To analyze data in a review set, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, and then select **Cases** in the left navigation.
3. Select a case.
    1. (Optional) select **Case settings**.
    2. On **Case settings**, select **Search & analytics**.
    3. On **Search & analytics**, configure [analytics settings](edisc-settings-search-analytics) for your case.
    4. After selecting the applicable search and analytics options, select **Save**. Close **Case settings**.
4. Select the **Review sets** tab.
5. Select a review set, then select the **All items** tab.
6. Select **Analytics** &gt; **Run document & email analytics**.
7. A notification dialog appears about the time it takes to complete the analytics process. Select **Yes** to continue with running the analytics process or select **Cancel**.
8. Select **OK** when notified that the analyze process is created.

You can check the progress of the analysis process by selecting **Process manager** in the review set. The process type is *Run analytics*.

After the analysis process completes, you can view the analytics report, [run queries](edisc-review-set-search) within your review set on outputs of the analysis, and see related documents of a given document.

## Use the For Review (preview) filter query

After running analytics for the review set, use an automatically generated filter query (called *For Review*) to filter your review. This query excludes immaterial, duplicate, or noninclusive items. The For Review filter query leaves you with only the items that are representative, unique, and inclusive in the review set.

To apply the **For Review - Unique items only (preview)** filter query to a review set, select the **Saved filter queries** dropdown list, and then select **[AutoGen] For Review - Unique items only (preview)**. Minimize the query details to view the results.

Here's the syntax for the **For Review - Unique items only (preview)** filter query in Keyword Query Language (KeyQL) format:

`(((FileClass=“Email”) AND (IsInclusive=“True”) AND (MarkAsRepresentative=“Unique”)) OR ((FileClass=“Attachment”) AND (MarkAsRepresentative=“Unique”)) OR ((FileClass=“Document”) AND (MarkAsRepresentative=“Unique”)) OR ((FileClass=“Conversations”) AND (MarkAsRepresentative=“Unique”)) OR ((FileClass=“Attachment” OR FileClass=“Conversations” OR FileClass=“Document” OR FileClass=“Email”) AND  isempty (MarkAsRepresentative)))`

The following list describes the result of the For Review - Unique items only (preview) filter query in terms of what content is displayed after you apply it to the review set.

- **Email**: Displays items that are marked as both **Inclusive** and **Representative**. An email is marked as IsInclusive True when it contains all the unique content from a thread, including all previous replies. It ensures that only the most comprehensive email in a thread is reviewed, which is essential for understanding the full context of the conversation without having to review each individual reply. An email is MarkedAsRepresentative Unique when it's the single representative copy among duplicates.
- **Attachments**: Filters out duplicate attachments in the review set. Only attachments that are unique in the review set are displayed.
- **Documents**: Filters out duplicate documents. Only documents that are unique in the review set are displayed.
- **Teams conversations**: Filter out duplicate Teams (and Viva Engage) conversations. Only conversations that are unique in the review set are displayed.
- **Other**: Any emails, attachments, documents, and conversations in the review set where the *MarkedAsRepresentative* field doesn't contain a value. The empty value means that analytics wasn't able to generate a value, so you should review and assess these items.

For more information about inclusive types and document uniqueness, see [Email threading in eDiscovery](edisc-settings-search-analytics#email-threading).

## Use the Potentially Immaterial Items filter query

The potentially immaterial query is designed to filter out specific types of files that could be immaterial in a review set. It targets two main categories:

1. Compressed files. It filters out files with extensions commonly associated with compressed or archived formats, such as .zip.
2. Small image files. It filters out image files that are smaller than 3,072 bytes (3 KB). These small image files are typically thumbnails, icons, or low-resolution images.

To apply the **Potentially Immaterial Items** filter query to a review set, select the **Saved filter queries** dropdown list, and then select **[AutoGen] Potentially Immaterial Items**. Minimize the query details to view the results.

## View the analytics report

To view the analytics report for a review set, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, and then select **Cases** in the left navigation.
3. Select a case, then select the **Review sets** tab.
4. Select a review set, select the **All items** tab.
5. Select **Analytics** &gt; **Show reports**.

The **Analytics** report has seven components from the analysis. Hover over the results to view counts for each component:

- **Target population:** The number of email messages, attachments, and loose documents found in the review set.
- **Documents (excluding attachments):** The number of loose documents that are pivots, unique near duplicates of a pivot, or an exact duplicate of another document.
- **Emails:** The number of email messages that are marked as *inclusive*.
- **Attachments:** The number of email attachments that are unique or duplicates of another email attachment in the review set.
- **Number documents by file type:** The number of files, identified by file extension.
- **Documents by source:** A summary of content by its original data source.
- **Documents aggregated by process:** A summary of content by review set processes.