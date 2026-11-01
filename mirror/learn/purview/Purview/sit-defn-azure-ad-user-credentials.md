---
layout: Conceptual
title: Microsoft Entra user credentials entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-ad-user-credentials
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
description: Microsoft Entra user credentials sensitive information type entity definition.
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: 6d839012-6256-8bdd-7f42-9ff28935eac5
document_version_independent_id: 6d839012-6256-8bdd-7f42-9ff28935eac5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-ad-user-credentials.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-ad-user-credentials
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-ad-user-credentials.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: f0c7a92a-b8b3-776d-e726-7150f0a0eb85
---

# Microsoft Entra user credentials entity definition | Microsoft Learn

This SIT is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A paired username and password related to \*.onmicrosoft.com domain.

or

Plain-text password used in code snippets.

or

Plain-text password used in XML configuration.

## Pattern

Various username and password formats, for example:

`username=...password=********``/user:.../pass:********``SharePointOnlineAuthenticatedContext``sign_in`

or

Various password formats in code snippets, for example:

`new X509Certificates2( ...``ConvertTo-SecureString -String ********...``password = "********"...``"password" : "********"...``UserPasswordCredential( ...`

or

Various password formats in XML, for example:

```xml
... <secret>********</secret> ...
... <password>********</password> ...
... <setting name="password" value="********" > ... 
... <setting name="password">********</setting> ... 
... <setting name="password"><value>********</value></setting> ... 
```

## Credential example

`<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used as individual user passwords to authenticate against [Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-users-reset-password-azure-portal).

It uses several primary resources:

- Patterns of Plain-text username and password for Microsoft Entra tenants.
- Patterns of Password context in code.
- Patterns of Password context in XML.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_AzureActiveDirectoryLoginCredentials:

- password
- pw
- userpass
- credentials
- cmdkey
- Authenti
- sign\_in

### Keyword\_PasswordContextInCode:

- key
- x509c
- credential
- password
- pw
- securestring

### Keyword\_PasswordContextInXml:

- userpass
- password
- pw
- connectionstring
- key
- credential
- token
- sas
- secret