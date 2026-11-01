---
layout: Conceptual
title: Singapore national registration identity card (NRIC) number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-singapore-national-registration-identity-card-number
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
description: Singapore national registration identity card (NRIC) number sensitive information type entity definition.
locale: en-us
document_id: 9128bd57-ec1f-68d4-ffaf-bc0a453d0253
document_version_independent_id: 9128bd57-ec1f-68d4-ffaf-bc0a453d0253
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-singapore-national-registration-identity-card-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-singapore-national-registration-identity-card-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-singapore-national-registration-identity-card-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: cc9a05a7-6e9e-128f-ff0e-3ebb7c6f8f83
---

# Singapore national registration identity card (NRIC) number entity definition | Microsoft Learn

## Format

Nine letters and digits

## Pattern

- Nine letters and digits:

    - the letter "F," "G," "M," "S," or "T" (not case-sensitive)
    - seven digits
    - an alphabetic check digit

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_singapore_nric` finds content that matches the pattern.
- A keyword from `Keyword_singapore_nric` is found.
- The checksum passes.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_singapore_nric` finds content that matches the pattern.
- The checksum passes.

```xml
      <!-- Singapore National Registration Identity Card (NRIC) Number -->

      <Entity id="cead390a-dd83-4856-9751-fb6dc98c34da" patternsProximity="300" recommendedConfidence="75" relaxProximity="true">
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Regex_singapore_nric" />
        </Pattern>
        <Version minEngineVersion="15.20.0191.000" maxEngineVersion="15.20.8124.999">
          <Pattern confidenceLevel="85">
            <IdMatch idRef="Regex_singapore_nric" />
            <Match idRef="Keyword_singapore_nric" />
          </Pattern>
          <Pattern confidenceLevel="75">
            <IdMatch idRef="Regex_singapore_nric" />
          </Pattern>
        </Version> 
        <Version minEngineVersion="15.20.8125.000">
          <Pattern confidenceLevel="85">
            <IdMatch idRef="Func_singapore_nric" />
            <Match idRef="Keyword_singapore_nric" />
          </Pattern>
          <Pattern confidenceLevel="75">
            <IdMatch idRef="Func_singapore_nric" />
          </Pattern>
        </Version>
      </Entity>
```

## Keywords

### Keyword\_singapore\_nric

- National Registration Identity Card
- Identity Card Number
- NRIC
- IC
- Foreign Identification Number
- FIN
- 身份证
- 身份證