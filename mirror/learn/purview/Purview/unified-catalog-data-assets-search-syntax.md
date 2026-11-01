---
layout: Conceptual
title: Keyword search syntax | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-assets-search-syntax
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2026-04-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
ai-usage: ai-assisted
description: Learn about keyword search syntax, operators, and field-scoped search for finding data assets in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 6cb28a78-a5e1-762a-82d5-ffc5c23bd5af
document_version_independent_id: 6cb28a78-a5e1-762a-82d5-ffc5c23bd5af
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-assets-search-syntax.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-assets-search-syntax
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-assets-search-syntax.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 1890408a-2675-8060-ce4b-1f4d7df9890e
---

# Keyword search syntax | Microsoft Learn

When you search for data assets, you can use keywords, operators, and field-scoped queries to find exactly the data you need. This article describes the supported query syntax so you can build precise, effective searches.

For a general overview of searching and browsing for data assets, see [Search for data assets in Unified Catalog](unified-catalog-data-assets-search).

Note

The syntax described in this article applies to the **Unified Catalog &gt; Discovery &gt; Data assets** search experience in the [Microsoft Purview portal](https://purview.microsoft.com). Search results are filtered based on your permissions, so you only see assets you have access to. For more information about permissions, see [Search for data assets in Unified Catalog](unified-catalog-data-assets-search#permissions-to-search-the-unified-catalog).

## Quick reference

The following table summarizes the query syntax options available in Unified Catalog search.

| Syntax | Example | Description |
| --- | --- | --- |
| **Keyword** | `customer` | Search all fields for the keyword. |
| **Multiple keywords** | `customer sales` | Search for assets matching either word. Assets matching both words are ranked higher. |
| **AND** | `customer AND sales` | Both terms must be present. |
| **OR** | `customer OR sales` | Either term can be present. |
| **NOT** | `customer NOT draft` | Must contain first term, must not contain second. |
| **Exact phrase** | `"sales report"` | Match the exact phrase in order. |
| **Grouping** | `(A OR B) AND C` | Control evaluation order. |
| **Field search** | `name:customer` | Search only within a specific field. |
| **Match all** | `*` or empty | Return all assets. |

## Simple keyword search

A single keyword searches across all searchable fields in the catalog, including asset name, description, qualified name, schema columns, glossary terms, contacts, classifications, custom attributes, collections, domains, and sensitivity labels.

The following example returns any asset where `customer` appears in any searchable field:

```
customer
```

Results are ranked by relevance. An exact match on the asset name scores higher than a partial match in the description.

## Multiple keywords

When you enter multiple words separated by spaces without an explicit operator, the search returns assets that contain *any* of the words. Assets that contain more of the keywords are ranked higher in the results.

The following example finds assets that contain `customer`, `sales`, or both:

```
customer sales
```

Important

A space-separated keyword search is **not** the same as an AND search. Consider the following differences:

| Query | Behavior | Example result |
| --- | --- | --- |
| `customer sales` | Matches `customer` OR `sales`. Assets with both score higher. | An asset named "Sales Dashboard" matches even without "customer." |
| `customer AND sales` | **Both**`customer` AND `sales` must be present. | "Sales Dashboard" doesn't match unless it also contains "customer." |
| `"customer sales"` | The exact phrase `customer sales` must appear in that order. | Only matches if `customer` is immediately followed by `sales`. |

## Boolean operators

Boolean operators let you combine search terms with explicit logic. Operators must be written in uppercase (`AND`, `OR`, `NOT`).

### AND operator

Use the AND operator when all terms must be present in the matching assets. The terms don't need to be adjacent or in the same field.

```
customer AND sales
azure AND sql AND database
```

### OR operator

Use the OR operator when any of the terms can be present.

```
customer OR client
sales OR marketing OR operations
```

### NOT operator

Use the NOT operator to exclude assets that contain a specific term.

```
customer NOT draft
sales NOT internal NOT test
```

The following example returns assets that contain `customer` but don't contain `draft`:

```
customer NOT draft
```

### Combine operators

You can chain operators in a single query:

```
customer AND sales NOT draft
```

This query returns assets that contain `customer` and `sales`, but don't contain `draft`.

## Exact phrase search

Wrap your query in double quotes to search for an exact phrase. The words must appear in the specified order and adjacent to each other.

```
"sales report"
"customer data analysis"
```

The following table shows how phrase search differs from a keyword search:

| Query | Matches | Doesn't match |
| --- | --- | --- |
| `"sales report"` | "Q1 **sales report** summary" | "report on sales" (wrong order) |
| `"sales report"` | "Annual **sales report**" | "sales quarterly report" (words not adjacent) |

Use `sales report` (no quotes) when you want any asset that mentions `sales` or `report`. Use `"sales report"` (with quotes) when you want only assets that contain the exact phrase.

## Grouping with parentheses

Parentheses control the order of evaluation, just like in math expressions.

```
(customer OR client) AND sales
```

Without parentheses, operator precedence can produce unexpected results. The following examples show how parentheses change the query interpretation:

| Query | Interpretation |
| --- | --- |
| `(customer OR client) AND sales` | Assets that contain `customer` or `client`, and also contain `sales`. |
| `customer OR (client AND sales)` | Assets that contain `customer`, or assets that contain both `client` and `sales`. |

You can nest parentheses for more complex queries:

```
(A AND B) OR (C AND D) NOT E
((alpha OR beta) AND gamma) NOT delta
```

## Field-scoped search

By default, a keyword is searched across all fields. Field-scoped search lets you restrict the search to a specific field.

Use the syntax `fieldName:value` or `fieldName:"phrase value"`:

```
name:customer
classification:Confidential
entityType:azure_sql_table
contact:alice@company.com
name:"sales report"
```

### Supported fields

The following fields can be used with the `field:value` syntax:

| Field name | Description | Example |
| --- | --- | --- |
| `name` | Asset name | `name:customer` |
| `qualifiedName` | Fully qualified name | `qualifiedName:sales_db.customers` |
| `description` | Asset description | `description:quarterly` |
| `userDescription` | User-provided description | `userDescription:important` |
| `displayText` | Display text | `displayText:customer` |
| `entityType` | Entity type | `entityType:azure_sql_table` |
| `assetType` | Asset category | `assetType:Tables` |
| `classification` | Sensitivity labels or tags | `classification:Confidential` |
| `endorsement` | Endorsement status | `endorsement:Certified` |
| `glossaryType` | Glossary type | `glossaryType:AtlasGlossaryTerm` |
| `termStatus` | Term status | `termStatus:Approved` |
| `termTemplate` | Term template | `termTemplate:BusinessTerm` |
| `glossary` | Glossary name | `glossary:Finance` |
| `fileExtension` | File extension | `fileExtension:csv` |
| `term` | Assigned glossary terms | `term:Revenue` |
| `contact` | Owner or expert contact | `contact:john@company.com` |
| `abbreviation` | Term abbreviation | `abbreviation:ROI` |
| `objectType` | Object type | `objectType:Tables` |
| `tag` | Tags | `tag:important` |

Field names are case-insensitive. For example, `Name:customer` and `name:customer` produce the same results.

If you use a field name that isn't in the Supported fields table, the search engine doesn't return an error. Instead, it treats the entire expression as an unscoped keyword. For example, `alice AND report:myreport` searches for `alice` AND the literal text `report:myreport` across all fields, rather than restricting `myreport` to a field called `report`.

Important

Only one value token is captured after the colon. To search for a multiword value, use quotes:

| Query | Behavior |
| --- | --- |
| `name:sales report` | Searches `name` for `sales`, then separately searches all fields for `report`. |
| `name:"sales report"` | Searches `name` for the exact phrase `sales report`. |

### Nested fields

Some supported fields, such as `contact` and `term`, represent composite data with multiple properties. For example, a contact has a display name, an email address, and an ID.

You can't use dot notation to target a specific property. The system only recognizes the top-level field names listed in the Supported fields table.

| Query | Supported | Behavior |
| --- | --- | --- |
| `contact:Alice` | Yes | Searches across all contact properties (display name, email, ID). |
| `contact.displayName:Alice` | No | Not recognized as a field-scoped search. |
| `term:Revenue` | Yes | Searches across all term properties (name, glossary). |
| `term.name:Revenue` | No | Not recognized as a field-scoped search. |

Use the top-level field name. For example, `contact:Alice` searches across all contact properties and returns assets where any property matches.

### Combine keywords with field-scoped search

When you mix a plain keyword with a field-scoped search, a space doesn't imply AND. Space-separated clauses are treated as OR.

| Query | Behavior |
| --- | --- |
| `alice contact:bob` | `alice` OR contact contains `bob`. |
| `alice AND contact:bob` | `alice` AND contact contains `bob`. |

Tip

Always use explicit `AND` or `OR` operators when combining keyword search with field-scoped search.

## Match all results

An empty query or `*` returns all assets, subject to your permissions and any applied filters.

```
*
```

This option is useful as a starting point when you want to browse assets by using only filters and facets.

## Case sensitivity

Search is generally case-insensitive. Searching for `Customer`, `customer`, or `CUSTOMER` returns the same results.

However, the casing and special characters in your search query can affect the number of results returned. Certain fields are processed by the search engine, which splits terms at specific boundaries before matching.

### Token-splitting delimiters

The following boundaries cause a term to be split into separate tokens during both indexing and searching:

| Delimiter | Example input | Tokens produced |
| --- | --- | --- |
| Case change (lowercase to uppercase) | `CustomerOrder` | `customer`, `order`, `customerorder` |
| Underscore (`_`) | `customer_order` | `customer`, `order`, `customer_order` |
| Hyphen (`-`) | `customer-order` | `customer`, `order`, `customer-order` |
| Dot (`.`) | `customer.order` | `customer`, `order`, `customer.order` |
| Comma (`,`) | `item1,item2` | `item1`, `item2` |
| Colon (`:`) | `db:schema` | `db`, `schema` |
| Whitespace | `customer order` | `customer`, `order` |
| Letter-to-number transition | `version2release` | `version`, `2`, `release` |
| Number-to-letter transition | `2ndEdition` | `2`, `nd`, `edition` |

Note

Splitting is cumulative. A name like `Customer_Order_Details` is split at every underscore and at every case-change boundary within each segment, producing tokens such as `customer`, `order`, `details`, `customer_order`, and `order_details`.

### How casing affects results

When your search query contains mixed case (such as PascalCase or camelCase), the search engine splits it at case-change boundaries, producing multiple tokens. Each token is independently matched, which broadens the result set.

When your query is all lowercase, there are no case-change boundaries to split on, so it stays as a single token and must match as a contiguous string.

The following example illustrates the difference:

| Search query | Behavior | Effect on results |
| --- | --- | --- |
| `CustomerOrder` | Split into tokens: `customer`, `order`, `customerorder` | Matches assets containing `customer` or `order` or `customerorder`. Broader results. |
| `customerorder` | Stays as one token: `customerorder` | Matches only assets containing the contiguous string `customerorder`. Narrower results. |

### Phrase search and casing

Quoted phrase search also interacts with casing. With `"CustomerOrder"` in quotes, the query tokens are still `customer`, `order`, `customerorder`, but because it's a phrase search, the tokens must appear adjacent and in order.

| Phrase query | Matches | Doesn't match |
| --- | --- | --- |
| `"CustomerOrder"` | `CustomerOrder`, `FAC_Customer_OrderLine` (where `customer` and `order` are adjacent tokens) | `legacy customer database` (no adjacent `order` token) |
| `"customerorder"` | `CustomerOrder` (indexed as contiguous `customerorder`) | `FAC_Customer_OrderLine` (no contiguous `customerorder` token) |

### Recommendations for casing

- For the broadest results, use the natural casing of the term (for example, `CustomerOrder` or `SalesReport`). The case-change splitting finds partial matches.
- For the most precise results, use all lowercase (for example, `customerorder`) or use an exact phrase search with quotes.
- When in doubt, search for both forms or use explicit Boolean operators: `CustomerOrder OR customerorder`.

## Result ranking

When a search returns multiple results, they're ordered by a relevance score. The following factors influence ranking, from highest to lowest impact. The exact ranking logic is subject to change as the relevance engine is continually tuned.

### Where the match occurs

Not all fields carry equal weight. A match in the asset name is considered more relevant than a match in the description or other fields:

| Priority | Match type | Example |
| --- | --- | --- |
| Highest | Exact match on asset name | Searching `customers` when the asset is named exactly `customers`. |
| High | Case-insensitive exact match on name | Searching `Customers` when the asset is named `customers`. |
| Medium | Partial match on name or qualified name | Searching `customer` when the asset is named `CustomerOrderTable`. |
| Standard | Match in description, display text, classification, entity type, or other fields | Searching `customer` when the word appears in the asset description. |
| Lower | Match in schema columns, glossary terms, contacts, or custom attributes | Searching `customer` when a column named `customer_id` exists on the asset. |

Within each level, assets matching more of the search tokens score higher than assets matching fewer.

### Asset type

Leaf-level assets, such as individual tables, files, and glossary terms, receive a ranking boost over container assets like databases or storage accounts. When you search for `sales`, a table named `sales_data` typically ranks above the database that contains it.

### Data completeness

Assets that are more fully curated receive a ranking boost. Each of the following signals independently contributes to a higher score:

- Has a description
- Has one or more classifications (sensitivity labels)
- Has one or more glossary terms assigned
- Has owners or experts defined
- Has schema or column information
- Has custom attributes populated
- Has sensitivity labels applied

### Endorsement status

Endorsed assets rank higher than nonendorsed ones. **Promoted** assets receive a moderate boost, and **Certified** assets receive a boost that stacks with Promoted when both apply.

### Freshness

Recently updated assets receive a slight ranking boost over stale ones. The boost decays gradually.

### Popularity signals

Usage-based signals contribute to ranking, including modification frequency, data quality score, and user rating.

### Personalization

When you perform a search, assets where you're listed as an owner or expert receive a small boost, making your own assets easier to find.

### Smart keyword detection

The search system recognizes certain keywords and adjusts ranking:

- **`my`**: Boosts assets where you're an owner, expert, or recent editor.
- **Object type keywords**: Searching for a recognized asset category (such as `Tables`, `Files`, or `Folders`) boosts assets of that type.
- **Classification keywords**: Searching for a term that matches a known classification name (such as `PII` or `Confidential`) boosts assets with that classification.

Note

When an explicit sort order is applied (for example, sort by name or update time), relevance scoring is only used as a tiebreaker when two assets have the same sort value.

## Query limits

| Limit | Value |
| --- | --- |
| Maximum keyword length | 1,024 characters. Longer queries are truncated. |

## Known limitations

Grouping isn't supported within a field search. For example, `name:(alice AND bob)` is invalid syntax. Use `name:alice AND name:bob` instead.

## Resources

- [Search for data assets in Unified Catalog](unified-catalog-data-assets-search)
- [Discovery Query API reference](/en-us/rest/api/purview/datamapdataplane/discovery/query)