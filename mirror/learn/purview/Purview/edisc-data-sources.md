---
layout: Conceptual
title: Data sources in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-data-sources
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to add and manage user, group, SharePoint, and SharePoint Embedded data sources for searches and holds in Microsoft Purview eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-09-19T00:00:00.0000000Z
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
ms.custom: msecd-doc-authoring-1028
locale: en-us
document_id: 511d5f37-509e-c31a-fe2c-822b698ae3ea
document_version_independent_id: 511d5f37-509e-c31a-fe2c-822b698ae3ea
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-data-sources.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-data-sources
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-data-sources.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 0c4607d6-313b-8a57-98ba-9ae2e8704139
---

# Data sources in eDiscovery | Microsoft Learn

In Microsoft 365, data is stored across three platforms: Exchange, Microsoft Teams, and SharePoint. These platforms organize and manage data within Microsoft 365 applications. Most Microsoft 365 apps store data in one or more of the following containers:

- **Users**: Data associated with individual users, such as their mail, 1:1 Teams messages, and OneDrive files.
- **Groups**: Data owned by the organization or a group of users within an organization. These groups are often referred to as Unified Groups or Teams.

In Microsoft Purview eDiscovery, the concept of *data source* streamlines the process of identifying and managing data across Microsoft 365 platforms. eDiscovery users select a user or group, which creates a data source. eDiscovery automatically identifies and organizes relevant data stored across platforms. The data source gathers locations related to the user or group (mailboxes, OneDrive sites, SharePoint sites) and adds the locations in the data source hierarchy. eDiscovery users refine the scope by selecting or excluding specific locations as needed.

A user data source typically includes:

- User mailbox
- OneDrive site

## SharePoint Embedded application content

SharePoint Embedded container support in eDiscovery (preview) might change before general availability. Review the limitations in this section before using the feature in an investigation.

Some Microsoft 365 applications store content in SharePoint Embedded containers. Examples include Microsoft Loop, Microsoft Copilot Pages, Microsoft Copilot Notebooks, Microsoft Designer, and Outlook Newsletters. The applications represented in the Manage sources experience depend on the supported containers returned for the selected user.

When you add a user as an eDiscovery data source, eDiscovery identifies supported SharePoint Embedded containers relevant to that user and displays them with the user's other data locations. You can review and select the individual containers that are relevant to the investigation.

### Add SharePoint Embedded containers as data sources

You can add supported SharePoint Embedded containers as data sources in the following ways:

- **Discover containers for a user:** Add a user as a data source to display supported user-owned and tenant-owned SharePoint Embedded containers relevant to that user. You can select or clear individual containers before saving the data source.
- **Filter containers by application:** When reviewing containers for a selected user, use **Filter by app** to narrow the displayed containers to a specific supported application. The available filters depend on the applications represented in the returned container list.
- **Add a container by URL:** If you know the SharePoint Embedded container URL, enter it when adding a site location. eDiscovery resolves the container URL so you can select the container as a data source.
- **Add container URLs in bulk:** Include supported SharePoint Embedded container URLs when you bulk import data sources. eDiscovery resolves the URLs as data-source locations.

For each supported SharePoint Embedded container, the **Manage sources** pane displays:

- The full container URL
- The container display name
- The associated application label
- The `ContainerTypeId`

Use these details to distinguish between containers and select the locations relevant to the investigation.

Note

Microsoft Loop My workspace, Copilot Pages, and Copilot Notebooks use the same user-owned SharePoint Embedded container. In SharePoint Embedded administration and compliance experiences, this shared container is identified as **Loop**. As a result, Copilot Pages and Copilot Notebooks content can appear in a container labeled **Loop** and might not appear as separate application filters. For more information, see [Overview of Copilot Pages and Copilot Notebooks storage](/en-us/microsoft-365/loop/cpcn-storage).

Important

**SharePoint Embedded limitations:**

- **Container ownership:** Supported user-owned and tenant-owned SharePoint Embedded containers relevant to a selected user are surfaced in eDiscovery. Group-owned and app-owned SharePoint Embedded containers aren't currently supported.
- **Compliance boundaries:** eDiscovery compliance boundary enforcement isn't currently supported for SharePoint Embedded containers.

