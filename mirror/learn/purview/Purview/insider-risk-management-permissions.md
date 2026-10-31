---
layout: Conceptual
title: Assign permissions in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Assign the permissions required to perform tasks in Insider Risk Management.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-09-30T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 4f142d3a-08d9-9925-8de5-ca9f65ee87d3
document_version_independent_id: 4f142d3a-08d9-9925-8de5-ca9f65ee87d3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: a51ea77a-1f79-5bba-f136-d32537ce0a5d
---

# Assign permissions in Insider Risk Management | Microsoft Learn

Use six role groups to configure Insider Risk Management features. To make **Insider Risk Management** available as a menu option in Microsoft Purview and to continue with these configuration steps, you must be assigned to one of the following roles or role groups:

- Microsoft Entra ID [*Global Administrator*](/en-us/azure/active-directory/roles/permissions-reference#global-administrator) role
- Microsoft Entra ID [*Compliance Administrator*](/en-us/azure/active-directory/roles/permissions-reference#compliance-administrator) role
- Microsoft Purview [*Organization Management*](/en-us/microsoft-365/security/office-365-security/scc-permissions) role group
- Microsoft Purview [*Compliance Administrator*](/en-us/microsoft-365/security/office-365-security/scc-permissions) role group
- *Insider Risk Management* role group
- *Insider Risk Management Admins* role group

Depending on how you want to manage Insider Risk Management policies and alerts, assign users to specific role groups to manage different sets of Insider Risk Management features. You can assign users with different compliance responsibilities to specific role groups to manage different areas of Insider Risk Management features. Or you might decide to assign all user accounts for designated administrators, analysts, investigators, and viewers to the *Insider Risk Management* role group. Use a single role group or multiple role groups to best fit your compliance management requirements.

Important

After configuring your role groups, it might take up to 30 minutes for the role group permissions to apply to assigned users across your organization.

Choose from these role group options and solution actions when working with Insider Risk Management:

| Actions | Insider Risk Management | Insider Risk Management Admins | Insider Risk Management Analysts | Insider Risk Management Investigators | Insider Risk Management Auditors | Insider Risk Management Approvers |
| --- | --- | --- | --- | --- | --- | --- |
| Access & investigate alerts | Yes | No | Yes | Yes | No | No |
| Access & investigate cases | Yes | No | Yes | Yes | No | No |
| Access & view forensic evidence captures | Yes | No | No | Yes | No | No |
| Access & view the Content Explorer | Yes | No | No | Yes | No | No |
| Access analytics insights | Yes | Yes | Yes | No | No | No |
| Approve forensic evidence capturing requests | Yes | No | No | No | No | Yes |
| Configure Adaptive Protection | Yes | Yes | No | No | No | No |
| Configure notice templates | Yes | No | Yes | Yes | No | No |
| Configure policies and settings | Yes | Yes | No | No | No | No |
| Create forensic evidence capturing request | Yes | Yes | No | No | No | No |
| View & export audit logs | Yes | No | No | No | Yes | No |
| View Adaptive Protection users tab | Yes | No | Yes | Yes | No | No |
| View alert and case reports | Yes | Yes | Yes | Yes | No | No |
| View data risk graphs for alerts | Yes | No | Yes | Yes | No | No |

Important

Make sure you always have at least one user in the built-in *Insider Risk Management* or *Insider Risk Management Admins* role groups (depending on the option you choose) so that your Insider Risk Management configuration doesn't get into a 'zero administrator' scenario if specific users leave your organization.

Members of the following roles can assign users to Insider Risk Management role groups and have the same solution permissions included with the *Insider Risk Management Admins* role group:

- Microsoft Entra ID *Global Administrator*
- Microsoft Entra ID *Compliance Administrator*
- Microsoft Purview *Organization Management*
- Microsoft Purview *Compliance Administrator*

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Add users to the Insider Risk Management role group

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, select **Roles and groups**, then select **Roles groups** in the left navigation pane.
3. Select the *Insider Risk Management* role group, then select **Edit**.
4. Select **Choose users**, then select the checkboxes for all the users you want to add to the role group.
5. Select **Select**, then select **Next**.
6. Select **Save** to add the users to the role group, then select **Done**.

## Consider administrative units if you want to scope user permissions to a region or department

You can use administrative units in Insider Risk Management to scope user permissions to a particular geography or department. For example, a global company that has subsidiaries throughout the world might want to create an admin unit that provides a German scope for investigators so that they only see user activity for German users.

To use admin units in Insider Risk Management, you must first [create the admin units](purview-admin-units) if they aren't already created, then assign the admin units to members of role groups. After you assign admin units to members of role groups, those members become *restricted administrators* and have limited access to Insider Risk Management settings, policies, and user data in the organization. Members who aren't assigned administrative units are *unrestricted administrators* and have access to all settings, policies, and user data.

Important

Restricted administrators can't access alerts for the users assigned to them through security groups or distribution groups added in administrative units. Such user alerts are visible only to unrestricted administrators. Microsoft recommends adding users directly to administrative units to ensure their alerts are also visible to restricted administrators with administrative units assigned.

### Effect of admin unit scoping on Insider Risk Management roles

The following table shows how admin units, when enforced, affect each combination of Insider Risk Management task and role.

Note

*Scoped* in the following table means that the admin actions for that role are limited by their assigned admin unit.

| Task | Scoped Insider Risk Management | Scoped Insider Risk Management Admin | Scoped Insider Risk Management Analysts | Scoped Insider Risk Management Investigators | Scoped Insider Risk Management Approvers |
| --- | --- | --- | --- | --- | --- |
| Access analytics insights | Not allowed, if scoped | Not allowed, if scoped | Not allowed, if scoped | Never allowed | Never allowed |
| Access and investigate alerts | Scoped | Never allowed | Scoped | Scoped | Never allowed |
| Access and investigate cases | Scoped | Never allowed | Scoped | Scoped | Never allowed |
| Access and view forensic evidence captures | Not allowed, if scoped | Never allowed | Never allowed | Not allowed, if scoped | Never allowed |
| Access and view the Content explorer | Unrestricted | Never allowed | Never allowed | Unrestricted | Never allowed |
| Approve forensic evidence capturing requests | Not allowed, if scoped | Never allowed | Never allowed | Never allowed | Not allowed, if scoped |
| Assign or reassign alerts | Not allowed, if scoped | Never allowed | Not allowed, if scoped | Not allowed, if scoped | Never allowed |
| Assign or reassign cases | Not allowed, if scoped | Never allowed | Not allowed, if scoped | Not allowed, if scoped | Never allowed |
| Configure Adaptive Protection | Not allowed, if scoped | Not allowed, if scoped | Never allowed | Never allowed | Never allowed |
| Configure global settings | Unrestricted | Unrestricted | Never allowed | Never allowed | Never allowed |
| Configure notice templates | Unrestricted | Never allowed | Unrestricted | Unrestricted | Never allowed |
| Configure policies | Scoped | Scoped | Never allowed | Never allowed | Never allowed |
| Configure priority user groups | Not allowed, if scoped | Not allowed, if scoped | Never allowed | Never allowed | Never allowed |
| Configure priority-user-specific policies | Not allowed, if scoped | Not allowed, if scoped | Never allowed | Never allowed | Never allowed |
| Create forensic evidence capturing request | Not allowed, if scoped | Not allowed, if scoped | Never allowed | Never allowed | Never allowed |
| Create quick policies | Not allowed, if scoped | Not allowed, if scoped | Never allowed | Never allowed | Never allowed |
| Investigate user activity | Scoped | Never allowed | Never allowed | Scoped | Never allowed |
| Start scoring activity for users | Scoped | Scoped | Scoped | Scoped | Never allowed |
| View Adaptive Protection users tab | Not allowed, if scoped | Never allowed | Not allowed, if scoped | Not allowed, if scoped | Never allowed |
| View alert and case reports | Scoped | Scoped | Scoped | Scoped | Scoped |
| View data risk graphs for alerts | Not supported | Not supported | Not supported | Not supported | Not supported |
| View device health report | Not allowed, if scoped | Not allowed, if scoped | Never allowed | Never allowed | Never allowed |

Note

You can [use adaptive scopes together with admin units](purview-adaptive-scopes). If one or more admin units scope role groups for your organization, the admin units limit the adaptive scopes that you can select when you create or edit a policy.