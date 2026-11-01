---
layout: Conceptual
title: Azure Shared Access key / Web Hook token signature entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-shared-access-key-web-hook-token
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
description: Azure Shared Access key / Web Hook token sensitive information type entity definition.
locale: en-us
document_id: 8aa1acab-7eb0-674b-1f88-2232192c6895
document_version_independent_id: 8aa1acab-7eb0-674b-1f88-2232192c6895
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-shared-access-key-web-hook-token.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-shared-access-key-web-hook-token
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-shared-access-key-web-hook-token.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: f68440e7-4158-c71e-d42f-6c0cd11e42be
---

# Azure Shared Access key / Web Hook token signature entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of 44 characters consisting of letters, digits, and special characters.

or

A combination of up to 76 characters consisting of letters, digits, and special characters.

## Pattern

Any combination of 43 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- ends with an equal sign (=)

format example:

`gH4iJ5kL6mN7oP8qR9/sT0uV1wX=`

or

A combination of 43 to 73 characters consisting of:

- a-z (case insensitive)
- 0-9
- percent signs (%)
- ends with a suffix '%3d' (case insensitive)

for example:

`abcdefghijklmnopqrstuvwxyz0123456789%2F%2BABCDE%3D`

## Credential format example

`PrimaryKey=mN7oP8qR9sT0uV1wX2%yZ3aB4dE%3d;`

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to access general [Azure resources with restricted permission](/en-us/azure/notification-hubs/notification-hubs-push-notification-security).

It uses several primary resources:

- Patterns of Base64 encoded 256-bits symmetric key.
- Patterns of URL Encoded 256-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, ID.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary

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