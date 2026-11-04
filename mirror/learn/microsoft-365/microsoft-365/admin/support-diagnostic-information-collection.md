---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Understand Microsoft 365 Support Case Creation and Data Access - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/support-diagnostic-information-collection?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: frankroj
author: frankroj
manager: dansimp
ms.reviewer: onatwil; ramical
ms.date: 2026-11-02T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-admin
ms.localizationpriority: medium
ms.collection: Tier1
description: Learn what happens during the Microsoft 365 support case lifecycle, including data access for Microsoft Support engineers and audit log events. Review now.
customer-intent: As an IT leader, I want to understand the Microsoft Support case lifecycle and what to expect.
locale: en-us
document_id: c41eb18d-7e74-dc8b-2420-42aaa9043a75
document_version_independent_id: c41eb18d-7e74-dc8b-2420-42aaa9043a75
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/support-diagnostic-information-collection.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/support-diagnostic-information-collection
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/support-diagnostic-information-collection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: deb8bee0-a945-14d6-dd48-27dc24695e70
---

# Understand Microsoft 365 Support Case Creation and Data Access - Microsoft 365 admin | Microsoft Learn

Microsoft is improving your visibility into Microsoft Support's read-only access to your data during the Microsoft 365 support case lifecycle. When you create a support request, you grant [cross-tenant access](/en-us/entra/external-id/cross-tenant-access-overview) to Microsoft Support to access the information needed to troubleshoot the issue. This access is time bound and uses least-privileged access, in accordance with [Zero Trust Principles](/en-us/security/zero-trust/zero-trust-overview).

This article describes what you see in your Microsoft Entra audit logs when:

- A Microsoft 365 Support case is created
- A Microsoft Support engineer works on your case
- A Microsoft 365 Support case is closed

This article also lists who can create support cases and what permissions are granted to Microsoft Support engineers.

Note

This article is designed for enterprise admins and IT pros.

If you're a business user and you need technical support, see [Get support for Microsoft 365 for business](get-help-support).

If you're a home user and you need help, see [Contact us](https://support.microsoft.com/contactus).

## What happens when a Microsoft 365 support case is created?

