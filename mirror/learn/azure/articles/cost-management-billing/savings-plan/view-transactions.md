---
layout: Conceptual
title: View savings plan purchase transactions - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/view-transactions
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
description: Learn how to view savings plan purchase transactions and details.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: b7131527-54d8-1502-0326-6b4f6ecb5c06
document_version_independent_id: ccf747e6-e35e-f5fb-e410-e9b92393bcbd
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/view-transactions.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/view-transactions
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/view-transactions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: 598b9df0-d2f2-131f-299f-ac3be2f5ddda
---

# View savings plan purchase transactions - Microsoft Cost Management | Microsoft Learn

You can view savings plan purchase and refund transactions in the Azure portal.

## View savings plan purchases in the Azure portal

Enterprise Agreement and Microsoft Customer Agreement billing readers can view accumulated purchases for reservations in cost analysis.

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Navigate to **Cost Management + Billing**.
3. Select **Cost analysis** in the left menu.
4. Apply a filter for **Pricing Model** and then select **SavingsPlan**.
5. To view purchases for reservations, apply a filter for **Charge Type** and then select **purchase**.
6. Set the **Granularity** to **Monthly**.
7. Set the chart type to **Column (Stacked)**.[![Screenshot showing accumulated cost in cost analysis.](media/view-transactions/accumulated-costs-cost-analysis.png)](media/view-transactions/accumulated-costs-cost-analysis.png#lightbox)

## View payments made

You can view payments that were made using APIs, usage data, and cost analysis. For savings plans paid for monthly, the frequency value is shown as **recurring** in the usage data and the Savings Plan Charges API. For savings plans paid up front, the value is shown as **onetime**.

Cost analysis shows monthly purchases in the default view. Apply the **purchase** filter to **Charge type** and **recurring** for **Frequency** to see all purchases. To view only savings plans, apply a filter for **Savings Plan**.

[![Screenshot showing savings plan costs in cost analysis.](media/buy-savings-plan/cost-analysis-savings-plan-costs.png)](media/buy-savings-plan/cost-analysis-savings-plan-costs.png#lightbox)

## Need help? Contact us.

If you have savings plan questions, contact your account team or [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Currently, Microsoft provides expert support for savings plans only in English.