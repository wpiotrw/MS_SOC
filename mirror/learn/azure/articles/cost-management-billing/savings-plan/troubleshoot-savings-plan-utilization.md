---
layout: Conceptual
title: Troubleshoot savings plan utilization - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/troubleshoot-savings-plan-utilization
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
description: This article helps you understand why savings plans can temporarily have utilization greater than 100% in usage reporting UIs and APIs.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: troubleshooting
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: abadc713-c960-60fb-36ab-dba2a5776490
document_version_independent_id: 7f340387-9fe3-599b-8dd9-8e234709e021
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/troubleshoot-savings-plan-utilization.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/troubleshoot-savings-plan-utilization
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/troubleshoot-savings-plan-utilization.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: 1541ac99-0d44-1258-d93a-70a39086f213
---

# Troubleshoot savings plan utilization - Microsoft Cost Management | Microsoft Learn

This article helps you understand why savings plans can temporarily have high utilization.

## Why is my savings plan utilization lower than expected?

Only usage from eligible Azure resources can receive savings plan benefits. Resources must meet both of the following eligibility criteria:

1. Benefit scope - The resource must be within the savings plan's benefit scope. To learn more, see [Savings plan scopes](scope-savings-plan).
2. Product inclusion - The resource must be an instance of a product included in the savings plan model. To learn which products are eligible for a savings plan, follow the instructions in [Download your savings plan price sheet](download-savings-plan-price-sheet).

There are several reasons a savings plan might be underutilized, as shown in the following examples. In some cases, broadening the savings plan's benefit scope can increase utilization.

- **Custom hourly commitment too large** - Follow the purchase recommendations provided through Azure Advisor, the savings plan purchase experience in the Azure portal, and the Savings plan benefit recommendations API. Purchasing a commitment greater than the recommended value might result in underutilization and reduce your cost savings. To learn more, see [Savings plan recommendations](purchase-recommendations).
- **Recent changes in resource usage**- Your savings plan-eligible usage might have recently decreased. Reasons for these changes include:
    - ***VM rightsizing*** - To learn more, see [VM shutdown recommendations](/en-us/azure/advisor/advisor-cost-recommendations#shutdown-recommendations)
    - ***VM shutdowns*** - To learn more, see [Resize SKU recommendations](/en-us/azure/advisor/advisor-cost-recommendations#resize-sku-recommendations)
    - ***Switch to ineligible products*** - To learn which products are savings plan-eligible, compare your usage with the list of eligible products in your price sheet. Follow the instructions in [Download your savings plan price sheet](download-savings-plan-price-sheet).
- **Recent savings plan or reservation purchase** - Savings plans and Azure reservations can provide savings for some of the same products. A recently purchased or rescoped reservation might provide benefits for usage previously covered by your savings plan. Review the benefit scopes of any recently purchased savings plans or reservations and consider adjusting them.
- **Narrow benefit scope** - Your savings plan's scope may be excluding more usage than you intend. To learn more, see [Savings plan scopes](scope-savings-plan).

## Why am I incurring on-demand charges while my savings plan utilization is less than 100%?

A savings plan is an hourly benefit, so each of the 24 hours in a day is a separate benefit window. In some hours, you might underutilize your savings plan benefits. In other hours, you might fully utilize your savings plan and also incur on-demand charges. When you view daily usage, you might see both plan underutilization and on-demand charges for the same day.

## Why is my savings plan utilization greater than 100%?

Savings plans can temporarily have utilization greater than 100%, as shown in the Azure portal and from APIs.

Savings plan benefits are flexible and cover usage across various products and regions. Azure first applies plan benefits to the usage with the largest percentage discount from its pay-as-you-go rate, continuing until your hourly commitment is reached.

The Azure usage and billing systems determine your hourly cost by examining your usage for each hour. Usage for all services you used in the previous hour is reported to the Azure billing systems. However, usage isn't always reported immediately, which makes it difficult to determine which resources should receive the benefit. To compensate, Azure temporarily applies the maximum benefit to all usage received. This process might result in benefits that exceed the hourly commitment. Azure then performs additional processing to reconcile utilization back to 100%. Periods of overutilization are most likely to appear immediately after a usage hour.