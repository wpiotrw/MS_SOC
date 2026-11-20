---
layout: Conceptual
title: View your billing accounts in Azure portal - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts
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
description: Learn how to view your billing accounts in the Azure portal. See scope information for Enterprise, Microsoft Customer, and Microsoft Partner Agreements.
author: jkinma39
ms.reviewer: jkinma
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: concept-article
ms.date: 2026-11-18T00:00:00.0000000Z
ms.author: jkinma
service.tree.id: 95459a4b-434c-4f83-879b-aa5f509fc7fa
locale: en-us
document_id: 23040d03-c7f5-1213-6146-8fb6a3d2c8fb
document_version_independent_id: a55bac65-a49b-eff5-2309-f8a2ae7c094c
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/view-all-accounts.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/view-all-accounts
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/view-all-accounts.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: 6443b813-fd75-7350-6493-3b6db191d5b6
---

# View your billing accounts in Azure portal - Microsoft Cost Management | Microsoft Learn

A billing account is created when you sign up to use Azure. You use your billing account to manage your invoices, payments, and track costs. You can have access to multiple billing accounts. For example, if you signed up for Azure for your personal projects. You could also have access through your organization's Enterprise Agreement or Microsoft Customer Agreement. For each of these scenarios, you would have a separate billing account.

Azure portal supports the following type of billing accounts:

