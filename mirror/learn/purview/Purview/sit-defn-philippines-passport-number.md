---
layout: Conceptual
title: Philippines passport number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-philippines-passport-number
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
description: Philippines passport number sensitive information type entity definition.
locale: en-us
document_id: d131026a-6993-ec6d-583b-b3e1e2c0bb08
document_version_independent_id: d131026a-6993-ec6d-583b-b3e1e2c0bb08
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-philippines-passport-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-philippines-passport-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-philippines-passport-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 4db886fb-1488-acac-961a-69f0028f896a
---

# Philippines passport number entity definition | Microsoft Learn

## Format

seven or eight or nine alphanumeric characters

## Pattern

Seven or eight or nine alphanumeric characters:

- one letter followed by six digits or
- two letters followed by six digits or
- two letters followed by seven digits or
- one letter followed by seven digits followed by one letter.

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_philippines\_passport\_number finds content that matches the pattern.
- A keyword from Keyword\_philippines\_passport\_number is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_philippines\_passport\_number finds content that matches the pattern.

```xml
     <!-- Philippines Passport Number -->
     <Entity id="6fa57f91-314a-4561-8248-7ab921957448" patternsProximity="300" recommendedConfidence="85" relaxProximity="true" filters="philippines_passport_filter">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_philippines_passport_number" />
          <Match idRef="Keyword_philippines_passport_number" />
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Regex_philippines_passport_number" />
        </Pattern>
     </Entity>
```

## Keywords

### Keyword\_philippines\_passport\_number

- passport
- passport no
- passport number
- passport#
- passportno
- passport no.
- passportno#
- passport book
- passportbook#
- pasaporte
- numero ng pasaporte
- libro ng pasaporte