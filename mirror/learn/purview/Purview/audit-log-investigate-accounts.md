---
layout: Conceptual
title: Use MailItemsAccessed to investigate compromised accounts | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use the MailItemsAccessed mailbox-auditing action to trace email access and secure compromised accounts effectively.
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
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 60b1ec1b-6ac7-325d-0064-4809caa267b3
document_version_independent_id: 60b1ec1b-6ac7-325d-0064-4809caa267b3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-investigate-accounts.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-investigate-accounts
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-investigate-accounts.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2624a017-7337-44fa-9494-a407bb0e59fa
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a438284e-c3c3-4c36-ab0b-aa7c244b912c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: f4441d14-e4d5-6ad5-abfe-c4d86da63c65
---

# Use MailItemsAccessed to investigate compromised accounts | Microsoft Learn

A compromised user account (also called an *account takeover*) is a type of cyberattack where an attacker gains access to a user account and operates as the user. When investigating compromised email accounts, assume that more mail data is compromised than might be indicated by tracing the attacker's actual presence. Depending on the type of data in email messages, you might face regulatory fines unless you can prove that sensitive information wasn't exposed. For example, HIPAA-regulated organizations face significant fines if there's evidence that patient health information (PHI) was exposed.

Use the *MailItemsAccessed* mailbox-auditing action to investigate compromised email accounts by auditing accesses of mail data by mail protocols and clients. This auditing action helps you better understand email data breaches and identify the scope of compromises to specific mail items. When a cyberattacker gains access to a specific piece of mail, Exchange Online audits the event even though there's no indication that the mail item was read.

## The MailItemsAccessed mailbox-auditing action

The MailItemsAccessed action is part of [Audit (Standard)](audit-solutions-overview) functionality. It's part of [Exchange mailbox auditing](audit-mailboxes) and is enabled by default for users that are assigned an Office 365 E3/E5 or Microsoft 365 E3/E5 license.

The MailItemsAccessed mailbox-auditing action covers all mail protocols: POP, IMAP, MAPI, EWS, Exchange ActiveSync, and REST. It also covers both types of accessing mail: *sync*, where clients download sets of messages from the server, and *bind*, where a user or client accesses an individual message.

### Auditing sync access

Sync operations are only recorded when a mailbox is accessed by a desktop version of the Outlook client for Windows or Mac. During the sync operation, these clients typically download a large set of mail items from the cloud to a local computer. The audit volume for sync operations is huge. So, instead of generating an audit record for each mail item that's synced, the system generates an audit event for the mail folder containing items that were synced. All mail items in the synced folder are assumed to be compromised. The access type is recorded in the OperationProperties field of the audit record.

For an example of displaying the sync access type in an audit record, see Use MailItemsAccessed audit records for forensic investigations, specifically the procedure for checking sync activities to determine context.

### Auditing bind access

A bind operation is an individual access to an email message. For bind access, the InternetMessageId of individual messages is recorded in the audit record. The MailItemsAccessed audit action records bind operations and then aggregates them into a single audit record. All bind operations that occur within a 2-minute interval are aggregated in a single audit record in the Folders field within the AuditData property. Each message that was accessed is identified by its InternetMessageId. The number of bind operations that were aggregated in the record is displayed in the OperationCount field in the AuditData property.

For an example of displaying the bind access type in an audit record, see the "Check for bind activities" procedure in Use MailItemsAccessed audit records for forensic investigations.

## Use MailItemsAccessed audit records for forensic investigations

Mailbox auditing generates audit records for access to email messages so that you can be confident that email messages aren't compromised. In circumstances where data access is uncertain, assume that the data is compromised by recording all mail access activity.

Use MailItemsAccessed audit records for forensic purposes after a data breach is resolved and the bad actor is evicted. Complete the following steps to begin your investigation:

1. Identify the set of mailboxes that the bad actor compromised.
2. Determine the time frame when the bad actor had access to mailboxes in your organization.
3. Use the **Search-UnifiedAuditLog** cmdlet in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) to search audit records that correspond to the data breach.

