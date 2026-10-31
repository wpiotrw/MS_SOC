---
layout: Conceptual
title: Close, reopen, or delete eDiscovery (Standard) cases | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-close-reopen-delete-cases
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to manage eDiscovery (Standard) cases. This includes closing a case, reopening a closed case, deleting a case, and upgrading a case to eDiscovery (Premium).
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
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
ms.custom: sfi-image-nochange
locale: en-us
document_id: 4a7be4a5-15b0-e106-ad33-5c8fdbcc3947
document_version_independent_id: 4a7be4a5-15b0-e106-ad33-5c8fdbcc3947
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-close-reopen-delete-cases.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-close-reopen-delete-cases
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-close-reopen-delete-cases.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 4564e1c3-3cd0-1325-056c-345100bef93a
---

# Close, reopen, or delete eDiscovery (Standard) cases | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

This article describes how to close, reopen, delete, or upgrade a Microsoft Purview eDiscovery (Standard) cases in Microsoft Purview.

## Close a case

When the legal case or investigation supported by an eDiscovery (Standard) case is completed, you can close the case. Here's what happens when you close a case:

- If the case contains any eDiscovery holds, they'll be turned off. After the hold is turned off, a 30-day grace period (called a *delay hold*) is applied to content locations that were on hold. This helps prevent content from being immediately deleted and provides admins the opportunity to search for and restore content before it may be permanently deleted after the delay hold period expires. For more information, see [Removing content locations from an eDiscovery hold](ediscovery-create-holds#removing-content-locations-from-an-ediscovery-hold).
- Closing a case only turns off the holds that are associated with that case. If other holds are placed on a content location (such as a Litigation Hold, a retention policy, or a hold from a different eDiscovery (Standard) case) those holds will still be maintained.
- The case is still listed on the eDiscovery (Standard) page in the Microsoft Purview portal. The details, holds, searches, and members of a closed case are retained.
- You can edit a case after it's closed. For example, you can add or remove members, create searches, and export search results. The primary difference between active and closed cases is that eDiscovery holds are turned off when a case is closed.

To close a case:

1. In the Microsoft Purview portal, select **eDiscovery** &gt; **eDiscovery (Standard)** to display the list of eDiscovery (Standard) cases in your organization.
2. Select the name of the case that you want to close.

    ![Close case on case home page.](media/ediscoverycasehomepage.png)
3. On the home page, under **Status**, select **Close case**.

    A warning is displayed saying that the holds associated with the case will be turned off.
4. Select **Yes** to close the case.

    The status on the case home page is changed from **Active** to **Closing**.
5. On the **eDiscovery (Standard)** page, select **Refresh** to update the status of the closed case. It might take up to 60 minutes for the closing process to complete.

    When the process is complete, the status of the case is changed to **Closed** on the **eDiscovery (Standard)** page.

## Reopen a closed case

When you reopen a case, any eDiscovery holds that were in place when the case was closed won't be automatically reinstated. After the case is reopened, you'll have to go to the **Holds** page and turn on the previous holds. To turn on a hold, select it to display the flyout page, and then set the **Status** toggle to **On**.

1. In the Microsoft Purview portal, select **eDiscovery (Standard)** to display the list of eDiscovery (Standard) cases in your organization.
2. Select the name of the case that you want to reopen.

    ![Reopen a closed case.](media/ediscoverycasehomepagereopen.png)
3. On the home page, under **Status**, select **Reopen case**.

    A warning is displayed saying that the holds that were associated with the case when it was closed won't be turned on automatically.
4. Select **Yes** to reopen the case.

    The status on the case home page flyout page is changed from **Closed** to **Active**.
5. On the **eDiscovery (Standard)** page, select **Refresh** to update the status of the reopened case. It might take up to 60 minutes for the reopening process to complete.

    When the process is complete, the status of the case is changed to **Active** on the **eDiscovery (Standard)** page.
6. (Optional) To turn on any holds associated with the reopened case, go to **Holds** tab, select a hold, and then select the checkbox under **Status** on the hold flyout page.

## Delete a case

You can also delete active and closed eDiscovery (Standard) cases. When you delete a case, all searches and exports in the case are deleted, and the case is removed from the list of cases on the **eDiscovery (Standard)** page in the Microsoft Purview portal. You can't reopen a deleted case.

Before you can delete a case (whether it's active or closed), you must first delete *all* eDiscovery holds associated with the case. That includes deleting holds with a status of **Off**.

To delete an eDiscovery hold:

1. Go to the **Holds** tab in the case that you want to delete.
2. Select the hold that you want to delete.
3. On the flyout page, select **Delete**.

    ![Delete an eDiscovery hold.](media/deleteediscoveryhold.png)

To delete a case:

1. In the Microsoft Purview portal, select **eDiscovery** &gt; **eDiscovery (Standard)** to display the list of eDiscovery (Standard) cases in your organization.
2. Select the name of the case that you want to delete.
3. On the case home page, under **Status**, select **Delete case**.

    ![Delete a case.](media/ediscoverycasehomepagedelete.png)

If the case you're trying to delete still contains eDiscovery holds, you'll receive an error message. You'll have to delete all holds associated with the case and then try again to delete the case.