---
layout: Conceptual
title: Review data with the Insider Risk Management content explorer | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-content-explorer
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about Insider Risk Management Content explorer in Microsoft Purview
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-18T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
locale: en-us
document_id: 499f7385-de62-867d-49fb-e98ae17931db
document_version_independent_id: 499f7385-de62-867d-49fb-e98ae17931db
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-content-explorer.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-content-explorer
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-content-explorer.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: c0616a5d-93c3-ed59-247b-c464e17c3b45
---

# Review data with the Insider Risk Management content explorer | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

The Insider Risk Management **Content explorer** enables users assigned the *Insider Risk Management Investigators* role to examine the context and details of content associated with activity in alerts. The case data in Content explorer refreshes daily to include new risk activity. For all alerts that you confirm to a case, the solution archives copies of data and message files as a snapshot in time of the items, while maintaining the original files and messages in the storage sources. If needed, you can export case data files as a portable document file (PDF) or in the original file format.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Use the Content explorer to view details for a specific case

To examine the emails and files captured by the policies included in a specific case, go to the Insider Risk Management **Cases** page and select the row of the *Case name* in the list for the case you want to view details for. Then in the case details page, select the **Content explorer** tab to open the Content explorer.

If content download is off for the case, select **Add content** from the Content explorer tab. If you've reached the maximum number cases with content downloaded limit, you must resolve cases to download additional content.

Important

After you confirm an alert to a case, Content explorer doesn't display any details for that case if the organization hasn't assigned a user to either the *Insider Risk Management Investigators* or *Insider Risk Management* role group.

Content explorer includes user activities related to Microsoft 365 service files, such as user activity on SharePoint, Exchange, and OneDrive for Business. For new cases, it usually takes about an hour for content to populate in Content explorer. For cases with large amounts of content, it might take longer to create a snapshot. If content is still loading in Content explorer, you see a progress indicator that displays the completion percentage.

In some cases, you might not be able to review data associated with a case as a snapshot in Content explorer. This situation might occur when you delete or move case data, or when a temporary error occurs when processing case data. If this situation occurs, select **View files** in the warning bar to view the file names, file path, and reason for the failure for each file. If needed, you can export this information to a .csv (comma-separated values) file.

If the content includes Information Rights Management permissions, these permissions are maintained for the copied content and users assigned the *Insider Risk Management Investigators* role need these permissions and rights if they need to open and view the files. Each file and message are automatically assigned a unique file ID in the Insider Risk Management case for management purposes. Documents associated with device indicator activities aren't included in Content explorer.

Note

After a case is active for over 30 days, Content explorer isn't updated to reflect new activities. To update content explorer with new activities for a user in this scenario, resolve the case and open a new case for the user.

## View options

### Source view

The **Source** viewer displays the richest view of a selected document. It supports hundreds of file types and is meant to display the truest to native experience possible. For Microsoft Office files, the viewer uses the web version of Office apps to display content such as document comments, Microsoft Teams chats, Excel formulas, hidden rows and columns, and PowerPoint notes.

### Plain text view

The **Plain text** viewer (preview) provides a view of the extracted text of a selected file. It ignores any embedded images and formatting but is useful if you want to understand the content quickly. The text view also includes these features:

- Line counter makes it easier to reference specific portions of a document
- Search hit highlighting that highlights terms within the document and in the scrollbar

### Annotate view

The **Annotate** view (preview) provides features that let you apply markup on a selected document, including the ability to:

- **Select annotations**: Select annotations on a document to delete
- **Select text**: Select text on the document to delete
- **Area redactions**: Draw a box on the document to hide sensitive content
- **Pencil**: Free-hand draw in selectable colors on a document to bring attention to certain portions of a document
- **Toggle annotation transparency**: Make annotations semi-transparent to view the content behind the annotation
- **Previous page**: Navigate to previous page
- **Next page**: Navigate to the next page
- **Go to page**: Enter a specific page number to navigate to
- **Zoom**: Set the zoom level for annotate view
- **Rotate**: Rotate the document clockwise

### Metadata view

The panel in the **Metadata** view (preview) displays various metadata associated with the selected document. Search for specific metadata by using the **Search metadata name** field.

You can toggle the panel in the **Metadata** view on or off to display various metadata associated with the selected document. Although you can customize the search results grid to display specific metadata, there are instances where scrolling horizontally can be difficult while reviewing data. The File metadata panel allows you to toggle on a view within the viewer.

## Group options

Use the **Group** control to view content grouped by the following options:

- **Group by families**: All items related to a specific file are grouped together using the same Group ID. For example, if you have a PowerPoint file in the alert that includes imbedded images or .zip files, these images and files are grouped with the PowerPoint file and shown as nested items with the file in the item list view. Microsoft 365 Copilot and Microsoft 365 Copilot Chat user prompts and responses are also grouped together using the same Group ID when there are multiple prompts and responses associated with a file.
- **Group by conversations and related items**: All email messages, Teams conversations, and Viva Engage conversations are grouped using the same Thread ID and appear as nested items. Additionally, all associated content for these messages and conversations is also grouped together. For example, if you have an email conversation that includes several email messages, some of which include attachments and some that include embedded images, all of the email messages, attachments, and images are grouped together in the alert list view under an applicable item.

