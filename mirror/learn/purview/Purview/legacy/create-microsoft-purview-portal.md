---
layout: Conceptual
title: Create a Microsoft Purview account | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/create-microsoft-purview-portal
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This quickstart describes how to create a Microsoft Purview account and configure permissions to begin using it.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.topic: quickstart
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.custom: mode-ui, msecd-doc-authoring-1030
locale: en-us
document_id: 4a882e45-bcdb-334b-fad9-0f19bc8d5125
document_version_independent_id: 4a882e45-bcdb-334b-fad9-0f19bc8d5125
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/create-microsoft-purview-portal.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/create-microsoft-purview-portal
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/create-microsoft-purview-portal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6f16064b-3333-1e65-c79f-2956424d9725
---

# Create a Microsoft Purview account | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

You can only create one Microsoft Purview account per tenant. If your organization already has a Microsoft Purview account, you won't be able to create a new Microsoft Purview account unless your organization already had multiple accounts and is still under the [the preexisting quota](../classic-how-to-manage-quotas#classic-microsoft-purview-data-governance-limits). For more information, see [the FAQ](../data-governance-purview-portal-faq#can-i-create-new-microsoft-purview-accounts-in-my-subscription-).

Tip

If your organization hasn't created a Microsoft Purview account in Azure before, start in the [new Microsoft Purview portal](../purview-portal): https://purview.microsoft.com. You can use [the free version](../data-governance-free-version-get-started) to test capabilities, and upgrade to [the enterprise version](../data-governance-free-version-upgrade-to-enterprise) for the full [data governance in Microsoft Purview features.](../unified-catalog)

This quickstart describes the steps to create a Microsoft Purview (formerly Azure Purview) account through the Azure portal. Then we'll get started on the process of classifying, securing, and discovering your data in the Microsoft Purview Data Map!

The Microsoft Purview governance portal surfaces tools like the Microsoft Purview Data Map and Microsoft Purview Data Catalog that help you manage and govern your data landscape. By connecting to data across your on-premises, multicloud, and software-as-a-service (SaaS) sources, the Microsoft Purview Data Map creates an up-to-date map of your data estate. It identifies and classifies sensitive data, and provides end-to-end linage. Data consumers are able to discover data across your organization, and data administrators are able to audit, secure, and ensure right use of your data.

