---
layout: Conceptual
title: Pay your Microsoft Customer Agreement or Microsoft Online Subscription Program bill - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/pay-bill
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
description: Learn how to pay your bill in the Azure portal. You must be a billing profile owner, contributor, or invoice manager to pay in the portal.
keywords: billing, past due, balance, pay now,
author: KennyDay
ms.author: souchak
ms.reviewer: souchak
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.date: 2026-09-16T00:00:00.0000000Z
service.tree.id: 3b35c9b8-bf14-4e4a-bc0d-21055e56b28c
locale: en-us
document_id: 9b4e8220-2dd3-3ce2-b07e-03c793bac520
document_version_independent_id: 5c7ca9c5-205a-66b0-eabe-ccae39ad0d61
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/understand/pay-bill.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/understand/pay-bill
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/understand/pay-bill.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: d2ed3467-fe1c-2aad-9014-e47d83624187
---

# Pay your Microsoft Customer Agreement or Microsoft Online Subscription Program bill - Microsoft Cost Management | Microsoft Learn

This article applies to:

- Customers who have a Microsoft Customer Agreement.
- Customers who signed up for Azure through the Azure website to create a Microsoft Online Subscription Program account. This type of account is also called a *pay-as-you-go* account.

If you're unsure of your billing account type, see Check the type of your account later in this article.

There are two ways to pay your bill for Azure. You can pay with the default payment method of your billing profile, or you can make a one-time payment with the **Pay now** option.

If you signed up for Azure through a Microsoft representative, your default payment method is always set to wire transfer. Automatic credit card payment isn't an option if you signed up for Azure through a Microsoft representative. Instead, you can pay with a credit card for individual invoices.

If you have a Microsoft Online Subscription Program account, your default payment method is credit card. Normally, payments are automatically deducted from your credit card. But you can also make one-time payments manually by credit card.

If you have Azure credits, they automatically apply to your invoice each billing period.

Note

Regardless of the payment method that you select to complete your payment, you must specify the invoice number in the payment details.

Here's a table that summarizes payment methods for agreement types:

