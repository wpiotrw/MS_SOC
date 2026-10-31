---
layout: Conceptual
title: Calculate Enterprise Agreement (EA) savings plan cost savings - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/calculate-ea-savings-plan-savings
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
description: Learn how Enterprise Agreement users manually calculate their savings plan savings.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: 07bd4c26-f3b1-3483-11d6-5bd2b98acfa7
document_version_independent_id: af60a348-269f-8864-f5a6-7517edb0d151
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/calculate-ea-savings-plan-savings.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/calculate-ea-savings-plan-savings
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/calculate-ea-savings-plan-savings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60932d05-feee-4685-a73b-595e25dd9318
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/c43bb58b-1190-419b-8d18-e6052371b599
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 32709eb2-ce2a-74c0-f9b6-58577bb834d2
---

# Calculate Enterprise Agreement (EA) savings plan cost savings - Microsoft Cost Management | Microsoft Learn

This article helps Enterprise Agreement (EA) users manually calculate their savings plan savings. You download your amortized usage and charges file, prepare an Excel worksheet, and then calculate your savings. The following sections guide you through the process. Although the example uses Excel, you can use the spreadsheet application of your choice.

Note

The prices shown in this article are for example purposes only.

This article is specific to EA users.

Microsoft Customer Agreement (MCA) users can use similar steps to calculate their savings plan savings through invoices. The MCA amortized usage file doesn't contain UnitPrice (on-demand pricing) for savings plans. You can get unit prices from your [MCA price sheet](download-savings-plan-price-sheet#download-mca-price-sheet).

## Required permissions

To view and download usage data as an EA customer, you must be an Enterprise Administrator, Account Owner, or Department Admin with the view charges policy enabled.

## Download all usage amortized charges

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Search for *Cost Management + Billing*.[![Screenshot showing search for cost management.](media/calculate-ea-savings-plan-savings/search-cost-management.png)](media/calculate-ea-savings-plan-savings/search-cost-management.png#lightbox)
3. If you have access to multiple billing accounts, select the billing scope for your EA billing account.
4. Select **Usage + charges**.
5. For the month you want to download, select **Download**.[![Screenshot showing Usage + charges download.](media/calculate-ea-savings-plan-savings/download-usage-ea.png)](media/calculate-ea-savings-plan-savings/download-usage-ea.png#lightbox)
6. On the Download Usage + Charges page, under Usage Details, select **Amortized charges (usage and purchases)**.[![Screenshot showing the Download usage + charges window.](media/calculate-ea-savings-plan-savings/select-usage-detail-charge-type-small.png)](media/calculate-ea-savings-plan-savings/select-usage-detail-charge-type.png#lightbox)
7. Select **Prepare document**.
8. It could take a while for Azure to prepare your download, depending on your monthly usage. When it's ready for download, select **Download csv**.

## Prepare data and calculate savings

Because Azure usage files are in CSV format, you need to prepare the data for use in Excel. Then you calculate your savings.

1. Open the amortized cost file in Excel and save it as an Excel workbook.
2. The data resembles the following example.[![Example screenshot of the unformatted amortized usage file.](media/calculate-ea-savings-plan-savings/unformatted-data.png)](media/calculate-ea-savings-plan-savings/unformatted-data.png#lightbox)
3. In the Home ribbon, select **Format as Table**.
4. In the Create Table window, select **My table has headers**.
5. In the **benefitName** column, set a filter to clear **Blanks**.[![Screenshot showing clear Blanks data.](media/calculate-ea-savings-plan-savings/savings-plan-name-clear-blanks.png)](media/calculate-ea-savings-plan-savings/savings-plan-name-clear-blanks.png#lightbox)
6. Find the **ChargeType** column. To the right of the column name, select the sort and filter symbol (the down arrow).
7. Filter the **ChargeType** column to select only **Usage**. Clear any other selections. [![Screenshot showing ChargeType selection.](media/calculate-ea-savings-plan-savings/charge-type-selection-small.png)](media/calculate-ea-savings-plan-savings/charge-type-selection.png#lightbox)
8. To the right of **UnitPrice**, insert a column and label it with a title like **TotalUsedSavings**.
9. In the first cell under **TotalUsedSavings**, create a formula that calculates *(UnitPrice – EffectivePrice) \* Quantity*.[![Screenshot showing the TotalUsedSavings formula.](media/calculate-ea-savings-plan-savings/total-used-savings-formula.png)](media/calculate-ea-savings-plan-savings/total-used-savings-formula.png#lightbox)
10. Copy the formula to all the other empty **TotalUsedSavings** cells.
11. At the bottom of the **TotalUsedSavings** column, sum the column's values.[![Screenshot showing the summed values.](media/calculate-ea-savings-plan-savings/total-used-savings-summed.png)](media/calculate-ea-savings-plan-savings/total-used-savings-summed.png#lightbox)
12. Somewhere under your data, create a cell named *TotalUsedSavingsValue*. Next to it, copy the **TotalUsed** cell and paste it as **Values**. This step is important because the next step will change the applied filter and affect the summed total.[![Screenshot showing pasting the TotalUsedSavings cell as Values.](media/calculate-ea-savings-plan-savings/paste-value-used.png)](media/calculate-ea-savings-plan-savings/paste-value-used.png#lightbox)
13. Filter the **ChargeType** column to select only **UnusedSavingsPlan**. Clear any other selections.
14. To the right of the **TotalUsedSavings** column, insert a column and label it with a title like **TotalUnused**.
15. In the first cell under **TotalUnused**, create a formula that calculates *EffectivePrice \* Quantity*.[![Screenshot showing the TotalUnused formula.](media/calculate-ea-savings-plan-savings/total-unused-formula.png)](media/calculate-ea-savings-plan-savings/total-unused-formula.png#lightbox)
16. At the bottom of the **TotalUnused** column, sum the column's values.
17. Somewhere under your data, create a cell named *TotalUnusedValue*. Next to it, copy the **TotalUnused** cell and paste it as **Values**.
18. Under the **TotalUsedSavingsValue** and **TotalUnusedValue** cells, create a cell named *SavingsPlanSavings*. Next to it, subtract **TotalUnusedValue** from **TotalUsedSavingsValue**. The calculation result is your savings plan savings.[![Screenshot showing the SavingsPlanSavings calculation and final savings.](media/calculate-ea-savings-plan-savings/savings-plan-savings.png)](media/calculate-ea-savings-plan-savings/savings-plan-savings.png#lightbox)

If you see a negative savings value, then you're likely to have unused savings plans. You should review your savings plan usage. For more information, see [View savings plan utilization after purchase](view-utilization).

## Other ways to get data and see savings

Using the preceding steps, you can repeat the process for any number of months. Doing so allows you to see your savings over a longer period.

Instead of downloading one usage file per month, you can use Cost Management exports to get all your usage data for a specific date range and save it to Azure Storage. This approach lets you see your savings over a longer period. For more information about creating an export, see [Create and manage exported data](../costs/tutorial-improved-exports).