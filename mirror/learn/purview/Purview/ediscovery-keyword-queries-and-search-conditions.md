---
layout: Conceptual
title: Keyword queries and search conditions for eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-keyword-queries-and-search-conditions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about email and document properties that you can search by using the eDiscovery search tools in Microsoft Purview.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
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
ms.custom:
- seo-marvel-apr2020
- sfi-image-nochange
locale: en-us
document_id: 9a6fe31e-cdf0-03cc-de53-a7e25a518089
document_version_independent_id: 9a6fe31e-cdf0-03cc-de53-a7e25a518089
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-keyword-queries-and-search-conditions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-keyword-queries-and-search-conditions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-keyword-queries-and-search-conditions.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 09957b89-6c47-6b10-3f4f-6fcffb06aef6
---

# Keyword queries and search conditions for eDiscovery | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

This article describes the properties available to help find content across email and chat in Exchange Online and documents and files stored on SharePoint and OneDrive using the eDiscovery search tools in the Microsoft Purview portal.

This includes Content search, Microsoft Purview eDiscovery (Standard), and Microsoft Purview eDiscovery (Premium) (eDiscovery searches in eDiscovery (Premium) are called *collections*). You can also use the **\*-ComplianceSearch** cmdlets in [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell) to search for these properties.

This article also describes:

- Using Boolean search operators, search conditions, and other search query techniques to refine your search results.
- Searching for communications of various types related to specific users and projects during a specific time frame.
- Searching for site content that is related to a specific project, users and/or subjects during a specific time period.

For step-by-step instructions on how to create different eDiscovery searches, see:

- [Content search](ediscovery-content-search)
- [Search for content in eDiscovery (Standard)](ediscovery-search-for-content)
- [Create a collection estimate in eDiscovery (Premium)](ediscovery-create-draft-collection)

Note

eDiscovery searches in the Microsoft Purview portal and the corresponding **\*-ComplianceSearch** cmdlets in Security & Compliance PowerShell use the Keyword Query Language (KeyQL). For more detailed information, see [Keyword Query Language syntax reference](/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference).

## Search tips and tricks

- The time zone for all searches is Coordinated Universal Time (UTC). Changing time zones for your organization isn't currently supported. Time zone display settings in the search view are only for applicable for values in *Data* column and don't affect time stamps on collected items.
- Keyword searches aren't case-sensitive. For example, **cat** and **CAT** return the same results.
- The Boolean operators **AND**, **OR**, **NOT**, and **NEAR** must be uppercase.
- Using quotes stops wild cards and any operations inside the quotes.
- A space between two keywords or two `property:value` expressions is the same as using **OR**. For example, `from:"Sara Davis" subject:reorganization` returns all messages sent by Sara Davis or messages that contain the word reorganization in the subject line. However, using a mix of spaces and **OR** conditionals in a single query might lead to unexpected results. We recommend using either spaces or **OR** in a single query.
- Use syntax that matches the `property:value` format. Values aren't case-sensitive, and they can't have a space after the operator. If there's a space, your intended value is a full-text search. For example `to: pilarp` searches for "pilarp" as a keyword, rather than for messages sent to pilarp.
- When searching a recipient property, such as To, From, Cc, or Recipients, you can use an SMTP address, alias, or display name to denote a recipient. For example, you can use pilarp@contoso.com, pilarp, or "Pilar Pinilla."
- You can use only prefix searches; for example, **cat\*** or **set\***. Suffix searches (**\*cat**), infix searches (**c\*t**), and substring searches (**\*cat\***) aren't supported.
- When searching a property, use double quotation marks (" ") if the search value consists of multiple words or special characters. For example, `subject:budget Q1` returns messages that contain **budget** in the subject line and that contain **Q1** anywhere in the message or in any of the message properties. Using `subject:"budget Q1"` returns all messages that contain **budget Q1** anywhere in the subject line.
- To exclude content marked with a certain property value from your search results, place a minus sign (-) before the name of the property. For example, `-from:"Sara Davis"` excludes any messages sent by Sara Davis.
- You can export items based on message type. For example, to export Skype conversations and chats in Microsoft Teams, use the syntax `kind:im`. To return only email messages, you would use `kind:email`. To return chats, meetings, and calls in Microsoft Teams, use `kind:microsoftteams`.
- When searching sites, you have to add the trailing `/` to the end of the URL when using the `path` property to return only items in a specified site. If you don't include the trailing `/`, items from a site with a similar path name are also returned. For example, if you use `path:sites/HelloWorld` then items from sites named `sites/HelloWorld_East` or `sites/HelloWorld_West` would also be returned. To return items only from the HelloWorld site, you have to use `path:sites/HelloWorld/`.
- The **Query language-country/region** must be defined in your search query prior to collecting content.
- When searching the **Sent** folders for emails, using the SMTP address for the sender isn't supported. Items in the **Sent** folder contain only display names.

## Finding content in Exchange Online

Admins are often charged with finding out who knew what when in the most efficient and effective way possible to respond to requests concerning ongoing or potential litigation, internal investigations, and other scenarios. These requests are often urgent, involve multiple stakeholder teams, and have significant impact if not completed in a timely manner. Knowing how to find the right information is critical for admins to complete searches successfully and help their organizations to manage the risk and cost associated with eDiscovery requirements.

When an eDiscovery request is submitted, often there's only partial information available for the admin to start to collect content that might be related to a particular investigation. The request might include employee names, project titles, rough date ranges when the project was active, and not much more. From this information, the admin needs to create queries to find relevant content across Microsoft 365 services to determine the information needed for a particular project or subject. Understanding how information is stored and managed for these services help admins more efficiently find what they need quickly and in an effective manner.

