---
layout: Conceptual
title: Saudi Arabia National ID entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-saudi-arabia-national-id
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-09-13T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Saudi Arabia National ID sensitive information type entity definition.
locale: en-us
document_id: 6a00a407-acd3-1c2f-9e3e-5204aa7853bd
document_version_independent_id: 6a00a407-acd3-1c2f-9e3e-5204aa7853bd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-saudi-arabia-national-id.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-saudi-arabia-national-id
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-saudi-arabia-national-id.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: d0be92cb-64aa-f9aa-ffaf-fc53802ebcab
---

# Saudi Arabia National ID entity definition | Microsoft Learn

## Format

10 digits

## Pattern

10 consecutive digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_saudi_arabia_national_id` finds content that matches the pattern.
- A keyword from `Keyword_saudi_arabia_national_id` is found.

```xml
<!-- Saudi Arabia National ID -->
<Entity id="8c5a0ba8-404a-41a3-8871-746aa21ee6c0" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_saudi_arabia_national_id" />
        <Any minMatches="1">
          <Match idRef="Keyword_saudi_arabia_national_id" />
        </Any>
    </Pattern>
</Entity>
```

## Keywords

### Keyword\_saudi\_arabia\_national\_id

- Identification Card
- I card number
- ID number
- الوطنية الهوية بطاقة رقم