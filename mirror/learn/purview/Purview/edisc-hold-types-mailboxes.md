---
layout: Conceptual
title: Identify Exchange mailbox hold types in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-hold-types-mailboxes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to identify the different types of holds placed on an Exchange Online mailbox in eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-23T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom:
- msecd-doc-authoring-1014
- msecd-doc-authoring-1015
locale: en-us
document_id: f410538b-f0ca-a1fc-ff55-7a0c89a07ced
document_version_independent_id: f410538b-f0ca-a1fc-ff55-7a0c89a07ced
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-hold-types-mailboxes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-hold-types-mailboxes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-hold-types-mailboxes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 1817d8d4-76c0-e5ef-4e48-3ea5d8082af1
---

# Identify Exchange mailbox hold types in eDiscovery | Microsoft Learn

Microsoft Purview offers several ways that your organization can prevent mailbox content from being permanently deleted. This protection allows your organization to retain content to meet compliance regulations or during legal and other types of investigations. This article explains how to identify the different types of holds placed on an Exchange Online mailbox and how to use PowerShell cmdlets to get the GUID for each hold.

Tip

To determine *whether* a mailbox or site is on hold (for example, because a content purge or site deletion isn't working), start with the diagnostic checklist in [Check for holds on a mailbox or site](edisc-hold-manage#check-for-holds-on-a-mailbox-or-site). This article explains the hold types themselves in more depth.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Overview of Exchange mailbox hold types

Here's a list of the retention features (also called *holds*) in Microsoft Purview and Microsoft 365:

- **[Litigation Hold](/en-us/microsoft-365/admin/misc/create-litigation-hold-mac?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json)**: Holds that you apply to user mailboxes in Exchange Online.
- **[eDiscovery hold](edisc-hold-create)**: Holds that you associate with an eDiscovery case in the Microsoft Purview portal. You can place a hold on the Exchange mailboxes and OneDrive accounts of people you're investigating in the case. You can also place a hold on the mailboxes and sites that are associated with Microsoft Teams, Microsoft 365 groups, and Viva Engage Groups.
- **[Microsoft Purview retention policies](retention)**: Can be configured to retain (or retain and then delete) content in user mailboxes in Exchange Online and in the corresponding mailbox for Microsoft 365 Groups and Microsoft Teams. You can also create a retention policy to retain Skype for Business Conversations, which are stored in user mailboxes.

    There are two types of Microsoft Purview retention policies that you can assign to mailboxes.

    - **Specific location retention policies**: These policies are assigned to the content locations of specific users. Use the **Get-Mailbox** cmdlet in Exchange Online PowerShell to get information about retention policies assigned to specific mailboxes. For more information about this type of retention policy, see the section [A policy with specific inclusions or exclusions](retention-settings#a-policy-with-specific-inclusions-or-exclusions) from the retention policy documentation.
    - **Organization-wide retention policies**: These policies are assigned to all content locations in your organization. Use the **Get-OrganizationConfig** cmdlet in Exchange Online PowerShell to get information about organization-wide retention policies. For more information about this type of retention policy, see the section [A policy that applies to entire locations](retention-settings#a-policy-that-applies-to-entire-locations) from the retention policy documentation.
- **[Microsoft Purview retention labels](retention)**: If a user applies a Microsoft Purview retention label (one that's configured to retain content or retain and then delete content) to *any* folder or item in their mailbox, a hold is placed on the mailbox as if you placed the mailbox on Litigation Hold or assigned it to a Microsoft Purview retention policy. For more information, see the Identifying mailboxes on hold because a retention label was applied to a folder or item section in this article.

To manage mailboxes on hold, you might need to identify the type of hold that's placed on a mailbox so that you can perform tasks such as changing the hold duration, temporarily or permanently removing the hold, or excluding a mailbox from a Microsoft Purview retention policy. In these cases, the first step is to identify the type of hold placed on the mailbox. Because multiple holds (and different types of holds) can be placed on a single mailbox, you need to identify all holds placed on a mailbox if you want to remove or change a hold.

## Step 1: Get the GUID for holds placed on a mailbox

To connect to Exchange Online PowerShell, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell). You must connect before you run the cmdlets in this step.

Run the following two cmdlets in Exchange Online PowerShell to get the GUID of the holds that are placed on a mailbox. After you get a GUID, use it to identify the specific hold in Step 2. A Litigation Hold doesn't use a GUID. Litigation Holds are either enabled or disabled for a mailbox.

- **Get-Mailbox**: Use this cmdlet to check if Litigation Hold is enabled for a mailbox and to get the GUIDs for eDiscovery holds and Microsoft Purview retention policies that are assigned to a mailbox. The output of this cmdlet also shows if a mailbox is explicitly excluded from an organization-wide retention policy.
- **Get-OrganizationConfig**: Use this cmdlet to get the GUIDs for organization-wide retention policies.

### Use Get-Mailbox to view holds on a mailbox

Run the following command to get information about the holds and Microsoft Purview retention policies applied to a mailbox.

```powershell
Get-Mailbox <username> | FL LitigationHoldEnabled,InPlaceHolds
```

Tip

If there are too many values in the InPlaceHolds property and not all of them show up, run the `Get-Mailbox <username> | Select-Object -ExpandProperty InPlaceHolds` command to display each GUID on a separate line.

The following table describes how to identify different types of holds based on the values in the *InPlaceHolds* property when you run the **Get-Mailbox** cmdlet.

| Hold type | Example value | How to identify the hold |
| --- | --- | --- |
| Litigation Hold | `True` | Litigation Hold is enabled for a mailbox when the *LitigationHoldEnabled* property is set to `True`. |
| eDiscovery hold | `UniH7d895d48-7e23-4a8d-8346-533c3beac15d` | The *InPlaceHolds property* contains the GUID of any hold associated with an eDiscovery case in the Microsoft Purview portal. You can tell this is an eDiscovery hold because the GUID starts with the `UniH` prefix (which denotes a Unified Hold). |
| Microsoft Purview retention policy applied to the mailbox | `mbxcdbbb86ce60342489bff371876e7f224:1` or `skp127d7cf1076947929bf136b7a2a8c36f:3` | The *InPlaceHolds* property contains GUIDs of any specific location retention policy that's applied to the mailbox. You can identify retention policies because the GUID starts with the `mbx` or the `skp` prefix. The `skp` prefix indicates that the retention policy is applied to Skype for Business conversations in the user's mailbox. |
| Excluded from an organization-wide Microsoft Purview retention policy | `-mbxe9b52bf7ab3b46a286308ecb29624696` | If a mailbox is excluded from an organization-wide Microsoft Purview retention policy, the GUID for the retention policy that the mailbox is excluded from shows up in the *InPlaceHolds* property and uses the `-mbx` prefix. |

### Use Get-OrganizationConfig to identify organization-wide holds

If the *InPlaceHolds* property is empty when you run the **Get-Mailbox** cmdlet, one or more organization-wide Microsoft Purview retention policies might still apply to the mailbox. Run the following command in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) to get a list of GUIDs for organization-wide Microsoft Purview retention policies.

```powershell
Get-OrganizationConfig | FL InPlaceHolds
```

Tip

If the `InPlaceHolds` property contains too many values and not all of them display, run the `Get-OrganizationConfig | Select-Object -ExpandProperty InPlaceHolds` command to display each GUID on a separate line.

The following table describes the different types of organization-wide holds and how to identify each type based on the GUIDs contained in the *InPlaceHolds* property when you run the **Get-OrganizationConfig** cmdlet.

| Hold type | Example value | Description |
| --- | --- | --- |
| Microsoft Purview retention policies applied to Exchange mailboxes, Exchange public folders, and Teams chats | `mbx7cfb30345d454ac0a989ab3041051209:2` | Organization-wide retention policies applied to Exchange mailboxes, Exchange public folders, and 1xN chats in Microsoft Teams are identified by GUIDs that start with the `mbx` prefix. Note 1xN chats are stored in the mailbox of the individual chat participants. |
| Microsoft Purview retention policy applied to Microsoft 365 Groups and Teams channel messages | `grp1a0a132ee8944501a4bb6a452ec31171:3` | Organization-wide retention policies applied to Microsoft 365 groups and channel messages in Microsoft Teams are identified by GUIDs that start with the `grp` prefix. Note channel messages are stored in the group mailbox that is associated with a Microsoft Team. |

For more information about retention policies applied to Microsoft Teams, see [Learn about retention policies for Microsoft Teams](retention-policies-teams).

### Understand the format of the InPlaceHolds value for retention policies

In addition to the prefix (`mbx`, `skp`, or `grp`) that identifies an item in the `InPlaceHolds` property as a Microsoft Purview retention policy, the value also contains a suffix that identifies the type of retention action that's configured for the policy. For example, the action suffix is highlighted in bold type in the following examples:

`skp127d7cf1076947929bf136b7a2a8c36f`**:1**

`mbx7cfb30345d454ac0a989ab3041051209`**:2**

`grp1a0a132ee8944501a4bb6a452ec31171`**:3**

The following table defines the three possible retention actions:

| Value | Description |
| --- | --- |
| **1** | The retention policy is configured to delete items or the retention policy is used to publish retention labels. If the policy is publishing retention labels, check the retention configuration for each published label. |
| **2** | The retention policy is configured to hold items. The policy doesn't delete items after the retention period expires. |
| **3** | The retention policy is configured to hold items and then delete them after the retention period expires. |

Note

Because retention label policies publish or autoapply labels that apply item-level actions, they always show an action value of 1 within the `InPlaceHolds` property of the mailbox.

To identify whether a hold is applied to a folder or item within the mailbox, see Identifying mailboxes on hold because a retention label has been applied to a folder or item.

For more information about retention actions, see the [Retaining content for a specific period of time](retention-settings#retaining-content-for-a-specific-period-of-time) section.

## Step 2: Use the GUID to identify the hold

After you get the GUID for a hold that's applied to a mailbox, use that GUID to identify the hold. The following sections show how to identify the name of the hold and other information by using the hold GUID.

### eDiscovery holds

Run the following commands in [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell) to find an eDiscovery hold that's applied to the mailbox. Use the GUID (without the UniH prefix) for the eDiscovery hold that you found in Step 1.

To connect to Security & Compliance PowerShell, see [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

The first command creates a variable that holds information about the eDiscovery hold. Use this variable in the other commands. The second command shows the name of the eDiscovery case that the hold is associated with. The third command shows the name of the hold and lists the mailboxes that the hold applies to.

```powershell
$CaseHold = Get-CaseHoldPolicy <hold GUID without prefix>
```

```powershell
Get-ComplianceCase $CaseHold.CaseId | FL Name
```

```powershell
$CaseHold | FL Name,ExchangeLocation
```

### Identify Microsoft Purview retention policies by GUID

[Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) and run the following command to find the Microsoft Purview retention policy (organization-wide or specific location) that's applied to the mailbox. Use the GUID (without the mbx, skp, or grp prefix or the action suffix) that you found in Step 1.

```powershell
Get-RetentionCompliancePolicy <hold GUID without prefix or suffix> -DistributionDetail  | FL Name,*Location
```

New retention policies that apply to the following locations don't stamp directly on organization configuration or Exchange Online objects:

- Enterprise AI apps
- Microsoft Copilot experiences
- Teams chats
- Teams private channel messages
- Viva Engage community messages
- Viva Engage user messages
- Other AI apps

To determine whether these retention compliance policies apply to a mailbox during an investigation, use Policy Lookup or [Retention cmdlets for newer locations](retention-cmdlets#retention-cmdlets-for-newer-locations).

```powershell
Get-AppRetentionCompliancePolicy <hold GUID without prefix or suffix> -DistributionDetail  | FL Name, Applications, *Location
```

## Identify mailboxes on hold because a retention label is applied to a folder or item

When a user applies a retention label that's configured to *retain* or *retain and then delete* content to any folder or item in their mailbox, the *ComplianceTagHoldApplied* mailbox property is set to **True**. When this property is **True**, treat the mailbox as if it's on hold, such as when you assign it to a Microsoft Purview retention policy or place it on Litigation Hold, but with some caveats. When the *ComplianceTagHoldApplied* property is **True**, the following things occur:

- If you delete the mailbox or the user's Microsoft 365 account, the mailbox becomes an [inactive mailbox](inactive-mailboxes-in-office-365).
- You can't disable the mailbox (either the primary mailbox or the archive mailbox, if it's enabled).
- Items that you delete from the mailbox follow one of two paths depending on whether they're labeled or not:
    - **Unlabeled items** follow the same path deleted items take when no holds apply to the mailbox. The time that it takes for these items to be permanently deleted is determined by the [deleted item retention](/en-us/exchange/security-and-compliance/recoverable-items-folder/recoverable-items-folder?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json#deleted-item-retention) configuration and whether [single item recovery](/en-us/exchange/security-and-compliance/recoverable-items-folder/recoverable-items-folder?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json#single-item-recovery) is enabled for the mailbox or not.
    - **Labeled items** are retained within the [recoverable items folder](/en-us/exchange/security-and-compliance/recoverable-items-folder/recoverable-items-folder?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json#recoverable-items-folder) in the same way they would be if a Microsoft Purview retention policy applied, but at the individual item level. If multiple items have different labels that are configured to *retain* or *retain and then delete* content at different intervals, each item is retained based on the configuration of the applied label.
- Other holds, such as Microsoft Purview retention policies, eDiscovery holds, or litigation hold can extend how long labeled items are retained based on the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence).

To view the value of the *ComplianceTagHoldApplied* property for a single mailbox, run the following command in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell):

```powershell
Get-Mailbox <username> | FL ComplianceTagHoldApplied
```

For more information about retention labels, see [retention labels](retention#retention-labels).

A *True* value for **ComplianceTagHoldApplied** doesn't mean the mailbox currently has items with a retention label. When you apply a retention label to a mailbox, **ComplianceTagHoldApplied** changes to *True*. After it changes to *True*, it doesn't automatically change back to *False*, even when the mailbox no longer has labeled items.

To change the *ComplianceTagHoldApplied* value to *False*, run the following command in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell):

```powershell
Set-Mailbox -Identity <username> -RemoveComplianceTagHoldApplied -ProvideConsent
```

For more information, see [Set-Mailbox](/en-us/powershell/module/exchangepowershell/set-mailbox). For the full procedure to delete items from the Recoverable Items folder, see [Delete items in the Recoverable Items folder](edisc-hold-delete-recoverable-items).

## Manage mailboxes on delay hold

When you remove any type of hold from a mailbox, Exchange Online applies a *delay hold*. This hold delays the actual removal of the hold for 30 days to prevent data from being permanently deleted (purged) from the mailbox. This delay gives admins an opportunity to search for or recover mailbox items that are purged after a hold is removed. The Managed Folder Assistant places a delay hold on a mailbox the next time it processes the mailbox and detects that a hold was removed. Specifically, the Managed Folder Assistant applies a delay hold to a mailbox when it sets one of the following mailbox properties to **True**:

- **DelayHoldApplied**: This property applies to email-related content (generated by people using Outlook and Outlook on the web) that's stored in a user's mailbox.
- **DelayReleaseHoldApplied**: This property applies to cloud-based content (generated by non-Outlook apps such as Microsoft Teams, Microsoft Forms, and Microsoft Viva Engage) that's stored in a user's mailbox. Cloud data generated by a Microsoft app is typically stored in a hidden folder in a user's mailbox.

When the Managed Folder Assistant places a delay hold on the mailbox (by setting either of the previous properties to **True**), the mailbox is still considered to be on hold for an unlimited hold duration, as if the mailbox was on Litigation Hold. After 30 days, the delay hold expires, and Microsoft 365 automatically attempts to remove the delay hold (by setting the *DelayHoldApplied* or *DelayReleaseHoldApplied* property to **False**) so that the hold is removed. After either of these properties are set to **False**, the corresponding items that are marked for removal are purged the next time the Managed Folder Assistant processes the mailbox.

Note

If the user account for the mailbox is disabled, the Managed Folder Assistant doesn't process the mailbox and the delay hold remains after the 30 days expire. For more information, see Delay hold considerations.

To view the values for the DelayHoldApplied and DelayReleaseHoldApplied properties for a mailbox, run the following command in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).

```powershell
Get-Mailbox <username> | FL *HoldApplied*
```

To remove the delay hold before it expires, run one (or both) of the following commands in Exchange Online PowerShell, depending on which property you want to change:

```powershell
Set-Mailbox <username> -RemoveDelayHoldApplied
```

Or

```powershell
Set-Mailbox <username> -RemoveDelayReleaseHoldApplied
```

You must be assigned the Legal Hold role in Exchange Online to use the *RemoveDelayHoldApplied* or *RemoveDelayReleaseHoldApplied* parameters.

To remove the delay hold on an inactive mailbox, run one of the following commands in Exchange Online PowerShell:

```powershell
Set-Mailbox <DN or Exchange GUID> -InactiveMailbox -RemoveDelayHoldApplied
```

Or

```powershell
Set-Mailbox <DN or Exchange GUID> -InactiveMailbox -RemoveDelayReleaseHoldApplied
```

Tip

The best way to specify an inactive mailbox in the previous command is to use its Distinguished Name or Exchange GUID value. Using one of these values helps prevent accidentally specifying the wrong mailbox.

For more information about using these parameters for managing delay holds, see [Set-Mailbox](/en-us/powershell/module/exchange/set-mailbox).

### Delay hold considerations

Keep the following points in mind when managing a mailbox on delay hold:

- If you set either the *DelayHoldApplied* or *DelayReleaseHoldApplied* property to **True** and you delete a mailbox (or the corresponding user account), the mailbox becomes an inactive mailbox. A mailbox is considered to be on hold if either property is set to **True**. Deleting a mailbox on hold results in an inactive mailbox. To delete a mailbox and not make it an inactive mailbox, set both properties to **False**.
- A mailbox is on hold for an unlimited hold duration if either the *DelayHoldApplied* or *DelayReleaseHoldApplied* property is set to **True**. However, that condition doesn't mean that *all* content in the mailbox is preserved. The value of each property determines what content is preserved. For example, let's say both properties are set to **True** because you remove holds from the mailbox. Then, you remove only the delay hold that applies to non-Outlook cloud data by using the *RemoveDelayReleaseHoldApplied* parameter. The next time the Managed Folder Assistant processes the mailbox, it purges the non-Outlook items marked for removal. It doesn't purge any Outlook items marked for removal because the *DelayHoldApplied* property is still set to **True**. The opposite condition is also true: if *DelayHoldApplied* is set to **False** and *DelayReleaseHoldApplied* is set to **True**, then only Outlook items marked for removal are purged.

## How to confirm that an organization-wide retention policy is applied to a mailbox

When you apply or remove an organization-wide retention policy to a mailbox, exporting the mailbox diagnostics logs helps you confirm that Exchange Online applied or removed the retention policy to the mailbox. To view this information, you first need to validate a few things by using [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).

### Obtain the GUIDs for any retention policies explicitly applied to a mailbox

Run the following command to list the retention policy GUIDs that are explicitly applied to the mailbox.

```powershell
Get-Mailbox <username> | Select-Object -ExpandProperty InPlaceHolds
```

### Obtain the GUIDs for any organization-wide retention policies applied to mailboxes

Run the following command to list the GUIDs for organization-wide retention policies.

```powershell
Get-OrganizationConfig | Select-Object -ExpandProperty InPlaceHolds
```

### Get the Mailbox Diagnostics for HoldTracking

The Hold Tracking Mailbox Diagnostics logs maintain a history of the holds applied to a user mailbox. If the object is inactive, include `-IncludeInactiveMailboxes` parameter.

```powershell
$ht = Export-MailboxDiagnosticLogs <username> -ComponentName HoldTracking
$ht.MailboxLog | Convertfrom-Json
```

### Get the Mailbox Diagnostics for Substrate HoldTracking

The Substrate Hold Tracking Mailbox Diagnostics logs maintain a history of the holds applied to a user mailbox. If the object is inactive, include `-IncludeInactiveMailboxes` parameter.

```powershell
$sht = Export-MailboxDiagnosticLogs <username> -ComponentName SubstrateHoldTracking
$sht.MailboxLog | Convertfrom-Json
```

### Review the results of the Mailbox Diagnostics logs

After you run `Export-MailboxDiagnosticLogs` for HoldTracking or SubstrateHoldTracking, the resulting data might look something like this example:

> 
> **ed**`  : 0001-01-01T00:00:00.0000000`**hid**` : mbx7cfb30345d454ac0a989ab3041051209:1`**ht**`  : 4`**lsd**` : 2020-03-23T18:24:37.1884606Z`**osd**` : 2020-03-23T18:24:37.1884606Z`

Use the following table to help you understand each of the values listed in the diagnostics log.

| Value | Description |
| --- | --- |
| **ed** | Indicates the end date, which is the date the retention policy was disabled. MinValue means the policy is still assigned to the mailbox. |
| **hid** | Indicates the GUID for the retention policy. This value correlates to the GUIDs that you collected for the explicit or organization-wide retention policies assigned to the mailbox. |
| **ht** | Indicates the hold type. Values are *0* for LitigationHold, *1* for InPlaceHold, *2* for ComplianceTagHold, *3* for DelayReleaseHold, *4* for OrganizationRetention, *5* for CompliancePolicy, *6* for SubstrateAppPolicy, and *7* for SharepointPolicy. |
| **lsd** | Indicates the last start date, which is the date the retention policy was assigned to the mailbox. |
| **osd** | Indicates the original start date, which is the date that Exchange first recorded information about the retention policy. |

When you remove a retention policy from a mailbox, Exchange places a temporary delay hold on the user to prevent purging content. You can disable a delay hold by running the `Set-Mailbox -RemoveDelayHoldApplied` command.