---
layout: Conceptual
title: Use the eDiscovery Export Tool in Microsoft Edge | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-configure-edge-to-export-search-results
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: You have to enable ClickOnce support to use the newest version of Microsoft Edge to download search results from Content Search and eDiscovery in the security and Microsoft Purview portal.
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
locale: en-us
document_id: dc3c9967-a62b-1967-e968-67fde8997c2f
document_version_independent_id: dc3c9967-a62b-1967-e968-67fde8997c2f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-configure-edge-to-export-search-results.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-configure-edge-to-export-search-results
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-configure-edge-to-export-search-results.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: f7d5f68c-050e-9887-37ce-81c963b664cf
---

# Use the eDiscovery Export Tool in Microsoft Edge | Microsoft Learn

Important

The eDiscovery Export tool was permanently **retired on August 31, 2025**, this functionality isn't available in the new [eDiscovery experience](edisc).

As a result of recent changes to the newest version of Microsoft Edge, ClickOnce support is no longer enabled by default. To continue using the eDiscovery Export Tool to download Content Search or eDiscovery search results, you either need to use [Microsoft Internet Explorer](https://support.microsoft.com/help/17621/internet-explorer-downloads) or enable ClickOnce support in the newest version of Microsoft Edge.

## Enable ClickOnce support in Microsoft Edge

1. In Microsoft Edge, go to **edge://flags/#edge-click-once**.
2. If the existing value is set to **Default** or **Disabled** in the dropdown list, change it to **Enabled**.

    ![Select Enabled from dropdown list.](media/clickonceimage1.png)
3. Scroll down to the bottom of the browser window and select **Restart** to restart Microsoft Edge.

    ![Select Restart.](media/clickonceimage2.png)

Note

Organizations can use Group Policy to disable ClickOnce support. To check if there's an organizational policy for ClickOnce support, go to **edge://policy**. The following screenshot shows that ClickOnce is enabled across the entire organization. If this policy value is set to **false**, you'll need to contact an admin in your organization.

![List of Edge organizational policies.](media/clickonceimage3.png)

## Install and run the eDiscovery Export Tool

1. Select **Download results** on the flyout page of an export in Content Search or an eDiscovery case.

    ![Select Download results on the flyout page to download search results.](media/clickonceexport1.png)
2. You'll be prompted with a confirmation to launch the tool, select **Open**. If the eDiscovery Export Tool isn't installed, you'll be prompted with a Security Warning.

    ![Select Open to launch the eDiscovery Export Tool.](media/clickonceimage4.png)
3. Select **Install**. After it's installed, the export tool will launch automatically.

For more information, see the following articles:

- [Export Content Search results](ediscovery-export-search-results)
- [How to enable experiment flags in Microsoft Edge](https://microsoftedgesupport.microsoft.com/hc/articles/360034075294-How-to-enable-experiment-flags-in-Microsoft-Edge-Insider-channels)