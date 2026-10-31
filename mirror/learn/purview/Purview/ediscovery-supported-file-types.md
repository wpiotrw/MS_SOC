---
layout: Conceptual
title: Supported file types in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-supported-file-types
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: A list of supported file types in Microsoft 365 eDiscovery (Premium), including image file types supported by the OCR functionality in eDiscovery (Premium).
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
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
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: 2f8270f7-4d89-ff39-86db-a95cc520c3ca
document_version_independent_id: 2f8270f7-4d89-ff39-86db-a95cc520c3ca
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-supported-file-types.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-supported-file-types
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-supported-file-types.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 0fb2a92b-058f-33bf-4163-c7a39c2b66c4
---

# Supported file types in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Microsoft Purview eDiscovery (Premium) supports many file types at many different levels. The following tables in this article list the currently supported files types.

These tables indicate if a file type is supported for text extraction (and Optical Character Recognition or OCR text extraction for image files), viewable in the native viewer, and also supported in the Annotate viewer in eDiscovery (Premium).

## Archive / Container

| Mime type | File identification | Metadata extraction | Container extraction | Possible Extensions |
| --- | --- | --- | --- | --- |
| application/x-7z-compressed | Yes | Yes | Yes | .7z |
| application/x-rar-compressed | Yes | Yes | Yes | .rar^1^ |
| application/x-tar | Yes | Yes | Yes | .tar |
| application/zip | Yes | Yes | Yes | .zip |
|  |  |  |  |  |

Note

^1^ Version 5 .rar files aren't currently supported.

## Audio / Video

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/mp4 | Yes | Yes | No | Yes | No | .f4v; .m4a; .m4v; .mp4; .mp4v; .mpeg; .mpeg4 |
| audio/mpeg | Yes | Yes | No | Yes | No | .mpeg |
| video/3gpp | Yes | Yes | No | Yes | No | .3gp |
| video/3gpp2 | Yes | Yes | No | Yes | No | .3g2; .3gp2 |
| video/quicktime | Yes | Yes | No | Yes | No | .moov; .mov; .qt |
| video/x-m4v | Yes | Yes | No | Yes | No | .m4v |
|  |  |  |  |  |  |  |

## Database

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/x-msaccess | Yes | Yes | Yes | No | No | .mdb |
|  |  |  |  |  |  |  |

## Email

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/vnd.ms-outlook | Yes | Yes | Yes | Yes | Yes | .msg |
| message/rfc822 | Yes | Yes | Yes | Yes | Yes | .eml |
| text/vcard-contact | Yes | Yes | Yes | Yes | Yes | .vcf |
|  |  |  |  |  |  |  |

## Email Container

| Mime type | File identification | Metadata extraction | Container extraction | Possible Extensions |
| --- | --- | --- | --- | --- |
| application/mbox | Yes | Yes | Yes | .mbox |
| application/vnd.ms-outlook-pst | Yes | Yes | Yes | .pst |
|  |  |  |  |  |

## HTML

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/xhtml+xml | Yes | Yes | Yes | Yes | Yes | .xhtml |
| application/xml | Yes | Yes | Yes | Yes | Yes | .xml |
| text/html | Yes | Yes | Yes | Yes | Yes | .htm; .html; .shtml |
|  |  |  |  |  |  |  |

## Image

| Mime type | File identification | Metadata extraction | OCR text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| image/bmp | Yes | Yes | Yes | Yes | Yes | .bmp |
| image/emf | Yes | Yes | Yes | Yes | Yes | .emf |
| image/gif | Yes | Yes | Yes | Yes | Yes | .gif |
| image/jpeg | Yes | Yes | Yes | Yes | Yes | .jpeg; .jpg |
| image/png | Yes | Yes | Yes | Yes | Yes | .png |
| image/svg+xml | Yes | Yes | Yes | Yes | No | .svg |
| image/tiff | Yes | Yes | Yes | Yes | Yes | .tif |
| image/vnd.dwg | Yes | Yes | Yes | Yes | Yes | .dwg; .dxf |
| image/wmf | Yes | Yes | Yes | Yes | Yes | .wmf |
|  |  |  |  |  |  |  |

