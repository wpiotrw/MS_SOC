---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Understand Microsoft 365 Support case creation and data access - Microsoft 365 admin | Microsoft Learn
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
ms.date: 2026-08-12T00:00:00.0000000Z
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
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: deb8bee0-a945-14d6-dd48-27dc24695e70
---

# Understand Microsoft 365 Support case creation and data access - Microsoft 365 admin | Microsoft Learn

Microsoft is improving your visibility into Microsoft Support's read-only access to your data during the Microsoft 365 support case lifecycle. When you create a support request, you grant [cross-tenant access](/en-us/entra/external-id/cross-tenant-access-overview) to Microsoft Support to access the information needed to troubleshoot the issue. This access is time bound and uses least-privileged access, in accordance with [Zero Trust Principles](/en-us/security/zero-trust/zero-trust-overview).

This article describes what you see in your Microsoft Entra audit logs when:

- A Microsoft 365 Support case is created
- A Microsoft Support engineer works on your case
- A Microsoft 365 Support case is closed

This article also lists who can create support cases and what permissions are granted to Microsoft Support engineers.

Note

This article is designed for enterprise admins and IT Pros.

If you're a business user and you need technical support, see [Get support for Microsoft 365 for business](get-help-support).

If you're a home user and you need help, see [Contact us](https://support.microsoft.com/contactus).

## What happens when a Microsoft 365 support case is created?

When a user who has an appropriate role creates a support case in the [Microsoft 365 admin center](https://admin.microsoft.com), a special type of cross-tenant access policy resource must be created between your tenant and the Microsoft Support tenant. Only users who have one of the following roles can create the cross-tenant access policy that's needed for Microsoft Support to work on the case:

- [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator)
- [Security Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)
- [Teams Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#teams-administrator)

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

The level of access is captured as *Delegated Admin Service Provider Constraints*, using the *Microsoft 365 Support Engineer* role. To see the read permissions that are granted, see [Microsoft Entra built-in roles: Microsoft 365 Support Engineer](/en-us/entra/identity/role-based-access-control/permissions-reference#microsoft-365-support-engineer).

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
| **Support data** | All data provided to Microsoft by the customer as part of a customer engagement to obtain support services. | - Support requests from customers and phone conversations, online chat sessions, or remote assistance sessions between support professionals and customers.<br>- Case notes and records related to support requests from customers.<br>- Data provided to Microsoft by the customer as part of support activities. |
| **Account data** | Contact, billing, purchase, payment, and license information. | - Customer's provisioning information.<br>- Account configuration and billing data.<br>- Tenant administrator contact information, such as tenant administrator's name, address, e-mail address, phone number.<br>- Licensing and purchase information. |
| **System metadata** | Data generated in the course of running the service. | - Event logs.<br>- Access control logs.<br>- Account information belonging to Microsoft operations personnel.<br>- Microsoft server names and server IPs.<br>- Server patching and vulnerability data.<br>- Service configuration data.<br>- Telemetry (on-premises or cloud). |
| **Organization information** | Data that can be used to identify a particular tenant, deployment, or organization (generally configuration or usage data). | - Tenant ID (non-GUID).<br>- Tenant ID (GUID) due to the existence of many out of boundary Tenant ID to name mapping tables.<br>- Tenant usage data.<br>- Tenant IP addresses (IPv4), such as tenant's firewall IP address.<br>- Global prefix and subnet ID (first 64 bits of IPv6 address).<br>- Tenant domain name in e-mail address, such as `joe@contoso.com`.<br>- Mapping of organizational GUID to organization. |
| **Customer data** | Data that directly identifies or could be used to identify the authenticated user of a Microsoft service. | - User-specific IP address (IPv4).<br>- User principal name (`joe@company.com`).<br>- Address book data.<br>- User's machine name.<br>- SIP URI. |
| **Pseudonymous identifiers** | An identifier created by Microsoft tied to the user of a Microsoft service. | - User GUIDs or PUIDs.<br>- Session IDs. |

## How long does Microsoft Support have access to tenant data?

Microsoft Support loses access to your tenant data when the support tenant is removed from your cross-tenant access settings. This process is automated and directly linked to the lifecycle of support cases within your tenant.

- If a case is open for more than 30 days, access is revoked automatically, provided there aren't any other, newer cases opened. You can restore access by opening a new support case or reopening a closed case.
- You can revoke access at any time by deleting the Microsoft Support tenant partner in your cross-tenant access settings. To remove the Microsoft Support tenant, which is listed as Office 365 with Tenant ID `b4c546a4-7dac-46a6-a7dd-ed822a11efd3`, see [Cross-tenant access settings: Remove an organization](/en-us/entra/external-id/cross-tenant-access-settings-b2b-collaboration#remove-an-organization).

Caution

If you revoke access manually, Microsoft Support loses the ability to help resolve your support cases.

## What happens when a support case is closed?

When a support case is closed, Microsoft checks if there are any other active support cases open. If there are no other active support cases, Microsoft initiates the access revocation process, which includes multiple steps.

## How long is diagnostic data retained in Microsoft systems?

Microsoft retains diagnostic data related to your support case for up to 28 days after collection. After this period, Microsoft deletes the data.

For information about how Microsoft protects your data, see [Privacy and data management overview](/en-us/compliance/assurance/assurance-privacy).

## Who can create support cases?

### Roles to create a support case and a cross-tenant access policy resource

Users assigned the following roles can create a support case and the cross-tenant access policy resource needed for the case:

- [Global Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator)
- [Security Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)
- [Teams Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#teams-administrator)

### Roles to create a support case only

Users assigned one of the following roles can create a support case, but they can't create a cross-tenant policy resource:

- [Application Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)
- [Authentication Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator)
- [Authentication Policy Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator)
- [Azure Information Protection Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#azure-information-protection-administrator)
- [Billing Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator)
- [Cloud Application Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)
- [Compliance Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#compliance-administrator)
- [Compliance Data Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#compliance-data-administrator)
- [Desktop Analytics Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#desktop-analytics-administrator)
- [Dynamics 365 Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#dynamics-365-administrator)
- [Exchange Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator)
- [Fabric Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#fabric-administrator)
- [Global Secure Access Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#global-secure-access-administrator)
- [Groups Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator)
- [Helpdesk Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator)
- [Hybrid Identity Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator)
- [Insights Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#insights-administrator)
- [Intune Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator)
- [Office Apps Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#office-apps-administrator)
- [Power Platform Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#power-platform-administrator)
- [Privileged Authentication Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator)
- [Security Operator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator)
- [Service Support Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#service-support-administrator)
- [SharePoint Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator)
- [Skype for Business Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#skype-for-business-administrator)
- [Teams Communications Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#teams-communications-administrator)
- [Teams Telephony Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#teams-telephony-administrator)
- [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator)
- [Windows 365 Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#windows-365-administrator)

For more information about roles in Microsoft Entra ID, see [Support least privileged roles](/en-us/entra/identity/role-based-access-control/delegate-by-task#support-least-privileged-roles).