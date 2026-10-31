---
layout: Conceptual
title: Manage mailbox auditing | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-mailboxes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to manage mailbox auditing, verify default settings, and ensure compliance with predefined audit actions for your organization.
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
document_id: d72d87fb-66c4-7b01-a75e-ef4bb4b265f9
document_version_independent_id: d72d87fb-66c4-7b01-a75e-ef4bb4b265f9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-mailboxes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-mailboxes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-mailboxes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: d3c2aa30-7a20-b8b8-78db-0cd2c34e10fc
---

# Manage mailbox auditing | Microsoft Learn

Mailbox audit logging is turned on by default in all organizations. This setting automatically logs certain actions that mailbox owners, delegates, and admins perform. Admins can search the mailbox audit log for the corresponding mailbox audit records.

Some benefits of mailbox auditing on by default include:

- Auditing is automatically turned on when you create a new mailbox. You don't need to manually enable mailbox auditing for new users.
- You don't need to manage the mailbox actions that are audited. A predefined set of mailbox actions are audited by default for each sign-in type (Admin, Delegate, and Owner).
- When Microsoft releases a new mailbox action, the action might be automatically added to the list of mailbox actions that are audited by default, subject to the user having the appropriate license. Because new actions are added automatically, you don't need to add new actions on mailboxes as they're released.
- You have a consistent mailbox auditing policy across your organization because you're auditing the same actions for all mailboxes.

## Verify mailbox auditing on by default is turned on

To verify that mailbox auditing on by default is turned on for your organization, run the following command in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell):

```PowerShell
Get-OrganizationConfig | Format-List AuditDisabled
```

The value **False** indicates that mailbox auditing on by default is turned on for the organization. Mailbox auditing on by default in the organization overrides whether auditing is enabled or disabled on individual mailboxes. It doesn't override mailbox-level audit operation settings.

How organization-level and mailbox-level auditing work together:

- **If organization-level auditing is ON and mailbox-level auditing is OFF**: Organization-level auditing overrides the mailbox setting and enables auditing. The mailbox's configured audit operations apply.
- **If organization-level auditing is ON and mailbox-level auditing is ON**: Mailbox-level auditing remains enabled, and the mailbox's configured audit operations apply.

For example, if mailbox auditing on by default is turned on for the organization, the *AuditEnabled* property returned by the `Get-Mailbox` cmdlet always displays **True**. The mailbox audits mailbox activity by using the mailbox's configured mailbox actions.

To keep mailbox auditing disabled for specific mailboxes, configure *mailbox auditing bypass* for the mailbox owner and other users with delegated access to the mailbox. For more information, see Bypass mailbox audit logging.

## Supported mailbox types

The following table describes mailbox types that mailbox auditing supports by default:

| Mailbox type | Auditing supported | On by default supported |
| --- | --- | --- |
| Microsoft 365 Group mailboxes | ✔ | ✔ |
| Public folder mailboxes |  |  |
| Resource mailboxes |  |  |
| Shared mailboxes | ✔ | ✔ |
| User mailboxes | ✔ | ✔ |

Important

In a multigeo environment, cross-geo mailbox auditing isn't supported. If you assign a user permissions to access a shared mailbox in a different geo location, mailbox actions that the user performs aren't logged in the mailbox audit log of the shared mailbox. Exchange admin audit events are available for all locations via [Microsoft Purview Audit](audit-solutions-overview) and the [Search-UnifiedAuditLog](/en-us/powershell/module/exchange/search-unifiedauditlog) cmdlet.

## Sign-in types and mailbox actions

Sign-in types classify who's responsible for the audited actions on the mailbox. The following list describes the sign-in types that mailbox audit logging uses:

- **Owner**: The mailbox owner (the account associated with the mailbox).
- **Delegate**:
    - A user assigned the SendAs, SendOnBehalf, or FullAccess permission to another mailbox.
    - An admin assigned the FullAccess permission to a user's mailbox.
