---
layout: Conceptual
title: UAE identity card number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-uae-identity-card-number
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
description: U.A.E identity card number sensitive information type entity definition.
locale: en-us
document_id: db93052a-2ea8-c35b-9a98-afb1d84afa89
document_version_independent_id: db93052a-2ea8-c35b-9a98-afb1d84afa89
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-uae-identity-card-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-uae-identity-card-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-uae-identity-card-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 5c2c5e8a-4e56-18f8-4b7f-9ac7caa3020f
---

# UAE identity card number entity definition | Microsoft Learn

## Format

Fifteen digits with optional hyphens and must pass the Luhn check

## Pattern

Fifteen digits pattern

- three digits
- optional hyphen
- four digits
- optional hyphen
- seven digits
- optional hyphen
- one digit

## Checksum

Luhn check

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_uae_id_card_number` finds content that matches the pattern.
- A keyword from Keyword\_uae\_id\_card\_number is found.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_uae_id_card_number` finds content that matches the pattern.

```xml
     <!-- UAE Identity Card Number -->
      <Entity id="853a8051-ad90-417c-9345-c73ac0adc1c3" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_uae_id_card_number" />
          <Match idRef="Keyword_uae_id_card_number" />
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_uae_id_card_number" />
        </Pattern>
      </Entity>
```

## Keywords

**Keyword\_uae\_id\_card\_number**

- Emirates id
- ID number
- id no
- id #
- id#
- identification number
- identification no
- identification #
- identification#
- emirates identity card
- Insurance Number
- insurance no
- insurance#
- insurance #
- التأمين رقم
- التأمينرقم#
- رقم الهوية
- رقم الهوية#