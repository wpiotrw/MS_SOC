---
layout: Conceptual
title: Assign permissions in Communication Compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Assign the permissions required to perform tasks in Communication Compliance.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-08-14T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
search.appverid:
- MET150
- MOE150
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 78bd9342-8d0c-9ad1-ce8b-9696381f941d
document_version_independent_id: 78bd9342-8d0c-9ad1-ce8b-9696381f941d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 00131943-1f5c-54f1-015c-3bba00a7370c
---

# Assign permissions in Communication Compliance | Microsoft Learn

Use six role groups to configure initial permissions for managing Communication Compliance features. To make **Communication Compliance** available as a menu option in Microsoft Purview portal and to continue with these configuration steps, you must be assigned to one of the following roles or role groups:

- Microsoft Entra ID [*Global Administrator*](/en-us/azure/active-directory/roles/permissions-reference#global-administrator) role
- Microsoft Entra ID [*Compliance Administrator*](/en-us/azure/active-directory/roles/permissions-reference#compliance-administrator) role
- Microsoft Purview portal [*Organization Management*](/en-us/microsoft-365/security/office-365-security/scc-permissions) role group
- Microsoft Purview portal [*Compliance Administrator*](/en-us/microsoft-365/security/office-365-security/scc-permissions) role group
- *Communication Compliance* role group
- *Communication Compliance Admins* role group

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Members of the following roles have the same solution permissions included with the *Communication Compliance Admins* role group:

- Microsoft Entra ID *Global Administrator*
- Microsoft Entra ID *Compliance Administrator*
- Microsoft Purview portal *Organization Management*
- Microsoft Purview portal *Compliance Administrator*

Important

Make sure you always have at least one user in the *Communication Compliance* or *Communication Compliance Admins* role groups (depending on the option you choose) so that your Communication Compliance configuration doesn't get in to a 'zero administrator' scenario if specific users leave your organization.

Depending on how you want to manage Communication Compliance policies and alerts, assign users to specific role groups to manage different sets of Communication Compliance features. You can assign users with different compliance responsibilities to specific role groups to manage different areas of Communication Compliance features. Or you might decide to assign all user accounts for designated administrators, analysts, investigators, and viewers to the *Communication Compliance* role group. Use a single role group or multiple role groups to best fit your compliance management requirements.

Important

After configuring your role groups, it might take up to 30 minutes for the role group permissions to apply to assigned users across your organization.

Choose from these solution role group options when configuring and managing Communication Compliance:

| Actions | Communication Compliance | Communication Compliance Admins | Communication Compliance Analysts | Communication Compliance Investigators | Communication Compliance Viewers |
| --- | --- | --- | --- | --- | --- |
| Access and investigate alerts | Yes | No | Yes | Yes | No |
| Access reports | Yes | No | No | No | Yes |
| Configure policies and settings | Yes | Yes | No | No | No |
| Create message details report | Yes | No | No | Yes | No |
| Manage privacy settings and notice templates | Yes | Yes | No | No | No |
| Take advanced remediation actions: - Escalate for investigation - Remove message in Teams  - Download items and reports - Run Power Automate flows | Yes | No | No | Yes | No |
| View **Conversation** and **Translation** tabs for a specific message | Yes | No | No | Yes | No |
| View and export policy updates | Yes | Yes | No | No | Yes |

### Consider admin units if you want to scope user permissions to a region or department

You can use administrative units in Communication Compliance to scope user permissions to a particular geography or department. For example, a global company that has subsidiaries throughout the world might want to create an admin unit that provides a German scope for investigators so that they only see user activity for German users.

To use admin units in Communication Compliance, you must [first create the admin units](purview-admin-units) (if they aren't already created), then assign the admin units to members of role groups. After you assign admin units to members of role groups, those members become *restricted administrators* and have limited access to Communication Compliance settings, policies, and user data in the organization. Members who aren't assigned administrative units are *unrestricted administrators* and have access to all settings, policies, and user data.

Important

At this time, you can't use administrative units together with [adaptive scopes](purview-adaptive-scopes) in Communication Compliance. SharePoint sites and inactive mailboxes can only be segmented through adaptive scopes.

#### Effect of admin unit scoping on Communication Compliance roles

The following table shows how admin units, when enforced, affect each combination of Communication Compliance task and role.

Note

*Scoped*, in the following table, means that the admin actions for that role are limited by their assigned admin unit.

| Task | Scoped Communication Compliance | Scoped Communication Compliance Admins | Scoped Communication Compliance Analysts | Scoped Communication Compliance Investigators | Scoped Communication Compliance Viewers |
| --- | --- | --- | --- | --- | --- |
| Access and investigate alerts | Scoped | No | Scoped | Scoped | No |
| Access reports | No | No | No | No | No |
| Configure policies | Scoped | Scoped | No | No | No |
| Configure settings (including notice templates) | No | No | No | No | No |
| View and export audit logs | No | No | No | No | No |

### Option 1: Assign all compliance users to the Communication Compliance role group

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, select **Roles and groups**, then select **Role groups** in the left navigation pane.
3. Select the *Communication Compliance* role group, then select **Edit**.
4. Select **Choose users**, then select the checkboxes for all the users you want to add to the role group.
5. Select **Select**, then select **Next**.
6. Select **Save** to add the users to the role group, then select **Done**.

### Option 2: Assign users to specific Communication Compliance role groups

Use this option to assign users to specific role groups to segment Communication Compliance access and responsibilities among different users in your organization.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Role groups** in the left navigation pane.
3. Select one of the Communication Compliance role groups, then select **Edit**.
4. Select **Choose users**, then select the checkboxes for all the users you want to add to the role group.
5. Select **Select**, then select **Next**.
6. Select **Save** to add the users to the role group.
7. Select the next Communication Compliance role group, then repeat the previous steps for each required role group.
8. Select **Close** when you're done.

For more information about role groups and permissions, see [Permissions in the Microsoft Purview portal](purview-permissions).