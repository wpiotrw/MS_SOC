---
layout: Conceptual
title: Ecuador unique identification number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-ecuador-unique-identification-number
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
description: Ecuador unique identification number sensitive information type entity definition.
locale: en-us
document_id: 64b04237-69e4-9f7d-a892-79c2485df1ba
document_version_independent_id: 64b04237-69e4-9f7d-a892-79c2485df1ba
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-ecuador-unique-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-ecuador-unique-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-ecuador-unique-identification-number.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a62ff464-c796-da27-1af2-be6cf60f80f5
---

# Ecuador unique identification number entity definition | Microsoft Learn

## Format

Ten digits

## Pattern

- two digits in the range of 01 to 30 or can be either 90 or 99
- followed by eight digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regex `Regex_Ecuador_Unique_Identification_Number` finds content that matches the pattern.
- A keyword from `Keyword_Ecuador_Unique_Identification_Number` is found.
- The checksum passes.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regex `Regex_Ecuador_Unique_Identification_Number` finds content that matches the pattern.
- The checksum passes.

```xml
    <!-- Ecuador Unique Identification Number -->
    <Entity id="bc99c8a0-95ea-410e-9b7c-05e51b02e469" patternsProximity="300" recommendedConfidence="85" relaxProximity="true">
      <Pattern confidenceLevel="85">
        <IdMatch idRef="Regex_Ecuador_Unique_Identification_Number" />
        <Match idRef="Keyword_Ecuador_Unique_Identification_Number" />
      </Pattern>
      <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_Ecuador_Unique_Identification_Number" />
      </Pattern>
    </Entity>
```

## Keywords

### Keyword\_Ecuador\_Unique\_Identification\_Number

- Identity card
- Id card
- idnumber#
- id number
- identity no
- identitynumber#
- identity number
- National insurance
- national identification number
- national id
- NI Number
- NI No.
- NI #
- NI#
- insurance#
- insurancenumber
- nationalinsurance#
- nationalinsurancenumber
- national insurance number
- Seguro
- número de seguro Nacional
- numero de seguro
- numero de identidad
- Identificación nacional