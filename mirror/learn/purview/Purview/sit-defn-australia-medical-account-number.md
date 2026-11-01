---
layout: Conceptual
title: Australia medical account number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-australia-medical-account-number
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
description: Australia medical account number sensitive information type entity definition.
locale: en-us
document_id: 0179c957-ee3f-a47f-1ed1-9c9f60daadf9
document_version_independent_id: 0179c957-ee3f-a47f-1ed1-9c9f60daadf9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-australia-medical-account-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-australia-medical-account-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-australia-medical-account-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 99715799-6a39-357c-9930-8929afe001fa
---

# Australia medical account number entity definition | Microsoft Learn

## Format

10-11 digits

## Pattern

10-11 digits:

- First digit is in the range 2-6
- Ninth digit is a check digit
- Tenth digit is the issue digit
- 11th digit (optional) is the individual number

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function Func\_australian\_medical\_account\_number finds content that matches the pattern.
- A keyword from Keyword\_Australia\_Medical\_Account\_Number is found.
- The checksum passes.

```xml
  <!-- Australia Medical Account Number -->
<Entity id="104a99a0-3d3b-4542-a40d-ab0b9e1efe63" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
     <IdMatch idRef="Func_australian_medical_account_number"/>
     <Match idRef="Keyword_Australia_Medical_Account_Number"/>
    </Pattern>
</Entity>
```

## Keywords

### Keyword\_Australia\_Medical\_Account\_Number

- bank account details
- medicare payments
- mortgage account
- bank payments
- information branch
- credit card loan
- department of human services
- local service
- medicare