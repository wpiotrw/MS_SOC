---
layout: Conceptual
title: Microsoft Bing maps key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-microsoft-bing-maps-key
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-05-29T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Microsoft Bing maps key sensitive information type entity definition.
locale: en-us
document_id: da4ddee1-9eef-9e8a-1122-86d80209ec85
document_version_independent_id: da4ddee1-9eef-9e8a-1122-86d80209ec85
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-microsoft-bing-maps-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-microsoft-bing-maps-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-microsoft-bing-maps-key.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3c847666-7892-494c-aa0e-0bb3d16cc2cc
- https://authoring-docs-microsoft.poolparty.biz/devrel/9b11aaae-66fe-4b2c-9a1f-36ce40bf4e7f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e17fb6eb-4cdd-4a57-81df-0dfec430dfdd
- https://authoring-docs-microsoft.poolparty.biz/devrel/c0b42e77-fe0d-40dd-9718-99dacb85bf74
platformId: ac6966a8-55a8-8fc5-afe7-9484e0dec05a
---

# Microsoft Bing maps key entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of 64 characters consisting of letters, digits, and special characters.

## Pattern

A combination of 64 characters:

- a-z (not case-sensitive)
- 0-9
- underlines (\_)
- or hyphens (-)

format example:

`aB1cD2eF-3gH4iJ5kL6_mN7oP8qR`

## Credential format example

`bingMapsKey=aB1cD2eF-3gH4iJ5kL6-mN7oP8qR`

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to call [Bing Maps API.](/en-us/bingmaps/getting-started/bing-maps-dev-center-help/getting-a-bing-maps-key)

It uses several primary resources:

- Patterns of Base64 URL encoded 384-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKey384Url:

- virtualearth
- api/maps
- key