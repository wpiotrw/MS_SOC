---
layout: Conceptual
title: Israel National ID entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-israel-national-identification-number
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-01-16T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Israel National ID sensitive information type entity definition.
locale: en-us
document_id: a73ed287-c6ee-c922-2923-1ab1a2ecbd80
document_version_independent_id: a73ed287-c6ee-c922-2923-1ab1a2ecbd80
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-israel-national-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-israel-national-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-israel-national-identification-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 99285688-de9b-3fd7-6938-4c38f96999fe
---

# Israel National ID entity definition | Microsoft Learn

## Format

nine digits

## Pattern

nine consecutive digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_israeli_national_id_number` finds content that matches the pattern.
- A keyword from `Keyword_Israel_National_ID` is found.
- The checksum passes.

```xml
<!-- Israel National ID Number -->
<Entity id="e05881f5-1db1-418c-89aa-a3ac5c5277ee" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
        <IdMatch idRef="Func_israeli_national_id_number" />
        <Any minMatches="1">
          <Match idRef="Keyword_Israel_National_ID" />
        </Any>
    </Pattern>
</Entity>
```

## Keywords

### Keyword\_Israel\_National\_ID

- תעודת זהות
- .ת.ז
- מספר זיהוי
- מספר זהות
- זהותישר אלית
- מספר הזהות
- هوية إسرائ يلية
- رقم الهوية
- بطاقة تعريف
- idnumber#
- id number
- identity no
- identitynumber#
- identity number
- israeliidentitynumber
- personal id
- unique id