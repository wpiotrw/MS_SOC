---
layout: Conceptual
title: Customize an archive and deletion policy (MRM) for mailboxes | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/set-up-an-archive-and-deletion-policy-for-mailboxes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: brenle
ms.date: 2024-12-03T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-exchange-legacy
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MED150
- MBS150
- BCS160
- MET150
ms.assetid: ec3587e4-7b4a-40fb-8fb8-8aa05aeae2ce
ms.custom:
- seo-marvel-apr2020
- admindeeplinkEXCHANGE
- sfi-ga-nochange
description: How to create a custom messaging records management (MRM) archiving and deletion policy to automatically move items to a user's archive mailbox.
locale: en-us
document_id: 53bf9168-b379-6ef5-4e53-2ada5e1250a9
document_version_independent_id: 53bf9168-b379-6ef5-4e53-2ada5e1250a9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/set-up-an-archive-and-deletion-policy-for-mailboxes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: set-up-an-archive-and-deletion-policy-for-mailboxes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/set-up-an-archive-and-deletion-policy-for-mailboxes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a68bc39a-ef8e-f14b-0817-13197ea4e2d9
---

# Customize an archive and deletion policy (MRM) for mailboxes | Microsoft Learn

To retain and delete emails, we recommend you use [Microsoft 365 retention policies and retention labels](retention) rather than the older messaging records management (MRM) from Exchange Online. However, a valid reason to still use this older feature is to automatically move emails from a user's primary mailbox to their [archive mailbox](archive-mailboxes). You might also need to use MRM to apply retention and deletion settings to specific folders in the mailbox, rather than the entire mailbox.

Use this article as an example scenario to better understand these two valid reasons to use MRM retention policies and retention tags. For all other retention and deletion scenarios, use Microsoft 365 retention policies and retention labels.

The configuration steps in our example scenario require you to create an MRM retention policy that you then assign to mailboxes. This policy moves items to a user's archive mailbox after a specified period of time and also deletes items from the Deleted items folder after they reach a specific age limit.

Note

Instructions in this article use the [Microsoft Purview portal](purview-portal) and the [Exchange admin center](/en-us/exchange/features-in-new-eac).

The actual rules that determine what items are moved or deleted and when that happens are called **retention tags**. Retention tags are linked to an **MRM retention policy**, that in turn is assigned to a user's mailbox. A retention tag applies retention settings to individual messages and folders in a user's mailbox. It defines how long a message remains in the mailbox and what action is taken when the message reaches the specified retention age. When a message reaches its retention age, it's either moved to the user's archive mailbox or it's deleted.

## Example scenario for the instructions

The steps in this article set up an archiving and retention policy for a fictitious organization named Alpine House. This example deployment requires the following tasks:

- Step 1: Enable an archive mailbox for every user in the organization. This procedure gives users more mailbox storage, and is required so that a retention policy can automatically move items to the archive mailbox. A user can also manually move items to their archive mailbox for archival storage.
- Step 2: Create two custom retention tags to do the following actions:

    - Automatically move items that are 3 years old to the user's archive mailbox. Moving items to the archive mailbox frees up space in a user's primary mailbox.
    - Automatically delete items that are 5 years old from the Deleted Items folder. This also frees up space in the user's primary mailbox. Users will have the opportunity to recover these items if necessary. For more information, see the final bullet in the More information section.
- Step 3: Create a new retention policy and add the new custom retention tags to it. Additionally, you'll add a built-in retention tag that can't be achieved with a recommended Microsoft 365 retention label because it also moves items to the archive mailbox. It's a personal tag for archiving after 1 year that users can assign to items in their mailbox when they want a shorter archive period than their default of 3 years.
- Step 4: Replace the Default MRM policy with the new retention policy you've created.

Optionally, you can also run the Managed Folder Assistant to apply the new settings, and make the new retention policy the default for your organization.

You can follow some or all of the steps in this article to help understand how to set up your own archive and deletion policy for mailboxes in your organization. We recommend that you test this process on a few mailboxes before implementing it on all mailboxes in your organization.

## Before you set up the archive and deletion policy

