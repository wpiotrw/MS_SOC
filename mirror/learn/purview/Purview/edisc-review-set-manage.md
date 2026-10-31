---
layout: Conceptual
title: Manage review sets in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-manage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to analyze, organize, annotate, and redact items in review sets in eDiscovery for your cases.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-02T00:00:00.0000000Z
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
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 2c1871a3-190d-0575-b9d9-e6dbbf3f7310
document_version_independent_id: 2c1871a3-190d-0575-b9d9-e6dbbf3f7310
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-manage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 86d7e9de-6baf-f072-412b-d2c1a6cd10b1
---

# Manage review sets in eDiscovery | Microsoft Learn

Review sets are a static set of documents where you can analyze, query, view, tag, and export data in a case. To view all review sets in a case, select the **Review sets** tab. You can't delete items from a review set, and you can't delete review sets from a case. To delete a review set and its data, you must delete the eDiscovery case that contains the review set.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Review set summary page

The **Review sets** dashboard lists all the review sets in a case. This dashboard lets you create review sets and displays information about review sets in the case. You can filter and group the review sets. The **Review sets** dashboard contains the following information and controls:

- **Review set**: The name of the review set.
- **Size**: The total file size of the items contained in the review set.
- **Created by**: The user that created the review set.
- **Last modified**: The date and time the review set was last modified. Select **Time zone** to switch between using local time and Coordinated Universal Time (UTC).
- **Modified by**: The user that modified the review set.
- **Searches (sources)**: The number of search sources contained in the review set.
- **Exports**: The number of exports from the review set.
- **Description**: The description information for the review set.

To customize the columns display on the **Review sets** dashboard, select **Customize columns** to choose the columns to display or drag and drop the columns in the list to reorder. To search for a specific review set, enter a keyword in the **Search** field.

To download the list of review sets and the column information, select **Download list** to create a .csv file containing this information.

### Grouping review sets

When you view a large list of review sets in a case, group the review sets by user information. Select **Group** to group review sets by the following parameters:

- **None**: Review sets aren't grouped on the **Review sets** dashboard.
- **Modified by**: Review sets are grouped by the *Modified by* values.
- **Created by**: Review sets are grouped by the *Created by* values.

## Review set management

To open a review set and start working with review set items, select the review set. The review set opens and contains the following tabs and information to help you manage the review set.

### All items

Important

Review sets for [limited format](edisc-cases-manage#limited-format-cases) cases use the legacy eDiscovery experience. Some features aren't available for these cases in the new eDiscovery experience.

After selecting a review set, you're ready to start working with the items contained in the review set. On the **All items** tab, use the controls on the command bar to take the following actions in the review set:

- [Search content with the condition builder in a review set](edisc-review-set-search). Use the condition builder for visual, no-code filtering with standard conditions like keywords, dates, senders, and file types.
- [Search content with the Advanced review set explorer (preview)](edisc-review-set-explorer). Use the Advanced review set explorer (preview) for KQL-based queries that support complex filtering, aggregation, pattern matching, and data visualization.
- [Group and view items in a review set](edisc-review-set-view)
- [Tag documents in a review set](edisc-review-set-tagging)
- [Run analytics on a review set](edisc-review-set-analytics)
- [Export items from a review set](edisc-review-set-export)
- [Add items from a review set to another review set](edisc-review-set-add-to-other-review-set)
- [Use the Query Report to create keyword reports for KeyQL queries (preview)](edisc-review-set-query-report)

Tip

Do you prefer an interactive configuration guide experience? Check out the [Create and manage review sets](https://mslearn.cloudguides.com/guides/Create%20and%20manage%20review%20sets%20with%20Microsoft%20Purview%20eDiscovery) guide.

#### Review set overview

Select **Overview** to display summary information about the review set:

- **Total extracted documents**: The total number of items added to the review set. This number indicates the sum of parent items and child items added to the review set.
- **Total processed items**: The total number of processed items added to the review set.
- **Total number of failed extracted documents**: The total number of documents that failed extraction to the review set.

#### Pagination

Pagination for review set items is enabled by default in review sets. When pagination is enabled, review set items are displayed as multiple pages of 50 items each. To view specific pages, use the forward and back controls to navigate pages or enter a specific page number. To disable automatic pagination, select **Manage** &gt; **Turn pagination off**.

### Advanced review set explorer (preview) tab

The **Advanced review set explorer (preview)** tab provides a Kusto Query Language (KQL) editor for running advanced queries directly against review set data. Use this tab for complex filtering, aggregation, pattern matching, and data visualization.

For detailed guidance, see [Search content in a review set with the Advanced review set explorer (preview)](edisc-review-set-explorer).

### Dashboard (preview) tab

The **Dashboard tab** provides a visual experience to help you quickly understand the composition and trends within the review set. You don't need to create custom queries because the dashboard automatically creates interactive charts and summaries.

Note

The dashboard doesn't render if the review set is empty. Ensure the review set contains data before using the dashboard.

#### Summary cards

Summary cards provide at-a-glance metrics for:

- Total items in the review set
- Items by type (conversation vs documents)
- Items breakdown by analytics results (items to review excluding duplicates, or immaterial items) if analytics has been run.

#### Interactive charts

Visualize review set data by using the following charts:

- **Top Communication Participants**: Senders or recipients for emails, [Teams chats](edisc-review-set-teams-data), and calendar invites in Exchange locations.
- **Top Data Sources**: Data sources that make up the most search hits matching your query.
- **Top item classes**: Top item classes that make up search hits matching your query.
- **Top file extension**: Top file extensions that make up search hits matching your query.

### Process manager

Select **Process manager** to display information about processes performed on the review set. For example, if you export data from the review set, an *Export* process appears as an item in the **Process manager** list.

- **Process type**: The type of process.
- **Status**: The status of the process.
- **Export name**: The name of the export. For non-export process types, this value is blank.
- **Created**: The date and time the process was created.
- **Completed**: The date and time the process was completed.
- **Duration**: The duration of the process.
- **Created by**: The user that created the process.

To download the list of processes and the column information, select **Download list** to create a .csv file containing this information.

To view information about all eDiscovery processes, see [Use the Process report in eDiscovery](edisc-process-report).