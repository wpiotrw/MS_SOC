---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Wipe devices in Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-wipe-devices?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
ms.date: 2025-08-14T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-security
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- basic-mobility-security
- trust-pod
ms.custom:
- AdminSurgePortfolio
- admindeeplinkMAC
- basic-mobility-security
- security
search.appverid:
- MET150
description: Admins can learn how to factory reset devices, remove company data from devices, and remove devices from management in Basic Mobility and Security.
locale: en-us
document_id: 4fc22f21-2f0b-56f5-3657-629442d66bc9
document_version_independent_id: 4fc22f21-2f0b-56f5-3657-629442d66bc9
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-wipe-devices.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365b-devices-basic-mobility-security-wipe-devices
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-wipe-devices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: cb00d872-1d05-3171-e64c-7c54eddb8c22
---

# Wipe devices in Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn

Mobile devices can store sensitive organizational information and provide access to your organization's Microsoft 365 resources. Admins can remotely remove company data from devices that are [enrolled in Basic Mobility and Security](m365b-devices-basic-mobility-security-enroll-devices). The following actions are available:

- **Factory reset**: Delete all data on the device, including all installed apps, photos, and personal information. This action returns the device to factory default settings. Typically, you use this action on company owned devices. For example:

    - Lost or stolen devices.
    - Reassigned devices before you reassign them.
- **Remove company data**: Remove only organization data from the device. Personal data, photos, and apps aren't affected. Typically, you use this action on personal devices when a user leaves the company. Removing company data has the following effects based on the device platform:

    - Policy settings applied by Basic Mobility and Security are no longer enforced; users can change the device settings. Applies to:

        - iOS/iPadOS
        - Android
    - Email profiles created by Basic Mobility and Security are removed and cached email is deleted. Applies to:

        - iOS/iPadOS

        Tip

        The **Require managing email profile** (*RequireEmailProfile*) setting is required in the applicable policy to remove company data.
- **Delete**: Remove the device from management by Basic Mobility and Security. The result is equivalent to **Remove company data**.

Regardless of your selection, the request is immediately sent to the device:

- The device is marked as not compliant in Microsoft Entra ID.
- The device is removed from the list of managed devices on the **Fully managed** tab of the **Active devices** page in the Microsoft 365 admin center.

## What do you need to know before you begin?

- You open the **Active devices** page for Basic Mobility and Security at https://admin.microsoft.com/Adminportal/Home?#/IntuneDevices/?isMifo=true.
- You need to be assigned permissions before you can do the procedures in this article. You have the following options:

    - [Microsoft Entra permissions](/en-us/entra/identity/role-based-access-control/manage-roles-portal): Membership in the **Global Administrator**^\*^ or **Cloud Device Administrator** roles gives users the required permissions *and* permissions for other features in Microsoft 365.

        Important

        ^\*^ Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.
- You can't use a delegated admin account to manage Basic Mobility and Security. For more information about delegated administration, see [Partners: Offer delegated administration](https://support.microsoft.com/office/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e).
- Questions? See the [Basic Mobility and Security FAQ](m365b-devices-basic-mobility-security-overview#basic-mobility-and-security-faq).

## Wipe a device

1. On the **Overview** tab of the Basic Mobility and Security page at https://compliance.microsoft.com/basicmobilityandsecurity, select **Manage devices**. Or, to go directly to the **Active devices** page, use https://admin.microsoft.com/Adminportal/Home?#/IntuneDevices/?isMifo=true.

    Devices on the **Fully managed** tab are enrolled in Basic Mobility and Security.
2. On the **Fully managed** tab of the **Active devices** page, do one of the following steps to select the device or devices you want to wipe:

    - Select the check box next to the **Device name** column of one or more devices.
    - Clicking anywhere in the row other than the check box next to the **Device name** column to open the details flyout.
    - Select **⋮** in the **Device name** column.
3. Select one of the following actions:

    - ![](../../media/m365-cc-sc-remove-company-data-icon.png)**Remove company data**: Delete only Microsoft 365 organization information. Read the information in the confirmation dialog that opens, and then select **Remove data**.
    - ![](../../media/m365-cc-sc-factory-reset-icon.png)**Factory reset**: Wipe the device and return it to factory settings. Read the information in the confirmation dialog that opens, and then select **Factory Reset**.
    - ![](../../media/m365-cc-sc-delete-icon.png)**Delete**: Equivalent to **Remove data**. Read the information in the confirmation dialog that opens, and then select **Delete**.

Tip

You can configure device security policies in Basic Mobility and Security to automatically factory reset devices after a specified number of unsuccessful device password attempts (the **Number of sign-in failures before device is wiped** setting). For more information, see [Access requirement settings in Basic Mobility and Security](m365b-devices-basic-mobility-security-overview#access-requirement-settings) and [Configure policies in Basic Mobility and Security](m365b-devices-basic-mobility-security-policies-configure).