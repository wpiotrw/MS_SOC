---
layout: Conceptual
title: User login credentials entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-user-login-credentials
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
description: User login credentials sensitive information type entity definition.
locale: en-us
document_id: 647ec992-a4ab-afee-cdfb-8a0ba3d8765d
document_version_independent_id: 647ec992-a4ab-afee-cdfb-8a0ba3d8765d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-user-login-credentials.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-user-login-credentials
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-user-login-credentials.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/545d40c6-c50c-444b-b422-1c707eeab28e
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b908d601-32e8-445a-b044-a507b5d1689e
platformId: 4e363029-61d9-b290-380a-be7192f4fa91
---

# User login credentials entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A paired username and password used in general authentication process.

or

A paired username and password used in PuTTY connection manager.

or

Plain text password used in code snippets.

or

A combination of 88 characters consisting of letters, digits, and special characters.

## Pattern

Various username and password formats, for example:

`username=...;password=********;``user id=...;password=********;``uid=...;pwd=********;``DB_USER=...;DB_PASS=********;``Service Account=...;Password=********;`

or

```xml
An XML element <login>
An embeded XML element <login>
Inner XML content
An embeded XML element </login>
An embeded XML element <password>
Inner XML content
An embeded XML element </password>
An XML element </login>
```

for example

`<login> <login>ZYXWVU_1</login> <password>ZY…`

or

Various password formats in code snippets, for example:

`new X509Certificates2(``ConvertTo-SecureString -String ********``password = "********"``"password" : "********"``UserPasswordCredential(`

or

A combination of 86 characters:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- ends with two equal signs (=)

format example:

`aB1cD2eF/3gH4iJ5kL6+mN7oP8qR==`

## Credential example

|Confidence Band|Example| |----|----| |High| `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`user=user\_name;password=\*\*\*\*\*\*\*\*\*\* | |Low| N/A |

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used in general [user login process](/en-us/azure/key-vault/quick-create-portal).

It uses several primary resources:

- Patterns of Plain-text username and password.
- Patterns of Plain-text username and password in PuTTYcm database file.
- Patterns of Password context in code.
- Patterns of Base64 encoded 512 bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, Id, AccountName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_LoginCredentials:

- password
- pw
- DB\_

### Keyword\_LoginCredentialsPutty:

- login

### Keyword\_PasswordContextInCode:

- key
- x509c
- credential
- password
- pw
- securestring

### Keyword\_SymmetricKey512:

- SharedAccessKey
- AccountKey