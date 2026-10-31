---
layout: Conceptual
title: Permissions for Microsoft Purview Data Security Posture Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: soqureshi
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.update-cycle: 180-days
ms.date: 2026-06-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- tier1
- m365copilot
- msec-ai-copilot
description: Identify the roles and role groups required for activities in Microsoft Purview Data Security Posture Management.
locale: en-us
document_id: f35a3619-9157-76e4-e4d5-6ff2670f34ae
document_version_independent_id: f35a3619-9157-76e4-e4d5-6ff2670f34ae
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 9c32e5a1-b2be-0f96-6774-a1a68d950063
---

# Permissions for Microsoft Purview Data Security Posture Management | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This documentation is for the **current** version of Data Security Posture Management that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

Most new features will be added to this version only but you can still access the previous versions and their documentation:

- [DSPM for AI (classic)](dspm-for-ai)
- [DSPM (classic)](data-security-posture-management)

Members of your security and compliance teams who are responsible for managing AI apps in [Microsoft Purview Data Security Posture Management](data-security-posture-management-learn-about) need appropriate permissions when they [sign in to the Microsoft Purview portal](https://purview.microsoft.com/).

Roles and role groups that can view, create, and edit in Data Security Posture Management:

- **Microsoft Entra Compliance Administrator** role
- **Microsoft Entra Global Administrator** role
- **Microsoft Purview Compliance Administrator** role group

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Roles and role groups that can view-only in Data Security Posture Management:

- **Microsoft Purview Security Reader** role group
- **Purview Data Security AI Viewer** role
- **Data Security Viewers** role group and **Data Security Viewer** role
- [**AI Administrator**](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator) role from Entra
- **Purview Data Security AI Content Viewer** role for AI interactions only

To help you assign the right permissions to users, use the following guidance, depending on the portal you're using:

- [Permissions in the Microsoft Purview portal](purview-permissions)
- [Assign Microsoft Entra roles to users](/en-us/entra/identity/role-based-access-control/manage-roles-portal)
- [Permissions in Exchange Online](/en-us/exchange/permissions-exo/permissions-exo)

Use the following table to understand the detailed permissions for different activities in Data Security Posture Management.

## Permissions by activities

**✓**: Supported. The role or role group have permissions to do the specified activities.

**✕**: Not supported. The role or role group don't have permissions to do the specified activities.

| Activities | Microsoft Entra Compliance Administrator role | Microsoft Entra Global Administrator role | Microsoft Purview Compliance Administrator role group | Roles or role groups that are view-only^1^ | Roles or role groups that are view-only for AI data^2^ | When not supported, additional role groups required |
| --- | --- | --- | --- | --- | --- | --- |
| Complete one-click get started steps | **✓** | **✓** | **✓** | **✕** | **✕** | Not applicable |
| View all get started steps | **✓** | **✓** | **✓** | **✓** | **✕** | Not applicable |
| View key posture metrics, data snapshot, and posture trends chart on the Posture page | **✓** | **✓** | **✓** | **✓** | **✕** | Not applicable |
| View Security Copilot insights and run prompts | **✕** | **✕** | **✕** | **✕** | **✕** | Data Security Viewers |
| Complete action on getting started steps | **✓** | **✓** | **✓** Excludes **Activate Audit** | **✕** | **✕** | Microsoft Exchange Compliance Management  Microsoft Exchange Records Management  Microsoft Exchange Organization Management |
| View completion status of getting started steps | **✓** | **✓** | **✓** Excludes status of **Activate Audit** | **✓** Excludes:  Status of **Activate Audit** Status of **Extend Your Insights** | **✓** Excludes:  Status of **Activate Audit** Status of **Extend Your Insights** | For **Activate Audit**:  Microsoft Exchange View-Only Organization Management  Microsoft Exchange Hygiene Management  Microsoft Exchange Compliance Management  Microsoft Exchange Records Management  Microsoft Exchange Organization Management  For **Extend Your Insights**:  Microsoft Purview Insider Risk Management Administrator  Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator |
| Connect to partner solutions in Microsoft Sentinel content hub | **✕** | **✕** | **✕** | **✕** | **✕** | Microsoft Sentinel Contributor |
| Create data security investigation | **✕** | **✕** | **✕** | **✕** | **✕** | Compliance Administrator  Data Security Management  Insider Risk Management Admin  Organization Management  Data Security Investigations Admin  Data Security Investigations Investigator |
| View all recommendations | **✓** | **✓** | **✓** | **✓** | **✓** | Not applicable |
| Complete actions on recommendation cards | **✓** | **✓** | **✓** | **✕** | **✕** | Not applicable |
| View completion status of recommendation cards | **✓** | **✓** | **✓** | **✓** Excludes **Unethical Behavior** card | **✓** Excludes **Unethical Behavior** card | Communication Compliance Administrator |
| View all activity and posture reports | **✓** | **✓** | **✓** | **✓** | **✓** | Not applicable |
| View all policies in the policy list, **Reports** page | **✓** | **✓** | **✓** | **✓** Excludes:  Insider risk management policies  Communication compliance policies | **✓** Excludes:  Insider risk management policies  Communication compliance policies | For insider risk management polices:  Microsoft Purview Insider Risk Management Administrator  Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator  For communication compliance policies:  Communication Compliance Administrator |
| View all events in activity explorer, AI activities tab | **✓** Excludes browse to URL (**AI Visit**) from insider risk management | **✓** Excludes browse to URL (**AI Visit**) from insider risk management | **✓** Excludes browse to URL (**AI Visit**) from insider risk management | **✓** Excludes browse to URL (**AI Visit**) from insider risk management | **✓** Excludes browse to URL (**AI Visit**) from insider risk management | Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator |
| View all events in activity explorer, **All activity types** tab | **✓** Excludes insider risk management events | **✓** Excludes insider risk management events | **✓** Excludes insider risk management events | **✓** Excludes insider risk management events | **✕** | Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator |
| View user risk level of an individual user in all events from activity explorer | **✕** | **✕** | **✕** | **✕** | **✕** | Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator |
| View user risk level of an individual user in all events from activity explorer, both tabs | **✕** | **✕** | **✕** | **✕** | **✕** | Microsoft Purview Insider Risk Management Analyst  Microsoft Purview Insider Risk Management Investigator |
| View the prompts and responses within **AI Interaction** events from activity explorer | **✕** | **✕** | **✕** | **✕** | **✕** | Content Explorer Content Viewer  Microsoft Purview Data Security AI Content Viewer |
| Create data risk assessments | **✓** | **✓** | **✓** | **✕** | **✕** | Not applicable |
| View data risk assessments | **✓** | **✓** | **✓** | **✓** | **✓** | Not applicable |
| View file details for data risk assessments | **✕** | **✕** | **✕** | **✕** | **✕** | Content Explorer Content Viewer  Content Explorer List Viewer |
| View **Apps and agents** page | **✓** | **✓** | **✓** | **✓** | **✓** | Not applicable |
| View objectives | **✓** | **✓** | **✓** | **✓** | **✓** | Not applicable |
| View remediation plan for objectives | **✓** | **✓** | **✓** | **✓** | **✕** | Not applicable |
| View remediation plan completion status | **✓** | **✓** | **✓** | **✓** | **✕** | Not applicable |
| View risk patterns | **✓** | **✓** | **✓** | **✓** | **✓** | Not applicable |
| View asset explorer | **✓** | **✓** | **✓** | **✓** | **✕** | Not applicable |
| View file metadata in asset explorer | **✕** | **✕** | **✕** | **✕** | **✕** | Content Explorer Content Viewer |

^1^ Includes Microsoft Purview Security Reader role group, Microsoft Purview Data Security AI Viewer role, the AI Administrator role from Entra, and the Data Security Viewers role group and Data Security Viewer role.

^2^ The activities that display AI data security information, for view-only. For example, AI data from objectives such as exfiltration to AI apps and prevent oversharing, with their AI-related policies and metrics. Includes Microsoft Purview Data Security AI Viewer role and the AI Administrator role from Entra.

### Custom role groups

Instead of granting access to Data Security Posture Management by using the built-in role groups, you can grant access by including the Microsoft Purview Compliance Administrator role in a custom role group. For read-only permissions, include the the Microsoft Purview Security Reader role, the Purview Data Security AI Viewer role, or the AI Administrator role from Entra.

If a custom role group includes the Microsoft Purview Compliance Administrator role, the user has the same access to Data Security Posture Management as the Microsoft Purview Compliance Administrator role group, except for the following:

- Create, view, update, and delete policies for insider risk management and communication compliance

If a custom role group includes the Microsoft Purview Security Reader role, the Purview Data Security AI Viewer role, or the AI Administrator role, the user has the same access to Data Security Posture Management the Microsoft Purview Security Reader role group, except for the following:

- View information protection policies