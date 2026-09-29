---
layout: Conceptual
title: What is Windows 365 for Agents? | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/agents/introduction-windows-365-for-agents
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Overview of Windows 365 for Agents, a platform where customers can deploy computer-using agents securely and at scale on Cloud PCs.
author: DelzeenMachhi
ms.author: dmachhi
ms.service: windows-365
ms.topic: overview
ms.date: 2026-07-23T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 57f3cb17-b997-9f3e-3e3a-9fd29426dc11
document_version_independent_id: 57f3cb17-b997-9f3e-3e3a-9fd29426dc11
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/agents/introduction-windows-365-for-agents.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agents/introduction-windows-365-for-agents
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/agents/introduction-windows-365-for-agents.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: c9a1f62a-4732-9fd7-dc52-f9ea9cbae61f
---

# What is Windows 365 for Agents? | Microsoft Learn

Windows 365 for Agents provides a brand-new class of Cloud PCs for agent use, built on top of the same Windows 365 platform that powers Windows 365 for Enterprise and Business. At the heart of the platform is the Cloud PC, a virtual Windows desktop hosted in the Microsoft Cloud.

To efficiently manage and allocate these resources, you create provisioning policies for Cloud PCs for Agents. Provisioning policies (agents) allow organizations and partners to group Cloud PCs for Agents for different teams or workloads, which ensures consistent Microsoft Intune policy enforcement and cost control.

Agents interact with Cloud PCs by using a check-out/check-in model. When an agent needs to perform a task, it checks out a Cloud PC. After the task is complete, the agent checks the Cloud PC back in, making it available for others. This approach maximizes resource efficiency and keeps costs predictable.

There are other versions available for Windows 365. For more information, see [What is Windows 365?](/en-us/windows-365/overview).

## Platform capabilities

Windows 365 for Agents enables agent makers to:

- **Provision secure Cloud PCs**: Instantly create and manage domain-joined, Intune-managed Cloud PCs governed by Microsoft Entra ID, which ensures agents operate within enterprise security and compliance boundaries.
- **Orchestrate agent sessions through APIs**: Automate lifecycle management - provisioning, session control, and UI automation - by using standardized platform APIs without handling underlying Cloud PC infrastructure.
- **Monitor and intervene in real time**: Access session logs, observability tools, and human-in-the-loop controls for debugging, trust, and operational reliability.

## AI solutions powered by Windows 365 for Agents

Windows 365 for Agents is the trusted platform for secure, scalable agentic compute, which enables enterprise-grade automation and integration across the Microsoft ecosystem.

- **Copilot Studio computer use**: Empowers custom Copilot agents to automate web tasks right from a prompt in a secure Cloud PC environment. For more information, see [Use a Cloud PC pool for computer use runs (preview)](/en-us/microsoft-copilot-studio/use-cloud-pc-pool).
- **Project Opal in Microsoft Copilot**: Orchestrates dynamic agent workflows for task-based automation in secure and managed Cloud PCs. For more information, see [Set up and manage Project Opal (Frontier)](https://go.microsoft.com/fwlink/?linkid=2339568).
- **Researcher Computer Use in Microsoft Copilot**: Delivers multi-step website navigation and action automation by using agent-driven sessions on Linux Cloud PCs. For more information, see [Researcher agent computer use FAQ](/en-us/copilot/microsoft-365/researcher-agent-computer-use-faq).
- **Agent 365**: Lets customers access publicly available agents or build their own. Along with WorkIQ tools, Windows 365 for Agents can be integrated into Agent 365 agents. For more information, see [Microsoft Agent 365](https://www.microsoft.com/microsoft-agent-365).

## Device management

Cloud PCs for Agents are managed through the Microsoft Intune admin center.

For Agent 365, to set up Windows 365 for Agents you [create a provisioning policy (agents)](create-provisioning-policy-agents). From an admin perspective, management is pool-based rather than device-based. This model is implemented through [Cloud PC agent pools](cloud-pc-agent-pools).

For other supported agent solution partners, such as Microsoft Copilot Studio computer use, Project Opal, and Researcher, you can create Cloud PC agent pools in their portals, and no setup is required in Intune.

After provisioning, you can use Intune to [manage and monitor](device-management-cloud-pcs-agents) Cloud PCs for Agents. To learn how agents can check out these Cloud PCs, see [Agent session lifecycle](agent-session-lifecycle).