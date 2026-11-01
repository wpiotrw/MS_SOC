---
layout: Conceptual
title: Taiwan Resident Certificate (ARC/TARC) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-resident-certificate-number
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
description: Taiwan Resident Certificate (ARC/TARC) sensitive information type entity definition.
locale: en-us
document_id: 7bc4e8c0-7249-faa1-dd28-e70219a59aed
document_version_independent_id: 7bc4e8c0-7249-faa1-dd28-e70219a59aed
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-taiwan-resident-certificate-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-taiwan-resident-certificate-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-taiwan-resident-certificate-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 76c84e7d-669b-ac0c-32d6-5ad24de2e6d4
---

# Taiwan Resident Certificate (ARC/TARC) entity definition | Microsoft Learn

## Format

10 letters and digits

## Pattern

10 letters and digits:

- two letters (not case-sensitive)
- eight digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_taiwan_resident_certificate` finds content that matches the pattern.
- A keyword from `Keyword_taiwan_resident_certificate` is found.

```xml
<!-- Taiwan Resident Certificate (ARC/TARC) -->
<Entity id="48269fec-05ea-46ea-b326-f5623a58c6e9" recommendedConfidence="75" patternsProximity="300">
  <Pattern confidenceLevel="75">
     <IdMatch idRef="Regex_taiwan_resident_certificate"/>
     <Match idRef="Keyword_taiwan_resident_certificate"/>
  </Pattern>
</Entity>
```

## Keywords

### Keyword\_taiwan\_resident\_certificate

- Resident Certificate
- Resident Cert
- Resident Cert.
- Identification card
- Alien Resident Certificate
- ARC
- Taiwan Area Resident Certificate
- TARC
- 居留證
- 外僑居留證
- 台灣地區居留證