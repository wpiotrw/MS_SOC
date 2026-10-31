---
layout: Conceptual
title: Microsoft Purview Classifiers Overview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-classification-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: libarson
author: k-reagle
manager: laurawi
ms.date: 2026-09-29T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
ms.collection:
- highpri
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
ms.custom:
- admindeeplinkDEFENDER
- sfi-ga-nochange
- msecd-doc-authoring-1028
search.appverid:
- MOE150
- MET150
description: Learn how to discover, create, inspect, and manage Microsoft Purview classifiers to identify sensitive content and understand classifier capabilities.
ai-usage: ai-assisted
locale: en-us
document_id: 5e0184e1-20f1-73e4-737b-051cb2a38817
document_version_independent_id: 5e0184e1-20f1-73e4-737b-051cb2a38817
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-classification-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-classification-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-classification-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d4f194af-3be4-1bfa-af52-b8f325ba2e81
---

# Microsoft Purview Classifiers Overview | Microsoft Learn

Microsoft Purview classifiers help administrators identify sensitive content so they can protect and manage it. The Classifiers page brings classification types together in one experience where you can discover, create, inspect, and manage classifiers.

Search and filtering help you find classifiers. When you create a new classifier, you can view how each classifier type works. This helps you understand the available options and choose a classifier for your scenario.

The **Classified items** count shows how many items were found with that specific classification. You can also see how many policies use a classifier and inspect those dependencies before changing it.

In the [Microsoft Purview portal](https://purview.microsoft.com), you can access **Classifiers** under **Information Protection**, **Data Loss Prevention**, or **DSPM** (Data Security Posture Management).

## Classification types and capabilities

Important

The new Classifiers experience in Microsoft Purview is in preview and is available alongside the existing classification experiences. Classifiers you create, edit, or delete in either experience are reflected in the other. Features and functionality in the new experience might change before general availability.

Explore the following classification types and related capabilities.

### Sensitive information types

Sensitive information types (SITs) identify content that matches patterns of sensitive information, such as social security, credit card, or bank account numbers. You can use preexisting sensitive information types or create your own.

For more information, see [Learn about sensitive information types](sit-sensitive-information-type-learn-about). For information about predefined types, see [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions).

### Named entities

Named entities are sensitive information types that use dictionaries and patterns to detect person names, physical addresses, and medical terms and conditions.

For more information, see [Learn about named entities](sit-named-entities-learn).

### Exact data match

Exact data match identifies sensitive content by matching exact values.

For more information, see [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types).

### Trainable classifiers

Microsoft Purview provides pretrained trainable classifiers that are ready to use. You can also create custom trainable classifiers by providing samples of the content you want to recognize.

For more information, see [Learn about trainable classifiers](trainable-classifiers-learn-about).

### Credentials

Credential sensitive information types detect credentials in content. The **All credentials** sensitive information type groups individual credential types to detect credentials from supported services and environments.

For more information, see [All credential types](sit-defn-all-creds).

### Fingerprinting

Document fingerprinting recognizes content that is a variation of a template.

For more information, see [Document fingerprinting](sit-document-fingerprinting).

### Optical character recognition

Optical character recognition (OCR) lets Microsoft Purview scan images for sensitive information. You can enable OCR to extend classification to images without creating separate classifiers.

For setup requirements and supported locations, see [Learn about optical character recognition](ocr-learn-about).

## On-demand classification

On-demand classification identifies and classifies sensitive content in files at rest, including files that haven't been classified or need updated classification.

For more information, see [Create and analyze an on-demand classification scan](on-demand-classification).

## Explore classified content

The Classifiers page helps you manage classifiers. Use Data Explorer to review items with classification matches and see where those items are located. Access to item lists and item contents requires the appropriate Data Explorer permissions.

You can find Data Explorer on the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection** &gt; **Explorers** page.

For supported content, access requirements, and instructions, see [Get started with Data Explorer](data-classification-data-explorer).

## Permissions

Access to the Classifiers page can come from a Microsoft Entra administrator role or a Microsoft Purview role group.

Note

As a best practice, always use the role with least privilege to grant access to the Classifiers page.

### Microsoft Entra administrator roles

The following Microsoft Entra roles provide access:

- Global administrator
- Compliance administrator
- Security administrator
- Compliance data administrator

### Microsoft Purview roles and role groups

In Microsoft Purview, a **role** defines permissions, and a **role group** contains a set of roles. Adding a user to a role group grants the permissions of the roles in that group. For details, see [Permissions in the Microsoft Purview portal](purview-permissions).

**Applicable Microsoft Purview roles**

- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader

**Applicable Microsoft Purview role groups**

Use the following role groups to assign access. Their permissions differ; choose the group that matches the user's responsibilities. For assignment guidance, see [Permissions in the Microsoft Purview portal](purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers