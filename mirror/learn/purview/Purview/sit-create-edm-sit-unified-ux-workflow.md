---
layout: Conceptual
title: Create exact data match sensitive information type in the New Experience workflow | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-unified-ux-workflow
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.date: 2026-06-26T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Get started creating exact data match based sensitive information types using the new experience.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 25026256-5ebf-2cb7-315b-4ad397d7f639
document_version_independent_id: 25026256-5ebf-2cb7-315b-4ad397d7f639
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-create-edm-sit-unified-ux-workflow.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-create-edm-sit-unified-ux-workflow
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-create-edm-sit-unified-ux-workflow.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 749962b9-1d6c-ab8d-92c3-e088c45432d1
---

# Create exact data match sensitive information type in the New Experience workflow | Microsoft Learn

Creating and making an exact data match (EDM) based sensitive information type (SIT) available is a multi-phase process. EDM-based sensitive information types can be used in Microsoft Purview data loss prevention policies, eDiscovery, and certain content governance tasks. This article outlines the workflow and links to the procedures for each of the phases

## Applies to these EDM scenarios

This article covers the new experience. If you want to create an EDM SIT using the classic experience, see [Create EDM SIT classic experience](sit-create-edm-sit-classic-ux-workflow).

## Before you begin

Make sure you review:

- [Learn about EDM based SITs](sit-learn-about-exact-data-match-based-sits)
- [Get started with exact data match based sensitive information types (Overview)](sit-get-started-exact-data-match-based-sits-overview)

## Overview of the EDM workflow (New experience)

The following table summarizes the phases of the EDM workflow and the requirements for each phase.

| Phase | Requirements |
| --- | --- |
| [Phase 1: Export source data for exact data match based sensitive information type](sit-get-started-exact-data-match-export-data#export-source-data-for-exact-data-match-based-sensitive-information-types) | *Read* access to the sensitive data |
| [Phase 2:Create the sample file](sit-create-edm-sit-unified-ux-sample-file) | Knowledge of the data fields (the column headers in your source table) and the format of the data you will be looking for in each column. |
| [Phase 3: Create the EDM SIT](sit-create-edm-sit-unified-ux-schema-rule-package) | Access to the **Microsoft Purview portal** and permissions to create and edit EDM SITs |
| [Phase 4: Hash and upload the sensitive information source table for exact data match sensitive information types](sit-get-started-exact-data-match-hash-upload) | - Custom security group and user account - To **Hash and upload from one computer**: Local admin access to a computer with direct internet access and to host the EDM Upload Agent - To **Hash and upload from separate computers**: Local admin access to a computer with direct internet access to host the EDM Upload Agent for uploading your data and *Local Admin* access to a secure computer for hosting the EDM Upload Agent and for hashing the sensitive information source table. - *Read* access to the sensitive information source table file. |
| [Phase 5: Test an exact data match sensitive information type](sit-get-started-exact-data-match-test#test-an-exact-data-match-sensitive-information-type) | Access to the Microsoft Purview portal. |