---
layout: Conceptual
title: Azure storage account access key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-access-key
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
description: Azure storage account access key sensitive information type entity definition.
locale: en-us
document_id: 780ffd01-036d-5e3e-aba2-c22707982231
document_version_independent_id: 780ffd01-036d-5e3e-aba2-c22707982231
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-storage-account-access-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-storage-account-access-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-storage-account-access-key.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a9a12e3a-5d9d-4197-ad96-b826bc774b60
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6dfd60ec-b0d6-48ef-9c74-057162ea03fb
platformId: ba93fbbf-83ef-03b4-3386-8f16beb5c5cd
---

# Azure storage account access key entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of up to 20,000 characters consisting of letters, digits, and special characters.

or

A combination of 88 characters consisting of letters, digits, and special characters.

## Pattern

Any combination of up to 20,000 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- Up to 2 equal signs (=)

format example:

`H4iJ5kL6mN7o==P8qR9sT0uV1wX2y/Z3a` or

Any combination of 86 characters consisting of:

a-z (not case-sensitive) 0-9 forward slashes (/) or plus signs (+) ends with two equal signs (=)

format example:

`N7oP8qR9sT0uV1wX2yZ3aB4/cD5eF6g==`

## Credential example

`<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`

## Checksum

Yes

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to make request against [Azure Storage services](/en-us/rest/api/storageservices/authorize-with-shared-key), like Blob, Queue, Table and File services.

It uses several primary resources:

- Patterns of Base64 encoded string literal.
- Patterns of Base64 encoded 512-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, Id, AccountName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_Base64EncodedStringLiteral:

- MII

### Keyword\_SymmetricKey512:

- SharedAccessKey
- AccountKey