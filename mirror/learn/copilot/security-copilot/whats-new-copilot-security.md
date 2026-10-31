---
layout: Conceptual
title: What's new in Microsoft Security Copilot? | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn what's new in Microsoft Security Copilot such as the latest release notes, and enhancements to capabilities, features, and experiences.
ms.date: 2026-04-17T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
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
document_id: fc98fbf2-2631-3a77-df79-b1cc98af9b98
document_version_independent_id: fc98fbf2-2631-3a77-df79-b1cc98af9b98
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/whats-new-copilot-security.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: whats-new-copilot-security
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/whats-new-copilot-security.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 98ae0039-c6f3-6497-789a-b133b6b64e7d
---

# What's new in Microsoft Security Copilot? | Microsoft Learn

Security Copilot receives improvements on an ongoing basis. To stay up to date with the most recent developments, this article provides you with information about:

- The latest releases
- Known issues
- Plans for changes

Each item describes where the enhancement can be experienced. For more information, see [Security Copilot experiences](experiences-security-copilot).

This page updates monthly, so revisit it regularly.

## April 2026

### Security Analyst Agent - Public preview

**Type:** New feature **Experience:** Standalone / Embedded 

The Security Analyst Agent in Security Copilot helps security analysts quickly identify, assess, and prioritize risks. The agent performs deep, multi-step investigations across Microsoft Defender and Microsoft Sentinel telemetry to surface high-impact risks and deliver prioritized insights. Each finding includes clear reasoning and supporting evidence, enabling analysts to quickly understand and act on the results.

Key capabilities include:

- **Flexible analysis**: Perform ready-to-use or custom analyses on security data. Get actionable and prioritized insights, recommendations, and reports to uncover top vulnerabilities and risks.
- **Data integration**: Analyze data from Microsoft Defender XDR, Sentinel Log Analytics, or Sentinel Data Lake, based on your instructions.
- **Interactive exploration**: Visualize data to spot anomalies and risks faster.
- **Conversation assistance**: Chat with the agent, ask follow-up questions, and perform related analyses to deepen your understanding.

The agent can perform single or multi-step analysis on large volumes of data, iteratively reasoning to uncover hidden risks and prioritizing findings with a detailed evidence trail, without the need to write any code or queries.

For more information, see [Security Analyst Agent](/en-us/copilot/security/security-analyst-agent).

## November 2025

### Microsoft Security Copilot for Microsoft 365 E5 customers

**Type:** New capability **Experience:** Standalone / Embedded 

Microsoft Security Copilot is included for all Microsoft 365 E5 customers. Expanded agent portfolio: 40 new Microsoft and partner-built agents added. 12 new Microsoft-built agents across Microsoft Defender, Entra, Intune, and Purview are available today in preview. Additionally, more than 30 new partner-built agents extend protection end-to-end. These agents automate large-scale tasks, which allows security teams to dedicate more time to strategic initiatives.

Existing Security Copilot customers with Microsoft 365 E5 subscriptions can get started with the agents:

- Security operations in [Microsoft Defender](/en-us/defender-xdr/security-copilot-in-microsoft-365-defender)
- Data security in [Microsoft Purview](/en-us/purview/copilot-in-purview-overview)
- Identity and access in [Microsoft Entra](/en-us/entra/security-copilot/security-copilot-in-entra)
- Endpoint management in [Microsoft Intune](/en-us/intune/copilot/)

To learn more on what's included for E5 customers, see [Security Copilot inclusion](/en-us/copilot/security/security-copilot-inclusion).

## September 2025

### Microsoft Sentinel and Security Copilot integration - General availability

**Type:** New feature **Experience:** Embedded 

Microsoft Sentinel data lake is now generally available. New capabilities such as Microsoft Sentinel graph and the Model Context Protocol (MCP) server are in public preview. This integration with Security Copilot lets agents access connected data across Sentinel, combining graph, structured, and semantic context to reason and act with greater precision. This foundation enhances AI-driven detection and response, helping your teams resolve incidents faster and uncover deeper insights across your environments.

For more information, see [Microsoft Sentinel platform](/en-us/azure/sentinel/datalake/sentinel-lake-onboarding).

### Build your own Security Copilot agent - Public preview

**Type:** New feature **Experience:** Standalone 

