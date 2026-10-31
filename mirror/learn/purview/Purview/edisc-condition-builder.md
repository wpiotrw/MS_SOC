---
layout: Conceptual
title: Use the condition builder to create search queries in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-condition-builder
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about using the condition builder to create search queries in eDiscovery in the Microsoft Purview portal.
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
ms.custom: sfi-image-nochange, msecd-doc-authoring-1014
locale: en-us
document_id: c32f70eb-f444-e239-7e9b-6a8b1a8928f1
document_version_independent_id: c32f70eb-f444-e239-7e9b-6a8b1a8928f1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-condition-builder.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-condition-builder
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-condition-builder.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: e14d1c9b-7f4d-0c51-ca01-78d0568296a8
---

# Use the condition builder to create search queries in eDiscovery | Microsoft Learn

The condition builder provides an easy-to-use search experience when you build [search queries](edisc-search-query) in eDiscovery. Use the condition builder in search and [review sets](edisc-review-set-search) to construct simple and complex keyword queries, queries with operators (AND, OR), or both to help identify items in your organization.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Use the condition builder

To create a query and custom conditional filtering for your search, use the following controls:

- The **Keywords** condition is always available as the first condition in your query, making it easy to get started with search tasks. This condition only supports the **Equal** operator and is removed from your query using **Delete**. In the **Value** field of the Keywords condition, apply logical operators such as **AND**, **OR**, and **NEAR**. For example, entering `red AND blue` treats **AND** as a logical operator rather than a literal keyword. To search for an exact phrase like `"red and blue"`, enclose the text in quotation marks. This tells the search engine to treat the text as a single string. You can also select **Enter** on your keyboard to create a new grid for the next keyword. If you paste a list of keywords separated by line breaks (carriage returns), the system automatically generates a separate grid for each keyword.

    When multiple keyword segments are entered using the condition builder, the query can be converted to [KeyQL](edisc-keyword-query-language) and each keyword segment is separated by c:s. If your query includes multiple keyword conditions, the resulting KeyQL includes c:s to ensure keyword segmenting so you see hits per segment. This behavior is automatic and doesn't require manual entry of c:s in the KeyQL builder.

    Note

    To generate a keyword report in the [statistics](/en-us/purview/edisc-search-results) view, you must populate at least two or more keyword grids. If you enter only a single keyword, the total hit count shown reflects the results for that one keyword, and a keyword report isn't generated.
- **Add conditions**: Add a condition for the specific data sources for the search. To add extra conditions to your query, select **Add conditions** to display the list of available conditions. Each condition value selection adds a new condition to your query. Select the **AND/OR** operator as appropriate.
- **AND/OR**: These conditional logical operators let you select the query operation that applies to a specific condition. These operators let you use multiple conditions connected to your query. The operator following the *keyword* condition must be **AND**.
- **Selecting an operator**: Depending on the selected condition, the operators compatible for the condition are available to select. For example, if you select the *Date* condition, the available operators are *Before*, *After*, and *Between*. If you select the *Size (in bytes)* condition, the available operators are *Greater than*, *Greater or equal*, *Less than*, *Less or equal*, *Between*, and *Equal*.
- **Value**: Depending on the selected condition, the values compatible for the condition appear in the value details pane or you can add inline. Depending on the condition type associated with the value, you see options to define, filter, or search for values associated with the selected condition. For example, if you select *Sender* as the condition, you can search for and add specific users in your organization or external users. If you select *Size (in bytes)* as the condition, you see the option to enter a number for the size as the value. If the value is blank, the value field border appears in red to help notify you that a value is needed.
- **Delete a filter condition**: To remove an individual condition, select the delete icon to the right of each filter line.
- **Clear a filter value:** To clear the value for a specific condition, select the remove icon to the right of each filter line.
- **Save as draft**: To save the current set of conditions as a draft, select **Save as draft** above the condition builder area.
- **Discard**: To discard any changes made to the search, including conditions, and data source, select **Discard** above the condition builder area.

### Guidelines for using conditions

Keep the following guidelines in mind when using search conditions:

