---
layout: Conceptual
title: Administrative units in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-admin-units
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to configure and use administrative units in Microsoft Purview.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-04T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-admin-units
audience: Admin
ms.topic: concept-article
ms.collection:
- purview-compliance
- essentials-manage
ms.custom:
- admindeeplinkCOMPLIANCE
- admindeeplinkEXCHANGE
ai-usage: ai-assisted
locale: en-us
document_id: 6195707f-73c7-1309-2497-8f01bad73bf1
document_version_independent_id: 6195707f-73c7-1309-2497-8f01bad73bf1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-admin-units.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-admin-units
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-admin-units.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 15912870-11e9-274c-0446-b8dcd37abc93
---

# Administrative units in Microsoft Purview | Microsoft Learn

By using [administrative units](/en-us/entra/identity/role-based-access-control/administrative-units) in Microsoft Entra ID, you can subdivide your organization into smaller units and restrict administrative permissions to specific parts of your Microsoft Entra organization. You can create, delete, and edit administrative units in Microsoft Entra, and manage the users or groups that are members of each unit.

Microsoft Purview integrates with administrative units by enabling you to assign [role group](purview-permissions) members to specific units. Microsoft Purview solutions that support administrative units restrict visibility and management permissions to members of the assigned unit.

For example, you can use administrative units to delegate permissions to administrators for each geographic region in a large multinational organization or to group administrator access by department. You can then create region-specific or department-specific policies, and view user activity as a result of those policies and administrative unit assignments. You can also use administrative units as an initial scope for a policy, where the users eligible for the policy depend on administrative unit membership.

If you're using adaptive scopes for compliance policies, see [How adaptive scopes work with Microsoft Entra administrative units](purview-adaptive-scopes#how-adaptive-scopes-work-with-azure-ad-administrative-units).

## Supported solutions

The following Microsoft Purview solutions support administrative units:

