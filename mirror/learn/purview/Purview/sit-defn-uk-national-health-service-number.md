---
layout: Conceptual
title: U.K. national health service number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-health-service-number
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
description: U.K. national health service number sensitive information type entity definition.
locale: en-us
document_id: 020fbf24-9f8f-9cf7-c8c4-d6529685d04b
document_version_independent_id: 020fbf24-9f8f-9cf7-c8c4-d6529685d04b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-uk-national-health-service-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-uk-national-health-service-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-uk-national-health-service-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 07746faa-e31b-ccea-a0ef-c6215d675ba2
---

# U.K. national health service number entity definition | Microsoft Learn

## Format

Ten digits separated by optional spaces

## Pattern

Ten digits:

- three digits
- a space (optional)
- three digits
- a space (optional)
- four digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_uk_nhs_number` finds content that matches the pattern.
- One of the following cases is true:
    - A keyword from `Keyword_uk_nhs_number` is found.
    - A keyword from `Keyword_uk_nhs_number1` is found.
    - A keyword from `Keyword_uk_nhs_number_dob` is found.
- The checksum passes.

```xml
<!-- U.K. NHS Number -->
<Entity id="3192014e-2a16-44e9-aa69-4b20375c9a78" patternsProximity="300" recommendedConfidence="85">
    <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_uk_nhs_number" />
        <Any minMatches="1">
          <Match idRef="Keyword_uk_nhs_number" />
          <Match idRef="Keyword_uk_nhs_number1" />
          <Match idRef="Keyword_uk_nhs_number_dob" />
        </Any>
    </Pattern>
</Entity>
```

## Keywords

### Keyword\_uk\_nhs\_number

- national health service
- nhs
- health services authority
- health authority

### Keyword\_uk\_nhs\_number1

- patient id
- patient identification
- patient no
- patient number

### Keyword\_uk\_nhs\_number\_dob

- GP
- DOB
- D.O.B
- Date of Birth
- Birth Date