---
layout: Conceptual
title: All full names entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names
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
description: All full names sensitive information type entity definition.
locale: en-us
document_id: cea8be78-ff85-495f-bbd5-687b03e56cd0
document_version_independent_id: cea8be78-ff85-495f-bbd5-687b03e56cd0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-all-full-names.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-all-full-names
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-all-full-names.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
platformId: 4241a118-d1e5-2555-ae32-1bfd10eb3f32
---

# All full names entity definition | Microsoft Learn

All full names is a bundled named entity. It detects full names for people from all supported countries/regions, which include Australia, China, Japan, U.S., and countries/regions in the EU. Use this SIT to detect all possible matches of full names.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a bundled SIT in an endpoint DLP policy. This requirement is specific to the combination of bundled SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

Various.

## Pattern

Various.

## Checksum

No.

## Keyword Highlighting

Not supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Cloud Support

Cloud support is available for the following:

- Microsoft Commercial Cloud
- Microsoft Government Community Cloud
- Microsoft 365 Government Community Cloud High
- Microsoft 365 Department of Defense

## Description

This named entity SIT matches personal names that a human would identify as a name with high confidence. For example, if a string is found consisting of a given name and is followed by a family name then a match is made with high confidence. It uses three primary resources:

- A dictionary of given names.
- A dictionary of family names.
- Patterns of how names are formed.

The three resources are different for each country/region. The strings *Olivia Wilson* would trigger a match. Common given/family names are given a higher confidence than rarer names. However, the pattern also allows partial matches. If a given name from the dictionary is found and it's followed by a family name that isn't in the dictionary, then a partial match is triggered. For example, *Tomas Richard* would trigger a partial match. Partial matches are given lower confidence.

In addition, patterns that a human would see as indicative of names are also matched with appropriate confidence. Like *O. Wilson*, *O.P. Wilson*, *Dr. O. P. Wilson*, *Wilson, O.P.* or *T. Richard, Jr.* would be matches.

## Supported languages

- English
- Bulgarian
- Croatian
- Czech
- Danish
- Estonian
- Finnish
- French
- German
- Hungarian
- Icelandic
- Irish
- Italian
- Japanese
- Latvian
- Lithuanian
- Maltese
- Dutch
- Norwegian
- Polish
- Portuguese
- Romanian
- Slovak
- Slovenian
- Spanish
- Swedish
- Turkish