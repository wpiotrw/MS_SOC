---
layout: Conceptual
title: Identify who modified mailbox rules | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-identify-mailbox-rules
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to track mailbox rule changes in Exchange Online. Use audit logs and PowerShell commands to find who created, modified, or deleted rules.
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
document_id: 9acc1189-b309-5297-796c-13e622483611
document_version_independent_id: 9acc1189-b309-5297-796c-13e622483611
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-identify-mailbox-rules.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-identify-mailbox-rules
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-identify-mailbox-rules.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 74e074a8-fa93-2892-eaea-8abb83760a55
---

# Identify who modified mailbox rules | Microsoft Learn

This guide explains how to investigate changes to mailbox rules in Exchange Online, including how to view a mailbox's current inbox and forwarding rules and how to search the Microsoft Purview audit log to identify who created, modified, or deleted those rules.

Use these methods to investigate:

- Changes to email forwarding rules
- Rules that cause emails to not appear in expected folders
- Unauthorized rule modifications

## Before you begin

To investigate mailbox rule modifications, you need:

- The *Audit Logs* role assigned in Microsoft Purview
- To connect to Exchange Online PowerShell by using [Connect-ExchangeOnline](/en-us/powershell/module/exchangepowershell/connect-exchangeonline)

## How to identify mailbox rule modifications

Use Get-InboxRule to check current mailbox rules and Search-UnifiedAuditLog to find mailbox rule modifications.

### Check current mailbox rules

The Get-InboxRule output shows:

- **Current rule configuration**: Rule configuration
- **Rule actions**: Move, delete, or forward
- **Rule status**: Enabled or disabled

To see what rules currently exist in a mailbox, run the following command:

```powershell
Get-InboxRule -Mailbox <mailbox> | FL Name,Description,DeleteMessage,MoveToFolder,Enabled
```

### Search for rule modification audit records

The Search-UnifiedAuditLog command looks for:

- **New-InboxRule**: New rules created
- **Set-InboxRule**: Existing rules modified
- **Remove-InboxRule**: Rules deleted

To find out who created, modified, or deleted mailbox rules, run the following command:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <user1,user2> -Operations New-InboxRule,Set-InboxRule,Remove-InboxRule -ResultSize 1000
```

## What to do when searches return no results

If your audit searches don't find rule modification records:

1. **Expand the date range** to capture older changes:

```powershell
Search-UnifiedAuditLog -StartDate 01/01/2020 -EndDate 03/31/2020 -UserIds <user1,user2> -Operations New-InboxRule,Set-InboxRule,Remove-InboxRule -ResultSize 1000
```

1. **Enable auditing** for future rule changes:

```powershell
Set-Mailbox <mailbox> -AuditEnabled $true -AuditOwner @{Add="Create","Update"}
```

## Quick reference

### Key operations for rule investigation

The following table lists the mailbox rule operations that appear in audit results.

| Operation | Description |
| --- | --- |
| New-InboxRule | New mailbox rule created. |
| Remove-InboxRule | Mailbox rule deleted. |
| Set-InboxRule | Existing mailbox rule modified. |

### Essential commands

The following commands are the primary tools for investigating mailbox rule changes.

| Command | Purpose |
| --- | --- |
| `Get-InboxRule -Mailbox <mailbox>` | Check current rule configuration. |
| `Search-UnifiedAuditLog -Operations New-InboxRule,Set-InboxRule,Remove-InboxRule` | Find who made rule changes. |