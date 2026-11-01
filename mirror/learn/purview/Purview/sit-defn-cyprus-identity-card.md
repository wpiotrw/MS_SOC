---
layout: Conceptual
title: Cyprus identity card entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-identity-card
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
description: Cyprus identity card sensitive information type entity definition.
locale: en-us
document_id: 15274d62-461f-c096-31dc-5b0377b716f6
document_version_independent_id: 15274d62-461f-c096-31dc-5b0377b716f6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-cyprus-identity-card.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-cyprus-identity-card
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-cyprus-identity-card.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 8110c33c-9b17-5086-2723-9d0e2374cdc4
---

# Cyprus identity card entity definition | Microsoft Learn

## Format

10 digits without spaces and delimiters

## Pattern

10 digits

## Checksum

Not applicable

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_cyprus_eu_national_id_card` finds content that matches the pattern.
- A keyword from `Keywords_cyprus_eu_national_id_card` is found.

```xml
      <!-- Cyprus Identity Card -->
      <Entity id="3ba8afe5-7a6c-4929-8247-0001b6878438" patternsProximity="300" recommendedConfidence="75">
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_cyprus_eu_national_id_card" />
          <Match idRef="Keywords_cyprus_eu_national_id_card" />
        </Pattern>
      </Entity>
```

## Keywords

### Keywords\_cyprus\_eu\_national\_id\_card

- id card number
- identity card number
- kimlik karti
- national identification number
- personal id number
- ταυτοτητασ