---
layout: Conceptual
title: Create an Enterprise Agreement subscription - Azure Cost Management + Billing | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-enterprise-subscription
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
description: Learn how to add a new Enterprise Agreement subscription in the Azure portal. See information about billing account forms and view other available resources.
author: mijeffer
ms.author: mijeffer
ms.reviewer: mijeffer
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.date: 2026-06-07T00:00:00.0000000Z
ms.custom:
- sfi-image-nochange
- sfi-ga-nochange
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: 51605112-4d86-919a-1f9f-71a2300aef85
document_version_independent_id: b5596e3f-b707-b805-df39-b36b9ec5557b
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/create-enterprise-subscription.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/create-enterprise-subscription
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/create-enterprise-subscription.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 88106536-b66f-e444-8e57-e485f1b33c3f
---

# Create an Enterprise Agreement subscription - Azure Cost Management + Billing | Microsoft Learn

This article helps you create an [Enterprise Agreement (EA)](https://azure.microsoft.com/pricing/enterprise-agreement/) subscription for yourself or for someone else in your current Microsoft Entra directory/tenant. You can create another subscription to avoid hitting subscription quota limits, to create separate environments for security, or to isolate data for compliance reasons.

If you want to create subscriptions for Microsoft Customer Agreements, see [Create a Microsoft Customer Agreement subscription](create-subscription). If you're a Microsoft Partner and you want to create a subscription for a customer, see [Create a subscription for a partner's customer](create-customer-subscription). Or, if you have a Microsoft Online Service Program (MOSP) billing account, also called pay-as-you-go, you can create subscriptions starting in the [Azure portal](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade) and then you complete the process at https://signup.azure.com/.

Note

You can't provision Azure resources such as subscriptions, virtual machines, Azure web apps, or Azure functions in a Microsoft Entra B2B or Azure AD B2C tenant. You must create those resources in your Microsoft Entra tenant.

To learn more about billing accounts and identify your billing account type, see [View billing accounts in Azure portal](view-all-accounts).

## Permission required to create Azure subscriptions

You need the following permissions to create subscriptions for an EA:

- An Enterprise Administrator can create a new subscription under any active enrollment account.
- Account Owner role on the Enterprise Agreement enrollment.

For more information, see [Understand Azure Enterprise Agreement administrative roles in Azure](understand-ea-roles).

Note

**Sign-in directory requirement:** Enterprise Administrators and Account Owners must sign in to their **primary Microsoft Entra directory**, also referred to as their primary tenant, to create an Enterprise Agreement subscription. Subscription creation isn't supported while the user is signed in to another directory as a guest, irrespective of their Microsoft Entra role or permissions in that directory.

## Create an EA subscription

A user with Enterprise Administrator or Account Owner permissions can use the following steps to create a new EA subscription for themselves or for another user. If the subscription is for another user, the user is sent a notification that they must approve.

Note

If you want to create an Enterprise Dev/Test subscription, an enterprise administrator must enable account owners to create them. Otherwise, the option to create them isn't available. To enable the dev/test offer for an enrollment, see [Enable the enterprise dev/test offer](direct-ea-administration#enable-the-enterprise-devtest-offer).