Email, chat, meeting, and Microsoft 365 Copilot and Microsoft 365 Copilot Chat activity data (user prompts and Copilot responses) are all stored in Exchange Online. Many communication properties are available for searching items included in Exchange Online. Some properties such as *From*, *Sent*, *Subject*, and *To* are unique to certain items and aren't relevant when searching for files or documents in SharePoint and OneDrive for Business. Including these types of properties when searching across workloads can sometimes lead to unexpected results.

For example, to find content related to specific employees (*User 1* and *User 2*), associated with a project called *Tradewinds*, and during January 2020 through January 2022, you might use a query with the following properties:

- Add User 1 and User 2's Exchange Online locations as data sources to the case
- Select User 1 and User 2's Exchange Online locations as collection locations
- For **Keyword**, use *Tradewinds*
- For **Date Range**, use the *January 1, 2020* to *January 31, 2022* range

Important

For emails, when a keyword is used, we search subject, body, and many properties related to the participants. However, due to recipient expansion, search might not return expected results when using the alias or part of the alias. Therefore we recommend using the full UPN.

## Searchable email properties

The following table lists the email message properties that can be searched by using the eDiscovery search tools in the Microsoft Purview portal or by using the **New-ComplianceSearch** or the **Set-ComplianceSearch** cmdlet.

Important

While email messages might have other properties supported in other Microsoft 365 services, only the email properties listed in this table are supported in eDiscovery search tools. Attempting to include other email messages properties in searches isn't supported.

The table includes an example of the *property:value* syntax for each property and a description of the search results returned by the examples. You can enter these `property:value` pairs in the keywords box for an eDiscovery search.

Note

When searching email properties, it's not possible to search for message headers. Header information isn't indexed for collections. Additionally, items in which the specified property is empty or blank aren't searchable. For example, using the *property:value* pair of **subject:""** to search for email messages with an empty subject line return zero results. This also applies when searching site and contact properties.

