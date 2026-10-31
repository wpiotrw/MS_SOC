---
layout: Conceptual
title: Learn about properties in Exchange audit records | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-exchange-properties
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Understand Exchange audit records with this guide to primary properties, JSON structures, and PowerShell examples for mailbox activity analysis.
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
document_id: 264f7aa9-4e5e-8c9a-c71c-dbe5d299ac35
document_version_independent_id: 264f7aa9-4e5e-8c9a-c71c-dbe5d299ac35
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-exchange-properties.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-exchange-properties
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-exchange-properties.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: 53c836fd-afdf-586e-b4dd-1a084ee66679
---

# Learn about properties in Exchange audit records | Microsoft Learn

This article explains the properties and fields you see in Exchange audit records returned by [Search‑UnifiedAuditLog](/en-us/powershell/module/exchangepowershell/search-unifiedauditlog). It's written for Exchange and Microsoft 365 admins who investigate mailbox activity or build scripts to parse audit output. You find a concise description of primary properties, representative AuditData JSON for common operations, PowerShell extraction examples, and a quick reference for common property values and investigation scenarios.

Use this reference to understand:

- Key properties in audit record results
- What each field represents and contains
- Common property values and their meanings
- How to extract basic information from audit data

## Audit record structure reference

Exchange audit records contain several key properties that provide different types of information about the audited activity.

### Primary audit record properties

When you run Search-UnifiedAuditLog, each result contains these main properties:

| Property | Data Type | Description | Example value |
| --- | --- | --- | --- |
| AuditData | JSON String | Detailed JSON data about the activity | Complex JSON structure |
| CreationDate | DateTime | When the activity occurred | 11/17/2025 2:30:15 PM |
| Identity | GUID | Unique identifier for the audit record | 00aa00aa-bb11-cc22-dd33-44ee44ee44ee |
| Operations | String | What type of activity occurred | SoftDelete, HardDelete, Move |
| ResultCount | Integer | Total results available | 150 |
| ResultIndex | Integer | Position in search results | 1, 2, 3... |
| UserIds | String | Who performed the activity | `<user@domain.com>` |

### AuditData JSON structure reference

The *AuditData* property contains detailed information in JSON format. Here are some typical JSON response structures for common operations:

- **Email deletion (SoftDelete/HardDelete)**

```json
{   
  "CreationTime": "2025-11-17T14:30:15",   
  "Id": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",   
  "Operation": "SoftDelete",   
  "OrganizationId": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",   
  "RecordType": 2,   
  "ResultStatus": "Success",   
  "UserKey": "user@domain.com",   
  "UserType": 0,   
  "Version": 1,   
  "Workload": "Exchange",   
  "ClientIP": "192.168.1.100",   
  "ObjectId": "AAMkADM2NDIyMzUzLWE1ZjQtNGVkNS04OGE3LTg5NzY4ZDc1ZTZhNwBGAAAAAAC7...",   
  "UserId": "user@domain.com",   
  "ClientInfoString": "Client=OWA;Mozilla/5.0...",   
  "ExternalAccess": false,   
  "InternalLogonType": 0,   
  "MailboxGuid": "87654321-4321-4321-4321-210987654321",   
  "MailboxOwnerUPN": "mailboxowner@domain.com",   
  "LogonType": 0,   
  "Item": {   
    "Id": "AAMkADM2NDIyMzUzLWE1ZjQtNGVkNS04OGE3LTg5NzY4ZDc1ZTZhNwBGAAAAAAC7...",   
    "Subject": "Meeting Request - Q4 Planning",   
    "ParentFolder": {   
      "Id": "AAMkADM2NDIyMzUzLWE1ZjQtNGVkNS04OGE3LTg5NzY4ZDc1ZTZhNwAuAAAAAAC7...",   
      "Name": "Inbox",   
      "Path": "[\\Inbox](file:///\\inbox\)"   
    }   
  },   
  "SessionId": "11111111-2222-3333-4444-555555555555"   
}
```

- **Mailbox rule creation (New-InboxRule)**

