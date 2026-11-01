---
layout: Conceptual
title: U.S./U.K. passport number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number
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
description: U.S./U.K. passport number sensitive information type entity definition.
locale: en-us
document_id: a0412e2e-5f3e-9d25-7543-d06e73094384
document_version_independent_id: a0412e2e-5f3e-9d25-7543-d06e73094384
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-us-uk-passport-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-us-uk-passport-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-us-uk-passport-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 15e96c1a-c567-899a-a1d4-16f89165cd3e
---

# U.S./U.K. passport number entity definition | Microsoft Learn

## Format

Nine digits

## Pattern

- one letter or digit
- eight digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

### Definition

A Data Loss Prevention (DLP) policy has high confidence that it detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_usa_uk_passport` finds content that matches the pattern.
- A keyword from `Keywords_eu_passport_number` or `Keywords_uk_eu_passport_number` is found.
- A keyword from `Keywords_eu_passport_date` is found

A DLP policy has medium confidence that it detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_usa_uk_passport` finds content that matches the pattern.
- A keyword from `Keywords_eu_passport_number` or `Keywords_uk_eu_passport_number` is found.

```xml
    <!-- U.S. / U.K. Passport Number -->
    <Entity id="178ec42a-18b4-47cc-85c7-d62c92fd67f8" patternsProximity="300" recommendedConfidence="75">
       <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_usa_uk_passport" />
          <Match idRef="Keywords_eu_passport_date" />
          <Any minMatches="1">
            <Match idRef="Keywords_eu_passport_number" />
            <Match idRef="Keywords_uk_eu_passport_number" />
          </Any>
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_usa_uk_passport" />
          <Any minMatches="1">
            <Match idRef="Keywords_eu_passport_number" />
            <Match idRef="Keywords_uk_eu_passport_number" />
          </Any>
        </Pattern>
    </Entity>
```

## Keywords

### Keywords\_eu\_passport\_number

- passport#
- passport #
- passportid
- passports
- passport no
- passport no
- passportnumber
- passport number
- passport numbers
- passport numbers

### Keywords\_uk\_eu\_passport\_number

- british passport
- uk passport

### Keywords\_eu\_passport\_date

- date of issue
- date of expiry