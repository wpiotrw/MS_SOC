---
layout: Conceptual
title: Russian Passport Number (Domestic) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-russia-passport-number-domestic
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
description: Russian Passport Number (Domestic) sensitive information type entity definition.
locale: en-us
document_id: 7012ab87-5556-3f5a-223f-f4e449fb23c0
document_version_independent_id: 7012ab87-5556-3f5a-223f-f4e449fb23c0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-russia-passport-number-domestic.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-russia-passport-number-domestic
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-russia-passport-number-domestic.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b965a4e5-29c3-208a-450e-e51067f291b1
---

# Russian Passport Number (Domestic) entity definition | Microsoft Learn

## Format

10-digit number

## Pattern

10-digit number:

- two digits
- an optional space or hyphen
- two digits
- an optional space
- six digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regex `Regex_Russian_Passport_Number_Domestic` finds content that matches the pattern.
- A keyword from `Keyword_Russian_Passport_Number` is found.

```xml
      <!-- Russian Passport Number Domestic -->
      <Entity id="76ec2f5d-cedb-48e1-8070-1998794af445" patternsProximity="300" recommendedConfidence="75">
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_Russian_Passport_Number_Domestic" />
          <Match idRef="Keyword_Russian_Passport_Number" />
        </Pattern>
      </Entity>
```

## Keywords

### Keyword\_russia\_passport\_number\_domestic

- passport number
- passport no
- passport #
- passport id
- passportno#
- passportnumber#
- паспорт нет
- паспорт id
- pоссийской паспорт
- pусский номер паспорта
- паспорт#
- паспортid#
- номер паспорта
- номерпаспорта#