When a user with a role that can create support cases opens a case in the [Microsoft 365 admin center](https://admin.cloud.microsoft/), a cross-tenant access policy is created between your tenant and the Microsoft Support tenant if one doesn't already exist. These roles can create this support-specific policy even if they don't have permission to create or manage cross-tenant access policies for other organizations.

This permission is restricted to the Microsoft Support tenant. It doesn't grant general cross-tenant access-policy management permissions or change any broader permissions already provided by the user's assigned roles.

With the cross-tenant access policy in place, Microsoft Support can access the information that's needed and you can view details about their permission to access diagnostic data in your tenant. The cross-tenant access policy:

- Is restricted to the Microsoft Support tenant and the [Microsoft 365 Support Engineer role](/en-us/entra/identity/role-based-access-control/permissions-reference#microsoft-365-support-engineer).
- Appears in Microsoft Entra audit logs as created by the user who initiated the support case.

The level of access granted for the Microsoft Support tenant is captured as *Delegated Admin Service Provider Constraints*.

Microsoft Entra audit events are logged throughout the Microsoft 365 Support case lifecycle.

## What audit events are logged during a Microsoft Support case lifecycle?

Audit events are logged when:

- A Microsoft 365 support case is opened and the cross-tenant access policy is created.
- A Microsoft Support engineer works on the support case.
- A Microsoft 365 support case is closed.

This article describes audit events during a Microsoft Support case. To learn more about Microsoft Entra audit logs, see the following articles:

- [What are Microsoft Entra audit logs?](/en-us/entra/identity/monitoring-health/concept-audit-logs)
- [How to access activity logs in Microsoft Entra ID](/en-us/entra/identity/monitoring-health/howto-access-activity-logs)

### Audit events during support case creation

A user who doesn't have general cross-tenant access-policy management permissions can therefore appear in your audit logs as creating the Microsoft Support policy. This is expected when that user initiates the support-case workflow. Review the events alongside the corresponding support case and the Microsoft Support tenant ID listed in the following table.

When you create a support case, Microsoft Entra records the following audit events:

| **Order** | **Event** | **Actor** |
| --- | --- | --- |
| 1 | If it doesn't already exist, **Add a partner to cross-tenant access setting**.Adds the Microsoft Support tenant with Tenant ID `b4c546a4-7dac-46a6-a7dd-ed822a11efd3`. | Identity of the user who created the support case. |
| 2 | If it doesn't already exist, **Adding allowed assignable roles**.Adds the Microsoft 365 Support Engineer role only. | Identity of the user who created the support case. |

### Audit events when Microsoft Support works on your case

When a Microsoft Support engineer works on your support case, the following Microsoft Entra audit events are recorded:

| **Order** | **Event** | **Actor** |
| --- | --- | --- |
| 1 | If it doesn't exist already, **Add a Service Principal** for the Microsoft Support tenant. Microsoft Entra GDAP application. | - Service Principal for the Assist API application.<br>- For more information, see What is the Assist API application, and how do I find it in my tenant? |
| 2 | **Add member to role**. Group from Microsoft Support tenant is added to the Microsoft 365 Support Engineer role. | - Assist API application.<br>- App ID `2b8844d8-6c87-4fce-97a0-fbec9006e140`. |

### Audit events during support case closure

When your support case is closed, the following Microsoft Entra audit events are recorded:

| **Order** | **Event** | **Actor** |
| --- | --- | --- |
| 1 | **Add a service principal**.The Microsoft Entra GDAP application handles revocation. | - Assist API application.<br>- App ID `2b8844d8-6c87-4fce-97a0-fbec9006e140`. |
| 2 | **Deleting allowed assignable roles**. | - Microsoft Entra GDAP application.<br>- App ID `bc56af95-7a3b-459f-98a9-bd86532b0e89`. |
| 3 | **Delete partner specific cross-tenant access setting**. Removes the Microsoft Support tenant if there are no other active support cases or 30 days have elapsed since the most recent case was created. | - Microsoft Entra GDAP application.<br>- App ID `bc56af95-7a3b-459f-98a9-bd86532b0e89`. |

### What is the Assist API application, and how do I find it in my tenant?

Assist API is a Microsoft-owned application with the Application ID `2b8844d8-6c87-4fce-97a0-fbec9006e140`. In Microsoft Entra audit events, you can see the service principal ID of the Assist API application for your tenant. The service principal ID is unique to your tenant.

To find the service principal ID in your tenant, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. From the left navigation bar, select **Entra ID** to expand it, and then select **Enterprise Apps**.
3. In the **Enterprise applications | All applications** page, under **Manage**, select **All applications**.
4. Select the **Application Type ==** filter.
5. In the **Application type** window, select **All Applications** from the dropdown, and then select **Apply**.
6. In the **Search by application name or object ID** search box, search for the Application ID `2b8844d8-6c87-4fce-97a0-fbec9006e140`.

    Your unique service principal ID is displayed.

## What level of access does Microsoft Support have in my tenant?

The level of access is captured as *Delegated Admin Service Provider Constraints*, using the *Microsoft 365 Support Engineer* role. To see the read permissions that this role grants, see [Microsoft Entra built-in roles: Microsoft 365 Support Engineer](/en-us/entra/identity/role-based-access-control/permissions-reference#microsoft-365-support-engineer).

Note

Use the Microsoft 365 Support Engineer role only for Microsoft Support cases. Don't assign this role to other users in your organization.

For more information, see the following articles:

- [What's new in Microsoft Entra RBAC documentation](/en-us/entra/identity/role-based-access-control/whats-new).
- [Roles not shown in the Microsoft Entra admin center](/en-us/entra/identity/role-based-access-control/permissions-reference#roles-not-shown-in-the-portal).
- [Microsoft 365 Support Engineer role](/en-us/entra/identity/role-based-access-control/permissions-reference#microsoft-365-support-engineer).

## What information can Microsoft Support access?

Microsoft Support accesses only the information needed to troubleshoot and resolve your support case. Depending on the nature of your support request, the data that Microsoft Support can access falls under the categories listed in the following table:

| **Category** | **Type Of Data** | **Examples** |
| --- | --- | --- |
| **Support data** | All data you provide to Microsoft as part of a customer engagement to get support services. | - Support requests from customers and phone conversations, online chat sessions, or remote assistance sessions between support professionals and customers.<br>- Case notes and records related to support requests from customers.<br>- Data you provide to Microsoft as part of support activities. |
| **Account data** | Contact, billing, purchase, payment, and license information. | - Your provisioning information.<br>- Account configuration and billing data.<br>- Tenant administrator contact information, such as tenant administrator's name, address, e-mail address, phone number.<br>- Licensing and purchase information. |
| **System metadata** | Data generated in the course of running the service. | - Event logs.<br>- Access control logs.<br>- Account information belonging to Microsoft operations personnel.<br>- Microsoft server names and server IPs.<br>- Server patching and vulnerability data.<br>- Service configuration data.<br>- Telemetry (on-premises or cloud). |
| **Organization information** | Data that can be used to identify a particular tenant, deployment, or organization (generally configuration or usage data). | - Tenant ID (non-GUID).<br>- Tenant ID (GUID) due to the existence of many out of boundary Tenant ID to name mapping tables.<br>- Tenant usage data.<br>- Tenant IP addresses (IPv4), such as tenant's firewall IP address.<br>- Global prefix and subnet ID (first 64 bits of IPv6 address).<br>- Tenant domain name in e-mail address, such as `joe@contoso.com`.<br>- Mapping of organizational GUID to organization. |
| **Customer data** | Data that directly identifies or could be used to identify the authenticated user of a Microsoft service. | - User-specific IP address (IPv4).<br>- User principal name (`joe@company.com`).<br>- Address book data.<br>- User's machine name.<br>- SIP URI. |
| **Pseudonymous identifiers** | An identifier created by Microsoft tied to the user of a Microsoft service. | - User GUIDs or PUIDs.<br>- Session IDs. |

## How long does Microsoft Support have access to tenant data?

Microsoft Support loses access to your tenant data when the support tenant is removed from your cross-tenant access settings. This process is automated and directly linked to the lifecycle of support cases within your tenant.

- If a case is open for more than 30 days, the system automatically revokes access, provided there aren't any other, newer cases opened. You can restore access by opening a new support case or reopening a closed case.
- You can revoke access at any time by deleting the Microsoft Support tenant partner in your cross-tenant access settings. To remove the Microsoft Support tenant, which is listed as Office 365 with Tenant ID `b4c546a4-7dac-46a6-a7dd-ed822a11efd3`, see [Cross-tenant access settings: Remove an organization](/en-us/entra/external-id/cross-tenant-access-settings-b2b-collaboration#remove-an-organization).

Caution

If you revoke access manually, Microsoft Support loses the ability to help resolve your support cases.

## What happens when a support case is closed?

When a support case is closed, Microsoft checks if there are any other active support cases open. If there are no other active support cases, Microsoft initiates the access revocation process, which includes multiple steps.

## How long is diagnostic data retained in Microsoft systems?

Microsoft retains diagnostic data related to your support case for up to 28 days after collection. After this period, Microsoft deletes the data.

For information about how Microsoft protects your data, see [Privacy and data management overview](/en-us/compliance/assurance/assurance-privacy).

## Who can create support cases?

### Roles that can create support cases and the Microsoft Support access policy

Users assigned the following roles can create a Microsoft 365 support case and the cross-tenant access policy with the Microsoft Support tenant needed for that case.

| **Role name** | **Role (template) ID** |
| --- | --- |
| AI Administrator | d2562ede-74db-457e-a7b6-544e236ebb61 |
| [Application Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) | 9b895d92-2cd3-44c7-9d02-a6ac2d5ea5c3 |
| [Authentication Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator) | c4e39bd9-1100-46d3-8c65-fb160da0071f |
| [Authentication Policy Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) | 0526716b-113d-4c15-b2c8-68e3c22b9f80 |
| [Azure Information Protection Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#azure-information-protection-administrator) | 7495fdc4-34c4-4d15-a289-98788ce399fd |
| [Billing Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator) | b0f54661-2d74-4c50-afa3-1ec803f12efe |
| [Cloud Application Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator) | 158c047a-c907-4556-b7ef-446551a6b5f7 |
| [Compliance Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#compliance-administrator) | 17315797-102d-40b4-93e0-432062caca18 |
| [Compliance Data Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#compliance-data-administrator) | e6d1a23a-da11-4be4-9570-befc86d067a7 |
| [Desktop Analytics Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#desktop-analytics-administrator) | 38a96431-2bdf-4b4c-8b6e-5d3d8abac1a4 |
| Domain Name Administrator | 8329153b-31d0-4727-b945-745eb3bc5f31 |
| [Dynamics 365 Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#dynamics-365-administrator) | 44367163-eba1-44c3-98af-f5787879f96a |
| Edge Administrator | 3f1acade-1e04-4fbc-9b69-f0302cd84aef |
| [Exchange Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator) | 29232cdf-9323-42fd-ade2-1d097af3e4de |
| [Fabric Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#fabric-administrator) | a9ea8996-122f-4c74-9520-8edcd192826c |
| [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) | 62e90394-69f5-4237-9190-012177145e10 |
| [Global Secure Access Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-secure-access-administrator) | ac434307-12b9-4fa1-a708-88bf58caabc1 |
| [Groups Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator) | fdd7a751-b60b-444a-984c-02652fe8fa1c |
| [Helpdesk Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator) | 729827e3-9c14-49f7-bb1b-9608f156bbb8 |
| [Hybrid Identity Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) | 8ac3fc64-6eca-42ea-9e69-59f4c7b60eb2 |
| [Insights Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#insights-administrator) | eb1f4a8d-243a-41f0-9fbd-c7cdf6c5ef7c |
| Insights Analyst | 25df335f-86eb-4119-b717-0ff02de207e9 |
| [Intune Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator) | 3a2c62db-5318-420d-8d74-23affee5d9d5 |
| Kaizala Administrator | 74ef975b-6605-40af-a5d2-b9539d836353 |
| Knowledge Administrator | b5a8dcf3-09d5-43a9-a639-8e29ef291470 |
| Knowledge Manager | 744ec460-397e-42ad-a462-8b3f9747a02c |
| Microsoft Hardware Warranty Administrator | 1501b917-7653-4ff9-a4b5-203eaf33784f |
| [Office Apps Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#office-apps-administrator) | 2b745bdf-0803-4d80-aa65-822c4493daac |
| Organizational Data Source Administrator | 9d70768a-0cbc-4b4c-aea3-2e124b2477f4 |
| [Power Platform Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#power-platform-administrator) | 11648597-926c-4cf3-9c36-bcebb0ba8dcc |
| [Privileged Authentication Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) | 7be44c8a-adaf-4e2a-84d6-ab2649e08a13 |
| Search Administrator | 0964bb5e-9bdb-4d7b-ac29-58e794862a40 |
| [Security Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) | 194ae4cb-b126-40b2-bd5b-6091b380977d |
| [Security Operator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator) | 5f2222b1-57c3-48ba-8ad5-d4759f1fde6f |
| [Service Support Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#service-support-administrator) | f023fd81-a637-4b56-95fd-791ac0226033 |
| [SharePoint Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator) | f28a1f50-f6e7-4571-818b-6a12f2af6b6c |
| SharePoint Advanced Management Administrator | 99009c4a-3b3f-4957-82a9-9d35e12db77e |
| [Skype for Business Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#skype-for-business-administrator) | 75941009-915a-4869-abe7-691bff18279e |
| [Teams Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#teams-administrator) | 69091246-20e8-4a56-aa4d-066075b2a7a8 |
| [Teams Communications Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#teams-communications-administrator) | baf37b3a-610e-45da-9e62-d9d1e5e8914b |
| [Teams Telephony Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#teams-telephony-administrator) | aa38014f-0993-46e9-9b45-30501a20909d |
| [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) | fe930be7-5e62-47db-91af-98c3a49a38b1 |
| Viva Glint Tenant Administrator | 0ec3f692-38d6-4d14-9e69-0377ca7797ad |
| Viva Goals Administrator | 92b086b3-e367-4ef2-b869-1de128fb986e |
| [Windows 365 Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#windows-365-administrator) | 11451d60-acb2-45eb-a7d6-43d0f0125c13 |
| Yammer Administrator | 810a2642-a034-447f-a5e8-41beaa378541 |

For more information about roles in Microsoft Entra ID, see [Support least privileged roles](/en-us/entra/identity/role-based-access-control/delegate-by-task#support-least-privileged-roles).