---
layout: Conceptual
title: Finding content in mailboxes in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-mailboxes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about finding content in mailboxes in eDiscovery in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-08T00:00:00.0000000Z
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
document_id: d41bef1e-1a2d-b668-4ea7-c6744063f31b
document_version_independent_id: d41bef1e-1a2d-b668-4ea7-c6744063f31b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-mailboxes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-mailboxes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-mailboxes.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 62ece562-2ae1-c8bb-2b2e-43996d30d871
---

# Finding content in mailboxes in eDiscovery | Microsoft Learn

Admins often need to find out who knew what and when. They need to respond to requests about ongoing or potential litigation, internal investigations, and other scenarios in the most efficient and effective way possible. These requests are often urgent, involve multiple stakeholder teams, and have significant impact if not completed in a timely manner. Knowing how to find the right information is critical for admins to complete searches successfully and help their organizations manage the risk and cost associated with eDiscovery requirements.

For more information about finding content in mailboxes in eDiscovery, watch the following video:

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

When an eDiscovery request is submitted, admins often receive only partial information to start collecting content that might be related to a particular investigation. The request might include user names, project titles, rough date ranges when the project was active, and not much more. From this information, admins need to [create queries](edisc-search-query) to find relevant content across Microsoft 365 services to determine the information needed for a particular project or subject. Understanding how information is stored and managed for these services helps admins more efficiently find what they need quickly and in an effective manner.

Exchange Online stores email, chat, meeting, and Microsoft 365 Copilot and Microsoft 365 Copilot Chat activity data (user prompts and Copilot responses). Many communication properties are available for searching items included in Exchange Online. Some properties such as *From*, *Sent*, *Subject*, and *To* are unique to certain items and aren't relevant when searching for files or documents in SharePoint and OneDrive. Including these types of properties when searching across workloads can sometimes lead to unexpected results.

For example, to find content related to specific users (*User 1* and *User 2*), associated with a project called *Tradewinds*, and during January 2020 through January 2022, you might use a query with the following properties:

- Add User 1 and User 2's Exchange Online locations as [data sources](edisc-data-sources) to the case
- Select User 1 and User 2's Exchange Online locations as data source.
- For **Keyword**, use *Tradewinds*
- For **Date Range**, use the *January 1, 2020* to *January 31, 2022* range

When searching for emails or other mailbox content that might include [cloud attachments](edisc-cloud-attachments), the cloud attachment link to a storage location in SharePoint or OneDrive should be considered as attachments of the message file rather than separate documents.

This behavior is similar to how a search returns emails with embedded local attachments, these attachments are retrieved as if they're part of the emails. Any compliance boundaries for SharePoint or OneDrive aren't reflected in the collection of cloud attachments included in responsive messages.

Important

For emails, when you use a keyword, the search includes the subject, body, and many properties related to the participants. However, due to recipient expansion, search might not return expected results when using the alias or part of the alias. Therefore, use the full UPN.

## Searchable email properties in KeyQL

Important

While email messages might have other properties supported in other Microsoft 365 services, eDiscovery search tools support only the email properties listed in this table. You can't include other email message properties in searches.

