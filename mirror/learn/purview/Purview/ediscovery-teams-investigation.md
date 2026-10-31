---
layout: Conceptual
title: Conduct an eDiscovery investigation of content in Microsoft Teams | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-teams-investigation
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about conducting an eDiscovery investigation of content in Microsoft Teams.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
audience: admin
ms.collection:
- purview-compliance
- M365-collaboration
- ediscovery
ms.reviewer: anwara
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
search.appverid: MET150
f1.keywords:
- NOCSH
ms.custom:
- seo-marvel-mar2020
- sfi-image-nochange
locale: en-us
document_id: 307d9526-7024-2e98-c637-ee4c3d36c33b
document_version_independent_id: 307d9526-7024-2e98-c637-ee4c3d36c33b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-teams-investigation.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-teams-investigation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-teams-investigation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 8bf28089-3bdb-e3db-d64b-1ff9481f04a3
---

# Conduct an eDiscovery investigation of content in Microsoft Teams | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Large enterprises are often exposed to high penalty legal proceedings that demand submission of all Electronically Stored Information (ESI). Microsoft Teams content can be searched and used during eDiscovery investigations.

## Overview

All Microsoft Teams 1:1 or group chats are journaled through to the respective users' mailboxes. All standard channel messages are journaled through to the group mailbox representing the team. Files uploaded in standard channels are covered under the eDiscovery functionality for SharePoint Online and OneDrive for Business.

eDiscovery of messages and files in [private channels](/en-us/microsoftteams/private-channels) works differently than in standard channels. To learn more, see eDiscovery of private channels.

