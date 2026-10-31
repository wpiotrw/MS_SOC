---
layout: Conceptual
title: Feature reference for Content search | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-content-search-reference
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article contains reference information about the Content search eDiscovery tool in the Microsoft Purview portal to help you learn the many details about Content search.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: reference
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
- admindeeplinkMAC
- sfi-image-nochange
locale: en-us
document_id: f184525c-316e-af7e-5471-7b9581e17772
document_version_independent_id: f184525c-316e-af7e-5471-7b9581e17772
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-content-search-reference.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-content-search-reference
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-content-search-reference.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 75e1db17-59cd-c16d-ce52-892d68cb1b81
---

# Feature reference for Content search | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

This article describes features and functionality of Content search. To use the Content search eDiscovery tool in the Microsoft Purview portal to search for in-place content, see [Get started with Content search](ediscovery-content-search).

## Building a search query

For detailed information about creating a search query, using Boolean search operators and search conditions, and searching for sensitive information types and content shared with users outside your organization, see [Keyword queries and search conditions for Content Search](ediscovery-keyword-queries-and-search-conditions).

Keep the following things in mind when using the keyword list to create a search query.

- You have to select the **Show keyword list** checkbox and then type each keyword in a separate row to create a search query where the keywords (or keyword phrases) in each row are connected by the **OR** operator. If you paste a list of keywords in the keyword box or press the **Enter** key after typing a keyword, they won't be connected by the **OR** operator. Here are incorrect and correct examples of how to add a list of keywords.

    **Incorrect**

    ![The incorrect way to format a keyword list (by pasting the list into the keyword box).](media/fb54e3df-232a-439a-b3d7-27a60ec76a4c.png)

    **Correct**

    ![The correct way to format a keyword list (by selecting checkbox and then pasting list).](media/5d511a7b-c1f9-499c-bffe-e075bfc9adec.png)
