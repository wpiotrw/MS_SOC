---
layout: Conceptual
title: International classification of diseases (ICD-9-CM) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-9-cm
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-05-29T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: International classification of diseases (ICD-9-CM) sensitive information type entity definition.
locale: en-us
document_id: b8a2a0f6-b005-ba0f-3b67-445a1d2c5009
document_version_independent_id: b8a2a0f6-b005-ba0f-3b67-445a1d2c5009
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-international-classification-of-diseases-icd-9-cm.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-international-classification-of-diseases-icd-9-cm
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-international-classification-of-diseases-icd-9-cm.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b4b3ffe9-57c4-caeb-5b07-a50488df2155
---

# International classification of diseases (ICD-9-CM) entity definition | Microsoft Learn

## Format

Dictionary

## Pattern

Keyword

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- A keyword from `Dictionary_icd_9_updated` is found.
- A keyword from `Dictionary_icd_9_codes` is found.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- A keyword from `Dictionary_icd_9_updated` is found.

```xml
    <Entity id="fa3f9c74-ee07-4c52-b5f2-085d6b2c0ec4" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Dictionary_icd_9_updated" />
          <Match idRef="Dictionary_icd_9_codes" />
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Dictionary_icd_9_updated" />
        </Pattern>
      </Entity>
```

## Keywords