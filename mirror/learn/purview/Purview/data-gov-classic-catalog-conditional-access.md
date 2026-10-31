---
layout: Conceptual
title: Configure Microsoft Entra Conditional Access for Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-catalog-conditional-access
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-05-23T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to configure Microsoft Entra Conditional Access for Microsoft Purview.
locale: en-us
document_id: 973a7b95-70fa-cad2-1a1f-34d33d25dee9
document_version_independent_id: 973a7b95-70fa-cad2-1a1f-34d33d25dee9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-catalog-conditional-access.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-catalog-conditional-access
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-catalog-conditional-access.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 0f385918-4aae-19b6-29f9-88822fb1df35
---

# Configure Microsoft Entra Conditional Access for Microsoft Purview | Microsoft Learn

Microsoft Purview governance solutions support Microsoft Conditional Access.

The following steps show how to configure Microsoft Purview to enforce a Conditional Access policy.

## Prerequisites

- When multi-factor authentication is enabled, to sign in to the Microsoft Purview governance portal, you must perform multi-factor authentication.

## Configure conditional access

1. Sign in to the Azure portal, select **Microsoft Entra ID**.
2. Browse to **Security** &gt; **Conditional Access**. For more information, see [Microsoft Entra Conditional Access technical reference](/en-us/azure/active-directory/conditional-access/concept-conditional-access-conditions).
3. Select **Create new policy**, provide a name, and then select **Configure rules**.
4. Under **Assignments**, select **Users and groups**, check **Select users and groups**, and then select the user or group for Conditional Access. Select **Select**, and then select **Done** to accept your selection.
5. Select **Cloud apps**, select **Select apps**. You see all apps available for Conditional Access. Select **Azure Purview**, at the bottom select **Select**, and then select **Done**.
6. Select **Access controls**, select **Grant**, and then check the policy you want to apply.
7. Set **Enable policy** to **On** and select **Create**.