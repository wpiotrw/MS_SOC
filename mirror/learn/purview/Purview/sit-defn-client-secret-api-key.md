---
layout: Conceptual
title: Client secret / API key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-client-secret-api-key
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
description: Client secret / API key sensitive information type entity definition.
locale: en-us
document_id: fa6d2e52-0feb-4182-cdb9-9ccb48b562c9
document_version_independent_id: fa6d2e52-0feb-4182-cdb9-9ccb48b562c9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-client-secret-api-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-client-secret-api-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-client-secret-api-key.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f3cc9c6d-2fa5-a91f-1fd7-f1ed10330b68
---

# Client secret / API key entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A client secret or refresh token used in OAuth 2.0 protocol.

or

A combination of 24 characters consisting of letters, digits, and special characters.

or

A combination of 32 characters consisting of letters and digits.

or

A combination of 40 characters consisting of letters and digits.

or

A combination of 44 characters consisting of letters, digits, and special characters.

or

A combination of 56 characters consisting of letters, digits, and special characters

or

A combination of 88 characters consisting of letters, digits, and special characters.

## Pattern

Various client secret or refresh token formats for example:

`ClientSecret:********``AppSecret=********``ConsumerKey:=********``Refresh_Token:********`

or

A combination of 22 characters:

- a-z (not case-sensitive)
- digits, forward slashes, or plus signs
- ends with two equal signs (=)

for example:

`abcdefgh0123456789/+AB==`

or

A combination of 32 characters:

- a-f or A-F (case-sensitive)
- or 0-9

for example:

`abcdef0123456789abcdef0123456789`

or

A combination of 40 characters:

- a-f or A-F (case-sensitive)

or

- 0-9

for example:

`Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2`

or

A combination of 43 characters:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- ends with an equal sign (=)

for example:

`abcdefghijklmnopqrstuvwxyz0123456789/+ABCDE=`

or

A combination of 54 characters:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/) or plus signs (+)
- ends with two equal signs (==)

for example:

`abcdefghijklmnopqrstuvwxyz0123456789/+ABCDEFGHIJKLMNOP==`

or

A combination of 86 characters:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/) or plus signs (+)
- ends with two equal signs (=)

for example:

`abcdefghijklmnopqrstuvwxyz0123456789/+ABCDEabcdefghijklmnopqrstuvwxyz0123456789/+ABCDE==`

## Credential example

`<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's known only to the [OAuth application and the authorization server to exchange](/en-us/azure/active-directory/develop/active-directory-how-applications-are-added) for an access token at runtime.

It uses several primary resources:

- Patterns of Client secret context.
- Patterns of Base64 encoded 128 bits symmetric key.
- Patterns of Hex encoded 128 bits symmetric key.
- Patterns of Hex encoded 160 bits Symmetric Key.
- Patterns of Base64 encoded 256 bits symmetric key.
- Patterns of Base64 encoded 320 bits symmetric key.
- Patterns of Base64 encoded 512 bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, Id, AccountName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_ClientSecretContext:

- secret
- token
- auth
- securestring
- key

### Keyword\_SymmetricKey128:

- secret
- key
- password
- pw

### Keyword\_SymmetricKey128Hex:

- dapi
- key
- secret
- token
- password
- pw

### Keyword\_SymmetricKey160Hex:

- token

### Keyword\_SymmetricKey256:

- SharedAccessKey
- AccountKey

### Keyword\_SymmetricKey320:

- code=
- key

### Keyword\_SymmetricKey512:

- SharedAccessKey
- AccountKey