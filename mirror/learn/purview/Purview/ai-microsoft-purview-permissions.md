---
layout: Conceptual
title: Permissions for Microsoft Purview Data Security Posture Management for AI (classic) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-microsoft-purview-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: helenachen-microsoft
ms.service: purview
ms.update-cycle: 180-days
ms.date: 2026-04-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
description: Identify the roles and role groups required for activities in Microsoft Purview Data Security Posture Management for AI (classic).
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 42e03c02-6788-0b1a-a0b1-02a40a2940de
document_version_independent_id: 42e03c02-6788-0b1a-a0b1-02a40a2940de
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-microsoft-purview-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-microsoft-purview-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-microsoft-purview-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 5cdf1527-76d7-0247-106d-dfbacce6203b
---

# Permissions for Microsoft Purview Data Security Posture Management for AI (classic) | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This article is for the **classic** version of Data Security Posture Management for AI that's now replaced with a new version that incorporates support for AI apps and agents, new features and broader reach, with simplified management.

These improvements won't be added to this classic version so we invite you to try the new [Data Security Posture Management](data-security-posture-management-learn-about).

Members of your security and compliance teams who are responsible for managing AI apps in the [Microsoft Purview Data Security Posture Management for AI](dspm-for-ai) need appropriate permissions when they [sign in to the Microsoft Purview portal](https://purview.microsoft.com/).

Roles and role groups that can view, create, and edit in Data Security Posture Management for AI:

- **Microsoft Entra Compliance Administrator** role
- **Microsoft Entra Global Administrator** role
- **Microsoft Purview Compliance Administrator** role group

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Roles and role groups that can view-only in Data Security Posture Management for AI:

- **Microsoft Purview Security Reader** role group
- **Purview Data Security AI Viewer** role
- [**AI Administrator**](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator) role from Entra
- **Purview Data Security AI Content Viewer** role for AI interactions only

To help you assign the right permissions to users, use the following guidance, depending on the portal you're using:

- [Permissions in the Microsoft Purview portal](purview-permissions)
- [Assign Microsoft Entra roles to users](/en-us/entra/identity/role-based-access-control/manage-roles-portal)
- [Permissions in Exchange Online](/en-us/exchange/permissions-exo/permissions-exo)

Use the following table to understand the detailed permissions for different activities in Data Security Posture Management for AI.

## Permissions by activities

**✓**: Supported. The role or role group have permissions to do the specified activities.

**✕**: Not supported. The role or role group don't have permissions to do the specified activities.

| Activities | Microsoft Entra Compliance Administrator role | Microsoft Entra Global Administrator role | Microsoft Purview Compliance Administrator role group | Roles or role groups that are view-only^\*^ | When not supported, additional role groups required |
| --- | --- | --- | --- | --- | --- |
| View all get started steps | **✓** | **✓** | **✓** | **✓** | Not applicable |
| Complete action on getting started steps | **✓** | **✓** | **✓** Excludes **Activate Audit** | **✕** | Microsoft Exchange Compliance Management  Microsoft Exchange Records Management  Microsoft Exchange Organization Management |
| View completion status of getting started steps | **✓** | **✓** | **✓** Excludes status of **Activate Audit** | **✓** Excludes:  Status of **Activate Audit** Status of **Extend Your Insights** | For **Activate Audit**:  Microsoft Exchange View-Only Organization Management  Microsoft Exchange Hygiene Management  Microsoft Exchange Compliance Management  Microsoft Exchange Records Management  Microsoft Exchange Organization Management  For **Extend Your Insights**:  Microsoft Purview Insider Risk Management Administrator  Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator |
| View all recommendations | **✓** | **✓** | **✓** | **✓** | Not applicable |
| Complete actions on recommendation cards | **✓** | **✓** | **✓** | **✕** | Not applicable |
| View completion status of recommendation cards | **✓** | **✓** | **✓** | **✓** Excludes **Unethical Behavior** card | Communication compliance Administrator |
| View all graphs from the **Reports** page | **✓** | **✓** | **✓** | **✓** | Not applicable |
| View all policies in the policy list | **✓** | **✓** | **✓** | **✓** Excludes:  Insider risk management policies  Communication compliance policies | For insider risk management polices:  Microsoft Purview Insider Risk Management Administrator  Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator  For communication compliance policies:  Communication Compliance Administrator |
| View all events in activity explorer | **✓** Excludes browse to URL (**AI Visit**) from insider risk management | **✓** Excludes browse to URL (**AI Visit**) from insider risk management | **✓** Excludes browse to URL (**AI Visit**) from insider risk management | **✓** Excludes browse to URL (**AI Visit**) from insider risk management | Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator |
| View user risk level of an individual user in all events from activity explorer | **✕** | **✕** | **✕** | **✕** | Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator |
| View link to view user details in insider risk management in all events from activity explorer | **✕** | **✕** | **✕** | **✕** | Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator |
| View the prompts and responses within **AI Interaction** events from activity explorer | **✕** | **✕** | **✕** | **✕** | Content Explorer Content Viewer  Microsoft Purview Data Security AI Content Viewer |
| Create data risk assessments | **✓** | **✓** | **✓** | **✕** | Not applicable |
| View data risk assessments | **✓** | **✓** | **✓** | **✓** | Not applicable |
| View file details for data risk assessments | **✕** | **✕** | **✕** | **✕** | Content Explorer Content Viewer  Content Explorer List Viewer |
| View **Apps and agents** page | **✓** | **✓** | **✓** | **✓** | Not applicable |

^\*^ Includes Microsoft Purview Security Reader role group, Microsoft Purview Data Security AI Viewer role, and the AI Administrator role from Entra

### Custom role groups

Instead of granting access to Data Security Posture Management for AI by using the built-in role groups, you can grant access by including the Microsoft Purview Compliance Administrator role in a custom role group. For read-only permissions, include the the Microsoft Purview Security Reader role, the Purview Data Security AI Viewer role, or the AI Administrator role from Entra.

If a custom role group includes the Microsoft Purview Compliance Administrator role, the user has the same access to Data Security Posture Management for AI as the Microsoft Purview Compliance Administrator role group, except for the following:

- Create, view, update, and delete policies for insider risk management and communication compliance

If a custom role group includes the Microsoft Purview Security Reader role, the Purview Data Security AI Viewer role, or the AI Administrator role, the user has the same access to Data Security Posture Management for AI as the Microsoft Purview Security Reader role group, except for the following:

- View information protection policies