- To follow this example configuration, use an isolated, test environment that won't impact users on your production network. Then take your learnings to your production network.
- In your isolated test environment, consider using a global administrator account so you can perform all the steps for this example scenario. In a production environment, always use administrative roles that grant least privilege.
- When you create a new user account and assign the user an Exchange Online license, a mailbox is automatically created for the user. When the mailbox is created, it's automatically assigned a default retention policy, named Default MRM Policy. In this example deployment, you'll create a new MRM retention policy and then assign it to user mailboxes, replacing the Default MRM policy. A mailbox can have only one MRM retention policy assigned to it at any one time.
- To learn more about retention tags and MRM retention policies in Exchange Online, see [Retention tags and retention policies](/en-us/exchange/security-and-compliance/messaging-records-management/retention-tags-and-policies) and the associated instructions. For example:

    - [Create a retention policy for Exchange Online](/en-us/exchange/security-and-compliance/messaging-records-management/create-a-retention-policy)
    - [Add retention tags to or remove retention tags from a retention policy in Exchange Online](/en-us/exchange/security-and-compliance/messaging-records-management/add-or-remove-retention-tags)

## Step 1: Enable archive mailboxes for users

The first step is to ensure each user in your organization has an archive mailbox. A user's archive mailbox must be enabled so that for our example scenario, a retention tag with a "Move to Archive" retention action can move the item after the retention age expires.

For instructions to enable archive mailboxes, see [Enable archive mailboxes in Microsoft 365](enable-archive-mailboxes).

Note

You can enable archive mailboxes any time during this process, just as long as they're enabled at some point before you complete the process. If an archive mailbox isn't enabled, no action is taken on any items that have an archive or deletion policy assigned to it.

## Step 2: Create new retention tags for the archive and deletion policies

In this step, you'll create the two custom retention tags that were previously described for our example scenario.

- A custom archive default policy tag, which we'll name "Alpine House 3 Year Move to Archive".
- A custom retention policy tag configured for the Deleted Items folder, which we'll name "Alpine House Deleted Items 5 Years Delete and Allow Recovery".

For this configuration, you use the [Microsoft Purview portal](purview-portal).

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Exchange (legacy)** &gt; **MRM Retention tags**.

    A list of the retention tags for your organization is displayed.

Follow the step-by-steps instructions how to create the example retention tags for our scenario.

### Create the custom archive default policy tag

First for our example scenario, you'll create a custom archive default policy tag (DPT) that will move items to the archive mailbox after 3 years.

1. On the **MRM Retention tags** page, select **+ New tag**, and then on the **Name your tag** page, type a name for the new retention tag, and an optional description that explains the purpose of the custom retention tag.

    For our example scenario, we'll name this tag "Alpine House 3 Year Move to Archive".
2. On the **Define how the tag will be applied** page, select **Automatically to entire mailbox (default)**.
3. On the **Define retention settings** page, complete the following fields:

    1. **When items reaches the following age (in days)** Enter the duration of the retention period. For this scenario, items will be moved to the archive mailbox after 1095 days (3 years).
    2. For the **Retention Action** Select **Move item to archive** to move items to the archive mailbox when the retention period expires.
4. Select **Next**, and then review and submit to create the custom archive DPT.

The new archive DPT is displayed in the list of retention tags.

### Create the custom retention policy tag for the Deleted Items folder

The second retention tag to create for our example scenario is a custom retention policy tag (RPT) for the Deleted Items folder. This retention tag will delete items in the Deleted Items folder after 5 years, and provides a recovery period when users can use the Recover Deleted Items tool to recover an item.

1. Back on the **MRM Retention tags** page, select **+ New tag**, and on the **Name your tag** page, type a name for the new retention tag, and an optional description that explains the purpose of the custom retention tag.

    For our example scenario, we'll name this tag "Alpine House Deleted Items 5 Years Delete and Allow Recovery".
2. On the **Define how the tag will be applied** page, select **Automatically to default folder** and then for the **Apply tag to this folder** option, select **Deleted items**.
3. On the **Define retention settings** page, complete the following fields:

    1. **When items reaches the following age (in days)** Enter the duration of the retention period. For this scenario, items will be deleted after 1825 days (5 years).
    2. For the **Retention Action** Select **Delete and allow recovery** to delete items when the retention period expires, but allow users to recover a deleted item within the deleted item retention period (which by default is 14 days).
