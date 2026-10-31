---
layout: Conceptual
title: Get started with records management in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/get-started-with-records-management
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2025-09-18T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.subservice: purview-records-management
ms.collection:
- purview-compliance
- highpri
- SPO_Content
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MOE150
- MET150
description: Prescriptive steps for admins, licensing requirements, and common scenarios that manage high-value content in Microsoft 365 for your legal, business, or regulatory obligations.
locale: en-us
document_id: e4829ed5-fff6-f326-df40-a927dcaeaeec
document_version_independent_id: e4829ed5-fff6-f326-df40-a927dcaeaeec
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/get-started-with-records-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: get-started-with-records-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/get-started-with-records-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 7feb09ff-d323-822f-13d7-9b58ff2ef26d
---

# Get started with records management in Microsoft 365 | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Ready to start managing your organization's high-value content for legal, business, or regulatory obligations by using a records management solution in Microsoft 365? Use the following guidance to get started:

1. **Understand how retention and deletion works** in Microsoft 365, and identify whether you need to use retention policies to supplement retention labels that manage documents and emails at the item level: [Learn about retention policies and retention labels](retention)

    If necessary, [create retention policies](create-retention-policies) for baseline governance of data across Microsoft 365 workloads.
2. **Understand the records management solution** and how retention labels can be used to allow or block actions when documents and emails are declared records: [Learn about records management](records-management)
3. **Create your file plan for retention and deletion settings and actions, and when items should be marked as records** by importing an existing plan if you have one, or create new retention labels: [Use file plan to create and manage retention labels](file-plan-manager)
4. **Publish and apply your retention labels**. Retention labels are reusable building blocks that can be used in multiple policies and can be incorporated into user workflows:

    - [Publish retention labels and apply them in apps](create-apply-retention-labels)
    - [Apply a retention label to content automatically](apply-retention-labels-automatically)

Tip

