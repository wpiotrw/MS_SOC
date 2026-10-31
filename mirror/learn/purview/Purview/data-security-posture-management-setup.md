---
layout: Conceptual
title: Setup tasks for Microsoft Purview Data Security Posture Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-setup
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
ms.localizationpriority: high
ms.collection:
- highpri
- tier1
- m365copilot
- msec-ai-copilot
description: Learn about the setup tasks in Microsoft Purview Data Security Posture Management to help you discover, protect, and investigate data across your digital environments.
locale: en-us
document_id: 46d252b6-7af1-feea-bcb8-95aa56ad8e90
document_version_independent_id: 46d252b6-7af1-feea-bcb8-95aa56ad8e90
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-setup.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-setup
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-setup.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 0aa4763a-70c9-2e48-07bf-c2a041333927
---

# Setup tasks for Microsoft Purview Data Security Posture Management | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This documentation is for the **current** version of Data Security Posture Management that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

Most new features will be added to this version only but you can still access the previous versions and their documentation:

- [DSPM for AI (classic)](dspm-for-ai)
- [DSPM (classic)](data-security-posture-management)

When you first access [Data Security Posture Management (DSPM)](data-security-posture-management-learn-about) for your tenant, you see an initial setup task for **Audting and analytics** that's required to see meaningful data that you can take action on. Optionally, create [collection policies](collection-policies-solution-overview) to capture AI interactions. Other setup tasks can be revealed in the context of data security objectives.

All setup tasks can found from **DSPM** &gt; **Actions** &gt; **Setup tasks**. They include step-by-step instructions, status, estimated time to complete, and other helpful information such as any impact to users and links to additional information.

Some of these setup tasks include creating preconfigured policies with just one click so you can more quickly gain insights and protect your data. These one-click policies originated from the previous version, and so have the prefix of **DSPM for AI**. For more information about these policies, see the DSPM for AI documentation, [One-click policies from Data Security Posture Management for AI](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai).

Note

Although not listed as setup tasks, you might also want to check for [prerequisites](data-security-posture-management-considerations#prerequisites-for-data-security-posture-management), such as permissions, and other requirements for specific tasks.

## Activate Microsoft Purview Audit

This setup task is likely already complete because auditing is on by default for new tenants, and checked when you first run Data Security Posture Management. If you need more information, see [Learn about auditing solutions in Microsoft Purview](audit-solutions-overview) and [Turn auditing on or off](audit-log-enable-disable).

## Extend insights into sensitive data in AI interactions

Create a one-click policy that helps you gain visibility into sensitive data shared wtih AI apps through network activity.

## Extend insights for data discovery

Create one-click policies for collecting information about users visiting [third-party generative AI sites](ai-microsoft-purview-supported-sites) and sending sensitive information to them.

## Install Microsoft Purview browser extension

The [Microsoft Purview browser extension](insider-risk-management-browser-support#configure-browser-signal-detection-for-microsoft-edge) must be deployed to Windows users to discover visits to third-party generative AI sites by using an Insider Risk Management policy. The browser extension is also required for endpoint DLP policies on Windows when you use Chrome.

## Integrate with partner solutions

This options is in preview.

Set up Microsoft Sentinel data lake to integrate partner solutions and centralize security posture monitoring across all data sources. To see the available partner solutions and then select one from this task, you must first [connect to the Microsoft Sentinel content hub](/en-us/azure/sentinel/sentinel-solutions-deploy?tabs=defender-portal#prerequisites). Initial partners include Varonis (for Salesforce), Cyera (for Snowflake), BigID (for Databricks), and OneTrust (for Google Cloud Platform).

## Onboard devices to Microsoft Purview

Devices must be [onboarded to Microsoft Purview](device-onboarding-overview) for:

- Gaining visibility into sensitive information that's shared with third-party generative AI sites. For example, a user pastes credit card numbers into ChatGPT.
- Applying endpoint DLP policies to warn or block users from sharing sensitive information with third-party generative AI sites. For example, a user identified as elevated risk in Adaptive Protection is blocked with the option to override when they paste credit card numbers into ChatGPT.

## Protect your data with sensitivity labels

Create [default sensitivity labels and sensitivity label policies](default-sensitivity-labels-policies), if they don't already exist in your tenant.

## Secure interactions from enterprise AI apps

Create a one-click policy that captures prompts and responses for regulatory compliance from enterprise AI apps, such as Chat GPT Enterprise and AI apps connected through Microsoft Entra or Azure AI Foundry, so they can be managed in Microsoft Purview solutions like eDiscovery, Data Lifecycle Management, and more.

## Secure interactions in Microsoft Copilot experiences

Create a one-click policy that captures prompts and responses for data security posture and regulatory compliance from Copilot in Fabric and Security Copilot.

## Set up pay-as-you-go billing for data storage

For some options you must set up [pay-as-you-go billing](purview-billing-models) for your organization. When this billing model is applicable for specific configurations, you'll see notifications and instructions in the UI.

You might find it helpful to use the **Usage center** to help you understand and manage your usage. For more information, see [Manage pay-as-you-go and per-user licensing usage](purview-billing-usage).