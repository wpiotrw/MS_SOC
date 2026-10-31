---
layout: Conceptual
title: Use Content Search in Microsoft Teams | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-teams-content-search
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about using Content search in the Microsoft Purview portal to search for Microsoft Teams content that's stored in Exchange Online, SharePoint Online, OneDrive for Business, and OneNote.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.topic: how-to
audience: admin
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- M365-collaboration
- content-search
ms.reviewer: anwara
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
search.appverid: MET150
f1.keywords:
- NOCSH
ms.custom: seo-marvel-mar2020
locale: en-us
document_id: 583daa3e-7889-6c44-e22f-6629555d1615
document_version_independent_id: 583daa3e-7889-6c44-e22f-6629555d1615
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-teams-content-search.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-teams-content-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-teams-content-search.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 037733c0-e638-4bdc-34fc-1ffa05fd0fcc
---

# Use Content Search in Microsoft Teams | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Note

Content search of messages and files in [private channels](/en-us/microsoftteams/private-channels) work differently than in standard channels. To learn more, see Content search of private channels.

[Content search](ediscovery-content-search) provides a way to query Microsoft Teams information spanning Exchange, SharePoint Online, and OneDrive for Business. For example, using **Content search** against your *Manufacturing Specs* mailbox and *Manufacturing Specs* SharePoint site, you can search against Teams standard channel conversations from Exchange, file uploads and modifications from SharePoint Online, and OneNote changes.

You can also add query criteria to the **Content Search** to narrow the results returned. In the previous example, you can look for content where the keywords "**New Factory Specs"** were used.

Tip

After adding search conditions, you can export a report or the actual content to your computer for analysis.

## Content search of private channels

Records for messages sent in a private channel are delivered to the mailbox of all private channel members, rather than to a group mailbox. The titles of the records are formatted to indicate which private channel they were sent from.

Because each private channel has its own SharePoint site collection that's separate from the parent team site, files in a private channel are managed independently of the parent team.

Teams doesn't support content search of a single channel, so the whole team must be searched. To perform a content search of a private channel, search across the team, the site collection associated with the private channel (to include files), and mailboxes of private channel members (to include messages).

Use the following steps to identify files and messages in a private channel to include in your content search.

### Include private channel files in a content search

Before you perform these steps, install the [SharePoint Online Management Shell and connect to SharePoint Online](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?view=sharepoint-ps).

1. Run the following to get a list of all SharePoint site collections associated with private channels in the team.

    ```PowerShell
    Get-SPOSite
    ```
2. Run the following PowerShell script to get a list of all SharePoint site collection URLs associated with private channels in the team and the parent team group ID.

    ```PowerShell
    $sites = get-sposite -template "teamchannel#0"
    foreach ($site in $sites) {$x= get-sposite -identity $site.url -detail; $x.relatedgroupID; $x.url}
    ```
3. For each team or group ID, run the following PowerShell script to identify all relevant private channel sites.

    ```PowerShell
    $sites = get-sposite -template "teamchannel#0"
    $groupID = "e8195240-4a70-4830-9106-80193cf717cb"
    foreach ($site in $sites) {$x= Get-SpoSite -Identity $site.url -Detail; if ($x.RelatedGroupId -eq $groupID) {$x.RelatedGroupId;$x.url}}
    ```

### Include private channel messages in a content search

Before you perform these steps, make sure you have the [latest version of the Teams PowerShell module](/en-us/microsoftteams/teams-powershell-overview) installed.

1. Run the following to get a list of private channels in the team.

    ```PowerShell
    Get-TeamChannel -GroupId <GroupID> -MembershipType Private
    ```
2. Run the following to get a list of private channel members.

    ```PowerShell
    Get-TeamChannelUser -GroupId <GroupID> -DisplayName "Engineering" -Role Member
    ```
3. Include the mailboxes of all members from each private channel in the team as part of your content search query.