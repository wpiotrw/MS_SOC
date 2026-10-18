---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft 365 Apps Activations Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-office-activations-ww?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: cmcatee
author: cmcatee-MSFT
manager: scotv
ms.reviewer: hlu
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
ms.custom: 
ai-usage: ai-assisted
description: The Microsoft 365 Apps Activations report shows which users activated Microsoft 365 across desktops and devices. Learn how to view activations and support users who need help.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: 13582148-2da8-0605-1c5e-acd961e9a12d
document_version_independent_id: 13582148-2da8-0605-1c5e-acd961e9a12d
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-office-activations-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-office-activations-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-office-activations-ww.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e2c9f30c-00ec-44c0-846c-b20dbfb3283f
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/702271fe-87d7-4493-828b-2d6fde3de8ab
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 436696de-7d67-3761-bae3-5617e5d9689f
---

# Microsoft 365 Apps Activations Report - Microsoft 365 admin | Microsoft Learn

The Microsoft 365 Apps Activations report provides details about which users activated their Office subscription on at least one device. It provides a breakdown of the Microsoft 365 Apps for enterprise, Project, and Visio Pro for Microsoft 365 subscription activations, as well as the breakdown of activations across desktop and devices. This report can help you identify users who might need extra help and support to activate their Office subscription.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Microsoft 365 Apps Activations report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Microsoft 365 apps**, and then select the **Activations** tab.

## Interpret the Microsoft 365 Apps Activations report

[![Screenshot shows Microsoft 365 reports - Microsoft Office 365 activation.](../../media/e1df82a2-3336-4b38-b66c-b286c44b82ee.png)](../../media/e1df82a2-3336-4b38-b66c-b286c44b82ee.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Office 365 activations report column options.](../../media/d11a0efa-a067-4440-a4f3-71b618a90301.png)](../../media/d11a0efa-a067-4440-a4f3-71b618a90301.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| Username | The email address of the user. |
| Display name | The full name of the user. |
| Product licenses | The products that are assigned to this user. |
| Last activated date(UTC) | The date the user activated Microsoft 365 on a desktop or a device. |
| Activation on Windows computers | The number of Windows desktops a user activated Microsoft 365 on. |
| Activation on Mac computers | The number of Mac desktops a user activated Microsoft 365 on. |
| Activation on Windows 10 phones and tablets | The number of Windows 10 mobile devices a user activated Microsoft 365 on. |
| Activation on iOS phones and tablets | The number of iOS devices a user activated Microsoft 365 on. |
| Activation on Android phones and tablets | The number of Android devices a user activated Microsoft 365 on. |
| Used Shared Computer Activation | This metric is true if the user used Microsoft 365 through shared computer activation. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).