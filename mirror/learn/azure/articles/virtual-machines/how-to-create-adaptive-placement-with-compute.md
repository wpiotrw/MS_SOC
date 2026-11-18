---
layout: Conceptual
title: Create a virtual machine with adaptive placement using compute templates in Azure (Preview) - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/how-to-create-adaptive-placement-with-compute
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
author: iamwilliew
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: wwilliams
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Learn how to deploy a virtual machine with adaptive placement by using compute templates and Azure REST APIs.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.topic: quickstart
ai-usage: ai-assisted
locale: en-us
document_id: b4e749ca-b9af-aa0b-7314-b5c545344451
document_version_independent_id: 2526b609-4440-c521-623a-464f34e6b230
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/how-to-create-adaptive-placement-with-compute.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/how-to-create-adaptive-placement-with-compute
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/how-to-create-adaptive-placement-with-compute.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: ddfc9d85-ba68-d960-e195-0e69ae952868
---

# Create a virtual machine with adaptive placement using compute templates in Azure (Preview) - Azure Virtual Machines | Microsoft Learn

Important

Compute templates are in **Limited preview**. Your subscription must be enabled for the preview. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

This quickstart shows you how to use Azure REST APIs to deploy a virtual machine (VM) with adaptive placement by using a compute template.

## Prerequisites