1. Sign in to the [Azure portal](https://portal.azure.com)using an account that has Enterprise Administrator or Account Owner permissions. You must be signed in to your **primary Microsoft Entra directory** to create an EA subscription. If you’re currently signed in to another directory where you’re a guest, switch to your primary directory before continuing.
2. Navigate to **Subscriptions** and then select **Add**.[![Screenshot showing the Subscription page where you Add a subscription.](media/create-enterprise-subscription/subscription-add.png)](media/create-enterprise-subscription/subscription-add.png#lightbox)
3. On the Create a subscription page, on the **Basics** tab, type a **Subscription name**.
4. Select the **Billing account** where the new subscription gets created.
5. Select the **Enrollment account** where the subscription gets created.
6. Select an **Offer type**, select **Enterprise Dev/Test** if the subscription is for development or testing workloads. Otherwise, select **Microsoft Azure Enterprise**.[![Screenshot showing the Basics tab where you enter basic information about the enterprise subscription.](media/create-enterprise-subscription/create-subscription-basics-tab-enterprise-agreement.png)](media/create-enterprise-subscription/create-subscription-basics-tab-enterprise-agreement.png#lightbox)
7. Select the **Advanced** tab.
8. Select your **Subscription directory**. It's the Microsoft Entra ID where the new subscription gets created.
9. Select a **Management group**. It's the Microsoft Entra management group that the new subscription is associated with. You can only select management groups in the current directory.
10. Select one or more **Subscription owners**. You can select only users or service principals in the selected subscription directory. You can't select guest directory users. If you select a service principal, enter its App ID.[![Screenshot showing the Advanced tab where you specify the directory, management group, and owner for the EA subscription.](media/create-enterprise-subscription/create-subscription-advanced-tab.png)](media/create-enterprise-subscription/create-subscription-advanced-tab.png#lightbox)
11. Select the **Tags** tab.
12. Enter tag pairs for **Name** and **Value**.[![Screenshot showing the tags tab where you enter tag and value pairs.](media/create-enterprise-subscription/create-subscription-tags-tab.png)](media/create-enterprise-subscription/create-subscription-tags-tab.png#lightbox)
13. Select **Review + create**. You should see a message stating `Validation passed`.
14. Verify that the subscription information is correct, then select **Create**. You get a notification that the subscription is getting created.

After the new subscription is created, the account owner can see it in on the **Subscriptions** page.

## View the new subscription

When you created the subscription, Azure created a notification stating **Successfully created the subscription**. The notification also had a link to **Go to subscription**, which allows you to view the new subscription. If you missed the notification, you can view select the bell symbol in the upper-right corner of the portal to view the notification that has the link to **Go to subscription**. Select the link to view the new subscription.

Here's an example of the notification:

[![Screenshot showing the Successfully created the subscription notification.](media/create-enterprise-subscription/subscription-create-notification.png)](media/create-enterprise-subscription/subscription-create-notification.png#lightbox)

Or, if you're already on the Subscriptions page, you can refresh your browser's view to see the new subscription.

## Create subscription in other tenant and view transfer requests

While signed in to their primary directory, a user with one of the following EA billing roles can request that the subscription be created in another directory.

- Enterprise Administrator
- Account Owner

The request is subject to the subscription policies configured for the source and target directories. For more information, see [Setting subscription policy](manage-azure-subscription-policy#setting-subscription-policy).

When you try to create a subscription in a directory other than their primary directory (such as a customer's tenant), a *subscription creation request* is created. You specify the subscription directory and subscription owner details on the **Advanced** tab when creating the subscription. The subscription owner must accept the subscription ownership request before the subscription is created. The subscription owner is the customer in the target tenant where the subscription is being provisioned.

[![Screenshot showing Create a subscription outside the current directory.](media/create-enterprise-subscription/create-subscription-other-directory.png)](media/create-enterprise-subscription/create-subscription-other-directory.png#lightbox)

When the request is created, the subscription owner (the customer) is sent an email letting them know that they need to accept subscription ownership. The email contains a link used to accept ownership in the Azure portal. The customer must accept the request within seven days. If not accepted within seven days, the request expires. The person that created the request can also manually send their customer the ownership URL to accept the subscription.

After the request is created, it's visible in the Azure portal at **Subscriptions** &gt; **View Requests** by the following people:

- The tenant global administrator of the source tenant where the subscription provisioning request is made.
- The user who made the subscription creation request for the subscription being provisioned in the other tenant.
- The user who made the request to provision the subscription in a different tenant than where they make the [Subscription – Alias REST API](/en-us/rest/api/subscription/) call instead of the Azure portal.

The subscription owner in the request who resides in the target tenant doesn't see this subscription creation request on the View requests page. Instead, they receive an email with the link to accept ownership of the subscription in the target tenant.

[![Screenshot showing View Requests page that lists all subscription creation requests.](media/create-enterprise-subscription/view-requests.png)](media/create-enterprise-subscription/view-requests.png#lightbox)

Anyone with access to view the request can view its details. In the request details, the **Accept ownership URL** is visible. You can copy it to manually share it with the subscription owner in the target tenant for subscription ownership acceptance.

## Can't view subscription

If you created a subscription but can't find it in the Subscriptions list view, a view filter might be applied.

To clear the filter and view all subscriptions:

1. In the Azure portal, navigate to **Subscriptions**.
2. At the top of the list, select the Subscriptions filter item.
3. At the top of the subscriptions filter box, select **All**. At the bottom of the subscriptions filter box, clear **Show only subscriptions selected in the global subscriptions filter**.[![Screenshot showing the Subscriptions filter box with options.](media/create-enterprise-subscription/subscriptions-filter-item.png)](media/create-enterprise-subscription/subscriptions-filter-item.png#lightbox)
4. Select **Apply** to close the box and refresh the list of subscriptions.

## Create an Azure subscription programmatically

You can also create subscriptions programmatically. For more information, see [Create Azure subscriptions programmatically](programmatically-create-subscription).

## Need help? Contact us.

If you have questions or need help, [create a support request](https://go.microsoft.com/fwlink/?linkid=2083458).