For more information about the governance capabilities of Microsoft Purview, [see our governance solutions overview page](../purview-portal#new-experience-for-new-customers).

## Prerequisites

- If you don't have an Azure subscription, create a [free subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- A [Microsoft Entra tenant](/en-us/azure/active-directory/fundamentals/active-directory-access-create-new-tenant) associated with your subscription.
- The user account that you use to sign in to Azure must be a member of the *contributor* or *owner* role, or an *administrator* of the Azure subscription. To view the permissions that you have in the subscription, follow these steps:

    1. Go to the [Azure portal](https://portal.azure.com)
    2. Select your username in the upper-right corner.
    3. Select the ellipsis button ("**...**") for more options.
    4. Then select **My permissions**.
    5. If you have access to multiple subscriptions, select the appropriate subscription.

## Sign in to Azure

Sign in to the [Azure portal](https://portal.azure.com) with your Azure account.

## Create an account

Tip

If you're creating the first Microsoft Purview account in your tenant, you don't need to set anything up and you should use [the free version of Microsoft Purview governance solutions](../data-governance-free-version) at https://purview.microsoft.com.

Important

If you have any [Azure Policies](/en-us/azure/governance/policy/overview) preventing creation of **Storage accounts** or **Event Hub namespaces**, or preventing **updates to Storage accounts** first follow the [Microsoft Purview exception tag guide](../data-gov-azure-policy-exclusion) to create an exception for Microsoft Purview accounts. Otherwise you will not be able to deploy Microsoft Purview.

1. Search for **Microsoft Purview** in the [Azure portal](https://portal.azure.com).

    [![Screenshot showing the purview accounts page in the Azure portal](../media/create-catalog-portal/purview-accounts-page.png)](../media/create-catalog-portal/purview-accounts-page.png#lightbox)
2. Select **Create** to create a new Microsoft Purview account.

    [![Screenshot of the Microsoft Purview accounts page with the create button highlighted in the Azure portal.](../media/create-catalog-portal/select-create.png)](../media/create-catalog-portal/select-create.png#lightbox)

    Or instead, you can go to the marketplace, search for **Microsoft Purview**, and select **Create**.

    [![Screenshot showing Microsoft Purview in the Azure Marketplace, with the create button highlighted.](../media/create-catalog-portal/search-marketplace.png)](../media/create-catalog-portal/search-marketplace.png#lightbox)
3. On the new Create Microsoft Purview account page under the **Basics** tab, select the Azure subscription where you want to create your account.
4. Select an existing **resource group** or create a new one to hold your account.

    To learn more about resource groups, see our article on [using resource groups to manage your Azure resources](/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#what-is-a-resource-group).
5. Enter a **Microsoft Purview account name**. Spaces and symbols aren't allowed.

    The name of the Microsoft Purview account must be globally unique. If you see the following error, change the name of Microsoft Purview account and try creating again.

    [![Screenshot showing the Create Microsoft Purview account screen with an account name that is already in use, and the error message highlighted.](../media/create-catalog-portal/name-error.png)](../media/create-catalog-portal/name-error.png#lightbox)
6. Choose a **location**.

    The list shows only locations that support the Microsoft Purview governance portal, and if this is your organization's first Microsoft Purview account, the location is restricted to the one that matches your Microsoft Entra ID home region. This location is the region where your Microsoft Purview account and metadata are stored. Sources can be housed in other regions.

    Note

    The Microsoft Purview, formerly Azure Purview, does not support moving accounts across regions, so be sure to deploy to the correction region. You can find out more information about this in [move operation support for resources](/en-us/azure/azure-resource-manager/management/move-support-resources).
7. On the **Networking** tab you can choose to connect to all networks, or to use private endpoints. For more information and configuration options, see [Configure firewall settings for your Microsoft Purview account](../data-gov-classic-firewall) and [private endpoints for Microsoft Purview articles.](../data-gov-classic-private-link)
8. On **Configuration** tab you can choose to configure Event Hubs namespaces to programmatically monitor your Microsoft Purview account using Event Hubs and Atlas Kafka.

    - [Steps to configure Event Hubs namespaces](../data-map-kafa-notifications)
    - [Send and receive Atlas Kafka topics messages](../data-map-kafta-send-receive-events)

    [![Screenshot showing the Event Hubs configuration page in the Create Microsoft Purview account window.](../media/create-catalog-portal/configure-kafka-event-hubs.png)](../media/create-catalog-portal/configure-kafka-event-hubs.png#lightbox)

    Note

    [These options can be configured after you have created your account](../data-map-kafa-notifications) in **Kafka configuration** under settings on your Microsoft Purview account page in the Azure Portal.

    ![Screenshot showing Kafka configuration option on the Microsoft Purview account page in the Azure Portal.](../media/create-catalog-portal/select-kafka-configuration.png)
9. On the **Tags** tab, add a tag called **Purview environment**, and give it one of the below values:

    | Value | Meaning |
    | --- | --- |
    | Production | This account is being used or will be used in the future to support all my cataloging and governance requirements in production. |
    | Pre-Production | This account is being used or will be used in the future to validate cataloging and governance requirements before making it available to my users in production. |
    | Test | This account is being used or will be used in the future to test out capabilities in Microsoft Purview Governance. |
    | Dev | This account is being used or will be used in the future to test out capabilities or develop custom code, scripts etc. in Microsoft Purview Governance. |
    | Proof of Concept | This account is being used or will be used in the future to test out capabilities or develop custom code, scripts etc. in Microsoft Purview Governance. |

    [![Screenshot showing the tags tab, with a Purview environment tag added with the value Production.](../media/create-catalog-portal/tag-resource.png)](../media/create-catalog-portal/tag-resource.png#lightbox)
10. Select **Review & Create**, and then select **Create**. It takes a few minutes to complete the creation. The newly created account appears in the list on your **Microsoft Purview accounts** page.

    ![Screenshot showing the Create Microsoft Purview account screen with the Review + Create button highlighted](../media/create-catalog-portal/create-resource.png)

## Protect your account

To protect your Microsoft Purview Account from accidental deletion, Microsoft recommends that you create the Azure policy ['DenyAction'] (/azure/governance/policy/concepts/effect-deny-action#denyaction-example)

```json
{
  "if": {
    "allOf": [
      {
        "field": "type",
        "equals": "Microsoft.Purview/accounts"
      },
      {
        "field": "tags.environment",
        "equals": "Production"
      }
    ]
  },
  "then": {
    "effect": "denyAction",
    "details": {
      "actionNames": [
        "delete"
      ],
      "cascadeBehaviors": {
        "resourceGroup": "deny"
      }
    }
  }
}
```

## Open the Microsoft Purview portal

After your account is created, you can use the [Microsoft Purview portal](https://purview.microsoft.com) to access and manage it.

In a browser, navigate directly to https://purview.microsoft.com to access the portal.

[![Screenshot showing the Microsoft Purview portal main page.](../media/purview-portal.png)](../media/purview-portal.png#lightbox)

For more information about using the portal, see our [documentation on the Microsoft Purview portal](../purview-portal).