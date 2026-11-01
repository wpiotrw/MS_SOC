---
layout: Conceptual
title: Azure DevOps app secret entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-devops-app-secret
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
description: Azure DevOps app secret sensitive information type entity definition.
locale: en-us
document_id: 29f1d71e-5360-8557-ac8a-c636236de184
document_version_independent_id: 29f1d71e-5360-8557-ac8a-c636236de184
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-devops-app-secret.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-devops-app-secret
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-devops-app-secret.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5bd2b3fa-c186-4b92-a3c8-09f22a249d37
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7eba7926-b7b2-4a7a-bf89-e6ac53b3e7f6
platformId: 8a029b34-98b9-f340-885f-dc7a10d1177d
---

# Azure DevOps app secret entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of 52 characters consisting of letters, digits, and special characters.

## Pattern

Any combination of 52 characters consisting of:

- a-z or A-Z (case-sensitive)
- or 2-7

format example:

`A2bC2dE3fH4iJ5kL6mN7oP7qR7sT2u`

## Credential example

`<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`

Important

This example has been invalidated. It’s not a detectable example of this SIT.

## Checksum

Yes

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No**, other (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to authenticate web app users for [Azure DevOps REST API access.](/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops)

It uses several primary resources:

- Patterns of Base32 encoded 256-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKey256B32:

- pat
- token
- ado
- vsts
- azuredevops
- visualstudio.com
- dev.azure.com