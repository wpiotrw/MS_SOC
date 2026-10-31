---
layout: Conceptual
title: Manage investigation scopes in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-scope
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to manage investigation scopes in Data Security Investigations. Access, filter, and prepare data for AI analysis with step-by-step guidance.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 1dab564f-712b-9593-0b83-f6f874e5be7c
document_version_independent_id: 1dab564f-712b-9593-0b83-f6f874e5be7c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-scope.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-scope
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-scope.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 1ac67201-e9e3-af89-029b-e08a9777a469
---

# Manage investigation scopes in Data Security Investigations | Microsoft Learn

After you add data items from your [search queries](data-security-investigations-search) to the scope of the investigation, you can start working with your data and validate items before preparing for AI analysis. You can add items to an investigation scope by using any of the following search tools:

- [Query builder](data-security-investigations-search#query-builder): Search by keywords, file types, and conditions.
- [Audit search](data-security-investigations-search#audit-search): Identify content based on user activities in the unified audit log.
- [Endpoint DLP](data-security-investigations-search#endpoint-dlp-evidence-collection-preview): Query data captured by endpoint data loss prevention policies.

An investigation scope contains all the data items from your search results that you want to analyze and review. Analysts in your organization can now access this data for AI preparation and further review.

## Access the investigation scope

Select **Analysis** from the navigation options at the top of any page within a specific investigation to access the investigation scope. The investigation scope includes a dashboard of scoped items and includes filter and viewer tools to help with item review.

## Investigation scope dashboard

The investigation scope dashboard lists all the scoped data items in an investigation. This dashboard allows you to review details about individual data items and displays information about each item.

The investigation scope dashboard contains the following information and controls:

- **Subject/Title**: The subject or title of the data item.
- **Exclude**: The exclude status of a data item. Values are *Yes* or blank.
- **Vectorized**: The vectorization status of a data item. Values are *Yes* or blank.
- **Date**: The date and time the data item was last modified.

To customize the columns display on the investigation scope dashboard, select **Customize columns** to choose the columns to display or drag and drop the columns in the list to reorder.

To download the list of data items and the column information, select **Download list** to create a .csv file containing this information.

### Grouping data items

When you view a large list of data items in an investigation, it's often helpful to group the investigation scope by family or conversations and related items. Select **Group** to group data items by this criteria.

## Review data items

To view detailed information about individual data items, select the item in the investigation scope dashboard or use **Filters** to narrow items based on specific attributes.

### Filter items

Filters are automatically created based on the data items you add to the scope of the investigation. Typical filter options include attributes such as *Author*, *File class*, *Location name*, *Native file extension*, *Sender*, and many more.

Expand a filter area and select one or more filters to refine the data items included in the investigation scope dashboard view. Each filter attribute lists the total number of data items matching the attribute.

For example, to view only email and email attachments, expand the **File class** filter and select the **Email** and **Attachment** filters. The displayed data items are automatically filtered by the selected attributes.

### View item details

Select a data item to display more information about the item. Use the [investigation scope viewers](data-security-investigations-scope-views) to examine source, plain text, metadata, and audit details for the selected item.

### Item actions

For each data item, you can choose to exclude the item from AI analysis, add the item to your mitigation plan, or purge the item from its source location. Select **Actions** on the command bar for these options. To purge items directly from the investigation scope, see [Purge a single item](data-security-investigations-mitigation-actions#purge-a-single-item). To purge items by using a search query, see [Purge items with a search query](data-security-investigations-mitigation-actions#purge-items-with-a-search-query). Review and exclude any redundant items for your investigation, such as system generated emails or meeting invites. Reducing redundant data in your investigation helps reduce data preparation time and improves overall AI insight quality.

All data items in the investigation scope are prepared for AI analysis unless you explicitly exclude them. You can change the status of any excluded data item later if you want to have the data item processed for AI analysis.

## Automatic vectorization

After you add data items to the investigation scope, the system automatically prepares all items for AI analysis. This automatic vectorization process runs in the background during each **Add to scope** action and enables you to use AI-based categorization and examination tools on these items. Automatic data preparation utilizes the latest Azure OpenAI [embedding models](/en-us/azure/ai-services/openai/concepts/models#embeddings) to help improve the cost and performance of your AI results.

Automatic data preparation doesn't require many compute units, even for larger amounts of data included in an investigation scope. The system doesn't revectorize previously vectorized items. The system doesn't vectorize items that don't contain text. Some examples of these items include:

- Calendar notifications
- Meeting invites

You can see the Add to scope processing status of data items at the top of the investigation analysis page. Depending on the amount of scoped data, Add to scope can take some time to complete. If you need to cancel an in-progress **Add to scope** job, select **Cancel** on the **Analysis** tab. You still pay for any compute units consumed before the cancellation. For more information about billing, see [Billing in Data Security Investigations](data-security-investigations-billing).

## Existing investigations with unvectorized data

Starting June 2026, all new investigations automatically vectorize data when items are added to the investigation scope. The **Prepare for AI** action is no longer needed or available for new investigations created after this date.

For investigations created before June 2026, the following transition applies:

- **June–August 2026**: Existing investigations that already have scoped data retain the **Prepare for AI** experience. You can continue to use **Prepare for AI** to vectorize data in these investigations during this transition period.
- **After August 2026**: The **Prepare for AI** action is removed from all investigations. All existing investigations will vectorize data automatically during the Add to scope process. If you have an existing investigation with data that was never prepared for AI, you must rerun **Add to scope** to trigger automatic vectorization for those items.

Important

Rerunning **Add to scope** on previously scoped data doesn't create duplicate copies or incur additional storage charges. The system recognizes data that is already stored and only initiates the vectorization process for items that haven't been prepared yet.