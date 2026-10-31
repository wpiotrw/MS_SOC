---
layout: Conceptual
title: Configure search permissions filtering in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-permission-filtering
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use search permissions filtering in eDiscovery to let eDiscovery managers search only a subset of mailboxes and sites in your organization.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-29T00:00:00.0000000Z
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
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: e80c0355-b4f2-d774-f202-a8aac1ddf26a
document_version_independent_id: e80c0355-b4f2-d774-f202-a8aac1ddf26a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-permission-filtering.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-permission-filtering
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-permission-filtering.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 7ac9da79-8f24-96ae-fbdc-b6beadf1509e
---

# Configure search permissions filtering in eDiscovery | Microsoft Learn

Use search permissions filtering to let an eDiscovery manager search only a subset of mailboxes and sites in your organization. You can also use permissions filtering to let that same eDiscovery manager search only for mailbox or site content that meets a specific search criteria.

For example, you might want an eDiscovery manager to search only the mailboxes of users in a specific location or department. Create a filter that uses a supported recipient filter to limit which mailboxes a specific user or group of users can search. You can also create a filter that specifies what mailbox content a user can search for. This filter uses a searchable message property. Similarly, you can let an eDiscovery manager search only specific SharePoint sites in your organization. Create a filter that limits which site can be searched. You can also create a filter that specifies what site content can be searched. This filter uses a searchable site property.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Understand search permissions filters

The Microsoft Purview portal applies search permissions filters when you search for content. When you apply a search permissions filter to a specific user, that user can perform the following search-related actions:

- Search for content
- Preview search results
- Export search results
- Purge items returned by a search

Use search permissions filtering to create logical boundaries (called *compliance boundaries*) within an organization that control the user content locations (such as mailboxes, SharePoint sites, and OneDrive accounts) that specific eDiscovery managers can search. For more information, see [Set up compliance boundaries for eDiscovery investigations](edisc-compliance-boundaries).

The following four cmdlets in [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell) let you configure and manage search permissions filters:

- New-ComplianceSecurityFilter
- Get-ComplianceSecurityFilter
- Set-ComplianceSecurityFilter
- Remove-ComplianceSecurityFilter

## Requirements to configure permissions filtering

Before you configure permissions filtering, make sure the following requirements are met:

- To run the compliance security filter cmdlets, you need to be a member of the *Organization Management* role group and have the *eDiscovery administrator* role assigned in the Microsoft Purview portal. For more information, see [Permissions in the Security & Compliance Center](/en-us/microsoft-365/security/office-365-security/scc-permissions?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).
- You need to connect to both Exchange Online and Security & Compliance PowerShell to use the compliance security filter cmdlets. These cmdlets require access to mailbox properties, which is why you need to connect to Exchange Online PowerShell. See the steps in Connect to Exchange Online and Security & Compliance PowerShell in a single session.
- See the Additional considerations for search permissions filtering section for additional information about search permissions filters.
- Search permissions filtering applies to inactive mailboxes, which means you can use mailbox and mailbox content filtering to limit who can search an inactive mailbox. See the Additional considerations for search permissions filtering section for additional information about permissions filtering and inactive mailboxes.
- You can't use search permissions filtering to limit who can search public folders in Exchange.

Note

You can create unlimited search permission filters in an organization. However, a search query can have a maximum of 100 conditions. In this case, a condition is something that's connected to the query by a Boolean operator, such as **AND**, **OR**, and **NEAR**. The limit for the number of conditions includes the search query itself plus all search permissions filters that the user who runs the search applies. Therefore, the more search permissions filters you have - especially if these filters are applied to the same user or group of users - the better the chance of exceeding the maximum number of conditions for a search. To prevent your organization from reaching the conditions limit, keep the number of search permissions filters in your organization as few as possible to meet your business requirements. For more information, see [Set up compliance boundaries for eDiscovery investigations](edisc-compliance-boundaries#frequently-asked-questions).

## Connect to Exchange Online and Security & Compliance PowerShell in a single session

