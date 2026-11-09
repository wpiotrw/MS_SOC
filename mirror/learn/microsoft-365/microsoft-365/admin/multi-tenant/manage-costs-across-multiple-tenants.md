---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage costs across multiple tenants in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/multi-tenant/manage-costs-across-multiple-tenants?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Multi-tenant Cost Management lets you track Copilot Credit usage across governed tenants. Learn how to apply spending templates and policies at scale.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.topic: how-to
author: Smritib17
manager: dansimp
ms.author: smbhardwaj
audience: Admin
ms.service: m365-core
ms.subservice: tenant
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_NonTOC
- Adm_TOC
ms.custom:
- AdminSurgePortfolio
- admindeeplinkMAC
- multi-tenant
locale: en-us
document_id: 66ea4a86-1d66-018b-106e-4f12c811fc30
document_version_independent_id: 66ea4a86-1d66-018b-106e-4f12c811fc30
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/multi-tenant/manage-costs-across-multiple-tenants.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/multi-tenant/manage-costs-across-multiple-tenants
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/multi-tenant/manage-costs-across-multiple-tenants.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 5d8f74fb-729a-e77a-efa1-9a3fa069ef20
---

# Manage costs across multiple tenants in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

Multi-tenant Cost Management provides a central control tower for Copilot Credit usage across the tenants that you administer. From the Microsoft 365 admin center, partners and enterprise administrators can review consumption across governed tenants, identify tenants that need policies or controls, analyze the users and services driving usage, and apply reusable spending configurations at scale.

The experience extends the single-tenant Cost Management concepts of spending policies, limits, alerts, billing methods, and consumption reporting into the **All tenants** scope. Actions are evaluated separately for each governed tenant and remain subject to that tenant's delegated roles, billing configuration, Azure subscription access, and applicable commercial relationship.

Use the multi-tenant experience to:

- Understand Copilot Credit consumption across the tenant estate.
- Identify tenants that aren't configured, don't have enforceable controls, or are nearing limits.
- Create reusable spending templates for common governance patterns.
- Create independent spending policies in selected governed tenants.
- Review each tenant's policy scope, limits, funding path, and consumption.
- Analyze usage by tenant, policy, user, group, agent, and service, subject to permissions and privacy requirements.

## Who should use this experience

- Microsoft partners that administer customer tenants through Granular Delegated Admin Privileges (GDAP).
- Enterprises that centrally administer multiple tenants through Microsoft Entra Tenant Governance.
- Administrators who create or maintain Copilot Credit spending policies and billing configurations for governed tenants.

## Multi-tenant Cost Management Vs single-tenant Cost Management

| **Capability** | **Single-tenant Cost Management** | **Multi-tenant Cost Management** |
| --- | --- | --- |
| Scope | Shows policies, requests, and consumption for the current tenant. | Shows consolidated policy posture and consumption across eligible governed tenants. |
| Overview | Summarizes Copilot Credit usage, funding sources, requests, and actions for one tenant. | Aggregates Copilot Credit usage and highlights tenant populations that require action. |
| Tenant management | The tenant is implicit. | Provides a searchable, filterable tenant inventory for large estates. |
| Spending policies | Creates and manages policies directly in the current tenant. | Shows tenant policies across governed tenants and supports direct tenant-specific creation. |
| Reusable configuration | Policies are created for the current tenant. | Spending templates can be defined in the governing tenant and applied to selected governed tenants. |
| Template behavior | Not applicable. | Applying a template creates a new independent policy in each selected tenant. Existing policies don't remain linked to the template. |
| Billing | Uses billing methods and Azure subscriptions available to the current tenant and administrator. | Evaluates billing readiness, subscription access, and commercial authority separately for every selected tenant. |
| Consumption | Analyzes usage by policy, user, group, agent, service, and funding source in one tenant. | Aggregates usage across tenants and supports tenant-filtered drill-downs. |
| Execution | Most actions affect one tenant. | Bulk actions can partially succeed and return a separate outcome for every selected tenant. |

