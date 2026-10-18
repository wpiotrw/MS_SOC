---
layout: Conceptual
title: Associate a virtual machine to a capacity reservation group - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-associate-vm
breadcrumb_path: ../breadcrumb/azure-compute/toc.json
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
author: bdeforeest
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: jushiman
ms.author: bidefore
ms.update-cycle: 180-days
ms.service: azure-virtual-machines
description: Learn how to associate a new or existing virtual machine to a capacity reservation group.
ms.topic: how-to
ms.date: 2022-11-22T00:00:00.0000000Z
ms.custom: template-how-to, devx-track-azurecli, devx-track-azurepowershell, portal
locale: en-us
document_id: 97fee39d-d4b4-2aa3-8322-096525db6996
document_version_independent_id: 27510e2a-757f-2931-c71a-32b0ac70a3c0
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/capacity-reservation-associate-vm.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli,powershell
toc_rel: toc.json
asset_id: virtual-machines/capacity-reservation-associate-vm
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/capacity-reservation-associate-vm.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 7ddd0881-3dcb-5ec6-adfb-e6b28aa1f665
---

# Associate a virtual machine to a capacity reservation group - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Windows Virtual Machines ✔️ Linux Virtual Machines

You can use capacity reservation groups with new or existing virtual machines (VMs). To learn more about capacity reservations, see the [Capacity reservation overview](capacity-reservation-overview).

## Associate a new virtual machine

To associate a new virtual machine to the capacity reservation group, the group must be explicitly referenced as a property of the VM. This reference protects the matching reservation in the group for applications and workloads intended to use it.

# [API](#tab/api1)
To add the `capacityReservationGroup` property to a VM, construct the following `PUT` request to the `Microsoft.Compute` provider:

```rest
PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{VirtualMachineName}?api-version=2021-04-01
```

In the request body, include the `capacityReservationGroup` property:

```json
{ 
  "location": "eastus", 
  "properties": { 
    "hardwareProfile": { 
      "vmSize": "Standard_D2s_v3" 
    }, 
    … 
   "capacityReservation":{ 
    "capacityReservationGroup":{ 
        "id":"subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/CapacityReservationGroups/{CapacityReservationGroupName}" 
    } 
    "storageProfile": { 
    … 
    }, 
    "osProfile": { 
    … 
    }, 
    "networkProfile": { 
     …     
    } 
  } 
} 
```

