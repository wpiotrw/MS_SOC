---
layout: Conceptual
title: Resource sets in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-resource-sets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2026-03-31T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn what resource sets are and how they're created in Microsoft Purview.
locale: en-us
document_id: d6be13b6-2fa7-bd18-3242-81e8afad7ee9
document_version_independent_id: d6be13b6-2fa7-bd18-3242-81e8afad7ee9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-resource-sets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-resource-sets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-resource-sets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 643d1c0b-4769-b49f-4efa-e8eb8ef2ff67
---

# Resource sets in Microsoft Purview | Microsoft Learn

This article helps you understand how resource sets are used in Microsoft Purview to map data assets to logical resources.

Note

Now rolling out, the advanced resource sets capability is available to all customers in Microsoft Purview Unified Catalog. Pricing for advanced resource sets is consistent with existing rates for [classic Microsoft Purview data governance](data-gov-classic-pricing).

## Background info

At-scale data processing systems typically store a single table in storage as multiple files. In the Microsoft Purview Unified Catalog, this concept is represented by using resource sets. A resource set is a single object in the catalog that represents a large number of assets in storage.

For example, suppose your Spark cluster has persisted a DataFrame into an Azure Data Lake Storage (ADLS) Gen2 data source. Although in Spark the table looks like a single logical resource, on the disk there are likely thousands of Parquet files, each of which represents a partition of the total DataFrame's contents. IoT data and web log data have the same challenge. Imagine you have a sensor that outputs log files several times a second. It won't take long until you have hundreds of thousands of log files from that single sensor.

## How Microsoft Purview detects resource sets

Microsoft Purview supports detecting resource sets in Azure Blob Storage, ADLS Gen1, ADLS Gen2, Azure Files, and Amazon S3.

Microsoft Purview automatically detects resource sets when scanning. This feature looks at all of the data that's ingested via scanning and compares it to a set of defined patterns.

For example, suppose you scan a data source whose URL is `https://myaccount.blob.core.windows.net/mycontainer/machinesets/23/foo.parquet`. Microsoft Purview looks at the path segments and determines if they match any built-in patterns. It has built-in patterns for GUIDs, numbers, date formats, localization codes (for example, en-us), and so on. In this case, the number pattern matches *23*. Microsoft Purview assumes that this file is part of a resource set named `https://myaccount.blob.core.windows.net/mycontainer/machinesets/{N}/foo.parquet`.

Or, for a URL like `https://myaccount.blob.core.windows.net/mycontainer/weblogs/en_au/23.json`, Microsoft Purview matches both the localization pattern and the number pattern, producing a resource set named `https://myaccount.blob.core.windows.net/mycontainer/weblogs/{LOC}/{N}.json`.

Using this strategy, Microsoft Purview would map the following resources to the same resource set, `https://myaccount.blob.core.windows.net/mycontainer/weblogs/{LOC}/{N}.json`:

- `https://myaccount.blob.core.windows.net/mycontainer/weblogs/cy_gb/1004.json`
- `https://myaccount.blob.core.windows.net/mycontainer/weblogs/cy_gb/234.json`
- `https://myaccount.blob.core.windows.net/mycontainer/weblogs/de_Ch/23434.json`

### File types that Microsoft Purview will not detect as resource sets

Microsoft Purview intentionally doesn't try to classify most document file types like Word, Excel, or PDF as Resource Sets. The exception is CSV format since that is a common partitioned file format.

## How Microsoft Purview scans resource sets

When Microsoft Purview detects resources that it thinks are part of a resource set, it switches from a full scan to a sample scan. A sample scan opens only a subset of the files that it thinks are in the resource set. For each file it opens, it uses its schema and runs its classifiers. Microsoft Purview then finds the newest resource among the opened resources and uses that resource's schema and classifications in the entry for the entire resource set in the catalog.

## Advanced resource sets

Microsoft Purview can customize and further enrich your resource set assets through the **Advanced Resource Sets** capability. Advanced resource sets allow Microsoft Purview to understand the underlying partitions of data ingested and enables the creation of [resource set pattern rules](data-map-resource-set-pattern-rules) that customize how Microsoft Purview groups resource sets during scanning.

