---
layout: Conceptual
title: Use the audit log to identify Exchange inbox rules activities | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-search-mailbox-rules
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use audit logs to identify who created, modified, or removed transport rules in Exchange Online for security and compliance investigations.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
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
ms.custom: seo-marvel-apr2020, admindeeplinkEXCHANGE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 05aade2d-29a6-079c-68cd-14a8eef4a656
document_version_independent_id: 05aade2d-29a6-079c-68cd-14a8eef4a656
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-search-mailbox-rules.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-search-mailbox-rules
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-search-mailbox-rules.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: db034ec8-a457-080e-7f4e-18c4d3c360c6
---

# Use the audit log to identify Exchange inbox rules activities | Microsoft Learn

This article explains how to determine whether a user created, modified, or removed a transport rule in Exchange Online. Transport rules, also known as mail flow rules, can significantly impact email delivery and processing, so understanding their origin is important for security and compliance investigations.

## Before you begin

Before you begin, make sure you have the following information:

- The email address of the sender or recipient targeted by the transport rule.
- The license type assigned to the affected user.
- The exact date and time when the transport rule change occurred.
- The date and time when the audit search was run. If you perform the search shortly after the transport rule update, the logs might not yet reflect the change.
- An Extended Message Trace (EMT) from the Exchange Online admin center for sample emails sent before and after the transport rule change.

You must sign in to Exchange Online PowerShell and Microsoft Purview portal to complete the audit investigation procedure.

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

## Search the audit log for rule activities

When searching in Microsoft Purview Audit, use filters to narrow your results.

Recommended audit filters:

- **Date and time range (UTC)**: Specify the exact range when the activity occurred. Audit timestamps are always in UTC.
- **Activities – operation names**:

    - New-TransportRule: Logged when you create a new transport rule.
    - Set-TransportRule: Logged when you modify an existing transport rule.
    - Disable-TransportRule: Logged when you disable a transport rule.
    - Enable-TransportRule: Logged when you enable a transport rule.
    - Remove-TransportRule: Logged when you remove a transport rule.
- **User**: Enter the email address of the person who performed the operation. This field is optional if the user identity is unknown.

By applying these filters, you can identify whether a transport rule was created, modified, enabled, disabled, or removed, and by whom.