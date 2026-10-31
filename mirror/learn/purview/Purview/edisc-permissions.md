---
layout: Conceptual
title: Assign permissions in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Assign the permissions required to perform eDiscovery-related tasks in eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-09-18T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 2dfa854e-cacc-f17b-cd99-778cd0829100
document_version_independent_id: 2dfa854e-cacc-f17b-cd99-778cd0829100
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-permissions.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e922c432-bfe7-3f02-3cf1-77562abf0732
---

# Assign permissions in eDiscovery | Microsoft Learn

To use eDiscovery capabilities and features in the Microsoft Purview portal, assign the appropriate permissions to users. The easiest way to assign roles is to add users to the appropriate role group on the **Role groups** page in the [Microsoft Purview portal](purview-portal). This article describes the permissions required to perform eDiscovery tasks.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## eDiscovery roles and role groups

The primary eDiscovery-related role group in Microsoft Purview portal is called **eDiscovery Manager**. This role group contains two subgroups:

- **eDiscovery Manager**: An *eDiscovery Manager* can search content locations in the organization and perform various search-related actions such as preview and export search results in eDiscovery. Members can also create and manage cases, add, and remove users for a case, create case holds, run searches associated with a case, and access case data. eDiscovery Managers can only access and manage the cases they create. They can't access or manage cases created by other eDiscovery Managers.

    - You can add a mail-enabled security group as a member of the eDiscovery Managers subgroup in the *eDiscovery Manager* role group by using the **Add-RoleGroupMember** cmdlet in Security & Compliance PowerShell. For example, you can run the following command to add a mail-enabled security group to the *eDiscovery Manager* role group.

    ```powershell
    Add-RoleGroupMember "eDiscoveryManager" -Member <name of security group>
    ```

    - Exchange distribution groups and Microsoft 365 Groups aren't supported. You must use a mail-enabled security group, which you can create in Exchange Online PowerShell by running `New-DistributionGroup -Type Security`. You can also create a mail-enabled security group (and add members) in the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) or in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). It might take up to 60 minutes after you create it for a new mail-enabled security group to be available to add to the eDiscovery Managers role group.
    - You can't make a mail-enabled security group an eDiscovery Administrator by using the **Add-eDiscoveryCaseAdmin** cmdlet in Security & Compliance PowerShell. You can only add individual users as eDiscovery Administrators.
    - You also can't add a mail-enabled security group as a member of a case.
- **eDiscovery Administrator**: An *eDiscovery Administrator* is a member of the *eDiscovery Manager* role group, and can perform the same content search and case management-related tasks that an eDiscovery Manager can perform. Additionally, an eDiscovery Administrator can:

    - Access all cases that are listed on the **eDiscovery** area in the Microsoft Purview portal.
    - Configure eDiscovery solution settings.
    - Access process and hold reports scoped to all cases.
    - Access case data for any case in the organization.
    - Manage any eDiscovery case after they add themselves as a member of the case.
    - Remove members from an eDiscovery case. Only an eDiscovery Administrator can remove members from a case. Users who are members of the eDiscovery Manager subgroup can't remove members from a case, even if the user created the case.
    - If a person who is the only member of an eDiscovery case leaves your organization, no one (including members of the *Organization Management* role group or another member of the *eDiscovery Manager* role group) can access that eDiscovery case because they aren't a member of a case. In this situation, there's no way to access the data in the case. But because an eDiscovery Administrator can access all eDiscovery cases in the organization, they can view the case and add themselves or another eDiscovery manager as a member of the case.
    - An eDiscovery Administrator can view and access all eDiscovery cases, they can audit and oversee all cases and associated compliance searches. This functionality can help to prevent any misuse of compliance searches or eDiscovery cases. And because eDiscovery Administrators can access potentially sensitive information in the results of a compliance search, you should limit the number of people who are eDiscovery Administrators.

    Note

    To analyze a user's data when premium eDiscovery features are enabled, the user must be assigned an Office 365 E5 or Microsoft 365 E5 license. Alternatively, users with an Office 365 E1 or an Office 365 or Microsoft 365 E3 license can be assigned a Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance) or Microsoft 365 eDiscovery and Audit add-on license. Administrators, compliance officers, or legal personnel who are assigned to cases as members and use premium eDiscovery features to collect, view, and analyze data don't need an E5 license. For more information about subscriptions and licensing, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for eDiscovery.

## Before you assign permissions

