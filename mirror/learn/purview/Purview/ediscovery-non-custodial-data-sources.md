---
layout: Conceptual
title: Add non-custodial data sources to an eDiscovery (Premium) case | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-non-custodial-data-sources
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: You can add non-custodial data sources to an eDiscovery (Premium) case and place a hold on the data source. Non-custodial data sources are reindexed, so any content that was marked as partially indexed is reprocessed to make it fully and quickly searchable.
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
document_id: 0e5f80c8-0eda-30e8-272c-ed773ee255bb
document_version_independent_id: 0e5f80c8-0eda-30e8-272c-ed773ee255bb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-non-custodial-data-sources.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-non-custodial-data-sources
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-non-custodial-data-sources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: af49a7c2-5c36-dfe0-249f-03f732e1df93
---

# Add non-custodial data sources to an eDiscovery (Premium) case | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

In Microsoft Purview eDiscovery (Premium) cases, it doesn't always meet your needs to associate a Microsoft 365 data source with a custodian in the case. But you may still need to associate that data with a case so that you can search it, add it to a review set, and analyze and review it.

Non-custodial data sources in eDiscovery (Premium) let you add data to a case without having to associate it to a custodian. It also applies the same eDiscovery (Premium) functionality to non-custodial data that's available for data associated with custodian. Two of the most useful things that you can apply to non-custodial data is placing it on hold and processing it using [Advanced indexing](ediscovery-indexing-custodian-data).

## Add a non-custodial data source

Complete the following steps to add and manage non-custodial data sources in an eDiscovery (Premium) case.

1. In the Microsoft Purview portal, select **eDiscovery** &gt; **Premium**.
2. Select the **Cases** tab and select the case that you want to add the data to.
3. Select the **Data sources** tab and then select **Add data source** &gt; **Add data locations**.
4. On the **New non-custodial data locations** flyout page, choose the data sources that you want to add to the case. Select one or more of the following data source locations:

    - **SharePoint**: Expand this section and select **Edit** to add [SharePoint sites](/en-us/sharepoint/guide-to-sharepoint-modern-experience). Complete the following steps to add sites and configure holds:

        1. Select a site in the list or you can search for a site by typing the URL of the site in the search bar. Select the sites that you want to add as non-custodian data sources and select **Add**.
        2. After you add non-custodial data sources, you can place those locations on hold or not. Select or unselect the **Hold** checkbox next to the data source to place it on hold.
        3. Select **Add** at the bottom of the **New non-custodial data locations** flyout page to add the data sources to the case.
    - **Exchange**: Expand this section and select **Edit** to add one or more [Exchange mailboxes](/en-us/exchange/recipients-in-exchange-online/recipients-in-exchange-online). Complete the following steps to add mailboxes and configure holds:

        1. Type a name or alias (a minimum of three characters) in the search box for mailboxes or distribution groups. Select the mailboxes that you want to add as non-custodian data sources and select **Add**.
        2. After you add non-custodial data sources, you can place those locations on hold or not. Select or unselect the **Hold** checkbox next to the data source to place it on hold.
        3. Select **Add** at the bottom of the **New non-custodial data locations** flyout page to add the data sources to the case.

        Note

        You can use the **SharePoint** and **Exchange** sections to add sites and mailboxes associated with a Team or Viva Engage group as non-custodial data sources. You have to separately add the mailbox and site associated with a Team or Viva Engage group. Also, adding a root site URL (such as `https://contoso-my.sharepoint.com/personal/` or `https://contoso-my.sharepoint.com/`) as a SharePoint data source isn't supported. You have to add specific sites.
    - **Teams**: Expand this section and select **Add Teams locations** to add one or more [Microsoft Teams channels](/en-us/microsoftteams/teams-channels-overview). Complete the following steps to add channels and configure holds:

        1. On the **Channels** page, enter a team name and select from the channels associated with the team. You can add up to 10 teams at one time and all the associated private, standard, and shared channels. Select **Next**. This automatically selects the [storage locations] (/purview/ediscovery-teams-workflow#where-teams-content-is-stored) where the channel messages and files are stored.
        2. On the **Configure holds** page, select the locations associated with each Team and channel to place on a hold. Select **Next**.
        3. On the summary page, review the selected channel locations and hold configuration. Select **Add channels** to add the channels and configure holds.
        4. The **Status** page confirms if the locations were added successfully or if the location already exists in the case. Select **Done**.

Each non-custodial data source that you added is listed on the **Data sources** page. Non-custodial data sources are identified by the *Data location* value in the **Source type** column.

After you add non-custodial data sources to the case, a job named *Reindexing non-custodial data* is created and displayed on the **Jobs** tab of the case. After the job is created, the Advanced indexing process in initiated and the data sources are reindexed. For more information about managing holds, see [Manage holds in eDiscovery (Premium)](ediscovery-managing-holds).

## Release a hold for non-custodial data sources

After you place a hold on a non-custodial data source, a hold policy that contains the non-custodial data sources for the case is automatically created. When you place other non-custodial data sources on hold, they're added to this hold policy.

To release a hold on a non-custodial data source, complete the following steps:

1. In the Microsoft Purview portal, select **eDiscovery** &gt; **Premium**.
2. Select the **Cases** tab and select the case that you want to add the data to.
3. Select the **Data sources** tab and the locations to release from hold.
4. Select **Release**.
5. Select **Yes** to release the hold for the location. Any holds placed on the data sources in other cases still apply.