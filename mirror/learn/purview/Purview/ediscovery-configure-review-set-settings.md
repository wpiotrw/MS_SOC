---
layout: Conceptual
title: Configure review set grouping settings for eDiscovery (Premium) cases | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-configure-review-set-settings
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Configure review set settings that apply to a case in eDiscovery (Premium)
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-mar2020
locale: en-us
document_id: 03a4d285-4462-dd8a-6bb7-c7303d33ff72
document_version_independent_id: 03a4d285-4462-dd8a-6bb7-c7303d33ff72
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-configure-review-set-settings.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-configure-review-set-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-configure-review-set-settings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: e8f6a2bb-46b3-15d8-7a14-ae837ab0027f
---

# Configure review set grouping settings for eDiscovery (Premium) cases | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

You can configure grouping settings for each Microsoft Purview eDiscovery (Premium) case to control how the data in a review set is grouped and displayed. Turning on the **Enable group** setting is only available for review sets in cases created in your organization after March 15, 2023.

Depending when the case is created, items in a review set can be grouped in two ways:

- **Group review set items by Group ID and Thread ID**: When enabled, review set items are grouped by *Group ID* and *Thread ID*. This setting is the default for all cases created after March 15, 2023.
- **Group review set items by Family ID and Conversation ID**: When disabled, review set items are grouped by *Family ID* and *Conversation ID*. This setting is the default for all cases created before March 15, 2023.

For more information about review set grouping, see [Group and view documents in a review set](ediscovery-view-documents-in-review-set).

## Configure review set grouping settings for a case

To configure review set grouping settings for a case:

1. On the **eDiscovery (Premium)** page, select the case.
2. On the **Settings** tab, under **Review sets**, choose **Select**.
3. On the **Review sets** page, select the **Enable group** toggle to enable grouping review set items by *Group ID* and *Thread ID*.

Note

For cases created before March 15, 2023, the **Enable group** toggle is disabled. Item grouping in review sets for these cases is based on *Family ID* and *Conversation ID*.