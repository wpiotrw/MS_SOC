---
layout: Conceptual
title: Search content in a review set with the query condition builder | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-search
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to create a search in a review set with the query condition builder to organize content in a Microsoft Purview eDiscovery.
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
document_id: 29cea5f6-367e-d416-102b-57daaf49a306
document_version_independent_id: 29cea5f6-367e-d416-102b-57daaf49a306
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-search.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-search.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 73b12e5c-7b62-fd01-99d3-e64989317211
---

# Search content in a review set with the query condition builder | Microsoft Learn

In most cases, it's useful to dig deeper into the content in a [review set](edisc-review-set-manage) and organize it to facilitate a more efficient review. By using filters and queries in a review set, you can focus on a subset of documents that meet the criteria for your review. This article explains how to use the query condition builder to create and run filter queries, work with condition types and load sets, use KeyQL query language, and save queries for reuse.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Use the query condition builder

To use the query condition builder in a review set, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select the **Review sets** tab.
4. Select a review set, then select the **All items** tab.
5. On the **All items** tab, select **Query**.
6. Add conditions as needed. For more information about using conditions, see [Use the condition builder to create search queries in eDiscovery](edisc-condition-builder).

## Query content in a review set

The eDiscovery review set provides a querying experience that you can use to build flexible queries for review sets. The querying experience enables you to:

- Quickly search for review set content matching certain conditions.
- Create complex queries by using *AND* or *OR* conditions in KeyQL.
- Manage saved filters without going to another area and easily change your queries by loading saved queries.

Important

Review sets have pagination turned on by default and can display a maximum of 1,000 items per page. Use default or custom filters to adjust the displayed items as needed. Matched item counts are estimates. You can turn off pagination through **Manage** &gt; **Turn pagination off**.

To query content in your review set, use the following controls:

- Select **Query** in the toolbar or the blue bubble above the toolbar. Any applied query also appears in the query bubble above the toolbar.
- **Keyword** condition automatically populates for any new query.
- **AND/OR**: These conditional logical operators enable you to select the query condition that applies to specific filters.
- **Add conditions**: Enables you to add multiple conditions to your query.
- **Select an operator**: Depending on the selected filter, the operators compatible with the filter are available to select. For example, if you select the *Date* filter, you see the available operators *Before*, *After*, and *Between*. If you select the *Size* filter, you see the available operators *Greater than*, *Greater or equal*, *Less than*, *Less or equal*, *Between*, and *Equal*.
- **Value**: Depending on the selected filter, the values compatible with the filter are available. Additionally, some filters support multiple values and some filters support one specific value. For example, if you select the *Date* filter, you select date values. If you select the *Size (in bytes)* filter, you select a value for bytes.
- **Clear a condition value:** To clear the value inside a condition, select the X to the right of each condition line.
- **Remove a filter condition**: To remove an individual filter or subgroup, select the **Delete** icon to the right of each condition line.
- **Clear all**: To clear the entire query of all conditions and their values, select **Clear all**.
- **Save**: Saves the current conditions into a saved query by giving it a name.
- **Load saved filters:** Saved filters allow you to load any saved queries and overwrite existing query that is built.
- **Run query:** For any manually built conditions or opened saved filters, select **Run query** to apply the query to the review set. The last run query is retained and is available the next time you open the review set, even after you exit.
- **Hide and show query**: Use the hide and show button to expand and collapse the query section.

## Understand condition types

Every searchable field in a review set has a corresponding condition that you can use to filter items based on a specific property.

There are multiple types of filters:

- **Free-text**: A free-text condition is applied to text fields such as *Subject*. You can list multiple search terms by separating them with a comma.
- **Date**: A date condition is used for date fields such as *Last modified date*.
- **Search options**: A search options condition provides a list of possible values (each value is displayed with a checkbox that you can select) for particular fields in the review. This condition is used for fields, such as *Sender*, where there's a finite number of possible values in the review set.

Note

Some search options let you enter free‑text to match multiple values. For example, when using the **Sender** condition with **contains any**, entering *john* matches items where the sender is *johndoe@contoso.com*, *johnsmith@contoso.com*, or *johnwei@gmail.com*. Make sure the entered value appears as a pill for the free‑text input to apply.

- **Keyword**: A keyword condition is a specific instance of free-text condition that you can use to search for terms. You can also use Kusto-like query language in this type of condition. For example user can type *red AND blue* in a keyword condition grid, run the query and get all items in the review set that has both the word "red" and the word "blue". The matched keywords are also highlighted in the **plain text** view in the preview pane.

