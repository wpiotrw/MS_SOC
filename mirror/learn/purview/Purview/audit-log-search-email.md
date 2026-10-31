---
layout: Conceptual
title: Search the audit log for specific email messages | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-search-email
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Search Microsoft Purview audit logs to locate missing, moved, or accessed email messages. Learn how to use PowerShell commands for detailed investigations.
f1.keywords:
- NOCSH
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
document_id: 272c4ecc-1e8d-8694-3380-6b0d11e1da75
document_version_independent_id: 272c4ecc-1e8d-8694-3380-6b0d11e1da75
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-search-email.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-search-email
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-search-email.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: ebdc7964-4ba2-a64e-f7e9-19be1f0ee946
---

# Search the audit log for specific email messages | Microsoft Learn

Use this article to search the Microsoft Purview audit log for specific email messages that are missing, moved, or need investigation. It shows practical Exchange Online PowerShell searches and investigation steps you can use when standard audit searches don't return the records you expect.

Use these methods to investigate:

- Email migration issues
- Messages moved between folders
- Email access patterns
- Missing email items

## Before you begin

To search audit logs for specific email items, you need:

- The *Audit Logs* role assigned in Microsoft Purview
- To connect to Exchange Online PowerShell by using [Connect-ExchangeOnline](/en-us/powershell/module/exchangepowershell/connect-exchangeonline)

## Search for specific email messages

Use these methods to find audit records for specific email messages. Select the method based on what information you have about the email you're looking for.

### Search by email subject or keywords

Use the FreeText parameter to search for:

- Email subject lines
- Keywords from email content
- Sender names
- Any identifying text from the email

To search for audit records by using email subjects, keywords, or other identifying information, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -FreeText "<subject or keyword>" -ResultSize 1000
```

### Search for moved emails

To search for Move and MoveToDeletedItems operations in a mailbox, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <user1,user2> -Operations Move,MoveToDeletedItems -ResultSize 1000
```

Important

The audit feature for move operations isn't enabled by default.

### Search all email activities

To search for all email-related activities in a mailbox, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <user1,user2> -Operations Send,Create,Move,SoftDelete,HardDelete,MailItemsAccessed -ResultSize 1000
```

## What to do when searches return no result

If your audit log searches don't find the email records you're looking for, try these investigation steps.

### Missing emails after migration

Use the following steps to investigate missing emails after migration when searches return no results.

1. Check if auditing was enabled before the migration occurred.

```powershell
Get-Mailbox <mailbox> | Select AuditEnabled,WhenCreated
```

1. Expand the search date range to cover a broader timeframe.

```powershell
Search-UnifiedAuditLog -StartDate 01/01/2020 -EndDate 03/31/2020 -ObjectIds <mailbox> -ResultSize 1000
```

### Emails moved but no audit records found

Use the following steps to investigate when users move emails but you can't find audit records.

1. Check if auditing is configured for move operations.

```powershell
Get-Mailbox <mailbox> | Select AuditOwner
```

1. Enable auditing for move operations if it's not configured.

```powershell
Set-Mailbox <mailbox> -AuditOwner @{Add="Move","MoveToDeletedItems","SoftDelete","HardDelete"}
```

1. Search using additional operation types that might capture the activity.

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -ObjectIds <mailbox> -Operations Move,MoveToDeletedItems,Update -ResultSize 1000
```

## Locating specific email messages

The following steps help you investigate when you can't find audit records for specific email messages.

1. Search by subject or keywords

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -FreeText "<subject or keyword>" -ResultSize 1000 | FL
```

1. Search by user

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <sender> -ResultSize 1000 | FL
```

## Advanced investigation procedures

The following procedures help you resolve issues when standard investigation steps don't resolve the issue.

### Enable comprehensive mailbox auditing

To enable all relevant audit actions and ensure future activities are captured, run the following command:

```powershell
Set-Mailbox <mailbox> -AuditEnabled $true -AuditOwner @{Add="Move","MoveToDeletedItems","SoftDelete","HardDelete","Create"} -AuditDelegate @{Add="SendAs","Move"}
```

### Verify organization-wide audit configuration

To ensure that auditing is enabled at the organization level, run the following command:

```powershell
Set-OrganizationConfig -AuditDisabled $false
```

## Quick reference

### Search parameters

Use these key parameters to search audit logs for specific email items:

| Parameter | Description | Example |
| --- | --- | --- |
| -FreeText | Search for specific email identifiers | `<email subject or unique identifier>` |
| -Operations | Filter by deletion activity types | SoftDelete,HardDelete,MoveToDeletedItems |
| -ResultSize | Number of results to return | 1,000 (standard), 5,000 (comprehensive) |
| -StartDate/-EndDate | Define investigation timeframe | Based on when emails went missing |
| -UserIds | Filter by who performed the action | `<user1@domain.com,user2@domain.com>` |