---
layout: Conceptual
title: Permanently delete files with Microsoft Purview Priority Cleanup | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/priority-cleanup-permanent-deletion
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
author: prateekbhamri
ms.author: pbhamri
manager: laurawi
ms.reviewer: vanilc
ms.date: 2026-11-23T00:00:00.0000000Z
ai-usage: ai-generated
audience: Admin
ms.topic: how-to
ms.service: purview
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Permanently delete targeted SharePoint and OneDrive files with Microsoft Purview Priority Cleanup after required review and approval.
ms.subservice: purview-data-lifecycle-management
ms.custom: msecd-doc-authoring-1032
locale: en-us
document_id: 855e9999-aef8-3de2-a9a7-10f9abba1cc1
document_version_independent_id: 855e9999-aef8-3de2-a9a7-10f9abba1cc1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/priority-cleanup-permanent-deletion.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: priority-cleanup-permanent-deletion
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/priority-cleanup-permanent-deletion.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: d64c5ea3-b33f-ced5-68f3-1fffbaf6a34a
---

# Permanently delete files with Microsoft Purview Priority Cleanup | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use Microsoft Purview Priority Cleanup to permanently delete targeted files from SharePoint and OneDrive after the required review and approval. This option bypasses the SharePoint and OneDrive recycle bins. After deletion, the content is no longer discoverable in SharePoint search, Microsoft 365 Copilot, or eDiscovery.

Permanent deletion is an additional option for a Priority Cleanup policy. Use the standard Priority Cleanup workflow when you want identified items to move to the second-stage Recycle Bin.

Before you begin, review the required roles, approvers, auditing, and simulation requirements.

## Prerequisites

Before you configure permanent deletion:

- Review the prerequisites, permissions, approver requirements, and simulation process in [Override holds to clean up files for Copilot and reclaim storage](priority-cleanup-onedrive-sharepoint).
- Assign the **Priority Cleanup Admin** role to the administrator who creates and manages the policy.
- Assign the required roles to each approver before policy creation.
- Enable auditing at least one day before you create and run the first Priority Cleanup policy.
- Confirm that the permanent deletion option is available in your tenant. Public preview rollout begins on August 24, 2026.

Important

Permanent deletion can override retention settings or eDiscovery holds. Deleting items subject to legal holds requires explicit administrator approval for disposition. Items already copied to an eDiscovery review set aren't deleted by Priority Cleanup.

## Understand permanent deletion and recovery limitations

When an administrator selects **Delete data permanently**, they request permanent deletion of the targeted SharePoint and OneDrive content. Deleted content bypasses the recycle bins and isn't recoverable under ordinary circumstances. Review the consequences before you configure and approve permanent deletion.

After permanent deletion, Microsoft can retain a protected copy of the deleted content for up to 90 days. This copy is kept solely to handle exceptional privacy or security incidents involving permanent deletion. Customers, including users and administrators, can't access the copy. The copy isn't available through SharePoint search or eDiscovery.

In an exceptional scenario, customers can submit a support ticket to request recovery. Recovery is subject to Microsoft review and approval and is attempted only on a best-effort basis. Recovery isn't guaranteed. The temporary retention of deleted content doesn't provide a customer-accessible recovery option.

For general Microsoft 365 data-handling policies, see [Data retention, deletion, and destruction in Microsoft 365](/en-us/compliance/assurance/assurance-data-retention-deletion-and-destruction-overview).

This recovery information applies to SharePoint and OneDrive. For mailbox cleanup, see [Use priority cleanup to expedite the permanent deletion of sensitive information from mailboxes](priority-cleanup-exchange).

## Configure permanent deletion

Create a Priority Cleanup policy and explicitly select the permanent deletion option.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) and go to **Solutions** &gt; **Data Lifecycle Management** &gt; **Priority cleanup**.
2. Select **+ Create a priority cleanup**.
3. Enter the policy name and description, choose an adaptive or static scope, select the SharePoint or OneDrive locations, and define the query for the targeted files.
4. On the **Choose what to do with the content** page, select **Delete data permanently**.

    [![Screenshot of Microsoft Purview Priority Cleanup policy settings with Delete data permanently selected.](media/priority-cleanup-permanent-deletion/delete-data-permanently.png)](media/priority-cleanup-permanent-deletion/delete-data-permanently.png#lightbox)
5. Choose whether to delete matched items as soon as possible or prevent deletion until a set time.
6. Assign the required approvers.
7. Run the policy in simulation mode and review the returned samples.
8. After the simulation results are satisfactory, have a second Priority Cleanup admin review the results and turn on the policy.

Important

The last person to edit the policy can't also turn it on.

## Review and approve permanent deletion

Required approvers review identified items before permanent deletion occurs. Items subject to legal holds require explicit administrator approval for disposition.

1. In the Microsoft Purview portal, go to **Data Lifecycle Management** &gt; **Priority cleanup** &gt; **Pending cleanups**.
2. Select the cleanup and review the identified items, their locations, and their history.
3. Select the items to delete, and then select **Approve disposal**.
4. Acknowledge the action, optionally add a comment, and then select **Apply**.

After all required approvals are complete, the selected items bypass the recycle bins and are permanently deleted. The deleted content is no longer discoverable in SharePoint search, Microsoft 365 Copilot, or eDiscovery.

If an item shouldn't be deleted, select **Relabel**, and then assign an existing retention label.

## Monitor permanent deletion

Use the cleanup ID and auditing to monitor the policy and deletion activity.

1. Go to **Data Lifecycle Management** &gt; **Priority cleanup** and open the policy details.
2. Copy the cleanup ID.
3. In the [auditing solution](audit-search#get-started-with-search), use the cleanup ID as the keyword search string.
4. Check for the **PriorityCleanupFileDeleted** operation, which indicates that Priority Cleanup permanently deleted an item.