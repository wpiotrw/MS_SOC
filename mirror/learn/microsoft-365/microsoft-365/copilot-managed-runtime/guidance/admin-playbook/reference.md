---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Reference for Copilot Managed Runtime governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/reference?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
description: Find where common Copilot Managed Runtime admin tasks are documented, look up glossary terms, and read answers to frequently asked questions in this reference for Microsoft 365 admins.
ms.topic: concept-article
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: yapatel
author: yashpatel22
manager: mihaelab
ms.service: microsoft-copilot
ai-usage: ai-generated
locale: en-us
document_id: 225c609e-703e-d40e-fd40-f46db336d5dc
document_version_independent_id: 225c609e-703e-d40e-fd40-f46db336d5dc
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/copilot-managed-runtime/guidance/admin-playbook/reference.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-managed-runtime/guidance/admin-playbook/reference
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/copilot-managed-runtime/guidance/admin-playbook/reference.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 1d2a8f19-dd74-a382-3799-6edc33e589e6
---

# Reference for Copilot Managed Runtime governance | Microsoft Learn

This reference collects lookup material for the Intro to Copilot Managed Runtime playbook: where common admin tasks are documented, definitions for terms used in the playbook, and answers to two frequently asked questions. Use it when you know what you want to do or what a term means, and you don't need the full guidance in the other playbook articles.

## Common tasks and where they're documented

Step-by-step instructions for these tasks already exist on Microsoft Learn, so this playbook points to them instead of repeating them.

| Task | Learn more |
| --- | --- |
| Block or delete an app | [Actions in the app inventory](../../../admin/manage/apps/inventory#actions) |
| Approve a connector exception | [Customize connectors and MCP servers](../../../admin/manage/apps/governance#connectors-and-mcp-servers-1) |
| Add a content security policy (CSP) source | [Customize content security policy](../../../admin/manage/apps/governance#content-security-policy-1) |
| Set up a spending policy | [Turn on usage-based billing](../../../admin/manage/apps/licensing-credits#step-1-turn-on-usage-based-billing) and [Create a broad Copilot Managed Runtime spending policy](../../../admin/manage/apps/licensing-credits#step-2-create-a-broad-copilot-managed-runtime-spending-policy) |
| Change an app owner | [Hand over Copilot Managed Runtime apps and their personal environment](../../../admin/manage/apps/personal-environments-lifecycle-copilot-managed-runtime#hand-over-copilot-managed-runtime-apps-and-their-personal-environment) |

Note

The app inventory shows the current owner of an app, which can differ from the person who created it.

## Glossary

These terms are in addition to the five core terms defined in the [playbook overview](overview#core-terms-to-know): environment, Managed Environment, personal environment, environment group, and environment group rule. The core terms table also defines connector.

| Term | Definition | Think of it like... |
| --- | --- | --- |
| Advanced connector policy (ACP) | Controls which connectors, and which actions inside each connector, apps can use. Also covers MCP servers. Always set at the environment group level. | An allow list for what apps can talk to, down to the individual operation. |
| Classic data policy (DLP) | A Power Platform policy that sorts connectors into Business, Non-Business, and Blocked groups. An app or flow can't mix Business and Non-Business connectors, and Blocked connectors can't be used. Applies to the whole tenant or selected environments. | Sorting connectors into "work" and "personal" buckets that can't share data, plus a banned list. |
| Copilot Credits | The common metered unit for usage-based billing across eligible Microsoft AI services, including running Copilot Managed Runtime apps. Credits are pooled at the tenant level. | Mobile data minutes drawn from one shared pool: you pay for what's used, up to the limits you set. |
| Dataverse | The Power Platform data service. It's optional for Copilot Managed Runtime. Environments created for Copilot Managed Runtime start without it. | A database you can add to a site later. It isn't needed to host the app. |
| Environment routing | Decides which environment a maker builds in (for example, their own personal environment), using routing rules and security groups. | A provisioning rule: "everyone in group X gets their own space." |
| Managed Environment | An environment with extra governance features switched on. Environment groups can contain only Managed Environments. | A device that's enrolled for management, so it can receive central policy. |
| Spending policy | A rule in the Microsoft 365 admin center (**Copilot** &gt; **Cost management**) that says who can use Copilot Credits, for which services, and up to what limit. For Copilot Managed Runtime, you create one for managed applications. | A corporate card policy: who gets a card, what it can be used for, and the limit. |