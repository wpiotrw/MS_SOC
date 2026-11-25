---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: What's in place on day 0 for Copilot Managed Runtime governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/day-zero?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn what governance Copilot Managed Runtime sets up automatically before the first app exists, how it interacts with existing Power Platform routing, and what to watch for. For Microsoft 365 admins.
ms.topic: concept-article
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: yapatel
author: yashpatel22
manager: mihaelab
ms.service: microsoft-copilot
ai-usage: ai-generated
locale: en-us
document_id: e9a81466-fc3e-f4cc-a5e8-f29f8d2b95af
document_version_independent_id: e9a81466-fc3e-f4cc-a5e8-f29f8d2b95af
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/day-zero.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-managed-runtime/guidance/admin-playbook/day-zero
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/copilot-managed-runtime/guidance/admin-playbook/day-zero.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: b19a0366-27c3-f6b3-bc34-1d8097d1e7af
---

# What's in place on day 0 for Copilot Managed Runtime governance | Microsoft Learn

Copilot Managed Runtime applies default governance before the first app exists, so every app is governed from the moment you create it. You don't need to configure anything before makers start building. This article describes what's already in place, how it interacts with an existing Power Platform setup, and which behaviors you can't undo.

Use this article to understand the starting point. To review and change individual settings, see [Review and adjust the defaults for Copilot Managed Runtime governance](review-defaults).

## How default governance is set up

Configure default governance, including the default environment group, once. It's triggered by whichever of these happens first:

- A maker starts to create the first app.
- An admin selects **Set up governance** on the **Apps** &gt; **Overview** page in the Microsoft 365 admin center.

Either way, governance is in place before the first app exists. After you configure it, the **Set up governance** option is no longer available. For instructions to find and review the environment group rules, see [Review the default settings](../../../admin/manage/apps/governance#review-the-default-settings).

## Day-0 defaults at a glance

The following table summarizes the default for each governance area, and whether you can change it. For details about each area, see [Review and adjust the defaults for Copilot Managed Runtime governance](review-defaults).

| Area | Default | Can you change it? |
| --- | --- | --- |
| Sign-in | Every app uses Microsoft Entra ID. Copilot Managed Runtime checks that the user is signed in and has permission before delivering any app code. You can further control access with Conditional Access policies. | No |
| Auditing | Audit records for app creation, launch, deletion, and governance changes appear in Microsoft Purview. | No |
| Where apps live | Each maker builds in their own personal environment, which is a Managed Environment. | Yes |
| Creation paths | On: Copilot Studio, Copilot Code, and Copilot Cowork. Off: CLI.^1^ | Yes |
| Connectors | A Microsoft-curated allow list of first-party connectors and MCP servers that use Entra-only authentication. High-risk actions are blocked. | Yes |
| Browser behavior | A restrictive content security policy is enforced. Apps can talk only to their own origin unless you allow more. | Yes |
| Sharing links | Apps are private to their owner until shared. Creators can generate a link that any member of your organization can open. | Yes |
| Guest users | B2B users are off by default. | Yes |
| Build and release | Source is stored in a Git repository, either platform-managed or the developer's own GitHub Enterprise Cloud repository. Deploying externally built artifacts is off by default. | External artifacts: yes |
| Inventory and health | Every app appears in **Apps** &gt; **All apps** within about 15 minutes. No health alerts exist until you create them. | Alerts: yes |

^1^ Environment admins can create apps with the CLI even when this setting is off.

## If you already use Power Platform

Copilot Managed Runtime works alongside your existing Power Platform setup. It uses [environment routing](/en-us/power-platform/admin/default-environment-routing-copilot-managed-runtime?toc=/microsoft-365/copilot-managed-runtime/toc.json&amp;bc=/microsoft-365/breadcrumb/TOC.json) to give each maker a personal developer environment. Environment routing for Copilot Managed Runtime is turned on automatically in every tenant and can't be turned off.

What happens next depends on whether your tenant already has routing rules.

| Your tenant today | What Copilot Managed Runtime does |
| --- | --- |
| No routing configured | Routing is enabled for Copilot Managed Runtime only. New personal developer environments go into one environment group that's preconfigured with the Copilot Managed Runtime rules. |
| Routing enabled for another product, but no rules | Routing is turned on automatically for Copilot Managed Runtime. A rule sends new personal developer environments to one preconfigured environment group. |
| Routing rules that include an Everyone catch-all | The Microsoft 365 admin center reflects your existing groups and rules. Each group gains Copilot Managed Runtime settings, such as sharing limits and content security. |
| Routing rules scoped to security groups, no catch-all | Same as the previous row, but people outside every group can't create Copilot Managed Runtime apps until you add them to a group or add an Everyone rule. |

For details about these routing scenarios, see [If you're an existing Power Platform customer](../../../admin/manage/apps/governance#if-youre-an-existing-power-platform-customer).

## What doesn't change

Copilot Managed Runtime leaves the following parts of your existing setup alone:

- **Your makers' existing experience.** If Copilot Managed Runtime is the only product with routing turned on, makers who use Power Apps, Power Automate, or Copilot Studio aren't routed to personal developer environments. They keep building where they do today.
- **Your existing routing rules and environment groups.**
- **Licensing for makers.** Makers who use their personal developer environment only to build Copilot Managed Runtime apps don't need a premium license. For details, see [Copilot Managed Runtime licensing FAQ](../../../admin/manage/apps/licensing-faq#building-apps).

## What to watch for

Review these behaviors before you make routing changes:

- **Some changes can't be undone.** You can't delete an Everyone routing rule, and it must always be last in priority. If your tenant has an Everyone rule above a security group rule, change the order before you make other routing changes.
- **Restricting developer environment creation doesn't block routing.** The **Environment creation: Developer** tenant setting affects only environments that people create manually. It doesn't stop routing from creating personal developer environments.
- **New routing rules need an environment group.** You can't create a routing rule without selecting one.
- **Dataverse isn't included.** Environments created for Copilot Managed Runtime start without Dataverse. Makers or admins can add it later.
- **Classic data policies might still apply.** Classic data policies (DLP) can still apply to existing environment groups alongside advanced connector policies. See [How connector policies are evaluated for existing environment groups](../../../admin/manage/apps/governance#how-connector-policies-are-evaluated-for-existing-environment-groups).