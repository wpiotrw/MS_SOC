---
layout: Conceptual
title: Azure DocumentDB auth key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-document-db-auth-key
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-07T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Azure DocumentDB auth key sensitive information type entity definition.
locale: en-us
document_id: 39b90166-c6d2-eeb3-c1d8-0ce511df0059
document_version_independent_id: 39b90166-c6d2-eeb3-c1d8-0ce511df0059
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-document-db-auth-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-document-db-auth-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-document-db-auth-key.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/63b4a448-7cf0-47e3-916c-0c12c7086ac5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/2d05d82b-73c9-42c9-a8ea-1459358f0bef
platformId: 2f2e6754-81cd-8862-3891-e5d287eccdfe
---

# Azure DocumentDB auth key entity definition | Microsoft Learn

## Format

The string `DocumentDb` followed by the characters and strings outlined in the pattern below.

## Pattern

- The string `DocumentDb`
- Any combination of between 3-200 lower- or uppercase letters, digits, symbols, special characters, or spaces
- A greater than symbol (&gt;), an equal sign (=), a quotation mark ("), or an apostrophe (')
- Any combination of 86 lower- or uppercase letters, digits, forward slash (/), or plus sign (+)
- Two equal signs (=)

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `CEP_Regex_AzureDocumentDBAuthKey` finds content that matches the pattern.
- The regular expression `CEP_CommonExampleKeywords` doesn't find content that matches the pattern.

```xml
<!-- Azure Document DB Auth Key -->
<Entity id="0f587d92-eb28-44a9-bd1c-90f2892b47aa" patternsProximity="300" recommendedConfidence="85">
  <Pattern confidenceLevel="85">
        <IdMatch idRef="CEP_Regex_AzureDocumentDBAuthKey" />
        <Any minMatches="0" maxMatches="0">
            <Match idRef="CEP_CommonExampleKeywords" />
          </Any>
  </Pattern>
</Entity>
```

## Keywords

### CEP\_CommonExampleKeywords

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