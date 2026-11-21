---
layout: Conceptual
title: Use CLI to deploy Azure Spot Virtual Machines - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/spot-cli
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
author: kaza-sriram
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: prkazasr
ms.update-cycle: 365-days
description: Learn how to use the CLI to deploy Azure Spot Virtual Machines to save costs.
ms.service: azure-virtual-machines
ms.subservice: azure-spot-vm
ms.custom: devx-track-azurecli, linux-related-content
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
locale: en-us
document_id: 6b3ac13a-41c6-761a-071d-efa8c8ef6a4c
document_version_independent_id: 71fd04b6-13c6-ddf1-bed0-250f3a96a874
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/linux/spot-cli.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli
toc_rel: ../toc.json
asset_id: virtual-machines/linux/spot-cli
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/linux/spot-cli.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 1b591f97-77f2-c771-85c6-4ff97dddfd79
---

# Use CLI to deploy Azure Spot Virtual Machines - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Flexible scale sets

By using [Azure Spot Virtual Machines](../spot-vms), you can take advantage of unused capacity at a significant cost savings. At any point in time when Azure needs the capacity back, the Azure infrastructure evicts Azure Spot Virtual Machines. Therefore, Azure Spot Virtual Machines are great for workloads that can handle interruptions like batch processing jobs, dev/test environments, large compute workloads, and more. [Spot Plus (Public Preview)](../spot-plus-public-preview-azure-compute-technical) is an enhanced tier of Azure Spot Virtual Machines for interruption-tolerant workloads. It's designed to deliver better runtimes and improved eviction and rebalance signals, while remaining evictable when Azure needs the capacity.

Pricing for Azure Spot Virtual Machines is variable, based on region and SKU. For more information, see VM pricing for [Linux](https://azure.microsoft.com/pricing/details/virtual-machines/linux/) and [Windows](https://azure.microsoft.com/pricing/details/virtual-machines/windows/).

You have the option to set a max price you're willing to pay, per hour, for the VM. The max price for an Azure Spot Virtual Machine can be set in US dollars (USD), using up to 5 decimal places. For example, the value `0.98765` is a max price of $0.98765 USD per hour. If you set the max price to be `-1`, the VM is evicted based on price. The price for the VM is the current price for Azure Spot Virtual Machine or the price for a standard VM, whichever is less, as long as there's capacity and quota available. For more information about setting the max price, see [Azure Spot Virtual Machines - Pricing](../spot-vms#pricing).

The process to create an Azure Spot Virtual Machine by using the Azure CLI is the same as detailed in the [quickstart article](quick-create-cli). Just add the `--priority Spot` or `--priority SpotPlus` parameter, set the `--eviction-policy` to either `Deallocate` (the default) or `Delete`, and provide a max price or `-1`.

## Install Azure CLI

To create Azure Spot Virtual Machines, you need to be running the Azure CLI version 2.0.74 or later. Run **az --version** to find the version. If you need to install or upgrade, see [Install the Azure CLI](/en-us/cli/azure/install-azure-cli).

Sign in to Azure using [az login](/en-us/cli/azure/reference-index#az-login).

```azurecli
az login
```

## Create an Azure Spot Virtual Machine

This example shows how to deploy a Linux Azure Spot Virtual Machine that isn't evicted based on price. For Spot Plus, change the priority parameter to `--priority SpotPlus`. Set the eviction policy to deallocate the VM, so that it can be restarted later. If you want to delete the VM and the underlying disk when the VM is evicted, set `--eviction-policy` to `Delete`.

```azurecli
az group create -n mySpotGroup -l eastus
az vm create \
    --resource-group mySpotGroup \
    --name myVM \
    --image Ubuntu2204 \
    --admin-username azureuser \
    --generate-ssh-keys \
    --priority Spot \
    --max-price -1 \--eviction-policy Deallocate
```

After the VM is created, you can query to see the max billing price for all of the VMs in the resource group.

```azurecli
az vm list \
   -g mySpotGroup \
   --query '[].{Name:name, MaxPrice:billingProfile.maxPrice}' \
   --output table
```

## Simulate an eviction

You can simulate an eviction of an Azure Spot Virtual Machine using REST, PowerShell, or the CLI, to test how well your application responds to a sudden eviction.

In most cases, you want to use the REST API [Virtual Machines - Simulate Eviction](/en-us/rest/api/compute/virtualmachines/simulateeviction) to help with automated testing of applications. For REST, a `Response Code: 204` means the simulated eviction was successful. You can combine simulated evictions with the [Scheduled Event service](scheduled-events), to automate how your app responds when the VM is evicted.

To see scheduled events in action, watch Azure Friday - [Using Azure Scheduled Events to prepare for VM maintenance](https://youtu.be/ApsoXLVg_0U).

### Quick test

For a quick test to show how a simulated eviction works, let's walk through querying the scheduled event service to see what it looks like when you simulate an eviction using the Azure CLI.

The Scheduled Event service is enabled for your service the first time you make a request for events.

Remote into your VM, and then open a command prompt.

From the command prompt on your VM, type:

```
curl -H Metadata:true http://169.254.169.254/metadata/scheduledevents?api-version=2019-08-01
```

This first response could take up to 2 minutes. From now on, they should display output almost immediately.

From a computer that has the Azure CLI installed (like your local machine), simulate an eviction using [az vm simulate-eviction](/en-us/cli/azure/vm#az-vm-simulate-eviction). Replace the resource group name and VM name with your own.

```azurecli
az vm simulate-eviction --resource-group mySpotRG --name mySpot
```

The response output has `Status: Succeeded` if the request was successfully made.

Quickly go back to your remote connection to your Spot Virtual Machine and query the Scheduled Events endpoint again. Repeat the following command until you get an output that contains more information:

```
curl -H Metadata:true http://169.254.169.254/metadata/scheduledevents?api-version=2019-08-01
```

When the Scheduled Event Service gets the eviction notification, you get a response that looks similar to the following output:

```output
{"DocumentIncarnation":1,"Events":[{"EventId":"A123BC45-1234-5678-AB90-ABCDEF123456","EventStatus":"Scheduled","EventType":"Preempt","ResourceType":"VirtualMachine","Resources":["myspotvm"],"NotBefore":"Tue, 16 Mar 2021 00:58:46 GMT","Description":"","EventSource":"Platform"}]}
```

You can see that `"EventType":"Preempt"`, and the resource is the VM resource `"Resources":["myspotvm"]`.

You can also see the VM's eviction condition by checking the `"NotBefore"` - the VM will not be evicted before the time given, so that is your window for your application to gracefully close out.