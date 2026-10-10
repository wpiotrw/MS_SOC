---
layout: Conceptual
title: Deploy Azure dedicated hosts - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/dedicated-hosts/how-to
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
description: Deploy VMs and scale sets to dedicated hosts.
author: mattmcinnes
ms.author: mattmcinnes
ms.service: azure-dedicated-host
ms.topic: how-to
ms.custom: devx-track-azurepowershell, devx-track-azurecli, portal
ms.update-cycle: 180-days
ms.date: 2026-09-25T00:00:00.0000000Z
locale: en-us
document_id: e5f875ed-eee6-c56e-4533-35aed7f633fb
document_version_independent_id: ab279753-f864-54ac-1439-6f87e9f1b99d
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/dedicated-hosts/how-to.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli,azurepowershell
toc_rel: ../toc.json
asset_id: virtual-machines/dedicated-hosts/how-to
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/dedicated-hosts/how-to.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a48df08f-c196-4114-998c-7d0528e51d7a
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7853f9c-f51c-437c-a7f2-85bda0416f2e
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: f1a2ab22-0c1c-6591-7da4-984bd34c4b39
---

# Deploy Azure dedicated hosts - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Uniform scale sets

This article guides you through how to create an Azure [dedicated host](overview) to host your virtual machines (VMs) and scale set instances.

## Limitations

