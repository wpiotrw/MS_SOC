---
layout: Conceptual
title: Create an exact data match sensitive information type (Classic experience workflow) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-classic-ux-workflow
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
ms.date: 2025-03-31T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Get started creating exact data match based sensitive information types using the classic EDM UX workflow.
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: b840c7d7-b29c-1d04-11e3-edb7a033b2b9
document_version_independent_id: b840c7d7-b29c-1d04-11e3-edb7a033b2b9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-create-edm-sit-classic-ux-workflow.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-create-edm-sit-classic-ux-workflow
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-create-edm-sit-classic-ux-workflow.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c8785398-2829-cdd8-186e-9f4cda450910
---

# Create an exact data match sensitive information type (Classic experience workflow) | Microsoft Learn

Creating and making a sensitive information type (SIT) based on exact data matching criteria (an EDM SIT) is a multi-phase process. These SITs can be used in Microsoft Purview data loss prevention policies, auto-labeling, eDiscovery, and certain content governance tasks. This article outlines the workflow and links to the procedures for each phase using the classic experience.

## Applies to

- Classic experience

If you want to create an EDM SIT using the new experience see, [Create an EDM SIT (New experience)](sit-create-edm-sit-unified-ux-workflow).

## Before you begin

Make sure you review:

- [Learn about EDM based SITs](sit-learn-about-exact-data-match-based-sits)
- [Get started with exact data match based sensitive information types overview](sit-get-started-exact-data-match-based-sits-overview)

## Overview of the EDM workflow (Classic experience)

![exact data match workflow phases](media/swimlane_edm_process.png)

| Phase | What's needed |
| --- | --- |
| [Phase 1: Export source data for exact data match based sensitive information types](sit-get-started-exact-data-match-export-data#export-source-data-for-exact-data-match-based-sensitive-information-types) | - Read access to the sensitive data |
| [Phase 2: Create the schema for exact data match based sensitive information types](sit-get-started-exact-data-match-create-schema#create-the-schema-for-exact-data-match-based-sensitive-information-types) | - Access to the sensitive information type wizard in the Microsoft Purviews portal - access to the [Microsoft 365 admin center via Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) |
| [Phase 3: Hash and upload the sensitive information source table for exact data match sensitive information types](sit-get-started-exact-data-match-hash-upload#hash-and-upload-the-sensitive-information-source-table-for-exact-data-match-sensitive-information-types) | - Custom security group and user account - **Hash and upload from one computer**: local admin access to a computer with direct internet access and to host the EDM Upload Agent - **Hash and upload from separate computers**: local admin access to a computer with direct internet access and host the EDM Upload Agent for the upload and local admin access to a secure computer to host the EDM Upload Agent to hash the sensitive information source table - Read access to the sensitive information source table file  the schema file |
| [Phase 4: Create exact data match sensitive information type/rule package](sit-get-started-exact-data-match-create-rule-package#create-exact-data-match-sensitive-information-typerule-package) | - Access to the Microsoft Purview portal |
| [Test an exact data match sensitive information type](sit-get-started-exact-data-match-test#test-an-exact-data-match-sensitive-information-type) | - Access to the Microsoft Purview portal |