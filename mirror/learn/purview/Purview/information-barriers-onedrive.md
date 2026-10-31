---
layout: Conceptual
title: Use Information Barriers with OneDrive | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-onedrive
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about associating segments with a OneDrive, and what happens when segments are associated with a OneDrive.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
audience: Admin
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-barriers
ms.collection:
- purview-compliance
- M365-collaboration
- essentials-compliance
ms.custom:
- onedrive-toc
- sfi-ga-nochange
search.appverid:
- ODB160
- ODB150
- MET150
ai-usage: ai-assisted
locale: en-us
document_id: 75381dbb-9ea7-54f6-3912-b650e632b2bd
document_version_independent_id: 75381dbb-9ea7-54f6-3912-b650e632b2bd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-onedrive.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-onedrive
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-onedrive.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 247f5ff5-0378-d902-3077-bd423d805f66
---

# Use Information Barriers with OneDrive | Microsoft Learn

[Microsoft Purview Information Barriers](information-barriers) are policies that prevent users from communicating and collaborating with each other. This article covers IB behavior in OneDrive.

For OneDrive, Information Barriers can determine and prevent the following kinds of unauthorized collaborations:

- User access to OneDrive or stored content
- Sharing OneDrive or stored content with other users

## Information Barriers modes and OneDrive

