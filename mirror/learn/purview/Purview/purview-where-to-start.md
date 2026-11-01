---
layout: Conceptual
title: Get Started Understanding and Using Microsoft Purview solutions work together | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-where-to-start
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how Microsoft Purview data security, data governance, and data compliance solutions work together to protect, govern, and manage your organization's data in the era of AI.
keywords: Microsoft Purview, data security, data governance, data compliance, AI, solutions
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
audience: ITPro
ms.topic: concept-article
ms.service: purview
search.appverid:
- MET150
ms.collection:
- purview-compliance
- essentials-compliance
- essentials-overview
ai-usage: ai-generated
ms.date: 2026-06-16T00:00:00.0000000Z
locale: en-us
document_id: ad257e4f-40c6-4cd3-c26a-f4bf0f7500b8
document_version_independent_id: ad257e4f-40c6-4cd3-c26a-f4bf0f7500b8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-where-to-start.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-where-to-start
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-where-to-start.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 97660444-98dd-5c7d-5f5d-8def87c461c4
---

# Get Started Understanding and Using Microsoft Purview solutions work together | Microsoft Learn

Microsoft Purview brings together [data security](purview-security), [data governance](data-governance-overview), and [data compliance](purview-compliance) solutions in a [unified platform, the Microsoft Purview portal](purview-portal). These solutions share capabilities, exchange signals, and reinforce each other to give your organization comprehensive visibility and control over its data.

But with its breadth of solutions and capabilities, it can be hard to know where to begin with Purview. There's no single path that works for every organization because priorities differ based on your industry, regulatory requirements, and how far along you are in your AI adoption. However, most organizations follow a similar progression:

![Steps for getting started with Microsoft Purview.](media/purview-get-started-steps.png)

1. **Discover and understand your data**: Find out what data you have, where it lives, and how much of it is sensitive.
2. **Protect your sensitive data**: Apply labels, encryption, and policies to prevent data loss.
3. **Govern your data estate**: Catalog your assets, ensure data quality, and establish accountability.
4. **Control access and user behavior**: Make sure users can only reach the data they need and that they interact with it safely.
5. **Secure AI interactions**: Extend your protections and compliance controls to Copilot, agents, and other AI apps.

This article walks through each stage and explains which Purview solutions apply, how they connect, and where to start.

Tip

Before you begin configuring solutions, make sure the right people in your organization have the [roles and permissions](purview-permissions) they need. Most exploration tasks, like viewing Data Security Posture Management dashboards, require only reader roles.

## Discover and understand your data

Before you can protect or govern anything, you need to know what data you have and identify which data is sensitive. Discovery is the foundation for every other stage, and Purview provides several ways to build that picture.

### Assess your data security posture

[Data Security Posture Management (DSPM)](data-security-posture-management-learn-about) brings together signals from across Purview to give you a unified view of sensitive data risks. DSPM helps you discover where sensitive data lives, identify oversharing risks, and get personalized recommendations for remediation. If your organization uses AI apps, DSPM provides extra visibility into how AI interacts with your data.

DSPM is a good starting point if you want a single dashboard that shows what needs attention first.

### Classify sensitive data

[Sensitive information types](sensitive-information-type-learn-about) and [trainable classifiers](classifier-learn-about) identify sensitive items across your Microsoft 365 environment by using pattern matching, machine learning, or examples of data you provide. These classifiers are *shared* across Purview, so a sensitive information type you configure here is also available to Data Loss Prevention policies, Insider Risk Management, Communication Compliance, and data classification reports.

[Data classification](data-classification-overview) provides dashboards and explorers that show how data is classified and used across your organization. Use [activity explorer](data-classification-activity-explorer) to see how users interact with sensitive data, including labeling activity and AI interactions.

To learn more, see [Get started with data classification](data-classification-overview).

### Scan and catalog data assets

[Data Map](data-map) scans your data sources and multicloud environments to capture metadata about your data assets. This process creates a comprehensive inventory that spans your entire data estate and feeds the [Unified Catalog](unified-catalog), where data owners and stewards curate data products and data consumers discover trusted datasets. Data Map and Purview share data to support various shared capabilities, as detailed in [How data flows in Microsoft Purview](purview-data-flows).

To learn more, see [Plan for data governance](data-governance-plan).

## Protect your sensitive data

After you understand what sensitive data you have and where it lives, the next step is to apply protections. Purview data security solutions work together to protect data throughout its lifecycle.

### Apply sensitivity labels

[Sensitivity labels](sensitivity-labels) are the foundational protection mechanism in Purview. Labels provide visibility into the sensitivity of data and can apply encryption, access restrictions, and visual markings. When you apply a label to a document or email, the protection travels with the content wherever it goes - across services, devices, and into AI interactions.

