---
layout: Conceptual
title: International banking account number (IBAN) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-international-banking-account-number
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-06-01T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: International banking account number (IBAN) sensitive information type entity definition.
locale: en-us
document_id: deeab446-482d-5faf-5015-388bf0528c93
document_version_independent_id: deeab446-482d-5faf-5015-388bf0528c93
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-international-banking-account-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-international-banking-account-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-international-banking-account-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 69b05a61-e050-e752-5d93-7999f1cbd8c4
---

# International banking account number (IBAN) entity definition | Microsoft Learn

## Format

Country code (two letters) plus check digits (two digits) plus bban number (up to 30 characters)

## Pattern

Pattern must include all of these patterns:

- Two-letter country code
- Two check digits (followed by an optional space)
- 1-7 groups of four letters or digits (can be separated by spaces)
- 1-3 letters or digits

The format for each country/region is slightly different. The IBAN sensitive information type covers these 68 countries:

- ad
- ae
- al
- at
- az
- ba
- be
- bg
- bh
- br
- ch
- cr
- cy
- cz
- de
- dk
- do
- ee
- es
- fi
- fo
- fr
- gb
- ge
- gi
- gl
- gr
- gt
- hr
- hu
- ie
- il
- is
- it
- jo
- kw
- kz
- lb
- li
- lt
- lu
- lv
- mc
- md
- me
- mk
- mr
- mt
- mu
- nl
- no
- pk
- pl
- ps
- pt
- qa
- ro
- rs
- sa
- se
- si
- sk
- sm
- tl
- tn
- tr
- vg
- xk

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_iban` finds content that matches the pattern.
- The checksum passes.

```xml
<Entity id="e7dc4711-11b7-4cb0-b88b-2c394a771f0e" patternsProximity="300" recommendedConfidence="85">
  <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_iban" />
  </Pattern>
</Entity>
```

## Keywords

None