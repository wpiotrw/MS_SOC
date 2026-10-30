---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Add users and assign licenses in Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/add-users?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how to add users and assign licenses in Microsoft 365. Create user accounts, manage access to apps and mailboxes for your organization.
customer intent: As an admin, I want to add users and assign licenses in Microsoft 365 so that they can access the necessary tools and services.
f1.keywords:
- NOCSH
ms.author: deniseb
author: denisebmsft
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: identity
ms.localizationpriority: medium
ms.collection:
- Tier1
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365_Setup
- Adm_TOC
ms.custom:
- VSBFY23
- okr_smb
- AdminSurgePortfolio
- AdminTemplateSet
- adminvideo
- business_assist
- user-accounts
search.appverid:
- MET150
ms.date: 2026-01-06T00:00:00.0000000Z
locale: en-us
document_id: 83719909-241b-2902-5ff1-496934da24e3
document_version_independent_id: d05e079d-f0d6-11ac-577c-f407cc49fcb7
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/add-users.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/add-users
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/add-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: c31cdc62-a3dd-5c19-3827-2831af9f0a81
---

# Add users and assign licenses in Microsoft 365 - Microsoft 365 admin | Microsoft Learn

Each person in your organization needs a user account before they can sign in and access [Microsoft 365 for business](https://www.microsoft.com/microsoft-365/business). This article describes how to add users one at a time, or adds multiple users at once.

If you need help with adding users, [Get support for Microsoft 365 for business](../get-help-support).

## Before you begin

Make sure that licenses are purchased for users. For more information, see [Buy or remove licenses for a Microsoft business subscription](/en-us/microsoft-365/commerce/licenses/buy-licenses).

You must be a license or user administrator to add users and assign licenses. For more information, see [About admin roles](about-admin-roles).

Important

Use roles with the fewest permissions. Lower permissioned accounts help improve security for your organization. Global Administrator is a highly privileged role. Limit its use to emergency scenarios when you can't use an existing role. For more information, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Add a user in Microsoft 365

The following video shows how to add a user in Microsoft 365. It's one minute and 57 seconds long.

Note

The steps used in the video show the *simplified view* starting point for adding users, but the remaining steps are the same as the *dashboard view*.

::: moniker range="o365-worldwide"

Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft).

::: moniker-end

::: moniker range="o365-21vianet"

1. Sign in to the [Microsoft 365 admin center](https://portal.partner.microsoftonline.cn).

::: moniker-end

1. Determine which admin center view you're currently using.

    - If the top of the Microsoft 365 admin center shows **Dashboard view**, go to **Users** &gt; **Active users**, and select **Add a user**.

        ![A screenshot of the Dashboard view in the Microsoft 365 admin center.](../../media/classic-admin-center.png)
    - If the top of the Microsoft 365 admin center shows **Simplified view**, select **Add user**. You can select either the **Add user** button at the top of the page or in the **Users** tab under **Your organization**.

        ![A screenshot of the Simplified view in the Microsoft 365 admin center.](../../media/vsb-add-user-view.png)
2. **Set up the basics**: fill in the basic user information, and then select **Next**.

    - **Name**: Fill in the first name, family name, display name, and username.
    - **Domains**: Choose the domain for the user's account. For example, if their username is `Jakob`, and the domain is `contoso.com`, then they sign in with `jakob@contoso.com`.
    - **Password settings**:
        - By default, the option to **Automatically create a password** is selected. If you deselect this option, create a strong password for the user.
        - By default, the option to **Require this user to change their password when they first sign in** is selected. The user must change their password after 90 days.
3. **Assign product licenses**: select the location and the appropriate license for the user.

    - If you don't have any licenses available, you can still add a user and buy more licenses.
    - To limit the apps the user has a license for, expand **Apps** and select or deselect apps.
4. **Optional settings**:

    - If you want to make this user an admin, expand **Roles**.
    - To add more information about the user, expand **Profile info**.
5. **Review and finish**: review your new user's settings, make further changes, and then select **Finish adding**.
6. On the completion page:

    - To give the user their password, select **Print** to create a hard copy or a PDF of their credentials that you can securely share with them.
    - To help them get started with Microsoft 365, send them an email that contains useful information.
    - Decide whether you want to save these user settings as a template.
    - Choose whether you want to add another user or **Close** the **Add a user** pane.

## Add multiple users in Microsoft 365

The following video shows how to add multiple users in Microsoft 365. It's one minute and 31 seconds long.

### Add multiple users in the dashboard view

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), go to **Users** &gt; **Active users**, and then select **Add multiple users**.
2. **Add list of users**: choose whether to add users via rows on this page or upload a CSV with user information.

    ![A screenshot from the Microsoft 365 admin center to add a list of users.](../../media/upload-csv-file.png)

    If you select **I'd like to upload a CSV with user information**, follow these steps:

    1. Download either the blank CSV file or file that includes example user information.
    2. Open and edit the CSV file, and fill in values for user name and display name for each user you want to add. For example, `bob@contoso.com, Bob Kelly`. Don't change the column headings or the order of columns.
    3. When you're done entering the users' information in your spreadsheet, save it in CSV format.
    4. In the Microsoft 365 admin center, select **Browse**, go to the location of your CSV file, and select **Open**.
3. **Licenses**: select the location, licenses, and apps you want to assign to all new users.
4. **Review and finish adding multiple users**: Review your selections and select **Add users**.

### Other methods to add multiple users

You can also use any of the following methods to add multiple users at the same time:

