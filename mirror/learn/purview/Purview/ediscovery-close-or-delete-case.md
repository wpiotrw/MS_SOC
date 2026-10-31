---
layout: Conceptual
title: Close or delete an eDiscovery (Premium) case | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-close-or-delete-case
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn what happens when an investigation or legal case supported by a Microsoft Purview eDiscovery (Premium) case is closed or deleted.
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
document_id: c1e0276a-c2b7-7777-54be-9d0dbf97b867
document_version_independent_id: c1e0276a-c2b7-7777-54be-9d0dbf97b867
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-close-or-delete-case.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-close-or-delete-case
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-close-or-delete-case.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: a5284fd9-91d0-66d2-31d6-ea99666d2c93
---

# Close or delete an eDiscovery (Premium) case | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When the legal case or investigation supported by a Microsoft Purview eDiscovery (Premium) case is completed, you can close or delete a case. You can also reopen a closed case.

## Close a case

Here's what happens when you close an eDiscovery (Premium) case:

- If the case contains any content locations on hold, these holds are turned off. After the hold is turned off, a 30-day grace period (called a *delay hold*) is applied to content locations that were on hold. This helps prevent content from being immediately deleted and gives admins an opportunity to search for or recover content that will be permanently deleted after the delay hold period expires. For more information, see [Removing content locations from an eDiscovery hold](ediscovery-create-holds#removing-content-locations-from-an-ediscovery-hold).
- Closing a case only turns off the holds that are associated with that case. If other holds are place on a content location (such as a Litigation Hold, Microsoft Purview eDiscovery (Standard) hold, or a hold from a different eDiscovery (Premium) case) those holds will still be maintained.
- The case is still listed on the eDiscovery page in the Microsoft Purview portal. The details, holds, searches, and members of a closed case are retained.
- You can edit a case after it's closed. For example, you can add or removing members, create searches, export search results, and prepare search results for analysis in eDiscovery (Premium). The primary difference between active and closed cases is that holds are turned off when a case is closed.

Important

If a case has more than 100 hold policies, you must manually remove the policies using PowerShell. For more information, see [Remove-CaseHoldPolicy](/en-us/powershell/module/exchange/remove-caseholdpolicy).

To close a case:

1. On the **eDiscovery (Premium)** page, select the case that you want to close.
2. On the **Settings** tab, under **Case Information**, choose **Select**.
3. At the bottom of the **Case Information** flyout page, select **Actions**, and then select **Close case**. It may take up to 60 minutes for the closing process to complete.

When closing a case, you'll see the status of the case changing as the case is processed for closing. The following table describes the case status messages that you'll see when closing a case:

| **Status** | **Description** |
| --- | --- |
| Active | The case is active. |
| Closed | The case is closed without errors and the case can be reopened. |
| Closed with Errors | The case is closed, but there are errors. Errors are most likely associated with holds that were not released during closing. To resolve, check policies with errors, resolve the errors, and redistribute the policies. |
| Closing | The case is being closed. This status is usually seen only for case with active holds. Cases without holds are immediately closed. |
| Pending delete | The case likely has a hold in the pending deletion state. Check the hold policy and redistribute to resolve the error. Afterwards, cases without any holds should be deleted successfully. |

## Reopen a closed case

When you reopen an eDiscovery (Premium) case, any holds that were in place when the case was closed won't be automatically reinstated. After the case is reopened, you'll have to go to the **Holds** tab and turn on the previous holds. To turn on a hold, select it to display the flyout page, and then set the **Status** toggle to **On**.

To reopen a closed case:

1. On the **eDiscovery (Premium)** page, select the case that you want to reopen.
2. On the **Settings** tab, under **Case Information**, select **Select**.
3. At the bottom of the **Case Information** flyout page, select **Actions**, and then select **Reopen case**.

It might take up to 60 minutes for the reopening process to complete.

## Delete a case

You can delete both active and closed eDiscovery (Premium) cases. When you delete a case, all components associated with the case, such as the list of custodians, communications, searches, review sets, and export job are deleted. The case is removed from the list of cases on the **eDiscovery (Premium)** page in the Microsoft Purview portal. You can't recover or reopen a deleted case.

Note

In data spillage scenarios, the only way to remove items in a review set is to delete the eDiscovery (Premium) case. Other "search and purge" methods don't remove items from a review set.

Before you can delete a case, you must first delete *all* holds listed on the holds page of the case. That includes deleting holds with a status of **Off**. Default hold policies can only be deleted when the hold is turned off. You must close an active case to turn off any default hold policies in the case. Once the holds are turned off for default hold policies, they can be deleted.

To delete holds associated with a case:

1. Go the **Holds** tab in the eDiscovery (Premium) case that you want to delete.
2. Select the hold that you want to delete.
3. On the flyout page, select **Delete**. Ensure that the hold is turned off.

To delete a case:

1. On the **eDiscovery (Premium)** page, select the case that you want to delete.
2. On the **Settings** tab, under **Case Information**, choose **Select**.
3. At the bottom of the **Case Information** flyout page, select **Actions**, and then select **Delete case**.