Recorded Teams meetings are stored in the OneDrive for Business account of the meeting organizer or initiator, depending on the [*MeetingRecordingOwnership* configuration](/en-us/microsoftteams/tmr-meeting-recording-change#recording-storage). Attendee identification information when using the **Hide Attendee Names** functionality for Teams meetings is stored in the user mailbox of the [meeting organizer](https://support.microsoft.com/office/roles-in-microsoft-teams-meetings-c16fa7d0-1666-4dde-8686-0a0bfe16e019). To learn more, see [eDiscovery (Premium) workflow for content in Microsoft Teams](ediscovery-teams-workflow).

Not all Teams content is eDiscoverable. The following table shows the Teams content types that you can search for using Microsoft eDiscovery tools:

| **Content type** | **Notes** |
| --- | --- |
| Audio recordings | Audio calls between Teams user and external contacts |
| Card content | See Search for card content for more information. |
| Chat links |  |
| Chat messages | This includes content in standard Teams channels, 1:1 chats, 1:N group chats, chats with yourself, and chats with guests. |
| Code snippets |  |
| Edited messages | If the user is on hold, previous versions of edited messages are also preserved. |
| Emojis, GIFs, and stickers |  |
| Inline images |  |
| Loop components | Content in a loop component is saved in a .fluid file that's stored in the OneDrive for Business account of the user who sends the loop component. That means you have to include OneDrive as a data source when searching for content in loop components. |
| Meeting IM conversations |  |
| Meeting metadata^1^ |  |
| Meeting recordings and transcripts | Transcripts of the meeting audio are extracted and provided as a separate file. Maximum supported recorded meeting .mp4 file size is 350 MB. If the recorded meeting file size is greater than 350 MB, a processing error occurs and the file is available for download. |
| Name of channel |  |
| Quotes | Quoted content is searchable. However, search results don't indicate that the content was quoted. |
| Reactions (such as likes, hearts, and other reactions) | Reactions are supported for all commercial customers after June 1, 2022. Reactions before this date aren't available for eDiscovery. Expanded reactions are now supported. To understand reaction history, the content must be on legal hold. |
| Subject |  |
| Tables |  |
| Teams Video Clip (TVC) | Search TVC with "Video-Clip" keyword and "save as" a .mp4 file for each TVC attachment by right-clicking the preview. <br> TVCs are collected as Teams conversation attachments (if smaller than 200 MB) and separate .mp4 files. TVC file data is discoverable in eDiscovery [review sets](ediscovery-add-data-to-review-set) and can be exported. Preview of video clips isn't currently supported. |

^1^ Meeting (and call) metadata includes the following:

- Meeting start and end time, and duration
- Meeting join and leave events for each participant
- VOIP joins/calls
- Federated user joins
- Guest joins

Important

Anonymous users joining meetings and calls aren't currently supported in eDiscovery search queries.

Here's an example of a chat conversation between participants during a meeting.

![Conversation between participants in Teams.](media/meetingimconversations.png)

Here's an example of the compliance copy of the same chat conversation viewed in an eDiscovery tool.

![Conversation between participants in eDiscovery search results.](media/meetingimconversation2.png)

Here's an example of the meeting metadata.

![The meeting metadata from the compliance copy.](media/conversationoption3.png)

For more information about conducting an eDiscovery investigation, see [Get started with eDiscovery (Standard)](ediscovery-standard-get-started).

Microsoft Teams data appears as IM or Conversations in the Excel eDiscovery export output. You can open the `.pst` file in Outlook to view those messages after you export them.

When viewing the .pst file for the team, all conversations are located in the Team Chat folder under Conversation History. The title of the message contains the team name and channel name. For example, the image below shows a message from Bob who messaged the Project 7 standard channel of the Manufacturing Specs team.

![Screenshot of a Team Chat folder in a user's mailbox in Outlook.](media/conduct_an_ediscovery_investigation_of_content_in_microsoft_teams_image1.png)

Private chats in a user's mailbox are stored in the Team Chat folder under Conversation History.

## eDiscovery of private and shared channels

Compliance copies of messages in private and shared channels are sent to different mailboxes depending on the channel type. That means you have to search different mailbox locations based on the type of channel a user is a member of.

- **Private channels**. Compliance copies are sent to the mailbox of all members of the private channel members. That means you have to search the user mailbox when searching for content in private channel messages.
- **Shared channels**. Compliance copies are sent to a system mailbox that's associated with the parent team. Because Teams doesn't support an eDiscovery search of a single system mailbox for a shared channel, you have to search the mailbox for the parent team (by selecting the name of the Team mailbox) when searching for message content in shared channels.

Each private and shared channel has its own SharePoint site that's separate from the parent team site. That means files in private and shared channels are stored in its own site and managed independently of the parent team. This means you must identify and search the specific site associated with a channel when searching for content in files and channel message attachments.

Use the following sections to help identify the private or shared channel to include in your eDiscovery search.

### Identifying the members of a private channel

Use the procedure in this section to identify members of a private channel so that you can use eDiscovery tools to search the member's mailbox for content in private channel messages.

Before you perform these steps, make sure you have the [latest version of the Teams PowerShell module](/en-us/microsoftteams/teams-powershell-overview) installed.

1. Run the following command to get the group ID of the team that contains the shared channels you want to search.

    ```powershell
    Get-Team -DisplayName <display name of the the parent team>
    ```

    Tip

    Run the **Get-Team** cmdlet without any parameters to display a list of all Teams in your organization. The list contains the group Id and DisplayName for every team.
2. Run the following command to get a list of private channels in the parent team. Use the group ID for the team that you obtained in step 1.

    ```PowerShell
     Get-TeamChannel -GroupId <parent team GroupId> -MembershipType Private
    ```
3. Run the following command to get a list of private channel owners and members for a specific private channel.

    ```PowerShell
     Get-TeamChannelUser -GroupId <parent team GroupId> -DisplayName "Partner Shared Channel"
    ```
4. Include the mailboxes of owners and members of a private channel as part of your [eDiscovery search query in eDiscovery (Standard)](ediscovery-search-for-content) or when [identifying and collecting custodian content in eDiscovery (Premium)](ediscovery-add-custodians-to-case).

### Identifying the SharePoint site for private and shared channels

As previously explained, files shared in private and shared channels (and files attached to channel messages) are stored in the site collection associated with the channel. Use the procedure in this section to identify the URL for the site associated with a specific private or shared channel. Then you can use eDiscovery tools to search for content in the site.

Before you perform these steps, [install the SharePoint Online Management Shell and connect to SharePoint Online](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

1. Optionally, run the following to get a list of all SharePoint site collections associated with shared channels in the parent team.

    ```PowerShell
     Get-SPOSite
    ```

    Tip

    The naming convention of the URL for a site that's associated with private and shared channels is `[SharePoint domain]/sites/[Name of parent team]-[Name of private or shared channel]`. For example, the URL for the shared channel named "Partner Collaboration", which is located in the "Engineer Team" parent team in the Contoso organization is `https://contoso.sharepoint.com/sites/EngineeringTeam-PartnerCollaboration`.
2. Run the following PowerShell commands to display the URL for all SharePoint sites associated with the private and shared channels in your organization. The output of the script also includes the group ID of the parent team, which you need to run the commands in step 3.

    ```PowerShell
    $sites = Get-SPOSite -Template "TEAMCHANNEL#1"
    foreach ($site in $sites) {$x= Get-SPOSite -Identity $site.url -Detail; $x.relatedgroupID; $x.url}
    ```

    Note

    SharePoint sites for private channels created before June 28, 2021 use the value `"TEAMCHANNEL#0"` for the custom template ID. To displays private channels created after this date, use the value `"TEAMCHANNEL#1"` when running the previous two scripts. Shared channels only use the value of `"TEAMCHANNEL#1"`.
3. For each parent team, run the following PowerShell commands to identify the private and shared channel sites, where `$groupID` is the group ID of the parent team.

    ```PowerShell
    $sites = Get-SPOSite -Template "TEAMCHANNEL#1"
    $groupID = "<group ID of parent team)"
    foreach ($site in $sites) {$x= Get-SpoSite -Identity $site.url -Detail; if ($x.RelatedGroupId -eq $groupID) {$x.RelatedGroupId;$x.url}}
    ```
4. Include the site associated with a private or shared channel as part of your [eDiscovery search query in eDiscovery (Standard)](ediscovery-search-for-content) or when [identifying and collecting custodian content in eDiscovery (Premium)](ediscovery-add-custodians-to-case).

## Search for content for guests

You can use eDiscovery tools to search for Teams content related to guests in your organization. Teams chat content that's associated with a guest is preserved in a cloud-based storage location and can be searched for using eDiscovery. This includes searching for content in 1:1 and 1:N chat conversations in which a guest is a participant with other users in your organization. You can also search for private channel messages in which a guest is a participant and search for content in *guest:guest* chat conversations where the only participants are guests.

To search for content for guests:

1. Connect to Microsoft Graph PowerShell. For more information, see the [Microsoft Graph PowerShell overview](/en-us/powershell/microsoftgraph/overview). Be sure to complete Step 1 and Step 2 in the previous article.
2. After you successfully connect to Microsoft Graph PowerShell, run the following command to display the user principal name (UPN) for all guests in your organization. You have to use the UPN of the guest when you create the search in step 4.

    ```powershell
    Get-MgUser -Filter "userType eq 'Guest'" -All $true | FL UserPrincipalName
    ```

    Tip

    Instead of displaying a list of user principal names on the computer screen, you can redirect the output of the command to a text file. You can do this by appending `> filename.txt` to the previous command. The text file with the user principal names will be saved to the current folder.
3. In a different Windows PowerShell window, connect to Security & Compliance PowerShell. For instructions, see [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell). You can connect with or without using multi-factor authentication.
4. Create a content search that searches for all content (such as chat messages and email messages) in which the specified guest was a participant by running the following command.

    ```powershell
    New-ComplianceSearch <search name> -ExchangeLocation <guest UPN>  -AllowNotFoundExchangeLocationsEnabled $true -IncludeUserAppContent $true
    ```

    For example, to search for content associated with the guest Sara Davis, you would run the following command.

    ```powershell
    New-ComplianceSearch "Sara Davis Guest" -ExchangeLocation "sara.davis_hotmail.com#EXT#@contoso.onmicrosoft.com" -AllowNotFoundExchangeLocationsEnabled $true -IncludeUserAppContent $true
    ```

    For more information about using PowerShell to create content searches, see [New-ComplianceSearch](/en-us/powershell/module/exchange/new-compliancesearch).
5. Run the following command to start the content search that you created in step 4:

    ```powershell
    Start-ComplianceSearch <search name>
    ```
6. Go to https://compliance.microsoft.com and then select **Show all** &gt; **Content search**.
7. In the list of searches, select the search that you created in step 4 to display the flyout page.
8. On the flyout page, you can do the following things:

    - Select **View results** to view the search results and preview the content.
    - Next to the **Query** field, select **Edit** to edit and then rerun the search. For example, you can add a search query to narrow the results.
    - Select **Export results** to export and download the search results.

## Search for card content

Card content generated by apps in Teams channels, 1:1 chats, and 1xN chats are stored in mailboxes and can be searched. A *card* is a UI container for short pieces of content. Cards can have multiple properties and attachments, and can include items that can trigger card actions. For more information, see [Cards](/en-us/microsoftteams/platform/task-modules-and-cards/what-are-cards)

Like other Teams content, where card content is stored is based on where the card was used. Content for cards used in a Teams channel is stored in the Teams group mailbox. Card content for 1:1 and 1xN chats are stored in the mailboxes of the chat participants.

To search for card content, you can use the `kind:microsoftteams` or `itemclass:IPM.SkypeTeams.Message` search conditions. When reviewing search results, card content generated by bots in a Teams channel has the **Sender/Author** email property as `<appname>@teams.microsoft.com`, where `appname` is the name of the app that generated the card content. If card content was generated by a user, the value of **Sender/Author** identifies the user.

When viewing card content in Content search results, the content appears as an attachment to the message. The attachment is named `appname.html`, where `appname` is the name of the app that generated the card content. The following screenshots show how card content (for an app named Asana) appears in Teams and in the results of a search.

### Card content in Teams

![Card content in Teams channel message.](media/cardcontentteams.png)

### Card content in search results

![Same card content in the results of a Content search.](media/cardcontentediscoverysearchresults.png)

Note

To display images from card content in search results at this time (such as the checkmarks in the previous screenshot), you have to be signed into Teams (at https://teams.microsoft.com) in a different tab in the same browser session that you use to view the search results. Otherwise, image placeholders are displayed.

## Search for Teams meetings by date

Admins can search for Teams meeting content based on the meeting start or end dates. To filter review set items by specific Teams meeting dates, you can use the *Meeting start date* and *Meeting end date* properties in the advanced filtering options in eDiscovery (Premium).

![Example of advanced filtering by Teams meeting dates.](media/ediscovery-filter-meeting-dates.png)

## Search for hidden attendees in Teams meetings

The **Hide Attendee Names** feature in Microsoft Teams hides the name of attendees from other attendees so only organizers can see attendees names. This feature may be used for meetings or events with external businesses, vendors, confidential meetings, or other meetings where personal privacy between attendees is important. When this feature is enabled, the names of attendees are hidden in the meeting roster, meeting chat, and meeting recordings.

To search for the names of attendees in Teams meetings where the **Hide Attendee Names** feature was enabled, you must include the organizer's mailbox in the scope for the search. Hidden attendee names are only available in the organizer's mailbox.

## eDiscovery in external access and guest environments

Admins can use eDiscovery to search for content in chats messages in a Teams meeting in external access and guest access environments based on the following restrictions:

- **External access**: In a Teams meeting with users from your organization and users from an external organization where external attendees are using external access, admins in both organizations can search for content in chat messages from the meeting.
- **Guest**: In a Teams meeting with users from your organization and guests, only admins in the organization who hosts the Teams meeting can search for content in chat messages from the meeting.