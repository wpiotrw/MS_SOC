---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Modern change management for Microsoft 365 - Overview - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/plan-for-change-management?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: mabond
author: mkbond007
manager: dansimp
ms.date: 2026-10-07T00:00:00.0000000Z
ms.reviewer: sangar
audience: Admin
ms.topic: overview
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- M365-subscription-management
- Adm_O365
- Adm_TOC
- change-management
ms.custom: 
search.appverid: MET150
description: Proactively plan for change using AI-enabled tools to help your organization assess impact, prioritize work, and make informed decisions.
ai-usage: ai-assisted
locale: en-us
document_id: 4b664eff-6310-678a-3d4a-46090b087217
document_version_independent_id: 4b664eff-6310-678a-3d4a-46090b087217
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/plan-for-change-management.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/plan-for-change-management
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/plan-for-change-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: bd9be4ac-01b2-5429-6add-593ea1f2cb01
---

# Modern change management for Microsoft 365 - Overview - Microsoft 365 admin | Microsoft Learn

Organizations now operate in an environment of continuous change. Managing continuous service change using traditional management models can be a challenge for IT admins trying to keep pace.

Microsoft is building modern change management solutions, so that IT admins can enable their organizations to proactively plan for change. By using AI enabled tools, admins can assess impact, prioritize work, and make informed decisions. Modern change management capabilities help IT admins manage risk, meet compliance requirements, and adopt Microsoft 365 features with confidence.

This model gives IT admins configurable release options to control rollout timing, an enhanced Message center for clearer and more actionable communications, and two MCP (Model Context Protocol) Servers—Microsoft Release Communications MCP Server and Microsoft MCP for Enterprise—for AI-assisted change planning.

## Customize your organization's release experience for Microsoft 365

From the Microsoft admin center, you can choose between various release options for Microsoft 365 updates, either during general availability or before general availability.

Important

In November 2026, admins will no longer have the ability to enroll additional users or tenants in [Targeted release](release-options-in-office-365). In January 2027, Targeted release will be retired and no longer available to use. For more information, see [Plan for the retirement of Targeted release](targeted-release-retirement).

We recommend configuring release preferences for Frontier, Standard release, and Deferred release audiences to align with the new release model as Microsoft begins delivering an increasing number of major features through it before Targeted release is retired. For more information, see [Configure Standard and Deferred release options for Microsoft 365](configure-release-options).

### General availability

Microsoft thoroughly tests and validates all features and services before release.

**Standard release** delivers fully supported features to your organization at general availability (GA). Standard is the default release option, and Microsoft recommends it for most organizations. If you need to delay features for some users, you can choose Standard release for your organization and assign specific users to Deferred release.

**Deferred release** delays deferred-capable GA features for up to 30 days, giving admins additional preparation time. After 30 days, the features appear to your Deferred release users. If your organization has additional validation requirements, you can assign some or all users to Deferred release. You can identify deferred-capable features in the Message center. To test and validate changes before they reach your Deferred release users, add select users to Standard release so they receive deferred-capable feature updates earlier.

For more information about modern release options and how to configure them, see [Configure Standard and Deferred release options for Microsoft 365](configure-release-options).

Note

Currently, Deferred release and Frontier aren't available in government cloud environments. Check this article for future updates regarding availability.

### Before general availability

As an IT admin, you can opt in to use features *before* general availability by assigning users to specific release audiences.

The **Microsoft Frontier program** gives organizations early access to innovative and emerging AI capabilities in Microsoft 365 before those features reach general availability. By opting in to Frontier program, IT administrators can evaluate new Copilot agents, test non-AI and AI-powered experiences, determine readiness for broader deployment across their tenant, and provide feedback about Frontier feature capabilities to Microsoft.

The Frontier program supports early experimentation, but the features aren't fully supported, might change, and might not reach GA. They're intended for evaluation and readiness, not production use.

For more information on the Frontier program, see [Get started with the Microsoft Frontier program](get-started-frontier).

## Updated Message center interface

The updated Message center experience helps you deliver timely, relevant, and actionable change communications. It provides:

- Launch-day announcements with brief summaries and links to supporting resources.
- A consistent post format that includes the change description, rollout timeline, affected users and platforms, recommended actions, and compliance considerations.

For more information, see [What's new in Message center](message-center-updates) and [Message center in the Microsoft 365 admin center](message-center).

## Microsoft Release Communications MCP Server

AI-enabled organizations use intelligent tooling to accelerate their internal processes. By integrating the Microsoft Release Communications (MRC) MCP Server with your AI tools, you can connect to the latest release information for updates on the [AI at Work Roadmap](https://www.microsoft.com/microsoft-365/roadmap), formerly known as the Microsoft 365 Roadmap, and Azure Roadmap to create the infrastructure for AI-assisted reasoning over upcoming changes, priorities, and business impact.

For information on how to start using MRC MCP server, see [Get started with Release Communications MCP Server](mrc-mcp).

## Microsoft MCP Server for Enterprise

Shift from passively reviewing service updates to actively reasoning over change data. With Microsoft MCP Server for Enterprise, you can give AI agents conversational, read-only access to your organization's Message center and Service Health Dashboard data. The server queries Microsoft Graph using your delegated permissions, so Microsoft Entra security, access controls, and compliance requirements stay in place.

Use Microsoft MCP Server for Enterprise to:

- Summarize tenant-relevant Message center posts through natural language
- Identify changes that affect your organization and determine actions to take
- Prioritize work by reasoning over change data without leaving your AI workflow

For more information, see [Overview of Microsoft MCP Server for Enterprise - Microsoft Graph](/en-us/graph/mcp-server/overview).

## Available workloads for modern change management

This is the first step in our modernization change management journey. Not all Microsoft 365 workloads are available in this new model. Existing and traditional change management tools and methodologies can still be used for these experiences.

| Modern change management | Traditional change management |
| --- | --- |
| - [Modern change management - Overview](plan-for-change-management) - [Configure modern release options](configure-release-options) - [Modern release options FAQ](release-options-faq) - [Release Communications MCP server](mrc-mcp) - [What's new in Message Center](message-center-updates) | - [Set up the Standard or Targeted release options](release-options-in-office-365)- [Plan for the retirement of Targeted release](targeted-release-retirement) - [Microsoft 365 change guide - Microsoft 365 Apps](/en-us/microsoft-365-apps/best-practices/microsoft-365-change-guide) - [Stay on top of changes](stay-on-top-of-updates) |

## Communication channels for Microsoft 365 updates

The following table shows various communication channels we have that you can use to help manage change:

| Communication channel | Description | Documentation |
| --- | --- | --- |
| Microsoft AI at Work Roadmap | - Understand what features are coming, when they're expected to release, and which environments they apply to.- Provides early planning signals that complement Message center announcements and supports proactive change management across Microsoft 365. | [Microsoft AI at Work Roadmap](https://www.microsoft.com/microsoft-365/roadmap) |
| Message center | - Learn about official service announcements and feature changes.- Read these messages in the Microsoft 365 admin center, the admin mobile app, or receive a weekly digest in email.- Share these messages with others in your organization when you see a message someone else should act on. | [Message center in the Microsoft 365 admin center](message-center) |