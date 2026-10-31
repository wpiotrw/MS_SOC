---
layout: Conceptual
title: Monitoring agents with Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how Microsoft Purview Insider Risk Management monitors AI agent activity, surfaces risky behaviors, and helps protect against data exposure in your organization.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance, agents
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: concept-article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-08-04T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
locale: en-us
document_id: 90c090e3-eea1-9ded-e9d0-0adb7384e851
document_version_independent_id: 90c090e3-eea1-9ded-e9d0-0adb7384e851
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-monitoring-agents.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-monitoring-agents
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-monitoring-agents.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/062d60c9-ee0f-402e-a046-b4e67c3572d6
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/17d3b3f6-a66e-4c69-9774-14a73c38e669
platformId: d5e9f94b-c62d-4d5d-53fc-9c9b577c4324
---

# Monitoring agents with Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Microsoft Purview Insider Risk Management enables organizations to identify, investigate, and respond to potential insider risks across users and agents. As organizations increasingly adopt AI agents, Insider Risk Management provides built-in capabilities to help monitor agent activity and surface risky behaviors that could lead to data exposure, compliance violations, or security concerns.

Before you begin monitoring agents in your organization, you must complete the steps provided in [Get started with Insider Risk Management](insider-risk-management-configure). For information about subscriptions, licensing, and permissions, see [Subscriptions and licensing](insider-risk-management-configure#subscriptions-and-licensing) and [Permissions in Insider Risk Management](insider-risk-management-configure#step-1-required-assign-permissions-for-insider-risk-management).

## Risky Agents policy

The Risky Agents (preview) policy provides out-of-the-box coverage for common risk scenarios associated with AI agents. The policy is designed to help surface behaviors that may indicate inappropriate or unsafe agent usage, including situations where agents interact with sensitive data, generate risky outputs, or share information outside organizational boundaries.

By default, the policy detects:

- Risky prompts
- Agents generating sensitive responses
- Agents accessing sensitive data
- Accessing risky websites

These detections help security, compliance, and risk teams gain visibility into how agents are being used and where potential risks may exist.

### Supported agents

The Risky Agents (preview) policy supports the following agent types:

- Copilot Studio agents
- Microsoft Foundry agents
- Agents built using the P4AI SDK

### Default policy availability and behavior

The Risky Agents (preview) policy is available by default to all organizations with supported licenses. When the service is set up, this policy is automatically present and ready to generate alerts based on observed agent activity.

This default configuration enables organizations to:

- Begin monitoring agent activity immediately.
- Gain early visibility into potential agent-related risks.
- Investigate agent behaviors using established Insider Risk Management workflows.

## Customize agent risk monitoring

While the default Risky Agents (preview) policy provides broad coverage for common scenarios, some organizations may require more specific or tailored monitoring.

If the default policy doesn't meet your organizational requirements, you can create a custom Insider Risk Management policy to better align with your risk posture or investigation needs. For more information, see [Create a new policy](insider-risk-management-policies#create-a-new-policy).

## Investigate agent-related alerts

When the Risky Agents (preview) policy detects relevant activity, alerts are generated within Insider Risk Management. These alerts can be reviewed and investigated using the standard alert investigation workflow.

Through alert investigation, analysts can:

- Review details of the detected activity.
- Understand the context of agent behavior.
- Determine whether further action is required.

    Note

    When guest users are interacting with agents, the full prompt and response content isn't available for investigation. Instead, only indicators of sensitive information detected in those prompts and responses are shown.

    Note

    Admins units are currently not supported for agent alerts. If a scoped analyst is signing in, then they can't see agent related alerts.

For detailed guidance on reviewing and managing alerts, see [Triaging alerts](insider-risk-management-activities#triaging-alerts).

## Share agent risk with other Microsoft solutions

Agent risk calculated in Microsoft Purview Insider Risk Management is shared with the following solutions:

- [Data Security Posture Management for AI](data-security-posture-management-get-started)
- [Microsoft 365 admin center](/en-us/microsoft-365/admin/admin-overview/admin-center-overview)