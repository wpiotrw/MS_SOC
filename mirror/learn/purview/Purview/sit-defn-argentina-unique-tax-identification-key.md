---
layout: Conceptual
title: Argentina Unique Tax Identification Key (CUIT/CUIL) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-argentina-unique-tax-identification-key
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
description: Argentina Unique Tax Identification Key (CUIT/CUIL) sensitive information type entity definition.
locale: en-us
document_id: 9af2ea36-e3a8-6858-0cd9-0dfcfb28139e
document_version_independent_id: 9af2ea36-e3a8-6858-0cd9-0dfcfb28139e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-argentina-unique-tax-identification-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-argentina-unique-tax-identification-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-argentina-unique-tax-identification-key.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: a4887da0-bc3c-05d5-0117-f7950c108184
---

# Argentina Unique Tax Identification Key (CUIT/CUIL) entity definition | Microsoft Learn

## Format

11 digits with dash

## Pattern

11 digits with a dash:

- two digits in 20, 23, 24, 27, 30, 33 or 34
- a hyphen (-)
- eight digits
- a hyphen (-)
- one check digit

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_Argentina_Unique_Tax_Key` finds content that matches the pattern.
- A keyword from `Keyword_Argentina_Unique_Tax_Key` is found.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_Argentina_Unique_Tax_Key` finds content that matches the pattern.

```xml
    <!-- Argentina Unique Tax Identification Key (CUIT/CUIL) -->
      <Entity id="98da3da1-9199-4571-b7c4-b6522980b507" patternsProximity="300" recommendedConfidence="75" relaxProximity="true">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_Argentina_Unique_Tax_Key" />
          <Match idRef="Keyword_Argentina_Unique_Tax_Key" />
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_Argentina_Unique_Tax_Key" />
        </Pattern>
      </Entity>
```

## Keywords

### Keyword\_Argentina\_Unique\_Tax\_Key

- Clave Unica de Identificacion Tributaria
- CUIT
- unique code of labour identification
- Clave Única de Identificación Tributaria
- unique labour identification code
- CUIL
- Unique Tax Identification Key
- Unique Labour Identification Key
- Unique Key of Labour Identification
- Unique Work Identification Code
- Unique Code of Work Identification
- Unique Work Identification Key
- Unique Key of Work Identification
- Unique Code of Tax Identification
- Unique Key of Tax Identification
- Unique Labor Identification Code
- Unique Code of Labor Identification
- Unique Labor Identification Key
- Unique Key of Labor Identification
- tax ID
- taxID#
- taxId
- taxidnumber
- tax number
- tax no
- tax #
- tax#
- taxpayer ID
- taxpayer number
- taxpayer no
- taxpayer #
- taxpayer#
- tax identity
- tax identification
- Número de Identificación Fiscal
- número de contribuyente