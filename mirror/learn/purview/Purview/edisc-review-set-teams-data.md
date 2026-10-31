---
layout: Conceptual
title: Review Microsoft Teams content in a review set in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-teams-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Choose how you group and view Microsoft Teams content in an eDiscovery review set.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-06-20T00:00:00.0000000Z
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
ms.custom: sfi-image-nochange
locale: en-us
document_id: c6154103-35ba-5c74-80f8-a4e3fef66014
document_version_independent_id: c6154103-35ba-5c74-80f8-a4e3fef66014
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-teams-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-teams-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-teams-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: fcdfda84-42ec-417e-2ab8-59d50d775527
---

# Review Microsoft Teams content in a review set in eDiscovery | Microsoft Learn

After you add Microsoft Teams content to a review set, review the content for its relevance to your investigation and remove any irrelevant content. To review Teams content, you need to understand how eDiscovery processes Teams meeting, chat conversations, and attachments when adding them to a review set. The following processing of Teams content takes place:

- **Grouping**: eDiscovery groups messages, posts, and replies in Teams conversations together and presents them in the review set. This processing also includes extracting and grouping attachments in chat conversations within the conversation.
- **Conversation transcript threading**: eDiscovery determines what additional content from a conversation to collect to provide context around items that matched the collection criteria.
- **Deduplication**: eDiscovery processes and manages duplicate Teams content.
- **Metadata**: eDiscovery adds metadata content for Teams content after the content is added to a review set.

Note

The date and time for all conversations in Teams are shown in Coordinated Universal Time (UTC).

Understanding grouping, conversation threading, deduplication, and Teams metadata helps you optimize the review and analysis of Teams content. This section also has tips for viewing Teams content in a review set.

## Grouping

When you [add content from Teams chat conversations to a review set](edisc-search-add-to-review-set), you aggregate messages, posts, and replies from conversations in HTML transcript files if you select the **Organize conversations into HTML transcript** setting. A single chat conversation can have multiple transcript files. These transcript files present Teams content as continuous conversations, not as individual or separate messages. This approach provides context for items that matched the search criteria of your collections in the previous step and reduces the number of items collected into the review set. Group transcripts and associated items by *family* or *conversation*. Items in the same family share the same value for the **FamilyId** or **GroupId** metadata property. Items in the same conversation share the same value for the **ConversationId** or **ThreadId** metadata property, depending on the [grouping configuration selected](edisc-review-set-view).

The following table describes how the different types of Teams content group by family and conversation.

| **Teams content type** | **Group by family** | **Group by conversation** |
| --- | --- | --- |
| Teams 1:1 and group chats | A transcript and all of its attachments and extracted items share the same **FamilyId**. Each transcript has a unique **FamilyId**. | All transcript files and their family items within the same conversation share the same **ConversationId**. This includes the following items: All extracted items and attachments of all transcripts that share the same **ConversationId**.- All transcripts for the same chat conversation<br>- All custodian copies of each transcript<br>- Transcripts from subsequent collections from the same chat conversation<br> For Teams 1:1 and group chat conversations, you might have multiple transcript files, each one corresponding to a different time frame within the conversation. Because these transcript files are from the same conversation with the same participants, they share the same **ConversationId**. |
| Standard, private, and shared channel chats | Each post and all replies and attachments are saved to its own transcript. This transcript and all of its attachments and extracted items share the same **FamilyId**. | Each post and its attachments and extracted items have a unique **ConversationId**. If there are subsequent collections or new replies from the same post, the delta transcripts resulting from those collections also have the same **ConversationId**. |
| Teams meetings | Each meeting |  |

Use the **Group** control in the command bar of a review set to view Teams content grouped by family or conversation.

- Select **Group family attachments** to view Teams content grouped by family. Each transcript file is displayed on a line in the list of review set items. Attachments are nested under the item.
- Select **Group Teams or Viva Engage conversations** to view Teams content grouped by conversation. Each conversation is displayed on a line in the list of review set items. Transcript files and attachments are nested under the top-level conversation.

Note

[Cloud attachments](edisc-cloud-attachments) group with the conversations they appear in. This grouping happens by assigning the same **GroupID** as the transcript file of the message the file was attached to and the same **ConversationId** as the conversation the message appeared in. This setup means multiple copies of cloud attachments might be added to the review set if you attach them to different conversations.

