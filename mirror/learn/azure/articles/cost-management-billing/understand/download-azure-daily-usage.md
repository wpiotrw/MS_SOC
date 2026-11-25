---
layout: Conceptual
title: View and download Azure usage and charges - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/download-azure-daily-usage
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
description: Learn how to download or view your Azure daily usage and charges, and see other available resources.
keywords: billing usage, usage charges, usage download, view usage, azure invoice, azure usage
author: jkinma39
ms.author: jkinma
ms.reviewer: jkinma
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.custom: devx-track-azurecli
ms.date: 2026-11-19T00:00:00.0000000Z
service.tree.id: 95459a4b-434c-4f83-879b-aa5f509fc7fa
locale: en-us
document_id: e301c2f1-5f0b-3151-cd8b-f3b4da3eb06c
document_version_independent_id: e334683c-3dd5-fec3-331d-07a28ea73f62
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/understand/download-azure-daily-usage.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/understand/download-azure-daily-usage
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/understand/download-azure-daily-usage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: d4219ef5-1d4c-181b-49d5-0651839d747a
---

# View and download Azure usage and charges - Microsoft Cost Management | Microsoft Learn

You can download a daily breakdown of your Azure usage and charges in the Azure portal. Only certain roles have permission to get Azure usage information, like the Account Administrator or Enterprise Administrator. To learn more about getting access to billing information, see [Manage access to Azure billing using roles](../manage/manage-billing-access).

