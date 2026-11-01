---
layout: Conceptual
title: Ukraine Passport Number (Domestic) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-ukraine-passport-domestic
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
description: Ukraine Passport Number (Domestic) sensitive information type entity definition.
locale: en-us
document_id: dbaa8e26-12c9-55b7-4a4d-484a97e4f257
document_version_independent_id: dbaa8e26-12c9-55b7-4a4d-484a97e4f257
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-ukraine-passport-domestic.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-ukraine-passport-domestic
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-ukraine-passport-domestic.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 56a99570-e0cc-3f89-344f-25b77450e6e6
---

# Ukraine Passport Number (Domestic) entity definition | Microsoft Learn

## Format

nine digits

## Pattern

nine digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regex `Regex_Ukraine_Passport_Domestic` finds content that matches the pattern.
- A keyword from `Keyword_Ukraine_Passport_Domestic` is found.

```xml
      <!-- Ukraine Passport Domestic -->
      <Entity id="1817a540-221f-4459-9202-3bd78b81d803" patternsProximity="300" recommendedConfidence="75">
        <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_Ukraine_Passport_Domestic"/>
          <Match idRef="Keyword_Ukraine_Passport_Domestic"/>
        </Pattern>
      </Entity>
```

## Keywords

### Keyword\_ukraine\_passport\_domestic

- ukraine passport
- passport number
- passport no
- паспорт України
- номер паспорта
- персональний