---
layout: Conceptual
title: Use Information Barriers with SharePoint | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about associating segments with a site, and what happens when segments are associated with a site.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
audience: Admin
f1.keywords:
- CSH
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-barriers
ms.custom:
- admindeeplinkSPO
- sfi-ga-nochange
- sfi-image-nochange
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.collection:
- purview-compliance
- M365-collaboration
ai-usage: ai-assisted
locale: en-us
document_id: b3c86d83-4ba7-d7e3-578e-ae0a47dbbc6e
document_version_independent_id: b3c86d83-4ba7-d7e3-578e-ae0a47dbbc6e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-sharepoint.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-sharepoint
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-sharepoint.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 7b94accc-f243-ad5b-a91b-fc5c1b5c7c35
---

# Use Information Barriers with SharePoint | Microsoft Learn

[Microsoft Purview Information Barriers (IB)](information-barriers) are policies that prevent users from communicating and collaborating with each other. This article covers IB behavior in SharePoint.

For SharePoint, Information Barriers can determine and prevent the following kinds of unauthorized collaborations:

- Adding a user to a site
- User access to a site or site content
- Sharing a site or site content with other users

## Information Barriers modes and SharePoint sites

[Information Barriers modes](information-barriers-policies#step-6-information-barriers-modes-optional) help strengthen access, sharing, and membership of a site based on its IB mode and segments associated with the site.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

When you use Information Barriers with SharePoint, the following [IB modes](information-barriers-policies#step-6-information-barriers-modes-optional) apply:

- **Open**: The site has no segments. Anyone can be invited to be a member. This mode is the default when a SharePoint site doesn't have segments.
- **Owner Moderated**: The site owner moderates collaboration between incompatible segments. Only the resource owner can add new members per their IB policy.
- **Implicit**: Microsoft Teams sets the site's IB mode when it provisions the site. A SharePoint Administrator or Global Administrator can't manage segments with the *Implicit* mode configuration.
- **Explicit**: Segments are associated with the site, either through user site creation or by a SharePoint Administrator. Only users matching the site's segments can access and share content.

## Open mode

### Open mode sharing behavior

When a site has no segments and you set the site's IB mode to *Open*:

- Users can share the site and its contents based on the IB policy applied to them. For example, if a user in HR is allowed to communicate with users in Research, the user can share the site with those users.

Tip

If you want to allow sharing of *Open* mode sites with mail-enabled security groups, see the Allow sharing of Open mode sites with mail-enabled security groups section in this article.

### Open mode access behavior

For a user to access a SharePoint site that has no segment and the site's Information Barriers mode is set to *Open*:

- The user has site access permissions.

## Owner Moderated mode

### Owner Moderated sharing behavior

When you set a site's Information Barriers mode to *Owner Moderated*:

- The option to share with *Anyone with the link* is disabled.
- The option to share with *Company-wide link* is disabled.
- (For group connected sites) The site and its content can be shared with existing members.
- (For non-group connected sites) Only the site owner can share the site and its content, according to their IB policy.

### Owner moderated access behavior

For a user to access a SharePoint site with the site's Information Barriers mode set to *Owner Moderated*:

- (For non-group connected sites) The user has site access permissions.
- (For group connected sites) The user must be a member of the Microsoft 365 group connected to the site.

## Implicit mode

### Implicit mode sharing behavior

When you set a site's Information Barriers mode to *Implicit*:

- The option to share with *Anyone with the link* is disabled.
- The option to share with *Company-wide link* is disabled.
- The site and its content can be shared with existing members via a sharing link.
- You can't add new users to the site directly. The Team owner should add users to the Team's group by using Microsoft Teams.

Note

If you enabled Information Barriers for SharePoint in your organization before March 15, 2022, see the **Enable SharePoint and OneDrive Information Barriers** section in this article.

### Implicit mode access behavior

To access SharePoint sites that use Information Barriers mode set to *Implicit*:

- You're a member of the Microsoft 365 group connected to the site.
- If you're not a member of the Microsoft 365 group connected to the site, you can't access the site.
- The Information Barriers compliance assistant ensures the group membership is IB compliant.

Note

If you enabled Information Barriers for SharePoint in your organization before March 15, 2022, see the **Enable SharePoint and OneDrive Information Barriers** section in this article.

## Explicit mode

### Explicit mode sharing behavior

When you associate a site with segments and set the site's Information Barriers mode to *Explicit*:

- The option to share with *Anyone with the link* is disabled.
- The option to share with *Company-wide link* is disabled.
- You can share the site and its content only with users whose segment matches that of the site. For example, if you associate a site with the HR segment, you can share the site with just HR users (even though HR is compatible with both Sales and Research segments).
- You can add new users as site members only if their segment matches the segment of the site.

### Explicit mode access behavior

To access SharePoint sites that use segments and site's Information Barriers mode is *Explicit*:

- Your segment matches a segment that's associated with the site.

    AND
- You have access permission to the site.

Non-segment users can't access a site associated with segments. They see an error message.

## Allow apps running in app-only mode to access IB sites

Many organizations use applications running in an app-only context in their organization. To allow these apps running in app-only mode to access IB protected sites, SharePoint admins can enable the opt-in capability.

Important

Information Barriers policies might impact the applications accessing sites in app-only mode. Enable the policy and then test the experience for the apps used in your organization.

To enable applications running in app-only mode to access IB sites, run the following command:

```powershell
Set-SPOTenant -AppBypassInformationBarriers $true
```

If you enable Teams Meeting Recording or EDU Assignment application in your organization, run the following command to allow these applications to interact with IB protected sites:

```powershell
Set-SPOTenant -AppOnlyBypassPeoplePickerPolicies $true
```

## Example scenario

The following example illustrates three segments in an organization: HR, Sales, and Research. An IB policy blocks communication and collaboration between the Sales and Research segments. These segments are incompatible.

![Example of segments in an organization.](media/info-barriers-segments-example.png)

By using SharePoint Information Barriers, a SharePoint Administrator or Global Administrator can associate segments to a site to prevent the site from being shared with or accessed by users outside the segments. You can associate up to 100 compatible segments with a site. You associate the segments at the site level (previously called site collection level). The Microsoft 365 group connected to the site is also associated with the site's segment.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

In the previous example, the HR segment is compatible with both Sales and Research. However, because the Sales and Research segments are incompatible, you can't associate them with the same site.

## Prerequisites

1. Make sure you meet the [licensing requirements for Information Barriers](https://aka.ms/M365EnterprisePlans).
2. [Create IB policies](information-barriers-policies) that allow or block communication between the segments, and then set them to active. Create segments and define the users in each segment.
3. Wait 24 hours after configuring and activating your IB policies for the changes to propagate through your organization.
4. Complete the steps in the following sections to enable and manage SharePoint and OneDrive Information Barriers in your organization.

## Enable SharePoint and OneDrive Information Barriers in your organization

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

SharePoint Administrators or Global Administrators can enable Information Barriers in SharePoint and OneDrive in your organization. Complete the following steps to enable Information Barriers for your organization:

1. You must use the latest version of the [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). If you installed a previous version of the SharePoint Online Management Shell, go to **Add or remove programs** and uninstall *SharePoint Online Management Shell*. Then, install the latest version. To learn more, see [Get started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
2. Connect to SharePoint Online as a Global Administrator or [SharePoint Administrator](/en-us/sharepoint/sharepoint-admin-role?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) in Microsoft 365. For more information, see [Getting started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
3. Run the following command to enable Information Barriers in SharePoint and OneDrive:

    ```PowerShell
    Set-SPOTenant -InformationBarriersSuspension $false
    ```
4. Wait for approximately 1 hour for the changes to take effect after you enable Information Barriers for SharePoint and OneDrive in your organization.

Note

If you enabled Information Barriers for SharePoint in your organization before March 15, 2022, the default access and sharing control for Implicit mode for Microsoft Teams-connected sites are based on the segments associated with the site.

To enable Microsoft 365 group-membership based access and sharing control for all Implicit mode Teams-connected sites in your tenant, run the following command:

```powershell
Set-SPOTenant -IBImplicitGroupBased $true
```

Note

If you have Microsoft 365 Multi-Geo, run this command for each of your geolocations.

## View and manage segments as an administrator

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

SharePoint Administrators or Global Administrators can view and manage segments on a SharePoint site. Your organization can have up to 5,000 segments, and users can be assigned to multiple segments.

Important

Support for 5,000 segments and assigning users to multiple segments is only available when your organization isn't in *Legacy* mode. Assigning users to multiple segments requires extra steps to change the Information Barriers mode for your organization. For more information, see [Use multi-segment support in Information Barriers](information-barriers-multi-segment).

For organizations in *Legacy* mode, the maximum number of segments supported is 250, and users are restricted to being assigned to only one segment. Organizations in *Legacy* mode are eligible to upgrade to the newest version of Information Barriers in the future. For more information, see the [Information Barriers roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=information%2Cbarriers).

View and manage Information Barriers segments as follows:

### 1. Use the SharePoint admin center to view and manage information segments

To view, edit, or remove information segments for a site, use [**Active sites** in the SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185220).

The Segments column lists the first segment associated with the site and shows whether the site has other segments associated. [Learn how to show or move this column](/en-us/sharepoint/customize-admin-center-site-list?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#customize-columns).

![Segments column on the Active sites page.](media/info-barriers-segments-column.png)

To view the complete list of segments associated with a site, select the site name to open the details panel, and then select the **Settings** tab.

To edit the segments associated with the site, select **Edit**, add or remove segments, and then select **Save**.

![Edit information segments panel.](media/info-barriers-edit-info-segments.png)

### 2. Use SharePoint PowerShell to view and manage information segments on a site

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

1. Connect to [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) as a Global Administrator.
2. Run the following command to get the list of segments and their GUIDs.

    ```PowerShell
    Get-OrganizationSegment | ft Name, EXOSegmentID
    ```
3. Save the list of segments.

    | **Name** | **EXOSegmentId** |
    | --- | --- |
    | Sales | a9592060-c856-4301-b60f-bf9a04990d4d |
    | Research | 27d20a85-1c1b-4af2-bf45-a41093b5d111 |
    | HR | a17efb47-e3c9-4d85-a188-1cd59c83de32 |
4. You must use the latest version of the [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). If you installed a previous version of the SharePoint Online Management Shell, go to **Add or remove programs** and uninstall *SharePoint Online Management Shell*. Then, install the latest version. To learn more, see [Get started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
5. Connect to SharePoint Online as a [Global Administrator or SharePoint Administrator](/en-us/sharepoint/sharepoint-admin-role?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) in Microsoft 365. For more information, see [Getting started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
6. Run the following command:

    ```PowerShell
    Set-SPOSite -Identity <site URL> -AddInformationSegment <segment GUID>
    ```

    For example:

    ```powershell
    Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite -AddInformationSegment 27d20a85-1c1b-4af2-bf45-a41093b5d111
    ```

You see an error message if you attempt to associate a segment that isn't compatible with the site's existing segments.

Note

When you add a segment to a site, the site's IB mode is automatically updated to *Explicit*.

To remove a segment from a site, run the following command:

```PowerShell
Set-SPOSite -Identity <site URL> -RemoveInformationSegment <segment GUID>
```

For example:

```powershell
Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite -RemoveInformationSegment 27d20a85-1c1b-4af2-bf45-a41093b5d111
```

Note

When you remove all segments from a site, the site's IB mode is automatically updated to *Open*.

To view the segments of a site, run the following command to return the GUIDs of any segments associated with the site.

```PowerShell
Get-SPOSite -Identity <site URL> | Select InformationSegment
```

### 3. Use the SharePoint REST API to view and manage information segments on a site

SharePoint includes a Representational State Transfer (REST) service that you can use to manage segments on a site. To access SharePoint resources and manage site segments by using REST, construct a RESTful HTTP request by using the OData standard. This request corresponds to the desired client object model application programming interface (API).

For more information about the SharePoint REST service, see [Get to know the SharePoint REST service](/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## View and manage IB modes as an administrator with SharePoint PowerShell

To view the IB mode of a site, run the following command:

```powershell
Get-SPOSite -Identity <site URL> | Select InformationBarriersMode
```

### Owner Moderated mode scenario

You want to allow a Sales and Research user to collaborate on a SharePoint site in the presence of an HR user.

*Owner Moderated* is a mode applicable to sites (Teams-connected sites, non-group connected sites) that grants incompatible segment users access to the site. Only the site owner can invite incompatible segment users to the same site.

To update a site's mode to *Owner Moderated*, run the following PowerShell command:

```powershell
Set-SPOSite -Identity <siteurl> -InformationBarriersMode OwnerModerated
```

You can't set the Owner Moderated IB mode on a site with segments. Remove the segments first before setting IB mode as Owner Moderated. Users who have site access permissions can access an Owner Moderated site. Only the site owner can share an Owner Moderated site and its contents according to their IB policy.

## Auditing

You can view audit events in the [Microsoft Purview portal](purview-portal) to monitor IB activities. The system logs audit events for the following activities:

- Enabling Information Barriers for SharePoint and OneDrive
- Applying a segment to a site
- Changing the segment of a site
- Removing the segment of a site
- Applying Information Barriers mode to a site
- Changing Information Barriers mode of a site
- Disabling Information Barriers for SharePoint and OneDrive

For more information about SharePoint segment auditing in Microsoft 365, see [Search the audit log in the Microsoft Purview portal](audit-supported-services).

## Site creation and management by site owners

When a segmented user creates a SharePoint site, the site associates with the user's segment and the site's Information Barriers mode automatically sets to *Explicit*.

Site owners can add more segments to a SharePoint site that already has segments with the site's mode set as *Explicit*. Site owners can't remove added segments from sites. SharePoint Administrators need to remove added segments in your organization if needed.

When a non-segmented user creates a SharePoint site, the site doesn't associate with any segment and the site's Information Barriers mode automatically sets to *Open*.

When a SharePoint Administrator creates a SharePoint site from the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219), the site doesn't associate with any segment and the site's IB mode sets to *Open*.

To help site owners add a segment to a site, share the [Associate information segments with SharePoint sites](https://support.microsoft.com/office/associate-information-segments-with-sharepoint-sites-2b03db07-6d3f-4297-a388-b943317a26a7) article with your SharePoint site owners.

## Microsoft Teams sites

When you create a team in Microsoft Teams, you also automatically create a SharePoint site for the team's files. To protect the Microsoft Teams sites by using Information Barriers control, enable Information Barriers in SharePoint for your tenant.

Within 24 hours, the site's Information Barriers mode is automatically set to *Implicit* and segments associated with the team's members are associated with the site.

Microsoft Teams sites with the IB mode set to *Implicit* have site access and sharing based on Microsoft 365 group membership.

For example, users have access to the Microsoft Teams site if they're members of the Microsoft 365 group connected to the site. The Microsoft 365 group connected to the Team is IB compliant.

Note

If you enabled Information Barriers for SharePoint in your organization before March 15, 2022, the Teams-connected site's access and sharing is based on the segments of the site. For example:

- You can share the site and its content with users whose segment matches that of the site.
- Users can access the site and its content if they have the same segment as that of the site and have site access permissions.

To enable Microsoft 365 group membership-based access and sharing control for all *Implicit* mode sites in your organization, see Enable SharePoint and OneDrive Information Barriers in your organization.

## Private channel and Information Barriers

When you enable SharePoint Information Barriers in your organization, any new private channel site automatically inherits its parent Microsoft Team's IB mode within 24 hours. The mode for a private channel is assigned as follows:

| Parent Team's IB mode | Private channel site's IB mode |
| --- | --- |
| Open | Open |
| Implicit or Owner Moderated | Implicit |

The private channel site's IB mode governs access and sharing for the private channel site:

- Private channel site with *Open* Information Barriers mode

    - Access anyone with site access permissions
    - Sharing links are allowed per the site's existing sharing policy
    - People picker allows discoverability of user per the sharer's IB policy
- Private channel site with *Implicit* Information Barriers mode

    - Access only to users who are currently members of the private channel
    - Sharing by using **People with existing access link**

Private channel sites already configured in your organization have their Information Barriers mode set as *Open*. To configure existing private channel sites to *Implicit* mode, run the following cmdlet in the SharePoint PowerShell module:

```powershell
Set-Sposite -Identity <site URL> -InformationBarriersMode Implicit
```

Learn more about managing [Microsoft Teams connected teams sites](/en-us/sharepoint/teams-connected-sites?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Search

Users see search results from:

- **Segment associated sites**: When the site's segment matches the user's segment and the user has site access permission. For example, a site with *Explicit* mode.
- **Non-segmented sites**: When the user has existing access to the content or site. For example, sites with *Open*, *Owner Moderated*, or *Implicit* mode. When the user selects the search result to open the content in the site, the user is denied access if they don't match the site's IB policy.

### Tenant wide search and Copilot experience

Users experience is as follows:

- **Segment associated sites**: When the site's segment matches the user's segment and the user has site access permission. For example, a site with *Explicit* mode.
- **Open mode sites:** When the user has existing access to the content or site.
- **Implicit and Owner moderated mode sites:**

    - When the user has existing access to the content or site.
    - If the user had access to the site and content prior to the policy application, they continue to see the site and its contents in search and Copilot results. However, when attempting to open the content, they're denied access if they don't comply with the site's IB policy.

## Effects of changes to user segments

If a SharePoint site owner or site member's segment changes, they retain access to the site or content according to the site's IB mode:

- **Open mode**: User can access the site if they have existing site access permissions.
- **Owner Moderated**: User can access the site if they have existing site access permissions.
- **Implicit Mode**: If the user is a member of the Microsoft 365 group, they retain access to the site.
- **Explicit Mode**: If the user's new segment matches the site's segment and user has site access permissions, they retain access to the site.

## Effects of changes to existing IB policies

If a compliance administrator changes an existing IB policy, the change might affect the compatibility of the segments associated with a site (in *Explicit* or *Implicit* mode\*). For example, segments that were once compatible might no longer be compatible.

By using the Information Barriers policy compliance report, the SharePoint Administrator can view the list of sites where segments are no longer compatible. For more information, see [Learn how to create an Information Barriers policy compliance report in PowerShell](information-barriers-sharepoint-report).

To manage out of compliance sites:

- In *Explicit* mode, a SharePoint Administrator must change the associated segments to bring them into IB compliance.
- In *Implicit* mode, a SharePoint Administrator can't manage segments directly. The Teams admin should manage the Team's membership to bring the Teams membership roster and segments into IB compliance.

## How to suspend SharePoint and OneDrive Information Barriers in your organization

If your organization wants to temporarily suspend Information Barriers on SharePoint, use SharePoint Online Management Shell and the [Set-Spotenant](/en-us/powershell/module/sharepoint-online/set-spotenant?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) cmdlet.

To suspend Information Barriers, run the following command:

```PowerShell
Set-SPOTenant -InformationBarriersSuspension $true
```

Note

If you have Microsoft 365 Multi-Geo, run this command for each of your geo-locations.

## Allow sharing of Open mode sites with mail-enabled security groups

IB supports an opt-in capability available in the [SharePoint PowerShell module](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) for sites in *Open* mode to be shared with [mail-enabled security groups](/en-us/microsoft-365/admin/email/create-edit-or-delete-a-security-group?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) for site permissions, sharing, and audience targeting. This capability is only supported in *Open* mode sites. SharePoint admins can enable this support in your organization. Ensure the security group membership is IB compliant.

Before enabling group support, verify that you meet the following prerequisites:

- Your organization has only IB [*Block* policies](information-barriers-policies#configuration-concepts).
- Your organization is enabled for SharePoint IB (see this section in this article).

To configure mail-enabled security group support in *Open* mode sites, run the following command:

```powershell
Set-SPOTenant -ShowPeoplePickerGroupSuggestionsForIB $true
```