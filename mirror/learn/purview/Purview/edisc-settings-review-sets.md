---
layout: Conceptual
title: Learn about review set settings in eDiscovery cases | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-settings-review-sets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about review set settings in eDiscovery cases.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-01T00:00:00.0000000Z
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
document_id: be003104-d03d-dbb9-8d49-3964c38a8648
document_version_independent_id: be003104-d03d-dbb9-8d49-3964c38a8648
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-settings-review-sets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-settings-review-sets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-settings-review-sets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: ad01e3d0-14e4-3c90-2808-281fa959e2d9
---

# Learn about review set settings in eDiscovery cases | Microsoft Learn

You can configure grouping settings for each Microsoft Purview eDiscovery case to control how the data in a review set is grouped and displayed. You can turn on the **Enable group** setting only for review sets in cases created in your organization after March 15, 2023.

Depending on when the case is created, items in a review set can be grouped in two ways:

- **Group review set items by Group ID and Thread ID**: When enabled, review set items are grouped by *Group ID* and *Thread ID*. This setting is the default for all cases created after March 15, 2023.
- **Group review set items by Family ID and Conversation ID**: When disabled, review set items are grouped by *Family ID* and *Conversation ID*. This setting is the default for all cases created before March 15, 2023.

For more information about review set grouping, see [Group and view documents in a review set](edisc-review-set-view).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Enable review set grouping settings for a case

To enable review set grouping settings for a case:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select **Case settings**.
4. On **Case settings**, select **Review sets**.
5. Select the **Enable group** toggle to enable grouping review set items by *Group ID* and *Thread ID*.

Note

For cases created before March 15, 2023, the **Enable group** toggle is disabled. Item grouping in review sets for these cases is based on *Family ID* and *Conversation ID*.

## Disable review set grouping settings for a case

To disable review set grouping settings for a case:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select **Case settings**.
4. On **Case settings**, select **Review sets**.
5. Select the **Enable group** toggle to disable grouping review set items by *Group ID* and *Thread ID*. Item grouping in review sets for cases is now based on *Family ID* and *Conversation ID*.