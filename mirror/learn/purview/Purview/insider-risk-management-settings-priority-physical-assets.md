---
layout: Conceptual
title: Identify priority physical assets for Insider Risk Management policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-priority-physical-assets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the Priority physical assets settings for Microsoft Purview Insider Risk Management.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 4a698b7f-a9f7-6eef-aa9e-b9301c2142a4
document_version_independent_id: 4a698b7f-a9f7-6eef-aa9e-b9301c2142a4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-priority-physical-assets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-priority-physical-assets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-priority-physical-assets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: b73fc880-3d1c-eba6-76ff-e66fd6c0d606
---

# Identify priority physical assets for Insider Risk Management policies | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Identifying access to priority physical assets and correlating access activity to user events is an important component of your Microsoft Purview Insider Risk Management compliance infrastructure. These physical assets represent priority locations in your organization, such as company buildings, data centers, or server rooms. Insider risk activities might be associated with users working unusual hours, attempting to access unauthorized sensitive or secure areas, and requests for access to high-level areas without legitimate needs.

When you enable priority physical assets and configure the [Physical badging data connector](import-physical-badging-data), Insider Risk Management integrates signals from your physical control and access systems with other user risk activities. By examining patterns of behavior across physical access systems and correlating these activities with other insider risk events, Insider Risk Management helps compliance investigators and analysts make more informed response decisions for alerts.

Insider Risk Management scores and identifies access to priority physical assets in insights differently from access to non-priority assets. For example, your organization has a badging system for users that governs and approves physical access to normal working and sensitive project areas. You have several users working on a sensitive project and these users return to other areas of your organization when the project is completed. As the sensitive project nears completion, you want to make sure that the project work remains confidential and that access to the project areas is tightly controlled.

You enable the Physical badging data connector in Microsoft 365 to import access information from your physical badging system and specify priority physical assets in Insider Risk Management. By importing information from your badging system and correlating physical access information with other risk activities identified in Insider Risk Management, you notice that one of the users on the project is accessing the project offices after normal working hours and is also exporting large amounts of data to a personal cloud storage service from their normal work area. This physical access activity associated with the online activity might point to possible data theft and compliance investigators and analysts can take appropriate actions as dictated by the circumstances for this user.

![Screenshot of the Priority physical assets settings page in Insider Risk Management showing the configuration options for adding and managing physical asset IDs.](media/insider-risk-settings-priority-assets.png)

## Configure priority physical assets

To configure priority physical assets, configure the Physical badging connector and use setting controls in the Insider Risk Management solution. To configure priority physical assets, you must be a member of the *Insider Risk Management* or *Insider Risk Management Admin* role group.

Important

For Insider Risk Management policies to use and correlate signal data related to departing and terminated users with event data from your physical control and access platforms, also configure the Microsoft 365 HR connector. If you enable the Physical badging connector without enabling the Microsoft 365 HR connector, Insider Risk Management policies only process events for physical access activities for users in your organization.

1. Follow the configuration steps for Insider Risk Management in the [Getting started with Insider Risk Management](insider-risk-management-configure) article. In Step 3, make sure to configure the Physical badging connector.
2. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) using credentials for an admin account in your Microsoft 365 organization, select **Settings** in the upper-right corner of the page, and select **Insider Risk Management** to open the Insider Risk Management settings. Select **Priority physical assets**.
3. On the **Priority physical assets** page, you can either manually add the physical asset IDs imported by the Physical badging connector or import a CSV file of all physical asset IDs imported by the Physical badging connector:

    1. To manually add physical asset IDs, choose **Add priority physical assets**, enter a physical asset ID, and then select **Add**. Enter other physical asset IDs, then select **Add priority physical assets** to save all the assets you entered.
    2. To add a list of physical asset IDs from a CSV file, choose **Import priority physical assets**. In the file explorer dialog box, select the CSV file you want to import, then select **Open**. The physical asset IDs from the CSV files are added to the list.
4. In settings, select **Policy indicators**.
5. On the **Policy indicators** page, go to the **Physical access indicators** section, then select the **Physical access after termination or failed access to sensitive asset** check box.
6. Select **Save**.

## Delete a priority physical asset

To delete a priority physical asset, you must be a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group.

Important

When you delete a priority physical asset, you remove it from examination by any active policy that includes it. However, alerts generated by activities associated with the priority physical asset aren't deleted.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) as a member of the *Insider Risk Management* or *Insider Risk Management Admins* role group.
2. Select **Settings** in the upper-right corner of the page.
3. Select **Insider Risk Management** to go to the Insider Risk Management settings.
4. Select **Priority physical assets**.
5. On the **Priority physical assets** page, select the asset you want to delete.
6. Select **Delete**.