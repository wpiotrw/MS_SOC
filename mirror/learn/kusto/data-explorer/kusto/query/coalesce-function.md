---
layout: Conceptual
monikers:
- microsoft-sentinel
- azure-monitor
- azure-data-explorer
- microsoft-fabric
defaultMoniker: microsoft-fabric
versioningType: Ranged
title: coalesce() - Kusto | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/kusto/query/coalesce-function?view=microsoft-fabric
config_moniker_range: 'microsoft-fabric || azure-data-explorer || azure-monitor || microsoft-sentinel '
breadcrumb_path: /kusto/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Kusto
feedback_system: Standard
recommendations: true
author: spelluru
ms.author: spelluru
ms.service: kusto
services: kusto
description: Learn how to use the coalesce() function to evaluate a list of expressions to return the first non-null expression.
ms.reviewer: alexans
ms.topic: reference
ms.date: 2024-08-11T00:00:00.0000000Z
locale: en-us
document_id: c1b4ce3c-93e7-bda5-2e98-351d0cea2f0c
document_version_independent_id: c1b4ce3c-93e7-bda5-2e98-351d0cea2f0c
original_content_git_url: https://github.com/MicrosoftDocs/dataexplorer-docs-pr/blob/live/data-explorer/kusto/query/coalesce-function.md
default_moniker: microsoft-fabric
site_name: Docs
depot_name: Learn.kusto-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Learn.kusto-docs/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: query/coalesce-function
moniker_range_name: f0081dc5071f32aee7689305c3508dfe
monikers:
- microsoft-sentinel
- azure-monitor
- azure-data-explorer
- microsoft-fabric
item_type: Content
source_path: data-explorer/kusto/query/coalesce-function.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 08958235-5662-79de-0143-a8bd6d938f18
---

# coalesce() - Kusto | Microsoft Learn

> 
> Switch services using the **Version** drop-down list. [Learn more about navigation](../docs-navigation).  Applies to: ✅ Microsoft Fabric ✅ Azure Data Explorer ✅ Azure Monitor ✅ Microsoft Sentinel

Evaluates a list of expressions and returns the first non-null (or non-empty for string) expression.

## Syntax

`coalesce(`*arg*`,`*arg\_2*`,[`*arg\_3*`,...])`

Learn more about [syntax conventions](/en-us/kusto/query/syntax-conventions).

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| arg | scalar | ✔️ | The expression to be evaluated. |

Note

- All arguments must be of the same type.
- Maximum of 64 arguments is supported.

## Returns

The value of the first *arg* whose value isn't null (or not-empty for string expressions).

## Examples

```kusto
print result=coalesce(tolong("not a number"), tolong("42"), 33)
```

**Output**

| result |
| --- |
| 42 |