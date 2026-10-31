---
layout: Conceptual
title: Apply the prediction score filter to a review set | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-predictive-coding-apply-prediction-filter
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use a prediction score filter to displays items that a predictive coding model as predicted as relevant or not relevant.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
ms.reviewer: jefwan
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
search.appverid:
- MET150
ms.collection:
- purview-compliance
- ediscovery
locale: en-us
document_id: 7821ee38-d763-35d4-bdd7-f8ebe007efd1
document_version_independent_id: 7821ee38-d763-35d4-bdd7-f8ebe007efd1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-predictive-coding-apply-prediction-filter.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-predictive-coding-apply-prediction-filter
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-predictive-coding-apply-prediction-filter.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 472abee3-f548-dbb4-aef5-b9c47371fd09
---

# Apply the prediction score filter to a review set | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

After you create a predictive coding model in Microsoft Purview eDiscovery (Premium) and train it to the point where it's stable, you can apply the prediction score filter to display review set items that the model has determined are relevant (or not relevant). When you create a model, a corresponding prediction score filter is also created. You can use this filter to display items assigned a prediction score within a specified range. In general, prediction scores between **0** and **.5** are assigned to items that model has predicted are not relevant. Items assigned prediction scores between **.5** and **1.0** are items the model has predicted are relevant.

Here are two ways you can use the prediction score filter:

- Prioritize the review of items in a review set that the model has predicted are relevant.
- Cull items from the review set that the model has predicted aren't relevant. Alternative, you can use the prediction score filter to deprioritize the review of nonrelevant items.

## Before you apply a prediction score filter

- Create a predictive coding model so that a corresponding prediction score filter is created.
- You can apply a prediction score filter after any of the training rounds. But you may want to wait after performing several rounds or until the model is stable before using the prediction score filter.

## Apply a prediction score filter

1. In the Microsoft Purview portal, open the eDiscovery (Premium) case, select the **Review sets** tab, and then open the review set.

    ![Select Filters to display the Filters flyout page.](media/predictionscorefilter0.png)

    The preloaded default filters are displayed at the top of the review set page. You can leave these set to **Any**.
2. Select **Filters** to display the **Filters** flyout page.
3. Expand the **Analytics & predictive coding** section to display a set of filters.

    ![Prediction score filter in the Analytics &amp; predictive coding section.](media/predictionscorefilter1.png)

    The naming convention for prediction score filters is **Prediction score (model name)**. For example, the prediction score filter name for a model named **Model A** is **Prediction score (Model A)**.
4. Select the prediction score filter that you want to use and then select **Done**.
5. On the review set page, select the dropdown for the prediction score filter and type minimum and maximum values for the prediction score range. For example, the following screenshot shows a prediction score range between **.5** and **1.0**.

    ![Minimum and maximum values for the prediction score filter.](media/predictionscorefilter2.png)
6. Select outside the filter to automatically apply the filter to the review set.

A list of documents with a prediction score within the range you specified is displayed on the review set page.

Tip

To view the actual prediction score assign to a document, you can select the **Metadata** tab in the reading pane. The prediction scores for all models in the review set are displayed in the **RelevanceScores** metadata property.

## More information

- For more information about using filters, see [Query and filter content in a review set](ediscovery-review-set-search).