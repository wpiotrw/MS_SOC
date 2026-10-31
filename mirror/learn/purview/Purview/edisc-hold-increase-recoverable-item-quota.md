---
layout: Conceptual
title: Increase the Recoverable Items quota for mailboxes on hold in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-hold-increase-recoverable-item-quota
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Enable the archive mailbox and turn on auto-expanding archiving to increase the size of the Recoverable Items folder for a mailbox.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-10-15T00:00:00.0000000Z
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
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: e10c0bb6-fc65-9014-29be-55d6cf7ef585
document_version_independent_id: e10c0bb6-fc65-9014-29be-55d6cf7ef585
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-hold-increase-recoverable-item-quota.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-hold-increase-recoverable-item-quota
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-hold-increase-recoverable-item-quota.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
platformId: 4ae9d9a1-b591-75c9-768b-3c1a62d5fe44
---

# Increase the Recoverable Items quota for mailboxes on hold in eDiscovery | Microsoft Learn

The default Exchange retention policy—named *Default MRM Policy*—that automatically applied to new mailboxes in Exchange Online contains a retention tag named Recoverable Items 14 days move to archive. This retention tag moves items from the Recoverable Items folder in the user's primary mailbox to the Recoverable Items folder in the user's archive mailbox after the 14-day retention period expires for an item.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

Emails in the Deletions folder retain based on the **RetainDeletedItemsFor** parameter and move to other folders in recoverable deleted items and then to the archive mailbox. For this process to work, the user's archive mailbox must be enabled. If the archive mailbox isn't enabled, no action is taken, which means that items in the Recoverable Items folder for a mailbox on hold aren't moved to the archive mailbox after the 14-day retention period expires. Because nothing is deleted from a mailbox on hold, it's possible that the storage quota for the Recoverable Items folder might be exceeded, especially if the user's archive mailbox isn't enabled. For information about deleting items from the Recoverable Items folder, see [Delete Recoverable Items from mailboxes on hold](edisc-hold-delete-recoverable-items).

To help reduce the chance of exceeding the Recoverable Items folder storage quota, the storage quota for the Recoverable Items folder automatically increases from 30 GB to 100 GB when you [create an eDiscovery hold](edisc-hold-create) on a mailbox in Exchange Online. If the archive mailbox is enabled, the storage quota for the Recoverable Items folder in the archive mailbox also increases from 30 GB to 100 GB. If archive is enabled on a mailbox that is on hold with auto-expanding archive disabled, the storage quota of the Recoverable Items folder quota increases from 100 GB to 105 GB. If the auto-expanding archiving feature in Exchange Online is enabled, the total storage quota for the user's archive mailbox, including the Recoverable Items folder, is 1.5 TB or 3 TB, depending on the user's license. For license eligibility details, see [Learn about auto-expanding archiving](autoexpanding-archiving).

The following table summarizes the storage quota for the Recoverable Items folder.

| Location of Recoverable Items folder | Mailboxes not on hold | Mailboxes on hold |
| --- | --- | --- |
| Primary mailbox | 30 GB | 100 GB |
| Archive mailbox, including Recoverable Items folder ^\*^ | 1.5 TB or 3 TB, depending on the user's license | 1.5 TB or 3 TB, depending on the user's license |

Note

^\*^ The initial storage quota for the archive mailbox is 100 GB for users with an Exchange Online (Plan 2) license. However, when auto-expanding archiving is turned on for mailboxes on hold, the storage quota for both the archive mailbox and the Recoverable Items folder increases to 110 GB. Additional archive storage space (which includes the Recoverable Items folder) up to 1.5 TB or 3 TB is provisioned when necessary, depending on the user's license. For more information about auto-expanding archiving and license eligibility, see [Learn about auto-expanding archiving](autoexpanding-archiving).

Note

When archiving is enabled for a specific user whose mailbox is on hold or assigned to a retention policy, the storage quota for the user's primary mailbox's Recoverable Items folder raises from 100 GB to 105 GB and Recoverable items warning quota raises from 90 GB to 95 GB. This extra space supports an efficient archiving experience for users, even if auto-expanding archive isn't enabled.

When the storage quota for the Recoverable Items folder in the primary mailbox of a mailbox on hold is close to reaching its limit, you can do the following things:

- **Enable the archive mailbox and turn on auto-expanding archiving.** You can enable an extra storage capacity for the Recoverable Items folder by enabling the archive mailbox and then turning on the auto-expanding archiving feature in Exchange Online. This change results in 110 GB for the Recoverable Items folder in the primary mailbox and up to 1.5 TB or 3 TB of combined storage capacity for the archive and Recoverable Items folder, depending on the user's license. For more information, see [Enable archive mailboxes](enable-archive-mailboxes) and [Enable auto-expanding archiving](enable-autoexpanding-archiving).

    Note

    After you enable the archive for a mailbox that's close to exceeding the storage quota for the Recoverable Items folder, you might want to run the Managed Folder Assistant to manually trigger the assistant to process the mailbox so that expired items move to the Recoverable Items folder in the archive mailbox. See Run the Managed Folder Assistant to apply the new retention settings for instructions. Other items in the user's mailbox might move to the new archive mailbox. Consider telling the user that this change might happen after you enable the archive mailbox.
