---
layout: Conceptual
title: SQL Server connection string entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-sql-server-connection-string
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
description: SQL Server connection string sensitive information type entity definition.
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: 3282049d-47cb-c795-e2e5-f1a695af54f4
document_version_independent_id: 3282049d-47cb-c795-e2e5-f1a695af54f4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-sql-server-connection-string.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-sql-server-connection-string
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-sql-server-connection-string.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: f52f84ea-30a9-0cd7-1f5d-d4c58615a50d
---

# SQL Server connection string entity definition | Microsoft Learn

## Format

The string `User Id`, `User ID`, `uid`, or `UserId` followed by the characters and strings outlined in the pattern below.

## Pattern

- the string `User Id`, `User ID`, `uid`, or `UserId`
- any combination of between 1-200 lower- or uppercase letters, digits, symbols, special characters, or spaces
- the string `Password` or `pwd` where `pwd` isn't preceded by a lowercase letter
- an equal sign (=)
- any character that isn't a dollar sign ($), percent symbol (%), greater than symbol (&gt;), at symbol (@), quotation mark ("), semicolon (;), left brace([), or left bracket ({)
- any combination of 7-128 characters that aren't a semicolon (;), forward slash (/), or quotation mark (")
- a semicolon (;) or quotation mark (")

## Checksum

No

## Keyword Highlighting

Supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Definition

A DLP policy has high confidence that it's detected this type of sensitive information if, within a proximity of 300 characters:

- The regular expression `CEP_Regex_SQLServerConnectionString` finds content that matches the pattern.
- A keyword from `CEP_GlobalFilter` isn't found.
- The regular expression `CEP_PasswordPlaceHolder` doesn't find content that matches the pattern.
- The regular expression `CEP_CommonExampleKeywords` doesn't find content that matches the pattern.

```sql
<!---SQL Server Connection String>
<Entity id="e76b6205-d3cb-46f2-bd63-c90153f2f97d" patternsProximity="300" recommendedConfidence="85">
  <Pattern confidenceLevel="85">
        <IdMatch idRef="CEP_Regex_SQLServerConnectionString" />
        <Any minMatches="0" maxMatches="0">
            <Match idRef="CEP_GlobalFilter" />
            <Match idRef="CEP_PasswordPlaceHolder" />
            <Match idRef="CEP_CommonExampleKeywords" />
        </Any>
    </Pattern>
</Entity>
```

## Keywords

### CEP\_GlobalFilter

- some-password
- somepassword
- secretPassword
- sample

### CEP\_PasswordPlaceHolder

This sensitive information type identifies these keywords by using a regular expression, not a keyword list.

- `Password` or `pwd` followed by 0-2 spaces, an equal sign (=), 0-2 spaces, and an asterisk (\*) -OR-
- `Password` or `pwd`followed by:
    - Equal sign (=)
    - Less than symbol (&lt;)
    - Any combination of 1-200 characters that are upper- or lowercase letters, digits, an asterisk (\*), hyphen (-), underline (\_), or whitespace character
    - Greater than symbol (&gt;)

### CEP\_CommonExampleKeywords

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