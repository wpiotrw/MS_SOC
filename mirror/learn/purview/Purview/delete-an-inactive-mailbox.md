---
layout: Conceptual
title: Delete an inactive mailbox | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/delete-an-inactive-mailbox
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-08-05T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-mailboxes
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
ms.assetid: f5caf497-5e8d-4b7a-bfff-d02942f38150
ms.custom:
- seo-marvel-apr2020
description: When you no longer need to preserve the contents of a Microsoft 365 inactive mailbox, you can permanently delete the inactive mailbox.
locale: en-us
document_id: 54839a5d-4512-1569-3421-f07ae06d4812
document_version_independent_id: 54839a5d-4512-1569-3421-f07ae06d4812
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/delete-an-inactive-mailbox.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: delete-an-inactive-mailbox
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/delete-an-inactive-mailbox.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: a453ee46-d713-4e83-904d-32b47fe008cc
---

# Delete an inactive mailbox | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

When you no longer need to keep the contents of an [inactive mailbox](inactive-mailboxes-in-office-365), you can permanently delete the mailbox by removing all holds on it. Then, the inactive mailbox is automatically marked for deletion and permanently deleted after it's processed.

Holds can be any of the following:

- [Microsoft 365 retention policies and labels](retention) with retain or retain and delete settings
- A hold associated with an [eDiscovery](ediscovery) case
- [Litigation hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds)
- An [In-Place Hold](/en-us/exchange/security-and-compliance/in-place-and-litigation-holds#placing-a-mailbox-on-in-place-hold)
- A [delay hold](ediscovery-identify-a-hold-on-an-exchange-online-mailbox#managing-mailboxes-on-delay-hold), which Microsoft 365 applies automatically after another hold is removed

Important

It is strongly recommended that you use Microsoft 365 retention when proactively planning to use inactive mailboxes.

- eDiscovery holds are intended for specific, time-bound cases related to a legal issue. At some point, a legal case will probably end and the holds associated with the case will be removed and the eDiscovery case will be closed (or deleted). If a hold that's placed on an inactive mailbox is associated with an eDiscovery case, and the hold is released or the eDiscovery case is closed or deleted, the inactive mailbox will be permanently deleted.
- In-Place Holds in the Exchange admin center are now retired. As of July 1, 2020, new In-Place Holds were unable to be created in Exchange Online. As of October 1, 2020, the hold duration of in-place holds could no longer be changed. Any inactive mailbox that has an In-Place Hold applied can only be deleted by removing the In-Place Hold. Existing inactive mailboxes that are on In-Place Hold will continue to be preserved until the hold is removed. For more information about In-Place Holds retirement, see [Retirement of legacy eDiscovery tools](ediscovery-legacy-retirement).
- [Litigation hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds) remains supported as an alternative method to retain content in a mailbox and make it inactive after a user account is deleted. However, as an older technology, we recommend you use Microsoft 365 retention instead.

See the More information section for a description of what happens after holds are removed from an inactive mailbox.

## Before you delete an inactive mailbox

- You must use Exchange Online PowerShell to remove holds from an inactive mailbox. You can't use the Exchange admin center (EAC), or the Microsoft Purview portal for these procedures. For step-by-step instructions to use Exchange Online PowerShell, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
- Identify the holds on an inactive mailbox by using the instructions from [Step 1: Identify the holds on an inactive mailbox](change-the-hold-duration-for-an-inactive-mailbox#step-1-identify-the-holds-on-an-inactive-mailbox). You'll need this information to know which holds to remove, and identifying information.
- Consider whether you want to copy the contents of an inactive mailbox to another mailbox before you remove the final hold that will result in the deletion of the inactive mailbox. For details, see [Restore an inactive mailbox](restore-an-inactive-mailbox).
- Be aware that if you remove the final hold from an inactive mailbox the mailbox will be permanently deleted after the 30-day soft-deleted mailbox retention period expires. After the inactive mailbox is permanently deleted, it can't be recovered. Before you remove a hold, be sure that you no longer need the contents in the mailbox. If you want to reactivate an inactive mailbox, you can recover it. For details, see [Recover an inactive mailbox](recover-an-inactive-mailbox).
- For more information about inactive mailboxes, see [Learn about inactive mailboxes](inactive-mailboxes-in-office-365).

## How to delete an inactive mailbox by removing holds

After you've [identified what type of hold is placed on the inactive mailbox](change-the-hold-duration-for-an-inactive-mailbox#step-1-identify-the-holds-on-an-inactive-mailbox) and whether there are multiple holds, you can remove the holds on the mailbox. An exception is if the inactive mailbox has one or more retention labels configured to retain items. In this case, you can't remove the hold.

When the last hold is removed, no further action is required from you because the inactive mailbox will be automatically deleted.

Use the instructions for the type of hold you need to remove:

- Remove an inactive mailbox from a retention policy
- Remove an inactive mailbox from an eDiscovery hold
- Remove Litigation hold from an inactive mailbox
- Remove an In-Place Hold from an inactive mailbox
- Remove a delay hold from an inactive mailbox

Note

A delay hold is applied automatically after you remove another hold, so it's a common reason a mailbox is still listed as inactive after you think you removed the last hold. Check for a delay hold before you conclude that hold removal didn't work.

Caution

When the instructions require you to specify an identity for the inactive mailbox, the best way to do this is by using its Distinguished Name or Exchange GUID value. Using one of these values instead of the SMTP address helps prevent accidentally specifying the wrong mailbox. However, for instructions that specifically tell you to use the primary SMTP address, you can't use the Distinguished Name or Exchange GUID value and must use the primary SMTP address.

### Remove an inactive mailbox from a retention policy

The procedure to remove an inactive mailbox from a Microsoft 365 retention policy depends on whether the policy scope is [adaptive or static](retention#adaptive-or-static-policy-scopes-for-retention).

You won't be able to remove an inactive mailbox if the retention policy has [Preservation Lock](retention-preservation-lock) applied.

#### How to remove an inactive mailbox from a retention policy with an adaptive scope

When you use the advanced query builder to define your adaptive scope for mailboxes, modify it to exclude inactive mailboxes by using the OPATH property *IsInactiveMailbox*:

```Console
IsInactiveMailbox -eq "False"
```

You can't exclude inactive mailboxes by using the simple query builder. If the retention policy is configured to use an adaptive scope that used the simple query builder, create a new adaptive policy scope that uses the advanced query builder. Then modify the retention policy to use this new adaptive scope.

#### How to remove an inactive mailbox from a retention policy with a static scope

This procedure depends on whether the retention policy applied to the inactive mailbox is configured for the entire policy location (sometimes referred to as "organization-wide") or the policy is configured to include specific mailboxes (sometimes referred to as "explicit"). For more information, see [Configuration information for static scopes](retention-settings#configuration-information-for-static-scopes).

Use the following PowerShell cmdlets to retrieve a policy GUID and identify the type of hold for a mailbox:

- If the policy is configured for the entire location: Use the **Get-OrganizationConfig** cmdlet in Exchange Online PowerShell to get information about these policies.
- If the policy is configured to include specific mailboxes: Use the **Get-Mailbox -IncludeInactiveMailbox** cmdlet and parameter in Exchange Online PowerShell to get information about these policies.

##### Static scope: How to remove an inactive mailbox from a retention policy that's configured for the entire location

Run the following PowerShell command for a specific retention policy:

```powershell
Set-Mailbox <identity of inactive mailbox> -ExcludeFromOrgHolds <retention policy GUID without prefix or suffix>
```

Alternatively, you can run the following PowerShell commands to remove the inactive mailbox:

- For retention policies that use the [older retention locations](retention-cmdlets#retention-cmdlets-for-older-locations), such as **Exchange mailboxes**, **Teams chats and Copilot interactions**, and **Teams channel messages**:

    ```powershell
    Set-Mailbox <identity of inactive mailbox> -ExcludeFromAllOrgHolds
    ```
- For retention policies that use the [newer retention locations](retention-cmdlets#retention-cmdlets-for-newer-locations), such as **Teams private channel messages** (applicable [pre-migration](retention-policies-teams#migration-of-private-channel-messages-in-2025) only), **Teams chats**, and **Microsoft Copilot experiences**:

    ```powershell
    Set-AppRetentionCompliancePolicy -Identity <retention policy GUID without prefix or suffix> -AddExchangeLocationException <identity of inactive mailbox> -DeletedResources "[{'EmailAddress':'<Primary SMTP address of inactive mailbox>'}]"
    ```

    You can also specify the identity of the inactive mailbox by using a variable and JSON, which is required if you need to specify more than one inactive mailbox with the same command. For more information, see the [PowerShell examples](/en-us/powershell/module/exchange/set-appretentioncompliancepolicy#examples).

    Important

    Before you run the command, make sure you read the Caution information for the [DeletedResources parameter](/en-us/powershell/module/exchange/set-appretentioncompliancepolicy#-deletedresources) about duplicate SMTP addresses.

##### Static scope: How to remove an inactive mailbox from a retention policy that's configured to include specific mailboxes

Run the following [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) commands:

- For retention policies that use the [older retention locations](retention-cmdlets#retention-cmdlets-for-older-locations), such as **Exchange mailboxes**, **Teams chats and Copilot interactions**, and **Teams channel messages**:

    ```powershell
    Set-RetentionCompliancePolicy -Identity <retention policy GUID without prefix or suffix> -RemoveExchangeLocation <identity of inactive mailbox>
    ```
- For retention policies that use the [newer retention locations](retention-cmdlets#retention-cmdlets-for-newer-locations), such as **Teams private channel messages**, **Teams chats**, and **Microsoft Copilot experiences**:

    ```powershell
      Set-AppRetentionCompliancePolicy -Identity <retention policy GUID without prefix or suffix> -RemoveExchangeLocation <identity of inactive mailbox>
    
    ```

### Remove an inactive mailbox from an eDiscovery hold

See [Removing content locations from an eDiscovery hold](ediscovery-create-holds#removing-content-locations-from-an-ediscovery-hold).

### Remove a Litigation hold from an inactive mailbox

Run the following PowerShell command to remove a Litigation hold from a mailbox:

```powershell
Set-Mailbox -InactiveMailbox -Identity <identity of inactive mailbox> -LitigationHoldEnabled $false
```

### Remove an In-Place Hold from an inactive mailbox

There are two ways to remove an In-Place Hold from an inactive mailbox:

- **Delete the In-Place Hold object**. If the inactive mailbox that you want to permanently delete is the only source mailbox for an In-Place Hold, you can just delete the In-Place Hold object.

    Note

    You have to disable the hold before you can delete an In-Place Hold object. If you try to delete an In-Place Hold object that has the hold enabled, you'll receive an error message.
- **Remove the inactive mailbox as a source mailbox of an In-Place Hold**. If you want to retain other source mailboxes for an In-Place Hold, you can remove the inactive mailbox from the list of source mailboxes and keep the In-Place Hold object.

#### How to remove an inactive mailbox from an eDiscovery In-Place Hold

If the eDiscovery hold is active, the user can be [removed from eDiscovery location](/en-us/purview/ediscovery-create-holds).

Use the [Invoke-HoldRemovalAction](/en-us/powershell/module/exchange/invoke-holdremovalaction)) cmdlet to find and remove an eDiscovery in-place hold

1. When running the Invoke-HoldRemovalAction with GetHolds parameter, holds that apply on specified mailbox can be found:

    ```powershell
    Invoke-HoldRemovalAction -Action GetHolds -ExchangeLocation <identity of inactive mailbox> 
    ```

If legacy eDiscovery hold is present, HoldId value will be only a GUID without any prefix or have “cld” one, see [How to identify the type of hold placed on an Exchange Online mailbox](/en-us/purview/ediscovery-identify-a-hold-on-an-exchange-online-mailbox).

1. The legacy eDiscovery holds or inactive case hold policy can be removed from the inactive mailbox by providing the HoldId:

    ```powershell
    Invoke-HoldRemovalAction -Action RemoveHold -ExchangeLocation <identity of inactive mailbox> -HoldId <hold ID>
    
    ```

### Remove a delay hold from an inactive mailbox

After you remove any other type of hold, Microsoft 365 automatically applies a *delay hold* so that content isn't purged immediately. While a delay hold is applied, the mailbox is still treated as being on hold, so it remains an inactive mailbox and isn't marked for deletion. This is a common reason a mailbox is still listed as inactive after you removed what you thought was the last hold.

A delay hold is applied by setting either of the following mailbox properties to **True**:

- *DelayHoldApplied* for Outlook content
- *DelayReleaseHoldApplied* for cloud content generated by non-Outlook apps such as Microsoft Teams

Run the following command to check whether either property is set on the inactive mailbox:

```powershell
Get-Mailbox -InactiveMailbox -Identity <identity of inactive mailbox> | FL *Delay*
```

A delay hold expires automatically after 30 days. To remove it sooner, run one or both of the following commands, depending on which property is set to **True**:

```powershell
Set-Mailbox -InactiveMailbox -Identity <identity of inactive mailbox> -RemoveDelayHoldApplied
```

```powershell
Set-Mailbox -InactiveMailbox -Identity <identity of inactive mailbox> -RemoveDelayReleaseHoldApplied
```

Note

You must be assigned the Legal Hold role in Exchange Online to use the *RemoveDelayHoldApplied* or *RemoveDelayReleaseHoldApplied* parameters.

Removing the delay hold also recalculates the hold status of the mailbox. If no other holds remain, the mailbox stops being an inactive mailbox and becomes a soft-deleted mailbox.

For more information about delay holds, including how they interact with each other, see [Managing mailboxes on delay hold](ediscovery-identify-a-hold-on-an-exchange-online-mailbox#managing-mailboxes-on-delay-hold).

## More information

- **An inactive mailbox is a type of soft-deleted mailbox.** In Exchange Online, a soft-deleted mailbox is a mailbox that's been deleted but can be recovered within a specific retention period. For soft-deleted mailboxes that aren't on hold, the mailbox is recoverable within 30 days. An inactive mailbox (a mailbox on hold before it was deleted) will remain in a soft-deleted with hold state until the hold is removed. After the last hold is removed from an inactive mailbox, the mailbox will no longer be in an inactive state. Instead it will become soft-deleted and remain in Exchange Online for 30 days from the day the hold was removed and recoverable during that time. After 30 days, a soft-deleted mailbox is marked for permanent deletion and can't be recovered.
- **What happens after you remove the last hold on an inactive mailbox?** The mailbox is treated like other soft-deleted mailboxes and is marked for permanent deletion after the 30-day soft-deleted mailbox retention period expires. This retention period starts on the date when the last hold is removed from the inactive mailbox. The *InactiveMailboxRetireTime* property is set when the mailbox transitions from being inactive (soft-deleted on hold) to no longer being inactive (soft-deleted with no holds). At that point, the *InactiveMailboxRetireTime* property is set to the current date when the transition occurred. There is an assistant that runs (called the *MailboxLifeCycle* assistant) that looks for mailboxes that have the *InactiveMailboxRetireTime* property set. If "InactiveMailboxRetireTime + 30 days" is less than the current date, then it will purge the mailbox.

    If mailboxes still show as *Inactive* after you remove the last hold and *InactiveMailboxRetireTime* isn't set, first confirm that no hold is still applied — including a delay hold, which is applied automatically after another hold is removed:

    ```powershell
    Get-Mailbox -InactiveMailbox -Identity <identity of inactive mailbox> | FL LitigationHoldEnabled,ComplianceTagHoldApplied,InPlaceHolds,*Delay*
    ```

    If a hold is still applied, remove that hold. Recalculating the hold status doesn't remove a hold, so it doesn't change a mailbox that's still on hold.

    If no holds remain, you can force the recalculation of the hold status for the inactive mailbox by using the following command:

    ```powershell
    Set-Mailbox -Identity <identity of inactive mailbox> -RecalculateInactiveMailbox
    ```
- **Is an inactive mailbox permanently deleted immediately after all holds are removed?** A formerly inactive mailbox will be available in the soft-deleted state for 30 days. After 30 days, the mailbox will be marked for permanent deletion.
- **How do you display information about an inactive mailbox after all holds are removed?** After all holds are removed and the inactive mailbox is reverted back to a soft-deleted mailbox, it won't be returned by using the *InactiveMailboxOnly* parameter with the **Get-Mailbox** cmdlet. But you can display information about the mailbox by using the **Get-Mailbox -SoftDeletedMailbox** command. For example:

    ```powershell
    Get-Mailbox -SoftDeletedMailbox -Identity pilarp | FL Name,Identity,LitigationHoldEnabled,In
    Placeholds,WhenSoftDeleted,IsInactiveMailbox,WasInactiveMailbox,InactiveMailboxRetireTime
    
    Name                   : pilarp
    Identity               : Soft Deleted Objects\pilarp
    LitigationHoldEnabled  : False
    InPlaceHolds           : {}
    WhenSoftDeleted        : 6/16/2022 1:19:04 AM
    IsInactiveMailbox      : False
    WasInactiveMailbox     : True
    InactiveMailboxRetireTime : 9/30/2022 11:16:23 PM
    ```

    In the above example, the *WhenSoftDeleted* property identifies the soft-deleted date, which in this example is June 16, 2022. The *WasInactiveMailbox* property is listed as `True` because it was previously an inactive mailbox. The mailbox will be permanently deleted 30 days after September 30, 2022.