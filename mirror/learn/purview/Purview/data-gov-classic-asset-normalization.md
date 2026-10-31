---
layout: Conceptual
title: Asset normalization in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-asset-normalization
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2023-05-26T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how Microsoft Purview prevents duplicating assets in Data Map through automatic asset normalization.
locale: en-us
document_id: e7073c9a-ceca-6201-6a1c-efb72097be73
document_version_independent_id: e7073c9a-ceca-6201-6a1c-efb72097be73
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-asset-normalization.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-asset-normalization
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-asset-normalization.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/655f39c4-21c5-49d3-8367-a1f9c1a0b930
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d30b39f7-a405-488d-84ef-d6d5296ad372
platformId: f3076b77-f2c7-db8b-2cba-104537827f4d
---

# Asset normalization in Microsoft Purview Data Map | Microsoft Learn

When ingesting assets into the Microsoft Purview Data Map, different sources updating the same data asset may send similar, but slightly different qualified names. While these qualified names represent the same asset, slight differences such as an extra character may cause these assets on the surface to appear different and cause duplicate entries in Microsoft Purview. To avoid storing duplicate entries and causing confusion when consuming the Unified Catalog, Microsoft Purview automatically applies normalization during ingestion to ensure all fully qualified names of the same entity type are in the same format.

For example, you scan in an Azure Blob with the qualified name `https://myaccount.file.core.windows.net/myshare/folderA/folderB/my-file.parquet`. This blob is also consumed by an Azure Data Factory pipeline that will then add lineage information to the asset. The ADF (Azure Data Factory) pipeline may be configured to read the file as `https://myAccount.file.core.windows.net//myshare/folderA/folderB/my-file.parquet`. While the qualified name is different, this ADF pipeline is consuming the same piece of data. Normalization ensures that all the metadata from both Azure Blob Storage and Azure Data Factory is visible on a single asset, `https://myaccount.file.core.windows.net/myshare/folderA/folderB/my-file.parquet`.

Important

The rules listed below are the only kinds of potential duplication Microsoft Purview currently recognizes. If you are experiencing accidental asset duplication, compare the assets fully qualified names to check for capitalization differences or extra characters. Update any ingestion points, for example your ADF pipelines, so that the qualified names match.

## Normalization rules

These are the normalization rules that Microsoft Purview automatically applies.

### Encode curly brackets

Applies to: All Assets

Before: `https://myaccount.file.core.windows.net/myshare/{folderA}/folder{B/`

After: `https://myaccount.file.core.windows.net/myshare/%7BfolderA%7D/folder%7BB/`

### Trim section spaces

Applies to: Azure Blob, Azure Files, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2, Azure Data Factory, Azure SQL Database, Azure SQL Managed Instance, Azure SQL pool, Azure Cosmos DB, Azure Cognitive Search, Azure Data Explorer, Azure Data Share, Amazon S3

Before: `https://myaccount.file.core.windows.net/myshare/  folder A/folderB   /`

After: `https://myaccount.file.core.windows.net/myshare/folder A/folderB/`

### Remove hostname spaces

Applies to: Azure Blob, Azure Files, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2, Azure SQL Database, Azure SQL Managed Instance, Azure SQL pool, Azure Cosmos DB, Azure Cognitive Search, Azure Data Explorer, Azure Data Share, Amazon S3

Before: `https://myaccount .file. core.win dows. net/myshare/folderA/folderB/`

After: `https://myaccount.file.core.windows.net/myshare/folderA/folderB/`

### Remove square brackets

Applies to: Azure SQL Database, Azure SQL Managed Instance, Azure SQL pool

Before: `mssql://foo.database.windows.net/[bar]/dbo/[foo bar]`

After: `mssql://foo.database.windows.net/bar/dbo/foo%20bar`

Note

Spaces between two square brackets will be encoded

### Lowercase scheme

Applies to: Azure Blob, Azure Files, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2, Azure SQL Database, Azure SQL Managed Instance, Azure SQL pool, Azure Cosmos DB, Azure Cognitive Search, Azure Data Explorer, Amazon S3

Before: `HTTPS://myaccount.file.core.windows.net/myshare/folderA/folderB/`

After: `https://myaccount.file.core.windows.net/myshare/folderA/folderB/`

### Lowercase hostname

Applies to: Azure Blob, Azure Files, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2, Azure SQL Database, Azure SQL Managed Instance, Azure SQL pool, Azure Cosmos DB, Azure Cognitive Search, Azure Data Explorer, Amazon S3

Before: `https://myAccount.file.Core.Windows.net/myshare/folderA/folderB/`

After: `https://myaccount.file.core.windows.net/myshare/folderA/folderB/`

### Lowercase file extension

Applies to: Azure Blob, Azure Files, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2, Amazon S3

Before: `https://myAccount.file.core.windows.net/myshare/folderA/data.TXT`

After: `https://myaccount.file.core.windows.net/myshare/folderA/data.txt`

### Remove duplicate slash

Applies to: Azure Blob, Azure Files, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2, Azure Data Factory, Azure SQL Database, Azure SQL Managed Instance, Azure SQL pool, Azure Cosmos DB, Azure Cognitive Search, Azure Data Explorer, Azure Data Share, Amazon S3

Before: `https://myAccount.file.core.windows.net//myshare/folderA////folderB/`

After: `https://myaccount.file.core.windows.net/myshare/folderA/folderB/`

### Convert to ADL scheme

Applies to: Azure Data Lake Storage Gen1

Before: `https://mystore.azuredatalakestore.net/folderA/folderB/abc.csv`

After: `adl://mystore.azuredatalakestore.net/folderA/folderB/abc.csv`

### Remove Trailing Slash

Remove the trailing slash from higher level assets for Azure Blob, ADLS Gen1, and ADLS Gen2.

Applies to: Azure Blob, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2

Asset types: "azure\_blob\_container", "azure\_blob\_service", "azure\_storage\_account", "azure\_datalake\_gen2\_service", "azure\_datalake\_gen2\_filesystem", "azure\_datalake\_gen1\_account".

Before: `https://myaccount.core.windows.net/`

After: `https://myaccount.core.windows.net`

## Troubleshooting

If your data isn't being normalized, and you're experiencing accidental asset duplication, compare the assets fully qualified names to check for capitalization differences or additional characters.

The rules listed above are the only types of duplication Microsoft Purview currently recognizes. If your data is falling outside of these rules, update any ingestion points, for example your ADF pipelines, so that the qualified names match.

If your assets meet the rules but aren't being normalized, [contact support](https://portal.azure.com/?quickstart=true#view/Microsoft_Azure_Support/HelpAndSupportBlade/%7E/overview).