- You need to be a member of the *Organization Management* role group or be assigned the *Role Management* role to assign eDiscovery permissions in the Microsoft Purview portal.
- You can use the [Add-RoleGroupMember](/en-us/powershell/module/exchange/Add-RoleGroupMember) cmdlet in Security & Compliance PowerShell to add a mail-enabled security group as a member of the *eDiscovery Managers* subgroup in the *eDiscovery Manager* role group. However, you can't add a mail-enabled security group to the *eDiscovery Administrators* subgroup.

## Configure app-only authentication for eDiscovery PowerShell

Important

App-only authentication for eDiscovery cmdlets in Security & Compliance PowerShell is unsupported. Transition automations to Microsoft Graph APIs where available. The following steps are best-effort guidance for existing automations that continue to use this unsupported configuration and don't change its support status.

Certificate-based authentication (CBA), also known as app-only authentication, requires both Microsoft Entra authorization and eDiscovery role-based access control (RBAC). The API permission allows the application to authenticate, while service principal registration and role group membership authorize eDiscovery cmdlets.

1. Follow [App-only authentication for unattended scripts in Exchange Online PowerShell and Security & Compliance PowerShell](/en-us/powershell/exchange/app-only-auth-powershell-v2) to create the Microsoft Entra application and configure its certificate.
2. On the application, select **Add a permission** &gt; **APIs my organization uses** &gt; **Microsoft Exchange Online Protection** &gt; **Application permissions** &gt; **Exchange** &gt; **Exchange.ManageAsApp**, and then grant tenant-wide admin consent. The similarly named **Office 365 Exchange Online** permission isn't required for this Security & Compliance PowerShell connection. If the application also runs other Exchange Online automations, keep any permissions that those separate workflows require.
3. Connect to [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) with an account that can manage role groups. Register the enterprise application's service principal in Exchange and Microsoft Purview:

    ```powershell
    New-ServicePrincipal -AppId <application-client-id> -ObjectId <enterprise-application-object-id> -DisplayName "<display-name>"
    ```

    The *AppId* value is the application (client) ID. The *ObjectId* value is the Object ID from **Enterprise applications**, not the Object ID from **App registrations**. Use a descriptive *DisplayName* value to make the service principal easy to identify.
4. In the Microsoft Purview portal, the *eDiscovery Manager* role group appears under **Settings** &gt; **Role groups**. Assign the registered service principal to this role group by using Security & Compliance PowerShell and the same enterprise application Object ID:

    ```powershell
    Add-RoleGroupMember -Identity "eDiscoveryManager" -Member <enterprise-application-object-id>
    ```

    The *eDiscovery Manager* role group is the validated least-privileged assignment for app-only eDiscovery. Don't use *eDiscovery Administrator* as an interchangeable service principal assignment.
5. Verify the role group membership:

    ```powershell
    Get-RoleGroupMember -Identity "eDiscoveryManager"
    ```
6. Use ExchangeOnlineManagement 3.10.1 or later, and include the *EnableSearchOnlySession* switch when you connect:

    ```powershell
    Connect-IPPSSession -CertificateThumbprint "<certificate-thumbprint>" -AppId "<application-client-id>" -Organization "<tenant>.onmicrosoft.com" -EnableSearchOnlySession
    ```

If the connection returns HTTP 401, verify that **Microsoft Exchange Online Protection** &gt; **Exchange.ManageAsApp** is configured as an Application permission and has tenant-wide admin consent. If the connection succeeds but eDiscovery cmdlets aren't recognized, verify the service principal registration and its membership in the *eDiscovery Manager* role group.

## Assign eDiscovery permissions

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with an account that can assign permissions.
2. Go to **Settings** &gt; **Role groups**.
3. On **Role groups for Microsoft Purview solutions**, select **eDiscovery Manager**.
4. On the **eDiscovery Manager** pane, do one of the following actions based on the eDiscovery permissions that you want to assign.

    - Select **Edit**.
    - On **Manage eDiscovery Manager**, select **Choose users** or **Choose groups**.
    - Search and select the users you want to add as an *eDiscovery Manager*, then select **Select**.
    - Select **Next**.
    - To assign users to the *eDiscovery Administrator* role group, select **Choose users** or **Choose groups**.
    - Search and select the users you want to add as an *eDiscovery Administrator*, then select **Select**.
    - Select **Next**.
5. If the selected users or groups need organization-wide access as part of this role group assignment, go to Step 8.
6. If the selected users or groups need to be assigned to administrative units, select the users or groups and select **Assign admin units**.
7. On **Assign admin units**, select the checkbox for all the administrative units you want to assign to the users or groups. Select **Select**.
8. Select **Next** and **Save** to add the users or groups to the role group. Select **Done** to complete the steps.

Note

