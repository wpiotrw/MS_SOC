---
layout: Conceptual
title: Azure Bot service app secret entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-bot-service-app-secret
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
description: Azure Bot service app secret sensitive information type entity definition.
locale: en-us
document_id: 51af24e2-e933-c55a-9f48-2cd900b727fd
document_version_independent_id: 51af24e2-e933-c55a-9f48-2cd900b727fd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-bot-service-app-secret.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-bot-service-app-secret
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-bot-service-app-secret.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/c77662da-253d-4b38-abc0-3b65206a0557
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/26b19be3-4ba6-4089-b62b-7846d2268660
platformId: db9d1bcf-942a-9e29-6c3a-c4d065574a1c
---

# Azure Bot service app secret entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of up to 40 characters consisting of letters, digits, and special characters.

## Pattern

A combination of up to 40 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- dashes (-)
- underlines (\_)
- dots (.)
- or tilde accents (~)

for example:

`Dd4Ee~5Ff6.-Gg7Hh8Ii9Jj0Kk1Ll2_Mm3Nn4Oo5`

## Credential example

`<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`

## Checksum

Yes

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to establish secure communication between an [Azure Bot, WebChat channels and client applications](/en-us/azure/bot-service/bot-builder-concept-authentication-types?view=azure-bot-service-4.0).

It uses several primary resources:

- Patterns of Client Secret with specific format.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_AppSecret:

- secret
- password
- key