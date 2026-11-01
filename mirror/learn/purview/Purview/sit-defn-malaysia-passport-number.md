---
layout: Conceptual
title: Malaysia passport number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-malaysia-passport-number
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
description: Malaysia passport number sensitive information type entity definition.
locale: en-us
document_id: 8012520a-0b16-4c49-ff3f-4b5bf9b05e77
document_version_independent_id: 8012520a-0b16-4c49-ff3f-4b5bf9b05e77
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-malaysia-passport-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-malaysia-passport-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-malaysia-passport-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: ca41d9a0-eb1a-acaf-7f6d-7a5423aaf413
---

# Malaysia passport number entity definition | Microsoft Learn

## Format

Nine alphanumeric characters with only specific values for letters

## Pattern

- a letter (A/H/K/a/h/k) followed by
- eight digits

## Checksum

Not applicable

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A Data Loss Protection (DLP) policy has high confidence of detection for this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_malaysia_passport_number` finds content that matches the pattern.
- A keyword from `Keyword_malaysia_passport_number` is found.

A DLP policy has low confidence of detection for this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_malaysia_passport_number` finds content that matches the pattern.

```xml
        <!-- Malaysia Passport Number -->
      <Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee" patternsProximity="300" recommendedConfidence="85" relaxProximity="true">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_malaysia_passport_number" />
          <Match idRef="Keyword_malaysia_passport_number" />
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Regex_malaysia_passport_number" />
        </Pattern>
      </Entity>
```

## Keywords

**Keyword\_malaysia\_passport\_number**

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