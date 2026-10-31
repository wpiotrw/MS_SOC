---
layout: Conceptual
title: Search for and export Teams chat data for on-premises users | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-search-cloud-based-mailboxes-for-on-premises-users
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Admins can use eDiscovery tools in Microsoft 365 to search for and export Teams chat data for on-premises users in an Exchange hybrid deployment.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
- contentengagementFY23
search.appverid:
- MOE150
- MST160
- MET150
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: a7921bf6-0690-d766-dc78-947bb8260c79
document_version_independent_id: a7921bf6-0690-d766-dc78-947bb8260c79
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-search-cloud-based-mailboxes-for-on-premises-users.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-search-cloud-based-mailboxes-for-on-premises-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-search-cloud-based-mailboxes-for-on-premises-users.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 164e42e6-c2fd-e61a-af01-5c4a54fbde52
---

# Search for and export Teams chat data for on-premises users | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

If your organization has an Exchange hybrid deployment, you can use eDiscovery tools to search for and export Teams chat data for on-premises users. This option is also available for organizations that synchronize on-premises Exchange organization with Microsoft 365.

For a cloud-based users using Microsoft Teams enabled in your organization, chat data (also called *1x1 or 1xN chats*) is saved to their primary cloud-based mailbox. When an on-premises user uses the Teams chat application, their chat messages can't be stored in their primary mailbox, which is located on-premises. To get around this limitation, a feature where a cloud-based storage area is created so that you use eDiscovery tools to search for and export Teams chat data for on-premises users.

Here are the requirements and limitations for enabling cloud-based storage for on-premises users:

- The user accounts in your on-premises directory service (such as Active Directory) must be synchronized with Microsoft Entra ID, the directory service in Microsoft 365. This means that a mail user account is created in Microsoft 365 and is associated with a user whose primary mailbox is located in the on-premises organization.
- The user whose primary mailbox is located in the on-premises organization must be assigned a Microsoft Teams license and a minimum of an Exchange Online Plan 1 license.
- If your organization doesn't have an Exchange hybrid deployment, you must synchronize your on-premises Exchange schema to Microsoft Entra ID. If you don't do this, you might risk creating duplicate cloud-based mailboxes in Exchange Online for users that have a mailbox in your on-premises Exchange organization.
- Only the Teams chat data associated with an on-premises user is stored in the cloud-based storage area. An on-premises user can't access this storage area.

Note

Teams channel conversations are always stored in the cloud-based mailbox that's associated with the Team, which means you can search for channel conversations. For more information about searching Teams channel conversations, see [Searching Microsoft Teams and Microsoft 365 Groups](ediscovery-content-search-reference#searching-microsoft-teams-and-microsoft-365-groups).

## How it works

If a Microsoft Teams-enabled user has an on-premises mailbox and their user account/identity has been synched to the cloud, Microsoft creates cloud-based storage to associate the on-premises user's 1xN Teams chat data with. Teams chat data for on-premises users is indexed for search. This lets you use Content search (and searches associated with Microsoft Purview eDiscovery (Standard) and Microsoft Purview eDiscovery (Premium) cases) to search, preview, and export Teams chat data for on-premises users. You can also use **\*ComplianceSearch** cmdlets in [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell) to search for Teams chat data for on-premises users.

The following graphic shows the workflow of how Teams chat data for on-premises users is available to search, preview, and export.

![Cloud-based storage for on-premises users in Microsoft Teams.](media/ehamshard1.png)

In addition to this capability, you can also use eDiscovery tools to search, preview, and export Teams content in the cloud-based SharePoint site and Exchange mailbox associated with each Microsoft Team and 1xN Teams chat data in the Exchange Online mailbox for cloud-based users.

## Searching for and exporting Teams chat content for on-premises users

Here's how to use Content search in the Microsoft Purview portal to search for Teams chat data for on-premises users. You can also use the search tool in eDiscovery (Standard) to search for chat data for on-premises users.

