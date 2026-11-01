---
layout: Conceptual
title: Learn about retention for Exchange | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/retention-policies-exchange
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2024-09-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- purview-compliance
- m365copilot
- SPO_Content
search.appverid:
- MOE150
- MET150
description: Learn how Microsoft 365 retention works for Exchange, using retention policies and retention labels to manage the automatic retention or deletion of data for your organization.
locale: en-us
document_id: 7b83fc05-ccd2-3120-bc91-0470d63cc93e
document_version_independent_id: 7b83fc05-ccd2-3120-bc91-0470d63cc93e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/retention-policies-exchange.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: retention-policies-exchange
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/retention-policies-exchange.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5b0c3dac-d268-d141-8f5e-109c9d0308d0
---

# Learn about retention for Exchange | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

The information in this article supplements [Learn about retention](retention) because it has information that's specific to Exchange. For other workloads, see:

- [Learn about retention for SharePoint and OneDrive](retention-policies-sharepoint)
- [Learn about retention for Microsoft Teams](retention-policies-teams)
- [Learn about retention for Viva Engage](retention-policies-viva-engage)
- [Learn about retention for Copilot](retention-policies-copilot)

## What's included for retention and deletion

The following Exchange items from user mailboxes and shared mailboxes can be retained and deleted by using retention policies and retention labels: Mail messages (includes received messages, drafts, sent messages) with any attachments, tasks when they have an end date, and notes.

Calendar items that have an end date are supported for retention policies but aren't supported for retention labels.

Public folders are supported for retention policies but aren't supported for retention labels.

Contacts, and any tasks and calendar items that don't have an end date are not supported.

Other items stored in a mailbox, such as Skype and Teams messages, aren't included in retention policies or labels for Exchange. These items have their own retention policies.

Mailboxes must have at least 10 MB of data before retention settings will apply to them, and retention labels can be published to them.

## How retention works for Exchange

Both a mailbox and a public folder use the [Recoverable Items folder](/en-us/exchange/security-and-compliance/recoverable-items-folder/recoverable-items-folder) to retain items. Only people who have been assigned eDiscovery permissions can view items in another user's Recoverable Items folder.

When a user deletes a message in a folder other than the Deleted Items folder, by default, the message moves to the Deleted Items folder. However, a user can soft delete an item (Shift+Delete) in any folder, which bypasses the Deleted Items folder and moves the item directly to the Recoverable Items folder.

When you apply retention settings to Exchange data, a timer job periodically evaluates items in the Recoverable Items folder. If an item doesn't match the rules of at least one retention policy or retention label to retain the item, it is permanently deleted (also called hard deleted) from the Recoverable Items folder. Items configured for [disposition review](disposition) are never permanently deleted from the Recoverable Items folder until the disposition is confirmed.

Note

Because of the [first principle of retention](retention#the-principles-of-retention-or-what-takes-precedence), permanent deletion is always suspended if the same item must be retained because of another retention policy or retention label, or it is under eDiscovery holds for legal or investigative reasons.

The timer job can take up to seven days to run and the Exchange location must contain at least 10 MB.

When a user attempts to change properties of a mailbox item—such as the subject, body, attachments, senders and recipients, or date sent or received for a message—a copy of the original item is saved to the Recoverable Items folder before the change is committed. This action happens for each subsequent change. At the end of the retention period, copies in the Recoverable Items folder are permanently deleted.

After retention settings are applied to Exchange content, the paths the content takes depend on whether the retention settings are to retain and delete, to retain only, or delete only.

When the retention settings are to retain and delete:

![Diagram of retention flow in email and public folders.](media/88f174cc-bbf4-4305-93d7-0515f496c8f9.png)

1. **If the item is modified or permanently deleted** by the user (either SHIFT+DELETE or deleted from Deleted Items) during the retention period: The item is moved (or copied, in the case of edit) to the Recoverable Items folder. There, a timer job runs periodically and identifies items whose retention period has expired, and these items are permanently deleted within 14 days of the end of the retention period. Note that 14 days is the default setting, but it can be configured up to 30 days.
2. **If the item is not modified or deleted** during the retention period: The same process runs periodically on all folders in the mailbox and identifies items whose retention period has expired, and these items are permanently deleted within 14 days of the end of the retention period. Note that 14 days is the default setting, but it can be configured up to 30 days.

When the retention settings are retain-only, or delete-only, the contents paths are variations of retain and delete:

### Content paths for retain-only retention settings

1. **If the item is modified or deleted** during the retention period: A copy of the original item is created in the Recoverable Items folder and retained until the end of the retention period, when the copy in the Recoverable Items folder is permanently deleted within 14 days after the item expires.
2. **If the item is not modified or deleted** during the retention period: Nothing happens before and after the retention period; the item remains in its original location.

### Content paths for delete-only retention settings

1. **If the item is not deleted** during the configured period: At the end of the configured period in the retention policy, the item is moved to the Recoverable Items folder.
2. **If the item is deleted** during the configured period: The item is immediately moved to the Recoverable Items folder. If a user deletes the item from there or empties the Recoverable Items folder, the item is permanently deleted. Otherwise, the item is permanently deleted after being in the Recoverable Items folder for 14 days.

## User notification of expiry date

Retention policies for Exchange, unlike retention policies for the other Microsoft 365 workloads, have a user presence by displaying at the top of each email message the name of the retention policy that has the shortest expiry date for the item, and the calculated expiry date for that item. Users don't see this notification if the retention policy doesn't delete items (retain-only).

If a retention label is applied to an email message, the name of that label and corresponding expiry date is always displayed, and will replace the name and date from any retention policy applied to the mailbox.

Remember, in this context, the expiry date for when an email will be deleted is when users can expect the email message to automatically move to the Recoverable Items folder (if not already there). Emails in the Recoverable Items folder will not be permanently deleted but remain there for compliance purposes if they are subject to any retention settings to retain it, or they are under an eDiscovery hold for legal or investigative reasons.

## When a user leaves the organization

If a user leaves your organization and the user's mailbox is included in a policy for retention, the mailbox becomes an inactive mailbox when the user's Microsoft 365 account is deleted. The contents of an inactive mailbox are still subject to any retention policy that was placed on the mailbox before it was made inactive, and the contents are available to an eDiscovery search. For more information, see [Inactive mailboxes in Exchange Online](inactive-mailboxes-in-office-365).

When the retention settings no longer apply because the data is permanently deleted or the retention period has expired, the Exchange admin can now [delete the inactive mailbox](delete-an-inactive-mailbox). In this scenario, the inactive mailbox isn't automatically deleted.

## Configuration guidance

If you're new to configuring retention in Microsoft 365, see [Get started with data lifecycle management](get-started-with-data-lifecycle-management).

If you're ready to configure a retention policy or retention label for Exchange, see the following instructions:

- [Create and configure retention policies](create-retention-policies)
- [Publish retention labels and apply them in apps](create-apply-retention-labels)
- [Apply a retention label to content automatically](apply-retention-labels-automatically)