The following table lists the email message properties supported in search using the eDiscovery [KeyQL](edisc-keyword-query-language) editor in the Microsoft Purview portal or by using the [New-ComplianceSearch](/en-us/powershell/module/exchangepowershell/new-compliancesearch?view=exchange-ps) or [Set-ComplianceSearch](/en-us/powershell/module/exchangepowershell/set-compliancesearch?view=exchange-ps) cmdlets. For a list of supported condition builder properties, see [Use the condition builder to create search queries in eDiscovery](edisc-condition-builder#conditions-for-mail-properties).

The table includes an example of the *property:value* syntax for each property and a description of the search results returned by the examples. You can enter these `property:value` pairs in the keywords box for an eDiscovery search.

Note

When searching email properties, you can't search for message headers. Header information isn't indexed for searches. Additionally, you can't search for items in which the specified property is empty or blank. For example, using the *property:value* pair of **subject:""** to search for email messages with an empty subject line returns zero results. This limitation also applies when searching site and contact properties.

| Property | Property description | Examples | Search results returned by the examples |
| --- | --- | --- | --- |
| AttachmentNames | The names of files attached to an email message. | `attachmentnames:annualreport.ppt`<br>`attachmentnames:annual*` | Messages that have an attached file named *annualreport.ppt*. In the second example, using the wildcard character ( \* ) returns messages with the word *annual* in the file name of an attachment.^1^ |
| Bcc | The Bcc field of an email message.^1^ | `bcc:pilarp@contoso.com`<br>`bcc:pilarp`<br><br>`bcc:"Pilar Pinilla"` | All examples return messages with *Pilar Pinilla* included in the Bcc field.(See Recipient Expansion) |
| Category | The categories to search. Users can define categories by using Outlook or Outlook on the web (formerly known as Outlook Web App). The possible values are: <br>- blue<br>- green<br>- orange<br>- purple<br>- red<br>- yellow | `category:"Red Category"` | Messages that are assigned the *red* category in the source mailboxes. |
| Cc | The Cc field of an email message.^1^ | `cc:pilarp@contoso.com`<br>`cc:"Pilar Pinilla"` | In both examples, messages with *Pilar Pinilla* specified in the Cc field.(See Recipient Expansion) |
| From | The sender of an email message.^1^ | `from:pilarp@contoso.com` | Messages sent by the specified user.(See Recipient Expansion) |
| HasAttachment | Indicates whether a message has an attachment. Use the values **true** or **false**. | `from:pilar@contoso.com AND hasattachment:true` | Messages sent by the specified user that have attachments. |
| Importance | The importance of an email message, which a sender can specify when sending a message. By default, messages are sent with normal importance, unless the sender sets the importance as **high** or **low**. | `importance:high`<br>`importance:medium`<br><br>`importance:low` | Messages that are marked as high importance, medium importance, or low importance. |
| IsRead | Indicates whether messages are read. Use the values **true** or **false**. | `isread:true`<br>`isread:false` | The first example returns messages with the IsRead property set to **True**. The second example returns messages with the IsRead property set to **False**. |
| ItemClass | Use this property to search specific third-party data types that your organization imported to Microsoft 365. Use the following syntax for this property: `itemclass:ipm.externaldata.<third-party data type>*` | `itemclass:ipm.externaldata.Facebook* AND subject:contoso`<br>`itemclass:ipm.externaldata.Twitter* AND from:"Ann Beebe" AND "Northwind Traders"` | The first example returns Facebook items that contain the word "contoso" in the Subject property. The second example returns Twitter items that were posted by Ann Beebe and that contain the keyword phrase "Northwind Traders". |
| Kind | The type of email message to search for. Possible values: <br> contacts <br><br> docs <br><br> email <br><br> externaldata <br><br> faxes <br><br> im <br><br> journals <br><br> meetings <br><br> microsoftteams (returns items from chats, meetings, and calls in Microsoft Teams) <br><br> notes <br><br> posts <br><br> rssfeeds <br><br> tasks <br><br> voicemail | `kind:email`<br>`kind:email OR kind:im OR kind:voicemail`<br><br>`kind:externaldata` | The first example returns email messages that meet the search criteria. The second example returns email messages, instant messaging conversations (including Skype for Business conversations and chats in Microsoft Teams), and voice messages that meet the search criteria. The third example returns items that were imported to mailboxes in Microsoft 365 from third-party data sources, such as Twitter, Facebook, and Cisco Jabber that meet the search criteria. For more information, see [Archiving third-party data](archive-third-party-data). |
| Participants | All the people fields in an email message. These fields are From, To, Cc, and Bcc.^1^ | `participants:garthf@contoso.com`<br>`participants:contoso.com` | Messages sent by or sent to garthf@contoso.com. The second example returns all messages sent by or sent to a user in the contoso.com domain.(See Recipient Expansion) |
| Received | The date that an email message is received by a recipient. | `received:2021-04-15`<br>`received>=2021-01-01 AND received<=2021-03-31` | Messages that are received on April 15, 2021. The second example returns all messages received between January 1, 2021 and March 31, 2021. |
| Recipients | All recipient fields in an email message. These fields are To, Cc, and Bcc.^1^ | `recipients:garthf@contoso.com`<br>`recipients:contoso.com` | Messages sent to garthf@contoso.com. The second example returns messages sent to any recipient in the contoso.com domain.(See Recipient Expansion) |
| Sent | The date that an email message is sent by the sender. | `sent:2021-07-01`<br>`sent>=2021-06-01 AND sent<=2021-07-01` | Messages that are sent on the specified date or sent within the specified date range. |
| Size | The size of an item, in bytes. | `size>26214400`<br>`size:1..1048567` | Messages larger than 25 MB. The second example returns messages from 1 through 1,048,567 bytes (1 MB) in size. |
| Subject | The text in the subject line of an email message. <br>**Note:** When you use the Subject property in a query, the search returns all messages in which the subject line contains the text you're searching for. In other words, the query doesn't return only those messages that have an exact match. For example, if you search for `subject:"Quarterly Financials"`, your results include messages with the subject "Quarterly Financials 2018". | `subject:"Quarterly Financials"`<br>`subject:northwind` | Messages that contain the phrase "Quarterly Financials" anywhere in the text of the subject line. The second example returns all messages that contain the word northwind in the subject line. |
| To | The To field of an email message.^1^ | `to:annb@contoso.com`<br>`to:annb ``to:"Ann Beebe"` | All examples return messages where Ann Beebe is specified in the To: line. |

Note

^1^ For the value of a recipient property, you can use email address (also called user principal name (UPN)), display name, or alias to specify a user. For example, you can use annb@contoso.com, annb, or "Ann Beebe" to specify the user Ann Beebe.

## Searchable sensitive data types

You can use eDiscovery search tools in the Microsoft Purview portal to search for sensitive data, such as credit card numbers or social security numbers, stored in documents in mailboxes. To search for this data, use the `SensitiveType` property and the name or ID of a sensitive information type in a keyword query. For example, the query `SensitiveType:"Credit Card Number"` returns documents that contain a credit card number. The query `SensitiveType:"U.S. Social Security Number (SSN)"` returns documents that contain a U.S. social security number.

To see a list of sensitive information types that you can search for, go to **Data classifications** &gt; **Sensitive info types** in the Microsoft Purview portal. Or, use the **Get-DlpSensitiveInformationType** cmdlet in Security & Compliance PowerShell to display a list of sensitive information types.

`SensitiveType` behavior depends on the workload and how the content is indexed. Use the following matrix to set expectations before running a query:

| Workload | `SensitiveType`supported? | When the match is evaluated | Common caveats |
| --- | --- | --- | --- |
| Exchange Online (mail, calendar, contacts) | Yes | At indexing time, against the message body and indexed attachments | Sensitive types added or modified *after* an item was indexed don't match that item until it's reindexed. Inline images, scanned PDFs, and other non-text content aren't evaluated. |
| Items that are [partially indexed](edisc-ref-partially-indexed-items) | Not evaluated | N/A | `SensitiveType` queries don't return partially indexed items. To include them, also export partially indexed items separately. |
| Microsoft Teams (chat and channel messages) | Limited | At indexing time, against message text only | Match accuracy is lower for short messages because most sensitive info types require corroborating context. Attachments in Teams messages follow the SharePoint/OneDrive rules. |
| SharePoint Online / OneDrive for Business (documents) | Yes | At indexing time, against the document content | Same reindexing caveat as Exchange. Files larger than the [indexing size limit](edisc-ref-limits#indexing-limits) are partially indexed and might not match. |

If you expect a hit but don't get one, confirm that (1) the workload is in the supported column, (2) the item was indexed *after* the sensitive type was last published, and (3) the item isn't in the partially indexed set.

## Recipient expansion

Mailboxes are flexible storage, and clients connecting to a mailbox control some aspects of recipient information, especially for the sender. Clients can choose the *SMTP*, *Name*, or *LegacyDN* properties as the sender address. To compensate for variations in client behavior and how data is stored, eDiscovery search's recipient expansion is a useful feature.

Often, sender information created by some clients only stores the name of the sender, such as *John Doe*, without including the SMTP address like *johndoe@contoso.com*. Additionally, federated items with legacy systems might only store the LegacyExchangeDN, which is a unique identifier used in older versions of Exchange to represent a mailbox or a distribution list. Federated systems refer to messages or data that are integrated from different systems or organizations, often involving legacy systems that use older formats or identifiers.

The recipient expansion function solves the issue of not searching broadly enough by expanding the search to capture content stored with these variations. Querying Microsoft Entra ID expands any values specified in the participant filter. This expansion includes the user's email address, UPN, alias, display name, and LegacyExchangeDN. This expansion ensures that searches cast a wider net, capturing all relevant content regardless of how participant information is stored and improves the accuracy and comprehensiveness of eDiscovery searches.

Note

Recipient expansion doesn't resolve cases where the user's Microsoft Entra ID object is deleted - typically a departed user whose mailbox was deleted without first being placed on hold. Departed users whose mailboxes are placed on hold remain in Microsoft Entra ID as [inactive mailboxes](edisc-data-sources), and recipient expansion still works for them (subject to the SMTP and display name conditions described later in this section). When the Microsoft Entra ID object is gone, you must manually include all known identifiers (for example, previous SMTP addresses, aliases, or display names) in your query. To preserve recipient expansion for departing employees, place the mailbox on hold before deleting the account.

When you search any of the recipient properties (From, To, Cc, Bcc, Participants, and Recipients), Microsoft 365 attempts to expand the identity of each user by looking them up in Microsoft Entra ID. If the user is found in Microsoft Entra ID, the query is expanded to include the user's email address (or UPN), alias, display name, and LegacyExchangeDN. For example, a query such as `participants:ronnie@contoso.com` expands to `participants:ronnie@contoso.com OR participants:ronnie OR participants:"Ronald Nelson" OR participants:"<LegacyExchangeDN>"`.

To prevent recipient expansion, add a wildcard character (asterisk) to the end of the email address and use a reduced domain name; for example, `participants:"ronnie@contoco*"` Be sure to surround the email address with double quotation marks.

Preventing recipient expansion in the search query might result in relevant items not being returned in the search results. Email messages in Exchange can be saved with different text formats in the recipient fields. Recipient expansion is intended to help mitigate this fact by returning messages that might contain different text formats. So preventing recipient expansion might result in the search query not returning all items that might be relevant to your investigation.

Recipient expansion isn't designed to support scenarios involving user name and alias changes. If the SMTP/UPN for a user changes, Microsoft Entra ID might not find the user, leading to incomplete search results. Also, LegacyExchangeDN, which rarely changes, might not be present in the substrate for all email items. Recipient expansion only handles cases where the client uses LegacyExchangeDN instead of SMTP. If the SMTP address changes but the LegacyExchangeDN doesn't, then recipient expansion doesn't help and you need to manually find and use all variations of these addresses. This limitation can lead to users mistakenly believing that recipient expansion catches all variations, including name and SMTP changes.

When you use the *From* condition with the *equal* condition (=), only the display name is queryable in the index. This means that if you use an SMTP address in the *From* or *Sender* conditions, search returns a result if both of the following conditions are met:

- The SMTP address used in the condition matches an active or inactive user in Microsoft Entra.
- The display name of the active or inactive user hasn't changed since the targeted item was sent or received.

When you use the *Sender* or *From* conditions in an eDiscovery search, the system attempts recipient expansion and expands the query to include *Display Name*. If successful, the query includes all email addresses assigned to the user's SMTP address and legacy Exchange display name. If recipient expansion isn't successful, the search uses only the value supplied in the *From* and *Sender* conditions to search the index. Conditions that might result in recipient expansion failing are:

- Departed users without a retained inactive mailbox.
- Active or inactive users where the SMTP address is no longer present on an object.
- Active or inactive users where the display name has been changed (when display name is used with the *Sender* or *From* conditions).

In some scenarios, recipient expansion might also cause hits on additional items when organization searches are used. For example, one user's display name might form a part of another user's display name. For example, a user might have a display name of *John Doe* and another user might have a display name of *John Doe Jr*. An organization-wide search might return result hits from both mailboxes. Consider suppressing recipient expansion in this scenario by adding a period at the end of the SMTP address.

Additional considerations include, the recipient expansion only supports sending from your own mailbox and no delegated or send-as activity. Make sure you review relevant limits, including the accuracy of the maximum number of distribution group members and the maximum level of nesting for distribution groups. Security groups are supported, and only distribution groups and the distribution group should be valid when the email is sent.

Note

If you need to review or reduce the items returned by a search query due to recipient expansion, consider using premium eDiscovery features. You can search for messages (taking advantage of recipient expansion), add them to a review set, and then use review set queries or filters to review or narrow the results.

## Content stored in Exchange Online mailboxes for eDiscovery

You primarily use a mailbox in Exchange Online to store email-related items such as messages, calendar items, tasks, and notes. But that's changing as more cloud-based apps also store their data in a user's mailbox. One advantage of storing data in a mailbox is that you can use the search tools in eDiscovery to find, view, and export the data from these cloud-based apps.

The data from some of these apps is stored in hidden folders located in a non-interpersonal message (non-IPM) subtree in the mailbox. Data from other cloud-based apps might not be stored *in* the mailbox, but it's *associated with* the mailbox, and is returned in searches if that data matches the search query. Regardless of whether cloud-based data is stored in or associated with a user mailbox, the data is typically not visible in an email client when a user opens their mailbox.

The following table lists the apps that either store or associate data with a cloud-based mailbox. The table also describes the type of content that each app produces.

| Microsoft 365 app | Description |
| --- | --- |
| Class Schedule | Plans you create in Class Schedule are stored in the mailbox of the corresponding Microsoft 365 Group that's provisioned when you create a new plan. The alias for the group mailbox is the name of the plan. |
| Forms^\*^ | Forms and responses to a form are stored in files that are attached to email messages and stored in a hidden folder in the mailbox of the user who created the form. Forms created before April 2020 are stored as a PDF file. Forms created after 2020 are stored as a JSON file. Responses to a form are stored in a CSV file. When you export content from Forms in a PST file, this data is located in the **ApplicationDataRoot** folder in a subfolder named with the following globally unique identified (GUID): **c9a559d2-7aab-4f13-a6ed-e7e9c52aec87**. |
| Microsoft 365 Copilot and Microsoft 365 Copilot Chat | All Copilot activity data (user prompts and Copilot responses) generated in supported Microsoft 365 apps and services is stored in custodian mailboxes. |
| Microsoft 365 Groups | Email messages, calendar items, contacts (People), notes, and tasks are stored in the mailbox that's associated with a Microsoft 365 group. |
| Outlook/Exchange Online | Email messages, calendar items, contacts (People), notes, and tasks are stored in a user's mailbox. |
| People | Contacts in the People app (which are the same contacts as the ones accessible in Outlook) are stored in a user's mailbox. |
| Skype for Business | Conversations in Skype for Business are stored in the Conversation History folder in a user's mailbox. If the mailbox of a participant of a Skype meeting is placed on [Litigation Hold](/en-us/microsoft-365/admin/misc/create-litigation-hold-mac?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) or assigned to a [retention policy](retention), files attached to a meeting are retained in the participants mailbox. |
| Sway^\*^ | Sways are stored as an HTML file that is attached to an email message and stored in a hidden folder in the mailbox of the user who created the sway. When you export content from Sway in a PST file, this data is located in the **ApplicationDataRoot** folder in a subfolder named with the following GUID: **905fcf26-4eb7-48a0-9ff0-8dcc7194b5ba**. |
| Tasks | Tasks in the Tasks app (which are the same tasks as the ones accessible in Outlook) are stored in a user's mailbox. |
| Teams | Conversations that are part of a Teams channel are associated with the Teams mailbox. Conversations that are part of the Chat list in Teams (also called *1 x N chats*) are associated with the mailbox of the users who participate in the chat. Also, summary information for meetings and calls in a Teams channel are associated with mailboxes of users who dialed into the meeting or call. So when searching for Teams content, you search the Teams mailbox for content in channel conversations and search user mailboxes for content in 1 x N chats. |
| To-Do | Tasks (called *to-dos*, which are saved in to-do lists) in the To-Do app are stored in a user's mailbox. |
| Viva Engage | Conversations and comments within a Viva Engage community are associated with the Microsoft 365 group mailbox, as well as the user mailbox of the author and any named recipients (@ mentioned or Cc'ed users). Private messages sent outside of a Viva Engage community are stored in the mailbox of the users who participate in the private message. |

Note

^\*^ At this time, if you place a hold on a mailbox using holds in eDiscovery cases, the hold doesn't preserve content from this app.