### Terminology

| **Term** | **Meaning** |
| --- | --- |
| Governing tenant | The tenant from which administrators centrally view and manage Cost Management information in other tenants. |
| Governed tenant | A tenant whose Cost Management information can be viewed or managed by an authorized administrator in the governing tenant. |
| Spending policy | A tenant-owned configuration that controls access to supported agents and services, spending limits, alerts, model profiles where applicable, and the billing method. |
| Spending template | A reusable configuration blueprint owned by the governing tenant. A template isn't itself a tenant policy. |
| Apply template | Creates an independent spending policy in each selected governed tenant by copying the template's current settings. |
| Tenant policy | A spending policy owned by one governed tenant. It can be created directly or created from a spending template. |
| Copilot Credits | The usage unit shown in Microsoft 365 Cost Management for eligible AI experiences enabled by usage-based billing. |
| Prepaid credits | Credits available through supported prepaid capacity or pre-purchase mechanisms. |
| Pay-as-you-go | Usage billed to the Azure subscription selected for the spending policy after applicable prepaid credits are used. |
| Policy subscription | The customer-associated Azure subscription used by a spending policy for its billing method. |
| GDAP | Granular Delegated Admin Privileges. Partners use GDAP to receive time-bound, role-scoped access to customer tenants. |
| Governance relationship | A Microsoft Entra Tenant Governance relationship between a governing tenant and a governed tenant. |

## Before you begin

Ensure you meet the following requirements:

- The governing tenant has an active supported relationship with at least one governed tenant.
- The signed-in administrator has an applicable delegated Microsoft Entra role in each governed tenant.
- Each governed tenant has the licenses, services, discovery settings, and billing prerequisites required for the Copilot experiences that it uses.
- Administrators who change a billing method can access an eligible Azure subscription and billing account for the governed tenant.
- Partner administrators understand that GDAP, Azure role-based access control, and the commercial relationship are separate permission planes.
- Privacy and customer-consent requirements are satisfied before user-level identities are displayed across tenants.

Available tenants and actions can differ because relationships, roles, subscriptions, billing ownership, and service eligibility are evaluated per tenant.

## Roles and permissions

The current single-tenant role model is the starting point for multi-tenant authorization. The multi-tenant service must confirm which roles it can delegate and use for every cross-tenant read and write operation.

| **Role or permission** | **Expected capability** |
| --- | --- |
| AI Administrator, AI Reader, Global Reader, and other supported reader roles | View consumption dashboards and reports without changing policies, limits, alerts, request policies, or billing methods. |
| AI Administrator or Billing Administrator | Can edit spending policies and manage limits and alerts. Validate current Microsoft Learn guidance for policy creation and billing-method changes in delegated multi-tenant scenarios. |
| Billing Administrator or Global Administrator | Complete initial setup and add, select, or change billing methods. |
| Global Administrator | Can create a new Azure subscription directly from the Microsoft 365 admin center when the supported billing path is available. |
| Azure subscription or billing-scope permissions | Can enumerate, select, or manage eligible subscriptions and billing scopes. GDAP alone doesn't grant these permissions. |
| Partner Center commercial permissions | Required for CSP orders, partner-billed subscriptions, invoice access, and other commercial transactions. GDAP alone doesn't grant these permissions. |

Important

Use the least-privileged role that completes the task. Global Administrator is a highly privileged role and shouldn't be the normal role for ongoing Cost Management operations.

## Authorization and billing boundaries

The experience evaluates three independent planes for every governed tenant:

1. **Tenant administration** - The active GDAP or governance relationship and delegated Microsoft Entra role determine whether you can view or change the tenant and its Microsoft 365 Cost Management data.
2. **Azure subscription and billing scope** - Azure permissions determine whether you can see, select, create, or configure the Azure subscription used for billing.
3. **Commercial relationship** - CSP and billing relationships determine who can transact, create partner-billed subscriptions, purchase on the customer's behalf, view invoices, and receive incentives.