Many solutions use sensitivity labels. Data Loss Prevention enforces them, AI apps honor them, Microsoft Purview Audit logs capture them, Microsoft Purview eDiscovery makes them searchable, and DSPM makes them visible. When you define and apply your labels, you build the foundation for protections that extend across the entire platform.

To learn more, see [Get started with sensitivity labels](get-started-with-sensitivity-labels).

### Prevent data loss

[Data Loss Prevention (DLP)](dlp-learn-about-dlp) policies monitor for sensitive information across Microsoft 365 services and endpoints. In a DLP policy, you define the sensitive information to monitor, the locations to monitor, the conditions that must be matched, and the actions to take when a match is found. DLP uses the same classifiers and sensitivity labels that other solutions rely on, so your protection policies are consistent across the platform.

To learn more, see [Learn about data loss prevention](dlp-learn-about-dlp).

### Manage data retention and deletion

[Data Lifecycle Management](data-lifecycle-management) provides retention and deletion policies that help you keep content you need and delete content you don't. Retaining data often addresses compliance and regulatory requirements. Deleting data that no longer has business value reduces your exposure to cyberattacks and data breaches. These policies apply across Exchange, SharePoint, OneDrive, Teams, and other Microsoft 365 services.

To learn more, see [Get started with data lifecycle management](get-started-with-data-lifecycle-management).

## Govern your data estate

With sensitive data protected, your organization can focus on making sure all data is well-organized, trustworthy, and accessible to the right people. Purview [data governance solutions](data-governance-overview) help your organization establish a federated governance model where a central data office sets the rules and domain experts manage the data they know best.

### Curate data in Unified Catalog

[Unified Catalog](unified-catalog) is a searchable catalog powered by the metadata captured in [Data Map](data-map). Data owners and stewards use it to curate data products, manage data quality, and grant access to data consumers. Data consumers discover trusted datasets through a self-service experience with natural language search.

Governance domains organize data products and business concepts to make data easier to find and use. Built-in data quality capabilities help data owners measure and improve the health of their data, which is especially important in the era of AI because AI systems that ingest trusted, high-quality data produce more accurate and reliable results.

### How governance supports security and compliance

Governance and security complement each other. Data governance helps you understand *what* data you have and *where* it lives. Data security helps you *protect* that data. For example, when Data Map identifies sensitive data sources, your security team can prioritize applying sensitivity labels and DLP policies to those sources.

Governance also supports compliance. Data lineage capabilities in Unified Catalog help you see the relationships between data products and their sources, which is useful for responding to regulatory inquiries and demonstrating compliance.

To learn more, see [Plan for data governance](data-governance-plan) and [Get started with data governance](data-governance-get-started).

## Control access and user behavior

Protecting data and governing data assets addresses the data itself. But you also need to make sure that *people* interact with data in safe, secure, and compliant ways. Purview provides several solutions that monitor user behavior, enforce access boundaries, and help you respond to incidents.

### Detect and act on insider risks

[Insider Risk Management](insider-risk-management-solution-overview) identifies potentially risky user activities by correlating signals from Microsoft 365 and third-party sources. It can detect behaviors such as unusual data downloads, sensitive data sharing, and risky AI usage patterns. Insights from insider risk signals are integrated into Microsoft Defender XDR for a comprehensive view of security threats.

To learn more, see [Learn about insider risk management](insider-risk-management).

### Restrict communication and collaboration

[Information Barriers](information-barriers) restrict two-way communication and collaboration between groups and users in Teams, SharePoint, and OneDrive. Often used in highly regulated industries, Microsoft Purview Information Barriers help avoid conflicts of interest and safeguard internal information between users and organizational areas.

To learn more, see [Learn about information barriers](information-barriers).

### Limit privileged access

[Privileged Access Management](privileged-access-management-solution-overview) helps protect your organization by limiting standing access to sensitive data or critical configuration settings. Instead of administrators having constant access, just-in-time access rules are implemented for tasks that need elevated permissions.

To learn more, see [Learn about privileged access management](privileged-access-management).

### Monitor organizational activity

[Audit](audit-solutions-overview) captures, records, and retains user and admin activities across Microsoft 365 services. Audit logs are essential for security investigations, compliance obligations, and forensic analysis. Audit records include AI interactions, such as user prompts and responses with Copilot and other AI apps.

To learn more, see [Get started with auditing solutions](audit-get-started).

### Detect inappropriate communications

[Communication Compliance](communication-compliance-solution-overview) monitors email and Teams communications for regulatory violations, harassment, threats, and inappropriate sharing of sensitive information. You can also set policies to monitor interactions with generative AI apps.

For more information, see [Learn about communication compliance](communication-compliance).

### Investigate data security incidents

