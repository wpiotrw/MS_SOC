---
layout: Conceptual
title: Azure SQL connection string entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-sql-connection-string
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-04-09T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Azure SQL connection string sensitive information type entity definition.
locale: en-us
document_id: 2093fb51-0382-aa19-6618-1cb8e489788c
document_version_independent_id: 2093fb51-0382-aa19-6618-1cb8e489788c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-sql-connection-string.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-sql-connection-string
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-sql-connection-string.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
platformId: 92ac38f7-9a28-397a-cfe3-34c35212261e
---

# Azure SQL connection string entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

Up to 20,000-character combination of letters, digits, and special characters.

or

A pair of username and password used in general authentication process.

## Pattern

Any combination of up to 20,000 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- Up to 2 equal signs (=)

format example:

`H4iJ5kL6mN7o==P8qR9sT0uV1wX2y/Z3a+`

or

Variant username and password formats, for example:

`username=...;password=********;``user id=...;password=********;``uid=...;pwd=********;``DB_USER=...;DB_PASS=********;``Service Account=...;Password=********;`

## Credential example

`server=server.database.windows.net;database=database;user=user;pwd=\*\*\*\*\*\*\*\*\*\*

## Checksum

Yes

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to connect to [Azure SQL Databases](/en-us/azure/sql-database/sql-database-aad-authentication-configure).

It uses several primary resources:

- Patterns of Base64 encoded string literal.
- Patterns of Plain-text username and password.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.
- Patterns of mockup values, redactions, and placeholders.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_Base64EncodedStringLiteral:

- MII

### Keyword\_LoginCredentials:

- password
- pw
- DB\_