You can create custom Security Copilot agents. Use the standalone agent builder (no-code experience) or use developer tools to design, test, and deploy agents that automate the workflows you need most. Your team controls how the agents work and what they do.

For more information on building custom agents using the agent builder, see [Agents in standalone](/en-us/copilot/security/developer/agent-standalone-overview).

For information on building agents using MCP, see [MCP overview](/en-us/copilot/security/developer/mcp-overview).

### Microsoft and partner agents - Public preview

**Type:** New capability **Experience:** Standalone / Embedded 

These new agents help teams address common security and IT challenges faster and smarter:

- **Access Review Agent in Microsoft Entra**: Streamline access reviews, flag unusual patterns, and reduce fatigue for security and compliance teams. It helps maintain governance and compliance by automatically analyzing ongoing access reviews and highlighting potential risks.

    For more information, see [Access Review Agent](/en-us/entra/id-governance/access-review-agent).
- **Phishing Triage Agent in Microsoft Defender**: In this new customer spotlight, St. Luke is seeing the impact of integrating Security Copilot agents into their daily workflows saving nearly 200 hours a month. With routine triage automated, security teams can shift from reactive response to proactive threat hunting, freeing up time for higher-value work and faster threat mitigation.

    For more information, see [Customer Success](https://www.microsoft.com/en/customers/story/25330-st-lukes-university-health-network-microsoft-security-copilot).

About 30 new partner-built agents are now available in the Microsoft Security Store. These agents deliver solutions such as:

- **Forensic Agent by glueckkanja AG**: Delivers deep-dive analysis of Defender Extended Detection and Response (XDR) incidents to accelerate investigations and uncover root causes faster.
- **Privileged Admin Watchdog Agent by glueckkanja AG**: Helps enforce zero standing privilege principles by removing persistent admin identities, reducing risk, and strengthening administrative security.
- **Ransomware Kill Chain Investigator Agent by adaQuest**: Automates ransomware triage to quickly detect and respond to threats, enabling security teams to focus on high-priority incidents.
- **Entity Guard Investigator Agent by adaQuest**: Investigates Defender incidents and provides actionable insights to accelerate incident resolution and strengthen security posture.
- **Admin Guard Insight Agent by adaQuest**: Analyzes administrative activity, detects anomalies, evaluates risk exposure and compliance, and delivers actionable guidance to improve administrative security.
- **Identity Workload ID Agent by Invoke**: Empowers identity administrators and security teams to manage and secure Workload Identities in Microsoft Entra, reducing risk, strengthening compliance, and controlling identity sprawl.

Learn about these agents and more in the [Microsoft Security Store](https://securitystore.microsoft.com/).

### Microsoft Security Store - Public preview

**Type:** New feature **Experience:** Standalone 

The Microsoft Security Store makes it simple to discover, deploy, and buy Security Copilot agents and partner solutions. You can use any of the 30 new agents or 50 SaaS solutions to power your SOC, IT, privacy, and compliance workflows.

For more information, see [Security Store](/en-us/security/store/what-is-security-store).

## July 2025

### Copilot in Microsoft Intune – General availability

**Type:** Changed **Experience:** Embedded 

IT admins can now use Security Copilot in Intune, which includes a dedicated data exploration experience, allowing them to ask questions, extract insights, and take action—all from within the Intune admin center. Whether it’s identifying noncompliant devices, managing updates, or automating remediation, Copilot simplifies complex workflows and brings data and actions together in one place.

For more information, see [Microsoft Copilot in Intune](/en-us/intune/intune-service/copilot/copilot-intune-overview)

### Copilot in Microsoft Entra – General availability

**Type:** Changed **Experience:** Embedded 

Security Copilot in Microsoft Entra now brings AI-assisted investigation and identity management directly into the Microsoft Entra admin center. Admins can ask natural language questions to troubleshoot sign-ins, review access, monitor tenant health, and analyze role assignments—without writing queries or switching tools. With expanded coverage and improved performance, Copilot helps teams move faster, close gaps, and stay ahead of threats.

For more information, see [Microsoft Copilot in Microsoft Entra](/en-us/entra/fundamentals/copilot-security-entra).

### Conditional Access Optimization Agent – General availability

**Type:** Changed **Experience:** Embedded 

The Conditional Access Optimization Agent in Microsoft Entra brings AI-powered automation to identity workflows. The agent runs autonomously to detect gaps, overlaps, and outdated policy assignments—then recommends precise, one-click remediations to close them fast. Key benefits include:

- Autonomous protection: Automatically identifies users and apps not covered by policies
- Explainable decisions: Plain-language summaries and visual activity maps
- Custom adaptability: Learns from natural-language feedback and supports business rules
- Full auditability: All actions logged for compliance and transparency

For more information, see [Microsoft Entra Conditional Access optimization agent with Microsoft Security Copilot](/en-us/entra/identity/conditional-access/agent-optimization).

### Phishing Triage Agent in Microsoft Defender - Public preview

**Type:** New capability **Experience:** Embedded 

The Phishing Triage Agent in Microsoft Defender is now in public preview, bringing autonomous, AI-powered threat detection to your SOC workflows. Powered by large language models, the agent performs deep semantic analysis of emails, URLs, and files to determine whether a submission is a phishing threat or a false alarm—without relying on static rules.

It learns from analyst feedback, adapts to your organization’s patterns, and provides clear, natural language explanations for every verdict. A visual decision map shows exactly how the agent reached its conclusion, making the process fully transparent and reviewable.

For more information, see [Phishing Triage Agent](/en-us/defender-xdr/phishing-triage-agent).

### Threat Intelligence Briefing Agent is now - Public Preview

**Type:** New capability **Experience:** Standalone 

The Threat Intelligence Briefing agent has entered public preview in the Security Copilot standalone experience, transforming how security teams stay ahead of emerging threats. With this powerful agent, creating highly relevant, organization-specific threat intelligence briefings now takes minutes rather than hours or days, empowering teams to act with speed and confidence. Through real-time dynamic reasoning, the agent surfaces the most relevant threat intelligence based on attributes such as the organization's industry, geographic location, and unique attack surface to deliver critical context and invaluable situational awareness.

For more information, see [Threat Intelligence Briefing Agent](/en-us/copilot/security/threat-intel-briefing-agent).

### Security Copilot Capacity Calculator

The Security Copilot Capacity Calculator is now available in the standalone experience (Azure account required), helping teams estimate how many SCUs they may need. Security Copilot supports:

- Provisioned SCUs for predictable workloads
- Overage SCUs to scale with variable workloads

Teams can estimate initial capacity using the capacity calculator, monitor usage in the in-product usage dashboard, and adjust their SCU allocation as needed. Learn more about [Security Copilot pricing here](https://azure.microsoft.com/pricing/details/microsoft-security-copilot/).

Learn more: [New tools for Security Copilot management and capacity planning](https://techcommunity.microsoft.com/blog/securitycopilotblog/new-tools-for-security-copilot-management-and-capacity-planning/4432723).

### Audit agent changes with Purview Unified Audit Log (UAL) integration - General availability

**Type:** New capability **Experience:** Embedded 

Agent administration auditing is now generally available in Microsoft Purview Unified Audit Log, allowing teams to trace agent creation, updates, and deletions with detailed metadata for improved visibility and compliance.

For more information, see [Access the Security Copilot audit log](/en-us/copilot/security/audit-log).

### GPT 4.1 support - General availability

**Type:** Changed **Experience:** Standalone / Embedded 

GPT 4.1 Support is now generally available for all experiences at evaluation level in Security Copilot. With GPT-4.1 support, Security Copilot can now offer significantly larger context windows with better interactions and have observed accuracy increased.

### Large output support - General availability

**Type:** Changed **Experience:** Standalone / Embedded 

Large output support is now generally available for all experiences. With this capability, Security Copilot can now support over 2MB of data for usage in LLM with restrictions only on OpenAI token limits.

### Agent administration auditing - General availability

**Type:** Changed **Experience:** Standalone / Embedded 

Agent administration auditing is now generally available for Microsoft Purview Unified Audit Log. Agent administration actions whether creating, updating, or deleting agents and triggers are entered into the unified audit log as unique events. Each event type includes metadata pertaining to the agent, tenant, and user of the activation event providing admins the ability to trace changes across complex agent environments.

### Dynamic suggested prompts for Microsoft Entra skills

**Type:** Changed **Experience:** Standalone / Embedded 

Dynamic suggested prompts are now generally available for Microsoft Entra skills, offering faster and more deterministic follow-up suggestions using direct skill invocation—bypassing the orchestrator for improved performance.

### FedRAMP High authorization for Security Copilot

Security Copilot is now included within the [Federal Risk and Authorization Management Program (FedRAMP)](https://www.fedramp.gov/) High Authorization for [Azure Commercial](/en-us/azure/security/fundamentals/feature-availability#microsoft-365-integration). This Provisional Authorization to Operate (P-ATO) within the existing FedRAMP High Azure Commercial environment was approved by the FedRAMP Joint Authorization Board (JAB). This milestone marks a significant step forward in our mission to bring Microsoft Security Copilot’s cutting-edge AI-powered security capabilities to our [Government Community Cloud (GCC)](/en-us/office365/servicedescriptions/office-365-platform-service-description/office-365-us-government/gcc) customers. Stay tuned for updates on when Security Copilot will be fully available for GCC customers.

## June 2025

### Workspace level plugin management - General availability

**Type:** Changed **Experience:** Standalone 

Security Copilot now supports workspaces, giving organizations a flexible way to segment environments by team, region, or business unit. With workspaces now in public preview, admins can align access, data boundaries, and SCU capacity with operational and compliance needs. Each workspace supports role-based access control, localized prompt history, and independent capacity planning – making it easier to manage complex, distributed security and IT operations.

As part of this model, workspace-level plugin management is now generally available, allowing admins to configure plugin settings at the workspace or organization level. This eliminates the need for per-user setup and improves efficiency across large environments.

### Microsoft Entra embedded experience powered by the NL2API skill - General availability

**Type:** New capability **Experience:** Embedded 

Enables Security Copilot to perform advanced reasoning over APIs (MS Graph APIs) and answer complex, multi-stage questions across Microsoft Entra resources.

### Korean language

**Type:** Changed **Experience:** Standalone 

Korean language is now supported in security copilot standalone and embedded experiences.

For more information, see [Supported languages](/en-us/copilot/security/supported-languages).

### Swiss region data residency

**Type:** Changed **Experience:** Standalone 

Swiss region data residency is now available enabling storage of Security Copilot data within Switzerland boundary.

For more information, see [Availability and recovery](/en-us/copilot/security/copilot-security-availability-recovery#availability-zones).

## May 2025

### Censys - Public preview

**Type:** New capability **Experience:** Standalone 

This plugin allows Security Copilot users to enrich investigations using threat intelligence from the Censys Platform.

For more information, see [Censys](plugin-censys)

### HP Workforce Experience Platform - Public preview

**Type:** New capability **Experience:** Standalone 

Allows users to query data about their fleet and get responses back quickly and efficiently. This plugin can answer questions about PC warranty, Windows 11 readiness, resource consumption. It can also answer device age/stability/health, security, blue screens, and app performance including hangs and crashes.

For more information, see [HP Workforce Experience Platform](plugin-hp-wxp)

### Copilot Studio connector - General Availability

**Type:** New capability **Experience:** Standalone 

This connector helps users submit natural language prompts to create a new Security Copilot investigation through Copilot Studio. After completion, the evaluation result is returned to the workflow.

For more information, see [Copilot Studio connector](connector-copilot-studio).

## April 2025

### Overage SCUs - General Availability

**Type:** New capability **Experience:** Standalone 

Customers can set an overage amount of SCUs to ensure that additional SCUs are available when initially provisioned units are depleted during unexpected workload spikes. Overage units are billed on-demand and can be set as unlimited or a maximum amount.

For more information, see [Manage usage](manage-usage).

### Splunk - Public preview

**Type:** New feature **Experience:** Standalone 

The Splunk plugin enables customers to perform searches in Splunk, retrieve alerts, and others.

For more information, see [Splunk](plugin-splunk).

### Microsoft Threat Intelligence recommended actions - General Availability

**Type:** Changed **Experience:** Standalone 

When investigating a vulnerability or attack utilizing an exploit, it's critical to understand the recommended actions for mitigation. This information is now available through the Microsoft Threat Intelligence plugin.

### Microsoft Threat Intelligence - Malware encyclopedia integration - Public preview

**Type:** New capability **Experience:** Standalone 

When investigating an incident involving a malware it's critical to quickly get the information about this malware, relevant Defender for Endpoint version and guidance for next steps. This capability allows customers to query this information directly in Security Copilot.

### Microsoft Threat Intelligence - Reason for inclusion - General Availability

**Type:** New capability **Experience:** Standalone 

When the analyst receives a response with multiple results – such as multiple actors or attacks, multiple articles, and others, it's sometimes difficult to understand which result is the most relevant for the next level of drill-down. With this enhancement it's easier to understand the relevance of each result.

### Microsoft Threat Intelligence - Suggested prompts - General Availability

**Type:** New capability **Experience:** Standalone 

During a session in Security Copilot customers often need help selecting the next prompt for their investigation. This is a critical part of a guided experience.

### Microsoft Threat Intelligence - Indicator skills - General Availability

**Type:** New capability **Experience:** Standalone 

Microsoft Threat Intelligence indicator skills allow direct access to all suspicious IOC and the mass datasets of web scan data including DNS, WHOIS, host pairs, certificates, detonation data, and others.

## March 2025

### Global Copilot experience - Public preview

**Type:** New feature **Experience:** Embedded 

The Global Copilot experience is a new global entry point in the Suite Header on the Microsoft Purview compliance portal home page and all solution pages. This capability allows for easy invocation of the Copilot experience. For each page, Copilot offers readily available prompts for you to get started, learn more about Purview, and troubleshoot issues.

For more information, see [Security Copilot in Microsoft Purview](/en-us/purview/copilot-in-purview-overview).

### Microsoft Surface Management integration - Public preview

**Type:** New feature **Experience:** Embedded 

With Copilot in Intune, IT Admins can quickly search for and resolve specific device issues, summarize warranty information, and access support tickets and service orders related to their organization’s Surface devices. This reduces the time and effort needed for routine maintenance tasks, creating more time to focus on other initiatives. In addition, Copilot pulls contextually relevant data from your Intune-enrolled Surface devices along with public information into a single view, streamlining the management process and enhancing overall efficiency.

For more information, see [Security Copilot in Microsoft Surface Management Portal](/en-us/mem/intune/copilot/security-copilot-surface-portal).

### CheckPhish - General Availability

**Type:** New feature **Experience:** Standalone 

This plugin allows users to utilize the CheckPhish AI to analyze URLs for potential phishing threats, tech support scams, cryptojacking, and other security risks.

For more information, see [CheckPhish](plugin-checkphish).

### Plugin management - General Availability

**Type:** New feature **Experience:** Standalone 

You can personalize the way Security Copilot interacts with you by managing plugins.

For more information, see [Manage plugins](manage-plugins).

### KQL response explanation feature in Query assistant - General Availability

**Type:** New feature **Experience:** Standalone / Embedded 

The Security Copilot Query Assistant in Advanced hunting generates KQL queries from user requests in natural language, allowing junior and first-tier analysts that aren't familiar with KQL to easily hunt for threats. With this new feature, customers can see the logic behind the KQL queries generated by Copilot, including a breakdown of the query. This enhancement helps customers validate that the query aligns with their intent and needs, even if they don't have a deep understanding of KQL. Additionally, this feature helps customers improve their knowledge and proficiency in KQL, and will also increase their trust in the Query Assistant.

For more information, see [Microsoft Security Copilot in advanced hunting](/en-us/defender-xdr/advanced-hunting-security-copilot).

### Set prompts to continue on failure - General Availability

**Type:** New feature **Experience:** Standalone 

The **Continue on failure** feature is now available in Security Copilot promptbooks. This feature allows users to set a promptbook to continue running the next prompt even after a prompt fails, instead of halting the entire promptbook.

For more information, see [Set prompts to continue on failure](build-promptbooks#set-prompts-to-continue-on-failure).

### Call system capabilities directly - Public preview

**Type:** New feature **Experience:** Standalone 

You can now directly call a Security Copilot system capability during promptbook creation. System capabilities are the various actions that Security Copilot can perform for you. This feature allows you to generate responses more efficiently and might help lower SCU consumption.

For more information, see [Call capabilities directly in the prompt](build-promptbooks#call-system-capabilities-in-the-prompt-preview).