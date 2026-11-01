---
layout: Conceptual
title: U.K. electoral roll number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-uk-electoral-roll-number
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
description: U.K. electoral roll number sensitive information type entity definition.
locale: en-us
document_id: 0d18096d-d60f-e27e-6a02-88f4b9738cb6
document_version_independent_id: 0d18096d-d60f-e27e-6a02-88f4b9738cb6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-uk-electoral-roll-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-uk-electoral-roll-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-uk-electoral-roll-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
2PlusCloud:
- Azure
- M365
- Power
__autotagging_hash:
- 3852174890B1F548E577ADBBB834201D0EC2042A0FEDFA3D5786E4BAA2C2ABB5
platformId: b1d47c57-4154-de0f-2a58-7af4ae6e6dec
---

# U.K. electoral roll number entity definition | Microsoft Learn

## Format

two letters followed by 1-4 digits

## Pattern

two letters (not case-sensitive) followed by 1-4 numbers

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_uk_electoral` finds content that matches the pattern.
- A keyword from `Keyword_uk_electoral` is found.

```xml
<!-- U.K. Electoral Number -->
<Entity id="a3eea206-dc0c-4f06-9e22-aa1be3059963" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_uk_electoral" />
        <Any minMatches="1">
          <Match idRef="Keyword_uk_electoral" />
        </Any>
    </Pattern>
</Entity>
```

## Keywords

### Keyword\_uk\_electoral

- council nomination
- nomination form
- electoral register
- electoral roll