---
layout: Conceptual
title: Azure Dedicated Host SKU Retirement Modernization Guide - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/dedicated-hosts/modernization-guide
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
ms.reviewer: vamckMS
description: Walkthrough on how to modernize a retiring Dedicated Host SKU
author: mattmcinnes
ms.author: mattmcinnes
ms.service: azure-dedicated-host
ms.topic: how-to
ms.date: 2026-09-25T00:00:00.0000000Z
locale: en-us
document_id: d5bfc9e0-c512-6025-8d4d-dd4a942a9a17
document_version_independent_id: 31d2ddf5-adba-9ff1-ffd2-6011d958d4b7
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/dedicated-hosts/modernization-guide.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli,azurepowershell
toc_rel: ../toc.json
asset_id: virtual-machines/dedicated-hosts/modernization-guide
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/dedicated-hosts/modernization-guide.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a48df08f-c196-4114-998c-7d0528e51d7a
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7853f9c-f51c-437c-a7f2-85bda0416f2e
platformId: 776f70b1-bec2-f5b7-0a81-2ca8d48d82f1
---

# Azure Dedicated Host SKU Retirement Modernization Guide - Azure Virtual Machines | Microsoft Learn

Like standard virtual machine sizes, Dedicated Host SKUs follow a [hardware lifecycle](../sizes/lifecycle/lifecycle-overview). As the underlying hardware ages, older Dedicated Host SKUs are retired, and you need to modernize your workloads to newer, faster, and more efficient SKUs. Compared to older Dedicated Host SKUs, the recommended SKUs offer:

- Newer, more efficient processors
- Increased RAM
- Increased available vCPUs
- Greater regional capacity

