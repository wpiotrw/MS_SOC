---
layout: Conceptual
title: Get started with Data Security Posture Management - (classic) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to get started with Data Security Posture Management (classic).
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
ms.custom: sfi-ga-nochange
locale: en-us
document_id: b37a94ea-3ec0-8d4b-94f0-b11cc3ec7297
document_version_independent_id: b37a94ea-3ec0-8d4b-94f0-b11cc3ec7297
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-get-started.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: a4344e5c-8468-7f53-6cf2-24992ed55d43
---

# Get started with Data Security Posture Management - (classic) | Microsoft Learn

Note

This article is for the **classic** version of Data Security Posture Management, now replaced with a new version that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

These improvements won't be added to this classic version so we invite you to try the new [Data Security Posture Management](data-security-posture-management-learn-about).

Use Data Security Posture Management (DSPM) to quickly identify unprotected sensitive data assets and potentially risky user activities in your organization. Complete the steps in this article to get started with the DSPM [workflow](data-security-posture-management#workflow).

## Subscriptions and licensing

Before getting started with DSPM, confirm your [Microsoft 365 subscription](https://www.microsoft.com/microsoft-365/compare-all-microsoft-365-plans) and any add-ons. Depending on the licensing and subscriptions for your organization, you can access other data security and risk and compliance solutions in the Microsoft Purview portal.

To access and use DSPM, you need a Microsoft 365 E5 or Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance) license. Administrators need to verify that their organization has a supported subscription and assign the appropriate licenses to users. For more information about subscriptions and licensing, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for DSPM.

## Step 1: Assign permissions

Important

If your permissions are restricted in specific administrative units in your organization, you can't access DSPM.

To continue with these configuration steps, you must be assigned to one of the following roles or role groups:

- [*Data Security Management*](/en-us/defender-office-365/scc-permissions#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) role group
- [*Data Security Viewer*](/en-us/defender-office-365/scc-permissions#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) role. If the DSPM dashboard is opted in, this role grants permission to view all the insights. This role is required to use Security Copilot in DSPM.
- [Insider Risk Management Admins](insider-risk-management-configure) role
- Microsoft Entra ID [*Global Administrator*](/en-us/azure/active-directory/roles/permissions-reference#global-administrator) role
- Microsoft Entra [*Compliance Administrator*](/en-us/entra/identity/role-based-access-control/permissions-reference#compliance-administrator) role

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Step 2: Opt in to analytics processing and scanning

To get started with DSPM, you need to enable analytics in Insider Risk Management and data loss prevention (DLP). When you opt into DSPM, the system automatically enables analytics in Insider Risk Management and analytics in DLP if they're not already active. If you enable analytics in Insider Risk Management and analytics in DLP, the system automatically enables DSPM.

For more information about analytics in these solutions, see:

- [Enable analytics in Insider Risk Management](insider-risk-management-settings-analytics)
- [Enable analytics in DLP](dlp-analytics-get-started)

When you complete the opt-in process, the system starts an automated scan of data and user activities for your organization. Scanning times vary based on the size of your organization and the amount of data and activities that need processing. It might take up to three days for this processing to complete.

## Step 3: Configure Security Copilot

To access Copilot in DSPM, you must configure your organization for Security Copilot. For step by step guidance, see [Get started with Microsoft Copilot for Security](/en-us/copilot/security/get-started-security-copilot).

## Step 4: Evaluate insights and take action

### Review and take action with recommendations

DSPM generates recommendations directly from the processed data, user activities, and current state of unprotected assets in your organization. Specific recommendations let you take action and quickly create data loss prevention (DLP) and Insider Risk Management policies to help you mitigate data security risks.

For more information about recommendations, see [Take action with Data Security Posture Management recommendations - (classic)](data-security-posture-management-recommendations).

### Use Microsoft Security Copilot investigate data security details

Use Security Copilot promptbooks and custom prompts to quick dive into the details and get answers about unprotected sensitive data assets and potentially risky user activities in your organization. Data security insights are generated from scanned data across data loss prevention (DLP), information protection, and Insider Risk Management solutions.

For more information about using Security Copilot, see [Use Microsoft Security Copilot with Data Security Posture Management - (classic)](data-security-posture-management-copilot).

## Step 5: Review analytics and trends to track your data security posture

DSPM analytics trends and reports help you quickly see the unprotected and protected sensitive assets and potentially risky user activities in your organization.

For more information about using trends and reports, see [Use Data Security Posture Management analytics trends and reports - (classic)](data-security-posture-management-reports).