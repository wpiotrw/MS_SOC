---
layout: Conceptual
title: Override holds to clean up files for Copilot and reclaim storage | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/priority-cleanup-onedrive-sharepoint
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: joagarwal
ms.date: 2025-11-17T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Use priority cleanup to override holds to clean up files that shouldn't be accessible to Copilot, and delete files in OneDrive to reclaim that storage, even if the files have existing holds for retention or eDiscovery.
ms.subservice: purview-data-lifecycle-management
locale: en-us
document_id: 5551b45d-7953-3da1-f014-1eb904fb35ba
document_version_independent_id: 5551b45d-7953-3da1-f014-1eb904fb35ba
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/priority-cleanup-onedrive-sharepoint.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: priority-cleanup-onedrive-sharepoint
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/priority-cleanup-onedrive-sharepoint.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 4e3e410c-9559-77a3-4b82-f1563fa9c8fb
---

# Override holds to clean up files for Copilot and reclaim storage | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the **Priority cleanup** feature under **Data Lifecycle Management** in Microsoft Purview when you need to override existing retention settings or eDiscovery holds to delete content from OneDrive and SharePoint. Despite the existing holds, items are moved to the second-stage Recycle Bin and from there, go through the [same processes with the same time periods](retention-policies-sharepoint#how-retention-works-for-sharepoint-and-onedrive) to ensure a compliant deletion process.

Although priority cleanup might be needed for security or privacy in response to an incident, or for compliance with regulatory requirements, typical use cases for SharePoint and OneDrive include the following;

