---
layout: Conceptual
title: Copy managed disk snapshot to a subscription - CLI Sample - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/scripts/copy-snapshot-to-same-or-different-subscription
breadcrumb_path: ../../breadcrumb/azure-compute/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/94/azure-virtual-machines/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ec2f1827-be25-ec11-b6e6-000d3a4f0f1c
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
description: Azure CLI Script Sample - Copy (or move) snapshot of a managed disk to same or different subscription with CLI
author: ushnaarshadkhan
ms.service: azure-disk-storage
ms.topic: sample
ms.date: 2023-02-22T00:00:00.0000000Z
ms.author: uarshadkhan
ms.custom: mvc, devx-track-azurecli
locale: en-us
document_id: fd3d0e23-3ca1-fcae-7ef7-ad579222146a
document_version_independent_id: 61e3f652-d95f-20ae-862a-6ecfa5a3be13
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/scripts/copy-snapshot-to-same-or-different-subscription.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli
toc_rel: ../toc.json
asset_id: virtual-machines/scripts/copy-snapshot-to-same-or-different-subscription
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/scripts/copy-snapshot-to-same-or-different-subscription.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/089c8ba6-d135-43ff-bfaf-b8197fb72fb9
- https://authoring-docs-microsoft.poolparty.biz/devrel/cdc80360-921e-4b45-947f-2719acf06f23
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/32516e21-6665-416f-be21-413febe47d91
- https://authoring-docs-microsoft.poolparty.biz/devrel/539badf0-028a-4e3e-bda6-770b2552b4d8
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: cacf4bc3-800b-a247-d06b-286fe78465c8
---

# Copy managed disk snapshot to a subscription - CLI Sample - Azure Virtual Machines | Microsoft Learn

This article contains two scripts. The first script copies a snapshot of a managed disk that was using platform-managed keys to the same or a different subscription. The second script copies a snapshot of a managed disk that was using customer-managed keys to the same or a different subscription. These scripts can be used for the following scenarios:

- Migrate a snapshot in Premium storage (Premium\_LRS) to Standard storage (Standard\_LRS or Standard\_ZRS) to reduce your cost.
- Migrate a snapshot from locally redundant storage (Premium\_LRS, Standard\_LRS) to zone redundant storage (Standard\_ZRS) to benefit from the higher reliability of ZRS storage.
- Move a snapshot to different subscription in the same region for longer retention.

Note

Both subscriptions must be located under the same tenant

If you don't have an Azure account, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

## Prerequisites

