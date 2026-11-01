---
layout: Conceptual
title: Data Quality Alerts in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-alerts
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2024-04-08T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to use data quality alerts and notifications in Microsoft Purview Unified Catalog to notify users when data quality misses expectations, so they can drive quick resolutions.
ms.custom: sfi-image-nochange
locale: en-us
document_id: df6495cd-a7be-2df5-dcaa-e3b41d502d2c
document_version_independent_id: df6495cd-a7be-2df5-dcaa-e3b41d502d2c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-alerts.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-alerts
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-alerts.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 8b47102e-f98a-b140-3997-ba70d3b984f7
---

# Data Quality Alerts in Unified Catalog | Microsoft Learn

Data quality alerts notify you about important events or unexpected behavior detected around the quality of the data. When you create alerts for data assets, you receive email notifications about data quality scores.

## Required roles

To create data quality alerts, you need the [data quality steward role](data-governance-roles-permissions#how-to-assign-governance-domain-roles).

## Set data quality alerts

1. In Microsoft Purview Unified Catalog, select **Health management**, then select **Data quality**.
2. On the **Data Quality** page, select a governance domain from the list.
3. Select **Manage**, then select **Alerts**.
4. Select **New** to set up a new alert for the data products and data assets in your selected governance domain.
5. On the **Overview** tab, enter a **Display name** and a **Description**.
6. For **Target**, select any of the following options:

    - **Score less than**: Alerts you if the assets' data quality score is less than certain percentage.
    - **Score decreased by more than**: Alerts you if the current quality score drops by certain percentage after a new scan is run.
7. Select the threshold that triggers an alert.
8. Select **Turn on notifications** for failed quality scan to enable alert notifications.
9. Add a **Recipient** to send the notification email to the recipient alias.

    ![Screenshot of the create alert menu overview page.](media/how-to-data-quality-notifications/dq-create-alerts.png)
10. Select **Continue** to define the scope of alerts.
11. On the **Scope** tab, select data products and data assets that the alert will monitor, then select **Save**.
12. Select **Continue** to review.
13. Check alert details on the **Review** tab, then select **Submit** to create the alert.

## Disable data quality alerts

Alerts are enabled by default. To disable an alert:

1. In Unified Catalog, select **Health management**, then select **Data quality**.
2. On the **Data Quality** page, select a governance domain from the list.
3. Select **Manage**, then select **Alerts**.
4. Select the **Notifications** toggle next to the alert, or select the alert and select the **Turn off notifications** checkbox.

    ![Screenshot of the create alert menu review page.](media/how-to-data-quality-notifications/dq-disable-alerts.png) .

Note

Disabling an alert stops the sending of notification emails related to the assets within the alert's scope.