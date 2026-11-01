---
layout: Conceptual
title: Enable Microsoft Purview pay-as-you-go features via subscription | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
description: Learn how enable the Microsoft Purview pay-as-you-go features by associating your Microsoft 365 tenant with an Azure subscription for billing purposes.
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2025-04-04T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-portal
audience: ITPro
ms.topic: concept-article
ms.collection:
- purview-compliance
- essentials-get-started
ms.custom:
- admindeeplinkCOMPLIANCE
- intro-overview
- sfi-ga-nochange
locale: en-us
document_id: 65997c8a-eabd-61cd-7d62-4ebea1b659e5
document_version_independent_id: 65997c8a-eabd-61cd-7d62-4ebea1b659e5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-payg-subscription-based-enablement.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-payg-subscription-based-enablement
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-payg-subscription-based-enablement.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 7373832d-b27c-a535-2444-b13f8f157779
---

# Enable Microsoft Purview pay-as-you-go features via subscription | Microsoft Learn

Applies to:

- Organizations that aren't current Azure Purview customers using the classic data governance pricing model customers.

In this procedure, you enable the Microsoft Purview pay-as-you-go features by associating your Microsoft 365 tenant with an Azure subscription for billing purposes.

If you aren't familiar with the pay-as-you-go model see, [Learn about Microsoft Purview billing models](purview-billing-models#learn-about-microsoft-purview-billing-models).

This featue is in preview.

## Prerequisites for pay-as-you-go

To enable pay-as-you go, you must have:

- An Azure subscription in the same tenant as Microsoft Purview.
- An Azure resource group in that subscription.
- Either of the following service plan
    - MIP\_S\_Exchange
    - EXCHANGE\_S\_FOUNDATION

If you already have these resources, you can use them with Microsoft Purview.

If you don't already have these resources, see:

- [Create your initial Azure subscriptions](/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/initial-subscriptions)
- [Manage Azure resource groups by using the Azure portal](/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal).

### Roles and permissions to consent to the new pricing structure

Only an account in the Global Administrator role can enable the pay-as-you-go model

## Subscription based

The enablement flow requires you to associate your Microsoft Purview tenant to an Azure subscription. All consumption and billing information is available in the [Azure portal](https://portal.azure.com) under **Cost Management + Billing**.

You can use an existing Azure subscription and resource group or create a new one. The Azure subscription must be active to bill against before you can enable the pay-as-you-go billing model.

1. Open the [Microsoft Purview portal](https://purview.microsoft.com) and select the rocket icon on the top right in the header pane, near the **Settings** icon.
2. Select **Get Started** in the ribbon menu to start the process. This can also be done from **Settings** &gt; **Account details**.
3. Select your active Azure subscription from the list. If you don't have an active Azure subscription, you must create a new one before you can proceed. See [Create your initial Azure subscriptions](/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/initial-subscriptions).
4. Select the resource group. If you don't have a **Resouce group** in your Azure tenant, you must create a new one before you can proceed. See - [Manage Azure resource groups by using the Azure portal](/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal). The billing resource is created under the resource group. This is where the pay-as-you-go version of Microsoft Purview is hosted in the Azure portal.

The *Country/Region* value is fixed for the tenant.

Upon completion, it can take a few hours for changes to complete. When completed, you can use pay-as-you-go features to protect your non-Microsoft 365 assets on the **Solutions** page.