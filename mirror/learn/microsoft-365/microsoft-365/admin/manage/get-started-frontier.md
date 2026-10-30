---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Get started with the Microsoft Frontier Program - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/get-started-frontier?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how IT administrators can get started with the Microsoft Frontier program to evaluate innovative and emerging AI and non-AI features and AI agents before general availability.
author: mkbond007
ms.author: mabond
manager: dansimp
ms.reviwer: perfarny
ms.date: 2026-10-15T00:00:00.0000000Z
ms.topic: how-to
ms.service: m365-core
ms.subservice: change-management
ms.custom: copilot-frontier
audience: Admin
ms.collection: change-management
ms.localizationpriority: medium
ai-usage: ai-assisted
locale: en-us
document_id: 38f23ecc-4ec1-d183-93bf-5aee4a0f0a97
document_version_independent_id: 38f23ecc-4ec1-d183-93bf-5aee4a0f0a97
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/get-started-frontier.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/get-started-frontier
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/get-started-frontier.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 7b2e97a4-7e98-9c71-ab22-baed75ab99cd
---

# Get started with the Microsoft Frontier Program - Microsoft 365 admin | Microsoft Learn

The Microsoft Frontier program gives organizations preview access to innovative and emerging capabilities in Microsoft 365 before those features reach general availability (GA). By opting in to Frontier, IT administrators can evaluate new Microsoft Copilot agents, review AI and non-AI powered experiences, determine readiness for broader deployment across their tenant, and provide feedback about Frontier feature capabilities to Microsoft.

Microsoft's audience-based release model helps IT admins control how features are delivered to different user groups. This release model includes:

- **Frontier** (opt-in) is designed for users who want access before general availability to features to evaluate and prepare.
- **Standard release** is the default release experience where users receive new features as soon as they're generally available.
- **Deferred release** is for audiences in more complex environments that need additional time (approximately 30 days after rollout to the Standard release audience begins) to validate changes before deployment.

You can opt in users to both Frontier preview *and* assign them to Standard release or Deferred release. Users who are opted in to Frontier receive eligible Microsoft 365 features before general availability. For features that aren't part of Frontier, the user's existing Standard release or Deferred release preference determines when they receive features at GA.

To learn more about the audience-based release model, see [Configure modern release options for Microsoft 365 features](/en-us/microsoft-365/admin/manage/configure-release-options).

Access to Frontier program experiences vary depending on your organization's subscription and user roles.

Frontier features are preview and subject to change.

To learn more about the Microsoft Frontier program, what's new, and how to try what's next, see [Microsoft Frontier program](https://www.microsoft.com/microsoft-365-copilot/frontier-program).

Important

Frontier is managed at the tenant level. Production tenants can safely enroll users into the Frontier program to allow your organization access to Frontier features. IT admins have explicit control which users have access to which Frontier features.

Frontier features are preview and subject to change.

## Prerequisites

Review the following requirements and recommendations:

- Verify your [admin role](/en-us/microsoft-365/admin/add-users/about-admin-roles)in Microsoft 365 admin center. You need an account that includes one of the following roles:
    - AI Administrator
    - Security Administrator
    - Office Apps Administrator
- Assign users licenses that provide access to the products you want them to preview.
    - With the expansion of Frontier across Microsoft 365 previews to include both AI and non-AI features, a Microsoft Copilot license isn't required to enroll users in Frontier. However, to use Frontier features for Copilot, users need a [Microsoft Copilot license](/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing) or a license that includes access to Copilot. Users enrolled in Frontier without a Microsoft Copilot license aren't presented with Copilot-related Frontier features.
    - As another product example, to use Frontier features for Microsoft Teams, users need a license that includes access to Teams. Users enrolled in Frontier without a license that includes access to Teams aren't presented with Teams-related Frontier features.
- Verify that your own admin account has also has a corresponding license for products to ensure full access to Frontier AI settings and agents. Some Frontier settings and agents in the Microsoft 365 admin center might not appear.

## Enroll users in Frontier

Important

Frontier is for access to pre-GA features and Targeted release is for access to features early within general availability. With the retirement of Targeted release in January 2027, users assigned to Targeted release will default to their general availability release preferences, either [Standard release or Deferred release](configure-release-options). If you already have users enrolled in Frontier, these users will stay enrolled in Frontier after the retirement of Targeted release. For more information, see [Plan for the retirement of Targeted release](targeted-release-retirement).

You can manage Frontier settings in the Microsoft 365 admin center.

To turn on Frontier preview experiences for your users, do the following steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com).
2. Go to **Copilot** &gt; **Settings**.
3. Select the **View all** tab.
4. In the **Search all Copilot settings** search bar, type "Frontier".
5. Select **Copilot Frontier**.
6. Choose how Frontier access is assigned in your organization:

    - **No access** (default) - Users don't have access to Frontier features and agents.
    - **All users** - All users automatically receive Frontier features and agents.
    - **Specific users and groups** - Only specified users and groups automatically receive Frontier features and agents.

