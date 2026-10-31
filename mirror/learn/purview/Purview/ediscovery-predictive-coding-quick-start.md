---
layout: Conceptual
title: Predictive coding in eDiscovery (Premium) - Quick start | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-predictive-coding-quick-start
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to get started using the predictive coding module in eDiscovery (Premium). This article walks you through the end-to-end process of using predictive coding to identify content in a review set that's most relevant to your investigation.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
ms.reviewer: jefwan
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
manager: laurawi
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
search.appverid:
- MET150
ms.collection:
- purview-compliance
- ediscovery
locale: en-us
document_id: 83d80095-ee02-b7af-404b-e4706436ee6b
document_version_independent_id: 83d80095-ee02-b7af-404b-e4706436ee6b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-predictive-coding-quick-start.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-predictive-coding-quick-start
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-predictive-coding-quick-start.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 856b4668-54c5-c7a0-e4ae-a6db9b9cc71a
---

# Predictive coding in eDiscovery (Premium) - Quick start | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

This article presents a quick start for using predictive coding in Microsoft Purview eDiscovery (Premium). The predictive coding module uses intelligent, machine learning capabilities to help you cull large volumes of case content that's not relevant to your investigation. This is accomplished by creating and training your own predictive coding models that help you prioritize the most relevant items for review.

Here's an a quick overview of the predictive coding process:

![Quick start process for prediction coding.](media/predictivecodingquickstartprocess.png)

To get started, you create a model, label as few as 50 items as relevant or not relevant. The system then uses this training to apply prediction scores to every item in the review set. This lets you filter items based on the prediction score, which allows you to review the most relevant (or non-relevant) items first. If you want to train models with higher accuracies and recall rates, you can continue labeling items in subsequent training rounds until the model stabilizes. Once the model is stabilized, you can apply the final prediction filter to prioritize items to review.

For a detailed overview of predictive coding, see [Learn about predictive coding in eDiscovery (Premium)](ediscovery-predictive-coding-overview).

## Step 1: Create a new predictive coding model

The first step is to create a new predictive coding model in the review set:

1. In the Microsoft Purview portal, open an eDiscovery (Premium) case and then select the **Review sets** tab.
2. Open a review set and then select **Analytics** &gt; **Manage predictive coding (preview)**.

    ![Select the Analyze dropdown menu in review set to go to the Predictive coding page.](media/managepredictivecoding.png)
3. On the **Predictive coding models (preview)** page, select **New model**.
4. On the flyout page, type a name for the model and an optional description.
5. Select **Save** to create the model.

    It will take a couple minutes for the system to prepare your model. After it's ready, you can perform the first round of training.

For more detailed instructions, see [Create a predictive coding model](ediscovery-predictive-coding-create-model).

## Step 2: Perform the first training round

After you create the model, the next step is to complete the first training round by labeling items as relevant or not relevant.

1. Open the review set and then select **Analytics** &gt; **Manage predictive coding (preview)**.
2. On the **Predictive coding models (preview)** page, select the model that you want to train.
3. On the **Overview** tab, under **Round 1**, select **Start next training round**.

    The **Training** tab is displayed and contains 50 items for you to label.
4. Review each document and then select **Relevant** or **Not relevant** at the bottom of the reading pane to label it.

    ![Label each document as relevant or not relevant.](media/trainmodel1.png)
5. After you've labeled all 50 items, select **Finish**.

    It will take a couple minutes for the system to "learn" from your labeling and update the model. When this process is complete, a status of **Ready** is displayed for the model on the **Predictive coding models (preview)** page.

For more detailed instructions, see [Train a predictive coding model](ediscovery-predictive-coding-train-model).

## Step 3: Apply the prediction score filter to items in review set

After you perform at lease one training round, you can apply the prediction score filter to items in review set. This lets you review the items the model has predicted as relevant or not relevant.

1. Open the review set.

    ![Select Filters to display the Filters flyout page.](media/predictionscorefilter0.png)

    The pre-loaded default filters are displayed at the top of the review set page. You can leave these set to **Any**.
2. Select **Filters** to display the **Filters** flyout page.
3. Expand the **Analytics & predictive coding** section to display a set of filters.

    ![Prediction score filter in the Analytics &amp; predictive coding section.](media/predictionscorefilter1.png)

    The naming convention for prediction score filters is **Prediction score (model name)**. For example, the prediction score filter name for a model named **Model A** is **Prediction score (Model A)**.
4. Select the prediction score filter that you want to use and then select **Done**.
5. On the review set page, select the dropdown for the prediction score filter and type minimum and maximum values for the prediction score range. For example, the following screenshot shows a prediction score range between **.5** and **1.0**.

    ![Minimum and maximum values for the prediction score filter.](media/predictionscorefilter2.png)
6. Select outside the filter to automatically apply the filter to the review set.

A list of documents with a prediction score within the range you specified is displayed on the review set page.

For more detailed instructions, see [Apply a prediction filter to a review set](ediscovery-predictive-coding-apply-prediction-filter).

## Step 4: Perform more training rounds

More than likely, you'll have to perform more training rounds to train the module to better predict relevant and non-relevant items in the review set. In general, you'll train the model enough times until it stabilizes enough to meet your requirements.

For more information, see [Perform additional training rounds](ediscovery-predictive-coding-train-model#perform-additional-training-rounds)

## Step 5: Apply the final prediction score filter to prioritize review

Repeat the instructions in Step 3 to apply the final prediction score to the review set to prioritize the review of relevant and non-relevant items after you complete all the training rounds and stabilize the model.