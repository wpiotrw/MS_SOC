---
layout: Conceptual
title: Document metadata fields in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-document-metadata-fields
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article defines the metadata fields for documents in a review set in a case in Microsoft Purview eDiscovery (Premium).
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
locale: en-us
document_id: a18373d7-7544-a944-9916-69458ce76a55
document_version_independent_id: a18373d7-7544-a944-9916-69458ce76a55
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-document-metadata-fields.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-document-metadata-fields
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-document-metadata-fields.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: abb73757-c929-27c5-b2be-7ee4defcc89b
---

# Document metadata fields in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

The following table lists the metadata fields for documents in a review set in a case in Microsoft Purview eDiscovery (Premium). For more information about searchable properties when searching Microsoft 365 content locations when you're collecting data for an eDiscovery (Premium) case, see [Keyword queries and search conditions for Content Search](ediscovery-keyword-queries-and-search-conditions).

This table provides the following information:

- **Field name** and **Display field name:** The name of the metadata field and the name of the field that's displayed when viewing the file metadata of a selected document in a review set. Some metadata fields aren't included when viewing the file metadata of a document. These fields are highlighted with an asterisk (\*).
- **Searchable field name:** The name of the property that you can search for when running a [review set query](ediscovery-review-set-search).
- **Exported field name:** The name of the metadata field that included when documents are exported.
- **Description:** A description of the metadata field.

Note

The **Keywords** field in [review set search](ediscovery-review-set-search) uses Keyword Query Language (KeyQL). The fields listed in the **Searchable field name** column can be used in the **Keywords** field in a review set search to form complex queries without you having to use the query builder. For more information about KeyQL, see [Keyword Query Language syntax reference](/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference).

