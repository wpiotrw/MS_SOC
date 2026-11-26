---
layout: Conceptual
title: Region optimization for Microsoft Azure customers - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/region-optimization
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ebeaa30a-2425-ec11-b6e6-000d3a4f0f84
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
learn_banner_products:
- azure
description: Learn about the region optimization policy and how it might affect you.
author: diberry
ms.author: diberry
ms.reviewer: mjeffer
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: concept-article
ms.date: 2026-06-15T00:00:00.0000000Z
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: 8e76a496-c4b5-b124-904d-ca4b6a0525c9
document_version_independent_id: 0193571f-00d0-34d1-8267-a88907eccee3
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/region-optimization.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/region-optimization
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/region-optimization.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: a6c87464-ef90-3fcf-f50b-6aed1959209b
---

# Region optimization for Microsoft Azure customers - Microsoft Cost Management | Microsoft Learn

This article helps you understand the region optimization policy and how it might affect you. The purpose of the region optimization policy is to help you get the best possible performance. The policy relies on finding the list of the best available healthy regions based on your geography.

The policy might affect you when you try to create a resource in a region that can’t support your request. In this situation, you might see a message like the following notification:

`You can create resources in the following regions <ListofRegions> only. For business reasons, if you need access to any other regions, please see the Region optimization article for help.`

The region optimization policy is designed to be flexible, scalable, and secure while balancing our customer needs, capacity optimization, and security.

If you have a suitable business reason and the region where you want to deploy resources isn’t available to you, you can submit a [support request in the Azure portal](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/overview).