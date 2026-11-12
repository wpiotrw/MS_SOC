---
layout: Conceptual
title: 'Quickstart: Create a Microsoft Purview (formerly Azure Purview) account using a Bicep file | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/quickstart-bicep-create-microsoft-purview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This Quickstart describes how to create a Microsoft Purview (formerly Azure Purview) account using a Bicep file.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jife
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.topic: quickstart
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.custom: devx-track-bicep, msecd-doc-authoring-1030
locale: en-us
document_id: e651d4d2-9333-8d1e-06a6-81e818ca1b27
document_version_independent_id: e651d4d2-9333-8d1e-06a6-81e818ca1b27
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/quickstart-bicep-create-microsoft-purview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
interactive_type: azurecli,azurepowershell
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/quickstart-bicep-create-microsoft-purview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/quickstart-bicep-create-microsoft-purview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 75685b63-f739-6574-92af-0ff4808e6141
---

# Quickstart: Create a Microsoft Purview (formerly Azure Purview) account using a Bicep file | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

You can only create one Microsoft Purview account per tenant. If your organization already has a Microsoft Purview account, you won't be able to create a new Microsoft Purview account unless your organization already had multiple accounts and is still under the [the preexisting quota](../classic-how-to-manage-quotas#classic-microsoft-purview-data-governance-limits). For more information, see [the FAQ](../data-governance-purview-portal-faq#can-i-create-new-microsoft-purview-accounts-in-my-subscription-).

This quickstart describes the steps to deploy a Microsoft Purview (formerly Azure Purview) account using a Bicep file.

After you've created the account, you can begin registering your data sources, and using the Microsoft Purview governance portal to understand and govern your data landscape. By connecting to data across your on-premises, multicloud, and software-as-a-service (SaaS) sources, the Microsoft Purview Data Map creates an up-to-date map of your information. It identifies and classifies sensitive data, and provides end-to-end data linage. Data consumers are able to discover data across your organization and data administrators are able to audit, secure, and ensure right use of your data.

For more information about the classic governance capabilities of Microsoft Purview, [see our governance solutions overview page](../governance-solutions-overview).

To deploy a Microsoft Purview account to your subscription using a Bicep file, follow the guide below.

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

## Review the Bicep file

The Bicep file used in this quickstart is from [Azure Quickstart Templates](https://azure.microsoft.com/resources/templates/azure-purview-deployment/).

```bicep
@description('Specify a name for the Azure Purview account.')
param purviewName string = 'azurePurview${uniqueString(resourceGroup().id)}'

@description('Specify a region for resource deployment.')
param location string = resourceGroup().location

resource purview 'Microsoft.Purview/accounts@2021-12-01' = {
  name: purviewName
  location: location
  sku: {
    name: 'Standard'
    capacity: 1
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    publicNetworkAccess: 'Enabled'
    managedResourceGroupName: 'managed-rg-${purviewName}'
  }
}
```

The following resources are defined in the Bicep file:

- [Microsoft.Purview/accounts](/en-us/azure/templates/microsoft.purview/accounts?pivots=deployment-language-bicep)

The Bicep file performs the following tasks:

- Creates a Microsoft Purview account in a specified resource group.

## Deploy the Bicep file

1. Save the Bicep file as **main.bicep** to your local computer.
2. Deploy the Bicep file using either Azure CLI or Azure PowerShell.

# [CLI](#tab/CLI)
```azurecli
    az group create --name exampleRG --location eastus
    az deployment group create --resource-group exampleRG --template-file main.bicep
    ```

# [PowerShell](#tab/PowerShell)
```azurepowershell
    New-AzResourceGroup -Name exampleRG -Location eastus
    New-AzResourceGroupDeployment -ResourceGroupName exampleRG -TemplateFile ./main.bicep
    ```

---

You'll be prompted to enter the following values:

- **Purview name**: enter a name for the Microsoft Purview account.

When the deployment finishes, you should see a message indicating the deployment succeeded.

## Open the Microsoft Purview governance portal

After your account is created, you can use the [Microsoft Purview portal](https://purview.microsoft.com) to access and manage it.

In a browser, navigate directly to https://purview.microsoft.com to access the portal.

![Screenshot showing the Microsoft Purview portal main page.](../media/purview-portal.png)

For more information about using the portal, see our [documentation on the Microsoft Purview portal](../purview-portal).

## Get started with your Purview resource

After deployment, the first activities are usually:

- [Create a collection](../data-map-collections-create-classic)
- [Register a resource](../data-map-data-sources)
- [Scan the resource](../data-map-scan-ingestion)

At this time, these actions aren't able to be taken through a Bicep file. Follow the guides above to get started!

## Clean up resources

When you no longer need them, use the Azure portal, Azure CLI, or Azure PowerShell to remove the resource group, firewall, and all related resources.

# [CLI](#tab/CLI)
```azurecli
az group delete --name exampleRG
```

# [PowerShell](#tab/PowerShell)
```azurepowershell
Remove-AzResourceGroup -Name exampleRG
```

---