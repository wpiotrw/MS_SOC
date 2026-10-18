---
layout: FAQ
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Centralized deployment FAQ | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/centralized-deployment-faq?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
summary: >
  <p>Centralized deployment is a way for a Microsoft 365 admin to deploy Office Add-ins (Word, Excel, PowerPoint, and Outlook) to users and groups within an organization, provided the organization meets all requirements for using centralized deployment as outlined in this article. However, note that the <a href="test-and-deploy-microsoft-365-apps">integrated apps portal</a> is the recommended and most feature-rich way for most customers to centrally deploy Office add-ins to users and groups within your organization. But add-ins can also be centrally deployed through the <strong>Add-in</strong> page of the Microsoft 365 admin center.</p>
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/help/4021566/windows-10-send-feedback-to-microsoft-with-feedback-hub-app
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
ms.date: 2026-02-25T00:00:00.0000000Z
f1.keywords:
- NOCSH
ms.author: kwekua
author: kwekuako
manager: scotv
audience: Admin
ms.topic: faq
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_NonTOC
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- integrated-apps
search.appverid:
- BCS160
- MET150
- MOE150
description: Review the answers to frequent questions about centralized deployment from the Microsoft 365 admin center.
locale: en-us
document_id: 32aaf301-bc79-ea37-f3fd-94ae9e9ab02f
document_version_independent_id: 7482cca5-faac-3276-8481-e6323cafef31
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/centralized-deployment-FAQ.yml
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: faq
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/centralized-deployment-faq
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/centralized-deployment-FAQ.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: cc57d07d-b9d1-9afe-606d-084e9f6e1897
---

# Centralized deployment FAQ | Microsoft Learn

Centralized deployment is a way for a Microsoft 365 admin to deploy Office Add-ins (Word, Excel, PowerPoint, and Outlook) to users and groups within an organization, provided the organization meets all requirements for using centralized deployment as outlined in this article. However, note that the [integrated apps portal](test-and-deploy-microsoft-365-apps) is the recommended and most feature-rich way for most customers to centrally deploy Office add-ins to users and groups within your organization. But add-ins can also be centrally deployed through the **Add-in** page of the Microsoft 365 admin center.

## How do I know if my organization is set up for centralized deployment?

Centralized deployment of add-ins requires that users are using apps in Microsoft 365 for enterprise (and are signed into Microsoft 365 using their organizational log-in credentials) and have Exchange Online mailboxes. Your subscription directory must either be in, or federated to, Microsoft Entra ID.

Centralized deployment is only supported for online mailboxes. It doesn't support deployment to on-premises Exchange mailboxes.

You can use the [Centralized Deployment Compatibility Checker](centralized-deployment-of-add-ins#centralized-deployment-compatibility-checker) to determine if your subscription is eligible.

## How do you target add-in user assignments with centralized deployment?

Centralized deployment supports assignments to individual users, groups, and everyone in the tenant. Centralized deployment can be used for users in top-level groups (groups without parent groups), but not for users in nested groups (groups that have parent groups). Centralized deployment also supports most Microsoft Entra groups, including Microsoft 365 Groups, distribution lists, dynamic groups, and security groups.

It's better to use groups assignments instead of individual user assignment for easier management.

For more details, see [User and Group assignments](centralized-deployment-of-add-ins?view=o365-worldwide#user-and-group-assignments).

## How long does it take for add-ins to show up for all users?

It can take up to 24 hours for a new add-in deployment to show up for all users. It can take up to 72 hours for add-in updates, changes from turn on or turn off to reflect for users.

## How long does it take for add-ins to get removed for all users?

It can take up to 24 hours for add-in removal to reflect for all users.

## As an administrator, how do I manage the user access to add-ins for my organization?

For easy deployment of add-ins to users, groups, or to your entire organization, we recommend administrators use centralized deployment whenever deployment through the integrated apps portal is not suitable.

For more information about managing user access, see:

- [Manage add-in downloads by turning on/off Microsoft Marketplace across all apps (except Outlook)](/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center#manage-add-in-downloads-by-turning-on-off-microsoft-marketplace-across-all-apps-except-outlook)
- [Specify the administrators and users who can install and manage add-ins for Outlook](/en-us/Exchange/specify-who-can-install-and-manage-add-ins-2013-help)

## Will centralized deployment provide admins the flexibility to choose the deployment method for Outlook add-ins?

Yes. Centralized deployment provides admins the flexibility to choose one of three deployment methods for Outlook add-ins during add-in deployment:

**Fixed** The add-in will be automatically deployed to the assigned users and they won't be able to remove it from their ribbon.

**Available** Users can install the add-in in Outlook by choosing **Home &gt; Get More add-ins &gt; Admin-managed**.

**Optional** The add-in is deployed automatically to the assigned users, but they can choose to remove it.

Note

Integrated Apps don't have this option available; however, admins can still use the legacy Add-in page to perform this under **Settings** &gt; **Integrated Apps**, and then selecting the **Add-in** link. [![Screenshot that shows the Adoption Score page in Reports.](../../media/addin-links.png)](../../media/addin-links.png#lightbox)

## Can admins update Line-of-Business (LOB) add-ins?

Yes. Admins can upload a new manifest file to support metadata changes for admin-deployed LOB add-ins. The add-in updates the next time the Microsoft 365 app starts. The web application can change at any time.

For more information, see [line-of-business add-in](manage-addins-in-the-admin-center).

## Can admins turn off add-ins?

Yes. Admins can turn on or off the add-ins they deploy for all users from the Microsoft admin center.

For more information, see [Add-in states](manage-addins-in-the-admin-center#add-in-states-in-the-microsoft-365-admin-center).

## Can admins delete or remove add-ins?

Yes. Admins can delete add-ins they deployed for all users from the Microsoft admin center.

For more information, see [Delete an add-in](manage-addins-in-the-admin-center#remove-an-add-in-from-the-microsoft-365-admin-center).

## Can admins deploy paid add-ins from Microsoft Marketplace using centralized deployment?

Yes.

## Which admin role do I need to manage add-ins for my organization?

Global Admin is the recommended role with complete access to the add-in management lifecycle. If you're the person who purchased your Microsoft 365 Business subscription, you're the Global admin.

Your subscription comes with a set of admin roles that you can assign to other users in your organization. Each admin role maps to common business functions and gives people in your organization permissions to perform specific tasks in the Microsoft 365 admin center.

For more information, see [Assign admin roles](../add-users/assign-admin-roles?view=o365-worldwide).

## How many add-ins can I deploy?

A total of 200 Excel, Outlook, PowerPoint, and Word add-ins can be deployed by admins within their tenant.

## Why do add-in deployment times for Word, Excel, and PowerPoint differ compared to Outlook add-ins?

There are architectural differences between add-in deployments for Word, Excel, and PowerPoint vs Outlook.