# [Portal](#tab/portal1)
1. Open the [Azure portal](https://portal.azure.com).
2. In the search bar, enter **virtual machine**.
3. Under **Services**, select **Virtual machines**.
4. On the **Virtual machines** page, select **Create** and then select **Virtual machine**.
5. On the **Basics** tab, under **Project details**, select the correct subscription. Then choose to create a new resource group or use an existing one.
6. Under **Instance details**, enter the VM name and choose your region.
7. Select an **Image** and the VM size.
8. Under **Administrator account**, enter a username and a password. The password must be at least 12 characters long and meet the defined complexity requirements.
9. Go to the **Advanced section**.
10. In the **Capacity Reservations**dropdown list, select the capacity reservation group that you want to associate to the VM:
    1. If you are using the Capacity Reservation Group from the same subscription, select **Capacity reservation group**
    2. If you are using Capacity Reservation Group from another subscription, select **Shared capacity reservation group**(Preview):
        1. Select **Provider subscription**
        2. Select **Capacity reservation group**
11. Select **Review + create**.
12. After validation runs, select **Create**.
13. After the deployment is finished, select **Go to resource**.

# [CLI](#tab/cli1)
Use `az vm create` to create a new VM and add the `capacity-reservation-group` property to associate it to an existing capacity reservation group. The following example creates a Standard\_D2s\_v3 VM in the East US location and associates the VM to a capacity reservation group.

```azurecli
az vm create 
--resource-group myResourceGroup 
--name myVM 
--location eastus 
--size Standard_D2s_v3 
--image Ubuntu2204 
--capacity-reservation-group /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}
```

# [PowerShell](#tab/powershell1)
Use `New-AzVM` to create a new VM and add the `CapacityReservationGroupId` property to associate it to an existing capacity reservation group. The following example creates a Standard\_D2s\_v3 VM in the East US location and associates the VM to a capacity reservation group.

```powershell
New-AzVm
-ResourceGroupName "myResourceGroup"
-Name "myVM"
-Location "eastus"
-VirtualNetworkName "myVnet"
-SubnetName "mySubnet"
-SecurityGroupName "myNetworkSecurityGroup"
-PublicIpAddressName "myPublicIpAddress"
-Size "Standard_D2s_v3"
-CapacityReservationGroupId "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}"
```

To learn more, see the Azure PowerShell command [New-AzVM](/en-us/powershell/module/az.compute/new-azvm).

# [ARM template](#tab/arm1)
An [Azure Resource Manager template (ARM template)](/en-us/azure/azure-resource-manager/templates/overview) is a JavaScript Object Notation (JSON) file that defines the infrastructure and configuration for your project. The template uses declarative syntax. In declarative syntax, you describe your intended deployment without writing the sequence of programming commands to create the deployment.

ARM templates let you deploy groups of related resources. In a single template, you can create a capacity reservation group and capacity reservations. You can deploy templates through the Azure portal, the Azure CLI, or Azure PowerShell, or from continuous integration/continuous delivery (CI/CD) pipelines.

To associate a VM with a Capacity Reservation Group, see the following ARM template. Replace the resource names with your own. The following example creates a VM of SKU D2s\_v3 and associates it to a capacity reservation group.

Alternatively, you can remove the *zone* information to create a regional VM and associate it to a Capacity Reservation Group.

```json
{
   "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
   "contentVersion": "1.0.0.0",
   "parameters": {
       "adminUsername": {
           "type": "string",
           "metadata": {
               "description": "Username for the Virtual Machine."
           }
       },
       "adminPassword": {
           "type": "securestring",
           "minLength": 12,
           "metadata": {
               "description": "Password for the Virtual Machine."
           }
       },
       "dnsLabelPrefix": {
           "type": "string",
           "defaultValue": "[toLower(concat(parameters('vmName'),'-', uniqueString(resourceGroup().id, parameters('vmName'))))]",
           "metadata": {
               "description": "Unique DNS Name for the Public IP used to access the Virtual Machine."
           }
       },
       "publicIpName": {
           "type": "string",
           "defaultValue": "myPublicIP",
           "metadata": {
               "description": "Name for the Public IP used to access the Virtual Machine."
           }
       },
       "publicIPAllocationMethod": {
           "type": "string",
           "defaultValue": "Dynamic",
           "allowedValues": [
               "Dynamic",
               "Static"
           ],
           "metadata": {
               "description": "Allocation method for the Public IP used to access the Virtual Machine."
           }
       },
       "publicIpSku": {
           "type": "string",
           "defaultValue": "Basic",
           "allowedValues": [
               "Basic",
               "Standard"
           ],
           "metadata": {
               "description": "SKU for the Public IP used to access the Virtual Machine."
           }
       },
       "OSVersion": {
           "type": "string",
           "defaultValue": "2019-Datacenter",
           "allowedValues": [
               "2008-R2-SP1",
               "2012-Datacenter",
               "2012-R2-Datacenter",
               "2016-Nano-Server",
               "2016-Datacenter-with-Containers",
               "2016-Datacenter",
               "2019-Datacenter",
               "2019-Datacenter-Core",
               "2019-Datacenter-Core-smalldisk",
               "2019-Datacenter-Core-with-Containers",
               "2019-Datacenter-Core-with-Containers-smalldisk",
               "2019-Datacenter-smalldisk",
               "2019-Datacenter-with-Containers",
               "2019-Datacenter-with-Containers-smalldisk"
           ],
           "metadata": {
               "description": "The Windows version for the VM. This will pick a fully patched image of this given Windows version."
           }
       },
       "vmSize": {
           "type": "string",
           "defaultValue": "Standard_D2s_v3",
           "metadata": {
               "description": "Size of the virtual machine."
           }
       },
       "location": {
           "type": "string",
           "defaultValue": "[resourceGroup().location]",
           "metadata": {
               "description": "Location for all resources."
           }
       },
       "vmName": {
           "type": "string",
           "defaultValue": "myD2v3VM",
           "metadata": {
               "description": "Name of the virtual machine."
           }
       }
   },
   "variables": {
       "storageAccountName": "[concat('bootdiags', uniquestring(resourceGroup().id))]",
       "nicName": "myVMNic",
       "addressPrefix": "10.0.0.0/16",
       "subnetName": "Subnet",
       "subnetPrefix": "10.0.0.0/24",
       "virtualNetworkName": "MyVNET",
       "subnetRef": "[resourceId('Microsoft.Network/virtualNetworks/subnets', variables('virtualNetworkName'), variables('subnetName'))]",
       "networkSecurityGroupName": "default-NSG"
   },
   "resources": [{
           "type": "Microsoft.Storage/storageAccounts",
           "apiVersion": "2019-06-01",
           "name": "[variables('storageAccountName')]",
           "location": "[parameters('location')]",
           "sku": {
               "name": "Standard_LRS"
           },
           "kind": "Storage",
           "properties": {}
       }, {
           "type": "Microsoft.Network/publicIPAddresses",
           "apiVersion": "2020-06-01",
           "name": "[parameters('publicIPName')]",
           "location": "[parameters('location')]",
           "sku": {
               "name": "[parameters('publicIpSku')]"
           },
           "properties": {
               "publicIPAllocationMethod": "[parameters('publicIPAllocationMethod')]",
               "dnsSettings": {
                   "domainNameLabel": "[parameters('dnsLabelPrefix')]"
               }
           }
       }, {
           "type": "Microsoft.Network/networkSecurityGroups",
           "apiVersion": "2020-06-01",
           "name": "[variables('networkSecurityGroupName')]",
           "location": "[parameters('location')]",
           "properties": {
               "securityRules": [{
                       "name": "default-allow-3389",
                       "properties": {
                           "priority": 1000,
                           "access": "Allow",
                           "direction": "Inbound",
                           "destinationPortRange": "3389",
                           "protocol": "Tcp",
                           "sourcePortRange": "*",
                           "sourceAddressPrefix": "*",
                           "destinationAddressPrefix": "*"
                       }
                   }
               ]
           }
       }, {
           "type": "Microsoft.Network/virtualNetworks",
           "apiVersion": "2020-06-01",
           "name": "[variables('virtualNetworkName')]",
           "location": "[parameters('location')]",
           "dependsOn": [
               "[resourceId('Microsoft.Network/networkSecurityGroups', variables('networkSecurityGroupName'))]"
           ],
           "properties": {
               "addressSpace": {
                   "addressPrefixes": [
                       "[variables('addressPrefix')]"
                   ]
               },
               "subnets": [{
                       "name": "[variables('subnetName')]",
                       "properties": {
                           "addressPrefix": "[variables('subnetPrefix')]",
                           "networkSecurityGroup": {
                               "id": "[resourceId('Microsoft.Network/networkSecurityGroups', variables('networkSecurityGroupName'))]"
                           }
                       }
                   }
               ]
           }
       }, {
           "type": "Microsoft.Network/networkInterfaces",
           "apiVersion": "2020-06-01",
           "name": "[variables('nicName')]",
           "location": "[parameters('location')]",
           "dependsOn": [
               "[resourceId('Microsoft.Network/publicIPAddresses', parameters('publicIPName'))]",
               "[resourceId('Microsoft.Network/virtualNetworks', variables('virtualNetworkName'))]"
           ],
           "properties": {
               "ipConfigurations": [{
                       "name": "ipconfig1",
                       "properties": {
                           "privateIPAllocationMethod": "Dynamic",
                           "publicIPAddress": {
                               "id": "[resourceId('Microsoft.Network/publicIPAddresses', parameters('publicIPName'))]"
                           },
                           "subnet": {
                               "id": "[variables('subnetRef')]"
                           }
                       }
                   }
               ]
           }
       }, {
           "type": "Microsoft.Compute/virtualMachines",
           "apiVersion": "2020-06-01",
           "name": "[parameters('vmName')]",
           "location": "[parameters('location')]",
           "zones": "[parameters('Zones')]",
           "dependsOn": [
               "[resourceId('Microsoft.Storage/storageAccounts', variables('storageAccountName'))]",
               "[resourceId('Microsoft.Network/networkInterfaces', variables('nicName'))]"
           ],
           "properties": {
               "hardwareProfile": {
                   "vmSize": "[parameters('vmSize')]"
               },
               "capacityReservation": {
                   "capacityReservationGroup": {
                       "id": "subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{CapacityReservationGroupName}"
                   }
               },
               "osProfile": {
                   "computerName": "[parameters('vmName')]",
                   "adminUsername": "[parameters('adminUsername')]",
                   "adminPassword": "[parameters('adminPassword')]"
               },
               "storageProfile": {
                   "imageReference": {
                       "publisher": "MicrosoftWindowsServer",
                       "offer": "WindowsServer",
                       "sku": "[parameters('OSVersion')]",
                       "version": "latest"
                   },
                   "osDisk": {
                       "createOption": "FromImage",
                       "managedDisk": {
                           "storageAccountType": "StandardSSD_LRS"
                       }
                   },
                   "dataDisks": [{
                           "diskSizeGB": 1023,
                           "lun": 0,
                           "createOption": "Empty"
                       }
                   ]
               },
               "networkProfile": {
                   "networkInterfaces": [{
                           "id": "[resourceId('Microsoft.Network/networkInterfaces', variables('nicName'))]"
                       }
                   ]
               },
               "diagnosticsProfile": {
                   "bootDiagnostics": {
                       "enabled": true,
                       "storageUri": "[reference(resourceId('Microsoft.Storage/storageAccounts', variables('storageAccountName'))).primaryEndpoints.blob]"
                   }
               }
           }
       }
   ],
   "outputs": {
       "hostname": {
           "type": "string",
           "value": "[reference(parameters('publicIPName')).dnsSettings.fqdn]"
       }
   }
}

```

---

## Associate an existing virtual machine

Existing zonal virtual machines can simply be updated with Capacity Reservation Group property without the need of deallocation and it will automatically consume the capacity reservation. Existing regional virtual machines must be reallocated.

### Regional Virtual Machine

For the initial release of a capacity reservation, a virtual machine must be allocated to a capacity reservation:

1. Follow guidance to create a capacity reservation group and capacity reservation, if necessary. Or increment the quantity of an existing capacity reservation so there's unused reserved capacity.
2. Deallocate the virtual machine.
3. Update the capacity reservation group property on the VM.
4. Restart the VM.

Follow the steps to associate the virtual machine to a capacity reservation group.

# [API](#tab/api2)
1. Deallocate the virtual machine:

    ```rest
    PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourcegroupname}/providers/Microsoft.Compute/virtualMachines/{VirtualMachineName}/deallocate?api-version=2021-04-01
    ```
2. Add the `capacityReservationGroup` property to the VM. Construct the following `PUT` request to `Microsoft.Compute` provider:

    ```rest
    PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{VirtualMachineName}?api-version=2021-04-01
    ```

    In the request body, include the `capacityReservationGroup` property:

    ```json
    {
    "location": "eastus",
    "properties": {
        "capacityReservation": {
            "capacityReservationGroup": {
                "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}"
            }
        }
    }
    }
    ```

# [Portal](#tab/portal2)
1. Open the [Azure portal](https://portal.azure.com).
2. Go to your VM.
3. Select **Overview**.
4. Select **Stop** at the top of the page to deallocate the VM.
5. Go to **Configurations** on the left.
6. In the **Capacity Reservations**dropdown list, select the capacity reservation group that you want to associate to the VM:
    1. If you are using the Capacity Reservation Group from the same subscription, select **Capacity reservation group**
    2. If you are using Capacity Reservation Group from another subscription, select **Shared capacity reservation group**(Preview):
        1. Select **Provider subscription**
        2. Select **Capacity reservation group**

# [CLI](#tab/cli2)
1. Deallocate the virtual machine:

    ```azurecli
    az vm deallocate 
    -g myResourceGroup 
    -n myVM
    ```
2. Associate the VM to a capacity reservation group:

    ```azurecli
    az vm update 
    -g myresourcegroup 
    -n myVM 
    --capacity-reservation-group subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{CapacityReservationGroupName}
    ```

# [PowerShell](#tab/powershell2)
1. Deallocate the virtual machine:

    ```powershell
    Stop-AzVM
    -ResourceGroupName "myResourceGroup"
    -Name "myVM"
    ```
2. Associate the VM to a capacity reservation group:

    ```powershell
    $VirtualMachine =
    Get-AzVM
    -ResourceGroupName "myResourceGroup"
    -Name "myVM"
    
    Update-AzVM
    -ResourceGroupName "myResourceGroup"
    -VM $VirtualMachine
    -CapacityReservationGroupId "subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{CapacityReservationGroupName}"
    ```

To learn more, see the Azure PowerShell commands [Stop-AzVM](/en-us/powershell/module/az.compute/stop-azvm), [Get-AzVM](/en-us/powershell/module/az.compute/get-azvm), and [Update-AzVM](/en-us/powershell/module/az.compute/update-azvm).

---

### Zonal Virtual Machine

A zonal virtual machine can be allocated to a capacity reservation without the need of reallocation. If you have capacity in an existing capacity reservation group, you can add an existing zonal virtual machine to the capacity reservation group and update the VM to use a matching capacity reservation in the capacity reservation group.

Note

Terraform on Azure support isn't available for the capability to allow in-place association of a zonal VM to a capacity reservation group.

1. Follow guidance to create a capacity reservation group and capacity reservation, if necessary. Or increment the quantity of an existing capacity reservation so there's unused reserved capacity.
2. Update the capacity reservation group property on the VM.

Follow the steps to associate the virtual machine to a capacity reservation group.

# [API](#tab/api2)
Add the `capacityReservationGroup` property to the VM. Construct the following `PUT` request to `Microsoft.Compute` provider:

```rest
    PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{VirtualMachineName}?api-version=2021-04-01
```

In the request body, include the `capacityReservationGroup` property:

```json
    {
    "location": "eastus",
    "properties": {
        "capacityReservation": {
            "capacityReservationGroup": {
                "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}"
            }
        }
    }
    }
```

# [Portal](#tab/portal2)
1. Open the [Azure portal](https://portal.azure.com).
2. Go to your VM.
3. Select **Overview**.
4. Go to **Configurations** on the left.
5. In the **Capacity Reservations**dropdown list, select the capacity reservation group that you want to associate to the VM:
    1. If you are using the Capacity Reservation Group from the same subscription, select **Capacity reservation group**
    2. If you are using Capacity Reservation Group from another subscription, select **Shared capacity reservation group**(Preview):
        1. Select **Provider subscription**
        2. Select **Capacity reservation group**

# [CLI](#tab/cli2)
Associate the VM to a capacity reservation group:

```azurecli
    az vm update 
    -g myresourcegroup 
    -n myVM 
    --capacity-reservation-group subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{CapacityReservationGroupName}
```

# [PowerShell](#tab/powershell2)
Associate the VM to a capacity reservation group:

```powershell
    $VirtualMachine =
    Get-AzVM
    -ResourceGroupName "myResourceGroup"
    -Name "myVM"
    
    Update-AzVM
    -ResourceGroupName "myResourceGroup"
    -VM $VirtualMachine
    -CapacityReservationGroupId "subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{CapacityReservationGroupName}"
```

To learn more, see the Azure PowerShell commands [Stop-AzVM](/en-us/powershell/module/az.compute/stop-azvm), [Get-AzVM](/en-us/powershell/module/az.compute/get-azvm), and [Update-AzVM](/en-us/powershell/module/az.compute/update-azvm).

---

### Secure existing zonal virtual machine using zero size reservation

Zonal virtual machines can be converted to using an On Demand Capacity Reservation without reallocation. If you do not have capacity in an existing capacity reservation group, you can start by creating a zero size matching reservation to secure your workloads. The basic process involves 3 steps:

1. Create a Capacity Reservation Group and then matching capacity reservations in each target zone with the reserved quantity set to zero. This requires no additional quota or capacity. For more information on how to create a reservation, see [Create a capacity reservation](/en-us/azure/virtual-machines/capacity-reservation-create?tabs=portal1%2Capi1%2Capi2#create-a-capacity-reservation-1).
2. Associate existing running zonal virtual machine to the capacity reservation. Set the Virtual Machine capacityReservationGroup property to the desired Capacity Reservation Group. When complete, each target capacity reservation will be overallocated. See Zonal Virtual Machine.
3. Increase the reserved quantity of each capacity reservation (CR) to match the allocated Virtual Machine (VM) count. Since each CR is already overallocated, this step requires no additional quota or capacity. For more information on how to update the reserved count, see [Capacity reservation modify](/en-us/azure/virtual-machines/capacity-reservation-modify?tabs=api1%2Capi2%2Capi3#update-the-number-of-instances-reserved).

After the quantity increase, you should see the CR in a fully allocated state with all the virtual machines allocated. See View VM allocation with the Instance View.

For information on using shared capacity reservation group, see [Secure existing zonal workloads using zero size reservation in Shared capacity Reservation Group](/en-us/azure/virtual-machines/capacity-reservation-group-share?tabs=api-1%2Capi-2%2Capi-3%2Capi-4%2Capi-5%2Capi-6%2Cportal-7#secure-existing-zonal-workloads-using-zero-size-reservation-in-shared-capacity-reservation-group).

## View VM allocation with the Instance View

After the `capacityReservationGroup` property is set, an association now exists between the VM and the group. Azure automatically finds the matching capacity reservation in the group and consumes a reserved slot. The capacity reservation's Instance View reflects the new VM in the `virtualMachinesAllocated` property:

# [API](#tab/api3)
```rest
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/CapacityReservationGroups/{capacityReservationGroupName}?$expand=instanceView&api-version=2021-04-01 
```

```json
{
   "name":"{CapacityReservationGroupName}",
   "id":"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{CapacityReservationGroupName}",
   "type":"Microsoft.Compute/capacityReservationGroups",
   "location":"eastus",
   "properties":{
      "capacityReservations":[
         {
            "id":"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/ {CapacityReservationGroupName}/capacityReservations/{CapacityReservationName}"
         }
      ],
      "virtualMachinesAssociated":[
         {
            "id":"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{myVM}"
         }
      ],
      "instanceView":{
         "capacityReservations":[
            {
               "name":"{CapacityReservationName}",
               "utilizationInfo":{
                  "virtualMachinesAllocated":[
                     {
                        "id":"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{myVM}"
                     }
                  ],
                  "currentCapacity": 1
               },
               "statuses":[
                  {
                     "code":"ProvisioningState/succeeded",
                     "level":"Info",
                     "displayStatus":"Provisioning succeeded",
                     "time":"2021-05-25T15:12:10.4165243+00:00"
                  }
               ]
            }
         ]
      }
   }
} 
```

# [CLI](#tab/cli3)
```azurecli
az capacity reservation show 
-g myResourceGroup
-c myCapacityReservationGroup 
-n myCapacityReservation
--instance-view 
```

# [PowerShell](#tab/powershell3)
```powershell
$CapRes=
Get-AzCapacityReservation
-ResourceGroupName <"ResourceGroupName">
-ReservationGroupName <"CapacityReservationGroupName">
-Name <"CapacityReservationName">
-InstanceView

$CapRes.InstanceView.Utilizationinfo.VirtualMachinesAllocated
```

To learn more, see the Azure PowerShell command [Get-AzCapacityReservation](/en-us/powershell/module/az.compute/get-azcapacityreservation).

# [Portal](#tab/portal3)
1. Open the [Azure portal](https://portal.azure.com).
2. Go to your capacity reservation group.
3. Under **Settings** on the left, select **Resources**.
4. Look at the table to see all the VMs that are associated to the capacity reservation group.

---