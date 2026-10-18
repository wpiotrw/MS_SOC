---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Upgrade Microsoft 365 Apps for Business Users - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/upgrade-users-to-latest-office-client?view=o365-worldwide
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
ms.date: 2026-06-12T00:00:00.0000000Z
audience: Admin
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- Adm_O365
- Adm_TOC
- operations-pod
search.appverid:
- BCS160
- MET150
- MOE150
ms.custom:
- fwlink 824861; CampaignID
- O365_Comm_SR_UpgradeOffice
- seo-marvel-may2020
- fwlink 824861; CampaignID O365_Comm_SR_UpgradeOffice
- AdminSurgePortfolio
- user-accounts
description: Learn how to upgrade Microsoft 365 apps for business users to get the latest security and productivity features. To start upgrading now, follow the steps in this article.
ms.topic: upgrade-and-migration-article
locale: en-us
document_id: ceb1be80-0fd7-30ea-8829-52638a71e7a7
document_version_independent_id: e069acfc-c11a-2382-b548-a2c74c3db340
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/setup/upgrade-users-to-latest-office-client.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/setup/upgrade-users-to-latest-office-client
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/setup/upgrade-users-to-latest-office-client.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e2c9f30c-00ec-44c0-846c-b20dbfb3283f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/702271fe-87d7-4493-828b-2d6fde3de8ab
platformId: 77e42742-dfcc-ca7c-c96b-3e8ac4f3d9ca
---

# Upgrade Microsoft 365 Apps for Business Users - Microsoft 365 admin | Microsoft Learn

## Get ready to upgrade to Microsoft 365

As an admin, you can upgrade Microsoft 365 apps for business users in your organization. This article explains how to move from older Office versions to the latest apps so users get current security and productivity improvements.

Note

If you have a [Microsoft 365 Family](https://support.microsoft.com/office/28cbc8cf-1332-4f04-9123-9b660abb629e#BKMK_OfficePlans) subscription and an older home version of Office, see the following article on how to upgrade your Office apps:

[How do I upgrade Office?](https://support.microsoft.com/office/ee68f6cf-422f-464a-82ec-385f65391350)

## Upgrade steps

The following steps guide you through the process of upgrading your users to the latest Microsoft 365 desktop apps. Microsoft recommends you read through these steps before beginning the upgrade process.

## Step 1 - Check system requirements

[Check the system requirements](https://support.microsoft.com/office/system-requirements/microsoft-365-and-office-resources) to make sure your devices are compatible with the latest version of Office. For example, newer versions of the apps in Microsoft 365 might not work on devices running versions of Windows that are out of support.

### Check application compatibility

To ensure a successful upgrade, Microsoft recommends identifying your applications and assessing their compatibility with the latest version of Microsoft 365. For example, check the following items:

- VBA scripts.
- Macros.
- Non-Microsoft add-ins.
- Complex documents and spreadsheets.

When necessary, contact non-Microsoft application manufacturers to make sure they're compatible with the latest version of Microsoft 365.

## Step 2 - Check your existing subscription plan

Some Microsoft 365 plans don't include the full desktop versions of the apps. The steps to upgrade are different if your plan doesn't include desktop versions of the apps.

Tip

Not sure which subscription plan you have? See [What Microsoft 365 for business subscription do I have?](../admin-overview/what-subscription-do-i-have)

If your existing plan includes the Microsoft 365 apps, move on to Step 3 - Uninstall Office.

If your existing plan doesn't include the Microsoft 365 apps, then select from one of the following three options:

- **Switch subscriptions**: Switch to a subscription that includes the Microsoft 365 productivity apps. For more information, see [Switch to a different Microsoft 365 for business plan](../../commerce/subscriptions/switch-to-a-different-plan).
- **Buy an individual subscription of Microsoft 365**: For more information, see [Microsoft 365 Family & Business](https://www.microsoft.com/microsoft-365/buy/compare-all-microsoft-365-products)
- **Buy multiple copies of Office through a volume license**: For more information, see [Compare suites available through volume licensing](https://products.office.com/business/microsoft-office-volume-licensing-suites-comparison).

## Step 3 - Uninstall Office

Before you install the latest version of Microsoft 365, uninstall all older versions of the Office apps. However, if you change your mind about upgrading, note the following instances where you can't reinstall Office apps after uninstalling it:

- **Office through a volume license**: If you no longer have access to the source files from a volume license version, you can't reinstall Office.
- **Office preinstalled on your computer**: If you don't have an Office install disk or Office product key, you can't reinstall Office.
- **Non-supported subscriptions**: You can't reinstall Office if the following conditions apply:

    - Your copy of Office was obtained through a subscription that is no longer supported. Examples of subscriptions that are no longer supported include Office 365 Small Business Premium and Office 365 Mid-size Business.
    - You don't have the Office product key that came with your subscription.

Certain older versions of Office can be installed side-by-side with the latest version of Microsoft 365. If you have one of these versions, you can choose to keep it installed and use it alongside the latest version of Microsoft 365. For more information, see [Install and use different versions of Office on the same PC](https://support.microsoft.com/office/6ebb44ce-18a3-43f9-a187-b78c513788bf). If you have a version of Office that doesn't support side-by-side installation, you need to uninstall it before you install the latest version of Microsoft 365.

To uninstall Office, select one of the following options based on your operating system:

- [Uninstall Microsoft 365 or Office from Windows](https://support.microsoft.com/office/9dd49b83-264a-477a-8fcc-2fdf5dbf61d8)
- [Uninstall Office for macOS](https://support.microsoft.com/office/eefa1199-5b58-43af-8a3d-b73dc1a8cae3)

## Step 4 - Assign licenses to users

Assign licenses to any users in your organization who need to install the latest version of Microsoft 365. For more information, see [Assign licenses to users in Microsoft 365 for business](../manage/assign-licenses-to-users).

## Step 5 - Install Microsoft 365 apps

After verifying the users you want to upgrade have the required licenses, the final step is to have them install the Microsoft 365 apps. For more information, see [Download and install or reinstall Microsoft 365 or Office 2021 on a PC or Mac](https://support.microsoft.com/office/4414eaaf-0478-48be-9c42-23adc4716658).

Tip

If you don't want your users installing Office themselves, see [Manage Microsoft 365 installation options in the Microsoft 365 admin center](/en-us/DeployOffice/manage-software-download-settings-office-365). You can use the [Office Deployment Tool](/en-us/DeployOffice/overview-office-deployment-tool) to download apps to your local network and then deploy using the software deployment method your organization typically uses.