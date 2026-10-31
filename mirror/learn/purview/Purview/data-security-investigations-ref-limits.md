---
layout: Conceptual
title: Limits in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-ref-limits
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover the feature area and item limits for Microsoft Purview Data Security Investigations. Learn how to manage investigations effectively within support limits.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
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
document_id: f9e722e7-e8ca-9a08-c995-d0863fee743b
document_version_independent_id: f9e722e7-e8ca-9a08-c995-d0863fee743b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-ref-limits.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-ref-limits
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-ref-limits.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9c355b56-8838-f711-7807-d393fa5e89e8
---

# Limits in Data Security Investigations | Microsoft Learn

This article describes the limits in Microsoft Purview Data Security Investigations.

## Investigation limits

The following table lists the limits for investigations in Data Security Investigations.

| Description of limit | Data Security Investigations feature support |
| --- | --- |
| Total number of documents that you can add to an investigation. | 40 million |
| Total file size per investigation. | 1 TB |

## Purge limits

The following table lists the limits for purge in Data Security Investigations.

| Description of limit | Data Security Investigations feature support |
| --- | --- |
| Maximum number of items per purge search query. | 10,000 |

## Search and integration limits

The following table lists the search and integration limits for Data Security Investigations. These limits apply to searches and investigations created from the following solutions:

- [Audit search](data-security-investigations-search#audit-search)
- [Endpoint DLP evidence collection](data-security-investigations-search#endpoint-dlp-evidence-collection-preview). For more information about endpoint DLP, see [Learn about endpoint data loss prevention](endpoint-dlp-learn-about).
- [Insider Risk Management](data-security-investigations-investigation#create-an-investigation-from-insider-risk-management)
- [Microsoft Defender XDR](data-security-investigations-investigation#create-an-investigation-from-defender-xdr)

| Description of limit | Data Security Investigations feature support |
| --- | --- |
| Maximum items returned per search or integration query. | Approximately 3,000 |
| Maximum concurrent audit searches per user. | 10 |

Tip

If your investigation involves more than approximately 3,000 audit items, you can split the data into smaller time-based slices. For more information, see [Work with large audit search results](data-security-investigations-search#work-with-large-audit-search-results).