- **Automate adding accounts and assigning licenses.** Choose this method if you're already familiar with using Windows PowerShell cmdlets. For more information, see [Create user accounts with Microsoft 365 PowerShell](../../enterprise/create-user-accounts-with-microsoft-365-powershell).
- **Synchronize with Active Directory.** Use the Microsoft Entra Connect tool to replicate Active Directory user accounts in Microsoft 365. The sync only adds the user accounts. You must assign licenses to the synced users before they can use email and other apps for Microsoft 365. For more information, see [Set up directory synchronization for Microsoft 365](../../enterprise/set-up-directory-synchronization).
- **Migrate email accounts from Exchange.** When you migrate multiple mailboxes to Microsoft 365 by using either cutover, staged, or a hybrid Exchange method, you automatically add users as part of the migration. The migration only adds the user accounts. You must assign licenses to the users before they can use email and other apps for Microsoft 365. If you don't assign a license to a user, their mailbox is disabled after a grace period of 30 days. Learn how to [assign licenses to users](../manage/assign-licenses-to-users) in the Microsoft 365 admin center. For more information, see [Ways to migrate multiple email accounts to Microsoft 365](/en-us/Exchange/mailbox-migration/mailbox-migration).

## Create, edit, or delete custom user views

If you're a user management admin of a Microsoft 365 for business subscription, you can create up to 50 custom user views to view subsets of users. These views are in addition to the standard set of views. You can create, edit, or delete custom user views, and all admins can access the custom views you create.

When you create, edit, or delete a custom user view, all admins in your company see the changes in the **Filter set** list when they go to the **Active users** page.

### Standard filters

The **Filter set** list displays standard user views by default. You can't edit or delete standard views. The standard filters include:

- Billing admins
- Global admins
- Guest users
- Helpdesk admins
- Licensed users
- Service support admins
- Unlicensed users
- User admins
- Users with errors

A few things to note about standard views:

- If there are more than 2,000 users in the list, some standard views display an unsorted list. To locate specific users in this list, use the search field.
- If you didn't purchase Microsoft 365 from Microsoft, **Billing admins** don't appear in the standard views list. For more information, see [Assigning admin roles](assign-admin-roles).

### Custom filters

To create a custom filter, select **New filter** from the **Filter set** list. This action opens the **Custom filter** pane.

Create and edit your custom views in the **Custom filter** pane. If you select multiple filter options, you get results that contain users who match all the selected criteria. Many conditions are available for custom filters, such as:

- **Domain**: If you have multiple domains for your organization, you can choose from the list of available domains.
- **Sign-in status**: Choose users that are allowed or blocked.
- **Location**: Choose a location from the list of countries/regions.
- **Assigned product license**: Choose from the list of licenses that are available to your organization. Use this filter to show users who have the assigned license. Users might also have other licenses.

You can also filter by other user profile details used in your organization, such as department, city, state or province, country/region, or job title.

You can select these **Other conditions**:

- **Synchronized users only**: Select this option to show all users who are synced with the local Active Directory. This filter works whether you activate the users or not.
- **Users with errors**: Select this option to show users who might have provisioning errors.
- **Unlicensed users**: Select this option to find all the users who aren't assigned a license. The results for this view can also include users who have an Exchange mailbox but don't have a license. To track those users specifically, use the filter **Unlicensed users with Exchange mailboxes or archives**. The results for this view can also include users who have an Exchange archive, but don't have a license.
- **Unlicensed users with Exchange mailboxes or archives**: Select this option to show user accounts that you created in Exchange Online and who were assigned an Exchange mailbox, but didn't get a Microsoft 365 license. The results of this filter include users who have or who were assigned an Exchange archive.

    Note

    The **Unlicensed users with Exchange mailboxes** filter works when:

    - The mailbox was recently converted from **shared** to **user** and it has no license.
    - The mailbox was recently migrated to Microsoft 365 but a license wasn't assigned.
    - The mailbox was created using PowerShell, and a license wasn't assigned.
    - A new mailbox is provisioned for the user, and that mailbox was created on-premises with the **New-RemoteMailbox** cmdlet.

### Create a custom user view

::: moniker range="o365-worldwide"

In the [Microsoft 365 admin center](https://admin.microsoft.com), go to **Users** &gt; **Active users**.

::: moniker-end

::: moniker range="o365-21vianet"

1. In the admin center, go to **Users** &gt; **[Active users](https://portal.partner.microsoftonline.cn/AdminPortal/Home?ref=users)**.

::: moniker-end

1. On **Active users**, select **Filter set** and select **New filter**.
2. On the **Custom filter** pane, enter the name for your filter, choose the conditions for your custom filter, and then select **Add**.

Your custom view is now included in the custom filters set.

### Edit or delete a custom user view

::: moniker range="o365-worldwide"

In the [Microsoft 365 admin center](https://admin.microsoft.com), go to **Users** &gt; **Active users**.

::: moniker-end

::: moniker range="o365-21vianet"

1. In the admin center, go to **Users** &gt; **[Active users](https://portal.partner.microsoftonline.cn/AdminPortal/Home?ref=users)**.

::: moniker-end

1. On **Active users**, select **Filter set**, select **Custom filters set**, and switch to the filter you want to change. You can only edit custom filters.
2. Select **Filter set** again, then select **Edit filter**.
3. On the **Custom filter** pane:

    - To change the filter: edit the conditions, then select **Save**.
    - To delete the filter: select the ellipsis (`...`), then select **Delete**.