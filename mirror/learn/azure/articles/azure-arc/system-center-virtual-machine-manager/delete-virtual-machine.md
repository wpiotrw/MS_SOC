---
layout: Conceptual
title: Delete a SCVMM-managed VM in Azure through Azure Arc-enabled System Center Virtual Machine Manager - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/delete-virtual-machine
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: Jeronika-MS
learn_banner_products:
- azure
ms.author: v-gajeronika
ms.service: azure-arc
description: In this article, you learn how to delete a SCVMM-managed virtual machine and its Azure resource through Azure Arc enabled SCVMM.
ms.topic: how-to
ms.date: 2026-09-24T00:00:00.0000000Z
ms.subservice: azure-arc-scvmm
ms.reviewer: v-gajeronika
locale: en-us
document_id: d5788730-6612-0d21-e5ea-1183c42738ca
document_version_independent_id: d0fcbc86-df5a-7915-7da3-8c3d1878ce10
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/system-center-virtual-machine-manager/delete-virtual-machine.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/system-center-virtual-machine-manager/delete-virtual-machine
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/system-center-virtual-machine-manager/delete-virtual-machine.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/c89972e1-0a93-4ce3-b588-9c24d08ca424
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/b2144970-2aee-47fb-9df2-af491ca710ec
platformId: 72ca20e3-adbe-b0eb-c328-fc666194f9ea
---

# Delete a SCVMM-managed VM in Azure through Azure Arc-enabled System Center Virtual Machine Manager - Azure Arc | Microsoft Learn

Note

Azure Arc-enabled SCVMM retires in September 2029. If you're using Azure Arc-enabled SCVMM, transition to [Azure Arc-enabled Servers](/en-us/azure/azure-arc/servers/overview) or contact arc-vmm-feedback@microsoft.com. For more information, see the [transition guidance](transition-guidance).

In this article, you learn how to delete a SCVMM-managed virtual machine and its Azure resource through Azure Arc-enabled SCVMM.

## Prerequisites

Before you delete a virtual machine or remove its Azure resource, make sure that you meet the following prerequisites:

- The SCVMM management server manages the VM that you want to delete from the host or remove its Azure resource. The server is in a *Connected* state, and its associated Azure Arc resource bridge is in a *Running* state.
- The VM that you want to delete from the host or remove its Azure resource is [enabled for management in Azure](enable-scvmm-inventory-resources).
- If the VM that you want to delete from the host or remove its Azure resource has the Arc agent installed (guest management enabled), [uninstall the agent and remove any VM extensions](/en-us/azure/azure-arc/servers/manage-agent?toc=%2Fazure%2Fazure-arc%2Fsystem-center-virtual-machine-manager%2Ftoc.json&amp;tabs=windows#uninstall-the-agent) to prevent billing beyond the lifetime of the VM.
- *Azure Arc SCVMM VM Contributor* role or a custom Azure role with permissions to delete the SCVMM VMs that you want to delete.

## Delete a virtual machine

Important

- This operation also deletes the VM on your SCVMM managed on-premises host. To remove the machine from Azure only and keep the on-premises resources intact, perform the Remove from Azure instead.
- Before you delete a VM, ensure all the critical data is backed up, the VM owner is informed, and all dependencies and services regarding the VM are considered.

To delete a VM, follow these steps:

1. Sign in to the [Azure portal](https://portal.azure.com/), go to **Azure Arc** &gt; **SCVMM management server**, and then select the SCVMM server that manages the VM you want to delete from Azure.
2. Go to the dedicated **Virtual machines** inventory view under the SCVMM inventory. Alternatively, you can go to the inventory view for VMs enabled for management in Azure from **Azure Arc** &gt; **Machines** blade.
3. Select the machine you want to delete and then select **Delete**.

    [![Screenshot showing delete VM option.](media/delete-virtual-machine/delete-virtual-machine.png)](media/delete-virtual-machine/delete-virtual-machine.png#lightbox)

    When prompted, confirm that you want to delete the VM.

    [![Screenshot showing Delete screen.](media/delete-virtual-machine/delete.png)](media/delete-virtual-machine/delete.png#lightbox)

## Remove a virtual machine from Azure only

To remove a VM from Azure only, follow these steps:

1. Sign in to the [Azure portal](https://portal.azure.com/), go to **Azure Arc** &gt; **SCVMM management server**, and then select the SCVMM server that manages the VM you want to operate from Azure.
2. Go to the dedicated **Virtual machines** inventory view under the SCVMM inventory. Select the machine for which you want to remove the Azure representation and then select **Remove from Azure**.

    [![Screenshot showing Virtual machines screen.](media/delete-virtual-machine/remove-from-azure.png)](media/delete-virtual-machine/remove-from-azure.png#lightbox)

    When prompted, confirm that you want to remove the Azure representation of the VM.

You can track the progress of the Azure operations from the Azure [activity log](https://portal.azure.com/#view/Microsoft_Azure_ActivityLog/ActivityLogBlade).