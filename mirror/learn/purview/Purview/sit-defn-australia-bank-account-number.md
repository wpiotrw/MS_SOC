---
layout: Conceptual
title: Australia bank account number entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-australia-bank-account-number
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
description: Australia bank account number sensitive information type entity definition.
locale: en-us
document_id: e14be693-3cda-0f9a-de7a-6dd84ff8b49e
document_version_independent_id: e14be693-3cda-0f9a-de7a-6dd84ff8b49e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-australia-bank-account-number.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-australia-bank-account-number
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-australia-bank-account-number.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 703204b6-018a-8b2c-57de-90f8ac6f16d8
---

# Australia bank account number entity definition | Microsoft Learn

## Format

six to 10 digits with or without a bank state branch number

## Pattern

Account number is 6 to 10 digits.

Australia bank state branch number:

- three digits
- a hyphen
- three digits

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_australia\_bank\_account\_number finds content that matches the pattern.
- A keyword from Keyword\_australia\_bank\_account\_number is found.
- The regular expression Regex\_australia\_bank\_account\_number\_bsb finds content that matches the pattern.

A DLP policy has medium confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression Regex\_australia\_bank\_account\_number finds content that matches the pattern.
- A keyword from Keyword\_australia\_bank\_account\_number is found.

```xml
<!-- Australia Bank Account Number -->
<Entity id="74a54de9-2a30-4aa0-a8aa-3d9327fc07c7" patternsProximity="300" recommendedConfidence="75">
  <Pattern confidenceLevel="85">
        <IdMatch idRef="Regex_australia_bank_account_number" />
        <Match idRef="Keyword_australia_bank_account_number" />
        <Match idRef="Regex_australia_bank_account_number_bsb" />
  </Pattern>
  <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_australia_bank_account_number" />
        <Match idRef="Keyword_australia_bank_account_number" />
  </Pattern>
 </Entity>
```

## Keywords

### Keyword\_australia\_bank\_account\_number

- swift bank code
- correspondent bank
- base currency
- usa account
- holder address
- bank address
- information account
- fund transfers
- bank charges
- bank details
- banking information
- full names
- iaea