If you're migrating records to Microsoft 365 and need to validate that they haven't been altered, see [Validating migrated records](records-management#validating-migrated-records).

## Licensing and billing requirements

A number of different subscriptions support records management and the licensing requirements for users depends on the features you use.

To see the options for licensing your users to benefit from Microsoft Purview features, see the [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description). For Records Management, see the [Microsoft Purview Data Lifecycle Management & Records Management](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-data-lifecycle--records-management) section for feature-level licensing requirements.

You must set up [pay-as-you-go billing](purview-billing-models) to create retention policies that include the locations Microsoft Copilot experiences, Enterprise AI apps, and Other AI apps. There's no charge for Microsoft 365 Copilot interactions.

## Permissions

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Members of your compliance team who are responsible for records management need permissions to the [Microsoft Purview portal](purview-portal). To grant permissions for this limited administration, we recommend that you add users to the **Records Management** admin role group. This role group grants permissions for all features related to records management, which include the permissions to create and manage [adaptive policy scopes](retention#adaptive-or-static-policy-scopes-for-retention), and [disposition review and verification](disposition).

For a read-only role, you can create a new role group and add the **View-Only Record Management** role to this group.

For instructions to add users to the default roles or create your own role groups, see [Permissions in the Microsoft Purview portal](purview-permissions).

These permissions are required only to create, configure, and apply retention labels that declare records, and manage disposition. The person configuring these labels doesn't require access to the content.

## Support for administrative units

Records management supports [administrative units that have been configured in Microsoft Entra ID](/en-us/azure/active-directory/roles/administrative-units):

- You can assign administrative units to members of role groups that are used with Microsoft Purview Records Management. Edit the Records Management role group or other role groups that support administrative units. From these role groups, select individual members, and then the **Assign admin units** option to select administrative units from Microsoft Entra ID. These administrators are now restricted to managing just the users in those administrative units.
- You can define the initial scope of retention policies and retention label policies when you create or edit these policies. When you select administrative units, only the users in those administrative units will be eligible for the policy.

    Important

    Don't select administrative units for a retention label policy that you want to apply to SharePoint sites. Because administrative units support only users and groups, if you configure a retention label policy to use administrative units, you won't be able to select the locations for SharePoint sites.
- Both adaptive scopes and static scopes support administrative units.
- Additional impact for restricted administrators

    - [Policy lookup](retention#policy-lookup): Restricted administrators will see policies only from users within their assigned administrative units
    - [Disposition review and verification](disposition): Restricted administrators will be able to add reviewers only from within their assigned administrative units, and see disposition reviews and items disposed only from users within their assigned administrative units
- Currently, retention labels and [events](event-driven-retention) don't support administrative units.
- Currently, retention policies for Copilots and AI apps don't support administrative units.
- Currently, a restricted administrator can create and view adaptive scopes for all administrative units when they use PowerShell cmdlets.
- Currently, inactive mailboxes aren't supported in a policy when you select one or more administrative units. To include inactive mailboxes in the policy, you must be an unrestricted administrator and select **Full directory**.

For more information about how Microsoft Purview supports administrative units, see [Administrative units](purview-admin-units#permissions-for-administrative-units).

## Common scenarios

Use the following table to help you map your business requirements to the scenarios that are supported by records management.

Tip

Need to comply with a specific industry regulation? Check [Regulatory requirements for data lifecycle management and records management](retention-regulatory-requirements) for regulation-specific guidance.

| I want to ... | Documentation |
| --- | --- |
| Declare a record | [Declare records by using retention labels](declare-records) |
| Update a record | [Use record versioning to update records stored in SharePoint or OneDrive](record-versioning) |
| Let admins and users manually apply retain and delete actions for documents and emails: - SharePoint - OneDrive - Outlook and Outlook on the web | [Publish retention labels and apply them in apps](create-apply-retention-labels) |
| Let site admins set default retain and delete actions for all content in a SharePoint library, folder, or document set | [Publish retention labels and apply them in apps](create-apply-retention-labels) |
| Let users automatically apply retain and delete actions to emails by using Outlook rules | [Publish retention labels and apply them in apps](create-apply-retention-labels) |
| Let admins apply retain and delete actions to a Microsoft Syntex model, so that these settings are automatically applied to identified files in a SharePoint library | [Publish retention labels and apply them in apps](create-apply-retention-labels) |
| Automatically apply retain and delete actions to documents and emails | [Apply a retention label to content automatically](apply-retention-labels-automatically) |
| Automatically retain and delete Teams meeting transcripts or recordings and their accompanying transcripts | [Apply a retention label to content automatically](apply-retention-labels-automatically#microsoft-teams-meeting-recordings-and-transcripts) |
| Automatically retain and delete documents and emails with a specific sensitivity label | [Apply a retention label to content automatically](apply-retention-labels-automatically#identify-files-and-emails-that-have-a-sensitivity-label) |
| Start the retention period when an event occurs, such as: - Employees leave the organization - Contracts expire - End of product lifetime | [Start retention when an event occurs](event-driven-retention) |
| Do custom actions or integrate with other solutions at the end of the retention period | [Customize what happens at the end of the retention period](retention-label-flow) |
| Restrict changes to policies to help meet regulatory requirements or safeguard against rogue administrators | [Use Preservation Lock to restrict changes to retention policies and retention label policies](retention-preservation-lock) |
| Manage the lifecycle of different document types in SharePoint | [Use retention labels to manage the lifecycle of documents stored in SharePoint](auto-apply-retention-labels-scenario) |
| Apply a retention label to a file when I receive an alert that content containing personal data is being stored or remains untouched for too long | [Investigate and remediate alerts in Privacy Risk Management](/en-us/privacy/priva/risk-management-alerts) |
| Make sure somebody reviews and approves before content is deleted at the end of its retention period | [Disposition reviews](disposition#disposition-reviews) |
| Have proof of disposition for content that is permanently deleted at the end of its retention period | [Disposition of records](disposition#disposition-of-records) |
| Monitor how and where retain and delete settings are applied to items | [Monitoring retention labels](retention#monitoring-retention-labels) |
| Programamtically create retention labels, and manage events and event type retention triggers | [Microsoft Graph API for records management](purview-extensibility#microsoft-graph-api-for-records-management) |
| Programmatically apply and manage retention labels in SharePoint and OneDrive | Microsoft Graph API for retention labels in SharePoint and OneDrive:  - [lock and unlock records](/en-us/graph/api/driveitem-lockorunlockrecord) - [set retention labels](/en-us/graph/api/driveitem-setretentionlabel) - [remove retention labels](/en-us/graph/api/driveitem-removeretentionlabel) - [get metadata for retention labels](/en-us/graph/api/driveitem-getretentionlabel) |

## End-user documentation

If you're using retention policies for baseline data governance, they typically work unobtrusively in the background without user interaction. As a result, they need little documentation for users. Retention policies for Teams inform users when their messages have been deleted with a link to [Teams messages about retention policies](https://support.microsoft.com/office/teams-messages-about-retention-policies-c151fa2f-1558-4cf9-8e51-854e925b483b).

In comparison, retention labels have a UI presence in Microsoft 365 apps, so make sure you provide guidance for end users and your help desk before these labels are deployed to your production network. To help users apply retention labels in SharePoint and OneDrive, and information about unlocking records for editing, see [Apply retention labels to files in SharePoint or OneDrive](https://support.microsoft.com/office/apply-retention-labels-to-files-in-sharepoint-or-onedrive-11a6835b-ec9f-40db-8aca-6f5ef18132df).

However, the most effective end-user documentation will be customized guidance and instructions you provide for the retention label names and configurations you choose.