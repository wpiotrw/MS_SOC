---
layout: Conceptual
title: Colombia national ID entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-colombia-national-id
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-06-12T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Colombia national ID sensitive information type entity definition.
locale: en-us
document_id: 18103596-4fe8-a3d9-2e72-788bbe0d2c36
document_version_independent_id: 18103596-4fe8-a3d9-2e72-788bbe0d2c36
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-colombia-national-id.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-colombia-national-id
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-colombia-national-id.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: b5a7c636-bba2-c7ae-bda4-1a8771643889
---

# Colombia national ID entity definition | Microsoft Learn

## Format

Eight to 10 digits with optional separators (dots or commas).

## Pattern

Eight to 10 digits:

- Two digits followed by six digits (with optional dot or comma separators between groups of three), or
- The digit 1 followed by nine digits (with optional dot or comma separators between groups of three)

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Checksum

No

## Definition

A data loss prevention (DLP) policy has medium confidence that it detects this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_colombia_national_id_number` finds content that matches the pattern.
- A keyword from `Keywords_colombia_national_id_number` is found.

```xml
    <!-- Colombia National ID -->
    <Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_colombia_national_id_number" />
        <Match idRef="Keywords_colombia_national_id_number" />
      </Pattern>
    </Entity>
```

## Keywords

### Keywords\_colombia\_national\_id\_number

- Cedula
- Cédula
- documento de identificacion
- documento de identificación
- NUIP
- Número Único de Identificación