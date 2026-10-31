---
layout: Conceptual
title: Health Management Reports in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-reports
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2025-03-20T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about the health management reports available in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 9bc68aa5-1936-0a46-a495-cd325e613610
document_version_independent_id: 9bc68aa5-1936-0a46-a495-cd325e613610
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-reports.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-reports
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-reports.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 465290fe-a913-01d9-d1c2-542725be96ef
---

# Health Management Reports in Unified Catalog | Microsoft Learn

Data health management reports in Microsoft Purview Unified Catalog enable your users to explore detailed information about your data health management and create customized reports for your organization.

## Report types

### Classic reports

- [Classic assets](unified-catalog-reports-classic-assets): An overview of assets by type and collection, and their curation status.
- [Classic catalog adoption](unified-catalog-reports-classic-catalog-adoption): Helps you see at a glance how the classic Microsoft Purview Data Catalog is being used.
- [Classic classifications](unified-catalog-reports-classic-classifications): An overview of assets classified and the types of classifications.
- [Classic data stewardship](unified-catalog-reports-classic-data-stewardship): Helps governance and quality focused users, like data stewards and chief data officers, understand governance health gaps like asset curation and asset ownership.
- [Classic glossary](unified-catalog-reports-classic-glossary): An overview of the health and use of glossary terms.
- [Classic sensitivity labels](unified-catalog-reports-classic-sensitivity-labels): An overview of assets that have sensitivity labels applied and the types of labels applied.

Note

Classic reports refresh weekly. You can't change the schedule. Classic reports don't have any impact to the [data governance billing model](data-governance-billing). When you consent to using Unified Catalog, the billing model starts, but classic reports have no charge.

### Data governance reports

- [Data governance (preview)](unified-catalog-reports-data-governance): Helps you understand your data estate governance and performance of data governance controls.

    - The data governance (preview) report depends on [data health controls](unified-catalog-controls). If you don't use data health controls, the report isn't refreshed. Make sure that you set up the schedule to run data health controls and refresh the health controls scores and data governance report.
- [Data quality health](unified-catalog-reports-data-quality-health): Includes assessments of various data quality dimensions, and metrics to help stakeholders understand the accuracy, completeness, consistency, reliability, and freshness of your data estate.

    - The data quality health report depends on [data health controls](unified-catalog-controls) and the [Microsoft Purview metadata self-serve analytics](unified-catalog-self-serve-analytics) model. If you don't use data health controls and don't subscribe Unified Catalog metadata, the data quality health report isn't refreshed. You either need to use data health controls or need to subscribe Unified Catalog metadata for self-serve analytics to refresh the data quality health report.
    - If you don't use the data quality feature, the data quality health report shows as blank because the report is created using data generated from data quality scans.

Note

- Data governance (preview) and Data quality health reports are part of the [data governance billing model](data-governance-billing). If you don't want to use these reports, then you need to disable **self-serve analytics metadata subscription**, and you also need to disable the **health controls refresh schedule**. For details, see [self-serve analytics and insights](unified-catalog-self-serve-analytics).