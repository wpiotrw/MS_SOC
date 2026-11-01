---
layout: Conceptual
title: Azure service bus connection string entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-azure-service-bus-connection-string
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-10T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: Azure service bus connection string sensitive information type entity definition.
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: a6239a32-76aa-a2c1-e10a-ce9fde0166ab
document_version_independent_id: a6239a32-76aa-a2c1-e10a-ce9fde0166ab
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-azure-service-bus-connection-string.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-azure-service-bus-connection-string
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-azure-service-bus-connection-string.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/828c518e-a2df-46f1-8871-b760959c8fa8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/54f6b674-eb1d-48ca-9254-9665ddd64677
platformId: a3d6da80-e1bf-acb8-ef9b-e1ffe0f01273
---

# Azure service bus connection string entity definition | Microsoft Learn

## Format

The string `EndPoint` followed by the characters and strings outlined in the pattern below, including the strings `servicebus.windows.net` and `SharedAccesKey`.

## Pattern

- the string `EndPoint`
- zero to two whitespace characters
- an equal sign (=)
- zero to two whitespace characters
- any combination of between 1-200 lower- or uppercase letters, digits, symbols, special characters, or spaces
- the string `servicebus.windows.net`
- any combination of between 1-200 lower- or uppercase letters, digits, symbols, special characters, or spaces
- the string `SharedAccessKey`
- zero to two whitespace characters
- an equal sign (=)
- zero to two whitespace characters
- any combination of 43 characters that are lower- or uppercase letters, digits, forward slash (/), or plus sign (+)
- an equal sign (=)

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `CEP_Regex_AzureServiceBusConnectionString` finds content that matches the pattern.
- The regular expression `CEP_CommonExampleKeywords` doesn't find content that matches the pattern.

```xml
<!--Azure Service Bus Connection String-->
<Entity id="b9a6578f-a83f-4fcd-bf44-2130bae49a6f" patternsProximity="300" recommendedConfidence="85">
  <Pattern confidenceLevel="85">
        <IdMatch idRef="CEP_Regex_AzureServiceBusConnectionString" />
        <Any minMatches="0" maxMatches="0">
            <Match idRef="CEP_CommonExampleKeywords" />
        </Any>
  </Pattern>
</Entity>
```

## Keywords

### CEP\_common\_example\_keywords

This sensitive information type identifies these keywords by using a regular expression, not a keyword list.

- contoso
- fabrikam
- northwind
- sandbox
- onebox
- localhost
- 127.0.0.1
- testacs.com
- s-int.net