---
layout: Conceptual
title: Download your savings plan price sheet - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/download-savings-plan-price-sheet
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
description: This article explains how you can download the price sheet for an Enterprise Agreement (EA) or Microsoft Customer Agreement (MCA).
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: 1523bc47-aca9-a4a9-e211-fd649480326a
document_version_independent_id: 5c66ad84-1f56-bc7f-0b9d-e60d543c370a
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/download-savings-plan-price-sheet.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/download-savings-plan-price-sheet
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/download-savings-plan-price-sheet.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: d15dbb35-bed0-2480-8e06-3e700024eb49
---

# Download your savings plan price sheet - Microsoft Cost Management | Microsoft Learn

This article explains how to download the price sheet for an Enterprise Agreement (EA) or Microsoft Customer Agreement (MCA) through the Azure portal. The price sheet lists products that are eligible for savings plans and their one-year and three-year savings plan prices.

## Download EA price sheet

To download your EA price sheet through the Azure portal, follow these steps:

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Search for **Cost Management + Billing**.
3. Select your billing profile.
4. In the left menu under Billing, select **Usage + charges**.
5. Select the desired month and select the corresponding **Download** link.
6. In the Download Usage + Charges window, under Price Sheet, select **Prepare Download Azure**. File generation may take a few moments.
7. After you receive a notification that the price sheet is ready, select **Download csv**.
8. Open the file and filter on `Price type` to see `SavingsPlan` price records.

## Download MCA price sheet

To download your MCA price sheet through the Azure portal, follow these steps:

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Search for **Cost Management + Billing**.
3. Select your billing account.
4. At the bottom of the page in the **Shortcuts** section, select **Download usage and prices**.
5. Select **Download Azure price sheet for***current month and year*. File generation may take a few moments.
6. Open the file and filter on `priceType` to see `SavingsPlan` price records.

## Download price sheet using APIs

To learn more about downloading your price sheet using price sheet APIs, see the following articles:

- [Learn more about EA price sheet](/en-us/rest/api/cost-management/price-sheet).
- [Learn more about MCA price sheet](/en-us/rest/api/consumption/price-sheet).
- [Learn more about retail price sheet](/en-us/rest/api/cost-management/retail-prices/azure-retail-prices).

## Need help? Contact us.

If you have questions about savings plans, contact your account team or [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Currently, Microsoft provides expert support for savings plans only in English.