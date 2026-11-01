---
layout: Conceptual
title: Philippines Unified Multi-Purpose ID Number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-philippines-unified-multi-purpose-identification-number
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
description: Philippines Unified Multi-Purpose ID Number sensitive information type entity definition.
locale: en-us
document_id: c322f56a-5da6-32c7-d509-0f3b178cfd8b
document_version_independent_id: c322f56a-5da6-32c7-d509-0f3b178cfd8b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-philippines-unified-multi-purpose-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-philippines-unified-multi-purpose-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-philippines-unified-multi-purpose-identification-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 1b4df71a-921f-ef88-d8cd-22adcb46b3c1
---

# Philippines Unified Multi-Purpose ID Number entity definition | Microsoft Learn

## Format

12 digits separated by hyphens

## Pattern

12 digits:

- four digits
- a hyphen
- seven digits
- a hyphen
- one digit

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_philippines_unified_id` finds content that matches the pattern.
- A keyword from `Keyword_philippines_id` is found.

```xml
<!-- Philippines Unified Multi-Purpose ID number -->
<Entity id="019b39dd-8c25-4765-91a3-d9c6baf3c3b3" recommendedConfidence="75" patternsProximity="300">
  <Pattern confidenceLevel="75">
     <IdMatch idRef="Regex_philippines_unified_id"/>
     <Match idRef="Keyword_philippines_id"/>
  </Pattern>
</Entity>
```

## Keywords

### Keyword\_philippines\_id

- Unified Multi-Purpose ID
- UMID
- Identity Card
- Pinag-isang Multi-Layunin ID