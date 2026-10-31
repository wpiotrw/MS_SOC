---
layout: Conceptual
title: Search the audit log for mailbox activities in specific mailboxes | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-search-for-mailbox-activities
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to search for mailbox activities in Microsoft Purview Audit, including shared mailboxes. Follow step-by-step instructions to investigate and resolve issues.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-03-23T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
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
ai-usage: ai-assisted
locale: en-us
document_id: 01593364-1370-fb63-bf22-eb831bec6f87
document_version_independent_id: 01593364-1370-fb63-bf22-eb831bec6f87
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-search-for-mailbox-activities.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-search-for-mailbox-activities
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-search-for-mailbox-activities.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 0cc17fbd-4dcf-2c88-6f98-ce97e2c94c5a
---

# Search the audit log for mailbox activities in specific mailboxes | Microsoft Learn

This article explains how to search for mailbox activities in Microsoft Purview Audit for a specific mailbox, including shared mailboxes. It covers common investigation scenarios, such as when mailbox audit logs are missing or can't be found. It provides step-by-step instructions to verify auditing configuration, permissions, retention policies, and search methods.

## Before you begin

To complete the steps in this article, you need:

- The email address of the affected mailbox.
- The license type assigned to the affected mailbox.
- Details about the operation you're searching for and the date and time it occurred.
- An understanding of how audit log searches are performed in Microsoft Purview Audit.

## Check mailbox auditing status

Note

Before searching for audit activity, verify that mailbox auditing is enabled for the affected user.

Complete the following steps to confirm that mailbox auditing is enabled:

1. In Exchange Online PowerShell, run the following command to check the organization-level audit configuration:

    ```powershell
    Get-AdminAuditLogConfig | FL UnifiedAudit*
    ```

    Note

    Run this command in Exchange Online PowerShell. In Security & Compliance PowerShell, the `UnifiedAuditLogIngestionEnabled` property always returns `False`, even when auditing is enabled.
2. Check if mailbox audit logs are disabled at the tenant level:

    ```powershell
    Get-OrganizationConfig | FL AuditDisabled
    ```
3. At the mailbox level, `AuditEnabled` always returns `True`, even if auditing is disabled for a specific mailbox. To verify, use:

    ```powershell
    Get-Mailbox -Filter {AuditEnabled -eq "True"}
    ```

If you receive an error that the mailbox can't be found, auditing is disabled for that mailbox. For more information, see [Verify the auditing status for your organization](audit-log-enable-disable#verify-the-auditing-status-for-your-organization).

## Verify administrator permissions

Ensure that you have the required permissions to search or export audit logs:

1. In the Microsoft Purview portal, go to **Settings** &gt; **Roles and scopes** &gt; **Role groups**.
2. Verify that your account is assigned to the **View-Only Audit Logs** or **Audit Logs** role.
3. In the Exchange admin center, use the **Audit Logs** role to enable or disable auditing and access audit cmdlets. Use the **View-Only Audit Logs** role to grant read-only access to audit logs.

For more information, see [Assign permissions to search the audit log](audit-get-started#step-2-assign-permissions-to-search-the-audit-log).

## Check audit log retention policies

Audit log retention policies determine whether older activities are still available:

1. Determine when the activity occurred.
2. By default, audit logs are retained for 180 days.
3. If the affected user doesn't have an Audit (Premium) license and no audit retention policy is configured, audit logs older than 180 days aren't available.

For more information, see [Get-UnifiedAuditLogRetentionPolicy](/en-us/powershell/module/exchangepowershell/get-unifiedauditlogretentionpolicy).

## Search for mailbox activities in Microsoft Purview Audit

When searching for activities, use the correct filters based on mailbox type.

### User mailbox – recommended audit filters

- **Date and time range (UTC)**: Specify when the activity occurred. Audit timestamps are always in UTC.
- **Users**: Enter the affected mailbox.
- **Activities – operation names**: Select the specific operation you're looking for.
- **Activities – friendly names**: Alternatively, use the friendly activity names from the dropdown list.

### Shared mailbox – recommended audit filters

- **Date and time range (UTC)**: Specify when the activity occurred.
- **Keywords**: Enter the primary SMTP address or Exchange GUID of the shared mailbox.

Note

When searching for shared mailbox activities, enter the SMTP address under the **Keywords** field, not the **Users** field.

## Shared mailbox auditing specifics

By default, the system doesn't audit all actions for shared mailboxes. The audited actions depend on the role of the person accessing the mailbox:

- **Owner**: The account associated with the mailbox.
- **Delegate**: A user with SendAs, SendOnBehalf, or FullAccess permissions to another mailbox. This role can include admins assigned FullAccess to a user's mailbox.
- **Admin**: Access via Microsoft eDiscovery tools in Microsoft Purview or Exchange Online, use of the Microsoft Exchange Server MAPI Editor, or access by an account impersonating another user (with the ApplicationImpersonation role).

Before searching, check the official documentation to confirm whether the action you're investigating is audited for the specific sign-in type. See [Mailbox actions for user mailboxes and shared mailboxes](audit-mailboxes#mailbox-actions-for-user-mailboxes-and-shared-mailboxes).