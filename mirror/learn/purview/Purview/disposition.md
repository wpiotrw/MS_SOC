---
layout: Conceptual
title: Disposition of content | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/disposition
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-07-22T00:00:00.0000000Z
ai-usage: ai-assisted
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-records-management
ms.collection:
- purview-compliance
ms.custom:
- admindeeplinkMAC
- sfi-ga-nochange
- sfi-image-nochange
- msecd-doc-authoring-1017
search.appverid:
- MOE150
- MET150
description: Monitor and manage the disposal of content for when you use a disposition review or items marked as records are automatically deleted according to the settings you configured.
locale: en-us
document_id: 20c944a1-e58b-9ef0-e167-6a10b3a0a58e
document_version_independent_id: 20c944a1-e58b-9ef0-e167-6a10b3a0a58e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/disposition.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: disposition
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/disposition.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 078ffe10-20e3-23b9-ef55-aaf7641cdfca
---

# Disposition of content | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the **Disposition** page from **Records Management** in the Microsoft Purview portal to manage disposition reviews and view the metadata of [items marked as records](records-management#records) that have been automatically deleted at the end of their retention period.

## Prerequisites for viewing content dispositions

To manage disposition reviews and confirm that items marked as records have been deleted, you must have sufficient permissions and auditing must be enabled. Also be aware of any [limitations](retention-limits#maximum-numbers-for-disposition-review) for disposition.

### Permissions for disposition

To successfully access **Disposition** in the Microsoft Purview portal, users must have the **Disposition Management** role. This role is included in the **Records Management** default role group.

Note

By default, a global admin isn't granted the **Disposition Management** role.

To grant users just the permissions they need for disposition reviews without granting them permissions to view and configure other features for retention and records management, create a custom role group (for example, named "Disposition Reviewers") and grant this group the **Disposition Management** role.

For instructions to add users to the default roles or create your own role groups, see [Permissions in the Microsoft Purview portal](purview-permissions).

Additionally:

- To view the contents of items during the disposition process, add users to the **Content Explorer Content Viewer** role group. If users don't have the permissions from this role group, they can still select a disposition review action to complete the disposition review, but must do so without being able to view the item's contents from the mini-preview pane in the Microsoft Purview portal.
- By default, each person that accesses the **Disposition** page sees only items that they're assigned to review. For a records management administrator to see all items assigned to all users, and all retention labels that are configured for disposition review: From the Microsoft Purview portal, navigate to **Settings** &gt; **Solution settings** &gt; \*\*Records Management \*\* &gt; **Disposition** to select and then enable a mail-enabled security group that contains the administrator accounts. Permissions are then granted to the group members, but not the group owner.

    Microsoft 365 groups and security groups that aren't mail-enabled don't support this feature and don't display in the list to select. If you need to create a new mail-enabled security group, use the link to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) to create the new group.

    Important

    After you've enabled the group, you can't change it in the Microsoft Purview portal. See the next section for how to enable a different group by using PowerShell.
- The Records Management settings are visible only to record management administrators.

#### Enabling another security group for disposition

After you've enabled a security group for disposition from the **Records Management settings** in the Microsoft Purview portal, you can't disable this permission for the group or replace the selected group in the portal. However, you can enable another mail-enabled security group by using the [Enable-ComplianceTagStorage](/en-us/powershell/module/exchange/enable-compliancetagstorage) cmdlet.

For example:

```PowerShell
Enable-ComplianceTagStorage -RecordsManagementSecurityGroupEmail dispositionreviewers@contosoi.com
```

### Enable auditing

Make sure that auditing is enabled at least one day before the first disposition action. For more information, see [Search the audit log](audit-search).

## Disposition reviews

When content reaches the end of its retention period, there are several reasons why you might want to review that content and confirm whether it can be permanently deleted ("disposed"). For example, instead of deleting the content, you might need to:

- Suspend the deletion of relevant content for litigation or an audit.
- Assign a different retention period to the content, perhaps because the original retention settings were a temporary or provisional solution.
- Move the content from its existing location to an archive location, for example, if that content has research or historical value.

When a disposition review is triggered at the end of the retention period, your chosen reviewers receive an email notification that they have content to review. These reviewers can be individual users or members of a mail-enabled security group. When you use a mail-enabled security group, only group members and not the group owner receive the email notifications.

You can customize the notification email that reviewers receive, including instructions in different languages. For multi-language support, you must specify the translations yourself and this custom text is displayed to all reviewers irrespective of their locale.

Users receive an initial email notification per label at the end of the item's retention period, with a reminder per label once a week of all disposition reviews that they're assigned. They can click the link in the notification and reminder emails to go directly to the records management **Disposition** page in the Microsoft Purview portal to review the content and take an action. Alternately, the reviewers can navigate to this **Disposition** page in the Microsoft Purview portal. Then:

- Reviewers see only the disposition reviews that are assigned to them, whereas administrators who are added to the selected security group for records manager see all disposition reviews.
- Reviewers can add new users to the same disposition review. Note that this action does not automatically grant these added users the required permissions.
- For the disposition review process, a mini-review pane for each item shows a preview of the content if they have permissions to see it. If they don't have permissions, they can select the content link and request permissions. This mini-review pane also has tabs for additional information about the content:

    - **Details** to display indexed properties, where it's located, who created it and when, and who last modified it and when.
    - **History** that shows the history of any disposition review actions to date, with reviewer comments if available.

A disposition review can include content in Exchange mailboxes, SharePoint sites, and OneDrive accounts. Content pending a disposition review in those locations is permanently deleted only after a reviewer for the final stage of disposition chooses to permanently delete the content.

Note

A mailbox must have at least 10 MB data to support disposition reviews.

Administrators can see an overview of all pending dispositions in the **Overview** tab. Reviewers see only their items pending disposition.

Select the **View all pending dispositions**, to view them the **Disposition** page.

### Disposition timelines

Disposition involves three separate timelines:

| Timeline | Length | Notes |
| --- | --- | --- |
| Permanent deletion after approval | Within 15 days after the final (or only) reviewer selects **Approve disposal** | Applies when an item is marked as eligible for permanent deletion. |
| Auto-approval timeout (optional) | 7-365 days; default 14 days | If reviewers take no manual action, the item advances to the next stage or, in the final stage, is disposed. |
| Configuration change propagation | Up to 7 days | Applies when you turn auto-approval on or off, or change the number of days, like all retention label changes. |

### Workflow summary for a disposition review

Basic workflow for a disposition review, single stage:

1. The admin configures a retention label to start a disposition review at the end of the retention period.
2. The admin publishes the label and a user applies the label to one or more items, or the admin automatically applies the retention label to items.
3. At the end of the retention period for each item, the designated disposition reviewers receive an email to review the item for disposition.
4. One of the reviewers selects the link to review the item in the disposition page from the Microsoft Purview portal, and confirms that the item should be permanently deleted.

### Auto-approval for disposition

You can optionally specify a time period (7-365 days) for auto-approval. The default period if you select this option is 14 days.

If designated reviewers don't take manual action during this time period by using the standard disposition review process, the item automatically passes to the next review stage. If the item is in the final review stage, the item is automatically disposed with permanent deletion.

Important

If you configure this option and items are already pending disposition review, they automatically become auto-approved if they have already exceeded the number of days that you specified for auto-approval. The time period always starts from when the item is ready for disposition review and not from when you configure the option.

As with all retention label changes, allow up to 7 days if you turn on, turn off, or change the number of days for this option.

There's no new auditing event for auto-approval. Instead, use the details in the existing [Approved disposal](audit-log-activities#disposition-review-activities) auditing event to identify whether the item was manually approved or automatically approved by using this option.

### How to configure a retention label for disposition review

Triggering a disposition review at the end of the retention period is a configuration option that's available only with a retention label. Disposition review isn't available for a retention policy. For more information about these two retention solutions, see [Learn about retention policies and retention labels](retention).

From the **Choose what happens after the retention period** page for a retention label:

![Retention settings for a label that include disposition review.](media/disposition-review-option.png)

After you select the **Start a disposition review** option, select **+ Create stages and assign reviewers**. On the next page of the configuration, you'll specify how many consecutive stages of disposition you want and the disposition reviewers for each stage:

![Disposition review configuration settings for a retention label.](media/disposition-reviewers.png)

Optionally, select whether you want to use automatic-approval. If you use this option, specify the number of days reviewers have to take manual action before the item is automatically moved to the next disposition stage or automatically disposed.

Select **+ Add a stage**, and name your stage for identification purposes. Then specify the reviewers for that stage.

For the reviewers, specify up to 10 individual users or mail-enabled security groups. Microsoft 365 groups aren't supported for this option.

If you need more than one person to review an item at the end of its retention period, select **Add another stage** and repeat the configuration process for the number of stages that you need, with a maximum of five stages.

Within each individual stage of disposition, any of the users you specify for that stage are authorized to take the next action for the item at the end of its retention period. These users can also add other users to their disposition review stage.

Note

If you configured retention labels before multi-staged disposition review was available, you can upgrade your labels to support this feature: Edit the label and select **Edit stages and reviewers** on the **Choose what happens after the retention period** page.

During the configuration phase, for each stage specified, you can rename it, reorder it, or remove it by selecting **Edit stages and reviewers** that now displays for the **Start a disposition review** option. Then for each stage, you can select the Stage actions option (**...**):

![Stage actions for disposition reviews.](media/stage-actions-disposition-review.png)

However, you can't reorder or remove a stage after you've created the retention label. You'll see only the **Add a stage** and **Rename a stage** options available. You can still edit the reviewers.

After you've specified your reviewers, remember to grant them the **Disposition Management** role permission. For more information, see the Permissions for disposition section on this page.

### How to customize email messages for disposition review

Example default email notification sent to a reviewer:

![Email notification example with default text when an item is ready for disposition review.](media/disposition-review-email.png)

You can customize the email messages that are sent to disposition reviewers for the initial notification and then reminders.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Settings** &gt; **Solutions settings** &gt; **Records Management** &gt; **Disposition**.
2. From the **Email notifications for disposition reviews** section, select and specify whether you want to use just the default email message, or add your own text to the default message. Your custom text is added to the email instructions after the information about the retention label and before the next steps instructions.

    Text for all languages can be added, but formatting and images are unsupported. URLs and email addresses can be entered as text and depending on the email client, display as hyperlinks or unformatted text in the customized email.

    Example text to add:

    ```console
    If you need additional information, visit the helpdesk website (https://support.contoso.com) or send them an email (helpdesk@contoso.com).
    ```
3. Select **Save** to save any changes.

### Viewing and disposing of content

When a reviewer is notified by email that content is ready to review, they can click a link in the email that takes them directly to the **Disposition** page from **Records management** in the Microsoft Purview portal. There, the reviewers can see how many items for each retention label are waiting disposition with the **Type** displaying **Pending disposition**. They then select a retention label, and **Open in new window** to see all content with that label:

![Open in new window for disposition review.](media/open-in-new-window.png)

From the **Pending dispositions** page, they see all pending dispositions for that label. When one or more items are selected, they can use the mini-preview pane and the **Source**, **Details**, and **History** tab to inspect the content before taking action on it:

![Disposition options.](media/retention-disposition-options.png)

If you use the horizontal scroll bar, or close the min-review pane, you see more columns that include the expiry date and the name of the disposition review stage.

As you can see from the example shown, the actions supported are:

- **Approve disposal**:

    - When this action is selected for an interim stage of disposition review (you've configured multiple stages): The item moves to the next disposition stage.
    - When this action is selected for the final stage of disposition review, or there's only one stage of disposition: The item is marked as eligible for permanent deletion, which happens within 15 days.
- **Relabel**:

    - When this action is selected, the item exits the disposition review process for the original label. The item is then subject to the retention settings of the newly selected retention label.
- **Extend**:

    - When this action is selected, disposition review is effectively suspended until the end of the extended period and then disposition review is triggered again from the first stage.
- **Add reviewers**:

    - When this action is selected, the user is prompted to specify and add other users for review.

    Note

    This action doesn't automatically grant the required permissions to the users who are added. If they don't have these permissions, they can't participate in the disposition review.

Each action taken has a corresponding audit event in the [Disposition review activities](audit-log-activities#disposition-review-activities) auditing activities group.

During the disposition review process, unless you're using the optional setting of an auto-approval timeout period, the content never moves from its original location, and it's not marked for permanent deletion until this action is selected by a reviewer for the final or only disposition stage.

## Disposition of records

From the **Records management** main page &gt; **Disposition** tab, you can identify:

- Items deleted as a result of a disposition review.
- Items marked as a record or regulatory record but not marked for disposition review and automatically deleted at the end of their retention period.

These items indicate **Records Disposed** in the **Type** column. For example:

![Items that were disposed of without a disposition review.](media/records-disposed2.png)

Note

This functionality uses information from the [unified audit log](audit-search) and therefore requires auditing to be [enabled and searchable](audit-log-enable-disable) so the corresponding events are captured.

For auditing of deleted items that were marked as records or regulatory records, search for **Deleted file marked as a record** in the **File and page activities** category. This audit event is applicable to documents and emails.

## Filter and export the views

When you select a retention label from the **Disposition** page, the **Pending disposition** tab (if applicable) and the **Disposed items** tab let you filter the views to help you more easily find items.

For pending dispositions, the time range is based on the expiration date. For disposed items, the time range is based on the deletion date.

You can export information about the items in either view as a .csv file that you can then sort and manage using Excel.