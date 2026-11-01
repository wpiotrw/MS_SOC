---
layout: Conceptual
title: Microsoft Entra client access token entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-ad-client-access-token
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
description: Microsoft Entra client access token sensitive information type entity definition.
locale: en-us
document_id: f5f17ab4-8912-5374-6e67-e7b5a56b9210
document_version_independent_id: f5f17ab4-8912-5374-6e67-e7b5a56b9210
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-ad-client-access-token.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-ad-client-access-token
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-ad-client-access-token.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: d3067163-f1ef-2db6-6166-dfadf6cfe28b
---

# Microsoft Entra client access token entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of up to 10,000 characters consisting of letters, digits, and special characters.

or

A client secret or refresh token used in OAuth2.0 protocol.

or

A combination of up to 1,000 characters consisting of letters, digits, and special characters.

## Pattern

Any combination of:

- up to 10,000
- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- Up to 2
- equal signs (=)

for example:

`"VersionProfile": null, "TokenCache": { "CacheData": A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u

or

Variant client secret or refresh token formats for example. `ClientSecret:********``AppSecret=********``ConsumerKey:=********``Refresh_Token:********`

or

3 letters: eyJ (case-sensitive)

And

A combination of up to 1,000 characters consisting

- a-z (not case-sensitive)
- 0-9
- dashes (-)
- underlines (\_)
- or dots (.)

format example:

`A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u`

## Credential example

| Confidence Band | Example |
| --- | --- |
| High | `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>` |
| Medium | `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>` |
| Low | `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>` |

## Checksum

Yes

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's contains claims that one can use in [Azure Active Directory B2C](/en-us/azure/active-directory-b2c/active-directory-b2c-access-tokens) (Azure AD B2C) to identify the granted permissions to Azure resources.

It uses several primary resources:

- Patterns of Azure PowerShell Token Cache
- Patterns of Client secret context
- Patterns of Json Web Token
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName
- Patterns of mockup values, redactions, and placeholders
- A dictionary of vocabulary

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKeyContextInXml:

- tokencache

### Keyword\_ClientSecretContext:

- secret
- token
- auth
- securestring
- key

### Keyword\_JsonWebToken:

- eyJ