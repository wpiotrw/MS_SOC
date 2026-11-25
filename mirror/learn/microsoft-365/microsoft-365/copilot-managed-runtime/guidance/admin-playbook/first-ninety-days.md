---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Your first 90 days of Copilot Managed Runtime governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/first-ninety-days?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
description: Use the day-1 checklist, a 30/60/90-day rollout plan, and a weekly, monthly, and quarterly rhythm to govern Copilot Managed Runtime if you're a Microsoft 365 admin who's new to Power Platform.
ms.topic: concept-article
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: yapatel
author: yashpatel22
manager: mihaelab
ms.service: microsoft-copilot
ai-usage: ai-generated
locale: en-us
document_id: 3bfaa570-3f13-a1fe-e849-1ccc918df5cb
document_version_independent_id: 3bfaa570-3f13-a1fe-e849-1ccc918df5cb
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/first-ninety-days.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-managed-runtime/guidance/admin-playbook/first-ninety-days
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/copilot-managed-runtime/guidance/admin-playbook/first-ninety-days.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/e6f942e8-55a7-4c86-b8e3-7456508ea850
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/f1834696-48d6-470d-966b-6ee418881596
platformId: c2f36173-b353-5b9b-fd31-8c99d4654e6b
---

# Your first 90 days of Copilot Managed Runtime governance | Microsoft Learn

This article in the Copilot Managed Runtime playbook for Microsoft 365 admins gives you a checklist for your first sitting, a phased plan for the first 90 days, and a recurring review rhythm. Use it to plan the work. It summarizes each task and where to do it, and it doesn't replace the detailed articles for each setting.

## Day-1 checklist

Work through the checklist in your first sitting. It takes roughly two hours. You need a Global Administrator, or a Power Platform Administrator working with a Billing Administrator.

| Task | Where |
| --- | --- |
| Confirm which admin roles you and your team hold. Move anyone who only needs visibility to a read-only role. | Microsoft Entra admin center or Microsoft 365 admin center, **Roles**. See [Roles and responsibilities](../../../admin/manage/apps/roles-responsibilities). |
| Review the governance model, core terms, and admin responsibilities. | [Playbook overview](overview), [day-0 defaults](day-zero), and [before you start](before-start) |
| If you already use Power Platform routing, review it first. Decide whether to scope routing to security groups or include all users. | Power Platform admin center, **Tenant settings** &gt; **Environment routing**. See [Environment routing for Copilot Managed Runtime](/en-us/power-platform/admin/default-environment-routing-copilot-managed-runtime). |
| Open the default environment group and review its four rules. | Microsoft 365 admin center, **Apps** &gt; **Settings** &gt; **Environment groups**. See [Review the default settings](../../../admin/manage/apps/governance#review-the-default-settings). |
| Decide who can build. Create a pilot Microsoft Entra security group and limit Copilot Studio app creation to it. | Microsoft 365 admin center, **Apps** &gt; **Overview** &gt; **Set up app creation spaces**. See [Scope access to Copilot Studio app creation with security groups](../../../admin/manage/apps/#scope-access-to-copilot-studio-app-creation-with-security-groups). |
| Confirm the CLI creation path is off (the default) unless you have a developer group ready. | Power Platform admin center, **Copilot** &gt; **Settings** &gt; **Managed apps**. See [Control whether apps can be created using the CLI](../../../admin/manage/apps/governance#control-whether-apps-can-be-created-using-the-cli). |
| Check the sharing controls. Decide your starting position on organization-wide and guest sharing. | Microsoft 365 admin center, **Apps** &gt; **Settings** &gt; **Environment groups** &gt; **Sharing**. See [Configure sharing settings](../../../admin/manage/apps/governance#sharing-1). |
| Set up runtime cost guardrails. Turn on usage-based billing and create one spending policy for managed applications that covers all users. | Microsoft 365 admin center, **Copilot** &gt; **Cost management**. See [Enable users to run apps](../../../admin/manage/apps/licensing-credits#enable-users-to-run-apps). |
| Run the audit test. Create, launch, and delete a test app, then find the events in Microsoft Purview audit search. | Microsoft Purview portal. See [Search and export app events](../../../admin/manage/apps/security-compliance#search-and-export-app-events). |
| Agree who owns what between Microsoft 365 admins, Power Platform admins, security, and finance. | Your team (see [Before you start on Copilot Managed Runtime governance](before-start)) |

Note

For background on the decisions in this checklist, see [Review and adjust the defaults for Copilot Managed Runtime governance](review-defaults).

## 30/60/90-day plan

The plan has three phases. Each phase has a goal, actions, and exit criteria that tell you when you're ready to move on. The recommendations suit a gradual rollout. Adjust them to your organization's size, risk tolerance, and existing policies.

### Days 0 to 30: Learn and pilot

The goal is to understand the defaults and run a small, safe pilot.

Actions:

- Complete the day-1 checklist.
- Pilot with 5 to 20 builders in one security group.
- Keep the default connector, content security policy, and sharing policies.
- [Create a health alert](../../../admin/manage/apps/alerts). Review **All apps** and alerts weekly.

Exit criteria:

- Pilot apps are running.
- The audit test passed.
- A spending policy is in place.

### Days 31 to 60: Harden exceptions and oversight

The goal is to create repeatable processes for exceptions.

Actions:

- Create an intake form for connector and content security policy exceptions.
- Test content security policy changes in report-only mode.
- Decide your guest and organization-wide sharing stance.
- Start the monthly exception review.

Exit criteria:

- The exception process is used at least once.
- Your sharing stance is documented.

### Days 61 to 90: Scale deliberately

The goal is to widen access.

Actions:

- Expand the creation security group in stages.
- Plan environment groups for team and organization apps if needed.
- Write the owner-change and offboarding process. Use [Manage the lifecycle of personal environments](../../../admin/manage/apps/personal-environments-lifecycle-copilot-managed-runtime) for handover steps.
- Report health, usage, and spend to leadership.
- Re-read the preview watch list in [Reference for Copilot Managed Runtime governance](reference).

Exit criteria:

- A wider audience is live.
- The operating rhythm is running.
- Leadership is briefed.

## Ongoing rhythm

After the first 90 days, review on the following schedule.

| How often | Task | Where |
| --- | --- | --- |
| Weekly | Review **All apps** for new apps, unexpected locations or groups, and unknown owners. Check triggered alerts. | Microsoft 365 admin center, **Apps** &gt; **All apps** and **Monitor**. See [App inventory](../../../admin/manage/apps/inventory#app-inventory) and [Monitor the health of apps](../../../admin/manage/apps/visibility-monitoring). |
| Weekly | Review credit consumption against limits, and handle credit requests. | Microsoft 365 admin center, **Copilot** &gt; **Cost management**. See [Monitor and adjust](../../../admin/manage/apps/licensing-credits#monitor-and-adjust). |
| Monthly | Review connector and content security policy exceptions, apps owned by people who left, and unused apps. Spot-check audit records. | Environment group rules, **All apps**, Microsoft Purview |
| Quarterly | Re-assess defaults, roles, spending limits, and the watch list. Check Microsoft Learn for changes. | This playbook and Microsoft Learn |