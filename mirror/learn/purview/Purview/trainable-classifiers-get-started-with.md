---
layout: Conceptual
title: Get started with trainable classifiers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-08-21T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkDEFENDER
search.appverid:
- MOE150
- MET150
description: A Microsoft Purview classifier is a tool you can train to recognize various types of content by giving it samples to look at. This article shows you how to create and train a custom classifier.
locale: en-us
document_id: 35a7dab6-afec-0be6-a495-63f1b89d9180
document_version_independent_id: 35a7dab6-afec-0be6-a495-63f1b89d9180
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/trainable-classifiers-get-started-with.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: trainable-classifiers-get-started-with
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/trainable-classifiers-get-started-with.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: ab1284ba-442b-733a-dadc-1fee8b78c1c3
---

# Get started with trainable classifiers | Microsoft Learn

A Microsoft Purview trainable classifier is a tool you can train to recognize various types of content by giving it samples to evaluate. Once trained, you can use it to identify items for application of Office sensitivity labels, Communications compliance policies, and retention label policies.

Implementing a custom trainable classifier requires two steps:

1. Provide two sets of sample data (selected by humans).
    1. A set that contains only items that belong in the category.
    2. A set that contains only items that **do not** belong in the category.
2. Test the classifier's ability to detect matches.

This article explains how to create and test a custom classifier.

For more information about the different types of classifiers, see [Learn about trainable classifiers](trainable-classifiers-learn-about).

Important

Microsoft Purview Communication Compliance supports the use of the Microsoft provided trainable classifiers only. Custom trainable classifiers aren't supported.

## Prerequisites

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

To use classifiers in the following scenarios, you need the following permissions:

| Scenario | Required Role Permissions |
| --- | --- |
| Retention label policy | Record Management  Retention Management |
| Sensitivity label policy | Security Administrator  Compliance Administrator  Compliance Data Administrator |
| Communication compliance policy | Insider Risk Management Administrator  Supervisory Review Administrator |

Important

By default, only the user who creates a custom classifier can train it and review predictions made by that classifier.

## Prepare for a custom trainable classifier

Before you create a custom trainable classifier, it's helpful to understand what's involved.

### Overall workflow

For more information about the overall workflow of creating custom trainable classifiers, see the [process flow for creating custom trainable classifiers](trainable-classifiers-learn-about#process-flow-for-creating-custom-classifiers).

### Seed content

To ensure that your trainable classifier can independently and accurately identify that an item belongs to a particular category of content, you must present it with many samples of the type of content that is in the category. This feeding of samples to the trainable classifier is known as *seeding*. A human must select the seed content, and that content must include two sets of data: one set contains only items that strongly represent the content the classifier is designed to detect (positive samples) and a second set contains items that clearly don't belong (negative samples).

You need at least 50 positive samples (up to 500) and at least 150 negative samples (up to 1,500) to train a classifier. The more samples you provide, the more accurate the predictions the classifier makes will be. The trainable classifier processes up to the 2,000 most recently created samples (by file created date/time stamp).

Tip

For best results, have at least 200 items in your test sample set that includes at least 50 positive examples and at least 150 negative examples.

## How to create a trainable classifier

**In preview:** The following process automates the testing of trainable classifiers and shortens the creation workflow from 12 days to two days. In some cases, the process can take only a few hours.

1. Collect between 50 and 500 seed content items that strongly represent the data you want the classifier to positively identify as being in the category. For a list of supported file types, see [Default crawled file name extensions and parsed file types in SharePoint Server](/en-us/sharepoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types).

    Note

    When seeding content for training or testing custom trainable classifiers, only text-based files are supported. You cannot use image files or image-only PDFs.
2. Collect a *second* set of seed content (from 150 to 1,500 items) that represents data that **don't** belong in the category.
3. Place the positive and negative seed content in separate SharePoint folders. Use a Communication site or other SharePoint site type, but not a Teams folder type or a OneDrive folder. Each folder must be dedicated to holding *only the seed content*. Make note of the site, library, and folder URL for each set.

    Tip

    If you create a new SharePoint site and folder for your seed data, allow at least an hour for that location to be indexed before creating the trainable classifier that uses that seed data.
4. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with either Compliance admin or Security admin role access and navigate to **Data loss prevention** &gt; **Data classification** &gt; **Classifiers**.

Important

The account you use must have access to the seed content folders in SharePoint.

1. Select the **Trainable classifiers** tab.
2. Select **Create trainable classifier**.
3. Add the source of your **positive** examples: select the SharePoint site, library, and folder URL for the seed content that the classifier should detect and then choose **Next**.
4. Add the source of your **negative** examples: select the SharePoint site, library, and folder URL for the seed content that the classifier should ignore and then choose **Next**.
5. Review the settings and select **Create trainable classifier**.
6. Within 24 hours or less, the trainable classifier processes the seed data and builds a prediction model. The classifier status is **In progress** while it processes the seed data. When the classifier finishes processing the seed data, the status changes to **Training is complete and items have been tested**.
7. When training completes and items are (automatically) tested, publish the classifier by choosing **Publish for use**.

After you publish your classifier, it's available as a condition in [Office auto-labeling with sensitivity labels](apply-sensitivity-label-automatically), [autoapply retention label policy based on a condition](apply-retention-labels-automatically#configuring-conditions-for-auto-apply-retention-labels), and in [Communication compliance](communication-compliance).

### Test your classifier

After the trainable classifier processes enough positive and negative samples to build a prediction model, test the predictions it makes. When you test the classifier, you verify whether its predictions are correct. After the classifier processes all the data, you can go through the results to verify whether each prediction is correct, incorrect, or uncertain. Microsoft uses this feedback in aggregate to improve the prediction model.