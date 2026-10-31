---
layout: Conceptual
title: Add or remove members from an eEdiscovery (Premium) case | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-add-or-remove-members-from-a-case
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to add or remove the members who can access a case when managing an eDiscovery (Premium) case.
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
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-mar2020
locale: en-us
document_id: a38c63ba-cb00-9c60-7669-e79929ec8a7b
document_version_independent_id: a38c63ba-cb00-9c60-7669-e79929ec8a7b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-add-or-remove-members-from-a-case.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-add-or-remove-members-from-a-case
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-add-or-remove-members-from-a-case.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: df3d5a3f-98c8-f04e-bc16-7ed15066d2aa
---

# Add or remove members from an eEdiscovery (Premium) case | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

You can add or remove members to manage who can access the case. However, before a member can access an eDiscovery (Premium) case (and perform tasks in the case), you must add the user to the eDiscovery Manager role group on the **Permissions** page in the Microsoft Purview portal. For more information, see [Assign eDiscovery permissions](ediscovery-assign-permissions).

1. On the **eDiscovery (Premium)** page, go to the case that you want to add a member to.
2. Select the **Settings** tab and then choose **Select** in the **Access & permissions** tile.
3. Under **Manage members**, select **Add** to add members to the case. You can also choose to add a role group to the case by selecting **Add** under **Manage role groups**.
4. In the list of people or role groups that can be added as members of the case, select the check box next to the names of the people or role groups that you want to add.

    Note

    When adding a role group to a case, you can only add the role groups that you are a member of.
5. After you've selected the people or role groups to add as members of the case, select **Add**.
6. In the **Manage this case** flyout page, select **Save** to save the new list of case members.

Important

If a role is added or removed from a role group that you've added as a member of a case, then the role group will be automatically removed as a member of the case (or any case the role group is a member of). The reason for this is to protect your organization from inadvertently providing additional permissions to members of a case. Similarly, if a role group is deleted, it will be removed from all cases it was a member of. For more information, see [Assign eDiscovery permissions](ediscovery-assign-permissions#add-role-groups-as-members-of-ediscovery-cases).

## Removing members from a case

Only an [eDiscovery Administrator](ediscovery-assign-permissions) can remove members from a case. Even if you're assigned to the eDiscovery Manager role group or initially created the case, you won't be able to remove yourself or other members from a case unless you're also an eDiscovery Administrator. To remove yourself or other members from a case, contact an eDiscovery Administrator in your organization.