- You can also prepare a list of keywords or keyword phrases in an Excel file or a plain text file, and then copy and paste your list into the keyword list. To do this, you have to select the **Show keyword list** check box. Then, select the first row in the keyword list and paste your list. Each line from the Excel or text file is pasted into separate row in the keyword list.
- After you create a query using the keyword list, it's a good idea to verify the search query syntax to make the search query is what you intended. In the search query that's displayed under **Query** in the details pane, the keywords are separated by the text **(c:s)**. This indicates that the keywords are connected by a logical operator similar in functionality to the **OR** operator. Similarly, if your search query includes conditions, the keywords and the conditions are separated by the text **(c:c)**. This indicates that the keywords are connected to the conditions with a logical operator similar in functionality to the **AND** operator. Here's an example of the search query (displayed in the Details pane) that results when using the keyword list and a condition.

    ![Example of the query that's created when using the keyword list and a condition.](media/b463750c-57fa-4602-9fed-0d5a420db3ad.png)
- When you run a content search, Microsoft 365 automatically checks your search query for unsupported characters and for Boolean operators that may not be capitalized. Unsupported characters are often hidden and typically cause a search error or return unintended results. For more information about the unsupported characters that are checked, see [Check your Content Search query for errors](ediscovery-check-your-content-search-query-for-errors).
- If you have a search query that contains keywords for non-English characters (such as Chinese characters), you can select **Query language-country/region**![Query language-country/region icon in Content search.](media/8d4b60c8-e1f1-40f9-88ae-ee2a7eca0886.png) and select a language-country/region culture code value for the search. The default language/region is neutral. How can you tell if you need to change the language setting for a content search? If you're certain content locations contain the non-English characters you're searching for, but the search returns no results, the language setting may be the cause.

## Partially indexed items

- Partially indexed items in mailboxes are included in the estimated search results. Partially indexed items from SharePoint and OneDrive aren't included in the estimated search results. For more information, see [Partially indexed items in eDiscovery](ediscovery-partially-indexed-items-in-content-search).

## Searching OneDrive accounts

- To collect a list of the URLs for the OneDrive sites in your organization, see [Create a list of all OneDrive locations in your organization](/en-us/onedrive/list-onedrive-urls). This script in this article creates a text file that contains a list of all OneDrive sites. To run this script, you have to install and use the SharePoint Online Management Shell. Be sure to append the URL for your organization's MySite domain to each OneDrive site that you want to search. This is the domain that contains all your OneDrive; for example, `https://contoso-my.sharepoint.com`. Here's an example of a URL for a user's OneDrive site: `https://contoso-my.sharepoint.com/personal/sarad_contoso_onmicrosoft.com`.

    In the rare case of a person's user principal name (UPN) being changed, the URL for their OneDrive location is changed to incorporate the new UPN. If this happens, you have to modify a content search by adding the user's new OneDrive URL and removing the old one. For more information, see [How UPN changes affect the OneDrive URL](/en-us/onedrive/upn-changes).

## Searching Microsoft Teams and Microsoft 365 Groups

You can search the mailbox that's associated with a Microsoft Team or Microsoft 365 Group. Because Microsoft Teams is built on Microsoft 365 Groups, searching them is similar. In both cases, only the group or team mailbox is searched. The mailboxes of the group or team members aren't searched. To search them, you've to specifically add them to the search.

Keep the following things in mind when searching for content in Microsoft Teams and Microsoft 365 Groups.

- To search for content located in Teams and Microsoft 365 Groups, you have to specify the mailbox and SharePoint site that are associated with a team or group.
- Content from private channels is stored in each user's mailbox, not the team mailbox. To search for content in private channels, see [eDiscovery of private and shared channels](/en-us/microsoftteams/ediscovery-investigation#ediscovery-of-private-and-shared-channels).
- Run the **Get-UnifiedGroup** cmdlet in Exchange Online to view properties for a team or a Microsoft 365 Group. This is a good way to get the URL for the site that's associated with a team or a group. For example, the following command displays selected properties for a Microsoft 365 Group named Senior Leadership Team:

    ```text
    Get-UnifiedGroup "Senior Leadership Team" | FL DisplayName,Alias,PrimarySmtpAddress,SharePointSiteUrl
    DisplayName            : Senior Leadership Team
    Alias                  : seniorleadershipteam
    PrimarySmtpAddress     : seniorleadershipteam@contoso.onmicrosoft.com
    SharePointSiteUrl      : https://contoso.sharepoint.com/sites/seniorleadershipteam
    ```

    Note

    To run the **Get-UnifiedGroup** cmdlet, you have to be assigned the View-Only Recipients role in Exchange Online or be a member of a role group that's assigned the View-Only Recipients role.
- When a user's mailbox is searched, any team or Microsoft 365 Group that the user is a member of won't be searched. Similarly, when you search a team or a Microsoft 365 Group, only the group mailbox and group site that you specify is searched. The mailboxes and OneDrive for Business accounts of group members aren't searched unless you explicitly add them to the search.
- To get a list of the members of a team or a Microsoft 365 Group, you can view the properties on the **Home** &gt; [**Groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855) page in the Microsoft 365 admin center. Alternatively, you can run the following command in Exchange Online PowerShell:

    ```powershell
    Get-UnifiedGroupLinks <group or team name> -LinkType Members | FL DisplayName,PrimarySmtpAddress
    ```

    Note

    To run the **Get-UnifiedGroupLinks** cmdlet, you have to be assigned the View-Only Recipients role in Exchange Online or be a member of a role group that's assigned the View-Only Recipients role.
- Conversations that are part of a Teams channel are stored in the mailbox that's associated with the team. Similarly, files that team members share in a channel are stored on the team's SharePoint site. Therefore, you have to add the team mailbox and SharePoint site as a content location to search conversations and files in a channel.
- Alternatively, conversations that are part of the Chat list in Teams are stored in the Exchange Online mailbox of the users who participate in the chat. And files that a user shares in Chat conversations are stored in the OneDrive for Business account of the user who shares the file. Therefore, you have to add the individual user mailboxes and OneDrive for Business accounts as content locations to search conversations and files in the Chat list.

    Note

    In an Exchange hybrid deployment, users with an on-premises mailbox might participate in conversations that are part of the Chat list in Teams. In this case, content from these conversations is also searchable because it's saved to a cloud-based storage area (called a *cloud-based mailbox for on-premises users*) for users who have an on-premises mailbox. For more information, see [Search for Teams chat data for on-premises users](ediscovery-search-cloud-based-mailboxes-for-on-premises-users).
- Every team or team channel contains a Wiki for note-taking and collaboration. The Wiki content is automatically saved to a file with a .mht format. This file is stored in the Teams Wiki Data document library on the team's SharePoint site. You can use the Content Search tool to search the Wiki by specifying the team's SharePoint site as the content location to search.

    Note

    The capability to search the Wiki for a team or channel (when you search the team's SharePoint site) was released on June 22, 2017. Wiki pages that were saved or updated on that date or after are available to be searched. Wiki pages last saved or updated before that date aren't available for search.
- Summary information for meetings and calls in a Teams channel are also stored in the mailboxes of users who dialed into the meeting or call. This means you can use Content Search to search these summary records. Summary information includes:

    - Date, start time, end time, and duration of a meeting or call
    - The date and time when each participant joined or left the meeting or call
    - Calls sent to voice mail
    - Missed or unanswered calls
    - Call transfers, which are represented as two separate calls

    It can take up to 8 hours for meeting and call summary records to be available to be searched.

    In the search results, meeting summaries are identified as **Meeting** in the **Type field**, and call summaries are identified as **Call**. Also, conversations that are part of a Teams channel and 1xN chats are identified as **IM** in the **Type** field.

    ![Teams meetings, calls, and 1xN chats are identified in the Type field.](media/o365-contentsearch-teams-messagekind.png)

    For more information, see [Microsoft Teams launches eDiscovery for calls and meetings](https://techcommunity.microsoft.com/t5/microsoft-teams-blog/microsoft-teams-launches-ediscovery-for-calling-and-meetings/ba-p/210947).
- Card content generated by apps in Teams channels, 1:1 chats, and 1xN chats are stored in mailboxes and can be searched. A *card* is a UI container for short pieces of content. Cards can have multiple properties and attachments, and can include items that trigger card actions. For more information, see [Cards](/en-us/microsoftteams/platform/task-modules-and-cards/what-are-cards)

    Like other Teams content, where card content is stored is based on where the card was used. Content for cards used in a Teams channel is stored in the Teams group mailbox. Card content for 1:1 and 1xN chats are stored in the mailboxes of the chat participants.

    To search for card content, you can use the `kind:microsoftteams` or `itemclass:IPM.SkypeTeams.Message` search conditions. When reviewing search results, card content generated by bots in a Teams channel has the **Sender/Author** email property as `<appname>@teams.microsoft.com`, where `appname` is the name of the app that generated the card content. If card content was generated by a user, the value of **Sender/Author** identifies the user.

    When viewing card content in Content search results, the content appears as an attachment to the message. The attachment is named `appname.html`, where `appname` is the name of the app that generated the card content. The following screenshots show how card content (for an app named Asana) appears in Teams and in the results of a search.

    **Card content in Teams**

    ![Card content in Teams channel message.](media/cardcontentteams.png)

    **Card content in search results**

    ![Same card content in the results of a Content search.](media/cardcontentediscoverysearchresults.png)

    Note

    To display images from card content in search results at this time (such as the checkmarks in the previous screenshot), you have to be signed into Teams (at https://teams.microsoft.com) in a different tab in the same browser session that you use to view the search results. Otherwise, image placeholders are displayed.
- You can use the **Kind** email property or the **Message kind** search condition to search specifically for content in Teams.

    - To use the **Kind** property as part of the keyword search query, in the **Keywords** box of a search query, type `kind:microsoftteams`.

        ![Use kind:microsoftteams in the Keywords box.](media/o365-contentsearch-teams-keywords.png)
    - To use a search condition, add the **Message kind** condition and use the value `microsoftteams`.

        ![Use the Message kind condition with the value microsoftteams.](media/o365-contentsearch-teams-messagekindcondition.png)

    Conditions are logically connected to the keyword query by the **AND** operator. That means an item must match both the keyword query and the search condition to be returned in the search results. For more information, see the "Guidelines for using conditions" section in [Keyword queries and search conditions for Content Search.](ediscovery-keyword-queries-and-search-conditions#guidelines-for-using-conditions)

## Searching Viva Engage Groups

You can use the **ItemClass** email property or the **Type** search condition to search specifically for conversation items in Viva Engage Groups.

- To use the **ItemClass** property as part of the keyword search query, in the **Keywords** box of a search query, you can type one (or all) of the following property:value pairs:

    - ItemClass:IPM.Yammer.message
    - ItemClass:IPM.Yammer.poll
    - ItemClass:IPM.Yammer.praise
    - ItemClass:IPM.Yammer.question

    For example, you can use the following search query to return Viva Engage messages and Viva Engage praise items:

    ![Use the ItemClass property to search for Viva Engage items.](media/viva-engage-content-search1.png)
- Alternatively, you can use the **Type** email condition and select **Viva Engage messages** to return Viva Engage items. For example, the following search query returns all Viva Engage conversation items that contain the keyword "confidential".

    ![Use the Type condition card to search for Viva Engage conversation items.](media/viva-search-content-search2.png)

## Searching inactive mailboxes

You can search inactive mailboxes in a content search. To get a list of the inactive mailboxes in your organization, run the command `Get-Mailbox -InactiveMailboxOnly` in Exchange Online PowerShell. Alternatively, you can go to **Data lifecycle management** &gt; **Microsoft 365** &gt; **Retention** in the Microsoft Purview portal, and then select **More**![Navigation Bar ellipses.](media/9723029d-e5cd-4740-b5b1-2806e4f28208.gif) &gt; **Inactive mailboxes**.

Here are a few things to keep in mind when searching inactive mailboxes.

- If an existing content search includes a user mailbox and that mailbox is made inactive, the content search will continue to search the inactive mailbox when you rerun the search after it becomes inactive.
- Sometimes a user may have an active mailbox and an inactive mailbox that have different SMTP addresses. In this case, only the specific mailbox that you select as a location for a content search is searched. In other words, if you add a user's mailbox to a search, you can't assume that both their active and inactive mailboxes are searched. Only the mailbox that you explicitly add to the search is searched.
- You can use Security & Compliance PowerShell to create a content search to search an inactive mailbox. To do this, you have to pre-append a period ( . ) to the email address of the inactive mailbox. For example, the following command creates a content search that searches an inactive mailbox with the email address pavelb@contoso.onmicrosoft.com:

    ```powershell
    New-ComplianceSearch -Name InactiveMailboxSearch -ExchangeLocation .pavelb@contoso.onmicrosoft.com -AllowNotFoundExchangeLocationsEnabled $true
    ```
- We strongly recommend that you avoid having an active mailbox and inactive mailbox with the same SMTP address. If you need to reuse the SMTP address that is assigned to an inactive mailbox, we recommend that you recover the inactive mailbox or restore the contents of an inactive mailbox to an active mailbox (or the archive of an active mailbox), and then delete the inactive mailbox. For more information, see one of the following articles:

    - [Recover an inactive mailbox in Office 365](recover-an-inactive-mailbox)
    - [Restore an inactive mailbox in Office 365](restore-an-inactive-mailbox)
    - [Delete an inactive mailbox in Office 365](delete-an-inactive-mailbox)

## Searching disconnected or de-licensed mailboxes

If the Exchange Online license (or the entire Microsoft 365 license) is removed from a user account or in Microsoft Entra ID, the user's mailbox becomes a *disconnected* mailbox. This means that the mailbox is no longer associated with the user account. Here's what happens when searching disconnected mailboxes:

- If the license is removed from a mailbox, the mailbox is no longer searchable.
- If an existing content search includes a mailbox in which the license is removed, no search results from the disconnected mailbox will be returned if you rerun the content search.
- If you use the **New-ComplianceSearch** cmdlet to create a content search and specify a disconnected mailbox as the Exchange content location to search, the content search won't return any search results from the disconnected mailbox.

If you need to preserve the data in a disconnected mailbox so that it's searchable, you must place a hold on the mailbox before removing the license. This preserves the data and keeps the disconnected mailbox searchable until the hold is removed. For more information about holds, see [How to identify the type of hold placed on an Exchange Online mailbox](ediscovery-identify-a-hold-on-an-exchange-online-mailbox).

## Searching for content in a SharePoint multi-geo environment

If it's necessary for an eDiscovery manager to search for content in SharePoint and OneDrive in different regions in a [SharePoint multi-geo environment](/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365), then you need to do the following things to make that happen:

1. Create a separate user account for each satellite geo location that the eDiscovery manager needs to search. To search for content in sites in that geo location, the eDiscovery manager must sign in to the account you created for that location, and then run a content search.
2. Create a search permissions filter for each satellite geo location (and corresponding user account) the eDiscovery manager needs to search. Each of these search permissions filters limits the scope of the content search to a specific geo location when the eDiscovery manager is signed in to the user account associated with that location.

Tip

You don't have to use this strategy when using the search tool in [eDiscovery (Premium)](ediscovery-overview). That's because all datacenters are searched when you search SharePoint sites and OneDrive accounts in Microsoft Purview eDiscovery (Premium). You have to use this strategy of region-specific user accounts and search permissions filters only when using the Content Search tool and running searches associated with [eDiscovery cases](ediscovery-standard-get-started).

For example, let's say that an eDiscovery manager needs to search for SharePoint and OneDrive content in satellite locations in North American, Europe, and Asia Pacific. The first step is to create three users accounts, one for each location. The next step is to create three search permissions filters, one for each location *and* corresponding user account. Here are examples of the three search permissions filters for this scenario. In each of these examples, the **Region** specifies the SharePoint datacenter location for that geo and the **Users** parameter specifies the corresponding user account.

**North America**

```powershell
New-ComplianceSecurityFilter -FilterName "SPMultiGeo-NAM" -Users ediscovery-nam@contoso.com -Region NAM -Action ALL
```

**Europe**

```powershell
New-ComplianceSecurityFilter -FilterName "SPMultiGeo-EUR" -Users ediscovery-eur@contoso.com -Region EUR -Action ALL
```

**Asia Pacific**

```powershell
New-ComplianceSecurityFilter -FilterName "SPMultiGeo-APC" -Users ediscovery-apc@contoso.com -Region APC -Action ALL
```

Keep the following things in mind when using search permissions filters to search for content in multi-geo environments:

- The **Region** parameter directs searches to the specified satellite location. If an eDiscovery manager only searches SharePoint and OneDrive sites outside of the region specified in the search permissions filter, no search results are returned.
- The **Region** parameter doesn't control searches of Exchange mailboxes. All datacenters are searched when you search mailboxes.

For more information about using search permissions filters in a multi-geo environment, see the "Searching and exporting content in Multi-Geo environments" section in [Set up compliance boundaries for eDiscovery investigations](ediscovery-set-up-compliance-boundaries#searching-and-exporting-content-in-multi-geo-environments).

## Need help with eDiscovery issues?

Check out the [Resolve common eDiscovery issues](/en-us/microsoft-365/troubleshoot/ediscovery/resolve-ediscovery-issues) article for basic troubleshooting steps that you can take to identify and resolve issues that you might encounter during an eDiscovery search or elsewhere in the eDiscovery process.