- **Admin**:
    - The mailbox is searched by using one of the following Microsoft eDiscovery tools:
        - eDiscovery in the Microsoft Purview portal.
        - In-Place eDiscovery in Exchange Online.
    - The mailbox is accessed by using the Microsoft Exchange Server MAPI Editor.
    - The mailbox is accessed by an account impersonating another user. This access happens when the *ApplicationImpersonation* role is assigned to an account, such as an application, which is now actively accessing the data. For more information, see [Configure impersonation](/en-us/exchange/client-developer/exchange-web-services/how-to-configure-impersonation).

### Mailbox actions for user mailboxes and shared mailboxes

The following table describes the mailbox actions that you can use in mailbox audit logging for user mailboxes and shared mailboxes.

- A check mark (✔) indicates the mailbox action you can log for the sign-in type (not all actions are available for all sign-in types).
- An asterisk ( ^\*^ ) after the check mark indicates the mailbox action is logged by default for the sign-in type.
- An admin with Full Access permission to a mailbox is considered a delegate.

| Mailbox action | Description | Admin | Delegate | Owner |
| --- | --- | --- | --- | --- |
| **AddFolderPermissions** | Although this value is accepted as a mailbox action, it's already included in the **UpdateFolderPermissions** action and isn't audited separately. In other words, don't use this value. |  |  |  |
| **ApplyRecord** | An item is labeled as a record. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **AttachmentAccess** | A mail message attachment was accessed through the Microsoft Graph API. This operation is enabled by default and can't be configured with the other mailbox actions. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **Copy** | A message was copied to another folder. | ✔ |  |  |
| **Create** | An item was created in the Calendar, Contacts, Draft, Notes, or Tasks folder in the mailbox (for example, a new meeting request is created). Creating, sending, or receiving a message isn't audited. Also, creating a mailbox folder isn't audited. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **FolderBind** | A mailbox folder was accessed. This action is also logged when the admin or delegate opens the mailbox. **Note**: Audit records for folder bind actions performed by delegates are consolidated. One audit record is generated for individual folder access within a 24-hour period. | ✔ | ✔ |  |
| **HardDelete** | A message purged from the Recoverable Items folder. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **MailboxLogin** | The user signed into their mailbox. |  |  | ✔ |
| **MailItemsAccessed** | Occurs when mail data is accessed by mail protocols and clients. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **MessageBind** | **Note**: This value is available only for users *without* E5/A5/G5 licenses.  A message was viewed in the preview pane or opened by an admin. | ✔ |  |  |
| **ModifyFolderPermissions** | Although this value is accepted as a mailbox action, it's already included in the **UpdateFolderPermissions** action and isn't audited separately. In other words, don't use this value. |  |  |  |
| **Move** | A message was moved to another folder. | ✔ | ✔ | ✔ |
| **MoveToDeletedItems** | A message deleted and moved to the Deleted Items folder. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **RecordDelete** | An item that's labeled as a record was soft-deleted (moved to the Recoverable Items folder). Items labeled as records can't be permanently deleted (purged from the Recoverable Items folder). | ✔ | ✔ | ✔ |
| **RemoveFolderPermissions** | Although this value is accepted as a mailbox action, it's already included in the **UpdateFolderPermissions** action and isn't audited separately. In other words, don't use this value. |  |  |  |
| **SearchQueryInitiated** | A person uses Outlook (Windows, Mac, iOS, Android, or Outlook on the web) or the Mail app for Windows 10 to search for items in a mailbox. |  |  | ✔ |
| **Send** | The user sends an email message, replies to an email message, or forwards an email message. | ✔^\*^ |  | ✔^\*^ |
| **SendAs** | A message was sent using the SendAs permission. This permission allows another user to send the message as though it came from the mailbox owner. | ✔^\*^ | ✔^\*^ |  |
| **SendOnBehalf** | A message was sent using the SendOnBehalf permission. This permission allows another user to send the message on behalf of the mailbox owner. The message indicates to the recipient who the message was sent on behalf of and who actually sent the message. | ✔^\*^ | ✔^\*^ |  |
| **SoftDelete** | A message permanently deleted or deleted from the Deleted Items folder. Soft-deleted items are moved to the Recoverable Items folder. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **Update** | A message or any of its properties changed. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **UpdateCalendarDelegation** | A calendar delegation was assigned to a mailbox. Calendar delegation gives someone else in the same organization permissions to manage the mailbox owner's calendar. | ✔^\*^ |  | ✔^\*^ |
| **UpdateFolderPermissions** | A folder permission was changed. Folder permissions control which users in your organization can access folders in a mailbox and the messages located in those folders. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **UpdateInboxRules** | An inbox rule was added, removed, or changed. Inbox rules process messages in the user's Inbox based on conditions. Actions specify what to do to messages that match the conditions of the rule. For example, move the message to a specified folder or delete the message. | ✔^\*^ | ✔^\*^ | ✔^\*^ |

