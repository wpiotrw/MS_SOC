---
layout: Conceptual
title: Netherlands tax identification number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-tax-identification-number
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
description: Netherlands tax identification number sensitive information type entity definition.
locale: en-us
document_id: 8a5bb8b9-4628-5283-e713-1c6faf2123fa
document_version_independent_id: 8a5bb8b9-4628-5283-e713-1c6faf2123fa
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-netherlands-tax-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-netherlands-tax-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-netherlands-tax-identification-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 288dfe51-1b53-d38b-7a35-9b3e4b042b47
---

# Netherlands tax identification number entity definition | Microsoft Learn

## Format

nine digits without spaces or delimiters

## Pattern

nine digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_netherlands_eu_tax_file_number` finds content that matches the pattern.
- A keyword from `Keywords_netherlands_eu_tax_file_number` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_netherlands_eu_tax_file_number` finds content that matches the pattern.

```xml
      <!-- Netherlands Tax Identification Number -->
      <Entity id="01f42a64-eba7-4892-a67b-398237e4ade2" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_netherlands_eu_tax_file_number" />
          <Match idRef="Keywords_netherlands_eu_tax_file_number" />
        </Pattern>
        <Pattern confidenceLevel="65">
          <IdMatch idRef="Func_netherlands_eu_tax_file_number" />
        </Pattern>
      </Entity>
```

## Keywords

### Keywords\_netherlands\_eu\_tax\_file\_number

- btw nummer
- hollânske tax identification
- hulandes impuesto id number
- hulandes impuesto identification
- identificatienummer belasting
- identificatienummer van belasting
- impuesto identification number
- impuesto number
- nederlands belasting id nummer
- nederlands belasting identificatie
- nederlands belasting identificatienummer
- nederlands belastingnummer
- nederlandse belasting identificatie
- netherlands tax identification
- netherland's tax identification
- netherlands tin
- netherland's tin
- tax id
- tax identification no
- tax identification number
- tax identification tal
- tax no#
- tax no
- tax number
- tax registration number
- tax tal
- taxid#
- taxidno#
- taxidnumber#
- taxno#
- taxnumber#
- taxnumber
- tin id
- tin no
- tin#