1. In the [Microsoft Purview portal](https://compliance.microsoft.com), go to **Content search**.
2. On the **Searches** tab, select **New search**, and name the new search.
3. On the **Locations** page, set the toggle to **On** for Exchange mailboxes.
4. To search for Teams content for specific users (including on-premises users), select **Choose user, groups, or teams** and choose specific users to include in the search. If you don't list specific users, the search will include all users, including on-premises users.
5. Make sure the **Add app content for on-premises users** checkbox is selected. This ensures that the cloud-bases storage for on-premises users will be searched.

    ![Select the &quot;Add Office app content for on-premises users&quot; checkbox on the Locations workflow page.](media/ehamshardcheckbox.png)
6. On the **Define your search conditions** page, create a keyword query and add conditions to the search query if necessary. To only search for Team chats data, you can add the following query in the **Keywords** box:

    ```text
    kind:im AND kind:microsoftteams
    ```
7. Submit and run the search. Any search results for on-premises users can be previewed like any other search results. You can also export the search results (including any Teams chat data) to a PST file. For more information, see:

    - [Create a search](ediscovery-content-search)
    - [Preview search results](ediscovery-preview-search-results)
    - [Export search results](ediscovery-export-search-results)

## Using PowerShell to search for Teams chat data for on-premises users

You can use the **New-ComplianceSearch** cmdlets in [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell) to search for Teams chat data for on-premises users. As previously explained, you don't have to submit a support request to use PowerShell to search for Teams chat data for on-premises users.

1. Connect to [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
2. Run the following PowerShell command to create a content search that searches for Teams chat data for on-premises users.

    ```powershell
    New-ComplianceSearch <name of new search> -ContentMatchQuery <search query> -ExchangeLocation <on-premises user> -IncludeUserAppContent $true -AllowNotFoundExchangeLocationsEnabled $true
    ```

    The *IncludeUserAppContent* parameter is used to specify the cloud-based storage for the user or users who are specified by the *ExchangeLocation* parameter. The *AllowNotFoundExchangeLocationsEnabled* allows you to search the cloud-based storage for on-premises users. When you use the `$true` value for this parameter, the search doesn't try to validate the existence of the mailbox before it runs. This is required to search the cloud-based storage for on-premises users because this cloud-based storage doesn't resolve as a regular cloud-based mailbox.

    The following example searches for Teams chats that contain keyword "redstone" in the cloud-based storage for Sara Davis, who is an on-premises user in the Contoso organization.

    ```powershell
    New-ComplianceSearch "Redstone_Search" -ContentMatchQuery "redstone AND (kind:im AND kind:microsoftteams)" -ExchangeLocation sarad@contoso.com -IncludeUserAppContent $true -AllowNotFoundExchangeLocationsEnabled $true
    ```

    After you create a search, be sure to use the **Start-ComplianceSearch** cmdlet to run the search.

For more information using these cmdlets, see:

- [New-ComplianceSearch](/en-us/powershell/module/exchange/new-compliancesearch)
- [Start-ComplianceSearch](/en-us/powershell/module/exchange/start-compliancesearch)

## Limits

- Currently, you can search, preview, and export Teams chat data for on-premises users. You can also place the Teams chat data for an on-premises user on a hold associated with an eDiscovery (Standard) or eDiscovery (Premium) case, and apply a retention policy for Teams chats or channel messages for on-premises users. However, you can't apply a retention policy for other content locations (such as Exchange mailboxes and SharePoint sites) for on-premises users.

## Frequently asked questions

**Do I have to submit a support request to search for chat messages for on-premises users?**

No. This feature is enabled by default for all organizations. At one point, you did have to contact Microsoft Support but that is no longer the case.

**Can eDiscovery tools find older Teams chat data for on-premises users before the time that this feature was enabled by default for all organizations?**

Microsoft started storing the Teams chat data for on-premises users on January 31, 2018. If the identity of an on-premises Teams user has been synched between your on-premises Active Directory and Microsoft Entra ID in Microsoft 365 since this date, then their Teams chat data is stored in the cloud and is searchable using eDiscovery tools.

**Do on-premises users need a license to store their Teams chat data in the cloud?**

Yes. To store Teams chat data for an on-premises user in a cloud-based storage, the user must be assigned a Microsoft Teams license and an Exchange Online Plan license in Office 365 (or Microsoft 365).

**Where is the cloud-based storage for on-premises users located?**

Teams chat data is stored in the Preferred Data Location (PDL) for an on-premises user. The PDL is honored in both Single-Geo and Multi-Geo environments. For more information, see [Microsoft 365 Multi-Geo](/en-us/microsoft-365/enterprise/microsoft-365-multi-geo).

**Is there a risk of losing the Teams chat data if the user's on-premises mailbox is migrated to the cloud?**

No. When you migrate the primary mailbox of an on-premises user to the cloud, the Teams chat data for that user will be migrated to their new cloud-based primary mailbox.

**Can I apply an eDiscovery hold or retention policies to on-premises users?**

Yes. You can apply eDiscovery holds or retention policies for Teams chats and channel messages of on-premises users. But to preserve or retain Teams content for on-premises users, an on-premises user must be assigned an Exchange Online Plan 2 license.