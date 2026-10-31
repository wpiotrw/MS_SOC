---
layout: Conceptual
title: Learn about Microsoft Purview Data Security Posture Management (DSPM) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: helenachen-microsoft
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.update-cycle: 180-days
ms.date: 2026-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- tier1
- m365copilot
- msec-ai-copilot
description: Learn how Microsoft Purview Data Security Posture helps you manage data security, automate risk detection and remediation, simplify compliance, and gain clear visibility across all environments—empowering your organization to adopt AI securely and confidently.
locale: en-us
document_id: c1d214d9-8cb1-fcce-03b4-24cdf065be55
document_version_independent_id: c1d214d9-8cb1-fcce-03b4-24cdf065be55
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-learn-about.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-learn-about
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-learn-about.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: b97cfe47-e1f3-a748-5635-13fea169b014
---

# Learn about Microsoft Purview Data Security Posture Management (DSPM) | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This documentation is for the **current** version of Data Security Posture Management that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

Most new features will be added to this version only but you can still access the previous versions and their documentation:

- [DSPM for AI (classic)](dspm-for-ai)
- [DSPM (classic)](data-security-posture-management)

Microsoft Purview Data Security Posture Management (DSPM) helps organizations discover, protect, and investigate sensitive data risks across their digital estate. This solution provides unified visibility and control for both traditional applications and AI apps and agents, supporting data governance across Microsoft 365, Azure, Fabric, and integrated third-party SaaS platforms. Monitor, assess, and remediate data risks, regardless of where sensitive data resides.

Instead of focusing on infrastructure or endpoints, Data Security Posture Management centers on the data itself—identifying where it resides, who can access it, how it's used, and whether it’s adequately protected. This is especially important as data becomes more distributed and exposed in today's AI-driven workplaces where data is constantly moving and changing, making it harder to keep track of and control.

Data Security Posture Management continuously scans your environment to identify sensitive data, assess risk, and recommend actions to reduce exposure. It consolidates insights from the Microsoft Purview solutions data loss prevention (DLP), Insider Risk Management, information protection with sensitivity labels, and Data Security Investigations. These insights provide a single view for monitoring data risks, policy coverage, and posture trends. This version of Data Security Posture Management extends coverage to third-party SaaS and IaaS platforms, such as Google Cloud Platform, Snowflake, and Databricks, and integrates with partner solutions such as Varonis, Cyera, BigID, and OneTrust for comprehensive risk insights.

Dedicated dashboards and metrics monitor risks associated with AI apps and agents. AI observability enables you to track agent-specific activities, such as oversharing, exfiltration, and unusual access patterns, across both Microsoft and third-party environments. Enhanced reporting provides advanced filtering and customizable views, supporting granular analysis of sensitive data usage, DLP activity, and posture trends. The dashboards and reports can be tailored to align with your organization’s compliance requirements and operational priorities. Audit logs and activity explorer features help track interactions with AI apps and agents, supporting compliance investigations and incident response. Integrated investigation and forensics tools support rapid incident response and root cause analysis for data security events.

