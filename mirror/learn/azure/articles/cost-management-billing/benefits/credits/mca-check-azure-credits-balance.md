---
layout: Conceptual
title: Track Your Azure Credit Balance for a Microsoft Customer Agreement - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/credits/mca-check-azure-credits-balance
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
description: Learn how to check the Azure credit balance for a Microsoft Customer Agreement.
author: shrutis06
ms.reviewer: shrshett
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.date: 2026-09-11T00:00:00.0000000Z
ms.author: shrshett
locale: en-us
document_id: a358d6ed-dc54-d6b8-4550-4333b5c77c5c
document_version_independent_id: 49a4636f-d4e1-4793-8ce9-7f7ea9056582
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/benefits/credits/mca-check-azure-credits-balance.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/benefits/credits/mca-check-azure-credits-balance
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/benefits/credits/mca-check-azure-credits-balance.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 7969f099-bdad-cef9-585f-02d49b459195
---

# Track Your Azure Credit Balance for a Microsoft Customer Agreement - Microsoft Cost Management | Microsoft Learn

You can check the Azure credit balance for your billing account for a Microsoft Customer Agreement in the Azure portal or through REST APIs.

In the billing account for a Microsoft Customer Agreement, credits are assigned to a billing profile. Each billing profile has its own credits that are automatically applied to the charges on its invoice. To view the Azure credit balance for a billing profile, you must have one of these roles:

- Owner, contributor, reader, or invoice manager role on the billing profile
- Owner, contributor, or reader role on the billing account

To learn more about the roles, see [Understand Microsoft Customer Agreement administrative roles in Azure](../../manage/understand-mca-roles).

Note

New credit can take up to 24 hours to appear in the Azure portal.

This article applies to a billing account for a Microsoft Customer Agreement. Check if you have access to a Microsoft Customer Agreement.

## How credits are used

In a billing account for a Microsoft Customer Agreement, you use billing profiles to manage your invoices and payment methods. A monthly invoice is generated for each billing profile, and you use the payment methods to pay the invoice.

Credits that you acquire are assigned to a billing profile. When an invoice is generated for the billing profile, credits are automatically applied to the total charges to calculate the amount that you need to pay. You pay the remaining amount by using payment methods like check, wire transfer, or credit card.

## Products and services that Azure credits don't cover

Azure credits don't apply to certain products and services. Any usage of these offerings is billed separately and charged regardless of your available Azure credit balance.

In general, Azure credits don't cover:

- Partner-provided products or services, along with non-Microsoft products on Microsoft Marketplace.
- Azure support plans.
- Software subscriptions or licenses that aren't billed as Azure consumption.

In addition to those general limitations, Azure Sponsorship credits don't cover:

- Entitlement-based purchases, even when Azure sells those offerings directly (for example, savings plans or reserved instances).

For AI models:

- Azure Sponsorship credits might cover [models that Azure sells directly](/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure).
- Azure Sponsorship credits don't cover [models from partners and the community](/en-us/azure/ai-foundry/foundry-models/concepts/models-from-partners).

## Check your credit balance

