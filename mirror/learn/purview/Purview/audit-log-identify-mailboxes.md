---
layout: Conceptual
title: Investigate shared mailbox activities using audit logs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-identify-mailboxes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to use Microsoft Purview audit logs to monitor shared mailbox activities, including email deletions, delegate access, and rule modifications.
f1.keywords:
- NOCSH
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
document_id: 4626c77a-c5a3-24c8-4443-3300a5d28ea7
document_version_independent_id: 4626c77a-c5a3-24c8-4443-3300a5d28ea7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-identify-mailboxes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-identify-mailboxes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-identify-mailboxes.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: ba8deda8-d461-6eb8-1bb7-a43219b08ae3
---

# Investigate shared mailbox activities using audit logs | Microsoft Learn

This article explains how to investigate shared mailbox activity by using the Microsoft Purview audit log and Exchange Online PowerShell. It describes practical search patterns and remediation steps to find deletions, sent‑as activity, folder browsing, mailbox rule and forwarding changes, and other delegate actions.

Use these methods to investigate:

- Email deletions from shared mailboxes
- Who sent emails from shared mailboxes
- Delegate access activities
- Email moves between folders
- Forwarding and rule configurations
- Missing emails in shared mailboxes

## Before you begin

To investigate shared mailbox activities, you need:

- The *Audit Logs* role assigned in Microsoft Purview
- To connect to Exchange Online PowerShell by using [Connect-ExchangeOnline](/en-us/powershell/module/exchangepowershell/connect-exchangeonline)

## How to investigate shared mailbox activities

Use these methods to investigate activities in shared mailboxes. Choose the method based on the type of activity you're investigating.

### Search for deleted emails in shared mailboxes

To search for audit records of email deletions from a shared mailbox, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -FreeText <shared-mailbox@domain.com> -Operations SoftDelete,HardDelete,MoveToDeletedItems -ResultSize 500
```

This command searches for:

- **SoftDelete**: Items moved to Deleted Items folder.
- **HardDelete**: Items permanently removed from mailbox.
- **MoveToDeletedItems**: Items moved to Deleted Items by user action.

### Search for emails sent from shared mailboxes

To identify who sent emails from a shared mailbox using delegate permissions, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <user1,user2> -FreeText <shared-mailbox@domain.com> -Operations SendAs -ResultSize 500
```

### Search for email moves between folders

To search for move operations in a shared mailbox, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <user1,user2> -FreeText <shared-mailbox@domain.com> -Operations Move,MoveToDeletedItems -ResultSize 300
```

### Monitor delegate folder access (FolderBind)

To track when delegates browse specific folders in shared mailboxes, use the following steps:

**Check FolderBind configuration:**

```powershell
Get-Mailbox <shared-mailbox@domain.com> | Select AuditDelegate | Where-Object {$_.AuditDelegate -contains "FolderBind"}
```

**Enable FolderBind auditing:**

```powershell
Set-Mailbox <shared-mailbox@domain.com> -AuditDelegate @{Add="FolderBind"}
```

**Search for folder browsing activities:**

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -FreeText <shared-mailbox@domain.com> -Operations FolderBind -ResultSize 500
```

Important

FolderBind tracks delegate and admin folder access only. It doesn't log shared mailbox owners browsing folders. Enable it proactively for compliance and security monitoring.

**Common use cases:**

- Monitor access to confidential folders in executive shared mailboxes
- Compliance audit trails for regulatory requirements
- Security investigations of unauthorized folder browsing
- Delegate behavior analysis for governance

### Investigate delegate access activities

To identify users with delegate permissions to a shared mailbox, run the following command:

```powershell
Get-MailboxPermission <shared-mailbox@domain.com> | Where-Object {$_.AccessRights -eq "FullAccess"}
```

