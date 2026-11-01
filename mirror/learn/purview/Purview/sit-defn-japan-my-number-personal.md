---
layout: Conceptual
title: Japanese My Number Personal entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-japan-my-number-personal
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
description: Japanese My Number Personal sensitive information type entity definition.
locale: en-us
document_id: 9a0499ec-4ac0-89aa-b5e0-85b2a66563bf
document_version_independent_id: 9a0499ec-4ac0-89aa-b5e0-85b2a66563bf
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-japan-my-number-personal.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-japan-my-number-personal
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-japan-my-number-personal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 0732e547-c9fe-2bba-a85f-5c36ca608cf5
---

# Japanese My Number Personal entity definition | Microsoft Learn

## Format

12-digit number

## Pattern

12-digit number:

- four digits
- an optional space, dot, or hyphen
- four digits
- an optional space, dot, or hyphen
- four digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A data loss prevention (DLP) policy has high confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_japanese_my_number_personal` finds content that matches the pattern.
- A keyword from `Keywords_japanese_my_number_personal` is found.

A DLP policy has low confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_japanese_my_number_personal` finds content that matches the pattern.

```xml
      <!-- Japanese My Number – Personal -->
      <Entity id="98da8e66-7299-4ebd-9f82-c871ab37d3ef" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_japanese_my_number_personal" />
          <Match idRef="Keywords_japanese_my_number_personal" />
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Func_japanese_my_number_personal" />
        </Pattern>
      </Entity>
```

## Keywords

### Keyword\_japan\_my\_number\_personal

- my number
- マイナンバー
- 個人番号
- 共通番号
- マイナンバーカード
- マイナンバーカード番号
- 個人番号カード
- 個人識別番号
- 個人識別ナンバー
- 通知カード