## Group and organization-wide data sources

Unified groups are classified into three types, each covering specific data locations:

- **Teams**: Includes Exchange mailbox storage for Teams chats and emails, as well as all associated SharePoint sites for channels and the team.
- **Viva Engage**: Includes Exchange mailbox storage for Viva Engage messages.
- **Classic**: Includes only SharePoint sites.

eDiscovery users can also use organization-wide sources to perform searches across your organization. Organization-wide sources include:

- **All people and groups**: Includes all users and all groups in your organization.
- **All public folders**: Includes all content in Exchange [public folders](/en-us/exchange/collaboration-exo/public-folders/public-folders?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) mailboxes.

Note

Organization-wide searches include content from supported SharePoint Embedded containers. However, selecting an organization-wide source doesn't display a tenant-wide list of every SharePoint Embedded container. To review and select individual supported containers, use the user-based **Manage sources** experience.

Important

For large organizations, tenant-wide searches across all Exchange mailboxes and SharePoint sites are long-running processes. Service throttling can affect these searches because of the number of mailboxes and sites to search. Before running these tenant-wide searches, review scale limits and throughput guidance in [Limits in eDiscovery](edisc-ref-limits#search-limits). Plan to conduct searches in batches as applicable. To improve performance and operability, break the search into scoped runs by using [compliance boundaries](edisc-compliance-boundaries) (for example, by region, business unit, or department) so each search targets a subset of mailboxes and sites.

It's common to search a set of user mailboxes when you manage the list as a distribution list. Adding distribution lists is supported, and the search includes only the Exchange mailboxes listed in the group.

You can [search for specific data sources or data locations](edisc-search-query#create-a-search-query) by using user or group's names, mailbox Simple Mail Transfer Protocol (SMTP) addresses, and OneDrive or SharePoint site URLs. When you create a search by using specific data sources, you search only the locations specified in the data source.

If you use the organization-wide source **All people and groups**, the search covers all Exchange mailboxes, OneDrive, and SharePoint sites. To search all Exchange mailboxes only, select mailboxes under **All people and groups** and deselect the sites. To search all SharePoint and OneDrive sites only, select sites under **All people and groups** and deselect the mailboxes.

Real-time data source sync helps ensure that you're always informed about the latest changes in data locations associated with users and groups. You can query if any specific data sources are added to a search, if a hold includes newly provisioned data locations, or if data locations are removed.

For example, if you create a private channel for a Teams group, the sync feature on the data source panel alerts you of the new location. You can quickly and easily include it in searches or holds. This sync ensures that new data doesn't go unnoticed and is included in your investigations. This sync also helps prevent potential data loss from location changes.

For more information about using data sources effectively, check out the following video: 

## Supported group types

The following table summarizes which group types can be added as data sources in eDiscovery, and how membership is handled for hold policies vs. searches.

| Group type | Supported as data source | Hold behavior | Search behavior |
| --- | --- | --- | --- |
| Distribution list (static) | Yes | Members snapshotted at hold creation. Re-add the group to reflect membership changes. | Members re-resolved each time the search runs. |
| Exchange Dynamic Distribution Group (DDG) | No | Not supported as a hold data source. | Not supported as a search data source. |
| Mail-enabled security group | Yes | Same as distribution list. | Same as distribution list. |
| Microsoft 365 group | Yes | Group mailbox and associated SharePoint site snapshotted at hold creation. | Group mailbox and site re-resolved each time the search runs. |
| Microsoft Entra ID dynamic Microsoft 365 group | No | Same limitation as Entra dynamic security groups. | Same limitation as Entra dynamic security groups. |
| Microsoft Entra ID dynamic security group | No | Entra dynamic security groups (groups with a `membershipRule`) aren't supported. | Entra dynamic security groups aren't supported. |
| Microsoft Teams group | Yes | Group mailbox plus the associated SharePoint site snapshotted at hold creation. Channel sites resolved at hold creation. | Group mailbox and site re-resolved each time the search runs. |
| Viva Engage group | Yes | Group mailbox snapshotted at hold creation. | Group mailbox re-resolved each time the search runs. |

Note

If you need a scope that tracks dynamic membership criteria, create a static mail-enabled security group, synchronize its membership from the dynamic group on a schedule (for example, by using a scheduled Microsoft Graph and Exchange Online PowerShell job), and add the static shadow group as the data source. For holds, re-add the shadow group periodically to reflect updates. For searches, membership is re-resolved at each run.

## Add data sources to cases

Important

Data sources in the legacy eDiscovery experience don't synchronize to the same case in the new eDiscovery experience. You must add the data sources in the case in the new eDiscovery experience in the Microsoft Purview portal again.

After you [enable premium eDiscovery features](edisc-settings-cases) for a case, use the following options to add data sources to the case:

Tip

Want to try premium eDiscovery features? See the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Microsoft 365 Enterprise E5 licensing.

### Bulk import data sources to a case

In an eDiscovery case, you can add multiple data sources by importing a list of SMTP addresses, SharePoint site URLs, or supported SharePoint Embedded container URLs. The import feature validates the entries before adding the sources, so you can correct any potential problems, such as typos. This streamlined process helps you save time and add many data sources to your cases more efficiently.

Before you import data sources, review the following considerations:

- You can import up to 500 data sources at a time. To minimize the processing time for searching and adding locations, split the import into multiple imports instead of importing the maximum number of data sources at one time.
- You must use the `;` delimiter in your list of SMTP addresses or URLs. Your list should follow the formatting of the following example:

    `abh784@contoso.ms;https://contosodemos2.sharepoint.com/sites/Logistics;https://contosodemos2.sharepoint.com/sites/Mark8Project-UETConference;https://contosodemos2.sharepoint.com/sites/WG-ProjectObsidian;maib31@contoso.ms;rma230@contoso.ms;sva561@contoso.ms;mmz776@contoso.ms;LogisticsDSIGoldenSetDataToloka1@contoso.ms;jka132@contoso.ms;shafar929@contoso.ms;ika636@contoso.ms;brobet@contoso.ms;koka81@contoso.ms;rash95@contoso.ms;mvga66@contoso.ms;mra715@contoso.ms;abe543@contoso.ms;kto888@contoso.ms;moba80@contoso.ms;mian41@contoso.ms;inch48@contoso.ms;Mario.Smith_0803@contoso.ms;yape61@contoso.ms;mwo365@contoso.ms;fasi19@contoso.ms;HumanResourcesDugoPlannerTest@contoso.ms;kamo78@contoso.ms;bga844@contoso.ms;salesteam@contoso.ms;cko475@contoso.ms;ProjectZ@contoso.ms;TalentSourcingDanieltest5@contoso.ms;las450@contoso.ms;elfl69@contoso.ms;jch952@contoso.ms;asch81@contoso.ms;gmu955@contoso.ms;okbo68@contoso.ms`
- Distribution groups aren't expanded to individual members during the import process.
- To import an inactive mailbox as a data source, add a `.` prefix to the email address of the inactive mailbox. For example, `.sarad@contoso.onmicrosoft.com`.
- Unverified SMTP addresses aren't added, but unverified URLs are supported. An unverified URL means the data source can't be verified against a valid SharePoint site that is in a locked state.

To bulk import data sources to a case, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in by using the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, and then select **Cases** in the left navigation.
3. Select a case, and then select the **Data sources** tab to add data sources to the case. When you add sources to this tab, you make these data sources available to choose from in all searches and holds in the case.
4. Select **Bulk import**.
5. On **Add data sources**, enter or copy a list of SMTP addresses or URLs separated by a semicolon.
6. Select **Next**.
7. On **Confirm data sources**, view the list of data sources and the verification status.
8. After verification of the data sources finishes, unverified sources are highlighted in red and marked as *Unverified* for you to review.

    - To update unverified sources, select the check box next to the data source and select **Edit** to update the data source information. You can correct any typo, path, or format errors. After editing the selected source, select **Save** and the updated data sources are automatically reverified.
    - To export the list of data sources, select **Export list**. This action creates a .csv file that contains user inputs, matched sources, and the status of the sources.
    - Any input with multiple matches is shown with *(Duplicate)* in front. You can include a subset of duplicated matched sources based on your needs.
    - To remove any data sources from the import, select the data source and select **Delete**.
9. When you're ready to add any of the listed data sources, select the check box for each item you want to add and then select **Add**.

    Note

    Depending on the number of sources selected, it might take some time to process and add the data sources to the case.

### Add one or more data sources to a case

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in by using the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, and then select **Cases** in the left navigation.
3. Select a case, and then select the **Data sources** tab to add data sources to the case. When you add sources to this tab, all searches and holds in the case can choose these data sources.
4. Select **Add** and pick choices from the following data source areas:

    Note

    When searching for sources, some sources show up with a *?* in front of the source and labeled as *Unverified*. You can't verify these sources (sites or mailboxes) as valid sources when selected. These mailboxes or sites are external or the site is private or [locked](/en-us/sharepoint/manage-lock-status). You can add unverified sources to searches or holds and the system tries verification for these sources again when the search runs. Final search and hold results are included in the *location* .csv file in the [process report](edisc-process-report).

    1. The left side of the pane displays the **Filter** options for sources.
    2. In the **Scope items by** section, only **All sources in the tenant (default)** is available. Select any data source available in your organization.
    3. Use one of the following options in the **Show for** filter to help scope your sources in the **Search** section:

        - *All people and groups (default)*
        - *People only*
        - *Groups only*
    4. If applicable, select **Exclude inactive users** to reduce the scope of sources to only currently active users in your organization.
    5. After you filter data sources, use the search control and selectors in the **Search** section to add specific data sources, users, and groups to the search query. Enter the specific users, groups, or organization locations you want to add in the search field and select **Search**. You can use ";" as delimiter to trigger multiple searches at once. For example, input *john@contoso.com;david@contoso.com* allows you to search and find matches to both mailboxes at once. The `;` delimiter doesn't support site URLs.

        To add a supported SharePoint Embedded container directly, enter its full container URL as a site location.

        Search for people using the following values:

        - First and family name of the user display name (for example, John Smith)
        - First name only
        - User SMTP address
        - User alias
        - Exchange GUID
        - URL of the user's OneDrive site

        Search for groups using the following values:

        - Group mailbox SMTP address
        - URL of group site. The URL of a Teams channel site resolves the Teams group as a data source.

            If you add a distribution group, the list of group members isn't listed and the group is added to the search as a data source mailbox. When the search runs, the distribution group member mailboxes are expanded and fully searched.

            To confirm the mailboxes searched for the distribution group members, use the Locations\_*the date/time of the report* information in the [Process report](edisc-process-report) after the search is completed. To confirm group membership before running the search, select the ellipse menu for the group and *Members*.
5. Select **Add** to add the data source to the selected case. This data source is now available when adding data sources for searches and holds in the case.

Important

You can manage individual data resources for a data source only when you add the case-level data source to an individual search and hold in the case. For example, to include or exclude mailboxes or sites in a search or hold for a data source configured at the case level, add the case-level data source to the search or hold, and then select **Manage**.

## Add data sources to searches and holds

Add data sources to a specific search or hold by following these steps:

1. In a new search or hold, select **Add sources**. Or, select **+** and choose **Add data sources** from the dropdown. You can search for and select specific data sources to search or hold against.

    If you need to perform the search against organizational-wide mailboxes or sites, select **Add tenant-side sources in the empty search** or select the **+** button and choose an organizational-wide source from the dropdown.

    Note

    Organizational-wide sources are only available in searches, not holds.
2. The left side of the pane displays the **Filter** options for sources. Use filters to scope the data sources by:

    - **All sources in the tenant (default):** Use this option to search from data sources available in your organization.
    - **All sources in this case**: Use this option to choose from data sources added at the case level. By using this option, you can quickly use data sources added to the case in a search or hold without having to search across your entire organization.
    - Use one of the following options in the **Show for** filter to help scope your sources in the **Search** section:

        - *All people and groups (default)*
        - *People only*
        - *Groups only*
    - If applicable, select **Exclude inactive users** to reduce the scope of sources to only currently active users.
    - Use **Locations to include control** to specify if the selected data sources added to the search or hold include:

        - *Mailboxes and sites (default)*: Selected people or group sources include the mailbox and site to the search or hold. This selection means selecting the user includes both the mailbox and OneDrive for the user. Selecting a Microsoft 365 group includes the group mailbox and all associated group sites.
        - *Mailboxes only*: Only mailbox associated with the select user or group is included. OneDrive and SharePoint sites aren't included.
        - *Sites only*: Only sites associated with the select user or group are included. Mailboxes aren't included.
3. After you filter the data sources, use the search control and selectors in the **Search** section to add specific data sources, users, and groups to the search query. Enter the specific users, groups, or organization locations you want to add in the search field and select **Search**. Use a semicolon as delimiter for multiple searches at once. For example, *john@contoso.com;david@contoso.com* searches and finds matches for both mailboxes at once. The semicolon delimiter doesn't support site URLs.

    To add a supported SharePoint Embedded container directly, enter its full container URL as a site location.
4. Select **Manage** to review the locations associated with the selected sources.

    If you added a user as a data source, use **Filter by app** as needed, and then select or clear the supported SharePoint Embedded containers relevant to the investigation.
5. Select **Save and close** to add the data source to the current search or hold.

### Other considerations

- In the data source picker, you might not find some users or groups. In the **Manage** sources view, some selected sources might not display associated sites. This problem can happen for several reasons:

    - **OneDrive not provisioned, provisioning delay, or sync issues**: If a user doesn't have OneDrive provisioned, their source includes only a mailbox and not a OneDrive site. The OneDrive site exists, but it isn't synced in the compliance directory due to provisioning latency.
    - **Deleted or departed user**: If you remove a user from the directory or soft-delete or deactivate their account, their OneDrive site might still exist but isn't linked to their user object. It doesn't appear under their source in the **Manage** view. For email content, consider using an inactive mailbox if the mailbox was placed on hold before deletion. For OneDrive content from a deleted user, add the OneDrive site URL directly as a SharePoint location in the search or hold.
    - **Unlicensed user**: The user's Microsoft 365 license was removed, which breaks the link to their OneDrive site and can deactivate their mailbox. Reassign the required license and wait for the service to provision the data source before adding it again.
    - **Mailbox converted**: The user’s mailbox was converted to a shared mailbox or a mail user. This change might affect how the system associates OneDrive.
    - **Multiple site collection admins**: If the OneDrive site has multiple admins and ownership is unclear, the system might not map it to the original user.
    - **Retention or hold-only state**: The user has an inactive mailbox or hold-only state, and OneDrive might be cleaned up per retention policies.
    - **Unverified source**: When searching for data sources, some mailboxes or sites might appear with a **?** icon and the label *Unverified*. This status means the system couldn’t confirm the source as valid at selection time – often because the mailbox or site is external, private, or [locked](/en-us/sharepoint/manage-lock-status). You can still add unverified sources to searches or holds. Verification is attempted again when the search runs, and the final status is reflected in the **location.csv** file in the **[process report](edisc-process-report).**
    - **Ambiguous identity**: Duplicate entries exist in the directory, such as two users with similar names or an old account with the same alias. Work with your Microsoft Entra ID or Exchange admin to identify and remove duplicate objects so each email address corresponds to a single unique mailbox.
    - **Unresolved recipient**: The user can't be found in the directory. For newly created accounts, allow up to 24 hours for directory synchronization to complete. Verify in the Exchange admin center that the mailbox exists and is active.

If a user shows *Not available* after adding, remove and re-add the user after the underlying account issue is resolved. You can verify data source availability by checking the Microsoft 365 admin center for the user's account status. To check for duplicate objects, run `Get-Recipient -Filter "EmailAddresses -eq 'user@domain.com'"` in Exchange Online PowerShell.

Note

When sites show as **Not available**, manually add the URLs to the search or hold data sources.

- When you add a distribution group, the list of group members isn't displayed. The distribution group is added to the search as a data source mailbox. When you run the search, the system expands and fully searches the distribution group member mailboxes. To confirm the mailboxes searched for the distribution group members, use the `Locations_*the date/time of the report*` information in the **[Process report](edisc-process-report)** after the search completes. To confirm group membership before running the search, select the ellipsis menu for the group and members.

    If the membership of the distribution group changes after adding it as a data source in the search, run the search again to include items for the current members of the group. Each time you run the search, current members are included and former members are excluded.

### Inactive mailboxes

You can search, review, and export inactive mailboxes stored in your organization in eDiscovery. To hold inactive mailbox content, first apply the hold policy to the active mailbox, verify success, and then change the mailbox to inactive.

When using inactive mailboxes in eDiscovery searches and holds, consider the following points:

- Search inactive mailboxes in an eDiscovery search. For a list of the inactive mailboxes in your organization, run `Get-Mailbox -InactiveMailboxOnly` in Exchange Online PowerShell. Alternatively, go to **Data lifecycle management** &gt; **Microsoft 365** &gt; **Retention** in the Microsoft Purview portal and select **More** (the navigation bar ellipses).
- If an existing search includes a user mailbox and you update that mailbox to inactive, the search continues to search the inactive mailbox when you rerun the search.
- Some users might have an active mailbox and an inactive mailbox that have different SMTP addresses. In this case, only the specific mailbox you select as a location for a search is searched. If you add a user's mailbox to a search, you can't assume that both active and inactive mailboxes are searched. Only the mailbox you explicitly add to the search is searched.
- Use Security & Compliance PowerShell to create a search for an inactive mailbox. You must append a period to the email address of the inactive mailbox. For example, the following command creates a content search that searches an inactive mailbox with the email address pavelb@contoso.onmicrosoft.com:

    `New-ComplianceSearch -Name InactiveMailboxSearch -ExchangeLocation .pavelb@contoso.onmicrosoft.com -AllowNotFoundExchangeLocationsEnabled $true`
- Avoid having an active mailbox and inactive mailbox with the same SMTP address. If you need to reuse the SMTP address assigned to an inactive mailbox, recover the inactive mailbox or restore the contents of an inactive mailbox to an active mailbox (or the archive of an active mailbox), and then delete the inactive mailbox. For more information, see the following articles:

    - [Recover an inactive mailbox in Office 365](recover-an-inactive-mailbox)
    - [Restore an inactive mailbox in Office 365](restore-an-inactive-mailbox)
    - [Delete an inactive mailbox in Office 365](delete-an-inactive-mailbox)
- Hold policies aren't supported for inactive mailboxes. You must place holds on active mailboxes before the mailbox is deleted. For more information, see [Create and manage inactive mailboxes](create-and-manage-inactive-mailboxes).

## Data source options

After you add sources to a search or hold, you can edit the sources or explore related sources as needed. Select the *ellipsis* next to the source you want to edit or remove.

The following options are available in **User or group options**:

- Manage data source
- Include or remove a mailbox
- Include or remove sites

### Explore related sources

You can explore and add related sources from existing sources in a search or hold. These options give you the ability to investigate potentially relevant sources and bring in more sources to a specific search or hold.

For users you add in the **Data Sources** pane, you can explore the following connections:

- Manager
- Direct reports
- Frequent collaborators
- Groups the user owns
- Groups the user is a member of

By exploring these relationships, you can quickly identify and include relevant individuals and data sources in a search scope. Use *Manage* to fine-tune whether to include only mailboxes, only sites, or both related sources in a search or hold.

#### Manager

Use this option to explore upward in the reporting chain. When you select the user's manager, you include supervisory or decision-making context in your investigation.

#### Direct reports

Use this option to explore downward in the organization hierarchy for the user. This option is useful when the selected user is a manager or team lead, and you want to include their team members' communications or content.

#### Frequent collaborators

Use this option to find other users that frequently collaborate with the selected user. *Frequent collaborators* are the top 10 users who are most relevant to the selected user. You can select the mailboxes and sites for these users as data sources for searches.

#### Groups the user owns

This option shows groups that the selected user is listed as an owner. These groups might contain shared content or communications relevant to the investigation.

#### Groups the user is a member of

This option includes all groups the user is a member of, even if they're not the owner. These groups might provide additional context or shared data sources.

#### Group members

When you add a group in the **Data Sources** pane, you can explore and expand the group to view its members. By using this feature, you can:

- Identify individual users within the group that might hold relevant data.
- Select specific members as additional data sources for targeted searches.

This feature helps when investigating shared content or communications originating from collaborative groups such as Microsoft 365 Groups, Teams, or distribution lists.

Note

The list of group members and groups that a user is in (or owns) is capped at 100. If a user is included in more than 100 groups, owns more than 100 groups, or if a group has more than 100 members, the portal displays only the first 100 members.