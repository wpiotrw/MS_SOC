---
layout: Conceptual
title: Limits in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-limits
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about limits in Microsoft Purview Insider Risk Management
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance, limitations
ms.service: purview
ms.topic: article
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-07-18T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
ms.subservice: purview-insider-risk-management
locale: en-us
document_id: 7c9532c4-230f-d712-bdf3-aa6daae657ba
document_version_independent_id: 7c9532c4-230f-d712-bdf3-aa6daae657ba
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-limits.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-limits
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-limits.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 822873c5-f7be-efe7-b392-517395592bfb
---

# Limits in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

This article describes the limits in Microsoft Purview Insider Risk Management.

## Global settings

| Item | Limit |
| --- | --- |
| Lookback period limits (Exchange Online). | 10 days |
| Lookback period limits for all other signals. | 90 days |
| Maximum number of custom indicators. | 10 |
| Maximum number of fields per custom indicator. | 20 |
| Maximum number of items in a detection group | 200 |
| Maximum number of items in each global exclusion list (Domains, SharePoint sites, File paths, Keywords, and File types). | 500 for each list |
| Maximum number of users that you can add to a priority user group. | 10,000 |
| Maximum number of variants per indicator. | 3 |

## Triggers (per UTC calendar day)

| Item | Limit |
| --- | --- |
| [Custom indicators](import-insider-risk-indicators) | 15,000 |
| All other triggers | 5,000 |
| All signals collected through the [HR connector](import-hr-data) | 15,000 |
| Maximum trigger volume for an organization | 50,000 |
| User account deleted from Microsoft Entra ID | 15,000 |

Note

Limitations apply to each individual trigger type.

## Maximum number of users in scope for a policy template

| Template name | Limit |
| --- | --- |
| [Data leaks by priority users](insider-risk-management-policy-templates#data-leaks-by-priority-users) | 1,000 |
| [Data leaks by risky users](insider-risk-management-policy-templates#data-leaks-by-risky-users) | 7,500 |
| [Data leaks](insider-risk-management-policy-templates#data-leaks) | 15,000 |
| [Data theft by departing users](insider-risk-management-policy-templates#data-theft-by-departing-users) | 20,000 |
| [Forensic evidence](insider-risk-management-forensic-evidence-configure#step-4-create-a-policy) | Unlimited |
| [Patient data misuse (preview)](insider-risk-management-policy-templates#patient-data-misuse-preview) | 5,000 |
| [Risky AI usage](insider-risk-management-policy-templates#risky-ai-usage) | 10,000 |
| [Risky browser usage (preview)](insider-risk-management-policy-templates#risky-browser-usage-preview) | 7,000 |
| [Security policy violations by departing users](insider-risk-management-policy-templates#security-policy-violations-by-departing-users) | 15,000 |
| [Security policy violations by priority users](insider-risk-management-policy-templates#security-policy-violations-by-priority-users) | 1,000 |
| [Security policy violations by risky users](insider-risk-management-policy-templates#security-policy-violations-by-risky-users) | 7,500 |
| [Security policy violations](insider-risk-management-policy-templates#security-policy-violations) | 1,000 |

Note

You can add any number of users to a policy. The limit applies to users *in scope* of a policy template (users brought in scope after a triggering event).

## Other policy limits

| Item | Limit |
| --- | --- |
| Maximum number of policies that you can create per template type. | 100 |
| Maximum number of priority file extensions. | 50 |
| Maximum number of priority sensitive info types. | 50 |
| Maximum number of priority sensitivity labels. | 50 |
| Maximum number of priority sites. | 50 |
| Maximum number of priority trainable classifiers. | 5 |

Note

The **Users in scope** column on the **Policies** tab shows the number of included users for a policy.

## Adaptive protection

| Item | Limit |
| --- | --- |
| Maximum number of users that you can include in a Data Loss Prevention (DLP) policy for each risk level. | 10,000 |

## Manual user scoring

| Item | Limit |
| --- | --- |
| Maximum number of users that you can score manually. | 4,000 |

### Cases

| Item | Limit |
| --- | --- |
| Maximum number of active cases. | 100 |

## Exporting

| Item | Limit |
| --- | --- |
| Maximum number of alerts that you can export from the **Alerts** page. | 1,000 |
| Maximum number of logs that you can export to a CSV file from Activity explorer. | 100,000 |
| Maximum number of users that you can export from the **Users** page. | 1,000 |

## Retention limits for alerts, cases, and associated artifacts

As Insider Risk Management alerts age, their value to minimize potentially risky activity diminishes for most organizations. Conversely, active cases and associated artifacts (alerts, insights, activities) are always valuable to organizations and shouldn't have an automatic expiration date. This value includes all future alerts and artifacts in an active status for any user associated with an active case.

To help minimize the number of older items that provide limited current value, the following retention limits apply for Insider Risk Management alerts, cases, and user reports:

| Item | Retention period |
| --- | --- |
| Active cases (and associated artifacts) | Indefinite retention, never expire. |
| Alerts with Needs review or Dismissed status | 120 days from alert creation, then automatically deleted. |
| Resolved cases (and associated artifacts) | 120 days from case resolution, then automatically deleted. |
| User activities reports | 120 days from report creation, then automatically deleted. |

## Connectors

| Item | Limit |
| --- | --- |
| Maximum number of records in the JSON file that the API processes | 50,000 |