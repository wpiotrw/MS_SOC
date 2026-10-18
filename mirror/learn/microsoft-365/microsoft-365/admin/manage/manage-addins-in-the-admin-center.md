---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage Add-ins in the Microsoft 365 Admin Center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: kwekua
author: kwekuako
manager: scotv
ms.date: 2026-03-16T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
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
- AdminTemplateSet
- integrated-apps
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 737e8c86-be63-44d7-bf02-492fa7cd9c3f
description: Learn how to manage, enable, disable, and remove Office add-ins in the Microsoft 365 admin center. Control add-in access for users and groups in your organization.
locale: en-us
document_id: d61e46dd-c1ff-dfec-5e0e-9f2e7251a5c1
document_version_independent_id: 49f69fa9-33e8-373f-a7f9-26b828510fda
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/manage-addins-in-the-admin-center.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/manage-addins-in-the-admin-center
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/manage-addins-in-the-admin-center.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19e6356c-ba1e-4d22-9557-6222c183f04d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/01e6eca5-e701-4cd9-a21f-56c9258f473e
platformId: 537dc30c-aaca-dee3-afe7-06bf30f4ee63
---

# Manage Add-ins in the Microsoft 365 Admin Center - Microsoft 365 admin | Microsoft Learn

Tip

The [integrated apps portal](test-and-deploy-microsoft-365-apps) is the recommended and most feature-rich way for most customers to centrally deploy Office add-ins to users and groups within your organization.

Office Add-ins, also known as Integrated Apps, help users in your organization to personalize documents and streamline access to information on the web. An admin can centrally manage add-ins that are deployed to users and groups via the Microsoft 365 admin center. For example, an admin can:

- Enable or disable add-ins.
- Change which users or groups have access to add-ins.
- Remove add-ins that are no longer used.

For more information about installing add-ins from the Microsoft 365 admin center, see [Deploy Office Add-ins in the Microsoft 365 admin center](manage-deployment-of-add-ins).

## Add-in states in the Microsoft 365 admin center

An add-in can be in one of the following states:

| State | How the state occurs | Effect |
| --- | --- | --- |
| **Enabled** | Admin downloads the add-in in the Microsoft 365 admin center and assigns it to users or groups. | Users and groups assigned the add-in have access to the add-in. |
| **Not assigned** | Admin downloads the add-in in the Microsoft 365 admin center but the add-in isn't assigned to a user or group. | Unassigned users and groups can't access the add-in. |
| **Removed** | Admin removes the add-in from the Microsoft 365 admin center. | No users can access the add-in. |

Choosing not to assign an add-in versus removing it might make sense if the add-in is only used during specific times of the year. If no one is using an add-in anymore, consider removing the add-in from the Microsoft 365 admin center.

## Remove an add-in from the Microsoft 365 admin center

To remove an add-in that you deployed and no longer need, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select **Integrated apps**.
4. In the **Integrated apps** page, select the deployed add-in that you want to remove.
5. In the add-in properties pane, make sure **Overview** is selected.
6. In the **Remove apps** window, select **Yes, I'm sure I want to remove the app and associated data**, and then select **Remove**.

## Edit user access to an add-in in the Microsoft 365 admin center

After you deploy an add-in, you can manage user access to the add-in. To manage user access to an add-in, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select **Integrated apps**.
4. In the **Integrated apps** page, select the deployed add-in that you want to edit.
5. In the add-in properties pane, select **Users**.
6. Under **Assigned users**, add or remove users who should have access to the add-in, and then select **Update**.

## Manage add-in downloads by enabling or disabling Microsoft Marketplace

Important

In the Microsoft 365 admin center, **Microsoft Marketplace** is sometimes referred to as **Office Store**.

As an admin, you can manage access to the Microsoft Marketplace and control whether users can download add-ins. Managing access to the Microsoft Marketplace is important for the following reasons:

- Ensure users can download Office Add-ins and take advantage of their features.
- Ensure users can access only add-ins approved through centralized deployment.

Use this setting if you want to:

- Allow users to discover and install approved add-ins themselves.
- Block all user-initiated add-in downloads and rely only on centralized deployment.

### Enable or disable access to the Microsoft Marketplace for all apps

The **Let users access the Office Store** setting in the Microsoft 365 admin center controls all users' ability to acquire the following add-ins from Microsoft Marketplace:

- Add-ins for non-subscription Word, Excel, and PowerPoint on Windows and Mac
- Add-ins for subscription Microsoft 365

When you disable access to the Microsoft Marketplace, a user who tries to access it sees the following message:

**Office store not available. Unfortunately, your organization has disabled access to the Office Store. Please contact your administrator to get access to the store.**

Support for enabling or disabling access to the Microsoft Marketplace starts in the following versions:

- Office on Windows: 16.0.9001.
- Office on Mac: 16.10.18011401.
- Office on iOS: 2.9.18010804.
- Office for the web.

