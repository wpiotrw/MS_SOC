---
layout: Conceptual
title: Assign eDiscovery permissions in the Microsoft Purview portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-assign-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to assign eDiscovery permissions in the Microsoft Purview portal so users can search, hold, and export content in compliance cases.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
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
ms.custom:
- seo-marvel-apr2020
- admindeeplinkCOMPLIANCE
locale: en-us
document_id: fceb5d1f-6741-8219-ec80-e50d0f21169f
document_version_independent_id: fceb5d1f-6741-8219-ec80-e50d0f21169f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-assign-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-assign-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-assign-permissions.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 2f10c983-751b-a312-14ed-079502cb6756
---

# Assign eDiscovery permissions in the Microsoft Purview portal | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

To use any of the [eDiscovery-related tools](ediscovery) in the Microsoft Purview portal, assign the appropriate permissions. The easiest way to assign roles is to add the person to the appropriate role group on the **Permissions** page in the Purview portal. This article describes the permissions required to perform these tasks.

Tip

You can view your own permissions on the eDiscovery (Premium) overview page in the Purview portal. You must have at least one role assigned for your permissions to be displayed.

The primary eDiscovery-related role group in Purview portal is called **eDiscovery Manager**. Two subgroups exist within this role group:

- **eDiscovery Manager** - An eDiscovery Manager can use eDiscovery search tools to search content locations in the organization, and perform various search-related actions such as preview and export search results. Members can also create and manage cases in Microsoft Purview eDiscovery (Premium), add and remove members to a case, create case holds, run searches associated with a case, and access case data. eDiscovery Managers can only access and manage the cases they create. They can't access or manage cases created by other eDiscovery Managers.
- **eDiscovery Administrator** - An eDiscovery Administrator is a member of the eDiscovery Manager role group, and can perform the same content search and case management-related tasks that an eDiscovery Manager can perform. An eDiscovery Administrator can also:

    - Access all cases that are listed on the **eDiscovery (Premium)** page in the Purview portal.
    - Access case data in eDiscovery (Premium) for any case in the organization.
    - Manage any eDiscovery case after they add themselves as a member of the case.
    - Remove members from an eDiscovery case. Only an eDiscovery Administrator can remove members from a case. Users who are members of the eDiscovery Manager subgroup can't remove members from a case, even if the user created the case.

    For reasons why you might want eDiscovery Administrators in your organization, see eDiscovery Administrator considerations.

Note

eDiscovery (Premium) licensing requirements:

- The custodian of the data must be assigned an Office 365 E5 or Microsoft 365 E5 license.
- Users with an Office 365 E1 or an Office 365 or Microsoft 365 E3 license can be assigned a Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance) or Microsoft 365 eDiscovery and Audit add-on license.
- Administrators, compliance officers, or legal personnel who are assigned to cases as members and use eDiscovery (Premium) to collect, view, and analyze data don't need an E5 license.

