---
layout: Conceptual
title: Transfer Azure product billing ownership to a Microsoft Customer Agreement - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/mca-request-billing-ownership
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
description: Learn how to transfer billing ownership of Azure subscriptions, reservations, and savings plans.
ms.topic: how-to
ms.date: 2026-10-30T00:00:00.0000000Z
author: ChrisLodwig
ms.author: clodwig
ms.reviewer: clodwig
ms.service: cost-management-billing
ms.subservice: billing
ms.custom: sfi-image-nochange
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: 3da55773-b402-6079-d8e2-76eb3b4f25e0
document_version_independent_id: 4b6ec90e-b9c4-f586-11cf-f5ab2f562266
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/mca-request-billing-ownership.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/mca-request-billing-ownership
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/mca-request-billing-ownership.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: b78bfa3f-ae9c-7987-0808-81f112762b51
---

# Transfer Azure product billing ownership to a Microsoft Customer Agreement - Microsoft Cost Management | Microsoft Learn

This article helps you transfer billing ownership for your Azure products (subscriptions, reservations, and savings plans) to a Microsoft Customer Agreement when:

- You want to move billing responsibilities for a product to a different billing owner.
- You want to transfer your Azure products from one licensing agreement to another. For example, from an Enterprise Agreement or a Microsoft Online Subscription Program (MOSP) to a Microsoft Customer Agreement.
- You want to transfer reservation or savings plan ownership.

Check if you have access to a Microsoft Customer Agreement.

The transition moves only the billing responsibility for your Azure products – the Azure resources tied to your products don't move, so the transition doesn't interrupt your Azure services.

This process contains the following primary tasks:

1. Request billing ownership
2. Review and approve the transfer request
3. Check transfer request status

There are four options to transfer products:

- Transfer only subscriptions
- Transfer only reservations
- Transfer only savings plans
- Transfer a combination of products

