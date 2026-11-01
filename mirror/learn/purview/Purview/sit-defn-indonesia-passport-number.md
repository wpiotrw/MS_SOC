---
layout: Conceptual
title: Indonesia passport number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-indonesia-passport-number
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-10-08T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Indonesia passport number sensitive information type entity definition.
locale: en-us
document_id: 5aad4122-9290-5361-fca2-94581427040b
document_version_independent_id: 5aad4122-9290-5361-fca2-94581427040b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-indonesia-passport-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-indonesia-passport-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-indonesia-passport-number.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 936470ab-3720-ee0c-a0ff-edab422b6a21
---

# Indonesia passport number entity definition | Microsoft Learn

## Format

Seven to Nine alphanumeric characters

## Pattern

- one or two letters
- followed by six or seven digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regex `Regex_indonesia_passport_number` finds content that matches the pattern.
- A keyword from `Keyword_indonesia_passport_numbe` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regex `Regex_indonesia_passport_number` finds content that matches the pattern.

```xml
    <!-- Indonesia Passport Number -->
    <Entity id="d0001c83-e72f-4360-98d3-f5a41dc5a380" patternsProximity="300" recommendedConfidence="75" relaxProximity="true">
      <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_indonesia_passport_number" />
        <Match idRef="Keyword_indonesia_passport_number" />
      </Pattern>
      <Pattern confidenceLevel="65">
        <IdMatch idRef="Regex_indonesia_passport_number" />
      </Pattern>
    </Entity>
```

## Keywords

### Keyword\_indonesia\_passport\_number

- passport#
- passport #
- passportno
- passport no
- passportnumber
- passport number
- passportnumbers
- passport numbers
- passport
- passport no.
- passportno#
- passport book
- passportbook#
- paspor
- nomor paspor
- paspornomor
- paspor no
- no. paspor.