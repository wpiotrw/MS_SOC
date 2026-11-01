---
layout: Conceptual
title: New Zealand ministry of health number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-ministry-of-health-number
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
description: New Zealand ministry of health number sensitive information type entity definition.
locale: en-us
document_id: eff51f7f-8d9a-e69f-8715-eca5f1f537ea
document_version_independent_id: eff51f7f-8d9a-e69f-8715-eca5f1f537ea
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-new-zealand-ministry-of-health-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-new-zealand-ministry-of-health-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-new-zealand-ministry-of-health-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 6955824c-d704-799d-19cf-73ffeaa52ce8
---

# New Zealand ministry of health number entity definition | Microsoft Learn

## Format

three letters and four digits

## Pattern

- three letters (not case-sensitive) except 'I' and 'O'
- four digits

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_new_zealand_ministry_of_health_number` finds content that matches the pattern.
- A keyword from `Keyword_nz_terms` is found.
- The checksum passes.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_new_zealand_ministry_of_health_number` finds content that matches the pattern.
- The checksum passes.

```xml
    <!-- New Zealand Health Number -->
    <Entity id="2b71c1c8-d14e-4430-82dc-fd1ed6bf05c7" patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_new_zealand_ministry_of_health_number" />
          <Match idRef="Keyword_nz_terms" />
      </Pattern>
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_new_zealand_ministry_of_health_number" />
       </Pattern>
    </Entity>
```

## Keywords

### Keyword\_nz\_terms

- NHI
- New Zealand
- National Health Index
- NHI#
- National Health Index#