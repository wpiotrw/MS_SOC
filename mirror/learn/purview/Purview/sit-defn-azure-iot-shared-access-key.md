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
ms.date: 2023-09-13T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Azure IoT shared access key sensitive information type entity definition.
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
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/203e4af6-88b5-4e82-bf7b-51a6102005c3
platformId: a06f06d0-0fc3-5589-4f43-9622ab92ac62
---

# Azure IoT shared access key entity definition | Microsoft Learn

## Format

A combination of 44-characters consisting of letters, digits, and special characters ending with and equals sign that isn't part of the pattern.

## Pattern

Any combination of 43 characters consisting of:

- a-z (not case-sensitive)
- 0-9
- forward slashes (/)
- or plus signs (+)
- ends with an equal sign (=) that isn't part of the pattern.

Format example:

`A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u+=`

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

The patterns are designed to match actual credentials with reasonable confidence. The patterns don't match credentials formatted as examples. Mockup values, redacted values, and placeholders, like credential type or usage descriptions, in the position where an actual secret value should present won't be matched.

## Keywords

### Keyword\_SymmetricKey256:

- SharedAccessKey
- AccountKey