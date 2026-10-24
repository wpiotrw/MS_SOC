---
layout: Conceptual
title: Azure product transfer hub - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/subscription-transfer
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
description: This article helps you understand the Azure subscription, reservation, and savings plan transfer requirements and support. This article also provides links to other articles for more detailed information.
author: Nicholak-MS
ms.author: clodwig
ms.reviewer: clodwig
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: concept-article
ms.date: 2026-10-16T00:00:00.0000000Z
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: 55151e88-c7c5-47e4-573c-04441dc23577
document_version_independent_id: f0253fd2-838c-23c5-bb1f-f702ca04923d
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/subscription-transfer.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/subscription-transfer
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/subscription-transfer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 8ac0e875-5041-83e1-2476-390e8fcd904a
---

# Azure product transfer hub - Microsoft Cost Management | Microsoft Learn

This article describes the types of supported transfers for Azure subscriptions, reservations, and savings plans referred to as *products*. This article also helps you understand the requirements to transfer Azure products across different billing agreements and it provides links to other articles for in-depth information on specific transfer processes. Azure products are created using different Azure agreement types and a transfer from a source agreement type to another varies depending on the source and destination agreement types. Azure product transfers can be an automatic or a manual process, depending on the source and destination agreement type. If it's a manual process, the agreement types determine how much manual effort is needed.

Note

There are many types of Azure products, however not every product can be transferred from one type to another. Only supported product transfers are documented in this article. If you need help with a situation that isn't addressed in this article, you can create an [Azure support request](https://go.microsoft.com/fwlink/?linkid=2083458) for assistance.

This article also helps you understand the things you should know *before* you transfer billing ownership of an Azure product to another account. You might want to transfer billing ownership of your Azure product if you're leaving your organization, or you want your product to be billed to another account. Transferring billing ownership to another account provides the administrators in the new account permission for billing tasks. They can change the payment method, view charges, and cancel the product.

Note

You can't transfer subscriptions to a Microsoft Entra B2B or Azure B2C tenant.

If you want to keep the billing ownership but change the type of product, see [Switch your Azure subscription to another offer](switch-azure-offer). To control who can access resources in the product, see [Azure built-in roles](../../role-based-access-control/built-in-roles).

If you're an Enterprise Agreement (EA) customer, your enterprise administrators can transfer billing ownership of your products between accounts in the Azure portal. For more information, see [Change Azure subscription or account ownership](direct-ea-administration#change-azure-subscription-or-account-ownership).

This article focuses on product transfers. However, resource transfer is also discussed because it's necessary for some product transfer scenarios.

For more information about product transfers between different Microsoft Entra tenants, see [Transfer an Azure subscription to a different Microsoft Entra directory](../../role-based-access-control/transfer-subscription).

Note

Most billing ownership transfers don't change the service tenant of the underlying products. They don't cause any downtime. However, even when a billing tenant does change, the change doesn't affect running services or resources.

## Product transfer planning

As you begin to plan your product transfer, consider the information needed to answer the following questions:

- Why is the product transfer required?
- What's the wanted timeline for the product transfer?
- What's the product's current offer type and what do you want to transfer it to?
    - Microsoft Online Services Program (MOSP), also known as pay-as-you-go
    - Previous Azure offer in CSP
    - Enterprise Agreement (EA)
    - Microsoft Customer Agreement in the Enterprise motion (MCA-E) where you buy Azure services through a Microsoft representative. Also called an MCA enterprise agreement.
    - Microsoft Customer Agreement that you bought through the Azure website (MCA-online).
    - Cloud Solution Provider (CSP) - MCA managed by partner
    - Others like Visual Studio, EOPEN, Azure Pass, and Free Trial
- Do you have the required permissions on the product to accomplish a transfer? Specific permission needed for each transfer type is listed in the following product transfer support table.
    - Only the billing administrator of an account can transfer subscription ownership.
    - Only a billing administrator owner can transfer reservation or savings plan ownership.
- Are there existing subscriptions that benefit from reservations or savings plans, and do they need to be transferred with the subscription?

You should have an answer for each question before you continue with any transfer.

