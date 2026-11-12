---
layout: Conceptual
title: Monitor Data Quality Jobs in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-job-monitor
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how data quality stewards can monitor data quality profiling and scanning jobs in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 0b6911d8-9dc4-858b-3552-ca465bd25b9a
document_version_independent_id: 0b6911d8-9dc4-858b-3552-ca465bd25b9a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-job-monitor.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-job-monitor
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-job-monitor.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: b86fdfdd-f2e2-194b-3072-d4cd3b27e3f9
---

# Monitor Data Quality Jobs in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Data quality job monitoring enables [data quality stewards](data-gov-classic-permissions#roles) to see the progress of [data profiling](unified-catalog-data-quality-profiling), [data quality rule generation](unified-catalog-data-quality-rules), and [data quality scanning jobs](unified-catalog-data-quality-scan). You can view the progress of both manually configured and scheduled jobs from the data quality monitoring page.

## Browse data quality job status

1. In Microsoft Purview Unified Catalog, select **Health Management**, then select **Data quality**.
2. Select a **governance domain**.
3. From the **Manage** dropdown menu, select **Monitoring**.
4. The **Activities** tab shows a summary of all activities. Use the filters to scope your view by submit time, status, activity type, scan type, or scan name. Select the activity for more details.
5. You can switch between governance domains from this menu, using the governance domain tab next to the page title.
6. Select the **Scan** tab to see the progress of scheduled scans.
7. Select and open a completed job for a data asset. Under **Scan details**, you can view the processing units consumed at **PU consumed**. To calculate the cost of the data quality job, multiply the **PU consumed** with SKU cost.