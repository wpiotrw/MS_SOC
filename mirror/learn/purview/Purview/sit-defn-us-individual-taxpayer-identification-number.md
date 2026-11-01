---
layout: Conceptual
title: U.S. individual taxpayer identification number (ITIN) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number
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
description: U.S. individual taxpayer identification number (ITIN) sensitive information type entity definition.
locale: en-us
document_id: 6898f351-a0f0-7854-d2f5-3e9d58011bfc
document_version_independent_id: 6898f351-a0f0-7854-d2f5-3e9d58011bfc
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-us-individual-taxpayer-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-us-individual-taxpayer-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-us-individual-taxpayer-identification-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 0ef8cd02-be5f-1586-5294-dd3842990d81
---

# U.S. individual taxpayer identification number (ITIN) entity definition | Microsoft Learn

## Format

nine digits, optionally formatted with spaces or dashes

## Pattern

formatted:

- the digit "9"
- two digits
- a space or dash (optional)
- two digits "50" to "65", "70" to "88", “90” to “92” and “94” to “99” for the fourth and fifth digit
- a space, or dash (optional)
- four digits

unformatted:

- the digit "9"
- two digits
- two digits "50" to "65", "70" to "88", “90” to “92”, and “94” to “99” for the fourth and fifth digits
- four digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_formatted_itin` finds content that matches the pattern.
- A keyword from `Keyword_itin` is found.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_unformatted_itin` finds content that matches the pattern.
- A keyword from `Keyword_itin` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_formatted_itin` or `Func_unformatted_itin` finds content that matches the pattern.

```xml
    <!-- U.S. Individual Taxpayer Identification Number (ITIN) -->
    <Entity id="e55e2a32-f92d-4985-a35d-a0b269eb687b" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_formatted_itin" />
        <Match idRef="Keyword_itin" />
      </Pattern>
      <Pattern confidenceLevel="75">
        <IdMatch idRef="Func_unformatted_itin" />
        <Match idRef="Keyword_itin" />
      </Pattern>
      <Pattern confidenceLevel="65">
        <IdMatch idRef="Func_formatted_itin" />
      </Pattern>
      <Pattern confidenceLevel="65">
        <IdMatch idRef="Func_unformatted_itin" />
      </Pattern>
    </Entity>
```

## Keywords

### Keyword\_itin

- taxpayer
- tax id
- tax identification
- itin
- i.t.i.n.
- ssn
- tin
- social security
- tax payer
- itins
- taxid
- individual taxpayer