---
layout: Conceptual
title: Delete items in the Recoverable Items folder for mailboxes on hold in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-hold-delete-recoverable-items
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how admins can delete items in a user's Recoverable Items folder for an Exchange Online mailbox, even if that mailbox is placed on hold.
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
document_id: fa9aed4a-d0d9-0203-519a-62dc3716599b
document_version_independent_id: fa9aed4a-d0d9-0203-519a-62dc3716599b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-hold-delete-recoverable-items.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-hold-delete-recoverable-items
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-hold-delete-recoverable-items.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e744a444-a59f-de91-26a7-0f0198abfd9c
---

# Delete items in the Recoverable Items folder for mailboxes on hold in eDiscovery | Microsoft Learn

The **Recoverable Items** folder for an Exchange Online mailbox protects against accidental or malicious deletions. Exchange Online also uses this folder to store items that compliance features retain and access, such as holds and eDiscovery searches. However, in some situations, organizations might need to delete data unintentionally retained in the Recoverable Items folder.

For example, a user might unknowingly send or forward an email message that contains sensitive information or information that might have serious business consequences. Even if the user permanently deletes the message, it might be retained indefinitely because a legal hold was placed on the mailbox. This scenario is known as *data spillage* because data was unintentionally *spilled* into Microsoft 365. In these situations, you can delete items in a user's Recoverable Items folder for an Exchange Online mailbox, even if you placed the mailbox on hold by using one of the different hold features in Microsoft 365. These types of holds include [Litigation Holds](/en-us/microsoft-365/admin/misc/create-litigation-hold-mac?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json), [eDiscovery holds](edisc-hold-create), and [retention policies](retention) created in Microsoft Purview.

The following procedure explains how to delete items from the Recoverable Items folder for cloud-based Exchange Online mailboxes that are on hold. This procedure involves disabling access to the mailbox and disabling single item recovery, disabling the Managed Folder Assistant from processing the mailbox, temporarily removing the hold, deleting items from the Recoverable Items folder, and then reverting the mailbox to its previous configuration.

Here's a summary of the process:

- Step 1: Collect information about the mailbox
- Step 2: Prepare the mailbox
- Step 3: Remove all holds from the mailbox
- Step 4: Remove the delay hold from the mailbox
- Step 5: Delete items in the Recoverable Items folder
- Step 6: Revert the mailbox to its previous state

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Before you delete items

Important

Before you start, confirm that no hold source still applies to the mailbox. If any hold (eDiscovery hold, Litigation Hold, Microsoft Purview retention policy, retention label hold, or delay hold) is in effect, the HardDelete purge in Step 5 silently leaves items in the Recoverable Items folder by design. For the full diagnostic checklist and the `InPlaceHolds` prefix decoder, see [Check for holds on a mailbox or site](edisc-hold-manage#check-for-holds-on-a-mailbox-or-site).

Caution

Following the procedures outlined in this article results in data being permanently deleted (purged) from an Exchange Online mailbox. That means messages that you delete from the Recoverable Items folder can't be recovered and won't be available for legal discovery or other compliance purposes. If you want to delete messages from a mailbox that's placed on hold as part of a Litigation Hold, eDiscovery hold, or retention policy created in the Microsoft Purview portal, check with your records management or legal departments before removing the hold. Your organization might have a policy that defines whether a mailbox on hold or a data spillage activity takes priority.

- To create and run a search, you need to be a member of the eDiscovery Manager role group or be assigned the *Compliance Search* management role. To delete messages, you need to be a member of the *Organization Management* role group or be assigned the Search And Purge management role. For information about adding users to a role group, see [Assign eDiscovery permissions](edisc-permissions).
- If you assign a mailbox to an organization-wide retention policy, you need to exclude the mailbox from the policy before you can delete items from the Recoverable Items folder. It might take up to 24 hours to synchronize the policy change and remove the mailbox from the policy. For more information, see "Remove organization-wide retention policies" in the Remove all holds from the mailbox section in this article.
- You can't perform this procedure for a mailbox that has retention settings assigned with a retention policy locked by using Preservation Lock. This lock prevents you from removing or excluding the mailbox from the policy and from disabling the Managed Folder Assistant on the mailbox. For more information about locking policies for retention, see [Use Preservation Lock to restrict changes to retention policies and retention label policies](retention-preservation-lock).
- The procedure described in this article isn't supported for inactive mailboxes. That's because you can't reapply a hold (or retention policy) to an inactive mailbox after you remove it. When you remove a hold from an inactive mailbox, the mailbox changes to a normal soft-deleted mailbox and is permanently deleted from your organization after it's processed by the Managed Folder Assistant.
- If a mailbox isn't on hold (or doesn't have single item recovery enabled), you can delete the items from the Recoverable Items folder.