- A condition connects logically to the keyword query (specified in the keyword condition) by the **AND** operator. That connection means that items need to satisfy both the keyword query and the condition to be included in the results.
- All conditions that follow the *keyword* condition are grouped together.
- If you add two or more unique conditions to a search query (conditions that specify different properties), those conditions connect logically by the **AND** and **OR** operators. That connection means the search returns only items that satisfy all the conditions (in addition to any keyword query).
- If you add multiple values (separated by commas or semicolons) to a single condition, those values connect by the **OR** operator. That connection means the search returns items if they contain any of the specified values for the property in the condition.
- Any condition that uses an operator with **Contains** and **Equals** logic returns similar search results for simple string searches. A simple string search is a string in the condition that doesn't include a wildcard. For example, a condition that uses **Equals any of** returns the same items as a condition that uses **Contains any of**.
- The search query that you create by using the keywords box and conditions appears on the **Search** page, in the details pane for the selected search. In a query, everything to the right of the notation `(c:c)` indicates conditions that you add to the query. Don't use `(c:c)` in manually entered queries. `(c:c)` isn't equal to **AND** or **OR**.
- If you are searching using *Compliance Tag* or *Retention Label* and the name of the label includes special characters that aren't supported (listed in the Special characters section, they are ignored as a condition of the search.

## Find and select conditions

When you select **Add conditions** in the condition builder, you get quick access to some commonly used conditions such as *Date*, *Subject/Title*, and *Participants* along with conditions you used most recently. Select **Show more** and the **Choose which conditions to add** flyout pane appears to help you refine your search query with specific conditions. Use the options in the following sections to help you choose applicable conditions.

### Filter conditions by area

Quickly filter the condition view for mailboxes and site properties to help locate a specific condition for your search query. Filter available conditions in the following global groups:

- **All**: Shows all conditions and condition groups.
- **Common**: Filters and displays only the conditions that apply to both mailboxes and sites.
- **Exchange mailboxes**: Filters and displays only the conditions that apply to mailboxes.
- **SharePoint and OneDrive sites**: Filters and displays only the conditions that apply to SharePoint and OneDrive sites.

### Condition picker

To quickly search for a specific condition, use the **Tell us what you're looking for** field to enter the name of the condition. The results automatically scope to the filter for global groups. For example, to search for any condition named *Type* (or one that contains the term *type* in the condition name), select **All** as the global filter, then enter *type* in the **Tell us what you're looking for** field. The condition view returns all conditions in all condition groups that contain the term *type*. Select the applicable condition to add to your search query.

![Screenshot of the condition picker page for adding search conditions such as Message kind, Participants, Received, and Recipients.](media/ediscovery-condition-builder-picker.png)

Important

You can only use the *Keyword* and *KeyQL* conditions once each in the condition builder.

## Scenario example

The eDiscovery administrator needs to create a query to find emails sent from User1 to User2 that were sent between September 15, 2024 and October 15, 2024 that contains the keywords *compliance* and *audit*. For this example, the administrator creates the following query using the new query builder:

1. For the first filter, the administrator uses the *Keywords* condition, the *Equal* operator, and *compliance, audit* as the keyword *Value*.
2. Next, the administrator selects **Add conditions**, selects *Sender*, then selects the *Contains any of* operator, then enter *User1@contoso.com* in the **Value** field. This can include external users.
3. Next, the administrator selects **Add conditions**, selects the *To* filter, then selects the *Contains any of* operator, then selects *User2@contoso.com* in the **Value** field. This can include external users.
4. To define the date range, the administrator selects **Add conditions**, selects *Date*, then selects the *Between* operator, and then selects the starting and ending dates for the *Value*.
5. Finally, the administrator selects **Run query** to return results matching the conditions and their values.

![Screenshot of a condition builder search with Keywords, Sender, To, and Date conditions configured for a sample query.](media/ediscovery-condition-builder-example.png)

## Use search conditions

You can add conditions to a search query to narrow a search and return a more refined set of results. Each condition adds a clause to the KeyQL search query that is created and run when you start the search.

- Special characters
- Conditions for common properties
- Conditions for mail properties
- Conditions for document properties
- Operators used with conditions

### Special characters

