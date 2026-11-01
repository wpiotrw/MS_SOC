---
layout: Conceptual
title: South Korea passport number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-south-korea-passport-number
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
description: South Korea passport number sensitive information type entity definition.
locale: en-us
document_id: c2309012-28e5-088a-8287-000c74a58553
document_version_independent_id: c2309012-28e5-088a-8287-000c74a58553
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-south-korea-passport-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-south-korea-passport-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-south-korea-passport-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: f50fe478-45c3-cbf2-98e9-57ab771ab684
---

# South Korea passport number entity definition | Microsoft Learn

## Format

Nine alphanumeric characters; only specific values are allowed.

## Pattern

- a letter (M|S|R|O|D) followed by
- eight digits

Or

- a letter (M|S|R|O|D) followed by
- three digits followed by
- one letter followed by
- four digits

## Checksum

Not applicable

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_south_korea_passport_number` finds content that matches the pattern.
- A keyword from `Keyword_south_korea_passport_number` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_south\_korea\_passport\_number finds content that matches the pattern.

```xml
      <!-- South Korea Passport Number -->
      <Entity id="cb725748-0f69-4282-8a03-e9b222a10a18" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_south_korea_passport_number" />
          <Match idRef="Keyword_south_korea_passport_number" />
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Regex_south_korea_passport_number" />
        </Pattern>
      </Entity>
```

## Keywords

**Keyword\_south\_korea\_passport\_number**

- passport#
- passport #
- passportno
- passport no
- passportnumber
- passport number
- passportnumbers
- passport numbers
- 여권 번호
- 한국어 여권
- 여권 번호
- 여권번호
- 한국 여권
- 한국여권
- 한국 여권 번호