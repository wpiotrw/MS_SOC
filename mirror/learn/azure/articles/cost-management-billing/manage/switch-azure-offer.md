---
layout: Conceptual
title: Change Azure subscription offer - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/switch-azure-offer
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
description: Learn about how to change your Azure subscription and switch to a different offer.
author: diberry
ms.author: diberry
ms.reviewer: mjeffer
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.date: 2026-06-15T00:00:00.0000000Z
ms.custom: sfi-image-nochange
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: cecfbb3c-3fed-785d-7954-282046cd9089
document_version_independent_id: cfb7d8f0-e710-3ea1-e2c3-c3e0c1a18b75
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/switch-azure-offer.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/switch-azure-offer
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/switch-azure-offer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/4628cbd9-6f47-4ae1-b371-d34636609eaf
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/be21deb8-8c64-44b0-b71f-2dc56ca7364f
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 734888a7-8940-75d1-a465-71401247a55e
---

# Change Azure subscription offer - Microsoft Cost Management | Microsoft Learn

As a customer with a [pay-as-you-go subscription](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn), you can switch your Azure subscription to another offer in the Azure portal. For example, you can use this feature to take advantage of the [monthly credits for Visual Studio subscribers](https://azure.microsoft.com/pricing/member-offers/msdn-benefits-details/).

If you have an expired Visual Studio subscription, you can switch to a [pay-as-you-go subscription](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn) .

**Just want to upgrade from Free Trial?** See [upgrade your subscription](upgrade-azure-subscription).

## What's supported

You can switch from a pay-as-you-go subscription to:

- [Pay-As-You-Go Dev/Test](https://azure.microsoft.com/offers/ms-azr-0023p/)
- [Visual Studio Professional](https://azure.microsoft.com/offers/ms-azr-0059p/)
- [Visual Studio Test Professional](https://azure.microsoft.com/offers/ms-azr-0060p/)
- [MSDN Platforms](https://azure.microsoft.com/offers/ms-azr-0062p/)
- [Visual Studio Enterprise](https://azure.microsoft.com/offers/ms-azr-0063p/)

You can also switch from an expired [Visual Studio Enterprise subscription](https://azure.microsoft.com/offers/ms-azr-0063p/) to a [pay-as-you-go subscription](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn).

Note

For other offer changes, [contact support](https://portal.azure.com/?#blade/Microsoft_Azure_Support/HelpAndSupportBlade).

## Switch from a pay-as-you-go subscription

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Navigate to **Subscriptions** and then select your pay-as-you-go subscription.
3. At the top of the page, select **Switch Offer**. The option is only available if you have a pay-as-you-go subscription and have completed your first billing period.[![Screenshot showing subscription details with the Switch Offer option.](media/switch-azure-offer/switch-offer.png)](media/switch-azure-offer/switch-offer.png#lightbox)
4. Select the offer that you want from the list of offers your subscription can be switched to. This list varies based on the memberships that your account is associated with. If nothing is available, check the list of available offers you can switch to and make sure you have the right memberships. Then select **Next**. [![Screenshot showing where to select an offer that you want to switch to.](media/switch-azure-offer/select-offer.png)](media/switch-azure-offer/select-offer.png#lightbox) Depending on the offer you’re switching to, you may see a note about the consequence of switching. Go through the list carefully and follow the instructions before you continue. You might also need to verify your phone number.
5. After reviewing any notes or verifying your phone number, select **Switch Offer**.
6. Your subscription is now switched to the new offer.

## Convert a Visual Studio Enterprise subscription

When your Visual Studio Enterprise subscription expires, it gets disabled. To continue using Azure services with the subscription, you must convert it to a pay-as-you-subscription.

Note

- When you upgrade to a pay-as-you-go subscription, you stop receiving monthly credits and your payment method starts getting charged on a monthly basis based on your monthly usage.
- When you switch to pay-as-you-go subscription, you lose your usage and billing information. We recommend that you [save any past invoices and usage data](download-azure-invoice-daily-usage-date) before switching the offer.

To convert your subscription:

1. Navigate to **Subscriptions** and then select your Visual Studio Enterprise subscription.
2. You'll see a banner at the top of the page stating `Your Visual Studio subscription is expired and has been disabled. To continue using this subscription, please click here to convert to a pay-as-you-go subscription`. Select the banner.[![Screenshot showing an expired subscription with the banner to convert it.](media/switch-azure-offer/visual-studio-expired-banner.png)](media/switch-azure-offer/visual-studio-expired-banner.png#lightbox)
3. On the Switch Offer page, Select an offer tab, select the pay-as-you-go option, and then select **Next**.[![Screenshot showing the Switch Offer option.](media/switch-azure-offer/select-offer-pay-as-you-go.png)](media/switch-azure-offer/select-offer-pay-as-you-go.png#lightbox)
4. On the Select payment method tab, select **Select a payment method**, enter your payment method information, and then select **Next**.
5. On the Review + convert page, you can optionally change the subscription name. Review the agreement information, select the **I agree** option, and then at the bottom of the page, select **Switch Offer**.[![Screenshot showing the Review + convert tab with subscription name and agreement acceptance.](media/switch-azure-offer/switch-offer-visual-studio-agreement.png)](media/switch-azure-offer/switch-offer-visual-studio-agreement.png#lightbox)

View your new converted subscription by navigating to **Subscriptions**.

## Frequently asked questions for pay-as-you-go subscriptions

The following sections answer commonly asked questions about switching from a pay-as-you-go subscription.

### What is an Azure offer?

An Azure offer is the *type* of the Azure subscription you have. For example, [a subscription with pay-as-you-go rates](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn), [Azure in Open](https://azure.microsoft.com/offers/ms-azr-0111p/), and [Visual Studio Enterprise](https://azure.microsoft.com/offers/ms-azr-0063p/) are all Azure offers. Each offer has different [terms](https://azure.microsoft.com/support/legal/offer-details/) and some have special benefits. The offer of your subscription is shown on the subscription details page.

[![Screenshot showing the subscription details page with the offer type.](media/switch-azure-offer/subscription-details.png)](media/switch-azure-offer/subscription-details.png#lightbox)

### Why don't I see the Switch Offer option?

You might not see the **Switch Offer** option if:

- You don't have a [subscription with pay-as-you-go rates](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn). Currently only subscriptions with pay-as-you-go rates can be converted to another offer.
    - If you have a [Free Trial](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn), learn how to [upgrade to Pay-As-You-Go](upgrade-azure-subscription).
    - To switch offer from a different subscription, [contact support](https://portal.azure.com/?#blade/Microsoft_Azure_Support/HelpAndSupportBlade).
- You're still in your first billing period; you must wait for your first billing period to end before you can switch offers.

### Why do I see "There are no offers available in your country/region at this time"?

- You might not be eligible for any offer switches. Check the list of available offers you can switch to and make sure that you've activated the right benefits with Visual Studio.
- Some offers may not be available in all countries/regions.

### What does switching Azure offers do to my service and billing?

Here are the details of what happens when you switch Azure offers.

#### No service downtime

There's no service downtime for any users associated with the subscription. However, the offer you switch to may have restrictions. For instance, some offers prohibit production use, so you would need to move production resources to another subscription.

#### Quota increases are reset

When you switch offers, any [limit or quota increases above the default limit](/en-us/azure/azure-portal/supportability/regional-quota-requests) are reset. There's no service downtime, even if you have more resources beyond the default limit. For example, you're using 200 cores on your subscription, then switching offers resets your cores quota back to the default of 20 cores. The VMs that use the 200 cores are unaffected and would continue to run. If you don't make another quota increase request, however, you can't provision any more cores.

#### Billing

On the day you switch, an invoice is generated for all outstanding charges. Then, your subscription is billed per the new offer’s pricing terms. Your subscription billing anniversary changes to the date on which you changed offers. Usage and billing data before the offer change isn't kept, so we recommend that you download a copy before switching.

### Can I migrate from a subscription with pay-as-you-go rates to Cloud Solution Provider (CSP) or Enterprise Agreement (EA)?

- To migrate to CSP, see [Transfer Azure subscriptions between subscribers and CSPs](transfer-subscriptions-subscribers-csp).
- If you have a pay-as-you-go subscription (Azure offer ID MS-AZR-0003P) or an Azure plan with pay-as-you-go rates (Azure offer ID MS-AZR-0017G) and you want to migrate to an EA enrollment, have your Enrollment Admin add your account into the EA. Follow instructions in the invitation email to have your subscriptions moved under the EA enrollment. For more information, see [Change Azure subscription or account ownership](direct-ea-administration#change-azure-subscription-or-account-ownership).

### Can I migrate data and services to a new subscription?

- You can migrate the resources directly to the new subscription, see [Move resources to new resource group or subscription](../../azure-resource-manager/management/move-resource-group-and-subscription).
- To transfer ownership of an Azure subscription and everything in it to someone else, see [Transferring ownership of an Azure subscription](billing-subscription-transfer)

## Need help? Contact us.

If you have questions or need help, [create a support request](https://go.microsoft.com/fwlink/?linkid=2083458).