You can also use the **Add-eDiscoveryCaseAdmin** cmdlet to make a user an eDiscovery Administrator. However, you must assign the *Case Management* role to the user before you can use this cmdlet to make them an eDiscovery Administrator. For more information, see [Add-eDiscoveryCaseAdmin](/en-us/powershell/module/exchange/add-ediscoverycaseadmin).

On the **Role groups** page in the Microsoft Purview portal, you can also assign users eDiscovery-related permissions by adding them to the *Compliance Administrator*, *Organization Management*, and *Reviewer* role groups. For a description of the eDiscovery-related role-based access control roles assigned to each of these role groups, see Role-based access control roles related to eDiscovery.

## RBAC roles related to eDiscovery

The following table lists the eDiscovery-related role-based access control roles in the Microsoft Purview portal, and shows the built-in role groups that each role belongs to by default.

| Role | Compliance Administrator | eDiscovery Manager & Administrator | Organization Management | Reviewer |
| --- | --- | --- | --- | --- |
| Case Management | ![Check mark indicating the Case Management role is assigned to this role group.](media/checkmark.png) | ![Check mark indicating the Case Management role is assigned to this role group.](media/checkmark.png) | ![Check mark indicating the Case Management role is assigned to this role group.](media/checkmark.png) |  |
| Communication |  | ![Check mark indicating the Communication role is assigned to eDiscovery Manager and Administrator.](media/checkmark.png) |  |  |
| Compliance Search | ![Check mark indicating the Compliance Search role is assigned to Compliance Administrator.](media/checkmark.png) | ![Check mark.](media/checkmark.png) | ![Check mark.](media/checkmark.png) |  |
| Custodian (Data Sources) |  | ![Check mark indicating the Custodian role is assigned to eDiscovery Manager and Administrator.](media/checkmark.png) |  |  |
| Export |  | ![Check mark indicating the Export role is assigned to eDiscovery Manager and Administrator.](media/checkmark.png) |  |  |
| Hold | ![Check mark indicating the Hold role is assigned to Compliance Administrator.](media/checkmark.png) | ![Check mark.](media/checkmark.png) | ![Check mark.](media/checkmark.png) |  |
| Manage review set tags |  | ![Check mark indicating the Manage review set tags role is assigned to eDiscovery Manager and Administrator.](media/checkmark.png) |  |  |
| Preview |  | ![Check mark indicating the Preview role is assigned to eDiscovery Manager and Administrator.](media/checkmark.png) |  |  |
| Review |  | ![Check mark indicating the Review role is assigned to eDiscovery Manager and Administrator.](media/checkmark.png) |  | ![Check mark](media/checkmark.png) |
| RMS Decrypt |  | ![Check mark indicating the RMS Decrypt role is assigned to eDiscovery Manager and Administrator.](media/checkmark.png) |  |  |
| Search And Purge |  |  | ![Check mark indicating the Search And Purge role is assigned to Organization Management.](media/checkmark.png) |  |

Note

To view the list of eDiscovery cases, a user must have at least one of the roles listed in the preceding table. For users who aren't eDiscovery Administrators, the cases shown are limited to those where the user is a member. The Custodian role provides access to the **Data Sources** tab in eDiscovery to manage data sources related to specific cases.

Run the following diagnostic test to check if the *Export*, *Preview*, or *Search* roles are assigned to the designated admin account.