## Step 1: Collect information about the mailbox

In this step, collect selected properties from the target mailbox that affect this procedure. Write down these settings or save them to a text file because you change some of these properties and then revert back to the original values in Step 6, after you delete items from the Recoverable Items folder. Here's a list of the mailbox properties you need to collect.

- *SingleItemRecoveryEnabled* and *RetainDeletedItemsFor*. If necessary, you disable single recovery and increase the deleted items retention period in Step 3.
- *LitigationHoldEnabled* and *InPlaceHolds*. You need to identify all the holds placed on the mailbox so that you can temporarily remove them in Step 3. For tips about how to identify the type of hold that might be placed on a mailbox, see Identify hold types by InPlaceHolds property values.

Additionally, you need to get the mailbox client access settings so you can temporarily disable them so the owner (or other users) can't access the mailbox during this procedure. Finally, you get the current size and number of items in the Recoverable Items folder. After you delete items in the Recoverable Items folder in Step 5, you use this information to verify that items were removed.

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell). Be sure to use a user name and password for an administrator account that's been assigned the appropriate management roles in Exchange Online.
2. Run the following command to get information about single item recovery and the deleted item retention period.

    ```powershell
    Get-Mailbox <username> | FL SingleItemRecoveryEnabled,RetainDeletedItemsFor
    ```

    If single item recovery is enabled, you have to disable it in Step 2. If the deleted item retention period isn't set for 30 days (the maximum value in Exchange Online), then you can increase it in Step 2.
3. Run the following command to get the mailbox access settings for the mailbox.

    ```powershell
    Get-CASMailbox <username> | FL EwsEnabled,ActiveSyncEnabled,MAPIEnabled,OWAEnabled,ImapEnabled,PopEnabled
    ```

    You disable all of these access methods in Step 2.
4. Run the following command to get information about the holds and retention policies applied to the mailbox.

    ```powershell
    Get-Mailbox <username> | FL LitigationHoldEnabled,InPlaceHolds
    ```

    Tip

    If there are too many values in the *InPlaceHolds* property and not all of them are displayed, run the `Get-Mailbox <username> | Select-Object -ExpandProperty InPlaceHolds` command to display each value on a separate line.
5. Run the following command to get information about any organization-wide retention policies.

    ```powershell
    Get-OrganizationConfig | FL InPlaceHolds
    ```

    If your organization has any organization-wide retention policies, you have to exclude the mailbox from these policies in Step 3. It might take up to 24 hours to replicate the change.

    Tip

    If there are too many values in the *InPlaceHolds* property and not all of them are displayed, run the `Get-OrganizationConfig | Select-Object -ExpandProperty InPlaceHolds` command to display each value on a separate line.
6. Run the following command to determine if a delay hold is applied to the mailbox.

    ```powershell
    Get-Mailbox <username> | FL DelayHoldApplied,DelayReleaseHoldApplied
    ```

    If the value of the *DelayHoldApplied* or *DelayReleaseHoldApplied* property is set to **True**, a delay hold is applied to the mailbox and must be removed. For more information about delay holds, see Step 4: Remove the delay hold from the mailbox.

    If the value of either the *DelayHoldApplied* or *DelayReleaseHoldApplied* property is set to **False**, a delay hold isn't applied to the mailbox, and you can skip Step 4.
