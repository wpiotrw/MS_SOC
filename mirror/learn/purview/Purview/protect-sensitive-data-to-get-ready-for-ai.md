---
layout: Conceptual
title: Protect sensitive data to get ready for AI - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/protect-sensitive-data-to-get-ready-for-ai
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to prepare for AI with Microsoft Purview by discovering sensitive data, reducing exposure, applying protections, and governing AI interactions.
author: cjwoodling6
ms.author: v_cjwoodling
ms.date: 2026-10-23T00:00:00.0000000Z
ms.topic: concept-article
ms.service: purview
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1028
locale: en-us
document_id: 4fb62fcb-31e8-b588-579d-e819a2ab8fac
document_version_independent_id: 4fb62fcb-31e8-b588-579d-e819a2ab8fac
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/protect-sensitive-data-to-get-ready-for-ai.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: protect-sensitive-data-to-get-ready-for-ai
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/protect-sensitive-data-to-get-ready-for-ai.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: b5d43820-c680-62e6-fdf8-281a4b140941
---

# Protect sensitive data to get ready for AI - Microsoft Purview | Microsoft Learn

**Security imperative: Get ready for AI** **Job to be done: Protect sensitive data**

A proactive data protection strategy creates the trusted data foundation organizations need to adopt and scale AI with confidence. By unifying data security and compliance, organizations can understand sensitive data and exposure, apply consistent protections across human and AI interactions, investigate risk, and demonstrate that controls are working.

## Context and problem

AI expands how organizations discover, access, summarize, and act on their data—creating opportunities to improve productivity, decision-making, and innovation. A strong data security foundation helps organizations realize these benefits with confidence by helping provide continuous visibility into sensitive data, access, usage, and protection. It also helps address existing challenges such as oversharing, excessive permissions, inconsistent classification, and protection gaps before they limit AI adoption.

Organizations can accelerate AI adoption by treating data readiness as a continuous operating model rather than a one-time deployment checkpoint. This approach helps ensure that the right people, apps, and agents can access the right data with the right permissions and protections as data, access, and AI usage evolve. Extending the same trusted foundation across supported human activity, AI apps, agents, and models enables organizations to:

- Understand where your sensitive data lives.
- Gain visibility into what data AI can access across apps, browsers, on-premises, file shares and other endpoints.
- Scale classification, policy creation, investigations, and compliance reporting to AI usage.
- Ensure the right permissions and controls are in place to help prevent oversharing.
- Maintain consistent protections as data grows and spreads across systems.
- Proactively identify and remediate issues before they become data security and/or compliance incidents.
- Provide measurable proof of data protection to regulators, auditors, executives, and/or customers.

## Solution

An effective data protection strategy gives organizations a connected, proactive operating model for scaling AI with confidence. It starts with discovering and accurately classifying sensitive data, then connects data, permissions, activity, and protection signals to prioritize the actions that matter most. Organizations can apply controls across supported human and AI interactions, investigate incidents with shared context, govern AI activity according to business and regulatory requirements, and measure improvements in their posture. This continuous loop strengthens readiness as AI adoption expands.

## Guidance