| **Field name and Display field name** | **Searchable field name** | **Exported field name** | **Description** |
| --- | --- | --- | --- |
| Attachment Content ID | AttachmentContentId | *Not exported* | Attachment content ID of the item. |
| Attorney client privilege score | AttorneyClientPrivilegeScore | *Not exported* | Attorney-client privilege model content score. |
| Author | Author | Doc\_authors | Author from the document metadata. |
| BCC | Bcc | Email\_bcc | Bcc field for message types. The format is *DisplayName &lt;SMTPAddress&gt;*. |
| CC | Cc | Email\_cc | Cc field for message types. The format is *DisplayName &lt;SMTPAddress&gt;*. |
| Channel Name | Channel | ChannelName | This field is the Teams channel name. Only applies to Microsoft Teams content. |
| Compliance labels | ComplianceLabels | Compliance\_labels | [Retention labels](retention) applied to content in Office 365. |
| Compound Path | CompoundPath | Compound\_path | Human readable path that describes the source of the item. |
| Content\* | Content | *Not exported* | Extracted text of the item. |
| Conversation Body | ConversationBody | *Not exported* | Conversation body of the item. |
| Conversation ID | ConversationId | Conversation\_ID | Conversation ID from the message. For Teams 1:1 and group chats, all transcript files and their family items within the same conversation share the same Conversation ID. For more information, see [eDiscovery (Premium) workflow for content in Microsoft Teams](ediscovery-teams-workflow). |
| Conversation Family ID | ConversationFamilyID | ConversationFamilyID | The ID that identifies individual elements of a conversation and the related items in the conversation. |
| Conversation Index | *Not searchable* | Conversation\_index | Conversation index from the message. |
| Conversation Name | *Not searchable* | ConversationName | This field depends on content type.**Teams 1:1 chat:** first 40 characters of first message.**Teams 1:N chat:** Name of group chat; if not available, the first 40 characters of the first message.**Teams Channel Post:** Post title or announcement subhead; if not available, the first 40 characters of the first message. |
| Conversation Pdf Time | ConversationPdfTime | *Not exported* | Date when the PDF version of the conversation was created. |
| Conversation Redaction Burn Time | ConversationRedactionBurnTime | *Not exported* | Date when the PDF version of the conversation was created for Chat. |
| Conversation Topic | ConversationTopic | *Not exported* | Conversation topic of the item. |
| Conversation Type | ConversationType | ConversationType | The type of chat conversation. Values are: **Teams 1:1 and group chats and all Viva Engage conversations:** Group**Teams channels and private channels:** Channel |
| Contains Deleted Message | ContainsDeletedMessage | ContainsDeletedMessage | Indicates if the chat transcript includes a deleted message |
| Contains Edited Message | ContainsEditedMessage | ContainsEditedMessage | Indicates if the chat transcript includes an edited message |
| Teams Announcement Title | TeamsAnnouncementTitle | TeamsAnnouncementTitle | Title from a [teams announcement](https://support.microsoft.com/office/send-an-announcement-to-a-channel-8f244ea6-235a-4dcc-9143-9c5b801b4992). |
| *N/A* | *N/A* | Converted\_file\_path | The path of the converted export file. For internal Microsoft use only. |
| Custodian | Custodian | Custodian | Name of the custodian the item was associated with. |
| Date | Date | Date | Date is a computed field that depends on the file type.<br>**Email**: Sent date**Email attachments**: Last modified date of the document; if not available, the parent's sent date**Embedded documents**: Last modified date of the document; if not available, the parent's last modified date**SPO documents (includes modern attachments)**: Last modified date of the document; if not available, SharePoint last modified date**Non-Office 365 documents**: Last modified date**Meetings**: Meeting start date**VoiceMail**: Sent date**IM**: Sent date**Teams**: Sent date |
| Document comments | DocComments | Doc\_comments | Comments from the document metadata. |
| Document company | *Not searchable* | Doc\_company | Company from the document metadata. |
| Document date created | CreatedTime | Doc\_date\_created | Create date from document metadata. |
| DocIndex\* | *Not searchable* | *Not exported* | The index in the family. *-1* or *0* means it's the root. |
| Document keywords | *Not searchable* | Doc\_keywords | Keywords from the document metadata. |
| Document modified by | *Not searchable* | Doc\_modified\_by | The user who last modified the document from document metadata. |
| Document revision | Doc\_Version | Doc\_Version | Revision from the document metadata. |
| Document subject | *Not searchable* | Doc\_subject | Subject from the document metadata. |
| Document template | *Not searchable* | Doc\_template | Template from the document metadata. |
| DocLastSavedBy | *Not searchable* | Doc\_last\_saved\_by | The name of the user who last saved the document. |
| Dominant theme | DominantTheme | Dominant\_theme | Dominant theme as calculated for analytics. |
| Duplicate subset | *Not searchable* | Duplicate\_subset | Group ID for exact duplicates. |
| EmailAction\* | *Not searchable* | Email\_action | Values are *None*, *Reply*, or *Forward*; based on the subject line of a message. |
| Email Delivery Receipt Requested | *Not searchable* | Email\_delivery\_receipt | Email address supplied in Internet Headers for delivery receipt. |
| Importance | EmailImportance | Email\_importance | Importance of the message: *0* - Low; *1* - Normal; *2* - High |
| Ignored processing errors | ErrorIgnored | Error\_Ignored | Error was ignored and not remediated. |
| EmailInternetHeaders | EmailInternetHeaders | Email\_internet\_headers | The full set of email headers from the email message |
| EmailLevel\* | *Not searchable* | Email\_level | Indicates a message's level within the email thread it belongs to; attachments inherit its parent message's value. |
| Email Message ID | *Not searchable* | Email\_message\_ID | Internet message ID from the message. |
| EmailReadReceiptRequested | *Not searchable* | Email\_read\_receipt | Email address supplied in Internet Headers for read receipt. |
| Email Security | EmailSecurity | Email\_security | Security setting of the message: *0* - None; *1* - Signed; *2* - Encrypted; *3* - Encrypted and signed. |
| Email Sensitivity | EmailSensitivity | email\_sensitivity | Sensitivity setting of the message: *0* - None; *1* Personal; *2* - Private; *3* - CompanyConfidential. |
| Email set | EmailSet | Email\_set | Group ID for all messages in the same email set. |
| EmailThread\* | *Not searchable* | Email\_thread | Position of the message within the email set; consists of node IDs from the root to the current message and are separated by periods (.). |
| *N/A* | *N/A* | Export\_native\_path | The path of the exported file. |
| Extracted content type | *Not searchable* | Native\_type | Extracted content type, in the form of mime type; for example, *image/jpeg* |
| *N/A* | *N/A* | Extracted\_text\_path | The path to the extracted text file in the export. |
| ExtractedTextLength\* | *Not searchable* | Extracted\_text\_length | Number of characters in the extracted text. |
| FamilyDuplicateSet\* | *Not searchable* | Family\_duplicate\_set | Numeric identifier for families that are exact duplicates of each other (same content and all the same attachments). |
| Family ID | FamilyId | Family\_ID | Groups together attachments and extracted items from email and chats with its parent item. This includes the chat or email and all attachments and extracted items. |
| Family Size | *Not searchable* | Family\_size | Number of documents in the family. |
| File class | FileClass | File\_class | For content from SharePoint and OneDrive: *Document*. For content from Exchange: *Email* or *Attachment*. For content from Teams or Viva Engage: *Conversations*. |
| File ID | FileId | File\_ID | Document identifier unique within the case. |
| File system date created | *Not searchable* | File\_system\_date\_created | Created date from file system (only applies to non-Office 365 data). |
| File system date modified | *Not searchable* | File\_system\_date\_modified | Modified date from file system (only applies to non-Office 365 data). |
| File Type | FileType | *Not exported* | File type of the item based on file extension. |
| Group ID | GroupId | Group\_ID | Groups together all items for email and documents. For email, this includes the message and all attachments and extracted items. For documents, this includes the document and any embedded items. |
| Has attachment | EmailHasAttachment | Email\_has\_attachment | Indicates whether or not the message has attachments. |
| Has attorney | HasAttorney | *Not exported* | *True* when at least one of the participants is found in the attorney list; otherwise, the value is *False*. |
| HasText\* | *Not searchable* | Has\_text | Indicates whether or not the item has text; possible values are *True* and *False*. |
| Immutable ID | *Not searchable* | Immutable\_ID | This ID is used to uniquely identify a document within a review set. This field can't be used in a review set search and the ID can't be used to access a document in its native location. |
| Inclusive type | InclusiveType | Inclusive\_type | Inclusive type calculated for analytics: *0* - not inclusive; *1* - inclusive; *2* - inclusive minus; *3* - inclusive copy. |
| In Reply To ID | *Not searchable* | In\_reply\_to\_ID | In reply to ID from the message. |
| InputFileExtension | *Not searchable* | Original\_file\_extension | The original file extension of the file. |
| InputFileID | *Not searchable* | Input\_file\_ID | The file ID of the top level item in the review set. For an attachment, this ID will be the ID of the parent. This can be used to group families together. |
| Is modern attachment | IsModernAttachment | *Not exported* | This file is a modern attachment or linked file. |
| Is from document version | IsFromDocumentVersion | *Not exported* | Current document is from a different version of another document. |
| Is email attachment | IsEmailAttachment | *Not exported* | This item is from an email attachment that shows up as an attached item to the message. |
| Is inline attachment | IsInlineAttachment | *Not exported* | This was attached inline and shows up in the body of the message. |
| Is Representative | IsRepresentative | Is\_representative | One document in every set of exact duplicates is marked as representative. |
| Item class | ItemClass | Item\_class | Item class supplied by exchange server; for example, *IPM.Note* |
| Last modified date | LastModifiedDate | Doc\_date\_modified | Last modified date from document metadata. |
| Load ID | LoadId | Load\_ID | The ID of the load set in which the item was added to a review set. |
| Location | Location | Location | String that indicates the type of location that documents were sourced from.<br>**Imported Data** - Non-Office 365 data**Teams** - Microsoft Teams**Exchange** - Exchange mailboxes**SharePoint** - SharePoint sites**OneDrive** - OneDrive accounts |
| Location name | LocationName | Location\_name | String that identifies the source of the item. For exchange, this will be the SMTP address of the mailbox; for SharePoint and OneDrive, the URL for the site collection. |
| *N/A* | *N/A* | Marked\_as\_pivot | This file is the pivot in a near duplicate set. |
| Marked as representative | MarkAsRepresentative | *Not exported* | One document from each set of exact duplicates is marked as representatives. |
| Meeting End Date | MeetingEndDate | Meeting\_end\_date | Meeting end date for meetings. |
| Meeting Start Date | MeetingStartDate | Meeting\_start\_date | Meeting start date for meetings. |
| Message kind | MessageKind | Message\_kind | The type of message to search for. Possible values: * contacts docs email externaldata faxes im journals meetings microsoftteams * (returns items from chats, meetings, and calls in Microsoft Teams) *notes posts rssfeeds tasks voicemail* |
| Modern Attachment Parent ID | *Not searchable* | ModernAttachment\_ParentId | The Immutable ID of the document's parent. |
| Native Extension | NativeExtension | Native\_extension | Native extension of the item. |
| Native file name | NativeFileName | Native\_file\_name | Native file name of the item. |
| Native file size | Size | Native\_size | Number of bytes of the native item. |
| NativeMD5 | *Not searchable* | Native\_MD5 | MD5 hash (128-bit hash value) of the file stream. |
| NativeSHA256 | *Not searchable* | Native\_SHA\_256 | SHA256 hash (256-bit hash value) of the file stream. |
| ND/ET Sort: Excluding attachments | NdEtSortExclAttach | ND\_ET\_sort\_excl\_attach | Concatenation of the email thread (ET) set and Near-duplicate (ND) set. This field is used for efficient sorting at review time. A *D* is prefixed to ND sets and an *E* is prefixed to ET sets. |
| ND/ET Sort: Including attachments | NdEtSortInclAttach | ND\_ET\_sort\_incl\_attach | Concatenation of an email thread (ET) set and near-duplicate (ND) set. This field is used for efficient sorting at review time. A *D* is prefixed to ND sets and an *E* is prefixed to ET sets. Each email item in an ET set is followed by its appropriate attachments. |
| Near Duplicate Set | *Not searchable* | ND\_set | Items that are similar to the pivot document share the same ND\_set. |
| O365 authors | *Not searchable* | O365\_authors | Author from SharePoint. |
| O365 created by | *Not searchable* | O365\_created\_by | Created by from SharePoint. |
| O365 date created | *Not searchable* | O365\_date\_created | Created date from SharePoint. |
| O365ModifiedDate | *Not searchable* | O365\_date\_modified | The date a document (or document version) collected from SharePoint or OneDrive for Business was modified. This is the same modified date as the one displayed in the version history in the SharePoint and OneDrive user experience. |
| O365 modified by | *Not searchable* | O365\_modified\_by | Modified by from SharePoint or OneDrive. |
| Other custodians | DedupedCustodians | Deduped\_custodians | List of custodians of documents that are exact duplicates (for email, based on content; for documents, based on hash). |
| Other file IDs | DedupedFileIds | Deduped\_file\_IDs | List of file IDs of documents that are exact duplicates (for email, based on content; for documents, based on hash). |
| Other paths | Dedupedcompoundpath | Deduped\_compound\_path | List of compound paths of documents that are exact duplicates (email: based on content, documents: based on hash). |
| Parent ID | ParentId | Parent\_ID | ID of the item's parent. |
| ParentNode | *Not searchable* | Parent\_node | The closest preceding email message in the email thread. |
| Participant domains | ParticipantDomains | Email\_participant\_domains | List of all domains of participants of a message. |
| Participants | Participants | Email\_participants | List of all participants of a message; for example, *Sender*, *To*, *Cc*, *Bcc*. |
| Pivot ID | PivotId | Pivot\_ID | The ID of a pivot. |
| Potentially privileged | PotentiallyPrivileged | Potentially\_privileged | True if attorney-client privilege detection model considers the document potentially privileged |
| Processing status | ProcessingStatus | Error\_code | Processing status after the item was added to a review set. |
| Read percentile | ReadPercentile | *Not exported* | Read percentile for the document based on Relevance. |
| Received | Received | Email\_date\_received | The date and time the email was received in UTC. |
| Recipient Count | *Not searchable* | Recipient\_count | Number of recipients in the message. |
| Recipient domains | RecipientDomains | Email\_recipient\_domains | List of all domains of recipients of a message. |
| Recipients | Recipients | Email\_recipients | List of all recipients of a message (To, Cc, Bcc). |
| *N/A* | *N/A* | Redacted\_file\_path | The path of the redacted replacement file in the export. |
| *N/A* | *N/A* | Redacted\_text\_path | The path of the redacted text file replacement in the export. For internal Microsoft use only. |
| Relevance tag Case issue 1 | *Not searchable* | Relevance\_tag\_case\_issue\_1 | Relevance tag Case issue 1 from Relevance. |
| Relevance score | RelevanceScore | *Not exported* | Relevance score of a document based on Relevance. |
| Relevance tag | RelevanceTag | *Not exported* | Relevance score of a document based on Relevance. |
| Representative ID | RepresentativeId | *Not exported* | Numeric identifier of each set of exact duplicates. |
| *N/A* | *N/A* | Row\_number | The row number of the item in the load file. |
| Sender | Sender | Email\_sender | Sender (From) field for message types. The format is *DisplayName &lt;SmtpAddress&gt;*. |
| Sender/Author | SenderAuthor | *Not exported* | Calculated field comprised of the sender or author of the item. |
| Sender domain | SenderDomain | Email\_sender\_domain | Domain of the sender. |
| Sent | Sent | Email\_date\_sent | Sent date of the message.Chats: Beginning date from the transcript |
| Set ID | *Not searchable* | Set\_ID | Documents of similar content (ND\_set) or email within the same email thread (Email\_set) share the same Set\_ID. |
| Set Order: Inclusive First | SetOrderInclusivesFirst | Set\_order\_inclusives\_first | Sorting field - email and attachments: counter-chronological; documents: pivot first then by descending similarity score. |
| SimilarityPercent | *Not searchable* | Similarity\_percent | Indicates how similar a document is to the pivot of the near duplicate set. |
| Subject | Subject | Email\_subject | Subject of the message. |
| Subject/Title | SubjectTitle | *Not searchable* | Calculated field comprised of the subject or title of the item. |
| Tags | Tags | Tags | Tags applied in a review set. |
| Team Name | TeamName | TeamName | **Teams:** Name of team**Viva Engage:** Community name |
| Themes list | ThemesList | Themes\_list | Themes list as calculated for analytics. |
| Thread ID | ThreadId | Thread\_ID | The Thread ID from email messages, Teams conversations, and Viva Engage conversations. For email messages, all reply messages and attachments share the same Thread ID. For Teams 1:1 and group chats, all transcript files and their associated items within the same conversation share the same Thread ID. For more information, see [View documents in a review set](ediscovery-view-documents-in-review-set#grouping). |
| Title | Title | Doc\_title | Title from the document metadata. Title from the document metadata. For Teams and Viva Engage content, this is the value from the ConversationName property. |
| To | To | Email\_to | To field for message types. The format is *DisplayName&lt;SmtpAddress&gt;* |
| Unique in email set | UniqueInEmailSet | *Not exported* | *False* if there's a duplicate of the attachment in its email set. |
| Version Group ID | *Not searchable* | Version\_Group\_Id | Groups together the different versions of the same document. |
| VersionNumber | *Not searchable* | Version\_Number | The version number of a document collected from SharePoint or OneDrive for Business. This is the same version number as the one displayed in the version history in the SharePoint and OneDrive user experience. |
| Was Remediated | WasRemediated | Was\_Remediated | *True* if the item was remediated, otherwise *False*. |
| Word count | WordCount | Word\_count | Number of words in the item. |
|  |  |  |  |