---
layout: Conceptual
title: Use sharing auditing in the audit log | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-sharing
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use sharing auditing in the Microsoft 365 audit log to track and manage resources shared with external users. Improve security and compliance today.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-audit
search.appverid:
- SPO160
- MOE150
- BCS160
- MET150
ms.collection:
- purview-compliance
- audit
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: bb197b28-0954-6930-39c3-47aa829f28a3
document_version_independent_id: bb197b28-0954-6930-39c3-47aa829f28a3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-sharing.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-sharing
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-sharing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/f9be14f8-8c50-42e5-902f-9be1b3f4de11
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/ffd919fc-9768-405d-a372-71b0f52e07cb
platformId: 5c6a7162-df19-9d43-c84c-3189393a58ce
---

# Use sharing auditing in the audit log | Microsoft Learn

Sharing is a key activity in SharePoint Online and OneDrive for Business, and organizations widely use it. Administrators can use sharing auditing in the audit log to determine how sharing is used in their organization.

## SharePoint sharing schema reference

Sharing events (not including events related to sharing policy and sharing links) differ from file- and folder-related events in one primary way: one user performs an action that affects another user. For example, when a resource User A gives User B access to a file. In this example, User A is the *acting user* and User B is the *target user*. In the SharePoint File schema, the acting user's action only affects the file itself. When User A opens a file, the only information needed in the **FileAccessed** event is the acting user. To address this difference, there's a separate schema, called the *SharePoint Sharing schema* that captures more information about sharing events. This schema ensures that administrators have visibility into who shared a resource and the user the resource was shared with.

The Sharing schema provides two additional fields in an audit record related to sharing events:

- **TargetUserOrGroupType:** Identifies whether the target user or group is a Member, Guest, SharePointGroup, SecurityGroup, or Partner.
- **TargetUserOrGroupName:** Stores the UPN or name of the target user or group that a resource was shared with (User B in the previous example).

These two fields, in addition to other properties from the audit log schema such as User, Operation, and Date tell the full story about *which* user shared *what* resource with *whom* and *when*.

Another schema property is important to the sharing story. When you export audit log search results, the **AuditData** column in the exported CSV file stores information about sharing events. For example, when a user shares a site with another user, sharing the site adds the target user to a SharePoint group. The **AuditData** column captures this information to provide context for administrators. To parse the **AuditData** column into individual properties, use the JSON transform feature in the Power Query Editor in Excel as described in Use the PowerQuery Editor to format the exported audit log.

## SharePoint sharing events

Sharing occurs when a user (the *acting* user) shares a resource with another user (the *target* user). Audit records related to sharing a resource with an external user (a user who is outside of your organization and doesn't have a guest account in your organization's Microsoft Entra ID) are identified by the following events, which the audit log records:

- **SharingInvitationCreated:** A user in your organization tries to share a resource (likely a site) with an external user. This event results in an external sharing invitation sent to the target user. The invitation grants no access to the resource at this point.
- **SharingInvitationAccepted:** The external user accepts the sharing invitation sent by the acting user and now has access to the resource.
- **AnonymousLinkCreated:** An anonymous link (also called an "Anyone" link) is created for a resource. Because an anonymous link can be created and then copied, it's reasonable to assume that any document that has an anonymous link is shared with a target user.
- **AnonymousLinkUsed:** This event is logged when an anonymous link is used to access a resource.
- **SecureLinkCreated:** A user creates a "specific people link" to share a resource with a specific person. This target user might be someone who is external to your organization. The person that the resource is shared with is identified in the audit record for the **AddedToSecureLink** event. The time stamps for these two events are nearly identical.
- **AddedToSecureLink:** A user is added to a specific people link. Use the **TargetUserOrGroupName** field in this event to identify the user added to the corresponding specific people link. This target user might be someone who is external to your organization.

## How sharing auditing works

When a user (the acting user) wants to share a resource with another user (the target user), SharePoint (or OneDrive for Business) first checks if the email address of the target user is already associated with a user account in the organization's directory. If the target user is in the directory (and has a corresponding guest user account), SharePoint takes the following actions:

