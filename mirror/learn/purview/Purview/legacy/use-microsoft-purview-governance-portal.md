---
layout: Conceptual
title: Classic Microsoft Purview governance portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/use-microsoft-purview-governance-portal
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to use the classic Microsoft Purview governance portal.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2024-04-17T00:00:00.0000000Z
ms.custom: sfi-image-nochange
locale: en-us
document_id: 33acbd81-de88-e353-0b54-01d7d536445d
document_version_independent_id: 33acbd81-de88-e353-0b54-01d7d536445d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/use-microsoft-purview-governance-portal.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/use-microsoft-purview-governance-portal
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/use-microsoft-purview-governance-portal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6b5e8328-df16-5756-95a7-13c883e53a6b
---

# Classic Microsoft Purview governance portal | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This article gives an overview of some of the features in the classic Microsoft Purview governance portal.

Tip

Microsoft Purview has a new experience! If you're a new Microsoft Purview customer, or if you want more information, see our [article on the new portal](../purview-portal) or the article about our new [data governance experience](../unified-catalog).

## Prerequisites

- An Active Microsoft Purview account is already created in Azure portal
- The user has permissions to access [the classic Microsoft Purview governance portal](https://web.purview.azure.com/resource/).

## Launch Microsoft Purview account

- You can launch the Microsoft Purview account directly by going to `https://web.purview.azure.com`, selecting **Microsoft Entra ID** and the account name. Or by going to `https://web.purview.azure.com/resource/yourpurviewaccountname`
- To launch your Microsoft Purview account from the [Azure portal](https://portal.azure.com), go to Microsoft Purview accounts in Azure portal, select the account you want to launch and launch the account.

    ![Screenshot of Microsoft Purview window in Azure portal, with the Microsoft Purview governance portal button highlighted.](../media/use-purview-studio/open-purview-studio.png)

Tip

If you can't access the portal, [confirm you have the necessary permissions](../data-gov-classic-permissions).

## Home page

**Home** is the starting page for the Microsoft Purview governance portal.

![Screenshot of the homepage.](../media/use-purview-studio/purview-homepage.png)

The following list summarizes the main features of **Home page**. Each number in the list corresponds to a highlighted number in the preceding screenshot.

1. Friendly name of the catalog. You can set catalog name in **Management** &gt; **Account information**.
2. Catalog analytics shows the number of:

    - Data sources
    - Assets
    - Glossary terms
3. The search box allows you to search for data assets across the data catalog.
4. The quick access buttons give access to frequently used functions of the application. The buttons that are presented, depend on the role assigned to your user account at the root collection.

    - For *collection admin*, the available button is **Knowledge center**.
    - For *data curator*, the buttons are **Browse assets**, **Manage glossary**, and **Knowledge center**.
    - For *data reader*, the buttons are **Browse assets**, **View glossary**, and **Knowledge center**.
    - For *data source admin* + *data curator*, the buttons are **Browse assets**, **Manage glossary**, and **Knowledge center**.
    - For *data source admin* + *data reader*, the buttons are **Browse assets**, **View glossary**, and **Knowledge center**.

    Note

    For more information about Microsoft Purview roles, see [Access control in Microsoft Purview](../data-gov-classic-permissions).
5. The left navigation bar helps you locate the main pages of the application.
6. The **Recently accessed** tab shows a list of recently accessed data assets. For information about accessing assets, see [Search the Data Catalog](../unified-catalog-data-assets-search) and [Browse by asset type](../unified-catalog-data-assets-search#browse-the-unified-catalog). **My items** tab is a list of data assets owned by the logged-on user.
7. **Links** contains links to region status, documentation, pricing, overview, and Microsoft Purview status
8. The top navigation bar contains information about release notes/updates, change purview account, notifications, help, and feedback sections.

## Knowledge center

The knowledge center is where you can find all the videos and tutorials related to Microsoft Purview.

## Localization

Microsoft Purview is localized in 18 languages. To change the language used, go to the **Settings** from the top bar and select the desired language from the dropdown.

![Screenshot of how to localize the Microsoft Purview governance portal.](../media/use-purview-studio/localization.png)

Note

Only generally available features are localized. Features still in preview are in English regardless of which language is selected.

## Guided tours

Each UX in the Microsoft Purview governance portal will have guided tours to give overview of the page. To start the guided tour, select **help** on the top bar and select **guided tours**.

![Screenshot of the guided tour.](../media/use-purview-studio/guided-tour.png)