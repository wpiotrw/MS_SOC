---
layout: Conceptual
title: Create eDiscovery holds in an eDiscovery case | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-create-holds
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: You can create a hold that's associated with an eDiscovery case in Microsoft 365 to preserve content relevant to an investigation or legal case.
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
ms.custom: admindeeplinkMAC
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: 6b1ba699-1b7a-680d-4bf4-dbc100b92bce
document_version_independent_id: 6b1ba699-1b7a-680d-4bf4-dbc100b92bce
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-create-holds.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-create-holds
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-create-holds.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 25ef0672-c84b-0ab9-bafe-6027fcfe1ce8
---

# Create eDiscovery holds in an eDiscovery case | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

You can use a Microsoft Purview eDiscovery (Premium) or (Standard) case to create holds to preserve content that might be relevant to the case. You can place a hold on the Exchange mailboxes and OneDrive for Business accounts of people you're investigating in the case. You can also place a hold on the mailboxes and sites that are associated with Microsoft Teams, Microsoft 365 groups, and Viva Engage Groups. When you place content locations on hold, content is preserved until you remove the content location from the hold or until you delete the hold.

Important

For long term data retention not related to eDiscovery investigations, it is strongly advised to use retention policies and retention labels. For more information, see [Learn about retention policies and retention labels](retention#when-to-use-retention-policies-and-retention-labels-or-ediscovery-holds).

After you create an eDiscovery hold, it may take up to 24 hours for the hold to take effect.

When you create a hold, you have the following options to scope the content that's preserved in the specified content locations:

- Create an infinite hold where all content in the specified locations is placed on hold. Alternatively, you can create a query-based hold where only the content in the specified locations that matches a search query is placed on hold.
- Specify a date range to preserve only the content that was sent, received, or created within that date range. Alternatively, you can hold all content in specified locations regardless of when sent, received, or created.

## How to create an eDiscovery hold

To create an eDiscovery hold that's associated with an eDiscovery (Premium) or (Standard) case:

1. Go to [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149) and sign in using the credentials for user account with the appropriate eDiscovery permissions.
2. In the left navigation pane, select **Show all**, and then select **eDiscovery &gt; Premium** or **eDiscovery &gt; Standard**.
3. On the **eDiscovery &gt; Premium** or **eDiscovery (Standard)** page, select the name of the case that you want to create the hold in.
4. On the **Home** page for the case, select the **Hold** tab.
5. On the **Hold** page, select **Create**.
6. On the **Name your hold** workflow page, give the hold a name and add an optional description, and then select **Next**. The name of the hold must be unique in your organization.
7. On the **Choose locations** workflow page, choose the content locations that you want to place on hold. You can place mailboxes, sites, and public folders on hold.

    ![Choose the content locations to place on hold.](media/ediscoveryholdlocations.png)

    1. **Exchange mailboxes**: Set the toggle to **On** and then select **Choose users, groups, or teams** to specify the mailboxes to place on hold. Use the search box to find user mailboxes and distribution groups (to place a hold on the mailboxes of group members) to place on hold. You can also place a hold on the associated mailbox for a Microsoft Team, Microsoft 365 group, and Viva Engage Group. For more information about the application data that is preserved when a mailbox is placed on hold, see [Content stored in mailboxes for eDiscovery](ediscovery-what-is-stored-in-a-mailbox).

    Important

    When you select a distribution list to be placed on hold, the hold is placed on each of the member mailboxes in the distribution list when the policy is created. Subsequent changes in the distribution list do not change or update the holds or the policy.

    1. **SharePoint sites**: Set the toggle to **On** and then select **Choose sites** to specify SharePoint sites and OneDrive accounts to place on hold. Type the URL for each site that you want to place on hold. You can also add the URL for the SharePoint site for a Microsoft Team, Microsoft 365 group or a Yammer Group.

    Important

    To create a hold for a subsite related to a SharePoint Online site, you must use the *Path* property in a query filter to select a specific subsite.

    1. **Exchange public folders**: Set the toggle to **On** to put all public folders in your Exchange Online organization on hold. You can't choose specific public folders to put on hold. Leave the toggle switch off if you don't want to put a hold on public folders.

    Important

    When adding Exchange mailboxes or SharePoint sites to a hold, you must explicitly add at least one content location to the hold. In other words, if you set the toggle to **On** for mailboxes or sites, you must select specific mailboxes or sites to add to the hold. Otherwise, the eDiscovery hold will be created but no mailboxes or sites will be added to the hold.
8. When finished adding locations to the hold, select **Next**.
9. To create a query-based hold using keywords or conditions, complete the following steps. To preserve all content in the specified content locations, select **Next**.

    ![Create a query-based hold with keyword and conditions.](media/ediscoveryholdquery.png)

    1. In the box under **Keywords**, type a query to preserve only the content that matches the query criteria. You can specify keywords, email message properties, or site properties, such as file names. You can also use more complex queries that use a Boolean operator, such as **AND**, **OR**, or **NOT**.
    2. Select **Add condition** to add one or more conditions to narrow the query for the hold. Each condition adds a clause to the KeyQL search query that is created and run when you create the hold. For example, you can specify a date range so that email or site documents that were created within the date ranged are preserved. A condition is logically connected to the keyword query (specified in the **Keywords** box) and other conditions by the **AND** operator. That means items have to satisfy both the keyword query and the condition to be preserved.

    For more information about creating a search query and using conditions, see [Keyword queries and search conditions for eDiscovery](ediscovery-keyword-queries-and-search-conditions).
10. After configuring a query-based hold, select **Next**.
11. Review your settings (and edit them if necessary), and then select **Submit**.

After creating a hold, check that the hold is applied successfully by navigating to the **Hold** tab in the case and selecting the hold policy. For more information about troubleshooting holds with errors, see [Resolve eDiscovery hold errors](/en-us/microsoft-365/troubleshoot/ediscovery/resolve-ediscovery-hold-issues).

Note

When you create a query-based hold, all content from selected locations is initially placed on hold. Subsequently, any content that doesn't match the specified query is cleared from the hold every seven to 14 days. However, a query-based hold won't clear content if more than five holds of any type are applied to a content location, or if any item has indexing issues.

## Query-based holds placed on sites

Keep the following things in mind when you place a query-based eDiscovery hold on documents located in SharePoint sites:

- A query-based hold initially preserves all documents in a site for a short period of time after they're deleted. That means when a document is deleted, it is moved to the Preservation Hold library even if it doesn't match the criteria of the query-based hold. However, deleted documents that don't match a query-based hold will be removed by a timer job that processes the Preservation Hold library. The timer job runs periodically and compares all documents in the Preservation Hold library to your query-based eDiscovery holds (and other types of holds and retention policies). The timer job deletes the documents that don't match a query-based hold and preserves the documents that do.
- Query-based holds shouldn't be used to perform targeted preservation, like preserving documents in a specific folder or site or by using other location-based hold criteria. Doing so may have unintended results. We recommend using non-location based hold criteria such as keywords, date ranges, or other document properties to preserve site documents.

## Search locations on eDiscovery hold

When you [search for content](ediscovery-search-for-content) in an eDiscovery (Standard) case, you can quickly configure the search to only search the content locations that have been placed on a hold associated with the case.

Select the **Locations on hold** option to search all the content locations that have been placed on hold. If the case contains multiple eDiscovery holds, the content locations from all holds are searched when you select this option. Additionally, if a content location was placed on a query-based hold, only the items that match the hold query are searched when you run the search. In other words, only the content that matches both the hold criteria and the search criteria is returned with the search results. For example, if a user was placed on query-based case hold that preserves items that were sent or created before a specific date, only those items would be searched. This is accomplished by connecting the case hold query and the search query by an **AND** operator.

Here are some other things to keep in mind when searching locations on eDiscovery hold:

- If a content location is part of multiple holds within the same case, the hold queries are combined by **OR** operators when you search that content location using the all case content option. Similarly, if a content location is part of two different holds, where one is query-based and the other is an infinite hold (where all content is placed on hold), then all content is search because of the infinite hold.
- If a search is configured it to search locations on hold and then you change an eDiscovery hold in the case (by adding or removing a location or changing a hold query), the search configuration is updated with those changes. However, you have to rerun the search after the hold is changed to update the search results.
- If multiple eDiscovery holds are placed on a single location in an eDiscovery case and you select to search locations on hold, the maximum number of keywords for that search query is 500. That's because the search combines all the query-based holds by using the **OR** operator. If there are more than 500 keywords in the combined hold queries and the search query, then all content in the mailbox is searched, not just that content that matches the query-based case holds.
- If an eDiscovery hold has a status of **On (Pending)**, you can still search the locations on hold while the hold is being turned on.

## Preserve content in Microsoft Teams

Conversations that are part of a Microsoft Teams channel are stored in the mailbox that's associated with the Microsoft Team. Similarly, files that team members share in a channel are stored on the team's SharePoint site. Therefore, you have to place the Team mailbox and SharePoint site on eDiscovery hold to preserve conversations and files in a channel.

Alternatively, conversations that are part of the Chat list in Teams (called *1:1 chats* or *1:N group chats*) are stored in the mailboxes of the users who participate in the chat. And files that users share in chat conversations are stored in the OneDrive account of the user who shares the file. Therefore, you have to add the individual user mailboxes and OneDrive accounts to an eDiscovery hold to preserve conversations and files in the chat list. It's a good idea to place a hold on the mailboxes of members of a Microsoft Team in addition to placing the team mailbox and site on hold.

Note

If your organization has an Exchange hybrid deployment (or your organization synchronizes an on-premises Exchange organization with Office 365) and has enabled Microsoft Teams, on-premises users can use the Teams chat application and participate in 1:1 chats and 1:N group chats. These conversations are stored in cloud-based storage that's associated with an on-premises user. If an on-premises user is placed on an eDiscovery hold, the Teams chat content in the cloud-based storage will be preserved. For more information, see [Search for Teams chat data for on-premises users](ediscovery-search-cloud-based-mailboxes-for-on-premises-users).

For more information about preserving Teams content, see [Place a Microsoft Teams user or team on legal hold](/en-us/MicrosoftTeams/legal-hold).

### Preserve card content

Similarly, card content generated by apps in Teams channels, 1:1 chats, and 1:N group chats are stored in mailboxes and is preserved when a mailbox is placed on an eDiscovery hold. A *card* is a UI container for short pieces of content. Cards can have multiple properties and attachments, and can include items that trigger card actions. For more information, see [Cards](/en-us/microsoftteams/platform/task-modules-and-cards/what-are-cards). Like other Teams content, where card content is stored is based on where the card was used. Content for cards used in a Teams channel is stored in the Teams group mailbox. Card content for 1:1 and 1xN chats are stored in the mailboxes of the chat participants.

### Preserve meeting and call information

Summary information for meetings and calls in a Teams channel is also stored in the mailboxes of users who dialed into the meeting or call. This content is also preserved when an eDiscovery hold is placed on user mailboxes.

### Preserve content in private channels

Starting in February 2020, we also turned on the ability to preserve content in private channels. Because private channel chats are stored in the mailboxes of the chat participants, placing a user mailbox on eDiscovery hold preserves private channel chats. Also, if a user mailbox was placed on an eDiscovery hold prior to February 2020, the hold will now automatically apply to private channel messages stored in that mailbox. Preserving files shared in private channels is also supported.

### Preserve wiki content

Every Team or team channel also contains a Wiki for note taking and collaboration. The Wiki content is automatically saved to a file with a .mht format. This file is stored in the Teams Wiki Data document library on the team's SharePoint site. You can preserve the wiki content by adding the team's SharePoint site to an eDiscovery hold.

Note

The capability to preserve Wiki content for a Team or team channel (when you place the team's SharePoint site on hold) was released on June 22, 2017. If a team site is on hold, the Wiki content will be retained starting on that date. However, if a team site is on hold and the Wiki content was deleted before June 22, 2017, the Wiki content was not preserved.

### Microsoft 365 groups

Teams is built on Microsoft 365 groups. Therefore, placing Microsoft 365 groups on eDiscovery hold is similar placing Teams content on hold.

Keep the following things in mind when placing both Teams and Microsoft 365 groups on an eDiscovery hold:

- As previously explained, to place content located in Teams and Microsoft 365 groups on hold, you have to specify the mailbox and SharePoint site that associated with a group or team.
- Run the **Get-UnifiedGroup** cmdlet in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) to view properties for Teams and Microsoft 365 groups. This is a good way to get the URL for the site that's associated with a Team or Microsoft 365 group. For example, the following command displays selected properties for a Microsoft 365 group named Senior Leadership Team:

    ```text
    Get-UnifiedGroup "Senior Leadership Team" | FL DisplayName,Alias,PrimarySmtpAddress,SharePointSiteUrl
    
    DisplayName            : Senior Leadership Team
    Alias                  : seniorleadershipteam
    PrimarySmtpAddress     : seniorleadershipteam@contoso.onmicrosoft.com
    SharePointSiteUrl      : https://contoso.sharepoint.com/sites/seniorleadershipteam
    ```

    Note

    To run the **Get-UnifiedGroup** cmdlet, you have to be assigned the View-Only Recipients role in Exchange Online or be a member of a role group that's assigned the View-Only Recipients role.
- When a user's mailbox is searched, any Team or Microsoft 365 group that the user is a member of won't be searched. Similarly, when you place a Team or Microsoft 365 group on eDiscovery hold, only the group mailbox and group site are placed on hold. The mailboxes and OneDrive for Business sites of group members aren't placed on hold unless you explicitly add them to the eDiscovery hold. So if you have to place a Team or Microsoft 365 group on hold for a legal reason, consider adding the mailboxes and OneDrive accounts of team or group members on the same hold.
- To get a list of the members of a Team or Microsoft 365 group, you can view the properties on the [**Groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855) page in the Microsoft 365 admin center. Alternatively, you can run the following command in Exchange Online PowerShell:

    ```powershell
    Get-UnifiedGroupLinks <group or team name> -LinkType Members | FL DisplayName,PrimarySmtpAddress
    ```

    Note

    To run the **Get-UnifiedGroupLinks** cmdlet, you have to be assigned the View-Only Recipients role in Exchange Online or be a member of a role group that's assigned the View-Only Recipients role.

## Preserve content in OneDrive accounts

Important

The retention period for deleted OneDrive accounts is different from the retention period for mailboxes. For more information about the retention period for deleted OneDrive accounts, see [OneDrive retention and deletion](/en-us/sharepoint/retention-and-deletion#the-onedrive-deletion-process).

To collect a list of the URLs for the OneDrive for Business sites in your organization so you can add them to a hold or search associated with an eDiscovery case, see [Create a list of all OneDrive locations in your organization](/en-us/onedrive/list-onedrive-urls). The script in this article creates a text file that contains a list of all OneDrive sites in your organization. To run this script, you have to install and use the SharePoint Online Management Shell. Be sure to append the URL for your organization's MySite domain to each OneDrive site that you want to search. This is the domain that contains all your OneDrive; for example, `https://contoso-my.sharepoint.com`. Here's an example of a URL for a user's OneDrive site: `https://contoso-my.sharepoint.com/personal/sarad_contoso_onmicrosoft.com`.

Important

The URL for a user's OneDrive account includes their user principal name (UPN) (for example, `https://alpinehouse-my.sharepoint.com/personal/sarad_alpinehouse_onmicrosoft_com`). In the rare case that a person's UPN is changed, their OneDrive URL will also change to incorporate the new UPN. If a user's OneDrive account is part of an eDiscovery hold, and their UPN is changed, you need to update the hold by adding the user's new OneDrive URL and removing the old one. If the URL for the OneDrive site changes, previously placed holds on the site remain effective and content is preserved. For more information, see [How UPN changes affect the OneDrive URL](/en-us/onedrive/upn-changes).

## Removing content locations from an eDiscovery hold

After a mailbox, SharePoint site, or OneDrive account is removed from an eDiscovery hold, a *delay hold* is applied. This means that the actual removal of the hold is delayed for 30 days to prevent data from being permanently deleted (purged) from a content location. This gives admins an opportunity to search for or recover content that will be purged after an eDiscovery hold is removed. The details of how the delay hold works for mailboxes and sites are different.

- **Mailboxes:** A delay hold is placed on a mailbox the next time the Managed Folder Assistant processes the mailbox and detects that an eDiscovery hold was removed. Specifically, a delay hold is applied to a mailbox when the Managed Folder Assistant sets one of the following mailbox properties to **True**:

    - **DelayHoldApplied:** This property applies to email-related content (generated by people using Outlook and Outlook on the web) that's stored in a user's mailbox.
    - **DelayReleaseHoldApplied:** This property applies to cloud-based content (generated by non-Outlook apps such as Microsoft Teams, Microsoft Forms, and Microsoft Viva Engage) that's stored in a user's mailbox. Cloud data generated by a Microsoft app is typically stored in a hidden folder in a user's mailbox.

    When a delay hold is placed on the mailbox (when either of the previous properties is set to **True**), the mailbox is still considered to be on hold for an unlimited hold duration, as if the mailbox was on Litigation Hold. After 30 days, the delay hold expires, and Microsoft 365 will automatically attempt to remove the delay hold (by setting the DelayHoldApplied or DelayReleaseHoldApplied property to **False**) so that the hold is removed. After either of these properties are set to **False**, the corresponding items that are marked for removal are purged the next time the mailbox is processed by the Managed Folder Assistant.

    For more information, see [Managing mailboxes on delay hold](ediscovery-identify-a-hold-on-an-exchange-online-mailbox#managing-mailboxes-on-delay-hold).
- **SharePoint and OneDrive sites:** Any SharePoint or OneDrive content that's being retained in the Preservation Hold library isn't deleted during the 30-day delay hold period after a site is removed from an eDiscovery hold. This is similar to what happens when a site is released from a retention policy. Additionally, you can't manually delete this content in the Preservation Hold library during the 30-day delay hold period. To release a site from the 30-day delay hold/grace period hold, see the [Can't delete a site because of an invalid retention policy or eDiscovery hold](/en-us/sharepoint/troubleshoot/sites/compliance-policy-blocking-site-deletion) troubleshooting article.

    For more information, see [Releasing a policy for retention](retention#releasing-a-policy-for-retention).

A delay hold is also applied to content locations on hold when you close an eDiscovery (Standard) case because holds are turned off when a case is closed. For more information about closing a case, see [Close, reopen, and delete an eDiscovery (Standard) case](ediscovery-close-reopen-delete-cases).

## eDiscovery hold limits

The following table lists the limits for eDiscovery cases and case holds.

| Description of limit | Limit |
| --- | --- |
| Maximum number of cases for an organization. | No limit |
| Maximum number of eDiscovery hold policies for an organization. This limit includes the combined total of hold policies in eDiscovery (Standard) and eDiscovery (Premium) cases. | 10,000^1^ |
| Maximum number of mailboxes in a single eDiscovery hold. This limit includes the combined total of user mailboxes, and the mailboxes associated with Microsoft 365 groups, Microsoft Teams, and Viva Engage Groups. | 1,000 |
| Maximum number of sites in a single eDiscovery hold. This limit includes the combined total of OneDrive for Business sites, SharePoint sites, and the sites associated with Microsoft 365 groups, Microsoft Teams, and Viva Engage Groups. &lt;br/ | 100 |
| Maximum number of cases displayed on the eDiscovery home page, and the maximum number of items displayed on the Holds, Searches, and Export tabs within a case. | 1,000^1^ |
| Hold limits for SharePoint sites and OneDrive | For details, see [SharePoint limits](/en-us/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits#hold-limits). |

Note

^1^ To view a list of more than 1,000 cases, holds, searches, or exports, you can use the corresponding Security & Compliance PowerShell cmdlet:

- [Get-ComplianceCase](/en-us/powershell/module/exchange/get-compliancecase)
- [Get-CaseHoldPolicy](/en-us/powershell/module/exchange/get-caseholdpolicy)
- [Get-ComplianceSearch](/en-us/powershell/module/exchange/get-compliancesearch)
- [Get-ComplianceSearchAction](/en-us/powershell/module/exchange/get-compliancesearchaction)