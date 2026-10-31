---
layout: Conceptual
title: Document metadata fields in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-ref-document-metadata-fields
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article defines the metadata fields for documents in Microsoft Purview eDiscovery.
f1.keywords:
- NOCSH
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
ai-usage: ai-assisted
locale: en-us
document_id: 91d686f9-8a92-1720-c311-cefd0c0e49af
document_version_independent_id: 91d686f9-8a92-1720-c311-cefd0c0e49af
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-ref-document-metadata-fields.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-ref-document-metadata-fields
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-ref-document-metadata-fields.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 580f1212-7980-68bd-b2e1-a166ae10df7b
---

# Document metadata fields in eDiscovery | Microsoft Learn

The following table lists the metadata fields for documents in [Microsoft Purview eDiscovery](edisc). For more information about searchable properties when searching Microsoft 365 content locations when you're collecting data for an eDiscovery case, see [Create a search query for a case in eDiscovery](edisc-search-query).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

This table provides the following information:

- **Field name**: The name of the metadata field included in the `items.csv` report. Some metadata field values don't appear until analytics runs in the review set. These fields are highlighted with an asterisk (\*).
- **Description**: A description of the metadata field.
- **Direct export**: If the metadata field value is populated for direct exports from search.
- **Add to review set**: If the metadata field value is populated when adding search results to a review set.
- **Review set export**: If the metadata field value is populated when exporting items from a review set.

Note

When you [export search](edisc-search-export) results by using the **report only** option (without including content), some metadata fields might not be fully populated. Report-only exports rely on indexed properties, which might not reflect the most current or complete metadata for all items. To ensure all metadata fields are accurately populated, export search results **with content**. Export with data fully inspects each item and returns complete metadata values as documented in the following table.