Important

If you customize the mailbox actions to audit *before* mailbox auditing is turned on by default in your organization, the customized mailbox auditing settings are preserved on the mailbox and aren't overwritten by the default mailbox actions described in this section. To revert the audit mailbox actions to their default values (which you can do at any time), see Restore the default mailbox actions.

### Mailbox actions for Microsoft 365 Group mailboxes

When you turn on mailbox auditing, Microsoft 365 Group mailboxes start logging mailbox audit data. However, you can't customize the logged data or add or remove mailbox actions for any sign-in type.

The following table describes the mailbox actions that Microsoft 365 Group mailboxes log by default for each sign-in type.

An admin with Full Access permission to a Microsoft 365 Group mailbox is a delegate.

| Mailbox action | Description | Admin | Delegate | Owner |
| --- | --- | --- | --- | --- |
| **Create** | Creation of a calendar item. Creating, sending, or receiving a message isn't audited. | ✔^\*^ | ✔^\*^ |  |
| **HardDelete** | A message purged from the Recoverable Items folder. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **MoveToDeletedItems** | A message deleted and moved to the Deleted Items folder. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **SendAs** | A message sent by using the SendAs permission. | ✔^\*^ | ✔^\*^ |  |
| **SendOnBehalf** | A message sent by using the SendOnBehalf permission. | ✔^\*^ | ✔^\*^ |  |
| **SoftDelete** | A message permanently deleted or deleted from the Deleted Items folder. Soft-deleted items are moved to the Recoverable Items folder. | ✔^\*^ | ✔^\*^ | ✔^\*^ |
| **Update** | A message or any of its properties changed. | ✔^\*^ | ✔^\*^ | ✔^\*^ |

### Verify that default mailbox actions are logged for each sign-in type

The *DefaultAuditSet* property's value shows whether the default mailbox actions (managed by Microsoft) are audited on the mailbox.

To see which default audit action sets are currently applied to a user mailbox or shared mailbox, replace `<MailboxIdentity>` with the name, alias, email address, or user principal name (username) of the mailbox and run the following command in Exchange Online PowerShell:

```PowerShell
Get-Mailbox -Identity <MailboxIdentity> | Format-List DefaultAuditSet
```

To view the default audit set for a Microsoft 365 Group mailbox, replace `<MailboxIdentity>` with the name, alias, or email address of the group mailbox and run the following command in Exchange Online PowerShell:

```PowerShell
Get-Mailbox -Identity <MailboxIdentity> -GroupMailbox | Format-List DefaultAuditSet
```

The value `Admin, Delegate, Owner` means:

- The system audits the default mailbox actions for all three sign-in types. You see this value on Microsoft 365 Group mailboxes.
- An admin didn't change the audited mailbox actions for any sign-in type on a user mailbox or a shared mailbox.

If an admin changes the mailbox actions that the system audits for a sign-in type (by using the *AuditAdmin*, *AuditDelegate*, or *AuditOwner* parameters on the **Set-Mailbox** cmdlet), the property value is different.

For example, the value `Owner` for the *DefaultAuditSet* property on a user mailbox or shared mailbox means:

- The system audits the default mailbox actions for the mailbox owner.
- The audited mailbox actions for the `Delegate` and `Admin` sign-in types are changed from the default actions.

