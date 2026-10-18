---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Enable developers to use app analytics in the Developer Portal for Teams - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/enable-dev-analytics?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: kwekua
author: kwekuako
manager: scotv
ms.date: 2025-04-14T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-enterprise
ms.subservice: administration
ms.localizationpriority: medium
ms.reviewer: luywang
ms.collection:
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_O365_Setup
- must-keep
- operations-pod
ms.custom:
- admindeeplinkMAC
search.appverid:
- MET150
description: Enable developers to view and use app analytics for company apps in the Developer Portal using the Developer Portal for Teams setting.
locale: en-us
document_id: 5cd93b02-75dc-73ce-8837-703999f73320
document_version_independent_id: 5cd93b02-75dc-73ce-8837-703999f73320
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/enable-dev-analytics.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/enable-dev-analytics
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/enable-dev-analytics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 41bed80c-26ee-b2bd-3cc6-c25092cac3a9
---

# Enable developers to use app analytics in the Developer Portal for Teams - Microsoft 365 admin | Microsoft Learn

In the Microsoft 365 admin center, the **App usage for custom app** setting allows enterprise app developers to view and use app analytics for company apps in the Developer Portal. Developer Portal is a tool for managing apps and agents built for Copilot and Microsoft 365 apps. By viewing custom app usage, enterprise developers can see the number of active users and get other insights. Admins can allow app usage for your custom apps to be shown in the Developer Portal.

[![Image of the UI for enabling dev analytics.](../../media/enable-dev-analytics/enable-dev-analytics.png)](../../media/enable-dev-analytics/enable-dev-analytics.png#lightbox)

To enable the setting, in the Microsoft 365 Admin Center, sign in with the **Teams admin** role or **Global admin** role, and under **Org settings**, select **Developer Portal for Teams** and then enable the setting in the flyout pane as shown in the following image:

![Image of the flyout pane where you can enable the setting.](../../media/enable-dev-analytics/enable-dev-analytics-flyout.png)

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

## How will this setting affect admins and their organization?

By default, the **App usage for custom apps** setting is disabled. When you enable this setting, enterprise developers are provided with better insights into the performance and user engagement of custom apps, helping them make informed decisions about app improvements. If this setting is disabled, developers may be prevented from understanding app usage and other insights, causing disruptive change to their workflow.

## What actions are needed from admins?

To enable enterprise developers to view app usage, enable the setting in **Microsoft 365 admin center -&gt; Settings -&gt; Org settings -&gt; Services -&gt; Developer Portal for Teams**. Developers should be able to take advantage of the new experience right away.

## What do developers need to do?

Developers can configure access to analytics for company apps by following the guidance in [Analyze app usage in Developer Portal](/en-us/microsoftteams/platform/concepts/build-and-test/analyze-your-apps-usage-in-developer-portal?tabs=custom-apps-built-for-your-org#tabpanel_1_custom-apps-built-for-your-org).