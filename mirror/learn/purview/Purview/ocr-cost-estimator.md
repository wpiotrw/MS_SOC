---
layout: Conceptual
title: Estimate your OCR costs (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ocr-cost-estimator
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.date: 2026-06-22T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Use the OCR Cost Estimator to project optical character recognition scanning costs before deployment.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: fa0718be-5bb2-4a41-6ee7-8c3964d3da14
document_version_independent_id: fa0718be-5bb2-4a41-6ee7-8c3964d3da14
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ocr-cost-estimator.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ocr-cost-estimator
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ocr-cost-estimator.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: cf1f5975-d994-0649-7bdd-c5d916a45cb3
---

# Estimate your OCR costs (preview) | Microsoft Learn

You can use the OCR cost estimator tool (preview) to estimate your optical character recognition (OCR) scanning costs. The tool scans your selected locations—such as Exchange, SharePoint, OneDrive, Teams, and Endpoint—and projects how much OCR processing will cost before you enable it. Use this article to run an estimation, review the results, and download cost reports.

## Prerequisites

To enable the OCR cost estimator tool on Endpoint, you must first install the latest Windows Update released on February 29, 2024 or later.

## Estimate your bill

To estimate your bill, follow these instructions:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings**.
3. Select **Optical character recognition (OCR)**
4. Under **Estimate the cost of an OCR scan for free**, select **Try for free**.
5. In the flyout pane, select the locations where the files you want to scan are found and then choose **Run estimation**.
6. After **Estimation started successfully** displays in the flyout pane, select **View estimation** next to **Predict OCR cost estimate for free** to view the **Estimation** page.
7. To enable OCR scans from the **Estimation** page, select **Turn on OCR** in the flyout pane and then follow the steps to [configure your OCR settings](ocr-learn-about#configure-your-ocr-settings).

Note

Running an OCR estimation can take around 24 hours to complete the first time. After the first estimation completes, the dashboard is refreshed daily and can be viewed anytime.

### Edit the scope of your estimate

To change which locations are included in the estimate, follow these steps:

1. On the **Estimation** page, select **Edit scope** from the dropdown menu next to **Enable OCR**.
2. In the flyout pane, edit the locations with files that you wish to scan and then select **Restart estimation**.

### Download your estimate

To download your estimate reports, follow these steps:

1. On the **Estimation** page, select **Download Report** from the dropdown menu next to **Enable OCR**.
2. In the flyout pane, select **Download all**, or select the individual reports you want to download.

### Cancel an in-progress estimate

To cancel an estimate that is currently running, follow these steps:

1. On the **Estimation** page, Select **Stop estimation** from the dropdown menu next to **Enable OCR**.
2. On the next page, confirm your choice.

### Restart a stopped estimate

To restart a stopped estimate, follow these steps:

1. On the **Estimation** page, select **Start estimation** from the dropdown menu next to **Enable OCR**.
2. In the flyout pane, edit the locations with files that you wish to scan and then select **Start estimation**.

### Limitations

Be aware of the following limitations when using the OCR cost estimator:

- OCR and OCR cost estimator can't run at the same time.
- OCR cost estimator can be used only once by a customer and can't be re-enabled. Once turned on, you will have 90 days to complete 30-day estimation. You may pause the estimation any number of times
- Reports must be downloaded after using estimator. The data from dashboards is deleted after 90 days from the date estimator is first turned on.
- Estimation for embedded and standalone image is only supported for the Exchange workload. Estimation for embedded images in SharePoint and OneDrive is not supported yet.
- Estimation of images in pdf files is supported in Exchange and Teams. Estimation of images in pdf files isn't supported in SharePoint and OneDrive. As a result, your actual OCR bill for SharePoint and OneDrive may be higher than estimated, since OCR will run in SharePoint and OneDrive on all supported file types listed in [Supported file types](ocr-learn-about#supported-file-types)
- For Endpoint, each pdf file is estimated to have an image count of 4. This is the current average with OCR customers.
- In Exchange and Teams, there is the ability to cache small images, such as logos or email signatures, without being charged.
- Downloaded reports show the **To Date** in the **Estimation Timeframe** column as the date of latest scan (current date in case of ongoing scan) for all the rows in the report.
- All incoming emails and Teams messages from outside the organization are estimated if the scope is set to "ALL" when configuring OCR Cost Estimator for Exchange and Teams.
- All dashboards are reset when you restart estimation. Use the download report of the scan history before restarting an estimation. Even with the same location and scope, estimation can be restarted from scratch.