## View recorded meeting transcripts

The transcript of the recorded meeting audio is captured as a separate file and automatically indexed for search. Recorded meetings in a review set are stored as a .zip file that contains the following files:

- The transcript of the meeting audio in .txt format
- The video recording of the meeting in .mp4 format
- The thumbnail image of the meeting in .jpg format
- Meeting metadata and meeting chapters (as applicable) in .json format

To view meeting audio transcript files in a review set, select the meeting and the **Transcript** viewer on the meeting details pane. The following screenshots show an example of a meeting in the Teams client and the meeting transcript file of the same meeting in the review set.

### Meeting in Teams client

![Team meeting shown in Teams client.](media/ediscovery-meeting-in-teams-client.png)

### Meeting transcript file in a review set

![Meeting shown in the meeting transcript file in a review set.](media/ediscovery-teams-meeting-transcript-view.png)

### View conversation transcript files

When you view transcript files in a review set, some of the messages appear highlighted in purple. The highlighted messages depend on which custodian copy of the transcript you're viewing. For example, in a 1:1 chat between User4 and User2, the messages posted by User4 are highlighted in purple when you view the transcript collected from User4's mailbox. When you view User2's transcript of the same conversation, messages posted by User2 are highlighted in purple. This highlighting behavior is based on the same Teams client experience, where a user's posts are highlighted in purple in the Teams client.

The following screenshots show an example of conversation in the Teams client and the transcript file of the same conversation in the review set. The purple highlighting in the transcript file indicates that the transcript was collected from User2's mailbox.

#### Conversation in Teams client

![Conversation shown in Teams client.](media/teamsclient1.png)

#### Conversation in a transcript file

![Conversation shown in the transcript file in a review set.](media/ediscovery-conversation-transcript-view.png)

## Include contextual conversations for Teams chat messages

If you select **Include Teams and Viva Engage conversations** during the **add to review set** process, eDiscovery helps you identify contextual content related to items that might be relevant to your investigation. This feature produces distinct conversation views that include chat messages that precede and follow the items match the search query during collection. This capability allows you to review complete chat conversations in Microsoft Teams. This capability is independent from HTML threading and only affects whether contextual conversations are included in the process of adding items to a review set.

Here's the logic used by eDiscovery to include additional messages and replies that provide context around the items match the search query (called *responsive items*) you used when adding Teams content to a review set. Different behaviors are based on the types of chats and the search query used to collect the responsive items. There are two common search scenarios:

- Queries that use search parameters, such as keywords and property:value pairs
- Queries that only use date ranges

| **Teams content type** | **Queries with search parameters** | **Queries with date ranges** |
| --- | --- | --- |
| Teams 1:1 and group chats | Messages that were posted 12 hours before and 12 hours after responsive items are included | Messages that fall in between the data range and any contextual messages within a 24-hour window are included. |
| Standard, private, and shared Teams channel chats | Each post that contains responsive items and all corresponding replies are included. | Each post that contains responsive items and all corresponding replies are included. |

## Deduplication of Teams content

The following list describes the deduplication (and duplication) behavior when collecting Teams content into a review set when a user chooses to organize conversations in an HTML transcript.

- Each transcript file you add to a review set maps one-to-one to content stored in data locations. That means eDiscovery doesn't collect any Teams content that you already added to the review set. If you already collected a chat message in a review set, eDiscovery doesn't add the same message from the same data location to the review set in subsequent collections.
- For 1:1 and group chats, copies of messages are stored in the mailbox of each conversation participant. Copies of the same conversation that exist in different participants' mailboxes are collected with different metadata. As a result, each instance of the conversation is treated as unique and brought into the review set in separate transcript files. If you add all participants of a 1:1 or group chat as custodians in a case and include them in the scope of a collection, you add copies of each transcript (for the same conservation) to the review set and group them together with the same **ConversationId** or **ThreadId**. Each of these copies is associated with a corresponding data source.
- In subsequent **Add to review set** processes where there are items from the same conversation, only the delta content that you didn't previously add is added to the review set and grouped (by sharing the same **ConversationId** or **ThreadId**) with the previously added items from the same conversation. Here's an example of this behavior:

    1. Process A adds messages in a conversation between User1 and User2 to the review set.
    2. Process B adds messages from the same conversation, but there are new messages between User1 and User2 since process A was run.
    3. Only the new messages in Process B are added to the review set. These messages are added to a separate transcript file, but the new transcript is grouped with the transcripts from Process A by the same **ConversationId**.

    This behavior applies to all the types of Teams chats.

