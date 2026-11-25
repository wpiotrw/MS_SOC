---
layout: Conceptual
title: Compare downloads and exports for cost and price data - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/compare-downloads-exports
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
description: Learn how usage files and price sheets that you download differ from exports, including where to get them, which schema version they use, and where new columns appear for each agreement type.
author: Britt-Henderson
ms.author: britth
ms.reviewer: vikdesai
ms.service: cost-management-billing
ms.subservice: cost-management
ms.topic: concept-article
ms.date: 2026-11-19T00:00:00.0000000Z
locale: en-us
document_id: a1ca9441-f903-8381-5ff9-6249ed966482
document_version_independent_id: a248b88f-9d0f-4524-f4f9-316e974620a0
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/understand/compare-downloads-exports.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/understand/compare-downloads-exports
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/understand/compare-downloads-exports.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/a9a12e3a-5d9d-4197-ad96-b826bc774b60
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6dfd60ec-b0d6-48ef-9c74-057162ea03fb
platformId: d7f44f55-98b2-4586-f518-906a74fe2ce5
---

# Compare downloads and exports for cost and price data - Microsoft Cost Management | Microsoft Learn

You can get your cost and usage details and your price sheet in two ways:

- **Downloads**: Download a file from the Azure portal, or request one by using a download API.
- **Exports**: Have Cost Management write the data to an Azure Storage account, once or on a schedule.

Both provide the same kinds of data, but they differ in how you get the data and in how their columns change over time. This article explains the differences and shows where to download usage files and price sheets for each agreement type.

## Differences between downloads and exports

| Feature | Downloads | Exports |
| --- | --- | --- |
| How you get the data | Cost Management + Billing in the Azure portal, or a download API | The **Exports** page in Cost Management, or the Exports API |
| Where the data goes | Your browser, or a file location that the API returns | An Azure Storage account that you choose |
| When | On demand, one file at a time | One time, daily, or monthly |
| Schema version | Fixed to the latest API version. | You select a dataset version, such as 2026-10-01. |
| Best for | Reviewing one billing period associated with an invoice. | Recurring reports, large datasets, and automation |

For more information about exports, see [Create and manage exports](../costs/tutorial-improved-exports).

## How schema versions work

Each dataset, such as cost and usage details or the price sheet, has versions that define its columns. For the list of datasets and versions, see [Dataset schema index](../dataset-schema/schema-index).

- **Exports**: You select the dataset version when you create or update an export. To get new columns, select the latest version.
- **Downloads**: You can't select a version, and the version doesn't always change if new columns are added (but when new columns are added to the same API version, they're added at the end of the downloaded file, so existing columns keep their positions).

New values in existing columns can appear in every version and in downloads. For example, as of November 2026, the `pricingModel` column shows `FlexPlan` for Flex Plan purchases and covered usage in MCA price sheets in every version.

## Where to download usage files and price sheets

Where you download your data depends on your agreement type. To check your agreement type, see [Check your billing account type](../manage/ea-pricing#check-your-billing-account-type).

| Agreement type | Usage file | Price sheet | Column descriptions |
| --- | --- | --- | --- |
| Enterprise Agreement (EA), direct | [Download usage for EA customers](download-azure-daily-usage#download-usage-for-ea-customers) | [Download pricing for an Enterprise Agreement](../manage/ea-pricing#download-pricing-for-an-enterprise-agreement) | [EA cost and usage details](../dataset-schema/cost-usage-details-ea), [EA price sheet](../dataset-schema/price-sheet-ea) |
| EA, indirect (managed by a partner) | [Download usage for an indirect Enterprise Agreement](download-azure-daily-usage#download-usage-for-an-indirect-enterprise-agreement) | [Download pricing for an indirect Enterprise Agreement](../manage/ea-pricing#download-pricing-for-an-indirect-enterprise-agreement) | Same as direct EA |
| Microsoft Customer Agreement (MCA) | [Download usage for your Microsoft Customer Agreement](download-azure-daily-usage#download-usage-for-your-microsoft-customer-agreement) | [Download pricing for an MCA or MPA account](../manage/ea-pricing#download-pricing-for-an-mca-or-mpa-account) | [MCA cost and usage details](../dataset-schema/cost-usage-details-mca), [Terms in your MCA price sheet](../manage/mca-understand-pricesheet) |
| Microsoft Partner Agreement (MPA), for CSP partners | [Download usage for a Microsoft Partner Agreement](download-azure-daily-usage#download-usage-for-a-microsoft-partner-agreement) | [Download pricing for an MCA or MPA account](../manage/ea-pricing#download-pricing-for-an-mca-or-mpa-account) | [MPA cost and usage details](../dataset-schema/cost-usage-details-mca-partner) |
| Customers of CSP partners | Not available. If your partner allows it, view your costs in cost analysis or export them. | Not available. Your partner provides your prices. | [CSP subscription cost and usage details](../dataset-schema/cost-usage-details-mca-partner-subscription) |