---
layout: Conceptual
title: Find sensitive data stored on sites with eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-find-sensitive-data-stored-on-sites
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use eDiscovery to discover documents that contain sensitive data in your organization.
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
locale: en-us
document_id: 277e18e5-8857-5efc-d167-9bb53388efc3
document_version_independent_id: 277e18e5-8857-5efc-d167-9bb53388efc3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-find-sensitive-data-stored-on-sites.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-find-sensitive-data-stored-on-sites
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-find-sensitive-data-stored-on-sites.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
platformId: 14144a4a-871f-e585-7d4b-054904c8d8f2
---

# Find sensitive data stored on sites with eDiscovery | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Users often store sensitive data, such as credit card numbers, social security numbers, or personal, on their sites, and over time this can expose an organization to significant risk of data loss. Documents stored on sites—including OneDrive for Business sites—could be shared with people outside the organization who shouldn't have access to the information.

With Microsoft Purview eDiscovery, you can discover documents that contain sensitive data throughout your tenant. After discovering the documents, you can work with the document owners to protect the data. This article can help you form a query to search for sensitive data.

## Forming a basic query

There are three parts that make up a basic query: SensitiveType, count range, and confidence range. For example, **SensitiveType:"&lt;type&gt;"** is required, and both **|&lt;count range&gt;** and **|&lt;confidence range&gt;** are optional.

### Sensitive type - required

Queries typically begin with the property `SensitiveType:"` and an information type name from the [sensitive information types inventory](/en-us/Exchange/what-the-sensitive-information-types-in-exchange-look-for-exchange-2013-help), and end with a `"`. To search for custom sensitive information types, you have to specify the ID of the sensitive information type in the `SensitiveType` property. Using the name of a custom sensitive information type won't return any results.

### Ranges - optional

Both of the next two parts are ranges, so let's quickly examine what a range looks like. In SharePoint queries, a basic range is represented by two numbers separated by two periods, which looks like this: `[number]..[number]`. For instance, if `10..20` is used, that range would capture numbers from 10 through 20. There are many different range combinations and several are covered in this article.

Let's add a count range to the query. You can use count range to define the number of occurrences of sensitive information a document needs to contain before it's included in the query results. For example, if you want your query to return only documents that contain exactly five credit card numbers, use this: `SensitiveType:"Credit Card Number|5"`. Count range can also help you identify documents that pose high degrees of risk. For example, your organization might consider documents with five or more credit card numbers a high risk. To find documents fitting this criterion, you would use this query: `SensitiveType:"Credit Card Number|5.."`. Alternatively, you can find documents with five or fewer credit card numbers by using this query: `SensitiveType:"Credit Card Number|..5"`.

#### Confidence range

Finally, confidence range is the level of confidence that the detected sensitive type is actually a match. The values for confidence range work similarly to count range. You can form a query without including a count range. For example, to search for documents with any number of credit card numbers—as long as the confidence range is 85 percent or higher—you would use this query: `SensitiveType:"Credit Card Number|*|85.."`.

Important

The asterisk ( `*` ) is a wildcard character that means any value works. You can use the wildcard character ( `*` ) either in the count range or in the confidence range, but not in a sensitive type.

### Additional query properties and search operators available in the eDiscovery Center

Queries in SharePoint also contains the LastSensitiveContentScan property, which can help you search for files scanned within a specific timeframe. For query examples with the `LastSensitiveContentScan` property, see the Examples of complex queries in the next section.

You can use SharePoint eDiscovery search properties such as `Author` or `FileExtension`. You can use operators to build complex queries. For the list of available properties and operators, see the [Using Search Properties and Operators with eDiscovery](/en-us/archive/blogs/quentin/using-search-properties-and-operators-with-ediscovery) blog post.

## Examples of complex queries

The following examples use different sensitive types, properties, and operators to illustrate how you can refine your queries to find exactly what you're looking for.

| Query | Explanation |
| --- | --- |
| `SensitiveType:"International Banking Account Number (IBAN)"` | The name might seem strange because it's so long, but it's the correct name for that sensitive type. Make sure to use exact names from the [sensitive information types inventory](/en-us/Exchange/what-the-sensitive-information-types-in-exchange-look-for-exchange-2013-help). You can also use the name of a [custom sensitive information type](sit-create-a-custom-sensitive-information-type) that you created for your organization. |
| `SensitiveType:"Credit Card Number|1..4294967295|1..100"` | This returns documents with at least one match to the sensitive type "Credit Card Number." The values for each range are the respective minimum and maximum values. A simpler way to write this query is `SensitiveType:"Credit Card Number"`, but where's the fun in that? |
| `SensitiveType:"Credit Card Number|5..25" AND LastSensitiveContentScan:"8/11/2018..8/13/2018"` | This returns documents with 5-25 credit card numbers that were scanned from August 11, 2018 through August 13, 2018. |
| `SensitiveType:"Credit Card Number|5..25" AND LastSensitiveContentScan:"8/11/2018..8/13/2018" NOT FileExtension:XLSX` | This returns documents with 5-25 credit card numbers that were scanned from August 11, 2018 through August 13, 2018. Files with an XLSX extension aren't included in the query results. `FileExtension` is one of many properties that you can include in a query. For more information, see [Using Search Properties and Operators with eDiscovery](/en-us/archive/blogs/quentin/using-search-properties-and-operators-with-ediscovery). |
| `SensitiveType:"Credit Card Number" OR SensitiveType:"U.S. Social Security Number (SSN)"` | This returns documents that contain either a credit card number or a social security number. |
|  |  |

## Examples of queries to avoid

Not all queries are created equal. The following table gives examples of queries that don't work in SharePoint and describes why.

| Unsupported query | Reason |
| --- | --- |
| `SensitiveType:"Credit Card Number|.."` | You must add at least one number. |
| `SensitiveType:"NotARule"` | "NotARule" isn't a valid sensitive type name. Only names in the [sensitive information types inventory](/en-us/Exchange/what-the-sensitive-information-types-in-exchange-look-for-exchange-2013-help) work in eDiscovery queries. |
| `SensitiveType:"Credit Card Number|0"` | Zero isn't valid as either the minimum value or the maximum value in a range. |
| `SensitiveType:"Credit Card Number"` | It's might be difficult to see, but there's extra white space between "Credit" and "Card" that makes the query invalid. Use exact sensitive type names from the [sensitive information types inventory](/en-us/Exchange/what-the-sensitive-information-types-in-exchange-look-for-exchange-2013-help). |
| `SensitiveType:"Credit Card Number|1. .3"` | The two-period portion shouldn't be separated by a space. |
| `SensitiveType:"Credit Card Number| |1..|80.."` | There are too many pipe delimiters (|). Follow this format instead: `SensitiveType: "Credit Card Number|1..|80.."` |
| `SensitiveType:"Credit Card Number|1..|80..101"` | Because confidence values represent a percentage, they can't exceed 100. Choose a number from 1 through 100 instead. |
|  |  |

## For more information

- [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions)
- [Run a Content Search](ediscovery-content-search)
- [Keyword queries and search conditions for Content Search](ediscovery-keyword-queries-and-search-conditions)