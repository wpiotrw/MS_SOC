---
layout: Conceptual
monikers:
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Enable Group Level Aggregates in Adoption Score - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/adoption/group-level-aggregates?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-06-05T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: activity-reports
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
search.appverid:
- MET150
- MOE150
description: Use Group Level Aggregates in Adoption Score to compare groups, focus on specific teams, and get actionable insights for your organization. Learn how.
locale: en-us
document_id: 70d902a1-c74f-91b1-0ef4-39682c2174d3
document_version_independent_id: 70d902a1-c74f-91b1-0ef4-39682c2174d3
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/adoption/group-level-aggregates.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/adoption/group-level-aggregates
moniker_range_name: 2ccba01628bf08e8f21ea76d73b162e1
monikers:
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/adoption/group-level-aggregates.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: b47d678b-bede-5a59-af7a-64f544fd49bd
---

# Enable Group Level Aggregates in Adoption Score - Microsoft 365 admin | Microsoft Learn

Group Level Aggregates in Adoption Score help admins and adoption strategists compare how different groups perform in people experiences insights. This article explains how to enable group-level insights and use Microsoft Entra ID data to identify groups that are doing well and groups that need growth in Microsoft 365.

- **Compare** different groups of your organization to understand the overall distribution of adoption scores and insights, groups that are doing well, and groups that need growth.
- **Focus** on a specific group of your organization to understand more about it in isolation.

## How to enable Group Level Aggregates

Group Level Aggregates isn't enabled by default.

Note

Only the Global administrator role can enable Group Level Aggregates.

To enable Group Level Aggregates:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select **Org settings**.
4. In the **Org settings** page, make sure the **Services** tab is selected, and then select **Adoption Score** in the list of services.
5. In the **Adoption Score** pane, make sure the **Insights calculation and display** tab is selected. Under **Group data filtering**, select **Turn on group-level insights**.

Once enabled, all roles on the people experiences pages can access it.

[![Screenshot of turning on group-level insights in Adoption Score.](../../media/enable-group-level-insights-adoption-score.png)](../../media/enable-group-level-insights-adoption-score.png#lightbox)

## Data accuracy evaluation

Before you can enable group-level insights, run a data accuracy evaluation to check if group data is accurate. The evaluation helps you make an informed decision about which segments best reflect your organization's composition.

[![Screenshot of a warning to run a data accuracy evaluation before enabling group-level insights.](../../media/group-level-insights-data-accuracy.jpg)](../../media/group-level-insights-data-accuracy.jpg#lightbox)

The data accuracy evaluation check is a report that reflects the organization's composition based on key attributes in Microsoft Entra ID.

Currently, Microsoft Entra ID provides capabilities for five attributes:

- Company.
- Department.
- Country.
- State.
- City.

The report displays the number of users included for all the different organizational attributes out of the total number of users in Microsoft Entra ID. This data is included based on an entry in the Entra ID fields for those five selected attributes. You can download the report for these five attributes and check for data accuracy. You only run and approve this report once while setting up Group Level Aggregates.

For example, in the following screenshot, the organization has the **Department** attribute filled for XX out of the total YY users with ZZ unique departments mentioned. You see ZZ unique departments in the Group Level Aggregates filters on people experience insights pages.

[![Screenshot of the group-level data evaluation report.](../../media/group-level-aggregates-data-evaluation.png)](../../media/group-level-aggregates-data-evaluation.png#lightbox)

To include all users in the group-level insights reporting, make sure the five fields are accurately updated for all users in Microsoft Entra. For subsequent updates to the Microsoft Entra attributes, you don't need to run the evaluation again. The updates are available immediately. For more information about how to update user data in Microsoft Entra, see [Add or update a user's profile information and settings in the Microsoft Entra admin center](/en-us/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal).

## Filter people experiences scores

Group-level insights on people experience insights help filter the overall score and each insight for the selected group. When you apply certain filters, the portal displays an informative message when some insights aren't available.

Note

In some cases, you might not see an entire group in the filters despite all data being accurate in Microsoft Entra ID. This behavior happens when the group has fewer than 10 individuals for that unique group. This behavior protects user privacy so that no insights can be directly correlated to individual users.

[![Screenshot of filters for group-level insights in Adoption Score.](../../media/group-level-aggregates-filters.png)](../../media/group-level-aggregates-filters.png#lightbox)