## Use load sets to filter by collection

A load set is an instance of adding data to a review set. For example, if you add the results of two different searches to the same review set, each one represents a load set. To filter review set items by a specific load, use the **Load Id** condition in the query builder:

1. In the review set, select **+ Add conditions** in the query area.
2. Select **Load Id** as the condition.
3. Set the operator to **Equals any of**.
4. Start typing in the search field. Suggested load IDs from the review set appear automatically.
5. Select one or more load IDs to filter by, then run the query.

This filter is useful when you want to isolate items from a specific collection or compare data across different loads added to the same review set.

To download the list of load sets and the column information, select **Download list** to create a .csv file containing this information.

## Save and manage filter queries

After you build your conditions, save the condition combination as a filter query. This saved filter query lets you apply the same query in future review sessions.

To save, select **Save** and give it a name. You or other reviewers can run previously saved filter queries by selecting the **Saved filter** dropdown and selecting a filter query to open and select **Run query** to apply review set documents.

To edit or delete a saved filter query, select **Saved filter** and mouse over the saved filter and select **Edit** or **Delete** options for the saved filter query.

## Use query language support for KeyQL and Keyword filters

When you use the *[KeyQL](edisc-keyword-query-language)* or *Keyword* filters, you can use a Kusto-like query language to build your review set search query. The query language for the KeyQL and Keyword filters supports standard Boolean operators, such as **AND**, **OR**, **NOT**, and **NEAR**. It also supports a single-character wildcard (?) and a multi-character wildcard (\*).

Note

Review filters only support wildcards (? or \*) on a single term. Using wildcards in searches on phrases that consist of multiple terms isn't supported.

## Scenario examples

The following examples show common review set filtering scenarios using the query condition builder.

### Filter for untagged items in a review set

An eDiscovery administrator needs to create a query to find all items in the review set without any tagging applied. For this example, the administrator creates the following review set query:

1. For the first condition, the administrator selects *Add conditions* and searches for the *tag* condition. The *Tags* condition is displayed as a matching option. The administrator selects it and selects *Apply*.
2. The administrator then selects *Is empty* operator for the *Tags* condition.
3. The administrator selects *Run query*.

The review set list is updated to show all items that don't have any tags applied.

### Filter for native file type items in a review set

An eDiscovery administrator needs to create a query to find all items in the review set that are a certain type, such as .csv, .msg, or .pdf. For this example, the administrator creates the following review set query:

1. For the first condition, the administrator selects *Add conditions* and searches for the *file* in condition search. The condition *Native file extension* is one of the options displayed in the search results. The administrator selects it and selects *Apply*.
2. The administrator then selects the *Equals any of* operator.
3. The administrator selects the value box and chooses the file types in the dropdown such as csv to include in the query.
4. The administrator selects *Run query*.

The review set is updated and only the items that match the selected file types are displayed.

### Filter partially indexed items

If you select the option to include partially indexed items when you add the search to a review set, you probably want to identify and view those items. You can determine if an item might be relevant to your investigation and whether you need to fix the error that resulted in the item being partially indexed. Use the KQL (Keyword Query Language) condition to find partially indexed items.

1. Select **Add conditions** in the query building space.
2. Find the condition *KQL* and select **Apply**.
3. Keep the operator as *Equal* and type *AddedBy* in the KQL editor box. You can filter out items added to the review set by applying the KQL of `AddedBy=UnindexedQuery`.
4. Select **Run query**.

The review set is updated and only the items that match the partially indexed query are displayed.

### Filter documents by theme

Filtering documents by theme can save time when reviewing documents. For example, if you're looking for documents that discuss a particular subject, you can filter the documents by the dominant theme that relates to that subject. You can also filter documents by other themes in the theme list to find documents that are similar to a document that you're interested in. To display the themes for a document as a column in the document list for the review set, select **Customize columns** and select **Dominant theme** and **Themes list**.

To filter documents by theme, complete the following steps:

1. In a review set, add **Dominant theme** condition.
2. Select an operator to use with the **Dominant theme** and define the value to use with the operator.
3. Use an additional **Themes list** condition and the operator and values to apply to this filter. You can configure the **AND** and **OR** operators to filter documents by a combination of the **Dominant theme** and **Themes list** values.