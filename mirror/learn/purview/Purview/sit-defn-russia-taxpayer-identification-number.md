---
layout: Conceptual
title: Russia taxpayer identification number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-russia-taxpayer-identification-number
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-06-12T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Russia taxpayer identification number sensitive information type entity definition.
locale: en-us
document_id: ed9bc25c-67a3-fe05-dcf6-649ffabea04a
document_version_independent_id: ed9bc25c-67a3-fe05-dcf6-649ffabea04a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-russia-taxpayer-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-russia-taxpayer-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-russia-taxpayer-identification-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: a1ba5db2-775e-bff1-1e9c-85c8b74416ab
---

# Russia taxpayer identification number entity definition | Microsoft Learn

## Format

10 or 12 digits, validated by a checksum function.

## Pattern

10 digits (organizations) or 12 digits (individuals):

- Four digits (tax authority code)
- Five or six digits (serial number)
- One or two check digits

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Checksum

Yes

## Definition

A data loss prevention (DLP) policy has high confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_Russian_Taxpayer_Identification_Number` finds content that matches the pattern.
- A keyword from `Keyword_Russian_Taxpayer_Identification_Number` is found.

A DLP policy has medium confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_Russian_Taxpayer_Identification_Number` finds content that matches the pattern.

```xml
    <!-- Russian Taxpayer Identification Number -->
    <Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee" patternsProximity="300" recommendedConfidence="85" filters="russian_taxpayer_id_filter">
      <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_Russian_Taxpayer_Identification_Number" />
        <Match idRef="Keyword_Russian_Taxpayer_Identification_Number" />
      </Pattern>
      <Pattern confidenceLevel="75">
        <IdMatch idRef="Func_Russian_Taxpayer_Identification_Number" />
      </Pattern>
    </Entity>
```

## Keywords

The following keywords are used for detection. These include Taxpayer Identification Number (TIN) variations and Russian-language equivalents.

### Keyword\_Russian\_Taxpayer\_Identification\_Number

- `TIN`
- `taxpayer number`
- `taxpayer ID`
- `taxpayer no`
- `tax ID`
- `Tin`
- `tinno#`
- `Inn`
- `inn#`
- `taxpayerno#`
- `taxid#`
- `taxpayeridno#`
- `taxpayerid#`
- `taxpayer`
- `tax identification`
- `tax payer`
- `taxid`
- `НДС`
- `номер налогоплательщика`
- `Налогоплательщика ИД`
- `налог число`
- `налогчисло#`
- `ИНН`
- `НДС#`