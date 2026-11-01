---
layout: Conceptual
title: Medicare Beneficiary Identifier (MBI) card entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-medicare-beneficiary-identifier-card
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
description: Medicare Beneficiary Identifier (MBI) card sensitive information type entity definition.
locale: en-us
document_id: 6077d73e-a931-0cdc-3748-5c475e693369
document_version_independent_id: 6077d73e-a931-0cdc-3748-5c475e693369
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-medicare-beneficiary-Identifier-card.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-medicare-beneficiary-identifier-card
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-medicare-beneficiary-Identifier-card.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: cee7ce22-9c11-0871-745b-faa6ff412a82
---

# Medicare Beneficiary Identifier (MBI) card entity definition | Microsoft Learn

## Format

11 character alphanumeric pattern

## Pattern

- one digit between 1 to 9
- one letter excluding S, L, O, I, B, Z
- one digit or letter excluding S, L, O, I, B, Z
- one digit
- an optional Hyphen
- one letter excluding S, L, O, I, B, Z
- one digit or letter excluding S, L, O, I, B, Z
- one digit
- an optional Hyphen
- two letters excluding S, L, O, I, B, Z
- two digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_mbi_card` finds content that matches the pattern.
- A keyword from `Keyword_mbi_card` is found.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_mbi_card` finds content that matches the pattern.

```xml
    <!-- Medicare Beneficiary Identifier (MBI) card -->
      <Entity id="f753a286-f5cc-47e6-a592-4be25fd02591" patternsProximity="300" recommendedConfidence="75" relaxProximity="true">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_mbi_card" />
          <Match idRef="Keyword_mbi_card" />
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_mbi_card" />
        </Pattern>
      </Entity>
```

## Keywords

### Keyword\_mbi\_card

- mbi
- mbi#
- medicare beneficiary #
- medicare beneficiary identifier
- medicare beneficiary no
- medicare beneficiary number
- medicare beneficiary#