Run one of the following commands to search for MailItemsAccessed audit records:

**Unified audit log**:

```powershell
Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <user1,user2> -Operations MailItemsAccessed -ResultSize 1000
```

Complete the following steps to use MailItemsAccessed audit records to investigate a compromised user account. Each step includes the command syntax for the **Search-UnifiedAuditLog** cmdlet.

1. Check for sync activities. If a bad actor uses an email client to download messages in a mailbox, they can disconnect the computer from the Internet and access the messages locally without interacting with the server. In this case, mailbox auditing can't audit these activities.

    To search for MailItemsAccessed records where the mail items are accessed by a sync operation, run the following command:

    **Unified audit log**:

    ```powershell
    Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 02/20/2020 -UserIds <user1,user2> -Operations MailItemsAccessed -ResultSize 1000 | Where {$_.AuditData -like '*"MailAccessType","Value":"Sync"*'} | FL
    ```
2. Check sync activities to determine if any of them happen in the same context as the one used by the bad actor to access the mailbox. Context is identified and differentiated by the IP address of the client computer used to access the mailbox and the mail protocol.

    Use the properties listed in the following table to investigate. These properties are located in the **AuditData** or **OperationProperties** property. If any of the syncs occur in the same context as the bad actor activity, assume the bad actor synced all mail items to their client, which means the entire mailbox is compromised.

    | Property | Description |
    | --- | --- |
    | ClientInfoString | Describes protocol, client (includes version) |
    | ClientIPAddress | IP address of the client machine. |
    | SessionId | Session ID helps to differentiate bad actor actions vs day-to-day user activities on the same account (useful for compromised accounts) |
    | UserId | UPN of the user reading the message. |
3. Check for bind activities. After checking for sync activities and comparing their context to bad actor activity, you can be confident that all other access to email messages by the bad actor is captured in the MailItemsAccessed audit records that have a MailAccessType property with a value of "Bind".

    To search for MailItemsAccessed records where the mail items are accessed by a Bind operation, run the following command.

    **Unified audit log**:

    ```powershell
    Search-UnifiedAuditLog -StartDate 01/06/2020 -EndDate 01/20/2020 -UserIds <user1,user2> -Operations MailItemsAccessed -ResultSize 1000 | Where {$_.AuditData -like '*"MailAccessType","Value":"Bind"*'} | FL
    ```

    Email messages that are accessed are identified by their internet message ID. You can also check to see if any audit records have the same context as the ones for other bad actor activity.

    You can use the audit data for bind operations in two different ways:

    - Access or collect all email messages the bad actor accessed by using the InternetMessageId to find them and then checking to see if any of those messages contains sensitive information.
    - Use the InternetMessageId to search audit records related to a set of potentially sensitive email messages. This is useful if you're concerned only about a few messages.

## Filter duplicate audit records

To remove auditing noise, the system filters out duplicate audit records for the same bind operations that occur within an hour of each other. The system also filters out sync operations at one-hour intervals. An exception to this deduplication process occurs if, for the same InternetMessageId, any of the properties described in the following table are different. If one of these properties is different in a duplicate operation, the system generates a new audit record. The following table describes each property in more detail.

| Property | Description |
| --- | --- |
| ClientIPAddress | IP address of the client computer. |
| ClientInfoString | The client protocol, client used to access the mailbox. |
| ParentFolder | The full folder path of the mail item that was accessed. |
| Logon\_type | The logon type of the user who performed the action. The logon types (and their corresponding Enum value) are Owner (0), Admin (1), or Delegate (2). |
| MailAccessType | Whether the access is a bind or a sync operation. |
| MailboxUPN | The UPN of the mailbox where the message being read is located. |
| User | The UPN of the user reading the message. |
| SessionId | The Session ID helps to differentiate attacker actions and day-to-day user activities in the same mailbox (if an account is compromised). For more information about sessions, see [Contextualizing attacker activity within sessions in Exchange Online](https://techcommunity.microsoft.com/t5/exchange-team-blog/contextualizing-attacker-activity-within-sessions-in-exchange/ba-p/608801). |