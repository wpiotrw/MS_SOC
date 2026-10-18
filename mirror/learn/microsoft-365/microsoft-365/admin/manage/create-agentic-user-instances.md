---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Create agentic user instances on behalf of managers - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/create-agentic-user-instances?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how Global Admins and AI Admins can create agentic user instances from activated agent templates on behalf of managers in the Microsoft 365 admin center.
ai-usage: ai-assisted
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2026-09-23T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-copilot
ms.subservice: agent-management
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- m365copilot
- magic-ai-copilot
- operations-pod
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
search.appverid:
- BCS160
- MET150
- MOE150
locale: en-us
document_id: b516800c-b2d6-5f23-1ae8-1c18ab9d74de
document_version_independent_id: b516800c-b2d6-5f23-1ae8-1c18ab9d74de
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/create-agentic-user-instances.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/create-agentic-user-instances
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/create-agentic-user-instances.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: aa188198-f2ee-4002-942f-9c91fc9f42d5
---

# Create agentic user instances on behalf of managers - Microsoft 365 admin | Microsoft Learn

AI-powered agents are built on templates that your organization can deploy to automate business processes. As a Global Admin or AI Admin, you can create agentic users on behalf of end users directly from the Microsoft 365 admin center, giving your organization full governance and control over agent deployment.

This article walks you through the end-to-end process of creating an agentic user instance from an activated agent.

## Who should read this guide

Global Admins and AI Admins are responsible for activating agents within their Microsoft 365 tenant. End users who manage agentic users might also find this guide useful to understand what their admin configures on their behalf.

## Key concepts

### Roles and responsibilities

| Role | Responsibilities in the instance creation flow |
| --- | --- |
| Global Admin / AI Admin | Activates agents, initiates instance creation, assigns licenses and policies, and governs the deployment on behalf of the organization. |
| Manager | The designated business owner of the instance. Appears as the agentic user's manager in Microsoft Entra ID. The admin creates the instance on their behalf. |
| System (Microsoft 365 admin center, Microsoft Agent 365, and Microsoft Entra) | Provisions the instance identity, validates licenses, enforces governance policies, and maintains a complete audit log of all actions. |

### Key terminology

- **Agent template**: A prebuilt AI agent template published in your tenant. An AI teammate must be activated before instances can be created from it.
- **Instance**: A deployed instance of an agent template, assigned to a specific manager and configured for your organization's needs.
- **Instance creation**: The process of provisioning an instance from an activated agent template. Each instance is a unique, governed entity in your Microsoft Entra directory.
- **Owner**: The person in your organization responsible for the instance. They appear as its manager in the directory and interact with it through Microsoft Teams.

## Before you begin

Ensure the following prerequisites are in place before you start the instance creation flow:

- You're signed in to the Microsoft 365 admin center as a Global Admin or AI Admin.
- The agent template you want to deploy is already activated (published) in your tenant. For more information, see [Activate agents](agent-actions#activate-agents).
- You identified the manager, the person who will be the business owner of this instance.
- Sufficient licenses are available to assign to the new instance.
- You confirmed the manager has an active user account in Microsoft Entra ID.

Note

Agent activation and instance creation are separate, decoupled actions. Your organization can activate an agent when it's technically ready, and then create instances from it at any time when the business is ready. This article covers only the agentic user creation steps.

## Create an agentic user instance

Follow these steps to create an instance, also known as an agentic user, from an activated agent in the Microsoft 365 admin center.

### Step 1: Go to the agent registry

1. In the Microsoft 365 admin center, go to the **Agents** section and open the [Agent Registry](agent-registry). Here you see all agents that are activated for your tenant.
2. Locate the agent you want to use. Agents with a status of **Available** are eligible for instance creation.
3. Select the agent to open its Agent Details flyout panel.

### Step 2: Open the agent details

The [Agent Details](agent-details) panel provides a full overview of the agent, including its description, capabilities, supported scenarios, availability settings, data connections, and security configuration. Review these details to confirm this is the correct agent for your intended use case.

The panel includes several tabs you might want to review before creating an agentic user:

- **Overview**: Summary, description, and key capabilities of the agent.
- **Availability**: Which groups or users have access to this instance.
- **Data & tools**: Data sources and integrations the agent uses.
- **Security**: Permission scopes and compliance settings.

### Step 3: Start the instance creation flow

From the Agent Details flyout, select **Create instance**. This launches the instance creation wizard, a guided multistep experience that takes you through all the required configurations before the instance is provisioned.

## Use the instance creation wizard

The instance creation wizard guides you through four stages to configure and provision the instance.

### Stage 1: Select a manager

Search for and select the person who will be the business owner of this instance. The manager appears as the agentic user's manager in Microsoft Entra ID and interacts with the agent through Microsoft Teams. Only users with valid accounts in your directory can be selected. The admin performs this action on behalf of the manager or end user.

### Stage 2: License validation

The system automatically checks whether the required licenses are available to provision this instance. If a valid license is found, you can proceed. If licenses are insufficient, you see a warning and must resolve the licensing gap before continuing. This step ensures compliance with your organization's subscription and governance policies.

### Stage 3: Instance customization

Configure the instance identity and behavior for this specific instance. This might include the agentic user's display name, organizational placement, and any instance-specific settings supported by the agent. These settings determine how the instance appears to the owner and their team.

### Stage 4: Review and confirm

Review a complete summary of all configuration choices before the instance is created. This includes the selected manager, license assignment, customization settings, and access scope. After you confirm, the system provisions the instance, creating its identity in Microsoft Entra ID, applying the manager attribute, and making it available to the manager in Microsoft Teams.

## What happens after the instance is created

After you confirm in the instance creation wizard, the system automatically performs the following actions:

- An instance identity is provisioned in Microsoft Entra ID, with the selected manager set as the directory manager.
- The required license is assigned to the instance.
- The instance is placed within the organizational structure based on the manager's position.
- The manager can access and interact with their instance through Microsoft Teams.
- All provisioning actions are recorded in the audit log for compliance and traceability.

## Manager experience

After the admin completes the instance creation flow, the manager finds their new instance available in Microsoft Teams. From there, they can begin working with the agent, delegating tasks, and managing its activity, all within the familiar Teams interface.

## Governance, compliance, and auditing

All instance deployments through the Microsoft 365 admin center are governed by Microsoft's enterprise compliance framework. Key governance controls include:

- **License enforcement**: An instance can't be provisioned without a valid, available license.
- **Permission scoping**: Admins control which managers can be assigned and which data sources the agent can access.
- **Audit logging**: Every action in the instance creation flow, including who initiated it, when, and what was configured, is captured in the Microsoft 365 audit log.
- **Microsoft Entra ID integration**: All instances are first-class directory objects, subject to the same identity governance policies as human users.
- **Decoupled activation and instance creation**: Admins can activate AI teammates independently of creating instances, enabling staged rollouts and business-readiness gating.