A blank value for the *DefaultAuditSet* property means the mailbox actions for all three sign-in types are changed on the user mailbox or a shared mailbox.

For more information, see Change or restore mailbox actions logged by default.

### Display the mailbox actions that are logged on mailboxes

To see the mailbox actions that are currently logged on user mailboxes or shared mailboxes, replace `<MailboxIdentity>` with the name, alias, email address, or user principal name (username) of the mailbox. Then run one or more of the following commands in Exchange Online PowerShell.

Note

Although you can add the `-GroupMailbox` switch to the following **Get-Mailbox** commands for Microsoft 365 Group mailboxes, don't trust the values that are returned. The default and static mailbox actions that are audited for Microsoft 365 Group mailboxes are described in Mailbox actions for Microsoft 365 Group mailboxes.

#### Owner actions

To view the mailbox actions currently audited for the Owner sign-in type, run the following command:

```PowerShell
Get-Mailbox -Identity <MailboxIdentity> | Select-Object -ExpandProperty AuditOwner
```

#### Delegate actions

To review the delegate actions currently being audited on the mailbox, run the following command:

```PowerShell
Get-Mailbox -Identity <MailboxIdentity> | Select-Object -ExpandProperty AuditDelegate
```

#### Admin actions

To verify the admin actions currently being audited on the mailbox, run the following command:

```PowerShell
Get-Mailbox -Identity <MailboxIdentity> | Select-Object -ExpandProperty AuditAdmin
```

## Change or restore mailbox actions logged by default

One of the key benefits of using the default mailbox actions is that you don't need to manage the mailbox actions that are audited. Microsoft manages the actions for you and automatically adds new mailbox actions to audit by default as they're released.

However, your organization might be required to audit a different set of mailbox actions for user mailboxes and shared mailboxes. The procedures in this section show you how to change the mailbox actions that are audited for each sign-in type, and how to revert back to the Microsoft-managed default actions.

Important

If you use the following procedures to customize the mailbox actions that are logged on user mailboxes or shared mailboxes, new default mailbox actions released by Microsoft aren't automatically audited on those mailboxes. You need to manually add any new mailbox actions to your customized list.

### Change the mailbox actions to audit

To change the mailbox actions that Microsoft audits for user mailboxes and shared mailboxes, use the *AuditAdmin*, *AuditDelegate*, or *AuditOwner* parameters on the **Set-Mailbox** cmdlet. You can't customize audited actions for Microsoft 365 group mailboxes.

Use two different methods to specify the mailbox actions:

- *Replace* (overwrite) the existing mailbox actions by using this syntax: `action1,action2,...actionN`.
- *Add or remove* mailbox actions without affecting other existing values by using this syntax: `@{Add="action1","action2",..."actionN"}` or `@{Remove="action1","action2",..."actionN"}`.

The following example changes the admin mailbox actions for the mailbox named "Gabriela Laureano" by overwriting the default actions with SoftDelete and HardDelete.

```PowerShell
Set-Mailbox -Identity "Gabriela Laureano" -AuditAdmin HardDelete,SoftDelete
```

The following example adds the MailboxLogin action to the audited owner actions for the mailbox laura@contoso.onmicrosoft.com.

```PowerShell
Set-Mailbox -Identity laura@contoso.onmicrosoft.com -AuditOwner @{Add="MailboxLogin"}
```

The following example removes the MoveToDeletedItems action from the audited delegate actions for the Team Discussion mailbox.

```PowerShell
Set-Mailbox -Identity "Team Discussion" -AuditDelegate @{Remove="MoveToDeletedItems"}
```

Regardless of the method you use, customizing the audited mailbox actions on user mailboxes or shared mailboxes has the following results:

- Microsoft no longer manages the audited mailbox actions for the sign-in type that you customized.
- The sign-in type that you customized is removed from the *DefaultAuditSet* property value for the mailbox, indicating that Microsoft no longer manages the default actions for that sign-in type. For details on how to verify this value, see Verify that default mailbox actions are logged for each sign-in type.

