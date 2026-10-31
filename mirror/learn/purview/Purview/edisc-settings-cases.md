---
layout: Conceptual
title: Learn about case settings in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-settings-cases
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about case settings in eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-02T00:00:00.0000000Z
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
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 70db5a9e-9c71-61c0-f55e-3f05bfc56996
document_version_independent_id: 70db5a9e-9c71-61c0-f55e-3f05bfc56996
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-settings-cases.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-settings-cases
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-settings-cases.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: cb467477-793f-316b-39a1-96f2bd7e6e7d
---

# Learn about case settings in eDiscovery | Microsoft Learn

Case settings in eDiscovery let you [view and update case information](edisc-cases-manage) and take action on specific cases in eDiscovery.

The following information displays for the selected case:

- **Premium features**: Shows the status of [premium eDiscovery features](edisc#features-and-capabilities) enabled in the case. To use premium eDiscovery features for the selected case, turn on the **eDiscovery (Premium)** toggle.

Note

Premium features are enabled by default for tenants with premium feature access. To turn off, toggle the setting after a case is created.

- **License**: Shows the current licensing subscription for the case. Values are *eDiscovery (Premium)* or *eDiscovery (Standard)*.
- **ID**: Shows the case identification number. You can review this number, but you can't change it after the case is created.
- **Case name**: Shows the case name. This field is required. To change the case name, enter the new case name and select **Actions** &gt; **Save**.
- **Case number**: Shows an optional docket number or other numeric identifier for the case. To change the case number, enter the new case number and select **Actions** &gt; **Save**.
- **Case description**: Shows an optional description to help others understand this case. To change the case description, enter the new case description and select **Actions** &gt; **Save**.
- **Case status**: Shows the current case status.
- **Case created**: Shows the date and time when the case was created.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Close a case

When you complete the legal case or investigation supported by eDiscovery, you can close the case. Here's what happens when you close an eDiscovery case:

Note

You need to either disable or delete all active [hold policies](edisc-hold-manage) in the case before you can close the case.

- Delete any active hold policies. After you delete the hold, a 30-day grace period (called a *delay hold*) is applied to content locations that were on hold. This delay hold helps prevent content from being immediately deleted and gives you an opportunity to search for or recover content that is permanently deleted after the delay hold period expires.
- The case is still listed on the **Cases** page in the Microsoft Purview portal. The details, holds, searches, and members of a closed case are retained.
- You can edit a closed case. For example, you can add or remove members, create searches, export search results, and prepare search results for analysis in eDiscovery.

To close a case, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in using the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card and then select **Cases**.
3. Select a case, then navigate to the *Hold policies* tab.
4. Delete all hold policies in the case.
5. After the hold policies are deleted, select **Case settings**.
6. On **Case settings**, select **Actions**, then select **Close case**. It might take up to 60 minutes for the closing process to complete.

When you close a case, you see the status of the case changing as the case is processed for closing.

## Reopen a closed case

When you reopen an eDiscovery case, the process doesn't automatically reinstate any holds that were in place when the case was closed. After you reopen the case, go to the **Holds** tab and turn on the previous holds. To turn on a hold, select it to display the flyout page, then set the **Status** toggle to **On**.

To reopen a closed case, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in using the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select **Case settings**.
4. On **Case settings**, select **Actions**, then select **Reopen case**. It might take up to 60 minutes for the reopening process to complete.

## Delete a case

You can delete both active and closed eDiscovery cases. When you delete a case, you also delete all components associated with the case, such as the list of communications, searches, review sets, and exports. You can't recover or reopen a deleted case.

Note

In data spillage scenarios, the only way to remove items in a review set is to delete the eDiscovery case. Other search and purge methods don't remove items from a review set.

Before you can delete a case, you must delete *all* hold policies listed on the **Hold policies** tab of the case. This requirement includes deleting holds with a status of **Off**.

To delete hold policies associated with a case, complete the following steps:

1. Go the **Hold policies** tab in the eDiscovery case that you want to delete.
2. Select the hold policy that you want to delete.
3. On the hold policy page, select **Policy actions** &gt; **Delete policy**.

To delete a case, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in using the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select **Case settings**.
4. On the **Case settings** page, select **Actions**, then select **Delete case**.