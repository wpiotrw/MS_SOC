---
layout: Conceptual
title: Agent management roles and permissions in Microsoft 365 admin center | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-roles-perms
breadcrumb_path: ../breadcrumb/agent365/toc.json
uhfHeaderId: MSDocsHeader-Agent365
feedback_system: Standard
permissioned-type: public
ms.service: agent-365
hideScope: false
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
ms.subservice: admin
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
search.appverid:
- BCS160
- MET150
- MOE150
locale: en-us
document_id: 92e94f79-2ee8-28b7-51ff-c7e4bc918fe8
document_version_independent_id: 92e94f79-2ee8-28b7-51ff-c7e4bc918fe8
original_content_git_url: https://github.com/MicrosoftDocs/agent365-docs-pr/blob/live/agent365-docs/admin/agent-roles-perms.md
site_name: Docs
depot_name: Learn.agent365
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/agent-roles-perms
moniker_range_name: 
monikers: []
item_type: Content
source_path: agent365-docs/admin/agent-roles-perms.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 67d8a84a-56e8-e5dd-ac30-d717db5874e3
---

# Agent management roles and permissions in Microsoft 365 admin center | Microsoft Learn

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