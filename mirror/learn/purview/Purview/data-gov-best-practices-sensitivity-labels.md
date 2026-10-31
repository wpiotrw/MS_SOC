---
layout: Conceptual
title: ' Best practices for applying sensitivity labels in Microsoft Purview Data Map | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-best-practices-sensitivity-labels
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-05-22T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Find best practices for applying sensitivity labels in Microsoft Purview Data Map.
locale: en-us
document_id: 52b19806-aa38-07ff-7a27-84b0410d7398
document_version_independent_id: 52b19806-aa38-07ff-7a27-84b0410d7398
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-best-practices-sensitivity-labels.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-best-practices-sensitivity-labels
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-best-practices-sensitivity-labels.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c8d8c000-c92c-c4ac-e07c-245c7003d5c6
---

#  Best practices for applying sensitivity labels in Microsoft Purview Data Map | Microsoft Learn

Note

These best practices cover [applying sensitivity labels to your data in Data Map](data-map-sensitivity-labels-apply). For more information about applying sensitivity labels in Microsoft Purview risk and compliance solutions, see [Automatically apply a sensitivity label to Microsoft 365 data](apply-sensitivity-label-automatically).

Microsoft Purview Data Map supports labeling structured and unstructured data stored across various data sources. Labeling data within Data Map allows users to easily find data that matches predefined autolabeling rules that were configured in the Microsoft Purview portal. Data Map extends the use of sensitivity labels from Microsoft Purview Information Protection to assets stored in infrastructure cloud locations and structured data sources.

## Protect personal data with custom sensitivity labels for Microsoft Purview

Storing and processing personal data is subject to special protection. Labeling personal data is crucial to help you identify sensitive information. You can use the detection and labeling tasks for personal data in different stages of your workflows. Because personal data is ubiquitous and fluid in your organization, you need to define identification rules for building policies that suit your individual situation.

## Why do you need to use labeling within Data Map

In Data Map, you can extend your organization's investment in sensitivity labels from Microsoft Purview Information Protection to assets that are stored in files and database columns within Azure, multicloud, and on-premises locations. These locations are defined in [supported data sources](data-map-sensitivity-labels#supported-data-sources). When you apply sensitivity labels to your content, you can keep your data secure by stating how sensitive certain data is in your organization. The Data Map also abstracts the data itself, so you can use labels to track the type of data, without exposing sensitive data on another platform.

## Microsoft Purview Data Map labeling best practices and considerations

The following sections walk you through the process of implementing labeling for your assets.

### Get started

- To enable sensitivity labeling in the data map, follow the steps in [automatically apply sensitivity labels to your data in the Microsoft Purview Data Map](data-map-sensitivity-labels-apply).
- To find information on required licensing and helpful answers to other questions, see [Sensitivity labels in the Microsoft Purview Data Map FAQ](data-map-sensitivity-labels-faq).

### Label considerations

- If you already have sensitivity labels from Microsoft Purview Information Protection in use in your environment, continue to use your existing labels. Don't make duplicate or more labels for Data Map. This approach allows you to maximize the investment you've already made in the Microsoft Purview. It also ensures consistent labeling across your data estate.
- If you haven't created sensitivity labels in Microsoft Purview Information Protection, review the documentation to [get started with sensitivity labels](get-started-with-sensitivity-labels). Creating a classification schema is a tenant-wide operation. Discuss it thoroughly before you enable it within your organization.

### Label recommendations

- When you configure sensitivity labels for the Microsoft Purview Data Map, you might define autolabeling rules for files, database columns, or both within the label properties. Microsoft Purview labels files within the Microsoft Purview Data Map. When the autolabeling rule is configured, Microsoft Purview automatically applies the label or recommends that the label is applied.

    Warning

    If you haven't configured autolabeling for items on your sensitivity labels, users might be affected within your Office and Microsoft 365 environment. You can test autolabeling on database columns without affecting users.
- If you're defining new autolabeling rules for files when you configure labels for the Microsoft Purview Data Map, make sure that you have the condition for applying the label set appropriately.
- You can set the detection criteria to **All of these** or **Any of these** in the upper right of the autolabeling for items page of the label properties.
- The default setting for detection criteria is **All of these**. This setting means that the asset must contain all the specified sensitive information types for the label to be applied. While the default setting might be valid in some instances, many customers want to use **Any of these**. Then if at least one asset is found, the label is applied.

    ![Screenshot that shows detection criteria for a label.](media/concept-best-practices/label-detection-criteria.png)

    Note

    Trainable classifiers from Microsoft Purview Information Protection aren't supported by Microsoft Purview Data Map.
- Maintain consistency in labeling across your data estate. If you use autolabeling rules for files, use the same sensitive information types for autolabeling database columns.
- [Define your sensitivity labels via Microsoft Purview Information Protection to identify your personal data at a central place](information-protection).
- [Use policy templates as a starting point to build your rule sets](what-the-dlp-policy-templates-include#general-data-protection-regulation-gdpr).
- [Combine data classifications to an individual rule set](data-map-classification-supported-list).
- [Force labeling by using autolabel functionality](data-map-sensitivity-labels-apply).
- Build groups of sensitivity labels and store them as a dedicated sensitivity label policy. For example, store all required sensitivity labels for regulatory rules by using the same sensitivity label policy to publish.
- Capture all test cases for your labels. Test your label policies with all applications you want to secure.
- Promote sensitivity label policies to the Microsoft Purview Data Map.
- Run test scans from the Microsoft Purview Data Map on different data sources like hybrid cloud and on-premises to identify sensitivity labels.
- Gather and consider insights, for example, by using Microsoft Purview Data Estate Insights. Use alerting mechanisms to mitigate potential breaches of regulations.

By using sensitivity labels with Microsoft Purview Data Map, you can extend information protection beyond the border of your Microsoft data estate to your on-premises, hybrid cloud, multicloud, and software as a service (SaaS) scenarios.