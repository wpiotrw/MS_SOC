---
layout: Conceptual
title: All medical terms and conditions entity definition | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-defn-all-medical-terms-conditions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-09-13T00:00:00.0000000Z
audience: Admin
search.appverid: MET150
ms.topic: reference
ms.service: purview
ms.subservice: purview-sit-definitions
ms.collection:
- purview-compliance
recommendations: false
description: All medical terms and conditions sensitive information type entity definition.
locale: en-us
document_id: 221227ae-3508-7da6-35df-8ede89141b13
document_version_independent_id: 221227ae-3508-7da6-35df-8ede89141b13
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-defn-all-medical-terms-conditions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-defn-all-medical-terms-conditions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-defn-all-medical-terms-conditions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 02222098-61da-44ec-793a-a649744d1435
---

# All medical terms and conditions entity definition | Microsoft Learn

All medical terms and conditions is a bundled named entity that detects medical terms and medical conditions. It detects English terms only. Use this SIT to detect all possible matches of medical terms and conditions.

Important

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection) if you want to use a bundled SIT in an endpoint DLP policy. This requirement is specific to the combination of bundled SITS and endpoint DLP policies. The advanced classification article gives you information about enabling advanced classification, and about configuring endpoints and the supported file types.

## Format

Dictionary

## Pattern

Dictionary

## Checksum

No

## Keyword Highlighting

Not supported

When keyword highlighting is supported in the contextual summary for a sensitive information type or a trainable classifier, in the **Contextual Summary** view of activity explorer, the keywords in a document that were matched to a policy are highlighted.

## Cloud Support

Cloud support is available for the following:

- Microsoft Commercial Cloud
- Microsoft Government Community Cloud
- Microsoft 365 Government Community Cloud High
- Microsoft 365 Department of Defense

## Description

This bundled named entity matches text that mentions medical conditions that are present in curated dictionaries. There's one curated dictionary per supported language. The dictionaries are from many international medical resources. The dictionaries include as many medical conditions as possible without risking a large number of false positives. Each entry contains the different forms that a single condition is commonly written in to ensure coverage, for example:

- *TB*
- *tuberculosis*
- *phthisis pulmonalis*

## Contains

This bundled named entity SIT contains these individual SITs.

- Blood test terms
- Types of medication
- Diseases
- Generic medication names
- Impairments listed in the U.S. Disability Evaluation Under Social Security
- Lab test terms
- Lifestyles that relate to medical conditions
- Medical specialties
- Surgical procedures
- Brand medication names