## Column options

To help risk analysts and investigators review captured data and messages, the Content explorer includes several filtering and sorting tools. For basic sorting, the **Date** and **File class** columns support sorting by using the column titles in the content queue pane. You can add other queue columns to the view to provide different pivots on the files and messages.

To add, remove, or reorder column headings for the content queue, use the **Customize columns** control and select from the following column options. These columns map to the common, email, and document property conditions supported in the Content explorer.

View results in UTC or your local time by toggling the **Time zone** option in the action bar.

| **Column option** | **Description** |
| --- | --- |
| **Author** | The author field from Office documents, which persists if a document is copied. For example, if a user creates a document and the emails it to someone else who then uploads it to SharePoint, the document still retains the original author. |
| **Bcc** | Available for email messages, the users in the Bcc message field. |
| **Cc** | Available for email messages, the users in the Cc message field. |
| **Compound path** | Human readable path that describes the source of the item. |
| **Conversation ID** | Conversation ID from the message. |
| **Conversation index** | Conversation index from the message. |
| **Created time** | The time the file or email message was created. |
| **Date (UTC)** | For email, the date a message was received by a recipient or sent by the sender. For documents, the date a document was last modified. Date is in Coordinated Universal Time (UTC). |
| **Dominant theme** | Dominant theme as calculated for analytics. |
| **Email set ID** | Group ID for all messages in the same email set. |
| **Family ID** | Family ID groups together all items; for email, this column includes the message and all attachments; for documents, this column includes the document and any embedded items. |
| **File class** | For content from SharePoint and OneDrive: **Document**; for content from Exchange: **Email** or **Attachment**. |
| **File ID** | Document identifier unique within the case. |
| **File type icon** | The extension of a file; for example, docx, one, pptx, or xlsx. This field is the same property as the FileExtension site property. |
| **ID** | The GUID identifier for the file. |
| **Immutable ID** | Immutable ID as stored in Office 365. |
| **Inclusive type** | Inclusive type calculated for analytics: **0** - not inclusive; **1** - inclusive; **2** - inclusive minus; **3** - inclusive copy. |
| **Last modified** | The date that a document was last changed. |
| **Marked as representative** | One document from each set of exact duplicates is marked as representatives. |
| **Message kind** | The type of email message to search for. Possible values: contacts, docs, email, external data, faxes, im, journals, meetings, microsoft teams (returns items from chats, meetings, and calls in Microsoft Teams), notes, posts, RSS feeds, tasks, voicemail |
| **Participants** | List of all participants of a message; for example, Sender, To, Cc, Bcc. |
| **Pivot ID** | The ID of a pivot. |
| **Received** | The date that an email message was received by a recipient. This field is the same property as the Received email property. |
| **Recipients** | All recipient fields in an email message. These fields are To, Cc, and Bcc. |
| **Representative ID** | Numeric identifier of each set of exact duplicates. |
| **Sender** | The sender of an email message. |
| **Sender/Author** | For email, the person who sent a message. For documents, the person cited in the author field from Office documents. You can type more than one name, separated by commas. Two or more values are logically connected by the OR operator. |
| **Sensitive info types** | The sensitive info types identified in content. |
| **Sensitivity labels** | The sensitivity labels applied to the content. |
| **Sent** | The date that an email message was sent by the sender. This field is the same property as the Sent email property. |
| **Size** | For both email and documents, the size of the item (in bytes). |
| **Subject** | The text in the subject line of an email message. |
| **Subject/Title** | For email, the text in the subject line of a message. For documents, the title of the document. As previously explained, the Title property is metadata specified in Microsoft Office documents. You can type the name of more than one subject/title, separated by commas. Two or more values are logically connected by the OR operator. |
| **Themes list** | Themes list as calculated for analytics. |
| **Title** | The title of the document. The Title property is metadata that's specified in Office documents. It's different than the file name of the document. |
| **To** | The recipient of an email message in the To field. |

## Filtering

Use one or more filters to narrow the scope of a search and return a more refined set of results. To set a filter, select **Query** (preview) at the top of the content queue. Many filters include additional conditions to help narrow the results returned by the filter. For example, the *Date* filter includes controls to configure a *Start date* and *Ending date* for the **Date** filter. Save queries for future use by selecting **Save filters** and following the prompts. Select one or more filter items from the following example categories:

### Common filters

