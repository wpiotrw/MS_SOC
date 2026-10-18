---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Agent management roles and permissions in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-roles-perms?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Understand agent management roles and permissions within Microsoft 365 admin center.
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2026-05-08T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-copilot
ms.subservice: agent-management
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- m365copilot
- magic-ai-copilot
- operations-pod
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
search.appverid:
- BCS160
- MET150
- MOE150
locale: en-us
document_id: 33a4c498-20a6-8897-8284-7cb00c9b4462
document_version_independent_id: 33a4c498-20a6-8897-8284-7cb00c9b4462
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/agent-roles-perms.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/agent-roles-perms
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/agent-roles-perms.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 8cd4d357-eeba-c8ba-7888-c007d628a7d8
---

# Agent management roles and permissions in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

Access to agent management in Microsoft 365 admin center is controlled by [Microsoft Entra admin roles](/en-us/entra/identity/role-based-access-control/permissions-reference).

While several administrative and security roles can view agent-related information for monitoring and reporting purposes, only select roles are authorized to perform governance actions such as approving agent requests or assigning ownership.

The following table provides agent management capabilities in the Microsoft 365 admin center:

| Role | View insights and organization data | View agent registry information | Install, modify, approve, and manage agent configurations |
| --- | --- | --- | --- |
| Global Administrator | ✔ | ✔ | ✔ |
| AI Administrator | ✔ | ✔ | ✔ |
| Global Reader | ✔ | ✔ | ✖\* |
| AI Reader | ✔ | ✔ | ✖\* |
| Security Administrator | ✔ | ✔ | ✖ |
| Security Reader | ✔ | ✔ | ✖ |
| Reports Reader | ✔ | ✔ | ✖ |
| User Experience Success Manager | ✔ | ✔ | ✖ |
| User Account Administrator | ✔ | ✖ | ✖ |

\* *Read Only – Tools and settings*

The **AI Administrator** and **Global Administrator** roles have tenant-wide visibility and governance authority, where-as by contrast, product-specific admin roles allow governance only within the boundaries of their products (such as Power Platform Administrator and Fabric Administrator).

Important

Use and assign roles with the fewest permissions to accomplish tasks. Accounts with lower permission roles help improve security for your organization. Global Administrator is a highly privileged role. Limit its use to emergency scenarios when you can't use an existing role. For more information, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

For more information about roles and permissions related to agents, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).