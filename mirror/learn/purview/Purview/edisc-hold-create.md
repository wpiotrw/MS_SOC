---
layout: Conceptual
title: Create holds in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-hold-create
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Create a hold for an eDiscovery case to preserve content relevant to an investigation or legal matter. Learn how to scope holds by location, query, and date range.
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
document_id: 87118514-2796-9136-25ad-3c88b24853fb
document_version_independent_id: 87118514-2796-9136-25ad-3c88b24853fb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-hold-create.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-hold-create
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-hold-create.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 1b56f409-4261-22de-d22f-573409270696
---

# Create holds in eDiscovery | Microsoft Learn

Create holds to preserve content that might be relevant to an eDiscovery case. Place a hold on the Exchange mailboxes and OneDrive accounts of people you're investigating in the case. You can also place a hold on the mailboxes and sites that are associated with Microsoft Teams, Microsoft 365 groups, and Viva Engage Groups. When you place content locations on hold, you preserve content until you remove the content location from the hold or until you delete or release the hold.

Important

After you create an eDiscovery hold, it might take up to 24 hours for the hold to take effect. For long term data retention not related to eDiscovery investigations, use retention policies and retention labels. For more information, see [Learn about retention policies and retention labels](retention#when-to-use-retention-policies-and-retention-labels-or-ediscovery-holds).

eDiscovery holds **require an eligible license on every user whose content you preserve**. Frontline subscriptions such as Office 365 F1 and F3 don't include the rights required to be the *target* of an eDiscovery hold. Before you add a user to a hold, confirm the user's assigned subscription includes eDiscovery hold rights.

The eDiscovery (Premium) hold capabilities required for query-based, time-bound, and custodian-scoped holds are included only in higher tiers (for example, Microsoft 365 E5 / A5 / G5 or the Microsoft 365 E5 Compliance and E5 eDiscovery & Audit add-ons).

For the authoritative list of which hold capabilities are included in each subscription, see [Microsoft 365 guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#ediscovery). If the user's current subscription doesn't include the required rights, assign an add-on (such as Microsoft 365 E5 Compliance) **before** creating the hold. Placing a user on hold without proper licensing isn't supported.

When you create a hold, use the following options to scope the content that's preserved in the specified content locations:

- Create an infinite hold where all content in the specified locations is placed on hold. Alternatively, create a query-based hold where only the content in the specified locations that matches a search query is placed on hold.
- Specify a date range to preserve only the content that was sent, received, or created within that range. Alternatively, hold all content in specified locations regardless of when it was sent, received, or created.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Create a hold

Tip

Do you prefer an interactive configuration guide experience? Check out the [Apply a hold](https://mslearn.cloudguides.com/guides/Apply%20a%20hold%20with%20Microsoft%20Purview%20eDiscovery) guide.

To create an eDiscovery hold associated with an eDiscovery case, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card and then select **Cases** in the left navigation.
3. Select a case, and then select the **Hold policies** tab.
4. On the **Hold policies** dashboard, select **Create policy**.
5. On the **Enter details to get started** page, complete the following fields:

    - **Policy name**: Give the hold policy a name (required). The hold policy name must be unique in your organization.
    - **Policy description**: Add an optional description to help others understand this hold policy.
6. Select **Create** to create the new hold policy and start your hold on relevant data for the case.
7. To add data sources to a hold policy, see [Data sources in eDiscovery](edisc-data-sources) for step-by-step guidance.
8. On the **Manage data sources** flyout pane, add or remove data sources for your hold policy. You can choose one or more users, groups, or organization locations.

- You must select at least one data source to create a hold policy.
- Enter the specific users, groups, or organization locations you want to add to the hold policy.

    **Distribution groups**: When you create a hold and select a distribution group as a data source, all current members of the distribution group are listed. You can select all mailboxes or sites for each user to include in the hold. For more information about preserving Bcc and expanded distribution group recipients, see [Preserve Bcc and expanded distribution group recipients](edisc-hold-preserve-recipients).

    Important

    **Group membership is captured as a point-in-time snapshot when the hold policy is created.** This applies to every supported group type – distribution list, mail-enabled security group, Microsoft 365 group, Microsoft Teams group, and Viva Engage group. When you add any group as a data source, members are expanded and selected at the moment the policy is created. Members added to the group later are **not** automatically placed on hold; members removed from the group remain on hold until you update or release the policy. To reflect current membership, add the group again as a data source. Search behavior differs, search re-resolves group membership each time the search runs. For more information, see [Data sources in eDiscovery](edisc-data-sources).

    Distribution list expansion is limited to a maximum of 100 members. If a distribution list contains more than 100 members, the expansion might fail and the distribution list isn't added successfully. In this case, split the distribution list into smaller groups before adding them as data sources, or use [bulk import data sources](edisc-data-sources#bulk-import-data-sources-to-a-case).

    **Exchange mailboxes**: Applicable checkboxes are selected for the mailboxes placed on hold. Use **Edit** to find user mailboxes and distribution groups (the mailboxes of group members) to place on hold. You can also place a hold on the associated mailbox for a Microsoft Team, Microsoft 365 group, and Viva Engage Group. For more information about the application data that is preserved when a mailbox is placed on hold, see [Content stored in mailboxes for eDiscovery](edisc-search-mailboxes#content-stored-in-exchange-online-mailboxes-for-ediscovery).

    **SharePoint sites**: Applicable checkboxes are selected for SharePoint sites and OneDrive accounts placed on hold. Use **Edit** to enter the URL for additional sites that you want to place on hold. You can also add the URL for the SharePoint site for a Microsoft Team, Microsoft 365 group, or Viva Engage group. To avoid potential URL truncation, ensure SharePoint site names stay under 70 characters. Hold policies might not be able to locate sites for truncated site URLs and might have access errors. Placing a hold on a subsite isn't allowed even if the subsite is displayed in the location picker. If you select a subsite, the hold is placed on the parent SharePoint site instead.

    Important

    The Recycle Bin in SharePoint sites isn't indexed and therefore unavailable for searching. As a result, eDiscovery searches can't find any Recycle Bin content to place holds.

    eDiscovery doesn't continuously monitor location-level changes after a hold is applied. If mailbox or site identities change later (for example, SharePoint or OneDrive URL changes), or if the hold state changes outside the policy workflow, edit the hold policy data sources and reapply or retry the policy so hold status and scope stay accurate.

1. Select **Save**. You've now scoped the data sources for your hold policy.
2. To define the parameters of your hold policy, choose from the following options on the **Hold policy** tab:

    - **Condition builder**: The condition builder option in search provides a visual filtering experience when you build hold policies. Each condition adds a clause that is created and run when you create the hold. For example, you can specify a date range so that email or site documents that were created within the date range are preserved. For detailed information about using the condition builder option, see [Use the condition builder to create search queries in eDiscovery](edisc-condition-builder).
    - **Keyword Query Language (KeyQL)**: The Keyword Query Language (KeyQL) query option in search provides guidance and lets you quickly paste long, complex queries directly into the editor. For detailed information about building search queries with the KeyQL option, see [Use Keyword Query Language to create search queries in eDiscovery](edisc-keyword-query-language).

        You can also quickly build KeyQL queries for your search using Microsoft Security Copilot. For more information, see [Create a KeyQL search query with Microsoft Copilot (preview)](edisc-search-query#create-a-keyql-search-query-with-microsoft-copilot-preview).

    Important

    For the best results when dealing with encrypted or partially indexed items, limit conditions to *Date*, *Participants*, and *Type* in query-based holds. Queries aren't effective on other conditions within encrypted or partially indexed items and holds might not be applied to these items.
3. Select **Apply hold**.

Important

To apply a hold to a SharePoint site, the site must have a title.

After creating a hold, check that the hold is applied successfully by navigating to the **Details** tab for the hold policy. You can review the following information for the hold policy:

- **Name**: The name of the data source.
- **Location**: The specific location (such as the SMTP address of the mailbox or the URL of the site) of the data sources included in the hold policy.
- **Hold status**: The hold status of the location. Indicates whether the location is on hold, not on hold, or if there's an error with the hold.
- **Source type**: Shows whether the data source type is *People* or *Group*.
- **Location type**: Shows whether the location is *Mailbox* or *Site*.

Note

When you create a query-based hold, you initially place all content from the selected locations on hold. Later, the system clears any content that doesn't match the specified query from the hold every seven to 14 days. However, a query-based hold doesn't clear content if you apply more than five holds of any type to a content location. The hold always includes partially or unindexed items from a location with a query-based hold.

## Create a hold from a search

You can create an eDiscovery hold directly from search. However, creating a hold directly from a search has the following restrictions:

- The hold removes tenant-wide data sources contained in the search. Holds don't support tenant-wide data sources.
- The hold expands distribution lists contained in the search. You can choose to place all members' mailboxes and sites on hold or a subset or mix of these data sources on hold. Subsequent changes in distribution list membership don't change or update holds or the policy. If the distribution list is empty, it's removed from the hold because there's nothing to expand.
- The query used in the search isn't incorporated into the hold policy. The data sources in scope for the search are included in the hold policy.

To create an eDiscovery hold from a search, complete the following steps:

1. Complete the steps for [creating a search query](edisc-search-query#create-a-search-query).
2. Select **Create a hold** on the command bar for the search.
3. View the new hold policy and update as needed.

## Monitor hold processing in Process manager

The **Process manager** displays information about processes performed on the hold policy.

- **Process type**: The type of process.
- **Status**: The status of the process.
- **Created**: The date and time the process was created.
- **Completed**: The date and time the process was completed.
- **Duration**: The duration of the process.
- **Created by**: The user that created the process.

To download the list of processes and the column information, select **Download list** to create a .csv file containing this information.

To view information about all eDiscovery processes, see [Use the Process report in eDiscovery](edisc-process-report).

## Query-based holds placed on sites

Keep the following points in mind when you place a query-based eDiscovery hold on documents located in SharePoint sites:

- A query-based hold initially preserves all documents in a site for a short period of time after you delete them. When you delete a document, you move it to the Preservation Hold library even if it doesn't match the criteria of the query-based hold. However, a timer job removes deleted documents that don't match a query-based hold. The timer job runs periodically and compares all documents in the Preservation Hold library to your query-based eDiscovery holds (and other types of holds and retention policies). The timer job deletes the documents that don't match a query-based hold and preserves the documents that do.
- Use query-based holds to perform targeted preservation such as keywords, date ranges, or other document properties to preserve site documents.

## Preserve content in Microsoft Teams

Conversations that are part of a Microsoft Teams channel are stored in the mailbox that's associated with the Microsoft Team. Similarly, files that team members share in a channel are stored on the team's SharePoint site. Therefore, you have to place the Team mailbox and SharePoint site on eDiscovery hold to preserve conversations and files in a channel.

Alternatively, conversations that are part of the Chat list in Teams (called *1:1 chats* or *1:N group chats*) are stored in the mailboxes of the users who participate in the chat. Files that users share in chat conversations are stored in the OneDrive account of the user who shares the file. Therefore, you have to add the individual user mailboxes and OneDrive accounts to an eDiscovery hold to preserve conversations and files in the chat list. It's a good idea to place a hold on the mailboxes of members of a Microsoft Team in addition to placing the team mailbox and site on hold.

Note

If your organization has an Exchange hybrid deployment (or your organization synchronizes an on-premises Exchange organization with Microsoft 365) and has enabled Microsoft Teams, on-premises users can use the Teams chat application and participate in 1:1 chats and 1:N group chats. These conversations are stored in cloud-based storage that's associated with an on-premises user. If you place an on-premises user on an eDiscovery hold, the Teams chat content in the cloud-based storage is preserved. For more information, see [Find content in mailboxes](edisc-search-mailboxes).

### Preserve card content

Card content generated by apps in Teams channels, 1:1 chats, and 1:N group chats are stored in mailboxes and are preserved when you place a mailbox on an eDiscovery hold. A *card* is a UI container for short pieces of content. Cards can have multiple properties and attachments, and can include items that trigger card actions. For more information, see [Cards](/en-us/microsoftteams/platform/task-modules-and-cards/what-are-cards). Like other Teams content, where card content is stored is based on where the card was used. Content for cards used in a Teams channel is stored in the Teams group mailbox. Card content for 1:1 and 1xN chats are stored in the mailboxes of the chat participants.

### Preserve meeting and call information

Summary information for meetings and calls in a Teams channel is also stored in the mailboxes of users who dialed into the meeting or call. This content is also preserved when you place an eDiscovery hold on user mailboxes.

### Preserve content in private channels

You can also preserve content in private channels. Private channel chats are stored in a dedicated private channel mailbox. Private channel message data from each user’s mailbox is moved to the private channel’s mailbox and message edits and deleted messages aren't copied into the mailbox. For users on hold, copies of message edits and deleted messages remain in the user’s preserved library folder until the hold expires, while the latest version of private channel message data from each user’s mailbox is copied to the private channel’s mailbox.

### Preserve wiki content

Every team or team channel also contains a Wiki for note taking and collaboration. The Wiki content automatically saves to a file in the .mht format. The Teams Wiki Data document library on the team's SharePoint site stores this file. You can preserve the wiki content by adding the team's SharePoint site to an eDiscovery hold.

Note

The capability to preserve Wiki content for a Team or team channel (when you place the team's SharePoint site on hold) was released on June 22, 2017. If a team site is on hold, the Wiki content is retained starting on that date. However, if a team site is on hold and the Wiki content was deleted before June 22, 2017, the Wiki content isn't preserved.

### Microsoft 365 groups

Teams is built on Microsoft 365 groups. Therefore, placing Microsoft 365 groups on eDiscovery hold is similar to placing Teams content on hold.

Keep the following things in mind when placing both Teams and Microsoft 365 groups on an eDiscovery hold:

- To place content located in Teams and Microsoft 365 groups on hold, you must specify the mailbox and SharePoint site that are associated with a group or team.
- Run the **Get-UnifiedGroup** cmdlet in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) to view properties for Teams and Microsoft 365 groups. This method is a good way to get the URL for the site that's associated with a Team or Microsoft 365 group. For example, the following command displays selected properties for a Microsoft 365 group named Senior Leadership Team:

    ```text
    Get-UnifiedGroup "Senior Leadership Team" | FL DisplayName,Alias,PrimarySmtpAddress,SharePointSiteUrl
    
    DisplayName            : Senior Leadership Team
    Alias                  : seniorleadershipteam
    PrimarySmtpAddress     : seniorleadershipteam@contoso.onmicrosoft.com
    SharePointSiteUrl      : https://contoso.sharepoint.com/sites/seniorleadershipteam
    ```

    Note

    To run the **Get-UnifiedGroup** cmdlet, you need the View-Only Recipients role in Exchange Online or membership in a role group that's assigned the View-Only Recipients role.
- When you search a user's mailbox, the search doesn't include any Team or Microsoft 365 group that the user is a member of. Similarly, when you place a Team or Microsoft 365 group on eDiscovery hold, the hold applies only to the group mailbox and group site. The mailboxes and OneDrive sites of group members aren't placed on hold unless you explicitly add them to the eDiscovery hold. So if you have to place a Team or Microsoft 365 group on hold for a legal reason, consider adding the mailboxes and OneDrive accounts of team or group members on the same hold.
- To get a list of the members of a Team or Microsoft 365 group, you can view the properties on the [**Groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855) page in the Microsoft 365 admin center. Alternatively, you can run the following command in Exchange Online PowerShell:

    ```powershell
    Get-UnifiedGroupLinks <group or team name> -LinkType Members | FL DisplayName,PrimarySmtpAddress
    ```

    Note

    To run the **Get-UnifiedGroupLinks** cmdlet, you need the View-Only Recipients role in Exchange Online or membership in a role group that's assigned the View-Only Recipients role.

## Preserve content in OneDrive accounts

Important

The retention period for deleted OneDrive accounts is different from the retention period for mailboxes. For more information about the retention period for deleted OneDrive accounts, see [OneDrive retention and deletion](/en-us/sharepoint/retention-and-deletion?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json#the-onedrive-deletion-process).

To collect a list of the URLs for the OneDrive sites in your organization so you can add them to a hold or search associated with an eDiscovery case, see [Create a list of all OneDrive locations in your organization](/en-us/onedrive/list-onedrive-urls?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

The script in this article creates a text file that contains a list of all OneDrive sites in your organization. To run this script, you need to install and use the SharePoint Online Management Shell. Be sure to append the URL for your organization's MySite domain to each OneDrive site that you want to search. This domain contains all your OneDrive sites; for example, `https://contoso-my.sharepoint.com`. Here's an example of a URL for a user's OneDrive site: `https://contoso-my.sharepoint.com/personal/sarad_contoso_onmicrosoft.com`.

Important

The URL for a user's OneDrive account includes their user principal name (UPN) (for example, `https://alpinehouse-my.sharepoint.com/personal/sarad_alpinehouse_onmicrosoft_com`). In the rare case that a person's UPN is changed, their OneDrive URL also changes to incorporate the new UPN. If a user's OneDrive account is part of an eDiscovery hold, and their UPN is changed, you need to update the hold by adding the user's new OneDrive URL and removing the old one. If the URL for the OneDrive site changes, previously placed holds on the site remain effective and content is preserved. For more information, see [How UPN changes affect the OneDrive URL](/en-us/onedrive/upn-changes?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

## Remove content locations from an eDiscovery hold

After you remove a mailbox, SharePoint site, or OneDrive account from an eDiscovery hold, a *delay hold* is applied. This hold delays the actual removal of the hold for 30 days to prevent data from being permanently deleted (purged) from a content location. This delay gives admins an opportunity to search for or recover content that is purged after an eDiscovery hold is removed. The details of how the delay hold works for mailboxes and sites are different.

- **Mailboxes:** A delay hold is placed on a mailbox the next time the Managed Folder Assistant processes the mailbox and detects that an eDiscovery hold was removed. Specifically, a delay hold is applied to a mailbox when the Managed Folder Assistant sets one of the following mailbox properties to **True**:

    - **DelayHoldApplied:** This property applies to email-related content (generated by people using Outlook and Outlook on the web) that's stored in a user's mailbox.
    - **DelayReleaseHoldApplied:** This property applies to cloud-based content (generated by non-Outlook apps such as Microsoft Teams, Microsoft Forms, and Microsoft Viva Engage) that's stored in a user's mailbox. Cloud data generated by a Microsoft app is typically stored in a hidden folder in a user's mailbox.

    When a delay hold is placed on the mailbox (when either of the previous properties is set to **True**), the mailbox is still considered to be on hold for an unlimited hold duration, as if the mailbox was on [Litigation Hold](/en-us/microsoft-365/admin/misc/create-litigation-hold-mac?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json). After 30 days, the delay hold expires, and Microsoft 365 automatically attempts to remove the delay hold (by setting the DelayHoldApplied or DelayReleaseHoldApplied property to **False**) so that the hold is removed. After either of these properties are set to **False**, the corresponding items that are marked for removal are purged the next time the mailbox is processed by the Managed Folder Assistant.
- **SharePoint and OneDrive sites:** Any SharePoint or OneDrive content that's being retained in the Preservation Hold library isn't deleted during the 30-day delay hold period after a site is removed from an eDiscovery hold. Retention of content in the Preservation Hold library during the 30-day delay hold period is similar to what happens when a site is released from a retention policy. Additionally, you can't manually delete this content in the Preservation Hold library during the 30-day delay hold period. To release a site from the 30-day delay hold/grace period hold, see the [Can't delete a site because of an invalid retention policy or eDiscovery hold](/en-us/sharepoint/troubleshoot/sites/compliance-policy-blocking-site-deletion?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) troubleshooting article.

    For more information, see [Releasing a policy for retention](retention#releasing-a-policy-for-retention).

A delay hold is also applied to content locations on hold when you close an eDiscovery case because holds are turned off when a case is closed. For more information about closing a case, see [Learn about case settings in eDiscovery](edisc-settings-cases).