[Data Security Investigations](data-security-investigations) uses generative AI to help your security team analyze and respond to data security incidents, identify risks from sensitive data exposure, and collaborate more effectively on remediation.

### Meet regulatory requirements

[Compliance Manager](compliance-manager) helps your organization assess its compliance posture against more than 360 industry and regional regulatory standards. It provides risk-based scoring, improvement actions, and prebuilt assessment templates, including templates for AI regulations.

[eDiscovery](edisc) helps your organization identify, collect, preserve, and export electronic information for legal cases and regulatory investigations. [Records Management](records-management) helps declare content as records or regulatory records, manage retention schedules, and conduct disposition reviews with proof of deletion.

For more information, see [Get started with data compliance solutions](purview-compliance).

## Secure AI interactions

The rapid adoption of generative AI adds a new dimension to every stage described in this article. AI apps can surface content faster and at greater scale, which amplifies the risk of oversharing and sensitive data leakage. Purview provides [data security and compliance capabilities for AI](ai-microsoft-purview) that span Copilot experiences and agents, enterprise AI apps, and other AI apps.

The protections you built in earlier stages carry forward into AI scenarios:

- **Sensitivity labels** applied to content are honored by AI apps. If a user doesn't have permission to access data, AI apps don't return that data. Users must have the EXTRACT usage right, as well as VIEW, for AI apps to return labeled, encrypted data.
- **DLP policies** can block sensitive information from being shared with third-party AI apps. Endpoint DLP policies can warn or block users from pasting sensitive data into AI sites accessed through a browser.
- **Insider Risk Management** includes a risky AI usage policy template that can detect prompt injection attacks and attempts to access protected materials.
- **DSPM** provides visibility into how AI is used across your organization, surfaces AI-specific risks, and offers one-click policies to address them.
- **Audit** captures user prompts and AI responses, and these records flow into activity explorer for monitoring and analysis.
- **Communication Compliance** can monitor AI-generated communications for regulatory violations.
- **Retention policies** from Data Lifecycle Management apply to AI interaction data, ensuring it's kept for the required period and then deleted.
- **Compliance Manager** provides assessment templates specifically for AI regulations.
- **Data governance** ensures the data feeding your AI apps is high quality, well-curated, and trustworthy, so AI systems produce accurate and reliable results.

To learn more, see [Microsoft Purview data security and compliance for AI](ai-microsoft-purview).

## Shared capabilities across solutions

Purview solutions work well together because they share a common foundation of capabilities. When you configure these capabilities in one solution, they're available everywhere:

| Shared capability | How it's used |
| --- | --- |
| [Classifiers](data-classification-overview) (sensitive information types and trainable classifiers) | Used by DLP, Information Protection, Insider Risk Management, Communication Compliance, and data classification reports. Define once, use everywhere. |
| [Sensitivity labels](sensitivity-labels) | Applied by Information Protection, enforced by DLP, honored by AI apps, captured by Audit, searchable in eDiscovery, and visible in DSPM. |
| [Connectors](archive-third-party-data) | Bring third-party data into Microsoft 365 for compliance, governance, and security scenarios. |
| [Activity explorer](data-classification-activity-explorer) | Surfaces user and admin activities related to sensitive data, labeling, and AI interactions across solutions. |

## Iterate and improve over time

Deploying Purview isn't a one-time project. The deployment guides in [Microsoft Purview deployment models](deploymentmodels/) consistently emphasize an operational phase where you expand scope, refine policies, and act on what you learn. You don't need to get everything right upfront. Start with foundational protections and improve over time.

As your deployment matures, revisit these key areas:

- **Refine your classifiers.** Start with built-in [sensitive information types](sensitive-information-type-learn-about) and expand to [Exact Data Match](sit-learn-about-exact-data-match-based-sits), [trainable classifiers](classifier-learn-about), and [document fingerprinting](document-fingerprinting) as you learn which detections produce false positives and which miss important content.
- **Enable Adaptive Protection.**[Adaptive Protection](insider-risk-management-adaptive-protection) connects Insider Risk Management signals to DLP policies so that protections adjust dynamically based on user risk level. This approach reduces friction for low-risk users while applying stricter controls when risk increases.
- **Expand to new locations and workloads.** Most organizations start with a subset of locations (for example, SharePoint and Exchange). Over time, expand DLP policies to endpoints, Teams chat, and third-party apps. Extend sensitivity labels retroactively to existing content using auto-labeling policies.
- **Use data security objectives.** DSPM provides guided [data security objectives](data-security-posture-management-learn-about#data-security-objectives) that group relevant Purview solutions into end-to-end workflows. Each objective focuses on a specific security goal, such as preventing oversharing or data exfiltration, with prioritized actions, progress tracking, and one-click policy configuration.

The key principle is to start simple, monitor results, and expand when ready. Each improvement you make builds on the foundation you already have in place.