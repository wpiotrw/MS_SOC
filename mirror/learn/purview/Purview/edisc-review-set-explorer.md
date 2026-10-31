---
layout: Conceptual
title: Search content in a review set with the Advanced review set explorer (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-explorer
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use the Advanced review set explorer to query review set data with Kusto Query Language (KQL) in Microsoft Purview eDiscovery.
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
document_id: f84cf8b2-489b-5aec-1f3b-f34b85249358
document_version_independent_id: f84cf8b2-489b-5aec-1f3b-f34b85249358
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-explorer.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-explorer
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-explorer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 46a88617-f365-a8a0-da23-05d45209acc3
---

# Search content in a review set with the Advanced review set explorer (preview) | Microsoft Learn

The **Advanced review set explorer (preview)** in [Microsoft Purview eDiscovery](edisc) lets reviewers run real-time big data analytics on review set content by using a defined subset of Kusto Query Language (KQL). With the Advanced review set explorer (preview), you can query, filter, and visualize review set data directly in the Microsoft Purview portal without modifying the underlying content. Queries run against the full set of indexed items and return either tabular results or chart visualizations.

Use the Advanced review set explorer (preview) to:

- Identify top item types, spot patterns, and find trends within the review set.
- Build powerful queries with complex filtering, pattern-based text extraction, and data format parsing.
- Analyze and find key information specific to your case or organization.
- Visualize query results by using charts for a comprehensive understanding of review set data.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Open the Advanced review set explorer (preview)

To open the Advanced review set explorer (preview), complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned [eDiscovery permissions](edisc-permissions).
2. Select the **eDiscovery** solution card, and then select **Cases** in the left navigation.
3. Select a case, and then select the **Review sets** tab.
4. Select a review set, and then select the **Advanced review set explorer (preview)** tab.

From here, you can write and run KQL queries directly against the review set data.

Tip

If you prefer a visual, no-code approach to filtering review set content, see [Search content in a review set with the query condition builder](edisc-review-set-search).

## Navigate the Advanced review set explorer (preview)

The Advanced review set explorer (preview) includes a left navigation pane and a results area to help you build, discover, and run KQL queries.

Tip

If you're new to KQL, start with the **Getting started** tab to explore basic query patterns, then use the **Sample queries** in the left pane for more targeted analysis.

### Left navigation pane

The left navigation pane provides three collapsible sections that let you explore the review set schema and quickly insert query elements into the editor:

- **Schema**: Displays the available table (`ReviewSetTable`) for your review set. Select the table name to insert it into the query editor.
- **Operators**: Lists all supported KQL operators, including `count`, `distinct`, `extend`, `limit`, `mv-expand`, `order`, `project`, `project-away`, `project-keep`, `render`, `sort`, `summarize`, `take`, `top`, and `where`. Select any operator to add it to your query.
- **Sample queries**: Provides ready-to-use query templates for common review set analysis tasks, such as **FileClass count as piechart**, **FileType count**, **ItemClass count**, **Participants count**, **SensitivityLabel count**, and **Source count**. Select a sample query to load it directly into the query editor.

### Getting started tab

The **Getting started** tab below the query results area provides a quick reference for building queries. It includes selectable examples organized into two categories.

Select any query name to load the example directly into the query editor:

| Category | Queries | Description |
| --- | --- | --- |
| **Basic queries** | **Limit** | Shows 10 results from the specified table. |
|  | **Where** | Filters the result set by date and file names ending with ".jpg". |
|  | **Count** | Counts the number of rows that match the specified filter. |
|  | **Top** | Arranges results by date and shows the first 10 rows. |
|  | **Project** | Shows only the file name, file type, and date columns in the results. |
| **Advanced queries** | **Summarize** | Shows the top data sources and counts the number of items for each source. |
|  | **Extend** | Adds a column to combine title and author values. |
|  | **Mv-expand** | Expands the Participants list and counts occurrences per participant. |
|  | **Render** | Counts items by file class and renders the results as a pie chart. |

## How the Advanced review set explorer (preview) works in a review set

Each query runs against the full review set’s data and returns:

- A **tabular list** of matching items, or
- A **chart visualization**, depending on the query.

Queries follow standard KQL pipeline syntax, where each line builds on the results of the previous step. The portal automatically adds the `ReviewSetTable` table name as the first line. Each subsequent query line must start with `\|`.

For example:

```kusto
ReviewSetTable
| where SubjectTitle has "Case"
| summarize count() by FileClass
```

Note

All queries in the Advanced review set explorer (preview) run against the current review set’s indexed items. You don't need to specify a table name. The review set acts as the default data source.

### Best practices

Use the following best practices when writing queries in the Advanced review set explorer:

- Start with `where` filters to narrow data before using `summarize` or `render`.
- Use `take` to validate query logic before running full aggregations.
- Avoid overly broad regex patterns on large review sets.
- Use `where isnotempty(`*ColumnName*`)` to exclude items with empty values for a property, which helps avoid unexpected blank rows in your results.

### Other considerations

The Advanced review set explorer (preview) doesn't support all Kusto operators and properties. Keep the following considerations in mind when you create queries:

- Queries are read-only and don't modify review set content. For more information about working with review sets, see [Manage review sets in eDiscovery](edisc-review-set-manage).
- Results reflect the current indexed state of the review set. If you add more data to the review set, the query might return different results.
- Not all file types are queryable. For more information, see [Supported file types in eDiscovery](edisc-ref-supported-file-types).
- If the query returns more than 10,000 results, it returns only the first 10,000 results. Modify the query to narrow down the results.

For Kusto syntax and references, see the following articles:

- [Syntax conventions for reference documentation](/en-us/kusto/query/syntax-conventions)
- [Best practices for Kusto Query Language queries](/en-us/kusto/query/best-practices)

## Supported basic operators

Tip

For a complete list of available properties you can use in queries, see [Document metadata fields in eDiscovery](edisc-ref-document-metadata-fields).

### Where operator

Use the `where` operator to filter items based on metadata such as subject, keywords, item class, dates, or participants.

The following example filters the review set to return only items whose **Subject** contains the text "Day".

```kusto
ReviewSetTable
| where SubjectTitle has "Day"
```

This query filters the review set to include all calendar-related items whose **ItemClass** begins with `IPM.Appointment`, which covers standard appointments and extended classes like `IPM.AppointmentSnapshot.SkypeTeams.Call`.

```kusto
ReviewSetTable
| where ItemClass startswith "IPM.Appointment"
```

### Project operator

Use `project` to return only the properties you care about. For example, the following query performs two actions:

- **Filters items by subject text**: The `where SubjectTitle has "Day"` clause limits the results to only those items whose **SubjectTitle** contains the word "Day".
- **Projects a single column**: The `project SubjectTitle` clause then returns only the **SubjectTitle** property for those filtered items, removing all other columns from the output.

```kusto
ReviewSetTable
| where SubjectTitle has "Day"
| project SubjectTitle
```

### Project-away operator

The `project-away` operator removes specified columns from the query results while keeping all other columns. Use it when you want to exclude a few properties rather than listing every column you want to keep.

The following example returns all properties for items in the review set except **CompoundPath** and **InternetMessageId**, which are excluded from the output.

```kusto
ReviewSetTable
| where SubjectTitle has "Day"
| project-away CompoundPath, InternetMessageId
```

### Project-keep operator

The `project-keep` operator keeps only the columns that match a specified pattern or list, removing everything else. Unlike `project`, `project-keep` preserves the original column order and supports wildcard patterns.

The following example keeps only columns whose names start with "Sender" or "Recipient", making it easy to focus on communication participants without listing each property individually.

```kusto
ReviewSetTable
| where SubjectTitle has "Day"
| project-keep Sender*, Recipient*
```

### Mv-expand operator

The `mv-expand` operator expands multi-value properties (such as lists of participants or recipients) into separate rows, with one row per value. This is useful for analyzing individual entries within fields that contain multiple values.

The following example expands the **Participants** field so each participant appears on its own row, then counts the number of items associated with each participant. This helps identify the most active participants in the review set.

```kusto
ReviewSetTable
| mv-expand Participants
| summarize count() by tostring(Participants)
```

### Extend operator

The `extend` operator adds one or more calculated columns to your query results by creating new values derived from existing fields without altering the underlying data.

The following example classifies review set items into four size categories - **Small (&lt;1MB)**, **Medium (1–5MB)**, **Medium-Large (5–10MB)**, and **Large (&gt;10MB)** - by creating a new column `SizeCategory` using the `case()` function, and then aggregates the count of items in each category by using `summarize`. It helps investigators quickly understand the distribution of file sizes in the review set for risk assessment or prioritization.

```kusto
ReviewSetTable
| extend SizeCategory = case(Size > 10485760, "Large (>10MB)", Size >= 5242880 and Size <= 10485760, "Medium-Large (5–10MB)", Size >= 1048576 and Size < 5242880, "Medium (1–5MB)", "Small (<1MB)")
| summarize count() by SizeCategory
```

### Summarize operator

The `summarize` operator aggregates data by applying functions like `count()`, `sum()`, or `avg()`, and groups results based on specified columns.

The following example counts items grouped by **SubjectTitle** for items containing the word "Day".

```kusto
ReviewSetTable
| where SubjectTitle has "Day"
| summarize count() by SubjectTitle
```

### Render barchart, render columnchart, render piechart

The `render barchart` operator takes the tabular results of your query and displays them as a bar chart. This makes it easier to visualize the distribution or comparison of aggregated values.

The following example renders subject title counts as a bar chart.

```kusto
ReviewSetTable
| where SubjectTitle has "Day"
| summarize count() by SubjectTitle
| render barchart
```

### Take (limit) operator

The `take` operator limits the query output to a specified number of rows. It returns only the first *n* results from the dataset. The `limit` operator is a synonym for `take` and you can use them interchangeably.

The following example returns just the first 10 matching items, so you can validate query logic or spot-check content before running a full query. This approach helps when dealing with large review sets or complex filters, where results can take longer to compute and load without `take` limiting the output.

```kusto
ReviewSetTable
| where SubjectTitle has "day"
| project SubjectTitle, SenderDomain, Custodian, Size
| take 10
```

### Sort operator

The `sort` operator orders the query results based on one or more specified columns in ascending or descending order.

The following example query calculates the total number of items for each **NativeFileExtension** in the review set by using `summarize count()`. Then, it sorts those extension groups in descending order of item count so you can see which file types are most prevalent.

```kusto
ReviewSetTable
| summarize ItemCount = count() by NativeFileExtension
| sort by ItemCount desc
```

### Distinct operator

The `distinct` operator returns unique values for the specified columns by removing duplicate rows from the query results.

The following example uses `distinct` to remove duplicates so you only see unique custodians, and then uses `sort by Custodian asc` to order them alphabetically, making it easy to scan or export for reporting.

```kusto
ReviewSetTable
| distinct Custodian
| sort by Custodian asc
```

### Count operator

The `count` operator returns the total number of rows in the query result set, so you can quickly see how many items are in the set.

The following example counts the number of unique subject titles that contain the word "Day".

```kusto
ReviewSetTable
| where SubjectTitle has "Day"
| summarize by SubjectTitle
| count
```

### Top operator

The `top` operator returns the first *n* rows from the query results, ordered by one or more specified columns. Use it to get the highest or lowest values based on your sort criteria.

The following example gets the top five largest items in your review set.

```kusto
ReviewSetTable
| top 5 by Size desc
```

### Bin operator

The `bin()` function rounds a datetime or numeric value down to the nearest multiple of a specified bin size. Use this function to group data into time intervals or numeric ranges, such as hourly buckets or size ranges.

The following example groups items in the review set into size buckets of **1 MB** using `bin(Size, 1048576)`, counts how many items fall into each bucket with `summarize count()`, and then sorts the buckets in ascending order so you can see the distribution of file sizes from smallest to largest.

```kusto
ReviewSetTable
| summarize ItemCount = count() by bin(Size, 1048576)
| sort by bin(Size, 1048576) asc
```

## Common scenarios

The following scenarios demonstrate how Kusto queries in the Advanced review set explorer (preview) can help you analyze and better understand your review set data.

### Scenario 1: Communications between two users

Find items exchanged exclusively between two specific users - John and David - with no other participants. This query isolates their direct one-to-one communications and shows only three properties: subject title, sender, and recipients.

```kusto
ReviewSetTable
| where isnotempty(Participants)
| extend ParticipantEmails = extract_all(@"\<(\[^\>\]+)\>", tostring(Participants))
| extend ParticipantCount = array_length(ParticipantEmails)
| where ParticipantCount == 2
| where ParticipantEmails has "John@contoso.com" and ParticipantEmails has "David@contoso.com"
| project SubjectTitle, SenderAuthor, Recipients
```

### Scenario 2: Emails sent externally

Find all review set items that include at least one external recipient (outside your organization contoso.com), and list those external email addresses for each item.

```kusto
ReviewSetTable
| where isnotempty(Recipients)
| extend Emails = extract_all(@"\<(\[^\>\]+)\>", tostring(Recipients))
| mv-expand Email = Emails
| extend Email = tostring(Email)
| where Email !contains "@contoso.com"
| summarize ExternalRecipients = make_set(Email) by ImmutableId, SubjectTitle
```

### Scenario 3: Identify date and time patterns in the review set

Visualizing data over time helps investigators identify spikes or anomalies in communication or document creation, such as a sudden surge in emails that might correlate with a known incident. Quarterly views align with business cycles, making it easier to correlate findings with financial reporting periods, internal audits, or policy changes.

The following example analyzes how review set items are distributed over time by grouping items by year and quarter and visualizing the results as a column chart. It filters items by date range, extracts the year and quarter from each item's **Date** field, counts the items in each year-quarter combination, creates a readable label (for example, *Q2 2024*), and renders the results as a column chart.

```kusto
ReviewSetTable
| where Date > datetime(2015-01-01) and Date < datetime(2025-08-31)
| extend Year = datetime_part("year", Date), Quarter = datetime_part("quarter", Date)
| summarize EventCount = count() by Year, Quarter
| sort by Year asc, Quarter asc
| extend QuarterLabel = strcat("Q", tostring(Quarter), " ", tostring(Year))
| project QuarterLabel, EventCount
| render columnchart
```

### Scenario 4: Visualize Microsoft Teams message types in the review set

The following example categorizes and visualizes Microsoft Teams message types in the review set by item class, helping you understand the distribution of different message formats.

```kusto
ReviewSetTable
| where ItemClass startswith "IPM.SkypeTeams.Message."
| project SubjectTitle, Date, SenderAuthor, FileClass, ItemClass, InternetMessageId
| summarize ItemCount = count() by ItemClass
| sort by ItemCount desc
| render piechart
```

## Use regex in the Advanced review set explorer (preview)

The Advanced review set explorer (preview) supports **regular expressions (regex)** for powerful pattern matching in text fields. Regex support enables you to search for complex sequences of characters, such as alphanumeric combinations, special characters, or structured patterns, beyond simple keyword matching. Use regex to:

- Identify items with specific formats, such as IDs, codes, or structured tokens.
- Detect patterns that standard operators like `has` or `startswith` can't capture.
- Perform advanced filtering for compliance or forensic investigations.

### Tips for writing regex in KQL

- Escape backslashes properly (`\\`) when needed.
- Use anchors (`^` for start, `$` for end) for exact positioning.
- Test patterns incrementally to avoid overly broad matches.
- Combine with other operators (for example, `and`, `or`) for precise queries.
- Reference: [Regex syntax](/en-us/kusto/query/regex).

### Syntax

Use the `matches regex` operator in your `where` clause:

```kusto
where <PropertyName> matches regex "<pattern>"
```

### Example: Match a complex pattern in Keywords

The following query finds items whose **Keywords** field matches a pattern of 10 word characters, 10 digits, and 10 non-word characters:

```kusto
ReviewSetTable
| where Keywords matches regex "\\w{10}\\d{10}\\W{10}"
| project SubjectTitle, CompoundPath, Date, SenderAuthor, FileClass, ItemClass, InternetMessageId
```

- Filters items where the **Keywords** property contains:

    - 10 word characters (`\w`)
    - followed by 10 digits (`\d`)
    - followed by 10 non-word characters (`\W`)
- Returns key metadata fields as specified for review.

## Fix common KQL syntax errors

When you create queries in the Advanced review set explorer (preview), you might encounter syntax errors.

The following table lists common errors and how to fix them:

| Error | Cause | Fix |
| --- | --- | --- |
| `sort` operator requires a column name | Using `sort` without specifying what to sort by. | Add a column name after `sort by`. For example, `sort by Date desc`. |
| Expected `)` or `,` | Missing closing parenthesis or incorrect function arguments. | Check that all opening parentheses have matching closing parentheses and that function arguments are separated by commas. |
| Unknown function | Using a function name that isn't supported or is misspelled. | Verify the function name against the [KQL documentation](/en-us/kusto/query/syntax-conventions). Common examples include `count()`, `tostring()`, and `datetime()`. |
| Token expected: `\ | ` | A query line is missing the pipe operator at the start. | Ensure every line after `ReviewSetTable` begins with `\ | `. |
| Column not found | Referencing a property name that doesn't exist in the review set schema. | Check the available column names in your review set. Property names are case-sensitive. |
| `summarize` requires a `by` clause | Using `summarize` with an aggregation but no grouping column. | Add a `by` clause with one or more columns. For example, `summarize count() by FileClass`. |
| Unexpected end of query | Query is incomplete or has a trailing pipe with no operator. | Remove any trailing `\ | ` at the end of the query, or add the intended operator after it. |

Note

Some older review sets might not support certain KQL properties if those properties weren't available when the review set was created and data was generated. Querying an unsupported property in an older review set results in a column not found error. To resolve this error, create a new review set and use the **Add to review set** process to regenerate the data with the latest supported properties.