- Use the Bash environment in [Azure Cloud Shell](/en-us/azure/cloud-shell/overview). For more information, see [Get started with Azure Cloud Shell](/en-us/azure/cloud-shell/quickstart).

    [![](../../reusable-content/azure-cli/media/hdi-launch-cloud-shell.png)](https://shell.azure.com)
- If you prefer to run CLI reference commands locally, [install](/en-us/cli/azure/install-azure-cli) the Azure CLI. If you're running on Windows or macOS, consider running Azure CLI in a Docker container. For more information, see [How to run the Azure CLI in a Docker container](/en-us/cli/azure/run-azure-cli-docker).

    - If you're using a local installation, sign in to the Azure CLI by using the [az login](/en-us/cli/azure/reference-index#az-login) command. To finish the authentication process, follow the steps displayed in your terminal. For other sign-in options, see [Authenticate to Azure using Azure CLI](/en-us/cli/azure/authenticate-azure-cli).
    - When you're prompted, install the Azure CLI extension on first use. For more information about extensions, see [Use and manage extensions with the Azure CLI](/en-us/cli/azure/azure-cli-extensions-overview).
    - Run [az version](/en-us/cli/azure/reference-index?#az-version) to find the version and dependent libraries that are installed. To upgrade to the latest version, run [az upgrade](/en-us/cli/azure/reference-index?#az-upgrade).

## Sample script

### Launch Azure Cloud Shell

The Azure Cloud Shell is a free interactive shell that you can use to run the steps in this article. It has common Azure tools preinstalled and configured to use with your account.

To open the Cloud Shell, just select **Try it** from the upper right corner of a code block. You can also launch Cloud Shell in a separate browser tab by going to https://shell.azure.com.

When Cloud Shell opens, verify that **Bash** is selected for your environment. Subsequent sessions will use Azure CLI in a Bash environment, Select **Copy** to copy the blocks of code, paste it into the Cloud Shell, and press **Enter** to run it.

### Sign in to Azure

Cloud Shell is automatically authenticated under the initial account signed-in with. Use the following script to sign in using a different subscription, replacing *subscriptionId* with your Azure subscription ID.

If you don't have an Azure account, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

```azurecli
subscription="subscriptionId" # Set Azure subscription ID here

az account set -s $subscription # ...or use 'az login'
```

For more information, see [set active subscription](/en-us/cli/azure/account#az-account-set) or [log in interactively](/en-us/cli/azure/reference-index#az-login).

### Disks with platform-managed keys

```azurecli
#Provide the subscription Id of the subscription where snapshot exists
sourceSubscriptionId="<subscriptionId>"

#Provide the name of your resource group where snapshot exists
sourceResourceGroupName=mySourceResourceGroupName

#Provide the name of the snapshot
snapshotName=mySnapshotName

#Set the context to the subscription Id where snapshot exists
az account set --subscription $sourceSubscriptionId

#Get the snapshot Id 
snapshotId=$(az snapshot show --name $snapshotName --resource-group $sourceResourceGroupName --query [id] -o tsv)

#If snapshotId is blank then it means that snapshot does not exist.
echo 'source snapshot Id is: ' $snapshotId

#Provide the subscription Id of the subscription where snapshot will be copied to
#If snapshot is copied to the same subscription then you can skip this step
targetSubscriptionId=6492b1f7-f219-446b-b509-314e17e1efb0

#Name of the resource group where snapshot will be copied to
targetResourceGroupName=mytargetResourceGroupName

#Name of the location where snapshot will be copied to
location=locationName

#Set the context to the subscription Id where snapshot will be copied to
#If snapshot is copied to the same subscription then you can skip this step
az account set --subscription $targetSubscriptionId

#Copy snapshot to different subscription using the snapshot Id
#We recommend you to store your snapshots in Standard storage to reduce cost. Please use Standard_ZRS in regions where zone redundant storage (ZRS) is available, otherwise use Standard_LRS
#Please check out the availability of ZRS here: https://docs.microsoft.com/azure/storage/common/storage-redundancy-zrs#support-coverage-and-regional-availability
az snapshot create --resource-group $targetResourceGroupName --name $snapshotName --location $location --source $snapshotId --sku Standard_LRS
```

### Disks with customer-managed keys

```azurecli
#Provide the subscription Id of the subscription where snapshot exists
sourceSubscriptionId="<subscriptionId>"

#Provide the name of your resource group where snapshot exists
sourceResourceGroupName=mySourceResourceGroupName

#Provide the name of the target disk encryption set
diskEncryptionSetName=myName

#Provide the target disk encryption set resource group
diskEncryptionResourceGroup=myGroup

#Provide the name of the snapshot
snapshotName=mySnapshotName

#Set the context to the subscription Id where snapshot exists
az account set --subscription $sourceSubscriptionId

#Get the snapshot Id 
snapshotId=$(az snapshot show --name $snapshotName --resource-group $sourceResourceGroupName --query [id] -o tsv)

#If snapshotId is blank then it means that snapshot does not exist.
echo 'source snapshot Id is: ' $snapshotId

#Get the disk encryption set ID
diskEncryptionSetId=$(az disk-encryption-set show --name $diskEncryptionSetName --resource-group $diskEncryptionResourceGroup)

#Provide the subscription Id of the subscription where snapshot will be copied to
#If snapshot is copied to the same subscription then you can skip this step
targetSubscriptionId=6492b1f7-f219-446b-b509-314e17e1efb0

#Name of the resource group where snapshot will be copied to
targetResourceGroupName=mytargetResourceGroupName

#Set the context to the subscription Id where snapshot will be copied to
#If snapshot is copied to the same subscription then you can skip this step
az account set --subscription $targetSubscriptionId

#Copy snapshot to different subscription using the snapshot Id
#We recommend you to store your snapshots in Standard storage to reduce cost. Please use Standard_ZRS in regions where zone redundant storage (ZRS) is available, otherwise use Standard_LRS
#Please check out the availability of ZRS here: https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy-zrs#support-coverage-and-regional-availability
#To change the region, use the --location parameter
az snapshot create -g $targetResourceGroupName -n $snapshotName --source $snapshotId --disk-encryption-set $diskEncryptionSetID --sku Standard_LRS --encryption-type EncryptionAtRestWithCustomerKey
```

## Clean up resources

Run the following command to remove the resource group, VM, and all related resources.

```azurecli
az group delete --name mySourceResourceGroupName
```

## Sample reference

This script uses following commands to create a snapshot in the target subscription using the `Id` of the source snapshot. Each command in the table links to command specific documentation.

| Command | Notes |
| --- | --- |
| [az snapshot show](/en-us/cli/azure/snapshot) | Gets all the properties of a snapshot using the name and resource group properties of the snapshot. The `Id` property is used to copy the snapshot to different subscription. |
| [az snapshot create](/en-us/cli/azure/snapshot) | Copies a snapshot by creating a snapshot in different subscription using the `Id` and name of the parent snapshot. |