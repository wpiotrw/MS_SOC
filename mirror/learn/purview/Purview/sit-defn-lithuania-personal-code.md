---
layout: Conceptual
title: Lithuania personal code entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-personal-code
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
description: Lithuania personal code sensitive information type entity definition.
locale: en-us
document_id: 6d927335-cba8-c720-195e-b76b859152a1
document_version_independent_id: 6d927335-cba8-c720-195e-b76b859152a1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-lithuania-personal-code.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-lithuania-personal-code
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-lithuania-personal-code.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 51f924fb-560f-297e-4a65-9faed33368eb
---

# Lithuania personal code entity definition | Microsoft Learn

## Format

11 digits without spaces and delimiters

## Pattern

11 digits without spaces and delimiters:

- one digit (1-6) that corresponds to the person's gender and century of birth
- six digits that correspond to birth date (YYMMDD)
- three digits that correspond to the serial number of the date of birth
- one check digit

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_lithuania_eu_tax_file_number` finds content that matches the pattern.
- A keyword from `Keywords_lithuania_eu_tax_file_number` is found.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_lithuania_eu_tax_file_number` finds content that matches the pattern.

```xml
      <!-- Lithuania Personal Code -->
      <Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_lithuania_eu_tax_file_number" />
          <Match idRef="Keywords_lithuania_eu_tax_file_number" />
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_lithuania_eu_tax_file_number" />
          <Any minMatches="0" maxMatches="0">
            <Match idRef="Keywords_lithuania_eu_telephone_number" />
            <Match idRef="Keywords_lithuania_eu_mobile_number" />
          </Any>
        </Pattern>
      </Entity>
```

## Keywords

### Keywords\_lithuania\_eu\_national\_id\_card

- asmeninis skaitmeninis kodas
- asmens kodas
- citizen service number
- mokesčių id
- mokesčių identifikavimas numeris
- mokesčių identifikavimo numeris
- mokesčių numeris
- national identification number
- personal code
- personal numeric code
- piliečio paslaugos numeris
- tax id
- tax identification no
- tax identification number
- tax no#
- tax no
- tax number
- tax registration number
- taxid#
- taxidno#
- taxidnumber#
- taxno#
- taxnumber#
- taxnumber
- tin id
- tin no
- tin#
- unikalus identifikavimo kodas
- unikalus identifikavimo numeris
- unique identification number
- unique identity number
- uniqueidentityno#