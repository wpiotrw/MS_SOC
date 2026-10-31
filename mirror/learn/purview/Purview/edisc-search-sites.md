---
layout: Conceptual
title: Finding content in sites in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-sites
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about finding content in sites in eDiscovery in the Microsoft Purview portal.
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
document_id: d108b68f-06fd-d0d2-c9cf-bf60044f2092
document_version_independent_id: d108b68f-06fd-d0d2-c9cf-bf60044f2092
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-sites.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-sites
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-sites.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 747a51da-e03c-43fc-6b3b-ba9925277520
---

# Finding content in sites in eDiscovery | Microsoft Learn

When you [search for documents and files](edisc-search-query) in SharePoint or OneDrive sites, adjust your query approach based on the metadata for the documents and files you're interested in. Files and documents have relevant properties like *Author*, *Created*, *CreatedBy*, *FileName*, *LastModifiedTime*, and *Title*. Most of these properties aren't relevant when searching for communications content in Exchange Online. Using these properties might lead to unexpected results if you use them across both documents and communications. Additionally, the *FileName* and *Title* of a document might not be the same. Using one or the other to try to find a file with specific content might lead to different or inaccurate results. Keep these properties in mind when searching for specific document and file content in SharePoint and OneDrive.

For more information about finding content in sites in eDiscovery, watch the following video:

For example, to find content related to documents created by User 1, for a project called *Tradewinds*, for specific files named *Financials*, and from January 2020 to January 2022, use a query with the following properties:

- Add User 1 as a data source to the search.
- Select User 1's OneDrive site as the location of interest.
- Add additional groups and their associated SharePoint sites related to the project as [data sources](edisc-data-sources).
- For **FileName**, use *Financials*
- For **Keyword**, use *Tradewinds*
- For **Date Range**, use the *January 1, 2020* to *January 31, 2022* range

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Searchable site properties in KeyQL

