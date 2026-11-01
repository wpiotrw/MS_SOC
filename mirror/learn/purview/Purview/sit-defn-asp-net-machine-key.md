---
layout: Conceptual
title: ASP.NET machine key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-asp-net-machine-key
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-05-28T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: ASP.NET machine key sensitive information type entity definition.
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: bd3b94ff-6360-fec3-5a94-5856d03f56dc
document_version_independent_id: bd3b94ff-6360-fec3-5a94-5856d03f56dc
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-asp-net-machine-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-asp-net-machine-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-asp-net-machine-key.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/43ab1a66-ffe1-45dd-a4cb-6580218ef802
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bbc4fbf6-70c4-4d12-b47f-9360080c4977
platformId: 98e4b292-5c26-7f27-34ed-64a1d6fdfb54
---

# ASP.NET machine key entity definition | Microsoft Learn

This sensitive information type (SIT) is also included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

Symmetric keys in XML configuration.

## Pattern

Various symmetric key formats in XML, for example:

```xml
<machineKey decryptionKey="******** </br> 
<machineKey validationKey="********
```

## Credential example

```
<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>
```

See **How to generate a `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`** in the [Resolving view state message authentication code (MAC) errors](https://support.microsoft.com/en-us/topic/resolving-view-state-message-authentication-code-mac-errors-6c0e9fd3-f8a8-c953-8fbe-ce840446a9f3) support article for information on generating keys.

## Checksum

No

SITs that have checksums use a unique calculation to check if the information is valid. This means when the **Checksum** value is **Yes**, the service can make a positive detection based on the sensitive data alone. When the **Checksum** value is **No** additional (secondary) elements must also be detected for the service to make a positive detection.

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to encrypt or hash data in [ASP.NET](/en-us/dotnet/api/system.web.security.machinekey?view=netframework-4.8&amp;preserve-view=true) forms authentication and view state.

It uses several primary resources:

- Patterns of Symmetric key context in xml files.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName.

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKeyContextInXml:

- password
- key
- connectionstring