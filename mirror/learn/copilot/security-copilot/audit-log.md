---
layout: Conceptual
title: Access the Security Copilot audit log | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/audit-log
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to access the Security Copilot audit log through Microsoft Purview Unified Audit Log (UAL), Microsoft Purview Data Security Posture Management (DSPM) for AI, and the Office Management API.
ms.date: 2026-05-29T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: partner-contribution
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: 21b483c3-978a-e65e-15c0-f45babf0dd88
document_version_independent_id: 21b483c3-978a-e65e-15c0-f45babf0dd88
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/audit-log.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/audit-log.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d2ac9bce-c7d0-a346-e02a-d51208f04867
---

# Access the Security Copilot audit log | Microsoft Learn

In today's stringent regulatory environment, it's important for organizations to monitor and analyze how users interact with security products. Organizations may need to keep track of actions, transactions, and configuration settings on a platform to ensure that they're meeting compliance regulations and regulatory standards.

Security Copilot today provides access to audit logs through Microsoft Purview Unified Audit Log (UAL), Microsoft Purview Data Security Posture Management (DSPM) for AI, and the Office Management API to help you satisfy compliance and regulatory requirements. The UAL from Purview gives you visibility into information such as administrator events and activity metadata, whereas DSPM for AI provides insights into prompt/response pairs.

- **Admin events** - Privileged actions such as changes to tenant-level settings or administrative changes (for example, data sharing, agent, agent trigger, plugin and promptbook configurations).
- **Activity metadata** - Logs of user interactions within the Security Copilot platform (for example, a user asked a prompt at a specific time with information on the activity type).
- **Prompt Response Pairs** - Activity in Security Copilot can contain a prompt to a skill, which produces a response pair. The pair and its content are a core functionality of the platform and a critical point of inspection for audit purposes.

Note

Customer content such as that contained within the prompt and response pair is currently only included through Microsoft Purview DSPM for AI. For more information, please see [Microsoft Purview for DSPM](/en-us/purview/ai-microsoft-purview-considerations#prerequisites-for-data-security-posture-management-for-ai).

By keeping track of these interactions, you can potentially identify risks, ensure stable operation of important workflows, and protect production data.

## Enable Security Copilot for Purview Audit and DSPM Solutions

To enable Purview DSPM for AI and UAL solutions for Security Copilot, the capability must be enabled within Security Copilot and configured within the respective Purview solutions. There are two options to enable the capabilities within Security Copilot that are as follows:

- During the first run experience, a Security Administrator may opt into allowing Microsoft Purview to access, process, copy and store administrator actions, user actions, and Copilot responses. For more information on getting started with Security Copilot see [Get started with Security Copilot](get-started-security-copilot).

    [![The initial configuration during the Security Copilot onboarding process](media/security-copilot-audit-fre.png)](media/security-copilot-audit-fre.png#lightbox)
- A Security Administrator can also access this option through the Owner settings page. For more information on role types, see [Understand authentication](authentication).

### Update audit log settings

Use the following steps to update the audit log settings:

1. Sign in to Security Copilot (https://securitycopilot.microsoft.com).
2. Select the home menu icon.
3. Navigate to the **Owner** &gt; **Owner settings** &gt; **Logging audit data in Microsoft Purview**.

    [![Image of Logging audit data in Microsoft Purview in the Owner settings page](media/security-copilot-audit-owner.png)](media/security-copilot-audit-owner.png#lightbox)

    Important

    Microsoft Purview will store your Customer Data in the region where your Microsoft 365 data is stored. For more information, see, [Privacy and data security](privacy-data-security). The default retention period for audit logs is 180 days but can be extended using audit log retention policies. For more information, see [Manage audit log retention policies](/en-us/purview/audit-log-retention-policies?tabs=microsoft-purview-portal).
4. You can turn the toggle on or off.

## Access Security Copilot audit logs via Unified Audit Log in Microsoft Purview

### Before you begin

This section gives an overview of the prerequisites to access the Unified audit log.

You'll need to:

- Verify that you have opted to allow Microsoft Purview access inside Security Copilot. For more information, see Enable the audit log capability.
- Verify that the audit log feature is active within Microsoft Purview. For more information, see [Before you search the audit log](/en-us/purview/audit-search?tabs=microsoft-purview-portal#before-you-search-the-audit-log).

Note

You'll require proper permissions to access the audit log in Microsoft Purview. For more information, see [Permissions in the Microsoft Purview portal](/en-us/purview/purview-permissions). These access rights might be different from those in Security Copilot.

### Options to access the Unified Audit Log in Microsoft Purview

You can take the following actions to access the audit log in Microsoft Purview:

- [Search the audit log](/en-us/purview/audit-search?tabs=microsoft-purview-portal) - Article that provides instructions on how to access and search through the audit log event data to gain insight and further investigate user activities.
- [Search through the audit log activities](/en-us/purview/audit-log-activities) - Article that describes the activities that are captured in the audit log.
- [Activities Operation Name References for Security Copilot](/en-us/purview/audit-log-activities#microsoft-security-copilot-agent-management) - A listing of activity operation names for Security Copilot management, agent management, and AI interactions such as prompts.
- [Search the audit log using a PowerShell script](/en-us/purview/audit-log-search-script) - Article that provides instructions on how you can run a PowerShell script to search the audit log to help you investigate security incidents and compliance issues.
- [Monitor user activities and system events with Security Copilot and Microsoft Sentinel](https://techcommunity.microsoft.com/blog/securitycopilotblog/monitor-user-activities-and-system-events-with-security-copilot-and-microsoft-se/4303368) - Blog that provides insight on how to leverage sending Security Copilot audit logs to your cloud native SIEM to gain deeper insights into usage and take proactive measures to mitigate risks.

## Access prompt response pair content in Microsoft Purview DSPM for AI

### Before you begin

This section gives an overview of the prerequisites to access prompt response pair content via Purview DSPM for AI.

You'll need to:

- Verify that you have opted to allow Microsoft Purview access inside Security Copilot. For more information, see Enable the audit log capability.
- Verify that necessary setup steps are complete, see [Learn | DSPM for AI Setup](/en-us/purview/ai-microsoft-purview-considerations#prerequisites-for-data-security-posture-management-for-ai).
- Validate that any administrator requiring policy creation or the ability to view content captured in prompts and responses meets the minimum permission levels. The role and permission configurations are detailed on [Learn | DSPM for AI](/en-us/purview/ai-microsoft-purview-permissions)
- Confirm that DSPM policies for Copilot content capture have been configured, see [DSPM for AI Default Policies on Learn](/en-us/purview/ai-microsoft-purview-considerations#default-policies-from-data-security-to-help-you-protect-sensitive-data-used-in-generative-ai).

Once the prerequisties are met different ways to enact information protection, and viewing the content within prompt and response pairs are posbible.

- Review the capbilites of the Purview DSPM for AI solution [Microsoft Purview data security and compliance protections for generative AI apps](/en-us/purview/ai-microsoft-purview)
- Protect the information accessed by different Copilot experiences [Information protection considerations for Copilot](/en-us/purview/ai-microsoft-purview-considerations#information-protection-considerations-for-copilot)
- View and search content within the Activity explorer events for Purview DSPM for AI [Activity explorer events](/en-us/purview/ai-microsoft-purview-considerations#activity-explorer-events)