| Field name | Description | Direct export | Add to review set | Review set export |
| --- | --- | --- | --- | --- |
| Added by | Indicates how the item was included in this process, whether it was a match from *IndexQuery*, *AdvancedIndexed*, or *PartiallyIndexed*. | Yes | Yes | Yes |
| All custodians | Union of the `Custodian` and the `Deduped custodians` fields. | No | Yes | Yes |
| Attachment names | List of attachment names of the email item. | No | Yes | Yes |
| Author | Author from the document metadata. | Yes | Yes | Yes |
| BCC | Bcc field for message types. The format is `DisplayName <SMTPAddress>`. This field is only available when the email is collected from the sender mailbox. | Yes | Yes | Yes |
| BCC expanded | The value in Bcc field of an email expanded. This field is only available when the email is collected from the sender mailbox. For example, if Bcc is a distribution list, this field shows the Bcc and all of its members. | Yes | Yes | Yes |
| Category | Category label applied in Outlook to the email item. This field is only available for items residing in the mailbox where the category label is applied. | Yes | Yes | Yes |
| CC | Cc field for message types. The format is `DisplayName <SMTPAddress>`. | Yes | Yes | Yes |
| CC expanded | Cc field of the email or message expanded. If the CC field is a distribution list, the Cc expanded field contains a list of its members. This expansion is only available if the item is collected from the sender's mailbox. | Yes | Yes | Yes |
| Channel Name | Teams channels and private channels: *Channel*. | Yes | Yes | Yes |
| Client conversation ID | The Exchange email or Teams conversation ID. | No | Yes | Yes |
| Compound path | Path that shows the full location of an item across its source systems (such as mailbox or SharePoint), including the source name, to describe where the item originated. | Yes | Yes | Yes |
| Contains deleted message | Boolean field indicating if the item contains a deleted message. | Yes | Yes | Yes |
| Contains edited message | Boolean field indicating if the item contains an edited message. | Yes | Yes | Yes |
| Content source application | Application from which the content originates. For example, *SharePoint* for documents and list items stored in SharePoint; *MicrosoftTeams* for Teams messages, chats, and channel content. This field applies to top-level items and cloud attachments only. Embedded attachment rows have this field empty because they are sub-items of the parent message. Use the parent ID field to look up the parent item's value. | No | Yes | Yes |
| Conversation index | Index of each item within the same conversation. | No | Yes | Yes |
| Conversation name | Sub-header of Teams announcement posts or the title of Teams channel post. | Yes | Yes | Yes |
| Conversation topic | This field depends on content type. Emails: typically the subject of the email without the forward or reply. Teams 1:1 chat: the first 40 characters of the first message. Teams 1:N chat: Name of the group chat; if not available, the first 40 characters of the first message. Teams Channel Post: Post title or announcement subheader; if not available, the first 40 characters of the first message. | No | Yes | Yes |
| Conversation type | The type of chat conversation. Values are: Teams 1:1 and group chats and all Viva Engage conversations: *Group*. | Yes | Yes | Yes |
| Created | Date and time of the item's creation time. | Yes | Yes | Yes |
| Created by | *Created by* value from SharePoint. | Yes | Yes | Yes |
| Custodian | SMTP address of the custodian the item was associated with. | No | Yes | Yes |
| Data source | The data source name of the person or group from which the item is collected. | Yes | Yes | No |
| Date^1^ | Date is a computed field that depends on the file type: - **Email**: Sent date. **For draft emails, see Note 2.**- **Email attachments**: Last modified date of the document; if not available, the parent's sent date. - **Embedded documents**: Last modified date of the document; if not available, the parent's last modified date. - **SharePoint documents (includes modern attachments)**: Last modified date of the document; if not available, SharePoint last modified date. - **Non-Office 365 documents**: Last modified date. - **Meetings**: Meeting start date. - **VoiceMail**: Sent date. - **IM**: Sent date. - **Teams**: Sent date | Yes | Yes | Yes |
| Deduped compound path\* | List of compound paths of documents that are exact duplicates (email: based on content, documents: based on hash). | N/A | N/A | Yes |
| Deduped custodians\* | List of custodians of documents that are exact duplicates (for email, based on content; for documents, based on hash). | N/A | N/A | Yes |
| Deduped file IDs\* | List of file IDs of documents that are exact duplicates (for email, based on content; for documents, based on hash). | N/A | N/A | Yes |
| Deduped group file IDs\* | List of Group file IDs of documents that are exact duplicates (for email, based on content; for documents, based on hash). | N/A | N/A | Yes |
| Deduped thread file IDs\* | List of thread file IDs of documents that are exact duplicates (for email, based on content; for documents, based on hash). | N/A | N/A | Yes |
| Detected language | The language identified in the item, typically represented by a locale code (for example, en-us), as determined by SharePoint. | No | Yes | Yes |
| DG expansion result | Indicates whether the expansion of distribution group membership was successful. When emails are sent to distribution groups, additional fields such as *To Expanded*, *Cc Expanded*, or *Bcc Expanded* capture the expanded membership. These values are saved in the sender's mailbox copy if the sender is on hold. This field records failures in that expansion process. | Yes | Yes | Yes |
| Doc authors | Author from the document metadata. | Yes | Yes | Yes |
| Doc comments | Comments from the document metadata. | No | Yes | Yes |
| Doc company | Company from the document metadata. | No | No | Yes |
| Doc date created | Create date from document metadata. | No | Yes | Yes |
| Doc index | Position of a document within its hierarchical family, where a value of 0 represents the root (top-level item) and higher numbers denote increasing levels of embedding within another document. | No | Yes | Yes |
| Doc keywords | Keywords from the document metadata. | No | No | No |
| Doc subject | Subject from the document metadata. | No | Yes | Yes |
| Doc template | Template from the document metadata. | No | No | Yes |
| Document ID index | An internal index identifier for an item that's unique only within a single mailbox; items in different mailboxes (including different archive mailboxes for the same user) can share the same value. | Yes | Yes | Yes |
| Document ID path | Represents the hierarchical sequence of item IDs, showing the relationship when an item is embedded within another. A single ID indicates a top-level item with no parent. | No | Yes | Yes |
| Dominant theme\* | Dominant theme as calculated for analytics. | N/A | N/A | Yes |
| Email action | Values are *None*, *Reply*, or *Forward* and are based on the subject line of a message. | Yes | Yes | Yes |
| Email date sent | Sent date of the message. For chats, the beginning date from the transcript. **For draft emails, see Note 2.** | Yes | Yes | Yes |
| Email delivery receipt | Boolean field indicating whether the sender requested a delivery receipt for the email message. | No | No | Yes |
| Email importance | Importance of the message: Low; Normal; High | Yes | Yes | Yes |
| Email internet headers | The full set of email headers from the email message | No | Yes | Yes |
| Email level | Indicates a message's level within the email thread it belongs to; attachments inherit its parent message's value. | No | No | No |
| Email participant domains | List of domains of all participants. | Yes | Yes | Yes |
| Email read receipt | True or false value if a read receipt was received at sender end. | No | Yes | Yes |
| Email recipient domains | List of all domains of recipients of a message. | Yes | Yes | Yes |
| Email recipients | List of all recipients of a message (To, Cc, Bcc). | Yes | Yes | Yes |
| Email sender domain | Domain of the sender. | Yes | Yes | Yes |
| Email set | **Retired field**. | No | No | No |
| Email thread | **Retired field** | No | No | No |
| Error detail | If Status isn't successful, this field shows all the warnings and errors associated with the item. | Yes | Yes | Yes |
| Extracted content type | MIME media type of the item. For example, image/jpeg, application/vnd.ms-outlook, text/plain; charset=windows-1252, video/mp4. This type identifies the format of the extracted content. | No | Yes | Yes |
| Extracted text length | Number of characters in the extracted text. | No | Yes | Yes |
| Extracted text path | The path to the extracted text file in the export. This path applies only to review set export and only when user selects *export text file* in the settings. | No | No | Yes |
| Family duplicate set\* | Numeric identifier for families that are exact duplicates of each other (same content and all the same attachments). | N/A | N/A | Yes |
| Family ID | Groups together attachments and extracted items from email and chats with its parent item. This grouping includes the chat or email and all attachments and extracted items. | No | Yes | Yes |
| Family size | Number of documents in the family. | No | Yes | Yes |
| File class | For content from SharePoint and OneDrive: Document. For content from Exchange: Email or Attachment. For content from Teams or Viva Engage: Conversations. | No | Yes | Yes |
| File extension | Extension of the file, such as .csv, .pdf, .html, .txt, .jpg, and more. | Yes | Yes | Yes |
| File ID | Document identifier unique within a case. | No | Yes | Yes |
| File name | Native file name of the item. | Yes | Yes | Yes |
| Group ID | Groups together all items for email and documents. For email, this grouping includes the message and all attachments and extracted items. For documents, this grouping includes the document and any embedded items. | No | Yes | Yes |
| Group representative ID\* | Numeric identifier of each set of exact duplicates within the same group. The Group Representative ID corresponds to the document ID of the chosen representative in the group. | N/A | N/A | Yes |
| Has attachment | Indicates whether the message has attachments. Some items might indicate they have an attachment when they are actually embeddings in the email (.png or .html). When viewed in the review set, the email item won't have any attachments associated with it. | Yes | Yes | Yes |
| Has text | A Boolean field indicating whether the item contains extractable text content; possible values are True (text is present) or False (no text available). | Yes | Yes | Yes |
| Has unique attachment\* | This field marks emails that contain attachments not found in other emails within the same thread. Even if the email content is duplicated, unique attachments are flagged to ensure that all relevant documents are reviewed. This field is important in the legal review process to ensure that no unique evidence is overlooked, even if the email body isn't unique. | N/A | N/A | Yes |
| Identifier | The Internet Message ID for Exchange items and the SitePropertyPath for SharePoint items. | No | Yes | Yes |
| Immutable ID | An unchangeable identifier assigned to each item. This value is unique for parent items across mailboxes, but attachments and extracted items inherit the Immutable ID from their parent, so it isn't unique across all items. To uniquely identify individual items within a case, use the **File ID** field instead. | Yes | Yes | Yes |
| In reply to ID | In reply to ID from the message. This field identifies the unique message ID of the email or message that the current item is replying to. It's used to track conversational threads and message relationships, especially in threaded discussions or email chains. This field helps reconstruct the context of a reply by linking it back to the original message, but it doesn't contain the full content of the original message itself. | No | Yes | Yes |
| Inclusive type | **Retired field**. | N/A | N/A | N/A |
| Input file ID | The file ID of the top level item in the review set. For an attachment, this ID is the ID of the parent. Use this ID to group families together. | No | Yes | Yes |
| Internet message ID | Internet message ID from the message. | Yes | Yes | Yes |
| Is attachment from transcript | Is attachment part of teams transcript | Yes | Yes | Yes |
| Is bcc to me | Boolean metadata field that indicates whether the user was included in the Bcc line of the email. | No | Yes | Yes |
| Is doc from conversation | Boolean metadata field that indicates whether the document originated from a Microsoft Teams or Viva Engage conversation. | Yes | Yes | Yes |
| Is draft | Indicate if the email is a draft. **Use this field to identify items described in Note 2.** | No | Yes | Yes |
| Is encrypted | Indicate if the item is encrypted. | Yes | Yes | Yes |
| Is external | Indicate if the email is from an external organization. | No | Yes | Yes |
| Is group representative\* | This field indicates whether an email is marked as the single representative copy within a specific group. Only one email with the same hash from the same group is designated as the group representative. | N/A | N/A | Yes |
| Is inclusive\* | This field identifies whether an email contains all the unique content from a thread, including all previous replies. It ensures that only the most comprehensive email in a thread is reviewed, which is essential for understanding the full context of the conversation without having to review each individual reply. This field helps in efficiently managing long email threads by focusing on the most informative emails. | N/A | N/A | Yes |
| Is modern attachment | Boolean field indicating if this file is a modern attachment or linked file. | Yes | Yes | Yes |
| Is read | Boolean field indicates whether an email is opened or viewed by the recipient. | Yes | Yes | No |
| Is representative\* | One document in every set of exact duplicates is marked as representative. | N/A | N/A | Yes |
| Is thread representative\* | This field indicates whether an email is marked as the single representative copy within a specific thread. Only one email with the same hash from the same thread is designated as the thread representative. | N/A | N/A | Yes |
| Is top for group | Boolean field indicating if this item is the parent of the group. | No | Yes | Yes |
| Item class | Field that categorizes the type and structure of a message item such as *IPM.Note* for email, *IPM.File* for documents, or *IPM.SkypeTeams.Message* for Teams chats. | Yes | Yes | Yes |
| Item source | Mailbox or site from which the item originates. | Yes | Yes | Yes |
| Last modified by | The user who last modified the document. | No | Yes | Yes |
| Last modified time | Last modified date from document metadata. | No | Yes | Yes |
| Last modified time for retention | SharePoint document upload time for retention purposes. | No | No | No |
| Load ID | The ID of the load set in which the item was added to a review set. This ID corresponds to the job ID of the specific Add To Review Set job. | No | Yes | Yes |
| Location ID | Site ID for SharePoint locations and mailbox ID for exchange locations. | Yes | Yes | Yes |
| Location sub type | Specifies the type of location, such as *PrimaryMailbox*, *SystemMailbox*, *ArchiveMailbox*, or *OneDriveSite*. | Yes | Yes | Yes |
| Marked as pivot\* | Boolean field indicating if This file is the pivot in a near duplicate set. | N/A | N/A | Yes |
| Meeting end date | End time of the meeting for items of item class. Values are *IPM.Schedule.Meeting.Request*, *IPM.Appointment*, or *IPM.AppointmentSnapshot.SkypeTeams.Meeting*. | Yes | No | Yes |
| Meeting name | Name of Teams meeting. | No | No | No |
| Meeting start date | Start time of the meeting for items such as item class. For example, *IPM.AppointmentSnapshot.SkypeTeams.Meeting*. | No | No | Yes |
| Message kind | The type of message to search for.  Possible values: - *contacts*- *docs*- *email*- *externaldata*- *faxes*- *im*- *journals*- *meetings*- *microsoftteams* (returns items from chats, meetings, and calls in Microsoft Teams) - *notes*- *posts*- *rssfeeds*- *tasks*- *voicemail*. | Yes | Yes | Yes |
| Modern attachment embedded URLs | A modern attachment URL is embedded into item. | No | No | No |
| Modern attachment parent ID | The Immutable ID of the document's parent. | No | No | Yes |
| Native copy from | Field that contains the blob URL of the original document. | No | Yes | Yes |
| Native MD5 | MD5 hash (128-bit hash value) of the file stream. | No | Yes | Yes |
| Native SHA 256 | SHA256 hash (256-bit hash value) of the file stream. | No | Yes | Yes |
| ND ET sort excl attach | **Retired field**. | N/A | N/A | N/A |
| ND ET sort incl attach | **Retired field**. | N/A | N/A | N/A |
| ND set | **Retired field**. | N/A | N/A | N/A |
| Organizer | Meeting organizer's display name. | No | Yes | Yes |
| Original file extension | The original file extension of the file. | No | Yes | Yes |
| Original path | Original path of item in mailbox or path in SharePoint. | Yes | Yes | No |
| Parent ID | ID of the item's parent. | No | Yes | Yes |
| Parent node | The closest preceding email message in the email thread. | No | No | No |
| Participant expansion | Lists all individual members of a group participant such as a distribution list by expanding it into its constituent participants. | No | Yes | No |
| Participants | List of all participants of a message; for example, sender, to, Cc, Bcc. | Yes | Yes | Yes |
| Pivot ID\* | Analytics field value generated after running analytics in review set. The ID of a pivot. | N/A | N/A | Yes |
| Potentially privileged\* | Analytics field value generated after running analytics in review set - True if attorney-client privilege detection model considers the document potentially privileged. | N/A | N/A | Yes |
| Preservation original URL | This field that captures the original location and version of an item before it was moved to the Preservation Hold Library (PHL). | No | Yes | No |
| Received | The date and time the email was received in UTC. **For draft emails, see Note 2.** | Yes | Yes | Yes |
| Recipient count | Number of recipients in the message. | Yes | Yes | Yes |
| Redacted file path | The path of the redacted replacement file in the export. | No | No | No |
| Redacted text path | The path of the redacted text file replacement in the export. For internal Microsoft use only. | No | No | No |
| Representative ID\* | Numeric identifier of each set of exact duplicates. | N/A | N/A | Yes |
| Retention label | [Retention labels](retention) applied to content in Office 365. | Yes | Yes | Yes |
| Retention URL | Captures the SharePoint or OneDrive path of an item under retention, typically pointing to its preserved version in the Preservation Hold Library (PHL). | Yes | No | No |
| Sender | Sender (From) field for message types. The format is `DisplayName <SMTPAddress>`. | Yes | Yes | Yes |
| Sender/Author | Calculated field comprised of the sender or author of the item. | No | Yes | Yes |
| Sensitive type | List if SIT GUIDs associated with the item. | Yes | Yes | Yes |
| Sensitivity label | GUID of the Sensitivity label applied to the item. | Yes | Yes | Yes |
| Set ID | **Retired field**. | N/A | N/A | N/A |
| Set order inclusives first | **Retired field**. | N/A | N/A | N/A |
| Shared with | Lists the users or groups that have access to the SharePoint item. | No | No | No |
| SharePoint Item Content Type ID | Hexadecimal strings used as SharePoint content type identifiers are stored in the *SharepointItemContentTypeID* field, which helps identify the item's content type and map SharePoint content into the substrate's flexible schema. | Yes | Yes | No |
| Similarity percent\* | Indicates how similar a document is to the pivot of the near duplicate set. | N/A | N/A | Yes |
| Size | Number of bytes of the item. | Yes | Yes | Yes |
| Source ID | SMTP for mailbox or URL for site of the item source. | Yes | Yes | No |
| SPO document link | SharePoint document path associated with an item. It references the location of the document within SharePoint. | No | Yes | Yes |
| SPO preservation original document unique ID | A unique identifier assigned to a document that's preserved in SharePoint under a preservation policy. | No | Yes | Yes |
| SPO unique ID | Unique ID of the SharePoint from where the document is retrieved. | No | Yes | Yes |
| Status | Overall status of the item in the process; indication whether item is successful or it encounters issues. Values are *Successful*, *Retrieval error*, *Skipped*, and more. | Yes | Yes | Yes |
| Subject/Title | Calculated field comprised of the subject or title of the item. | Yes | Yes | Yes |
| Tags | Tags applied to the item, only apply to Review set export items. | No | No | Yes |
| Target path | Target path of the item in the export package .zip files. | Yes | No | Yes |
| Team name | Name of the Teams channel. | Yes | Yes | No |
| Teams announcement title | Title of the Teams announcement post. | Yes | Yes | No |
| Teams channel | Teams channel name. Only applies to Microsoft Teams content. | No | Yes | Yes |
| Themes list\* | Themes list as calculated for analytics. | N/A | N/A | Yes |
| Thread participant domains\* | Domains of all participants in a thread. | N/A | N/A | Yes |
| Thread participants\* | Participants in a thread. | N/A | N/A | Yes |
| Thread representative ID\* | Numeric identifier of each set of exact duplicates within the same thread. The thread Representative ID corresponds to the document ID of the chosen representative in the group. | N/A | N/A | Yes |
| Title | Title of the document. | No | Yes | Yes |
| To | To field value of email and messages. | Yes | Yes | Yes |
| To expanded | The *To* field of the email or message expanded, that is, if the To field is a distribution list, the To expanded field contains a list of its members. This expansion is only available if the item is collected from the sender's mailbox. | Yes | Yes | Yes |
| Type | Type of the content for the item. For example, *Message*. | Yes | Yes | Yes |
| Version group ID | Groups together the different versions of the same document. | No | Yes | Yes |
| Version number | The version number of a document collected from SharePoint or OneDrive. This version number matches the one displayed in the version history in the SharePoint and OneDrive user experience. | No | Yes | Yes |
| Was remediated | Indicate whether this item was remediated by the error remediation process. Only applies to review set exports. | No | No | Yes |
| Word count | The word count of the extracted text. | No | Yes | Yes |
| Workload | Indicates which workload the item comes from, Exchange or SharePoint. | Yes | Yes | Yes |

Note

^1^ When you use the *Date* condition in an eDiscovery search, you might see discrepancies in the results because Microsoft 365 content types store and interpret dates differently. For example, emails, documents, and Teams messages might have several date-related metadata fields, such as *Created*, *Last Modified*, *Received*, and *Sent*. The *Date* condition might apply differently across these items, depending on the content source and query.

To improve accuracy and get the results you want, use date ranges instead of specific dates. Combine date conditions with keywords or other metadata filters to narrow your results. Review search statistics and preview results to validate search results before finalizing exports.

^2^ Draft email items carry values in the **Received**, **Email date sent**, and **Date** fields even though the message was never actually sent or received. These values reflect the underlying Exchange properties stored on the item and shouldn't be interpreted as actual send or delivery events.

Use the **Is draft** field to identify these items. Because the computed **Date** field derives from the Sent date for email, drafts might also be returned unexpectedly by date-range conditions in searches and review set queries. Filter on **Is draft** where date accuracy is required for review or production.