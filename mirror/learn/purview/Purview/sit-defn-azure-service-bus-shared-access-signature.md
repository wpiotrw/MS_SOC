---
layout: Conceptual
title: Azure service bus shared access signature entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-service-bus-shared-access-signature
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
description: Azure service bus shared access signature sensitive information type entity definition.
locale: en-us
document_id: fbbe000e-047c-f8f4-520c-060e74eb738e
document_version_independent_id: fbbe000e-047c-f8f4-520c-060e74eb738e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-service-bus-shared-access-signature.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-service-bus-shared-access-signature
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-service-bus-shared-access-signature.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/828c518e-a2df-46f1-8871-b760959c8fa8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/54f6b674-eb1d-48ca-9254-9665ddd64677
platformId: ee18f86a-231f-fa37-0d49-502d28377ab0
---

# Azure service bus shared access signature entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of 44-characters consisting of letters, digits, and special characters ending with an equals sign (=) that isn't part of the pattern.

or

A combination of up to 76-characters consisting of letters, digits, and special characters ending with an equals sign (=) that isn't part of the pattern.

## Pattern

Any combination of 43 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- ends with an equal sign (=) that isn't part of the pattern

format example:

`kL6mN7oP8qR9sT0uV1+wX2yZ3aB=`

or

Any combination of 43 to 73 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- or percent signs (%)
- ends with a suffix ‘%3d’ (not case-sensitive)

format example:

`mN7oP8qR9sT0uV1wX2%yZ3aB4dE%3D`

## Credential example

`<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that’s used to grant a user access to [Azure Service Bus resources](/en-us/azure/service-bus-messaging/service-bus-authentication-and-authorization) with specific rights.

It uses several primary resources:

- Patterns of Base64 encoded 256-bits symmetric key.
- Patterns of URL Encoded 256-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, ID.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKey256:

- SharedAccessKey
- AccountKey

### Keyword\_SymmetricKey256UrlEncoded:

- sig=
- key
- token
- secret
- password