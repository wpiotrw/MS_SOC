---
layout: Conceptual
title: GitHub personal access token entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-github-personal-access-token
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
description: GitHub personal access token sensitive information type entity definition.
locale: en-us
document_id: 96c84216-db4f-c98c-4252-1f02419e7fdc
document_version_independent_id: 96c84216-db4f-c98c-4252-1f02419e7fdc
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-github-personal-access-token.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-github-personal-access-token
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-github-personal-access-token.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9bdc1705-9b40-49d6-8377-caa0b71fda66
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/686ed158-d915-41e9-9760-efa46ba88f6d
platformId: c17da929-727f-4bb7-9a6c-febed46e4567
---

# GitHub personal access token entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A combination of 40 characters consisting of letters, digits, and special characters.

or

Paired username and password used in URL.

or

A combination of 40 characters consisting of letters and digits.

## Pattern

- A token prefix (case-sensitive) 'ghp\_', 'gho\_', 'ghu\_', 'ghs\_', or 'ghr\_'
- Any combination of 36 a-z (not case-sensitive) or 0-9

format example:

`ghp_A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u`

or

Various URL username and password formats for example:

`https://username:********@contoso.com/`

`ftp://username:********@contoso.com:20/`

or

A combination of 40 characters:

- a-f or A-F (case-sensitive) or 0-9

format example:

`A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u`

## Credential format example

`pat=ghp_A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u`

## Checksum

Yes

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used as an alternate password for authentication to GitHub when using [GitHub API or the command line](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

It uses several primary resources:

- Patterns of Identifiable GitHub PAT.
- Patterns of User Login Credentials in URL.
- Patterns of Hex encoded 160 bits Symmetric Key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.
- Patterns of mockup values, redactions, and placeholders.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_GitHubPatIdentifiableSecret:

- gh\_

### Keyword\_LoginCredentialsInUrl:

- ://

### Keyword\_SymmetricKey160Hex:

- token