---
layout: Conceptual
title: Azure Bot Framework secret key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-bot-framework-secret-key
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-06T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Azure Bot Framework secret key sensitive information type entity definition.
locale: en-us
document_id: 33610d4a-8c1f-5c21-4711-f92607a51f28
document_version_independent_id: 33610d4a-8c1f-5c21-4711-f92607a51f28
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-bot-framework-secret-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-bot-framework-secret-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-bot-framework-secret-key.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: d15062b2-841a-384e-5c96-dfdd6ac09c28
---

# Azure Bot Framework secret key entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of 55 characters consisting of letters, digits, and special characters.

or

A combination of 63 characters consisting of letters, digits, and special characters.

## Pattern

A combination of 55 characters:

- a-z (not case-sensitive)
- 0-9
- underlines (\_)
- or dots (.)

for the 63 characters

A combination of 11 characters:

- a-z (not case-sensitive)
- 0-9
- dashes (-)
- or underlines (\_)
- a dot

A combination of three characters:

- a-z (not case-sensitive)
- 0-9
- dashes (-)
- or underlines (\_)
- a dot

A combination of three characters:

- a-z (not case-sensitive)
- 0-9
- dashes (-)
- or underlines (\_)
- a dot

A combination of 43 characters

- a-z (not case-sensitive)
- 0-9
- dashes (-)
- or underlines (\_)

format example:

`Gg7Hh~8Ii9.-Jj0Kk1Ll2Mm3Nn4Oo5_Pp6Qq7Rr8`

## Credential example

`<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to connect to [WebChat channels from Azure Bot services.](/en-us/azure/bot-service/bot-service-channel-connect-webchat?view=azure-bot-service-4.0)

It uses several primary resources:

- Patterns of Base64 URL encoded 328-bits symmetric key.
- Patterns of Base64 URL encoded 360-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKey328Url:

- botframework
- key

### Keyword\_SymmetricKey360Url:

- botframework
- key