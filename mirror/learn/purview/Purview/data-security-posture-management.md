---
layout: Conceptual
title: Learn about Data Security Posture Management (classic) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use Copilot with Data Security Posture Management (classic).
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2025-12-15T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.collection:
- purview-compliance
- data-security-posture-management
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
locale: en-us
document_id: e669a54c-c433-6fdd-409c-a330547b2e39
document_version_independent_id: e669a54c-c433-6fdd-409c-a330547b2e39
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 84d7676b-4628-37ef-5dd4-076e49e6b72e
---

# Learn about Data Security Posture Management (classic) | Microsoft Learn

Note

This article is for the **classic** version of Data Security Posture Management, now replaced with a new version that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

These improvements won't be added to this classic version so we invite you to try the new [Data Security Posture Management](data-security-posture-management-learn-about).

Strengthening data security and minimizing exposure to data risks for sensitive information is often challenging for organizations in the modern workplace. The increasing complexity of data, the variety of data sources and platforms, limited visibility into sensitive data, and fragmented security solutions can pose significant challenges for administrators and data security professionals. Adding multicloud platforms and generative AI applications to these areas makes it even more difficult to assess data security coverage and to correlate insights from user data points. To help discover and mitigate data risks, organizations must address the following questions:

- What is my sensitive data?
- Where is it located?
- What data is currently unprotected?
- How is unprotected sensitive data being handled and accessed?
- How can I help lower the risk and help secure unprotected sensitive data?

Microsoft Purview Data Security Posture Management (DSPM) enables you to quickly and easily monitor cross-cloud data and user risk through dynamic reports and trend analysis. By processing and correlating data across other Microsoft Purview data security and risk and compliance solutions, DSPM helps you identify vulnerabilities with unprotected data and quickly take action to help you improve your data security posture and minimize risk. DSPM provides:

- **Data security recommendations**: Gain insights into your data security posture and get recommendations for creating Insider Risk Management and data loss prevention (DLP) policies to help protect sensitive data and to close data security gaps. For example, some recommendations might include creating policies to prevent users from printing sensitive files or to prevent users from copying sensitive files to other network locations.
- **Data security analytic trends and reports**: Track your organization's data security posture over time with reports summarizing sensitivity label usage, DLP policy coverage, changes in risky user behavior, and more.
- **Microsoft Security Copilot**: Use Security Copilot promptbooks and custom prompts to help you investigate alerts, identify risk patterns, and pinpoint the top data security risks in your organization.

## Integration with Microsoft Purview solutions

DSPM processes and correlates data state, signals, and user activities based on the current configuration of other data security and risk and compliance solutions in Microsoft Purview. For optimal coverage and deeper insights, consider using the features and capabilities of the following solutions:

- **Data loss prevention (DLP)**: [Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp) policies help you prevent users from inappropriately sharing sensitive data. DLP detects sensitive information by using content analysis that includes keyword matching, evaluations of expressions, internal validation, machine learning algorithms, and more.

    Depending on the specific recommendations for the data, you can choose to quickly create an applicable [DLP policy](dlp-policy-design) directly in the DSPM workflow.
- **Information protection**: [Microsoft Purview Information Protection](information-protection) provides a framework, process, and capabilities you can use to protect sensitive data across clouds, apps, and devices. By using sensitivity labels, trainable classifiers, and sensitive information types, you can define and apply protection policies to sensitive data.
- **Insider risk management**: [Microsoft Purview Insider Risk Management](insider-risk-management) uses the full breadth of built-in service and third-party indicators to help you quickly identify, triage, and act on potentially risky activity by users in your organization. By using logs from Microsoft 365 and Microsoft Graph, Insider Risk Management allows you to define specific policies to identify risk indicators. After identifying the risks, you can take action to mitigate these risks, and if necessary open investigation cases and take appropriate legal action.

    Depending on the specific recommendations for the data, you can choose to quickly create an applicable [Insider Risk Management policy](insider-risk-management-policy-templates) directly in the DSPM workflow.

### Working with Adaptive Protection

[Adaptive protection](insider-risk-management-adaptive-protection) in Microsoft Purview uses machine learning to identify the most critical risks and proactively and dynamically apply protection controls from data loss prevention, data lifecycle management, and Microsoft Entra conditional access. If Adaptive Protection isn't currently enabled for unprotected sensitive data, you can create a new Adaptive Protection policy directly in the DSPM workflow.

## Workflow

The DSPM workflow helps you investigate and take action to address potential security concerns with unprotected data across your organization.

![Data security posture management workflow diagram.](media/dspm-workflow.png)

1. **Opt in to analytics processing**: To get started with DSPM, enable and opt in to:
    1. Insider risk management analytics
    2. DLP analytics
    3. Analytics processing in DSPM to scan for unprotected data in your organization.
2. **Evaluate insights and take action**: After the automated analytics processing completes, evaluate the insights created by DSPM to help mitigate risks for unprotected data.
3. **Actions**:
    1. **Investigate with Security Copilot**: Use built-in promptbooks and custom prompts with Security Copilot to help identify specific areas of risk.
    2. **Create policies with recommendations**: Use recommendations to quickly create Insider Risk Management and DLP policies to help mitigate data security risks for unprotected data assets.
4. **Track posture with analytic trends and reports**: Use analytic trends and reports to view your posture over time and for data locations across your organization.

### Using DSPM (classic) in new environments

For organizations just getting started with Microsoft Purview, DSPM helps provide easy configuration and new policy creation across several data security and risk and compliance solutions.

By automatically scanning data and activities across your organization, you quickly get baseline insights and recommendations focused on unprotected data that can help you quickly get started in DLP, information protection, and Insider Risk Management.

### Using data security in existing environments

If your organization is already using DLP, information protection, and Insider Risk Management in Microsoft Purview, DSPM helps identify any gaps in your current policy coverage.

Without having to conduct deeper dives into your existing policies, DSPM can quickly determine and highlight any unprotected data at risk, saving you the time and effort associated with reviewing and testing numerous individual data security and risk and compliance policies.

## Ready to get started?

- [Get started with Data Security Posture Management - (classic)](data-security-posture-management-get-started)
- [Take action with Data Security Posture Management recommendations - (classic)](data-security-posture-management-recommendations)
- [Use Microsoft Security Copilot with Data Security Posture Management - (classic)](data-security-posture-management-copilot)
- [Use Data Security Posture Management analytics trends and reports - (classic)](data-security-posture-management-reports)