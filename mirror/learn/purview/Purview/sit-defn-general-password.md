---
layout: Conceptual
title: General password entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-general-password
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-09T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: General password sensitive information type entity definition.
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: ef118b59-72e5-5f08-7ce1-9a78f6c43469
document_version_independent_id: ef118b59-72e5-5f08-7ce1-9a78f6c43469
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-general-password.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-general-password
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-general-password.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 73a6cee7-2853-395c-6eb2-2e9f29367680
---

# General password entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

Up to 20,000-character combination of letters, digits, and special characters.

or

Sign in credentials used in command lines

or

Plain-text password used in code snippets

or

Plain-text password used in script

or

Plain-text password used in XML configuration

or

A combination of 24 characters consisting of letters, digits, and special characters.

or

A combination of 32 characters consisting of letters and digits.

or

A combination of 32 characters consisting of letters, digits, and special characters.

or

A combination of 44 characters consisting of letters, digits, and special characters.

or

An 88-character combination of letters, digits, and special characters.

## Patterns

1. Any combination of up to 20,000 characters consisting of:

    - a-z (case insensitive)
    - 0-9
    - forward slashes (/) or plus signs (+)
    - Up to two equal signs (=)
2. Various command line sign-in credentials formats
3. Various password formats in code snippets
4. Various password formats in script
5. Various password formats in XML
6. Any combination of 22 characters consisting of:

    - a-z (case insensitive)
    - digits, forward slashes, or plus signs
    - ends with two equal signs (=)
7. Any combination of 32 characters consisting of:

    - a-f or A-F (case-sensitive) or 0-9
8. Any combination of 32 characters consisting of:

    - a-z (case insensitive)
    - 0-9
    - forward slashes (/) or plus signs (+)
9. Any combination of 43 characters consisting of:

    - a-z (case insensitive)
    - 0-9
    - forward slashes (/) or plus signs (+)
    - ends with an equal sign (=)
10. Any combination of 86 characters consisting of:

    - a-z (case insensitive)
    - 0-9
    - forward slashes (/) or plus signs (+)
    - ends with two equal signs (=)

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

## Description

This SIT is designed to match security information, such as usernames and passwords, that are used in the sign-in process [user login process](/en-us/azure/key-vault/quick-create-portal). It uses several primary resources:

- Patterns of Base64 encoded string literal.
- Patterns of Password context in command line.
- Patterns of Password context in code.
- Patterns of Password context in script.
- Patterns of Password context in XML.
- Patterns of Base64 encoded 128-bits symmetric key.
- Patterns of Hex encoded 128-bits symmetric key.
- Patterns of Base64 encoded 192-bits symmetric key.
- Patterns of Base64 encoded 256-bits symmetric key.
- Patterns of Base64 encoded 512-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, ID, AccountName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary words.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. For instance, mockup values, redacted values, and placeholders, like credential type or usage descriptions, that are in the position where an actual secret value should present aren't matched.

## Keywords

Important

This SIT detects passwords related keywords in English only.

### Keyword\_Base64EncodedStringLiteral

- MII

### Keyword\_PasswordContextInCmdLine

- certutil
- zdbg
- secret
- VSTS\_TOKEN
- curl
- PowerShell
- ps1
- -u
- Smc
- AutoLogon
- ldifde
- Rclone
- --env
- SignTool
- winexe
- net

## Keyword\_PasswordContextInCode

- key
- x509c
- credential
- password
- pw
- securestring

### Keyword\_PasswordContextInScript

- secret
- password
- pw

### Keyword\_PasswordContextInXml

- userpass
- password
- pw
- connectionstring
- key
- credential
- token
- sas
- secret

### Keyword\_SymmetricKey128

- secret
- key
- password
- pw

### Keyword\_SymmetricKey128Hex

- dapi
- key
- secret
- token
- password
- pw

### Keyword\_SymmetricKey192

- password
- -p
- azurecr

### Keyword\_SymmetricKey256

- SharedAccessKey
- AccountKey

### Keyword\_SymmetricKey512

- SharedAccessKey
- AccountKey