Answers to the above questions can help you to communicate early with others to set expectations and timelines. Product transfer effort varies greatly, but a transfer is likely to take longer than expected.

Note

Azure Marketplace products may transfer differently than the Azure subscription. In particular, software as a service (SaaS) subscriptions are billed through an Azure subscription but don't move with it. You must transfer SaaS subscriptions separately. For SaaS and Marketplace transfer behavior, see [Transfer Azure product billing ownership to your Microsoft Partner Agreement (MPA)](mpa-request-ownership#software-as-a-service-saas-transfer) and [Transfer Azure product billing ownership to a Microsoft Customer Agreement](mca-request-billing-ownership#marketplace-purchases).

Understanding the answers to source and destination offer type questions is crucial to determine the technical steps required and to recognize any potential restrictions in the transfer process. Limitations are covered in more detail in the next section.

If you're not sure what type of subscription you have, see [Check the type of your account](view-all-accounts#check-the-type-of-your-account).

## Parent subscription cancellation and transfer limitations

If your subscription contains an active Microsoft Azure Consumption Commitment (MACC) agreement, you can't cancel or transfer the subscription because of the contractual obligation to fulfill the terms of the MACC commitment. The parent subscription must remain active as long as it contains an active MACC. Once the MACC expires, the subscription is able to be canceled or transferred.

## Support plan transfers

