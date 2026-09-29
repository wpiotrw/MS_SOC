---
layout: Conceptual
title: Overview of Microsoft Purview APIs - purview-sdk | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/developer/microsoft-purview-sdk-documentation-overview
uhfHeaderId: MSDocsHeader-Purview
enable_rest_try_it: true
rest_product: purview-sdk
breadcrumb_path: breadcrumb/toc.json
author: ReezaAli149
ms.author: v-reezaali
ms.topic: article
ms.date: 2026-04-07T00:00:00.0000000Z
ms.service: purview
feedback_system: None
description: Use Microsoft Purview APIs in Microsoft Graph to build secure, compliant applications (AI, line-of-business, SaaS) with data loss prevention and governance.
locale: en-us
document_id: 2d9d6e9b-16ad-d7ba-7b86-af7ba82b09fa
document_version_independent_id: 6e37b7ac-72c9-10e6-eea6-1da5112d6135
original_content_git_url: https://github.com/MicrosoftDocs/Microsoft-Purview-SDK/blob/live/PurviewSDK/Microsoft-Purview-SDK-Documentation-overview.md
site_name: Docs
depot_name: Learn.PurviewSDK
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: developer/microsoft-purview-sdk-documentation-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: PurviewSDK/Microsoft-Purview-SDK-Documentation-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: d1fee35e-d016-55ea-8211-914e7cef74c6
---

# Overview of Microsoft Purview APIs - purview-sdk | Microsoft Learn

The Microsoft Purview APIs in Microsoft Graph give you the tools to build apps that are secure, compliant, and policy-aware by design. With a rich set of APIs and services, the platform enables your applications to integrate directly with your organization's data governance, security, and compliance policies.

As organizations use Microsoft Purview to discover, classify, protect, and govern sensitive information, it’s critical that applications handling this data also respect these controls. Apps built on the Microsoft Purview APIs can:

- Interpret actions to take on sensitivity labels.
- Enforce policies defined in the Microsoft Purview portal.
- Prevent data misuse by aligning with compliance and security requirements.
- Deliver a seamless and trusted user experience by applying policies natively.

If you're building line-of-business (LoB) apps or multitenant SaaS solutions, using the Microsoft Purview APIs ensures that your app respects the value of the data it processes and the policies that protect that data.

To learn more about Microsoft Purview, see [Learn about Microsoft Purview](/en-us/purview/purview).

## Why use the Microsoft Purview APIs in Microsoft Graph?

When you integrate your application with the Microsoft Purview APIs in Microsoft Graph, you can:

- Focus on the core value proposition of your app, while supporting data security and compliance outcomes as required by the organization, which enhances the overall value of the app for your customers (organizations).
- Help your customers meet their data security and compliance requirements for your app, which unblocks adoption of your app in their environment.
- Empower business users to interact with your apps in a secure and compliant manner, which improves business productivity.

## Enterprise app integration benefits

You can achieve the following outcomes by integrating your enterprise applications (AI and non-AI) with the Microsoft Purview APIs:

- Protect against data loss and insider risk by:
    - Enabling inline blocking of sensitive data based on data loss prevention (DLP) policies set within the enterprise.
    - Supporting Insider Risk Management (IRM) alerts defined in the policies.
- Address oversharing concerns by honoring sensitivity labels applied to data.
- Enable governance for app usage to meet regulations and policies. For example, you can send app content (such as user inputs, generated outputs, or transferred files — including AI prompts and responses) into Microsoft Purview to enable visibility of app interactions, risk analytics, and support all relevant compliance outcomes (Audit, eDiscovery, Data Lifecycle Management, Communication Compliance).

Important

To set up a new DLP policy in Microsoft Purview to test DLP integration, run the `New-DlpComplianceRule` cmdlet. For more information, see [New-DlpComplianceRule](/en-us/powershell/module/exchangepowershell/new-dlpcompliancerule?#example-4).

## Scenarios and API overview

Enterprise applications (AI, line-of-business, SaaS) call Microsoft Purview APIs that are available in Microsoft Graph to evaluate and enforce data protection policies at runtime.

Applications can compute applicable protection scopes for a user, submit content for policy evaluation, and process the results to determine allowed actions. These interactions enable consistent enforcement of Microsoft Purview policies across all enterprise apps.

The following diagram shows how enterprise applications integrate with Microsoft Purview through the Microsoft Graph APIs to enforce data protection, apply sensitivity labels, and capture audit and compliance signals.

[![Supported scenarios and capabilities of the Microsoft Purview APIs in the Microsoft Graph.](images/overview-capabilities.png)](images/overview-capabilities.png#lightbox)

The diagram highlights several common integration patterns:

- **Policy evaluation and enforcement**: Applications use the `protectionScopes` and `processContent` APIs to compute which data protection scopes apply to a user/tenant, and to evaluate content against those policies.
- **Audit and compliance signals**: Applications send content activity using the `contentActivities` API, enabling auditing, compliance tracking, and detection of unusual behavior.
- **Sensitivity label integration**: Applications query `sensitivityLabels` APIs to list available labels, retrieve label details, and compute user rights and inheritance for labeled content.

Together, these APIs allow developers to embed Microsoft Purview governance, protection, and compliance capabilities directly into their applications using a single, unified Microsoft Graph endpoint.