---
layout: Conceptual
title: Azure Redis cache connection string entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-redis-cache-connection-string
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-10T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- tier2- purview-compliance
recommendations: false
description: Azure Redis cache connection string sensitive information type entity definition.
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: 754a6d82-05d2-71a2-b464-8e595a344cb9
document_version_independent_id: 754a6d82-05d2-71a2-b464-8e595a344cb9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-redis-cache-connection-string.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-redis-cache-connection-string
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-redis-cache-connection-string.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f80a1aa9-ec39-45c7-bff1-e6916def6921
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b47bd505-a970-48d0-a7c0-cc58500975e6
platformId: bf11252d-7191-e302-8f82-f80e459a0627
---

# Azure Redis cache connection string entity definition | Microsoft Learn

## Format

The string `redis.cache.windows.net` followed by the characters and strings outlined in the pattern below, including the string `password` or `pwd`.

## Pattern

- the string `redis.cache.windows.net`
- any combination of between 1-200 lower- or uppercase letters, digits, symbols, special characters, or spaces
- the string `password` or `pwd`
- zero to two whitespace characters
- an equal sign (=)
- zero to two whitespace characters
- any combination of 43 characters that are lower- or uppercase letters, digits, forward slash (/), or plus sign (+)
- an equal sign (=)

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `CEP_Regex_AzureRedisCacheConnectionString` finds content that matches the pattern.
- The regular expression `CEP_CommonExampleKeywords` doesn't find content that matches the pattern.

```xml
<!--Azure Redis Cache Connection String-->
<Entity id="095a7e6c-efd8-46d5-af7b-5298d53a49fc" patternsProximity="300" recommendedConfidence="85">
  <Pattern confidenceLevel="85">
        <IdMatch idRef="CEP_Regex_AzureRedisCacheConnectionString" />
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