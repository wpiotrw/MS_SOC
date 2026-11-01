---
layout: Conceptual
title: Greek Tax Identification Number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-greece-tax-identification-number
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
description: Greek Tax Identification Number sensitive information type entity definition.
locale: en-us
document_id: 658751a3-ba1e-605d-cb84-b7a035776f17
document_version_independent_id: 658751a3-ba1e-605d-cb84-b7a035776f17
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-greece-tax-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-greece-tax-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-greece-tax-identification-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: c1e7c278-c2a3-6f13-9f76-5cbe3a4b3312
---

# Greek Tax Identification Number entity definition | Microsoft Learn

## Format

Nine digits without spaces and delimiters

## Pattern

Nine digits

## Checksum

Not applicable

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A data loss prevention (DLP) policy has medium confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_greece_eu_tax_file_number` finds content that matches the pattern.
- A keyword from `Keywords_greece_eu_tax_file_number` is found.

```xml
      <!-- Greek Tax Identification Number -->
      <Entity id="15a54a5a-53d4-4080-ad43-a2a4fe1d3bf7" patternsProximity="300" recommendedConfidence="75">
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_greece_eu_tax_file_number" />
          <Match idRef="Keywords_greece_eu_tax_file_number" />
        </Pattern>
      </Entity>
```

## Keywords

The following keywords are used for detection. These include the Greek tax file number (AFM) and related terms.

### Keywords\_greece\_eu\_tax\_file\_number

- `afm#`
- `afm`
- `aφμ|aφμ αριθμός`
- `aφμ`
- `tax id`
- `tax identification no`
- `tax identification number`
- `tax no#`
- `tax no`
- `tax number`
- `tax registration number`
- `tax registry no`
- `tax registry number`
- `taxid#`
- `taxidno#`
- `taxidnumber#`
- `taxno#`
- `taxnumber#`
- `taxnumber`
- `taxregistryno#`
- `tin id`
- `tin no`
- `tin#`
- `αριθμός φορολογικού μητρώου`
- `τον αριθμό φορολογικού μητρώου`
- `φορολογικού μητρώου νο`