- **Create a custom Exchange retention policy for mailboxes on hold.** In addition to enabling the archive mailbox and auto-expanding archiving for mailboxes on [Litigation Hold](/en-us/microsoft-365/admin/misc/create-litigation-hold-mac?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json), you might also want to create a custom Exchange retention policy for mailboxes on hold. This policy lets you apply a retention policy to mailboxes on hold that's different from the Default MRM Policy that's applied to mailboxes that aren't on hold, and lets you apply retention tags that are designed for mailboxes on hold. This policy includes creating a new retention tag for the Recoverable Items folder.

The rest of this article describes the step-by-step procedures to create a custom Exchange retention policy for mailboxes on hold.

- Step 1: Create a custom retention tag for the Recoverable Items folder
- Step 2: Create a new Exchange retention policy for mailboxes on hold
- Step 3: Apply the new Exchange retention policy to mailboxes on hold
- (Optional) Step 4: Run the Managed Folder Assistant to apply the new retention settings

## Step 1: Create a custom retention tag for the Recoverable Items folder

First, create a custom retention tag (called a retention policy tag or RPT) for the Recoverable Items folder. This RPT moves items from the Recoverable Items folder in the user's primary mailbox to the Recoverable Items folder in the user's archive mailbox. Use PowerShell to create an RPT for the Recoverable Items folder. You can't use the Exchange admin center (EAC).

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell)
2. Run the following command to create a new RPT for the Recoverable Items folder:

    ```powershell
    New-RetentionPolicyTag -Name <Name of RPT> -Type RecoverableItems -AgeLimitForRetention <Number of days> -RetentionAction MoveToArchive
    ```

    For example, the following command creates an RPT for the Recoverable Items folder named "Recoverable Items 30 days for mailboxes on hold", with a retention period of 30 days. This means that after an item has been in the Recoverable Items folder for 30 days, it's moved to the Recoverable Items folder in the user's archive mailbox.

    ```powershell
    New-RetentionPolicyTag -Name "Recoverable Items 30 days for mailboxes on hold" -Type RecoverableItems -AgeLimitForRetention 30 -RetentionAction MoveToArchive
    ```

    Tip

    Set the retention period (defined by the *AgeLimitForRetention* parameter) for the Recoverable Items RPT to match the deleted item retention period for the mailboxes that the RPT applies to. This setup gives users the entire deleted item retention period to recover deleted items before they're moved to the archive mailbox. In the previous example, the retention period was set to 30 days based on the assumption that the deleted item retention period for mailboxes is also 30 days. An Exchange Online mailbox is configured to retain deleted items for 14 days, by default. But you can change this setting to a maximum of 30 days. For more information, see [Change the deleted item retention period for a mailbox in Exchange Online](/en-us/exchange/recipients-in-exchange-online/manage-user-mailboxes/change-deleted-item-retention?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

## Step 2: Create a new Exchange retention policy for mailboxes on hold

Next, create a new retention policy and add retention tags to it, including the Recoverable Items RPT that you created in Step 1. In Step 3, you apply this new policy to mailboxes on hold.

Before you create the new retention policy, determine the additional retention tags that you want to add. For a list of the retention tags that are added to the Default MRM Policy and for information about creating new retention tags, see the following:

- [Default Retention Policy in Exchange Online](/en-us/exchange/security-and-compliance/messaging-records-management/default-retention-policy?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json)
- [Default folders that support Retention Policy Tags](/en-us/exchange/security-and-compliance/messaging-records-management/default-folders?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json)
- The "Create a retention tag" section in the [Create a Retention Policy](/en-us/exchange/security-and-compliance/messaging-records-management/create-a-retention-policy?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) article.

You can use the EAC or Exchange Online PowerShell to create a retention policy.

### Use the EAC to create a retention policy

Perform the following steps in the EAC to create the retention policy:

1. In the EAC, go to **Compliance management** &gt; **Retention policies**, and then select **Add**![Icon for adding a new retention policy in the Exchange admin center.](media/itpro-eac-addicon.gif).
2. On **New retention policy**, under **Name**, type a name that describes the purpose of the retention policy; for example, **MRM Policy for Mailboxes on Hold**.
3. Under **Retention tags**, select **Add**![Icon for adding retention tags to the policy.](media/itpro-eac-addicon.gif).
4. In the list of retention tags, select the Recoverable Items RPT that you created in Step 1, and then select **Add**.
5. Select additional retention tags to add to the retention policy. For example, you might want to add the same tags that are included in the Default MRM Policy.
6. When you finish adding retention tags, select **OK**.
7. Select **Save** to create the new retention policy. The details pane displays the retention tags linked to the retention policy.

### Use Exchange Online PowerShell to create a retention policy

Run the following command to create new retention policy for mailboxes on hold.

```powershell
New-RetentionPolicy <Name of retention policy>  -RetentionPolicyTagLinks <list of retention tags>
```

For example, the following command creates the retention policy and links the retention tags listed in the EAC procedure earlier in this section.

