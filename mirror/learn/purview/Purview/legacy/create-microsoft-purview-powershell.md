---
layout: Conceptual
title: 'Quickstart: Create a Microsoft Purview (formerly Azure Purview) account with PowerShell/Azure CLI | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/create-microsoft-purview-powershell
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This Quickstart describes how to create a Microsoft Purview (formerly Azure Purview) account using Azure PowerShell/Azure CLI.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.topic: quickstart
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.custom: devx-track-azurepowershell, mode-api, devx-track-azurecli, msecd-doc-authoring-1030
ms.devlang: azurecli
locale: en-us
document_id: fec382b8-2545-f529-00d0-31561d2b1ae3
document_version_independent_id: fec382b8-2545-f529-00d0-31561d2b1ae3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/create-microsoft-purview-powershell.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/create-microsoft-purview-powershell
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/create-microsoft-purview-powershell.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e4ed5d3a-8fc7-8e66-f4d8-3b82523bc315
---

# Quickstart: Create a Microsoft Purview (formerly Azure Purview) account with PowerShell/Azure CLI | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

You can only create one Microsoft Purview account per tenant. If your organization already has a Microsoft Purview account, you won't be able to create a new Microsoft Purview account unless your organization already had multiple accounts and is still under the [the preexisting quota](../classic-how-to-manage-quotas#classic-microsoft-purview-data-governance-limits). For more information, see [the FAQ](../data-governance-purview-portal-faq#can-i-create-new-microsoft-purview-accounts-in-my-subscription-).

In this Quickstart, you'll create a Microsoft Purview account using Azure PowerShell/Azure CLI. [PowerShell reference for Microsoft Purview](/en-us/powershell/module/az.purview/) is available, but this article will take you through all the steps needed to create an account with PowerShell.

The Microsoft Purview governance portal surfaces tools like the Microsoft Purview Data Map and Microsoft Purview Data Catalog that help you manage and govern your data landscape. By connecting to data across your on-premises, multi-cloud, and software-as-a-service (SaaS) sources, the Microsoft Purview Data Map creates an up-to-date map of your information. It identifies and classifies sensitive data, and provides end-to-end linage. Data consumers are able to discover data across your organization, and data administrators are able to audit, secure, and ensure right use of your data.

For more information about the classic governance capabilities of Microsoft Purview, [see our governance solutions overview page](../governance-solutions-overview).

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

### Install PowerShell

Install either Azure PowerShell or Azure CLI in your client machine to deploy the template: [Command-line deployment](/en-us/azure/azure-resource-manager/templates/template-tutorial-create-first-template?tabs=azure-cli#command-line-deployment)

## Create an account

1. Sign in with your Azure credential

# [PowerShell](#tab/azure-powershell)
```azurepowershell
    Connect-AzAccount
    ```

# [Azure CLI](#tab/azure-cli)
```azurecli
    az login
    ```

---
2. If you have multiple Azure subscriptions, select the subscription you want to use:

# [PowerShell](#tab/azure-powershell)
```azurepowershell
    Set-AzContext [SubscriptionID/SubscriptionName]
    ```

# [Azure CLI](#tab/azure-cli)
```azurecli
    az account set --subscription [SubscriptionID/SubscriptionName]
    ```

---
3. Create a resource group for your account. You can skip this step if you already have one:

# [PowerShell](#tab/azure-powershell)
```azurepowershell
    New-AzResourceGroup -Name myResourceGroup -Location 'East US'
    ```

# [Azure CLI](#tab/azure-cli)
```azurecli
    az group create \
      --name myResourceGroup \
      --location "East US"
    ```

---
4. Create or Deploy the account:

# [PowerShell](#tab/azure-powershell)
Use the [New-AzPurviewAccount](/en-us/powershell/module/az.purview/new-azpurviewaccount) cmdlet to create the Microsoft Purview account:

    ```azurepowershell
    New-AzPurviewAccount -Name yourPurviewAccountName -ResourceGroupName myResourceGroup -Location eastus -IdentityType SystemAssigned -SkuCapacity 4 -SkuName Standard -PublicNetworkAccess Enabled
    ```

# [Azure CLI](#tab/azure-cli)
1. Create a Microsoft Purview template file such as `purviewtemplate.json`. You can update `name`, `location`, and `capacity` (`4` or `16`):

        ```json
        {
          "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
          "contentVersion": "1.0.0.0",
          "resources": [
            {
              "name": "<yourPurviewAccountName>",
              "type": "Microsoft.Purview/accounts",
              "apiVersion": "2020-12-01-preview",
              "location": "EastUs",
              "identity": {
                "type": "SystemAssigned"
              },
              "properties": {
                "networkAcls": {
                  "defaultAction": "Allow"
                }
              },
              "dependsOn": [],
              "sku": {
                "name": "Standard",
                "capacity": "4"
              },
              "tags": {}
            }
          ],
          "outputs": {}
        }
        ```
    2. Deploy Microsoft Purview template

        To run this deployment command, you must have the [latest version](/en-us/cli/azure/install-azure-cli) of Azure CLI.

        ```azurecli
        az deployment group create --resource-group "<myResourceGroup>" --template-file "<PATH TO purviewtemplate.json>"
        ```

---
5. The deployment command returns results. Look for `ProvisioningState` to see whether the deployment succeeded.
6. If you deployed the account using a service principal, instead of a user account, you'll also need to run the below command in the Azure CLI:

    ```azurecli
    az purview account add-root-collection-admin --account-name [Microsoft Purview Account Name] --resource-group [Resource Group Name] --object-id [User Object Id]
    ```

    This command will grant the user account [collection admin](../data-gov-classic-permissions#roles) permissions on the root collection in your Microsoft Purview account. This allows the user to access the Microsoft Purview governance portal and add permission for other users. For more information about permissions in Microsoft Purview, see our [permissions guide](../data-gov-classic-permissions). For more information about collections, see our [manage collections article](../data-map-collections-manage-classic).