You can't transfer support plans. If you have a support plan, then you should cancel it. Then you can buy a new one for the new agreement. If you cancel an Azure support plan, you get billed for the rest of the month. Cancelling a support plan doesn't result in a prorated refund. For more information about support plans, see [Azure support plans](https://azure.microsoft.com/support/plans/).

For information about how to cancel a support plan, see [Cancel your Azure subscription](cancel-azure-subscription).

## Product transfer support

The following table describes product transfer support between the different agreement types. Links are provided for more information about each type of transfer.

Currently transfer isn't supported for [Free Trial](https://azure.microsoft.com/pricing/offers/ms-azr-0044p?cid=msft_learn) products. For a workaround, see [Move resources to new resource group or subscription](../../azure-resource-manager/management/move-resource-group-and-subscription).

Dev/Test products aren't shown in the following table. Transfers for Dev/Test products are handled in the same way as other product types. For example, an EA Dev/Test product transfer is handled in the way an EA product transfer.

Note

Reservations and savings plans transfer with most supported product transfers. However, there are some transfers where reservations or savings plans won't transfer, as noted in the following table. For transfer with currency change, refer to the Transfer Reservations and Savings Plans with currency change section below.

| Source (current) product agreement type | Destination (future) product agreement type | Notes |
| --- | --- | --- |
| EA | MOSP (pay-as-you-go) | • Transfer from an EA enrollment to a MOSP subscription requires a [billing support ticket](https://azure.microsoft.com/support/create-ticket/). • Reservations and savings plans don't automatically transfer and transferring them isn't supported. |
| EA | MCA-online | • For details, see [Transfer Azure subscription billing ownership for a Microsoft Customer Agreement](mca-request-billing-ownership). • Self-service reservation and savings plan transfers with no currency change are supported.  • If your enrollment transfer (e.g. EA to MCA, EA to EA, etc.) involves a change in pricing currency (e.g. EUR to USD), refer to the Transfer Reservations and Savings Plans with currency change section below. |
| EA | EA | • Transferring between EA enrollments requires a [billing support ticket](https://azure.microsoft.com/support/create-ticket/). • Reservations and savings plans automatically get transferred during EA to EA transfers, except in transfers with a currency change. • Transfer within the same enrollment is the same action as changing the account owner. For details, see [Change Azure subscription or account ownership](direct-ea-administration#change-azure-subscription-or-account-ownership). |
| EA | MCA-E | • Transferring all enrollment products is completed as part of the MCA transition process from an EA. For more information, see [Complete Enterprise Agreement tasks in your billing account for a Microsoft Customer Agreement](mca-enterprise-operations).• For details about how to transfer an EA enrollment to a Microsoft Customer Agreement (enterprise), see [Set up your billing account for a Microsoft Customer Agreement](mca-setup-account).  • If you want to transfer specific products but not all of the products in an enrollment, see [Transfer Azure subscription billing ownership for a Microsoft Customer Agreement](mca-request-billing-ownership). • Self-service reservation and savings plan transfers with no currency change are supported.  • If your enrollment transfer (e.g. EA to MCA, EA to EA, etc.) involves a change in pricing currency (e.g. EUR to USD), refer to the Transfer Reservations and Savings Plans with currency change section below. |
| EA | CSP (MCA managed by partner) | • If your enrollment transfer (e.g. EA to MCA, EA to EA, etc.) involves a change in pricing currency (e.g. EUR to USD), refer to the Transfer Reservations and Savings Plans with currency change section below.  • Transfers are supported for CSP authorized Direct Bill partners with an Azure Solutions Partner designation or Azure Expert MSP status, and CSP authorized distributors with a Frontier Distributor designation can request to transfer Azure products for their customers that have an Enterprise Agreement (EA). For more information, see [Get billing ownership of Azure subscriptions to your MPA account](mpa-request-ownership). Product transfers are allowed only for customers that accepted a Microsoft Customer Agreement (MCA) and purchased an Azure plan with the CSP Program. • There are limitations and restrictions. For more information, see [Transfer EA subscriptions to a CSP partner](transfer-subscriptions-subscribers-csp). |
| MCA-online | MOSP (pay-as-you-go) | • Microsoft doesn't support the transfer, so you must move resources yourself. For more information, see [Move resources to a new resource group or subscription](../../azure-resource-manager/management/move-resource-group-and-subscription). • Reservations and savings plans don't automatically transfer and transferring them isn't supported. |
| MCA-online | MCA-online | • For details, see [Transfer Azure subscription billing ownership for a Microsoft Customer Agreement](mca-request-billing-ownership). • Self-service reservation and savings plan transfers are supported. |
| MCA-online (Individual billing account) | EA | • Supported. When the identity that originated the Individual billing account is added as an EA account owner and activates the account, all subscriptions on any account that has that user's identity as its backing entity (as opposed to a business) move to the EA.**Note:** The conversion is all or nothing and can't be reversed. For details, see [Transfer MCA-Online subscriptions to an Enterprise Agreement](mca-online-ea-transfer). • Reservations and savings plans don't necessarily transfer automatically. Because the whole account moves, you can't leave products behind. Review the product behaviors in Transfer Reservations and Savings Plans with currency change. |
| MCA-online (any other account type) | EA | • Microsoft doesn't support the transfer, so you must move resources yourself. For more information, see [Move resources to a new resource group or subscription](../../azure-resource-manager/management/move-resource-group-and-subscription). • Reservations and savings plans don't automatically transfer and transferring them isn't supported. |
| MCA-online | MCA-E | • For details, see [Transfer Azure subscription billing ownership for a Microsoft Customer Agreement](mca-request-billing-ownership).• Self-service reservation and savings plan transfers are supported. |
| MCA-online | CSP (MCA managed by partner) | • Microsoft doesn't support the transfer, so you must move resources yourself. For more information, see [Move resources to a new resource group or subscription](../../azure-resource-manager/management/move-resource-group-and-subscription). • Reservations and savings plans don't automatically transfer and transferring them isn't supported. |
| MCA-E | EA | • Microsoft doesn't support the transfer, so you must move resources yourself. For more information, see [Move resources to a new resource group or subscription](../../azure-resource-manager/management/move-resource-group-and-subscription). • Reservations and savings plans don't automatically transfer and transferring them isn't supported. |
| MCA-E | MOSP | • Microsoft doesn't support the transfer, so you must move resources yourself. For more information, see [Move resources to a new resource group or subscription](../../azure-resource-manager/management/move-resource-group-and-subscription). • Reservations and savings plans don't automatically transfer and transferring them isn't supported. |
| MCA-E | MCA-online | • For details, see [Transfer Azure subscription billing ownership for a Microsoft Customer Agreement](mca-request-billing-ownership). • Self-service reservation and savings plan transfers are supported. |
| MCA-E | MCA-E | • For details, see [Transfer Azure subscription billing ownership for a Microsoft Customer Agreement](mca-request-billing-ownership). • Self-service reservation and savings plan transfers are supported. |
| MCA-E | CSP (MCA managed by partner) | • Transfers are supported for CSP authorized Direct Bill partners with an Azure Solutions Partner designation or Azure Expert MSP status, and CSP authorized distributors with a Frontier Distributor designation can request to transfer Azure products for their customers that have an Enterprise Microsoft Customer Agreement with a Microsoft representative. For more information, see [Get billing ownership of Azure subscriptions to your MPA account](mpa-request-ownership). Product transfers are allowed only for customers that accepted a Microsoft Customer Agreement (MCA) and purchased an Azure plan with the CSP Program. • Self-service reservation and savings plan transfers are supported. • There are limitations and restrictions. For more information, see [Transfer EA subscriptions to a CSP partner](transfer-subscriptions-subscribers-csp#transfer-direct-enterprise-agreement-%28ea%29-or-enterprise-microsoft-customer-agreement-%28mca-e%29-subscriptions-to-a-csp-partner). |
| Previous Azure offer in CSP | Previous Azure offer in CSP | • Requires a [billing support ticket](https://azure.microsoft.com/support/create-ticket/). • Reservations don't automatically transfer and transferring them isn't supported. |
| Previous Azure offer in CSP | CSP (MCA managed by partner) | • For details, see [Transfer a customer's Azure subscriptions to a different CSP (under an Azure plan)](/en-us/partner-center/transfer-azure-subscriptions-under-azure-plan). |
| CSP (MCA managed by partner) | EA | • Automatic transfer isn't supported. Any transfer requires resources to move from the existing CSP (MCA managed by partner) product manually to a newly created or an existing EA product. • Use the information in the Perform resource transfers section.  • Reservations and savings plans don't automatically transfer and transferring them isn't supported. |
| CSP (MCA managed by partner) | MCA-online | • Microsoft doesn't support the transfer, so you must move resources yourself. For more information, see [Move resources to a new resource group or subscription](../../azure-resource-manager/management/move-resource-group-and-subscription). • Reservations and savings plans don't automatically transfer and transferring them isn't supported. |
| CSP (MCA managed by partner) | CSP (MCA managed by partner) | • For details, see [Transfer a customer's Azure subscriptions and/or Reservations (under an Azure plan) to a different CSP](/en-us/partner-center/transfer-azure-subscriptions-under-azure-plan). |
| MOSP (pay-as-you-go) | MOSP (pay-as-you-go) | • If you're changing the billing owner of the subscription, see [Transfer billing ownership of an Azure subscription to another account](billing-subscription-transfer). • Reservations don't automatically transfer so you must open a [billing support ticket](https://azure.microsoft.com/support/create-ticket/) to transfer them. |
| MOSP (pay-as-you-go) | MCA-online | • For details, see [Transfer Azure subscription billing ownership for a Microsoft Customer Agreement](mca-request-billing-ownership). • Self-service reservation transfers are supported. |
| MOSP (pay-as-you-go) | EA | • If you're transferring the admin account to the EA enrollment, see [Transfer a subscription to an EA](mosp-ea-transfer#transfer-the-subscription-to-the-ea). • If you're transferring subscriptions to the EA enrollment or if reservations don't automatically transfer, you must create a [billing support ticket](https://azure.microsoft.com/support/create-ticket/). |
| MOSP (pay-as-you-go) | MCA-E | • For details, see [Transfer Azure subscription billing ownership for a Microsoft Customer Agreement](mca-request-billing-ownership). • Self-service reservation transfers are supported. |

### Transfer Reservations and Savings Plans with currency change

Self-service reservation and savings plan transfers with no pricing or billing currency change are supported if the channel and audience permits. In this case, the existing payment plan will continue.

**Reservation**:

- Transfer of reservations with only **pricing currency** change is supported.
- If your enrollment transfer (e.g. EA to MCA, EA to EA, etc.) involves a change in **billing currency** (e.g. EUR to USD) from billing group, the transfer will proceed. However, if the reservation has monthly or flexible payment plan, the billing plan will be cancelled at next billing cycle. If the reservation has an upfront payment, there will be no impact on the reservation.

**Savings Plan**:

- Savings plan transfers that involve a change in **pricing currency** (e.g. EUR to USD) are permitted only when the transfer is from EA to MCA-E, MCA-online, or CSP (MCA managed by partner), **and** the original pricing currency is non-USD. In these cases, there are two options:

    - Choose to have all savings plans automatically canceled in the source account and repurchased in the destination account as 1-year plans.
        - Newly purchased savings plans will have:
            - A USD-equivalent commitment. For example, assuming a €1:$1.17 exchange rate, a €5/hr. plan will be replaced by a $5.85/hr. plan.
            - Monthly billing frequency, regardless of the original billing frequency.
        - Canceled savings plans will result in a prorated refund.
        - If the original savings plan has a 1-year term, the new plan will provide identical savings.
        - One-year savings plans provide less savings than 3-year savings plans because of the discount differences between the terms. To retain the 3-year discount, don't proceed with the automatic cancellation option.
    - If you want to retain the discount level of a 3-year savings plan, contact Azure support immediately for assistance purchasing new 1-year and 3-year savings plans in the destination account and canceling savings plans in the source account.
- If your enrollment transfer (e.g. EA to MCA, EA to EA, etc.) involves a change in **billing currency** (e.g. EUR to USD) from billing group, the transfer will proceed. If the savings plan has monthly or flexible payment plan, the billing plan will be cancelled at next billing cycle. If the savings plan has an upfront payment, there will be no impact on the savings plan.

## Perform resource transfers

Some product transfers require you to manually move Azure resources between subscriptions. Moving resources can incur downtime and there are various limitations to move Azure resource types such as VMs, NSGs, App Services, and others.

Microsoft doesn't provide a tool to automatically move resources between subscriptions. When needed, you must manually move Azure resources between subscriptions. For details, see [Move resources to a new resource group or subscription](../../azure-resource-manager/management/move-resource-group-and-subscription). Extra time and planning are needed when you have a large number of resources to move.

## Other planning considerations

Read the following sections to learn more about other considerations before you start a product transfer.

### Cost Management Considerations

When you transfer your subscriptions between different agreement types, you may need to update role-based access control (RBAC) assignments to ensure that you and other users can view cost information.

The table below outlines the requirements for successfully visualizing cost data after a subscription transfer.

Note

For detailed instructions and additional scenarios, see the Cost Management documentation in the [Related content](/en-us/azure/cost-management-billing/manage/subscription-transfer?branch=main#related-content) section of this article.

Cost Management Data Access Requirements After Subscription Transfer

| Scenario | Prerequisites to Access Cost Data | Possible Scopes and Required RBAC Roles |
| --- | --- | --- |
| **Subscription transferred from one Partner to another** | • Partner to enable Cost visibility policy for the customer• Customer to have correct RBAC | **Customer (Partner Led)**Admin Agent or Billing admin**MPA/MCA Billing Account**Owner, Contributor or Reader**MCA Billing Profile**Owner, Contributor, Reader or Invoice Manager**MCA Invoice Section**Owner, Contributor or Reader**Subscription/Resource group**Owner, Contributor, Reader, Cost Management Contributor or Cost Management Reader |
| **Subscription transferred to MCA** | • Partner to enable Cost visibility policy for the customer• Customer to have correct RBAC | **Customer (Partner Led)**Admin Agent or Billing admin**MPA/MCA Billing Account**Owner, Contributor or Reader**MCA Billing Profile**Owner, Contributor, Reader or Invoice Manager**MCA Invoice Section**Owner, Contributor or Reader**Subscription/Resource group**Owner, Contributor, Reader, Cost Management Contributor or Cost Management Reader |
| **Subscription transferred to MPA** | • Partner to enable Cost visibility policy for the customer• Customer to have correct RBAC | **Customer (Partner Led)**Admin Agent or Billing admin**MPA/MCA Billing Account**Owner, Contributor or Reader**MCA Billing Profile**Owner, Contributor, Reader or Invoice Manager**MCA Invoice Section**Owner, Contributor or Reader**Subscription/Resource group**Owner, Contributor, Reader, Cost Management Contributor or Cost Management Reader |
| **Subscription moved to Enterprise Agreement (EA)** | • Customer to have correct RBAC• Select the new Billing Account• View charges policy is enabled (Account Owners/Department Admins)• Markup is published by the Partner (Indirect EA) | **EA Billing Account**Enterprise Admin (Non Read-Only or Read-Only), Department Admin (Non Read-Only or Read-Only) or Account Owner**Management Group**Owner, Contributor, Reader, Cost Management Contributor or Cost Management Reader**Subscription/Resource group**Owner, Contributor, Reader, Cost Management Contributor or Cost Management Reader |

### Transfer terms and conditions

When you send or accept a transfer, you agree to terms and conditions. The following information provides more details.

#### Azure Marketplace: Transfer Between Billing Accounts — Subscription Type Eligibility

**Overview:**

When you transfer an Azure subscription from one billing account to another, all Azure Marketplace resources on that subscription move with it. The subscription itself remains the same — only the billing account it belongs to changes.

Before the transfer proceeds, Azure validates whether the **target billing account** supports the Marketplace products on the subscription.

**How does the eligibility check work?**

The check evaluates the **target billing account's** payment type. The source billing account's type is not relevant to this check.

- **Paid Marketplace products**: The target billing account must have a supported payment type (see the table below).
- **Free Marketplace products**: No payment type restriction — the transfer is allowed to any billing account type.

**Transfer Eligibility by Payment Type — Paid Marketplace Products:**

Each Azure billing account has a **payment type**. For paid Marketplace products, the transfer is allowed only when the target billing account's payment type is **Paid** or **SponsoredPlus (MultipleSponsorships)**.

| Target Payment Type | Transfer Allowed | Examples |
| --- | --- | --- |
| **Paid** | ✅ | Pay-As-You-Go, Microsoft Customer Agreement, Enterprise Agreement, CSP |
| **SponsoredPlus** (MultipleSponsorships) | ✅ | Azure Sponsorship |
| SponsoredPlus (without MultipleSponsorships) | ❌ | — |
| Free | ❌ | Azure Free Account, Azure for Students |
| Sponsored | ❌ | Academic Sponsorship |
| Entitlement | ❌ | Visual Studio Enterprise, Visual Studio Professional, MPN, MSDN Platforms |
| Benefit | ❌ | Partner benefit |

**Free Marketplace products have no payment type restrictions. Transfers are allowed regardless of the target billing account type.**

Common Scenarios:

| Scenario | Allowed | Reason |
| --- | --- | --- |
| Transfer paid product to a Pay-As-You-Go billing account | ✅ | Payment type is Paid. |
| Transfer paid product to a Microsoft Customer Agreement billing account | ✅ | Payment type is Paid. |
| Transfer paid product to a CSP billing account | ✅ | Payment type is Paid. |
| Transfer paid product to an Azure Sponsorship (MultipleSponsorships) billing account | ✅ | Payment type is SponsoredPlus with MultipleSponsorships. |
| Transfer paid product to an Azure Free Account | ❌ | Payment type is Free. |
| Transfer paid product to an Academic Sponsorship billing account | ❌ | Payment type is Sponsored. |
| Transfer paid product to a Visual Studio Enterprise billing account | ❌ | Payment type is Entitlement. |
| Transfer free product to any billing account | ✅ | Free products have no payment type restrictions. |

**Error Message:**

If the target billing account does not support the Marketplace product being transferred, you will see the following error:

> 
> *"The operation has failed because we couldn't find a valid payment method on this Azure subscription, or the existing payment method is not allowed for transfer. Please add/update current payment method for this subscription and retry."*

**How to resolve:**

- Verify that the target billing account has a **Paid** or **SponsoredPlus (MultipleSponsorships)** payment type.
- Billing accounts with a Free, Sponsored, Entitlement, or Benefit payment type do not support transfer of paid Marketplace products.
- Free Marketplace products can be transferred to any billing account type. If you see this error for a free product, please contact support.

#### Send transfer

When you send a transfer request, must select the **Send transfer request** option. By making the selection, you also agree to the following terms and conditions:

`By sending this transfer request, you acknowledge and agree that the selected items will transfer to your account as of the Transition Date (date when the transfer completed successfully). You will be responsible to Microsoft for all ongoing, scheduled billings related to the transfer items as of the Transition Date; provided that Microsoft will move any prepaid subscriptions (including reserved instances) to your account. You agree that you may not cancel any prepaid subscriptions transferred to your account.`

#### Transfer acceptance

When you accept a transfer, must select the **Review + validate** option. By making the selection, you also agree to the following terms and conditions:

`By accepting this transfer request, you acknowledge and agree that the indicated items will transfer to the nominated destination account as of the Transition Date (date when the transfer completed successfully). Any prepaid subscriptions, if selected, (including reserved instances) will be moved to the destination account and, as of the Transition Date, you will no longer be responsible to Microsoft for ongoing payment obligations (if any) related to the transfer items.`

### Resources transfer with subscriptions

When only billing ownership is changing, then resources aren't affected. All resources from the subscriptions like VMs, disks, and websites transfer. However, when you do a resource move or change the service tenant, then resources could be affected.

### Transfer a product from one account to another

If you're an administrator of two accounts, you can transfer a product between your accounts. Your accounts are conceptually considered accounts of two different users so you can transfer products between your accounts.

To view the steps needed to transfer your product, see [Transfer billing ownership of an Azure subscription](billing-subscription-transfer).

### Transferring a product shouldn't create downtime

If you transfer a product to an account in the same Microsoft Entra tenant, there's no effect on the resources running in the subscription. However, context information saved in PowerShell isn't updated so you might have to clear it or change settings. When you do a resource move or change the service tenant, then resources could be affected.

### New account usage and billing history

The only information available to users for the new account is usage and billing history starting from the time of transfer. Usage and billing history doesn't transfer with the product.

### Remaining product credits

If you have a Visual Studio or Microsoft Cloud Partner Program product, you get monthly credits. Your credit doesn't carry forward with the product in the new account. The user who accepts the transfer request needs to have a Visual Studio license to accept the transfer request. The product uses the Visual Studio credit that's available in the user's account. For more information, see [Transferring Visual Studio and Partner Network subscriptions](billing-subscription-transfer#transfer-visual-studio-and-partner-network-subscriptions).

### Users keep access to transferred resources

Keep in mind that users with access to resources in a product keep their access when billing ownership is transferred. However, [administrator roles](add-change-subscription-administrator) and [Azure role assignments](/en-us/azure/role-based-access-control/role-assignments-portal) might get removed. Losing access occurs when your account is in a Microsoft Entra tenant other than the product's tenant and the user who sent the transfer request moves the product to your account's tenant.

You can view the users who have Azure role assignments to access resources in the product in the Azure portal. Visit the [Subscription page in the Azure portal](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade). Then select the product you want to check, and then select **Access control (IAM)** from the left-hand pane. Next, select **Role assignments** from the top of the page. The role assignments page lists all users who have access on the product.

Even if the [Azure role assignments](/en-us/azure/role-based-access-control/role-assignments-portal) are removed during transfer, users in the original owner account might continue to have access to the product through other security mechanisms, including:

- Management certificates that grant the user admin rights to subscription resources. For more information, see [Create and Upload a Management Certificate for Azure](../../cloud-services/cloud-services-certs-create).
- Access keys for services like Storage. For more information, see [About Azure storage accounts](../../storage/common/storage-account-create).
- Remote Access credentials for services like Azure Virtual Machines.

When the recipient needs to restrict access to resources, they should consider updating any secrets associated with the service. Most resources can be updated. Sign in to the [Azure portal](https://portal.azure.com/) and then on the Hub menu, select **All resources**. Next, select the resource. Then in the resource page, select **Settings**. There you can view and update existing secrets.

### You pay for usage when you receive ownership

Your account is responsible for payment for any usage that is reported from the time of transfer onwards. There might be some usage that took place before the transfer but was reported afterwards. The usage is included in your account's bill.

### Transfer Enterprise Agreement product ownership

The Enterprise Administrator can update account ownership for any account, even after an original account owner is no longer part of the organization. For more information about transferring Azure Enterprise Agreement accounts, see [Azure Enterprise transfers](ea-transfers).

## Supplemental information about transfers

The following sections provide additional information about transferring subscriptions.

### Cancel a prior support plan

When you move your Azure subscriptions to a new agreement, remember to cancel your existing Azure support plan. It doesn't automatically move with the subscriptions. For example, when you transfer a Microsoft Online Subscription Agreement (an Azure subscription purchased on the web) to the Microsoft Customer Agreement. To cancel your support plan:

Use your account administrator credentials for your old account if the credentials differ from the ones used to access your new Microsoft Customer Agreement account.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Navigate to **Cost Management + Billing**.
3. Select **Billing Scopes** in the left pane.
4. Select the billing account associated with your Microsoft support plan.
    - For a Microsoft Customer Agreement:
        - Select **Recurring charges** in the left pane.
        - In the right pane, to the right of the support plan line item, select the ellipsis (**...**) and then select **Turn off auto-renewal**.
    - For a Microsoft Online Subscription Agreement (MOSA):
        - Select **Subscriptions** in the left pane.
        - Select the support plan subscription in the right pane and then select **Cancel**.

### Access your historical invoices

You might want to access your invoices for your old Microsoft Online Subscription Agreement account (an Azure subscription purchased on the web) after you transfer billing ownership to your new Microsoft Customer Agreement account. To do so, use the following steps:

Use your account administrator credentials for your old account if the credentials differ from the ones used to access your new Microsoft Customer Agreement account.

1. Sign in to the Azure portal at https://portal.azure.com/.
2. Navigate to **Cost Management + Billing**.
3. Select **Billing Scopes** in the left pane.
4. Select the billing account associated with your Microsoft Online Subscription Agreement account.
5. Select **Invoices** in the left pane to access your historical invoices.

### Disabled subscriptions

Disabled subscriptions can't be transferred. Subscriptions must be in active state to transfer their billing ownership.

### Azure Marketplace products transfer

Azure Marketplace products transfer along with their respective subscriptions. Software as a service (SaaS) products are a type of Azure Marketplace product, but they don't move with the Azure subscription and transfer differently. For the criteria that determine whether a Marketplace product can transfer, see [Transfer eligibility](/en-us/marketplace/transfer-eligibility).

### Azure Reservations transfer

If you're transferring Enterprise Agreement (EA) subscriptions or Microsoft Customer Agreements, Azure Reservations automatically move with the subscriptions.

### Access to Azure services

Access for existing users, groups, or service principals that was assigned using [Azure role-based access control (Azure RBAC)](../../role-based-access-control/overview) isn't affected during the transition.

### Charges for transferred subscription

Any charges after the time of transfer appear on the new account's invoice. Charges before the time of transfer appear on the previous account's invoice.

The original billing owner of the subscriptions is responsible for any charges that were reported up to the time that the transfer completes. Your invoice section is responsible for charges reported from the time of transfer onwards. There might be some charges that happened before the transfer but were reported afterward. The charges appear on your invoice section.

### Cancel a transfer request

You can cancel the transfer request until the request is approved or declined. To cancel the transfer request, go to the [transfer details page](mca-request-billing-ownership#check-the-transfer-request-status) and select cancel from the bottom of the page.

### Software as a Service (SaaS) transfer

SaaS products are sold as SaaS subscriptions that are associated with, and billed through, an Azure subscription. A SaaS subscription doesn't move with its associated Azure subscription when billing ownership transfers, so you must transfer it separately. Ask the user to [Contact Azure support](https://portal.azure.com/?#blade/Microsoft_Azure_Support/HelpAndSupportBlade) to transfer billing ownership of SaaS subscriptions. Along with the billing ownership, the user can also transfer resource ownership. Resource ownership lets you conduct management operations like deleting and viewing the details of the product. The user must be a resource owner on the SaaS product to transfer resource ownership. For the criteria that determine whether a SaaS product can transfer, see [Transfer eligibility](/en-us/marketplace/transfer-eligibility).