[![Data Security Posture Management with sample data on the initial page, Posture.](media/dspm-posture.png)](media/dspm-posture.png#lightbox)

These insights help uncover shadow data, classify sensitive information, analyze access patterns, and highlight risks. The unified approach replaces the need for multiple solutions and manual audits, answering the four practical questions:

- What data do we have?
- Where is it stored?
- Who can access it?
- How is it protected?

When these questions are addressed, Data Security Posture Management can automate remediation steps, such as removing public sharing links or applying data loss prevention policies, to help prevent incidents before they happen. Investigation, alerting, analytics, and reporting are all integrated, supporting a layered security approach. Key metrics are tracked over time, supporting continuous improvement of your organization’s data security posture.

## Data security objectives

New in this version of Data Security Posture Management, after the initial setup tasks, you see **Data security objectives** displayed as prominent, selectable cards or modules. They're also available in context from the initial **Posture** page. Each security objective represents a specific security goal, such as **Prevent data exposure in Microsoft 365 Copilot and Microsoft Copilot interactions**, **Prevent oversharing of sensitive data**, **Prevent exfiltration to risky locations**, and **Discover sensitive data in your organization**.

[![Data Security Posture Management with sample data on the Objectives page.](media/dspm-objectives.png)](media/dspm-objectives.png#lightbox)

Selecting each one guides you through an end-to-end workflow by grouping together the most relevant Microsoft Purview solutions, such as information protection, data loss prevention (DLP), Insider Risk Management, and eDiscovery. As a result, you can focus on achieving specific data security outcomes rather than navigating separate solutions. Each **Outcome** card displays key metrics, such as the percentage of data covered by policies, number of risky sharing incidents, or improvements over time. This information lets you quickly see your current security posture and track progress as you remediate risks.

Within each outcome, you see suggested prioritized actions, such as applying sensitivity labels, configuring DLP policies, or investigating alerts, all tailored to your organzation's data. You can take action directly from the workflow, such as remediating oversharing, configuring one-click policies, or launching investigations into suspicious activity. Reporting and analytics are also organized by outcome, making it easier to identify and report improvements, compliance, and risk reduction.

The **Prevent exfiltration to risky destinations** objective also supports [proactive AI insights powered by Data Security Investigations](data-security-investigations-investigation#create-an-investigation-from-data-security-posture-management). When enabled, Data Security Investigations automatically creates and refreshes an investigation that continuously analyzes recently exfiltrated sensitive data across five risk categories.

Operational insights are surfaced throughout Data Security Posture Management, including:

- Impact prediction visuals and progress tracking for remediation steps
- Role-based access controls to provide granular access to features and AI content for delegated administration and compliance

### How AI helps achieve data security outcomes

This version of Data Security Posture Management not only secures and governs AI apps and agents, but also uses [Microsoft Security Copilot and AI agents](copilot-in-purview-agents-overview) to help secure and govern your data. This AI integration helps you more quickly identify, protect, and investigate data that resides across cloud, SaaS, on-premises, and AI environments. Data security becomes more adaptive and less reliant on manual intervention. AI analyzes access patterns, sharing behaviors, and policy gaps to surface actionable risks. It can also detect unusual activity, such as excessive sharing or suspicious downloads, and prioritize incidents that seem to need immediate attention.

You're always in control of your data and under your guidance, AI agents can take direct action on detected risks, such as removing public sharing links, applying DLP policies, or revoking permissions. To streamline investigations, AI-driven triage agents review alerts from the DLP and insider risk management solutions, filtering out noise and highlighting the most critical threats. You review, approve, or customize automated actions taken by AI agents, and these actions are always [audited](edisc-search-copilot-data). Use the **View agent activity** options throughout the data security objectives for easy access to the agents' activity.

For example, the [proactive AI insights](data-security-investigations-investigation#enable-proactive-ai-insights-from-dspm) feature uses Data Security Investigations to automatically analyze exfiltrated data and surface risk counts by category on the exfiltration objective card, without requiring manual investigation creation.

These AI capabilities from Data Security Posture Management help ensure that sensitive data is governed, labeled, and monitored, with streamlined management. For more information:

- How AI is used within Data Security Posture Management, see [Application card: Microsoft Purview Data Security Posture Management](data-security-posture-management-application-card)
- For the best experience using Security Copilot prompts, see [Tips for custom Security Copilot prompts in Data Security Posture Management](data-security-posture-management-considerations#tips-for-custom-security-copilot-prompts-in-data-security-posture-management)

## How to use Data Security Posture Management

To get started with Data Security Posture Management, use the [Microsoft Purview portal](purview-portal). You need an account that has appropriate permissions for security and compliance management, such as an account that's a member of the Entra **Compliance Administrator** role, or the **Microsoft Purview Compliance Administrator** role group. Some Data Security Posture Management activities need additional permissions, such as the Data Security Viewer role to use Security Copilot. For more information, see [Permissions for Data Security Posture Management](data-security-posture-management-permissions).

If you're new to Data Security Posture Management, the following steps provide a recommended walkthrough.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **DSPM**.

    Don't confuse this with the previous versions, that are now named **Data Security Posture Management (classic)** and **DSPM for AI (classic)**.
2. With the first-time use of DSPM, you're prompted to accept some initial setup tasks if they're not already turned on for your tenant. Allow a day or so before you start to see data from your tenant that you can take action on.

    In the meantime, watch the Microsoft Mechanics video, [New Data Security Posture Management](https://www.youtube.com/watch?v=NLfoFpFxhrA) for an overview introduction with same sample data to see how you might use the following key pages from DSPM to discover, protect, and investigate sensitive data:

    - **Posture**: The dashboard that lets you immediate interact with Security Copilot with suggested prompts, or work your way down the key posture metrics, top objectives to address based on risk, a snapshot of data use across your data estate, and a 30-day trending graph for your organization's data security posture.
    - **Objectives**: Data security objectives to help you address data security risks that have been identified for your organization, each with a remediation plan that includes one-click policies and recommended actions.
    - **AI observability**: An inventory of all AI apps and agents (including recently released Microsoft Agent 365) with activity in the last 30 days, how many are high risk and the total with sensitive interactions, with a breakdown of individual agents and policies to govern them.
    - **Asset explorer**: Use the **Agent** tab for the [Data Security Posture Agent](copilot-in-purview-posture-agent-get-started), and the **Standard** tab to see a unified view across your organization of unlabeled or classified data by workload, filtered by Microsoft and non-Microsoft locations. Microsoft locations currently include Microsoft 365 only. Non-Microsoft locations are made possible by integration with partner solutions.

    - **Reports**: To help you track sensitive data usage and labeling, policy usage, and risky behavior of users and AI agents.
    - **Setup tasks**: To identify and complete configuration steps independently from the security objectives. They include, in preview, setting up Microsoft Sentinel data lake to integrate with partner solutions for non-Microsoft data sources, such as Google Cloud Platform and Snowflake.
3. Explore the following DSPM pages that aren't directly covered in the video:

    - **Discover** &gt; **Apps and agents**: To view a dashboard of AI apps and their agents that have been used across your organization, although it doesn't include Agent 365 (use the **AI observability** page, instead). For the top 20 most recently used agents, view details about sensitive data that they accessed and how they're protected by policies from Microsoft Purview.
    - **Discover** &gt; **Activity explorer**: To understand activity related to content that contains sensitive information or has sensitivity labels applied. Use the **AI activities** tab to see data specific to AI interactions, such as when a user browsed to a generative AI site, the prompts and responses and if they contained sensitive information, and when a data loss prevention rule was matched during one of these interactions. For more information about these events, see [Activity explorer events in Data Security Posture Management](data-security-posture-management-considerations#activity-explorer-events-in-data-security-posture-management).
    - **Discover** &gt; **Data risk assessments**: To help prevent oversharing of sensitive data in your organization with the default or custom assessments that identify and fix potential data oversharing risks. For more information, see [Prevent oversharing with data risk assessments from Data Security Posture Management](data-security-posture-management-oversharing).
    - **Tasks and actions** &gt; **Remediation actions**: To identify and create automatic policies independently from the initial setup tasks and security objectives. Most of these policies originate from the previous version, DSPM for AI. For more information about them, see:

        - [Default policies for data discovery using Data Security Posture Management for AI](dspm-for-ai-considerations#default-policies-for-data-discovery-using-data-security-posture-management-for-ai)
        - [Default policies from data security to help you protect sensitive data used in generative AI](dspm-for-ai-considerations#default-policies-from-data-security-to-help-you-protect-sensitive-data-used-in-generative-ai)

If you're familiar with the previous versions that are now named DSPM for AI (classic) and DSPM (classic), you might find it helpful to refer to [Find familiar tasks that you did in DSPM for AI or in DSPM](dspm-task-mapping).