When you enable Information Barriers on SharePoint and OneDrive, you automatically protect the OneDrive of segmented users with IB policies. [Information Barriers modes](information-barriers-policies#step-6-information-barriers-modes-optional) help strengthen access, sharing, and membership of a OneDrive site based on its IB mode and segments associated with the OneDrive.

When you use Information Barriers with OneDrive, the following [IB modes](information-barriers-policies#step-6-information-barriers-modes-optional) apply:

- **Open**: The OneDrive has no segments. This mode is the default when a non-segmented user provisions their OneDrive.
- **Owner Moderated**: The OneDrive is used for collaboration with incompatible users in the presence of the site owner/moderator. See this section for details.
- **Explicit**: The user's segment and other compatible segments are associated with the OneDrive. This mode is the default when a segmented user provisions their OneDrive within 24 hours of enablement.
- **Mixed**: The segmented user's OneDrive is allowed to be shared with unsegmented users. This mode is an opt-in mode that the SharePoint admin can set on a OneDrive of a segmented user.

Note

Starting July 12, 2022, *Inferred* mode changed to *Mixed* mode. The functionality for the mode remains the same.

## Open mode

### Open mode sharing behavior

When a OneDrive has no segments and IB mode as *Open*:

- The user can share files and folders based on the IB policy applied to the user and the sharing setting for the OneDrive.

### Open mode access behavior

For a user to access content in a OneDrive with no segments and IB mode as *Open*:

- The files must be shared with the user.

## Owner Moderated mode

### Owner Moderated sharing behavior

When a OneDrive has Information Barriers mode set to *Owner Moderated*:

- The option to share with *Anyone with the link* is disabled.
- The option to share with *Company-wide link* is disabled.
- You can share the site and its content with existing members.
- Only the OneDrive owner can share the site and its content, following their IB policy.

### Owner Moderated access behavior

For a user to access a OneDrive with Information Barriers mode set to *Owner Moderated*:

- The user has site access permissions.

## Explicit mode

### Explicit mode sharing behavior

When a OneDrive has Information Barriers segments and the mode is set to *Explicit*:

- The option to share with *Anyone with the link* is disabled.
- The option to share with *Company-wide link* is disabled.
- You can share files and folders only with users whose segment matches that of the OneDrive.

### Explicit mode access behavior

For a user to access content in a OneDrive with segments and IB mode set to *Explicit*:

1. The user's segment matches a segment associated with the OneDrive.

    AND
2. The files are shared with the user.

Note

By default, non-segment users can access shared OneDrive files only from other non-segment users with IB modes set to *Open*. They can't access shared files from OneDrive that have segments applied and the IB mode is *Explicit*.

## Mixed mode

### Mixed mode sharing behavior

When a OneDrive uses Information Barriers segments and the mode is set to *Mixed*:

- The option to share with *Anyone with the link* is disabled.
- The option to share with *Company-wide link* is disabled.
- You can share files and folders with users whose segment matches that of the OneDrive and unsegmented users in the tenant.

### Mixed mode access behavior

For a segmented user to access content in a OneDrive with segments and IB mode set to *Mixed*:

1. The user's segment matches a segment associated with the OneDrive.

    AND
2. The files are shared with the user.

For an unsegmented user to access content in a OneDrive with segments and IB mode set to *Mixed*:

- The user has site access permissions.

## Example scenario

The following example illustrates three segments in an organization: HR, Sales, and Research. You define an IB policy that blocks communication and collaboration between the Sales and Research segments.

![Example of segments in an organization](media/info-barriers-segments-example.png)

By using Information Barriers in OneDrive, when you apply a segment to a user, the segment automatically associates with the user's OneDrive within 24 hours. The OneDrive also associates with other segments that are compatible with the user's segment and with each other. A OneDrive can have up to 100 associated segments. A global or SharePoint admin can manage these segments by using PowerShell, as described later in the section Associate or remove additional segments on a user's OneDrive.

The following table shows the effects of this example configuration:

| Components | HR users | Sales users | Research users | Non-segment users |
| --- | --- | --- | --- | --- |
| Segments associated with OneDrive | HR | Sales, HR | Research, HR | None |
| IB mode on OneDrive | Explicit | Explicit | Explicit | Open |
| OneDrive content can be shared with | HR only | Sales and HR | Research and HR | Anyone based on the sharing settings selected |
| OneDrive content can be accessed by | HR only | Sales and HR | Research and HR | Anyone with whom the content is shared |

## Enable SharePoint and OneDrive Information Barriers in your organization

You configure enabling Information Barriers for SharePoint and OneDrive in a single action. You can't enable Information Barriers for the services separately. For more information, see [Enable SharePoint and OneDrive Information Barriers in your organization](information-barriers-sharepoint#enable-sharepoint-and-onedrive-information-barriers-in-your-organization). After you enable Information Barriers for SharePoint and OneDrive, continue with the OneDrive guidance in this article.

## Prerequisites

1. Make sure you meet the [licensing requirements for Information Barriers](https://aka.ms/M365EnterprisePlans).
2. [Create IB policies](information-barriers-policies) that allow or block communication between the segments and activate the policies. Create segments and define the users in each.
3. After you configure and activate your IB policies, wait 24 hours for the changes to propagate through your organization.
4. Enable Information Barriers for OneDrive. You configure enabling Information Barriers for SharePoint and OneDrive in a single action. You can't enable these services separately. For more information, see the guidance and steps in the [Use Information Barriers with SharePoint](information-barriers-sharepoint) article.
5. Complete the steps in the following sections to customize and manage Information Barriers for OneDrive in your organization.

## Use PowerShell to view the segments associated with a OneDrive

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

A global admin or SharePoint admin can view and change the segments associated with a user's OneDrive. Your organization can have up to 5,000 segments, and users can be assigned to multiple segments.

Important

Support for 5,000 segments and assigning users to multiple segments is only available when your organization isn't in *Legacy* mode. Assigning users to multiple segments requires extra steps to change the Information Barriers mode for your organization. For more information, see [Use multi-segment support in Information Barriers](information-barriers-multi-segment).

For organizations in *Legacy* mode, the maximum number of segments supported is 250, and users are restricted to being assigned to only one segment. Organizations in *Legacy* mode are eligible to upgrade to the newest version of Information Barriers in the future. For more information, see the [Information Barriers roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=information%2Cbarriers).

1. Connect to [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) as a global admin.
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
5. Connect to SharePoint as a [global admin or SharePoint admin](/en-us/sharepoint/sharepoint-admin-role?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) in Microsoft 365. For more information, see [Getting started with SharePoint Online Management Shell](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).
6. Run the following command:

    ```PowerShell
    Get-SPOSite -Identity <site URL> | Select InformationSegment
    ```

    For example:

    ```powershell
    Get-SPOSite -Identity https://contoso-my.sharepoint.com/personal/John_contoso_onmicrosoft_com | Select InformationSegment
    ```

## Manage segments on a user's OneDrive

Warning

If the segments associated with a user's OneDrive don't match the segment you apply to the user, the user can't access their OneDrive. Don't associate any segments with the OneDrive of a non-segment user.

Note

Any changes you make are overwritten if the user's segment changes.

To associate a segment with a OneDrive, run the following command in the SharePoint Online Management Shell.

```PowerShell
Set-SPOSite -Identity <site URL> -AddInformationSegment <segment GUID>
```

For example:

```powershell
Set-SPOSite -Identity https://contoso-my.sharepoint.com/personal/John_contoso_onmicrosoft_com -AddInformationSegment 27d20a85-1c1b-4af2-bf45-a41093b5d111
```

When you add segments to a OneDrive, the site's IB mode automatically updates to *Explicit*. An error appears if you attempt to associate a segment that isn't compatible with the existing segments on the OneDrive.

To remove a segment from a OneDrive, run the following command.

```PowerShell
Set-SPOSite -Identity <site URL> -RemoveInformationSegment <segment GUID>
```

For example:

```powershell
Set-SPOSite -Identity https://contoso-my.sharepoint.com/personal/John_contoso_onmicrosoft_com -RemoveInformationSegment 27d20a85-1c1b-4af2-bf45-a41093b5d111
```

If you remove all the segments of a OneDrive site, the IB mode of the OneDrive automatically updates to *Open*.

## Manage the IB mode of a user's OneDrive (preview)

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

To view the IB mode of a OneDrive site, run the following command in the SharePoint Online Management Shell as a SharePoint admin or global administrator:

```powershell
Get-SPOSite -Identity <site URL> | Select InformationBarriersMode
```

For example:

```powershell
Get-SPOSite -Identity https://contoso-my.sharepoint.com/personal/John_contoso_onmicrosoft_com | Select InformationBarriersMode
```

A SharePoint admin or global administrator can also manage the IB mode of a OneDrive site to meet the needs of your organization by using new IB modes:

### Owner Moderated mode example

Allow an incompatible segment user access to a OneDrive. For example, you want to allow HR user's OneDrive to be accessed by both Sales and Research segment users in your tenant.

*Owner Moderated* is a mode applicable to OneDrive sites that allows incompatible segment users to access OneDrive in the presence of a moderator/owner. Only the site owner has the capability to invite incompatible segment users on the same site.

To update a OneDrive site IB mode to *Owner Moderated*, run the following PowerShell command:

```powershell
Set-SPOSite -Identity <siteurl> -InformationBarriersMode OwnerModerated
```

You can't set the Owner Moderated IB mode on a site with segments. Remove the segments before setting the IB mode as Owner Moderated. Users with site access permissions can access an Owner Moderated site. Only the site owner can share an Owner Moderated OneDrive and its contents per their IB policy.

### Mixed mode example

Allow unsegmented users to access OneDrive associated with segments. For example, you want to allow HR users' OneDrive to be accessed by HR segment and unsegmented users in your tenant. Mixed mode applies to OneDrive sites that allow segmented and unsegmented users to access OneDrive.

To update a OneDrive site's IB Mode to Mixed, run the following PowerShell command:

```powershell
Set-SPOSite -Identity <siteurl> -InformationBarriersMode Mixed
```

You can't set mixed IB mode on a site without segments. Add segments before setting the IB mode as mixed.

## Effects of changes to user segments

If a user's segment changes, the OneDrive segment and IB mode automatically update within 24 hours as described in the OneDrive Information Barriers section.

**Example 1:** User's segment updated from Research to Sales, the user's OneDrive updates as follows within 24 hours:

- Segment: Sales, HR
- IB mode: *Explicit*

**Example 2:** User's segment updated from HR to None

- Segment: None
- IB mode: *Open*

## Effects of changes to IB policies

If a compliance administrator changes an existing policy, the change might affect the compatibility of the segments associated with the OneDrive.

For example, segments that were once compatible might no longer be compatible. A SharePoint admin must change the segments associated with an affected site. For more information, see [create an Information Barriers policy compliance report in PowerShell](information-barriers-sharepoint-report).

If you change a policy after users share files, the sharing links work only if the user attempting to access the shared files has a segment applied that matches a segment associated with the OneDrive.

## Auditing

Audit events are available in the [Microsoft Purview portal](purview-portal) to help you monitor IB activities. The system logs audit events for the following activities:

- Enabling Information Barriers for SharePoint and OneDrive
- Applying segment to site
- Changing segment of site
- Removing segment of site
- Applying Information Barriers mode to site
- Changing Information Barriers mode of site
- Disabling Information Barriers for SharePoint and OneDrive

For more information about OneDrive segment auditing in Microsoft 365, see [Search the audit log](audit-search).