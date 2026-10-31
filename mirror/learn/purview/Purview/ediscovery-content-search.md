---
layout: Conceptual
title: Get started with Content search | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-content-search
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the Content search eDiscovery tool in the Microsoft Purview portal to search for content in different Microsoft 365 services.
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
- MED150
- MET150
ms.custom:
- seo-marvel-apr2020
- admindeeplinkCOMPLIANCE
locale: en-us
document_id: f2db87b7-1d87-fd4a-31de-e58b3379220d
document_version_independent_id: f2db87b7-1d87-fd4a-31de-e58b3379220d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-content-search.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-content-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-content-search.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 8992e0ec-fa50-a728-e920-ae8162ae3981
---

# Get started with Content search | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

You can use the Content search eDiscovery tool in the Microsoft Purview portal to search for in-place content such as email, documents, and instant messaging conversations in your organization. Use this tool to search for content in these cloud-based Microsoft 365 data sources:

- Exchange Online mailboxes
- SharePoint Online sites and OneDrive for Business accounts
- Microsoft Teams
- Microsoft 365 Groups
- Viva Engage

After you run a search, the number of content locations and an estimated number of search results are displayed on the search flyout page. You can quickly view statistics, such as the content locations that have the most items that match the search query. After you run a search, you can preview the results or export them to a local computer.

## Before you run a search

- To access to the Content search tool in the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149) (to run searches and preview results and export results), an administrator, compliance officer, or eDiscovery manager must be a member of the eDiscovery Manager role group in the Microsoft Purview portal. For more information, see [Assign eDiscovery permissions](ediscovery-assign-permissions).
- In an Exchange hybrid deployment, you can't use the Content search tool to search emails in on-premises mailboxes. You can only use the tool to search cloud-based mailboxes.
- In an Exchange hybrid deployment, you can search for Teams chat data in on-premises mailboxes. For more information, see [Search for and export Teams chat data for on-premises users](ediscovery-search-cloud-based-mailboxes-for-on-premises-users).

## Create and run a search

1. Go to the [Microsoft Purview portal](https://compliance.microsoft.com) and sign in using the credentials of an account that's been assigned the appropriate permissions.
2. In the left navigation pane, select **Content search**.
3. On the **Content search** page, select **New search**.
4. On the **Name and description** page, enter a name for the search, an optional description that helps identify the search. The name of the search must be unique in your organization.
5. On the **Locations** page, choose the content locations that you want to search. You can search mailboxes, sites, and public folders.

    ![Choose the content locations to search.](media/contentsearchlocations.png)

    1. **Exchange mailboxes**: Set the toggle to **On**. The option to search all Exchange mailboxes is automatically selected. If needed, select **Choose users, groups, or teams** to specify the mailboxes to search. Use the search box to find user mailboxes and distribution groups. You can also search the mailbox associated with a Microsoft Team (for channel messages), Microsoft 365 Group, and Viva Engage community. All Microsoft 365 Copilot and Microsoft 365 Copilot Chat activity data (user prompts and Copilot responses) generated in supported Microsoft 365 apps and services is stored in custodian mailboxes. For more information about the application data stored in mailboxes, see [Content stored in mailboxes for eDiscovery](ediscovery-what-is-stored-in-a-mailbox).
    2. **SharePoint sites**: Set the toggle to **On**. The option to search all SharePoint sites is automatically selected. Select **Choose sites** to specify SharePoint sites and OneDrive sites to search. Enter the URL for each site that you want to search. You can also add the URL for the SharePoint site for a Microsoft Team, Microsoft 365 Group, or Viva Engage community. The Recycle Bin in SharePoint sites is not indexed and therefore unavailable for searching. As a result, eDiscovery searches can't find any Recycle Bin content to place holds.
    3. **Exchange public folders**: Set the toggle to **On**. The option to search all Exchange public folders is automatically selected to search all public folders in your Exchange Online organization. You can't choose specific public folders to search. Leave the toggle switch off if you don't want search all public folders.
    4. Keep this checkbox selected to search for Teams content for on-premises users. For example, if you search all Exchange mailboxes in the organization and this checkbox is selected, the cloud-based storage used to store Teams chat data for on-premises users will be included in the scope of the search. For more information, see [Search for Teams chat data for on-premises users](ediscovery-search-cloud-based-mailboxes-for-on-premises-users).
6. On the **Conditions** page, enter a keyword query and add conditions to the search query if necessary.

    ![Configure the search query.](media/contentsearchquery.png)

    1. Specify keywords, message properties such as sent and received dates, or document properties such as file names or the date that a document was last changed. You can use more complex queries that use a Boolean operator, such as **AND**, **OR**, **NOT**, and **NEAR**. If you leave the keyword box empty, all content located in the specified content locations is included in the search results. For more information, see [Keyword queries and search conditions for eDiscovery](ediscovery-keyword-queries-and-search-conditions).
    2. Alternatively, you can select the **Show keyword list** checkbox and then enter a keyword in each row. If you do this, the keywords on each row are connected by a logical operator (**c:s**) that is similar in functionality to the **OR** operator in the search query that's created.

        **Why use the keyword list**? You can get statistics that show how many items match each keyword. This can help you quickly identify which keywords are the most (and least) effective. You can also use a keyword phrase (surrounded by parentheses) in a row. For more information about the keyword list and search statistics, see [Get keyword statistics for searches](ediscovery-view-keyword-statistics-for-content-search#get-keyword-statistics-for-searches).

        Note

        To help reduce issues caused by large keyword lists, you're limited to a maximum of 20 rows in the keyword list.
    3. You can add search conditions to narrow a search and return a more refined set of results. Each condition adds a clause to the search query that is created and run when you start the search. A condition is logically connected to the keyword query (specified in the keyword box) by a logical operator (**c:c**) that is similar in functionality to the **AND** operator. That means that items have to satisfy both the keyword query and one or more conditions to be included in the results. This is how conditions help to narrow your results. For a list and description of conditions that you can use in a search query, see [Search conditions](ediscovery-keyword-queries-and-search-conditions#search-conditions).
7. Review the search settings (and edit if necessary), and then select **Submit** to start the search.

To access this content search again or access other content searches listed on the **Content search** page, select a search to view the search summary and search statistics.

For more information about Content search, such as searching for content in different Microsoft 365 services, see [Feature reference for Content search](ediscovery-content-search-reference).