1. Select the **Help** control in the top right of the Microsoft Purview portal. Enter *Diag:edisRBACdiag* in search (or select this [link](https://aka.ms/PillareDisRBACDiag)) to run the **eDiscovery RBAC Check** test.
2. In the **Run diagnostics** section, enter the UPN or email address of the user trying to run an export, preview, or search task.
3. Select **Run Tests**. If the user doesn't have the necessary eDiscovery roles, assign the roles to perform the desired task.

## Custom role combinations

If you need to provide custom access to specific feature components of eDiscovery for specific users, use custom role combinations for specific users. For example, you might need to allow a user to manage data sources, but without access to search features. For another user, you might need to allow to manage searches, but without access to data sources.

Consider using the following role combinations as needed:

- *Case Management* and *Search* roles for access to only search features.
- *Case Management* and *Custodian* roles for access to only data source features.
- *Case Management*, *Review*, and *Manage Tags* roles for access to only review features.
- *Case Management* and *Hold* roles for access to only hold features.
- *Case Management* and *Export* roles for access to only export features.
- *Case Management*, *Search*, and *Purge* roles for access to only purge features.

## eDiscovery roles

The following sections describe each of the eDiscovery-related RBAC roles listed in the RBAC roles related to eDiscovery table.

### Case Management

This role lets users create, edit, delete, and control access to eDiscovery cases in the Microsoft Purview portal. You must assign the *Case Management* role before you can use the **Add-eDiscoveryCaseAdmin** cmdlet to make a user an eDiscovery Administrator. For more information, see [Get started with eDiscovery](edisc-get-started).

### Compliance Search

This role lets users search mailboxes and public folders, SharePoint sites, OneDrive sites, Skype for Business conversations, Microsoft 365 groups, Microsoft Teams, and Viva Engage groups. This role allows a user to get an estimate of the search results and create export reports, but other roles are needed to initiate search actions such as previewing, exporting, or deleting search results.

In eDiscovery, users who are assigned the *Compliance Search* role but don't have the *Preview* role can preview the results of a search when a user assigned the *Preview* role initiates the preview action. The user without the *Preview* role can preview results for up to two weeks after the initial preview action was created.

Similarly, users in eDiscovery who are assigned the *Compliance Search* role but don't have the *Export* role can download the results of a search when a user assigned the *Export* role initiates the export action. The user without the *Export* role can download the results of a search for up to two weeks after the initial export action was created. After that, they can't download the results unless someone with the *Export* role restarts the export.

The two-week grace period for previewing and exporting search results (without the corresponding search and export roles) doesn't apply when premium features are enabled in eDiscovery. Users must be assigned the *Preview* and *Export* roles to preview and export content when premium eDiscovery features are enabled.

### Custodian

This role lets users identify and manage custodians for eDiscovery cases managed in the retired Microsoft Purview compliance portal and use the information from Microsoft Entra ID and other sources to find data sources associated with custodians. The user can associate other data sources such as mailboxes, SharePoint sites, and Teams with custodians in a case. The user can also place a legal hold on the data sources associated with custodians to preserve content in the context of a case.

### Export

This role lets users export search results to a local computer. It also lets them prepare search results for analysis when premium eDiscovery features are enabled. For more information about exporting search results, see [Export search results in eDiscovery](edisc-search-export).

### Hold

This role lets users place content on hold in mailboxes, public folders, sites, Skype for Business conversations, and Microsoft 365 groups. When content is on hold, content owners can still modify or delete the original content, but the content is preserved until the hold is removed or until the hold duration expires. For more information about holds, see [Create a hold in eDiscovery](edisc-hold-create).

### Manage review set tags

This role lets users create, edit, and delete review set tags for cases they can access. Users need to at least have the *Review* role and this role to [manage tags](edisc-review-set-tagging) during reviews.

Note

eDiscovery guest users are limited to the *Reviewer* role group and can't be assigned the *Manage review set tags* role. Therefore, guest users can't perform review set tagging. For more information about guest-user permissions, see [Configure guest user settings in eDiscovery](edisc-settings-guest-users).

### Preview

This role lets users view a list of items that a search returns. They can also open and view each item from the list to view its contents.

### Review

This role lets users access review sets in eDiscovery. Users who are assigned this role can see and open the list of cases that they're members of. After the user accesses an eDiscovery case, they can select **Review sets** to access case data. This role doesn't allow the user to preview the results of a search that's associated with the case or do other search or case management tasks. Users with this role can only access the data in a review set.

### RMS Decrypt

This role lets users view rights-protected email messages when previewing search results and export decrypted rights-protected email messages. This role also lets users view (and export) a file that's encrypted with a [Microsoft encryption technology](encryption) when the encrypted file is attached to an email message that's included in the results of an eDiscovery search. Additionally, this role lets users review and query encrypted email attachments that are added to a review set in eDiscovery. For more information about decryption in eDiscovery, see [Decryption in Microsoft 365 eDiscovery tools](edisc-decryption).

### Search And Purge

This role lets users perform bulk removal of data matching the criteria of a search. For more information, see [Find and delete email messages in eDiscovery](edisc-search-mailbox-data).

## Add role groups as members of eDiscovery cases

You can add role groups as members of eDiscovery cases so that members of the role groups can access and perform tasks in the assigned cases. The roles assigned to the role group define what members of the role group can do. When you add a role group as a member of the case, members can access and perform those tasks in a specific case.

With this requirement in mind, if you add or remove a role from a role group, the role group is automatically removed as a member of any case it belongs to. This behavior protects your organization from inadvertently providing extra permissions to members of a case. Similarly, if you delete a role group, you remove it from all cases it was a member of.

Before you add or remove roles to a role group that might be a member of an eDiscovery case, run the following commands in [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) to get a list of cases the role group is a member of. After you update the role group, add the role group back as a member of those cases.