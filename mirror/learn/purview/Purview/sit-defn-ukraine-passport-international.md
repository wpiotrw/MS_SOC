---
layout: Conceptual
title: Ukraine Passport Number (International) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-ukraine-passport-international
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
description: Ukraine Passport Number (International) sensitive information type entity definition.
locale: en-us
document_id: 37b6256c-291c-a3f7-d520-d35e8f2a7ac3
document_version_independent_id: 37b6256c-291c-a3f7-d520-d35e8f2a7ac3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-ukraine-passport-international.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-ukraine-passport-international
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-ukraine-passport-international.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 492d1302-1ad1-894c-1de2-07ef98b346ae
---

# Ukraine Passport Number (International) entity definition | Microsoft Learn

## Format

eight-character alphanumeric pattern

## Pattern

eight-character alphanumeric pattern:

- two letters or digits
- six digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regex `Regex_Ukraine_Passport_International` finds content that matches the pattern.
- A keyword from `Keyword_Ukraine_Passport_International` is found.

```xml
      <!-- Ukraine Passport International -->
      <Entity id="cfbe032d-22e0-4f28-ab68-d66e9641f1e2" patternsProximity="300" recommendedConfidence="75">
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_Ukraine_Passport_International"/>
          <Match idRef="Keyword_Ukraine_Passport_International"/>
        </Pattern>
      </Entity>
```

## Keywords

### Keyword\_ukraine\_passport\_international

- ukraine passport
- passport number
- passport no
- паспорт України
- номер паспорта