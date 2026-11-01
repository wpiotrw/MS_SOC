---
layout: Conceptual
title: Google API key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-google-api-key
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
description: Google API key sensitive information type entity definition.
locale: en-us
document_id: 08a88eb2-21fb-4987-47f4-e375ed0aead0
document_version_independent_id: 08a88eb2-21fb-4987-47f4-e375ed0aead0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-google-api-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-google-api-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-google-api-key.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
2PlusCloud:
- Azure
- M365
__autotagging_hash:
- 0224331FB8DA2C5D952AF7A195D2ACB53CEB5759E514E845398F550EC47AE56E
platformId: 831d916f-0e4c-9811-5105-ffba97452d4c
---

# Google API key entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of 39 characters consisting of letters, digits, and special characters.

## Pattern

A token prefix (case-sensitive) 'AIza'

A combination of 35 characters:

- a-z (not case-sensitive)
- 0-9
- hyphen (-)
- underline (\_)
- or backward slashes (\)

format example:

`A1bC2dE3f-4iJ5_L6mN\oP8qR9sT0u`

## Credential format example

`apiKey=A1bC2dE3f-4iJ5_L6mN\oP8qR9sT0u;`

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used as a simple encrypted string that identifies a [Google REST API client](https://cloud.google.com/docs/authentication/api-keys) without any principal that is used to associate API requests with your project for quota and billing.

It uses several primary resources:

- Patterns of Base64 encoded 210 bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKey210:

- AIza