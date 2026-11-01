---
layout: Conceptual
title: UAE passport number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-uae-passport-number
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
description: U.A.E passport number sensitive information type entity definition.
locale: en-us
document_id: 45d78d79-44dc-7553-26a2-e5bfab45f749
document_version_independent_id: 45d78d79-44dc-7553-26a2-e5bfab45f749
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-uae-passport-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-uae-passport-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-uae-passport-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 876cbe1d-2ecc-33e4-6549-9729e2dfaf8a
---

# UAE passport number entity definition | Microsoft Learn

## Format

Nine alphanumeric characters that must include letters of specific values

## Pattern

Nine alphanumeric characters from numerals 0–9 and letters C, F, G, H, J, K, L, M, N, P, R, T, V, W, X, Y, Z

## Checksum

All nine characters shouldn't be digits.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_uae_passport_number` finds content that matches the pattern.
- A keyword from `Keyword_uae_passport_number` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

The regular expression `Regex_uae_passport_number` finds content that matches the pattern.

```xml
  <!-- UAE Passport Number -->
      <Entity id="111b5e63-6f4e-47c6-99bc-dd95625a5acf" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_uae_passport_number" />
          <Match idRef="Keyword_uae_passport_number" />
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Regex_uae_passport_number" />
        </Pattern>
      </Entity>
```

## Keywords

**Keyword\_uae\_passport\_number**

- جواز سفر
- جواز سفر#
- passport#
- passport #
- passportno
- passport no
- passportnumber
- passport number
- passportnumbers
- passport numbers