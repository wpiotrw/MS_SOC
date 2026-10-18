---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage Office Scripts settings - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-office-scripts-settings?view=o365-worldwide
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
ms.date: 2025-10-10T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
- admindeeplinkMAC
- tenant
search.appverid: MET150
description: Learn how to manage Office Scripts settings for users in your organization.
locale: en-us
document_id: 3a5bcf4d-f5ce-d4d7-5ac8-c26d34a0c4b4
document_version_independent_id: 14b25292-216b-d4be-32e9-616dddd2aad4
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/manage-office-scripts-settings.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/manage-office-scripts-settings
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/manage-office-scripts-settings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/60932d05-feee-4685-a73b-595e25dd9318
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/c43bb58b-1190-419b-8d18-e6052371b599
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: 3a8b0640-ad81-d192-7363-1f20f76c51dd
---

# Manage Office Scripts settings - Microsoft 365 admin | Microsoft Learn

[Office Scripts](/en-us/office/dev/scripts) allows users to automate tasks by recording, editing, and running scripts in Excel. Office Scripts works with Power Automate, and users run scripts on workbooks by using the Excel Online (Business) connector. Microsoft 365 admins can manage Office Scripts settings from the Microsoft 365 admin center.

Important

We're moving the management of Office Scripts admin controls from the Microsoft 365 admin center to the Microsoft 365 Cloud Policy service. For more information, see Office Scripts admin controls transition.

Note

To manage Office Scripts settings, you must be at least an Office Apps admin. For more information, see [About admin roles](../add-users/about-admin-roles).

## Manage availability of Office Scripts and sharing of scripts

1. In the Microsoft 365 admin center, go to the **Settings** &gt; **Org settings** &gt; **[Services](https://go.microsoft.com/fwlink/p/?linkid=2053743)** tab.
2. Select **Office Scripts**.
3. Office Scripts is turned on by default, and everyone in your organization can access and use the feature and share scripts. To turn off Office Scripts for your organization, clear the **Let users automate their tasks in Excel** checkbox.
4. If you previously turned off Office Scripts for your organization and you want to turn it back on, select **Let users automate their tasks in Excel**, and then specify who can access and use the feature:

    - To allow all users in your organization to access and use Office Scripts, leave **Everyone** (the default) selected.
    - To allow only members of a specific group to access and use Office Scripts, select **Specific group**, and then enter the name or email alias of the group to add it to the allowlist. You may add only one group to the allowlist, and it must be one of the following types:

        - Microsoft 365 group
        - Distribution group
        - Security group
        - Mail-enabled security group

        To learn more about the different types of groups, see [Compare groups](../create-groups/compare-groups).
5. To allow users with access to Office Scripts to share their scripts with others in your organization, select **Let users with access to Office Scripts share their scripts with others in the organization**. Sharing scripts outside of an organization isn't allowed.

    Note

    If you later turn off script sharing for your organization, users will still be able to run previously-shared scripts.
6. Specify which users with access to Office Scripts can share their scripts:

    - To allow all users with access to Office Scripts to share their scripts, leave **Everyone** (the default) selected.
    - To allow only members of a specific group with access to Office Scripts to share their scripts, select **Specific group**, and then enter the name or email alias of the group to add it to the allowlist. You may add only one group to the allowlist, and it must be one of the following types:

        - Microsoft 365 group
        - Distribution group
        - Security group
        - Mail-enabled security group

        To learn more about the different types of groups, see [Compare groups](../create-groups/compare-groups).
7. To allow users to run their Office Scripts inside Power Automate flows, select **Let users with access to Office Scripts run their scripts with Power Automate**. This allows users to add flow steps with the [Excel Online (Business) connector](/en-us/connectors/excelonlinebusiness)**Run script** option.

    - To allow all users with access to Office Scripts to use their scripts in flows, leave **Everyone** (the default) selected.
    - To allow only members of a specific group with access to Office Scripts to use their scripts in flows, select **Specific group**, and then enter the name or email alias of the group to add it to the allowlist. You may add only one group to the allowlist, and it must be one of the following types:

        - Microsoft 365 group
        - Distribution group
        - Security group
        - Mail-enabled security group

        To learn more about the different types of groups, see [Compare groups](../create-groups/compare-groups).
    - To learn more about using Office Scripts with Power Automate, see [Run Office Scripts with Power Automate](/en-us/office/dev/scripts/develop/power-automate-integration).
8. Select **Save**.

    It can take up to 48 hours for changes to Office Scripts settings to take effect.

## Manage the availability of Office Scripts in Excel desktop by using Group Policy

Group Policy has a setting to control whether Office Scripts (including the relevant commands on the **Automate** tab) are available for use.

If you enable this policy setting, Office Scripts won't be available for use in the installed Excel app on a desktop. You'll find Office Scripts settings under User Configuration\Administrative Templates\Microsoft Excel 2016\Miscellaneous in the Group Policy Management Console.

After applying this policy setting, users will still see the **Automate** tab, but the **Office Scripts** and **Automate** options will be greyed out. They can select the **Record Actions** button, but if they do, they'll see the following message: "You don't have access to Office Scripts. Your organization's admin may have turned off this feature, or you don't meet the requirements."

To learn more, see [Use Group Policy to configure update settings for Microsoft 365 Apps](/en-us/deployoffice/configure-update-settings-microsoft-365-apps#use-group-policy-to-configure-update-settings-for-microsoft-365-apps).

## Office Scripts admin controls transition

The management of Office Scripts admin controls is moving from the Microsoft 365 admin center to the Microsoft 365 Cloud Policy service. After October 27, 2025, admins will no longer be able to make changes to their old settings in the Microsoft 365 admin center. Any existing settings need to be moved to the Cloud Policy service by this date to ensure that they are honored. If you don't configure the settings by then, then all three will be set to the default value of enabled.

The three settings moving to the Cloud Policy service are:

- Let users automate their tasks in Excel
- Let users with access to Office Scripts share their scripts with others in the organization
- Let users with access to Office Scripts run their scripts with Power Automate

You only need to take action if you've changed these settings from their default value of enabled. If you haven't changed the settings, then no action is required. If you've customized any of the settings, then you need to configure their equivalent in the Microsoft 365 Cloud Policy service before October 20, 2025. For an overview of how to manage policies using the Cloud Policy service, see [Overview of Cloud Policy service for Microsoft 365](/en-us/microsoft-365-apps/admin-center/overview-cloud-policy).