| **Property** | **Property description** | **Examples** | **Search results returned by the examples** |
| --- | --- | --- | --- |
| AttachmentNames | The names of files attached to an email message. | `attachmentnames:annualreport.ppt`<br>`attachmentnames:annual*` | Messages that have an attached file named *annualreport.ppt*. In the second example, using the wildcard character ( \* ) returns messages with the word *annual* in the file name of an attachment.^1^ |
| Bcc | The Bcc field of an email message.^1^ | `bcc:pilarp@contoso.com`<br>`bcc:pilarp`<br><br>`bcc:"Pilar Pinilla"` | All examples return messages with *Pilar Pinilla* included in the Bcc field.([See Recipient Expansion](ediscovery-keyword-queries-and-search-conditions#recipient-expansion)) |
| Category | The categories to search. Categories can be defined by users by using Outlook or Outlook on the web (formerly known as Outlook Web App). The possible values are: <br>- blue<br>- green<br>- orange<br>- purple<br>- red<br>- yellow | `category:"Red Category"` | Messages that have been assigned the *red* category in the source mailboxes. |
| Cc | The Cc field of an email message.^1^ | `cc:pilarp@contoso.com`<br>`cc:"Pilar Pinilla"` | In both examples, messages with *Pilar Pinilla* specified in the Cc field.([See Recipient Expansion](ediscovery-keyword-queries-and-search-conditions#recipient-expansion)) |
| Folderid | The folder ID (GUID) of a specific mailbox folder in 48-character format. If you use this property, be sure to search the mailbox that the specified folder is located in. Only the specified folder is searched. Any subfolders in the folder won't be searched. To search subfolders, you need to use the *Folderid* property for the subfolder you want to search. | `folderid:4D6DD7F943C29041A65787E30F02AD1F00000000013A0000`<br>`folderid:2370FB455F82FC44BE31397F47B632A70000000001160000 AND participants:garthf@contoso.com` | The first example returns all items in the specified mailbox folder. The second example returns all items in the specified mailbox folder that were sent or received by *garthf@contoso.com*. |
| From | The sender of an email message.^1^ | `from:pilarp@contoso.com` | Messages sent by the specified user.([See Recipient Expansion](ediscovery-keyword-queries-and-search-conditions#recipient-expansion)) |
| HasAttachment | Indicates whether a message has an attachment. Use the values **true** or **false**. | `from:pilar@contoso.com AND hasattachment:true` | Messages sent by the specified user that have attachments. |
| Importance | The importance of an email message, which a sender can specify when sending a message. By default, messages are sent with normal importance, unless the sender sets the importance as **high** or **low**. | `importance:high`<br>`importance:medium`<br><br>`importance:low` | Messages that are marked as high importance, medium importance, or low importance. |
| IsRead | Indicates whether messages have been read. Use the values **true** or **false**. | `isread:true`<br>`isread:false` | The first example returns messages with the IsRead property set to **True**. The second example returns messages with the IsRead property set to **False**. |
| ItemClass | Use this property to search specific third-party data types that your organization imported to Office 365. Use the following syntax for this property: `itemclass:ipm.externaldata.<third-party data type>*` | `itemclass:ipm.externaldata.Facebook* AND subject:contoso`<br>`itemclass:ipm.externaldata.Twitter* AND from:"Ann Beebe" AND "Northwind Traders"` | The first example returns Facebook items that contain the word "contoso" in the Subject property. The second example returns Twitter items that were posted by Ann Beebe and that contain the keyword phrase "Northwind Traders". <br> For a complete list of values to use for third-party data types for the ItemClass property, see [Use Content search to search third-party data that was imported to Office 365](use-content-search-to-search-third-party-data-that-was-imported). |
| Kind | The type of email message to search for. Possible values: <br> contacts <br><br> docs <br><br> email <br><br> externaldata <br><br> faxes <br><br> im <br><br> journals <br><br> meetings <br><br> microsoftteams (returns items from chats, meetings, and calls in Microsoft Teams) <br><br> notes <br><br> posts <br><br> rssfeeds <br><br> tasks <br><br> voicemail | `kind:email`<br>`kind:email OR kind:im OR kind:voicemail`<br><br>`kind:externaldata` | The first example returns email messages that meet the search criteria. The second example returns email messages, instant messaging conversations (including Skype for Business conversations and chats in Microsoft Teams), and voice messages that meet the search criteria. The third example returns items that were imported to mailboxes in Microsoft 365 from third-party data sources, such as Twitter, Facebook, and Cisco Jabber that meet the search criteria. For more information, see [Archiving third-party data in Office 365](https://www.microsoft.com/?ref=go). |
| Participants | All the people fields in an email message. These fields are From, To, Cc, and Bcc.^1^ | `participants:garthf@contoso.com`<br>`participants:contoso.com` | Messages sent by or sent to garthf@contoso.com. The second example returns all messages sent by or sent to a user in the contoso.com domain.([See Recipient Expansion](ediscovery-keyword-queries-and-search-conditions#recipient-expansion)) |
| Received | The date that an email message was received by a recipient. | `received:2021-04-15`<br>`received>=2021-01-01 AND received<=2021-03-31` | Messages that were received on April 15, 2021. The second example returns all messages received between January 1, 2021 and March 31, 2021. |
| Recipients | All recipient fields in an email message. These fields are To, Cc, and Bcc.^1^ | `recipients:garthf@contoso.com`<br>`recipients:contoso.com` | Messages sent to garthf@contoso.com. The second example returns messages sent to any recipient in the contoso.com domain.([See Recipient Expansion](ediscovery-keyword-queries-and-search-conditions#recipient-expansion)) |
| Sent | The date that an email message was sent by the sender. | `sent:2021-07-01`<br>`sent>=2021-06-01 AND sent<=2021-07-01` | Messages that were sent on the specified date or sent within the specified date range. |
| Size | The size of an item, in bytes. | `size>26214400`<br>`size:1..1048567` | Messages larger than 25 MB. The second example returns messages from 1 through 1,048,567 bytes (1 MB) in size. |
| Subject | The text in the subject line of an email message. <br>**Note:** When you use the Subject property in a query, the search returns all messages in which the subject line contains the text you're searching for. In other words, the query doesn't return only those messages that have an exact match. For example, if you search for `subject:"Quarterly Financials"`, your results include messages with the subject "Quarterly Financials 2018". | `subject:"Quarterly Financials"`<br>`subject:northwind` | Messages that contain the phrase "Quarterly Financials" anywhere in the text of the subject line. The second example returns all messages that contain the word northwind in the subject line. |
| To | The To field of an email message.^1^ | `to:annb@contoso.com`<br>`to:annb ``to:"Ann Beebe"` | All examples return messages where Ann Beebe is specified in the To: line. |

Note

^1^ For the value of a recipient property, you can use email address (also called *user principal name* or UPN), display name, or alias to specify a user. For example, you can use annb@contoso.com, annb, or "Ann Beebe" to specify the user Ann Beebe.

### Recipient expansion

Tip

Use the new [eDiscovery](edisc) experience and condition builder to use common mailbox and site [properties](edisc-condition-builder#conditions-for-common-properties) like *MessageIDs* and *ChatThreadIds* when searching for specific recipients or messages.

When searching any of the recipient properties (From, To, Cc, Bcc, Participants, and Recipients), Microsoft 365 attempts to expand the identity of each user by looking them up in Microsoft Entra ID. If the user is found in Microsoft Entra ID, the query is expanded to include the user's email address (or UPN), alias, display name, and LegacyExchangeDN. For example, a query such as `participants:ronnie@contoso.com` expands to `participants:ronnie@contoso.com OR participants:ronnie OR participants:"Ronald Nelson" OR participants:"<LegacyExchangeDN>"`.

To prevent recipient expansion, add a wild card character (asterisk) to the end of the email address and use a reduced domain name; for example, `participants:"ronnie@contoso*"` Be sure to surround the email address with double quotation marks.

However, be aware that preventing recipient expansion in the search query might result in relevant items not being returned in the search results. Email messages in Exchange can be saved with different text formats in the recipient fields. Recipient expansion is intended to help mitigate this fact by returning messages that might contain different text formats. So preventing recipient expansion might result in the search query not returning all items that might be relevant to your investigation.

Note

If you need to review or reduce the items returned by a search query due to recipient expansion, consider using eDiscovery (Premium). You can search for messages (taking advantage of recipient expansion), add them to a review set, and then use review set queries or filters to review or narrow the results. For more information, see [Collect data for a case](ediscovery-collections) and [Query the data in a review set](ediscovery-review-set-search).

## Finding content in SharePoint and OneDrive

Tip

Use the new [eDiscovery](edisc) experience and search [export options](edisc-search-export#export-search-results) to download all list attachments for SharePoint sites.

When searching for documents and files located in SharePoint or OneDrive for Business, it might make sense to adjust the query approach based on the metadata for the documents and files of interest. Files and documents have relevant properties like *Author*, *Created*, *CreatedBy*, *FileName*, *LastModifiedTime*, and *Title*. Most of these proprieties aren't relevant when searching for communications content in Exchange Online, and using these properties might lead to unexpected results if used across both documents and communications. Additionally, *FileName* and *Title* of a document might not be the same and using one or the other to try to find a file with specific content might lead to different or inaccurate results. Keep these properties in mind when searching for specific document and file content in SharePoint and OneDrive for Business.

For example, to find content related to documents created by User 1, for a project called *Tradewinds*, for specific files named *Financials*, and from January 2020 to January 2022, you might use a query with the following properties:

- Add User 1's OneDrive for Business site as a data sources to the case
- Select User 1's OneDrive for Business site as a collection location
- Add additional SharePoint site locations related to the project as collection locations
- For **FileName**, use *Financials*
- For **Keyword**, use *Tradewinds*
- For **Date Range**, use the *January 1, 2020* to *January 31, 2022* range

## Searchable site properties

The following table lists the SharePoint and OneDrive for Business properties that can be searched by using the eDiscovery search tools in the Microsoft Purview portal or by using the **New-ComplianceSearch** or the **Set-ComplianceSearch** cmdlet.

Important

While documents and files stored on SharePoint and OneDrive for Business might have other properties supported in other Microsoft 365 services, only the document and file properties listed in this table are supported in eDiscovery search tools. Attempting to include other document or file properties in searches isn't supported.

The table includes an example of the *property:value* syntax for each property and a description of the search results returned by the examples.

| Property | Property description | Example | Search results returned by the examples |
| --- | --- | --- | --- |
| Author | The author field from Office documents, which persists if a document is copied. For example, if a user creates a document and the emails it to someone else who then uploads it to SharePoint, the document will still retain the original author. Be sure to use the user's display name for this property. | `author:"Garth Fort"` | All documents that are authored by Garth Fort. |
| ContentType | The SharePoint content type of an item, such as Item, Document, or Video. | `contenttype:document` | All documents would be returned. |
| Created | The date that an item is created. | `created>=2021-06-01` | All items created on or after June 1, 2021. |
| CreatedBy | The person that created or uploaded an item. Be sure to use the user's display name for this property. | `createdby:"Garth Fort"` | All items created or uploaded by Garth Fort. |
| DetectedLanguage | The language of an item. | `detectedlanguage:english` | All items in English. |
| DocumentLink | The path (URL) of a specific folder on a SharePoint or OneDrive for Business site. If you use this property, be sure to search the site that the specified folder is located in. We recommend using this property instead of the *Site* and *Path* properties. <br> To return items located in subfolders of the folder that you specify for the documentlink property, you have to add /\* to the URL of the specified folder; for example, `documentlink: "https://contoso.sharepoint.com/Shared Documents/*"` | `documentlink:"https://contoso-my.sharepoint.com/personal/garthf_contoso_com/Documents/Private"`<br>`documentlink:"https://contoso-my.sharepoint.com/personal/garthf_contoso_com/Documents/Shared with Everyone/*" AND filename:confidential` | The first example returns all items in the specified OneDrive for Business folder. The second example returns documents in the specified site folder (and all subfolders) that contain the word "confidential" in the file name. |
| FileExtension | The extension of a file; for example, docx, one, pptx, or xlsx. | `fileextension:xlsx` | All Excel files (Excel 2007 and later) |
| FileName | The name of a file. | `filename:"marketing plan"`<br>`filename:estimate` | The first example returns files with the exact phrase "marketing plan" in the title. The second example returns files with the word "estimate" in the file name. |
| LastModifiedTime | The date that an item was last changed. | `lastmodifiedtime>=2021-05-01`<br>`lastmodifiedtime>=2021-05-01 AND lastmodifiedtime<=2021-06-01` | The first example returns items that were changed on or after May 1, 2021. The second example returns items changed between May 1, 2021 and June 1, 2021. |
| ModifiedBy | The person who last changed an item. Be sure to use the user's display name for this property. | `modifiedby:"Garth Fort"` | All items that were last changed by Garth Fort. |
| SharedWithUsersOWSUser | Documents that have been shared with the specified user and displayed on the **Shared with me** page in the user's OneDrive for Business site. These are documents that have been explicitly shared with the specified user by other people in your organization. When you export documents that match a search query that uses the SharedWithUsersOWSUser property, the documents are exported from the original content location of the person who shared the document with the specified user. For more information, see Searching for site content shared within your organization. | `sharedwithusersowsuser:garthf`<br>`sharedwithusersowsuser:"garthf@contoso.com"` | Both examples return all internal documents that have been explicitly shared with Garth Fort and that appear on the **Shared with me** page in Garth Fort's OneDrive for Business account. |
| Size | The size of an item, in bytes. | `size>=1`<br>`size:1..10000` | The first example returns items larger than 1 byte. The second example returns items from 1 through 10,000 bytes in size. |
| Title | The title of the document. The Title property is metadata that's specified in Microsoft Office documents. It's different from the file name of the document. | `title:"communication plan"` | Any document that contains the phrase "communication plan" in the Title metadata property of an Office document. |

## Searchable contact properties

The following table lists the contact properties that are indexed and that you can search for using eDiscovery search tools. These are the properties that are available for users to configure for the contacts (also called personal contacts) that are located in the personal address book of a user's mailbox. To search for contacts, you can select the mailboxes to search and then use one or more contact properties in the keyword query.

Tip

To search for values that contain spaces or special characters, use double quotation marks (" ") to contain the phrase; for example, `businessaddress:"123 Main Street"`.

| Property | Property description |
| --- | --- |
| BusinessAddress | The address in the **Business Address** property. The property is also called the **Work** address on the contact properties page. |
| BusinessPhone | The phone number in any of the **Business Phone** number properties. |
| CompanyName | The name in the **Company** property. |
| Department | The name in the **Department** property. |
| DisplayName | The display name of the contact. This is the name in the **Full Name** property of the contact. |
| EmailAddress | The address for any email address property for the contact. Users can add multiple email addresses for a contact. Using this property would return contacts that match any of the contact's email addresses. |
| FileAs | The **File as** property. This property is used to specify how the contact is listed in the user's contact list. For example, a contact could be listed as *FirstName,LastName* or *LastName,FirstName*. |
| GivenName | The name in the **First Name** property. |
| HomeAddress | The address in any of the **Home** address properties. |
| HomePhone | The phone number in any of the **Home** phone number properties. |
| IMAddress | The IM address property, which is typically an email address used for instant messaging. |
| MiddleName | The name in the **Middle** name property. |
| MobilePhone | The phone number in the **Mobile** phone number property. |
| Nickname | The name in the **Nickname** property. |
| OfficeLocation | The value in **Office** or **Office location** property. |
| OtherAddress | The value for the **Other** address property. |
| Surname | The name in the **Last** name property. |
| Title | The title in the **Job title** property. |

## Search operators

Boolean search operators, such as **AND**, **OR**, and **NOT**, help you define more-precise searches by including or excluding specific words in the search query. Other techniques, such as using property operators (such as `>=` or `..`), quotation marks, parentheses, and wildcards, help you refine a search query. The following table lists the operators that you can use to narrow or broaden search results.

| Operator | Usage | Description |
| --- | --- | --- |
| AND | keyword1 AND keyword2 | Returns items that include all of the specified keywords or `property:value` expressions. For example, `from:"Ann Beebe" AND subject:northwind` would return all messages sent by Ann Beebe that contained the word northwind in the subject line. ^2^ |
| + | keyword1 + keyword2 + keyword3 | Returns items that contain *either*`keyword2` or `keyword3`*and* that also contain `keyword1`. Therefore, this example is equivalent to the query `(keyword2 OR keyword3) AND keyword1`. <br> The query `keyword1 + keyword2` (with a space after the **+** symbol) isn't the same as using the **AND** operator. This query would be equivalent to `"keyword1 + keyword2"` and return items with the exact phase `"keyword1 + keyword2"`. |
| OR | keyword1 OR keyword2 | Returns items that include one or more of the specified keywords or `property:value` expressions. ^2^ |
| NOT | keyword1 NOT keyword2 <br> NOT from:"Ann Beebe" <br><br> NOT kind:im | Excludes items specified by a keyword or a `property:value` expression. In the second example excludes messages sent by Ann Beebe. The third example excludes any instant messaging conversations, such as Skype for Business conversations that are saved to the Conversation History mailbox folder. ^2^ |
| NEAR | keyword1 NEAR(n) keyword2 | Returns items with words that are near each other. In the *keyword1 NEAR(n) keyword2* syntax, *n* equals the number of words exclusive of *keyword1* and *keyword2*. For example, to identify instances where the term *best* is within 3 words of *worst* (example sentence, 'Best is opposite of worst.'), you would use **best NEAR(3) worst**. This returns any items where there are 3 or fewer words between *best* (keyword1) and *worst* (keyword2). If no number is specified, the default *n* value is 8. ^2^ |
| : | property:value | The colon (:) in the `property:value` syntax specifies that the value of the property being searched for contains the specified value. For example, `recipients:garthf@contoso.com` returns any message sent to garthf@contoso.com. |
| = | property=value | The same as the `:` operator. |
| &lt; | property&lt;value | Denotes that the property being searched is less than the specified value. ^1^ |
| &gt; | property&gt;value | Denotes that the property being searched is greater than the specified value.^1^ |
| &lt;= | property&lt;=value | Denotes that the property being searched is less than or equal to a specific value.^1^ |
| &gt;= | property&gt;=value | Denotes that the property being searched is greater than or equal to a specific value.^1^ |
| .. | property:value1..value2 | Denotes that the property being searched is greater than or equal to value1 and less than or equal to value2.^1^ |
| " " | "fair value" <br> subject:"Quarterly Financials" | In a keyword query (where you type the `property:value` pair in the **Keyword** box), use double quotation marks (" ") to search for an exact phrase or term. However, if you use the **Subject** or **Subject/Title**search condition condition, don't add double quotation marks to the value because quotation marks are automatically added when using these search conditions. If you do add quotation marks to the value, two pairs of double quotations are added to the condition value, and the search query will return an error. |
| \* | cat\* <br> subject:set\* | Prefix searches (also called *prefix matching*) where a wildcard character ( \* ) is placed at the end of a word in keywords or `property:value` queries. In prefix searches, the search returns results with terms that contain the word followed by zero or more characters. For example, `title:set*` returns documents that contain the word "set", "setup", and "setting" (and other words that start with "set") in the document title. <br>**Note:** You can use only prefix searches; for example, **cat\*** or **set\***. Suffix searches (**\*cat**), infix searches (**c\*t**), and substring searches (**\*cat\***) aren't supported. <br><br> Also, adding a period ( . ) to a prefix search changes the results that are returned. That's because a period is treated as a stop word. For example, searching for **cat\*** and searching for **cat.\*** will return different results. We recommend not using a period in a prefix search. |
| ( ) | (fair OR free) AND (from:contoso.com) <br> (IPO OR initial) AND (stock OR shares) <br><br> (quarterly financials) | Parentheses group together Boolean phrases, `property:value` items, and keywords. For example, `(quarterly financials)` returns items that contain the words quarterly and financials. |

Note

^1^ Use this operator for properties that have date or numeric values.^2^ Boolean search operators must be uppercase; for example, **AND**. If you use a lowercase operator, such as **and**, it is treated as a keyword in the search query.

## Search conditions

You can add conditions to a search query to narrow a search and return a more refined set of results. Each condition adds a clause to the KeyQL search query that is created and run when you start the search.

- Conditions for common properties
- Conditions for mail properties
- Conditions for document properties
- Operators used with conditions
- Guidelines for using conditions
- Examples of using conditions in search queries

### Conditions for common properties

Create a condition using common properties when searching mailboxes and sites in the same search. The following table lists the available properties to use when adding a condition.

| Condition | Description |
| --- | --- |
| Date | For email, the date a message was created or imported from a PST file. For documents, the date a document was last modified.  If you're searching for email messages for a specific time period, you should use the message *Received* and *Sent* conditions if you're unsure if the email messages might have been imported instead of natively created in Exchange. |
| Sender/Author | For email, the person who sent a message. For documents, the person cited in the author field from Office documents. You can type more than one name, separated by commas. Two or more values are logically connected by the **OR** operator.([See Recipient Expansion](ediscovery-keyword-queries-and-search-conditions#recipient-expansion)) |
| Size (in bytes) | For both email and documents, the size of the item (in bytes). |
| Subject/Title | For email, the text in the subject line of a message. For documents, the title of the document. As previously explained, the Title property is metadata specified in Microsoft Office documents. You can type the name of more than one subject/title values, separated by commas. Two or more values are logically connected by the **OR** operator. <br>**Note**: Don't include double quotation marks to the values for this condition because quotation marks are automatically added when using this search condition. If you add quotation marks to the value, two pairs of double quotations are added to the condition value, and the search query will return an error. |
| Retention label | For both email and documents, retention labels that can be automatically or manually applied to messages and documents. Retention labels can be used to declare records and help you manage the data lifecycle of content by enforcing retention and deletion rules specified by the label. You can type part of the retention label name and use a wildcard or type the complete label name. For more information about retention labels, see [Learn about retention policies and retention labels](retention). |

### Conditions for mail properties

Create a condition using mail properties when searching mailboxes or public folders in Exchange Online. The following table lists the email properties that you can use for a condition. These properties are a subset of the email properties that were previously described. These descriptions are repeated for your convenience.

| Condition | Description |
| --- | --- |
| Message kind | The message type to search. This is the same property as the Kind email property. Possible values: <br>- contacts<br>- docs<br>- email<br>- externaldata<br>- fax<br>- im<br>- journals<br>- meetings<br>- microsoftteams<br>- notes<br>- posts<br>- rssfeeds<br>- tasks<br>- voicemail |
| Participants | All the people fields in an email message. These fields are From, To, Cc, and Bcc. ([See Recipient Expansion](ediscovery-keyword-queries-and-search-conditions#recipient-expansion)) |
| Type | The message class property for an email item. This is the same property as the ItemClass email property. It's also a multi-value condition. So to select multiple message classes, hold the **CTRL** key and then select two or more message classes in the drop-down list that you want to add to the condition. Each message class that you select in the list is logically connected by the **OR** operator in the corresponding search query. <br> For a list of the message classes (and their corresponding message class ID) that are used by Exchange and that you can select in the **Message class** list, see [Item Types and Message Classes](/en-us/office/vba/outlook/Concepts/Forms/item-types-and-message-classes). |
| Received | The date that an email message was received by a recipient. This is the same property as the Received email property. |
| Recipients | All recipient fields in an email message. These fields are To, Cc, and Bcc. ([See Recipient Expansion](ediscovery-keyword-queries-and-search-conditions#recipient-expansion)) |
| Sent | The date that an email message was sent by the sender. This is the same property as the Sent email property. |
| Subject | The text in the subject line of an email message. <br>**Note**: Don't include double quotation marks to the values for this condition because quotation marks are automatically added when using this search condition. If you add quotation marks to the value, two pairs of double quotations are added to the condition value, and the search query will return an error. |
| To | The recipient of an email message in the To field. |

### Conditions for document properties

Create a condition using document properties when searching for documents on SharePoint and OneDrive for Business sites. The following table lists the document properties that you can use for a condition. These properties are a subset of the site properties that were previously described. These descriptions are repeated for your convenience.

| Condition | Description |
| --- | --- |
| Author | The author field from Office documents, which persists if a document is copied. For example, if a user creates a document and the emails it to someone else who then uploads it to SharePoint, the document will still retain the original author. |
| Title | The title of the document. The Title property is metadata that's specified in Office documents. It's different than the file name of the document. |
| Created | The date that a document is created. |
| Last modified | The date that a document was last changed. |
| File type | The extension of a file; for example, docx, one, pptx, or xlsx. This is the same property as the FileExtension site property. <br>**Note:** If you include a File type condition using the **Equals** or **Equals any of** operator in a search query, you can't use a prefix search (by including the wildcard character ( \* ) at the end of the file type) to return all versions of a file type. If you do, the wildcard is ignored. For example if you include the condition `Equals any of doc*`, only files with an extension of `.doc` are returned. Files with an extension of `.docx` won’t be returned. To return all versions of a file type, used the *property:value* pair in a keyword query; for example, `filetype:doc*`. |

### Operators used with conditions

When you add a condition, you can select an operator that is relevant to type of property for the condition. The following table describes the operators that are used with conditions and lists the equivalent that is used in the search query.

| Operator | Query equivalent | Description |
| --- | --- | --- |
| After | `property>date` | Used with date conditions. Returns items that were sent, received, or modified after the specified date. |
| Before | `property<date` | Used with date conditions. Returns items that were sent, received, or modified before the specified date. |
| Between | `date..date` | Use with date and size conditions. When used with a date condition, returns items there were sent, received, or modified within the specified date range. When used with a size condition, returns items whose size is within the specified range. |
| Contains any of | `(property:value) OR (property:value)` | Used with conditions for properties that specify a string value. Returns items that contain any part of one or more specified string values. |
| Doesn't contain any of | `-property:value`<br>`NOT property:value` | Used with conditions for properties that specify a string value. Returns items that don't contain any part of the specified string value. |
| Doesn't equal any of | `-property=value`<br>`NOT property=value` | Used with conditions for properties that specify a string value. Returns items that don't contain the specific string. |
| Equals | `size=value` | Returns items that are equal to the specified size.^1^ |
| Equals any of | `(property=value) OR (property=value)` | Used with conditions for properties that specify a string value. Returns items that are a match of one or more specified string values. |
| Greater | `size>value` | Returns items where the specified property is greater than the specified value.^1^ |
| Greater or equal | `size>=value` | Returns items where the specified property is greater than or equal to the specified value.^1^ |
| Less | `size<value` | Returns items that are greater than or equal to the specific value.^1^ |
| Less or equal | `size<=value` | Returns items that are greater than or equal to the specific value.^1^ |
| Not equal | `size<>value` | Returns items that don't equal the specified size.^1^ |

Note

^1^ This operator is available only for conditions that use the Size property.

### Guidelines for using conditions

Keep the following in mind when using search conditions.

- A condition is logically connected to the keyword query (specified in the keyword box) by the **AND** operator. That means that items have to satisfy both the keyword query and the condition to be included in the results. This is how conditions help to narrow your results.
- If you add two or more unique conditions to a search query (conditions that specify different properties), those conditions are logically connected by the **AND** operator. That means only items that satisfy all the conditions (in addition to any keyword query) are returned.
- If you add more than one condition for the same property, those conditions are logically connected by the **OR** operator. That means items that satisfy the keyword query and any one of the conditions are returned. So, groups of the same conditions are connected to each other by the **OR** operator and then sets of unique conditions are connected by the **AND** operator.
- If you add multiple values (separated by commas or semi-colons) to a single condition, those values are connected by the **OR** operator. That means items are returned if they contain any of the specified values for the property in the condition.
- Any condition that uses an operator with **Contains** and **Equals** logic will return similar search results for simple string searches. A simple string search is a string in the condition that doesn't include a wildcard). For example, a condition that uses **Equals any of** will return the same items as a condition that uses **Contains any of**.
- The search query that is created by using the keywords box and conditions is displayed on the **Search** page, in the details pane for the selected search. In a query, everything to the right of the notation `(c:c)` indicates conditions that are added to the query. `(c:c)` shouldn't be used in manually entered queries and isn't equal to **AND** or **OR**.
- Conditions only add properties to the search query; they don't add operators. This is why the query displayed in the detail pane doesn't show operators to the right of the `(c:c)` notation. KeyQL adds the logical operators (according to the previously explained rules) when the executing the query.
- You can use the drag and drop control to resequence the order of conditions. Select the control for a condition and move it up or down.
- As previously explained, some condition properties allow you to type multiple values (separated by semi-colons). Each value is logically connected by the **OR** operator, and results in the query `(filetype=docx) OR (filetype=pptx) OR (filetype=xlsx)`. The following illustration shows an example of a condition with multiple values.

    ![One condition with multiple values.](media/searchconditions1.png)

    Note

    You can't add multiple conditions (by selecting **Add condition** for the same property). Instead, you have to provide multiple values for the condition (separated by semi-colons), as shown in the previous example.

### Examples of using conditions in search queries

The following examples show the GUI-based version of a search query with conditions, the search query syntax that is displayed in the details pane of the selected search (which is also returned by the **Get-ComplianceSearch** cmdlet), and the logic of the corresponding KeyQL query.

#### Example 1

This example returns email items or documents that contain the keyword "report", that were sent or created before April 1, 2021, and that contain the word "northwind" in the subject field of email messages or in the title property of documents. The query excludes Web pages that meet the other search criteria.

**GUI**:

![Second example of search conditions.](media/searchconditions3.png)

**Search query syntax**:

`report(c:c)(date<2021-04-01)(subjecttitle:"northwind")(-filetype:aspx)`

**Search query logic**:

`report AND (date<2021-04-01) AND (subjecttitle:"northwind") NOT (filetype:aspx)`

#### Example 2

This example returns email messages or calendar meetings that were sent between December 1, 2019 and November 30, 2020 and that contain words that start with "phone" or "smartphone".

**GUI**:

![Third example of search conditions.](media/searchconditions4.png)

**Search query syntax**:

`phone* OR smartphone*(c:c)(sent=2019-12-01..2020-11-30)(kind="email")(kind="meetings")`

**Search query logic**:

`phone* OR smartphone* AND (sent=2019-12-01..2020-11-30) AND ((kind="email") OR (kind="meetings"))`

## Special characters

Some special characters aren't included in the search index and therefore aren't searchable. This also includes the special characters that represent search operators in the search query. Here's a list of special characters that are either replaced by a blank space in the actual search query or cause a search error.

`+ - = : ! @ # % ^ & ; _ / ? ( ) [ ] { }`

## Searchable sensitive data types

You can use eDiscovery search tools in the Microsoft Purview portal to search for sensitive data, such as credit card numbers or social security numbers, that is stored in documents on SharePoint and OneDrive for Business sites. You can do this by using the `SensitiveType` property and the name (or ID) of a sensitive information type in a keyword query. For example, the query `SensitiveType:"Credit Card Number"` returns documents that contain a credit card number. The query `SensitiveType:"U.S. Social Security Number (SSN)"` returns documents that contain a U.S. social security number.

To see a list of the sensitive information types that you can search for, go to **Data classifications** &gt; **Sensitive info types** in the Microsoft Purview portal. Or you can use the **Get-DlpSensitiveInformationType** cmdlet in Security & Compliance PowerShell to display a list of sensitive information types.

### Limitations for searching sensitive data types

- To search for custom sensitive information types, you have to specify the ID of the sensitive information type in the `SensitiveType` property. Using the name of a custom sensitive information type (as shown in the example for built-in sensitive information types in the previous section) will return no results. Use the **Publisher** column on the **Sensitive info types** page in the Microsoft Purview portal (or the **Publisher** property in PowerShell) to differentiate between built-in and custom sensitive information types. Built-in sensitive data types have a value of `Microsoft Corporation` for the **Publisher** property.

    To display the name and ID for the custom sensitive data types in your organization, run the following command in Security & Compliance PowerShell:

    ```powershell
    Get-DlpSensitiveInformationType | Where-Object {$_.Publisher -ne "Microsoft Corporation"} | FT Name,Id
    ```

    Then you can use the ID in the `SensitiveType` search property to return documents that contain the custom sensitive data type; for example, `SensitiveType:7e13277e-6b04-3b68-94ed-1aeb9d47de37`
- You can't use sensitive information types and the `SensitiveType` search property to search for sensitive data at-rest in Exchange Online mailboxes. This includes 1:1 chat messages, 1:N group chat messages, and team channel conversations in Microsoft Teams because all of this content is stored in mailboxes. However, you can use data loss prevention (DLP) policies to protect sensitive email data in transit. For more information, see [Learn about data loss prevention](dlp-learn-about-dlp) and [Search for and find personal data](/en-us/compliance/regulatory/gdpr).

## Searching for site content shared with external users

You can also use eDiscovery search tools in the Microsoft Purview portal to search for documents stored on SharePoint and OneDrive for Business sites that have been shared with people outside of your organization. This can help you identify sensitive or proprietary information that's being shared outside your organization. You can do this by using the `ViewableByExternalUsers` property in a keyword query. This property returns documents or sites that have been shared with external users by using one of the following sharing methods:

- A sharing invitation that requires users to sign in to your organization as an authenticated user.
- An anonymous guest link, which allows anyone with this link to access the resource without having to be authenticated.

Here are some examples:

- The query `ViewableByExternalUsers:true AND SensitiveType:"Credit Card Number"` returns all items that have been shared with people outside your organization and contain a credit card number.
- The query `ViewableByExternalUsers:true AND ContentType:document AND site:"https://contoso.sharepoint.com/Sites/Teams"` returns a list of documents on all team sites in the organization that have been shared with external users.

Tip

A search query such as `ViewableByExternalUsers:true AND ContentType:document` might return numerous .aspx files in the search results. To eliminate these (or other types of files), you can use the `FileExtension` property to exclude specific file types; for example `ViewableByExternalUsers:true AND ContentType:document NOT FileExtension:aspx`.

What is considered content that is shared with people outside your organization? Documents in your organization's SharePoint and OneDrive for Business sites that are shared by sending a sharing invitation or that are shared in public locations. For example, the following user activities result in content that is viewable by external users:

- A user shares a file or folder with a person outside your organization.
- A user creates and sends a link to a shared file to a person outside your organization. This link allows the external user to view (or edit) the file.
- A user sends a sharing invitation or a guest link to a person outside your organization to view (or edit) a shared file.

### Issues using the ViewableByExternalUsers property

While the `ViewableByExternalUsers` property represents the status of whether a document or site is shared with external users, there are some caveats to what this property does and doesn't reflect. In the following scenarios, the value of the `ViewableByExternalUsers` property won't be updated, and the results of a search query that uses this property might be inaccurate.

- Changes to sharing policy, such as turning off external sharing for a site or for the organization. The property will still show previously shared documents as being externally accessible even though external access might have been revoked.
- Changes to group membership, such as adding or removing external users to Microsoft 365 Groups or Microsoft 365 security groups. The property won't automatically be updated for items the group has access to.
- Sending sharing invitations to external users where the recipient hasn't accepted the invitation, and therefore doesn't yet have access to the content.

In these scenarios, the `ViewableByExternalUsers` property won't reflect the current sharing status until the site or document library is recrawled and reindexed.

## Searching for site content shared within your organization

As previously explained, you can use the `SharedWithUsersOWSUser` property so search for documents that have been shared between people in your organization. When a person shares a file (or folder) with another user inside your organization, a link to the shared file appears on the **Shared with me** page in the OneDrive for Business account of the person who the file was shared with. For example, to search for the documents that have been shared with Sara Davis, you can use the query `SharedWithUsersOWSUser:"sarad@contoso.com"`. If you export the results of this search, the original documents (located in the content location of the person who shared the documents with Sara) are downloaded.

Documents must be explicitly shared with a specific user to be returned in search results when using the `SharedWithUsersOWSUser` property. For example, when a person shares a document in their OneDrive account, they have the option to share it with anyone (inside or outside the organization), share it only with people inside the organization, or share it with a specific person. Here's a screenshot of the **Share** window in OneDrive that shows the three sharing options.

![Only files shared with specific people are returned by a search query that uses the SharedWithUsersOWSUser property.](media/469a4b61-68bd-4ab0-b612-ab6302973886.png)

Only documents that are shared by using the third option (shared with **Specific people**) are returned by a search query that uses the `SharedWithUsersOWSUser` property.

## Searching for Skype for Business conversations

You can use the following keyword query to specifically search for content in Skype for Business conversations:

```powershell
kind:im
```

The previous search query also returns chats from Microsoft Teams. To prevent this, you can narrow the search results to include only Skype for Business conversations by using the following keyword query:

```powershell
kind:im AND subject:conversation
```

The previous keyword query excludes chats in Microsoft Teams because Skype for Business conversations are saved as email messages with a Subject line that starts with the word "Conversation".

To search for Skype for Business conversations that occurred within a specific date range, use the following keyword query:

```powershell
kind:im AND subject:conversation AND (received=startdate..enddate)
```

## Character limits for searches

There's a 4,000 character limit for search queries when searching for content in SharePoint sites and OneDrive accounts. Here's how the total number of characters in the search query are calculated:

- The characters in keyword search query (including both user and filter fields) count against this limit.
- The characters in any location property (such as the URLs for all the SharePoint sites or OneDrive locations being searched) count against this limit.
- The characters in all the search permissions filters that are applied to the user running the search count against the limit.

Note

The 4,000 character limit applies to Content search, eDiscovery (Standard), and eDiscovery (Premium).