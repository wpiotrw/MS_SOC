---
layout: Conceptual
title: Colombia tax identification number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-colombia-tax-identification-number
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-06-12T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Colombia tax identification number sensitive information type entity definition.
locale: en-us
document_id: 082b4ec0-97e3-2e06-2f80-37b13167a285
document_version_independent_id: 082b4ec0-97e3-2e06-2f80-37b13167a285
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-colombia-tax-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-colombia-tax-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-colombia-tax-identification-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 4b8cff0d-b4bd-f949-02ff-6fabf73a5729
---

# Colombia tax identification number entity definition | Microsoft Learn

## Format

Ten digits with a verification digit, validated by a checksum function.

## Pattern

Ten digits:

- Nine digits followed by
- One check digit (verification digit)

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Checksum

Yes

## Definition

A data loss prevention (DLP) policy has high confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_Colombian_Tax_Identification_Number` finds content that matches the pattern.
- A keyword from `Keyword_Colombian_Tax_Identification_Number` is found.

A DLP policy has medium confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_Colombian_Tax_Identification_Number` finds content that matches the pattern.

```xml
    <!-- Colombian Tax Identification Number-->
    <Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee" patternsProximity="300" recommendedConfidence="85" filters="colombian_tax_id_filter">
      <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_Colombian_Tax_Identification_Number" />
        <Match idRef="Keyword_Colombian_Tax_Identification_Number" />
      </Pattern>
      <Pattern confidenceLevel="75">
        <IdMatch idRef="Func_Colombian_Tax_Identification_Number" />
      </Pattern>
    </Entity>
```

## Keywords

### Keyword\_Colombian\_Tax\_Identification\_Number

- NIT.
- NIT
- nit.
- nit
- Nit.
- tax ID
- taxID#
- taxId
- taxidnumber
- tax number
- tax no
- tax #
- tax#
- taxpayer ID
- taxpayer number
- taxpayer no
- taxpayer #
- taxpayer#
- tax identity
- tax identification
- tin id
- tin no
- tin#