---
layout: Conceptual
title: Set up compliance boundaries in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to set up compliance boundaries that control which content locations eDiscovery managers can search in Microsoft Purview eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-09-19T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
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
ms.custom: msecd-doc-authoring-1028
locale: en-us
document_id: 54c43527-0541-0e4d-21b9-214fa99b5d4f
document_version_independent_id: 54c43527-0541-0e4d-21b9-214fa99b5d4f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-compliance-boundaries.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-compliance-boundaries
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-compliance-boundaries.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 55feb23c-dd4a-eaf4-aab3-1a6afd7af9e2
---

# Set up compliance boundaries in eDiscovery | Microsoft Learn

Compliance boundaries create logical boundaries within an organization that control the user content locations, such as mailboxes, OneDrive accounts, and SharePoint sites, that eDiscovery managers can search. Compliance boundaries also apply to searches in [Data Security Investigations](data-security-investigations). Compliance boundaries control who can access eDiscovery cases used to manage the legal, human resources, or other investigations within your organization. Compliance boundaries control search scope within eDiscovery and DSI only. They don't restrict access in other Microsoft Purview or Defender solutions.

You often need compliance boundaries for multinational corporations that have to respect geographical borders and regulations, and for governments that are divided into different agencies. In Microsoft 365, compliance boundaries help you meet these requirements when performing content searches and managing investigations by using eDiscovery cases.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

Note

**SharePoint Embedded container support in eDiscovery (preview):** Compliance boundary enforcement isn't currently supported for SharePoint Embedded containers. For supported container scenarios and other limitations, see [Data sources in eDiscovery](edisc-data-sources#sharepoint-embedded-application-content).

## Scenario example

The following illustration shows how compliance boundaries work.

![Diagram that shows how search permissions filters control agency content access and role groups control access to eDiscovery cases.](media/m365_complianceboundary_orgchart_v2.png)

In this example, Contoso LTD is an organization that consists of two subsidiaries, Fourth Coffee and Coho Winery. The business requires that eDiscovery managers and investigators can only search the Exchange mailboxes, OneDrive accounts, and SharePoint sites in their agency. Also, eDiscovery managers and investigators can only see eDiscovery cases in their agency, and they can only access the cases that they're a member of. In this scenario, investigators can't place content locations on hold or export content from a case. Here's how compliance boundaries meet these requirements.