4. Select **Next**, and then review and submit to create the custom deletion DPT.

The new RPT is displayed in the list of retention tags.

## Step 3: Create a new retention policy

After you create the custom retention tags, the next step for our example scenario is to create a new retention policy and add the retention tags. You'll add the two custom retention tags that you created in Step 2, and a built-in tag that's preconfigured for you. In Step 4, you'll assign this new retention policy to user mailboxes.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** card &gt; **Exchange (legacy)** &gt; **MRM Retention policies**.
2. On the **MRM Retention policies** page, select **New policy**.
3. In the **Name** box, type a name for the new retention policy; for example, **Alpine House Archive and Deletion Policy**.
4. Select **+ Add tag**.

    A list of the retention tags in your organization is displayed, which includes the custom tags that you created in Step 2.
5. Add the 3 retention tags that are described in more detail in the More information section:

    - **Alpine House 3 Year Move to Archive** - the custom archive default policy tag created in step 2 of these instructions
    - **Alpine House Deleted Items 5 Years Delete and Allow Recovery** - the custom tag for the Deleted Items folder created in step 2 of these instructions
    - **Personal 1 year move to archive** - a built-in tag that's preconfigured

    To add these retention tags, select them, and then select **Add**.
6. Back on the **Configure your policy** page, select **Next** to review and submit the new policy.

The new retention policy is displayed in the list. Select it to display the retention tags linked to it in the details pane.

## Step 4: Assign the new retention policy to user mailboxes

When a new mailbox is created, a retention policy named Default MRM policy is assigned to it by default. In this step for our example scenario, you'll replace this retention policy by assigning the new retention policy that you created in Step 3 to the user mailboxes in your organization.

Replacement is required because a mailbox can have only one MRM retention policy assigned to it at a time. This step assumes that you'll assign the new policy to all mailboxes in your organization.

To follow these steps, make sure you use the [new Exchange admin center](/en-us/exchange/features-in-new-eac), rather than the classic version.

