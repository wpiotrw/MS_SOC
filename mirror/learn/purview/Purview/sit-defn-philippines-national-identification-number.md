---
layout: Conceptual
title: Philippines National ID entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-philippines-national-identification-number
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
description: Philippines National ID sensitive information type entity definition.
locale: en-us
document_id: e22caadc-b60d-5eeb-dd8d-800ab418e78d
document_version_independent_id: e22caadc-b60d-5eeb-dd8d-800ab418e78d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-philippines-national-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-philippines-national-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-philippines-national-identification-number.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c7959f3c-2c30-ba34-3cb2-bb885a2998ba
---

# Philippines National ID entity definition | Microsoft Learn

## Format

Twelve digits plus optional delimiters

## Pattern

- four digits
- followed by hyphen (optional)
- four digits
- followed by hyphen (optional)
- four digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regx `Regex_phillipines_national_id` finds content that matches the pattern.
- A keyword from `Keyword_phillipines_national_id` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regx `Regex_phillipines_national_id` finds content that matches the pattern.

```xml
<!-- Philippines National ID -->
    <Entity id="3257da62-3d98-44ca-a923-6f8b0cd94b7f" patternsProximity="300" recommendedConfidence="75" relaxProximity="true">
      <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_phillipines_national_id" />
        <Match idRef="Keyword_phillipines_national_id" />
      </Pattern>
      <Pattern confidenceLevel="65">
        <IdMatch idRef="Regex_phillipines_national_id" />
      </Pattern>
    </Entity>
```

## Keywords

### Keyword\_phillipines\_national\_id

- PhilSys
- Phil ID
- National ID
- PSN
- PhilSys Number
- ID number
- National identification number