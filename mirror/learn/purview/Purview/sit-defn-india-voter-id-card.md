---
layout: Conceptual
title: India Voter ID Card entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-india-voter-id-card
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
description: India Voter ID Card sensitive information type entity definition.
locale: en-us
document_id: b00720c0-2d10-6afa-b992-a54ee76d7e2d
document_version_independent_id: b00720c0-2d10-6afa-b992-a54ee76d7e2d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-india-voter-id-card.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-india-voter-id-card
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-india-voter-id-card.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 506d1b75-2d49-aab6-532b-e9d9db53e7a2
---

# India Voter ID Card entity definition | Microsoft Learn

## Format

10 character alphanumeric pattern

## Pattern

10 letters or digits:

- three letters
- seven digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_india_voter_id_card` finds content that matches the pattern.
- A keyword from `Keyword_india_voter_id_card` is found.

A DLP policy has low confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `Regex_india_voter_id_card` finds content that matches the pattern.

```xml
      <!-- India Voter Id Card  -->
        <Entity id="646d643f-5228-4408-acc8-f2e81a6df897" patternsProximity="300" recommendedConfidence="75" relaxProximity="true">
           <Pattern confidenceLevel="75">
             <IdMatch idRef="Regex_india_voter_id_card" />
             <Match idRef="Keyword_india_voter_id_card" />
            </Pattern>
           <Pattern confidenceLevel="65">
              <IdMatch idRef="Regex_india_voter_id_card" />
            </Pattern>
        </Entity>
```

## Keywords

### Keyword\_india\_voter\_id\_card

- voter
- voterid
- votercard
- voteridcard
- electoral photo identity card
- EPIC
- ECI
- election commmision