```json
{   
  "CreationTime": "2025-11-17T14:45:22",   
  "Id": "98765432-8765-8765-8765-876543218765",   
  "Operation": "New-InboxRule",   
  "OrganizationId": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",   
  "RecordType": 1,   
  "ResultStatus": "Success",   
  "UserKey": "user@domain.com",   
  "UserType": 0,   
  "Version": 1,   
  "Workload": "Exchange",   
  "ClientIP": "10.0.0.50",   
  "ObjectId": "InboxRule:aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",   
  "UserId": "user@domain.com",   
  "ClientInfoString": "Client=WebServices;ExchangeWebServices",   
  "MailboxGuid": "87654321-4321-4321-4321-210987654321",   
  "MailboxOwnerUPN": "mailboxowner@domain.com",   
  "Parameters": \[   
    {   
      "Name": "Name",   
      "Value": "Move Microsoft Security Emails"   
    },   
    {   
      "Name": "MoveToFolder",   
      "Value": "[\\Inbox\\Security](file:///\\inbox\Security)"   
    },   
    {   
      "Name": "From",   
      "Value": "security-noreply@microsoft.com"   
    }   
  \],   
  "SessionId": "22222222-3333-4444-5555-666666666666"   
} 
```

- **Mailbox access (MailItemsAccessed)**

```json
{   
  "CreationTime": "2025-11-17T15:00:10",   
  "Id": "13579246-1357-1357-1357-135792468135",   
  "Operation": "MailItemsAccessed",   
  "OrganizationId": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",   
  "RecordType": 50,   
  "ResultStatus": "Success",     
  "UserKey": "user@domain.com",   
  "UserType": 0,   
  "Version": 1,   
  "Workload": "Exchange",   
  "ClientIP": "203.0.113.45",   
  "UserId": "user@domain.com",   
  "ClientInfoString": "Client=ActiveSync;Apple-iPhone/1309.63",   
  "MailboxGuid": "87654321-4321-4321-4321-210987654321",   
  "MailboxOwnerUPN": "mailboxowner@domain.com",   
  "ClientAppId": "00000002-0000-0ff1-ce00-000000000000",   
  "Folders": \[   
    {   
      "Id": "AAMkADM2NDIyMzUzLWE1ZjQtNGVkNS04OGE3LTg5NzY4ZDc1ZTZhNwAuAAAAAAC7...",   
      "Path": "[\\Inbox](file:///\\inbox\)",   
      "FolderItems": \[   
        {   
          "Id": "AAMkADM2NDIyMzUzLWE1ZjQtNGVkNS04OGE3LTg5NzY4ZDc1ZTZhNwBGAAAAAAC7...",   
          "Subject": "Weekly Status Report"   
        }   
      \]   
    }   
  \],   
  "OperationCount": 5,   
  "SessionId": "33333333-4444-5555-6666-777777777777"   
} 
```

Here are the key fields organized by category:

**User and session information**

| Field | Data type | Description | Example value |
| --- | --- | --- | --- |
| ClientInfoString | String | Client application information | Client=OWA, Client=WebServices |
| ClientIP | String | IP address of the client | 192.168.1.100 |
| SessionId | GUID | Unique session identifier | 00aa00aa-bb11-cc22-dd33-44ee44ee44ee |
| UserId | String | User who performed the action | user@domain.com |
| UserKey | String | User identifier key | user@domain.com |
| UserType | String | Type of user account | Regular, Admin, System, Application |

**Activity details**

| Field | Data type | Description | Example value |
| --- | --- | --- | --- |
| CreationTime | DateTime | When the activity occurred (UTC) | 2025-11-17T14:30:15Z |
| Operation | String | Specific operation performed | SoftDelete, New-InboxRule, MailItemsAccessed |
| OrganizationId | GUID | Organization identifier | 00aa00aa-bb11-cc22-dd33-44ee44ee44ee |
| RecordType | String | Type of audit record | ExchangeItem, ExchangeAdmin |
| Workload | String | Microsoft 365 service | Exchange, SharePoint, OneDrive |

**Target information**

| Field | Data type | Description | Example value |
| --- | --- | --- | --- |
| Item.Id | String | Exchange item identifier | AAMkADM2... |
| Item.ParentFolder.Name | String | Folder name where item was located | Inbox, Sent Items, Deleted Items |
| Item.ParentFolder.Path | String | Full folder path | \Inbox, \Deleted Items |
| Item.Subject | String | Email subject line | Meeting Request |
| MailboxGuid | GUID | Target mailbox identifier | 00aa00aa-bb11-cc22-dd33-44ee44ee44ee |
| MailboxOwnerUPN | String | Mailbox owner's email address | mailboxowner@domain.com |