A user might be able to view consumption or edit a spending policy but still be unable to change its billing method. Similarly, a billing partner might be able to transact for a customer without having delegated access to administer that customer's Microsoft 365 tenant.

The Cost Management experience reports operational usage in **Copilot Credits**. It isn't the authoritative invoice or wholesale-cost view. Use Azure Cost Management, Azure billing, or Partner Center for monetary charges, invoices, and partner reconciliation.

## Multi-tenant Cost Management experience

1. Sign in to the Microsoft 365 admin center with an account in the governing tenant.
2. Select **All tenants** in the scope selector.
3. Go to **Cost management**.
4. Use the available tabs:

- **Overview**
- **Configuration**
- **Consumption**

The **All tenants** scope is expected to be available when the governing tenant has at least one supported tenant relationship and the signed-in administrator has a supported delegated role.

### Review the multi-tenant overview

The **Overview** tab summarizes Copilot Credit usage and helps administrators prioritize the tenants that need action.

Use the financial and usage summary to review:

- Total Copilot Credits used for the selected period.
- Prepaid credits used.
- Pay-as-you-go credits used.
- Active users of Copilot Credits.
- Tenants with the most active users.
- Tenants with the highest credit consumption.
- Consumption by supported agents and services.
- Items that require administrative attention.

### Review policy actions needed

The prototype groups tenants into actionable populations:

- **Not configured** - The tenant has no active spending policy.
- **Configured without controls** - The tenant has at least one active policy, but one or more active policies don't have an enforceable tenant, group, or per-user limit.
- **Nearing controls** - Every active policy has an enforceable limit, and at least one policy is approaching, at, or capped by its limit.

Select a card or action to open the **Tenants** tab with the corresponding filter applied.

An alert threshold, service selection, or billing connection doesn't by itself count as an enforceable spending control.

### View and manage governed tenants

Use the **Tenants** tab as the inventory and management surface for large tenant estates.

The page provides:

- Summary cards for total managed tenants and key policy states.
- Search, sorting, filtering, saved views, and column management.
- Export for offline analysis.
- Multi-select and select-all-matching behavior.
- Entry points for applying a spending template or creating a tenant-specific policy.

Tenant information can include:

- Enablement status.
- Controls and policy scope.
- Active and disabled policy counts.
- Consumption status.
- Copilot Credits used.
- Percentage of configured limit.
- Active users.
- Policy-subscription count.
- Funding coverage.
- Last activity.
- Tags.

Useful views include:

- All tenants.
- Not configured.
- Configured without controls.
- Configured with controls.
- Nearing controls.
- Multiple active policies.
- Has disabled policies.
- Tenant-level policies only.
- Granular policies only.
- Tenant-level plus granular policies.
- No usage in the selected period.
- Active, approaching limit, and capped.

When you select a tenant, you see its details without losing the current page, filters, or scroll position.

### Review a governed tenant

The tenant details experience brings together policy configuration, billing, and consumption so administrators can understand why a tenant is enabled and how its credits are being used.

Review:

- Enablement status and policy-scope summary.
- Active users and Copilot Credits used.
- Active and disabled policies.
- Prepaid and pay-as-you-go consumption.
- Consumption trend.
- Tags and recent Cost Management activity.

For each policy, review:

- Policy name, description, status, and scope.
- Tenant, group, or user targeting.
- Monthly policy limit and optional per-user limit.
- Alert thresholds and recipients.
- Covered agents and services.
- Model profile, when applicable.
- Billing method and customer-associated Azure subscription.
- Prepaid-credit availability and pay-as-you-go behavior.
- Consumption, sessions, active users, and percentage of limit.
- Source template and creation date, when the policy was created from a template.

Enable or disable a policy only from the governed tenant's details. Disabled policies remain visible for history and retain their billing and consumption context, but they don't enable new usage.