To enable or disable access to the Microsoft Marketplace and downloading of add-ins via the **Let users access the Office Store** setting, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [Org settings](https://go.microsoft.com/fwlink/p/?linkid=2053743).
4. In the **Org settings** page, make sure **Services** is selected, and then select **User owned apps and services**.
5. In the **User owned apps and services** pane:

    - Select **Let users access the Office Store** to give users access to the Microsoft Marketplace and allow users to download. This setting is the default setting.
    - Clear **Let users access the Office Store** to block users from accessing the Microsoft Marketplace and prevent users from downloading add-ins.

    [![Screenshot of the user-owned apps and services settings for non-educational tenants in the Microsoft 365 admin center.](../../media/user-owned-apps-and-services.png)](../../media/user-owned-apps-and-services.png#lightbox)
6. Select **Save** after you choose the desired setting. If the setting is already in the desired state, select the **X** in the top-right corner to cancel.

### Important limitations and exceptions

- Access to the Microsoft Marketplace doesn't apply to Microsoft Outlook add-ins. To manage Microsoft Outlook add-ins, see [Specify the administrators and users who can install and manage add-ins for Outlook in Exchange Online](/en-us/exchange/clients-and-mobile-in-exchange-online/add-ins-for-outlook/specify-who-can-install-and-manage-add-ins).
- Even if users can download add-ins from Microsoft Marketplace, they can't launch or use the add-in in the client.
- To prevent a user from signing into the Microsoft Marketplace by using a personal Microsoft account, restrict sign in to use only an organizational account. For more information, see [Identity, authentication, and authorization in Office 2016](/en-us/DeployOffice/security/identity-authentication-and-authorization-in-office).
- If you prevent users from accessing Microsoft Marketplace, they also can't [Sideload Office Add-ins for testing from a network share](/en-us/office/dev/add-ins/testing/create-a-network-shared-folder-catalog-for-task-pane-and-content-add-ins).

#### User owned apps and services settings for educational tenants

Additional access options are available for educational tenants in the **User owned apps and services** pane. You can control access based on whether a user is:

- A faculty, staff, and other non-student users.
- An adult student.
- A non-adult student.

[![Screenshot of the user-owned apps and services settings for educational tenants in the Microsoft 365 admin center.](../../media/user-owned-apps-and-services-edu.png)](../../media/user-owned-apps-and-services-edu.png#lightbox)

The user's license information defines the type of user.

- A faculty, staff, and other non-student users: A user who doesn't have an educational license.
- An adult or non-adult student: A user who has an educational license. The **Age Group** property checks whether the student is an adult.

For more information, see the following articles:

- [Assign or unassign licenses for users in the Microsoft 365 admin center](assign-licenses-to-users).
- [Add or update a user's profile information and settings in the Microsoft Entra admin center](/en-us/entra/fundamentals/how-to-manage-user-profile-info).

## End-user experience with add-ins in Office applications

After you deploy an add-in, users interact with the add-in directly in their Office apps. An add-in appears on all platforms that the add-in supports. For more information, see [Start using your Office Add-in](https://support.microsoft.com/office/82e665c4-6700-4b56-a3f3-ef5441996862).

Some add-ins support commands that appear in the ribbon. For example, the **Citations** add-in shows the command **Search Citation** in the ribbon:

[![Screenshot of the Microsoft 365 ribbon showing the Search Citations add-in command.](../../media/553b0c0a-65e9-4746-b3b0-8c1b81715a86.png)](../../media/553b0c0a-65e9-4746-b3b0-8c1b81715a86.png#lightbox)

If an add-in doesn't support commands that appear in the ribbon, the user can view the add-in via **Manage your apps**. They can also view all add-ins that are deployed in the organization in **Manage your apps**.

### View add-ins in Manage your apps

To view add-ins in **Manage your apps**, select the tab based on which application you want to view add-ins for:

- [**Word, Excel, or PowerPoint**](manage-addins-in-the-admin-center?&amp;tabs=word-excel-powerpoint#view-add-ins-in-manage-your-apps).
- [**Outlook**](manage-addins-in-the-admin-center?&amp;tabs=outlook#view-add-ins-in-manage-your-apps).

# [Word, Excel, or PowerPoint](#tab/word-excel-powerpoint)
#### View add-ins in Word, Excel, or PowerPoint

To view add-ins in **Manage your apps** in Word, Excel, or PowerPoint, follow these steps:

1. On the **Home** ribbon of the app, select **Add-ins**.
2. In the pane that opens, select **+ More Add-ins**.
3. At the bottom of the left-hand navigation pane of the **Apps** page, select **Manage your apps** to see a list of all deployed apps, agents, and add-ins.
4. To see the details of an add-in, select it from the list.

# [Outlook](#tab/outlook)
#### View add-ins in Outlook

To view add-ins in **Manage your apps** in Outlook, follow these steps:

1. Select one of the following options to access the **Apps** pane:

    - From the left-hand **App Bar**, select the **More Apps** button.
    - On the **Home** ribbon, select **More Apps** (Outlook) or **All Apps** (Outlook (classic)).
2. Select **Add apps** in the pane that opens.
3. At the bottom of the left-hand navigation pane of the **Apps** page, select **Manage your apps** to see a list of all deployed apps, agents, and add-ins.
4. To see the details of an add-in, select it from the list.

---