To search for activities performed by a specific delegate, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <delegate@domain.com> -ResultSize 500
```

Important

Use `-UserIds` to find activities performed **BY** a specific delegate user. Don't use `-UserIds` with the shared mailbox address, as this action doesn't return delegate activities performed **IN** the shared mailbox. For activities performed in the shared mailbox by any user (including delegates), use the `-FreeText` parameter as shown in other sections.

### Monitor email access activities

Note

This command requires Microsoft 365 E5 licensing to capture `MailItemsAccessed` operations.

To search for email access activities in shared mailboxes, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <user1,user2> -FreeText <shared-mailbox@domain.com> -Operations MailItemsAccessed -ResultSize 200
```

### Search for email forwarding configuration

To find who configured email forwarding on a shared mailbox, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <user1,user2> -FreeText <shared-mailbox@domain.com> -Operations Set-Mailbox -ResultSize 200
```

### Search for mailbox rule modifications

To search for inbox rule creation or modification activities, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -FreeText <shared-mailbox@domain.com> -Operations New-InboxRule,Set-InboxRule -ResultSize 100
```

Tip

For comprehensive mailbox rule investigation, see [Identify who modified mailbox rules](audit-log-identify-mailbox-rules) for detailed guidance on identifying who created, modified, or deleted mailbox rules that might be affecting email delivery.

## What to do when searches return no results

If your audit log searches don't find shared mailbox activity records, try these steps to verify the auditing configuration.

### Verify and enable mailbox auditing

1. Check if auditing is enabled at the organization level.

```powershell
Get-OrganizationConfig | Select AuditDisabled
```

1. Check if auditing is enabled for the specific shared mailbox.

```powershell
Get-Mailbox <shared-mailbox@domain.com> | Select AuditEnabled
```

1. Enable auditing if it's disabled.

```powershell
Set-OrganizationConfig -AuditDisabled $false
Set-Mailbox <shared-mailbox@domain.com> -AuditEnabled $true
```

## Advanced procedures

The following commands apply common shared mailbox fixes:

To enable sent items copying to shared mailbox (so sent emails appear in shared mailbox Sent Items), run the following command:

```powershell
Set-Mailbox <shared-mailbox@domain.com> -MessageCopyForSentAsEnabled $true
```

To remove email forwarding from a shared mailbox, run the following command:

```powershell
Set-Mailbox <shared-mailbox@domain.com> -ForwardingSmtpAddress $null
```

## Quick reference

The following tables summarize common audit operations and key search parameters for shared mailbox investigations.

### Common audit operations for shared mailboxes

The following table lists common audit operations you can use when investigating shared mailbox activity.

| Operation | Description | Investigation Focus |
| --- | --- | --- |
| Create | Emails created or sent | Email creation activities |
| FolderBind | **Delegate folder access/browsing** | **Monitor who accessed specific folders** |
| HardDelete | Items permanently deleted | Permanent deletions from shared mailbox |
| MailItemsAccessed | Mailbox items accessed | Email access tracking (E5 required) |
| Move | Items moved between folders | Folder organization changes |
| New-InboxRule | Inbox rules created | Rule creation investigation |
| SendAs | Emails sent using delegate permissions | Identify who sent from shared mailbox |
| Set-Mailbox | Mailbox settings modified | Forwarding and configuration changes |
| SoftDelete | Items moved to Deleted Items folder | User deletions from shared mailbox |

### Key search parameters

The following table describes the main parameters used in the shared mailbox audit log search examples.

| Parameter | Description | Example |
| --- | --- | --- |
| -FreeText | Activities performed in a specific mailbox | `<shared-mailbox@domain.com>` |
| -Operations | Filter by operation type | SoftDelete,HardDelete,SendAs |
| -ResultSize | Limit results (max 5000) | 500 (standard), 1000 (comprehensive) |
| -StartDate/-EndDate | Define investigation timeframe | 01/06/2020, 01/20/2020 |
| -UserIds | Activities performed by a specific user | `<delegate@domain.com>` |

Important

Replace `<shared-mailbox@domain.com>` and `<delegate@domain.com>` with actual email addresses before running commands.