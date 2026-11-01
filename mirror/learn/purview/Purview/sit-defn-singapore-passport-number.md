---
layout: Conceptual
title: Singapore passport number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-singapore-passport-number
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
description: Singapore passport number sensitive information type entity definition.
locale: en-us
document_id: d7b3bd4e-dff6-3940-f48c-ae76fc76106e
document_version_independent_id: d7b3bd4e-dff6-3940-f48c-ae76fc76106e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-singapore-passport-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-singapore-passport-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-singapore-passport-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 27e94777-8d71-4a70-4468-dc9588310e25
---

# Singapore passport number entity definition | Microsoft Learn

## Format

Nine alphanumeric characters with only specific values for letters.

## Pattern

- a letter e/E or k/K followed by
- seven digits followed by
- a letter

## Checksum

Not applicable

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A Data Loss Protection (DLP) policy has high confidence of detection for this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_singapore_passport_number` finds content that matches the pattern.
- A keyword from `Keyword_singapore_passport_number` is found.

A DLP policy has low confidence of detection for this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_singapore\_passport\_number finds content that matches the pattern.

```xml
      <!-- Singapore Passport Number -->
      <Entity id="4081ae73-c4ec-405d-932c-8b36ae35b20c" patternsProximity="300" recommendedConfidence="85" relaxProximity="true">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_singapore_passport_number" />
          <Match idRef="Keyword_singapore_passport_number" />
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Regex_singapore_passport_number" />
        </Pattern>
      </Entity>
```

## Keywords

**Keyword\_singapore\_passport\_number**

- passport#
- passport #
- passportno
- passport no
- passportnumber
- passport number
- passportnumbers
- passport numbers
- pasport#
- pasport #
- pasportno
- pasport no
- pasportnumber
- pasport number
- pasportnumbers
- pasport numbers
- no. pasport
- nombor pasport
- nomborpasport