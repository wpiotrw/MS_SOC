---
layout: Conceptual
title: India unique identification (Aadhaar) number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-india-unique-identification-number
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
description: India unique identification (Aadhaar) number sensitive information type entity definition.
locale: en-us
document_id: 9484fccc-3af2-385f-5dee-8c09203b98a4
document_version_independent_id: 9484fccc-3af2-385f-5dee-8c09203b98a4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-india-unique-identification-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-india-unique-identification-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-india-unique-identification-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: aebb17c1-19d6-2b22-0787-f5b9a469e670
---

# India unique identification (Aadhaar) number entity definition | Microsoft Learn

## Format

12 digits containing optional spaces or dashes

## Pattern

12 digits:

- A digit that isn't 0 or 1
- Three digits
- An optional space or dash
- Four digits
- An optional space or dash
- Three digits
- The final digit, which is the check digit

## Checksum

Yes

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_india_aadhaar` finds content that matches the pattern.
- A keyword from `Keyword_india_aadhar` is found.
- The checksum passes.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The function `Func_india_aadhaar` finds content that matches the pattern.
- The checksum passes.

```xml
<!-- India Unique Identification (Aadhaar) number -->
<Entity id="1ca46b29-76f5-4f46-9383-cfa15e91048f" recommendedConfidence="85" patternsProximity="300">
  <Pattern confidenceLevel="85">
     <IdMatch idRef="Func_india_aadhaar"/>
     <Match idRef="Keyword_india_aadhar"/>
  </Pattern>
  <Pattern confidenceLevel="75">
     <IdMatch idRef="Func_india_aadhaar"/>
  </Pattern>
</Entity>
```

## Keywords

### Keyword\_india\_aadhar

- aadhaar
- aadhar
- aadhar#
- uid
- आधार
- uidai