---
layout: Conceptual
title: Manage agents across multiple tenants in the Microsoft 365 admin center | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-multi-tenant
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
description: Manage agents across multiple tenants in the Microsoft 365 admin center.
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2026-07-17T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.localizationpriority: medium
ms.collection:
- Tier2
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
document_id: 70ffde71-7ce1-ae86-671c-08517cc7fa86
document_version_independent_id: 70ffde71-7ce1-ae86-671c-08517cc7fa86
original_content_git_url: https://github.com/MicrosoftDocs/agent365-docs-pr/blob/live/agent365-docs/admin/agent-multi-tenant.md
site_name: Docs
depot_name: Learn.agent365
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/agent-multi-tenant
moniker_range_name: 
monikers: []
item_type: Content
source_path: agent365-docs/admin/agent-multi-tenant.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 9ae58485-0779-6c72-be64-292c3021cc29
---

# Manage agents across multiple tenants in the Microsoft 365 admin center | Microsoft Learn

Important

Multi-tenant agent management is in public preview. Preview features might change before general availability. This article describes only the capabilities available in the public preview.

Multi-tenant agent management is a central control tower that lets partners and enterprise administrators govern agents across the tenants they administer from the Microsoft 365 admin center. With this experience, you can view agent inventory, add agents, install or block agents across multiple tenants, review risk and activity, and use the tenant switcher to move directly into a governed tenant without signing out or maintaining a separate account in that tenant.

Use the multi-tenant experience to reduce repetitive administration, maintain a consistent rollout posture, and prioritize remediation across governed tenants. Actions are applied to each selected governed tenant and are subject to the administrator's delegated role in that tenant.

## Before you begin

Make sure the following requirements are met:

- The governing tenant has an active relationship with at least one governed tenant. Partners establish GDAP relationships in Partner Center. Enterprises establish governance relationships through Microsoft Entra Tenant Governance. Learn more about [What is Microsoft Entra Tenant Governance? (preview)](/en-us/entra/id-governance/tenant-governance/overview).

    Important

    Microsoft Entra Tenant Governance is not same as Multitenant Collaboration (MTO) in Microsoft 365.
- The signed-in administrator has a supported delegated role in each governed tenant. Access and available actions can differ by tenant if role assignments differ.
- Viewing and managing agents across connected tenants requires no additional licenses. Viewing agent risk and activity requires a Microsoft Agent 365 license assigned to the end user.

## Who should use this experience

- Microsoft's Partners that manage customer tenants using Partner Center.
- Enterprises that manage multiple tenants and connected using Microsoft Entra Tenant Governance.

## Terminology

| Term | Meaning |
| --- | --- |
| Governing tenant | The tenant from which administrators centrally view and manage agents in other tenants. |
| Governed tenant | A tenant whose agents can be viewed and managed by authorized administrators in the governing tenant. |
| GDAP | Granular Delegated Admin Privileges. Partners and Enterprises can use GDAP to receive time-bound, role-scoped access to managed tenants. |
| Governance relationship | A CSP relationship established by partners with their customer tenants, or a directional Microsoft Entra Tenant Governance relationship between a governing tenant and a governed tenant. |

## How multi-tenant management differs from single-tenant management

Multi-tenant agent management extends the single-tenant experience by consolidating inventory, navigation, rollout, governance, and response across eligible governed tenants.

| Capability | Single-tenant agent management | Multi-tenant agent management |
| --- | --- | --- |
| Scope | Shows agents and settings for the current tenant. | Shows a consolidated inventory across eligible governed tenants. |
| Tenant navigation | Requires the administrator to already be working in the tenant. | Uses the tenant switcher to move from the governing tenant into an eligible governed tenant in delegated context. |
| Agent rollout | Adds and installs an agent in one tenant. | Adds an agent to the inventory, and then installs it in all eligible governed tenants or a selected set. |
| Governance | Reviews and acts on one tenant's agent instances. | Surfaces tenant-level risk, permissions, and activity from one location. |
| Response | Blocks or changes availability in the current tenant. | Blocks an agent or updates its availability across selected governed tenants. |

## Roles and permissions

Access to view and manage agents depends on the delegated role assigned in each governed tenant.

| Delegated role in the governed tenant | View agent inventory | Add, install, block, or change availability |
| --- | --- | --- |
| AI Administrator | Yes | Yes |
| Global Administrator | Yes | Yes |
| Global Reader | Yes | No |

Important

Use the least-privileged role that completes the task. Global Administrator is a highly privileged role and should be limited to scenarios where a less-privileged role can't be used.

## Tenant switcher

The tenant switcher is a key benefit for partners and enterprise administrators. It lets you move from the governing tenant directly into an eligible governed tenant and continue administration in that tenant's context. You don't need to sign out, use a separate browser session, or maintain a local administrator account in each governed tenant.

