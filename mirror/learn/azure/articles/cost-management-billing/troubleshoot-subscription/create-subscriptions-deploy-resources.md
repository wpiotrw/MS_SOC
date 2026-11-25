---
layout: Conceptual
title: Message appears when you try to create multiple subscriptions - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/troubleshoot-subscription/create-subscriptions-deploy-resources
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/748a4eaa-0e25-ec11-b6e6-000d3a4f07b8
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
description: Provides help for the message you might see when you try to create multiple subscriptions.
author: mjeffer
ms.author: diberry
ms.reviewer: mjeffer
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: troubleshooting
ms.date: 2026-06-15T00:00:00.0000000Z
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: d1694b1f-1571-2409-3624-c968882b3e40
document_version_independent_id: d44b0af2-fd43-209f-5303-212111021d4c
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/troubleshoot-subscription/create-subscriptions-deploy-resources.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/troubleshoot-subscription/create-subscriptions-deploy-resources
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/troubleshoot-subscription/create-subscriptions-deploy-resources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: e03b31de-713a-2992-adb5-9f14bd9bcec2
---

# Message appears when you try to create multiple subscriptions - Microsoft Cost Management | Microsoft Learn

When you try to create multiple Azure subscriptions in a short period of time, you might receive a message stating:

`Subscription not created. Please try again later.`

The message is normal and expected.

Important

All existing subscriptions should generate consumption history before you create another one

The message can appear for customers with the following Azure subscription agreement types:

- [Microsoft Customer Agreement purchased directly through Azure.com](../manage/create-subscription)
    - You can have a maximum of five subscriptions in a Microsoft Customer Agreement purchased directly through Azure.com.
    - You can create one subscription per 24 hour period.
    - The ability to create other subscriptions is determined on an individual basis according to your history with Azure.
- [Microsoft Online Services Program](https://signup.azure.com/signup?offer=ms-azr-0003p)
    - A new billing account for a Microsoft Online Services Program can have a maximum of five subscriptions. However, subscriptions transferred to the new billing account don't count against the limit.
    - The ability to create other Microsoft Online Services Program subscriptions is determined on an individual basis according to your history with Azure.

## Solution

Expect a delay before you can create another subscription.

If you're new to Azure and don't have any consumption usage, read the [Get started guide for Azure developers](../../guides/developer/azure-developer-guide) to help you get started with Azure services.

## Need help? Contact us.

If you have questions or need help, [create a support request](https://go.microsoft.com/fwlink/?linkid=2083458).