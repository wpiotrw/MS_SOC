---
layout: Conceptual
title: Supported file types in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-ref-supported-file-types
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: A list of supported file types for OCR text extraction and processing in Microsoft Purview Data Security Investigations.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
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
ai-usage: ai-assisted
locale: en-us
document_id: 8c09e8f6-9f2a-8880-adab-aa2e0c9fd9b6
document_version_independent_id: 8c09e8f6-9f2a-8880-adab-aa2e0c9fd9b6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-ref-supported-file-types.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-ref-supported-file-types
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-ref-supported-file-types.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 75ca29b8-a28f-a436-2116-94ac9a9090c6
---

# Supported file types in Data Security Investigations | Microsoft Learn

Microsoft Purview Data Security Investigations supports Optical Character Recognition (OCR) text extraction for supported image file types. The following table lists the currently supported image file types and indicates if a file type is supported for file identification, metadata extraction, and OCR text extraction.

## Image

Extraction of images is part of adding items to an investigation scope and automatic OCR processing isn't an additional charge for your organization.

| Mime type | File identification | Metadata extraction | OCR text extraction | Possible Extensions |
| --- | --- | --- | --- | --- |
| image/bmp | Yes | Yes | Yes | .bmp |
| image/emf | Yes | Yes | Yes | .emf |
| image/gif | Yes | Yes | Yes | .gif |
| image/jpeg | Yes | Yes | Yes | .jpeg; .jpg |
| image/png | Yes | Yes | Yes | .png |
| image/svg+xml | Yes | Yes | Yes | .svg |
| image/tiff | Yes | Yes | Yes | .tif |
| image/vnd.dwg | Yes | Yes | Yes | .dwg; .dxf |
| image/wmf | Yes | Yes | Yes | .wmf |

Note

The **OCR text extraction** column indicates that you can extract text from these image formats when data is [automatically vectorized](data-security-investigations-scope#automatic-vectorization). OCR text extraction occurs automatically during data preparation and the extracted text is vectorized for use in AI-based analysis tools.