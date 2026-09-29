---
layout: Conceptual
title: Permissions in the Microsoft Purview portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about managing role group and role permissions for users who perform tasks in the Microsoft Purview portal.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-07-30T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-permissions
audience: Admin
ms.topic: concept-article
ms.collection:
- purview-compliance
- essentials-manage
ms.custom:
- admindeeplinkCOMPLIANCE
- admindeeplinkEXCHANGE
- sfi-ga-nochange
- msecd-doc-authoring-1018
ai-usage: ai-assisted
locale: en-us
document_id: e31a3d4d-b25a-f0e3-709c-8cd1e2038719
document_version_independent_id: e31a3d4d-b25a-f0e3-709c-8cd1e2038719
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 0cd48463-f726-886c-d368-d8f50510db2b
---

# Permissions in the Microsoft Purview portal | Microsoft Learn

The [Microsoft Purview portal](purview-portal) supports direct management of permissions for users who perform tasks within [Microsoft Purview](purview). By using the **Roles and scopes** area in **Settings** for the portal, you can manage permissions for users across your Purview data security, data governance, and risk and compliance solutions. You can limit users to perform only specific tasks that you explicitly grant them access to.

Important

To view **Role groups** in the **Roles and scopes** area in the Microsoft Purview portal, users need to be a global administrator or need to be assigned the *Role Management* role (assigned only to the *Organization Management* role group). The *Role Management* role allows users to view, create, and modify role groups.

![Screenshot of the Role groups page in the Microsoft Purview portal showing role groups, Microsoft Entra roles, and administrative units.](media/purview-portal-roles.png)

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the [Global Administrator role](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) helps improve security for your organization. When planning your access control strategy, follow the [best practice](/en-us/entra/identity/role-based-access-control/best-practices) to manage access with the least privilege for your users.

## Microsoft Purview permissions

The Microsoft Purview portal uses the role-based access control (RBAC) permissions model. Most Microsoft 365 services use RBAC, so if you're familiar with the permission structure in these services, granting permissions in the Microsoft Purview portal is similar. The permissions you manage in the Microsoft Purview portal don't cover the management of all the permissions needed in each individual service. You still need to manage certain service-specific permissions in the admin center for the specific service. For example, if you need to assign permissions for archiving, auditing, and MRM retention policies, you need to manage these permissions in the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104).

### Solution-specific permissions

For specific Microsoft Purview solution permission guidance, see the following articles:

**Data security**

