---
layout: Conceptual
title: India GST Number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-india-gst-number
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
description: India GST Number sensitive information type entity definition.
locale: en-us
document_id: e46f3758-b9ab-4c3e-007b-6dd1ca0ecb69
document_version_independent_id: e46f3758-b9ab-4c3e-007b-6dd1ca0ecb69
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-india-gst-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-india-gst-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-india-gst-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 49063fcc-8107-fb42-09d5-1e2f4af9a20b
---

# India GST Number entity definition | Microsoft Learn

## Format

15 character alphanumeric pattern

## Pattern

15 letters or digits:

- two digits representing valid state code
- an optional space or dash
- ten characters representing Permanent Account Number (PAN)
- one letter or digit
- an optional space or dash
- one letter 'z' or 'Z'
- an optional space or dash
- one check digit

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_india_gst_number` finds content that matches the pattern.
- A keyword from `Keyword_india_gst_number` is found.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_india_gst_number` finds content that matches the pattern.

```xml
    <!-- India GST number  -->
      <Entity id="9f5a721c-2fd2-446a-a27e-0c02fbe4630c" patternsProximity="300" recommendedConfidence="85" relaxProximity="true">
        <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_india_gst_number" />
          <Match idRef="Keyword_india_gst_number" />
        </Pattern>
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_india_gst_number" />
        </Pattern>
      </Entity>
```

## Keywords

### Keyword\_india\_gst\_number

- gst
- gstin
- goods and services tax
- goods and service tax