7. Run the following command to get the current size and total number of items in folders and subfolders in the Recoverable Items folder in the user's primary mailbox.

    ```powershell
    Get-MailboxFolderStatistics <username> -FolderScope RecoverableItems | FL Name,FolderAndSubfolderSize,ItemsInFolderAndSubfolders
    ```

    If the user's archive mailbox is enabled, run the following command to get the size and total number of items in folders and subfolders in the Recoverable Items folder in their archive mailbox.

    ```powershell
    Get-MailboxFolderStatistics <username> -FolderScope RecoverableItems -Archive | FL Name,FolderAndSubfolderSize,ItemsInFolderAndSubfolders
    ```

    When you delete items in Step 5, you can choose to delete or not delete items in the Recoverable Items folder in the user's primary archive mailbox. If auto-expanding archiving is enabled for the mailbox, items in an auxiliary archive mailbox won't be deleted.

## Step 2: Prepare the mailbox

Note

The actions in this step (disabling the Managed Folder Assistant and Single Item Recovery) are preparation. They aren't the delete mechanism. The Managed Folder Assistant (also called messaging records management, or MRM) enforces retention; it doesn't delete items from the Recoverable Items folder. The actual delete happens in Step 5 with the `New-ComplianceSearchAction -Purge -PurgeType HardDelete` command.

After you collect and save information about the mailbox, prepare the mailbox by performing the following tasks:

- **Disable client access to mailbox** so that the mailbox owner can't access their mailbox or make any changes to the mailbox data during this procedure.
- **Increase the deleted item retention period** to 30 days (the maximum value in Exchange Online) so that items aren't purged from the Recoverable Items folder before you can delete them in Step 5.
- **Disable single Item recovery** so that items aren't retained (during the deleted item retention period) after you delete them from the Recoverable Items folder in Step 5.
- **Disable the Managed Folder Assistant** so that it doesn't process the mailbox and retain the items that you delete in Step 5.

Perform the following steps in Exchange Online PowerShell.

1. Run the following command to disable all client access to the mailbox. The command syntax assumes that all client access methods are enabled on the mailbox.

    ```powershell
    Set-CASMailbox <username> -EwsEnabled $false -ActiveSyncEnabled $false -MAPIEnabled $false -OWAEnabled $false -ImapEnabled $false -PopEnabled $false
    ```

    Note

    It might take up to 60 minutes to disable all client access methods to the mailbox. Disabling these access methods doesn't disconnect the mailbox owner if they're currently signed in. If the owner isn't signed in, they can't access their mailbox after these access methods are disabled.
2. Run the following command to increase the deleted item retention period to the maximum of 30 days. This step assumes that the current setting is less than 30 days.

    ```powershell
    Set-Mailbox <username> -RetainDeletedItemsFor 30
    ```
3. Run the following command to disable single item recovery.

    ```powershell
    Set-Mailbox <username> -SingleItemRecoveryEnabled $false
    ```

    Note

    It might take up to 240 minutes to disable single item recovery. Don't delete items in the Recoverable Items folder until this period has elapsed.
4. Run the following command to prevent the Managed Folder Assistant from processing the mailbox. You can disable the Managed Folder Assistant only if a retention policy with a Preservation Lock isn't applied to the mailbox.

    ```powershell
    Set-Mailbox <username> -ElcProcessingDisabled $true
    ```

    Note

    Setting the *ElcProcessingDisabled* parameter to *True* doesn't prevent all messages within the Recoverable Items folder from processing. If holds are removed from mailboxes, the substrate hold folder is deleted over time.

## Step 3: Remove all holds from the mailbox

Before you can delete items from the Recoverable Items folder, remove all holds (identified in Step 1) that you placed on the mailbox. Remove all holds so that the system doesn't retain items after you delete them from the Recoverable Items folder. The following sections explain how to remove different types of holds on a mailbox. For tips about how to identify the type of hold that might be placed on a mailbox, see Identify hold types by InPlaceHolds property values. For more information, see [How to identify the type of hold placed on an Exchange Online mailbox](edisc-hold-types-mailboxes).

Caution

Check with your records management or legal departments before removing a hold from a mailbox.

### Remove Litigation Hold from the mailbox

Run the following command in Exchange Online PowerShell to remove a Litigation Hold from the mailbox.

```powershell
Set-Mailbox <username> -LitigationHoldEnabled $false
```

Note

Similar to disabling single item recovery, it might take up to 240 minutes to remove the Litigation Hold. Don't delete items from the Recoverable Items folder until this period has elapsed.