## Basic data extraction techniques

Use these techniques to extract and inspect key values from the AuditData JSON payload.

### Convert JSON data

To extract information from the `AuditData` JSON, use the following commands:

`\$AuditData = ConvertFrom-Json \$Results[0].AuditData``\$AuditData.UserId``\$AuditData.ClientIP``\$AuditData.MailboxOwnerUPN`

### Display key properties

To see the main properties in a readable format, use the following command:

`\$Results \| Select CreationDate, UserIds, Operations, @{Name="MailboxOwner";Expression={(ConvertFrom-Json \$\_.AuditData).MailboxOwnerUPN}} \| Format-Table -AutoSize`

## Understanding common property values

The following tables help you understand common values found in audit record properties.

### Operation types

The following table lists common Exchange audit operations and what they typically indicate during an investigation.

| Operation | Description | Investigation focus |
| --- | --- | --- |
| HardDelete | Item permanently removed | Permanent deletions |
| MailItemsAccessed | Mailbox items were accessed | Unauthorized access investigation |
| Move | Item moved between folders | Folder organization changes |
| New-InboxRule | New mailbox rule created | Rule creation investigation |
| Send | Email was sent | Email communication tracking |
| Set-InboxRule | Mailbox rule modified | Rule modification tracking |
| SoftDelete | Item moved to Deleted Items | User-initiated deletions |

### RecordType values

The following table explains common RecordType values and the Exchange activities they represent.

| RecordType | Workload | Typical operations |
| --- | --- | --- |
| ExchangeAdmin | Exchange | New-InboxRule, Set-InboxRule, Set-Mailbox |
| ExchangeAggregatedOperation | Exchange | MailItemsAccessed (bulk operations) |
| ExchangeItem | Exchange | SoftDelete, HardDelete, Move, Send |

### UserType values

UserType identifies what kind of account performed the audited action.

| UserType | Description | Investigation notes |
| --- | --- | --- |
| Admin | Administrator account | Administrative actions |
| Application | Application service principal | App-based access |
| Regular | Standard user account | Normal user activity |
| System | System or service account | Automated processes |

### ClientInfoString examples

ClientInfoString values show which client, protocol, or access method was used.

| ClientInfoString | Description | Access method |
| --- | --- | --- |
| Client=ActiveSync | Exchange ActiveSync | Mobile device sync |
| Client=IMAP4 | IMAP protocol | IMAP client access |
| Client=OWA | Outlook Web App | Web browser access |
| Client=POP3 | POP3 protocol | POP3 client access |
| Client=WebServices | Exchange Web Services (EWS) | Programmatic access |

## Quick reference

Use the following tables as a quick lookup for the most useful audit properties and PowerShell techniques.

### Essential properties for investigations

The following table highlights which audit properties are most useful for common investigation scenarios.

| Investigation type | Key properties to focus on |
| --- | --- |
| Bulk Operations | SessionId, ItemCount, ClientIP, UserIds, Operations |
| Email Deletions | CreationDate, UserIds, Operations, Item.Subject, Item.ParentFolder.Name |
| Rule Changes | UserIds, Operations, Parameters, ClientIP, MailboxOwnerUPN |
| Unauthorized Access | UserIds, ClientIP, ClientInfoString, MailboxOwnerUPN, SessionId |

### Useful PowerShell techniques

These PowerShell techniques help you inspect, filter, and present Exchange audit records more effectively.

| Technique | Command example | Purpose |
| --- | --- | --- |
| Convert JSON | `ConvertFrom-Json \$\_.AuditData` | Extract detailed audit information |
| Filter Data | `Where-Object {\$\_.ClientIP -like "192.168.\*"}` | Focus on specific criteria |
| Format Output | `Format-Table -Wrap -AutoSize` | Display results clearly |
| Group Results | `Group-Object ClientIP` | Identify patterns and anomalies |
| Select Properties | Select CreationDate, UserIds, Operations | Show only relevant information |