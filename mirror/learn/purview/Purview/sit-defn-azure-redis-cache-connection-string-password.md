---
layout: Conceptual
title: Azure Redis cache connection string password entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-redis-cache-connection-string-password
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-10T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Azure Redis cache connection string password sensitive information type entity definition.
locale: en-us
document_id: 04db57db-b95c-2928-9e99-d4b949222519
document_version_independent_id: 04db57db-b95c-2928-9e99-d4b949222519
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-redis-cache-connection-string-password.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-redis-cache-connection-string-password
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-redis-cache-connection-string-password.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f80a1aa9-ec39-45c7-bff1-e6916def6921
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b47bd505-a970-48d0-a7c0-cc58500975e6
platformId: a3566def-31ef-c335-8257-7d146fceb81f
---

# Azure Redis cache connection string password entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of up to 20,000-characters consisting of letters, digits, and special characters.

or

A combination of 44-characters consisting of letters, digits, and special characters.

## Pattern

Any combination of up to 20,000 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- Up to 2 equal signs (=)

format example:

`aB1cD2eF/3gH4iJ5kL6-mN7oP8qR=`

or

Any combination of 43 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- ends with an equal sign (=)

format example:

`iJ5kL6mN7oP8qR9sT0+uV1wX2yZ==`

## Credential example

`HostName=account.redis.cache.windows.net;Password=\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Checksum

Yes

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that’s used to connect to [Azure Cache for Redis servers](/en-us/azure/azure-cache-for-redis/).

It uses several primary resources:

- Patterns of Base64 encoded string literal.
- Patterns of Base64 encoded 256-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, ID.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_Base64EncodedStringLiteral:

- MII

### Keyword\_SymmetricKey256:

- SharedAccessKey
- AccountKey