If you have a Microsoft Customer Agreement (MCA), you must be a billing profile Owner, Contributor, Reader, or Invoice manager to view your Azure usage and charges. If you have a Microsoft Partner Agreement (MPA), only the [billing admin](/en-us/partner-center/account-settings/permissions-overview#billing-admin-role) and Admin Agent role in the partner organization Microsoft can view and download Azure usage and charges.

Based on the type of subscription that you use, options to download your usage and charges vary.

Your cost and usage data files show unrounded data. For more information about rounding, see [Cost rounding](../costs/understand-cost-mgt-data#cost-rounding).

Note

The usage file that you download includes the `priceFactors` and `supplementalChargeDetails` columns at the end of the file. These columns explain how a charge was priced, such as when a savings plan or Flex Plan applies. For more information, see [Understand price factors and supplemental charge details](../automate/understand-price-factors-supplemental-charge-details). Downloaded usage files keep their schema version. To select a dataset version, such as 2026-10-01, use [exports](../costs/tutorial-improved-exports). For more information, see Columns in downloaded usage files and [Compare downloads and exports](compare-downloads-exports).

If you want to get cost and usage data using the Azure CLI, see [Get usage data with the Azure CLI](../automate/get-usage-data-azure-cli).

## Download usage for MOSP billing accounts

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for *Cost Management + Billing*.![Screenshot showing Azure portal search for Cost Management + Billing.](media/download-azure-daily-usage/portal-cm-billing-search.png)
3. Depending on your access, you might need to select a Billing account or Billing profile.
4. In the left menu, select **Invoices** under **Billing**.
5. In the invoice grid, find the row of the billing period corresponding to the usage you want to download.
6. Select the **download icon** or the ellipsis (`...`) on the right.![Screenshot showing the Cost Management + Billing Invoices page with the download option.](media/download-azure-daily-usage/download-usage-others.png)
7. The Download pane opens on the right. Select **Download** from the **Usage Details** section.

## Download usage for EA customers

To view and download usage data as a EA customer, you must be an Enterprise Administrator, Account Owner, or Department Admin with the view charges policy enabled.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for *Cost Management + Billing*.![Screenshot shows an Azure portal search.](media/download-azure-daily-usage/portal-cm-billing-search.png)
3. If you have access to multiple billing accounts, select the billing scope for your EA billing account.
4. Select **Usage + charges**.
5. For the month you want to download, select **Download**.![Screenshot shows the Cost Management + Billing Invoices page for E A customers.](media/download-azure-daily-usage/download-usage-ea.png)
6. On the Download Usage + Charges page, under Usage Details, select the type of charges that you want to download from the list. Depending on your selection, the CSV file provides all charges (usage and purchases) including RI (reservation) purchases. Or, amortized charges (usage and purchases) including reservation purchases. ![Screenshot showing the Usage Details charge type selection to download.](media/download-azure-daily-usage/select-usage-detail-charge-type.png)
7. Select **Prepare document**.
8. It could take a while for Azure to prepare your download, depending on your monthly usage. When it's ready for download, select **Download csv**.

## Download usage for your Microsoft Customer Agreement

To view and download usage data for a billing profile, you must be a billing profile Owner, Contributor, Reader, or Invoice manager.

Use the following information to download your Azure usage file.

### Download usage file from the billing account or billing profile overview page

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for *Cost Management + Billing*.
3. If necessary, select a billing scope.
4. On the billing scope overview page, at the bottom of the page under **Shortcuts**, select **Download usage and prices**.
5. On the Download usage and prices page, under **Azure usage file**, select **Prepare**. A notification message appears stating that the usage file is being prepared. [![Screenshot showing navigation to Download usage and prices.](media/download-azure-daily-usage/download-usage-prices.png)](media/download-azure-daily-usage/download-usage-prices.png#lightbox)
6. When the file is ready to download, select **Download**. If you missed the notification, you can view it from **Notifications** area in top right of the Azure portal (the bell symbol).

### Download the usage file from the Invoices page

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for *Cost Management + Billing*.
3. If necessary, select a billing scope.
4. Select Billing&gt;Invoices
5. On the invoice list view, click the ellipses at the end of any invoice and select "Prepare Azure usage file".
6. You can also download the Azure usage file from the invoice details page.

### Calculate discount in the usage file

You can use the two columns `paygCostInBillingCurrency` and `costInBillingCurrency`to calculate your discount amount and discount percentage.

To determine discount amount = `( paygCostInBillingCurrency) - ( costInBillingCurrency)`

To determine discount percentage = `( paygCostInBillingCurrency - costInBillingCurrency) / paygCostInBillingCurrency * 100`

For more information on cost details fields, see: [Understand cost details fields](../automate/understand-usage-details-fields#list-of-fields-and-descriptions)

## Download usage for an indirect Enterprise Agreement

If a partner manages your enrollment (an indirect EA), partner administrators can download usage for the enrollment. Enterprise administrators of indirect enrollments use the steps in Download usage for EA customers.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for *Cost Management + Billing*.
3. Select **Billing scopes**, and then select the billing account that you want to work with.
4. Select **Billing profiles**, and then select the billing profile that you want to work with.
5. Select **Usage + charges**.
6. For the month you want to download, select **Download**.
7. On the **Download Usage + Charges** page, under **Usage Details**, select the type of charges, and then select **Prepare document**.
8. When it's ready for download, select **Download csv**.

For more information, see [View your usage summary details and download reports for EA enrollments](../manage/direct-ea-azure-usage-charges-invoices#download-usage-charges-csv-file).

## Download usage for a Microsoft Partner Agreement

If you're a Cloud Solution Provider (CSP) partner with a Microsoft Partner Agreement (MPA), you must have the Admin Agent or billing admin role to download usage. You download usage for each billing profile's invoice.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for *Cost Management + Billing*.
3. Select your billing account, select **Billing profiles**, and then select a billing profile.
4. Select **Invoices**.
5. In the invoice grid, select the ellipsis (`...`) at the end of the row for the invoice, and then select the option to download the Azure usage file.

Customers of CSP partners can't download usage files from a billing account. If their partner turns on the cost visibility policy, they can view their costs at pay-as-you-go rates in cost analysis. For more information, see [Get started with Cost Management for partners](../costs/get-started-partners).

## Columns in downloaded usage files

You can't select a dataset version for a downloaded usage file, and its version doesn't change when a new dataset version is released for exports. When new columns are added, they're added at the end of the file. If you process the file with scripts or reports, read columns by name instead of by position.

| Agreement type | Column descriptions | Flex Plan | Columns at the end of the file |
| --- | --- | --- | --- |
| EA (direct and indirect) | [EA cost and usage details](../dataset-schema/cost-usage-details-ea) | Not available | `priceFactors`, `supplementalChargeDetails` |
| MCA | [MCA cost and usage details](../dataset-schema/cost-usage-details-mca) | `pricingModel` is `FlexPlan` for Flex Plan purchases and for usage that a Flex Plan covered | `priceFactors`, `supplementalChargeDetails` |
| MPA | [MPA cost and usage details](../dataset-schema/cost-usage-details-mca-partner) | Same as MCA | `priceFactors`, `supplementalChargeDetails` |

For more information about how downloads differ from exports, see [Compare downloads and exports](compare-downloads-exports).

## Get usage data with Azure CLI

Start by preparing your environment for the Azure CLI:

- Use the Bash environment in [Azure Cloud Shell](/en-us/azure/cloud-shell/overview). For more information, see [Get started with Azure Cloud Shell](/en-us/azure/cloud-shell/quickstart).

    [![](../../reusable-content/azure-cli/media/hdi-launch-cloud-shell.png)](https://shell.azure.com)
- If you prefer to run CLI reference commands locally, [install](/en-us/cli/azure/install-azure-cli) the Azure CLI. If you're running on Windows or macOS, consider running Azure CLI in a Docker container. For more information, see [How to run the Azure CLI in a Docker container](/en-us/cli/azure/run-azure-cli-docker).

    - If you're using a local installation, sign in to the Azure CLI by using the [az login](/en-us/cli/azure/reference-index#az-login) command. To finish the authentication process, follow the steps displayed in your terminal. For other sign-in options, see [Authenticate to Azure using Azure CLI](/en-us/cli/azure/authenticate-azure-cli).
    - When you're prompted, install the Azure CLI extension on first use. For more information about extensions, see [Use and manage extensions with the Azure CLI](/en-us/cli/azure/azure-cli-extensions-overview).
    - Run [az version](/en-us/cli/azure/reference-index?#az-version) to find the version and dependent libraries that are installed. To upgrade to the latest version, run [az upgrade](/en-us/cli/azure/reference-index?#az-upgrade).

Then use the [az costmanagement export](/en-us/cli/azure/costmanagement/export) commands to export usage data to an Azure storage account. You can download the data from there.

1. Create a resource group or use an existing resource group. To create a resource group, run the [az group create](/en-us/cli/azure/group#az-group-create) command:

    ```azurecli
    az group create --name TreyNetwork --location "East US"
    ```
2. Create a storage account to receive the exports or use an existing storage account. To create an account, use the [az storage account create](/en-us/cli/azure/storage/account#az-storage-account-create) command:

    ```azurecli
    az storage account create --resource-group TreyNetwork --name cmdemo
    ```
3. Run the [az costmanagement export create](/en-us/cli/azure/costmanagement/export#az-costmanagement-export-create) command to create the export:

    ```azurecli
    az costmanagement export create --name DemoExport --type Usage \
    --scope "subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e" --storage-account-id cmdemo \
    --storage-container democontainer --timeframe MonthToDate --storage-directory demodirectory
    ```

## Need help? Contact us.

If you have questions or need help, [create a support request](https://go.microsoft.com/fwlink/?linkid=2083458).