### Remove retention policies applied to specific mailboxes

Run the following command in [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) to identify the retention policy that is applied to the mailbox. This command also returns any Teams conversation retention policies applied to a mailbox. Use the GUID (not including the `mbx` or `skp` prefix) for the retention policy that you identified in Step 1.

```powershell
Get-RetentionCompliancePolicy <retention policy GUID without prefix> | FL Name
```

After you identify the retention policy, go to **Data lifecycle management** &gt; **Retention policies** in the Microsoft Purview portal, edit the retention policy that you identified in the previous step, and remove the mailbox from the list of recipients that are included in the retention policy.

### Remove organization-wide retention policies

Organization-wide, Exchange-wide, and Teams-wide retention policies apply to every mailbox in the organization. You apply these policies at the organization level (not the mailbox level). When you run the **Get-OrganizationConfig** cmdlet in Step 1, it returns these policies. Run the following command in [Security & Compliance PowerShell](/en-us/powershell/exchange/exchange-online-powershell) to identify the organization-wide retention policies. Use the GUID (not including the `mbx` prefix) for the organization-wide retention policies that you identified in Step 1.

```powershell
Get-RetentionCompliancePolicy <retention policy GUID without prefix> | FL Name
```

After you identify the organization-wide retention policies, go to the **Data lifecycle management** &gt; **Retention policies** page in the Microsoft Purview portal, edit each organization-wide retention policy that you identified in the previous step, and add the mailbox to the list of excluded recipients. This action removes the user's mailbox from the retention policy.

Important

After you exclude a mailbox from an organization-wide retention policy, it might take up to 24 hours to synchronize this change and remove the mailbox from the policy.

### Remove retention labels that preserve mailbox items

When a user applies a label that's configured to retain content or retain and then delete content to any folder or item in their mailbox, the *ComplianceTagHoldApplied* mailbox property is set to **True**. When this property is set, the mailbox is considered to be on hold, as if it was placed on Litigation Hold or assigned to a retention policy.

To view the value of the *ComplianceTagHoldApplied* property, run the following command in Exchange Online PowerShell:

```powershell
Get-Mailbox <username> |FL ComplianceTagHoldApplied
```

After you identify that a mailbox is on hold because a retention label is applied to a folder or item, you can use search in the Microsoft Purview portal to search for labeled items by using the **Retention label** condition. To learn how to search for content with specific retention labels, see:

