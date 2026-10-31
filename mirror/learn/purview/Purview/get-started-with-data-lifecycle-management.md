---
layout: Conceptual
title: Get started with data lifecycle management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-02-26T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- purview-compliance
- highpri
- SPO_Content
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MOE150
- MET150
description: Prescriptive steps for admins, licensing requirements, and common scenarios that manage the lifecycle of your organization's data.
locale: en-us
document_id: 73696f89-b237-b5b8-f8c1-87487f8e4030
document_version_independent_id: 73696f89-b237-b5b8-f8c1-87487f8e4030
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/get-started-with-data-lifecycle-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: get-started-with-data-lifecycle-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/get-started-with-data-lifecycle-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 8adf0c63-31d2-0c47-8df3-e354d61a63dd
---

# Get started with data lifecycle management | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Ready to start managing the lifecycle of your organization's data by retaining the content that you need to keep, and deleting the content that you don't? To get started, use the following guidance for Microsoft Purview Data Lifecycle Management:

1. **Understand how retention and deletion works** in Microsoft 365, and then identify the workloads that need a retention policy and whether you need to create retention labels for exceptions: [Learn about retention](retention)

    Note

    If you need to manage high-value items for business, legal, or regulatory record-keeping requirements: Use retention labels with [records management](records-management) rather than data lifecycle management.
2. **Create retention policies** for the workloads you identified, specifying retention settings and actions that are required by your organization policies or industry regulations: [Create retention policies](create-retention-policies)

    If needed, [create and apply retention labels for your exceptions](create-retention-labels-data-lifecycle-management).
3. **Enable mailbox archiving** to provide users with additional mailbox storage space: [Enable archive mailboxes in Microsoft 365](enable-archive-mailboxes)

    If required to support archive mailboxes:

    - [Enable auto-expanding archiving](enable-autoexpanding-archiving) for mailboxes that need more than 100 GB storage.
    - Use [retention tags with a retention policy from messaging records management (MRM)](set-up-an-archive-and-deletion-policy-for-mailboxes) if you need to customize how emails are automatically moved from a user's primary mailbox to their archive mailbox, or if you need to specify retention and deletion settings for specific folders rather than the whole mailbox.