### Restore the default mailbox actions

Note

The following procedures don't apply to Microsoft 365 Group mailboxes. Those mailboxes are limited to the default actions described in Mailbox actions for Microsoft 365 Group mailboxes.

If you customize the mailbox actions that the system audits on a user mailbox or a shared mailbox, you can restore the default mailbox actions for one or all sign-in types by using this syntax:

```PowerShell
Set-Mailbox -Identity <MailboxIdentity> -DefaultAuditSet <Admin | Delegate | Owner>
```

You can specify multiple *DefaultAuditSet* values separated by commas.

This example restores the default audited mailbox actions for all sign-in types on the mailbox **mark@contoso.onmicrosoft.com**.

```PowerShell
Set-Mailbox -Identity mark@contoso.onmicrosoft.com -DefaultAuditSet Admin,Delegate,Owner
```

This example restores the default audited mailbox actions for the Admin sign-in type on the mailbox **chris@contoso.onmicrosoft.com**, but keeps the customized audited mailbox actions for the Delegate and Owner sign-in types.

```PowerShell
Set-Mailbox -Identity chris@contoso.onmicrosoft.com -DefaultAuditSet Admin
```

When you restore the default audited mailbox actions for a sign-in type, you get the following outcomes:

- The current list of mailbox actions is replaced with the default mailbox actions for the sign-in type.
- Any new mailbox actions that Microsoft releases are automatically added to the list of audited actions for the sign-in type.
- The *DefaultAuditSet* property value for the mailbox is updated to include the restored sign-in type.

## Turn off mailbox auditing on by default for your organization

To turn off mailbox auditing on by default for your entire organization, run the following command in Exchange Online PowerShell:

```PowerShell
Set-OrganizationConfig -AuditDisabled $true
```

When you turn off mailbox auditing on by default, you make the following changes:

- Mailbox auditing is turned off for your organization.
- From the time you turn off mailbox auditing on by default, no mailbox actions are audited, even if mailbox auditing is enabled on a mailbox (the *AuditEnabled* property on the mailbox is **True**).
- Mailbox auditing isn't turned on for new mailboxes and setting the *AuditEnabled* property on a new or existing mailbox to **True** is ignored.
- Any mailbox audit bypass association settings (configured by using the **Set-MailboxAuditBypassAssociation** cmdlet) are ignored.
- Existing mailbox audit records are retained until the audit log age limit for the record expires.

### Turn on mailbox auditing on by default

To turn mailbox auditing back on for your organization, run the following command in Exchange Online PowerShell:

```PowerShell
Set-OrganizationConfig -AuditDisabled $false
```

## Bypass mailbox audit logging

Currently, you can't disable mailbox auditing for specific mailboxes when mailbox auditing on by default is turned on in your organization. For example, the system ignores setting the *AuditEnabled* mailbox property to **False**.

However, you can use the **Set-MailboxAuditBypassAssociation** cmdlet in Exchange Online PowerShell to prevent *all* mailbox actions by the specified users from being logged, regardless of where the actions occur. For example:

- Mailbox owner actions that the bypassed users perform aren't logged.
- Delegate actions that the bypassed users perform on other users' mailboxes (including shared mailboxes) aren't logged.
- Admin actions that the bypassed users perform aren't logged.

To bypass mailbox audit logging for a specific user, replace `<MailboxIdentity>` with the name, email address, alias, or user principal name (username) of the user and run the following command:

```PowerShell
Set-MailboxAuditBypassAssociation -Identity <MailboxIdentity> -AuditByPassEnabled $true
```

To verify that auditing is bypassed for the specified user, run the following command:

```PowerShell
Get-MailboxAuditBypassAssociation -Identity <MailboxIdentity> | Format-List AuditByPassEnabled
```

The value **True** indicates that mailbox audit logging is bypassed for the user.

Note

The `AuditLogAgeLimit` property is no longer applicable for managing mailbox audit log retention. Audit log retention is now configured and managed through Microsoft Purview. For more information, see [Manage audit log retention policies](audit-log-retention-policies).