---
layout: Conceptual
title: Find and delete email messages in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-mailbox-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use eDiscovery and PowerShell to search for and delete email messages in your organization.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
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
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 4f28c70b-b6c9-192f-dc1c-ac39e0088c05
document_version_independent_id: 4f28c70b-b6c9-192f-dc1c-ac39e0088c05
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-mailbox-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-mailbox-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-mailbox-data.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: aa91d713-3850-f6bb-11d6-8bfc5a99f01b
---

# Find and delete email messages in eDiscovery | Microsoft Learn

Tip

You can also use the purge feature in Data Security Investigations to search for and permanently delete Exchange mailbox and Microsoft Teams items in your organization. Data Security Investigations provides a built-in search and purge workflow with a purge queue dashboard to help you manage and track purge queries. For more information, see [Purge in Data Security Investigations](data-security-investigations-mitigation-actions#purge).

You can use the search feature to search for and delete email messages from all mailboxes in your organization. This process can help you find and remove potentially harmful or high-risk email, such as:

- Messages that contain dangerous attachments or viruses
- Phishing messages
- Messages that contain sensitive data

However, the eDiscovery purge process isn't intended for general mailbox management tasks such as:

- Reducing mailbox quota
- Clearing out mailboxes
- Enforcing data retention policies

The purge process described in this article is specifically designed to address **data spillage incidents**, such as when a small message is accidentally shared with a large group of users. For routine mailbox management and compliance, use the following tools instead:

- **Retention Policies**: To manage the lifecycle of data and ensure compliance with organizational standards.
- **Archive Policies**: To offload older content and manage mailbox storage effectively.
- **Mailbox Ownership and Manual Deletion**: For precise control over specific mailboxes, especially when content needs to be reviewed or removed by the mailbox owner.

Tip

If your organization has a Defender for Office 365 Plan 2 subscription, use the procedure detailed in [Remediate malicious email delivered in Office 365](/en-us/microsoft-365/security/office-365-security/remediate-malicious-email-delivered-office-365?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json), rather than following the procedure described in this article.

## Before you begin

Important

Carefully review the following guidance before starting the search and purge steps for email messages.

- Depending on the eDiscovery subscription for your organization, cases can either be enabled for eDiscovery premium features, if the organization has E5 licenses, or not. Verify the level of feature support for the case to determine if you should use PowerShell or Microsoft Graph to search and purge.
- For cases not configured for eDiscovery premium features, you can only use PowerShell to search and delete email messages. For E3 customers, cases created by cmdlets or the Microsoft Purview portal can only purge email by using PowerShell. You can purge up to 10 items per location.
- For cases configured for eDiscovery premium features, you can use PowerShell or Microsoft Graph to search and delete email messages. Cases configured by using Graph or the Microsoft Purview portal with premium features can only purge email and Teams messages by using Graph. You can purge up to 100 items per location.

    Important

    Don't use a combination of PowerShell and Microsoft Graph to purge email messages.
- After data is permanently deleted, it can't be recovered. Follow the guidance in this article carefully and validate the scope of the search before issuing the purge command. After you run the purge command, it can't be undone and email messages can't be restored.
- Search conditions such as identifier (including message ID), sensitivity label, and sensitive information type aren't supported for search and delete for non-premium enabled cases in eDiscovery. Using these conditions results in unexpected data loss.
- Run an export report to review all items that match your search criteria prior to the purge. By using the search and export experience in the Microsoft Purview portal and [exporting the results in report-only format](edisc-search-export), you can examine detailed metadata before deletion. This approach helps refine your search scope and ensures a more targeted and accurate purge.
- Don't use the search and purge workflow described in this article to delete chat messages or other content from Microsoft Teams. If the search that you create in Step 2 returns items from Microsoft Teams, follow the steps outlined in [Find and delete Microsoft Teams chat messages in eDiscovery](edisc-search-teams-data) to delete them.
- To create and run a search, you must be a member of the *eDiscovery Manager* role group or be assigned the *Compliance Search* role in the Microsoft Purview portal. To delete messages, you must be a member of the *Organization Management* role group or be assigned the *Search And Purge* role in the Microsoft Purview portal. For information about adding users to a role group, see [Assign eDiscovery permissions](edisc-permissions).

    Note

    The *Organization Management* role group exists in both Exchange Online and in the Microsoft Purview portal. These are separate role groups that give different permissions. Being a member of *Organization Management* in Exchange Online doesn't grant the required permissions to delete email messages. If you aren't assigned the *Search And Purge* role in the Microsoft Purview portal (either directly or through a role group such as *Organization Management*), you receive an error in Step 3 when you run the *New-ComplianceSearchAction* cmdlet with the message "A parameter can't be found that matches parameter name 'Purge'".
- You must use Security & Compliance PowerShell to delete messages. See Step 1: Connect to Security & Compliance PowerShell for instructions about how to connect.
- You can remove a maximum of 10 items per mailbox at one time. Because the capability to search for and remove messages is intended to be an event-response tool, this limit helps ensure that messages are quickly removed from mailboxes. This feature isn't intended to clean up user mailboxes.

Note

Search and purge isn't supported if a mailbox has a [litigation hold](/en-us/microsoft-365/admin/misc/create-litigation-hold-mac?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json). Only 10 items are removed from view of the user. These 10 items aren't permanently deleted, so these 10 items are the only ones processed.

- The maximum number of mailboxes in a content search that you can use to delete items by doing a search and purge action is 50,000. If the search (that you create in Create a search query to find the message to delete) searches more than 50,000 mailboxes, the purge action (that you create in Step 3) fails. Searching more than 50,000 mailboxes in a single search might typically happen when you configure the search to include all mailboxes in your organization. This restriction still applies even when fewer than 50,000 mailboxes contain items that match the search query. See the Frequently asked questions section for guidance about using search permissions filters to search for and purge items from more than 50,000 mailboxes.
- You can only use the procedure in this article to delete items in Exchange Online mailboxes and public folders. You can't use it to delete content from SharePoint or OneDrive sites.
- You can't delete email items in a review set in an eDiscovery case by using the procedures in this article. That's because items in a review set are stored in an Azure Storage location, and not in the live service. This means they're not returned by the content search that you create in Step 1. To delete items in a review set, you have to delete the eDiscovery case that contains the review set.

## Step 1: Connect to Security & Compliance PowerShell

First, connect to [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell) for your organization. For step-by-step instructions, see [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

Important

To use this cmdlet for purge actions in Security & Compliance PowerShell, you need to meet the following requirements:

- Use the Exchange Online PowerShell version 3.9.0 or later (August 2025). For more information, see [What's new in the Exchange Online PowerShell module](/en-us/powershell/exchange/whats-new-in-the-exo-module). Installing this version of the module might require you to uninstall previous versions of the module.
- Run the **Connect-IPPSSession** cmdlet with the [EnableSearchOnlySession](/en-us/powershell/module/exchangepowershell/connect-ippssession) switch.

## Step 2: Create a search query to find the message to delete

Next, create and run a search to find the message that you want to remove from mailboxes in your organization. You can create the search by using the [Microsoft Purview portal](https://purview.microsoft.com) or by running the **New-ComplianceSearch** and **Start-ComplianceSearch** cmdlets in Security & Compliance PowerShell. The messages that match the query for this search are deleted by running the **New-ComplianceSearchAction -Purge** command in Delete the message. For information about creating and configuring search queries, see the following articles:

- [Create a search query](edisc-search-query)
- [Use the condition builder](edisc-condition-builder)
- [New-ComplianceSearch](/en-us/powershell/module/exchange/New-ComplianceSearch)
- [Start-ComplianceSearch](/en-us/powershell/module/exchange/Start-ComplianceSearch)

Note

The content locations that you include in the search query can't include SharePoint or OneDrive sites. You can only include mailboxes and public folders in a search that is used for email messages. If the search includes sites, you receive an error when you run the **New-ComplianceSearchAction** cmdlet in Delete the message.

### Tips for finding messages to remove

The goal of the search query is to narrow the results to only the messages that you want to remove. Here are some tips:

- If you know the exact text or phrase used in the subject line of the message, use the **Subject** property in the search query.
- If you know the exact date or date range of the message, include the **Received** property in the search query.
- If you know who sent the message, include the **From** property in the search query.
- Preview the search results to verify that the search returns only the messages that you want to delete.
- Use the search estimate statistics, displayed in the details pane of the search in the Microsoft Purview portal or by using the [Get-ComplianceSearch](/en-us/powershell/module/exchange/get-compliancesearch) cmdlet, to get a count of the total number of results.

Here are two examples of queries to find suspicious email messages.

- This query returns messages that users received between April 13, 2024 and April 14, 2024 and that contain the words "action" and "required" in the subject line.

    ```powershell
    (Received:4/13/2024..4/14/2024) AND (Subject:'Action required')
    ```
- This query returns messages sent by user@contoso.com and that contain the exact phrase "Update your account information" in the subject line.

    ```powershell
    (From:user@contoso.com) AND (Subject:"Update your account information")
    ```

Here's an example of using a query to create and start a search by running the **New-ComplianceSearch** and **Start-ComplianceSearch** cmdlets to search all mailboxes in the organization:

```powershell
$Search=New-ComplianceSearch -Name "Remove Phishing Message" -ExchangeLocation All -ContentMatchQuery '(Received:4/13/2016..4/14/2016) AND (Subject:"Action required")'
Start-ComplianceSearch -Identity $Search.Identity
```

## Step 3: Delete the message

After you create and refine a search query to return the messages that you want to remove, run the **New-ComplianceSearchAction -Purge** command in Security & Compliance PowerShell to delete the message.

Important

If you use search in eDiscovery to validate the result and scope what you want to delete, rerun the search cmdlet to validate the search in eDiscovery. The search in eDiscovery isn't run in PowerShell, so the ItemCount is 0 and the JobEndTime isn't set. The search needs to be rerun using PowerShell and you should wait for the search to complete. Verify the results in the cmdlet return the same results before performing the purge.

You can soft-delete or hard-delete the message. A soft-deleted message is moved to a user's Recoverable Items folder and retained until the deleted item retention period expires. Hard-deleted messages are marked for permanent removal from the mailbox and are permanently removed the next time the mailbox is processed by the Managed Folder Assistant. If single item recovery is enabled for the mailbox, hard-deleted items are permanently removed after the deleted item retention period expires. If a mailbox is placed on hold, deleted messages are preserved until the hold duration for the item expires or until the hold is removed from the mailbox.

Note

Items from Microsoft Teams that are returned by the search query aren't deleted when you run the **New-ComplianceSearchAction -Purge** command.

To run the following commands to delete messages, make sure you're [connected to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

### Soft-delete messages

In the following example, the command soft-deletes the search results returned by a search query named "Remove Phishing Message".

```powershell
New-ComplianceSearchAction -SearchName "Remove Phishing Message" -Purge -PurgeType SoftDelete
```

### Hard-delete messages

Warning

Hard-deleted messages are marked for permanent removal and can't be recovered by the user. If single item recovery is enabled, hard-deleted items are permanently removed after the deleted item retention period expires. Verify your search scope before running this command.

To hard-delete the items returned by the "Remove Phishing Message" content search, run the following command:

```powershell
New-ComplianceSearchAction -SearchName "Remove Phishing Message" -Purge -PurgeType HardDelete
```

When you run the **New-ComplianceSearchAction -Purge -PurgeType SoftDelete** or **New-ComplianceSearchAction -Purge -PurgeType HardDelete** command, the search specified by the *SearchName* parameter is the search query that you created in Create a search query to find the message to delete.

For more information, see [New-ComplianceSearchAction](/en-us/powershell/module/exchange/New-ComplianceSearchAction).

## Frequently asked questions

The following questions address common issues with search and purge operations.

- **I followed the steps in this article for search, verify, and purge but it still doesn't delete items from a mailbox.**

    Sometimes the items matching the search query are more than 10 items (or 100 items if using Microsoft Graph) for a mailbox. If you run the purge by using the PowerShell cmdlet and only delete 10 items, or run the purge by using Microsoft Graph and only delete 100 items, this behavior is normal. Repeat the process multiple times if you want to delete more than 10 (or 100) items per mailbox. We strongly recommend against working around these limits by continually running the purge command. If you need to delete more data from a single location, see [Remediate malicious email delivered in Office 365](/en-us/microsoft-365/security/office-365-security/remediate-malicious-email-delivered-office-365?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) or [Zero-hour auto purge (ZAP) in Microsoft Defender for Office 365](/en-us/defender-office-365/zero-hour-auto-purge?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

    A mailbox on litigation hold can also prevent items from being deleted. If the export report associated to the search run in Step 2 (or done in eDiscovery) indicates items are in the *Recoverable Items* folder, this result means there are holds but the items are moved out of view. If you want to remove items from hold, we strongly recommend using [Priority Cleanup](priority-cleanup). Alternatively, you can release the hold and try purging again. Check the status of the hold by running the following cmdlet in Exchange PowerShell:

    ```powershell
    Get-Mailbox (or MailUser) | fl *Hold*,*Recovery*
    ```

Verify the following values in the cmdlet results:

- InPlaceHolds should be empty or only have values prefixed with –

    - DelayHold should be false
    - SingleItemRecovery should be false

    Check for tenant level policies by running the following cmdlet:

    ```powershell
    Get-OrganizationConfig | fl *Hold*
    ```

    If there are any tenant level policies, you must exclude each affected mailbox from the purge:
- Mailbox is on [delay hold](edisc-hold-types-mailboxes#manage-mailboxes-on-delay-hold).

    - Items of interest are still found after purge because they're moved to the *Recoverable items* folder.
- **How do I verify if items are under recoverable items folder?**

    To verify items are in the *Recoverable Items* folder, run an export report for the search and review the file path of the items in the CSV report to see if the items are in the *Recoverable items* folder. If yes, the *New-ComplianceSearch* cmdlet doesn't attempt to delete the item. If the CSV report indicates that the items are in the *Recoverable items* folder and the item's mailbox is archived, the mailbox is being resized. These backup items can't be deleted and eventually are removed automatically.
- **How do you get status on the search and remove operation?**

    Run the **Get-ComplianceSearchAction** to get the status on the delete operation. The object that is created when you run the **New-ComplianceSearchAction** cmdlet is named using this format: `<name of Content Search>_Purge`.
- **What happens after you delete a message?**

    A message that's deleted with the `New-ComplianceSearchAction -Purge -PurgeType HardDelete` command is moved to the Purges folder and can't be accessed by the user. After the message is moved to the Purges folder, the message is retained for the deleted item retention period if single item recovery is enabled for the mailbox. (In Microsoft 365, single item recovery is enabled by default when a new mailbox is created.) After the deleted item retention period expires, the message is marked for permanent deletion and is purged from Microsoft 365 the next time the mailbox is processed by the Managed Folder assistant.

    If you use the `New-ComplianceSearchAction -Purge -PurgeType SoftDelete` command, messages are moved to the Deletions folder in the user's Recoverable Items folder. It isn't immediately purged from Microsoft 365. The user can recover messages in the Deleted Items folder for the duration based on the deleted item retention period configured for the mailbox. After this retention period expires (or if user purges the message before it expires), the message is moved to the Purges folder and can no longer be accessed by the user. After the message reaches the Purges folder, the message is retained for the duration based on the deleted item retention period configured for the mailbox if single items recovery is enabled for the mailbox. (In Microsoft 365, single item recovery is enabled by default when a new mailbox is created.) After the deleted item retention period expires, the message is marked for permanent deletion and is purged from Microsoft 365 the next time that the mailbox is processed by the Managed Folder assistant.
- **What if I have to delete a message from more than 50,000 mailboxes?**

    You can perform a search and purge operation on a maximum of 50,000 mailboxes (even if less than 50,000 contain items that match the search query). If you need to do a search and purge operation on more than 50,000 mailboxes, consider creating temporary search permissions filters that reduce the number of mailboxes that would be searched to less than 50,000 mailboxes. For example, if your organization contains mailboxes in different departments, states, or a different country/region, you can create a mailbox search permissions filter based on one of those mailbox properties to search a subset of mailboxes in your organization. After you create the search permissions filter, you would create the search (described in Step 1) and then delete the message (described in Step 3). Then you can edit the search permissions filter to search for and purge messages in a different set of mailboxes. For more information about creating search permissions filters, see [Configure search permissions filtering in eDiscovery](edisc-search-permission-filtering).

Note

Each mailbox location including primary, archive, and any others are counted as individual locations for this limit.

- **Will unindexed items included in the search results be deleted?**

    No, the `New-ComplianceSearchAction -Purge` command doesn't delete unindexed items.
- **What happens if a message is deleted from a mailbox that is placed on Litigation Hold or assigned to a Microsoft 365 retention policy?**

    After the message is purged and moved to the Purges folder, the message is retained until the hold duration expires. If the hold duration is unlimited, then items are retained until the hold is removed or the hold duration is changed.
- **Why is the search and remove workflow divided among different Microsoft Purview portal role groups?**

    A person has to be a member of the *eDiscovery Manager* role group or be assigned the *Compliance Search management* role to search mailboxes. To delete messages, a person has to be a member of the *Organization Management* role group or be assigned the *Search And Purge management* role. This division makes it possible to control who can search mailboxes in the organization and who can delete messages.