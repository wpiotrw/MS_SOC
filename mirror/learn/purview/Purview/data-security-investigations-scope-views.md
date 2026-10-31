---
layout: Conceptual
title: Group and view items in an investigation scope in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-scope-views
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Choose how you group and view content in Data Security Investigations investigation scopes, including specialized viewers to examine details about individual items.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-05-29T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 7ec6a059-f73a-be98-11ec-4f99428397ec
document_version_independent_id: 7ec6a059-f73a-be98-11ec-4f99428397ec
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-scope-views.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-scope-views
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-scope-views.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0fc65d4-7c73-4029-a261-7f99ff744363
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b2daec57-5914-4967-8ed3-1d444897ba59
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 986723c7-4ac7-8712-969a-f7f9ed165245
---

# Group and view items in an investigation scope in Data Security Investigations | Microsoft Learn

Data Security Investigations investigation scopes display content by using different grouping options. They include specialized viewers that you can use to examine details about individual items.

## Grouping

Use the **Group** control in the command bar of an investigation scope to view review content grouped by the following options:

- **Group by families**: All items related to a specific file are grouped together by using the same Group ID. For example, if you have a PowerPoint file in the investigation scope that includes embedded images or .zip files, these images and files are grouped with the PowerPoint file and shown as nested items with the file in the item list view. Microsoft 365 Copilot and Microsoft 365 Copilot Chat user prompts and responses are also grouped together by using the same Group ID when there are multiple prompts and responses associated with a file.
- **Group by conversations**: All email messages, Teams conversations, and Viva Engage conversations are grouped by using the same Thread ID and appear as nested items. Additionally, all associated content for these messages and conversations is also grouped together. For example, if you have an email conversation that includes several email messages, some of which include attachments and some that include embedded images, all of the email messages, attachments, and images are grouped together in the investigation scope list view under an applicable item.

## Source view

The **Source** viewer displays the richest view of a selected document. It supports hundreds of file types and is meant to display the truest to native experience possible. For Microsoft Office files, the viewer uses the web version of Office apps to display content such as document comments, Microsoft Teams chats, Excel formulas, hidden rows and columns, and PowerPoint notes.

## Plain text view

The **Plain text** viewer provides a view of the extracted text of a selected file. It ignores any embedded images and formatting but is useful if you're trying to understand the content quickly. A line counter makes it easier to reference specific portions of a document.

For image-based items, the evidence detail pane displays text extracted through Optical Character Recognition (OCR) alongside the original image. This view allows you to verify the accuracy of the text extraction and review content identified through OCR processing.

## Metadata view

The panel in the **Metadata** view displays various metadata associated with the selected document. Search for specific metadata by using the **Search metadata name** field.

## AI Summary view

Note

This viewer is only available for items returned as results when you use [Search with AI (preview)](data-security-investigations-ai#search-with-ai-preview).

The AI Summary viewer provides information about the relevance categorization for an item and provides an AI summary and explanation for the reasoning behind the categorization.