---
layout: Conceptual
title: Charge back savings plan costs - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/charge-back-costs
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
description: Learn how to view savings plan costs for chargeback.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: 3338b602-366a-ceff-f671-e05703273ac6
document_version_independent_id: 227f358f-21cf-87f3-4897-276b203f2c9c
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/charge-back-costs.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/charge-back-costs
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/charge-back-costs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 4f359be3-5c98-6721-70e0-fb1ab5684bdf
---

# Charge back savings plan costs - Microsoft Cost Management | Microsoft Learn

Enterprise Agreement and Microsoft Customer Agreement billing readers can view amortized cost data for savings plans. They can use the data to charge back costs associated with a subscription, resource group, resource, or tag to their partners. In amortized data, the effective price is the prorated hourly savings plan cost. The cost is the total cost of savings plan usage by the resource on that day.

Users with an individual subscription can get the amortized cost data from their usage file. When a resource gets a savings plan discount, the *AdditionalInfo* section in the usage file contains the savings plan details. For more information, see [View and download your Azure usage and charges](../understand/download-azure-daily-usage).

## View savings plan usage data for show back and charge back

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Navigate to **Cost Management + Billing**.
3. Select **Cost analysis** from the left navigation menu.
4. Under **Actual Cost**, select the **Amortized Cost** metric.
5. To see which resources were used by a savings plan, apply a filter for **Pricing Model** and then select **SavingsPlan**.
6. Set the **Granularity** to **Monthly** or **Daily**.
7. Set the chart type to **Table**.
8. Set the **Group by** option to **Resource**.

## Get the data for show back and charge back

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Navigate to **Cost Management + Billing**.
3. Select **Export** from the left navigation menu.
4. Select **Add**.
5. Select **Amortized cost** as the metric and set up your export.

The *EffectivePrice* for usage that receives a savings plan discount is the prorated cost of the savings plan instead of zero. This value shows the monetary value of savings plan consumption by a subscription, resource group, or resource. You can use it to charge back savings plan costs internally. The dataset also includes unused savings plan benefits.

## Get Azure consumption and savings plan usage data using API

You can get the data using the API or download it from the Azure portal.

You call the [Usage Details API](/en-us/rest/api/consumption/usagedetails/list) to get the new data. For more information about terminology, see [Usage terms](../understand/understand-usage).

Here's an example call to the Usage Details API:

```http
https://management.azure.com/providers/Microsoft.Billing/billingAccounts/{enrollmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodId}/providers/Microsoft.Consumption/usagedetails?metric={metric}&api-version=2019-05-01&$filter={filter}

```

For more information about `{enrollmentId}` and `{billingPeriodId}`, see the [Usage Details – List](/en-us/rest/api/consumption/usagedetails/list) API article.

The following table describes metrics and filters that can help solve common savings plan problems.

| Type of API data | API call action |
| --- | --- |
| **All Charges (usage and purchases)** | Request for an ActualCost report. |
| **Usage that got savings plan discount** | Request for an ActualCost report.  Once you've ingested all of the usage, look for records with ChargeType = 'Usage' and PricingModel = 'SavingsPlan'. |
| **Usage that didn't get savings plan discount** | Request for an ActualCost report. Once you've ingested all of the usage, filter for usage records with PricingModel = 'OnDemand'. |
| **Amortized charges (usage and purchases)** | Request for an AmortizedCost report. |
| **Unused savings plan report** | Request for an AmortizedCost report. Once you've ingested all of the usage, filter for usage records with ChargeType = 'UnusedSavingsPlan' and PricingModel = 'SavingsPlan'. |
| **Savings plan purchases** | Request for an AmortizedCost report. Once you've ingested all of the usage, filter for usage records with ChargeType = 'Purchase' and PricingModel = 'SavingsPlan'. |
| **Refunds** | Request for an AmortizedCost report. Once you've ingested all of the usage, filter for usage records with ChargeType = 'Refund'. |

## Download the usage CSV file with new data

If you're an EA admin, you can download the CSV file that contains new usage data from the Azure portal.

In the Azure portal, navigate to [Cost Management + Billing](https://portal.azure.com/#blade/Microsoft_Azure_Billing/ModernBillingMenuBlade/BillingAccounts).

1. Select the scope.
    1. For EA, your scope is the enrollment.
    2. For MCA, your scope is the billing account.
2. Select **Usage + charges**.
3. Select **Download**.
4. In **Usage Details**, select **Amortized usage data**.

The CSV files that you download contain actual costs and amortized costs.

## Need help? Contact us.

If you have savings plan questions, contact your account team or [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Currently, Microsoft provides expert support for savings plans only in English.