```powershell
New-RetentionPolicy "MRM Policy for Mailboxes on Hold"  -RetentionPolicyTagLinks "Recoverable Items 30 days for mailboxes on hold","1 Month Delete","1 Week Delete","1 Year Delete","5 Year Delete","6 Month Delete","Default 2 year move to archive","Junk Email","Never Delete","Personal 1 year move to archive","Personal 5 year move to archive"
```

## Step 3: Apply the new Exchange retention policy to mailboxes on hold

In the last step, apply the new retention policy that you created in Step 2 to mailboxes on hold in your organization. You can use the EAC or Exchange Online PowerShell to apply the retention policy to a single mailbox or to multiple mailboxes.

### Use the EAC to apply the new retention policy

Use the following steps in the EAC to apply the new retention policy to one or more mailboxes:

1. Go to **Recipients** &gt; **Mailboxes**.
2. In the list view, select the mailbox you want to apply the retention policy to, then select **Edit**.
3. On the **User Mailbox** page, select **Mailbox features**.
4. Under **Retention policy**, select the retention policy that you created in Step 2, then select **Save**.

You can also use the EAC to apply the retention policy to multiple mailboxes.

1. Go to **Recipients** &gt; **Mailboxes**.
2. In the list view, use the Shift or Ctrl keys to select multiple mailboxes.
3. In the details pane, select **More options**.
4. Under **Retention Policy**, select **Update**.
5. On the **Bulk assign retention policy** page, select the retention policy that you created in Step 2, then select **Save**.

### Use Exchange Online PowerShell to apply the new retention policy

You can use Exchange Online PowerShell to apply a new retention policy to a single mailbox. But the real power of PowerShell is that you can use it to quickly identify all the mailboxes in your organization that are on Litigation Hold, and then apply the new retention policy to all mailboxes on hold in a single command. Here are some examples of using Exchange PowerShell to apply a retention policy to one or more mailboxes. All of the examples apply the retention policy that you created in Step 2.

This example applies the new retention policy to Pilar Pinilla's mailbox.

```powershell
Set-Mailbox "Pilar Pinilla" -RetentionPolicy "MRM Policy for Mailboxes on Hold"
```

This example applies the new retention policy to all mailboxes in the organization that are on Litigation Hold.

```powershell
$LitigationHolds = Get-Mailbox -ResultSize unlimited | Where-Object {$_.LitigationHoldEnabled -eq 'True'}
```

```powershell
$LitigationHolds.DistinguishedName | Set-Mailbox -RetentionPolicy "MRM Policy for Mailboxes on Hold"
```

You can use the **Get-Mailbox** cmdlet to verify that you applied the new retention policy.

Here are some examples to verify that the commands in the previous examples applied the "MRM Policy for Mailboxes on Hold" retention policy to mailboxes on Litigation Hold.

```powershell
Get-Mailbox "Pilar Pinilla" | Select RetentionPolicy
```

```powershell
Get-Mailbox -ResultSize unlimited | Where-Object {$_.LitigationHoldEnabled -eq 'True'} | FT DisplayName,RetentionPolicy -Auto
```

## (Optional) Step 4: Run the Managed Folder Assistant to apply the new retention settings

After you apply the new Exchange retention policy to mailboxes on hold, it can take up to seven days in Exchange Online for the Managed Folder Assistant to process these mailboxes by using the settings in the new retention policy. Instead of waiting for the Managed Folder Assistant to run, you can use the **Start-ManagedFolderAssistant** cmdlet to manually trigger the assistant to process the mailboxes that you applied the new retention policy to.

Run the following command to start the Managed Folder Assistant for Pilar Pinilla's mailbox.

```powershell
Start-ManagedFolderAssistant "Pilar Pinilla"
```

Run the following commands to start the Managed Folder Assistant for all mailboxes on hold.

```powershell
$MailboxesOnHold = Get-Mailbox -ResultSize unlimited | Where-Object {($_.InPlaceHolds -ne $null) -or ($_.LitigationHoldEnabled -eq "True")}
```

```powershell
$MailboxesOnHold.DistinguishedName | Start-ManagedFolderAssistant
```

## Additional considerations for archive mailboxes and retention policies

### User communication considerations

- When you enable a user's archive mailbox, consider telling the user that other items in their mailbox (not just items in the Recoverable Items folder) might move to the archive mailbox. This behavior occurs because the Default MRM Policy that's assigned to Exchange Online mailboxes contains a retention tag (named Default 2 years move to archive) that moves items to the archive mailbox two years after the date the item is delivered to the mailbox or created by the user. For more information, see [Default Retention Policy in Exchange Online](/en-us/exchange/security-and-compliance/messaging-records-management/default-retention-policy?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).
- When you enable a user's archive mailbox, consider telling the user that they can recover deleted items in the Recoverable Items folder in their archive mailbox. They can do this in Outlook by selecting the **Deleted Items** folder in the archive mailbox, then selecting **Recover Deleted Items from Server** on the **Home** tab. For more information about recovering deleted items, see [Recover deleted items in Outlook for Windows](https://go.microsoft.com/fwlink/p/?LinkId=624829).