- Review the [compute template prerequisites and limitations](overview-compute-templates#prerequisites).
- Use Bash with the [Azure CLI installed](/en-us/cli/azure/install-azure-cli), or use Bash in [Azure Cloud Shell](https://shell.azure.com/).
- Complete the setup steps in the VM quickstart: [sign in and select a subscription](create-virtual-machine-with-compute-templates#sign-in-to-azure-and-select-a-subscription), [check subscription access](create-virtual-machine-with-compute-templates#check-subscription-access-to-the-compute-template-apis), create a [resource group](create-virtual-machine-with-compute-templates#create-a-resource-group), [virtual network](create-virtual-machine-with-compute-templates#create-a-virtual-network), [subnet](create-virtual-machine-with-compute-templates#create-a-subnet), and [Azure Compute Gallery](create-virtual-machine-with-compute-templates#create-an-azure-compute-gallery). If you already completed that quickstart, reuse these resources.
- Have an SSH public key available. To create one, see [Create SSH keys](linux/mac-create-ssh-keys).

Replace `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` in the examples with your subscription ID. The examples use the resource names from the VM quickstart, including the gallery `testIpGallery12`.

The commands use `az rest` to call the preview REST APIs.

## Create a network interface

Create a separate network interface for this VM. If you completed the VM quickstart, its network interface is already attached to another VM and can't be reused.

```azurecli
az network nic create \
    --resource-group "rg-ip-preview-test" \
    --location "eastus2euap" \
    --name "nic-ip-adaptive-01" \
    --vnet-name "vnet-ip-preview" \
    --subnet "subnet-ip-preview"
```

## Create an instance profile definition

Save the following JSON as `adaptive-placement-instance-profile.json` in your current directory:

```json
{
  "tags": {
    "purpose": "adaptive-placement-example"
  },
  "location": "eastus2euap",
  "properties": {
    "description": "Instance profile for a VM with adaptive placement"
  }
}
```

Run the following command:

```azurecli
az rest \
    --method PUT \
    --url "https://management.azure.com/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Compute/galleries/testIpGallery12/instanceProfiles/adaptive-placement-ip?api-version=2026-03-03" \
    --body "@adaptive-placement-instance-profile.json"
```

Example response:

```json
{
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Compute/galleries/testIpGallery12/instanceProfiles/adaptive-placement-ip",
  "location": "eastus2euap",
  "name": "adaptive-placement-ip",
  "properties": {
    "description": "Instance profile for a VM with adaptive placement",
    "provisioningState": "Succeeded"
  },
  "tags": {
    "purpose": "adaptive-placement-example"
  },
  "type": "Microsoft.Compute/galleries/instanceProfiles"
}
```

## Create an instance profile version

Save the following JSON as `adaptive-placement-instance-profile-version.json` in your current directory:

```json
{
  "name": "1.0.0",
  "location": "eastus2euap",
  "properties": {
    "targetLocations": [
      {
        "name": "eastus2euap"
      }
    ],
    "instanceProfileType": "VirtualMachine",
    "virtualMachineProfile": {
      "flexProfile": {
        "preferredVMSize": "Standard_D2s_v5"
      },
      "storageProfile": {
        "imageReference": {
          "publisher": "Canonical",
          "offer": "0001-com-ubuntu-server-jammy",
          "sku": "22_04-lts-gen2",
          "version": "latest"
        },
        "osDisk": {
          "createOption": "FromImage",
          "deleteOption": "Delete"
        }
      },
      "osProfile": {
        "adminUsername": "azureuser",
        "allowExtensionOperations": true,
        "linuxConfiguration": {
          "disablePasswordAuthentication": true,
          "provisionVMAgent": true
        }
      }
    }
  }
}
```

Run the following command:

```azurecli
az rest \
    --method PUT \
    --url "https://management.azure.com/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Compute/galleries/testIpGallery12/instanceProfiles/adaptive-placement-ip/versions/1.0.0?api-version=2026-03-03" \
    --body "@adaptive-placement-instance-profile-version.json"
```

Example response:

```json
{
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Compute/galleries/testIpGallery12/instanceProfiles/adaptive-placement-ip/versions/1.0.0",
  "location": "eastus2euap",
  "name": "1.0.0",
  "properties": {
    "instanceProfileType": "VirtualMachine",
    "provisioningState": "Succeeded",
    "targetLocations": [
      {
        "name": "eastus2euap"
      }
    ],
    "replicationStatus": {
      "aggregatedState": "Completed",
      "summary": [
        {
          "region": "eastus2euap",
          "state": "Completed",
          "progress": 100
        }
      ]
    },
    "virtualMachineProfile": {
      "flexProfile": {
        "preferredVMSize": "Standard_D2s_v5"
      },
      "storageProfile": {
        "imageReference": {
          "publisher": "Canonical",
          "offer": "0001-com-ubuntu-server-jammy",
          "sku": "22_04-lts-gen2",
          "version": "latest"
        },
        "osDisk": {
          "createOption": "FromImage",
          "deleteOption": "Delete"
        }
      },
      "osProfile": {
        "adminUsername": "azureuser",
        "allowExtensionOperations": true,
        "linuxConfiguration": {
          "disablePasswordAuthentication": true,
          "provisionVMAgent": true
        }
      }
    }
  },
  "type": "Microsoft.Compute/galleries/instanceProfiles/versions"
}
```

## Create a VM with adaptive placement

Save the following JSON as `adaptive-placement-virtual-machine.json` in your current directory. Replace `<ssh-public-key>` with your SSH public key.

The request sets `storageAccountType` to `StandardSSD_LRS` inline because the preview doesn't support that value in an instance profile.

```json
{
  "location": "eastus2euap",
  "properties": {
    "instanceProfile": {
      "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Compute/galleries/testIpGallery12/instanceProfiles/adaptive-placement-ip/versions/1.0.0"
    },
    "storageProfile": {
      "osDisk": {
        "managedDisk": {
          "storageAccountType": "StandardSSD_LRS"
        }
      }
    },
    "osProfile": {
      "computerName": "adaptive-placement-01",
      "linuxConfiguration": {
        "ssh": {
          "publicKeys": [
            {
              "path": "/home/azureuser/.ssh/authorized_keys",
              "keyData": "<ssh-public-key>"
            }
          ]
        }
      }
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Network/networkInterfaces/nic-ip-adaptive-01",
          "properties": {
            "primary": true
          }
        }
      ]
    }
  }
}
```

Run the following command:

```azurecli
az rest \
    --method PUT \
    --url "https://management.azure.com/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Compute/virtualMachines/adaptive-placement-01?api-version=2026-04-01" \
    --body "@adaptive-placement-virtual-machine.json"
```

Example response:

```json
{
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Compute/virtualMachines/adaptive-placement-01",
  "location": "eastus2euap",
  "name": "adaptive-placement-01",
  "properties": {
    "provisioningState": "Succeeded",
    "instanceProfile": {
      "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Compute/galleries/testIpGallery12/instanceProfiles/adaptive-placement-ip/versions/1.0.0"
    },
    "flexProfile": {
      "preferredVMSize": "Standard_D2s_v5"
    },
    "hardwareProfile": {
      "vmSize": "Standard_D2s_v5"
    },
    "storageProfile": {
      "imageReference": {
        "publisher": "Canonical",
        "offer": "0001-com-ubuntu-server-jammy",
        "sku": "22_04-lts-gen2",
        "version": "latest"
      },
      "osDisk": {
        "createOption": "FromImage",
        "deleteOption": "Delete",
        "osType": "Linux",
        "managedDisk": {
          "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Compute/disks/<generated-os-disk-name>",
          "storageAccountType": "StandardSSD_LRS"
        }
      }
    },
    "osProfile": {
      "computerName": "adaptive-placement-01",
      "adminUsername": "azureuser",
      "linuxConfiguration": {
        "disablePasswordAuthentication": true,
        "provisionVMAgent": true
      }
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg-ip-preview-test/providers/Microsoft.Network/networkInterfaces/nic-ip-adaptive-01"
        }
      ]
    }
  },
  "type": "Microsoft.Compute/virtualMachines"
}
```

Confirm that the response shows `provisioningState` as `Succeeded`.

To override values from the instance profile in your VM with adaptive placement request, see [Requests with overrides](create-virtual-machine-with-compute-templates#requests-with-overrides).