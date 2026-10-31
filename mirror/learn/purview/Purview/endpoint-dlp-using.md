---
layout: Conceptual
title: Endpoint DLP policy scenarios in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/endpoint-dlp-using
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- purview-compliance
- SPO_Content
search.appverid:
- MET150
description: Explore scenario-based guidance for using Microsoft Purview Endpoint DLP to audit, alert, block, and enforce controls on sensitive data across devices and integrated services.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 1e2b3a3a-d052-48e8-d81f-a8f396ffc3f6
document_version_independent_id: 1e2b3a3a-d052-48e8-d81f-a8f396ffc3f6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/endpoint-dlp-using.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: endpoint-dlp-using
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/endpoint-dlp-using.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 65bcb2d4-19b4-ba0e-9081-b7ccf5a84c1d
---

# Endpoint DLP policy scenarios in Microsoft Purview | Microsoft Learn

This article provides guidance on using Endpoint Data Loss Prevention (DLP) capabilities within Microsoft Purview to help safeguard sensitive information across organizational devices. It focuses on practical, scenario-based approaches for creating and modifying DLP policies, including auditing, alerting, blocking actions, and enforcing controls on how sensitive data is accessed, shared, or transferred. By addressing common administrative use cases, this guidance helps define how policies can be applied across endpoints and integrated services to monitor and regulate user activity effectively.

By applying these scenarios, administrators can reduce data loss risks, support compliance, and gain better visibility into user activity. This scenario-based approach helps strengthen data governance and improves the organization’s overall security posture.

Important

These Endpoint DLP scenarios aren't the official procedures for creating and tuning DLP policies. For general situations, see the following topics:

- [Learn about Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp)
- [Create and Deploy data loss prevention policies](dlp-create-deploy-policy)

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Before you begin

### SKU and subscription licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

These scenarios require that you already onboard devices and that they report to Activity explorer. If you didn't onboard devices yet, see [Get started with Endpoint data loss prevention](endpoint-dlp-getting-started).

Important

Before you start, make sure you understand the difference between an unrestricted administrator and an administrative unit restricted administrator. For more information, see [Administrative units](purview-admin-units).

## Endpoint DLP policy scenarios

The following scenarios show common Endpoint DLP policy configurations you can implement:

- [Create policy to audit activities using a template (audit only mode)](endpoint-dlp-create-policy-audit-activities)
- [Create policy to manage printer access using authorization groups](endpoint-dlp-create-policy-manage-printer-access)
- [Create policy to detect and alert on U.S. PII data exposure](endpoint-dlp-create-policy-detect-pii-data-exposure)
- [Help prevent unauthorized sensitive data sharing with block actions and allow overrides](endpoint-dlp-create-policy-unauthorized-data-sharing)
- [Help prevent risky user activity by monitoring or restricting access to sensitive service domains](endpoint-dlp-create-policy-restrict-access-to-domains)
- [Help prevent leakage of sensitive content by restricting paste actions into browsers](endpoint-dlp-create-policy-restrict-paste-in-browsers)
- [Help prevent exposure of sensitive files by configuring auto-quarantine for OneDrive sync](endpoint-dlp-create-policy-auto-quarantine-for-onedrive)
- [Help prevent sharing of sensitive items with unauthorized cloud apps and services](endpoint-dlp-create-policy-unauthorized-cloud-apps-services)
- [Create policy to manage file activities by implementing network exceptions](endpoint-dlp-create-policy-file-activities-using-network-exceptions)