Review the [FAQs](sku-lifecycle#faqs) before you get started on modernization. The next section will go over which Dedicated Host SKUs to modernize to help aid in modernization planning and execution.

## Retired host SKUs and recommended replacements

Note

No currently available Dedicated Host SKUs are planned for retirement. For retirement dates and the full list of retired Dedicated Host SKUs, see [Azure Dedicated Host SKU Lifecycle](sku-lifecycle#retired-and-retiring-dedicated-host-skus).

The following sections list the recommended replacements for retired Dedicated Host SKUs.

### Dsv3-Type1 and Dsv3-Type2

The retired Dsv3-Type1 and Dsv3-Type2 ran Dsv3-series VMs, which offer a combination of vCPU, memory, and temporary storage best suited for most general-purpose workloads. We recommend modernizing your existing VMs to one of the following Dedicated Host SKUs:

- Dsv3-Type3
- Dsv3-Type4

Neither the Dsv3-Type3 nor the Dsv3-Type4 is planned for retirement. We recommend moving to either the Dsv3-Type3 or Dsv3-Type4 based on regional availability, pricing, and your organization’s needs.

### Esv3-Type1 and Esv3-Type2

The retired Esv3-Type1 and Esv3-Type2 ran Esv3-series VMs, which offer a combination of vCPU, memory, and temporary storage best suited for most memory-intensive workloads. We recommend modernizing your existing VMs to one of the following Dedicated Host SKUs:

- Esv3-Type3
- Esv3-Type4

Neither the Esv3-Type3 nor the Esv3-Type4 is planned for retirement. We recommend moving to either the Esv3-Type3 or Esv3-Type4 based on regional availability, pricing, and your organization’s needs.

## Modernizing to supported hosts

To modernize your workloads and avoid Dedicated Host SKU retirement, follow the directions for your modernization method of choice.

### Automatic modernization (Resize)

Moving a host and all associated VMs to newer generation hardware can be done through the host resize feature. Resize simplifies the modernization process and avoids having to manually create new hosts and move all VMs individually.

Resize limitations:

- Host can only be resized to an ADH within the same VM family. A Dsv3-Type3 host can be resized to Dsv3-Type4 but **not** to an **E**sv3-Type4.
- You can only resize to newer generation of hardware. A Dsv3-Type3 host can be resized to Dsv3-Type4 but **not** Dsv3-Type2.
- Resizing changes the 'Host Asset ID'. The 'Host ID' remains the same.
- The host and all associated VMs become unavailable during the resize operation.

Warning

The resize operation causes the loss of any non-persistent data such as temp disk data. Save all your work to persistent data storage before triggering resize.

Note

If the source host is already running on the latest hardware, 'Size' page would display an empty list. If you're looking for enhanced performance, consider switching to a different VM family.

# [Portal](#tab/portal)
1. Search for and select the host.
2. In the left menu under **Settings**, select **Size**.
3. Once on the size page from the list of SKUs, select the desired SKU to resize to.
4. Selecting a target size from the list would enable **Resize** button on the bottom on the page.
5. Click **Resize**, host's 'Provisioning State' changes from 'Provisioning Succeeded' to 'Updating'
6. Once the resizing is complete, the host's 'Provisioning State' reverts to 'Provisioning Succeeded'

# [CLI](#tab/cli)
First list the sizes that you can resize in case you're unsure which to resize to.

Use [az vm host list-resize-options](/en-us/cli/azure/vm#az-vm-host-list-resize-options).

```azurecli
az vm host list-resize-options \
 --host-group myHostGroup \
 --host-name myHost \
 --resource-group myResourceGroup
```

Resize the host using [az vm host resize](/en-us/cli/azure/vm#az-vm-host-resize) .

```azurecli
az vm host resize \
 --host-group myHostGroup \
 --host-name myHost \
 --resource-group myResourceGroup \
 --sku Dsv3-Type4
```

# [PowerShell](#tab/powershell)
When using PowerShell, the resize feature is referred to as a host 'Update'. Use the following commands to update the host:

```azurepowershell
Update-AzHost
      [-ResourceGroupName] <String>
      [-HostGroupName] <String>
      [-Name] <String>
      [-Sku <String>]
      [-AutoReplaceOnFailure <Boolean>]
      [-LicenseType <DedicatedHostLicenseTypes>]
      [-DefaultProfile <IAzureContextContainer>]
      [-WhatIf]
      [-Confirm]
      [<CommonParameters>]
```

For more info on Update-AzHost, check out the [Update-AzHost reference docs](/en-us/powershell/module/az.compute/update-azhost).

---

### Manual modernization

This includes steps for manually placed VMs, automatically placed VMs, and virtual machine scale sets on your Dedicated Hosts:

# [Manually Placed VMs](#tab/manualVM)
1. Choose a target Dedicated Host SKU to modernize to.
2. Ensure you have quota for the VM family associated with the target Dedicated Host SKU in your given region.
3. Provision a new Dedicated Host of the target Dedicated Host SKU in the same Host Group.
4. Stop and deallocate the VM(s) on your old Dedicated Host.
5. Reassign the VM(s) to the target Dedicated Host.
6. Start the VM(s).
7. Delete the old host.

# [Automatically Placed VMs](#tab/autoVM)
1. Choose a target Dedicated Host SKU to modernize to.
2. Ensure you have quota for the VM family associated with the target Dedicated Host SKU in your given region.
3. Provision a new Dedicated Host of the target Dedicated Host SKU in the same Host Group.
4. Stop and deallocate the VM(s) on your old Dedicated Host.
5. Delete the old Dedicated Host.
6. Start the VM(s).

# [Virtual Machine Scale Sets](#tab/VMSS)
1. Choose a target Dedicated Host SKU to modernize to.
2. Ensure you have quota for the VM family associated with the target Dedicated Host SKU in your given region.
3. Provision a new Dedicated Host of the target Dedicated Host SKU in the same Host Group.
4. Stop the virtual machine scale set on your old Dedicated Host.
5. Delete the old Dedicated Host.
6. Start the virtual machine scale set.

---

More detailed instructions can be found in the following sections.

Note

**Certain sections are different for automatically placed VMs or virtual machine scale set**. These differences will explicitly be called out in the respective steps.

#### Ensure quota for the target VM family

Be sure that you have enough vCPU quota for the VM family of the Dedicated Host SKU that you'll be using. If you need quota, follow this guide to [request an increase in vCPU quota](/en-us/azure/azure-portal/supportability/per-vm-quota-requests) for your target VM family in your target region. Select the Dsv3-series or Esv3-series as the VM family, depending on the target Dedicated Host SKU.

#### Create a new Dedicated Host

Within the same Host Group as the existing Dedicated Host, [create a Dedicated Host](how-to#create-a-dedicated-host) of the target Dedicated Host SKU.

#### Stop the VM(s) or virtual machine scale set

# [PowerShell](#tab/PS)
Refer to the PowerShell documentation to [stop a VM through PowerShell](/en-us/powershell/module/az.compute/stop-azvm) or [stop a virtual machine scale set through PowerShell](/en-us/powershell/module/az.compute/stop-azvmss).

# [CLI](#tab/CLI)
Refer to the Command Line Interface (CLI) documentation to [stop a VM through CLI](/en-us/cli/azure/vm#az-vm-stop) or [stop a virtual machine scale set through CLI](/en-us/cli/azure/vmss#az-vmss-stop).

# [Portal](#tab/Portal)
On Azure portal, go through the following steps:

1. Navigate to your VM or virtual machine scale set.
2. On the top navigation bar, click “Stop”.

---

#### Reassign the VM(s) to the target Dedicated Host

Note

**Skip this step for automatically placed VMs and virtual machine scale set.**

Once the target Dedicated Host has been created and the VM has been stopped, [reassign the VM to the target Dedicated Host](how-to#reassign-an-existing-vm).

#### Start the VM(s) or virtual machine scale set

Note

**Automatically placed VM(s) and virtual machine scale set require that you delete the old host *before* starting the autoplaced VM(s) or virtual machine scale set.**

# [PowerShell](#tab/PS)
Refer to the PowerShell documentation to [start a VM through PowerShell](/en-us/powershell/module/az.compute/start-azvm) or [start a virtual machine scale set through PowerShell](/en-us/powershell/module/az.compute/start-azvmss).

# [CLI](#tab/CLI)
Refer to the Command Line Interface (CLI) documentation to [start a VM through CLI](/en-us/cli/azure/vm#az-vm-start) or [start a virtual machine scale set through CLI](/en-us/cli/azure/vmss#az-vmss-start).

# [Portal](#tab/Portal)
On Azure portal, go through the following steps:

1. Navigate to your VM or virtual machine scale set.
2. On the top navigation bar, click “Start”.

---

#### Delete the old Dedicated Host

Once all VMs have been moved from your old Dedicated Host to the target Dedicated Host, [delete the old Dedicated Host](how-to#deleting-a-host).

## Help and support

If you have questions, ask community experts in [Microsoft Q&A](/en-us/answers/topics/azure-dedicated-host.html).