---
layout: Conceptual
title: 'Quickstart: Create a Microsoft Purview (formerly Azure Purview) account using an ARM Template | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-instance-create-arm
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-06T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to create a Microsoft Purview (formerly Azure Purview) account using an ARM Template.
locale: en-us
document_id: 47786748-d7d3-34a5-9a9d-ae803309119f
document_version_independent_id: 47786748-d7d3-34a5-9a9d-ae803309119f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-instance-create-arm.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
interactive_type: azurepowershell
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-instance-create-arm
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-instance-create-arm.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/4e834929-0ce1-4c1d-9c81-fcb14721edfb
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/75670257-a3f0-4627-9981-8046f99219e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 4647e1ee-44e0-ec70-7e7e-669aa6d0679d
---

# Quickstart: Create a Microsoft Purview (formerly Azure Purview) account using an ARM Template | Microsoft Learn

Important

You can only create one Microsoft Purview account per tenant. If your organization already has a Microsoft Purview account, you won't be able to create a new Microsoft Purview account unless your organization already had multiple accounts and is still under the [the preexisting quota](classic-how-to-manage-quotas#classic-microsoft-purview-data-governance-limits). For more information, see [the FAQ](data-governance-purview-portal-faq#can-i-create-new-microsoft-purview-accounts-in-my-subscription-).

This quickstart describes the steps to deploy a Microsoft Purview (formerly Azure Purview) account using an Azure Resource Manager (ARM) template.

After you've created the account, you can begin registering your data sources and using the Microsoft Purview governance portal to understand and govern your data landscape. By connecting to data across your on-premises, multicloud, and software-as-a-service (SaaS) sources, the Microsoft Purview Data Map creates an up-to-date map of your information. It identifies and classifies sensitive data, and provides end-to-end data linage. Data consumers are able to discover data across your organization and data administrators are able to audit, secure, and ensure right use of your data.

For more information about the classic governance capabilities of Microsoft Purview, [see our governance solutions overview page](governance-solutions-overview).

To deploy a Microsoft Purview account to your subscription using an ARM template, follow the guide below.

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

## Deploy a custom template

If your environment meets the prerequisites and you're familiar with using ARM templates, select the **Deploy to Azure** button. The template will open in the Azure portal where you can customize values and deploy. The template will deploy a Microsoft Purview account into a new or existing resource group in your subscription.

[![Deploy to Azure](media/deploy-to-azure.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azurepurview%2Fazure-purview-deployment%2Fazuredeploy.json)

## Review the template

The template used in this quickstart is from [Azure Quickstart Templates](https://azure.microsoft.com/resources/templates/azure-purview-deployment/).

```JSON
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "metadata": {
    "_generator": {
      "name": "bicep",
      "version": "0.11.1.770",
      "templateHash": "10388724958841997784"
    }
  },
  "parameters": {
    "purviewName": {
      "type": "string",
      "defaultValue": "[format('azurePurview{0}', uniqueString(resourceGroup().id))]",
      "metadata": {
        "description": "Specify a name for the Azure Purview account."
      }
    },
    "location": {
      "type": "string",
      "defaultValue": "[resourceGroup().location]",
      "metadata": {
        "description": "Specify a region for resource deployment."
      }
    }
  },
  "resources": [
    {
      "type": "Microsoft.Purview/accounts",
      "apiVersion": "2021-12-01",
      "name": "[parameters('purviewName')]",
      "location": "[parameters('location')]",
      "sku": {
        "name": "Standard",
        "capacity": 1
      },
      "identity": {
        "type": "SystemAssigned"
      },
      "properties": {
        "publicNetworkAccess": "Enabled",
        "managedResourceGroupName": "[format('managed-rg-{0}', parameters('purviewName'))]"
      }
    }
  ]
}
```

The following resources are defined in the template:

- [Microsoft.Purview/accounts](/en-us/azure/templates/microsoft.purview/accounts?pivots=deployment-language-arm-template)

The template performs the following tasks:

- Creates a Microsoft Purview account in a specified resource group.

## Customize network settings for your account

When you're deploying your ARM template, you can also use the following settings in the template to manage your public network access settings:

- **Enabled for all networks**`"publicNetworkAccess": "Enabled", "managedResourcesPublicNetworkAccess": "Enabled" `
- **Disabled for ingestion only (Preview)**`"publicNetworkAccess": "Enabled", "managedResourcesPublicNetworkAccess": "Disabled" `
- **Disabled from all networks**`"publicNetworkAccess": "Disables", "managedResourcesPublicNetworkAccess": "Disabled" `

For example: `"resources": [ { "type": "Microsoft.Purview/accounts", "apiVersion": "2021-12-01", "name": "[parameters('purviewName')]", "location": "[parameters('location')]", "sku": { "name": "Standard", "capacity": 1 }, "identity": { "type": "SystemAssigned" }, "properties": { "publicNetworkAccess": "Enabled", "managedResourcesPublicNetworkAccess": "Enabled" "managedResourceGroupName": "[format('managed-rg-{0}', parameters('purviewName'))]" } } ]`

## Open the Microsoft Purview governance portal

After your account is created, you can use the [Microsoft Purview portal](https://purview.microsoft.com) to access and manage it.

In a browser, navigate directly to https://purview.microsoft.com to access the portal.

![Screenshot showing the Microsoft Purview portal main page.](media/purview-portal.png)

For more information about using the portal, see our [documentation on the Microsoft Purview portal](purview-portal).

## Get started with your Purview resource

After deployment, the first activities are usually:

- [Create a collection](data-map-collections-create-classic)
- [Register a resource](data-map-data-sources)
- [Scan the resource](data-map-scan-ingestion)

At this time, these actions aren't able to be taken through an Azure Resource Manager template. Follow the guides above to get started!

## Clean up resources

To clean up the resources deployed in this quickstart, delete the resource group, which deletes all resources in the group. You can delete the resources either through the Azure portal, or using the PowerShell script below.

```azurepowershell
$resourceGroupName = Read-Host -Prompt "Enter the resource group name"
Remove-AzResourceGroup -Name $resourceGroupName
Write-Host "Press [ENTER] to continue..."
```