- [Data Loss Prevention](dlp-create-deploy-policy#permissions)
- [Data Security Investigations](data-security-investigations-permissions)
- [Data Security Posture Management](data-security-posture-management-get-started#step-1-assign-permissions)
- [Device Onboarding](device-onboarding-overview#permissions)
- [Sensitive Information Types - Custom](sit-test-a-sit#permissions-and-role-groups)
- [Sensitive Information Types - Exact Data Match](sit-get-started-exact-data-match-based-sits-overview#required-licenses-and-permissions)
- [Sensitivity Labels](get-started-with-sensitivity-labels#permissions-required-to-create-and-manage-sensitivity-labels)

**Data governance**

- [Collection Policies](collection-policies-create-deploy-policy#granular-roles-and-role-groups)
- [Data Classification - Activity Explorer](data-classification-activity-explorer#permissions)
- [Data Classification - Content Explorer](data-classification-content-explorer#permissions)
- [Data Classification - Data Explorer](data-classification-data-explorer#permissions)
- [Data governance - Classic Data Catalog](data-gov-classic-catalog-roles-permissions)
- [Data governance - Unified Catalog](data-governance-roles-permissions)
- [Data Lifecycle Management](get-started-with-data-lifecycle-management#permissions)
- [Records Management](get-started-with-records-management#permissions)

**Risk and compliance**

- [Adaptive Protection - Insider Risk Management](insider-risk-management-adaptive-protection#permissions-for-adaptive-protection)
- [Administrative Units](purview-admin-units#permissions-for-administrative-units)
- [Audit](audit-get-started#step-2-assign-permissions-to-search-the-audit-log)
- [Communication Compliance](communication-compliance-permissions)
- [Compliance Manager](compliance-manager-setup#set-user-permissions-and-assign-roles)
- [eDiscovery](edisc-permissions)
- [Information Barriers](information-barriers-policies#required-subscriptions-and-permissions)
- [Insider Risk Management](insider-risk-management-permissions)
- [Privileged Access Management](privileged-access-management-configuration)

**AI and Copilot**

- [Data Security Posture Management for AI](ai-microsoft-purview-permissions)
- [Security Copilot for Purview](/en-us/copilot/security/authentication#access-copilot-for-security-platform)
- [Triage Agent in Data Loss Prevention](copilot-in-purview-triage-dlp-agent-get-started#permissions-and-roles)
- [Triage Agent in Insider Risk Management](copilot-in-purview-triage-irm-agent-get-started#permissions-and-roles)

To view all of the default role groups that are available in the Microsoft Purview portal and the roles that are assigned to the role groups by default, see [Roles and role groups in the Microsoft Defender XDR and Microsoft Purview portals](/en-us/microsoft-365/security/office-365-security/scc-permissions?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

Managing permissions in the Microsoft Purview portal only gives users access to the compliance and governance features that are available within the Microsoft Purview portal. To grant permissions to other features that aren't in the Microsoft Purview portal, such as Exchange mail flow rules (also known as transport rules), use the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104).

The current governance roles and role groups cover only broad access to the Microsoft Purview Data Map and Unified Catalog. For more access, Microsoft Purview governance uses a combination of role groups, data access, and solution-specific permissions.

## Relationship of members, roles, and role groups

A role grants permissions to perform a set of tasks. For example, the *Case Management* role lets users work with eDiscovery cases.

A role group is a set of roles that enable users to do their jobs across compliance and governance solutions in the Microsoft Purview portal. For example, by adding users to the *Insider Risk Management* role group, designated administrators, analysts, investigators, and auditors get the necessary insider risk management permissions in a single group. The Microsoft Purview portal includes default role groups for tasks and functions for each compliance and governance solution that you need to assign people to. Generally, add individual users as members to the default role groups as needed.

![Diagram showing the relationship of role groups to roles and members, where role groups contain roles and members are assigned to role groups.](media/2a16d200-968c-4755-98ec-f1862d58cb8b.png)

## Microsoft Entra roles in the Microsoft Purview portal

The roles that appear in the Microsoft Entra ID section of the **Roles and scopes** area are Microsoft Entra roles, and global administrators can see this section. These roles align with job functions in your organization's IT group, making it easy to give a person all the permissions necessary to get their job done. You can view the users currently assigned to each role by selecting an admin role and viewing the role panel details. To manage members of a Microsoft Entra role, select **Manage members** in Microsoft Entra ID. This choice redirects you to the Azure management portal.

For more information about Microsoft Entra roles, see [Microsoft Entra built-in roles](/en-us/entra/identity/role-based-access-control/permissions-reference).

| Entra role | Description | Mapped Purview role groups |
| --- | --- | --- |
| **AI Administrator** | Manage all aspects of Microsoft 365 Copilot and AI-related enterprise services in Microsoft 365. For more information, see [AI Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator). | Compliance Manager AdministratorsData Security AI AdminsData Security AI Viewers |
| **Attack Payload Author** | Create attack payloads but not actually launch or schedule them. For more information, see [Attack Payload Author](/en-us/entra/identity/role-based-access-control/permissions-reference#attack-payload-author). | Attack Simulator Payload Authors |
| **Attack Simulation Administrator** | Create and manage all aspects of attack simulation creation, launch/scheduling of a simulation, and the review of simulation results. For more information, see [Attack Simulation Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#attack-simulation-administrator). | Attack Simulator Administrators |
| **Compliance Administrator** | Help your organization stay compliant with any regulatory requirements, manage eDiscovery cases, and maintain data governance policies across Microsoft 365 locations, identities, and apps. For more information, see [Compliance Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#compliance-administrator). | Compliance Administrator |
| **Compliance Data Administrator** | Keep track of your organization's data across Microsoft 365, make sure it's protected, and get insights into any issues to help mitigate risks. For more information, see [Compliance Data Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#compliance-data-administrator). | Compliance Data Administrator |
| **Global Administrator** | Access to all administrative features in all Microsoft 365 services. Only global administrators can assign other administrator roles. For more information, see [Global Administrator / Company Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator). | Data Catalog CuratorsData Estate Insights ReadersOrganization ManagementPurview Administrators |
| **Global Reader** | The read-only version of the **Global administrator** role. View all settings and administrative information across Microsoft 365. For more information, see [Global Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader). | Global Reader |
| **Security Administrator** | Control your organization's overall security by managing security policies, reviewing security analytics and reports across Microsoft 365 products, and staying up-to-speed on the threat landscape. For more information, see [Security Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator). | Security Administrator |
| **Security Operator** | View, investigate, and respond to active threats to your Microsoft 365 users, devices, and content. For more information, see [Security Operator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator). | Security Operator |
| **Security Reader** | View and investigate active threats to your Microsoft 365 users, devices, and content, but (unlike the Security operator) they don't have permissions to respond by taking action. For more information, see [Security Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader). | Security Reader |

For more information about other Entra roles and user assignment synchronization from Purview for authorizing long-running operations, see the [Purview Role Assignment Migrator](purview-role-assignment-migrator).

## Privileged Identity Management for Groups in the Microsoft Purview portal

[Microsoft Entra Privileged Identity Management (PIM)](/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups) for Groups provides user eligibility for just-in-time membership to groups assigned to Microsoft Entra roles. By using PIM for Groups, you can assign Microsoft Entra security groups to Microsoft Purview role groups in the Microsoft Purview portal. This assignment allows users to activate just-in-time access and then perform tasks in the Microsoft Purview portal. Unlike Microsoft Entra role assignments with Privileged Identity Management (PIM) in Microsoft Entra ID, you [can't manage just-in-time activations](/en-us/entra/id-governance/privileged-identity-management/pim-roles) by using direct user assignments to role groups in the Microsoft Purview portal.

## Role precedence and scope behavior

If you assign both an Entra role and a scoped Microsoft Purview role group assignment to a user or group (for example, a role group scoped to an Administrative Unit), the Entra role takes precedence at runtime. As a result, the user's effective permissions are unscoped, even if a scoped Microsoft Purview role group assignment also exists.

- **Example 1**: If you assign the *Compliance Administrator* role in Entra to a user and also assign a scoped *Compliance Administrator* role in Microsoft Purview, the Entra role overrides the scoped assignment. The user's effective access is *unscoped*, and they can access all entities available to that role without Administrative Unit scoping.
- **Example 2**: If you assign the *Global Reader* role in Entra to a user and assign a scoped *DLP Compliance Management* role in Microsoft Purview, any features or APIs that overlap between these roles grant the user *unscoped access* to the corresponding data.
- **Example 3**: When both scoped Microsoft Purview role assignments and Entra roles are present, Entra roles always take precedence, and scoping applied through Administrative Units doesn't restrict the user's effective permissions for overlapping capabilities.

## Temporary permissions

You can assign role groups and grant temporary access that automatically revokes permissions when they're no longer needed. Automatically expiring permissions let administrators assign an expiration date to Microsoft Purview role group assignments. When the configured expiration date is reached, the assignment is automatically removed and access is revoked without requiring manual action from an administrator. Actions that are already completed or in progress aren't affected, but any new operation is denied after the assignment expires. This approach helps organizations implement least-privilege access by reducing long-term access that's no longer needed.

Automatic expiring permissions are optional and are configured on a per-user assignment basis. Administrators can create temporary assignments with an expiration date, update an existing expiration date, extend an assignment, or remove the expiration to make the assignment permanent. A minimum expiration period of one day and maximum expiration period of two years can be selected from the current date in the local time zone of the administrator who sets the expiration.

Role group assignments are evaluated independently. If a user receives the same role group through both an individual assignment and a security group assignment, each assignment retains its own expiration date. Access remains active as long as one of the assignments is still valid. Assigning a role group to a security group also means changes to that group's membership update any added users with the expiration date associated with the assigned role group. The **My Permissions** page displays the latest expiration date across active assignments. The expiration date is recorded as part of the [audit logs](audit-log-activities#microsoft-purview-permission-activities) for Microsoft Purview permissions when the date is added or updated by the admin. You don't receive a notification before permissions expire, nor are any additional audit logs are generated when a user's temporary permissions expires.

Important

All built-in and custom role groups except the following support automatic expiring permissions:

- eDiscovery Administrator
- eDiscovery Manager

## Manage role groups

The following sections describe how to add, remove, create, update, and delete role groups in the Microsoft Purview portal.

### Add users or groups to a Microsoft Purview built-in role group

Complete the following steps to add users or groups to a Microsoft Purview role group:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) by using credentials for an admin account assigned the *Role management* role. Go to **Settings** &gt; **Roles and scopes** to view and manage compliance and governance roles in your organization.
2. Select **Role groups**.
3. On **Role groups for Microsoft Purview solutions**, select a Microsoft Purview role group you want to add users to. Select **Edit** on the control bar.
4. On **Edit members of the role group**, select **Choose users** or **Choose groups**.

    Important

    Security groups are supported only in Microsoft 365 commercial cloud organizations.
5. Select the check box for all users or groups you want to add to the role group.
6. Select **Select**.
7. If the selected users or groups need organization-wide access as part of this role group assignment, go to step 11.
8. If the selected users or groups need temporary access, select the users or groups and select **Edit expiration**.
9. If the selected users or groups need to be assigned to administrative units, select the users or groups and select **Assign admin units**.
10. On **Assign admin units**, select the check box for all the administrative units you want to assign to the users or groups. Select **Select**.
11. Select **Next** and **Save** to add the users or groups to the role group. Select **Done** to complete the steps.

### Remove users or groups from a Microsoft Purview built-in role group

To remove users or groups from a Microsoft Purview role group, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) by using credentials for an admin account assigned the *Role management* role. Go to **Settings** &gt; **Roles and scopes** to view and manage compliance and governance roles in your organization.
2. Select **Role groups**.
3. On **Role groups for Microsoft Purview solutions**, select a Microsoft Purview role group that you want to remove users or groups from. Select **Edit** on the control bar.
4. On **Edit members of the role group**, select the check box for all users or groups you want to remove from the role group.
5. Select **Remove members**, and then select **Next**.
6. Select **Save** to remove the users or groups from the role group. Select **Done** to complete the steps.

### Create a custom Microsoft Purview role group

Complete the following steps to create a custom Microsoft Purview role group:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) by using credentials for an admin account assigned the *Role management* role. Go to **Settings** &gt; **Roles and scopes** to view and manage compliance and governance roles in your organization.
2. Select **Role groups**.
3. On **Role groups for Microsoft Purview solutions**, select **Create role group**.
4. On **Name the role group**, enter a name for the custom role group in the **Name** field. You can't change the name of the role group after you create it. If needed, enter a description for the custom role group in the **Description** field. Select **Next** to continue.
5. On **Add roles to the role group**, select **Choose roles**.
6. Select the checkboxes for the roles to add to the custom role group. Select **Select**.
7. Select **Next** to continue.
8. On **Add members to the role group**, select **Choose users** (or **Choose groups** if applicable).

    Important

    Security groups are supported only in Microsoft 365 commercial cloud organizations.
9. Select the checkboxes for the users (or groups) to add to the custom role group. Select **Select**.
10. Select **Next** to continue.
11. If the selected users or groups need organization-wide access as part of this role group assignment, go to step 15.
12. If the selected users or groups need temporary access, select the users or groups and select **Edit expiration**.
13. If the selected users or groups need to be assigned to administrative units, select the users or groups and select **Assign admin units**.
14. On **Assign admin units**, select the check box for all the administrative units you want to assign to the users or groups. Select **Select**.
15. Select **Next**.
16. On **Review the role group and finish**, review the details for the custom role group. If you need to edit the information, select **Edit** in the appropriate section. When all the settings are correct, select **Create** to create the custom role group or select **Cancel** to discard the changes and not create the custom role group.

### Update a custom Microsoft Purview role group

Complete the following steps to update a custom Microsoft Purview role group:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) by using credentials for an admin account assigned the *Role management* role. Go to **Settings** &gt; **Roles and scopes** to view and manage compliance and governance roles in your organization.
2. Select **Role groups**.
3. On **Role groups for Microsoft Purview solutions**, select a Microsoft Purview role group you want to update, and then select **Edit** on the control bar.
4. On **Name the role group**, update the description for the custom role group in the **Description** field. You can't change the name of the custom role group. Select **Next**.
5. On **Edit roles of the role group**, select **Choose roles** to add roles to update the roles assigned to the role group. You can also select any of the currently assigned roles and select **Remove roles** to remove the roles from the role group. After you update the roles, select **Next**.
6. On **Edit members of the role group**, select **Choose users** or **Choose groups**to add users or groups assigned to the role group.
    1. To change the expiration for the selected users or groups, select any of the currently assigned user or groups and select **Edit expiration**.
    2. To update the administrative units for users or groups, select any of the currently assigned user or groups and select **Assign admin units**. You can also select any of the currently assigned users and groups and select **Remove members** to remove the users or groups from the role group. After you update the members, select **Next**.
7. On **Review the role group and finish**, review the details for the custom role group. If you need to edit the information, select **Edit** in the appropriate section. When all the settings are correct, select **Save** to update the custom role group or select **Cancel** to discard the changes and not update the custom role group.

### Delete a custom Microsoft Purview role group

Complete the following steps to delete a custom Microsoft Purview role group:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) by using credentials for an admin account assigned the *Role management* role. Go to **Settings** &gt; **Roles and scopes** to view and manage compliance and governance roles in your organization.
2. Select **Role groups**.
3. On **Role groups for Microsoft Purview solutions**, select a Microsoft Purview role group you want to delete, then select **Delete** on the control bar.
4. On **Delete role group**, select **Delete** to delete the role group or select **Cancel** to cancel the deletion process.