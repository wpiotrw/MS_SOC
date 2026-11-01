---
layout: Conceptual
title: Azure IAAS database connection string and Azure SQL connection string entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-09-13T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Azure IAAS database connection string and Azure SQL connection string sensitive information type entity definition.
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: 1d632fae-6431-9e52-fd3d-4ff055b8d76e
document_version_independent_id: 1d632fae-6431-9e52-fd3d-4ff055b8d76e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
platformId: 345fc3cf-97e8-62f3-a730-944a70d87f3a
---

# Azure IAAS database connection string and Azure SQL connection string entity definition | Microsoft Learn

## Format

The string `Server`, `server`, or `data source` followed by the characters and strings outlined in the pattern below, including the string `cloudapp.azure.com` or `cloudapp.azure.net` or `database.windows.net`, and the string `Password` or `password` or `pwd`.

## Pattern

- the string `Server`, `server`, or `data source`
- zero to two whitespace characters
- an equal sign (=)
- zero to two whitespace characters
- any combination of between 1-200 lower- or uppercase letters, digits, symbols, special characters, or spaces
- The string "cloudapp.azure.com", "cloudapp.azure.net", or "database.windows.net"
- any combination of between 1-300 lower- or uppercase letters, digits, symbols, special characters, or spaces
- the string `Password`, `password`, or `pwd`
- zero to two whitespace characters
- an equal sign (=)
- zero to two whitespace characters
- one or more characters that aren't a semicolon (;), quotation mark ("), or apostrophe (')
- a semicolon (;), quotation mark ("), or apostrophe (')

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `CEP_Regex_AzureConnectionString` finds content that matches the pattern.
- The regular expression `CEP_CommonExampleKeywords` doesn't find content that matches the pattern.

```xml
<!--Azure IAAS Database Connection String and Azure SQL Connection String-->
<Entity id="ce1a126d-186f-4700-8c0c-486157b953fd" patternsProximity="300" recommendedConfidence="85">
  <Pattern confidenceLevel="85">
        <IdMatch idRef="CEP_Regex_AzureConnectionString" />
        <Any minMatches="0" maxMatches="0">
            <Match idRef="CEP_CommonExampleKeywords" />
        </Any>
    </Pattern>
</Entity>
```

## Keywords

### CEP\_common\_example\_keywords

This sensitive information type identifies these keywords by using a regular expression, not a keyword list.

- contoso
- fabrikam
- northwind
- sandbox
- onebox
- localhost
- 127.0.0.1
- testacs.com
- s-int.net