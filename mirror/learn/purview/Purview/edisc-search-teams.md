---
layout: Conceptual
title: Finding content in Microsoft Teams in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-teams
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about finding content in Microsoft Teams in eDiscovery in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-02T00:00:00.0000000Z
audience: Admin
ms.topic: article
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
locale: en-us
document_id: 185c38a7-9549-ef38-c5ad-49d291488100
document_version_independent_id: 185c38a7-9549-ef38-c5ad-49d291488100
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-teams.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-teams
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-teams.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 350481f0-afaa-923b-138d-9d347fa4904a
---

# Finding content in Microsoft Teams in eDiscovery | Microsoft Learn

This article provides a comprehensive set of procedures, guidelines, and best practices for using eDiscovery to preserve, collect, [review](edisc-review-set-teams-data), and export content from [Microsoft Teams](/en-us/microsoftteams/teams-overview). The goal of this article is to help you optimize your eDiscovery search for Teams content.

For more information about finding content in Microsoft Teams with eDiscovery, check out the following video: 

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Where Teams content is stored

To manage Teams content in eDiscovery, you need to understand the type of Teams content you can collect, process, and review in eDiscovery and where Microsoft 365 stores that content. To configure Teams content locations in a case, see [Configure data sources](edisc-data-sources). Teams data is stored in Azure Cosmos DB. Exchange Online stores Teams compliance records that the substrate captures, and eDiscovery can access these records. The data stored in Exchange Online is hidden from clients. eDiscovery never operates against the real Teams message data, which remains in Azure Cosmos DB.

The following table lists Teams content types and where Microsoft 365 stores each type for compliance purposes.

| Teams category | Description | Chat messages/posts location | Files/attachments location | Meeting recordings location |
| --- | --- | --- | --- | --- |
| Events | All data from webinars and town halls is stored in Cosmos DB. Substrate (SCD) serves as secondary storage for redundancy and eDiscovery purposes. | N/A | N/A | N/A |
| Private channels | Message posts, replies, and attachments shared in a private Teams channel. | Messages sent in a private channel are stored in the Exchange Online mailboxes of all members of the private channel. | Files shared in a private channel are stored in a dedicated SharePoint site associated with the private channel. | N/A |
| Shared channels | Message posts, replies, and attachments shared in a shared Teams channel. | Messages sent in a shared channel are stored in a system mailbox associated with the shared channel.^2^ | Files shared in a shared channel are stored in a dedicated SharePoint site associated with the shared channel. | N/A |
| Teams 1:1 chats | Chat messages, posts, and attachments shared in a Teams conversation between two people. Teams 1:1 chats are also called *conversations*. | Messages in 1:1 chats are stored in the Exchange Online mailbox of all chat participants. | Files shared in a 1:1 chat are stored in the OneDrive account of the person who shared the file. | N/A |
| Teams channels | Chat messages, posts, replies, and attachments shared in a standard Teams channel. | All channel messages and posts are stored in the Exchange Online mailbox associated with the team. | Files shared in a channel are stored in the SharePoint site associated with the team. | N/A |
| Teams group chats | Chat messages, posts, and attachments shared in a Teams conversation between three or more people. Also called *1:N* chats or *group conversations*. | Messages in group chats are stored in the Exchange Online mailbox of all chat participants. | Files shared in group chats are stored in the OneDrive account of the person who shared the file. | N/A |
| Teams meetings | Audio and transcripts from recorded Teams meetings. | Chats in recorded meetings are stored in an Exchange Online mailbox. For standard meetings, it's stored in the mailboxes of all participants. For channel meetings, it's stored in the mailbox associated with the team. | Files and attachments shared in recorded meetings are stored in the OneDrive account for the user recording the Teams meeting. | Meeting recordings are stored in the OneDrive account for the user recording the Teams meeting.^1^ |
| Teams reactions | Reactions applied to chat messages, posts, and attachments in a Teams conversation. | Messages in group chats are stored in the Exchange Online mailbox of all chat participants. | Files shared in group chats are stored in the OneDrive account of the person who shared the file. | N/A |

Note

