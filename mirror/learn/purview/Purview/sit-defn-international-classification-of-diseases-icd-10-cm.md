---
layout: Conceptual
title: International classification of diseases (ICD-10-CM) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-10-cm
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
description: International classification of diseases (ICD-10-CM) sensitive information type entity definition.
locale: en-us
document_id: ffe635a4-f052-cd82-75ba-02aa70ccd850
document_version_independent_id: ffe635a4-f052-cd82-75ba-02aa70ccd850
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-international-classification-of-diseases-icd-10-cm.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-international-classification-of-diseases-icd-10-cm
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-international-classification-of-diseases-icd-10-cm.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 43f90de3-ea78-ca84-066e-57d71dafaec3
---

# International classification of diseases (ICD-10-CM) entity definition | Microsoft Learn

## Format

Dictionary

## Pattern

Keyword

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- A keyword from `Dictionary_icd_10_updated` is found.
- A keyword from `Dictionary_icd_10_codes` is found.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- A keyword from `Dictionary_icd_10_ updated` is found.

```xml
      <!-- ICD-10 CM -->
      <Entity id="3356946c-6bb7-449b-b253-6ffa419c0ce7" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Dictionary_icd_10_updated" />
          <Match idRef="Dictionary_icd_10_codes" />
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Dictionary_icd_10_updated" />
        </Pattern>

```

## Keywords

Any term from the `Dictionary_icd_10_updated` keyword dictionary, which is based on the [International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM)](https://icd10cmtool.cdc.gov/). This type looks only for the term, not the insurance codes.

Any term from the `Dictionary_icd_10_codes` keyword dictionary, which is based on the [International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM)](https://icd10cmtool.cdc.gov/). This type looks only for insurance codes, not the description.