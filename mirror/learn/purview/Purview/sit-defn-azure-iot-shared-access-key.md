---
layout: Conceptual
title: Azure IoT shared access key entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-iot-shared-access-key
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-11-13T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Azure IoT shared access key sensitive information type entity definition.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1032
locale: en-us
document_id: 672de9a3-cadf-8416-d7b3-b9d31f2996ac
document_version_independent_id: 672de9a3-cadf-8416-d7b3-b9d31f2996ac
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-iot-shared-access-key.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-iot-shared-access-key
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-iot-shared-access-key.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8905b934-b96c-4513-8447-7040eb93b2b2
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/203e4af6-88b5-4e82-bf7b-51a6102005c3
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: a06f06d0-0fc3-5589-4f43-9622ab92ac62
---

# Azure IoT shared access key entity definition | Microsoft Learn

The Azure IoT shared access key sensitive information type (SIT) in Microsoft Purview identifies credentials used to authenticate Azure IoT devices and services, including shared access keys in Azure IoT connection strings.

This SIT is the newer detector for the credential type covered by the [Azure IoT connection string](sit-defn-azure-iot-connection-string) SIT. It supports additional credential variants.

This SIT is included in the [All credentials](sit-defn-all-creds) bundled SIT.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a credential scanning SIT in an endpoint DLP policy. This requirement is specific to the combination of credential scanning SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

A Base64-encoded 256-bit symmetric key. The encoded key contains 44 characters: 43 letters, digits, forward slashes (/), or plus signs (+), followed by an equal sign (=).

## Pattern

A sequence of 43 characters consisting of:

- Uppercase or lowercase letters (A-Z or a-z).
- Digits (0-9).
- Forward slashes (/).
- Plus signs (+).

The 43-character sequence is followed by an equal sign (=), for a total of 44 characters.

Format example:

`abcdefghijklmnopqrstuvwxyz0123456789/+ABCDE=`

This value illustrates the key format. Key length alone doesn't establish that the SIT will detect a value; the surrounding credential context also matters.

## Credential example

The following connection string provides a complete Azure IoT credential example for detection testing. The hostname and key are fictitious documentation values, not credentials for accessing an Azure resource.

`<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`

Use the complete connection string when testing detection. Shortened keys, redacted values, and placeholders aren't suitable substitutes for this positive-test example.

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

This SIT is designed to match the security information that's used to authenticate [Azure IoT devices and services](/en-us/azure/iot-fundamentals/iot-security-deployment).

It uses several primary resources:

- Patterns of Base64 encoded 256-bits symmetric key.
- Patterns of CredentialName, CredentialFeatures, AccountIdentityName, AccountIdentityValue, ResourceType, ResourceName, ID.
- Patterns of mockup values, redactions, and placeholders.
- A dictionary of vocabulary.

The patterns identify credentials with reasonable confidence and evaluate patterns for mockup values, redactions, and placeholders. Credential type names or usage descriptions in place of a key aren't suitable for positive detection testing. Use the complete connection string in the Credential example section to test detection.

## Keywords

### Keyword\_SymmetricKey256:

- SharedAccessKey
- AccountKey