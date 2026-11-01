---
layout: Conceptual
title: All Physical Addresses entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-all-physical-addresses
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
description: All Physical Addresses sensitive information type entity definition.
locale: en-us
document_id: 722fae21-a152-7a32-f341-1d3e3155226f
document_version_independent_id: 722fae21-a152-7a32-f341-1d3e3155226f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-all-physical-addresses.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-all-physical-addresses
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-all-physical-addresses.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: ffdb8bbb-2a3f-3d96-37a2-d84f8234ff68
---

# All Physical Addresses entity definition | Microsoft Learn

All physical addresses are a bundled entity SIT, which detects patterns related to physical addresses from all supported countries/regions.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a bundled SIT in an endpoint DLP policy. This requirement is specific to the combination of bundled SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

Various

## Pattern

Various

## Checksum

No

## Keyword Highlighting

Not supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Cloud Support

Cloud support is available for the following services:

- Microsoft Commercial Cloud
- Microsoft Government Community Cloud
- Microsoft 365 Government Community Cloud High
- Microsoft 365 Department of Defense

## Description

The matching of street addresses is designed to match strings that a human would identify as a street address. To achieve this matching, it uses several primary resources:

- A dictionary of settlements, counties, and regions.
- A dictionary of street suffixes, like Road, Street, or Avenue.
- Patterns of postal codes.
- Patterns of address formats.

The resources are different for each country/region. The primary resources are the patterns of address formats that are used in a given country/region. Different formats are chosen to make sure that as many addresses as possible are matched. These formats allow flexibility, for example, an address may omit the postal code or omit a town name or have a street with no street suffix. In all cases, such matches are used to increase the confidence of the match.

The patterns are designed to match individual single addresses, not generic locations. So strings such as *Redmond, WA 98052*, or *Main Street, Albuquerque* aren't matched.

## Contains

This bundled named entity SIT contains these individual SITs:

- Australia physical addresses
- Austria physical addresses
- Belgium physical addresses
- Brazil physical addresses
- Bulgaria physical addresses
- Canada physical addresses
- China physical addresses
- Croatia physical addresses
- Cyprus physical addresses
- Czech Republic physical addresses
- Denmark physical addresses
- Estonia physical addresses
- Finland physical addresses
- France physical addresses
- Germany physical addresses
- Greece physical addresses
- Greenland physical addresses
- Hungary physical addresses
- Iceland physical addresses
- Ireland physical addresses
- Italy physical addresses
- Japan physical addresses
- Latvia physical addresses
- Liechtenstein physical addresses
- Lithuania physical addresses
- Luxembourg physical addresses
- Malta physical addresses
- Netherlands physical addresses
- New Zealand physical addresses
- Norway physical addresses
- Poland physical addresses
- Portugal physical addresses
- Romania physical addresses
- Russia physical addresses
- Singapore physical addresses
- Slovakia physical addresses
- Slovenia physical addresses
- South Africa physical addresses
- Spain physical addresses
- Sweden physical addresses
- Switzerland physical addresses
- Turkey physical addresses
- Ukraine physical addresses
- United Kingdom physical addresses
- United States physical addresses

## Supported languages

- English
- Bulgarian
- Chinese
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