---
layout: Conceptual
title: Flowchart to determine when an item is retained or deleted | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/retention-flowchart
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2024-06-10T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- purview-compliance
- SPO_Content
search.appverid:
- MOE150
- MET150
description: Use a flowchart to determine the outcome when an item in Microsoft 365 has multiple retention policies or a retention label and retention policies
locale: en-us
document_id: 3d69f5eb-39f2-59f3-fbe8-ec9555965d2e
document_version_independent_id: 3d69f5eb-39f2-59f3-fbe8-ec9555965d2e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/retention-flowchart.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: retention-flowchart
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/retention-flowchart.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 45a4a940-5d96-8584-d1e0-f9e9cc423a41
---

# Flowchart to determine when an item is retained or deleted | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following flowchart to apply the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) to an item to determine if the system will retain it or permanently delete it as a result of a retention label or retention policy.

This logic flow is used for an item when any of the following conditions apply:

- There's more than one retention policy applied
- There's a retention label and one or more retention policies
- The item isn't subject to [priority cleanup](priority-cleanup)

When an item is subject to an eDiscovery hold (or the older technologies of Litigation hold or In-Place Hold), unless it is also subject to priority cleanup, it is always retained before the decision flows for retention policies and a retention label.

If any of the terms used in this flowchart are unfamiliar to you, see [Learn about retention policies and retention labels](retention).

![Flowchart to determine when an item will be retained or permanently deleted.](media/retention-flowchart.svg)

Note

It's important to distinguish between the longest retention period for the item vs. the longest specified period in a retention policy or label. And similarly, between the shortest expiry date for the item vs. the shortest specified period in a retention policy.

For more information, see the explanation after the graphic in the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) section.