When Advanced Resource Sets are enabled, Microsoft Purview runs extra aggregations to compute the following information about resource set assets:

- A sample path from a file that comprises the resource set.
- A partition count that shows how many files make up the resource set.
- The total size of all files that comprise the resource set.

These properties can be found on the asset details page of the resource set.

![The properties computed when advanced resource sets is on](media/concept-resource-sets/resource-set-properties.png)

### Turning on advanced resource sets

Advanced resource sets are off by default in all new Microsoft Purview instances. Only users with the Data Curator role at root collection can manage Advanced Resource Sets settings. To enable advanced resource sets, go to **Microsoft Purview portal** &gt; **Settings** &gt; **Account**, and select the toggle for **Advanced Resources Sets**, as seen in this image:

![Turn on advanced resource sets in Microsoft Purview settings.](media/data-governance-advanced-resource-sets.png)

After enabling advanced resource sets, the extra enrichments will occur on all newly ingested assets. These enrichments could take up to **12 hours** to be available on your assets after ingestion. The Microsoft Purview team recommends waiting an hour before scanning in new data lake data after toggling on the feature.

Important

Enabling advanced resource sets affects the refresh rate of asset and classification insights. When advanced resource sets are on, asset and classification insights update twice a day.

Also, when you enable advanced resource sets, it could take up to **12 hours** to see schema updates.

## Built-in resource set patterns

Microsoft Purview supports the following resource set patterns. These patterns can appear as a name in a directory or as part of a file name.

### Regex-based patterns

| Pattern Name | Display Name | Description |
| --- | --- | --- |
| Guid | {GUID} | A globally unique identifier as defined in [RFC 4122](https://tools.ietf.org/html/rfc4122) |
| Number | {N} | One or more digits |
| Date/Time Formats | {Year}{Month}{Day}{N} | We support various date/time formats but all are represented with {Year}[delimiter]{Month}[delimiter]{Day} or series of {N}s. |
| 4ByteHex | {HEX} | A four-digit HEX number. |
| Localization | {LOC} | A language tag as defined in [BCP 47](https://tools.ietf.org/html/bcp47), both - and \_ names are supported (for example, en\_ca and en-ca) |

### Complex patterns

| Pattern Name | Display Name | Description |
| --- | --- | --- |
| SparkPath | {SparkPartitions} | Spark partition file identifier |
| Date(yyyy/mm/dd)InPath | {Year}/{Month}/{Day} | Year/month/day pattern spanning multiple folders |

## How resource sets are displayed in Unified Catalog

When Microsoft Purview matches a group of assets into a resource set, it attempts to extract the most useful information to use as a display name in the catalog. Some examples of the default naming convention applied:

### Example 1

Qualified name: `https://myblob.blob.core.windows.net/sample-data/name-of-spark-output/{SparkPartitions}`

Display name: "name of spark output"

### Example 2

Qualified name: `https://myblob.blob.core.windows.net/my-partitioned-data/{Year}-{Month}-{Day}/{N}-{N}-{N}-{N}/{GUID}`

Display name: "my partitioned data"

### Example 3

Qualified name: `https://myblob.blob.core.windows.net/sample-data/data{N}.csv`

Display name: "data"

## Customizing resource set grouping using pattern rules

When scanning a storage account, Microsoft Purview uses a set of defined patterns to determine if a group of assets is a resource set. In some cases, Microsoft Purview's resource set grouping might not accurately reflect your data estate. These issues can include:

- Incorrectly marking an asset as a resource set.
- Putting an asset into the wrong resource set.
- Incorrectly marking an asset as not being a resource set.

To customize or override how Microsoft Purview detects which assets are grouped as resource sets and how they're displayed within the catalog, you can define pattern rules in the management center. For step-by-step instructions and syntax, see [resource set pattern rules](data-map-resource-set-pattern-rules).

## Known limitations with resource sets

- By default, resource set assets will only be deleted by a scan if Advanced Resource sets are enabled. If this capability is off, resource set assets can only be deleted manually or via API.