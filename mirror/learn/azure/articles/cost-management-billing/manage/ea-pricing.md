---
layout: Conceptual
title: View and download your organization's Azure pricing - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/ea-pricing
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
description: Learn how to view and download pricing or estimate costs with your organization's pricing.
author: mkmsft1
ms.reviewer: megankairiss
ms.service: cost-management-billing
ms.subservice: cost-management
ms.topic: how-to
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: megankairiss
service.tree.id: f1bb13fb-3d35-4f13-93af-d6137ba7f2e3
locale: en-us
document_id: c097f750-8235-7042-7741-650890a7f11d
document_version_independent_id: 61b94aae-5d90-d8b8-30ae-94c8b8f6cae9
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/ea-pricing.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/ea-pricing
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/ea-pricing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: 3d4fc202-3d47-a1c2-109a-095d6dc413a1
---

# View and download your organization's Azure pricing - Microsoft Cost Management | Microsoft Learn

Azure customers with an Azure Enterprise Agreement (EA), Microsoft Customer Agreement (MCA), or Microsoft Partner Agreement (MPA) can view and download their pricing in the Azure portal. Learn how to check your billing account type. Price sheets are available for download covering up to 13 months prior.

Note

The price sheet that you download includes the `priceFactors` column at the end of the file. This column shows when a price comes from a benefit, such as a savings plan or Flex Plan. For more information, see [Understand price factors and supplemental charge details](../automate/understand-price-factors-supplemental-charge-details). Downloaded price sheets keep their schema version. To select a dataset version, such as 2026-10-01, use [exports](../costs/tutorial-improved-exports). For more information, see Columns in downloaded price sheets and [Compare downloads and exports](../understand/compare-downloads-exports).

## Download pricing for an Enterprise Agreement

Depending on the policies set for your organization by the Enterprise Admin, only certain administrative roles provide access to your organization's EA pricing information. For more information, see [Understand Azure Enterprise Agreement administrative roles in Azure](understand-ea-roles).