## Metadata for Teams content

In large review sets with thousands or millions of items, it can be difficult to narrow the scope of your review to Teams content. To help you focus your review on Teams content, use metadata properties that are specific to Teams content. Use these properties to organize the columns in the review list and [configure filters and queries](edisc-search-query) to optimize the review of Teams content. These metadata properties are also included when you export Teams content from eDiscovery, to help you organize and view content post-export or in non-Microsoft eDiscovery tools.

The following table describes metadata properties for Teams content.

| **Metadata property** | **Description** |
| --- | --- |
| ContainsDeletedMessage | Indicates whether a transcript file contains a deleted message. Deleted messages are identified when viewing the transcript file. |
| ContainsEditedMessage | Indicates whether a transcript file contains an edited message. Edited messages are identified when viewing the transcript file. |
| ConversationId | A GUID that identifies the conversation that the item is associated with. Transcript files and attachments from the same conversation have the same value for this property. |
| Conversation name | The name of the conversation the transcript file or attachment is associated with. For Teams 1:1 and group chats, the value of this property is the User Principal Name (UPN) of all participants of the conversation are concatenated. For example, `User3 <User3@contoso.onmicrosoft.com>,User4 <User4@contoso.onmicrosoft.com>,User2 <User2@contoso.onmicrosoft.com>`. Teams channel (standard, private, and shared) chats use the following format for conversation name: `<Team name>,<Channel name>`. For example, `eDiscovery vNext, General`. |
| ConversationType | Indicates the type of Team chat. For Teams 1:1 and group chats, the value for this property is `Group`. For standard, private, and shared channel chats, the value is `Channel`. |
| Date | The time stamp of the first message in the transcript file in UTC. |
| FamilyId | A GUID that identifies the transcript file for a chat conversation. Attachments have the same value for this property as the transcript file that contains the message the file was attached to. |
| FileClass | Indicates that type of content. Items from Teams chats have the value `Conversation`. In contrast, Exchange email messages have the value `Email`. |
| MessageKind | The message kind property. Teams content has the value `microsoftteams , im`. |
| Participants | List of all people who are involved in the chat, includes both senders and recipients in a conversation. |
| Recipients | A list of all users who received a message within the transcript conversation. |
| TeamsChannelName | The Teams channel name of the transcript. |

For descriptions of other eDiscovery metadata properties, see [Document metadata fields in eDiscovery](edisc-ref-document-metadata-fields).

## Export Teams content

After you review and cull Teams content in a review set, you can export all items that are applicable to your investigation. There aren't any specific export settings for Teams content. If you add the content to the review set as a transcript file, then each transcript is exported as an HTML message file. The metadata properties discussed in the previous section are included when Teams content is exported.

Each export item (transcript or individual messages) is referenced in the [items.csv report](edisc-process-report-use#items-csv-report) and you can locate it by using the target path field in the report. Transcript files are located in the Conversations folder in the root export folder.

## Tips for viewing Teams content in a review set

Here are some tips and best practices for viewing Teams content in a review set.

- Use the **Customize columns** control in the command bar to add and organize columns to optimize the review of Teams content. You can add and remove columns that are useful for Teams content. You can also sequence the order of columns by dragging and dropping them in the **Edit column** flyout page. You can also sort on columns to group Teams content with similar values for the column you sort on.
- Useful columns that help you review Teams content include **Participants**, **Recipients**, and **File type** or **Message kind**.
- Use [filters](edisc-review-set-search) for Teams-related properties to quickly display Teams content. There are filters for most of the metadata properties described in the previous section.

## Delete Teams chat messages

You can use eDiscovery and the Microsoft Graph Explorer to respond to data spillage incidents when content containing confidential or malicious information is released through Teams chat messages. Admins in your organization can search for and delete chat messages in Microsoft Teams. This feature can help you remove sensitive information or inappropriate content in Teams chat messages. For more information, see [Search and purge chat messages in Teams](edisc-search-teams-data).