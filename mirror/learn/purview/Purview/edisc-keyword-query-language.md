---
layout: Conceptual
title: Use Keyword Query Language to create search queries in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-keyword-query-language
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about using Keyword Query Language to create search queries in eDiscovery in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-03-11T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 866b4d1f-f77f-b28f-0a11-2d51f4c103ea
document_version_independent_id: 866b4d1f-f77f-b28f-0a11-2d51f4c103ea
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-keyword-query-language.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-keyword-query-language
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-keyword-query-language.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 68e5e6d7-a87b-37ad-ae43-25ecf07611f3
---

# Use Keyword Query Language to create search queries in eDiscovery | Microsoft Learn

The Keyword Query Language (KeyQL) query condition option provides feedback and guidance when you build [search](edisc-search-query) and [hold policy](edisc-hold-create) queries in eDiscovery. When you enter queries in the editor, it autocompletes supported searchable properties and conditions. It also provides lists of supported values for standard properties and conditions. For example, if you specify the `kind` email property in your query, the editor presents a list of supported values that you can select.

The KeyQL editor also displays potential query errors in real time that you can fix before you run the search. Paste complex queries directly into the editor without manually building queries using the conditions cards in the condition builder. The KeyQL editor is also available when you create query-based holds in eDiscovery.

Here are the key benefits to using the KeyQL editor:

- Provides guidance and helps you build search queries from scratch.
- Lets you quickly paste long, complex queries directly into the editor. For example, if you receive a complex query from opposing counsel, you can paste that into the KeyQL editor instead of having to use the condition builder.
- Quickly identifies potential errors and displays hints about how to resolve issues.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Use the KeyQL editor

Use the KeyQL editor by selecting **Add conditions** and selecting *KeyQL*. For conditions and values already populated, these conditions and values are automatically converted into KeyQL. KeyQL query conditions can't be used with other conditions and need to be used as standalone conditions in your query.

The following sections show examples of how the KeyQL editor provides suggestions and detects potential errors.

### Autocompletion of search properties and operators

When you start to enter a search query in the KeyQL editor, the editor displays suggested autocompletion of supported search properties (also called *property restrictions*) that you can select. You need to type at least two characters to display a list of supported properties that begin with those two characters. For example, the following screenshot shows the suggested search properties that begin with `Bu`.

![KeyQL editor suggests supported properties.](media/edisc-keyql-editor-autocomplete-1.png)

Additionally, the editor suggests a list of supported operators (such as `:`, `=`, and `<>`) when you type in a complete property name. For example, the following screenshot shows the suggested operators for the `Date` property.

![KeyQL editor suggests operators.](media/edisc-keyql-editor-autocomplete-2.png)

For more information about the supported search conditions, see [Use the condition builder to create search queries in eDiscovery](edisc-condition-builder).

### Property value suggestions

The KeyQL editor provides suggestions for possible values of some properties. For example, the following screenshot shows the suggested values for the `Kind` property.

![KeyQL editor suggests values for some properties.](media/edisc-keyql-editor-autocomplete-3.png)

The editor also suggests a list of users (in User Principal Name (UPN) format) when you type email recipient properties, such as `From`, `To`, `Recipients`, and `Participants`.

### Detection of potential errors

The KeyQL editor detects potential errors in search queries, and provides a hint of what is causing the error to help you resolve the error. The editor also indicates a potential error when a property doesn't have a corresponding operation or value. Potential errors in the query are highlighted in red text, and explanations and possible fixes for the error are displayed in the **Potential errors** drop-down section.

Important

Nested quotation marks aren't supported in the KeyQL editor.

For example, if you paste the following query into the KeyQL editor, the editor detects three potential errors. Use the potential error hints to help troubleshoot and fix the query.

![KeyQL editor error detection.](media/edisc-keyql-editor-autocomplete-4.png)