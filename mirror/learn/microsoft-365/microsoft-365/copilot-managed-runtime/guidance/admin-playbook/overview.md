---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Admin 101 playbook for Copilot Managed Runtime | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/overview?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how Copilot Managed Runtime hosts and governs your organization's internal apps, the core terms to know, and the three principles behind its governance. Written for Microsoft 365 admins who are new to Power Platform.
ms.topic: overview
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: yapatel
author: yashpatel22
manager: mihaelab
ms.service: microsoft-copilot
ai-usage: ai-generated
locale: en-us
document_id: e969e791-c160-0361-12ad-e4497d41d7d3
document_version_independent_id: e969e791-c160-0361-12ad-e4497d41d7d3
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/overview.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-managed-runtime/guidance/admin-playbook/overview
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/copilot-managed-runtime/guidance/admin-playbook/overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 9c9ae87c-1cd3-d1f8-b438-25c3873b6e6c
---

# Admin 101 playbook for Copilot Managed Runtime | Microsoft Learn

[Copilot Managed Runtime](../../../admin/manage/apps/) hosts your organization's internal line-of-business apps and applies your [governance, security, and compliance controls](../../managed-runtime-security-governance) to every app from the moment it's created. This playbook helps Microsoft 365 admins who are new to Power Platform understand the model, make safe day-1 decisions, and run Copilot Managed Runtime for the first 90 days.

This article gives you the vocabulary and the big picture. To understand the governance model, continue with [what's in place on day 0](day-zero) and [what to know before you start](before-start). When you're ready to make decisions, [review and adjust the defaults](review-defaults) and [prepare for your first 90 days](first-ninety-days). For definitions, see the [glossary](reference#glossary).

## Copilot Managed Runtime at a glance

People can build apps with Copilot Cowork, Microsoft Copilot Studio, Copilot Code, or the Copilot Managed Runtime SDK and CLI. Whichever tool they use, every app:

- Runs in a Microsoft-hosted environment.
- Uses Microsoft Entra authentication.
- Follows your tenant's governance policies.
- Appears in the Microsoft 365 admin center.

Users find and open the apps shared with them in the Copilot Managed Runtime portal at https://managedapps.cloud.microsoft.

If you manage OneDrive, this model is familiar. Each maker builds in a private space, and an app stays private until its owner shares it. As an admin, you can see every app in your tenant, who built it, and whether it's shared.

You manage Copilot Managed Runtime in the Microsoft 365 admin center. You can keep the default governance policy that Microsoft provides, or adjust it to fit your organization. A few advanced settings, such as allowing app creation with the CLI, are available only in the Power Platform admin center. This playbook notes them where they apply.

Note

Governance is on from the very first app. You don't have to design a governance model before people start building. Microsoft ships a default policy that includes approved connectors, sharing limits, and content security rules. Your job is to review the defaults, decide where your organization needs to be stricter or more relaxed, and keep watch.

## Core terms to know

You manage Copilot Managed Runtime from the Microsoft 365 admin center, but some settings and messages use Power Platform terms. The following terms are enough to get started. For more definitions, see the [glossary](reference#glossary).

| Term | Definition | Think of it like... |
| --- | --- | --- |
| Environment | A logical container where you create apps and the governance boundary for the app. Settings and policies apply at the environment level, and every Copilot Managed Runtime app lives in one environment. | A SharePoint site: a boundary with its own settings that the content inside inherits. |
| Managed Environment | An environment with extra governance features turned on, such as sharing limits, content security policies, usage insights, and the ability to join an environment group. Every environment that hosts Copilot Managed Runtime apps is a Managed Environment. | A site or device that's enrolled in central management. |
| Personal environment (PE) | A private, isolated sandbox created automatically for each maker, separate from production. For Copilot Managed Runtime, personal environments are Managed Environments. | Each person's OneDrive: private by default, and provisioned for them automatically. |
| Environment group | A named collection of Managed Environments that share the same rules. An environment can be in only one group, and groups can't be nested. | A device group you assign a policy to. |
| Environment group rule | A setting that you configure and publish at the environment group level. After it's published, it applies to every environment in the group, and environment admins can't change it. To give one environment a different setting, move it to a different group. | A baseline policy setting that environment admins can't override. |
| Connector | A prebuilt, authenticated link from an app to a service such as SharePoint, Outlook, or SQL Server. More than 1,500 exist. | A preapproved integration. |

## Create, run, and govern apps

People in your organization can [create apps in four ways](../../overview#four-ways-to-create-an-app). Whichever way they choose, users open apps in one portal, and you govern them from the Microsoft 365 admin center.

| Task | Tool | Who uses it | Default | Where you control it |
| --- | --- | --- | --- | --- |
| Create | [Copilot Cowork](/en-us/microsoft-365/copilot/cowork/use-cowork#build-apps-with-the-app-skill) | Business users who describe an app in chat or invoke the `/app` skill | On | Microsoft 365 admin center |
| Create | [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/apps-experience/apps-overview) | Makers who want control over build and publish | On | Microsoft 365 admin center |
| Create | [Copilot Code](/en-us/copilot/code/use-code#build-and-publish-apps-to-copilot-managed-runtime) | Business users and developers using an AI coding agent | On | Microsoft 365 admin center |
| Create | [CLI and SDK](../../developer/apps/) | Professional developers who prefer a code-first workflow | Off\* | Power Platform admin center |
| Run | [Copilot Managed Runtime portal](../../overview#one-place-to-find-and-run-your-apps) | Users who find and open the apps they create and the apps shared with them | Anyone in the org can open links shared with them | Microsoft 365 admin center |
| Govern | [Apps section of Microsoft 365 admin center](../../../admin/manage/apps/) | Governance admins, security admins, and billing admins | Not applicable | Microsoft 365 admin center |

\*Environment admins can create apps with the CLI even when this setting is off.

## Three principles and nine governance areas

Copilot Managed Runtime governance follows three principles. [Review and adjust the defaults for Copilot Managed Runtime governance](review-defaults) groups nine governance areas under them, with one section for each area.

| Principle | What it means | Governance areas |
| --- | --- | --- |
| Safe by default | Every app has governance built in from the moment you create it. | - Who can create apps- Where apps live- What apps can connect to- What apps can load from the browser- Audit and sign-in |
| Govern at scale | As the number of apps grows, you can see what exists, who owns it, whether it's healthy, and what it costs, all in one place. | - Who can use apps (sharing)- What exists and whether it's healthy |
| Balance control and productivity | Controls shouldn't add friction for makers and users. | - Cost and spending policies- Code and release |