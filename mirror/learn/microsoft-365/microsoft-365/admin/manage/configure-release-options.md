---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Configure new Standard and Deferred release options for Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/configure-release-options?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: mabond
author: mkbond007
manager: dansimp
ms.date: 2026-10-15T00:00:00.0000000Z
ms.reviewer: sangar
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: change-management
ms.localizationpriority: medium
ms.collection:
- Tier2
- M365-subscription-management
- Adm_O365
- Adm_TOC
- change-management
ms.custom: 
search.appverid: MET150
description: Learn how to set up Standard release, Deferred release, and Frontier release options for new features in Microsoft 365 to better manage your organization.
ai-usage: ai-assisted
locale: en-us
document_id: d016e391-0d50-c855-2e45-90b405f17a5c
document_version_independent_id: d016e391-0d50-c855-2e45-90b405f17a5c
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/configure-release-options.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/configure-release-options
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/configure-release-options.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 751d7d88-fdf7-33ad-b866-ef1ca81d33b8
---

# Configure new Standard and Deferred release options for Microsoft 365 - Microsoft 365 admin | Microsoft Learn

Microsoft 365 delivers updates continuously, enabling organizations to adopt new capabilities without large, infrequent upgrades. To help IT admins manage this pace of change, Microsoft 365 offers a new three-tier, audience-based release model—**Frontier, Standard release, and Deferred release**—so organizations can balance early access with readiness and control.

## Release options

Use these new release options to align feature delivery with your organization's readiness, governance requirements, and overall change management strategy.

Important

In November 2026, administrators can no longer add users to, remove users from, or modify Targeted release enrollment. In January 2027, Targeted release will be retired and no longer available to use. For more information, see [Plan for retirement of Targeted release](targeted-release-retirement).

To prepare for this change, we recommend configuring Standard release and Deferred release options to manage when users in your organization receive generally available Microsoft 365 services as Microsoft delivers features through the new release model. If your organization has configured Targeted release in the Microsoft 365 admin center, you can continue using your existing configuration until its retired. Use the Message center to stay informed about updates delivered through the new audience-based release model.

### Frontier program

