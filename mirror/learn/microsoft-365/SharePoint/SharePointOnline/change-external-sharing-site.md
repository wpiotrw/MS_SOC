---
layout: Conceptual
title: Change the sharing settings for a site - SharePoint in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/sharepoint/change-external-sharing-site
breadcrumb_path: /sharepoint/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-SharePoint
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/06735c62-321c-ec11-b6e7-0022481f8472
recommendations: true
ms.date: 2026-05-07T00:00:00.0000000Z
ms.reviewer: srice
ms.author: deniseb
author: denisebmsft
manager: dansimp
audience: Admin
f1.keywords:
- CSH
ms.topic: how-to
ms.service: sharepoint-online
ms.subservice: admin
ms.localizationpriority: medium
ms.collection:
- Strat_OD_share
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ms.assetid: 6288296a-b6b7-4ea4-b4ed-c297bf833e30
customer-intent: As a SharePoint Administrator, I want to change the external sharing settings for a specific site so that I can control collaboration with people outside my organization.
description: Learn how Global and SharePoint Administrators can change site-level sharing settings.
locale: en-us
document_id: 3106844b-caae-38c5-3c88-fb17a9d67536
document_version_independent_id: 3e88e60e-24a3-cd83-9bfc-8bc3037a86ce
original_content_git_url: https://github.com/MicrosoftDocs/OfficeDocs-SharePoint-pr/blob/live/SharePoint/SharePointOnline/change-external-sharing-site.md
site_name: Docs
depot_name: office.OfficeDocs-SharePoint
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.OfficeDocs-SharePoint/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: change-external-sharing-site
moniker_range_name: 
monikers: []
item_type: Content
source_path: SharePoint/SharePointOnline/change-external-sharing-site.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: eea975cc-5ef0-bfcc-f51e-5427d4bbcb82
---

# Change the sharing settings for a site - SharePoint in Microsoft 365 | Microsoft Learn

You must be at least a [SharePoint Administrator](sharepoint-admin-role) in Microsoft 365 to change the sharing settings for a site. Site owners can't change these settings.

The steps in this article apply to team sites, communication sites, and classic sites. To learn how to change the external sharing setting for a user's OneDrive, see [Change the external sharing setting for a user's OneDrive](user-external-sharing-settings). For info about changing your organization-level settings, see [Manage sharing settings](turn-external-sharing-on-or-off). Guest sharing settings for Microsoft 365 Groups and Teams affect connected SharePoint sites.

For detailed information about how to set up guest access for a site, see [Collaborate with guests in a site](/en-us/Office365/Enterprise/collaborate-in-a-site).

Important

[Microsoft Entra external collaboration settings](/en-us/azure/active-directory/external-identities/external-collaboration-settings-configure) determine who can invite guests in your organization for site sharing (always) and file and folder sharing (if Azure B2B collaboration is enabled). Be sure to review Microsoft Entra guest access settings as part of your SharePoint and OneDrive sharing setup.

## How do I change the external sharing setting for a site?

To change the external sharing setting:

1. Go to [**Active sites** in the new SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185220), and sign in with an account that has [admin permissions](sharepoint-admin-role) for your organization.
2. In the left column, select a site. (For a channel site, select the link in the **Channel sites** column and then select the site.)
3. On the **Settings** tab, select **More sharing settings**.
4. Select an external sharing option (see the table in the next section).

    ![Changing the external sharing setting for a site](sharepointonline/media/external-sharing-site.png)
5. If you want to limit the sharing of this site by domain, select the **Limit sharing by domain** check box by expanding **Advanced settings for external sharing**, and add the domains that you want to allow or block.

    Important

    [Allowed or blocked domains in Microsoft Entra ID](/en-us/azure/active-directory/external-identities/allow-deny-list) also affect SharePoint and OneDrive site sharing (always) and file and folder sharing (if Azure B2B collaboration is enabled). Be sure to review Microsoft Entra collaboration restrictions as part of your SharePoint and OneDrive sharing setup.
6. If you want to change the guest access expiration setting for this site, clear the **Same as organization-level setting** check boxes and set the values that you want to use for this site.
7. If you want to change the default sharing link type or permissions for this site, clear the **Same as organization-level setting** check boxes and set the values that you want to use for this site. For more info, see [Change the default sharing link for a site](change-default-sharing-link).

    ![Changing the default sharing link settings](sharepointonline/media/default-sharing-link-settings.png)
8. Select **Save**.

## Which sharing option should I select?

| Select this option: | If you want to: |
| --- | --- |
| Anyone | Allow site owners and others with full control permission to share the site with people who authenticate. Allow site users to decide when sharing files and folders to require authentication or allow unauthenticated people to access the item. Anyone links to files and folders can be freely forwarded. |
| New and existing guests | Allow site owners and others with full control permission to share the site with people outside the organization. These people need to sign in and are added to the directory. Allow site users to share files and folders with people who aren't in the organization's directory. |
| Existing guests | Allow sharing with only people already in your directory. These users exist in your directory because they previously accepted sharing invitations or because they were [manually added](/en-us/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal). (These users have **#EXT#** in their user principal name.) |
| Only people in your organization | Prevent all site users from sharing any site content externally. |

The available settings depend on your organization-level setting. If you enable external sharing for a site and later turn it off for your organization, external sharing becomes unavailable at the site level and any shared links stop working. If you turn it back on for the organization, the site sharing setting returns to what it was before and the shared links resume working.

Note

You might have site content shared with a Microsoft 365 group that has guest members, and the group settings prevent guest members from accessing group resources. In this case, even if you turn on external sharing for the site, guests of the group might not be able to access site content. To enable or disable Microsoft 365 Group guest member access, see [Manage guest access in Microsoft 365 Groups](/en-us/microsoft-365/admin/create-groups/manage-guest-access-in-groups).

## What are the default site sharing settings?

The following table shows the default sharing setting for each site type.

| Site type | Default sharing setting |
| --- | --- |
| Classic | **Only people in your organization** |
| OneDrive | **Anyone** |
| Group-connected sites (including Teams) | **New and existing guests** if the Microsoft 365 Groups setting **Let group owners add people outside the organization to groups** is **On**; otherwise **Existing guests only** |
| Communication | **Only people in your organization** |
| Modern sites with no group (#STS3 TeamSite) | **Only people in your organization** |

Note

The root communication site (tenant-name.sharepoint.com) has a default sharing setting of **Anyone**.