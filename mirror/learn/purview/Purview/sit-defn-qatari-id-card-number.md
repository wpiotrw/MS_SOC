---
layout: Conceptual
title: Qatari ID Card Number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-qatari-id-card-number
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
description: Qatari ID Card Number sensitive information type entity definition.
locale: en-us
document_id: f0c6a154-bc01-53fc-a4fd-fcb2d7b50d8d
document_version_independent_id: f0c6a154-bc01-53fc-a4fd-fcb2d7b50d8d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-qatari-id-card-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-qatari-id-card-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-qatari-id-card-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: ebafc4ed-b75e-33d1-9e2b-c66aa0acb5f7
---

# Qatari ID Card Number entity definition | Microsoft Learn

## Format

11 digits

## Pattern

11 digits:

- a digit, either 2 or 3
- two digits representing the last two numbers of year of birth
- three digits representing ISO country code
- five digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A data loss prevention (DLP) policy has high confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_qatari\_id\_card finds content that matches the pattern.
- A keyword from Keyword\_qatari\_id\_card is found.

A DLP policy has medium confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_qatari\_id\_card finds content that matches the pattern.

```xml
     <!-- Qatari ID Card Number-->
        <Entity id="52b1b60e-a4be-4b5a-a67b-6f9bbb7811da" patternsProximity="300" recommendedConfidence="85" relaxProximity="true">
          <Pattern confidenceLevel="85">
            <IdMatch idRef="Regex_qatari_id_card" />
            <Match idRef="Keyword_qatari_id_card" />
          </Pattern>
          <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_qatari_id_card" />
          </Pattern>
        </Entity>
```

## Keywords

### Keyword\_qatari\_id\_card

- GP
- DOB
- D.O.B
- Date of Birth
- Birth Date
- date of issue
- date of expiry