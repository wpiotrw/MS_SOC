---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage people data and related experinces from the microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/people-settings-in-microsoft-365-admin-center?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: The People settings section in the Microsoft 365 admin center is a unified single location for IT admins to manage all people-related settings in their organization.
author: Sameergupta-2019
ms.author: samegupt
ms.service: microsoft-365-admin
ms.topic: overview
ms.date: 2025-10-10T00:00:00.0000000Z
manager: scotv
ms.custom: user-accounts
locale: en-us
document_id: b8e65ec6-0ff4-cd27-87c9-32bf286ebe9a
document_version_independent_id: b8e65ec6-0ff4-cd27-87c9-32bf286ebe9a
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/people-settings-in-microsoft-365-admin-center.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/people-settings-in-microsoft-365-admin-center
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/people-settings-in-microsoft-365-admin-center.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 930fc5d1-1c20-ced5-7613-a485f89ba08f
---

# Manage people data and related experinces from the microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

The *People settings* section in the Microsoft 365 admin center is a unified single location for IT admins to manage all people data and experiences related settings in their organization.

> 
> **How to access the People settings section**

1. **Sign in to the Microsoft 365 admin center** with an account that has the necessary admin role.
2. In the left navigation pane, go to **Settings** and select **Org settings**.
3. On the Org settings page, find the **Services** tab (the list of service-specific settings).
4. Select **People settings** from the list of services.

**Note:** To view or modify People settings, you must be a **Global Administrator** or have the **People Administrator** role in Microsoft 365 ([About admin roles in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn](/en-us/microsoft-365/admin/add-users/about-admin-roles)). The People Administrator role is a specialized admin role that allows managing people-centric features (like updating profile card settings, pronouns, and name pronunciations) without granting full global admin permissions. Global Readers can view these settings (read-only).

Important

Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. To learn more, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

**To assign the People Administrator role to a user:**

1. In the Microsoft 365 admin center, go to **Roles &gt; Role assignments**.
2. Search for **People Administrator** in the list of roles, and select it.
3. In the role details pane, choose **Assigned admins**, then **Add** and select the user(s) you want to assign.
4. Save your changes.

Once the role is assigned, that user can navigate to **Settings &gt; Org settings &gt; People settings** and have full access to configure those settings (just like a Global Admin would).

The People settings section includes the settings for

- [Profile card enrichment and customization](/en-us/microsoft-365/admin/manage/customize-profile-cards)
- [Turn pronouns on or off for your organization](/en-us/microsoft-365/admin/add-users/turn-pronouns-on-or-off)
- [User name pronunciation in Teams](/en-us/microsoftteams/name-pronunciation)