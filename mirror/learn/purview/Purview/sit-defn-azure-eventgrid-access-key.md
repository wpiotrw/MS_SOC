---
layout: Conceptual
title: Azure EventGrid access key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-eventgrid-access-key
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-07T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Azure EventGrid access key sensitive information type entity definition.
locale: en-us
document_id: 1379bf0c-3381-511b-c2b8-6ecf3315a196
document_version_independent_id: 1379bf0c-3381-511b-c2b8-6ecf3315a196
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-eventgrid-access-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-eventgrid-access-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-eventgrid-access-key.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 9cbb62d3-6dae-e6a5-a2fc-9afe70de2233
---

# Azure EventGrid access key entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of 43 characters consisting of letters, digits, and special characters ending in an equals sign (=) that isn't part of the pattern.

## Pattern

A combination of 43 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)

for example:

`A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u+`

## Credential example

`<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to authenticate an application publishing events to [Azure Event Grid resources (topics and domains).](/en-us/azure/event-grid/get-access-keys)

It uses several primary resources:

- Patterns of Base64 encoded 256-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, ID.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKey256:

- SharedAccessKey
- AccountKey