4. **Understand and manage inactive mailboxes** that retain mailbox content after employees leave the organization: [Learn about inactive mailboxes](inactive-mailboxes-in-office-365)
5. If you have PST files that contain data you want to govern: **Import PST files to online mailboxes** by using network upload or drive shipping: [Learn about importing your organization's PST files](pst-import-overview)

## Licensing and billing requirements

A number of different subscriptions support data lifecycle management capabilities.

To see the options for licensing your users to benefit from Microsoft Purview features, see the [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description). For the features listed on this page, see the [Microsoft Purview Data Lifecycle Management & Records Management](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-data-lifecycle--records-management) section for feature-level licensing requirements.

You must set up [pay-as-you-go billing](purview-billing-models) to create retention policies that include the locations Microsoft Copilot experiences, Enterprise AI apps, and Other AI apps. There's no charge for Microsoft 365 Copilot interactions.

## Permissions

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

See the following section for information about roles and role groups to manage Microsoft 365 retention.

For permissions to manage mailboxes for archiving, inactive mailboxes, and import, these typically require Exchange permissions, such as the Mail Recipients role. By default, this role is assigned to the Recipient Management and Organization Management role groups. For the exact permissions requirement for each management task, see the documentation that accompanies the admin instructions.

### Permissions for retention policies and retention labels

Members of your compliance team who will create and manage retention policies and retention labels need permissions to the [Microsoft Purview portal](purview-portal). To grant permissions for this limited administration, we recommend that you add users to the **Compliance Administrator** admin role group.

Alternatively to using this default role, you can create a new role group and add the **Retention Management** role to this group. For a read-only role, use **View-Only Retention Management**.

Specific to [priority cleanup](priority-cleanup) that can override retention labels and policies when it's necessary to expedite the permanent deletion of sensitive information, admins must have the **Priority Cleanup Admin** role. This role isn't included by default in the **Compliance Administrator** admin role group.

For instructions to add users to the default roles or create your own role groups, use the following guidance, depending on the portal you're using:

- [Permissions in the Microsoft Purview portal](purview-permissions)

These permissions are required only to create, configure, and apply retention policies and retention labels. The person configuring these policies and labels doesn't require access to the content.

## Support for administrative units

Data lifecycle management supports [administrative units that have been configured in Microsoft Entra ID](/en-us/azure/active-directory/roles/administrative-units):

- You can assign administrative units to members of custom role groups and any others that support administrative units. For example, role groups used with Microsoft Purview Records Management. Edit these role groups and select individual members, and then the **Assign admin units** option to select administrative units from Microsoft Entra ID. These administrators are now restricted to managing just the users in those administrative units.
- You can define the initial scope of retention policies and retention label policies when you create or edit these policies. When you select administrative units, only the users in those administrative units will be eligible for the policy.

Important

Don't select administrative units for a policy that you want to apply to SharePoint sites or to Exchange public folders. Because administrative units support only users and groups, if you configure policy for retention to use administrative units, you won't be able to select the locations for SharePoint sites or Exchange public folders.

- Both adaptive scopes and static scopes support administrative units.
- Additional impact for restricted administrators

    - [Policy lookup](retention#policy-lookup): Restricted administrators will see policies only from users within their assigned administrative units
    - [Import PST files](pst-import-overview): Restricted administrators won't be able to use the network upload feature to bulk-import PST files to Microsoft 365 mailboxes
    - [Exchange legacy features](data-lifecycle-management#exchange-legacy-features): Restricted administrators won't be able to configure the Exchange legacy features of retention policies and retention tags from messaging records management (MRM), and journaling rules
- Currently, retention labels don't support administrative units.
- Currently, a restricted administrator can create and view adaptive scopes for all administrative units when they use PowerShell cmdlets.
- Currently, inactive mailboxes aren't supported in a policy when you select one or more administrative units. To include inactive mailboxes in the policy, you must be an unrestricted administrator and select **Full directory**.

For more information about how Microsoft Purview supports administrative units, see [Administrative units](purview-admin-units#permissions-for-administrative-units).

## Common scenarios

Use the following table to help you map your business requirements to the most common scenarios for data lifecycle management.

| I want to ... | Documentation |
| --- | --- |
| Efficiently retain or delete data for Microsoft 365 services and Copilot interactions: - Exchange - SharePoint - OneDrive - Microsoft 365 Groups - Teams - Copilot and AI apps - Viva Engage - Skype for Business | [Create and configure retention policies](create-retention-policies) |
| Automatically retain content that's deleted by users who have been identified as having an elevated risk level | [Dynamically mitigate the risk of accidental or malicious deletes](retention#dynamically-mitigate-the-risk-of-accidental-or-malicious-deletes) |
| Provide users with additional mailbox storage | [Enable archive mailboxes in Microsoft 365](enable-archive-mailboxes) |
| Retain mailbox data after employees leave the organization | [Create and manage inactive mailboxes](create-and-manage-inactive-mailboxes) |
| Upload mailbox data from PST files | [Use network upload to import PST files](pst-import-network-upload) |

For scenarios that require data management of individual items, see the [common scenarios for records management](get-started-with-records-management#common-scenarios).

## End-user documentation

See the following section for information about end-user documentation to support Microsoft 365 retention.

The data lifecycle management capabilities for inactive mailboxes and import of PST files don't require end-user documentation because these are admin operations only. To help users understand and interact with their archive mailboxes in Outlook after you've enabled this capability, see [Manage email storage with online archive mailboxes](https://support.microsoft.com/office/manage-email-storage-with-online-archive-mailboxes-1cae7d17-7813-4fe8-8ca2-9a5494e9a721).

### End-user documentation for retention and deletion

Most retention policies work unobtrusively in the background without user interaction, and so need little documentation for users. Retention policies for Teams inform users when their messages have been deleted with a link to [Teams messages about retention policies](https://support.microsoft.com/office/teams-messages-about-retention-policies-c151fa2f-1558-4cf9-8e51-854e925b483b).

However, if you supplement retention policies with retention labels, these labels do have a UI presence in Microsoft 365 apps. Before you deploy these labels to your production network, make sure you provide information and instructions for end users and your help desk. To help users apply retention labels in SharePoint and OneDrive, see [Apply retention labels to files in SharePoint or OneDrive](https://support.microsoft.com/office/apply-retention-labels-to-files-in-sharepoint-or-onedrive-11a6835b-ec9f-40db-8aca-6f5ef18132df).

The most effective end-user documentation will always be customized guidance and instructions you provide for the retention label names and configurations you choose.