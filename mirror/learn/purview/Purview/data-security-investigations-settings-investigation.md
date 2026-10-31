---
layout: Conceptual
title: Investigation settings in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-settings-investigation
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Configure and manage investigation settings in Data Security Investigations. Learn how to update details, delete investigations, and maintain data security.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-02-18T00:00:00.0000000Z
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
document_id: 6d01697e-ea0a-453a-0991-80499de348af
document_version_independent_id: 6d01697e-ea0a-453a-0991-80499de348af
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-settings-investigation.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-settings-investigation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-settings-investigation.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f8ecfb24-e2e0-fb63-cd5c-8367227d1a43
---

# Investigation settings in Data Security Investigations | Microsoft Learn

Investigation details let you view and update investigation information. You can take action on specific investigations.

## Investigation details

The investigation settings display the following information for the selected investigation:

- **ID**: Shows the investigation ID number. You can review this ID but can't change it after the investigation is created.
- **Investigation name**: Shows the investigation name. This field is required. To change the investigation name, enter the new investigation name and select **Actions** &gt; **Save**.
- **Investigation description**: Shows an optional description to help others understand this investigation. To change the investigation description, enter the new investigation description and select **Actions** &gt; **Save**.
- **Investigation status**: Shows the current investigation status.
- **Investigation created**: Shows the date and time when the investigation was created.

## Delete an investigation

Delete investigations when they're no longer needed for your organization. When you delete an investigation, you also delete all components associated with the investigation, such as searches, investigation scopes, and mitigation plans. You can't recover a deleted investigation.

To delete an investigation, complete the following steps:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select **Investigation settings**.
4. On the **Investigation settings** page, select **Actions**, then select **Delete investigations**.