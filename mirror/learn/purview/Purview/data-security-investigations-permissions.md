---
layout: Conceptual
title: Assign permissions in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Assign permissions in Data Security Investigations to enable access to Microsoft Purview features. Learn how to configure roles and role groups effectively.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-22T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 4d548790-2bdd-40a8-c17a-9cd3ee49dada
document_version_independent_id: 4d548790-2bdd-40a8-c17a-9cd3ee49dada
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b6aaa7e2-ae45-4450-6276-cff496e9aa19
---

# Assign permissions in Data Security Investigations | Microsoft Learn

To enable users to access Data Security Investigations capabilities and features in the Microsoft Purview portal, assign users the appropriate permissions.

This article describes the permissions required to perform specific Data Security Investigations tasks. For more information about Microsoft Purview role groups and permissions, see [Permissions in the Microsoft Purview portal](purview-permissions).

## Roles and role groups

Important

After you configure your role groups, it might take up to 30 minutes for the role group permissions to apply to assigned users across your organization.

To quickly assign the *Admin* or *Investigator* roles to users, use the **Assign roles to your team members** setup task. Complete the following steps to assign these roles:

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal with an account assigned the *Global Administrator* role.
2. Select **Overview** in the left navigation.
3. Select **Assign roles to your team members** in the **Setup tasks** section.
4. Select users in the **Admin** field on the **Role assignment** flyout pane.
5. Select users in the **Investigators** field.
6. Select **Confirm** to assign users these roles.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

You can also add users to the appropriate role group on the **Role groups** page in the [Microsoft Purview portal](purview-portal). To continue with these configuration steps in the Microsoft Purview portal, you must be assigned to the *Data Security Investigations Admins* role group.

## Configure permissions

To manage Data Security Investigations workflow and investigations, assign users to specific [role groups](/en-us/defender-office-365/scc-permissions?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview) to manage different sets of Data Security Investigations features. You can assign users with different security responsibilities to specific role groups to manage different areas of Data Security Investigations features. Or, assign all user accounts for designated admins, investigators, and reviewers to the *Data Security Investigations Admins* role group. Use a single role group or multiple role groups to best fit your security management requirements.

Tip

Always have at least one user in the *Data Security Investigations Admins* role group so that your Data Security Investigations configuration doesn't get in to a 'zero administrator' scenario if specific users leave your organization.

Choose from these solution role group options when configuring and managing Data Security Investigations:

| Actions | Data Security Investigations Admins | Data Security Investigations Investigators | Data Security Investigations Reviewers |
| --- | --- | --- | --- |
| Add, delete, manage items for a mitigation plan | Yes | Yes | Yes |
| Create and manage all investigations | Yes | No | No |
| Create and manage assigned investigations | Yes | Yes | No |
| Create searches and add items to an investigation | Yes | Yes | No |
| Estimate and preview search results | Yes | Yes | No |
| Manage investigation scope | Yes | Yes | No |
| Run categorization activities | Yes | Yes | Yes |
| Run examination activities | Yes | Yes | Yes |
| Run vector searches | Yes | Yes | Yes |
| Create and run purge queries | Yes | Yes | No |
| View data risk graphs | Yes | Yes | Yes |
| View the Pay-as-you-go usage dashboard | Yes | No | No |

Important

Global admins must be assigned to one of the listed role groups for Data Security Investigations to create and access investigations.

### Additional role groups with Data Security Investigations access

In addition to the dedicated Data Security Investigations role groups, the following Microsoft Purview role groups automatically include Data Security Investigations roles. Members of these role groups have Data Security Investigations access without needing explicit assignment to a Data Security Investigations-specific role group.

| Role group | Data Security Investigations role included | Access level |
| --- | --- | --- |
| Compliance Administrator | Data Security Investigation Admin | Full administrative access |
| Organization Management | Data Security Investigation Admin, Data Security Investigation Contributor | Administrative and contributor access |
| Data Security Management | Data Security Investigation Contributor | Contributor access |
| Insider Risk Management | Data Security Investigation Contributor | Contributor access |

Members with the *Data Security Investigation Contributor* role can create and manage investigations they own or are members of. This role doesn't include access to data storage, AI job execution, or the Pay-as-you-go usage dashboard.

For more information about these role groups and their complete role assignments, see [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/defender-office-365/scc-permissions?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

### Option 1: Assign multiple users to the Data Security Investigations Admins role group

Complete these steps to give multiple users administrative access and responsibilities for Data Security Investigations in your organization.

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, select **Roles and groups**, then select **Role groups** in the left navigation.
3. Select the *Data Security Investigations Admins* role group, then select **Edit**.
4. Select **Choose users**, then select the checkboxes for all the users you want to add to the role group.
5. Select **Select**, then select **Next**.
6. Select **Save** to add the users to the role group, then select **Done**.

### Option 2: Assign users to specific Data Security Investigations role groups

Complete these steps to assign users to specific role groups to segment Data Security Investigations access and responsibilities among different users in your organization.

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Role groups** in the left navigation.
3. Select one of the Data Security Investigations role groups, then select **Edit**.
4. Select **Choose users**, then select the checkboxes for all the users you want to add to the role group.
5. Select **Select**, then select **Next**.
6. Select **Save** to add the users to the role group.
7. Select the next Data Security Investigations role group, then repeat the previous steps for each required role group.
8. Select **Close** when you're done.