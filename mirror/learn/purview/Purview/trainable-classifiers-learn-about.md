---
layout: Conceptual
title: Learn about trainable classifiers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/trainable-classifiers-learn-about
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-01T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.collection:
- highpri
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkMAC
search.appverid:
- MOE150
- MET150
description: Trainable classifiers can recognize various types of content for labeling or policy application by giving it positive and negative samples to look at.
locale: en-us
document_id: bdf23431-8de2-deea-9fb4-16abecc7a08b
document_version_independent_id: bdf23431-8de2-deea-9fb4-16abecc7a08b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/trainable-classifiers-learn-about.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: trainable-classifiers-learn-about
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/trainable-classifiers-learn-about.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 812c1cdb-9b73-4e7b-8c0f-943945f6849b
---

# Learn about trainable classifiers | Microsoft Learn

## Trainable Classifiers

This categorization method is well suited to content that can't be easily identified using either the manual or automated pattern-matching methods. A classifier learns how to identify a type of content by looking at hundreds of examples of the content you want to detect.

Note

**In Preview:** You can view the trainable classifiers in content explorer by expanding **Trainable Classifiers** in the filters panel. The trainable classifiers automatically display the number of incidents found in SharePoint and Teams, without requiring any labeling. If you don't want to use this feature, you must file a request with Microsoft Support. This request disables the display of your sensitive data that isn't used in any labeling policies within Content Explorer. You can disable scanning of your data as well. If scanning is turned off, sensitivity labeling and DLP policies with those classifiers don't work.

### Where you can use classifiers

Use classifiers as a condition for:

- [Auto-labeling Office files with sensitivity labels](apply-sensitivity-label-automatically)
- [Automatically applying a retention label policy based on a condition](apply-retention-labels-automatically#configuring-conditions-for-auto-apply-retention-labels)
- [Communication compliance](communication-compliance) supports Microsoft provided trainable classifiers only.
- Sensitivity label conditions. (See [Automatically apply a sensitivity label to Microsoft 365 data](apply-sensitivity-label-automatically))
- [Data loss prevention](dlp-learn-about-dlp)

Important

Classifiers only work with items that aren't encrypted.

## Types of classifiers

- **Microsoft provided Pretrained classifiers** - Microsoft created and pretrained multiple classifiers that you can start using without training them. These classifiers appear with the status of `Ready to use`. These classifiers evaluate items in all languages listed in the [suppported languages columns](trainable-classifiers-definitions).
- **Custom trainable classifiers** - If you need to identify and categorize your content beyond what the pretrained classifiers cover, you can create and train your own classifiers.

For a complete list of all pretrained classifiers, see [Trainable classifiers definitions](trainable-classifiers-definitions#trainable-classifiers-definitions).

### Custom classifiers

Important

**Language limitation:** Support for custom classifiers is limited to English.

When the Microsoft provided pretrained classifiers don't meet your needs, you can create and train your own classifiers. There's more work involved with creating your own, but they're better tailored to your organization's needs.

To create a custom trainable classifier, you start by feeding it one set of examples that are definitely in the category, and another set of examples that are definitely not in the category. Microsoft Purview processes those examples and the classifier then makes predictions as to whether any given item falls into the category you're building. You then confirm the results, sorting out the true positives, true negatives, false positives, and false negatives to help increase the accuracy of its predictions.

When you publish the classifier, it sorts through items in locations like SharePoint and Exchange, and classifies the content.

For example, you can create trainable classifiers for:

- Legal documents - such as attorney client privilege, closing sets, statement of work
- Strategic business documents - like press releases, merger and acquisition, deals, business or marketing plans, intellectual property, patents, design docs
- Pricing information - like invoices, price quotes, work orders, bidding documents
- Financial information - such as organizational investments, quarterly or annual results

#### Process flow for creating custom classifiers

The following flow diagram illustrates the process for creating and publishing a classifier for use in compliance solutions, such as retention policies and communication supervision. For more detail on creating a custom trainable classifier, see [Get started with trainable classifiers](trainable-classifiers-get-started-with#get-started-with-trainable-classifiers).

![Diagram of workflow for creating a custom trainable classifier.](media/trainable-classifiers-workflow-final.png)

Tip

If you create a new SharePoint site and folder for your seed data, allow at least an hour for that location to be indexed before creating the trainable classifier that uses that seed data.

### Retraining classifiers

Retraining published custom classifiers isn't supported. If you need to improve the accuracy of a trainable classifier you published, remove the classifier and [start over with larger sample sets](trainable-classifiers-get-started-with#get-started-with-trainable-classifiers).

To improve the accuracy of an unpublished classifier, review the test results, update the data set with additional data, and restart the training.