- Immediately assigns the target user permissions to access the resource by adding the target user to the appropriate SharePoint group, and logs an **AddedToGroup** event.
- Sends a sharing notification to the email address of the target user.
- Logs a **SharingSet** event. This event has a friendly name of "Shared file, folder, or site" and appears under **Sharing and access request activities** in the activities picker of the audit log search tool.

If a user account for the target user isn't in the directory, SharePoint takes the following actions:

- Logs one of the following events, based on how the resource is shared:

    - **AnonymousLinkCreated**
    - **SecureLinkCreated**
    - **AddedToSecureLink**
    - **SharingInvitationCreated** (this event is logged only when the shared resource is a site)
- When the target user accepts the sharing invitation (by clicking the link in the invitation), SharePoint logs a **SharingInvitationAccepted** event and assigns the target user permissions to access the resource. If the target user is sent an anonymous link, the **AnonymousLinkUsed** event is logged after the target user uses the link to access the resource. For secure links, a **FileAccessed** event is logged when an external user uses the link to access the resource.

Additional information about the target user is also logged, such as the identity of the user the invitation is to and the user who accepts the invitation. In some cases, these users (or email addresses) can be different.

## How to identify resources shared with external users

A common requirement for administrators is creating a list of all resources that administrators shared with users outside of the organization. By using sharing auditing in Office 365, administrators can generate this list. Complete the following steps.

### Step 1: Search for sharing events and export the results to a CSV file

To search the audit log for sharing events, complete the following steps. For more information including the required permissions, see [Search the audit log](audit-search).

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select the **Audit** solution card. If the **Audit** solution card isn't displayed, select **View all solutions** and then select **Audit** from the **Core** section.
3. On the **Search** page and under **Activities - friendly names**, select **Sharing and access request activities** to search for sharing-related events.
4. Select a date and time range to find the sharing events that occurred within that period.
5. Select **Search** to run the search.
6. When the search finishes and displays the results, select **Export results** &gt; **Download all results**.

    After you select the export option, a message at the bottom of the window prompts you to open or save the CSV file.
7. Select **Save** &gt; **Save as** and save the CSV file to a folder on your local computer.

### Step 2: Use the PowerQuery Editor to format the exported audit log

Use the JSON transform feature in the Power Query Editor in Excel to split each property in the **AuditData** column (which consists of a multi-property JSON object) into its own column. This feature lets you filter columns to view records related to sharing.

For step-by-step instructions, see "Step 2: Format the exported audit log using the Power Query Editor" in [Export, configure, and view audit log records](audit-log-export-records#step-2-format-the-exported-audit-log-using-the-power-query-editor).

### Step 3: Filter the CSV file for resources shared with external users

In this step, you filter the CSV file for the different sharing-related events that the SharePoint sharing events section describes. Alternatively, you can filter the **TargetUserOrGroupType** column to display all records where the value of this property is **Guest**.

After formatting the exported audit log with Power Query Editor in Excel so that each **AuditData** property has its own column, complete the following steps:

1. Open the formatted Excel file that contains the exported audit log with **AuditData** properties split into individual columns by the Power Query transformation.
2. On the **Home** tab, select **Sort & Filter**, then select **Filter**.
3. In the **Sort & Filter** dropdown list on the **Operations** column, clear all selections, then select one or more of the following sharing-related events and select **Ok**.

    - **SharingInvitationCreated**
    - **AnonymousLinkCreated**
    - **SecureLinkCreated**
    - **AddedToSecureLink**

    Excel displays the rows for the events you selected.
4. Go to the column named **TargetUserOrGroupType** and select it.
5. In the **Sort & Filter** dropdown list, clear all selections, then select **TargetUserOrGroupType:Guest**, and select **Ok**.

    Now Excel displays the rows for sharing events **and** where the target user is outside of your organization, because external users are identified by the value **TargetUserOrGroupType:Guest**.

Tip

For the audit records that are displayed, the **ObjectId** column identifies the resource that you shared with the target user. For example, `ObjectId:https:\/\/contoso-my.sharepoint.com\/personal\/sarad_contoso_com\/Documents\/Southwater Proposal.docx`.