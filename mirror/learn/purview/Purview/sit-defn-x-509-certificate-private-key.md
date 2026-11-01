---
layout: Conceptual
title: X.509 certificate private key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-x-509-certificate-private-key
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
description: X.509 certificate private key sensitive information type entity definition.
locale: en-us
document_id: 701b515d-9698-4b25-cad4-dc81c02d542c
document_version_independent_id: 701b515d-9698-4b25-cad4-dc81c02d542c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-x-509-certificate-private-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-x-509-certificate-private-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-x-509-certificate-private-key.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e8ea0d48-b19f-76e7-0054-5d3a60af242e
---

# X.509 certificate private key entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of up to 20,000 characters consisting of letters, digits, and special characters.

or

A combination of up to 40 characters consisting of upper-case letters, space, and dashes.

## Pattern

A combination of up to 20,000 characters:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- Up to two equal signs (==)

format example:

`cD2eF3gH4iJ5kL6mN7/oP+qR9sT=`

or

five dashes (-)

And a combination of up to 30 characters:

- A-Z (case-sensitive)
- spaces
- 5 dashes (-)

for example:

`-----BEGIN PRIVATE KEY-----`

## Credential format example

`-----BEGIN PRIVATE KEY----- cD2eF3gH4iJ5kL6mN7/oP+qR9sT=...`

Important

This example has been truncated. It’s not a detectable example of this SIT.

## Checksum

Yes

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used as a private component in [SSL certificates.](/en-us/azure/key-vault/certificate-scenarios)

It uses several primary resources:

- Patterns of Base64 encoded string literal.
- Patterns of Certificate private key header.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_Base64EncodedStringLiteral:

- MII

### Keyword\_CertificatePrivateKeyHeader:

- key