| **Filter** | **Description** |
| --- | --- |
| **Date (UTC)** | For email, the date a message was received by a recipient or sent by the sender. For documents, the date a document was last modified. |
| **Sender/Author** | For email, the person who sent a message. For documents, the person cited in the *Author* field from Office documents. Type more than one name, separated by commas. |
| **Source** | The location of the document in your organization. For example, a specific SharePoint site location. |
| **Subject/Title** | For email, the text in the subject line of a message. For documents, the title of the document. The Title property in documents is metadata specified in Microsoft Office documents. Type the name of more than one subject/title, separated by commas. Two or more values are logically connected by the OR operator. |

### Email filters

| **Filter** | **Description** |
| --- | --- |
| **Bcc** | The Bcc field of an email message. |
| **Cc** | The Cc field of an email message. |
| **Has attachment** | Indicates whether a message has an attachment. Values are listed as **true** or **false**. |
| **Is email attachment** | If the document is an attachment, the value is listed as **Yes**. |
| **Is embedded document** | If the document is embedded in the email message, the value is listed as **Yes**. |
| **Is inline attachment** | If the document is an inline attachment in the email message, the value is listed as **Yes**. |
| **Participants** | All the people fields in an email message. These fields are From, To, Cc, and Bcc. |
| **Received** | The date that an email message was received by a recipient. |
| **Recipient domains** | List of all domains of recipients of a message. |
| **Recipients** | The email message recipients. |
| **Sender domain** | Domain of the sender. |
| **Sender** | Sender (From) field for message types. Format is **DisplayName &lt;SmtpAddress&gt;**. |
| **To** | The To field of an email message. |
| **Unique in email set** | False if there's a duplicate of the attachment in its email set. |

### Document filters

| **Filters** | **Description** |
| --- | --- |
| **Compliance labels** | Compliance labels applied in Microsoft 365. |
| **Created time (UTC)** | The date and time the file or email message was created. The date and time are in Coordinated Universal Time (UTC). |
| **File extension** | The extension type of the file. |
| **Last modified date (UTC)** | The date that a document was last changed. The date and time are in Coordinated Universal Time (UTC). |
| **User activity events** | Activity for items related to specific user activity in a case. For example, when you select a link to 'Explore Content' for an activity in the **User Activity** page of a case, this filter is used to display items related to that activity. |
| **Work product** | The type of work product for the document. For example, annotations or tags in the document. |

## Advanced filters

Advanced filters (preview) let you build more flexible and granular filters. This advanced filtering capability enables you to:

- Quickly search for filter conditions.
- Create complex filters using subgroups, *AND*, or *OR* conditions.
- Easily change your queries with **Clear all** and **Reset all** controls.
- Manage saved filters without having to navigate to another area.
- Use *Is empty* and *Is not empty* conditions for each filter.

### Filter types

Every searchable field in an alert has a corresponding filter that you can use for filter items based on a specific field.

There are multiple types of filters:

- **Freetext**: A freetext filter is applied to text fields such as *Subject*. You can list multiple search terms by separating them with a comma.
- **Date**: A date filter is used for date fields such as *Last modified date*.
- **Search options**: A search options filter provides a list of possible values (each value is displayed with a checkbox that you can select) for particular fields in the review. This filter is used for fields, such as *Sender*, where there's a finite number of possible values in the alert.
- **Keyword**: A keyword condition is a specific instance of freetext condition that you can use to search for terms. You can also use Keyword Query language (KeyQL) in this type of filter. For more information, see the [Query language](#
) and [Advanced query builder](#
) sections in this article.

### Advanced filter controls

To create and custom filtering for your search results, use the following controls:

- **AND/OR**: These conditional logical operators allow you to select the query condition that applies to specific filters and filter subgroups. These operators allow you to use multiple filters or subgroups connected to a single filter in your query.
- **Add conditions**: Allows you to add multiple filtering conditions to your query. Is available after you've defined at least one query filter.
- **Select an operator**: Depending on the selected filter, the operators compatible for the filter are available to select. For example, if the *Date* filter is selected, the available operators are *Before*, *After*, and *Between*. If the *Size (in bytes)* filter is selected, the available operators are *Greater than*, *Greater or equal*, *Less than*, *Less or equal*, *Between*, and *Equal*. If it's a file name, ID, or keyword, the available operators are *Equal any of*, *Equal none of*, *Contains all of*, *Contains any of*, *Contains none of*, *Is empty*, or *Is not empty*.
- **Value**: Depending on the selected filter, the values compatible for the filter are available. Additionally, some filters support multiple values and some filters support one specific value. For example, if the *Date* filter is selected, select date values. If the *Size (in bytes)* filter is selected, select a value for bytes.
- **Add subgroup**: After you've defined a filter, you can add a subgroup to refine the results returned by the filter. You can also add a subgroup to a subgroup for multi-layered query refinement.
- **Save**: Allows you to save the current set of filters, conditions, and operators for future use. These saved queries are user-specific.
- **Remove a filter condition**: To remove an individual filter or subgroup, select the remove icon to the right of each filter line or subgroup.
- **Clear all**: To clear the entire query of all filters and subgroups, select **Clear all**.