For more information about eDiscovery (Premium) licensing, see [Subscriptions and licensing in eDiscovery (Premium)](ediscovery-overview#subscriptions-and-licensing).

## Prerequisites

- You must be a member of the *Organization Management* role group or be assigned the *Role Management* role to assign eDiscovery permissions in the Purview portal.
- You can use the [Add-RoleGroupMember](/en-us/powershell/module/exchange/Add-RoleGroupMember) cmdlet in Security & Compliance PowerShell to add a mail-enabled security group as a member of the *eDiscovery Managers* subgroup in the *eDiscovery Manager* role group. However, you can't add a mail-enabled security group to the *eDiscovery Administrators* subgroup. For details, see eDiscovery Administrator considerations.

## Assign eDiscovery permissions

To assign eDiscovery permissions to users in the Microsoft Purview portal, follow these steps:

1. Go to the [Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149) and sign in with an account that can assign permissions.
2. In the left pane, select **Roles & scopes** &gt; **Permissions**.
3. On **Permissions**, under **Microsoft Purview solutions**, select **Roles**.
4. On **Role groups for Microsoft Purview solutions**, select **eDiscovery Manager**.
5. On the **eDiscovery Manager** flyout, choose one of the following options based on the eDiscovery permissions that you want to assign.

    1. Select **Edit**.
    2. On **Manage eDiscovery Manager**, select **Choose users**.
    3. Search for and select the users you want to add as *eDiscovery Manager*, then select **Select**.
    4. Select **Next**.
    5. To assign users to the *eDiscovery Administrator* role group, select **Choose users**.
    6. Search for and select the users you want to add as *eDiscovery Administrator*, then select **Select**.
    7. Select **Next**.
    8. On **Review the role group and finish**, review the role group changes. Select **Save** to save the changes to the eDiscovery role groups.

Note

You can also use the **Add-eDiscoveryCaseAdmin** cmdlet to make a user an eDiscovery Administrator. However, you must assign the *Case Management* role to the user before you can use this cmdlet to make them an eDiscovery Administrator. For more information, see [Add-eDiscoveryCaseAdmin](/en-us/powershell/module/exchange/add-ediscoverycaseadmin).

On **Permissions** in the Microsoft Purview portal, you can also assign users eDiscovery-related permissions by adding them to the *Compliance Administrator*, *Organization Management*, and *Reviewer* role groups. For a description of the eDiscovery-related role-based access control roles assigned to each of these role groups, see Role-based access control roles related to eDiscovery.

## View assigned permissions

When eDiscovery users sign in to Discovery in the Microsoft Purview portal, the **Your permissions** card on the eDiscovery **Overview** tab displays their assigned permissions. This card outlines the user's access and roles, including any limitations to eDiscovery cases.

![Screenshot of the eDiscovery (Premium) Your permissions card showing assigned roles and access limitations.](media/ediscovery-your-permissions.png)

## RBAC roles related to eDiscovery

The following table lists the eDiscovery-related role-based access control roles in the Microsoft Purview portal, and shows the built-in role groups that each role belongs to by default.

| Role | Compliance Administrator | eDiscovery Manager & Administrator | Organization Management | Reviewer |
| --- | --- | --- | --- | --- |
| Case Management | ![Check mark.](media/checkmark.png) | ![Check mark.](media/checkmark.png) | ![Check mark.](media/checkmark.png) |  |
| Communication |  | ![Check mark.](media/checkmark.png) |  |  |
| Compliance Search | ![Check mark.](media/checkmark.png) | ![Check mark.](media/checkmark.png) | ![Check mark.](media/checkmark.png) |  |
| Custodian |  | ![Check mark.](media/checkmark.png) |  |  |
| Export |  | ![Check mark.](media/checkmark.png) |  |  |
| Hold | ![Check mark.](media/checkmark.png) | ![Check mark.](media/checkmark.png) | ![Check mark.](media/checkmark.png) |  |
| Manage review set tags |  | ![Check mark.](media/checkmark.png) |  |  |
| Preview |  | ![Check mark.](media/checkmark.png) |  |  |
| Review |  | ![Check mark.](media/checkmark.png) |  | ![Check mark.](media/checkmark.png) |
| RMS Decrypt |  | ![Check mark.](media/checkmark.png) |  |  |
| Search And Purge |  |  | ![Check mark.](media/checkmark.png) |  |

Note

To view the list of eDiscovery cases, a user must have at least one of the roles listed in the previous table. For users who aren't eDiscovery Administrators, the cases shown are limited to those where the user is a member.

Run the following diagnostic test to check if the *Export*, *Preview*, or *Search* roles are assigned to the designated admin account.

1. Select the **Help** control in the top right of the Microsoft Purview portal. Enter *Diag:edisRBACdiag* in search (or select the [eDiscovery RBAC Check diagnostic](https://aka.ms/PillareDisRBACDiag)) to run the **eDiscovery RBAC Check** test.
2. In the **Run diagnostics** section, enter the UPN or email address of the user trying to run an export, preview, or search task.
3. Select **Run Tests**. If the user doesn't have the necessary eDiscovery roles, assign the roles to perform the desired task.

The following sections describe each of the eDiscovery-related role-based access control roles listed in the previous table.

### Case Management role

This role lets users create, edit, delete, and control access to eDiscovery (Premium) cases in the Microsoft Purview portal. You must assign the *Case Management* role before you can use the **Add-eDiscoveryCaseAdmin** cmdlet to make a user an eDiscovery Administrator.

For more information, see [Get started with eDiscovery (Premium)](ediscovery-premium-get-started).

### Communication role

This role lets users manage all communications with the custodians identified in an eDiscovery (Premium) case. This management includes creating hold notifications, hold reminders, and escalations to management. The user can also track custodian acknowledgment of hold notifications and manage access to the custodian portal that each custodian uses to track communications for the cases where they were identified as a custodian.

For more information, see [Work with communications in eDiscovery (Premium)](ediscovery-managing-custodian-communications).

### Compliance Search role

This role lets users run the Content Search tool in the Microsoft Purview portal to search mailboxes and public folders, SharePoint Online sites, OneDrive for Business sites, Skype for Business conversations, Microsoft 365 groups, Microsoft Teams, and Viva Engage groups. This role allows a user to get an estimate of the search results and create export reports, but other roles are needed to initiate content search actions such as previewing, exporting, or deleting search results.

In Content search and eDiscovery (Standard), users who are assigned the *Compliance Search* role but don't have the *Preview* role can preview the results of a search when a user assigned the *Preview* role initiates the preview action. The user without the *Preview* role can preview results for up to two weeks after the initial preview action was created.

Similarly, users in Content search and eDiscovery (Standard) who are assigned the *Compliance Search* role but don't have the *Export* role can download the results of a search when a user assigned the *Export* role initiates the export action. The user without the *Export* role can download the results of a search for up to two weeks after the initial export action was created. After that, they can't download the results unless someone with the *Export* role restarts the export.

The two-week grace period for previewing and exporting search results (without the corresponding search and export roles) doesn't apply to eDiscovery (Premium). Users must be assigned the *Preview* and *Export* roles to preview and export content in eDiscovery (Premium).

### Custodian role

This role lets users identify and manage custodians for eDiscovery (Premium) cases and use the information from Microsoft Entra ID and other sources to find data sources associated with custodians. The user can associate other data sources such as mailboxes, SharePoint sites, and Teams with custodians in a case. The user can also place a legal hold on the data sources associated with custodians to preserve content in the context of a case.

For more information, see [Work with custodians in eDiscovery (Premium)](ediscovery-managing-custodians).

### Export role

This role lets users export the results of a Content Search to a local computer. It also lets them prepare search results for analysis in eDiscovery (Premium).

For more information about exporting search results, see [Export search results from Microsoft Purview portal](ediscovery-export-search-results).

### Hold role

This role lets users place content on hold in mailboxes, public folders, sites, Skype for Business conversations, and Microsoft 365 groups. When content is on hold, content owners can still modify or delete the original content, but the content is preserved until the hold is removed or until the hold duration expires.

For more information about holds, see:

- [Create a hold in eDiscovery (Standard)](ediscovery-create-holds)
- [Create a hold in eDiscovery (Premium)](ediscovery-add-custodians-to-case)

### Manage review set tags role

This role lets users create, edit, and delete review set tags for cases they can access. Users need to at least have the *Review* role and this role to [manage tags](ediscovery-tagging-documents) during reviews.

### Preview role

This role lets users view a list of items that a Content Search returns. They can also open and view each item from the list to view its contents.

### Review role

This role lets users access review sets in [eDiscovery (Premium)](ediscovery-overview). Users who are assigned this role can see and open the list of cases on the **eDiscovery &gt; Premium** page in the Microsoft Purview portal that they're members of. After the user accesses an eDiscovery (Premium) case, they can select **Review sets** to access case data. This role doesn't allow the user to preview the results of a collection search that's associated with the case or do other search or case management tasks. Users with this role can only access the data in a review set.

### RMS Decrypt role

This role lets users view rights-protected email messages when previewing search results and export decrypted rights-protected email messages. This role also lets users view and export a file that's encrypted with a [Microsoft encryption technology](encryption) when the encrypted file is attached to an email message that's included in the results of an eDiscovery search. Additionally, this role lets users review and query encrypted email attachments that are added to a review set in eDiscovery (Premium). For more information about decryption in eDiscovery, see [Decryption in Microsoft 365 eDiscovery tools](ediscovery-decryption).

### Search And Purge role

This role lets users perform bulk removal of data matching the criteria of a content search. For more information, see [Search for and delete email messages in your organization](ediscovery-search-for-and-delete-email-messages).

## Add role groups as members of eDiscovery cases

You can add role groups as members of eDiscovery (Standard) and eDiscovery (Premium) cases so that members of the role groups can access and perform tasks in the assigned cases. The roles assigned to the role group define what members of the role group can do. Adding a role group as a member of the case lets members access and perform those tasks in a specific case. For more information about adding role groups as members of cases, see:

- [Get started with eDiscovery (Standard)](ediscovery-standard-get-started#step-5-optional-add-members-to-an-ediscovery-standard-case)
- [Add or remove members from an eDiscovery (Premium) case](ediscovery-add-or-remove-members-from-a-case)

If you add or remove a role from a role group, the role group is automatically removed as a member of any case it belongs to. This behavior protects your organization from inadvertently providing extra permissions to members of a case. Similarly, if you delete a role group, you remove it from all cases it was a member of.

Before you add or remove roles to a role group that might be a member of an eDiscovery case, run the following commands in [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) to get a list of cases the role group is a member of. After you update the role group, add the role group back as a member of those cases.

### Get a list of eDiscovery (Standard) cases a role group is assigned to

```powershell
Get-ComplianceCase -RoleGroup "Name of role group"
```

### Get a list of eDiscovery (Premium) cases a role group is assigned to

```powershell
Get-ComplianceCase -RoleGroup "Name of role group" -CaseType AdvancedEdiscovery
```

## eDiscovery Administrator considerations

- **Why create an eDiscovery Administrator?** An eDiscovery Administrator is a member of the *eDiscovery Manager* role group who can view and access all eDiscovery cases in your organization. This ability to access all the eDiscovery cases has two important purposes:

    - If a person who is the only member of an eDiscovery case leaves your organization, no one (including members of the *Organization Management* role group or another member of the *eDiscovery Manager* role group) can access that eDiscovery case because they aren't a member of a case. In this situation, there's no way to access the data in the case. But because an eDiscovery Administrator can access all eDiscovery cases in the organization, they can view the case and add themselves or another eDiscovery manager as a member of the case.
    - Because an eDiscovery Administrator can view and access all eDiscovery (Standard) and eDiscovery (Premium) cases, they can audit and oversee all cases and associated compliance searches. This functionality can help to prevent any misuse of compliance searches or eDiscovery cases. And because eDiscovery Administrators can access potentially sensitive information in the results of a compliance search, you should limit the number of people who are eDiscovery Administrators.
- **Can I add a group as a member of the eDiscovery Manager role group?** As described in the Prerequisites section, you can add a mail-enabled security group as a member of the eDiscovery Managers subgroup in the *eDiscovery Manager* role group by using the **Add-RoleGroupMember** cmdlet in Security & Compliance PowerShell. For example, you can run the following command to add a mail-enabled security group to the *eDiscovery Manager* role group.

    ```powershell
    Add-RoleGroupMember "eDiscoveryManager" -Member <name of security group>
    ```

    Exchange distribution groups and Microsoft 365 Groups aren't supported. You must use a mail-enabled security group, which you can create in Exchange Online PowerShell by running `New-DistributionGroup -Type Security`. You can also create a mail-enabled security group (and add members) in the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) or in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). It might take up to 60 minutes after you create it for a new mail-enabled security group to be available to add to the eDiscovery Managers role group.

    You can't make a mail-enabled security group an eDiscovery Administrator by using the **Add-eDiscoveryCaseAdmin** cmdlet in Security & Compliance PowerShell. You can only add individual users as eDiscovery Administrators.

    You also can't add a mail-enabled security group as a member of a case.