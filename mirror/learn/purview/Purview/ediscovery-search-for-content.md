---
layout: Conceptual
title: Search for content in an eDiscovery (Standard) case | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-search-for-content
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Search for content that may be relevant to an eDiscovery (Standard) case.
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
document_id: 1384bc3e-4b12-2ea4-6a2a-31748b498268
document_version_independent_id: 1384bc3e-4b12-2ea4-6a2a-31748b498268
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-search-for-content.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-search-for-content
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-search-for-content.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: d372aa81-cf1c-f45b-8f2e-83590b79bdd6
---

# Search for content in an eDiscovery (Standard) case | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

After a Microsoft Purview eDiscovery (Standard) case is created and people of interest in the case are placed on hold, you can create and run one or more searches for content relevant to the case. Searches associated with an eDiscovery (Standard) case aren't listed on the **Content search** page in the Microsoft Purview portal. These searches are listed on the **Searches** page of the eDiscovery (Standard) case the searches are associated with. This also means that searches associated with a case can only be accessed by case members.

For organizations that have EU General Data Protection Regulation (GDPR) requirements to protect and enable individuals' privacy rights inside the European Union (EU), you can also manage investigations in response to a Data Subject Requests (DSRs) submitted by a person in your organization. The User Data Search case tool has been retired, and its functionality has merged with eDiscovery (Standard). You can now use content to search for content to support DSRs all locations supported by eDiscovery (Standard) searches.

To create an eDiscovery (Standard) search:

1. Go to https://compliance.microsoft.com and sign in using the credentials for user account that has been assigned the appropriate eDiscovery permissions and is a member of the case.
2. In the left navigation pane of the Microsoft Purview portal, select **Show all**, and then select **eDiscovery (Standard)**.
3. On the **eDiscovery (Standard)** page, select the case that you want to create an associated search, and then select **Open case**.
4. On the **Home** page for the case, select the **Searches** tab, and then select **New search**.

    ![Select New search to create an eDiscovery (Standard) search.](media/coreediscoverysearch1.png)
5. In the **New search** workflow, type a name for the search, and an optional description that helps identify the search. The name of the search must be unique in your organization.
6. On the **Locations** page, choose the content locations that you want to search. You can search mailboxes, sites, and public folders.

    ![Choose the content locations to place on hold.](media/contentsearchlocations.png)

    1. **Exchange mailboxes**: Set the toggle to **On** and then select **Choose users, groups, or teams** to specify the mailboxes to place on hold. Use the search box to find user mailboxes and distribution groups (to place a hold on the mailboxes of group members) to place on hold. You can also search the mailbox associated with a Microsoft Team (for channel messages), Office 365 Group, and Viva Engage Group. All Copilot activity data (user prompts and Copilot responses) generated in supported Microsoft 365 apps and services is stored in custodian mailboxes. For more information about the application data stored in mailboxes, see [Content stored in mailboxes for eDiscovery](ediscovery-what-is-stored-in-a-mailbox).
    2. **SharePoint sites**: Set the toggle to **On** and then select **Choose sites** to specify SharePoint sites and OneDrive accounts to place on hold. Type the URL for each site that you want to place on hold. You can also add the URL for the SharePoint site for a Microsoft Team, Office 365 Group, or Viva Engage Group. The Recycle Bin in SharePoint sites isn't indexed and therefore unavailable for searching. As a result, eDiscovery searches can't find any Recycle Bin content to place holds.
    3. **Exchange public folders**: Set the toggle to **On** to put all public folders in your Exchange Online organization on hold. You can't choose specific public folders to put on hold. Leave the toggle switch off if you don't want to put a hold on public folders.
    4. Keep this checkbox selected to search for Teams content for on-premises users. For example, if you search all Exchange mailboxes in the organization and this checkbox is selected, the cloud-based storage used to store Teams chat data for on-premises users is included in the scope of the search. For more information, see [Search for Teams chat data for on-premises users](ediscovery-search-cloud-based-mailboxes-for-on-premises-users).
7. On the **Define your search conditions** page, type a keyword query and add conditions to the search query if necessary.

    ![Configure the search query.](media/contentsearchquery.png)

    1. Specify keywords, message properties such as sent and received dates, or document properties such as file names or the date that a document was last changed. You can use more complex queries that use a Boolean operator, such as **AND**, **OR**, **NOT**, and **NEAR**. If you leave the keyword box empty, all content located in the specified content locations is included in the search results. For more information, see [Keyword queries and search conditions for eDiscovery](ediscovery-keyword-queries-and-search-conditions).
    2. Alternatively, you can select the **Show keyword list** checkbox and the type a keyword in each row. If you do this, the keywords on each row are connected by a logical operator (**c:s**) that is similar in functionality to the **OR** operator in the search query that's created.

        Why use the keyword list? You can get statistics that show how many items match each keyword. This can help you quickly identify which keywords are the most (and least) effective. You can also use a keyword phrase (surrounded by parentheses) in a row. For more information about the keyword list and search statistics, see [Get keyword statistics for searches](ediscovery-view-keyword-statistics-for-content-search#get-keyword-statistics-for-searches).

        Note

        To help reduce issues caused by large keyword lists, you're limited to a maximum of 20 rows in the keyword list.
    3. You can add search conditions to narrow a search and return a more refined set of results. Each condition adds a clause to the search query that is created and run when you start the search. A condition is logically connected to the keyword query (specified in the keyword box) by a logical operator (**c:c**) that is similar in functionality to the **AND** operator. That means that items have to satisfy both the keyword query and one or more conditions to be included in the results. This is how conditions help to narrow your results. For a list and description of conditions that you can use in a search query, see [Search conditions](ediscovery-keyword-queries-and-search-conditions#search-conditions).
8. Review the search settings (and edit if necessary), and then submit the search to start it.

After the search is completed, you can preview the search results. If necessary, select **Refresh** on the **Searches** page to display the search you created.

## More information about searching content locations

- When you select **Choose users, groups, or teams** to specify mailboxes to search, the mailbox picker that's displayed is empty. This is by design to enhance performance. To add recipients to this list, select **Choose users, groups, or teams**, type a name (a minimum of three characters) in the search box, select the check box next to the name, and then select **Choose**.
- You can add inactive mailboxes, Microsoft Teams, Viva Engage Groups, Office 365 Groups, and distribution groups to the list of mailboxes to search. Dynamic distribution groups aren't supported. If you add Microsoft Teams, Viva Engage Groups, or Office 365 Groups, the group or team mailbox is searched; the mailboxes of the group members aren't searched.
- To add sites to the search, turn on the toggle and then select **Choose sites**. Type the URL for each site that you want to search. You can also add the URL for the SharePoint site for a Microsoft Team, a Viva Engage Group, or an Office 365 Group.