For pre-GA availability, [Frontier](https://www.microsoft.com/microsoft-365-copilot/frontier-program) provides preview access to innovative and emerging AI and now non-AI capabilities in Microsoft 365 before those features reach general availability. You can opt in users to both Frontier preview *and* assign them to Standard release or Deferred release. Users who are opted in to Frontier receive eligible Microsoft 365 features before general availability. For features that aren't part of Frontier, the user's existing Standard release or Deferred release preference determines when they receive features at GA.

For more information about getting started with the Frontier preview, see [Get started with the Microsoft Frontier program](get-started-frontier).

### Standard release

With **Standard release**, your organization receives new features as soon as they're generally available (GA). Standard release should be the primary release channel for most customers. Microsoft thoroughly tests and validates all features and services before releasing them. For general availability updates, the default release preference for your organization is Standard release. You can update this setting to Deferred release if you need additional time for validation and change management.

In your modern release preferences, your organization is configured for Standard release by default. With Standard release, your organization receives new features as soon as they're generally available (GA). Standard release should be the primary release channel for most customers. Microsoft thoroughly tests and validates all features and services before releasing them. You can update this setting to Deferred release if you need additional time for validation and change management.

If your organization is using Targeted release, you can continue with your existing configuration until Targeted release is retired. Features that aren't in Targeted release follow your configured Standard release or Deferred release preference.

### Deferred release

If you have additional validation requirements, consider using **Deferred release** for some or all users. Deferred release lets you delay deferred-eligible major updates for specific users for approximately 30 days after rollout to the Standard release audience begins. After the 30-day period, deferred-eligible features are released to users in the Deferred release audience. If you have configured Deferred release for your organization, updates that aren't eligible for Deferred release aren't delayed and these updates are released to Deferred release users on the same schedule as Standard release. In the Message center, features included in Deferred release are tagged as both **Major update** and **Deferred feature**.

## How release validation works

Microsoft feature teams validate each new release first, followed by the Microsoft 365 feature team. Then, the feature rolls out to all of Microsoft. At each release phase, Microsoft collects feedback and further validates quality by monitoring key usage metrics before it goes to the public. This series of progressive validations helps make sure the worldwide rollout to general availability (Standard release) is as robust as possible.

As shown in the following figure, you can now use a modern, audience-based release model that includes the Frontier program, Standard release, and Deferred release as release options.

[![Figure displaying audience-based release audiences for Microsoft 365.](../../media/audience-based-release-model.png)](../../media/audience-based-model-expanded.png#lightbox)

For a comparison of release options, see the following table:

| Release audience | Primary purpose | Feature readiness | Key considerations for IT admins |
| --- | --- | --- | --- |
| **Frontier program** | Early experimentation and feedback | Pre-GA, not fully supported | You must opt in to access Frontier. Frontier features are preview, subject to change, and not governed by GA SLAs. IT admins can control which users have access to which Frontier features and agents. |
| **Standard release(default)** | Default GA rollout | Fully supported GA features | Features are supported, communicated through Message center and release notes, and expected to remain available under standard lifecycle policies. Recommended for most organizations. |
| **Deferred release** | Delayed GA for additional preparation | Fully supported GA features (delayed) | Same functionality as Standard release, delayed 30 days after Standard release (GA) for major updates. Consider if your organization has additional validation requirements. |

For significant updates, Microsoft first notifies you through the [AI at Work Roadmap](https://www.microsoft.com/microsoft-365/roadmap), formerly known as Microsoft 365 Roadmap. Before rollout, Microsoft notifies you through the [Microsoft 365 Message center](https://go.microsoft.com/fwlink/p/?linkid=2070717).

### What qualifies as a major update

Major updates are communicated at least 30 days in advance when an action is required and might include:

- User impacting changes to daily productivity such as changing a user's inbox, meetings, delegations, sharing and access that might result in help desk calls, or organizational conformance concerns.
- Changes to the themes, web parts, deployed Copilot agents, and other components that might impact customer customizations.
- Increases or decreases to visible capacity such as storage, number of rules, Copilot agents and prompts, items, or durations.
- Rebranding that might cause end-user confusion or result in help desk changes, collateral changes, or URL changes if the new URL isn't \*.cloud.microsoft
- A new service or application deployed with default settings turned on.
- Changes to where data is stored or accessed.

In the Message center, major updates are tagged as **Major update**. For more information about the Message center, see [Message center in the Microsoft 365 admin center](message-center).

## Prerequisites

To configure Standard release and Deferred release options, you need one of the following roles in the Microsoft 365 admin center:

- Office Apps Admin
- Security Admin
- AI Admin

For more information, see [About administrator roles in the Microsoft 365 admin center](../add-users/about-admin-roles).

### Security groups

To manage group-based exceptions, create or identify a dedicated Microsoft Entra ID security group to use for that release option. For more information about security groups, review the following articles:

- [Learn about groups](/en-us/entra/fundamentals/concept-learn-about-groups)
- [Manage groups with Microsoft Entra admin center](/en-us/entra/fundamentals/how-to-manage-groups)
- [Manage groups with Microsoft Graph PowerShell](/en-us/entra/identity/users/groups-settings-v2-cmdlets)

## Release option best practices

To balance early access with organizational readiness, use the release options in the following ways:

- Enroll your organization in Standard release to get the latest Microsoft 365 improvements as soon as they reach general availability. Optionally, assign business-critical users to Deferred release to give them more time to prepare for major changes.
- Use Deferred release if you need extra time to validate deferred-capable features before broad rollout. Assign a subset of IT pros or power users to Standard release to evaluate new features for privacy and compliance readiness.
- Plan release phases around user impact and readiness, not individual feature controls, to help manage risk and set clear expectations for users.
- Align your release configuration with your change management and support readiness, including documentation, training, and help desk preparation.
- Review and adjust audience assignments over time as your organization's readiness and change tolerance evolve.

## Configure general availability release options in Microsoft 365 admin center

Important

For customers in GCC, GCC High, and DoD environments, Standard release (general availability) remains the supported release option following the [retirement of Targeted release](targeted-release-retirement). Currently, Deferred release and Frontier aren't available in government cloud environments. Check this article for future updates regarding availability.

By default, use Standard release for Microsoft 365 service updates. This option meets the needs of most customers. To better manage your organization's readiness and testing needs, you can change the default release selection to Deferred release at any time in the Microsoft 365 admin center. It can take up to 24 hours for the following changes to take effect in Microsoft 365.

To assign users or [security groups](/en-us/entra/fundamentals/concept-learn-about-groups) to Deferred release, follow these steps:

1. Sign in to the Microsoft 365 admin center.
2. In the left navigation, expand **Copilot** and select **Settings**.

    [![Screenshot of Copilot settings in Microsoft 365 admin center.](../../media/copilot-settings-admin-center.png)](../../media/copilot-settings-admin-center-expanded.png#lightbox)
3. Under the **View all** tab, select **Copilot Release Preferences: General Availability**.
4. Choose either **Standard release** or **Deferred release**.
5. Add any user or security group exceptions. You can add up to 100 exceptions to Standard release or Deferred release. Each user in a security group and each user added individually count toward the 100-user limit.

    - If you want to assign only a specific user or security group to Deferred release, select **Standard release**, search for the user or group, and select their name.

        ![Screenshot of Standard release in Microsoft 365 admin center.](../../media/audience-release-options-standard.png)
    - If you want to assign only a specific user or security group to Standard release, select **Deferred release**, search for the user or group, and select their name.
6. Select **Save**.

To opt in to Frontier preview, follow the instructions in [Configure Frontier preview for Microsoft 365 services](get-started-frontier).

In November 2026, release preferences for Frontier, Standard release, and Deferred release can be managed through the unified release preferences experience in the Microsoft 365 admin center. The current experience for managing Standard release and Deferred release preferences will be retired when the unified release preferences experience becomes available. Additional details about related admin experience changes will be shared in Message center and this article will be updated to show the new navigation.

Note

If you move users from Standard release to Deferred release, they might lose access to features that aren't available yet in Deferred release.