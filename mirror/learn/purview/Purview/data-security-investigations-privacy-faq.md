---
layout: FAQ
title: Privacy FAQ for Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-privacy-faq
summary: ''
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.date: 2025-08-19T00:00:00.0000000Z
description: Find answers to frequently asked questions about privacy and Data Security Investigations.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
audience: Admin
ms.topic: faq
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: 5b11af76-e8a2-ca72-f905-9d34201736bb
document_version_independent_id: 5b11af76-e8a2-ca72-f905-9d34201736bb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-privacy-faq.yml
site_name: Docs
depot_name: MSDN.Purview
page_type: faq
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-privacy-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-privacy-faq.yml
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5c21b939-ec9c-eb90-a67e-9070fd9bbf65
---

# Privacy FAQ for Data Security Investigations | Microsoft Learn

## How is my data stored in Microsoft Purview Data Security Investigations?

When you use Data Security Investigations, Microsoft copies user queried organization data from the Microsoft 365 application storage to tenant-isolated regional investigation storage. This data is stored until Data Security Investigations administrators or investigators delete the investigation. Only Data Security Investigations Administrators, Investigators, and Reviewers have access to this data in your organization.

## How is my data processed for Data Security Investigations AI features?

Data Security Investigations partners closely with Microsoft Security Copilot platform to power Data Security Investigations AI features. This means that data leaves Data Security Investigations (Microsoft 365 compliance area) and travels to Microsoft Security Copilot (Microsoft Azure compliance area) for up to 48 hours and return with AI generated content and insights. This generates the vector embeddings for vector search, category and subject generation, and examination results.

To ensure user privacy, all data sharing, logging, and scanning is turned off by default for Microsoft Security Copilot processing of Data Security Investigations data. For more information on Microsoft Security Copilot, see [Privacy and data security in Microsoft Security Copilot](/en-us/copilot/security/privacy-data-security)

## What feedback information does Data Security Investigations collect?

Data Security Investigations collects customer feedback to enhance its AI features and improve user experience. This feedback is gathered during the public preview stage and includes specific metrics related to the AI features' inputs and outputs.

- **What we collect**: We collect metrics such as the number of files returned to a vector search query, the total number of vectorized files in the user's data set, category impact scores, AI generated risk and relevance scores of files, and the number of files selected for AI examination. These metrics help us understand the effectiveness and relevance of our AI features.
- **What we don't collect**: We don't collect customer content or any personal data from the files themselves. Our focus is solely on collecting metrics and qualitative data about the inputs and outputs of our AI services to improve their performance and accuracy.

By collecting these metrics, Data Security Investigations aims to continuously improve its AI features and provide users with more accurate and relevant results. Your feedback is invaluable in helping us achieve this goal.