- The "Using Content Search to find all content with a specific retention label" section in [Learn about retention policies and retention labels](retention#using-content-search-to-find-all-content-with-a-specific-retention-label)
- The "Search conditions" section in [Use the condition builder to create search queries in eDiscovery](edisc-condition-builder#conditions-for-common-properties).

For more information about labels, see [Learn about retention policies and retention labels](retention).

Tip

The *ComplianceTagHoldApplied* value doesn't automatically revert to *False* after all labels are removed. For information about how to reset this property, see [Identify mailboxes on hold because a retention label is applied to a folder or item](edisc-hold-types-mailboxes#identify-mailboxes-on-hold-because-a-retention-label-is-applied-to-a-folder-or-item).

### Remove eDiscovery holds from the mailbox

Run the following commands in [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) to identify the hold associated with an eDiscovery case (called *eDiscovery holds*) that you applied to the mailbox. Use the GUID (not including the `UniH` prefix) for the eDiscovery hold that you identified in Step 1. The second command displays the name of the eDiscovery case the hold is associated with; the third command displays the name of the hold.

```powershell
$CaseHold = Get-CaseHoldPolicy <hold GUID without prefix>
```

```powershell
Get-ComplianceCase $CaseHold.CaseId | FL Name
```

```powershell
$CaseHold.Name
```

After you identify the name of the eDiscovery case and the hold, go to **eDiscovery** in the Microsoft Purview portal, open the case, and remove the mailbox from the hold. For more information about identifying eDiscovery holds, see the "eDiscovery holds" section in [How to identify the type of hold placed on an Exchange Online mailbox](edisc-hold-types-mailboxes).

## Step 4: Remove the delay hold from the mailbox

After you remove any type of hold from a mailbox, the next time the Managed Folder Assistant processes the mailbox and detects that a hold is removed, it sets the value of the *DelayHoldApplied* or *DelayReleaseHoldApplied* mailbox property to **True**. This value is called a *delay hold* and means the actual removal of the hold is delayed for 30 days to prevent data from being permanently deleted from the mailbox. The purpose of a delay hold is to give admins an opportunity to search for or recover mailbox items purged after a hold is removed. When a delay hold is placed on the mailbox, the mailbox is still considered to be on hold for an unlimited duration, as if the mailbox was on Litigation Hold. After 30 days, the delay hold expires, and Microsoft 365 automatically attempts to remove the delay hold (by setting the *DelayHoldApplied* or *DelayReleaseHoldApplied* property to **False**) so that the hold is removed. For more information about a delay hold, see the "Managing mailboxes on delay hold" section in [How to identify the type of hold placed on an Exchange Online mailbox](edisc-hold-types-mailboxes).

You must be assigned the Legal Hold role in Exchange Online to use the *RemoveDelayHoldApplied* or *RemoveDelayReleaseHoldApplied* parameter.

If the value of the *DelayHoldApplied* or *DelayReleaseHoldApplied* property is set to **True**, run one of the following commands to remove the delay hold:

```powershell
Set-Mailbox <username> -RemoveDelayHoldApplied
```

Or

```powershell
Set-Mailbox <username> -RemoveDelayReleaseHoldApplied
```

## Step 5: Delete items in the Recoverable Items folder

Now you're ready to delete items in the Recoverable Items folder by using the [New-ComplianceSearch](/en-us/powershell/module/exchange/new-compliancesearch) and [New-ComplianceSearchAction](/en-us/powershell/module/exchange/new-compliancesearchaction) cmdlets in Security & Compliance PowerShell.

Note

If the mailbox quota is met and the user mailbox is declining emails, you might receive a 554 5.2.0 error when deleting recoverable items. For more information, see ["554 5.2.0 STOREDRV.Deliver.Exception" when sending emails in Exchange Online](/en-us/exchange/troubleshoot/email-delivery/ndr/mapiexceptionnotfound-ndr). For information about increasing the Recoverable Items quota, see [Increase the Recoverable Items quota for mailboxes on hold](edisc-hold-increase-recoverable-item-quota).

Here's an overview of the process to search for and delete items in a user's Recoverable Items folder:

1. **Identify recoverable items in the mailbox**: Use the [Get-RecoverableItems](/en-us/powershell/module/exchangepowershell/get-recoverableitems) cmdlet to retrieve information about items stored in the Recoverable Items folder of the target mailbox. This step helps you understand the volume and characteristics of recoverable items before attempting deletion. For example, you can run the cmdlet to review recoverable items associated with a specific mailbox and determine appropriate criteria for scoping a deletion.

    Review the output to identify common attributes, such as subject, sender, or date range, that you can use to precisely target the items you want to delete.
2. **Create a content search using searchable item properties**. After identifying the recoverable items, use the [New-ComplianceSearch](/en-us/powershell/module/exchange/new-compliancesearch) cmdlet (in Security & Compliance PowerShell) or use eDiscovery search tools in the Microsoft Purview portal to create a content search that returns items from the target items in the recoverable items folder. Use searchable item properties to target the specific items you want to delete. Use conditions that include properties such as *subject*, *sender*, *recipients*, *message type*, and *date range*.

    Define the search criteria carefully to ensure that only the intended items are included in the search results. After the search is created, run it and validate that the results match the items you identified in the previous step.
3. After you create a content search and validate that it returns the items that you want to delete, use the `New-ComplianceSearchAction -Purge -PurgeType HardDelete` command (in Security & Compliance PowerShell) to permanently delete the items returned by the content search. For example, you can run a command similar to the following command:

    ```powershell
    New-ComplianceSearchAction -SearchName "RecoverableItems" -Purge -PurgeType HardDelete
    ```
4. When you run the previous command, it deletes up to 10 items per mailbox. That limit means you might have to run the `New-ComplianceSearchAction -Purge` command multiple times to delete all the items that you want to delete in the Recoverable Items folder. To delete more items, you first have to remove the previous compliance search purge action. You do this by running the `Remove-ComplianceSearchAction` cmdlet. For example, to delete the purge action that you ran in the previous step, run the following command:

    ```powershell
    Remove-ComplianceSearchAction "RecoverableItems_Purge"
    ```

    After you complete this step, you can create a new compliance search purge action to delete more items. You must delete each purge action before creating a new one.

    To get a list of the compliance search actions, you can run the `Get-ComplianceSearchAction` cmdlet. Purge actions are identified by `_Purge` appended to the search name.

### Verify that you deleted items

To verify that you deleted items from the Recoverable Items folder of a mailbox, use the **Get-MailboxFolderStatistics** cmdlet in Exchange Online PowerShell to check the size and number of items in the Recoverable Items folder. You can compare these statistics with the ones you collected in Step 1.

Run the following command to get the current size and total number of items in folders and subfolders in the Recoverable Items folder in the user's primary mailbox.

```powershell
Get-MailboxFolderStatistics <username> -FolderScope RecoverableItems | FL Name,FolderAndSubfolderSize,ItemsInFolderAndSubfolders
```

Run the following command to get the size and total number of items in folders and subfolders in the Recoverable Items folder in the user's archive mailbox.

```powershell
Get-MailboxFolderStatistics <username> -FolderScope RecoverableItems -Archive | FL Name,FolderAndSubfolderSize,ItemsInFolderAndSubfolders
```

## Step 6: Revert the mailbox to its previous state

The final step is to revert the mailbox to its previous configuration. This step resets the properties that you changed in Step 2 and reapplies the holds that you removed in Step 3. This step includes:

- Changing the deleted item retention period back to its previous value. Alternatively, you can set this value to 30 days, the maximum value in Exchange Online.
- Re-enabling single item recovery.
- Re-enabling the client access methods so that the owner can access their mailbox.
- Reapplying the holds and retention policies that you removed.
- Re-enabling the Managed Folder Assistant to process the mailbox.

Important

Wait 24 hours after reapplying a hold or retention policy (and verifying that it's in place) before you re-enable the Managed Folder Assistant to process the mailbox.

Perform the following steps (in the specified sequence) in Exchange Online PowerShell.

1. Run the following command to change the deleted item retention period back to its original value. This example assumes that the previous setting is less than 30 days, such as 14 days.

    ```powershell
    Set-Mailbox <username> -RetainDeletedItemsFor 14
    ```
2. Run the following command to re-enable single item recovery.

    ```powershell
    Set-Mailbox <username> -SingleItemRecoveryEnabled $true
    ```
3. Run the following command to re-enable all client access methods to the mailbox.

    ```powershell
    Set-CASMailbox <username> -EwsEnabled $true -ActiveSyncEnabled $true -MAPIEnabled $true -OWAEnabled $true -ImapEnabled $true -PopEnabled $true
    ```
4. Reapply the holds that you removed in Step 3. Depending on the type of hold, use one of the following procedures.

    **Litigation Hold**

    Run the following command to re-enable a Litigation Hold for the mailbox.

    ```powershell
    Set-Mailbox <username> -LitigationHoldEnabled $true
    ```

    **Retention policies applied to specific mailboxes**

    Use the Microsoft Purview portal to add the mailbox back to the retention policy. Go to the **Data lifecycle management** &gt; **Retention policies** page in the Microsoft Purview portal, edit the retention policy, and add the mailbox back to the list of recipients that the retention policy is applied to.

    **Organization-wide retention policies**

    If you removed an organization-wide or Exchange-wide retention policy by excluding it from the policy, use the Microsoft Purview portal to remove the mailbox from the list of excluded users. Go to the **Data lifecycle management** &gt; **Retention policies** page in the Microsoft Purview portal, edit the organization-wide retention policy, and remove the mailbox from the list of excluded recipients. Doing this reapplies the retention policy to the user's mailbox.

    **eDiscovery case holds**

    Use the Microsoft Purview portal to add the mailbox back the hold that's associated with an eDiscovery case. Go to **eDiscovery**, open the case, and add the mailbox back to the hold.
5. Run the following command to allow the Managed Folder Assistant to process the mailbox again.

    ```powershell
    Set-Mailbox <username> -ElcProcessingDisabled $false
    ```
6. To verify that the mailbox is reverted back to its previous configuration, run the following commands and then compare the settings to the ones that you collected in Step 1.

    ```powershell
    Get-Mailbox <username> | FL ElcProcessingDisabled,InPlaceHolds,LitigationHoldEnabled,RetainDeletedItemsFor,SingleItemRecoveryEnabled
    ```

    ```powershell
    Get-CASMailbox <username> | FL EwsEnabled,ActiveSyncEnabled,MAPIEnabled,OWAEnabled,ImapEnabled,PopEnabled
    ```

## Identify hold types by InPlaceHolds property values

The following table describes how to identify different types of holds based on the values in the *InPlaceHolds* property when you run the **Get-Mailbox** or **Get-OrganizationConfig** cmdlets. For more detailed information, see [How to identify the type of hold placed on an Exchange Online mailbox](edisc-hold-types-mailboxes).

You need to remove all holds and retention policies from a mailbox before you can successfully delete items in the Recoverable Items folder.

| Hold type | Example value | How to identify the hold |
| --- | --- | --- |
| Litigation Hold | `True` | The *LitigationHoldEnabled* property is set to `True`. |
| Retention policies in the Microsoft Purview portal applied to specific mailboxes | `mbxcdbbb86ce60342489bff371876e7f224` or `skp127d7cf1076947929bf136b7a2a8c36f` | When you run the **Get-Mailbox** cmdlet, the *InPlaceHolds* property also contains GUIDs of retention policies applied to the mailbox. You can identify retention policies because the GUID starts with the `mbx` prefix. If the GUID of the retention policy starts with the `skp` prefix, that indicates that the retention policy is applied to Skype for Business conversations.  To identity the retention policy that's applied to the mailbox, run the following command in Security & Compliance PowerShell: `Get-RetentionCompliancePolicy <retention policy GUID without prefix> | FL Name`Be sure to remove the `mbx` or `skp` prefix when you run this command. |
| Organization-wide retention policies in the Microsoft Purview portal | No value  or `-mbxe9b52bf7ab3b46a286308ecb29624696` (indicates that the mailbox is excluded from an organization-wide policy) | Even if the *InPlaceHolds* property is empty when you run the **Get-Mailbox** cmdlet, one or more organization-wide retention policies might still apply to the mailbox.  To verify this, run the `Get-OrganizationConfig | FL InPlaceHolds` command in Exchange Online PowerShell to get a list of the GUIDs for organization-wide retention policies. The GUID for organization-wide retention policies applied to Exchange mailboxes starts with the `mbx` prefix. For example, `mbxa3056bb15562480fadb46ce523ff7b02`.  To identity the organization-wide retention policy that's applied to the mailbox, run the following command in Security & Compliance PowerShell: `Get-RetentionCompliancePolicy <retention policy GUID without prefix> | FL Name`If a mailbox is excluded from an organization-wide retention policy, the GUID for the retention policy appears in the *InPlaceHolds* property of the user's mailbox when you run the **Get-Mailbox** cmdlet. It's identified by the prefix `-mbx`. For example, `-mbxe9b52bf7ab3b46a286308ecb29624696`. |
| eDiscovery case hold in the Microsoft Purview portal | `UniH7d895d48-7e23-4a8d-8346-533c3beac15d` | The *InPlaceHolds* property also contains the GUID of any hold associated with an eDiscovery case in the Microsoft Purview portal that might be placed on the mailbox. You can tell this is an eDiscovery case hold because the GUID starts with the `UniH` prefix.  You can use the `Get-CaseHoldPolicy` cmdlet in Security & Compliance PowerShell to get information about the eDiscovery case that the hold on the mailbox is associated with. For example, you can run the command `Get-CaseHoldPolicy <hold GUID without prefix> | FL Name` to display the name of the case hold that's on the mailbox. Be sure to remove the `UniH` prefix when you run this command.  To identity the eDiscovery case that the hold on the mailbox is associated with, run the following commands:`$CaseHold = Get-CaseHoldPolicy <hold GUID without prefix>``Get-ComplianceCase $CaseHold.CaseId | FL Name` |