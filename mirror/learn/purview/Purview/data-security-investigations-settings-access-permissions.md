---
layout: Conceptual
title: Configure investigation access and permission settings in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-settings-access-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Configure investigation access and permissions in Data Security Investigations. Learn how to manage users, role groups, and guest access for secure investigations.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-01T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 37f38064-5776-d1f4-5c37-1a4a8336bc39
document_version_independent_id: 37f38064-5776-d1f4-5c37-1a4a8336bc39
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-settings-access-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-settings-access-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-settings-access-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 933dec51-771c-2763-0b2b-866a78383fa0
---

# Configure investigation access and permission settings in Data Security Investigations | Microsoft Learn

Access and permission settings in Data Security Investigations allow you to add or remove users to an investigation, manage role group membership for an investigation, and add people outside your organization as guest users for an investigation.

## Add or remove users from an investigation

You can add or remove users to manage who can access the investigation. However, before a user can access an investigation (and perform tasks in the investigation), you must add the user to the *Data Security Investigations Manager* role group in the Microsoft Purview portal. For more information, see [Assign Data Security Investigations permissions](data-security-investigations-permissions).

### Add users to an investigation

Complete the following steps to add users to an investigation:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in using the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select **Investigation settings**.
4. On the **Investigation settings** page, select **Permissions**.
5. Under **Users**, select **Add** to add users to the investigation. You can also choose to add a role group to the investigation by selecting **Add** under **Role groups**.
6. In the list of users or role groups that can be added to the investigation, select the check box next to the names of the users or role groups that you want to add.

    Note

    When adding a role group to an investigation, you can only add the role groups that you're a member of.
7. After selecting the people or role groups to add as members of the investigation, select **Add**. The selected users are added to the investigation.

    Important

    If a role is added or removed from a role group that you added as a member of an investigation, then the role group is automatically removed as a member of the investigation (or any investigation the role group is a member of). The reason for this process is to protect your organization from inadvertently providing additional permissions to members of an investigation. If a role group is deleted, it's removed from all investigations it's a member of. For more information, see [Assign Data Security Investigations permissions](data-security-investigations-permissions).

### Remove users from an investigation

Only a [Data Security Investigations Administrator](data-security-investigations-permissions) can remove users from an investigation. Even if you're assigned to the *Data Security Investigations Manager* role group or initially created the investigation, you aren't able to remove yourself or other members from an investigation unless you're also a Data Security Investigations Administrator. To remove yourself or other members from an investigation, contact a Data Security Investigations Administrator in your organization.

Complete the following steps to remove users from an investigation:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in using the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select **Investigation settings**.
4. On the **Investigation settings** page, select **Permissions**.
5. Under **Users**, select **Remove** to remove users from the investigation. You can also remove users from a role group for the investigation by selecting **Remove** under **Role groups**.
6. In the list of users or role groups that can be removed from the investigation, select the check box next to the names of the users or role groups that you want to remove.
7. After selecting the people or role groups to add as members of the investigation, select **Remove**. The selected users are removed from the investigation.