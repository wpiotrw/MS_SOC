---
layout: Conceptual
title: France health insurance number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-france-health-insurance-number
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
description: France health insurance number sensitive information type entity definition.
locale: en-us
document_id: a3df1547-bdfe-d359-d59b-67f32a99d861
document_version_independent_id: a3df1547-bdfe-d359-d59b-67f32a99d861
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-france-health-insurance-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-france-health-insurance-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-france-health-insurance-number.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 1efe8e25-565d-6464-a691-3d284b94129a
---

# France health insurance number entity definition | Microsoft Learn

## Format

21-digit number

## Pattern

21-digit number:

- 10 digits
- an optional space
- 10 digits
- an optional space
- a digit

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- the regex `Regex_France_Health_Insurance_Number` finds content that matches the pattern.
- a keyword from `Keyword_France_Health_Insurance_Number` is found.

```xml
      <!-- France Health Insurance Number -->
      <Entity id="9bc2069e-76df-4ff9-ac02-2f519469e236" patternsProximity="300" recommendedConfidence="75">
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_France_Health_Insurance_Number"/>
          <Match idRef="Keyword_France_Health_Insurance_Number"/>
        </Pattern>
      </Entity>
```

## Keywords

### Keyword\_France\_health\_insurance\_number

- insurance card
- carte vitale
- carte d'assuré social