- **Delete stale Teams meeting recordings and transcripts, turned on for Copilot recap**: The Copilot in Teams [recap feature](https://support.microsoft.com/office/recap-in-microsoft-teams-c2e3a0fe-504f-4b2c-bf85-504938f110ef) uses Teams meeting recordings and transcripts that might be [covered by a retention policy](retention-policies-sharepoint#whats-included-for-retention-and-deletion). These files are typically large and have little business value after 1-3 months. To reclaim the space from these files, or any other similarly large files that don't need to be retained as long as your retention policies, you can take action to remove them.

    Tip

    Most meeting recordings and transcripts are saved to OneDrive. However, recordings from channel meetings are stored in SharePoint. For more information, see [Use OneDrive and SharePoint to store meeting recordings](/en-us/MicrosoftTeams/tmr-meeting-recording-change).

    Priority cleanup lets you delete these files by overriding existing retention policies so you can better manage your storage requirements. Because these files are continually created, leave the priority cleanup policy running to automatically find and delete the stale files.
- **Delete labeled items in OneDrive's Preservation Hold library when a user leaves the organization**: When one or more items in a [Preservation Hold library have an unexpired retention period](retention-policies-sharepoint#how-retention-works-for-sharepoint-and-onedrive), the OneDrive site for the user can't be deleted. As a result, when users leave the organization, you might not be able to delete their OneDrive site until the longest retention period expires. Priority cleanup can delete these files instead of waiting for the expiration period to end, so you can then delete the site for the OneDrive account and reclaim that OneDrive storage space. Create a priority cleanup policy after a user has left the organization and their OneDrive account is blocked from deletion.

Because the deletion from priority cleanup can override existing holds and even [Preservation Lock](retention#use-preservation-lock-to-restrict-changes-to-policies) when the retention settings are for delete-only, the process requires multiple approvals, specific roles, and is audited. After considering these safeguards, if your organization still has concerns about this capability, you can just continue to use [retention policies and retention labels](retention) to ensure a compliant deletion of content instead of using priority cleanup.

Under the covers, priority cleanup uses retention labels with auto-apply policies. However, you don't interact manually with these labels and policies, and they supersede the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) so you don't need to wait for the longest retention period to expire.

Note

If an item is subject to multiple priority cleanups, the newest takes priority.

Important exceptions for priority cleanup:

- You can't use priority cleanup for items that are marked as a [record or regulatory record](records-management#records).
- Although priority cleanup can override eDiscovery holds, the data might already be copied to an [eDiscovery review set](edisc-search-add-to-review-set) where it can't be deleted by priority cleanup. This data is automatically deleted when the entire eDiscovery case is deleted by an eDiscovery admin.

Similar to auto-apply retention labels, priority cleanup supports [simulation](apply-retention-labels-automatically#learn-about-simulation-mode), to check the returned samples in case the policy configuration needs any fine-tuning. For SharePoint and OneDrive, you must run simulation at least one time, and for any change other than the policy description.

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

Make sure you can meet the prerequisites that must be in place before you can use priority cleanup to override existing holds for SharePoint and OneDrive. These requirements include permissions and approvers.

Because of the built-in safeguards, the feature itself is enabled by default at the tenant level. However, priority cleanup can be turned off on the priority cleanup settings page. If you can't create new priority cleanup policies, see the instructions for turning off the feature to check the status and reverse the configuration.

### Permissions for priority cleanup

To successfully access and manage **Priority cleanup** in the Microsoft Purview portal, you must have the **Priority Cleanup Admin** role. For SharePoint and OneDrive, this role is required to create and manage priority cleanup policies, and enable or disable the feature. This role is automatically added to the Organization Management role group but must be manually added to any other role group.

Alternatively, the **Priority Cleanup Viewer** role allows only the visibility of priority cleanup policies and settings without the ability to make changes or create new policies.

**Content Explorer List Viewer** and **Content Explorer Content Viewer** roles are required to view item content and details in simulation mode, and approval stages.

Similar to [records management disposition](disposition), each person that accesses the **Priority cleanup** &gt; **Pending cleanups** page sees only items that they're assigned to approve. To monitor the end-to-end process of a priority cleanup, use auditing and the priority cleanup ID as a search term.

### Policy approvers

As a safeguard against accidental or malicious deletions, each item subject to priority cleanup always requires at least one other person to approve the deletion in addition to the person who created the priority cleanup policy. Approvers must be individual users. Mail-enabled security groups aren't currently supported.

- Priority cleanup admin approval is required for all policies.
- If an item is also subject to one or more eDiscovery holds, eDiscovery admin approval is also required.
- Separate approval from a retention admin isn't required to override retention settings.

#### Approver role requirements

The approver at each stage of the review process must have the correct roles assigned.

| Reviewer | Required roles |
| --- | --- |
| Priority cleanup admins | - Priority Cleanup Admin- Data Classification Content Viewer- Data Classification List Viewer- Retention Management |
| eDiscovery admins | - Search And Purge- Hold- Review- Data Classification Content Viewer- Data Classification List Viewer- Disposition Management |

Note

If the reviewer for eDiscovery admin doesn't have the correct roles assigned in advance, policy creation fails with an error.

For instructions to add users to the default roles or create your own role groups, use the following guidance:

- [Permissions in the Microsoft Purview portal](purview-permissions)

Although you can specify multiple approvers for eDiscovery, just one person is required to approve overriding eDiscovery holds.

### Enable auditing

Make sure that auditing is enabled at least one day before you create and run the first priority cleanup policy. Auditing is also required to view simulation results. For more information, see [Search the audit log](audit-search).

## Limitations of priority cleanup

- In simulation mode, items under preservation lock where the retention settings are configured for delete-only may show up. These items are not actually in scope for priority cleanup outside simulation mode.
- Unlike [disposition review for retention labels](disposition):

    - You can't customize the email notification
    - Approvers can't nominate additional approvers
    - There's no automatic approval after a specified period of time
- If an approver doesn't agree to delete an identified item, they must assign an existing retention label (any configuration) to the item. Make sure your approvers know which retention labels are suitable for this action.
- Although you can delete a priority cleanup policy, if the approval process for it is complete, items might still be deleted.

## Create a priority cleanup policy

Decide before you create your priority cleanup policy whether to make it **adaptive** or **static**. For more information, see [Adaptive or static policy scopes for retention](retention#adaptive-or-static-policy-scopes-for-retention). If you decide to use an adaptive policy, you must have one or more adaptive scopes before you create your priority cleanup policy so that you can select them during the policy configuration. For instructions, see [Configuration information for adaptive scopes](purview-adaptive-scopes#configure-adaptive-scopes).

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Priority cleanup**, and then select **+ Create a priority cleanup**.

    If you don't see the **Priority cleanup** option, check your permissions.
2. Enter a name and description for this priority cleanup policy, and then select **Next**. The name is visible to end users, but the optional description is visible only to priority cleanup admins and the policy's specified approvers. This restriction means that any details you enter can be informative and specific, without worrying about unauthorized people seeing these details.
3. For **Choose the type of priority cleanup**, select **Adaptive** or **Static** then select **Next**.

    1. For Adaptive scope, add one or more adaptive scopes. For OneDrive accounts, add a scope for users. For sites, add a scope for SharePoint sites or Microsoft 365 Groups, as needed. Then select one or more of the locations to match your scopes.
    2. For Static scope, select **Policy for SharePoint/OneDrive** and then select one or more of the locations for sites and OneDrive accounts. Optionally, you can edit what sites and user accounts to include or exclude.
4. Select **Next**.
5. For the **Tell us what you're looking for** page, enter text into the KeyQL editor box to construct a query to target specific files. You can refine your query by using search operators such as AND, OR, and NOT.

    For example, to find Teams meeting recordings and transcripts, use **ProgID:Media AND ProgID:Meeting**. For files in a Preservation Hold library, use **ParentLink:PreservationHoldLibrary**.

    For more information about the query syntax that uses Keyword Query Language (KeyQL), see [Keyword Query Language (KeyQL) syntax reference](/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference) and [Automatically apply a retention label to retain or delete content](apply-retention-labels-automatically).

    This query-based policy uses the same search index as eDiscovery content search to identify content.
6. For the **Choose when content should be deleted** page, choose whether to delete the matched items as soon as possible or retain them for a specific period and then delete them. Most of the time, you'll select the first option so that you can delete the item as soon as possible. Use the alternative option only if the items should be retained for compliance reasons and you can't use a retention label for this purpose. For example, the item already has a retention label applied with a longer retention period.

    Note

    A priority cleanup policy overrides the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) that normally determine when an item should be retained or deleted.
7. For the **Assign who'll approve what gets deleted** page, this is where you need to specify an approver for when an identified item has one or more eDiscovery holds applied:

    - **eDiscovery admins**: Must be assigned the eDiscovery Administrator role. Approval from specified users is required if the identified content is subject to one or more eDiscovery holds.
8. For the **Choose the policy mode** page, choose whether to run the policy first in simulation mode or leave it turned off.

    Running the policy in simulation mode is required to initially set up priority cleanup for SharePoint and OneDrive locations. Simulation mode lets you verify that sample results match your query, so you can fine-tune it before approval. It also facilitates review with another priority cleanup admin.
9. Specific to priority cleanup, you must acknowledge by selecting a checkbox that you understand how this policy can override eDiscovery holds and other applied retention settings. Select **Submit**
10. On the **Your priority cleanup policy has been created** page, you see the **Cleanup ID** that's used to track and monitor this policy. Use the Copy function, or copy it later from the policy details so you can monitor the progress of this policy from auditing details.
11. Once simulation results are available, ask a second priority cleanup admin to review the results from the **Priority Cleanup Policies** page. They should select the policy from the list, and then select **View simulation details**.
12. If the results are satisfactory, this second priority cleanup admin can select **Turn on policy**. However, if the policy needs reconfiguration to add or remove items, they should make those edits and rerun simulation, and view results again. They should continue to make edits and rerun simulation each time. When the results are satisfactory, you, as the first priority cleanup admin, can turn on the policy.

    Important

    The last person to edit the policy can't also turn it on. We recommend that only one priority admin edits the policy after it's first created. So as a variation to step 12, the original priority cleanup admin could edit the policy and rerun simulation, and the second priority cleanup admin turns it on.

The Locations box shows scanned areas, and sample counts may differ from match counts. After the policy is turned on, wait for the “Enabled (Success)” status, [which may take up to seven days](apply-retention-labels-automatically#how-long-it-takes-for-retention-labels-to-take-effect).

## Approval process for a priority cleanup policy

When the priority cleanup policy is turned on and items are identified that are subject to eDiscovery, your assigned eDiscovery approvers for the policy are notified by email, with a reminder once a week. They can select the link in the notification and reminder emails to go directly to the **Data lifecycle management** &gt; **Priority cleanup** &gt; **Pending cleanups** page in the portal to review the content to approve. Alternately, the approvers can manually navigate to this page in the portal.

When any required approvals are complete, items are moved to the [second-stage Recycle Bin](retention-policies-sharepoint#how-retention-works-for-sharepoint-and-onedrive).

On the **Pending cleanups** page, items identified by a priority cleanup policy are listed with a status of **Pending disposition** and an estimated count of how many items are identified. These might be different items, or the same item in multiple locations.

When the approver selects one of the list items, the next page shows them the individual items with the item names, locations, and senders. When an item is selected, the preview pane displays the item's subject, source, details, and history. The history displays any priority cleanup approvals to date for that item, with approver comments if available.

After reviewing all the items, the approver can individually or multi-select them, and select **Approve disposal**. They must then acknowledge the action with an optional comment, and select **Apply**.

Alternatively, if the item shouldn't be deleted, the approver must select **Relabel**, and select an existing retention label.

Items that are approved or relabeled are then moved to the **Disposed items** tab. Allow up to seven days for items to be deleted.

### Export the views

An approver can use the **Export** option from the **Pending cleanups** and **Disposed items** pages to export information about the items in either view as a .csv file that they can then sort and manage with Excel.

## How to monitor priority cleanup

You can monitor the status of priority cleanups for each policy from **Data lifecycle management** &gt; **Priority cleanup**. For example, the status displays **In simulation**, or **Enabled (Pending)** that changes to **Enabled (Success)**.

Use the details of a policy to identify its cleanup ID, and paste this number as a keyword search string from the [auditing solution](audit-search#get-started-with-search). To use the date range, remember to specify the dates in UTC.

There are two auditing events specific to priority cleanup for SharePoint and OneDrive:

- Operation name of **PriorityCleanupTagApplied**: When an item is identified for priority cleanup, and if this resulted in removing an existing retention label.
- Operation name of **PriorityCleanupFileRecycled**: The deletion of an item in SharePoint or OneDrive by priority cleanup.

Currently, these events don't have friendly names to select from the Microsoft Purview portal.

Other auditing events are the same as those used for [creating and configuring a retention label and auto-labeling policy](audit-log-activities#retention-policy-and-retention-label-activities), and [events for disposition review](audit-log-activities#disposition-review-activities).

## The end user experience for priority cleanup

Files that are identified for priority cleanup display to users as an applied retention label that has the same name as the priority cleanup policy.

If users remove or replace this retention label, it will be automatically reapplied by the policy.

## Turn off priority cleanup for the tenant

After considering the safeguards of additional permissions and multiple approvals, if your organization still has concerns about this capability, you can turn off the ability to create priority cleanup policies. When you turn off priority cleanup, you're turning it off for [Exchange](priority-cleanup-exchange) as well as for SharePoint and OneDrive.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management**.
2. From the top right, select **Priority cleanup settings**.
3. From the **Configuration** page, turn off the control for priority cleanup, and select **Save**.

New priority cleanup policies can't be created until you turn on the control and select **Save** again.

If priority cleanup policies are already created when you turn off the control:

- Existing priority cleanup policies continue to function
- Existing priority cleanup policies can be deleted
- Existing priority cleanup policies can't be modified