Microsoft Purview is a unified data security and compliance solution that helps organizations discover, protect, and govern data across people, applications, and AI. Purview brings together data context, integrated protection, investigation, and compliance capabilities so organizations can understand where sensitive data and exposure exist, prioritize and take action, govern AI interactions, and continuously strengthen their [data security](https://info.microsoft.com/ww-landing-data-sec-index-2026.html?lcid=en-us) and compliance posture. The guidance below organizes [these capabilities](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Securing-your-data-with-Microsoft-Purview.pdf) into three connected stages for building a trusted data foundation and scaling AI with confidence.

**Phase 1: Understand data readiness and reduce exposure through discovery, classification, and protection**

Start by building a clear, shared view of sensitive data, permissions, protection coverage, and AI activity. Accurate classification helps organizations understand sensitive and overshared content, see who or what can access it, and prioritize the actions that will have the greatest impact on secure AI adoption. This foundation helps enable consistent labeling and protection while helping teams with the context they need to make more informed remediation decisions.

| **Step** | **Recommended action** | **Resource** |
| --- | --- | --- |
| **Understand your data risks** | Microsoft Purview Data Security Posture Management (DSPM) helps identify where sensitive data resides, who can access it, and where exposure exists by prioritizing data that is overshared, broadly accessible, or available to AI applications and agents. DSPM can help assess sensitive data exposure, identify overshared or high-risk content, and understand relationships between sensitive data, users, AI applications, agents, and Copilots. | [Learn about Microsoft Purview Data Security Posture Management (DSPM) | Microsoft Learn](data-security-posture-management-learn-about#how-ai-helps-achieve-data-security-outcomes)<br><br>[Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365 | Microsoft Learn](ai-agent-365#dspm-and-dspm-for-ai-classic) |
| **Discover, classify, and label critical information** | Microsoft Purview Information Protection (MIP) provides classification and labeling capabilities for confidential, regulated, and proprietary information. Using sensitive information types, trainable classifiers, and auto-labeling, coverage doesn't depend on individual user judgment.<br><br>MIP provides the foundation to help ensure data security controls can readily be extended to AI usage. | [Sensitivity labels and AI interactions | Microsoft Learn](ai-microsoft-purview#sensitivity-labels-and-ai-interactions)<br><br>[Data classification and AI interactions | Microsoft Learn](ai-entra-registered#data-classification-and-ai-interactions) |
| **Prevent unauthorized sharing of sensitive data** | Microsoft Purview Data Loss Prevention (DLP) extends sensitive data protections across Microsoft 365, endpoint devices, browsers, networks, Fabric, and Microsoft 365 Copilot. DLP also helps prevent sharing sensitive information with unmanaged AI apps through networks, Microsoft Edge, and cloud apps in Edge for Business. | [Microsoft Purview DLP for Microsoft 365 Copilot and Copilot Chat | Microsoft Learn](dlp-microsoft365-copilot-location-learn-about)<br><br>[Use Network Data Security to help prevent sharing sensitive information with unmanaged AI | Microsoft Learn](dlp-create-policy-ai-network-data-security)<br><br>[Help prevent sharing via Microsoft Edge for Business to unmanaged AI apps from managed devices | Microsoft Learn](dlp-create-policy-block-to-ai-via-edge) |

**Phase 2: Protect sensitive data and investigate risk across human and AI interactions**

With a trusted data foundation in place, organizations can apply controls that support appropriate use and sharing across supported human and AI interactions. When risk is detected, connected sensitivity, identity, activity, and policy context helps security and compliance teams quickly understand what happened, determine which data is affected, prioritize by business impact, and coordinate the right response across workloads.

| **Step** | **Recommended action** | **Resource** |
| --- | --- | --- |
| **Detect, investigate, and mitigate internal risks** | Microsoft Purview Insider Risk Management (IRM) helps identify and mitigate potential risks across user and agent activities. It can surface scenarios such as prompt injection attacks, access to protected materials, intellectual property theft, data leakage, and security policy violations—whether the activity is inadvertent or intentional—so teams can investigate and respond before risks become security incidents. | [Monitoring agents with Insider Risk Management | Microsoft Learn](insider-risk-management-monitoring-agents)<br><br>[Risky AI usage template | Microsoft Learn](insider-risk-management-policy-templates#risky-ai-usage) |
| **Investigate data risks within security incidents** | Microsoft Purview integrates with Microsoft Defender XDR to bring data context into security operations. Insider Risk Management and Data Loss Prevention alerts can be correlated with alerts from other Microsoft security solutions such as Microsoft Entra ID, into a single incident. This helps security teams understand what sensitive data is at risk and prioritize incidents by business impact. | [Investigate insider risk threats in the Microsoft Defender portal](/en-us/defender-xdr/irm-investigate-alerts-defender)<br><br>[Investigate data loss prevention alerts with Microsoft Defender XDR](/en-us/defender-xdr/dlp-investigate-alerts-defender) |
| **Ensure gen AI interactions meet regulatory compliance and business conduct guidelines** | Microsoft Purview Communication Compliance provides tools to help you detect and manage regulatory compliance and business conduct violations across various communication channels, which include user prompts and responses for AI apps. Communication Compliance can analyze AI prompts and responses to detect inappropriate interactions, sharing confidential information, harassing or threatening language, or adult content entered into generative AI applications. | [Configure a Communication Compliance policy to detect generative AI interactions | Microsoft Learn](communication-compliance-copilot)<br><br>[Detect channel signals with Communication Compliance | Microsoft Learn](communication-compliance-channels) |
| **Search and manage AI activities to support audits and investigations** | Microsoft Purview Audit provides robust tools for searching and managing audit records for various AI activities performed across various Microsoft services by users and admins. Using Audit logs and reports, organizations can understand which user interacted with AI, when the AI interactions took place and where it occurred. | [Auditing and AI interactions | Microsoft Learn](ai-agent-365#auditing-and-ai-interactions)<br><br>[Audit logs for Copilot and AI applications | Microsoft Learn](audit-copilot) |

**Phase 3: Govern AI interactions and demonstrate compliance effectiveness**

As AI use expands, organizations can strengthen confidence by combining preventive controls with a defensible record of AI activity and a repeatable governance model. This includes assessing applicable requirements, observing supported user, administrator, Copilot, and agent activity, detecting policy violations, retaining or deleting AI interaction data according to policy, and preserving relevant evidence for investigations. Together, these capabilities help organizations translate regulatory and business requirements into operational controls, demonstrate that those controls are working, and scale AI with greater consistency and accountability.

| Step | Recommended action | Resource |
| --- | --- | --- |
| **Manage retention and records requirements** | Microsoft Purview Data Lifecycle Management provides tools and capabilities to automatically manage lifecycle of AI apps, user prompts, and responses. By simply applying a single policy to multiple locations, specific locations or specific users, organizations can help ensure appropriate retention policies are applied as per industry standard. | [Data Lifecycle Management and AI interactions](ai-microsoft-purview#data-lifecycle-management-and-ai-interactions)<br><br>[Learn about retention for Copilot and AI apps | Microsoft Learn](retention-policies-copilot)<br><br>[Learn about retention policies & labels to retain or delete | Microsoft Learn](retention?tabs=table-overriden) |
| **Effectively respond to security events, investigations and compliance obligations** | Microsoft Purview eDiscovery provides tools and capability to respond to security, regulatory, and legal inquiries and investigations. Using Microsoft Graph Explorer, eDiscovery can help find and remove sensitive information or inappropriate content included in Copilot and other AI application activities. | [eDiscovery and AI interactions | Microsoft Learn](ai-agent-365#ediscovery-and-ai-interactions)<br><br>[Search for and delete AI application data in eDiscovery | Microsoft Learn](edisc-search-copilot-data) |
| **Ensure business and regulatory requirements are being met** | To help you keep compliant with AI regulations, Microsoft Purview Compliance Manager provides regulatory templates to help you assess, implement, and strengthen your compliance requirements for all generative AI apps. For example, monitoring AI interactions and helping prevent data loss in AI applications. | [Microsoft Purview Compliance Manager assessments for AI regulations | Microsoft Learn](compliance-manager-assessments#assessments-for-ai-regulations) |

## Outcomes

- Accelerate AI adoption with a clearer understanding of sensitive and overshared content, permissions, access, and the risks most likely to affect secure expansion.
- Enable appropriate use and sharing by applying classification, labels, and data loss prevention controls across supported collaboration tools, applications, endpoints, Copilot experiences, and AI interactions.
- Continuously strengthen data security posture by connecting sensitivity, permissions, activity, and policy signals; understanding why exposure exists; prioritizing remediation actions; and measuring improvements in protection coverage and risk indicators over time.

- Demonstrate compliance with defensible evidence by preserving AI activity, policy, retention, investigation, and control-effectiveness records that support audits, regulatory inquiries, legal matters, and executive oversight.

## Key success factors

- Help increase security ROI by using classification and labeling to scale consistent protection, help reduce manual effort, and help prevent sensitive data from being leaked or overshared.
- Scale AI adoption with confidence by establishing protection for sensitive information as a foundation and continuously addressing data exposure as usage expands.
- Maintain consistent protection at scale so teams can collaborate, adopt AI, an expand data use while policies continue to follow sensitive information across supported systems.
- Increase executive confidence with demonstratable policy effectiveness and audit readiness across your organization.

## Summary

The recommended actions can help you secure your data, which is foundational to confidently adopting AI. Microsoft Purview can help you understand your data, protect what is sensitive, investigate data risks, and govern AI interactions.

**By prioritizing data readiness, you can help identify and address protection gaps before AI apps and agents put your data to work.**