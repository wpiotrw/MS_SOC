---
layout: Conceptual
title: Swiss Social Security Number AHV entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-switzerland-ssn-ahv-number
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
description: Swiss Social Security Number AHV (Alters- und Hinterlassenenversicherung) sensitive information type entity definition.
locale: en-us
document_id: 553d3da9-9348-4c84-866f-f086cc4406ba
document_version_independent_id: 553d3da9-9348-4c84-866f-f086cc4406ba
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-switzerland-ssn-ahv-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-switzerland-ssn-ahv-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-switzerland-ssn-ahv-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 41ef8351-9684-cc42-c565-e3e740a79a24
---

# Swiss Social Security Number AHV entity definition | Microsoft Learn

The Swiss Social Security Number AHV (Alters- und Hinterlassenenversicherung) is a unique personal identification number used in Switzerland.

## Format

13-digit number

## Pattern

13-digit number:

- three digits - 756
- an optional dot
- four digits
- an optional dot
- four digits
- an optional dot
- two digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A data loss prevention (DLP) policy has high confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_swiss_social_security_number_ahv` finds content that matches the pattern.
- A keyword from `Keywords_swiss_social_security_number_ahv` is found.

A DLP policy has medium confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_swiss_social_security_number_ahv` finds content that matches the pattern.

```xml
      <!-- Swiss SSN AHV Number -->
      <Entity id="277cfa4b-6eaa-4a1b-9492-099dec849971" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_swiss_social_security_number_ahv" />
          <Match idRef="Keywords_swiss_social_security_number_ahv" />
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_swiss_social_security_number_ahv" />
        </Pattern>
      </Entity>
```

## Keywords

The following keywords are used for detection. These include Social Security Number (SSN) and AHV variations in multiple languages.

### Keyword\_swiss\_ssn\_AHV\_number

- `ahv`
- `ssn`
- `pid`
- `insurance number`
- `personalidno#`
- `social security number`
- `personal id number`
- `personal identification no.`
- `insuranceno#`
- `uniqueidno#`
- `unique identification no.`
- `avs number`
- `personal identity no versicherungsnummer`
- `identifikationsnummer`
- `einzigartige identität nicht`
- `sozialversicherungsnummer`
- `identification personnelle id`
- `numéro de sécurité sociale`