- The search permissions filtering functionality for eDiscovery controls the content locations that eDiscovery managers and investigators can search. This control means eDiscovery managers and investigators in the Fourth Coffee agency can only search content locations in the Fourth Coffee subsidiary. The same restriction applies to the Coho Winery subsidiary.
- [Role groups](edisc-permissions#rbac-roles-related-to-ediscovery) provide the following functions for compliance boundaries:

    - Control who can see the eDiscovery cases in the Microsoft Purview portal. This control means that eDiscovery managers and investigators can only see the eDiscovery cases in their agency.
    - Control who can assign members to an eDiscovery case. This control means eDiscovery managers and investigators can only assign members to cases that they themselves are a member of.
    - Control the eDiscovery-related tasks that members can perform by adding or removing roles that assign specific permissions.
- When a search permissions filter is applied to a role group, members of the role group can perform the following search-related actions as long as the permissions to perform an action are assigned to the role group:

    - Search for content
    - Preview search results
    - Export search results
    - Purge items returned by a search

## Before you set up compliance boundaries

- Assign users an Exchange Online license. To verify assignments, use the [Get-User](/en-us/powershell/module/exchange/get-user) cmdlet in Exchange Online PowerShell.

## Set up compliance boundaries

Complete the following steps to set up compliance boundaries:

- Step 1: Identify a user attribute to define your agencies
- Step 2: Create a role group for each agency
- Step 3: Create a search permissions filter to enforce the compliance boundary
- Step 4: Create an eDiscovery case for intra-agency investigations

### Step 1: Identify a user attribute to define your agencies

Choose an attribute to define your agencies. Use this attribute to create the search permissions filter that limits an eDiscovery manager to search only the content locations of users who are assigned a specific value for this attribute. For example, Contoso uses the **Department** attribute. The value for this attribute for users in the Fourth Coffee subsidiary is `FourthCoffee` and the value for users in Coho Winery subsidiary is `CohoWinery`. In Step 3, use this `attribute:value` pair (for example, *Department:FourthCoffee*) to limit the user content locations that eDiscovery managers can search.

Here are some examples of user attributes that you can use for compliance boundaries:

- Company
- CustomAttribute1 - CustomAttribute15
- Department
- Office
- CountryOrRegion (Two-letter country/region code)

Note

When selecting the attributes for the security filter, consider the attributes supported by different mailbox types in Exchange Online. Use CustomAttribute1 through CustomAttribute15 because all mailbox types in Exchange support these attributes.

### Step 2: Create a role group for each agency

Create role groups in the Microsoft Purview portal that align with your agencies.

To create the role groups, go to **Settings** &gt; **Roles and scopes** in the Microsoft Purview portal. Create a role group for each team in each agency that uses compliance boundaries and eDiscovery cases to manage investigations. You can use a single role group to assign both the eDiscovery roles and the security filter to its members. Membership in this role group manages both the roles assigned to the investigator and the content locations they can search.

Note

If you previously configured compliance boundaries using role groups with no roles attached (sometimes called 'empty role groups'), this configuration is no longer supported. Role groups used with search permissions filters must have at least one role assigned.

Use separate role groups. Use one role group to assign the security filter for the compliance boundary and another role group to assign the eDiscovery roles. By using two separate role groups, you manage the roles assigned to an investigator independently from the content locations they search. Use the role group for the compliance boundary only to apply the security filter to members. Use separate built-in (eDiscovery Manager) or custom role groups to assign roles to members. For more information about eDiscovery-related roles, see [Assign eDiscovery permissions](edisc-permissions).

Important

Role groups with a security filter assigned must have at least one role added for it to take effect.

Using the Contoso compliance boundaries scenario, create four role groups and add the appropriate members to each one.

- Fourth Coffee eDiscovery Managers
- Fourth Coffee Investigators
- Coho Winery eDiscovery Managers
- Coho Winery Investigators

Important

If you add or remove a role from a role group that you added as a member of a case, the role group is automatically removed as a member of the case (or any case the role group is a member of). This behavior protects your organization from inadvertently providing extra permissions to members of a case. If you delete a role group, you remove it from all cases it was a member of.

### Step 3: Create a search permissions filter to enforce the compliance boundary

After you create role groups for each agency, create search permissions filters that associate each role group with its specific agency and define the compliance boundary. You need to create one search permissions filter for each agency. For more information about creating security permissions filters, see [Configure permissions filtering for eDiscovery](edisc-search-permission-filtering).

Here's the syntax that's used to create a search permissions filter for compliance boundaries for the scenario in this article.

```powershell
New-ComplianceSecurityFilter -FilterName <name of filter> -Users <role groups> -Filters "Mailbox_<MailboxPropertyName>  -eq '<Value> '", "SiteContent_Path -like '<SharePointURL>' -or SiteContent_Path -like '<OneDriveURL>'"
```

Here's a description of each parameter in the command:

- `FilterName`: Specifies the name of the filter. Use a name that describes or identifies the agency that the filter is used in.
- `Users`: Specifies the users or groups who get this filter applied to the search actions they perform. For compliance boundaries, this parameter specifies the role groups (that you created in Step 2) in the agency that you're creating the filter for. This parameter is a multivalue parameter so you can include one or more role groups, separated by commas.
- `Filters`: Specifies the search criteria for the filter. For compliance boundaries, you define the following filters. Each one applies to different content locations.

    - `Mailbox`: Specifies the mailboxes or OneDrive accounts that the role groups defined in the `Users` parameter can search. This filter allows members of the role group to search only the mailboxes or OneDrive accounts in a specific agency; for example, `"Mailbox_Department -eq 'FourthCoffee'"`.

        Note

        Mailbox filters also apply to Microsoft 365 group mailboxes and connected SharePoint sites. To return results from a SharePoint site connected to a Microsoft 365 group, both the *Mailbox* and *SiteContent* filters must match to both the Microsoft 365 group mailbox and the associated SharePoint site.
- `SiteContent`: This filter includes two separate filters. The first `SiteContent_Path` specifies the SharePoint sites in the agency that the role groups defined in the `Users` parameter can search. For example, `SiteContent_Path -like 'https://contoso.sharepoint.com/sites/FourthCoffee*'`. The second `SiteContent_Path` filter (connected to the first `SiteContent_Path` filter by the `or` operator) specifies the agency's OneDrive domain (also called the *MySite* domain). For example, `SiteContent_Path -like 'https://contoso-my.sharepoint.com/personal*'`. You can also use the `Site_Path` filter in place of the `SiteContent` filter. The `Site` and `SiteContent` filters are interchangeable, and don't affect search permissions filters described in this article.

    Important

    Why is the `SiteContent` filter for OneDrive included in the previous search permissions filter? Although the `Mailbox` filter applies to *both* mailboxes and OneDrive accounts, the inclusion of the SharePoint filter would exclude OneDrive accounts if you didn't also include the OneDrive `Site` filter. If the search permissions filter didn't include a SharePoint filter, then you wouldn't have to include a separate OneDrive filter because the Mailbox filter would include OneDrive accounts in the scope of the compliance boundary. In other words, a search permissions filter with only the `Mailbox` filter would include both mailboxes and OneDrive accounts.

Here are examples of the two search permissions filters that you create to support the Contoso compliance boundaries scenario. Both of these examples include a comma-separated filters list, in which the mailbox and site filters are included in the same search permissions filter and are separated by a comma.

#### Fourth Coffee

```powershell
New-ComplianceSecurityFilter -FilterName "Fourth Coffee Security Filter" -Users "Fourth Coffee eDiscovery Managers", "Fourth Coffee Investigators" -Filters "Mailbox_Department -eq 'FourthCoffee'", "SiteContent_Path -like 'https://contoso.sharepoint.com/sites/FourthCoffee*' -or SiteContent_Path -like 'https://contoso-my.sharepoint.com/personal*'"
```

#### Coho Winery

```powershell
New-ComplianceSecurityFilter -FilterName "Coho Winery Security Filter" -Users "Coho Winery eDiscovery Managers", "Coho Winery Investigators" -Filters "Mailbox_Department -eq 'CohoWinery'", "SiteContent_Path -like 'https://contoso.sharepoint.com/sites/CohoWinery*' -or SiteContent_Path -like 'https://contoso-my.sharepoint.com/personal*'"
```

Note

The syntax for the `Filters` parameters in the previous examples includes a *filters list*. A filters list is a filter that includes a mailbox filter and a site path filter separated by a comma. In the previous example, notice that a comma separates `Mailbox` and `SiteContent` filters: `-Filters "Mailbox_<MailboxPropertyName>  -eq '<Value> '", "SiteContent_Path -like '<SharePointURL>' -or SiteContent_Path -like '<OneDriveURL>'"`. When this filter is processed during the running of an eDiscovery search, two search permissions filters are created from the filters list: one mailbox filter and one SharePoint/OneDrive filter. An alternative to using a filters list would be to create two separate search permissions filters for each agency: one search permissions filter for the mailbox attribute and one filter for the SharePoint and OneDrive site attributes. In either case, the results are the same. Using a filters list or creating separate search permissions filters is a matter of preference.

#### How do the search permissions filters work in this scenario?

Here's how the search permission filters are applied for each agency in this scenario.

1. The `Mailbox` filter is first applied to define the content locations that eDiscovery managers can search. In this case, Coho Winery eDiscovery managers can only search the mailboxes and OneDrive accounts of users whose *Department* mailbox property has a value of **FourthCoffee**; Coho Winery eDiscovery managers can only search the mailboxes and OneDrive accounts of users whose *Department* mailbox property has a value of **CohoWinery**. The `Mailbox` filter is a *content location filter*, because it specifies the content locations that eDiscovery managers can search. In both filters, eDiscovery managers can only search content locations with a specific mailbox property value.
2. After the content locations that can be searched are defined, the next part of the filter defines the content that eDiscovery managers can search. The first `SiteContent` filter lets Fourth Coffee eDiscovery managers only search for documents that have a site path property that contains (or starts with) `https://contoso.sharepoint.com/sites/FourthCoffee`; Coho Winery eDiscovery managers can only search documents that have a site path property that contains (or starts with) `https://contoso.sharepoint.com/sites/CohoWinery`. Therefore, the two `SiteContent` filters are *content filters* because they define the content that can be searched for. In both filters, eDiscovery managers can only search for documents with a specific document property value. All SharePoint-related filters are content filters because searchable site properties are stamped on all documents. For more information, see [Configure permissions filtering for eDiscovery](edisc-search-permission-filtering#create-a-search-permissions-filter-with-new-compliancesecurityfilter).

    Note

    Although the scenario in this article doesn't use them, you can also use mailbox content filters to specify the content that eDiscovery managers can search for. The syntax for mailbox content filters is `"MailboxContent_<property> -<comparison operator> '<value>'"`. You can create content filters based on date ranges, recipients, and domains or any searchable email property. For example, this filter would allow eDiscovery managers to only search for mail items sent or received by users in the contoso.com domain: `"MailboxContent_Participants -like 'contoso.com'"`. For more information about mailbox content filters, see [Configure search permissions filtering](edisc-search-permission-filtering#create-a-search-permissions-filter-with-new-compliancesecurityfilter).
3. The search permissions filter is joined to the search query by the **AND** Boolean operator. That means when an eDiscovery manager in one of the agencies runs an eDiscovery search, the items returned by the search must match the search query and the conditions defined in the search permissions filter.

### Step 4: Create an eDiscovery case for intra-agency investigations

In the final step, create an eDiscovery case in the Microsoft Purview portal. Then, add the role group that you created in Step 2 as a member of the case. This approach provides two important benefits when using compliance boundaries:

- Only members of the role group added to the case can see and access the case in the Microsoft Purview portal. For example, if the Fourth Coffee Investigators role group is the only member of a case, then members of the Fourth Coffee eDiscovery Managers role group (or members of any other role group) can't see or access the case.
- When a member of the role group assigned to a case runs a search associated with the case, they can only search the content locations within their agency. This restriction is defined by the search permissions filter that you created in Step 3.

To create a case and assign members:

1. Go to **eDiscovery** in the Microsoft Purview portal and create a case.
2. In the list of cases, select the name of the case you created.
3. Add role groups as members to the case.

Note

When adding a role group to a case, you can only add the role groups that you're a member of.

## Search and export content in multigeo environments

Search permissions filters also let you control where content is routed for export and which datacenter can be searched when searching content locations in a [SharePoint multigeo environment](/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

- **Export search results:** You can export the search results from Exchange mailboxes, SharePoint sites, and OneDrive accounts from a specific datacenter. This feature means that you can specify the datacenter location that search results are exported from.

    Use the *Region* parameter for **New-ComplianceSecurityFilter** or **Set-ComplianceSecurityFilter** cmdlets to create or change which datacenter the export is routed through.

    | Parameter value | Datacenter location |
    | --- | --- |
    | NAM | North American (datacenters are in the US) |
    | EUR | Europe |
    | APC | Asia Pacific |
    | CAN | Canada |
- **Route content searches:** You can route the content searches of SharePoint sites and OneDrive accounts to a satellite datacenter. This feature means you can specify the datacenter location where searches are run.

    Note

    If you're using premium eDiscovery features, the *Region* parameter doesn't control the region that data is exported from. Data is exported from the organization's central location. Also, searching for content in SharePoint and OneDrive isn't bound by the geographic location of datacenters. All datacenters are searched.

    Use one of the following values for the *Region* parameter to control the datacenter location that searches run in when searching SharePoint sites and OneDrive accounts.

    | Parameter value | Datacenter routing locations for SharePoint |
    | --- | --- |
    | NAM | US |
    | EUR | Europe |
    | APC | Asia Pacific |
    | CAN | US |
    | AUS | Asia Pacific |
    | KOR | The organization's default datacenter |
    | GBR | Europe |
    | JPN | Asia Pacific |
    | IND | Asia Pacific |
    | LAM | US |
    | NOR | Europe |
    | BRA | North American datacenters |

    If you don't specify the *Region* parameter for a search permissions filter, the organization's primary SharePoint region is searched. Search results are exported to the closest datacenter.

    To simplify the concept, the *Region* parameter controls the datacenter that is used to search for content in SharePoint and OneDrive. This parameter doesn't apply to searching for content in Exchange because Exchange content searches aren't bound by the geographic location of datacenters. Also, the same *Region* parameter value might also dictate the datacenter that exports are routed through. This routing is often necessary to control the movement of data across geographic borders.

    Important

    When creating security compliance filter and setting a specific GEO region: ESP, ITA, NZL and SWE aren't valid regions and generate an error redirecting to valid region values. This error includes the following valid regions: ARE, APC, AUS, AUT, BRA, CAN, CHE, CHL, DEU, EUR, FRA, GBR, IDN, IND, JPN, KOR, LAM, MYS, NAM, NOR, POL, QAT, ZAF.

Here are examples of using the *Region* parameter when creating search permission filters for compliance boundaries. This example assumes that the Fourth Coffee subsidiary is located in North America and that Coho Winery is in Europe.

```powershell
New-ComplianceSecurityFilter -FilterName "Fourth Coffee Security Filter" -Users "Fourth Coffee eDiscovery Managers", "Fourth Coffee Investigators" -Filters "Mailbox_Department -eq 'FourthCoffee'", "SiteContent_Path -like 'https://contoso.sharepoint.com/sites/FourthCoffee*' -or SiteContent_Path -like 'https://contoso-my.sharepoint.com/personal*'" -Region NAM
```

```powershell
New-ComplianceSecurityFilter -FilterName "Coho Winery Security Filter" -Users "Coho Winery eDiscovery Managers", "Coho Winery Investigators" -Filters "Mailbox_Department -eq 'CohoWinery'", "SiteContent_Path -like 'https://contoso.sharepoint.com/sites/CohoWinery*' -or SiteContent_Path -like 'https://contoso-my.sharepoint.com/personal*'" -Region EUR
```

Keep the following things in mind when searching and exporting content in multigeo environments.

- The *Region* parameter doesn't control searches of Exchange mailboxes. All datacenters are searched when you search mailboxes. To limit the scope of which Exchange mailboxes are searched, use the *Filters* parameter when creating or changing a search permissions filter.
- If it's necessary for an eDiscovery Manager to search across multiple SharePoint regions, you need to create a different user account for that eDiscovery manager to use in the search permissions filter to specify the region where the SharePoint sites or OneDrive accounts are located. For more information about setting this up, see [Configure search permissions filtering in eDiscovery](edisc-search-permission-filtering).
- When searching for content in SharePoint and OneDrive, the *Region* parameter directs searches to either the primary or satellite location where the eDiscovery manager conducts eDiscovery investigations. If an eDiscovery manager searches SharePoint and OneDrive sites outside of the region that's specified in the search permissions filter, no search results are returned.
- When exporting search results from eDiscovery, content from all content locations (including Exchange, Skype for Business, SharePoint, OneDrive, and other services that you can search by using the Content Search tool) are uploaded to the Azure Storage location in the datacenter that's specified by the *Region* parameter. This behavior helps organizations stay within compliance by not allowing content to be exported across controlled borders. If you don't specify a region in the search permissions filter, content is uploaded to the organization's primary datacenter.

    When exporting content with premium eDiscovery features enabled, you can't control where content is uploaded by using the *Region* parameter. Content is uploaded to an Azure Storage location in a datacenter in your organization's central location. For a list of geo locations based on your central location, see [Microsoft 365 Multi-Geo eDiscovery configuration](/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).
- You can edit an existing search permissions filter to add or change the region by running the following command:

    ```powershell
    Set-ComplianceSecurityFilter -FilterName <Filter name>  -Region <Region>
    ```

## Use compliance boundaries for SharePoint hub sites

[SharePoint hub sites](/en-us/sharepoint/dev/features/hub-site/hub-site-overview) often align with the same geographical or agency boundaries that eDiscovery compliance boundaries follow. You can use the site ID property of the hub site to create a compliance boundary. To do this, use the [Get-SPOHubSite](/en-us/powershell/module/sharepoint-online/get-spohubsite#examples) cmdlet in SharePoint Online PowerShell to get the SiteId for the hub site, then use this value for the department ID property to create a search permissions filter.

Use the following syntax to create a search permissions filter for a SharePoint hub site:

```powershell
New-ComplianceSecurityFilter -FilterName <Filter Name> -Users <User or Group> -Filters "Site_Departmentid -eq '{SiteId of hub site}'"
```

Here's an example of creating a search permissions filter for a hub site for the Coho Winery agency:

```powershell
New-ComplianceSecurityFilter -FilterName "Coho Winery Hub Site Security Filter" -Users "Coho Winery eDiscovery Managers", "Coho Winery Investigators" -Filters "Site_Departmentid -eq '44252d09-62c4-4913-9eb0-a2a8b8d7f863'"
```

## Compliance boundary considerations

Keep the following considerations in mind when managing eDiscovery cases and investigations that use compliance boundaries:

- When you create and run a search, you can select content locations that are outside of your agency. However, because of the search permissions filter, content from those locations isn't included in the search results.
- Compliance boundaries don't apply to holds in eDiscovery cases. That condition means an eDiscovery manager in one agency can place a user in a different agency on hold. However, the compliance boundary is enforced if the eDiscovery manager searches the content locations of the user who was placed on hold. That condition means the eDiscovery manager can't search the user's content locations, even though they were able to place the user on hold.
- If you're assigned a search permissions filter - either mailbox or site filters - and you attempt to export partially indexed items from a search that includes all SharePoint sites in your organization, by using the scope option to include partially indexed items even from locations without search hits (see [Export search results](edisc-search-export)), the export contains partially indexed items from all sites, including those outside your assigned compliance boundary.
- When retrieving partially indexed items from sites that contain search hits, eDiscovery uses a prefix-based approach. For example, if a site *`http://contoso.com/sales`* is identified as a location matching the search query, the results might also include items from a similarly prefixed site such as *`http://contoso.com/salesdepartment`*, even if the *`http://contoso.com/salesdepartment`* site falls outside the configured compliance boundary. This behavior can occur when the filter isn't based on the site path. For instance, if the compliance boundary is defined as `Property -eq 'abc'`, a site that doesn't match the property value `'abc'` might be included if its path shares a prefix with a site that does match the property.
- Search permissions filters aren't applied to Exchange public folders.
- Supported search filters include `-and`, `-or`, `-like`, `-not`, `-eq`, and `-ne`. Don't use other exclusion filters, such as `-notlike` or `inotlike`, in a search permissions filter for a content-based compliance boundary. Using these exclusion filters can have unexpected results if content with recently updated attributes hasn't been indexed.
- Respect for compliance boundaries for OneDrive sites in searches might be impacted when:

    - The sites or associated mailboxes are moved or rehomed.
    - OneDrive ownership is reassigned, or more than one owner is added.
    - The OneDrive site is renamed or re-issued.
    - Moving a OneDrive site can change the ownership of the content and might include creating an arbitration mailbox. When you move these resources, there's a chance that content search results might be available across compliance boundaries. When a OneDrive site is reassigned, renamed, or assigned to more than one owner, it's possible that the content from these sites might be available across compliance boundaries.
- Compliance boundaries for mailboxes might be impacted when:

    - The mailbox isn't associated with a licensed user, which includes disabled or deleted users.
    - A mailbox isn't managed or synced from Microsoft Entra ID.
- Additionally, several types of mailboxes might produce content during search, regardless of their compliance boundaries. These mailbox types include:

    - EquipmentMailbox
    - GuestMailUser
    - LinkedMailbox
    - RoomList
    - RoomMailbox
    - SchedulingMailbox
    - SharedMailbox
    - SystemMailbox
    - TeamMailbox
- To make sure that the search respects the compliance boundaries as expected for these mailboxes, set attributes on shared mailboxes, equipment mailboxes, and other mailboxes by using the [Set-Mailbox](/en-us/powershell/module/exchange/set-mailbox) cmdlet or by using [Invoke-ComplianceSecurityFilterAction](/en-us/powershell/module/exchange/invoke-compliancesecurityfilteraction) to ensure the attribute is set correctly. If you properly configure the attribute and align it with the compliance boundary attribute, the mailbox respects the compliance boundary.

## More information

- If you delicense or soft-delete a mailbox, the user is no longer within the compliance boundary. If you place a hold on the mailbox when you delete it, the content preserved in the mailbox is still subject to a compliance boundary or search permissions filter.
- If you implement compliance boundaries and search permissions filters for a user, don't delete the user's mailbox or their OneDrive account. If you delete a user's mailbox, also remove the user's OneDrive account since `mailbox_RecipientFilter` enforces the search permission filter for OneDrive.
- Compliance boundaries and search permissions filters depend on attributes stamped on content in Exchange, OneDrive, and SharePoint and the subsequent indexing of this stamped content.

## Frequently asked questions

**Who can create and manage search permissions filters by using the New-ComplianceSecurityFilter and Set-ComplianceSecurityFilter cmdlets?**

To create, view, and modify search permissions filters in the Microsoft Purview portal, you need to have the *Organization Management* and *eDiscovery Administrator* roles assigned.

**If an eDiscovery manager is assigned to more than one role group that spans multiple agencies, how do they search for content in one agency or the other?**

The eDiscovery manager can add parameters to their search query that restrict the search to a specific agency. For example, if an organization specifies the **CustomAttribute10** property to differentiate agencies, they can append the following to their search query to search mailboxes and OneDrive accounts in a specific agency: `CustomAttribute10:<value>`.

**What happens if I change the value of the attribute that's used as the compliance attribute in a search permissions filter?**

It takes up to three days for a search permission filter to enforce the compliance boundary if you change the value of the attribute used in the filter. For example, let's say that a user in the Fourth Coffee agency is transferred to the Coho Winery agency. As a result, the value of the **Department** attribute on the user object changes from *FourthCoffee* to *CohoWinery*. In this situation, Fourth Coffee eDiscovery and investors get search results for that user for up to three days after the attribute is changed. Similarly, it takes up to three days before Coho Winery eDiscovery managers and investigators get search results for the user.

**Can an eDiscovery manager see content from two separate compliance boundaries?**

Yes, this capability is available when searching Exchange mailboxes by adding the eDiscovery manager to role groups that have visibility to both agencies. However, when searching SharePoint sites and OneDrive accounts, an eDiscovery manager can search for content in different compliance boundaries only if the agencies are in the same region or geo location.

Note

This limitation for sites doesn't apply when premium eDiscovery features are enabled because searching for content in SharePoint and OneDrive isn't bound by geographic location.

**What happens to existing eDiscovery cases when a tenant moves between regions or across security boundaries?**

eDiscovery cases, searches, holds, and review sets are created against the tenant's content location at the time of creation. When a tenant moves to a different region or to a different security boundary (for example, from commercial to GCC, GCC High, or DoD), existing artifacts remain bound to the origin location's data plane and might not be reusable from the destination.

| Move type | Impact on existing eDiscovery artifacts |
| --- | --- |
| Tenant relocation within the same security boundary (for example, a region move within commercial — NAM, EUR, APC) | Cases, searches, holds, and review sets created before the move might not be accessible from the destination region. Plan to export any required evidence before initiating the move, or expect to recreate artifacts after the move. |
| Tenant migration **across** security boundaries (commercial ↔ GCC, GCC High, or DoD) | Cases, searches, holds, and review sets created in the origin cloud **can't** be migrated and aren't accessible from the destination cloud. The artifacts continue to exist in the origin cloud's data plane but can't be opened, exported, or modified from the destination cloud. Plan to complete or export any active matters in the origin cloud before initiating the migration. |

Symptoms after a move can include: existing cases appear in the portal but new case or search creation fails (often with a 500 error). If you encounter this error, contact Microsoft Support. There's a routing remediation, but for cross-cloud moves it requires accepting the loss of access to the origin-cloud artifacts in exchange for unblocking new artifact creation in the destination cloud.

For broader planning guidance on tenant migrations to the U.S. Government clouds, see [Plan for Microsoft Purview DoD deployments](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/plan-for-microsoft-purview-dod-deployments), [Plan for Microsoft Purview GCC High deployments](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/plan-for-microsoft-purview-gcc-high-deployments), and [Plan for Microsoft Purview GCC deployments](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/plan-for-microsoft-purview-gcc-deployments). For tenant relocation and data residency planning, see [Advanced Data Residency in Microsoft 365](/en-us/microsoft-365/enterprise/advanced-data-residency) and [Plan for Microsoft 365 Multi-Geo](/en-us/microsoft-365/enterprise/plan-for-multi-geo).

**Do search permissions filters work for eDiscovery case holds, Microsoft 365 retention policies, or DLP?**

No, not at this time.

**If I specify a region to control where content is exported, but I don't have a SharePoint organization in that region, can I still search SharePoint?**

If the region specified in the search permissions filter doesn't exist in your organization, the default region is searched.

**What is the maximum number of search permissions filters that I can create in an organization?**

There's no limit to the number of search permissions filters that you can create in an organization. However, a search query can have a maximum of 100 conditions. In this case, a condition is defined as something that's connected to the query by a Boolean operator (such as **AND**, **OR**, and **NEAR**). The limit of the number of conditions includes the search query itself plus all search permissions filters that are applied to the user who runs the search. Therefore, the more search permissions filters you have (especially if these filters are applied to the same user or group of users), the better the chance of exceeding the maximum number of conditions for a search.

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

Also, the number of search permissions filters appended to a query depends on the user who is running the search. When a specific user runs a search, the search permissions filters that are applied to the user (which is defined by the *Users* parameter in the filter) are appended to the query. Your organization could have hundreds of search permissions filters, but if you apply more than 100 filters to the same users, then it's likely the 100-condition limit is exceeded when those users run searches.

There's one more thing to keep in mind about the condition limit. The number of specific SharePoint sites that are included in the search query or search permissions filters also count against this limit.

To prevent your organization from reaching the conditions limit, keep the number of search permissions filters in your organization as few as possible to meet your business requirements.

**How do mailbox filters impact searches to OneDrive and M365 Group connected SharePoint sites?**

OneDrive sites and Microsoft 365 Group connected SharePoint sites are linked to the associated user or Microsoft 365 Group mailbox in Exchange. For security filters that include both a Mailbox and SiteContent filter, to return results from the OneDrive or Microsoft 365 Group connected SharePoint sites both must be a match. The Mailbox filter is evaluated against the connected user or Microsoft 365 Group Mailbox first before evaluating the SharePoint and OneDrive items against the SiteContent filter.

**What is an arbitration mailbox in the context of OneDrive sites?**

For active and licensed users that have both an Exchange Mailbox and OneDrive account, there's a link between the mailbox and their OneDrive site. This means that the Mailbox filter assigned to a compliance boundary is evaluated against the user's mailbox to check for a match before results are returned.

When this link is lost between a mailbox and a OneDrive site, the OneDrive is associated with an arbitration mailbox instead. This arbitration mailbox doesn't have any of the mailbox properties from the original mailbox applied to it.

**How do I check the status of a OneDrive site to determine if it is associated with an arbitration mailbox?**

To review a specific OneDrive site and check if it's in arbitration or linked to a user's mailbox, use the [Invoke-ComplianceSecurityFilterAction](/en-us/powershell/module/exchange/invoke-compliancesecurityfilteraction) cmdlet.

Use the following syntax to check the status of a OneDrive site:

```powershell
Invoke-ComplianceSecurityFilterAction -Action GetStatus -PropertyName <Boundary Property> -SiteUrl <SharePoint/OneDrive URL>
```

For a OneDrive site that's not in arbitration, the commands return the *BoundaryType* value as UserMailbox, as shown in the following example:

```powershell
PS C:\> Invoke-ComplianceSecurityFilterAction -action GetStatus -PropertyName "CustomAttribute10" -siteurl "https://contoso-my.sharepoint.com/personal/lila_contoso_onmicrosoft_com"

SiteUrlOrEmailAddress : https://contoso-my.sharepoint.com/personal/lila_contoso_onmicrosoft_com
BoundaryType          : UserMailbox
BoundaryInstruction   : Set via Set-Mailbox
BoundaryObjectId      : SPO_4531d99e-21df-4903-a8c1-76cc3ec82685@SPO_525ef3f5-fbf7-4f91-bb4a-e3c24116c8a9
BoundaryStatus        : Success
BoundaryProperty      : CustomAttribute10
BoundaryPropertyValue : Dept-CH
```

For a OneDrive site that's in arbitration, the commands return an empty or null value for the *BoundaryType* value, as shown in the following example.

```powershell
PS C:\> Invoke-ComplianceSecurityFilterAction -action GetStatus -PropertyName "CustomAttribute10" -siteurl "https://contoso-my.sharepoint.com/personal/lila_contoso_onmicrosoft_com"

SiteUrlOrEmailAddress : https://contoso-my.sharepoint.com/personal/lila_contoso_onmicrosoft_com
BoundaryType          :
BoundaryInstruction   :
BoundaryObjectId      : SPO_4531d99e-21df-4903-a8c1-76cc3ec82685@SPO_525ef3f5-fbf7-4f91-bb4a-e3c24116c8a9
BoundaryStatus        : Success
BoundaryProperty      : CustomAttribute10
BoundaryPropertyValue :
```

**How does a OneDrive site in arbitration affect results returned by an eDiscovery Manager with compliance boundaries applied to them?**

This behavior depends on how the security filter is configured for the compliance boundary. When a OneDrive site is in arbitration, a Mailbox filter doesn't include it in the returned results.

For security filters that use only a Mailbox filter, items from the OneDrive are returned within the results of a search because the mailbox filter doesn't apply in this scenario.

For security filters that use both a mailbox filter and a SiteContent filter, results are returned if the *SiteContent* filter matches the items in the OneDrive instance that's in arbitration. If there's no match, the results aren't returned. For example, if the SiteContent\_Path filter is used as separate agencies have a unique OneDrive URL due to the deployment of Microsoft 365 Multi-Geo, then the OneDrive items' path filters in or out results from the OneDrive in arbitration.

**How can I update a OneDrive site in arbitration so that Mailbox filters continue to apply?**

Use the [Invoke-ComplianceSecurityFilterAction](/en-us/powershell/module/exchange/invoke-compliancesecurityfilteraction) cmdlet to set the CustomAttribute1 through to CustomAttribute15 values on OneDrive instances that link to an arbitration mailbox.

Use the following syntax to set the status of a OneDrive site:

```powershell
Invoke-ComplianceSecurityFilterAction -Action Set -PropertyName <Boundary Property> -SiteUrl <SharePoint/OneDrive URL>
```

After you set it on the OneDrive, it honors the Mailbox filters that use the CustomAttribute property set on the OneDrive.

**What scenarios cause a OneDrive site to link to an arbitration mailbox?**

Many scenarios can cause a OneDrive site to lose its link to the user's mailbox and link to an arbitration mailbox. See the Compliance Boundary Limitations section for more information. As a result, when you move, change, or reassign a OneDrive, use the [Invoke-ComplianceSecurityFilterAction](/en-us/powershell/module/exchange/invoke-compliancesecurityfilteraction) cmdlet to validate that the relevant Mailbox filter behaves as expected.

As part of user deprovisioning processes, run the [Invoke-ComplianceSecurityFilterAction](/en-us/powershell/module/exchange/invoke-compliancesecurityfilteraction) cmdlet against the user's OneDrive to set the required CustomAttribute value.

**Why should I use CustomAttribute1 through CustomAttribute15 for Mailbox security filters?**

Although other Mailbox attributes work with security filters, use the CustomAttributes when you define the Mailbox security filter for the following reasons:

- All Exchange Online mailboxes support these attributes.
- The attributes stamp directly on the mailbox, not the associated user object, so they remain set in scenarios where there's no associated user object.
- The Invoke-ComplianceSecurityFilterAction cmdlet only supports setting CustomAttribute on OneDrive instances linked to an arbitration mailbox. **My organization previously configured compliance boundaries using role groups with no roles attached (empty role groups), how should I update this congifuration?**

First identify roles used in your New-ComplianceSecurityFilter commands by running Get-ComplianceSecurityFilter | FL FIlterName, Users

Then, add a minimal role (such as View-Only Audit Logs) to each role group, or restructure to use the two-role group structure recommended where you set up one role group for the security filter (with at least one role) and one role group for eDiscovery permissions.

Finally, verify your compliance boundaries are functioning as expected by running a test search.

Note: adding or removing roles from a role group that is a member of a case will automatically remove that role group from the case. Re-add the role group to the affected cases after makeing role changes.

**My search returns results outside the expected compliance boundary, what should I do?**

Verify the role group used in your security filter has at least one role assigned. Role groups with no roles assigned don't activate the security filter. Confirm the mailbox attribute is set on all target mailboxes, including shared mailboxes and group mailboxes. Check for OneDrive sites in arbitration status as sites linked to arbitration mailboxes don't inherit mailbox attributes. Allow up to three days for attribute changes to take effect in search permissions filters.