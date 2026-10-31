---
layout: Conceptual
title: Configure general settings in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-settings-general
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Set the default license level for new eDiscovery cases in Microsoft Purview. Learn who can change this setting and which Microsoft 365 subscription requirements apply.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
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
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: ffa4af09-37d7-ed54-5d88-6368e7dde2bd
document_version_independent_id: ffa4af09-37d7-ed54-5d88-6368e7dde2bd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-settings-general.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-settings-general
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-settings-general.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5c49fa7f-9546-0d51-21be-d83c222d2851
---

# Configure general settings in eDiscovery | Microsoft Learn

General settings in eDiscovery let you set the default license level for all cases you create in eDiscovery.

Only users assigned to the eDiscovery *Administrators* role can access this setting. When enabled, the Microsoft 365 Enterprise E5 subscription is the default level for all new eDiscovery cases. You can override this setting on a per-case basis after creating a new case in the settings for a case. This setting isn't available for organizations with Microsoft 365 Enterprise E3 subscription.

## Enable or disable premium eDiscovery features

Note

Enabling premium eDiscovery features only affects new cases and doesn't affect the license state of any existing cases.

To enable or disable premium features for your organization:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery *Administrator* permissions.
2. Select the **eDiscovery** solution card, then go to **Settings** &gt; **eDiscovery** &gt; **General**.
3. Select or clear the toggle for **eDiscovery (Premium)**.