Some special characters aren't included in the search index and therefore aren't searchable. This limitation also applies to the special characters that represent search operators in the search query. Here's a list of special characters that are either replaced by a blank space in the actual search query or cause a search error.

`+ - = : ! @ # % ^ & , ; _ / ? ( ) [ ] { }`

### Conditions for common properties

Create a condition using common properties when searching mailboxes and sites in the same search. The following table lists the available properties to use when adding a condition.

| Condition | Description |
| --- | --- |
| Content kind^1^ | Applied to both Exchange and SharePoint items, it refers to the type or category of the content. For example, *ContentKind:SharePointDocument*, *ContentKind:Copilot*, etc. |
| Content source application^1^ | Identifies the application or service where the content originated.For example, *ContentSourceApplication:OneDriveForBusiness*, *ContentSourceApplication:SharePoint*, etc. |
| Date | For email, the date a message was created or imported from a PST file. For documents, the date a document was last modified. For Teams messages, the original message date. Item reports and review set metadata might display different timestamps (such as ingestion or modification dates) for the same Teams message. The date condition filters on the original event date.  If you're searching for email messages for a specific time period, use the message *Received* and *Sent* conditions if you're unsure if the email messages might be imported instead of natively created in Exchange. |
| Identifier^1^ | For email, the ID for a specific message. *Message IDs* are included in the audit record, data loss prevention (DLP) alerts, or review set metadata and allow you build a specific search for an individual message.  For Microsoft Teams messages, the ID of the chat or reaction. The *ChatThreadID* is included in the audit record, data loss prevention (DLP) alerts, or review set metadata and allow you build a specific search for an individual chat or reaction. |
| Sender/Author | For email, the person who sent a message. For documents, the person cited in the author field from Office documents. You can type more than one name, separated by commas. Two or more values are logically connected by the **OR** operator. (See [Recipient expansion](edisc-search-mailboxes#recipient-expansion).) |
| Size (in bytes) | For both email and documents, the size of the item (in bytes). |
| Subject/Title | For email, the text in the subject line of a message. For documents, the title of the document. The Title property is metadata specified in Microsoft Office documents. You can type the name of more than one subject/title values, separated by commas. Two or more values are logically connected by the **OR** operator. <br>**Note**: Don't include double quotation marks to the values for this condition because quotation marks are automatically added when using this search condition. If you add quotation marks to the value, two pairs of double quotations are added to the condition value, and the search query returns an error. |
| Retention label | For both email and documents, retention labels applied to messages and documents. Retention labels can be used to declare records and help you manage the data lifecycle of content by enforcing retention and deletion rules specified by the label. <br>**Note**: If using Retention Label names that include unsupported special characters, they will be ignored as a condition for the search. For more information about retention labels, see [Retention policies and retention labels](retention). |

### Conditions for mail properties

Create a condition using mail properties when searching mailboxes or public folders in Exchange Online. The following table lists the email properties that you can use for a condition. These properties are a subset of the email properties listed in Conditions for common properties. These descriptions are repeated for your convenience.

| Condition | Description |
| --- | --- |
| Message kind | The message type to search. This property is the same as the Kind email property. Possible values: <br>- contacts<br>- docs<br>- email<br>- externaldata<br>- fax<br>- im<br>- journals<br>- meetings<br>- microsoftteams<br>- notes<br>- posts<br>- rssfeeds<br>- tasks<br>- voicemail |
| Participants | All the people fields in an email message. These fields are From, To, Cc, and Bcc. (See [Recipient expansion](edisc-search-mailboxes#recipient-expansion).) |
| Received | The date that an email message was received by a recipient. This property is the same as the Received email property. |
| Recipients | All recipient fields in an email message. These fields are To, Cc, and Bcc. For more information, see [Recipient expansion in mailbox searches](edisc-search-mailboxes#recipient-expansion). |
| Sender | The sender of an email message. |
| Sent | The date that an email message was sent by the sender. This property is the same as the Sent email property. |
| Subject | The text in the subject line of an email message. <br>**Note**: Don't include double quotation marks to the values for this condition because quotation marks are automatically added when using this search condition. If you add quotation marks to the value, two pairs of double quotations are added to the condition value, and the search query returns an error. |
| To | The recipient of an email message in the To field. |
| Topic^1^ | Summary of the main subject or theme discussed in an email thread or conversation. |
| Item class | The message class property for an email item. It's a multivalue condition. To select multiple message classes, hold the **CTRL** key and select two or more message classes in the drop-down list that you want to add to the condition. Each message class selected in the list are logically connected by the **OR** operator in the corresponding search query.  For a list of the message classes (and their corresponding message class ID) used by Exchange and that you can select in the **Message class** list, see [Item Types and Message Classes](/en-us/office/vba/outlook/Concepts/Forms/item-types-and-message-classes). |

### Conditions for document properties

Create a condition using document properties when searching for documents on SharePoint and OneDrive sites. The following table lists the document properties that you can use for a condition. These properties are a subset of the site properties listed in Conditions for common properties. These descriptions are repeated for your convenience.

| Condition | Description |
| --- | --- |
| Author | The author field from Office documents. |
| Created | The date that a document is created. |
| File type | The extension of a file; for example, docx, one, pptx, or xlsx. This is the same property as the FileExtension site property. <br>**Note:** If you include a File type condition using the **Equals** or **Equals any of** operator in a search query, you can't use a prefix search (by including the wildcard character ( \* ) at the end of the file type) to return all versions of a file type. If you do, the wildcard is ignored. For example if you include the condition `Equals any of doc*`, only files with an extension of `.doc` are returned. Files with an extension of `.docx` aren't returned. To return all versions of a file type, use the *property:value* pair in a keyword query; for example, `filetype:doc*`. |
| Last modified | The date that a document was last changed. |
| Path^1^ | The URL or location of a file or folder within a SharePoint site. |
| Sensitive information type (SIT)^1^ | Sensitive information types included in documents. SITs are pattern-based classifiers and they detect sensitive information like social security, credit card, or bank account numbers to identify sensitive items. For more information about SITs, see [Sensitive information types](sit-sensitive-information-type-learn-about). |
| Sensitivity label^1^ | Sensitivity labels applied to documents. Sensitivity labels let you classify and protect your organization's data, while making sure that user productivity and their ability to collaborate isn't hindered. For more information about sensitivity labels, see [Sensitivity labels](sensitivity-labels). |
| Title | The title of the document. The Title property is metadata that's specified in Office documents. It's different from the file name of the document. |

### Operators used with conditions

When you add a condition, select an operator that matches the type of property for the condition. The following table describes the operators that work with conditions and lists the equivalent operator used in the search query.

| Operator | Query equivalent | Description |
| --- | --- | --- |
| After | `property>date` | Use with date conditions. Returns items that were sent, received, or modified after the specified date. |
| Before | `property<date` | Use with date conditions. Returns items that were sent, received, or modified before the specified date. |
| Between | `date..date` | Use with date and size conditions. When used with a date condition, returns items that were sent, received, or modified within the specified date range. When used with a size condition, returns items whose size is within the specified range. |
| Contains any of | `(property:value) OR (property:value)` | Use with conditions for properties that specify a string value. Returns items that contain any part of one or more specified string values. |
| Doesn't contain any of | `-property:value`<br>`NOT property:value` | Use with conditions for properties that specify a string value. Returns items that don't contain any part of the specified string value. |
| Doesn't equal any of | `-property=value`<br>`NOT property=value` | Use with conditions for properties that specify a string value. Returns items that don't contain the specific string. |
| Equals^2^ | `size=value` | Returns items that are equal to the specified size. |
| Equals any of | `(property=value) OR (property=value)` | Use with conditions for properties that specify a string value. Returns items that match one or more specified string values. |
| Greater^2^ | `size>value` | Returns items where the specified property is greater than the specified value. |
| Greater or equal^2^ | `size>=value` | Returns items where the specified property is greater than or equal to the specified value. |
| Less^2^ | `size<value` | Returns items that are less than the specified value. |
| Less or equal^2^ | `size<=value` | Returns items that are less than or equal to the specified value. |
| Not equal^2^ | `size<>value` | Returns items that don't equal the specified size. |

Note

^1^ This operator is an eDiscovery premium feature condition.

^2^ This operator is available only for conditions that use the *Size* property.