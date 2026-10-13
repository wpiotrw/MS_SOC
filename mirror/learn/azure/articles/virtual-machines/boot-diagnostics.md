---
layout: Conceptual
title: Azure boot diagnostics - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/boot-diagnostics
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
author: mimckitt
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: mimckitt
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Overview of Azure boot diagnostics and managed boot diagnostics
services: virtual-machines
ms.custom: 
ms.topic: how-to
ms.date: 2023-02-25T00:00:00.0000000Z
locale: en-us
document_id: 691353ad-7c13-bce2-510f-b9a641cf95c4
document_version_independent_id: afced714-86a0-0fb7-b885-3021839b2fe3
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/boot-diagnostics.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/boot-diagnostics
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/boot-diagnostics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 76865732-76bf-f423-e69d-eb99602b8eb5
---

# Azure boot diagnostics - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

Boot diagnostics is a debugging feature for Azure virtual machines (VM) that allows diagnosis of VM boot failures. Boot diagnostics enables a user to observe the state of their VM as it is booting up by collecting serial log information and screenshots.

## Boot diagnostics storage account

When you create a VM in Azure portal, boot diagnostics is enabled by default. The recommended boot diagnostics experience is to use a managed storage account, as it yields significant performance improvements in the time to create an Azure VM. Using a managed storage account eliminates the time needed to create a user storage account to store the boot diagnostics data. When using a managed storage account: The managed storage account is not directly accessible, and the boot diagnostics data blobs (which comprise of logs and snapshot images) stored in the managed storage account are not currently billed.

An alternative boot diagnostic experience is to use a custom storage account. A user can either create a new storage account or use an existing one. When the storage firewall is enabled on the custom storage account (**Enabled from all networks** option isn't selected), you must:

- Make sure that access through the storage firewall is allowed for the Azure platform to publish the screenshot and serial log. To do this, go to the custom boot diagnostics storage account in the Azure portal and then select **Networking** from the **Security + networking** section. Check if the **Allow Azure services on the trusted services list to access this storage account** checkbox is selected.
- Allow storage firewall for users to view the boot screenshots or serial logs. To do this, add your network or the client/browser's Internet IPs as firewall exclusions. For more information, see [Configure Azure Storage firewalls and virtual networks](/en-us/azure/storage/common/storage-network-security).

To configure the storage firewall for Azure Serial Console, see [Use Serial Console with custom boot diagnostics storage account firewall enabled](/en-us/troubleshoot/azure/virtual-machines/serial-console-windows#use-serial-console-with-custom-boot-diagnostics-storage-account-firewall-enabled).

Note

The custom storage account associated with boot diagnostics requires the storage account and the associated virtual machines reside in the same region and subscription. To view the boot diagnostics data, users must also have the correct level of view and read permissions.

## Boot diagnostics view

Go to the virtual machine blade in the Azure portal, the boot diagnostics option is under the *Help* section in the Azure portal. Selecting boot diagnostics display a screenshot and serial log information. The serial log contains kernel messaging and the screenshot is a snapshot of your VMs current state. Based on if the VM is running Windows or Linux determines what the expected screenshot would look like. For Windows, users see a desktop background and for Linux, users see a login prompt.

![Screenshot of Linux boot diagnostics](media/boot-diagnostics/boot-diagnostics-linux.png)![Screenshot of Windows boot diagnostics](media/boot-diagnostics/boot-diagnostics-windows.png)

## Enable managed boot diagnostics

Managed boot diagnostics can be enabled through the Azure portal, CLI and ARM Templates.

### Enable managed boot diagnostics using the Azure portal

When you create a VM in the Azure portal, the default setting is to have boot diagnostics enabled using a managed storage account. Navigate to the *Management* tab during the VM creation to view it.

![Screenshot enabling managed boot diagnostics during VM creation.](media/boot-diagnostics/boot-diagnostics-enable-portal.png)

### Enable managed boot diagnostics using CLI

Boot diagnostics with a managed storage account is supported in Azure CLI 2.12.0 and later. If you don't input a name or URI for a storage account, a managed account is used. For more information and code samples, see the [CLI documentation for boot diagnostics](/en-us/cli/azure/vm/boot-diagnostics).

### Enable managed boot diagnostics using PowerShell

Boot diagnostics with a managed storage account is supported in Azure PowerShell 6.6.0 and later. If you don't input a name or URI for a storage account, a managed account is used. For more information and code samples, see the [PowerShell documentation for boot diagnostics](/en-us/powershell/module/az.compute/set-azvmbootdiagnostic).

### Enable managed boot diagnostics using Azure Resource Manager (ARM) templates

Everything after API version 2020-06-01 supports managed boot diagnostics. For more information, see [boot diagnostics instance view](/en-us/rest/api/compute/virtualmachines/createorupdate#bootdiagnostics).

```ARM
            "name": "[parameters('virtualMachineName')]",
            "type": "Microsoft.Compute/virtualMachines",
            "apiVersion": "2020-06-01",
            "location": "[parameters('location')]",
            "dependsOn": [
                "[concat('Microsoft.Network/networkInterfaces/', parameters('networkInterfaceName'))]"
            ],
            "properties": {
                "hardwareProfile": {
                    "vmSize": "[parameters('virtualMachineSize')]"
                },
                "storageProfile": {
                    "osDisk": {
                        "createOption": "fromImage",
                        "managedDisk": {
                            "storageAccountType": "[parameters('osDiskType')]"
                        }
                    },
                    "imageReference": {
                        "publisher": "publisherName",
                        "offer": "imageOffer",
                        "sku": "imageSKU",
                        "version": "imageVersion"
                    }
                },
                "networkProfile": {
                    "networkInterfaces": [
                        {
                            "id": "[resourceId('Microsoft.Network/networkInterfaces', parameters('networkInterfaceName'))]"
                        }
                    ]
                },
                "osProfile": {
                    "computerName": "[parameters('virtualMachineComputerName')]",
                    "adminUsername": "[parameters('adminUsername')]",
                    "linuxConfiguration": {
                        "disablePasswordAuthentication": true
                    }
                },
                "diagnosticsProfile": {
                    "bootDiagnostics": {
                        "enabled": true
                    }
                }
            }
        }
    ],

```

Note

Replace publisherName, imageOffer, imageSKU and imageVersion accordingly.

## Limitations

- Managed boot diagnostics is only available for Azure Resource Manager VMs.
- Managed boot diagnostics doesn't support VMs using unmanaged OS disks.
- Boot diagnostics doesn't support premium storage accounts or zone redundant storage accounts. If either of these are used for boot diagnostics users receive an `StorageAccountTypeNotSupported` error when starting the VM.
- Managed storage accounts are supported in Resource Manager API version "2020-06-01" and later.
- Portal only supports the use of boot diagnostics with a managed storage account for single instance VMs.
- Users can't configure a retention period for Managed Boot Diagnostics. The service stops writing logs when the total size reaches 1 GB.
- If the OS disk is swapped after enabling boot diagnostics, the VM will required a stop/ start before boot diagnostics will work again. To avoid this, disable boot diagnostics before swapping the OS disk and enable again after the OS disk swap has been completed.