Before you can successfully run the script in this section, you need to download and install the Exchange Online PowerShell module. For information, see [Install and maintain the Exchange Online PowerShell module](/en-us/powershell/exchange/exchange-online-powershell-v2#install-and-maintain-the-exchange-online-powershell-module).

1. Save the following text to a Windows PowerShell script file by using a filename suffix of **.ps1**. For example, you could save it to a file named **ConnectEXO-SCC.ps1**.

    ```powershell
    Import-Module ExchangeOnlineManagement
    $UserCredential = Get-Credential
    Connect-ExchangeOnline -Credential $UserCredential -ShowBanner:$false
    Connect-IPPSSession -Credential $UserCredential
    $Host.UI.RawUI.WindowTitle = $UserCredential.UserName + " (Exchange Online + Security & Compliance)"
    ```
2. On your local computer, open Windows PowerShell, go to the folder where the script that you created in the previous step is located, and then run the script. For example:

    ```powershell
    .\ConnectEXO-SCC.ps1
    ```

How do you know if this worked? After you run the script, cmdlets from Exchange Online PowerShell and Security & Compliance PowerShell are available. If you don't receive any errors, you connected successfully. A quick test is to run Exchange Online PowerShell and Security & Compliance PowerShell cmdlets. For example, you can run **Get-Mailbox** and **Get-ComplianceSearch**.

For troubleshooting PowerShell connection errors, see:

- [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell#how-do-you-know-this-worked)
- [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell#how-do-you-know-this-worked)

## Create a search permissions filter with New-ComplianceSecurityFilter

Use the **New-ComplianceSecurityFilter** cmdlet to create a search permissions filter. Here's the basic syntax for this cmdlet:

```powershell
New-ComplianceSecurityFilter -FilterName <name of filter> -Users <user or role group> -Filters <filter>
```

The following sections describe the parameters for this cmdlet. You need all parameters to create a search permissions filter.

### Specify the FilterName parameter

Use the *FilterName* parameter to specify the name of the permissions filter. Use this name to identify a filter when using the **Get-ComplianceSecurityFilter**, **Set-ComplianceSecurityFilter**, and **Remove-ComplianceSecurityFilter** cmdlets.

### Specify the Filters parameter

Use the *Filters* parameter to specify the search criteria for the compliance security filter. You can create three different types of filters:

- **Mailbox or OneDrive filtering:** This filter specifies the mailboxes and OneDrive accounts that assigned users (specified by the *Users* parameter) can search. This filter is called a *content location* filter because it defines the content locations that a user can search. The syntax for this filter is \*\*Mailbox\_\*\**MailboxPropertyName*, where *MailboxPropertyName* specifies a mailbox property used to scope the mailboxes and OneDrive accounts that can be searched. For example, the mailbox filter `"Mailbox_CustomAttribute10 -eq 'OttawaUsers'"` allows the user assigned this filter to search only the mailboxes and OneDrive accounts that have the value "OttawaUsers" in the CustomAttribute10 property.

    You can use any supported filterable recipient property for the *MailboxPropertyName* property in a mailbox or OneDrive filter. The following table lists four commonly used recipient properties used to create a mailbox or OneDrive filter. The table also includes an example of using the property in a filter.

    | Property name | Example |
    | --- | --- |
    | Alias | `"Mailbox_Alias -like 'v-'"` |
    | Company | `"Mailbox_Company -eq 'Contoso'"` |
    | CountryOrRegion | `"Mailbox_CountryOrRegion -eq 'United States'"` |
    | Department | `"Mailbox_Department -eq 'Finance'"` |

Note

The Mailbox filter applies to user and group mailboxes. The filter also includes the associated OneDrive site for the user mailbox and SharePoint sites associated to the group mailbox.

- **Mailbox content filtering:** This filter applies to the content that can be searched. This filter is called a *content filter* because it specifies the mailbox content or searchable email properties the assigned users can search for. The syntax for this filter is \*\*MailboxContent\_\*\**SearchablePropertyName*, where *SearchablePropertyName* specifies a Keyword Query Language (KeyQL) property that can be specified in a search. For example, the mailbox content filter `"MailboxContent_Recipients  -like 'contoso.com'"` allows the user assigned this filter to only search for messages sent to recipients in the contoso.com domain. For a list of searchable email properties, see [Keyword queries and search conditions for eDiscovery](edisc-search-mailboxes#searchable-email-properties-in-keyql).

    Important

    Within a *single component* of the `Filters` parameter, you can't mix a mailbox filter and a mailbox content filter (for example, you can't combine `Mailbox_*` and `MailboxContent_*` together with `-and` inside one quoted string). To combine these types in a single security filter, put each in its own component of a filters list that combines filter types — separate them with a comma. A single component can contain a more complex query of the *same* type — for example, `"Mailbox_CustomAttribute10 -eq 'FTE' -and Mailbox_MemberOfGroup -eq '$($DG.DistinguishedName)'"`.
- **Site and site content filtering:** You can use two SharePoint- and OneDrive-related filters to specify what site or site content the assigned users can search.

    - **Site\_***QueryableSiteProperty*
    - **SiteContent\_***QueryableSiteProperty*

    These two filters are interchangeable. For example, `"Site_Path -like 'https://contoso.sharepoint.com/sites/doctors'"` and `"SiteContent_Path -like 'https://contoso.sharepoint.com/sites/doctors'"` return the same results. For a list of searchable site properties, see [Keyword queries and search conditions for eDiscovery](edisc-search-sites#searchable-site-properties-in-keyql). For a more complete list, see [Overview of crawled and managed properties in SharePoint](/en-us/SharePoint/technical-reference/crawled-and-managed-properties-overview). Properties marked with a **Yes** in the **Queryable** column can be used to create a site or site content filter.

    Important

    Setting up a site filter with one of the supported properties doesn't mean the site property in the filter propagates to all documents on that site. This condition means the user is still responsible for populating the specific property fields associated with the documents on that site in order for the site filter to work and capture the right content. For example, if the user has a security filter "Site\_RefineableString00 -eq 'abc'" applied and then the user runs a search using keyword query "xyz". The security filter gets appended to the query and the actual query running would be "xyz **AND RefineableString0:'abc'**". The user needs to ensure that documents on the site have values in the RefineableString00 field as "abc". If not, the search query won't return any results.

Keep the following considerations in mind when configuring the *Filters* parameter for search permissions filters:

- Unlike mailboxes, there isn't a content location filter for sites even though the *Site* filter looks like a location filter. All filters for SharePoint and OneDrive are content filters (which is also why *Site\_* and *SiteContent\_* filters are interchangeable) because site-related properties like *Path* are stamped directly on the documents. This design is a result of the way that SharePoint is designed. In SharePoint, there isn't a "site object" with properties, like there is with Exchange mailboxes. Therefore, the *Path* property is stamped on the document and contains the URL of the site where the document is located. This design is why a *Site* filter is considered a content filter and not a content location filter.
- You have to create a search permissions filter to explicitly prevent users from searching content locations in a specific service (such as preventing a user from searching any Exchange mailbox or any SharePoint site). In other words, creating a search permissions filter that allows a user to search all SharePoint sites in the organization doesn't prevent that user from searching mailboxes. For example, to allow SharePoint admins to only search SharePoint sites, you have to create a filter that prevents them from searching mailboxes. Similarly, to allow Exchange admins to only search mailboxes, you have to create a filter that prevents them from searching sites.

### Specify the Users parameter

Use the *Users* parameter to specify the users who get the filter applied to their searches. Identify users by their alias or primary SMTP address. You can specify multiple values separated by commas, or you can assign the filter to all users by using the value **All**.

Use the *User* parameter to specify a Microsoft Purview portal role group. This approach lets you create a custom role group and then assign that role group a search permissions filter. For example, suppose you have a custom role group for eDiscovery managers for the U.S. subsidiary of a multinational corporation. You can use the *Users* parameter to specify this role group (by using the Name property of the role group) and then use the *Filter* parameter to allow only mailboxes in the U.S. to be searched. You can't specify distribution groups with this parameter.

### Use a filters list to combine filter types

A *filters list* is a `Filters` value that contains more than one filter component, with the components separated by commas. A single security filter can mix two different content-location filters (`Mailbox_*` and `Site_*`), or it can mix a content-location filter with a content filter on the same workload (`Mailbox_*` plus `MailboxContent_*`, or `Site_*` plus `SiteContent_*`). Each component is a separate quoted string in the `Filters` parameter.

```powershell
-Filters "Mailbox_CustomAttribute10 -eq 'OttawaUsers'", "SiteContent_Path -like 'https://contoso.sharepoint.com/sites/doctors'"
```

How a filters list composes depends on the **classes** of the components. There are two filter classes:

- **Content-location filters** — `Mailbox_*` and `Site_*`. These filters define *which* content locations the assigned user can search.
- **Content filters** — `MailboxContent_*` and `SiteContent_*`. These filters define *what* content can be returned from the locations allowed by the corresponding location filter.

The composition rules are:

| Components in the filters list | Logical composition |
| --- | --- |
| Two content-location filters for different workloads (`Mailbox_*` and `Site_*`) | **OR** across workloads. The user is granted access to mailboxes matching the `Mailbox_*` predicate *or* sites matching the `Site_*` predicate. This composition is the original "comma = OR" behavior described in earlier versions of this article. |
| A content-location filter and a content filter for the *same* workload (`Mailbox_*` plus `MailboxContent_*`, or `Site_*` plus `SiteContent_*`) | **Layered AND**. The location filter narrows which content locations are searchable, and the content filter further restricts which items can be returned from those locations. Both conditions must be satisfied for an item to be returned. |
| Multiple components of the *same* class (for example, two `Mailbox_*` components, or two `MailboxContent_*` components) | **OR** within the class. Multiple mailbox rules combine to expand the allowed location set; multiple mailbox-content rules combine to expand the allowed content set. The combined content set is then AND'd with the user's search query (see How does search permissions filtering work?). |

The preceding example contains a `Mailbox_*` filter and a `SiteContent_*` filter - two location filters for different workloads - so the comma is OR (mailboxes matching the first predicate *or* SharePoint content matching the second).

Compare that composition to the following example, which contains a `Mailbox_*` location filter and a `MailboxContent_*` content filter for the same workload - the comma here is a layered AND (mailboxes that are members of the group *and*, within those mailboxes, only items that aren't Microsoft 365 Copilot interactions):

```powershell
-Filters "Mailbox_MemberOfGroup -eq 'CN=Litigation Hold Group,OU=Groups,DC=contoso,DC=com'", "MailboxContent_ItemClass -notlike 'IPM.SkypeTeams.Message.Copilot*'"
```

An alternative to using a filters list is to create two separate search permissions filters and assign them to the same user - the behavior described in How does search permissions filtering work? applies (multiple security filters are OR'd together at evaluation time). When the two components fall into different *classes* (location vs. content), the filters list and the two-separate-filters approaches are *not* equivalent - prefer the filters list to keep the layered AND semantics within a single filter.

Keep the following things in mind about using a filters list:

- You must use a filters list to create a filter that includes a `Mailbox` filter and a `MailboxContent` filter (or a `Site` filter and a `SiteContent` filter). Within a single quoted component, you can't combine the two classes with `-and`.
- Each component of a filters list can contain a complex filter syntax. For example, the mailbox and site filters can contain multiple filters separated by an **-or** operator:

    ```powershell
    -Filters "Mailbox_Department -eq 'CohoWinery' -or Mailbox_CustomAttribute10 -eq 'CohoUsers'", "SiteContent_Path -like 'https://contoso.sharepoint.com/sites/CohoWinery*'"
    ```

## Examples of creating search permissions filters

The following examples show how to use the **New-ComplianceSecurityFilter** cmdlet to create a search permissions filter.

The first example enables members of the "US Discovery Managers" role group to search only the mailboxes and OneDrive accounts in the United States.

```powershell
New-ComplianceSecurityFilter -FilterName USDiscoveryManagers  -Users "US Discovery Managers" -Filters "Mailbox_CountryOrRegion  -eq 'United States'"
```

The second example enables the user annb@contoso.com to perform search actions only for mailboxes and OneDrive accounts in Canada. This filter contains the three-digit numeric country code for Canada from ISO 3166-1.

```powershell
New-ComplianceSecurityFilter -FilterName CountryFilter  -Users annb@contoso.com -Filters "Mailbox_CountryCode  -eq '124'"
```

The third example enables the users *donh* and *suzanf* to search only the mailboxes and OneDrive accounts that have the value 'Marketing' for the CustomAttribute1 mailbox property.

```powershell
New-ComplianceSecurityFilter -FilterName MarketingFilter  -Users donh,suzanf -Filters "Mailbox_CustomAttribute1  -eq 'Marketing'"
```

The fourth example enables members of the "Fourth Coffee eDiscovery Managers" role group to search only the mailboxes and OneDrive accounts that have the value 'FourthCoffee' for the Department mailbox property. The filter also enables the role group members to search for documents in the Fourth Coffee SharePoint site.

```powershell
New-ComplianceSecurityFilter -FilterName "Fourth Coffee Security Filter" -Users "Fourth Coffee eDiscovery Managers", "Fourth Coffee Investigators" -Filters "Mailbox_Department -eq 'FourthCoffee'", "SiteContent_Path -like 'https://contoso.sharepoint.com/sites/FourthCoffee*' -or SiteContent_Path -like 'https://contoso-my.sharepoint.com/personal*'"
```

Note

In the previous example, you need to include an additional site content filter (`SiteContent_Path -like 'https://contoso-my.sharepoint.com/personal*'`) so that role group members can search for documents in OneDrive accounts. If you don't include this filter, the filter only enables role group members to search for documents located in `https://contoso.sharepoint.com/sites/FourthCoffee`.

The fifth example enables members of the eDiscovery Manager role group to search only the mailboxes and OneDrive accounts of members of the Ottawa Users distribution group. The `Get-DistributionGroup` cmdlet in Exchange Online PowerShell is used to find the members of the Ottawa Users group.

```powershell
$DG = Get-DistributionGroup "Ottawa Users"
```

```powershell
New-ComplianceSecurityFilter -FilterName DGFilter  -Users eDiscoveryManager -Filters "Mailbox_MemberOfGroup -eq '$($DG.DistinguishedName)'"
```

The sixth example prevents any user from performing search actions on the mailboxes and OneDrive accounts of members of the Executive Team distribution group. That means users can delete content from these mailboxes. The `Get-DistributionGroup` cmdlet in Exchange Online PowerShell is used to find the members of the Executive Team group.

```powershell
$DG = Get-DistributionGroup "Executive Team"
```

```powershell
New-ComplianceSecurityFilter -FilterName NoExecutivesPreview  -Users All -Filters "Mailbox_MemberOfGroup -ne '$($DG.DistinguishedName)'"
```

The seventh example enables members of the OneDrive eDiscovery Managers custom role group to only search for content in OneDrive accounts in the organization.

```powershell
New-ComplianceSecurityFilter -FilterName OneDriveOnly  -Users "OneDrive eDiscovery Managers" -Filters "SiteContent_Path -like 'https://contoso-my.sharepoint.com/personal*'"
```

The eighth example restricts the user to performing search actions only on email messages sent during the calendar year 2015.

```powershell
New-ComplianceSecurityFilter -FilterName EmailDateRestrictionFilter -Users donh@contoso.com -Filters "MailboxContent_Received -ge '01-01-2015' -and MailboxContent_Received -le '12-31-2015'"
```

Similar to the previous example, the ninth example restricts the user to performing search actions only on documents that were last changed sometime in the calendar year 2015.

```powershell
New-ComplianceSecurityFilter -FilterName DocumentDateRestrictionFilter -Users donh@contoso.com -Filters "SiteContent_LastModifiedTime -ge '01-01-2015' -and SiteContent_LastModifiedTime -le '12-31-2015'"
```

The tenth example prevents members of the "OneDrive Discovery Managers" role group from performing search actions on any mailbox in the organization.

```powershell
New-ComplianceSecurityFilter -FilterName NoEXO -Users "OneDrive Discovery Managers" -Filters "Mailbox_Alias -notlike '*'"
```

The eleventh example prevents anyone in the organization from performing search actions on email messages that were sent or received by janets or sarad.

```powershell
New-ComplianceSecurityFilter -FilterName NoSaraJanet -Users All -Filters "MailboxContent_Participants -notlike 'janets@contoso.onmicrosoft.com' -and MailboxContent_Participants -notlike 'sarad@contoso.onmicrosoft.com'"
```

The twelfth example uses a filters list to combine mailbox and site filters. In this example, the mailbox filter is a content location filter and the site filter is a content filter.

```powershell
New-ComplianceSecurityFilter -FilterName "Coho Winery Security Filter" -Users "Coho Winery eDiscovery Managers", "Coho Winery Investigators" -Filters "Mailbox_Department -eq 'CohoWinery'", "SiteContent_Path -like 'https://contoso.sharepoint.com/sites/CohoWinery*'"
```

## View search permissions filters with Get-ComplianceSecurityFilter

Use **Get-ComplianceSecurityFilter** to return a list of search permissions filters. Use the *FilterName* parameter to return information for a specific search filter.

## Modify a search permissions filter with Set-ComplianceSecurityFilter

Use **Set-ComplianceSecurityFilter** to modify an existing search permissions filter. The following sections describe the parameters for this cmdlet. The only required parameter is *FilterName*.

### FilterName

Use the *FilterName* parameter to specify the name of the permissions filter.

### Users

Use the *Users* parameter to specify the users who get this filter applied to their searches. Because this parameter is a multivalue property, specifying a user or group of users overwrites the existing list of users. See the following examples for the syntax to add and remove selected users.

You can also use the *Users* parameter to specify a Microsoft Purview portal role group. This role group lets you create a custom role group and then assign that role group a search permissions filter. For example, suppose you have a custom role group for eDiscovery managers for the U.S. subsidiary of a multinational corporation. Use the *Users* parameter to specify this role group (by using the Name property of the role group) and then use the *Filters* parameter to allow only mailboxes in the U.S. to be searched. You can't specify distribution groups with this parameter.

### Filters

Use the *Filters* parameter to specify the search criteria for the compliance security filter. You can create three different types of filters:

- **Mailbox and OneDrive filtering:** This filter specifies the mailboxes and OneDrive accounts that assigned users (specified by the *Users* parameter) can search. The syntax for this filter is **Mailbox\_***MailboxPropertyName*. The *MailboxPropertyName* specifies a mailbox property used to scope the mailboxes that can be searched. For example, the mailbox filter `"Mailbox_CustomAttribute10 -eq 'OttawaUsers'"` allows the user assigned this filter to search only the mailboxes that have the value "OttawaUsers" in the CustomAttribute10 property. For the *MailboxPropertyName* property, you can use any supported filterable recipient property. For a list of supported properties, see [Filterable properties for the -RecipientFilter parameter](/en-us/powershell/exchange/recipientfilter-properties).
- **Mailbox content filtering:** This filter applies to the content that can be searched. It specifies the mailbox content that assigned users can search. The syntax for this filter is **MailboxContent\_***SearchablePropertyName*. The *SearchablePropertyName* specifies a Keyword Query Language (KQL) property that you can specify in a search. For example, the mailbox content filter `"MailboxContent_Recipients  -like 'contoso.com'"` allows the user assigned this filter to only search for messages sent to recipients in the contoso.com domain. For a list of searchable email properties, see [Use the condition builder to create search queries in eDiscovery](edisc-condition-builder).
- **Site and site content filtering:** Use two SharePoint and OneDrive for Business site-related filters to specify what site or site content the assigned users can search:

    - **Site\_***SearchableSiteProperty*
    - **SiteContent\_***SearchableSiteProperty*

    These two filters are interchangeable. For example, `"Site_Path -like 'https://contoso.spoppe.com/sites/doctors*'"` and `"SiteContent_Path -like 'https://contoso.spoppe.com/sites/doctors*'"` return the same results. For a list of searchable site properties, see [Overview of crawled and managed properties in SharePoint](/en-us/SharePoint/technical-reference/crawled-and-managed-properties-overview). Properties marked with a **Yes** in the **Queryable** column can be used to create a site or site content filter.

### Examples of changing search permissions filters

These examples show how to use the **Get-ComplianceSecurityFilter** and **Set-ComplianceSecurityFilter** cmdlets to add or remove a user from the existing list of users that the filter is assigned to. When you add or remove users from a filter, specify the user by using their SMTP address.

This example adds a user to the filter.

```powershell
$filterusers = Get-ComplianceSecurityFilter -FilterName OttawaUsersFilter
```

```powershell
$filterusers.users.add("pilarp@contoso.com")
```

```powershell
Set-ComplianceSecurityFilter -FilterName OttawaUsersFilter -Users $filterusers.users
```

This example removes a user from the filter.

```powershell
$filterusers = Get-ComplianceSecurityFilter -FilterName OttawaUsersFilter
```

```powershell
$filterusers.users.remove("annb@contoso.com")
```

```powershell
Set-ComplianceSecurityFilter -FilterName OttawaUsersFilter -Users $filterusers.users
```

## Remove a search permissions filter with Remove-ComplianceSecurityFilter

Use the **Remove-ComplianceSecurityFilter** cmdlet to delete a search filter. Use the *FilterName* parameter to specify the filter you want to delete.

## Additional considerations for search permissions filtering

**How does search permissions filtering work?** When you run a search, the permissions filter is added to the search query. The **AND** Boolean operator connects the permissions filter to the search query. The query logic for the search query and the permissions filter looks like this:

```text
<SearchQuery> AND <PermissionsFilter>
```

For example, you have a permissions filter that allows Bob to perform all search actions on the mailboxes of members of the Workers distribution group. Then Bob runs a search on all mailboxes in the organization with the search query `sender:jerry@adatum.com`. Because the permissions filter and the search query are logically combined by an **AND** operator, the search returns any message sent by jerry@adatum.com to any member of the Workers distribution group.

**What happens if you have multiple search permissions filters?** In a search query, multiple permissions filters are combined by **OR** Boolean operators. So results are returned if any of the filters are true. In a search, all filters (combined by **OR** operators) are then combined with the search query by the **AND** operator.

```text
<SearchQuery> AND  (<PermissionsFilter1> OR <PermissionsFilter2> OR <PermissionsFilter3>)
```

Let's take the previous example, where a search filter allows Bob to search only the mailboxes of the members of the Workers distribution group. Then we create another filter that prevents Bob from searching Phil's mailbox ("Mailbox\_Alias -ne 'Phil'"). And let's also assume that Phil is a member of the Workers group. When Bob runs a search (from the previous example) on all mailboxes in the organization, search results are returned for Phil's mailbox even though you applied filter to prevent Bob from searching Phil's mailbox. This is because the first filter, which allows Bob to search the Workers group, is true. And because Phil is a member of the Workers group, Bob can search Phil's mailbox.

**How are filter components within a single security filter combined?** Filters within a single security filter are evaluated in two layers:

1. **Mailbox filters first.** All `Mailbox_*` components in the filter are evaluated and combined with **OR** to produce the set of allowed mailbox locations. If multiple `Mailbox_*` rules are present (whether across components of a filters list or within a single component using `-or`), they combine as OR to expand the location set.
2. **Mailbox content filters next, scoped to those locations.** All `MailboxContent_*` components are then applied to content within the allowed mailbox locations from step 1. If multiple `MailboxContent_*` rules are present, they combine with **OR**. The combined `MailboxContent_*` predicate is then **AND**'d to the user's search query.

The same two-layer model applies to SharePoint and OneDrive: `Site_*` location filters compose with OR to define the allowed sites, and `SiteContent_*` filters compose with OR and are then AND'd to the user's search query, scoped to those sites.

```text
(<MailboxRule1> OR <MailboxRule2> ...)           // Layer 1: location scope
  AND
((<MailboxContentRule1> OR <MailboxContentRule2> ...) AND <SearchQuery>)   // Layer 2: content
```

For example, the filter `-Filters "Mailbox_MemberOfGroup -eq 'CN=Litigation Hold Group,...'", "MailboxContent_ItemClass -notlike 'IPM.SkypeTeams.Message.Copilot*'"` means: only mailboxes that are members of the group are searchable, and within those mailboxes, the user can return any item *except* Microsoft 365 Copilot interactions. Items that match the user's search query, are in an allowed mailbox, and pass the content filter are returned.

**Does search permissions filtering work for inactive mailboxes?** Yes, you can use mailbox and mailbox content filters to limit who can search inactive mailboxes in your organization. Like a regular mailbox, an inactive mailbox must be configured with the recipient property that's used to create a permissions filter. If necessary, you can use the **Get-Mailbox -InactiveMailboxOnly** command to display the properties of inactive mailboxes. For more information, see [Create and manage inactive mailboxes](create-and-manage-inactive-mailboxes).

**Does search permissions filtering work for public folders?** No. Search permissions filtering can't be used to limit who can search public folders in Exchange. For example, items in public folder locations can't be excluded from the search results by a permissions filter.

**Does allowing a user to search all content locations in a specific service also prevent them from searching content locations in a different service?** No. You have to create a search permissions filter to explicitly prevent users from searching content locations in a specific service (such as preventing a user from searching any Exchange mailbox or any SharePoint site). In other words, creating a search permissions filter that allows a user to search all SharePoint sites in the organization doesn't prevent that user from searching mailboxes. For example, to allow SharePoint admins to only search SharePoint sites, you have to create a filter that prevents them from searching mailboxes. Similarly, to allow Exchange admins to only search mailboxes, you have to create a filter that prevents them from searching sites.

**Do search permissions filters count against search query character limits?** Yes. Search permissions filters count against the character limit for search queries. For more information, see [Limits in eDiscovery](edisc-ref-limits).

**What is the maximum number of search permissions filters that can be created in an organization?**

There's no limit to the number of search permissions filters that can be created in an organization. However, a search query can have a maximum of 100 conditions. In this case, a condition is defined as something that's connected to the query by a Boolean operator (such as **AND**, **OR**, and **NEAR**). The limit of the number of conditions includes the search query itself plus all search permissions filters that are applied to the user who runs the search. Therefore, the more search permissions filters you have (especially if these filters are applied to the same user or group of users), the better the chance of exceeding the maximum number of conditions for a search.

To understand how this limit works, you need to understand that a search permissions filter is appended to the search query when a search is run. A search permissions filter is joined to the search query by the **AND** Boolean operator. The query logic for the search query and a single search permissions filter looks like this:

```text
<SearchQuery> AND <PermissionsFilter>
```

Multiple search permissions filters are combined together by the **OR** Boolean operator, and then those conditions are connected to the search query by the **AND** operator.

The query logic for the search query and multiple search permissions filters looks like this:

```text
<SearchQuery> AND (<PermissionsFilter1> OR <PermissionsFilter2> OR <PermissionsFilter3>...)
```

It's possible the search query itself might consist of multiple conditions connected by Boolean operators. Each condition in the search query also counts against the 100-condition limit.

Also, the number of search permissions filters appended to a query depends on the user who is running the search. When a specific user runs a search, the search permissions filters that are applied to the user (which is defined by the *Users* parameter in the filter) are appended to the query. Your organization could have hundreds of search permissions filters, but if more than 100 filters are applied to the same users, then it's likely the 100-condition limit is exceeded when those users run searches.

There's one more thing to keep in mind about the condition limit. The number of specific SharePoint sites that are included in the search query or search permissions filters also count against this limit.

To prevent your organization from reaching the conditions limit, keep the number of search permissions filters in your organization as few as possible to meet your business requirements.