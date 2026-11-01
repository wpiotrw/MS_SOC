---
layout: Conceptual
title: Japanese Residence Card Number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-japan-residence-card-number
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
description: Japanese Residence Card Number sensitive information type entity definition.
locale: en-us
document_id: b1f0f2fc-d767-1178-a8fb-66f7baf8e863
document_version_independent_id: b1f0f2fc-d767-1178-a8fb-66f7baf8e863
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-japan-residence-card-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-japan-residence-card-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-japan-residence-card-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 66846aeb-ed97-d6e6-5ece-272f87602803
---

# Japanese Residence Card Number entity definition | Microsoft Learn

## Format

Twelve letters and digits

## Pattern

Twelve letters and digits:

- two letters (not case-sensitive)
- eight digits
- two letters (not case-sensitive)

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A data loss prevention (DLP) policy has medium confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_jp_residence_card_number` finds content that matches the pattern.
- A keyword from `Keyword_jp_residence_card_number` is found.

```xml
<!--Japan Residence Card Number-->
-<Entity id="ac36fef2-a289-4e2c-bb48-b02366e89fc0" recommendedConfidence="75" patternsProximity="300">
   -<Pattern confidenceLevel="75">
      <IdMatch idRef="Regex_jp_residence_card_number"/>
      <Match idRef="Keyword_jp_residence_card_number"/>
   </Pattern>
</Entity>
```

## Keywords

### Keyword\_jp\_residence\_card\_number

- Residence card number
- Residence card no
- Residence card #
- 在留カード番号
- 在留カード
- 在留番号