^1^ To locate Teams meeting audio and transcript content, create an eDiscovery search targeting the organizer's OneDrive. Include the date range and file extension in the query. When the search completes, refine the results in a review set and select only the pertinent data. For example, a date range might be from *March 17, 2025 to March 18, 2025* and the file extension might be *mp4*.

^2^ To search for (and preserve) messages sent in a shared channel, you must search or specify the Exchange Online mailbox for the parent Team.

## Teams content types

All Microsoft Teams 1:1 or group chats are journaled through to the respective users' mailboxes. All standard channel messages are journaled through to the group mailbox representing the team. Files uploaded in standard channels are covered under the eDiscovery functionality for SharePoint and OneDrive.

eDiscovery of messages and files in [private channels](/en-us/microsoftteams/private-channels) works differently than in standard channels. For more information, see eDiscovery of private channels.

Recorded Teams meetings are stored in the OneDrive account of the meeting organizer or initiator, depending on the [*MeetingRecordingOwnership* configuration](/en-us/microsoftteams/tmr-meeting-recording-change#recording-storage). Attendee identification information when using the **Hide Attendee Names** functionality for Teams meetings is stored in the user mailbox of the [meeting organizer](https://support.microsoft.com/office/roles-in-microsoft-teams-meetings-c16fa7d0-1666-4dde-8686-0a0bfe16e019).

Not all Teams content is eDiscoverable. The following table shows the Teams content types that you can search for using Microsoft eDiscovery tools:

| Content type | Notes |
| --- | --- |
| Audio recordings | Audio calls between Teams user and external contacts |
| Card content | See Search for card content for more information. |
| Chat links |  |
| Chat messages | This includes content in standard Teams channels, 1:1 chats, 1:N group chats, chats with yourself, and chats with guests. |
| Code snippets |  |
| Edited messages | If the user is on hold, previous versions of edited messages are also preserved. |
| Emojis, GIFs, and stickers |  |
| Inline images |  |
| Loop components | Content in a loop component is saved in a .fluid file that's stored in the OneDrive account of the user who sends the loop component. That means you have to include OneDrive as a data source when searching for content in loop components. |
| Meeting IM conversations |  |
| Meeting metadata^1^ |  |
| Meeting recordings and transcripts | Transcripts of the meeting audio are extracted and provided as a separate file. Maximum supported recorded meeting .mp4 file size is 350 MB. If the recorded meeting file size is greater than 350 MB, a processing error occurs and the file is available for download. |
| Name of channel |  |
| Quotes | Quoted content is searchable. However, search results don't indicate that the content was quoted. |
| Reactions (such as likes, hearts, and other reactions) | Reactions are supported for all commercial customers after June 1, 2022. Reactions before this date aren't available for eDiscovery. Expanded reactions are now supported. To understand reaction history, the content must be on legal hold. |
| Subject |  |
| Tables |  |
| Teams Video Clip (TVC) | Search TVC with "Video-Clip" keyword and "save as" a .mp4 file for each TVC attachment by right-clicking the preview. <br> TVCs are collected as Teams conversation attachments (if smaller than 200 MB) and separate .mp4 files. TVC file data is discoverable in eDiscovery [review sets](edisc-search-add-to-review-set) and can be exported. Preview of video clips isn't currently supported. |

^1^ Meeting (and call) metadata includes the following:

- Meeting start and end time, and duration
- Meeting join and leave events for each participant
- VOIP joins/calls
- Federated user joins
- Guest joins

Important

Anonymous users joining meetings and calls aren't currently supported in eDiscovery search queries.

Microsoft Teams data appears as IM or Conversations in the Excel eDiscovery export output. You can open the `.pst` file in Outlook to view those messages after you export them.

When viewing the .pst file for the team, all conversations are located in the Team Chat folder under Conversation History. The title of the message contains the team name and channel name.

Private chats in a user's mailbox are stored in the Team Chat folder under Conversation History.

## eDiscovery of private and shared channels

Compliance copies of messages in private and shared channels go to different mailboxes depending on the channel type. That difference means you need to search different mailbox locations based on the type of channel a user belongs to.

- **Private channels**: Compliance copies go to the dedicated private channel mailbox. You need to search private channel mailboxes when searching for content in private channel messages.
- **Shared channels**: Compliance copies go to a system mailbox that's associated with the parent team. Because Teams doesn't support an eDiscovery search of a single system mailbox for a shared channel, you need to search the mailbox for the parent team (by selecting the name of the Team mailbox) when searching for message content in shared channels.

Each private and shared channel has its own SharePoint site that's separate from the parent team site. Files in private and shared channels are stored in their own site and managed independently of the parent team. You must identify and search the specific site associated with a channel when searching for content in files and channel message attachments.

Use the following sections to help identify the private or shared channel to include in your eDiscovery search.

### Identify the members of a private channel

Use the following procedure to identify members of a private channel so that you can use eDiscovery tools to search the member's mailbox for content in private channel messages.

Before you perform these steps, make sure you have the [latest version of the Teams PowerShell module](/en-us/microsoftteams/teams-powershell-overview) installed.

1. Run the following command to get the group ID of the team that contains the shared channels you want to search.

    ```powershell
    Get-Team -DisplayName <display name of the parent team>
    ```

    Tip

    Run the **Get-Team** cmdlet without any parameters to display a list of all Teams in your organization. The list contains the group ID and DisplayName for every team.
2. Run the following command to get a list of private channels in the parent team. Use the group ID for the team that you obtained in step 1.

    ```PowerShell
     Get-TeamChannel -GroupId <parent team GroupId> -MembershipType Private
    ```
3. Run the following command to get a list of private channel owners and members for a specific private channel.

    ```PowerShell
     Get-TeamChannelUser -GroupId <parent team GroupId> -DisplayName "Partner Shared Channel"
    ```
4. Include the mailboxes of owners and members of a private channel as part of your eDiscovery search query.

## Search for content for guests

You can use eDiscovery tools to search for Teams content related to guests in your organization. Teams chat content that's associated with a guest is preserved in a cloud-based storage location, and you can search for it by using eDiscovery. This content includes 1:1 and 1:N chat conversations where a guest participates with other users in your organization. You can also search for private channel messages where a guest participates and for content in *guest:guest* chat conversations where the only participants are guests.

To search for content for guests:

1. Connect to Microsoft Graph PowerShell. For more information, see the [Microsoft Graph PowerShell overview](/en-us/powershell/microsoftgraph/overview). Be sure to complete Step 1 and Step 2 in the previous article.
2. After you successfully connect to Microsoft Graph PowerShell, run the following command to display the user principal name (UPN) for all guests in your organization. You need to use the UPN of the guest when you create the search in step 4.

    ```powershell
    Get-MgUser -Filter "userType eq 'Guest'" -All $true | FL UserPrincipalName
    ```

    Tip

    Instead of displaying a list of user principal names on the computer screen, you can redirect the output of the command to a text file. You can do this by appending `> filename.txt` to the previous command. The text file with the user principal names is saved to the current folder.
3. In a different Windows PowerShell window, connect to Security & Compliance PowerShell. For instructions, see [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell). You can connect with or without using multifactor authentication.
4. Create a search query that searches for all content (such as chat messages and email messages) where the specified guest was a participant by running the following command.

    ```powershell
    New-ComplianceSearch <search name> -ExchangeLocation <guest UPN>  -AllowNotFoundExchangeLocationsEnabled $true -IncludeUserAppContent $true
    ```

    For example, to search for content associated with the guest Sara Davis, run the following command.

    ```powershell
    New-ComplianceSearch "Sara Davis Guest" -ExchangeLocation "sara.davis_hotmail.com#EXT#@contoso.onmicrosoft.com" -AllowNotFoundExchangeLocationsEnabled $true -IncludeUserAppContent $true
    ```

    For more information about using PowerShell to create searches, see [New-ComplianceSearch](/en-us/powershell/module/exchange/new-compliancesearch).
5. Run the following command to start the search that you created in step 4:

    ```powershell
    Start-ComplianceSearch <search name>
    ```
6. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in by using the credentials for a user account assigned eDiscovery permissions.
7. Select the **eDiscovery** solution card and then select **Cases** in the left navigation.
8. Select a case.
9. In the list of searches on the **Searches** tab, select the search that you created in step 4 to display the flyout page.
10. On the flyout page, you can do the following things:

    - Select **Sample** to view the search results and preview the content.
    - Next to the **Query** field, select **Edit** to edit and then rerun the search. For example, you can add a search query to narrow the results.
    - Select **Export** to export and download the search results.

## Search for card content

Apps generate card content in Teams channels, 1:1 chats, and 1xN chats. The content is stored in mailboxes and you can search it. A *card* is a UI container for short pieces of content. Cards can have multiple properties and attachments, and can include items that trigger card actions. For more information, see [Cards](/en-us/microsoftteams/platform/task-modules-and-cards/what-are-cards).

Like other Teams content, where you store card content depends on where you used the card. The Teams group mailbox stores content for cards used in a Teams channel. The mailboxes of the chat participants store card content for 1:1 and 1xN chats.

To search for card content, use the `kind:microsoftteams` or `itemclass:IPM.SkypeTeams.Message` search conditions. When you review search results, you see that bots generate card content in a Teams channel and the **Sender/Author** email property is `<appname>@teams.microsoft.com`, where `appname` is the name of the app that generated the card content. If a user generates card content, the **Sender/Author** value identifies the user.

When you view card content in search results, the content appears as an attachment to the message. The attachment is named `appname.html`, where `appname` is the name of the app that generated the card content.

Note

To display images from card content in search results (such as the checkmarks in the previous screenshot), you need to be signed into Teams (at https://teams.microsoft.com) in a different tab in the same browser session that you use to view the search results. Otherwise, image placeholders are displayed.

## Search for Teams meetings by date

Admins can search for Teams meeting content based on the meeting start or end dates. To filter review set items by specific Teams meeting dates, use the *Meeting start date* and *Meeting end date* properties in eDiscovery search tools.

## Search for hidden attendees in Teams meetings

The **Hide Attendee Names** feature in Microsoft Teams hides the name of attendees from other attendees so only organizers can see attendees names. Use this feature for meetings or events with external businesses, vendors, confidential meetings, or other meetings where personal privacy between attendees is important. When you enable this feature, the names of attendees are hidden in the meeting roster, meeting chat, and meeting recordings.

To search for the names of attendees in Teams meetings where the **Hide Attendee Names** feature was enabled, you must include the organizer's mailbox in the scope for the search. Hidden attendee names are only available in the organizer's mailbox.

## Search for Teams Events data

All data from webinars and town halls is stored in Cosmos DB. Substrate (SCD) serves as secondary storage for redundancy and eDiscovery purposes. For webinars created before September 2024, this data remains in the webinar organizer's SharePoint storage to ensure continuity for V1 webinars.

eDiscovery applies all event-related information, including *Event titles, Descriptions, Attendee registration data, Presenters,* and *Themes*. Event registration details, such as attendee lists and registrant email addresses, are captured in eDiscovery logs. Live attendance data isn't included.

For legal cases, use the **Microsoft Purview portal** to include *"Microsoft Teams Virtual Events"* as an external data source in the processes. After creating a case and selecting data sources, [create a search query](edisc-search-query) to collect relevant Teams Event data for legal and compliance needs.

For future updates, see the **Message Center** for feature availability and functionality.

## eDiscovery in external access and guest environments

Admins can use eDiscovery to search for content in chat messages in a Teams meeting in external access and guest access environments based on the following restrictions:

- **External access**: In a Teams meeting with users from your organization and users from an external organization where external attendees are using external access, admins in both organizations can search for content in chat messages from the meeting.
- **Guest**: In a Teams meeting with users from your organization and guests, only admins in the organization who hosts the Teams meeting can search for content in chat messages from the meeting.

## Search for Skype for Business conversations

You can use the following keyword query to specifically search for content in Skype for Business conversations:

```powershell
kind:im
```

The previous search query also returns chats from Microsoft Teams. To prevent this issue, you can narrow the search results to include only Skype for Business conversations by using the following keyword query:

```powershell
kind:im AND subject:conversation
```

The previous keyword query excludes chats in Microsoft Teams because Skype for Business conversations are saved as email messages with a Subject line that starts with the word "Conversation".

To search for Skype for Business conversations that occurred within a specific date range, use the following keyword query:

```powershell
kind:im AND subject:conversation AND (received=startdate..enddate)
```