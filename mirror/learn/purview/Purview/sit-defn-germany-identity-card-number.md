---
layout: Conceptual
title: Germany identity card number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-germany-identity-card-number
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-01-24T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Germany identity card number sensitive information type entity definition.
locale: en-us
document_id: 87ba55c4-41ea-0c3e-8612-d439b101b47b
document_version_independent_id: 87ba55c4-41ea-0c3e-8612-d439b101b47b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-germany-identity-card-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-germany-identity-card-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-germany-identity-card-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: cb37b6c1-b45b-b496-1e2b-01b76298dcde
---

# Germany identity card number entity definition | Microsoft Learn

## Format

since 1 November 2010: Nine to 11 letters and digits

from 1 April 1987 until 31 October 2010: 10 digits

## Pattern

since 1 November 2010: 9 to 11 characters alphanumeric pattern

- one L, M, N, P, R, T, V, W, X, Y (case insensitive)
- eight digits or letters in C, F, G, H, J, K, L, M, N, P, R, T, V, W, X, Y and Z (case insensitive)
- optional check digit
- Optional d/D

from 1 April 1987 until 31 October 2010:

- 10 digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_german_id_card_with_check` finds content that matches the pattern (10 to 11 characters alphanumeric pattern (post 2010)).
- A keyword from `Keyword_germany_id_card` is found.
- The checksum passes.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_germany_id_card` finds content that matches the pattern (9 characters without check digit issued post-2010 or 10 digits pattern issued pre-2010).
- A keyword from `Keyword_germany_id_card` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_german_id_card_with_check` finds content that matches the pattern (10 to 11 characters alphanumeric pattern (post 2010)).
- The checksum passes.

```xml
      <!-- Germany Identity Card Number -->
      <Entity id="e577372f-c42e-47a0-9d85-bebed1c237d4" patternsProximity="300" recommendedConfidence="75">
        <Pattern confidenceLevel="75">
         <IdMatch idRef="Regex_germany_id_card" />
         <Match idRef="Keyword_germany_id_card" />
        </Pattern>
        <Version minEngineVersion="15.20.4545.000">
          <Pattern confidenceLevel="85">
           <IdMatch idRef="Func_german_id_card_with_check" />
            <Match idRef="Keyword_germany_id_card" />
          </Pattern>
          <Pattern confidenceLevel="65">
           <IdMatch idRef="Func_german_id_card_with_check" />
          </Pattern>
        </Version>
      </Entity>
```

## Keywords

### Keyword\_germany\_id\_card

- ausweis
- gpid
- identification
- identifikation
- identifizierungsnummer
- identity card
- identity number
- id-nummer
- personal id
- personalausweis
- persönliche id nummer
- persönliche identifikationsnummer
- persönliche-id-nummer