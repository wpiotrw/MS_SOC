---
layout: Conceptual
title: General Symmetric key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-general-symmetric-key
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
description: General Symmetric key sensitive information type entity definition.
locale: en-us
document_id: 8b25859c-15b4-e278-9103-161401019613
document_version_independent_id: 8b25859c-15b4-e278-9103-161401019613
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-general-symmetric-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-general-symmetric-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-general-symmetric-key.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
2PlusCloud:
- Azure
- M365
- Power
__autotagging_hash:
- 8BFF7D56C4FA55E8A7DA98EBD49B8BE8C86360CEFBFA9411E39DB1CAD33A8C95
platformId: cbf7482d-929a-39c3-a047-b7f0b3a33a44
---

# General Symmetric key entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of 44 characters consisting of letters, digits, and special characters.

or

A combination of 88 characters consisting of letters, digits, and special characters.

## Pattern

A combination of 43 characters:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/) or plus signs (+)
- ends with an equal sign (=)

format example:

`Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0Kk1Ll2Mm34/+Nn=`

or

A combination of 86 characters:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/) or plus signs (+)
- ends with two equal signs (=)

format example:

`Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0Kk1Ll2Mm3Nn4/+==`

## Credential example

| Confidence Band | Example |
| --- | --- |
| High | `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>` |
| Medium | `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>` |
| Low | `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>` |

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used in [general authentication process.](/en-us/dotnet/api/system.security.cryptography.aes?view=net-5.0&amp;preserve-view=true)

It uses several primary resources:

- Patterns of Base64 encoded 256-bits symmetric key.
- Patterns of Base64 encoded 512-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, Id, AccountName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKey256:

- SharedAccessKey
- AccountKey

### Keyword\_SymmetricKey512:

- SharedAccessKey
- AccountKey