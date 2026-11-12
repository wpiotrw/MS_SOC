---
layout: Conceptual
title: Connect to Azure Data Share | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-link-azure-data-share
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to connect an Azure Data Share account with Microsoft Purview to search assets and track data lineage.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: e66bc8d0-8b05-5152-e50c-dcc1babe57a9
document_version_independent_id: e66bc8d0-8b05-5152-e50c-dcc1babe57a9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-link-azure-data-share.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-link-azure-data-share
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-link-azure-data-share.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7cf8f81d-2989-4e5d-aa91-5191d10a3323
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/1cb9c90f-9a3f-4389-8367-0a20c542621f
platformId: 6033a107-7b6b-5ef5-3118-aabda7691fe2
---

# Connect to Azure Data Share | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This article discusses how to connect your [Azure Data Share](/en-us/azure/data-share/overview) account with Microsoft Purview and govern the shared datasets (both outgoing and incoming) in your data estate. Various data governance personas can discover and track lineage of data across boundaries like organizations, departments and even data centers.

Important

- This article is about lineage for the [Azure Data Share service](/en-us/azure/data-share/overview). If you are using data sharing in Microsoft Purview, use this article for lineage: [Microsoft Purview Data Sharing lineage](../how-to-lineage-purview-data-sharing).
- Data sharing is accessed through the [classic Microsoft Purview governance portal](../use-microsoft-purview-governance-portal): https://web.purview.azure.com

## Common scenarios

Data Share Lineage is aimed to provide detailed information for root cause analysis and impact analysis.

### Scenario 1: 360 view of datasets shared in/out for a partner organization or internal department

Data officers can see a list of all datasets that are bi-directionally shared with their partner organizations. They can search and discover the datasets by organization name and see a complete view of all outgoing and incoming shares.

### Scenario 2: Root cause analysis - upstream dependency on datasets coming into organization (consumer view of incoming shares)

A report has incorrect information because of upstream data issues from an external Data Share account. The data engineers can understand upstream failures, be informed about the reasons, and further contact the owner of the share to fix the issues causing their data discrepancy.

### Scenario 3: Impact analysis on datasets going outside organization (provider view of outgoing shares)

Data producers want to know who will be impacted upon making a change to their dataset. Using lineage, a data producer can easily understand the impact of the downstream internal or external partners who are consuming data using Azure Data Share.

## Azure Data Share and Microsoft Purview connected experience

To connect your Azure Data Share and Microsoft Purview account, do the following:

1. Create a Microsoft Purview account. All the Data Share lineage information will be collected by a Microsoft Purview account. You can use an existing one or create a new Microsoft Purview account.
2. Connect your Azure Data Share to your Microsoft Purview account.

    1. In the Microsoft Purview governance portal, you can go to **Management Center** and connect your Azure Data Share under the **External connections** section.
    2. Select **+ New** on the top bar, find your Azure Data Share in the pop-up side bar and add the Data Share account. Run a snapshot job after connecting your Data Share to Microsoft Purview account, so that the Data Share assets and lineage information is visible in Microsoft Purview.

        ![Screenshot of the management center to link Azure Data Share.](../media/how-to-link-azure-data-share/connect-to-data-share.png)
3. Execute your snapshot in Azure Data Share.

    - Once the Azure Data share connection is established with Microsoft Purview, you can execute a snapshot for your existing shares.
    - If you don’t have any existing shares, go to the Azure Data Share portal to [share your data](/en-us/azure/data-share/share-your-data)[and subscribe to a data share](/en-us/azure/data-share/subscribe-to-data-share).
    - Once the share snapshot is complete, you can view associated Data Share assets and lineage in Microsoft Purview.
4. Discover Data Share accounts and share information in your Microsoft Purview account.

    - In the home page of Microsoft Purview account, select **Browse by asset type** and select the **Azure Data Share** tile. You can search for an account name, share name, share snapshot, or partner organization. Otherwise apply filters on the Search result page for account name, share type (sent vs received shares).

        ![Screenshot of Azure Data share in the search result page.](../media/how-to-link-azure-data-share/azure-data-share-search-result-page.png)

    Important

    For Data Share assets to show in Microsoft Purview, a snapshot job must be run after you connect your Data Share to Microsoft Purview.
5. Track lineage of datasets shared with Azure Data Share.

    - From the Microsoft Purview search result page, choose the Data share snapshot (received/sent) and select the **Lineage** tab, to see a lineage graph with upstream and downstream dependencies.

    ![Screenshot of the lineage of datasets shared using Azure Data Share.](../media/how-to-link-azure-data-share/azure-data-share-lineage.png)