1. In the Microsoft 365 admin center command bar, select the tenant switcher next to the current tenant name.

    [![Screenshot that shows Tenant switcher control next to the current tenant name in the Microsoft 365 admin center command bar.](media/agents/agent-multi-tenant-04.png)](media/agents/agent-multi-tenant-04.png#lightbox)
2. Search for or select the governed tenant that you want to administer.
3. The Microsoft 365 admin center opens in the selected governed tenant by using your delegated access.
4. Use the tenant switcher again to return to the governing tenant or move to another governed tenant.

Use the tenant switcher when you need to work in one governed tenant. To return to the consolidated experience, use the tenant switcher to return to the governing tenant, and then select **All tenants**.

[![Screenshot that shows Tenant switcher showing available governed tenants to move into or return to the governing tenant.](media/agents/agent-multi-tenant-01.png)](media/agents/agent-multi-tenant-01.png#lightbox)

## Multi-tenant agent experience

The multi-tenant agent experience opens the consolidated agent inventory from the governing tenant.

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com) with an account in the governing tenant.
2. Select **All tenants** &gt; **Agents**.

The **All tenants** scope is only available when the governing tenant has at least one supported tenant relationship and the signed-in administrator has a supported delegated role.

[![Screenshot that shows consolidated multi-tenant Agents page opened from the All tenants scope in the Microsoft 365 admin center.](media/agents/agent-multi-tenant-05.png)](media/agents/agent-multi-tenant-05.png#lightbox)

## View agents across tenants

The **Agents** page combines agent definitions with per-tenant deployment information. Use the summary cards, search, filters, and columns to identify agents that require attention.

- **Total agents** shows the agents discovered across eligible governed tenants.
- **Risky agents** highlights agents with security information that requires review.
- **Assigned tenants** shows where an agent is available. Select the tenant information to review the tenant instances.

Note

The public preview lets you work with all eligible governed tenants or any selected subset.

## Add an agent

After reviewing the consolidated listing, an authorized administrator can add a custom agent to the agent inventory. Adding the agent makes it available for review and later installation in governed tenants; it does not automatically install the agent in other tenants.

1. On the **Agents** page, select **Add agent**.
2. Complete the steps shown in the **Add agent** pane for the agent that you are adding.
3. Review the agent details and any permissions presented in the workflow.
4. Complete the workflow, and then confirm that the agent appears in the **Agents** listing.

[![Screenshot showing the 'Select tenants' pane.](media/agents/agent-multi-tenant-02.png)](media/agents/agent-multi-tenant-02.png#lightbox)

## Review agent details

Agent status is tenant-specific. A single agent can have different availability, permissions, risk information, and activity in different tenants, so review the selected tenant before you take an action.

1. On the **Agents** page, select an agent.
2. In the details pane, select a governed tenant from the tenant list.
3. Review the available tabs for that tenant instance, such as **Overview**, **Data & tools**, **Security & compliance**, **Permissions**, and **Activity**.

[![Screenshot showing agent details across tenants.](media/agents/agent-multi-tenant-03.png)](media/agents/agent-multi-tenant-03.png#lightbox)

## Take action for a specific tenant in agent details

Use agent details when an action should apply to one governed tenant instead of multiple tenants. Always confirm the selected tenant before applying a change.

1. In the agent details pane, select the governed tenant that you want to manage.
2. Review the tenant-specific availability, permissions, security information, and activity.
3. Depending on the agent status and your delegated role, install or block the agent for the selected tenant, or update the users for whom the agent is available.
4. Review the affected tenant and confirm the action.

## Install an agent in other tenants from the listing

After an agent appears in the consolidated listing, use **Install** to make it available in other eligible governed tenants. You can install it in all eligible tenants or a selected set in one workflow.

1. On the **Agents** page, select the agent, and then select **Install**.
2. Choose **All tenants** or **Specific tenants**. If you choose **Specific tenants**, search for and select the governed tenants.
3. Review the agent configuration and required permissions for the selected tenants.
4. Choose the users or groups that can use the agent in each selected tenant.
5. Review the installation summary, and then select **Install**.

The exact configuration steps shown in the installation pane can vary by agent.

## Block an agent across tenants

When an agent is unsafe, non-compliant, or no longer approved, block it in the governed tenants where it shouldn't run.

1. On the **Agents** page, select one or more agents.
2. Select **Block**.
3. Select the governed tenants where the block should apply.
4. Review the affected agent instances, and then confirm the action.

Blocking is applied separately in each selected governed tenant. Tenants where you have read-only access remain visible, but you can't apply the action in those tenants.

## Review risky agents

Risk information is tenant-specific, so investigate the affected tenant before remediation.

1. Select an agent, and then select an affected governed tenant.
2. For risk investigation, open **Security & compliance** to review the available protection and policy information.
3. Use the available links to continue the investigation in Microsoft Purview, Microsoft Entra, or Microsoft Defender, when shown.
4. Block the agent in the affected tenants or take other remediation actions as appropriate.

Note

Viewing agent risk in **Security** requires a Microsoft Agent 365 license assigned to the end user.

## Review agent activity

Use the **Activity** tab to understand adoption and operational behavior for the selected agent in the selected governed tenant.

1. Select an agent, and then select a governed tenant.
2. Open **Activity**.
3. Choose the date range.
4. Review total sessions, exceptions, active users, and last activity information.
5. Select **Export to CSV** when you need to analyze the displayed activity outside the admin center.

Note

Viewing agent activity requires a Microsoft Agent 365 license assigned to the end user.

## Example scenarios

### Partner deployment across customer tenants

A managed service provider has active GDAP relationships with its customer tenants. An AI Administrator reviews the consolidated listing, adds an approved custom agent when needed, and installs it in the required customer tenants in one workflow. When tenant-specific follow-up is needed, the administrator uses the tenant switcher to move directly into the customer tenant. The partner avoids repeated sign-ins and rollout steps across customer admin centers.

### Enterprise response to a risky agent

A central IT team uses a Microsoft Entra Tenant Governance relationship to oversee subsidiary tenants. The team filters the consolidated inventory for risky agents, opens the affected tenant instances, reviews **Security & compliance**, and blocks the agent in the tenants where remediation is required.

## Public preview scope and considerations

- This article covers the tenant switcher and the multi-tenant Agents experience, including cross-tenant inventory, adding agents, installation, blocking, tenant-level details, risky-agent information, and agent activity.
- Available tenants and actions are determined by the active relationship, delegated role assignment, and licensing in each governed tenant.
- Preview user interface labels and workflow steps might change before general availability.