---
layout: Conceptual
title: Mexico Unique Population Registry Code (CURP) entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-mexico-unique-population-registry-code
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
description: Mexico Unique Population Registry Code (CURP) sensitive information type entity definition.
locale: en-us
document_id: 37a33bf3-a655-7206-bd12-aa2ffc82fd00
document_version_independent_id: 37a33bf3-a655-7206-bd12-aa2ffc82fd00
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-mexico-unique-population-registry-code.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-mexico-unique-population-registry-code
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-mexico-unique-population-registry-code.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: ced3eb19-4bf2-40f2-b260-d96203dd61fe
---

# Mexico Unique Population Registry Code (CURP) entity definition | Microsoft Learn

## Format

18 character alphanumeric pattern

## Pattern

- four letters (case insensitive)
- six digits indicating a valid date
- a letter - H/h or M/m
- two letters indicating a valid Mexican state code
- three letters
- one letter or digit
- one digit

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_mexico_population_registry_code` finds content that matches the pattern.
- A keyword from `Keyword_mexico_population_registry_code` is found.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_mexico_population_registry_code` finds content that matches the pattern.

```xml
    <!-- Mexico Unique Population Registry Code (CURP) -->
      <Entity id="e905ad4d-5a74-406d-bf36-b1efca798af4" patternsProximity="300" recommendedConfidence="75" relaxProximity="true">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_mexico_population_registry_code" />
          <Match idRef="Keyword_mexico_population_registry_code" />
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_mexico_population_registry_code" />
        </Pattern>
      </Entity>
```

## Keywords

### Keyword\_mexico\_population\_registry\_code

- Clave Única de Registro de Población
- Clave Unica de Registro de Poblacion
- Unique Population Registry Code
- unique population code
- CURP
- Personal ID
- Unique ID
- personalid
- personalidnumber
- uniqueidkey
- uniqueidnumber
- clave única
- clave unica
- clave personal Identidad
- personal Identidad Clave
- ClaveÚnica
- claveunica
- clavepersonalIdentidad