---
layout: Conceptual
title: Microsoft Purview Data Sharing Lineage | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-lineage-purview-data-sharing
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to view lineage of shared datasets, shared using Microsoft Purview Data Sharing.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 9ef663d7-218d-afec-4c25-718cb7583b64
document_version_independent_id: 9ef663d7-218d-afec-4c25-718cb7583b64
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-lineage-purview-data-sharing.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-lineage-purview-data-sharing
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-lineage-purview-data-sharing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7cf8f81d-2989-4e5d-aa91-5191d10a3323
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/1cb9c90f-9a3f-4389-8367-0a20c542621f
platformId: b6fbc49c-a918-fc3e-7f26-9f3f863f293f
---

# Microsoft Purview Data Sharing Lineage | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently being retired, with support provided until September 2025 to allow for migration to [Microsoft Fabric external data sharing](/en-us/fabric/governance/external-data-sharing-overview).

This article discusses how to view the lineage of datasets shared using [Microsoft Purview Data Sharing](../concept-data-share). With these tools, users can discover and track lineage of data across boundaries like organizations, departments, and even data centers.

Important

This article is about lineage for [Microsoft Purview Data Sharing](../concept-data-share). If you are using Azure Data Share, use this article for lineage: [Azure Data Share lineage](../how-to-link-azure-data-share).

## Common scenarios

Data Sharing lineage aims to provide detailed information for root cause analysis and impact analysis.

Some common scenarios include:

- Full view of datasets shared in and out of your organization
- Root cause analysis for upstream dataset dependencies
- Impact analysis for shared datasets

### Full view of datasets shared in and out of your organization

Data officers can see a list of all bi-directionally shared datasets with their partner organizations. They can search and discover the datasets by organization name and see a complete view of all outgoing and incoming shares.

See the Microsoft Entra ID share lineage section to see a full view of outgoing and incoming shares.

### Root cause analysis for upstream dataset dependencies

A report has incorrect information because of upstream data issues from an external Microsoft Purview Data Sharing activity. The data engineers can understand upstream failures, understand possible cause, and further contact the owner of the share to fix the issues causing their data discrepancy.

See the lineage of a share or Microsoft Entra ID share lineage sections to see the upstream dependencies for your assets.

### Impact analysis for shared datasets

Data producers want to know who will be impacted when they make a change to their datasets. With a lineage map, a data producer can easily understand the impact of the downstream internal or external partners who are consuming data using Microsoft Purview Data Sharing.

See the lineage of a share or Microsoft Entra ID share lineage sections to see downstream dependencies of your shared assets.

## Lineage of a share

To see the data sharing lineage for your sent share or received share asset, you only need to have [data reader permissions](../data-gov-classic-permissions) on the collection where the asset is housed.

1. Discover your sent share or received share asset in the Catalog [search](../unified-catalog-data-assets-search) or [browse](../unified-catalog-data-assets-search#browse-the-unified-catalog) for the share in the data catalog, and narrow results to only data shares.

    ![Screenshot of the data catalog search, showing the data share filter selected and a share highlighted.](../media/how-to-lineage-purview-data-sharing/search-for-share.png)
2. Select your data share asset.
3. Select the lineage tab to see a graph with upstream and downstream dependencies.

    ![Screenshot of the data share asset lineage page, showing the lineage tab highlighted and a lineage graph.](../media/how-to-lineage-purview-data-sharing/select-lineage-tab.png)
4. You can select the files or folders, or the Microsoft Entra asset in the lineage canvas and see the data sharing lineage for those assets.

    ![Screenshot of the data share asset lineage page, showing the data asset selected and the switch to asset button highlighted.](../media/how-to-lineage-purview-data-sharing/select-lineage-asset.png)

## Microsoft Entra ID share lineage

1. You can search for your Microsoft Entra tenant asset in the Catalog using the search bar, or filtering by **Source type** and selecting **Microsoft Entra ID**.
2. Select your Microsoft Entra ID, then select the **Lineage** tab to see a lineage graph with either upstream or downstream dependencies.

    ![Screenshot of the Microsoft Entra asset with the lineage tab selected, showing the lineage map.](../media/how-to-lineage-purview-data-sharing/active-directory-lineage.png)
3. If you're seeing all sent shares, or all received shares, you can select the button to switch the view to see the other.

    ![Screenshot of the Microsoft Entra ID shares lineage map, showing the Switch to received shares button highlighted.](../media/how-to-lineage-purview-data-sharing/switch-shares.png)

    Note

    If you do not see this button it may be because your Microsoft Entra ID does not have any sent/received shares, or that you do not have permission on the collection where the sent/received shares are housed.
4. You can also select any file or folder in the lineage canvas and see the data sharing lineage for those assets.

    ![Screenshot of the Microsoft Entra ID shares lineage map, showing an asset selected and the Switch to asset button highlighted.](../media/how-to-lineage-purview-data-sharing/switch-to-asset.png)

Important

For Data Share assets to show in Microsoft Purview, the ADLS Gen2 or Blob Storage account that the shares (sent share or received share) belong to should be registered with Microsoft Purview and the user needs Reader permission on the collection where they are housed.

## Troubleshoot

Here are some common issues when viewing data sharing lineage and their possible resolutions.

### Can't see the recipient Microsoft Entra tenant on the sent share lineage

If you're unable to see the recipient Microsoft Entra tenant on the sent share lineage, it means the recipient hasn't attached the share yet.

### Can't find a sent share or received share asset in the Catalog

Sent or received share assets are housed in the same collection as their registered storage account assets.

- If the storage accounts the share assets belong to aren't registered, the share assets won't be discoverable.
- If you don't have a minimum of Data Reader permission to the collection where the share asset is housed, the share assets aren't discoverable.