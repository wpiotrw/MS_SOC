---
layout: Conceptual
title: Upgrade to Enterprise Microsoft Purview Data Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-free-version-upgrade-to-enterprise
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to upgrade from the free to the enterprise version of Microsoft Purview data governance solutions.
locale: en-us
document_id: c23c9bab-52cb-193c-854e-f3a60a3e1913
document_version_independent_id: c23c9bab-52cb-193c-854e-f3a60a3e1913
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-free-version-upgrade-to-enterprise.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-free-version-upgrade-to-enterprise
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-free-version-upgrade-to-enterprise.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 2d26acdd-f797-b907-f674-63496c0b3322
---

# Upgrade to Enterprise Microsoft Purview Data Governance | Microsoft Learn

Note

If you already have a Microsoft Purview account and enabled the new Microsoft Purview portal experience, you are using the enterprise version of Microsoft Purview. You can check your account type in the [Microsoft Purview portal](https://purview.microsoft.com) by selecting the **Settings** gear icon, then selecting **View all settings**.

When you upgrade from the free version of Microsoft Purview governance solutions to the enterprise version, the data in the free version will automatically be available in the enterprise version within minutes. Your experience in the portal remains the same, and you gain access to all Microsoft Purview data governance solutions' capabilities, including:

- [All Microsoft Purview supported sources](data-map-data-sources)
- [Collections](data-map-collections-manage-classic)
- [Scanning](data-map-scan-data-sources)
- [Automatic classification](data-map-classification-apply-auto)
- [Microsoft Purview policies](concept-policies-data-owner)
- [All reports in Data Estate Insights](concept-policies-data-owner)
- [Workflows](concept-insights)

Learn more about [getting started with Microsoft Purview data governance solutions](data-governance-get-started).

Important

If you [create a classic Microsoft Purview instance](create-microsoft-purview-portal) for the first time in your organization, the instance will automatically be upgraded to the enterprise version of Microsoft Purview.

## Upgrade

You can upgrade to the enterprise version of Microsoft Purview using these steps:

1. Open the [Microsoft Purview portal](https://purview.microsoft.com)
2. Select the upgrade button in the ribbon menu, or select **Settings**, then **View all settings**.

    ![Screenshot of upgrade button and the View all settings button highlighted in the ribbon menu.](media/upgrade/upgrade-button-settings.png)
3. Select **Upgrade**

    ![Screenshot of inline upgrade menu with the upgrade button highlighted.](media/upgrade/rocket-select-upgrade.png)

    ![Screenshot of the account settings menu with the upgrade button highlighted.](media/upgrade/settings-select-upgrade.png)
4. Your region is the same region as the free version of your Microsoft Purview account. For more information, [see the FAQ.](data-governance-purview-portal-faq#what-region-is-microsoft-purview-in-if-we-use-the-free-version-)
5. Select the Azure subscription where you would like to house the Azure linked Microsoft Purview resource.
6. Select the resource group where you would like to house the Azure linked resource.
7. Select the check box to acknowledge terms and conditions.
8. Select **Upgrade**

    [![Screenshot of the upgrade to Microsoft Purview Enterprise menu with the upgrade button highlighted.](media/upgrade/details-selection-inline.png)](media/upgrade/details-selection.png#lightbox)
9. You've upgraded! Select **Use default settings** to get started, or **Continue with setup** to manage settings.

## Protect your account

In order to protect your Microsoft Purview account from accidental deletion, we recommend creation of the Azure Policy ['DenyAction'](/en-us/azure/governance/policy/concepts/effect-deny-action#denyaction-example)

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

### Settings

Governance settings in the new Microsoft Purview portal include:

- Account type - either free or enterprise. [The free version](data-governance-free-version) only includes a subset of applications and sources. The enterprise version of Microsoft Purview includes all available governance applications and sources.
- [Kafka configurations](data-map-kafa-notifications) - configure Microsoft Purview to be able to send and receive Atlas Kafka topics events with Azure Event Hubs

## Possible exceptions

When you're upgrading to the enterprise version of Microsoft Purview, there are a few possible exceptions you can encounter. These guides address them.

### Private endpoints

If your Microsoft Purview account had disabled all public network access and is using private endpoints, you can still upgrade to the new experience.

You can continue to use your [*ingestion* private endpoints](data-gov-classic-private-link-end-to-end#deploy-ingestion-private-endpoint) as is, but the new experience also uses a *platform* private endpoint.

After upgrading to the new experience, you can follow [this guide to set up platform the private endpoint for governance solutions in the Microsoft Purview portal.](data-governance-private-endpoints)

For more information, see [what to do if your account has disabled all public network access.](data-governance-purview-portal#disabled-all-public-network-access)

### Resource providers

Before upgrading to the enterprise version of Microsoft Purview, you need to have these [resource providers registered in Azure](/en-us/azure/azure-resource-manager/management/resource-providers-and-types):

- Microsoft.Purview
- Microsoft.Storage
- Microsoft.EventHub

If all of them aren't already registered, you might receive an error.

### Default name isn't allowed

It's possible that default names have been disallowed in your organization, and you need to enter a new resource name.

To resolve, enter a new resource name and then complete the upgrade process.

For more information about default naming policies, you can see the [resource naming guidance documentation](/en-us/azure/cloud-adoption-framework/govern/resource-consistency/naming#enforce).

### Region

If your account is in a different region than your tenant, an admin needs to confirm setup.

Note

If you want to use a different region, you will either need to cancel and wait for upcoming region related features, or cancel and create a new Microsoft Purview account in one of the [available regions](data-governance-purview-portal#regions).

### Nonadmin request

If a user who isn't a [Purview Admin](data-governance-roles-permissions#tenant-level-role-groups) selects the upgrade button, a request to upgrade is sent to an administrator. The administrator can update from directly within the request email, or they can upgrade using the above steps.

If you don't have access to the Microsoft 365 role groups to assign [Purview Admins](data-governance-roles-permissions#tenant-level-role-groups), [contact support](https://portal.azure.com/?quickstart=true#view/Microsoft_Azure_Support/HelpAndSupportBlade/%7E/overview).

## Switch back to classic portal

Even after upgrading to the enterprise version of Microsoft Purview, you can switch back to the classic portal at any time using the toggle.

![Screenshot of the portal experience toggle.](media/upgrade/switch.png)

## Billing

Note

The enterprise version of Microsoft Purview uses the same pricing dimensions as the classic Microsoft Purview governance portal experience. You can check your account type in the [Microsoft Purview portal](https://purview.microsoft.com) under **Settings**, then **View all settings**.

Billing for the enterprise version of Microsoft Purview is pay-as-you-go.

For more information, see these articles:

- [Pricing guidelines](data-gov-classic-pricing)
- [Microsoft Purview elastic data map](/en-us/purview/concept-elastic-data-map#data-map-billing)
- [Pricing calculator](https://azure.microsoft.com/pricing/details/purview/)

## Linked resource

The enterprise version of Microsoft Purview is hosted by a linked resource in the Azure portal. If you delete this linked resource in the Azure portal, you lose all your Microsoft Purview information.

After deletion, you can reinstate the free version for your environment if it's been enabled for your organization by going to the [Microsoft Purview portal](https://purview.microsoft.com). But you're starting your environment from scratch.