When you send or accept a transfer request, you agree to terms and conditions. For more information, see [Transfer terms and conditions](subscription-transfer#transfer-terms-and-conditions).

Before you transfer billing products, read [Supplemental information about transfers](subscription-transfer#supplemental-information-about-transfers).

Note

You can't transfer subscriptions to a Microsoft Entra B2B or Azure B2C tenant.

## Prerequisites

Important

- Confirm that your source agreement, destination agreement, and transfer method support the reservation or Savings Plan transfer in the [product transfer support table](subscription-transfer#product-transfer-support).
- An individual product-transfer request can't transfer a non-USD-priced Savings Plan. If you select one, the request displays a warning directing you to contact Azure support. For currency outcomes after confirming transfer eligibility, use the [currency-change guidance in the Azure product transfer hub](subscription-transfer#transfer-reservations-and-savings-plans-with-currency-change). The EA-to-MCA enrollment migration has separate Savings Plan replacement options; don't apply either migration option to an individual product-transfer request.
- When you transfer subscriptions, cost and usage data for your Azure products aren't accessible after the transfer. We recommend that you [download your cost and usage data](../understand/download-azure-daily-usage) and invoices before you transfer subscriptions.

Before you begin, make sure that the people involved in the product transfer have the required permissions.

Note

To perform a transfer, the destination account must be a paid account with a valid form of payment. For example, if the destination is an Azure free account, you can upgrade it to a pay-as-you-go Azure plan under a Microsoft Customer Agreement. Then you can make the transfer.

You can also watch the following video, which outlines each step of the subscription transfer process. However, it doesn't cover reservation or savings plan transfers.

### Required permissions for the transfer requester

The product transfer requester must have one of the following permissions:

For a Microsoft Customer Agreement, the person must have an owner or contributor role for the billing account or for the relevant billing profile or invoice section. For more information, see [Billing roles and tasks](understand-mca-roles#invoice-section-roles-and-tasks).

### Required permissions for the transfer recipient

The subscription, reservation, or savings plan product owner (transfer request recipient) must have one of the following permissions:

- For a Microsoft Customer Agreement, the person must have an owner or contributor role for the billing account or for the relevant billing profile or invoice section. For more information, see [Billing roles and tasks](understand-mca-roles#invoice-section-roles-and-tasks).
- For an Enterprise Agreement subscription, the person must be an account owner or EA administrator.
- For an Enterprise Agreement savings plan or reservation, the person must be an EA administrator.
- For a Microsoft Online Subscription Agreement, the person must be an Account Administrator.

### Marketplace purchases

When you transfer a subscription from an Enterprise Agreement to a Microsoft Customer Agreement, Marketplace purchases transfer with it when the following conditions are met:

- The Marketplace purchase in the EA subscription must be active.
- The Marketplace purchase must pass all eligibility checks before transfer. For example, the purchase must be available for use in the target agreement.
- All other assets in the source subscription must also be able to successfully be transferred. Otherwise, the transfer fails.

Software as a service (SaaS) products are an exception. A SaaS subscription is billed through the Azure subscription but doesn't move with it, so you transfer SaaS billing ownership separately. For more information, see [Software as a Service (SaaS) transfer](mpa-request-ownership#software-as-a-service-saas-transfer).

## Create the product transfer request

The person creating the transfer request uses the following procedure. The transfer request asks the product owner to allow subscriptions and/or reservations associated with a subscription to be transferred.

When the request is created, an email is sent to the target recipient.

The following procedure has you navigate to **Transfer requests** by selecting **Billing scopes** &gt; **Billing account** &gt; **Billing profile** &gt; **Invoice sections** &gt; **Add a new request**. If you navigate to **Add a new request** from a billing profile, select a billing profile, and then select an invoice section.

1. Sign in to the [Azure portal](https://portal.azure.com) as an invoice section owner or contributor for a Microsoft Customer Agreement billing account. Use the same credentials that you used to accept your Microsoft Customer Agreement.
2. Search for **Cost Management + Billing**.[![Screenshot that shows Azure portal search for Cost Management + Billing.](media/mca-request-billing-ownership/billing-search-cost-management-billing.png)](media/mca-request-billing-ownership/billing-search-cost-management-billing.png#lightbox)
3. On the billing scopes page, select **Billing scopes** and then select the billing account, which would be used to pay for Azure usage in your products. Select the billing account labeled **Microsoft Customer Agreement**.[![Screenshot that shows search in portal for Cost Management + Billing.](media/mca-request-billing-ownership/billing-scopes.png)](media/mca-request-billing-ownership/billing-scopes.png#lightbox) The Azure portal remembers the last billing scope that you accessed and displays that scope the next time you open the Cost Management + Billing page. You won't see the billing scopes page if you visited Cost Management + Billing earlier. If so, check that you're in the right scope. If not, [switch the scope](view-all-accounts#switch-billing-scope-in-the-azure-portal) to select the billing account for a Microsoft Customer Agreement.
4. Select **Billing profiles** from the left-hand side and then select a **Billing profile** from the list. Once you take over the ownership of the products, their usage is billed to this billing profile.[![Screenshot that shows selecting billing profiles.](media/mca-request-billing-ownership/billing-profile.png)](media/mca-request-billing-ownership/billing-profile.png#lightbox)*If you don't see Billing profiles, you aren't in the right billing scope.* You need to select a billing account for a Microsoft Customer Agreement and then select Billing profiles. To learn how to change scopes, see [Switch billing scopes in the Azure portal](view-all-accounts#switch-billing-scope-in-the-azure-portal).
5. Select **Invoice sections** from the left-hand side and then select an invoice section from the list. Each billing profile contains one invoice section by default. Select the invoice where you want to move your Azure product billing - that's where the Azure product consumption is transferred to.[![Screenshot that shows selecting invoice sections.](media/mca-request-billing-ownership/invoice-section.png)](media/mca-request-billing-ownership/invoice-section.png#lightbox)
6. Select **Transfer requests** from the lower-left menu, and then select **Add a new request**. Enter the email address of the user you're requesting billing ownership from. The user must have an account administrator role for the old products.[![Screenshot that shows selecting transfer requests.](media/mca-request-billing-ownership/transfer-request-add-email.png)](media/mca-request-billing-ownership/transfer-request-add-email.png#lightbox)
7. Select **Send transfer request**.

## Review and approve transfer request

The recipient of the transfer request uses the following procedure to review and approve the transfer request. They can choose to:

- Transfer one or more subscriptions only
- Transfer one or more reservations only
- Transfer one or more savings plans only
- Transfer a combination of products

1. The user gets an email with instructions to review your transfer request. Select **Review the request** to open it in the Azure portal.[![Screenshot that shows review transfer request email.](media/mca-request-billing-ownership/mca-review-transfer-request-email.png)](media/mca-request-billing-ownership/mca-review-transfer-request-email.png#lightbox) If the transfer recipient’s user account doesn’t have email enabled, the person that created the request can manually give the target recipient a link to accept the transfer request after the request is created. The person that created the request can navigate to Transfer status page, copy it, and then manually give it to the recipient.[![Screenshot showing the Transfer status where you can copy the transfer link sent to the recipient.](media/mca-request-billing-ownership/transfer-status-pending-link.png)](media/mca-request-billing-ownership/transfer-status-pending-link.png#lightbox)
2. In the Azure portal, the user selects the billing account that they want to transfer Azure products from. Then they select eligible subscriptions on the **Subscriptions** tab. If the owner doesn’t want to transfer subscriptions and instead wants to transfer reservations only, make sure that no subscriptions are selected. [![Screenshot showing the Subscriptions tab.](media/mca-request-billing-ownership/review-transfer-request-subscriptions-select.png)](media/mca-request-billing-ownership/review-transfer-request-subscriptions-select.png#lightbox)*Disabled subscriptions can't be transferred.*
3. If there are reservations available to transfer, select the **Reservations** tab, and then select them. If you don't want to transfer reservations, make sure that no reservations are selected. If reservations are transferred, they're applied to the scope set in the request. If you want to change the scope of the reservation after it’s transferred, see [Change the reservation scope](../reservations/manage-reserved-vm-instance#change-the-reservation-scope). [![Screenshot showing the Reservations tab.](media/mca-request-billing-ownership/review-transfer-request-reservations-select.png)](media/mca-request-billing-ownership/review-transfer-request-reservations-select.png#lightbox)
4. If there are savings plans available to transfer, select the **Savings plan** tab, and then select them. If you don't want to transfer savings plans, make sure that no savings plans are selected. If savings plans are transferred, they're applied to the scope set in the request. If you want to change the scope of the savings plan after it's transferred, see [Change the savings plan scope](../savings-plan/manage-savings-plan#change-the-savings-plan-scope). [![Screenshot showing the Savings plan tab.](media/mca-request-billing-ownership/review-transfer-request-savings-plan-select.png)](media/mca-request-billing-ownership/review-transfer-request-savings-plan-select.png#lightbox)
5. Select the **Review request** tab and verify the information about the products to transfer. If there are warning or failed status messages, see the following information. When you're ready to continue, select **Transfer**.[![Screenshot showing the Review request tab where you review your transfer selections.](media/mca-request-billing-ownership/review-transfer-request-complete.png)](media/mca-request-billing-ownership/review-transfer-request-complete.png#lightbox)
6. The `Transfer is in progress` message is briefly shown. When the transfer is completed successfully, you see the Transfer details page with the `Transfer completed successfully` message.[![Screenshot showing the Transfer completed successfully page.](media/mca-request-billing-ownership/transfer-completed-successfully.png)](media/mca-request-billing-ownership/transfer-completed-successfully.png#lightbox)

On the Review request tab, the following status messages might be displayed.

- **Ready to transfer** - Validation for this Azure product passed and can be transferred.
- **Warnings** - There's a warning for the selected Azure product. While the product can still be transferred, doing so has some consequence that the user should be aware of in case they want to take mitigating actions. For example, the Azure subscription being transferred is benefitting from a reservation. After transfer, the subscription will no longer receive that benefit. To maximize savings, ensure that the reservation is associated to another subscription that can use its benefits. Instead, the user can also choose to go back to the selection page and unselect this Azure subscription. Select **Check details** for more information.
- **Failed** - The selected Azure product can't be transferred because of an error. The user needs to go back to the selection page and unselect this product to transfer the other selected Azure products.

## Check the transfer request status

As the user that requested the transfer:

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for **Cost Management + Billing**.
3. In the billing scopes page, select the billing account where the transfer request was started and then in the left menu, select **Transfer requests**.
4. Select the billing profile and invoice section where the transfer request was started and review the status.[![Screenshot that shows the list of transfers with their status.](media/mca-request-billing-ownership/transfer-requests-status-completed.png)](media/mca-request-billing-ownership/transfer-requests-status-completed.png#lightbox)

The Transfer requests page displays the following information:

| Column | Definition |
| --- | --- |
| Request date | The date when the transfer request was sent |
| Recipient | The email address of the user that you sent the request to transfer billing ownership |
| Expiration date | The date when the request expires |
| Status | The status of transfer request |

The transfer request can have one of the following states:

| Status | Definition |
| --- | --- |
| In progress | The user hasn't accepted the transfer request. |
| Processing | The user approved the transfer request. Billing for the products that the user selected is getting transferred to your invoice section. |
| Completed | The billing for products that the user selected is transferred to your invoice section. |
| Finished with errors | The request completed but billing for some products that the user selected couldn't be transferred. |
| Expired | The user didn't accept the request on time and it expired. |
| Canceled | Someone with access to the transfer request canceled the request. |
| Declined | The user declined the transfer request. |

As the user that approved the transfer:

Select a transfer request to view details. The transfer details page displays the following information:[![Screenshot that shows the Transfer status page with example status.](media/mca-request-billing-ownership/transfer-status-success-approver-view.png)](media/mca-request-billing-ownership/transfer-status-success-approver-view.png#lightbox)

| Column | Definition |
| --- | --- |
| Transfer ID | The unique ID for your transfer request. If you submit a support request, share the ID with Azure support to speed up your support request. |
| Transfer requested date | The date when the transfer request was sent. |
| Transfer requested by | The email address of the user who sent the transfer request. |
| Transfer request expires date | Only appears while the transfer status is `Pending`. The date when the transfer request expires. |
| Transfer link sent to recipient | Only appears while the transfer status is `Pending`. The URL that was sent to the user to review the transfer request. |
| Transfer completed date | Only appears when the transfer status is `Completed`. The date and time that the transfer was completed. |

## Supported subscription types

You can request billing ownership of products for the following subscription types.

- [Action pack](https://azure.microsoft.com/offers/ms-azr-0025p/)¹
- [Azure Pass Sponsorship](https://azure.microsoft.com/offers/azure-pass/)¹
- [Enterprise Dev/Test](https://azure.microsoft.com/offers/ms-azr-0148p/)
- [Pay-As-You-Go](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn)
- [Pay-As-You-Go Dev/Test](https://azure.microsoft.com/offers/ms-azr-0023p/)
- [Microsoft Azure Plan](https://azure.microsoft.com/offers/ms-azr-0017g/)²
- [Microsoft Azure Sponsored Offer](https://azure.microsoft.com/offers/ms-azr-0036p/)¹
- [Microsoft Enterprise Agreement](https://azure.microsoft.com/pricing/enterprise-agreement/)
    - Subscription, reservation, and savings plan transfers are supported for EA customers. For more details, see [Azure product transfer hub](subscription-transfer).
- [Microsoft Customer Agreement](https://azure.microsoft.com/pricing/purchase-options/microsoft-customer-agreement/)
- [Microsoft Cloud Partner Program](https://azure.microsoft.com/offers/ms-azr-0025p/)¹
- [MSDN Platforms](https://azure.microsoft.com/offers/ms-azr-0062p/)¹
- [Visual Studio Enterprise (Cloud Partner Program) subscribers](https://azure.microsoft.com/offers/ms-azr-0029p/)¹
- [Visual Studio Enterprise subscribers](https://azure.microsoft.com/offers/ms-azr-0063p/)¹
- [Visual Studio Professional](https://azure.microsoft.com/offers/ms-azr-0059p/)¹
- [Visual Studio Test Professional subscribers](https://azure.microsoft.com/offers/ms-azr-0060p/)¹

¹ Any credit available on the subscription won't be available in the new account after the transfer.

² Only supported for products in accounts that are created during sign-up on the Azure website.

## Troubleshooting

Use the following troubleshooting information if you're having trouble transferring subscriptions.

### Original Azure subscription billing owner leaves your organization

It's possible that the original billing account owner who created an Azure account and an Azure subscription leaves your organization. If that situation happens, then their user identity is no longer in the organization's Microsoft Entra ID. Then the Azure subscription doesn't have a billing owner. This situation prevents anyone from performing billing operations to the account, including viewing and paying bills. The subscription could go into a past-due state. Eventually, the subscription could get disabled because of nonpayment. Ultimately, the subscription could get deleted, affecting every service that runs on the subscription.

When a subscription no longer has a valid billing account owner, Azure sends an email to other billing account owners and subscription owners informing them of the situation and providing a link to accept billing ownership of the subscription. Any of these users can select the link to accept billing ownership. For more information about billing roles, see [Billing roles](understand-mca-roles) and [Azure roles, Microsoft Entra roles, and classic subscription administrator roles](../../role-based-access-control/rbac-and-directory-admin-roles).

Here's an example of what the email looks like.

[![Screenshot showing an example email to accept billing ownership.](media/mca-request-billing-ownership/orphaned-subscription-email.png)](media/mca-request-billing-ownership/orphaned-subscription-email.png#lightbox)

Additionally, Azure shows a banner in the subscription details window in the Azure portal for billing owners and subscription owners. Select the link in the banner to accept billing ownership.

[![Screenshot showing an example of a subscription without a valid billing owner.](media/mca-request-billing-ownership/orphaned-subscription-example.png)](media/mca-request-billing-ownership/orphaned-subscription-example.png#lightbox)

## Check for access

To determine whether you have access to a billing account for a Microsoft Customer Agreement, check the agreement type:

1. Go to the Azure portal. Search for and select **Cost Management + Billing**.

    [![Screenshot that shows a search for Cost Management + Billing.](../../includes/media/billing-check-mca/billing-search-cost-management-billing.png)](../../includes/media/billing-check-mca/billing-search-cost-management-billing.png#lightbox)
2. If you have access to just one billing scope, select **Settings** &gt; **Properties**. You have access to a billing account for a Microsoft Customer Agreement if the billing account type is **Microsoft Customer Agreement**.

    [![Screenshot of the Azure portal that shows a billing account type of Microsoft Customer Agreement for a single billing scope.](../../includes/media/billing-check-mca/billing-mca-property.png)](../../includes/media/billing-check-mca/billing-mca-property.png#lightbox)

    If you have access to multiple billing scopes, check the type in the **Billing account type** column. You have access to a billing account for a Microsoft Customer Agreement if the billing account type for any of the scopes is **Microsoft Customer Agreement**.

    [![Screenshot of the Azure portal that shows a billing account type of Microsoft Customer Agreement for multiple billing scopes.](../../includes/media/billing-check-mca/billing-mca-in-the-list.png)](../../includes/media/billing-check-mca/billing-mca-in-the-list.png#lightbox)

## Need help? Contact support

If you need help, [contact support](https://portal.azure.com/?#blade/Microsoft_Azure_Support/HelpAndSupportBlade) to get your issue resolved quickly.