# [Azure portal](#tab/portal)
1. Sign in to the [Azure portal](https://portal.azure.com).
2. In the search box, enter **cost management + billing**.
3. Under **Services**, select **Cost Management + Billing**.

    ![Screenshot that shows a search for Cost Management + Billing in the Azure portal.](../../manage/media/mca-check-azure-credits-balance/billing-search-cost-management-billing.png)
4. On the **Billing scopes** pane, select the billing account for which you want to track the credit balance. The billing account should be of type **Microsoft Customer Agreement**.

    ![Screenshot that shows billing scopes with a selected billing account.](../../manage/media/mca-check-azure-credits-balance/list-of-scopes.png)

    Note

    The Azure portal remembers the last billing scope that you access and displays the scope the next time you open the list of billing scopes. You don't see the **Billing scopes** pane if you visited **Cost Management + Billing** earlier. If so, check that you're in the [right scope](/en-us/azure/cost-management-billing/manage/mca-check-azure-credits-balance?tabs=portal). If not, [switch the scope](/en-us/azure/cost-management-billing/manage/view-all-accounts) to select the billing account for a Microsoft Customer Agreement.
5. Go to **Billing** &gt; **Payment methods**, and then select the **Azure credits** tab.

    ![Screenshot that shows the tab for Azure credits in the Azure portal.](../../manage/media/mca-check-azure-credits-balance/azure-credits-page-azportal.png)

    Check the following items:

    - **Available balance**. This area shows available credits after your last invoice. This list includes all active credits only and excludes any expired or future credits. When your available balance drops to zero, you're charged for all your usage, including products that are eligible for credits.
    - **Credit Details**. View a list of all credits with details.

        | Term | Definition |
        | --- | --- |
        | **Source** | Acquisition source of the credit. |
        | **Effective date** | Date when you acquired the credit. |
        | **Expiration date** | Date when the credit expires. |
        | **Original amount** | Original amount of the credit. |
        | **Balance** | Credit balance after the latest invoice. |
        | **Status** | Current status of the credit. The status can be **Active**, **Used**, **Expired**, or **Expiring**. |

        Note

        If Azure credits don't appear, either you don't have credits or you didn't select the right scope. Select the billing account that has credits or one of its billing profiles. To learn how to change scopes, see [Switch billing scope in the Azure portal](../../manage/view-all-accounts#switch-billing-scope-in-the-azure-portal).
    - **View all transactions**. Select this link to open a pane that displays all transactions that affected your credit balance.

        ![Screenshot that shows credit transactions in the Azure portal for Cost Management + Billing.](../../manage/media/mca-check-azure-credits-balance/credits-transactions-azportal.png)

        | Term | Definition |
        | --- | --- |
        | **Date** | Date when the transaction happened. |
        | **Description** | Description of the transaction. |
        | **Amount** | Amount of the transaction. |
6. If you're viewing Azure credits at the billing account scope and the billing account has more than one billing profile, the **Azure credits** tab shows a table with a summary of Azure credits for each billing profile. Select a billing profile from the list, select payment methods, and then select **Azure credits** to view details for a billing profile.

    ![Screenshot that shows the credit list for a billing account.](../../manage/media/mca-check-azure-credits-balance/mca-account-credit-list.png)

# [REST API](#tab/rest)
You can use the [Azure Billing](/en-us/rest/api/billing/) and [Consumption](/en-us/rest/api/consumption/) APIs to programmatically get the credit balance for your billing account.

The following examples use REST APIs. Currently, PowerShell and the Azure CLI aren't supported.

### Find billing profiles that you can access

```json
GET https://management.azure.com/providers/Microsoft.Billing/billingAccounts?$expand=billingProfiles&api-version=2019-10-01-preview
```

The API response returns a list of billing accounts and their billing profiles.

```json
{
  "value": [
    {
      "id": "/providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx",
      "name": "5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx",
      "properties": {
        "accountId": "5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "accountStatus": "Active",
        "accountType": "Enterprise",
        "agreementType": "MicrosoftCustomerAgreement",
        "billingProfiles": [
          {
            "id": "/providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingProfiles/PBFV-xxxx-xxx-xxx",
            "name": "PBFV-xxxx-xxx-xxx",
            "properties": {
              "address": {
                "addressLine1": "AddressLine1",
                "city": "City",
                "companyName": "CompanyName",
                "country": "Country",
                "postalCode": "xxxxx",
                "region": "Region"
              },
              "currency": "USD",
              "displayName": "Development",
              "hasReadAccess": true,
              "invoiceDay": 5,
              "invoiceEmailOptIn": true
            },
            "type": "Microsoft.Billing/billingAccounts/billingProfiles"
          }
        ],
        "displayName": "Contoso",
        "hasReadAccess": true,
      },
      "type": "Microsoft.Billing/billingAccounts"
    }
  ]
}
```

Use the `displayName` property of the billing profile to identify the billing profile for which you want to check the credit balance. Copy the `id` value of the billing profile. For example, if you want to check the credit balance for the `Development` billing profile, copy `/providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingProfiles/PBFV-xxxx-xxx-xxx`. Paste this value somewhere so that you can use it in the next step.

### Get a list of credits

Make the following request. Replace `<billingProfileId>` with the `id` value that you copied (`/providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingProfiles/PBFV-xxxx-xxx-xxx`).

```json
GET https://management.azure.com/providers/Microsoft.Billing/billingAccounts/<billingAccountId>/billingProfiles/<billingProfileId>/providers/Microsoft.Consumption/lots?api-version=2023-03-01
```

The API response returns original credit amounts and available balance across all credit lots for the billing profile. This information includes active credits, expired credits, and credits that have a future start date. You can compute the available balance by aggregating the values in `closedBalance` across all active credits.

```json
{
  "value": [
    {
      "id": "/providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingProfiles/PBFV-xxxx-xxx-xxx/providers/Microsoft.Consumption/lots/f2ecfd94-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "f2ecfd94-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": "Microsoft.Consumption/lots",
      "eTag": null,
      "properties": {
        "originalAmount": {
          "currency": "USD",
          "value": 500.0
        },
        "closedBalance": {
          "currency": "USD",
          "value": 500.0
        },
        "source": "Azure Promotional Credit",
        "startDate": "09/18/2019 21:47:31",
        "expirationDate": "09/18/2020 21:47:30",
        "poNumber": ""
      }
    },
    {
      "id": "/providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingProfiles/xxxx-xxxx-xxx-xxx/providers/Microsoft.Consumption/lots/4ea40eb5-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "4ea40eb5-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": "Microsoft.Consumption/lots",
      "eTag": null,
      "properties": {
        "originalAmount": {
          "currency": "USD",
          "value": 500.0
        },
        "closedBalance": {
          "currency": "USD",
          "value": 497.87
        },
        "source": "Azure Promotional Credit",
        "startDate": "09/18/2019 21:47:31",
        "expirationDate": "09/18/2020 21:47:30",
        "poNumber": ""
      }
    }
  ]
}
```

| Element name | Description |
| --- | --- |
| `creditCurrency` | Currency of the credit. |
| `billingCurrency` | Currency used for billing. |
| `originalAmount` | Original amount of the credit, in USD. |
| `originalAmountInBillingCurrency` | Original amount of the credit, in billing currency with exchange rate. |
| `expirationDate` | Date when the credit expires. |
| `closedBalance` | Balance as of the last invoice, in USD. |
| `closedBalanceInBillingCurrency` | Balance as of the last invoice, in billing currency with exchange rate. |
| `reseller` | Information about the reseller, if any. |
| `source` | Source of the credit; for example, Azure promotional credit. |
| `startDate` | Date when the credit became active. |
| `expirationDate` | Date when the credit expires. |
| `poNumber` | Purchase order number of the invoice on which the credit was billed. |
| `isEstimatedBalance` | Indicates whether the balance is estimated. |

### Get transactions that affected credit balance

Make the following request. Replace `<billingProfileId>` with the `id` value that you copied earlier (`providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingProfiles/PBFV-xxxx-xxx-xxx`). You need to pass a `startDate` value and an `endDate` value to get transactions for your required duration.

```json
GET https://management.azure.com/providers/Microsoft.Billing/billingAccounts/<billingAccountID>/billingProfiles/<billingProfileID>/providers/Microsoft.Consumption/events?api-version=2023-03-01&startDate=<date>&endDate=<date>
```

The API response returns all transactions that affected the credit balance for your billing profile.

```json
{
  "value": [
    {
      "id": "/providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingProfiles/PBFV-xxxx-xxx-xxx`/providers/Microsoft.Consumption/events/e2032eb5-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "e2032eb5-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": "Microsoft.Consumption/events",
      "eTag": null,
      "properties": {
        "transactionDate": "10/11/2019",
        "description": "Credit eligible charges as of 10/11/2019",
        "newCredit": {
          "currency": "USD",
          "value": 0.0
        },
        "adjustments": {
          "currency": "USD",
          "value": 0.0
        },
        "creditExpired": {
          "currency": "USD",
          "value": 0.0
        },
        "charges": {
          "currency": "USD",
          "value": -1.74
        },
        "closedBalance": {
          "currency": "USD",
          "value": 998.26
        },
        "eventType": "PendingCharges",
        "invoiceNumber": ""
      }
    },
    {
      "id": "/providers/Microsoft.Billing/billingAccounts/5e98e158-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx_xxxx-xx-xx/billingProfiles/PBFV-xxxx-xxx-xxx/providers/Microsoft.Consumption/events/381efd80-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "381efd80-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": "Microsoft.Consumption/events",
      "eTag": null,
      "properties": {
        "transactionDate": "09/18/2019",
        "description": "New credit added on 09/18/2019",
        "newCredit": {
          "currency": "USD",
          "value": 500.0
        },
        "adjustments": {
          "currency": "USD",
          "value": 0.0
        },
        "creditExpired": {
          "currency": "USD",
          "value": 0.0
        },
        "charges": {
          "currency": "USD",
          "value": 0.0
        },
        "closedBalance": {
          "currency": "USD",
          "value": 1000.0
        },
        "eventType": "PendingNewCredit",
        "invoiceNumber": ""
      }
    }
  ]
}
```

| Element name | Description |
| --- | --- |
| `transactionDate` | Date when the transaction happened. |
| `description` | Description of the transaction. |
| `adjustments` | Credit adjustments for the transaction. |
| `creditExpired` | Amount of credit that expired. |
| `charges` | Charges for the transaction. |
| `closedBalance` | Balance after the transaction. |
| `eventType` | Type of the transaction. |
| `invoiceNumber` | Invoice number of the invoice on which the transaction is billed. It's empty for a pending transaction. |

---

## Check access to a Microsoft Customer Agreement

To determine whether you have access to a billing account for a Microsoft Customer Agreement, check the agreement type:

1. Go to the Azure portal. Search for and select **Cost Management + Billing**.

    [![Screenshot that shows a search for Cost Management + Billing.](../../../includes/media/billing-check-mca/billing-search-cost-management-billing.png)](../../../includes/media/billing-check-mca/billing-search-cost-management-billing.png#lightbox)
2. If you have access to just one billing scope, select **Settings** &gt; **Properties**. You have access to a billing account for a Microsoft Customer Agreement if the billing account type is **Microsoft Customer Agreement**.

    [![Screenshot of the Azure portal that shows a billing account type of Microsoft Customer Agreement for a single billing scope.](../../../includes/media/billing-check-mca/billing-mca-property.png)](../../../includes/media/billing-check-mca/billing-mca-property.png#lightbox)

    If you have access to multiple billing scopes, check the type in the **Billing account type** column. You have access to a billing account for a Microsoft Customer Agreement if the billing account type for any of the scopes is **Microsoft Customer Agreement**.

    [![Screenshot of the Azure portal that shows a billing account type of Microsoft Customer Agreement for multiple billing scopes.](../../../includes/media/billing-check-mca/billing-mca-in-the-list.png)](../../../includes/media/billing-check-mca/billing-mca-in-the-list.png#lightbox)

## Get support

If you need help, [contact support](https://portal.azure.com/?#blade/Microsoft_Azure_Support/HelpAndSupportBlade) to get your issue resolved quickly.