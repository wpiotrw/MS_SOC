---
layout: Conceptual
title: Data Health Management in Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-health-management
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
description: Learn about health management for your organization's data in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 7916471c-e7ce-08f8-1ed5-b436478d4efe
document_version_independent_id: 7916471c-e7ce-08f8-1ed5-b436478d4efe
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-health-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-health-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-health-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 40d6073a-9e77-f19a-3821-9b39a58a1025
---

# Data Health Management in Microsoft Purview Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Health management refers to the ongoing processes and practices that ensure an organization's data remains accurate, complete, consistent, secure, and accessible throughout its lifecycle. It's a critical aspect of data governance, focusing on maintaining the overall "health" of data, much like how healthcare practices aim to maintain the health of individuals.

**Importance of health management:**

- **Informed decision-making:** High-quality, reliable data is essential for making informed business decisions.
- **Operational efficiency:** Healthy data reduces the time and resources spent on correcting errors and reconciling inconsistencies.
- **Risk management:** Proper data health management helps mitigate risks associated with data breaches, regulatory noncompliance, and inaccurate reporting.
- **Competitive advantage:** Organizations with healthy data are better positioned to leverage analytics, AI, and machine learning, leading to better insights and innovations.
- **Customer trust:** Ensuring data privacy and accuracy builds trust with customers and partners.

In summary, health management is about maintaining the integrity, reliability, and security of data throughout its lifecycle, ensuring that it remains a valuable asset to the organization.

Unified Catalog health management provides four key components and tools to help you understand your data and develop your data governance strategies:

- Controls
- [Data quality](unified-catalog-data-quality)
- Actions
- Reports

You can find these tools by opening **Unified Catalog** in the Microsoft Purview portal and selecting **Health management**.

This article provides a brief overview of each tool, its scope, and how you can use it to understand your data and develop your data governance strategies. Users need the **Data health owner** and **Data health reader** roles to access and configure rules for controls and to browse built-in reports.

| Role | Description | Application |
| --- | --- | --- |
| Data health owner | Create, update, and read artifacts in health management. | Health management |
| Data health reader | Can read artifacts in health management. | Health management |

## Controls

Controls help data stewards and chief data officers evaluate the health of their data estate through industry-recognized standards and controls. Set control rules at a global level but leave execution to individual [governance domains](concept-business-domain). This approach lets you set broad standards while meeting the needs of individual groups in your organization.

If you're a [data health owner](data-governance-roles-permissions#catalog-level-permissions), you can edit controls and change the preset health ranges and thresholds to customize how you measure the success of your data estate. You can also edit the schedule for the overall data refresh rate for all active controls. For more information, see the [Health management controls article](unified-catalog-controls).

[![Screenshot of the health controls page in health management.](media/data-estate-health/data-estate-health-controls-inline.png)](media/data-estate-health/data-estate-health-controls.png#lightbox)

## Data quality

Microsoft Purview Data Quality is a comprehensive solution that empowers governance domain and data owners to assess and oversee the quality of their data ecosystem, facilitating targeted actions for improvement. In today's AI-driven landscape, the reliability of data directly impacts the accuracy of AI-driven insights and recommendations. Without trustworthy data, there's a risk of eroding trust in AI systems and hindering their adoption.

Microsoft Purview Data Quality also incorporates AI-powered data profiling capabilities, recommending columns for profiling while allowing human intervention to refine these recommendations. This iterative process not only enhances the accuracy of data profiling but also contributes to the continuous improvement of the underlying AI models.

[![Screenshot of data quality overview page in health management.](media/data-estate-health/data-quality-overview.png)](media/data-estate-health/data-quality-overview.png#lightbox)

## Actions (preview)

Health actions give data governance practitioners truly actionable insights. All the anomalies that health controls note become actions, alerts with owners, and recommendations that you can track and address from within Unified Catalog.

As a [data steward](data-governance-roles-permissions#governance-domain-level-permissions), you can review actions and filter the list by finding type, finding subtype, and finding name. You can assign a task to anyone in your organization, and that user sees the action in their list. These actions update on the same [schedule as the health controls](unified-catalog-controls#schedule-control-refresh), since actions come from the controls themselves.

Get details about [viewing all actions on the Actions (preview) page](unified-catalog-data-health-management-actions-page).

[![Screenshot of the health actions page in health management.](media/data-estate-health/data-estate-health-actions-inline.png)](media/data-estate-health/data-estate-health-actions.png#lightbox)

## Reports

Data analysts and stewards in the federated data governance office can view built-in reports for deeper analysis of the data estate. These reports give summaries of individual business concepts like governance domains or data products. They also address data governance goals, catalog adoption, and asset information like classification. For more information, see the [health management reports article](unified-catalog-reports).

[![Screenshot of the reports page in health management.](media/data-estate-health/reports-inline.png)](media/data-estate-health/reports.png#lightbox)