| Agreement type | Credit card | Wire transfer^1^ |
| --- | --- | --- |
| Microsoft Customer Agreementpurchased through a Microsoft representative | ✔ (with a $50,000 USD limit) | ✔ |
| Enterprise Agreement | ✘ | ✔ |
| Microsoft Online Subscription Program | ✔ | ✔ (if you're approved to pay by invoice) |

^1^ An ACH credit transaction can be made automatically, if your bank supports it.

## Reserve Bank of India

In October 2021, automatic payments in India were restricted under RBI’s e-mandate guidelines, which initially capped recurring transactions at ₹5,000. Customers often had to make manual payments for Microsoft Online Subscription Program (MOSP) accounts in the Azure portal. This directive did not affect the total amount charged for Azure usage.

In June 2022, the Reserve Bank of India (RBI) raised the e-mandate limit for recurring card transactions from ₹5,000 to ₹15,000. Learn more on the [Reserve Bank of India website](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&amp;Mode=0).

In September 2022, Microsoft and other online merchants no longer store credit card information. To comply with this regulation, Microsoft removed all stored card details from Azure. Learn more about this directive on the [Reserve Bank of India website](https://rbidocs.rbi.org.in/rdocs/notification/PDFs/DPSSC09B09841EF3746A0A7DC4783AC90C8F3.PDF).

**Recent Updates:** As of December 2023, RBI further increased the e-mandate limit for certain categories—mutual fund subscriptions, insurance premium payments, and credit card bill payments—from ₹15,000 to ₹1,00,000 per transaction. This change allows higher-value recurring transactions without additional authentication steps for these categories. Additionally, RBI issued the *Authentication Mechanisms for Digital Payment Transactions Directions, 2025*, introducing broader principles for secure digital payments and enabling alternative authentication methods beyond SMS-based OTP. These directions take effect by April 1, 2026. Learn more on the [Reserve Bank of India notifications page](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12898).

### UPI and NetBanking payment options

Azure supports two alternate payment methods for India customers for MOSP accounts.

- Unified Payments Interface (UPI) is a real-time payment method. UPI is also supported for MCA accounts.
- NetBanking gives customers access to banking services through an online platform.

#### How do I make a payment with UPI or NetBanking?

UPI and NetBanking are supported only for one-time payment transactions.

To make a payment with UPI or NetBanking:

1. Select **Add a new payment method** when you're making a payment.
2. Select **UPI** or **NetBanking**.
3. You're redirected to a payment partner, like BillDesk, where you can choose your payment method.
4. You're redirected to your bank's website, where you can process the payment.
5. Wait until the payment finishes in your UPI or NetBanking app, and then return to the Azure portal and select **Complete**. Don't close your browser until the payment is complete.

After you submit the payment, allow time for the payment to appear in the Azure portal.

#### How am I refunded if I made a payment with UPI or NetBanking?

Refunds are treated as a regular charge. They go to your bank account.

### Paying with Pix in Brazil

Customers who have a billing address in Brazil and an MCA billing account type can use Pix for one-time payment transactions. To make a payment with Pix:

1. Select **Add a new payment method** when you're making a payment.
2. Select **PIX**.
3. You see a QR code in the payments blade within Azure portal. Alternatively, use the payment link provided to complete the payment. The link and the QR code are valid for 24 hours.
4. When you complete payment, the payment blade automatically closes and returns you to Azure portal.

After you submit the payment, wait for the payment to appear in the Azure portal.

Note

Paying with Pix is available only for MCA billing accounts. You can check your account type here.

### Paying with Alipay in China

Customers who have a billing address in China and an MCA billing account type can use Alipay for one-time payment transactions. To make a payment with Alipay:

1. Select **Add a new payment method** when you're making a payment.
2. Select **Alipay**.
3. You're redirected to a payment partner, like Worldpay, where you can view the QR code and complete the payment with your mobile device.
4. When you complete payment, the payment page automatically closes and returns you to Azure portal.

After you submit the payment, allow time for the payment to appear in the Azure portal.

Note

Paying with Alipay is available only for MCA billing accounts. You can check your account type here.

## Partial payments

Partial payment is available for Azure global pay-as-you-go customers who experience a payment failure during the [Pay Now](/en-us/azure/cost-management-billing/understand/pay-bill#pay-now-in-the-azure-portal) flow. If you accrue usage higher than your credit card limit, you can use the following self-serve process to split the invoice amount across multiple credit cards.

There is a minimum value required for each payment that you can submit, which varies by country/region.

Note

To avoid service interruption, pay the full invoice amount by the due date on the invoice.

To make a partial payment:

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for and select **Cost Management + Billing**.
3. On the left menu, under **Billing**, select **Invoices**.
4. If any of your eligible invoices are due or past due, a blue **Pay now** link for the invoice is available. Select the link.
5. In the **Pay now** window, select **Select a payment method** to choose an existing credit card or add a new one.
6. Select **Pay now**.
7. If the payment fails, the partial payment feature appears in the **Pay now** experience. There's a minimum partial payment amount. You must enter an amount greater than the minimum.
8. Select the **Select a payment method** option to choose an existing credit card or add a new one. It's the card that the first partial payment is applied to.
9. Select **Pay now**.
10. Repeat steps 8 to 9 until you fully pay the invoice amount.

## Credit or debit card

If the default payment method for your billing profile is a credit or debit card, it's automatically charged each billing period.

If your automatic credit or debit card charge is declined for any reason, you can make a one-time payment with a credit or debit card in the Azure portal by using **Pay now**.

If you have a Microsoft Online Subscription Program (pay-as-you-go) account and you have a bill due, the **Pay now** banner appears on your subscription property page.

If you want to learn how to change your default payment method to wire transfer, see the [article about how to pay by invoice](../manage/pay-by-invoice).

Although you can generally use debit cards to pay your Azure bill, consider these limitations:

- Hong Kong Special Administrative Region and Brazil don't allow the use of debit cards. They support only credit cards.
- India supports debit and credit cards through Visa and Mastercard.
- You can't use virtual cards to pay your Azure bill.
- Prepaid cards (also known as stored value cards, Visa gift cards, MasterCard gift cards, etc.) are not accepted as valid payment instruments.

## Wire transfer

If the default payment method of your billing profile is wire transfer, follow the payment instructions on your invoice PDF file.

Note

When you pay your bill by wire transfer, the payment might take up to 10 business days to get processed.

Alternatively, if your invoice is under the threshold amount for your currency, you can make a one-time payment in the Azure portal with a credit or debit card by using **Pay now**. If your invoice amount exceeds the threshold, you can't pay your invoice with a credit or debit card. You'll find the threshold amount for your currency in the Azure portal after you select **Pay now**.

Note

When multiple invoices are remitted in a single wire transfer, you must specify the invoice numbers for all of the invoices.

Important

SEPA (Single Euro Payments Area) transfers allow up to 140 characters in the payment details field. Exceeding this limit might cause processing issues.

### Bank details used to send wire transfer payments

If your default payment method is wire transfer, check your invoice for payment instructions. These bank details apply to all MCA wire transfer payments. Find payment instructions for your country/region in the following list:

- **Choose your country or region**
- [Afghanistan](/en-us/legal/pay/payment-details#afghanistan)
- [Albania](/en-us/legal/pay/payment-details#albania)
- [Algeria](/en-us/legal/pay/payment-details#algeria)
- [Angola](/en-us/legal/pay/payment-details#angola)
- [Argentina](/en-us/legal/pay/payment-details#argentina)
- [Armenia](/en-us/legal/pay/payment-details#armenia)
- [Australia](/en-us/legal/pay/payment-details#australia)
- [Austria](/en-us/legal/pay/payment-details#austria)
- [Azerbaijan](/en-us/legal/pay/payment-details#azerbaijan)
- [Bahamas](/en-us/legal/pay/payment-details#bahamas)
- [Bahrain](/en-us/legal/pay/payment-details#bahrain)
- [Bangladesh](/en-us/legal/pay/payment-details#bangladesh)
- [Barbados](/en-us/legal/pay/payment-details#barbados)
- [Belarus](/en-us/legal/pay/payment-details#belarus)
- [Belgium](/en-us/legal/pay/payment-details#belgium)
- [Belize](/en-us/legal/pay/payment-details#belize)
- [Bermuda](/en-us/legal/pay/payment-details#bermuda)
- [Bolivia](/en-us/legal/pay/payment-details#bolivia)
- [Bosnia and Herzegovina](/en-us/legal/pay/payment-details#bosnia-and-herzegovina)
- [Botswana](/en-us/legal/pay/payment-details#botswana)
- [Brazil](/en-us/legal/pay/payment-details#brazil)
- [Brunei](/en-us/legal/pay/payment-details#brunei)
- [Bulgaria](/en-us/legal/pay/payment-details#bulgaria)
- [Cameroon](/en-us/legal/pay/payment-details#cameroon)
- [Canada](/en-us/legal/pay/payment-details#canada)
- [Cabo Verde](/en-us/legal/pay/payment-details#cape-verde)
- [Cayman Islands](/en-us/legal/pay/payment-details#cayman-islands)
- [Chile](/en-us/legal/pay/payment-details#chile)
- [China (PRC)](/en-us/legal/pay/payment-details#china-prc)
- [Colombia](/en-us/legal/pay/payment-details#colombia)
- [Costa Rica](/en-us/legal/pay/payment-details#costa-rica)
- [Côte d'Ivoire](/en-us/legal/pay/payment-details#cote-divoire)
- [Croatia](/en-us/legal/pay/payment-details#croatia)
- [Curacao](/en-us/legal/pay/payment-details#curacao)
- [Cyprus](/en-us/legal/pay/payment-details#cyprus)
- [Czech Republic](/en-us/legal/pay/payment-details#czech-republic)
- [Democratic Republic of Congo](/en-us/legal/pay/payment-details#democratic-republic-of-congo)
- [Denmark](/en-us/legal/pay/payment-details#denmark)
- [Dominican Republic](/en-us/legal/pay/payment-details#dominican-republic)
- [Ecuador](/en-us/legal/pay/payment-details#ecuador)
- [Egypt](/en-us/legal/pay/payment-details#egypt)
- [El Salvador](/en-us/legal/pay/payment-details#el-salvador)
- [Estonia](/en-us/legal/pay/payment-details#estonia)
- [Ethiopia](/en-us/legal/pay/payment-details#ethiopia)
- [Faroe Islands](/en-us/legal/pay/payment-details#faroe-islands)
- [Fiji](/en-us/legal/pay/payment-details#fiji)
- [Finland](/en-us/legal/pay/payment-details#finland)
- [France](/en-us/legal/pay/payment-details#france)
- [French Guiana](/en-us/legal/pay/payment-details#french-guiana)
- [Georgia](/en-us/legal/pay/payment-details#georgia)
- [Germany](/en-us/legal/pay/payment-details#germany)
- [Ghana](/en-us/legal/pay/payment-details#ghana)
- [Greece](/en-us/legal/pay/payment-details#greece)
- [Grenada](/en-us/legal/pay/payment-details#grenada)
- [Guadeloupe](/en-us/legal/pay/payment-details#guadeloupe)
- [Guam](/en-us/legal/pay/payment-details#guam)
- [Guatemala](/en-us/legal/pay/payment-details#guatemala)
- [Guyana](/en-us/legal/pay/payment-details#guyana)
- [Haiti](/en-us/legal/pay/payment-details#haiti)
- [Honduras](/en-us/legal/pay/payment-details#honduras)
- [Hong Kong SAR](/en-us/legal/pay/payment-details#hong-kong)
- [Hungary](/en-us/legal/pay/payment-details#hungary)
- [Iceland](/en-us/legal/pay/payment-details#iceland)
- [India](/en-us/legal/pay/payment-details#india)
- [Indonesia](/en-us/legal/pay/payment-details#indonesia)
- [Iraq](/en-us/legal/pay/payment-details#iraq)
- [Ireland](/en-us/legal/pay/payment-details#ireland)
- [Israel](/en-us/legal/pay/payment-details#israel)
- [Italy](/en-us/legal/pay/payment-details#italy)
- [Jamaica](/en-us/legal/pay/payment-details#jamaica)
- [Japan](/en-us/legal/pay/payment-details#japan)
- [Jordan](/en-us/legal/pay/payment-details#jordan)
- [Kazakhstan](/en-us/legal/pay/payment-details#kazakhstan)
- [Kenya](/en-us/legal/pay/payment-details#kenya)
- [Korea](/en-us/legal/pay/payment-details#korea)
- [Kuwait](/en-us/legal/pay/payment-details#kuwait)
- [Kyrgyzstan](/en-us/legal/pay/payment-details#kyrgyzstan)
- [Latvia](/en-us/legal/pay/payment-details#latvia)
- [Lebanon](/en-us/legal/pay/payment-details#lebanon)
- [Libya](/en-us/legal/pay/payment-details#libya)
- [Liechtenstein](/en-us/legal/pay/payment-details#liechtenstein)
- [Lithuania](/en-us/legal/pay/payment-details#lithuania)
- [Luxembourg](/en-us/legal/pay/payment-details#luxembourg)
- [Macao Special Administrative Region](/en-us/legal/pay/payment-details#macao)
- [Malaysia](/en-us/legal/pay/payment-details#malaysia)
- [Malta](/en-us/legal/pay/payment-details#malta)
- [Mauritius](/en-us/legal/pay/payment-details#mauritius)
- [Mexico](/en-us/legal/pay/payment-details#mexico)
- [Moldova](/en-us/legal/pay/payment-details#moldova)
- [Monaco](/en-us/legal/pay/payment-details#monaco)
- [Mongolia](/en-us/legal/pay/payment-details#mongolia)
- [Montenegro](/en-us/legal/pay/payment-details#montenegro)
- [Morocco](/en-us/legal/pay/payment-details#morocco)
- [Namibia](/en-us/legal/pay/payment-details#namibia)
- [Nepal](/en-us/legal/pay/payment-details#nepal)
- [Netherlands](/en-us/legal/pay/payment-details#netherlands)
- [New Zealand](/en-us/legal/pay/payment-details#new-zealand)
- [Nicaragua](/en-us/legal/pay/payment-details#nicaragua)
- [Nigeria](/en-us/legal/pay/payment-details#nigeria)
- [North Macedonia, Republic of](/en-us/legal/pay/payment-details#macedonia)
- [Norway](/en-us/legal/pay/payment-details#norway)
- [Oman](/en-us/legal/pay/payment-details#oman)
- [Pakistan](/en-us/legal/pay/payment-details#pakistan)
- [Palestinian Authority](/en-us/legal/pay/payment-details#palestinian-authority)
- [Panama](/en-us/legal/pay/payment-details#panama)
- [Paraguay](/en-us/legal/pay/payment-details#paraguay)
- [Peru](/en-us/legal/pay/payment-details#peru)
- [Philippines](/en-us/legal/pay/payment-details#philippines)
- [Poland](/en-us/legal/pay/payment-details#poland)
- [Portugal](/en-us/legal/pay/payment-details#portugal)
- [Puerto Rico](/en-us/legal/pay/payment-details#puerto-rico)
- [Qatar](/en-us/legal/pay/payment-details#qatar)
- [Romania](/en-us/legal/pay/payment-details#romania)
- [Russia](/en-us/legal/pay/payment-details#russia)
- [Rwanda](/en-us/legal/pay/payment-details#rwanda)
- [Saint Kitts and Nevis](/en-us/legal/pay/payment-details#saint-kitts-and-nevis)
- [Saint Lucia](/en-us/legal/pay/payment-details#saint-lucia)
- [Saint Vincent and the Grenadines](/en-us/legal/pay/payment-details#saint-vincent-and-the-grenadines)
- [Saudi Arabia](/en-us/legal/pay/payment-details#saudi-arabia)
- [Senegal](/en-us/legal/pay/payment-details#senegal)
- [Serbia](/en-us/legal/pay/payment-details#serbia)
- [Singapore](/en-us/legal/pay/payment-details#singapore)
- [Slovakia](/en-us/legal/pay/payment-details#slovakia)
- [Slovenia](/en-us/legal/pay/payment-details#slovenia)
- [South Africa](/en-us/legal/pay/payment-details#south-africa)
- [Spain](/en-us/legal/pay/payment-details#spain)
- [Sri Lanka](/en-us/legal/pay/payment-details#sri-lanka)
- [Suriname](/en-us/legal/pay/payment-details#suriname)
- [Sweden](/en-us/legal/pay/payment-details#sweden)
- [Switzerland](/en-us/legal/pay/payment-details#switzerland)
- [Taiwan](/en-us/legal/pay/payment-details#taiwan)
- [Tajikistan](/en-us/legal/pay/payment-details#tajikistan)
- [Tanzania](/en-us/legal/pay/payment-details#tanzania)
- [Thailand](/en-us/legal/pay/payment-details#thailand)
- [Trinidad and Tobago](/en-us/legal/pay/payment-details#trinidad-and-tobago)
- [Turkmenistan](/en-us/legal/pay/payment-details#turkmenistan)
- [Tunisia](/en-us/legal/pay/payment-details#tunisia)
- [Türkiye](/en-us/legal/pay/payment-details#turkey)
- [Uganda](/en-us/legal/pay/payment-details#uganda)
- [Ukraine](/en-us/legal/pay/payment-details#ukraine)
- [United Arab Emirates](/en-us/legal/pay/payment-details#united-arab-emirates)
- [United Kingdom](/en-us/legal/pay/payment-details#united-kingdom)
- [United States](/en-us/legal/pay/payment-details#united-states)
- [Uruguay](/en-us/legal/pay/payment-details#uruguay)
- [Uzbekistan](/en-us/legal/pay/payment-details#uzbekistan)
- [Venezuela](/en-us/legal/pay/payment-details#venezuela)
- [Vietnam](/en-us/legal/pay/payment-details#vietnam)
- [Virgin Islands, US](/en-us/legal/pay/payment-details#virgin-islands)
- [Yemen](/en-us/legal/pay/payment-details#yemen)
- [Zambia](/en-us/legal/pay/payment-details#zambia)
- [Zimbabwe](/en-us/legal/pay/payment-details#zimbabwe)

## Pay now in the Azure portal

To pay invoices in the Azure portal, you must have the correct [Microsoft Customer Agreement permissions](../manage/understand-mca-roles) or be the account administrator. The account administrator is the user who originally signed up for the Microsoft Customer Agreement account.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for and select **Cost Management + Billing**.
3. On the left menu, under **Billing**, select **Invoices**.
4. If any of your eligible invoices are due or past due, a blue **Pay now** link appears for the invoice. Select the link.
5. In the **Pay now** window, select **Select a payment method** to choose an existing credit card or add a new one.
6. Select **Pay now**.

The invoice status shows **paid** within 24 hours.

The **Pay now** option might be unavailable if:

- You have a Microsoft Online Subscription Program account (pay-as-you-go account). You might instead see a **Settle balance** banner. If so, see [Resolve a past-due balance](../manage/resolve-past-due-balance#resolve-a-past-due-balance-in-the-azure-portal).
- Your default payment method and invoice amount don't support the **Pay now** option. Check your invoice for payment instructions.

For a complete list of all the counties/regions where the **Pay now** option is available, see [Regional considerations](../manage/resolve-past-due-balance#regional-considerations).

## Check the type of your account

To determine whether you have access to a billing account for a Microsoft Customer Agreement, check the agreement type:

1. Go to the Azure portal. Search for and select **Cost Management + Billing**.

    [![Screenshot that shows a search for Cost Management + Billing.](../../includes/media/billing-check-mca/billing-search-cost-management-billing.png)](../../includes/media/billing-check-mca/billing-search-cost-management-billing.png#lightbox)
2. If you have access to just one billing scope, select **Settings** &gt; **Properties**. You have access to a billing account for a Microsoft Customer Agreement if the billing account type is **Microsoft Customer Agreement**.

    [![Screenshot of the Azure portal that shows a billing account type of Microsoft Customer Agreement for a single billing scope.](../../includes/media/billing-check-mca/billing-mca-property.png)](../../includes/media/billing-check-mca/billing-mca-property.png#lightbox)

    If you have access to multiple billing scopes, check the type in the **Billing account type** column. You have access to a billing account for a Microsoft Customer Agreement if the billing account type for any of the scopes is **Microsoft Customer Agreement**.

    [![Screenshot of the Azure portal that shows a billing account type of Microsoft Customer Agreement for multiple billing scopes.](../../includes/media/billing-check-mca/billing-mca-in-the-list.png)](../../includes/media/billing-check-mca/billing-mca-in-the-list.png#lightbox)