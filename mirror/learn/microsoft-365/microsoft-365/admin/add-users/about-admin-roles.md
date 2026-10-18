---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: About administrator roles in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: deniseb
author: denisebmsft
manager: dansimp
ms.date: 2026-10-07T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: microsoft-365-admin
ms.localizationpriority: high
ms.collection:
- Tier1
- M365-subscription-management
- Adm_O365
- Adm_TOC
description: Learn about administrator roles, such as the global administrator role, or the service administrator role. Roles map to specific business functions and give permissions to do specific tasks in the Microsoft 365 admin center.
customer-intent: As an administrator, I want to understand administrator roles that are available with my Microsoft 365 for business subscription.
ms.custom: admin-center-experience
locale: en-us
document_id: f18d8345-78f3-0b16-f585-1e53f49d138f
document_version_independent_id: 015e98be-2db5-11a3-9abc-6f89b44c3f96
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/about-admin-roles.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/about-admin-roles
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/about-admin-roles.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 056101d9-f115-b686-6fea-3bb9bd52419a
---

# About administrator roles in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

> 
> Check out [Microsoft 365 small business help](https://go.microsoft.com/fwlink/?linkid=2197659) on YouTube. These resources are especially helpful for small business admins who are new to Microsoft 365.

To perform tasks like adding users, assigning licenses, or configuring services, you need an administrator role in Microsoft 365 for business. Your Microsoft 365 or Office 365 subscription includes a set of administrator roles that you can assign in the [Microsoft 365 admin center](https://admin.microsoft.com). Each administrator role corresponds to common business functions and enables people in your organization to complete specific tasks in the admin centers. This article provides an overview of administrator roles, security guidelines to keep in mind, and links to related content.

## Watch: What is an admin?

Check out this video and others on our [YouTube channel](https://go.microsoft.com/fwlink/?linkid=2198028).

1. Go to the [Microsoft 365 admin center](https://admin.microsoft.com) and sign in. If you can access the Microsoft 365 admin center, you're an administrator, and you can proceed to the next step.
2. In the left navigation pane, select **Users** &gt; **Active users**. (Or go directly to the [Active users page](https://go.microsoft.com/fwlink/p/?linkid=834822).)
3. Select the user account for the person who you want to make an administrator. The user's details appear in the right dialog box.

## Before you begin

The [Microsoft 365 admin center](https://go.microsoft.com/fwlink/?linkid=2024339) lets you manage Microsoft Entra roles and Microsoft Intune roles. However, these roles are a subset of the roles available in the Microsoft Entra admin center and the Microsoft Intune admin center.

- For the full list of detailed Microsoft Entra role descriptions you can manage in the Microsoft 365 admin center, see Administrator role permissions in [Microsoft Entra built-in roles](/en-us/azure/active-directory/roles/permissions-reference).
- For the full list of detailed Microsoft Intune role descriptions you can manage in the Microsoft 365 admin center, see [Role-based access control (RBAC) with Microsoft Intune](/en-us/mem/intune/fundamentals/role-based-access-control).

For more information on assigning roles in the Microsoft 365 admin center, see [Assign admin roles](assign-admin-roles).

Important

Microsoft recommends that you use roles with the fewest permissions, and that you limit the number of users who have administrative permissions. See [Least privileged roles by task in Microsoft Entra ID](/en-us/entra/identity/role-based-access-control/delegate-by-task).

## Security guidelines for assigning roles

Because administrators have access to sensitive data and files, follow these guidelines to keep your organization's data more secure.

| Recommendation | Why it's important |
| --- | --- |
| Have as few global administrators as possible | Global Administrators have almost unlimited access to your organization's settings and most of its data. Limit the number of Global Administrators as much as possible. A Global Administrator could inadvertently lock their account and require a password reset. Either another Global Administrator or a Privileged Authentication Administrator can reset a Global Administrator's password. Therefore, have at least a Privileged Authentication administrator in case a Global Administrator is locked out of their account. |
| Assign the *least permissive* role | Assigning the *least permissive* role means giving administrators only the access they need to get the job done. For example, if you want someone to reset user passwords, don't assign the unlimited global administrator role. Instead, assign a limited administrator role, like Password Administrator or Helpdesk Administrator. See [Least privileged roles by task in Microsoft Entra ID](/en-us/entra/identity/role-based-access-control/delegate-by-task). |
| Require multifactor authentication (MFA) for administrators | Require MFA for all of your users, especially administrators. MFA makes users use a second method of identification to verify their identity. Administrators can access user data, such as their name, email address, location, and so on. If you require MFA, even if the administrator's password gets compromised, the password alone isn't sufficient to sign in without another method of identification. When you turn on MFA, the next time the user signs in, they need to provide an alternate email address and phone number for account recovery. [Set up multifactor authentication](../security-and-compliance/set-up-multi-factor-authentication) |

If you get a message in the Microsoft 365 admin center that indicates you don't have permission to edit a setting or page, it's because you're assigned to a role that doesn't have that permission. In this case, take one or more of the following actions:

- Talk to another administrator to assign you the correct role.
- Learn more about how administrator roles are assigned. See [Assign administrator roles](assign-admin-roles).
- [Contact support for Microsoft 365 for business](../get-help-support).

## Commonly used Microsoft 365 admin center roles

To view administrator roles, follow these steps:

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), go to [Role assignments](https://go.microsoft.com/fwlink/p/?linkid=2097861).
2. Select any role to open its detail pane.
3. Select the **Permissions** tab to view the detailed list of what administrators assigned that role have permissions to do.
4. Select the **Assigned** or **Assigned admins** tab to add users to roles.

    To view the full list of roles, go to the bottom of the list and select **Show all by Category**. For detailed information, including the cmdlets associated with a role, see [Microsoft Entra built-in roles](/en-us/azure/active-directory/roles/permissions-reference).

### Administrator roles and who should be assigned

The following table lists administrator roles and information about who should be assigned these roles. To see the full list of roles, visit [Microsoft Entra built-in roles](/en-us/azure/active-directory/roles/permissions-reference).

| Administrator role | Who should be assigned this role? |
| --- | --- |
| [AI Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator) | This role provides AI- and agent-scoped administration, but doesn't grant broad tenant-wide Microsoft 365 workload administration. Assign the AI Administrator role to users who need to do the following tasks:<br>- Manage all aspects of Microsoft Copilot<br>- Manage AI-related enterprise services, extensibility, and Copilot agents on the Integrated Apps page in the Microsoft 365 admin center<br>- Manage agent instances and agent identities using available administrator experiences, such as upload, publish, install, activate, and block or unblock agents where supported<br>- Grant tenant-wide consent for apps and agents requesting permissions except Microsoft Graph application permissions. Apps or agents requiring Microsoft Graph application permissions continue to require Global Administrator approval.<br>- View usage reports, adoption insights, and organizational insight<br>- View basic subscription properties<br>- View agents flagged as risky in [Identity Protection for agents](/en-us/entra/id-protection/concept-risky-agents)<br>- Allow users to install an app or install an app for users in the organization if the app doesn't require permission<br>- Read and configure Microsoft Azure and Microsoft 365 service health dashboards<br>- Create and manage support requests in the Microsoft Azure portal and the Microsoft 365 admin center<br><br>The AI Administrator doesn't manage human user licensing or user sign-in sessions. Some high-privilege permission or consent scenarios (for example, certain Microsoft Graph application permissions) might still require a Global Administrator or Privileged Role Administrator. |
| [AI Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-reader) | This role is intended for visibility, monitoring, and reporting, but not administration. Assign the AI Reader role to users who need to view the features and settings in the admin centers that the AI Administrator can view. The AI Reader can't edit any settings. Assign the AI Reader role to users who need to do the following tasks: <br>- Read all aspects of Microsoft Copilot<br>- Read all properties of agent identities, agent identity blueprint principals, and agent identity blueprints<br>- Read and configure Microsoft Azure and Microsoft 365 service health dashboards<br><br>The AI Reader role is a read-only role and can't create, publish, approve, activate, deactivate, or modify agents. The AI Reader can't manage agent availability, permissions, policies, licenses, consent, or support requests. |
| [Application Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) | Assign the Application Administrator role to users who need to create and manage all aspects of enterprise applications, application registrations, and application proxy settings. Users assigned to this role aren't added as owners when creating new application registrations or enterprise applications. This role also grants the ability to consent for delegated permissions and application permissions, except for application permissions for Azure AD Graph and Microsoft Graph. |
| [Billing Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator) | Assign the Billing Administrator role to users who make purchases, manage subscriptions and service requests, and monitor service health. Billing administrators can also:<br>- Manage all aspects of billing<br>- Create and manage support tickets in the Azure portal |
| [Exchange Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator) | Assign the Exchange Administrator role to users who need to view and manage your user's email mailboxes, Microsoft 365 Groups, and Exchange Online. Exchange Administrators can also:<br>- Recover deleted items in a user's mailbox<br>- Set up "Send As" and "Send on behalf" delegates |
| [Fabric Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#fabric-administrator) | Assign the Fabric Administrator role to users who need to do the following tasks:<br>- Manage all admin features for Microsoft Fabric and Power BI<br>- Report on usage and performance<br>- Review and manage auditing |
| [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) | This is a privileged role. Global Administrators can view Directory Activity logs and elevate their access to manage all Microsoft Azure subscriptions and management groups. Global Administrators can get full access to all Microsoft Azure resources using their respective Microsoft Entra tenant.The person who purchased a subscription for your organization and signed up for Microsoft online services is a Global Administrator automatically. There can be more than one Global Administrator in your organization.Users with this role have access to all administrative features in Microsoft Entra ID, and services that use Microsoft Entra identities like the Microsoft Defender portal, the Microsoft Purview portal, Exchange Online, SharePoint Online, and Skype for Business Online. Global Administrators can:<br>- Reset passwords for any user and all other administrators<br>- Manage purchasing of your organization's subscriptions and products<br>- Reset passwords for all users<br>- Add and manage domains<br>- Unblock another Global Administrator<br><br>Additionally, only Global Administrators can view and manage subscriptions purchased through a Partner. A Global Administrator can't remove their own Global Administrator assignment. This limitation is to prevent a situation where an organization has zero Global Administrators. |
| [Global Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) | Assign the Global Reader role to users who need to perform the following tasks: <br>- View agent overview and agents in the registry for their tenant, with details around the metrics with all the richness of agent metadata details<br>- View administrator features and settings in admin centers that the Global Administrator can view.<br><br>The Global Reader can't edit any settings.  For subscriptions purchased through a partner, the Global Reader role isn't available. |
| [Groups Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator) | Assign the Groups Administrator role to users who need to manage all groups settings across admin centers, including the Microsoft 365 admin center and Microsoft Entra admin center. Groups Administrators can:<br>- Create, edit, delete, and restore Microsoft 365 Groups<br>- Create and update group creation, expiration, and naming policies<br>- Create, edit, delete, and restore Microsoft Entra security groups<br><br>Also see [Manage who can create Microsoft 365 Groups](/en-us/previous-versions/microsoft-365/solutions/manage-creation-of-groups). |
| [Helpdesk Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator) | Assign the Helpdesk Administrator role to users who need to do the following tasks:<br>- Reset passwords<br>- Force users to sign out<br>- Manage service requests<br>- Monitor service health<br><br> The Helpdesk admin can only help users who aren't administrator users and users who are assigned these roles: Directory reader, Guest inviter, Helpdesk admin, Message Center reader, and Reports reader. |
| [License Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator) | Assign the License Administrator role to users who need to assign and remove licenses from users and edit their usage location. License administrators can also:<br>- Reprocess license assignments for group-based licensing<br>- Assign product licenses to groups for group-based licensing |
| [Message Center Privacy Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#message-center-privacy-reader) | Assign the Message Center Privacy Reader role to users who need to read privacy and security messages and updates in the Microsoft 365 Message Center.Message Center privacy readers might get email notifications related to data privacy, depending on their preferences, and they can unsubscribe using Message Center preferences.Only Global Administrators and Message Center Privacy Readers can read data privacy messages.This role has no permission to view, create, or manage service requests.Message Center privacy readers can also: <br>- Monitor all notifications in the Message Center, including data privacy messages<br>- View groups, domains, and subscriptions |
| [Message Center Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#message-center-reader) | Assign the Message Center Reader role to users who need to do the following tasks: <br>- Monitor Message Center notifications<br>- Get weekly email digests of Message Center posts and updates<br>- Share Message Center posts<br>- Have read-only access to Microsoft Entra services, such as users and groups |
| [Microsoft Graph Data Connect Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#microsoft-graph-data-connect-administrator) | Assign the Microsoft Graph Data Connect Administrator role to users who need to do the following tasks: <br>- Access the full set of administrative capabilities of Microsoft Graph Data Connect<br>- Manage Microsoft Graph Data Connect settings in a tenant<br>- Enable or disable the Microsoft Graph Data Connect service<br>- Configure dataset workload selections in Microsoft Graph Data Connect<br>- Configure cross-tenant data movement settings in Microsoft Graph Data Connect<br>- View, approve, or deny application authorization requests for Microsoft Graph Data Connect<br>- View, create, update, or delete application registrations for Microsoft Graph Data Connect |
| [Migration Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#microsoft-365-migration-administrator) | Assign the Microsoft 365 Migration Administrator role to users who need to do the following tasks: <br>- Use Migration Manager in the Microsoft 365 admin center to manage content migration to Microsoft 365, including Microsoft Teams, OneDrive, and SharePoint sites, from various sources such as Google Drive, Dropbox, Box, and Slack<br>- Select migration sources, create migration inventories (such as Google Drive user lists), schedule and execute migrations, and download reports<br>- Create new SharePoint sites or Teams teams if the destination sites or teams don't already exist, create SharePoint lists under the SharePoint admin sites, and create and update items in SharePoint lists<br>- Manage migration project settings and migration lifecycle for tasks and manage permission mappings from source to destination.<br><br>With this role, you can only migrate from Google Drive, Box, Dropbox, Egnyte, and Slack. This role doesn't allow you to migrate from file share sources from the SharePoint admin center. Use the SharePoint admin to migrate from file share sources. |
| [Office Apps Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#office-apps-administrator) | Assign the Office Apps Administrator role to users who need to do the following tasks:<br>- Use the Cloud Policy service for Microsoft 365 to create and manage cloud-based policies.<br>- Create and manage service requests<br>- Manage the What's New content that users see in their apps in Microsoft 365<br>- Monitor service health<br>- Manage Office Scripts settings |
| [Organizational Messages Approver](/en-us/entra/identity/role-based-access-control/permissions-reference#organizational-messages-approver) | Assign the Organizational Messages Approver role to users who need to review, approve, or reject new organizational messages for delivery in the Microsoft 365 admin center before they're sent to users through Microsoft product surfaces. |
| [Organizational Data Source Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference?branch=pr-en-us-6603#organizational-data-source-administrator) | Assign the Organizational Data Source Administrator role to users who need to do the following tasks: <br>- Manage settings related to ingesting and managing organizational data for Microsoft 365 and Microsoft Viva applications.<br>- Upload, update, and delete the ingested organizational data in Microsoft 365 and Microsoft Viva applications<br>- Export organizational data from the authorized applications |
| [Organizational Messages Writer](/en-us/entra/identity/role-based-access-control/permissions-reference#organizational-messages-writer) | Assign the Organizational Messages Writer role to users who need to write, publish, manage, and review the organizational messages for end-users through Microsoft product surfaces. |
| [Password Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#password-administrator) | Assign the Password Administrator role to a user who needs to reset passwords for users. |
| [People Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#people-administrator) | Assign the People Administrator role to users who need to do the following tasks: <br>- Update profile photos for all users including administrators<br>- Update people settings for all users (pronouns, name pronunciation, and profile card settings) |
| [Power Platform Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#power-platform-administrator) | Assign the Power Platform Administrator role to users who need to do the following tasks: <br>- Manage all admin features for Power Apps, Power Automate, Power BI, Microsoft Fabric, and Microsoft Purview Data Loss Prevention<br>- Create and manage service requests<br>- Monitor service health |
| [Reports Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader) | Assign the Reports Reader role to users who need to do the following tasks: <br>- View agent overview and agents in the registry for their tenant, with details around the metrics with all the richness of agent metadata details<br>- View usage data and the activity reports in the Microsoft 365 admin center<br>- Get access to the Power BI adoption content pack<br>- Get access to sign-in reports and activity in Microsoft Entra ID<br>- View data returned by Microsoft Graph reporting API |
| [Search Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#search-administrator) | Assign the Search Administrator role to users who need to create and manage search result content and define query settings for improved search results within the organization. The Search admin manages the Microsoft search configuration and can perform all the content-management tasks that a Search editor can. |
| [Security Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) | Assign the Security Administrator role to users who manage security controls and monitoring across Microsoft 365.This privileged role provides access to security and compliance portals and read visibility into agents in the Microsoft 365 admin center for investigation and risk assessment, without allowing agent publishing or lifecycle management. |
| [Security Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) | Assign the Security Reader role to users who need access to security data and monitoring insights across Microsoft 365.This privileged role provides access to security and compliance portals, including Microsoft Defender, Microsoft Entra (ID Protection, Privileged Identity Management, sign-in reports, and audit logs), and Microsoft Purview.In the Microsoft 365 admin center, this role provides read-only visibility into agents and metadata for security review and compliance purposes, without allowing agent publishing or lifecycle management. |
| [Service Support Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#service-support-administrator) | Assign the Service Support Administrator role as another role to administrators or users who need to do the following tasks in addition to their usual admin role:<br>- Open and manage service requests<br>- View and share Message Center posts<br>- Monitor service health |
| [SharePoint Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator) | Assign the SharePoint Administrator role to users who need to access and manage the SharePoint admin center. SharePoint Administrators can also:<br>- Create and delete sites<br>- Manage site collections and global SharePoint settings |
| [SharePoint Advanced Management Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-advanced-management-administrator) | Assign the SharePoint Advanced Management Administrator role to users who need to perform the following kinds of tasks:<br>- Use the [SharePoint Admin Agent](/en-us/sharepoint/content-governance-agent)<br>- Manage all aspects of [SharePoint Advanced Management](/en-us/sharepoint/advanced-management)<br>- View names, paths, and URLs of files, folders, libraries, documents, and lists within SharePoint sites, without accessing file or item content<br>- Remove permissions from files, folders, libraries, documents, and lists within SharePoint sites |
| [Teams Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#teams-administrator) | Assign the Teams Administrator role to users who need to access and manage the Teams admin center. A Teams Administrator can also:<br>- Manage meetings<br>- Manage conference bridges<br>- Manage all org-wide settings, including federation, teams upgrade, and teams client settings |
| [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) | Assign the User Administrator role to users who need to do the following tasks:<br>- Create, disable, or enable user accounts<br>- Add users and groups<br>- Assign licenses<br>- Manage most users properties<br>- Create and manage user views<br>- Update password expiration policies<br>- Manage service requests<br>- Monitor service health<br>- Update (FIDO) device keys<br>- View a summary of agents across your tenant to gain visibility into overall usage and adoption trends |
| [User Experience Success Manager](/en-us/entra/identity/role-based-access-control/permissions-reference#user-experience-success-manager) | Assign the User Experience Success Manager role to users who need to perform the following tasks:<br>- Access Experience Insights, Adoption Score, and the Message Center in the Microsoft 365 admin center.<br>- View a summary of agents across your tenant to gain visibility into overall usage and adoption trends<br>- This role includes the permissions of the Usage Summary Reports Reader role. |
| [Viva Glint Tenant Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#viva-glint-tenant-administrator) | Assign the Viva Glint Tenant Administrator role to users who manage the Viva Glint app. See [Assign Viva Glint Tenant and Service Administrators](/en-us/viva/glint/setup/post-provisioning-next-steps). |

Also see [Check admin roles in your organization](/en-us/microsoft-365/admin/add-users/assign-admin-roles#check-admin-roles-in-your-organization).

## Permissions based on administrator roles and group type in the Microsoft 365 administrator center

| Administrator | Microsoft 365 Groups | Security Groups | Distribution Groups | Mail Enabled Security Groups |
| --- | --- | --- | --- | --- |
| [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) | Create, Read, Update, Delete | Create, Read, Update, Delete | Create, Read, Update, Delete | Create, Read, Update, Delete |
| [Global Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) | Read | Read | Read | Read |
| [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) | Create, Read, Update, Delete(Can't update Exchange Online properties) | Create, Read, Update, Delete | Read | Read |
| [Exchange Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator) | Create, Read, Update, Delete | Read, Update (only groups they own), Delete (only groups they own) | Create, Read, Update, Delete | Create, Read, Update, Delete |
| [Teams Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#teams-administrator) | Create, Read, Update, Delete(Can't update Exchange Online properties) | Create, Read, Update, Delete (only groups they own) | Read | Read |
| [SharePoint Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator) | Create, Read, Update, Delete(Can't update Exchange Online properties) | Create, Read, Update, Delete -*only groups they own* | Read | Read |
| [Billing Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator) | Read | Read | Read | Read |
| [Service Support Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#service-support-administrator) | Read | Read | Read | Read |
| [Groups Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator) | Create, Read, Update, Delete(Can't update Exchange Online properties) | Create, Read, Update, Delete | Read | Read |
| [AI administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator) | Read | Read | Read | Read |

## Delegated administration for Microsoft Partners

If you're working with a Microsoft partner, you can assign them administrator roles. They can assign users in your company, or their company, administrator roles. Assign administrator roles to partners if they're setting up and managing your online organization for you.

A partner can assign these roles:

- **Admin Agent** Privileges equivalent to a global administrator, except for managing multifactor authentication through the Partner Center.
- **Helpdesk Agent** Privileges equivalent to a helpdesk admin.

Before the partner can assign these roles to users, you must add the partner as a delegated administrator to your account. The partner has to be an authorized partner. The partner sends you an email to ask if you want to give them permission to act as a delegated admin. For instructions, see [Authorize or remove partner relationships](../misc/add-partner).

## Volume licensing roles

Volume licensing (VL) agreement administrators access their volume licenses in the [Microsoft 365 admin center](https://admin.microsoft.com).

- VL Administrators don't have permissions to any other admin center information or functionality outside the VL section.
- Global administrators don't assign any VL roles and don't need to assign any administrator role to a VL Administrator for them to access the VL agreement.
- Global administrators don't have access to VL information or functionality in the admin center, unless a VL Administrator assigns them to a VL role.

For more information, see [Manage volume licensing user roles](../../commerce/licenses/manage-user-roles-vl) or [contact the Volume Licensing Support team](../../commerce/licenses/contact-vl-support).