The following table lists the SharePoint and OneDrive properties supported in search using the eDiscovery [KeyQL](edisc-keyword-query-language) editor in the Microsoft Purview portal or by using the [New-ComplianceSearch](/en-us/powershell/module/exchangepowershell/new-compliancesearch?view=exchange-ps) or [Set-ComplianceSearch](/en-us/powershell/module/exchangepowershell/set-compliancesearch?view=exchange-ps) cmdlets. For a list of supported condition builder properties, see [Use the condition builder to create search queries in eDiscovery](edisc-condition-builder#conditions-for-mail-properties).

Important

While documents and files stored on SharePoint and OneDrive might have other properties supported in other Microsoft 365 services, only the document and file properties listed in this table are supported in eDiscovery search tools. Attempting to include other document or file properties in searches isn't supported.

If you set a site status to *Locked* and the site to *NoAccess*, eDiscovery doesn't return search results. For more information about managing site lock statuses, see [Lock and unlock sites](/en-us/sharepoint/manage-lock-status?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json). In addition, if a document is restricted in the content store, the eDiscovery manager must be a site admin, site owner, or the owner or last modifier of the restricted document to access it in eDiscovery. For more information about restricted content, see [Data Loss Prevention policy reference](dlp-policy-reference#actions).

Important

If a OneDrive site is archived and then searched within eDiscovery, the search triggers reindexing and the number of items increases over time as the site fully indexes. This effect persists until the site reindexing is complete. For more information about manually triggering re-indexing, see [Manually request crawling and reindexing of a site, a library, or a list](/en-us/sharepoint/crawl-site-content?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

The table includes an example of the *property:value* syntax for each property and a description of the search results returned by the examples.

| Property | Property description | Example | Search results returned by the examples |
| --- | --- | --- | --- |
| Author | The author field from Office documents. Be sure to use the user's display name for this property. | `author:"Garth Fort"` | All documents authored by Garth Fort. |
| ContentType | The SharePoint content type of an item, such as Item, Document, or Video. | `contenttype:document` | All documents. |
| Created | The date that an item is created. | `created>=2021-06-01` | All items created on or after June 1, 2021. |
| CreatedBy | The person that created or uploaded an item. Be sure to use the user's display name for this property. For all purpose, use *Author* instead as a more reliable way for searching for SharePoint document. | `createdby:"Garth Fort"` | All items created or uploaded by Garth Fort. |
| DetectedLanguage | The language of an item. | `detectedlanguage:english` | All items in English. |
| DocumentLink | The path (URL) of a specific folder on a SharePoint or OneDrive site. If you use this property, be sure to search the site that the specified folder is located in. Use this property instead of the *Site* and *Path* properties. <br> To return items located in subfolders of the folder that you specify for the documentlink property, you have to add /\* to the URL of the specified folder; for example, `documentlink: "https://contoso.sharepoint.com/Shared Documents/*"` | `documentlink:"https://contoso-my.sharepoint.com/personal/garthf_contoso_com/Documents/Private/*"`<br>`documentlink:"https://contoso-my.sharepoint.com/personal/garthf_contoso_com/Documents/Shared with Everyone/*" AND filename:confidential` | The first example returns all items in the specified OneDrive folder. The second example returns documents in the specified site folder (and all subfolders) that contain the word "confidential" in the file name. |
| FileExtension | The extension of a file; for example, docx, one, pptx, or xlsx. | `fileextension:xlsx` | All Excel files (Excel 2007 and later) |
| FileName | The name of a file. | `filename:"marketing plan"`<br>`filename:estimate` | The first example returns files with the exact phrase "marketing plan" in the title. The second example returns files with the word "estimate" in the file name. |
| LastModifiedTime | The date that an item was last changed. | `lastmodifiedtime>=2021-05-01`<br>`lastmodifiedtime>=2021-05-01 AND lastmodifiedtime<=2021-06-01` | The first example returns items that were changed on or after May 1, 2021. The second example returns items changed between May 1, 2021 and June 1, 2021. |
| MipSensitiveLabel | Search for [sensitivity labels](/en-us/purview/sensitivity-labels) applied to items in your organization's data. By using the Condition Builder, users can select the sensitivity label name (for example, Confidential, Highly Confidential, etc.) from the dropdown and then identify the GUID used in KeyQL for the sensitivity label. | `MipSensitiveLabel=f0c0c7ef-3d45-4c95-87bb-6dfc7a081f46` | All items that match the GUID of the sensitivity label. |
| ModifiedBy | The person who last changed an item. Be sure to use the user's display name for this property. | `modifiedby:"Garth Fort"` | All items that were last changed by Garth Fort. |
| SensitiveType | Search for identified and classified [sensitive information types](/en-us/purview/sit-sensitive-information-type-learn-about) in your organization's data. By using the Condition Builder, users can select the sensitive information type name (for example, SSN, credit card, bank account numbers, etc.) from the dropdown and then identify the GUID used in KeyQL for the sensitive information type. | `SensitiveType=“ba147552-2ed1-4a8f-a441-981e94ab1895”` | All items that match the GUID of the sensitive information type. |
| SharedWithUsersOWSUser | Documents that are shared with the specified user and displayed on the **Shared with me** page in the user's OneDrive site. These documents are explicitly shared with the specified user by other people in your organization. When you export documents that match a search query that uses the SharedWithUsersOWSUser property, the documents are exported from the original content location of the person who shared the document with the specified user. For more information, see Searching for site content shared within your organization. | `sharedwithusersowsuser:garthf`<br>`sharedwithusersowsuser:"garthf@contoso.com"` | Both examples return all internal documents that are explicitly shared with Garth Fort and that appear on the **Shared with me** page in Garth Fort's OneDrive account. |
| Size | The size of an item, in bytes. | `size>=1`<br>`size:1..10000` | The first example returns items larger than 1 byte. The second example returns items from 1 through 10,000 bytes in size. |
| Title | The title of the document. The Title property is metadata that's specified in Microsoft Office documents. It's different from the file name of the document. | `title:"communication plan"` | Any document that contains the phrase "communication plan" in the Title metadata property of an Office document. |

## Searchable sensitive data types

You can use eDiscovery search tools in the Microsoft Purview portal to search for sensitive data, such as credit card numbers or social security numbers, stored in documents on SharePoint and OneDrive sites. You can do this by using the `SensitiveType` property and the name (or ID) of a sensitive information type in a keyword query. For example, the query `SensitiveType:"Credit Card Number"` returns documents that contain a credit card number. The query `SensitiveType:"U.S. Social Security Number (SSN)"` returns documents that contain a U.S. social security number.

To see a list of the sensitive information types that you can search for, go to **Data classifications** &gt; **Sensitive info types** in the Microsoft Purview portal. Or you can use the **Get-DlpSensitiveInformationType** cmdlet in Security & Compliance PowerShell to display a list of sensitive information types.

### Limitations for searching sensitive data types

- To search for custom sensitive information types, you need to specify the ID of the sensitive information type in the `SensitiveType` property. Using the name of a custom sensitive information type (as shown in the example for built-in sensitive information types in the previous section) returns no results. Use the **Publisher** column on the **Sensitive info types** page in the Microsoft Purview portal (or the **Publisher** property in PowerShell) to differentiate between built-in and custom sensitive information types. Built-in sensitive data types have a value of `Microsoft Corporation` for the **Publisher** property.

    To display the name and ID for the custom sensitive data types in your organization, run the following command in Security & Compliance PowerShell:

    ```powershell
    Get-DlpSensitiveInformationType | Where-Object {$_.Publisher -ne "Microsoft Corporation"} | FT Name,Id
    ```

    Then you can use the ID in the `SensitiveType` search property to return documents that contain the custom sensitive data type; for example, `SensitiveType:7e13277e-6b04-3b68-94ed-1aeb9d47de37`
- You can't use sensitive information types and the `SensitiveType` search property to search for sensitive data at-rest in Exchange Online mailboxes. This limitation includes 1:1 chat messages, 1:N group chat messages, and team channel conversations in Microsoft Teams because all of this content is stored in mailboxes. However, you can use data loss prevention (DLP) policies to protect sensitive email data in transit. For more information, see [Learn about data loss prevention](dlp-learn-about-dlp) and [Search for and find personal data](/en-us/compliance/regulatory/gdpr).

### Forming a basic query

A basic query has three parts: SensitiveType, count range, and confidence range. For example, **SensitiveType:"&lt;type&gt;"** is required, and both **|&lt;count range&gt;** and **|&lt;confidence range&gt;** are optional.

### Sensitive type - required

Queries typically begin with the property `SensitiveType:"` and an information type name from the [sensitive information types inventory](/en-us/Exchange/what-the-sensitive-information-types-in-exchange-look-for-exchange-2013-help), and end with a `"`. You can also use the name of a [custom sensitive information type](sit-create-a-custom-sensitive-information-type) that you created for your organization. For example, you might be looking for documents that contain credit card numbers.

In such an instance, use the following format: `SensitiveType:"Credit Card Number"`. Because you didn't include count range or confidence range, the query returns every document in which a credit card number is detected. This is the simplest query that you can run, and it returns the most results. Keep in mind that the spelling and spacing of the sensitive type matters.

### Ranges - optional

Both of the next two parts are ranges, so let's quickly examine what a range looks like. In SharePoint queries, a basic range is represented by two numbers separated by two periods, which looks like this: `[number]..[number]`. For instance, if `10..20` is used, that range captures numbers from 10 through 20. This article covers many different range combinations.

Let's add a count range to the query. You can use count range to define the number of occurrences of sensitive information a document needs to contain before it's included in the query results. For example, if you want your query to return only documents that contain exactly five credit card numbers, use this: `SensitiveType:"Credit Card Number|5"`. Count range can also help you identify documents that pose high degrees of risk. For example, your organization might consider documents with five or more credit card numbers a high risk. To find documents fitting this criterion, use this query: `SensitiveType:"Credit Card Number|5.."`. Alternatively, you can find documents with five or fewer credit card numbers by using this query: `SensitiveType:"Credit Card Number|..5"`.

### Confidence range

Finally, confidence range is the level of confidence that the detected sensitive type is actually a match. The values for confidence range work similarly to count range. You can form a query without including a count range. For example, to search for documents with any number of credit card numbers—as long as the confidence range is 85 percent or higher—use this query: `SensitiveType:"Credit Card Number|*|85.."`.

Important

The asterisk ( `*` ) is a wildcard character that means any value works. You can use the wildcard character ( `*` ) either in the count range or in the confidence range, but not in a sensitive type.

### Additional query properties and search operators

Queries in SharePoint also contain the `LastSensitiveContentScan` property, which can help you search for files scanned within a specific timeframe. For query examples with the `LastSensitiveContentScan` property, see the Examples of complex queries in the next section.

You can use SharePoint eDiscovery search properties such as `Author` or `FileExtension`. You can use operators to build complex queries.

### Examples of complex queries

The following examples use different sensitive types, properties, and operators to show how you can refine your queries to find exactly what you're looking for.

| Query | Explanation |
| --- | --- |
| `SensitiveType:"Credit Card Number | 1..4294967295 | 1..100"` | This query returns documents with at least one match to the sensitive type "Credit Card Number." The values for each range are the respective minimum and maximum values. A simpler way to write this query is `SensitiveType:"Credit Card Number"`. |
| `SensitiveType:"Credit Card Number | 5..25" AND LastSensitiveContentScan:"8/11/2018..8/13/2018" NOT FileExtension:XLSX` | This query returns documents with 5-25 credit card numbers that were scanned from August 11, 2018 through August 13, 2018. Files with an XLSX extension aren't included in the query results. `FileExtension` is one of many properties that you can include in a query. For more information, see [Using Search Properties and Operators with eDiscovery](/en-us/archive/blogs/quentin/using-search-properties-and-operators-with-ediscovery). |
| `SensitiveType:"Credit Card Number | 5..25" AND LastSensitiveContentScan:"8/11/2018..8/13/2018"` | This query returns documents with 5-25 credit card numbers that were scanned from August 11, 2018 through August 13, 2018. |
| `SensitiveType:"Credit Card Number" OR SensitiveType:"U.S. Social Security Number (SSN)"` | This query returns documents that contain either a credit card number or a social security number. |
| `SensitiveType:"International Banking Account Number (IBAN)"` | The name might seem strange because it's so long, but it's the correct name for that sensitive type. Make sure to use exact names from the [sensitive information types inventory](/en-us/Exchange/what-the-sensitive-information-types-in-exchange-look-for-exchange-2013-help). You can also use the name of a [custom sensitive information type](sit-create-a-custom-sensitive-information-type) that you created for your organization. |

### Examples of queries to avoid

Not all queries work in SharePoint. The following table gives examples of queries that don't work and describes why.

| Unsupported query | Reason |
| --- | --- |
| `SensitiveType:"Credit Card Number .."` | You must add at least one number. |
| `SensitiveType:"Credit Card Number 0"` | Zero isn't valid as either the minimum value or the maximum value in a range. |
| `SensitiveType:"Credit Card Number 1. .3"` | The two-period portion shouldn't be separated by a space. |
| `SensitiveType:"Credit Card Number 1.. 80.."` | There are too many pipe delimiters `\|`. Follow this format instead: `SensitiveType: "Credit Card Number 1.. 80.."` |
| `SensitiveType:"Credit Card Number 1.. 80..101"` | Because confidence values represent a percentage, they can't exceed 100. Choose a number from 1 through 100 instead. |
| `SensitiveType:"Credit Card Number"` | It might be difficult to see, but there's extra white space between "Credit" and "Card" that makes the query invalid. Use exact sensitive type names from the [sensitive information types inventory](/en-us/Exchange/what-the-sensitive-information-types-in-exchange-look-for-exchange-2013-help). |
| `SensitiveType:"NotARule"` | "NotARule" isn't a valid sensitive type name. Only names in the [sensitive information types inventory](/en-us/Exchange/what-the-sensitive-information-types-in-exchange-look-for-exchange-2013-help) work in eDiscovery queries. |

## Search for site content shared with external users

You can use eDiscovery search tools in the Microsoft Purview portal to search for documents stored on SharePoint and OneDrive sites shared with people outside of your organization. This search can help you identify sensitive or proprietary information that's being shared outside your organization. Use the `ViewableByExternalUsers` property in a keyword query. This property returns documents or sites that you shared with external users by using one of the following sharing methods:

- A sharing invitation that requires users to sign in to your organization as an authenticated user.
- An anonymous guest link, which allows anyone with this link to access the resource without having to be authenticated.

Here are some examples:

- The query `ViewableByExternalUsers:true AND SensitiveType:"Credit Card Number"` returns all items shared with people outside your organization and contains a credit card number.
- The query `ViewableByExternalUsers:true AND ContentType:document AND site:"https://contoso.sharepoint.com/Sites/Teams"` returns a list of documents on all team sites in the organization that you shared with external users.

Tip

A search query such as `ViewableByExternalUsers:true AND ContentType:document` might return numerous .aspx files in the search results. To eliminate these or other types of files, use the `FileExtension` property to exclude specific file types; for example `ViewableByExternalUsers:true AND ContentType:document NOT FileExtension:aspx`.

What content counts as shared with people outside your organization? Documents in your organization's SharePoint and OneDrive sites that you shared by sending a sharing invitation or that you shared in public locations. For example, the following user activities result in content that external users can view:

- A user shares a file or folder with a person outside your organization.
- A user creates and sends a link to a shared file to a person outside your organization. This link allows the external user to view (or edit) the file.
- A user sends a sharing invitation or a guest link to a person outside your organization to view (or edit) a shared file.

### Issues using the ViewableByExternalUsers property

While the `ViewableByExternalUsers` property represents the status of whether a document or site is shared with external users, it has some caveats. In the following scenarios, the value of the `ViewableByExternalUsers` property isn't updated, and the results of a search query that uses this property might be inaccurate.

- Changes to sharing policy, such as turning off external sharing for a site or for the organization. The property still shows previously shared documents as being externally accessible even though external access might be revoked.
- Changes to group membership, such as adding or removing external users to Microsoft 365 Groups or Microsoft 365 security groups. The property isn't automatically updated for items the group has access to.
- Sending sharing invitations to external users where the recipient hasn't accepted the invitation, and therefore doesn't yet have access to the content.

In these scenarios, the `ViewableByExternalUsers` property doesn't reflect the current sharing status until the site or document library is recrawled and reindexed.

## Search for site content shared within your organization

You can use the `SharedWithUsersOWSUser` property to search for documents shared between people in your organization. When a person shares a file or folder with another user inside your organization, a link to the shared file appears on the **Shared with me** page in the OneDrive account of the person who the file was shared with. For example, to search for the documents shared with Sara Davis, you can use the query `SharedWithUsersOWSUser:"sarad@contoso.com"`. If you export the results of this search, you download the original documents located in the content location of the person who shared the documents with Sara.

Documents must be explicitly shared with a specific user to be returned in search results when using the `SharedWithUsersOWSUser` property. For example, when a person shares a document in their OneDrive account, they can share it with anyone (inside or outside the organization), share it only with people inside the organization, or share it with a specific person.

Only documents that are shared by using the third option (shared with **Specific people**) are returned by a search query that uses the `SharedWithUsersOWSUser` property.

## Character limits for searches

For more information about character limits, see [eDiscovery search limits](edisc-ref-limits).