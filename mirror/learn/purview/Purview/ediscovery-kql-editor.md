---
layout: Conceptual
title: Use the KeyQL editor to build search queries | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-kql-editor
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: You can use the KeyQL editor to configure eDiscovery search queries in Content search, eDiscovery (Standard), and eDiscovery (Premium).
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
ms.reviewer: nickrob
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
manager: laurawi
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
locale: en-us
document_id: c6571353-3e2b-618d-540b-42280f94db28
document_version_independent_id: c6571353-3e2b-618d-540b-42280f94db28
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-kql-editor.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-kql-editor
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-kql-editor.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f8d00540-ba9e-5b84-2bb8-47f550612c0a
---

# Use the KeyQL editor to build search queries | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

The Keyword Query Language (KeyQL) query option in Microsoft Purview eDiscovery tools search provides feedback and guidance when you build search queries in Content search, Microsoft Purview eDiscovery (Standard), and eDiscovery (Premium). When you enter queries in the editor, it provides autocompletion for supported searchable properties and conditions and provides lists of supported values for standard properties and conditions. For example, if you specify the `kind` email property in your query, the editor will present a list of supported values that you can select. The KeyQL editor also displays potential query errors in real time that you can fix before you run the search. Best of all, you can paste complex queries directly into the editor without having to manually build queries using the keywords and conditions cards in the standard condition builder.

Here are the key benefits to using the KeyQL editor:

- Provides guidance and helps you build search queries from scratch.
- Lets you quickly paste long, complex queries directly into the editor. For example, if you receive a complex query from opposing counsel, you can paste that into the KeyQL editor instead of having to use the condition builder.
- Quickly identifies potential errors and displays hints about how to resolve issues.

The KeyQL editor is also available when you create query-based holds in eDiscovery (Standard) and eDiscovery (Premium).

## Displaying the KeyQL editor

When you create or edit an eDiscovery search, the option to display and use the KeyQL editor is located on the **Conditions** page in the search or collections workflow.

### KeyQL editor in Content search and eDiscovery (Standard)

![KeyQL editor in Content search and eDiscovery (Standard)](media/kqleditorcore.png)

### KeyQL editor in eDiscovery (Premium)

![KeyQL editor in eDiscovery (Premium)](media/ediscovery-kql-premium.png)

## Using the KeyQL editor

The following sections show examples of how the KeyQL editor provides suggestions and detects potential errors.

### Autocompletion of search properties and operators

When you start to enter a search query in the KeyQL editor, the editor displays suggested autocompletion of supported search properties (also called *property restrictions*) that you can select. You have to type a minimum of two characters to display a list of supported properties that begin with those two characters. For example, the following screenshot shows the suggested search properties that begin with `Se`.

![KeyQL editor suggests supported properties](media/kqleditorautocompleteproperties.png)

Additionally, the editor also suggests provides a list of supported operators (such as `:`, `=` and `<>`) when you type in a complete property name. For example, the following screenshot shows the suggested operators for the `Date` property.

![KeyQL editor suggests operators](media/kqleditoroperatorsuggestions.png)

For more information about the supported search properties and operators, see [Keyword queries and search conditions for eDiscovery](ediscovery-keyword-queries-and-search-conditions).

### Property value suggestions

The KeyQL editor provides suggestions for possible values of some properties. For example, the following screenshot shows the suggested values for the `Kind` property.

![KeyQL editor suggests values for some properties](media/kqleditorvaluesuggestions.png)

The editor also suggests a list of users (in UPN format) when you type email recipient properties, such as `From`, `To`, `Recipients` and `Participants`.

![KeyQL editor suggests users for recipient email properties](media/kqleditorrecipientsuggestions.png)

### Detection of potential errors

The KeyQL editor detects potential errors in search queries, and provides a hint of what is causing the error to help you resolve the error. The editor also indicates a potential error when a property doesn't have a corresponding operation or value. Potential errors in the query are highlighted in red text, and explanations and possible fixes for the error are displayed in the **Potential errors** drop-down section.

Important

Nested quotation marks aren't supported in the KeyQL editor.

For example, if you pasted the following query into the KeyQL editor, four potential errors would be detected.

![KeyQL editor error detection](media/kqleditorerrordetection.png)

In this case, you can use the potential error hints to troubleshoot and fix the query.

## More information

- You can toggle between the condition builder and the KeyQL editor. For example, if you use the condition builder to configure a query using the Keywords box and multiple condition cards, you can display the resulting query in the KeyQL editor. However, if you create a complex query (with keywords and conditions) in the KeyQL editor, the resulting query is displayed only in the Keywords box when you view it in the condition builder.
- If you paste a complex query into the KeyQL editor, the editor detects potential errors and suggests possible solutions to resolve errors.