1. Sign in to the [Exchange admin center (EAC)](https://go.microsoft.com/fwlink/p/?linkid=2059104), and go to **Recipients** &gt; **Mailboxes**.

    A list of all user mailboxes in your organization is displayed.
2. Select all the mailboxes by selecting the box for **Display name**.
3. Select the **Mailbox policies** option.
4. In the **Mailbox policies** flyout pane, under **Retention Policy**, select the retention policy that you created in Step 3; for example, **Alpine House Archive and Retention Policy**.
5. Select **Save** to save the new retention policy assignment.
6. To verify that the new retention policy was assigned to mailboxes:

    1. Select a mailbox on the **Mailboxes** page.
    2. On the mailbox properties page for the selected user, select **Mailbox**.

    The name of the new policy assigned to the mailbox is displayed for the **Retention policy**.

## (Optional) Step 5: Run the Managed Folder Assistant to apply the new settings

After you apply the new retention policy to mailboxes in Step 4, it can take up to 7 days in Exchange Online for the new retention settings to be applied to the mailboxes. This is because a process called the *Managed Folder Assistant* processes mailboxes at least once every 7 days. Instead of waiting for the Managed Folder Assistant to run, you can force this to happen by running the **Start-ManagedFolderAssistant** cmdlet in Exchange Online PowerShell.

**What happens when you run the Managed Folder Assistant?** It applies the settings in the retention policy by inspecting items in the mailbox and determining whether they're subject to retention. It then stamps items subject to retention with the appropriate retention tag, and then takes the specified retention action on items past their retention age.

Here are the steps to connect to Exchange Online PowerShell, and then run the Managed Folder Assistant on every mailbox in your organization.

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the following two commands to start the Managed Folder Assistant for all user mailboxes in your organization.

    ```powershell
    $Mailboxes = Get-Mailbox -ResultSize Unlimited -Filter {RecipientTypeDetails -eq "UserMailbox"}
    ```

    ```powershell
    $Mailboxes.Identity | Start-ManagedFolderAssistant
    ```

That's it! You've set up an archive and deletion policy for the Alpine House organization.

### More information about the Managed Folder Assistant

As previously stated, the Managed Folder Assistant processes mailboxes at least once every 7 days. So it's possible that a mailbox can be processed by the Managed Folder Assistant more frequently. Also, admins can't predict the next time a mailbox is processed by the Managed Folder Assistant, which is one reason why you might want to run it manually.

However, if you want to temporarily prevent the Managed Folder Assistant from applying the new retention settings to a mailbox, you can run the `Set-Mailbox -ElcProcessingDisabled $true` command to temporarily disable the Managed Folder Assistant from processing a mailbox.

To re-enable the Managed Folder Assistant for a mailbox, run the `Set-Mailbox -ElcProcessingDisabled $false` command.

Finally, if a mailbox user has a disabled account, items aren't moved to the archive mailbox for that mailbox.

## (Optional) Step 6: Make the new retention policy the default for your organization

In Step 4, you have to assign the new retention policy to existing mailboxes. But you can configure Exchange Online so that the new retention policy is assigned to new mailboxes that are created in the future.

You do this by using Exchange Online PowerShell to update your organization's default mailbox plan. A *mailbox plan* is a template that automatically configures properties on new mailboxes. In this optional step, you can replace the current retention policy that's assigned to the mailbox plan (by default, the Default MRM Policy) with the MRM retention policy that you created in Step 3. After you update the mailbox plan, the new MRM retention policy will be assigned to new mailboxes.

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the following command to display information about the mailbox plans in your organization.

    ```powershell
    Get-MailboxPlan | Format-Table DisplayName,RetentionPolicy,IsDefault
    ```

    Note the mailbox plan that's set as the default.
3. Run the following command to assign the new MRM retention policy that you created in Step 3 (for example, **Alpine House Archive and Retention Policy**) to the default mailbox plan. This example assumes the name of the default mailbox plan is **ExchangeOnlineEnterprise**.

    ```powershell
    Set-MailboxPlan "ExchangeOnlineEnterprise" -RetentionPolicy "Alpine House Archive and Retention Policy"
    ```
4. You can rerun the command in step 2 to verify that the MRM retention policy assigned to the default mailbox plan was changed.

## More information

- The retention age of mailbox items is calculated from the date of delivery. Or from the date of creation for items such as draft messages that aren't sent but are created by the user. When the Managed Folder Assistant processes items in a mailbox, it stamps a start date and an expiration date for all items that have retention tags with the Delete and Allow Recovery or Permanently Delete retention action. Items that have an archive tag are stamped with a move date.
- The following table provides more information about each retention tag for the custom MRM retention policy in this article.

    | Retention tag | What this tag does | Built-in or custom? | Type |
    | --- | --- | --- | --- |
    | Alpine House 3 Year Move to Archive | Moves items that are 1095 days (3 years) old to the archive mailbox. | Custom (See Step 2: Create new retention tags for the archive and deletion policies) | Default Policy Tag (archive); this tag is automatically applied to the entire mailbox. |
    | Alpine House Deleted Items 5 Years Delete and Allow Recovery | Deletes items from the Deleted Items folder that are 5 years old. Users can recover these items for up 14 days after they're deleted. See the next list entry for more information. | Custom (See Step 2: Create new retention tags for the archive and deletion policies) | Retention Policy Tag (Deleted Items); this tag is automatically applied to items in the Deleted items folder. |
    | Personal 1 year move to archive | Moves items to the archive mailbox after 1 year. | Built-in | Personal; this tag can be applied by users. |
- Users can use the Recover Deleted Items tool in Outlook and Outlook on the web to recover a deleted item within the deleted item retention period, which by default is 14 days in Exchange Online. An administrator can use Exchange Online PowerShell to increase the deleted item retention period to a maximum of 30 days. For more information, see: [Recover deleted items in Outlook for Windows](https://support.office.com/article/49e81f3c-c8f4-4426-a0b9-c0fd751d48ce) and [Change the deleted item retention period for a mailbox in Exchange Online](/en-us/exchange/recipients-in-exchange-online/manage-user-mailboxes/change-deleted-item-retention).