## Microsoft Excel

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/vnd.ms-excel | Yes | Yes | Yes | Yes | Yes | .dat; .xls |
| application/vnd.ms-excel.sheet.binary.macroenabled.12 | Yes | Yes | Yes | Yes | No | .xlsb |
| application/vnd.ms-excel.sheet.macroenabled.12 | Yes | Yes | Yes | Yes | Yes | .xlsm |
| application/vnd.ms-excel.template.macroenabled.12 | Yes | Yes | Yes | No | No | .xltm |
| application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | Yes | Yes | Yes | Yes | Yes | .xlsx |
| application/vnd.openxmlformats-officedocument.spreadsheetml.template | Yes | Yes | Yes | Yes | Yes | .xltx |
|  |  |  |  |  |  |  |

## Microsoft OneNote

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/onenote | Yes | Yes | Yes | No | No | .one |
|  |  |  |  |  |  |  |

## Microsoft PowerPoint

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/vnd.ms-powerpoint | Yes | Yes | Yes | Yes | Yes | .pot; .pps; .ppt |
| application/vnd.openxmlformats-officedocument.presentationml.presentation | Yes | Yes | Yes | Yes | Yes | .pptx |
| application/vnd.openxmlformats-officedocument.presentationml.slideshow | Yes | Yes | Yes | Yes | Yes | .ppsx |
| application/vnd.openxmlformats-officedocument.presentationml.template | Yes | Yes | Yes | Yes | Yes | .potx |
|  |  |  |  |  |  |  |

## Microsoft Project

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/vnd.ms-project | Yes | Yes | Yes | No | Yes | .mpp |
|  |  |  |  |  |  |  |

## Microsoft Publisher

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/x-mspublisher | Yes | Yes | Yes | Yes | Yes | .pub |
|  |  |  |  |  |  |  |

## Microsoft Visio

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/vnd.ms-visio.drawing | Yes | Yes | Yes | Yes | No |  |
| application/vnd.visio | Yes | Yes | Yes | Yes | Yes | .vsd |
|  |  |  |  |  |  |  |

## Microsoft Word

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/msword | Yes | Yes | Yes | Yes | Yes | .dat; .doc |
| application/rtf | Yes | Yes | Yes | Yes | Yes | .doc; .rtf |
| application/vnd.ms-word.document.macroenabled.12 | Yes | Yes | Yes | Yes | Yes | .docm |
| application/vnd.ms-word.template.macroenabled.12 | Yes | Yes | Yes | Yes | Yes | .dotm |
| application/vnd.openxmlformats-officedocument.wordprocessingml.document | Yes | Yes | Yes | Yes | Yes | .docx |
| application/vnd.openxmlformats-officedocument.wordprocessingml.template | Yes | Yes | Yes | Yes | Yes | .dotx |
|  |  |  |  |  |  |  |

## Microsoft Works

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/vnd.ms-works-ss | Yes | Yes | No | No | No | .wps |
| application/vnd.ms-works-wp | Yes | Yes | No | No | No | .wps |
|  |  |  |  |  |  |  |

## Open Document Format

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/vnd.oasis.opendocument.text | Yes | Yes | Yes | Yes | Yes | .odt |
|  |  |  |  |  |  |  |

## Other

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/json | Yes | Yes | Yes | Yes | Yes | n/a |
| application/octet-stream | Yes | No | No | No | No | .fluid |
| application/vnd.ms-graph | Yes | Yes | No | No | No |  |
| application/winhlp | Yes | Yes | No | No | No | .hlp |
| application/x-tnef | Yes | Yes | No | No | No |  |
|  |  |  |  |  |  |  |

## Plain Text

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| text/csv | Yes | Yes | Yes | Yes | Yes | .csv |
| text/plain | Yes | Yes | Yes | Yes | Yes | .con; .css; .csv; .dat; .pl; .txt |
|  |  |  |  |  |  |  |

## Portable Document Format

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/pdf | Yes | Yes | Yes | Yes | Yes | .pdf |
|  |  |  |  |  |  |  |

## Word Perfect

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/vnd.wordperfect; version=5.0 | Yes | Yes | Yes | No | No | .wpd |
| application/vnd.wordperfect; version=5.1 | Yes | Yes | Yes | No | No | .wpd |
| application/vnd.wordperfect; version=6.x | Yes | Yes | Yes | No | No | .wpd |
|  |  |  |  |  |  |  |

## Word Pro

| Mime type | File identification | Metadata extraction | Text extraction | Native viewer | Annotate viewer | Possible Extensions |
| --- | --- | --- | --- | --- | --- | --- |
| application/vnd.lotus-wordpro | Yes | Yes | No | No | No | .lwp |
|  |  |  |  |  |  |  |