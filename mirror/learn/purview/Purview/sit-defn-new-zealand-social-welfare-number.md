---
layout: Conceptual
title: New Zealand social welfare number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-social-welfare-number
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
description: New Zealand social welfare number sensitive information type entity definition.
locale: en-us
document_id: cae11ae4-dbe6-4a3e-1037-2b674825210b
document_version_independent_id: cae11ae4-dbe6-4a3e-1037-2b674825210b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-new-zealand-social-welfare-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-new-zealand-social-welfare-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-new-zealand-social-welfare-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: b2385c63-1f7b-3883-5291-e6b9c7a22b43
---

# New Zealand social welfare number entity definition | Microsoft Learn

## Format

nine digits

## Pattern

nine digits

- three digits
- an optional hyphen
- three digits
- an optional hyphen
- three digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_newzealand_social_welfare_number` finds content that matches the pattern.
- A keyword from `Keywords_newzealand_social_welfare_number` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_newzealand_social_welfare_number` finds content that matches the pattern.

```xml
      <!-- Newzealand Social Welfare Number -->
      <Entity id="20f3c48d-4ac1-4cd2-86bd-34ecc1826e9d" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_newzealand_social_welfare_number" />
          <Match idRef="Keywords_newzealand_social_welfare_number" />
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Func_newzealand_social_welfare_number" />
        </Pattern>
      </Entity>
    </Version>
```

## Keywords

### Keyword\_new\_zealand\_social\_welfare\_number

- social welfare #
- social welfare#
- social welfare No.
- social welfare number
- swn#