After you turn on Frontier experiences for your organization, eligible users can access supported preview features as they're released. It might take three hours for Frontier features and agents to be available to users.

Note

Starting March 29, 2026, newly published Frontier agents are available only to Frontier-enrolled users. Frontier agents published before this date continue to be accessible to all users with a Microsoft Copilot license.

Note

Some Microsoft 365 AI features across platforms (Windows, Mac, iOS, and Android) are currently released as a part of the Microsoft 365 Insider program. Learn more about the [Microsoft 365 Insider Program for Business](https://aka.ms/msft365insiderbusiness).

### Allow access to Frontier agents

Before your users can access Frontier agents, make sure that agent types are approved for use.

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), go to **Agent** &gt; **Settings** &gt; **Agent and plugin access**.
2. Verify that **Allow agents and plugins built by Microsoft** is checked. This setting allows the use of Microsoft Frontier agents.

For more information about managing access to specific agents for specific users or groups, see [Agent settings in Microsoft 365 admin center](/en-us/microsoft-agent-365/admin/agent-settings).

For information about managing agents that show up in the Agent Store, see [Set up Agent Store in Microsoft Copilot](/en-us/microsoft-365/copilot/copilot-agent-store).

Note

The Frontier admin control doesn't override the settings configured in the Agent section of the admin center. If an admin turned off a Frontier agent in the Agent view, that agent isn't available to users, regardless of a user's Frontier enrollment.

Important

After you enroll users in the Frontier program, **Frontier agents** are available to them from the Agent store in Microsoft Copilot. Search for "Built by Microsoft", and Frontier program agents are displayed with **(Frontier)** in the name. It might take up to three hours for Frontier agents to appear in the store.

### Deploy agents to your users directly

You can install and pin specific agents for select users or groups directly rather than users needing to search the Agent store. This method helps users start using Frontier agents more quickly. You must assign these users in Frontier Admin Control

1. Go to **Agents** &gt; **All agents**.
2. Select the agent you want to install.
3. In the **Users**tab, add the specific users or security groups that you want to use this agent.
    - Use a Microsoft Entra ID security group to target specific users who can access Frontier agents. This approach helps you validate experiences with a small group before broad rollout.
4. In the agent flyout, select **Install**. To help users find the agent, you can select **Pin for users**. The agent appears in the Microsoft Copilot app.

### Manage AI provider large language models

Some Frontier features and agents require access to large language models from AI providers, such as Anthropic. Review the requirements and understand the implications for each large language model you want to use.

Even if a Frontier feature relies on a particular AI provider being turned on, Frontier will never enable AI providers on your behalf. If the corresponding AI provider isn't enabled by you, the Frontier feature will not be usable for you or your users. To allow access to other models, use the Microsoft 365 admin center to explicitly approve each model. For more information, see [Manage AI provider settings in the Microsoft 365 admin center](/en-us/microsoft-365/copilot/copilot-anthropic-apps#manage-the-setting-in-the-microsoft-365-admin-center).

### Configure AI-enabled Cloud PCs for Frontier

To use AI-enabled Cloud PCs during Frontier preview, you must meet the Cloud PC specifications and turn on AI-enabled features to Cloud PCs in Microsoft Intune.

To learn more about AI-enabled Cloud PCs, including minimum requirements that must be met before setup, see [AI-enabled Cloud PC (Frontier Preview)](/en-us/windows-365/enterprise/manage-ai-enabled-features). After meeting these requirements, follow the instructions in [Manage AI-enabled features (Frontier Preview)](/en-us/windows-365/enterprise/manage-ai-enabled-features) to set up AI-enabled Cloud PCs for your users.

Important

Frontier experiences are governed by your existing customer agreements, including the Product Terms and Microsoft Data Protection Addendum (DPA). Frontier experiences are preview features that allow for personal data processing, as described in the DPA. As preview features, Frontier experiences may be modified, suspended, or discontinued, may not be covered by standard support commitments or service level agreements, and may be subject to additional Frontier-specific preview terms where applicable. HIPAA Business Associate Agreement coverage is not included for Frontier experiences. Certain Frontier experiences may only be available on a paid basis. Copilot credit consumption requirements are described in the [Microsoft Copilot Credits Guide](https://go.microsoft.com/fwlink/?linkid=2368800).

Frontier features do not comply with ISO 27001, ISO 27002, or ISO 27018 requirements.