---
layout: Conceptual
title: Taiwan National ID entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-national-identification-number
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
description: Taiwan National ID sensitive information type entity definition.
locale: en-us
document_id: 4e90290a-99ec-73f6-b709-a61277be5d73
document_version_independent_id: 4e90290a-99ec-73f6-b709-a61277be5d73
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-taiwan-national-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-taiwan-national-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-taiwan-national-identification-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 157704a7-2c42-3f85-ae93-0ef2503f6119
---

# Taiwan National ID entity definition | Microsoft Learn

## Format

One letter (in English) followed by nine digits

## Pattern

One letter (in English) followed by nine digits:

- One letter (in English, not case-sensitive)
- the digit "1" or "2"
- eight digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A data loss prevention (DLP) policy has high confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_taiwanese_national_id` finds content that matches the pattern.
- A keyword from `Keyword_taiwanese_national_id` is found.
- The checksum passes.

A DLP policy has medium confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_taiwanese_national_id` finds content that matches the pattern.
- The checksum passes.

```xml
<!-- Taiwanese National ID -->
<Entity id="4C7BFC34-8DD1-421D-8FB7-6C6182C2AF03" patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_taiwanese_national_id" />
          <Match idRef="Keyword_taiwanese_national_id" />
      </Pattern>
       <Pattern confidenceLevel="75">
         <IdMatch idRef="Func_taiwanese_national_id" />
       </Pattern>
</Entity>
```

## Keywords

### Keyword\_taiwan\_national\_id

- 身份證字號
- 身份證
- 身份證號碼
- 身份證號
- 身分證字號
- 身分證
- 身分證號碼
- 身份證號
- 身分證統一編號
- 國民身分證統一編號
- 簽名
- 蓋章
- 簽名或蓋章
- 簽章