- The sizes and hardware types available for dedicated hosts vary by region. Refer to the host [pricing page](https://aka.ms/ADHPricing) to learn more.
- Not all Azure VM SKUs, regions and availability zones support Ultra Disks, for more information about this topic, see [Azure Ultra Disks](../disks-enable-ultra-ssd).
- Additional [limitations](overview#ultra-disk-support-for-virtual-machines-on-dedicated-hosts) would apply when using Ultra Disks on the following VM sizes: LSv2, M, Mv2, Msv2, Mdsv2, NVv3, NVv4 on a dedicated host.
- The fault domain count of the virtual machine scale set can't exceed the fault domain count of the host group.
- Users can not select hardware capabilities like accelerated networking when creating a dedicated host.
- Users would not be able to create VMs/VMSS with accelerated networking enabled on a dedicated host.

## Create a host group

A **host group** is a resource that represents a collection of dedicated hosts. You create a host group in a region and an availability zone, and add hosts to it. You can use one or both of the following options with your dedicated hosts to ensure high availability:

- Span across multiple availability zones. In this case, you're required to have a host group in each of the zones you wish to use.
- Span across multiple fault domains, which are mapped to physical racks.

In either case, you need to provide the fault domain count for your host group. If you don't want to span fault domains in your group, use a fault domain count of 1.

You can also decide to use both availability zones and fault domains.

Enabling Ultra Disks is a host group level setting and can't be changed after a host group is created.

# [Portal](#tab/portal)
In this example, we'll create a host group using one availability zone and two fault domains.

1. Open the Azure [portal](https://portal.azure.com).
2. Select **Create a resource** in the upper left corner.
3. Search for **Host group** and then select **Host Groups** from the results.
4. In the **Host Groups** page, select **Create**.
5. Select the subscription you would like to use, and then select **Create new** to create a new resource group.
6. Type *myDedicatedHostsRG* as the **Name** and then select **OK**.
7. For **Host group name**, type *myHostGroup*.
8. For **Location**, select **East US**.
9. For **Availability Zone**, select **1**.
10. Select **Enable Ultra Disk** to use Ultra Disks with supported Virtual Machines.
11. For **Fault domain count**, select **2**.
12. Select **Automatic placement** to automatically assign VMs and scale set instances to an available host in this group.
13. Select **Review + create** and then wait for validation.
14. Once you see the **Validation passed** message, select **Create** to create the host group.

It should only take a few moments to create the host group.

# [CLI](#tab/cli)
Not all host SKUs are available in all regions, and availability zones. You can list host availability, and any offer restrictions before you start provisioning dedicated hosts.

```azurecli
az vm list-skus -l eastus2  -r hostGroups/hosts  -o table
```

You can also verify if a VM series supports Ultra Disks.

```azurecli
subscription="<mySubID>"
# example value is southeastasia
region="<myLocation>"
# example value is Standard_E64s_v3
vmSize="<myVMSize>"

az vm list-skus --resource-type virtualMachines  --location $region --query "[?name=='$vmSize'].locationInfo[0].zoneDetails[0].Name" --subscription $subscription
```

In this example, we'll use [az vm host group create](/en-us/cli/azure/vm/host/group#az-vm-host-group-create) to create a host group using both availability zones and fault domains.

```azurecli
az vm host group create \
   --name myHostGroup \
   -g myDHResourceGroup \
   -z 1 \
   --platform-fault-domain-count 2
```

Add the `--automatic-placement true` parameter to have your VMs and scale set instances automatically placed on hosts, within a host group. For more information, see [Manual vs. automatic placement](overview#manual-vs-automatic-placement).

Add the `--ultra-ssd-enabled true` parameter to enable creation of VMs that can support Ultra Disks.

**Other examples**

You can also use [az vm host group create](/en-us/cli/azure/vm/host/group#az-vm-host-group-create) to create a host group in availability zone 1 (and no fault domains).

```azurecli
az vm host group create \
   --name myAZHostGroup \
   -g myDHResourceGroup \
   -z 1 \
   --platform-fault-domain-count 1
```

The following code snippet uses [az vm host group create](/en-us/cli/azure/vm/host/group#az-vm-host-group-create) to create a host group by using fault domains only (to be used in regions where availability zones aren't supported).

```azurecli
az vm host group create \
   --name myFDHostGroup \
   -g myDHResourceGroup \
   --platform-fault-domain-count 2
```

The following code snippet uses [az vm host group create](/en-us/cli/azure/vm/host/group#az-vm-host-group-create) to create a host group that supports Ultra Disks and auto placement of VMs enabled.

```azurecli
az vm host group create \
   --name myFDHostGroup \
   -g myDHResourceGroup \
   -z 1 \
   --ultra-ssd-enabled true \
   --platform-fault-domain-count 2 \
   --automatic-placement true
```

# [PowerShell](#tab/powershell)
This example uses [New-AzHostGroup](/en-us/powershell/module/az.compute/new-azhostgroup) to create a host group in zone 1, with 2 fault domains.

```azurepowershell
$rgName = "myDHResourceGroup"
$location = "EastUS"

New-AzResourceGroup -Location $location -Name $rgName
$hostGroup = New-AzHostGroup `
   -Name myHostGroup `
   -ResourceGroupName $rgName `
   -Location $location `
   -Zone 1 `
   -EnableUltraSSD `
   -PlatformFaultDomain 2 `
   -SupportAutomaticPlacement true
```

Add the `-SupportAutomaticPlacement true` parameter to have your VMs and scale set instances automatically placed on hosts, within a host group. For more information about this topic, see [Manual vs. automatic placement](overview#manual-vs-automatic-placement).

Add the `-EnableUltraSSD` parameter to enable creation of VMs that can support Ultra Disks.

---

## Create a dedicated host

Now create a dedicated host in the host group. In addition to a name for the host, you're required to provide the SKU for the host. Host SKU captures the supported VM series and the hardware generation for your dedicated host.

For more information about the host SKUs and pricing, see [Azure Dedicated Host pricing](https://aka.ms/ADHPricing).

If you set a fault domain count for your host group, you'll need to specify the fault domain for your host.

# [Portal](#tab/portal)
1. Select **Create a resource** in the upper left corner.
2. Search for **Dedicated host** and then select **Dedicated hosts** from the results.
3. In the **Dedicated Hosts** page, select **Create**.
4. Select the subscription you would like to use.
5. Select *myDedicatedHostsRG* as the **Resource group**.
6. In **Instance details**, type *myHost* for the **Name** and select *East US* for the location.
7. In **Hardware profile**, select *Standard Es3 family - Type 1* for the **Size family**, select *myHostGroup* for the **Host group** and then select *1* for the **Fault domain**. Leave the defaults for the rest of the fields.
8. Leave the **Automatically replace host on failure** setting *Enabled* to automatically service heal the host in case of any host level failure.
9. When you're done, select **Review + create** and wait for validation.
10. Once you see the **Validation passed** message, select **Create** to create the host.

# [CLI](#tab/cli)
Use [az vm host create](/en-us/cli/azure/vm/host#az-vm-host-create) to create a host. If you set a fault domain count for your host group, you'll be asked to specify the fault domain for your host.

```azurecli
az vm host create \
   --host-group myHostGroup \
   --name myHost \
   --sku DSv3-Type1 \
   --platform-fault-domain 1 \
   --auto-replace true \
   -g myDHResourceGroup
```

# [PowerShell](#tab/powershell)
In this example, we use [New-AzHost](/en-us/powershell/module/az.compute/new-azhost) to create a host and set the fault domain to 1.

```azurepowershell
$dHost = New-AzHost `
   -HostGroupName $hostGroup.Name `
   -Location $location -Name myHost `
   -ResourceGroupName $rgName `
   -Sku DSv3-Type1 `
   -AutoReplaceOnFailure True `
   -PlatformFaultDomain 1
```

---

## Create a VM

Now create a VM on the host.

To create a VM with Ultra Disk support, ensure the host group where you place the VM is Ultra Disk enabled. After you confirm this feature, create the VM in the same host group. For steps to attach an Ultra Disk to a VM, see [Deploy a VM with an Ultra Disk](../disks-enable-ultra-ssd#deploy-a-vm-with-an-ultra-disk).

# [Portal](#tab/portal)
1. Choose **Create a resource** in the upper left corner of the Azure portal.
2. In the search box above the list of Azure Marketplace resources, search for and select the image you want use, then choose **Create**.
3. In the **Basics** tab, under **Project details**, make sure the correct subscription is selected and then select *myDedicatedHostsRG* as the **Resource group**.
4. Under **Instance details**, type *myVM* for the **Virtual machine name** and choose *East US* for your **Location**.
5. In **Availability options** select **Availability zone**, select *1* from the drop-down.
6. For the size, select **Change size**. In the list of available sizes, choose one from the Esv3 series, like **Standard E2s v3**. You may need to clear the filter in order to see all of the available sizes.
7. Complete the rest of the fields on the **Basics** tab as needed.
8. If you want to specify which host to use for your VM, then at the top of the page, select the **Advanced** tab and in the **Host** section, select *myHostGroup* for **Host group** and *myHost* for the **Host**. Otherwise, your VM will automatically be placed on a host with capacity. ![Select host group and host](media/dedicated-hosts-portal/advanced.png)
9. Leave the remaining defaults and then select the **Review + create** button at the bottom of the page.
10. When you see the message that validation has passed, select **Create**.

It will take a few minutes for your VM to be deployed.

# [CLI](#tab/cli)
Create a virtual machine within a dedicated host using [az vm create](/en-us/cli/azure/vm#az-vm-create). If you specified an availability zone when creating your host group, you're required to use the same zone when creating the virtual machine. Replace the values like image and host name with your own. If you're creating a Windows VM, remove `--generate-ssh-keys` to be prompted for a password.

```azurecli
az vm create \
   -n myVM \
   --image myImage \
   --host-group myHostGroup \
   --admin-username azureuser \
   --generate-ssh-keys \
   --size Standard_D4s_v3 \
   -g myDHResourceGroup \
   --zone 1
```

To place the VM on a specific host, use `--host` instead of specifying the host group with `--host-group`.

Warning

If you create a virtual machine on a host which does not have enough resources, the virtual machine will be created in a FAILED state.

# [PowerShell](#tab/powershell)
Create a new VM on our host using [New-AzVM](/en-us/powershell/module/az.compute/new-azvm) For this example, because our host group is in zone 1, we need to create the VM in zone 1.

```azurepowershell
New-AzVM `
   -Credential $cred `
   -ResourceGroupName $rgName `
   -Location $location `
   -Name myVM `
   -HostId $dhost.Id `
   -Image myImage `
   -Zone 1 `
   -Size Standard_D4s_v3
```

Warning

If you create a virtual machine on a host which does not have enough resources, the virtual machine will be created in a FAILED state.

---

## Create a scale set

You can also create a scale set on your host.

Important

Starting November 2023, VM scale sets created using PowerShell and Azure CLI will default to Flexible Orchestration Mode if no orchestration mode is specified. For more information about this change and what actions you should take, go to [Breaking Change for VMSS PowerShell/CLI Customers - Microsoft Community Hub](https://techcommunity.microsoft.com/t5/azure-compute-blog/breaking-change-for-vmss-powershell-cli-customers/ba-p/3818295)

# [Portal](#tab/portal)
When you deploy a scale set, you specify the host group.

1. Search for *Scale set* and select **Virtual machine scale sets** from the list.
2. Select **Add** to create a new scale set.
3. Complete the fields on the **Basics** tab as you usually would, but make sure you select a VM size that is from the series you chose for your dedicated host, like **Standard E2s v3**.
4. On the **Advanced** tab, for **Spreading algorithm** select **Max spreading**.
5. In **Host group**, select the host group from the drop-down. If you recently created the group, it might take a minute to get added to the list.

# [CLI](#tab/cli)
When you deploy a scale set using [az vmss create](/en-us/cli/azure/vmss#az-vmss-create), you specify the host group using `--host-group`. In this example, we're deploying a Linux image. To deploy a Windows image, replace the value of `--image` and remove `--generate-ssh-keys` to be prompted for a password.

```azurecli
az vmss create \
  --resource-group myResourceGroup \
  --name myScaleSet \
  --image myImage \
  --orchestration-mode uniform \
  --upgrade-policy-mode automatic \
  --admin-username azureuser \
  --host-group myHostGroup \
  --generate-ssh-keys \
  --size Standard_D4s_v3 \
  -g myDHResourceGroup \
  --zone 1
```

If you want to manually choose which host to deploy the scale set to, add `--host` and the name of the host.

# [PowerShell](#tab/powershell)
Deploy a scale-set to the host using [New-AzVMSS](/en-us/powershell/module/az.compute/new-azvmss). When you deploy a scale set, you specify the host group.

```azurepowershell
New-AzVmss `
  -ResourceGroupName "myResourceGroup" `
  -Location "EastUS" `
  -VMScaleSetName "myDHScaleSet" `
  -VirtualNetworkName "myVnet" `
  -SubnetName "mySubnet" `
  -PublicIpAddressName "myPublicIPAddress" `
  -LoadBalancerName "myLoadBalancer" `
  -OrchestrationMode 'Uniform' `
  -UpgradePolicyMode "Automatic"`
  -HostGroupId $hostGroup.Id
```

If you want to manually choose which host to deploy the scale set to, add `--host` and the name of the host.

---

## Reassign an existing VM

You can reassign an existing multitenant VM or dedicated host VM to a different dedicated host, but the VM must first be Stop\Deallocated. Before you move a VM to a dedicated host, make sure that the VM configuration is supported:

- The VM size must be in the same size family as the dedicated host. For example, if your dedicated host is DSv3, then the VM size could be Standard\_D4s\_v3, but it couldn't be a Standard\_A4\_v2.
- The VM needs to be located in same region as the dedicated host.
- The VM can't be part of a proximity placement group. Remove the VM from the proximity placement group before moving it to a dedicated host. For more information about this topic, see [Move a VM out of a proximity placement group](../windows/proximity-placement-groups#move-an-existing-vm-out-of-a-proximity-placement-group).
- The VM can't be in an availability set.
- If the VM is in an availability zone, it must be the same availability zone as the host group. The availability zone settings for the VM and the host group must match.

# [Portal](#tab/portal)
Move the VM to a dedicated host using the [portal](https://portal.azure.com).

1. Open the page for the VM.
2. Select **Stop** to stop\deallocate the VM.
3. Select **Configuration** from the left menu.
4. Select a host group and a host from the drop-down menus.
5. When you're done, select **Save** at the top of the page.
6. After the VM has been added to the host, select **Overview** from the left menu.
7. At the top of the page, select **Start** to restart the VM.

# [CLI](#tab/cli)
Move the existing VM to a dedicated host using the CLI. The VM must be Stop/Deallocated using [az vm deallocate](/en-us/cli/azure/vm#az_vm_stop) in order to assign it to a dedicated host.

Replace the values with your own information.

```azurecli
az vm deallocate -n myVM -g myResourceGroup
az vm update - n myVM -g myResourceGroup --host myHost
az vm start -n myVM -g myResourceGroup
```

For automatically placed VMs, only update the host group. For more information about this topic, see [Manual vs. automatic placement](overview#manual-vs-automatic-placement).

Replace the values with your own information.

```azurecli
az vm deallocate -n myVM -g myResourceGroup
az vm update -n myVM -g myResourceGroup --host-group myHostGroup
az vm start -n myVM -g myResourceGroup
```

# [PowerShell](#tab/powershell)
Replace the values of the variables with your own information.

```azurepowershell
$vmRGName = "movetohost"
$vmName = "myVMtoHost"
$dhRGName = "myDHResourceGroup"
$dhGroupName = "myHostGroup"
$dhName = "myHost"

$myDH = Get-AzHost `
   -HostGroupName $dhGroupName `
   -ResourceGroupName $dhRGName `
   -Name $dhName

$myVM = Get-AzVM `
   -ResourceGroupName $vmRGName `
   -Name $vmName

$myVM.Host = New-Object Microsoft.Azure.Management.Compute.Models.SubResource

$myVM.Host.Id = "$myDH.Id"

Stop-AzVM `
   -ResourceGroupName $vmRGName `
   -Name $vmName -Force

Update-AzVM `
   -ResourceGroupName $vmRGName `
   -VM $myVM -Debug

Start-AzVM `
   -ResourceGroupName $vmRGName `
   -Name $vmName
```

---

## Move a VM from dedicated host to multitenant infrastructure

You can move a VM that is running on a dedicated host to multitenant infrastructure, but the VM must first be Stop\Deallocated.

- Make sure that your subscription has sufficient vCPU quota for the VM in the region where
- Your multitenant VM will be scheduled in the same region and zone as the dedicated host

# [Portal](#tab/portal)
Move a VM from dedicated host to multitenant infrastructure using the [portal](https://portal.azure.com).

1. Open the page for the VM.
2. Select **Stop** to stop\deallocate the VM.
3. Select **Configuration** from the left menu.
4. Select **None** under host group drop-down menu.
5. When you're done, select **Save** at the top of the page.
6. After the VM has been reconfigured as a multitenant VM, select **Overview** from the left menu.
7. At the top of the page, select **Start** to restart the VM.

# [CLI](#tab/cli)
Move a VM from dedicated host to multitenant infrastructure using the CLI. The VM must be Stop/Deallocated using [az vm deallocate](/en-us/cli/azure/vm#az_vm_stop) in order to assign it to reconfigure it as a multitenant VM.

Replace the values with your own information.

```azurecli
az vm deallocate -n myVM -g myResourceGroup
az vm update -n myVM -g myResourceGroup --set host.id=None
az vm start -n myVM -g myResourceGroup
```

# [PowerShell](#tab/powershell)
Move a VM from dedicated host to multitenant infrastructure using the PowerShell.

Replace the values of the variables with your own information.

```azurepowershell
$vmRGName = "moveoffhost"
$vmName = "myDHVM"
$dhRGName = "myDHResourceGroup"
$dhGroupName = "myHostGroup"
$dhName = "myHost"

$myDH = Get-AzHost `
   -HostGroupName $dhGroupName `
   -ResourceGroupName $dhRGName `
   -Name $dhName

$myVM = Get-AzVM `
   -ResourceGroupName $vmRGName `
   -Name $vmName

Stop-AzVM `
   -ResourceGroupName $vmRGName `
   -Name $vmName -Force

Update-AzVM `
   -ResourceGroupName $vmRGName `
   -VM $myVM `
   -HostId ''

Start-AzVM `
   -ResourceGroupName $vmRGName `
   -Name $vmName
```

---

## Check the status of the host

If you need to know how much capacity is still available on a how, you can check the status.

# [Portal](#tab/portal)
1. Search for and select the host.
2. In the **Overview** page for the host, scroll down to see the list of sizes still available for the host. It should look similar to:

![Check the available capacity of the host from the overview page for the host.](media/dedicated-hosts-portal/host-status.png)

# [CLI](#tab/cli)
You can check the host health status and how many virtual machines you can still deploy to the host using [az vm host get-instance-view](/en-us/cli/azure/vm/host#az-vm-host-get-instance-view).

```azurecli
az vm host get-instance-view \
   -g myDHResourceGroup \
   --host-group myHostGroup \
   --name myHost
```

The output will look similar to the below example:

```json
{
  "autoReplaceOnFailure": true,
  "hostId": "6de80643-0f45-4e94-9a4c-c49d5c777b62",
  "id": "/subscriptions/10101010-1010-1010-1010-101010101010/resourceGroups/myDHResourceGroup/providers/Microsoft.Compute/hostGroups/myHostGroup/hosts/myHost",
  "instanceView": {
    "assetId": "12345678-1234-1234-abcd-abc123456789",
    "availableCapacity": {
      "allocatableVms": [
        {
          "count": 31.0,
          "vmSize": "Standard_D2s_v3"
        },
        {
          "count": 15.0,
          "vmSize": "Standard_D4s_v3"
        },
        {
          "count": 7.0,
          "vmSize": "Standard_D8s_v3"
        },
        {
          "count": 3.0,
          "vmSize": "Standard_D16s_v3"
        },
        {
          "count": 1.0,
          "vmSize": "Standard_D32-8s_v3"
        },
        {
          "count": 1.0,
          "vmSize": "Standard_D32-16s_v3"
        },
        {
          "count": 1.0,
          "vmSize": "Standard_D32s_v3"
        },
        {
          "count": 1.0,
          "vmSize": "Standard_D48s_v3"
        },
        {
          "count": 0.0,
          "vmSize": "Standard_D64-16s_v3"
        },
        {
          "count": 0.0,
          "vmSize": "Standard_D64-32s_v3"
        },
        {
          "count": 0.0,
          "vmSize": "Standard_D64s_v3"
        }
      ]
    },
    "statuses": [
      {
        "code": "ProvisioningState/succeeded",
        "displayStatus": "Provisioning succeeded",
        "level": "Info",
        "message": null,
        "time": "2019-07-24T21:22:40.604754+00:00"
      },
      {
        "code": "HealthState/available",
        "displayStatus": "Host available",
        "level": "Info",
        "message": null,
        "time": null
      }
    ]
  },
  "licenseType": null,
  "location": "eastus2",
  "name": "myHost",
  "platformFaultDomain": 1,
  "provisioningState": "Succeeded",
  "provisioningTime": "2019-07-24T21:22:40.604754+00:00",
  "resourceGroup": "myDHResourceGroup",
  "sku": {
    "capacity": null,
    "name": "DSv3-Type1",
    "tier": null
  },
  "tags": null,
  "type": null,
  "virtualMachines": [
    {
      "id": "/subscriptions/10101010-1010-1010-1010-101010101010/resourceGroups/MYDHRESOURCEGROUP/providers/Microsoft.Compute/virtualMachines/MYVM",
      "resourceGroup": "MYDHRESOURCEGROUP"
    }
  ]
}

```

# [PowerShell](#tab/powershell)
You can check the host health status and how many virtual machines you can still deploy to the host using [Get-AzHost](/en-us/powershell/module/az.compute/get-azhost) with the `-InstanceView` parameter.

```azurepowershell
Get-AzHost `
   -ResourceGroupName $rgName `
   -Name myHost `
   -HostGroupName $hostGroup.Name `
   -InstanceView
```

The output will look similar to the below example:

```
ResourceGroupName      : myDHResourceGroup
PlatformFaultDomain    : 1
AutoReplaceOnFailure   : True
HostId                 : 12345678-1234-1234-abcd-abc123456789
ProvisioningTime       : 7/28/2019 5:31:01 PM
ProvisioningState      : Succeeded
InstanceView           :
  AssetId              : abc45678-abcd-1234-abcd-123456789abc
  AvailableCapacity    :
    AllocatableVMs[0]  :
      VmSize           : Standard_D2s_v3
      Count            : 32
    AllocatableVMs[1]  :
      VmSize           : Standard_D4s_v3
      Count            : 16
    AllocatableVMs[2]  :
      VmSize           : Standard_D8s_v3
      Count            : 8
    AllocatableVMs[3]  :
      VmSize           : Standard_D16s_v3
      Count            : 4
    AllocatableVMs[4]  :
      VmSize           : Standard_D32-8s_v3
      Count            : 2
    AllocatableVMs[5]  :
      VmSize           : Standard_D32-16s_v3
      Count            : 2
    AllocatableVMs[6]  :
      VmSize           : Standard_D32s_v3
      Count            : 2
    AllocatableVMs[7]  :
      VmSize           : Standard_D64-16s_v3
      Count            : 1
    AllocatableVMs[8]  :
      VmSize           : Standard_D64-32s_v3
      Count            : 1
    AllocatableVMs[9]  :
      VmSize           : Standard_D64s_v3
      Count            : 1
  Statuses[0]          :
    Code               : ProvisioningState/succeeded
    Level              : Info
    DisplayStatus      : Provisioning succeeded
    Time               : 7/28/2019 5:31:01 PM
  Statuses[1]          :
    Code               : HealthState/available
    Level              : Info
    DisplayStatus      : Host available
Sku                    :
  Name                 : DSv3-Type1
Id                     : /subscriptions/10101010-1010-1010-1010-101010101010/re
sourceGroups/myDHResourceGroup/providers/Microsoft.Compute/hostGroups/myHostGroup/hosts
/myHost
Name                   : myHost
Location               : eastus
Tags                   : {}
```

---

## Restart a host

Restarting a host does not completely power off the host. When the host restarts, the underlying VMs will also restart. The host will remain on the same underlying physical hardware and both the host ID and asset ID will remain the same after the restart. The host SKU will also remain the same after the restart.

# [Portal](#tab/portal)
1. Search for and select the host.
2. In the top menu bar, select the **Restart** button.
3. In the **Essentials** section of the Host Resource Pane, Host Status will switch to **Host undergoing restart** during the restart.
4. Once the restart has completed, the Host Status will return to **Host available**.

# [CLI](#tab/cli)
Restart the host using [az vm host restart](/en-us/cli/azure/vm#az-vm-host-restart).

```azurecli
az vm host restart \
 --resource-group myResourceGroup \
 --host-group myHostGroup \
 --name myDedicatedHost
```

To view the status of the restart, you can use the [az vm host get-instance-view](/en-us/cli/azure/vm#az-vm-host-get-instance-view) command. The **displayStatus** will be set to **Host undergoing restart** during the restart. Once the restart has completed, the displayStatus will return to **Host available**.

```azurecli
az vm host get-instance-view --resource-group myResourceGroup --host-group myHostGroup --name myDedicatedHost
```

# [PowerShell](#tab/powershell)
Restart the host using the [Restart-AzHost](/en-us/powershell/module/az.compute/restart-azhost) command.

```azurepowershell
Restart-AzHost -ResourceGroupName myResourceGroup -HostGroupName myHostGroup -Name myDedicatedHost
```

To view the status of the restart, you can use the [Get-AzHost](/en-us/powershell/module/az.compute/get-azhost) commandlet using the **InstanceView** parameter. The **displayStatus** will be set to **Host undergoing restart** during the restart. Once the restart has completed, the displayStatus will return to **Host available**.

```azurepowershell
$hostRestartStatus = Get-AzHost -ResourceGroupName myResourceGroup -HostGroupName myHostGroup -Name myDedicatedHost -InstanceView;
$hostRestartStatus.InstanceView.Statuses[1].DisplayStatus;
```

---

## Resize a host

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

## Redeploy a host [Preview]

If a VM or the underlying host remains unresponsive after following all the potential troubleshooting steps users can trigger service healing of the host and not wait for the platform to initiate the repair. Redeploying a host will move the host and all associated VMs to a different node of the same SKU. None of the host parameters would change except for the ‘Host asset ID’, which corresponds to the underlying Node Id.

Warning

Redeploy operation involves service healing hence would result in loss of any non-persistent data such as data stored on ephemeral disks. Save your work before redeploying.

# [Portal](#tab/portal)
1. Search for and select the host.
2. In the top menu bar, select the **Redeploy** button.
3. In the **Essentials** section of the Host Resource Pane, host's provisioning state will switch to **Updating** during the redeploy operation.
4. Once the redeploy operation is completed, host's provisioning state will revert to **Provisioning succeeded**.
5. In the **Essentials** section of the Host Resource Pane, **Host asset ID** would be updated to a new ID

# [CLI](#tab/cli)
Redeploying the host using [az vm host redeploy](/en-us/cli/azure/vm#az-vm-host-redeploy).

```azurecli
az vm host redeploy \
 --resource-group myResourceGroup \
 --host-group myHostGroup \
 --name myDedicatedHost
```

# [PowerShell](#tab/powershell)
PowerShell support coming soon.

---

## Deleting a host

You're being charged for your dedicated host even when no virtual machines are deployed on the host. You should delete any hosts you're currently not using to save costs.

You can only delete a host when there are no any longer virtual machines using it.

# [Portal](#tab/portal)
1. Search for and select the host.
2. In the left menu, select **Instances**.
3. Select and delete each virtual machine.
4. When all of the VMs have been deleted, go back to the **Overview** page for the host and select **Delete** from the top menu.
5. Once the host has been deleted, open the page for the host group and select **Delete host group**.

# [CLI](#tab/cli)
Delete the VMs using [az vm delete](/en-us/cli/azure/vm#az-vm-delete).

```azurecli
az vm delete -n myVM -g myDHResourceGroup
```

After deleting the VMs, you can delete the host using [az vm host delete](/en-us/cli/azure/vm/host#az-vm-host-delete).

```azurecli
az vm host delete -g myDHResourceGroup --host-group myHostGroup --name myHost
```

Once you've deleted all of your hosts, you may delete the host group using [az vm host group delete](/en-us/cli/azure/vm/host/group#az-vm-host-group-delete).

```azurecli
az vm host group delete -g myDHResourceGroup --host-group myHostGroup
```

You can also delete the entire resource group in a single command. The following command will delete all resources created in the group, including all of the VMs, hosts and host groups.

```azurecli
az group delete -n myDHResourceGroup
```

# [PowerShell](#tab/powershell)
Delete the VMs using [Remove-AzVM](/en-us/powershell/module/az.compute/remove-azvm).

```azurepowershell
Remove-AzVM -ResourceGroupName $rgName -Name myVM
```

After deleting the VMs, you can delete the host using [Remove-AzHost](/en-us/powershell/module/az.compute/remove-azhost).

```azurepowershell
Remove-AzHost -ResourceGroupName $rgName -Name myHost
```

Once you've deleted all of your hosts, you may delete the host group using [Remove-AzHostGroup](/en-us/powershell/module/az.compute/remove-azhostgroup).

```azurepowershell
Remove-AzHost -ResourceGroupName $rgName -Name myHost
```

You can also delete the entire resource group in a single command using [Remove-AzResourceGroup](/en-us/powershell/module/az.resources/remove-azresourcegroup). This following command will delete all resources created in the group, including all of the VMs, hosts and host groups.

```azurepowershell
Remove-AzResourceGroup -Name $rgName
```

---