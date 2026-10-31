---
layout: Conceptual
title: Get started with auditing solutions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-get-started
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to enable and optimize auditing solutions in Microsoft Purview for better compliance and activity tracking in your organization.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-02-18T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-audit
ms.collection:
- purview-compliance
- audit
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-apr2020
- admindeeplinkEXCHANGE
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 373c4ee3-df13-a2fa-1e32-da987111da8d
document_version_independent_id: 373c4ee3-df13-a2fa-1e32-da987111da8d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-get-started.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-get-started
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-get-started.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 893ca1a5-1965-45d6-10ee-db43032e1699
---

# Get started with auditing solutions | Microsoft Learn

Microsoft Purview Audit (Standard) and Audit (Premium) enable you to search for audit records of activities that users and admins perform in different Microsoft services. Because Audit (Standard) is enabled by default for most Microsoft 365 organizations, you only need to complete a few steps before you and others in your organization can search the audit log. To use features available only in Audit (Premium), you need to complete a few more configuration steps.

For more information about Audit (Standard) and Audit (Premium) capabilities, see [Microsoft Purview auditing solutions](audit-solutions-overview).

## Step 1: Verify organization subscription and billing

Licensing for Audit (Standard) and Audit (Premium) requires the appropriate organization subscription that provides access to the audit log search tool and per-user licensing that's required to log and retain audit records.

When a user or admin performs an audited activity, the system generates an audit record and stores it in the audit log for your organization. In Audit (Standard) and Audit (Premium), you can retain and search audit records in the audit log for 180 days.

Important

The default retention period for Audit (Standard) changed from 90 days to 180 days. Audit (Standard) logs that were generated before October 17, 2023, are retained for 90 days. Audit (Standard) logs that are generated on or after October 17, 2023, follow the new default retention of 180 days.

For a list of subscription and licensing requirements for these auditing solutions, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Audit (Standard) and Audit (Premium).

To audit user interactions with non-Microsoft 365 AI data, which includes information from other generative AI applications from Microsoft and connected external AI applications, you must enable [pay-as-you-go billing](purview-billing-models) for your organization. This data type includes [Copilot in Microsoft Fabric](/en-us/fabric/fundamentals/copilot-fabric-overview), [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot), [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and any connected or cloud AI application.

## Step 2: Assign permissions to search the audit log

Admins and members of investigation teams must be assigned the *View-Only Audit Logs* or *Audit Logs* role in the Microsoft Purview portal to search or export the audit log. By default, the Microsoft Purview portal **Role groups** page assigns these roles to the *Audit Reader* and *Audit Manager* role groups.

Note

Currently, Exchange admin center permissions are required to enable or disable auditing and to access audit cmdlets. Use the existing *Audit Logs* and *View-Only Audit Logs* roles in Exchange admin center to grant access to audit cmdlets. Use the existing *Audit Logs* role in Exchange admin center to grant access to enable or disable auditing.

You can also create custom role groups with the ability to search the audit log by adding the *View-Only Audit Logs* or *Audit Logs* roles to a custom role group. For more information, see [Permissions in the Microsoft Purview portal](purview-permissions).

Note

Access to the [Audit Search Graph API](/en-us/graph/api/resources/security-api-overview?view=graph-rest-beta) requires additional permissions to be configured in Microsoft Graph. For more information, see [Permissions in Audit Search Graph API](/en-us/graph/api/security-auditcoreroot-list-auditlogqueries).

### Assign permissions to scope audit logs

To search or export the audit log, administrators or members of investigation teams must be assigned to at least one of the following audit-related role groups in the Microsoft Purview portal:

- **Audit Manager**: A user assigned to the *Audit Manager* role group can search and export the audit log and manage audit settings for the tenant (like enabling or disabling audit logging). This role group grants the *View-Only Audit Logs* and *Audit Logs* roles to the user.
- **Audit Reader**: A user assigned to the **Audit Reader** role group can only search and export the audit log. They can't enable or disable audit logging. This role group grants the *View-Only Audit Logs* role to the user.

## Step 3: Enable/Disable SearchQueryInitiatedExchange/SearchQueryInitiatedSharePoint events

*SearchQueryInitiatedExchange* must be enabled explicitly for logging when users perform searches in Exchange Online.

*SearchQueryInitiatedSharePoint* is by default enabled for logging when users perform searches in SharePoint.

To enable Exchange Online and SharePoint events to be audited for users, run the following cmdlet (for each user) in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell):

```powershell
Set-Mailbox <user> -AuditOwner @{Add="SearchQueryInitiated"} // For Exchange Online

Set-Mailbox <user> -AuditOwner @{Add="SharepointSearchQueryInitiated"} // For SharePoint. Enabled by default.
```

In a multi-geo environment, you must run the **Set-Mailbox** command in the forest where the user's mailbox is located. To identify the user's mailbox location, run the following cmdlet:

```powershell
Get-Mailbox <user identity> | FL MailboxLocations
```

If you previously ran the cmdlet to enable auditing of search queries in a forest that's different than the forest where the user's mailbox is located, remove the *SearchQueryInitiated/SharepointSearchQueryInitiated* value from the user's mailbox. To remove the value, run `Set-Mailbox -AuditOwner @{Remove="SearchQueryInitiated"} for Exchange Online and Set-Mailbox -AuditOwner @{Remove="SharepointSearchQueryInitiated"}`. Then, add it to the user's mailbox in the forest where the user's mailbox is located.

Note

These PowerShell cmdlets are valid only for SearchQueryInitiated and SharepointSearchQueryInitiated events and don't apply to other events within the audit log.

## Step 4: Set up Audit (Premium) for users

Tip

Organizations using Audit (Standard) can skip this step.

Audit (Premium) features, such as the ability to log intelligent insights, require an appropriate E5 license assigned to users. Additionally, you must enable the Advanced Auditing app/service plan for those users.

To enable the Advanced Auditing service plan for users, complete the following steps for each user:

1. In the Microsoft 365 admin center, go to **Users** &gt; [**Active users**](https://go.microsoft.com/fwlink/p/?linkid=834822), and select a user.
2. On the user properties flyout page, select **Licenses and apps**.
3. In the **Licenses** section, verify that the user is assigned an E5 license or is assigned an appropriate add-on license. For a list of licenses that support Audit (Premium), see [Audit licensing requirements](audit-solutions-overview#licensing-requirements).
4. Expand the **Apps** section and select the **Microsoft 365 Advanced Auditing** checkbox.
5. Select **Save changes**. The logging of Audit (Premium) insights begins within 24 hours.

If you customize the mailbox actions that are logged on user mailboxes or shared mailboxes, new Audit (Premium) events released by Microsoft aren't automatically audited on those mailboxes. For information about changing the mailbox actions that are audited for each sign-in type, see the "Change or restore mailbox actions logged by default" section in [Manage mailbox auditing](audit-mailboxes#change-or-restore-mailbox-actions-logged-by-default).

## Step 5: Set up audit retention policies in Audit (Premium)

Tip

Organizations using Audit (Standard) can skip this step.

In addition to the default policy that retains Microsoft Entra ID, Exchange, OneDrive, and SharePoint audit records for one year, organizations using Audit (Premium) can create audit log retention policies to meet the requirements of your organization's security operations, IT, and compliance teams.

For more information, see [Manage audit log retention policies](audit-log-retention-policies).

## Step 6: Search for audited events

Now that you have Audit (Standard) or Audit (Premium) configured for your organization, you're ready to search the audit log in the Microsoft Purview portal. For detailed guidance, see [Search the audit log](audit-search).