### Create a spending template

A spending template is a reusable blueprint owned by the governing tenant. It isn't a policy and isn't linked to governed tenants.

To create a template:

1. On Configuration, select **Spending templates**.
2. Select **Create template**.
3. Enter the template name and description.
4. Configure the tenant monthly limit.
5. Optionally configure a per-user monthly limit.
6. Configure alert thresholds and recipients.
7. Select the agents and services that the template covers.
8. Select the model profile applicable for the template.
9. Choose whether future supported agents and services are automatically included.
10. Review the configuration and select **Create template**.

Creating a template doesn't select tenants, groups, subscriptions, or resource groups. Those values belong to the independent policy that you later create in each governed tenant.

Editing a template affects only policies created from it in the future. Deleting a template doesn't delete or change policies that were previously created from it.

### Apply a spending template

When you apply a template, you create an independent, tenant-owned spending policy for each selected governed tenant.

1. On **Tenants**, select the governed tenants.
2. Select **Apply template**.
3. Select a template and review its policy scope, limits, alerts, covered agents and services, and model profile where applicable.
4. For each governed tenant, choose an appropriate billing method.
5. Review the per-tenant outcomes and start the deployment.

The operation:

- Copies the template settings into a new tenant policy.
- Doesn't create a persistent link between the template and the policy.
- Doesn't synchronize later template changes.
- Can succeed for some tenants and fail or be skipped for others.
- Must return a result for every selected tenant.

The generated policy can record its source template and creation date for audit context. It doesn't use template versions, update states, drift states, or staged template-update rollouts.

### Manage tenant policies

The **Tenant policies** view shows policies across governed tenants, whether you created them directly or from a spending template.

Policy information can include:

- Policy name and governed tenant.
- Scope.
- Active or disabled status.
- Limits and alerts.
- Agents and services.
- Model profile, when applicable.
- Billing method and unique customer-associated Azure subscription.
- Funding summary.
- Source template, when applicable.
- Created date and last modified date.
- Copilot Credit consumption.

Editing a policy changes only that policy in that governed tenant. It doesn't change the source template or policies in other tenants.

For tenant-specific changes, open the governed tenant details and edit the policy there.

### Analyze consumption across tenants

Use the **Consumption** tab to understand how Copilot Credits are used across the governed tenant estate.

The prototype provides date-range selection, column management, export, and the following views:

- **By tenant** - Credits used, prepaid and pay-as-you-go split, limit utilization, sessions, funding owner, and last activity.
- **By user** - User identity, tenant, license state, credits used, limit utilization, sessions, and last activity. Show user identities only where customer consent and privacy requirements permit it.
- **By group** - Governed tenant, group, active users, credits used, configured limit, limit utilization, and sessions.
- **By service** - Supported agent or service, credits used, active users, and last activity.

The production experience should also align with single-tenant reporting by spending policy and agent where supported.

Exported reports can be point-in-time snapshots and might temporarily differ from continuously refreshed dashboard values.

### Related content

- [Usage-Based Billing and Cost Management for Copilot Credits](/en-us/copilot/plan/usage-based-billing-overview-copilot-credits)
- [Set up usage-based billing for Copilot Credits](/en-us/copilot/implement/usage-based-billing-copilot-credits-setup)
- [Managing AI experiences enabled by usage-based billing](/en-us/copilot/implement/usage-based-billing-manage-copilot-credits)
- [Monitor Copilot Credit spending](/en-us/copilot/implement/usage-based-billing-copilot-credits-monitor-spending)
- [View Copilot Credit consumption in the Microsoft 365 admin center and on your Azure bill](/en-us/copilot/implement/usage-based-billing-compare-dashboard-views)
- [Usage-based billing guidance for CSPs, partner-managed customers, and MACC](/en-us/copilot/implement/usage-based-billing-copilot-credits-csp-partner-macc)