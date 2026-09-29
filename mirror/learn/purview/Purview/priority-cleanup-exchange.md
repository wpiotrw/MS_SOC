---
layout: Conceptual
title: Use priority cleanup to expedite the permanent deletion of sensitive information from mailboxes | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: joagarwal
ms.date: 2025-12-03T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Use priority cleanup to expedite the permanent deletion of sensitive information from mailboxes, even if they have existing holds for retention or eDiscovery.
ms.subservice: purview-data-lifecycle-management
locale: en-us
document_id: 6245da81-a906-b604-4e77-ad38113cab80
document_version_independent_id: 6245da81-a906-b604-4e77-ad38113cab80
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/priority-cleanup-exchange.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: priority-cleanup-exchange
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/priority-cleanup-exchange.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 9d435151-a9a9-1ac8-1d83-1158f4bbaefe
---

# Use priority cleanup to expedite the permanent deletion of sensitive information from mailboxes | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

Priority cleanup is rolling out in preview and subject to change.

Although this feature requires additional permissions and multiple approvals, highly regulated organizations that use [Preservation Lock](retention#use-preservation-lock-to-restrict-changes-to-policies) might want the additional safeguard of turning off priority cleanup at the tenant level to ensure that their policies remain in compliance with required regulations.

Use the **Priority cleanup** feature under **Data Lifecycle Management** in Microsoft Purview when you need to permanently delete sensitive content from Exchange mailboxes, despite retention settings that retain the item or eDiscovery holds. Items still go through the [same deletion process with the same timings to ensure a compliant permanent deletion](retention-policies-exchange#how-retention-works-for-exchange), but there's no need to wait for the retention period to expire or the hold to be released. Priority cleanup might be implemented for security or privacy in response to an incident, or for compliance with regulatory requirements. For example:

- **Privacy request**: You receive a request to remove personal information about an employee who has left the organization and all mailboxes have a retention policy to retain items for two years.
- **Data spillage**: An employee accidentally emailed sensitive information about a future acquisition and you need to delete this information, despite any eDiscovery holds in progress in the organization.

Because the deletion is irreversible and can override existing holds and even [Preservation Lock](retention#use-preservation-lock-to-restrict-changes-to-policies), the process requires multiple approvals, specific roles, and is audited. After considering these safeguards, if your organization still has concerns about this capability, you can just continue to use [retention policies and retention labels](retention) to ensure a compliant deletion of content instead of using priority cleanup.

Under the covers, priority cleanup uses retention labels with auto-apply policies. However, you don't interact manually with these labels and policies, and they supersede the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) to achieve the required expedited deletion.

Note

If an item is subject to multiple priority cleanups, the newest takes priority.

Important exceptions for priority cleanup:

- You can't use priority cleanup for items that are marked as a [record or regulatory record](records-management#records).
- Although priority cleanup can override eDiscovery holds, the data might already be copied to an [eDiscovery review set](edisc-search-add-to-review-set) where it can't be deleted by priority cleanup. This data is automatically deleted when the entire eDiscovery case is deleted by an eDiscovery admin.

Similar to auto-apply retention labels, priority cleanup supports [simulation](apply-retention-labels-automatically#learn-about-simulation-mode), so you can check the returned samples in case the policy configuration needs any fine-tuning.

## Comparing priority cleanup for different workloads

Although you can use the priority cleanup feature for mailboxes and for files in SharePoint and OneDrive, the typical use cases are different. There are some other differences in behavior and configuration that are summarized in the following table. As a result of these differences, you can't create a cleanup policy for all three locations in same policy.

| Behavior or configuration | Exchange | SharePoint/OneDrive |
| --- | --- | --- |
| Typical use case: | Data spillage  Delete sensitive data for compliance requirements | Delete stale Teams meeting recordings and transcripts  Delete retained files in the Preservation Hold library |
| Typical policy use: | Rare | For Teams meeting recordings and transcripts: Continual  For the Preservation Hold library: After a user leaves the organization |
| Two-person rule: | Another priority cleanup admin is assigned in the policy to review items after the policy is turned on | Another priority cleanup admin is included in the policy configuration flow before the policy is turned on |
| Assign policy approvers: | - Priority cleanup admin  - eDiscovery admin  - Retention manager | - eDiscovery admin |
| Simulation required before running the policy: | No (but recommended) | Yes |
| Override Preservation Lock: | Yes | Only if the policy is configured for delete-only |

Additionally, the [required permissions for Exchange](priority-cleanup#permissions-for-priority-cleanup) are different from the [required permissions for SharePoint and OneDrive](priority-cleanup-onedrive-sharepoint#permissions-for-priority-cleanup).

## Prerequisites for priority cleanup

Make sure you can meet the prerequisites that must be in place before you can use priority cleanup to expedite the permanent deletion of sensitive data. These requirements include permissions and approvers.

Because of the built-in safeguards, the feature itself is enabled by default at the tenant level. However, priority cleanup can be turned off on the priority cleanup settings page. If you can't create new priority cleanup policies, see the instructions for turning off the feature to check the status and reverse the configuration.

Note

A mailbox must have at least 10-MB data to support priority cleanup.

### Permissions for priority cleanup

To successfully access and manage **Priority cleanup** in the Microsoft Purview portal, users must have the **Priority Cleanup Admin** role. This role is required to create and manage priority cleanup policies, enable or disable the feature, or approve items within the initial approval stage. This role is automatically added to the Organization Management role group but must be manually added to any other role group.

Alternatively, the **Priority Cleanup Viewer** role allows only the visibility of priority cleanup policies and settings without the ability to make changes or create new policies.

**Content Explorer List Viewer** and **Content Explorer Content Viewer** roles are required to view item content and details in simulation mode and approval stages.

Similar to [records management disposition](disposition), each person that accesses the **Priority cleanup** &gt; **Pending cleanups** page sees only items that they're assigned to approve. To monitor the end-to-end process of a priority cleanup, use auditing and the priority cleanup ID as a search term.

### Policy approvers

As a safeguard against accidental or malicious deletions, each item subject to priority cleanup always requires three other persons to approve the permanent deletion in addition to the person who created the priority cleanup policy. Approvers must be individual users. Mail-enabled security groups are not currently supported.

Three approvals are always required, irrespective of which type of hold is applied to the item:

- One priority cleanup admin approval.
- One retention manager approval.
- One eDiscovery admin approval.

#### Approver role requirements

The approver at each stage of the review process must have the correct roles assigned before the policy can be created.

| Reviewer | Required roles |
| --- | --- |
| Priority cleanup admins | - Priority Cleanup admin- Data Classification Content Viewer- Data Classification List Viewer- Disposition Management |
| Retention managers | - Retention Management- Data Classification Content Viewer- Data Classification List Viewer- Disposition Management |
| eDiscovery admins | - Search And Purge- Hold- Review- Data Classification Content Viewer- Data Classification List Viewer- Disposition Management |

Note

If the reviewer at any stage doesn't have the correct roles assigned in advance, policy creation fails with an error.

For instructions to add users to the default roles or create your own role groups, use the following guidance:

- [Permissions in the Microsoft Purview portal](purview-permissions)

Although you can specify multiple approvers for each stage, just one person from each stage is required to approve for their stage.

### Enable auditing

Make sure that auditing is enabled at least one day before you create and run the first priority cleanup policy. Auditing is also required to view simulation results if the policy is enabled in simulation mode. For more information, see [Search the audit log](audit-search).

## Limitations of priority cleanup

- Group mailboxes are supported via [adaptive scopes](/en-us/purview/purview-adaptive-scopes) only.
- For the KeyQL query, some properties and conditions supported by eDiscovery aren't supported by priority cleanup. These include SenderAuthor, SubjectTitle, (c:c), and (c:s).
- In simulation mode, the priority cleanup policy may incorrectly show email items marked as records and regulatory records. These items are not actually in scope for priority cleanup outside simulation mode.
- Unlike [disposition review for retention labels](disposition):

    - You can't customize the email notification
    - Approvers can't nominate additional approvers
    - There's no automatic approval after a specified period of time
- If an approver doesn't agree to permanently delete an identified item, they must assign an existing retention label (any configuration) to the item. Make sure your approvers know which retention labels are suitable for this action.
- Although you can delete a priority cleanup policy, if the approval process for it is complete, items might still be permanently deleted.

## Create a priority cleanup policy

Decide before you create your priority cleanup policy whether to make it **adaptive** or **static**. For more information, see [Adaptive or static policy scopes for retention](retention#adaptive-or-static-policy-scopes-for-retention). If you decide to use an adaptive policy, you must create one or more adaptive scopes before you create your priority cleanup policy, and then select them during the policy configuration. For instructions, see [Configuration information for adaptive scopes](purview-adaptive-scopes#configure-adaptive-scopes).

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Priority cleanup**, and then select **+ Create a priority cleanup**.

    If you don't see the **Priority cleanup** option, check your permissions.
2. Enter a name and description for this priority cleanup policy, and then select **Next**. The name is visible to end users, but the optional description is visible only to priority cleanup admins and the policy's specified approvers. This restriction means that any details you enter can be informative and specific, without worrying about unauthorized people seeing these details.
3. For **Choose the type of priority cleanup**, select **Adaptive** or **Static** then select **Next**.

    1. For Adaptive scope, add one or more adaptive scopes. For a user mailbox, add a user scope. For a group mailbox, add a Microsoft 365 Group scope. Then select one or more of the mailbox locations to match your scopes.
    2. For Static scope, select **Policy for Exchange Online** and then select Exchange Online location. Optionally, you can edit what mailboxes to include or exclude.

    To help you decide:

    - **All mailboxes are included**: Best when you're unsure where the content resides. It may take longer to apply the policy, but it's worth it if content might be in unknown mailboxes.
    - **Specific mailboxes**: Fastest option for a small, known set of mailboxes. Use to include or exclude up to 100 mailboxes confidently.
    - **User mailboxes by attributes**: You can't use a static scope if you want to use attributes to target user mailboxes by region, department, etc. Instead, go back in the policy configuration and choose to use adaptive scopes instead. However, avoid if the scope includes over 1 million mailboxes.
4. Select **Next**.
5. For the **Tell us what you're looking for** page, enter text into the KeyQL editor box to construct a query using Exchange email properties. You can refine your query by using search operators such as AND, OR, and NOT.

    For example, to find all content sent after February 2, 2024, with an attachment named ContosoEmployeeSalaries.xlsx: **AttachmentNames:ContosoEmployeeSalaries.xlsx AND sent&gt;=2024-02-02**

    For more information about the query syntax that uses Keyword Query Language (KeyQL), see [Keyword Query Language (KeyQL) syntax reference](/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference).

    This query-based policy uses the same search index as eDiscovery content search to identify content. For more information about the searchable properties that you can use for email, see [Finding content in Exchange Online](ediscovery-keyword-queries-and-search-conditions#finding-content-in-exchange-online).
6. For the **Choose when content should be deleted** page, choose whether to permanently delete the matched items as soon as possible or retain them for a specific period and then delete them. Most of the time, you'll select the first option so that you can delete the item as soon as possible. Use the alternative option only if the items should be retained for compliance reasons and you can't use a retention label for this purpose. For example, the item already has a retention label applied with a longer retention period.

    Note

    A priority cleanup policy overrides the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) that normally determine when an item should be retained or permanently deleted.
7. For the **Assign who'll approve what gets deleted** page, this is where you need to specify another priority cleanup approver, an approver for when an identified item has retention settings applied (such as a retention policy, retention label, or litigation hold policy), and an approver for when an identified item has one or more eDiscovery holds applied.

    - **Priority cleanup admins**: Must be assigned the Priority Cleanup Admin role and is the first-stage approver for all priority cleanups for this policy. This should be a different person to the user who created the priority cleanup policy, but isn't enforced.
    - **Retention managers**: Must be assigned the Retention Management role. Approval from specified users is required if the identified content is subject to one or more retention policies or Litigation holds.
    - **eDiscovery admins**: Must be assigned the eDiscovery Administrator role. Approval from specified users is required if the identified content is subject to one or more eDiscovery holds.
8. For the **Choose the policy mode** page, choose whether to run the policy first in simulation mode or turn it on, or neither for the time being.

    Running the policy in simulation mode delays permanent deletion but allows you to verify sample matches and refine the query. It also lets others review the results before approval, even if they're not designated approvers.
9. Specific to priority cleanup, you must acknowledge by selecting a checkbox that you understand how this policy can override eDiscovery holds and other applied retention settings.
10. On the **Your priority cleanup policy has been created** page, you see the **Cleanup ID** that's used to track and monitor this policy. Use the Copy function, or copy it later from the policy details so you can monitor the progress of this policy from auditing details.

If you chose to run the policy in simulation mode:

- You might need to wait a couple of hours for results, depending on the number of mailboxes to search.
- You can turn on the policy for up to seven days. After seven days, the simulation must be restarted.

If you turn on the policy, as with auto-apply retention label policies, it can take [up to seven days to apply the policy to items](apply-retention-labels-automatically#how-long-it-takes-for-retention-labels-to-take-effect) and trigger the approval process.

## Approval process for a priority cleanup policy

When the priority cleanup policy is turned on and items are identified, approvers for the policy are notified by email, with a reminder once a week. They can select the link in the notification and reminder emails to go directly to the **Data lifecycle management** &gt; **Priority cleanup** &gt; **Pending cleanups** page in the portal to review the content to approve. Alternately, the approvers can manually navigate to this page in the portal.

To implement the security control that uses the [two-person rule](https://en.wikipedia.org/wiki/Two-person_rule), each priority cleanup always requires another priority cleanup admin to approve the permanent deletion of identified items. Then if the items have retention settings applied, they require a next stage approval from retention admins. And finally, if the items are included in an eDiscovery hold, they also require another approval from an eDiscovery admin. When all the required approvals are complete, items are permanently deleted and cannot be restored by users, by admins, or by Microsoft.

On the **Pending cleanups** page, items identified by a priority cleanup policy are listed with a status of **Pending disposition** and an estimated count of how many items are identified. These might be different items, or the same item in multiple mailboxes.

When the approver selects one of the list items, the next page shows them the individual items with the item names, locations, and senders. When an item is selected, the preview pane displays the item's subject, source, details, and history. The history displays any priority cleanup approvals to date for that item, with approver comments if available.

After reviewing all the items, the approver can individually or multi-select them, and select **Approve disposal**. They must then acknowledge the action with an optional comment, and select **Apply**.

Alternatively, if the item shouldn't be permanently deleted as soon as possible, the approver must select **Relabel**, and select an existing retention label.

Items that are approved or relabeled are then moved to the **Disposed items** tab. Allow up to seven days for items to be permanently deleted.

### Export the views

An approver can use the **Export** option from the **Pending cleanups** and **Disposed items** pages to export information about the items in either view as a .csv file that they can then sort and manage with Excel.

## How to monitor priority cleanup

You can monitor the status of priority cleanups for each policy from **Data lifecycle management** &gt; **Priority cleanup**. For example, the status displays **In simulation**, or **Enabled (Pending)** that changes to **Enabled (Success)**.

Use the details of a policy to identify its cleanup ID, and paste this number as a keyword search string from the [auditing solution](audit-search#get-started-with-search). To use the date range, remember to specify the dates in UTC.

There are two auditing events specific to priority cleanup for mailboxes:

- Operation name of **PriorityCleanupTagApplied**: When an item is identified for priority cleanup, and if this resulted in removing an existing retention label.
- Operation name of **PriorityCleanupDelete**: The deletion of a mailbox item by priority cleanup.

Currently, these events don't have friendly names to select from the Microsoft Purview portal.

Other auditing events are the same as those used for [creating and configuring a retention label and auto-labeling policy](audit-log-activities#retention-policy-and-retention-label-activities), and [events for disposition review](audit-log-activities#disposition-review-activities).

## The end user experience for priority cleanup

Because priority cleanup doesn't use a soft-delete process, users see a **Retention:** message bar on their emails in Outlook when they're identified for priority cleanup. They also see the name of the priority cleanup policy, then **(-1 days)** to indicate that it should be deleted as soon as possible, and an estimated expiry day and time based on that -1 days.

For example, if your priority cleanup policy is named "Cleanup policy test":

**Retention: Cleanup policy test (-1 days) Expires: Thu 2/6/2024 AM**

Tip

If you prefer end users to not see the retention message, you can achieve this by first using [eDiscovery search and purge](ediscovery-data-spillage-search-and-purge) that soft-deletes items. When that completes, then apply the priority cleanup policy to permanently delete the soft deleted items.

After the final priority cleanup approval, the item silently disappears from Outlook.

## Turn off priority cleanup for the tenant

After considering the safeguards of additional permissions and multiple approvals, if your organization still has concerns about this capability, you can turn off the ability to create priority cleanup policies. When you turn off priority cleanup, you're turning it off for [SharePoint and OneDrive](priority-cleanup-onedrive-sharepoint) as well as for Exchange.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management**.
2. From the top right, select **Priority cleanup settings**.
3. From the **Configuration** page, turn off the control for priority cleanup, and select **Save**.

New priority cleanup policies can't be created until you turn on the control and select **Save** again.

If priority cleanup policies are already created when you turn off the control:

- Existing priority cleanup policies continue to function
- Existing priority cleanup policies can be deleted
- Existing priority cleanup policies can't be modified