1. As an Enterprise Admin, sign-in to the [Azure portal](https://portal.azure.com/).
2. Search for *Cost Management + Billing*.[![Screenshot that shows Azure portal search.](media/ea-pricing/portal-cm-billing-search.png)](media/ea-pricing/portal-cm-billing-search.png#lightbox)
3. Select a billing profile. Depending on your access, you might need to select a billing account first.
4. Select **Usage + Charges** from the navigation menu.[![Screenshot that shows usage and charges under Billing.](media/ea-pricing/ea-pricing-usage-charges-nav.png)](media/ea-pricing/ea-pricing-usage-charges-nav.png#lightbox)
5. Select ![Screenshot of the Download symbol.](media/ea-pricing/download-icon.png)**Download** for the month.
6. On the Download Usage + Charges page, under Price Sheet, select **Prepare document**. It could take a while to prepare your file.[![Screenshot shows the Download Usage + Charges options.](media/ea-pricing/download-enterprise-agreement-price-sheet-01.png)](media/ea-pricing/download-enterprise-agreement-price-sheet-01.png#lightbox)
7. When the file is ready to download, select **Download Azure price sheet**.

For billing periods January 2023 onwards, a new version of the Azure price sheet is available for download. The new version features a new schema. It's a .ZIP file to support large amounts of data.

Azure reservation pricing is available in the Azure Price Sheet for the current billing period. If you want to maintain an ongoing record of Azure reservation pricing, we recommend that you download your Azure Price Sheet for each billing period.

### Download pricing for an indirect Enterprise Agreement

If a partner manages your enrollment (an indirect EA), partner administrators can download the price sheet from the billing profile.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for *Cost Management + Billing*.
3. Select **Billing scopes**, and then select the billing account that you want to work with.
4. Select **Billing profiles**, and then select the billing profile that you want to work with.
5. Select **Usage + Charges**.
6. For the month you want, select **Download**.
7. On the **Download Usage + Charges** page, under **Price Sheet**, select **Prepare document**.
8. When the file is ready to download, select **Download Azure price sheet**.

For more information, see [View your usage summary details and download reports for EA enrollments](direct-ea-azure-usage-charges-invoices#download-usage-charges-csv-file).

## Download pricing for an MCA or MPA account

If you have an MCA, you must be the billing profile owner, contributor, reader, or invoice manager to view and download pricing. If you have an MPA, you must have the Admin Agent or [billing admin](/en-us/partner-center/account-settings/permissions-overview#billing-admin-role) role in the partner organization to view and download pricing.

### Download price sheets for billed charges

1. Sign-in to the [Azure portal](https://portal.azure.com).
2. Search for *Cost Management + Billing*.
3. Select a billing profile. Depending on your access, you might need to select a billing account first.
4. Select **Invoices**.
5. In the invoice grid, find the row of the invoice corresponding to the price sheet you want to download.
6. Select the ellipsis (`...`) at the end of the row.[![Screenshot that shows the ellipsis selected.](media/ea-pricing/billingprofile-invoicegrid-new.png)](media/ea-pricing/billingprofile-invoicegrid-new.png#lightbox)
7. If you want to see prices for the services in the selected invoice, select **Invoice price sheet**.
8. If you want to see prices for all Azure services for the given billing period, select **Azure price sheet**.[![Screenshot that shows context menu with price sheets.](media/ea-pricing/contextmenu-pricesheet01.png)](media/ea-pricing/contextmenu-pricesheet01.png#lightbox)
9. Azure prepares the price sheet. When the file is ready, it downloads automatically.

### Download usage and price sheet for the current billing period

If you have an MCA, you can download pricing for the current billing period at the billing profile scope.

1. Sign-in to the [Azure portal](https://portal.azure.com).
2. Search for *Cost Management + Billing*.
3. Select a billing profile. Depending on your access, you might need to select a billing account first.
4. In the left navigation menu, select **Billing profiles**.
5. On the Billing profiles page, select a billing profile.
6. At the bottom of the page under **Shortcuts**, select **Download usage and prices**.
7. On the Downloads page, select **Download Azure price sheet for *Month* *Year***.[![Screenshot that shows navigation to Download price sheet.](media/ea-pricing/download-price-sheet-month-year.png)](media/ea-pricing/download-price-sheet-month-year.png#lightbox)
8. Azure prepares the price sheet. When the file is ready, it downloads automatically.

## Columns in downloaded price sheets

You can't select a dataset version for a downloaded price sheet, and its version doesn't change when a new dataset version is released for exports. When new columns are added, they're added at the end of the file. If you process the file with scripts or reports, read columns by name instead of by position.

| Agreement type | Column descriptions | Flex Plan prices | Columns at the end of the file |
| --- | --- | --- | --- |
| EA (direct and indirect) | [EA price sheet schema](../dataset-schema/price-sheet-ea) | Not available | `priceFactors` |
| MCA | [Terms in your MCA price sheet](mca-understand-pricesheet) | A row for each Flex Plan offer that covers a meter, with `priceType` set to `FlexPlan` | `priceFactors` |
| MPA | [Terms in your MCA price sheet](mca-understand-pricesheet) | Same as MCA | `priceFactors` |

In a Flex Plan price row, `priceFactors` includes the product code of the Flex Plan offer. For more information, see [Review Flex Plan prices in your price sheet](../benefits/flex-plan/review-flex-plan-prices) and [Understand price factors and supplemental charge details](../automate/understand-price-factors-supplemental-charge-details). For more information about how downloads differ from exports, see [Compare downloads and exports](../understand/compare-downloads-exports).

## Estimate costs with the Azure pricing calculator

You can also use your organization’s pricing to estimate costs with the Azure pricing calculator.

1. Go to the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator).
2. On the top right, select **Sign in**.
3. Under **Programs and Offer** &gt; **Licensing Program**, select **Enterprise Agreement (EA)**.
4. Under **Programs and Offer** &gt; **Selected agreement**, select **None selected**.[![Screenshot showing the Programs and Offers available.](media/ea-pricing/ea-pricing-calculator-estimate.png)](media/ea-pricing/ea-pricing-calculator-estimate.png#lightbox)
5. Choose the organization.
6. Select **Apply**.
7. Search for and then add products to your estimate.
8. Estimated prices shown are based on pricing for the organization you selected.

## Check your billing account type

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for and select **Cost Management + Billing**.

    [![Screenshot that shows an Azure portal search for Cost Management and Billing.](../../includes/media/billing-check-account-type/billing-search-cost-management-billing.png)](../../includes/media/billing-check-account-type/billing-search-cost-management-billing.png#lightbox)
3. If you have access to just one billing scope, select **Properties** from the left menu.

    The **Type** value on the **Properties** pane determines the type of your account. It can be Microsoft Online Subscription Program, Enterprise Agreement, Microsoft Customer Agreement, or Microsoft Partner Agreement. To learn more about the types of billing accounts, see [View your billing accounts in the Azure portal](view-all-accounts).

    [![Screenshot that shows Microsoft Customer Agreement on the Properties pane.](../../includes/media/billing-check-account-type/billing-mca-property.png)](../../includes/media/billing-check-account-type/billing-mca-property.png#lightbox)

    If you have access to multiple billing scopes, select **Billing scopes** from the left menu, and then check the type in the **Billing account type** column.

    [![Screenshot that shows billing account types for multiple billing scopes.](../../includes/media/billing-check-account-type/billing-account-type-in-the-list.png)](../../includes/media/billing-check-account-type/billing-account-type-in-the-list.png#lightbox)