- **Microsoft Online Services Program**: A billing account for a Microsoft Online Services Program is created when you sign up for Azure through the Azure website. For example, when you sign up for an [Azure Free Account](https://azure.microsoft.com/pricing/offers/ms-azr-0044p?cid=msft_learn), [account with pay-as-you-go rates](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn) or as a [Visual Studio subscriber](https://azure.microsoft.com/pricing/member-offers/credit-for-visual-studio-subscribers/).

    - A new billing account for a Microsoft Online Services Program can have a maximum of five subscriptions. However, subscriptions transferred to the new billing account don't count against the limit.
    - The ability to create other Microsoft Online Services Program subscriptions is determined on an individual basis according to your history with Azure.
    - *If you have difficulty finding a new subscription* after you create it, you might need to change the global subscription filter. For more information about changing the global subscription filter, see [Can't view subscription](create-subscription#view-all-subscriptions).
- **Enterprise Agreement**: A billing account for an Enterprise Agreement (EA) is created when your organization signs an [Enterprise Agreement](https://azure.microsoft.com/pricing/enterprise-agreement/) to use Azure. An EA enrollment can contain an unlimited number of EA accounts.

    - An EA account has a subscription limit of 5000. If you need more subscriptions than the limit, create more EA accounts. Generally speaking, a subscription is a billing container.
    - We recommend that you avoid creating multiple subscriptions to implement access boundaries. To separate resources with an access boundary, consider using a resource group. For more information about resource groups, see [Manage Azure resource groups by using the Azure portal](../../azure-resource-manager/management/manage-resource-groups-portal).
- **Microsoft Customer Agreement**: A billing account for a Microsoft Customer Agreement is created when your organization works with a Microsoft representative to sign a Microsoft Customer Agreement. Some customers in select regions, who sign up through the Azure website for an [account with pay-as-you-go rates](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn) or an [Azure Free Account](https://azure.microsoft.com/pricing/offers/ms-azr-0044p?cid=msft_learn) might have a billing account for a Microsoft Customer Agreement as well.

    - You can have a maximum of five subscriptions in a Microsoft Customer Agreement for an individual. The ability to create more subscriptions is determined on an individual basis according to your history with Azure.
    - A Microsoft Customer Agreement for an enterprise can have up to 5,000 subscriptions under it.
- **Microsoft Partner Agreement**: A billing account for a Microsoft Partner Agreement is created for Cloud Solution Provider (CSP) partners to manage their customers in the new commerce experience. Partners need to have at least one customer with an [Azure plan](/en-us/partner-center/purchase-azure-plan) to manage their billing account in the Azure portal. A Partner billing account can have up to 10,000 subscriptions under it. For more information, see [Get started with your billing account for Microsoft Partner Agreement](../understand/mpa-overview).

Regardless of a subscription's state, it gets included in the subscription limit. So, deleted and disabled subscriptions are also included in the subscription limit.

To determine the type of your billing account, see Check the type of your billing account.

## Scopes for billing accounts

A scope is a node within a billing account that you use to view and manage billing. It's where you manage billing data, payments, invoices, and conduct general account management.

Some scopes are created automatically. For example, when you sign up for Azure with a Microsoft Online Services Program agreement, a billing account is created for you. This billing account contains a subscription. The subscription is the scope where you manage billing data, payments, and invoices.

Other scopes are created manually. For example, when you have an Enterprise Agreement, you can create departments and accounts which are billing scopes.

For more information about scopes, see [Understand and work with scopes](../costs/understand-work-scopes).

You might see a subscription created for an EA enrollment that appears in both the EA Account billing scope and also under the MOSP billing scope. Viewing it in both places is intended. For EA enrollment account owners, when a MOSP billing scope gets created, all of the subscriptions under the enrollment account are shown under the MOSP account. Although there's a single subscription, you can view it in both places.

If you don't have access to view or manage billing accounts, you probably don't have permission to access. You can ask your billing account administrator to grant you access. For more information, see the following articles:

- [Microsoft Online Services Program access](manage-billing-access)
- [Microsoft Customer Agreement access](understand-mca-roles)
- [Enterprise Agreement access](understand-ea-roles)

### Microsoft Online Services Program

![Screenshot that shows a M O S P hierarchy.](media/view-all-accounts/mosp-hierarchy.png)

| Scope | Definition |
| --- | --- |
| Billing account | Represents an agreement that a customer accepts to use Azure. It contains one or more subscriptions. |
| Subscription | Represents a grouping of Azure resources. Invoice is generated at this scope. Other billing information such as payment methods and usage address is associated to this scope. |

### Enterprise Agreement

![Screenshot that shows an E A hierarchy.](media/view-all-accounts/ea-hierarchy.png)

| Scope | Definition |
| --- | --- |
| Billing account | Represents an Enterprise Agreement enrollment. It contains one or more departments and accounts. Invoice is generated at this scope. |
| Department | Optional grouping of accounts to segment costs into logical groupings and set budget. |
| Account | Represents a single account owner. Account owners have permissions to create and manage Azure subscriptions that are billed to the enrollment. |

### Microsoft Customer Agreement

![Screenshot that shows an M C A hierarchy.](media/view-all-accounts/mca-hierarchy.png)

| Scope | Tasks |
| --- | --- |
| Billing account | Represents an agreement that a customer accepts to use Microsoft products and services. It contains one or more billing profiles. |
| Billing profile | Represents an invoice and the related billing information such as payment methods and billing address. It contains one or more invoice sections. |
| Invoice section | Represents a grouping of costs in an invoice. Azure subscriptions and other purchases such as Azure Marketplace and App source products are associated to this scope. |

### Microsoft Partner Agreement

![Screenshot that shows an M P A hierarchy.](media/view-all-accounts/mpa-hierarchy.png)

| Scope | Tasks |
| --- | --- |
| Billing account | Represents a partner agreement to manage customers' Microsoft products and services in the new commerce experience. It contains one or more billing profiles and customers. |
| Billing profile | Represents an invoice for a currency. |
| Customer | Represents a customer for a Cloud Solution Provider (CSP) partner. Azure subscriptions and other purchases such as Azure Marketplace and App source products are associated to this scope. |
| Reseller | Reseller that provides services to a customer. It's an optional field for a subscription and is applicable only for Indirect providers in the CSP two-tier model. |

## Switch billing scope in the Azure portal

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for **Cost Management + Billing**.

    ![Screenshot that shows Azure portal search for Cost Management + Billing.](media/view-all-accounts/billing-search-cost-management-billing.png)
3. In the overview page, select **Switch scope**.

    ![Screenshot that shows billing scopes.](media/view-all-accounts/overview-select-scopes.png)

    Note

    You will not see Switch scope if you only have access to one scope.
4. To view details, select a scope.

    ![Screenshot that shows billing scopes, which you can select for details.](media/view-all-accounts/list-of-scopes.png)

## Check the type of your account

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for and select **Cost Management + Billing**.

    [![Screenshot that shows an Azure portal search for Cost Management and Billing.](../../includes/media/billing-check-account-type/billing-search-cost-management-billing.png)](../../includes/media/billing-check-account-type/billing-search-cost-management-billing.png#lightbox)
3. If you have access to just one billing scope, select **Properties** from the left menu.

    The **Type** value on the **Properties** pane determines the type of your account. It can be Microsoft Online Subscription Program, Enterprise Agreement, Microsoft Customer Agreement, or Microsoft Partner Agreement. To learn more about the types of billing accounts, see [View your billing accounts in the Azure portal](view-all-accounts).

    [![Screenshot that shows Microsoft Customer Agreement on the Properties pane.](../../includes/media/billing-check-account-type/billing-mca-property.png)](../../includes/media/billing-check-account-type/billing-mca-property.png#lightbox)

    If you have access to multiple billing scopes, select **Billing scopes** from the left menu, and then check the type in the **Billing account type** column.

    [![Screenshot that shows billing account types for multiple billing scopes.](../../includes/media/billing-check-account-type/billing-account-type-in-the-list.png)](../../includes/media/billing-check-account-type/billing-account-type-in-the-list.png#lightbox)

## Need help? Contact us.

If you have questions or need help, [create a support request](https://go.microsoft.com/fwlink/?linkid=2083458).