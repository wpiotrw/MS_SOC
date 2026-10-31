---
layout: Conceptual
title: Adaptive Protection configuration guide | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection-guide
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about recommendations to configure Adaptive Protection with Insider Risk Management and Data Loss Prevention (DLP).
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance, Conditional Access, DLP, data lifecycle management
ms.service: purview
ms.subservice: purview-adaptive-protection
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-10-16T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE
locale: en-us
document_id: c7d2a7ab-0d04-f2c9-c40c-8555f6fe3438
document_version_independent_id: c7d2a7ab-0d04-f2c9-c40c-8555f6fe3438
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-adaptive-protection-guide.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-adaptive-protection-guide
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-adaptive-protection-guide.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: f3b57de5-f1b4-a171-33ef-518d21497c04
---

# Adaptive Protection configuration guide | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Adaptive Protection is highly configurable, from defining risk levels to setting up mitigation actions in [data loss prevention (DLP)](dlp-adaptive-protection-learn) or conditional access policies. How you configure your risk levels and your policies that use the Adaptive Protection condition depends on your organization’s security posture and your willingness to disrupt the end user experience for users and agents in your organization. You can define separate risk levels for users and agents by selecting the appropriate tab.

This configuration is our recommendation for organizations wanting to minimize false positives and potential disruptions to users and agents.

| Adaptive Protection settings | Elevated | Moderate | Minor |
| --- | --- | --- | --- |
| Risk level configuration | Confirmed alert of any severity for a user | High severity alert generated for a user | Low or medium severity alert generated for a user |

## Data loss prevention

### Teams and Exchange configuration

With this configuration, your organization creates two DLP policies for Teams and Exchange locations. One policy is for elevated risk users and agents, and the other is for moderate and minor risk users and agents.

Elevated risk users and agents can't share content on Teams and Exchange with people outside of your organization. Moderate and minor risk users and agents have their attempts to share content externally on Teams and Exchange audited. Users and agents of all risk levels receive an email notification that their attempt to share content externally conflicts with your organization’s policy.

You can modify these configurations to fit your organization’s security posture and policies. Policy tips aren't currently supported for Adaptive Protection in DLP.

| DLP policy element | Elevated | Moderate |
| --- | --- | --- |
| Actions | Restrict access or encrypt the content in Microsoft 365 locations  - Block only people outside your organization | None |
| Additional options | Off | Off |
| Conditions | Insider risk level for Adaptive Protection is  - Elevated Risk  AND  - Content is Shared from Microsoft 365 with people outside my organization | Insider risk level for Adaptive Protection is  - Moderate Risk  AND  - Content is Shared from Microsoft 365 with people outside my organization |
| Incident reports | On  - Severity Level-Low  - Send an alert every time an activity matches the rule | On  - Severity Level-Low  - Send an alert every time an activity matches the rule |
| Status | Run the policy in simulation mode  - Policy tips not selected | Run the policy in simulation mode  - Policy tips not selected |
| User notification | On  - Notify the user who sent, shared, or last modified the content | On  - Notify the user who sent, shared, or last modified the content |
| User override | Off | Off |

### Endpoint configuration

With this configuration, your organization creates two policies for devices. One policy is for elevated risk users and the other is for moderate and minor risk users.

Elevated risk users are blocked from uploading to restricted cloud service domains or accessing content from unallowed browsers. They're also blocked from copying content to the clipboard, removable USB devices, and network share. They're blocked from printing content that matches the policy conditions. They can't access content with restricted apps. For moderate and minor risk users, all of these activities are audited.

| DLP policy element | Elevated | Moderate |
| --- | --- | --- |
| Actions | Audit or restrict activities on devices  - Upload to a restricted cloud service domain or access from unallowed browsers (Block)  File activities for all apps  - Apply restrictions to specific activity  - Copy to clipboard (Block)  - Copy to removable USB device (Block)  - Copy to network share (Block)  - Print (Block)  Restricted App activities  - Access by restricted apps (Block) | Audit or restrict activities on devices  - Upload to a restricted cloud service domain or access from unallowed browsers (Audit)  File activities for all apps  - Apply restrictions to specific activity  - Copy to clipboard (Audit)  - Copy to removable USB device (Audit)  - Copy to network share (Audit)  - Print (Audit)  Restricted App activities  - Access by restricted apps (Audit) |
| Additional options | Off | Off |
| Conditions | Insider risk level for Adaptive Protection is  - Elevated Risk  AND  - File Type is *Word processing*, *Spreadsheet*, *Presentation*, *Archive*, and *Mail* | Insider risk level for Adaptive Protection is  - Moderate Risk, Minor risk  AND  - Content is Shared from Microsoft 365 with people outside my organization |
| Incident reports | On  - Severity Level-Low  - Send an alert every time an activity matches the rule | On  - Severity Level-Low  - Send an alert every time an activity matches the rule |
| Status | Run the policy in simulation mode  - Policy tips not selected | Run the policy in simulation mode  - Policy tips not selected |
| User notification | Off | Off |
| User override | Off | Off |

## Insider Risk Management

### Conditional access policy configuration

To minimize disruption to user productivity while protecting against risky users, we recommend creating the following Conditional Access policies with the Insider risk condition when configuring Adaptive Protection.

#### Elevated

For elevated risk users and agents, minimize potential impact by taking a multipronged approach to limit how they can access sensitive data. Depending on your organization's risk posture, choose any combination of these policies.

- [Block from Office 365 Apps](/en-us/entra/identity/conditional-access/how-to-policy-insider-risk): When used with the Insider risk condition, this configuration blocks elevated risk users from signing in to Office 365 apps.
- [Block from access to specific labeled sites](/en-us/sharepoint/authentication-context-example): When used with the Conditional Access Insider risk condition, this configuration blocks elevated users and agents from accessing those SharePoint sites and prevents Copilot from generating content grounded on these sites. By using the authentication context in Conditional Access, this configuration helps limit how risky users and agents can exploit access to sensitive information by using generative AI.
- [Block downloads using Conditional Access application control](/en-us/entra/identity/conditional-access/concept-conditional-access-session): Prevent data exfiltration by using the Insider risk condition with this configuration to block elevated risk users and agents from downloading from specific cloud applications. This configuration might be useful for organizations that don't want to block access from cloud apps entirely but still want to apply additional controls to elevated users and agents.

#### Moderate

- [Require Terms of Use at sign-in to Microsoft Admin Portals](/en-us/entra/identity/conditional-access/require-tou): Use the Insider risk condition in Conditional Access with a Terms of Use requirement to remind moderate risk users and agents of their security and privacy commitments while preserving productivity.

#### Minor

Get Conditional Access insights for minor risk users and agents while protecting their productivity. Using a policy with the Insider risk condition in Report-Only mode provides increased visibility on minor risk users and agents while preserving their productivity.

- [Conditional Access insights and reporting workbook](/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting)