---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Before you start on Copilot Managed Runtime governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/before-start?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn which admin roles can manage Copilot Managed Runtime, how to apply least privilege, who should own each governance decision, and which admin center to use for each task.
ms.topic: concept-article
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: yapatel
author: yashpatel22
manager: mihaelab
ms.service: microsoft-copilot
ai-usage: ai-generated
locale: en-us
document_id: 57ee5d97-41b4-06d3-8993-a6b135f9aa8f
document_version_independent_id: 57ee5d97-41b4-06d3-8993-a6b135f9aa8f
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/before-start.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-managed-runtime/guidance/admin-playbook/before-start
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/copilot-managed-runtime/guidance/admin-playbook/before-start.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/e6f942e8-55a7-4c86-b8e3-7456508ea850
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/f1834696-48d6-470d-966b-6ee418881596
platformId: a5f44093-e276-7a19-64f7-5a0b93f97041
---

# Before you start on Copilot Managed Runtime governance | Microsoft Learn

Copilot Managed Runtime uses your existing Microsoft 365 and Power Platform admin roles. Before you change any settings, confirm who holds which role, agree who owns each governance decision, and know which admin center to use for each task. This article is for Microsoft 365 admins who are new to Power Platform.

## Admin roles and access

Governance roles for Copilot Managed Runtime have one of two kinds of access:

- **Manage**: View apps and change settings, including governance and security policies, alerts, and how apps are shared.
- **Read only**: View apps, their components, and their health, but not change anything.

Cost management uses a [separate set of roles](../../../admin/manage/apps/roles-responsibilities#roles-for-licensing-and-copilot-credits), listed in the same table. The following table shows each role and where it applies.

| Role | Access | Where it applies | Notes |
| --- | --- | --- | --- |
| Power Platform Administrator | Manage | Microsoft 365 admin center (**Apps** only) and Power Platform admin center | Full view, block, and delete. Microsoft 365 admin staff should request this role be added to their profile so they can govern Copilot Managed Runtime effectively. |
| Global Administrator | Manage | Microsoft 365 admin center and Power Platform admin center | Same management access as Power Platform Administrator. If you already use this role to run Microsoft 365, you don't need another role. |
| Billing Administrator | Cost | Microsoft 365 admin center | Turns on usage-based billing and creates spending policies. Global Administrator can also do this. |
| AI Administrator | Read only | Microsoft 365 admin center | Read-only access to Copilot Managed Runtime apps and settings. Can edit existing spending policies but can't create new ones. |
| AI Reader, Global Reader | Read only | Microsoft 365 admin center | View apps, components, health, and consumption. |

For the current list of roles, see [Roles and responsibilities](../../../admin/manage/apps/roles-responsibilities).

## Recommended least-privilege approach

Follow least privilege: start people with read-only access, and grant Manage access only when their job requires it.

- Give Power Platform Administrator or Global Administrator to the small group of people who configure and govern apps.
- Give AI Reader or Global Reader to compliance reviewers and others who need visibility only.

Tip

Ensure at least one person holds the Power Platform Administrator or Global Administrator role. Those roles are the Manage roles for Copilot Managed Runtime.

## Who owns what

Agree on who owns each governance decision before you change settings. The following *RACI* table is a suggested starting point. In smaller organizations, one person or team often covers several columns.

The letters mean: R = Responsible (does the work), A = Accountable (makes the final decision), C = Consulted, I = Informed.

| Activity | Power Platform Administrator | Billing Administrator | AI Administrator | Security Administrator | AI Reader / Global Reader |
| --- | --- | --- | --- | --- | --- |
| Decide who can build | A/R | R | C | C | I |
| Routing and environment groups | A/R | I | I | C | I |
| Connector and content security exceptions | R | I | I | A | I |
| Sharing and guest policy | A/R | I | I | C | I |
| Audit review | C | I | I | A/R | I |
| Spending policy and credits | I | A/R | R | I | I |
| Inventory and Monitor | A/R | I | I | C | I |
| Code and release boundary | A/R | I | I | R | I |

Note

Global Administrator can do everything in this table, so treat it as a fallback and assign the narrowest role that does the job.

## Where to manage Copilot Managed Runtime

You manage Copilot Managed Runtime from two admin centers. Most tasks start in the Microsoft 365 admin center. The Power Platform admin center shows the same apps and environment groups alongside your other Power Platform resources, and it has a few controls that aren't yet available in the Microsoft 365 admin center.

Changes to environment groups appear in both admin centers. For example, the **Environment groups** page in the Microsoft 365 admin center shows the same information as the **Environment routing** panel in the Power Platform admin center.

| Task | Microsoft 365 admin center | Power Platform admin center |
| --- | --- | --- |
| [View all Copilot Managed Runtime apps](../../../admin/manage/apps/inventory) | **Apps** &gt; **All apps** | **Manage** &gt; **Inventory**. Filter **Item type** to Copilot Managed Runtime. The app's environment details are available only here. |
| [Review or edit the default environment group and its rules](../../../admin/manage/apps/governance) (routing, connectors and MCP servers, sharing, content security policy) | **Apps** &gt; **Settings** &gt; **Environment groups** | **Manage** &gt; **Environment groups** &gt; **Rules** |
| [Runtime spending policies and credits](../../../admin/manage/apps/licensing-credits) | **Copilot** &gt; **Cost management** | Not available |
| Allow [CLI creation](../../../admin/manage/apps/governance#control-whether-apps-can-be-created-using-the-cli) or [external artifact deployment](../../../admin/manage/apps/governance#configure-external-artifact-deployment) | Not available | **Copilot** &gt; **Settings** &gt; **Managed apps**, or an environment group rule |
| [Advanced connector policy details and configuration](/en-us/power-platform/admin/advanced-connector-policies#environment-group-configuration) | Partly visible | Fully available under **Manage** &gt; **Environment groups** |