| **Solution** | **Configuration support** |
| --- | --- |
| [Data lifecycle management](data-lifecycle-management) | [Role groups, retention policies, and retention label policies](get-started-with-data-lifecycle-management#support-for-administrative-units) |
| [Data Loss Prevention (DLP)](dlp-learn-about-dlp) | Role groups and [DLP policies](dlp-create-deploy-policy) |
| [Communication Compliance](communication-compliance) | [Role groups](communication-compliance-permissions#consider-admin-units-if-you-want-to-scope-user-permissions-to-a-region-or-department) and [policies](communication-compliance-configure) |
| [Insider Risk Management](insider-risk-management) | [Role groups](insider-risk-management-permissions#add-users-to-the-insider-risk-management-role-group) and [policies](insider-risk-management-policies) |
| [Records management](records-management) | [Role groups, retention policies, retention label policies](get-started-with-records-management#support-for-administrative-units), and [adaptive scopes](purview-adaptive-scopes) |
| [Sensitivity labeling](sensitivity-labels) | [Role groups, sensitivity label policies, and auto-labeling policies](get-started-with-sensitivity-labels#support-for-administrative-units) |

The configuration for administrative units automatically flows down to the following features:

- **Alerts**:
    - [DLP](dlp-alerts-dashboard-get-started) alerts are visible only to users in assigned administrative units.
- **Activity explorer**:
    - [Activity events](data-classification-activity-explorer) are visible only to users in assigned administrative units.
- **Adaptive scopes**:
    - Restricted administrators can select, create, edit, and view [adaptive scopes](purview-adaptive-scopes) only for users in those administrators' assigned administrative units.
    - When a restricted administrator configures a policy that uses adaptive scopes, the administrator can select only adaptive scopes that are assigned to their administrative units.
- **Audit log**:
    - [Search access](audit-search).
- **Communication Compliance**:
    - [Policy lookup and configuration](communication-compliance-policies): Restricted administrators can create or manage policies only for users assigned to their administrative units.
    - Alerts and policy matches: Restricted administrators can [investigate user activities only for users within their assigned administrative units](communication-compliance-investigate-remediate).
- **Data lifecycle management and records management**:
    - [Policy lookup](retention#policy-lookup): Restricted administrators see policies only from users within their assigned administrative units.
    - [Disposition review and verification](disposition): Restricted administrators can add reviewers only from within their assigned administrative units, and see disposition reviews and items disposed only from users within their assigned administrative units.
- **Insider Risk Management**:
    - [Policy lookup and configuration](insider-risk-management-policies): Restricted administrators can create or manage policies only for users assigned to their administrative units.
    - User activities: Restricted administrators can [start scoring activities](insider-risk-management-policies#immediately-start-scoring-user-activity) or [investigate user activities only for users within their assigned administrative units](insider-risk-management-activities).
    - Alerts and cases: Restricted administrators [can view and investigate alerts](insider-risk-management-activities#standard-alert-dashboard) and [cases](insider-risk-management-cases) only for users within their assigned administrative units.

Note

Although DLP and Insider Risk Management both surface [alerts](/en-us/defender-xdr/investigate-alerts?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json&amp;tabs=settings) in Microsoft Defender XDR, Microsoft Defender XDR only supports administrative units for DLP. Microsoft Defender XDR supports up to 100 administrative units.

## Permissions for administrative units

To assign a role group member to an administrative unit, administrators must be assigned the *Role management* role. For more information about managing role groups and roles in Microsoft Purview, see [Permissions in the Microsoft Purview portal](purview-permissions). To view the complete list of default role groups and the roles assigned to each, see [Role groups in Microsoft Purview](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

You can assign role group members to administrative units within the following built-in [role groups](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview):

| Role group | Solution area |
| --- | --- |
| [Communication Compliance](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Communication Compliance |
| [Communication Compliance Administrators](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Communication Compliance |
| [Communication Compliance Analysts](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Communication Compliance |
| [Communication Compliance Investigators](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Communication Compliance |
| [Compliance Administrator](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Cross-solution |
| [Compliance Data Administrators](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Cross-solution |
| [Global Reader](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Cross-solution |
| [Information Protection](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Information Protection |
| [Information Protection Admins](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Information Protection |
| [Information Protection Analyst](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Information Protection |
| [Information Protection Investigators](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Information Protection |
| [Information Protection Readers](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Information Protection |
| [Insider Risk Management](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Insider Risk Management |
| [Insider Risk Management Admins](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Insider Risk Management |
| [Insider Risk Management Analysts](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Insider Risk Management |
| [Insider Risk Management Approvers](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Insider Risk Management |
| [Insider Risk Management Investigators](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Insider Risk Management |
| [Insider Risk Management Session Approvers](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Insider Risk Management |
| [Organization Management](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Cross-solution |
| [Records Management](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Records Management |
| [Security Administrator](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Cross-solution |
| [Security Operator](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Cross-solution |
| [Security Reader](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) | Cross-solution |

When you [assign role groups](purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group), you can select individual members or groups, and then select the **Assign admin units** option to select administrative units that you define in [Microsoft Entra ID](/en-us/entra/identity/role-based-access-control/admin-units-manage):

[![Assign admin units option when you edit role groups.](media/assign-admin-units.png)](media/assign-admin-units.png#lightbox)

Important

**Assign admin units** is always available when you [create custom role groups](purview-permissions#create-a-custom-microsoft-purview-role-group). You can assign administrative units for any custom role group.

These administrators, referred to as *restricted administrators*, can select one or more of their assigned administrative units to automatically define the initial scope of policies that they create or edit. If administrators don't have administrative units assigned (*unrestricted administrators*), they can assign policies to the entire directory without being required to select individual administrative units.

Important

After you assign administrative units to members of the role groups, these restricted administrators can't see and edit existing policies. However, there's no operational change to these policies and they remain visible and can be edited by unrestricted administrators.

Restricted administrators also can't see historical data by using features that support administrative units, such as activity explorer and alerts. They remain visible to unrestricted administrators. Going forward, restricted administrators can see this related data for their assigned administrative units only.

## Prerequisites for administrative units

Before configuring administrative units for Microsoft Purview solutions, make sure your organization and users meet the following subscription and licensing requirements:

- [Microsoft Entra ID P1 or P2 licensing](/en-us/entra/identity/role-based-access-control/admin-units-manage#prerequisites)
- Microsoft Purview licensing (one of the following subscriptions):

    - Microsoft 365 E5/A5/G5
    - Microsoft 365 E5/A5/G5/F5 Compliance or F5 Security & Compliance
    - Microsoft 365 E5/A5/G5/F5 Information Protection & Governance
    - Microsoft 365 E5/A5/F5 Insider Risk Management

    For more information about licensing options for Microsoft Purview features, see the [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

## Configure administrative units

Complete the following steps to configure and use administrative units with Microsoft Purview solutions:

1. [Create administrative units](/en-us/entra/identity/role-based-access-control/admin-units-manage#create-an-administrative-unit) to restrict the scope of role permissions in Microsoft Entra ID.
2. [Add users and distribution groups](/en-us/entra/identity/role-based-access-control/admin-units-members-add) to administrative units.

    Important

    Members of [Dynamic Distribution Groups](/en-us/entra/identity/role-based-access-control/administrative-units#groups) don't automatically become members of an administrative unit.
3. If you create geographic region or department-based administrative units, configure administrative units by using [dynamic membership rules](/en-us/entra/identity/role-based-access-control/admin-units-members-dynamic).

    Note

    You can't add groups to an administrative unit that uses dynamic membership rules. If needed, create two administrative units, one for users and one for groups.
4. Use any of the [role groups](purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group) from the Microsoft Purview solutions that support administrative units to assign administrative units to members.

When restricted administrators create or edit policies that support administrative units, they can select administrative units so that only the users in those administrative units are eligible for the policy:

- *Unrestricted administrators* don't have to select administrative units as part of the policy configuration. They can keep the default of the entire directory or select one or more administrative units.
- *Restricted administrators* must select one or more administrative units as part of the policy configuration.

Later in the policy configuration, administrators who select administrative units must include or exclude (if supported) individual users and groups from the administrative units that they previously selected for the policy.

For information about administrative units that is specific to each supported solution, see the following sections:

- For audit: [Scoping access to audit logs using administrative units](audit-search#scoping-access-to-audit-logs-using-administrative-units)
- For communication compliance: [Consider administrative units if you want to scope user permissions to a region or department](communication-compliance-permissions#consider-admin-units-if-you-want-to-scope-user-permissions-to-a-region-or-department)
- For data lifecycle management: [Support for administrative units](get-started-with-data-lifecycle-management#support-for-administrative-units)
- For DLP: [Administrative Unit restricted policies](dlp-policy-reference#administrative-unit-restricted-policies)
- For insider risk management: [Consider administrative units if you want to scope user permissions to a region or department](insider-risk-management-permissions#consider-administrative-units-if-you-want-to-scope-user-permissions-to-a-region-or-department)
- For records management: [Support for administrative units](get-started-with-records-management#support-for-administrative-units)
- For sensitivity labeling: [Support for administrative units](get-started-with-sensitivity-labels#support-for-administrative-units)

## SharePoint site support for administrative units

Microsoft Purview now supports adding SharePoint sites to administrative units. By using this feature, you can tailor visibility and management control of Microsoft Purview administrators within the Microsoft Purview portal. This support is only available for Microsoft Information Protection auto-labeling policies and Microsoft Data Loss Prevention policies that support application to SharePoint sites.

Note

You manage administrative unit creation, deletion, and Microsoft Entra resource membership from [Microsoft Entra ID](/en-us/entra/identity/role-based-access-control/administrative-units). Any administrative unit you create appears in the listing for Microsoft Purview.

It can take up to five days for a SharePoint site query to fully populate. Changes aren't immediate. Wait until the query fully populates before you associate a policy with an administrative unit.

### Configure SharePoint sites for administrative units

Complete the following steps to configure administrative units. These steps guide you through administrative unit creation, how to associate resources to that administrative unit, and how to assign Microsoft Purview role group members to administrative units. After you create administrative units, use the following steps to associate SharePoint sites to the administrative unit.

Microsoft Purview customers entitled to this feature can now access **Administrative units** under the **Roles and scopes** in Microsoft Purview portal settings. Within **Administrative units**, select an administrative unit and edit it to associate SharePoint sites to the administrative unit.

To complete the following steps to configure SharePoint sites within administrative units for use in Microsoft Purview, you must have the [admin unit extension manager](/en-us/defender-office-365/scc-permissions?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) role assigned. An administrator with role management rights in Microsoft Purview assigns this role, either by using a built-in role group with this role or by using a [custom role group](purview-permissions#create-a-custom-microsoft-purview-role-group).

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** and select **Roles and scopes**.
3. Select **Administrative units**.
4. Select an existing administrative unit from the list.
5. Select **Edit**.
6. Create a query to associate SharePoint sites with the administrative unit.
7. Use any of the [role groups](purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group) from the Microsoft Purview solutions that support administrative units to assign administrative units to members.

Queries to associate SharePoint sites with administrative units support site properties for Site URL, site name, and `RefinableString00`-`RefinableString99`. These queries apply both to SharePoint sites and OneDrive accounts, with the exception of [shared channel SharePoint sites](/en-us/microsoftteams/shared-channels?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json). The property names for sites are based on SharePoint site managed properties. For more information about associating custom properties to managed properties (`RefinableString00`-`RefinableString99`), see [Using Custom SharePoint Site Properties to Apply Microsoft 365 Retention with Adaptive Policy Scopes](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/using-custom-sharepoint-site-properties-to-apply-microsoft-365/ba-p/3133970).

### Test your query

To test your query by using SharePoint search, complete the following steps:

1. With an account assigned the SharePoint admin role, go to `https://<your_tenant>.sharepoint.com/search`.
2. Use the search bar to enter the query shown in the **query summary** for your SharePoint sites in the administrative unit.
3. Verify that the search results match the expected site URLs for your administrative unit. If they don't, check your query and the URLs with the relevant administrator for SharePoint.

The same restricted and unrestricted administrator behavior that applies to user-scoped policies also applies to policies that include SharePoint sites. Additionally, administrators selecting administrative units can't include or exclude individual SharePoint sites. SharePoint sites support application to all sites associated with the administrative unit.

Important

To remove associated sites from an administrative unit, edit a SharePoint query for an administrative unit to result in no site memberships. To clear site membership, make the query result in no sites.

### View SharePoint site membership

After you create a SharePoint query for an administrative unit in Microsoft Purview, you can view the site members of the administrative unit. You can only view user and group membership of an administrative unit from the Microsoft Entra ID portal.

Complete the following steps to access the member details page and see SharePoint site members of an administrative unit in Microsoft Purview:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** and select **Roles and scopes**.
3. Select **Administrative units**.
4. Select an existing administrative unit from the list.
5. Select **Member Details**.
6. View the list of SharePoint site members.
7. Check the **State** column in the list, which shows *Added* for sites added to the administrative unit or *Removed* if the site was previously in the administrative unit but is removed after it's no longer a match for the SharePoint query.
8. Use the **Export** function to download a list of the displayed sites to a CSV file.

Note

It might take up to five days for the member details list to update added or removed sites.

For information about administrative units and the SharePoint site in Microsoft Purview solutions, see:

- **DLP**: [Administrative Unit restricted policies](dlp-policy-reference#administrative-unit-restricted-policies)
- **Sensitivity labels**: [Support for administrative units](get-started-with-sensitivity-labels#support-for-administrative-units)