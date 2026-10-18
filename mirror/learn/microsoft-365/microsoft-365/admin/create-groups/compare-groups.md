---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Compare types of groups in Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.reviewer: batre
ms.date: 2026-02-02T00:00:00.0000000Z
f1.keywords: CSH
ms.author: dansimp
author: Dansimp
manager: dansimp
audience: Admin
ms.topic: product-comparison
ms.service: microsoft-365-admin
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- trust-pod
ms.custom:
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- admindeeplinkMAC
- campaignIDs-batch2
- m365-groups
- user-accounts
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 758759ad-63ee-4ea9-90a3-39f941897b7d
description: Learn about the types of groups that are available in Microsoft 365
locale: en-us
document_id: 1a37b2d3-f63b-a719-565b-a46f2b1f2e96
document_version_independent_id: e267656e-4bda-f03b-4d9c-d5149ec0a227
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/create-groups/compare-groups.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/create-groups/compare-groups
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/create-groups/compare-groups.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
platformId: 4774ae07-993c-74d1-4918-c0a113c27116
---

# Compare types of groups in Microsoft 365 - Microsoft 365 admin | Microsoft Learn

In the Microsoft 365 admin center, in the [**Groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855) section, you can create and manage these types of groups:

- **Microsoft 365 Groups** that are used for collaboration between users, both inside and outside your company. They include collaboration services such as SharePoint and Planner. Microsoft Teams uses Microsoft 365 Groups for membership.
- **Distribution groups** that are used for sending email notifications to a group of people.
- **Security groups** that are used for granting access to resources such as SharePoint sites.
- **Mail-enabled security groups** that are used for granting access to resources such as SharePoint, and emailing notifications to those users.
- **Shared mailboxes** that are used when multiple people need access to the same mailbox, such as a company information or support email address.
- **Dynamic distribution groups** that are created to expedite the mass sending of email messages and other information within an organization.

Some groups allow dynamic membership or email, as listed in the following table:

| Group type | Mail enabled | Dynamic membership(In Microsoft Entra ID) |
| --- | --- | --- |
| Microsoft 365 Groups | Yes | Yes |
| Distribution groups | Yes | No |
| Security groups | No | Yes |
| Mail-enabled security groups | Yes | No |
| Shared mailboxes | Yes | No |
| Dynamic distribution groups | Yes | No |

Microsoft 365 groups can be used with Power Automate.

## Microsoft 365 Groups

Microsoft 365 Groups are used for collaboration between users, both inside and outside your company. With each Microsoft 365 group, members get a group email and shared workspace for conversations, files, and calendar events, Stream, and a Planner. Microsoft 365 Groups can also be connected to Teams or Viva Engage.

You can add people from outside your organization to a group as long as this feature is [enabled by the administrator](/en-us/microsoft-365/admin/create-groups/manage-guest-access-in-groups). You can also allow external senders to send email to the group email address.

Microsoft 365 Groups can be [configured for dynamic membership in Microsoft Entra ID](/en-us/azure/active-directory/users-groups-roles/groups-change-type), allowing group members to be added or removed automatically based on user attributes such as department, location, title, etc.

Microsoft 365 Groups can be accessed through mobile apps such as Outlook for iOS and Outlook for Android.

Group members can send as or send on behalf of the group email address if this feature is [enabled by the administrator](/en-us/previous-versions/microsoft-365/solutions/allow-members-to-send-as-or-send-on-behalf-of-group).

If recipients subscribe to receive group conversations in their inbox, they can delete email messages from the group without removing those messages from the group's shared mailbox. And, if an email is deleted from the group's shared mailbox, it isn't deleted from group members' personal inbox. See [Who can delete email from the Group inbox](/en-us/microsoft-365/admin/create-groups/create-groups#who-can-delete-email-from-the-group-inbox).

Microsoft 365 Groups support nesting through [dynamic groups in Microsoft Entra ID](/en-us/azure/active-directory/enterprise-users/groups-dynamic-rule-member-of).

Microsoft 365 Groups can be added to one of the three SharePoint groups (Owners, Members, or Visitors) to give people permissions to the site.

## Distribution groups

[Distribution groups](/en-us/exchange/recipients-in-exchange-online/manage-distribution-groups/manage-distribution-groups) are used for sending notifications to a group of people. They can receive external email if enabled by the administrator.

Distribution groups are best for situations where you need to broadcast information to a set group of people, such as "People in Building A" or "Everyone at Contoso."

Distribution groups can be added to a team in Microsoft Teams, though only the members are added and not the group itself.

Microsoft 365 Groups can't be members of distribution groups.

## Dynamic distribution groups

[Dynamic distribution groups](/en-us/exchange/recipients-in-exchange-online/manage-dynamic-distribution-groups/manage-dynamic-distribution-groups) are mail-enabled groups that are used to send mail to people with specific attributes, such as department or location. These attributes are defined in the Exchange admin center rather than Microsoft Entra ID.

Unlike regular distribution groups that contain a defined set of members, the membership list for dynamic distribution groups is determined each time a message is sent to the group, based on the filters and conditions that you define. When an email message is sent to a dynamic distribution group, it's delivered to all recipients in the organization that match the criteria defined for that group.

## Security groups

[Security groups](/en-us/microsoft-365/admin/email/create-edit-or-delete-a-security-group) are used for granting access to Microsoft 365 resources, such as SharePoint sites. They can make administration easier because you need only administer the group rather than adding users to each resource individually.

Security groups can contain users or devices. Creating a security group for devices can be used with mobile device management services, such as Microsoft Intune.

Security groups can be [configured for dynamic membership in Microsoft Entra ID](/en-us/azure/active-directory/users-groups-roles/groups-change-type), allowing group members or devices to be added or removed automatically based on user attributes such as department, location, or title; or device attributes such as operating system version.

Security groups can be added to a team.

Microsoft 365 Groups can't be members of security groups.

## Mail-enabled security groups

Mail-enabled security groups function the same as regular security groups, except that they can't be dynamically managed through Microsoft Entra ID and can't contain devices.

They include the ability to send mail to all the members of the group.

Mail-enabled security groups can be added to a team.

## Shared mailboxes

[Shared mailboxes](/en-us/microsoft-365/admin/email/create-a-shared-mailbox) are used when multiple people need access to the same mailbox, such as a company information or support email address, reception desk, or other function that might be shared by multiple people.

Shared mailboxes can receive external emails if the administrator has enabled this feature.

Shared mailboxes include a calendar that can be used for collaboration.

Users with permissions to the shared mailbox can send as or send on behalf of the mailbox email address, if the administrator has given that user permissions to do that. This feature is especially useful for help and support mailboxes, because users can send emails from mailbox names like "Contoso Support" or "Building A Reception Desk."

It's not possible to migrate a shared mailbox to Microsoft 365 Groups.