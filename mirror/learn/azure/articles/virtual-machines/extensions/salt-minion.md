---
layout: Conceptual
title: Salt Minion for Linux or Windows Azure VMs - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/salt-minion
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
description: Install Salt Minion on Linux or Windows VMs using the VM Extension.
ms.topic: concept-article
ms.service: azure-virtual-machines
ms.subservice: extensions
ms.custom: devx-track-arm-template, devx-track-azurecli, devx-track-terraform, linux-related-content
ms.author: gabsta
author: GabstaMSFT
ms.date: 2025-08-18T00:00:00.0000000Z
locale: en-us
document_id: ef3a27b7-d353-1746-d044-67a1ddb89d72
document_version_independent_id: 8e95c01c-980c-84bf-e1da-12250daa023d
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/extensions/salt-minion.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/extensions/salt-minion
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/extensions/salt-minion.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: f5bcb712-2dec-6578-ee5d-ab1dc9c13362
---

# Salt Minion for Linux or Windows Azure VMs - Azure Virtual Machines | Microsoft Learn

## Prerequisites

- A Microsoft Azure account with one (or more) Windows or Linux VMs
- A Salt Master (either on-premises or in a cloud) that can accept connections from Salt minions hosted on Azure
- The Salt Minion VM Extension requires that the target VM is connected to the internet in order to fetch Salt packages

Note

Try VM assist for faster diagnostics. We recommend that you run [VM assist for Windows](https://aka.ms/vmassistwindows) or [VM assist for Linux](https://aka.ms/vmassistlinux). These script-based diagnostic tools help you to identify common issues that affect the Azure VM Guest Agent and overall VM health.

If you're experiencing performance problems with virtual machines, before contacting support, run these tools.

## Supported platforms

Azure VM running any of the following supported OS:

- Ubuntu 20.04, 22.04 (x86\_64)
- Debian 10, 11 (x86\_64)
- Oracle Linux 7, 8, 9 (x86\_64)
- RHEL 7, 8, 9 (x86\_64)
- Microsoft Windows 10, 11 Pro (x86\_64)
- Microsoft Windows Server 2012 R2, 2016, 2019, 2022 Datacenter (x86\_64)

If you want another distro to be supported (assuming Salt [supports](https://docs.saltproject.io/salt/install-guide/en/latest/topics/salt-supported-operating-systems.html) it), an issue can be filed on [GitLab](https://gitlab.com/turtletraction-oss/azure-salt-vm-extensions/-/issues).

## Supported Salt Minion versions

- 3006 and up (onedir)

## Extension details

- Publisher name: `turtletraction.oss`
- Linux extension name: `salt-minion.linux`
- Windows extension name: `salt-minion.windows`

## Salt Minion settings

- `master_address` - Salt Master address to connect to (`localhost` by default)
- `minion_id` - Minion ID (hostname by default)
- `salt_version` - Salt Minion version to install, for example `3006.1` (`latest` by default)

## Install Salt Minion using the Azure portal

1. Select one of your VMs.
2. In the left menu click **Extensions + applications**.
3. Click **+ Add**.
4. In the gallery, type **Salt Minion** in the search bar.
5. Select the **Salt Minion** tile and click **Next**.
6. Enter configuration parameters in the provided form (see Salt Minion settings).
7. Click **Review + create**.

## Install Salt Minion using the Azure CLI

```shell
az vm extension set --resource-group my-group --vm-name vm-ubuntu22 --name salt-minion.linux --publisher turtletraction.oss --settings '{"master_address": "10.x.x.x"}'
az vm extension set --resource-group my-group --vm-name vm-windows11 --name salt-minion.windows --publisher turtletraction.oss --settings '{"master_address": "10.x.x.x"}'
```

To uninstall it:

```shell
az vm extension delete --resource-group my-group --vm-name vm-ubuntu22 --name salt-minion.linux
az vm extension delete --resource-group my-group --vm-name vm-windows11 --name salt-minion.windows
```

## Install Salt Minion using the Azure ARM template

```json
{
    "$schema": "http://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "vmName": {
            "type": "string"
        },
        "master_address": {
            "type": "string"
        },
        "salt_version": {
            "type": "string"
        },
        "minion_id": {
            "type": "string"
        }
    },
    "resources": [
        {
            "name": "[concat(parameters('vmName'),'/salt-minion.linux')]",
            "type": "Microsoft.Compute/virtualMachines/extensions",
            "location": "[resourceGroup().location]",
            "apiVersion": "2015-06-15",
            "properties": {
                "publisher": "turtletraction.oss",
                "type": "salt-minion.linux",
                "typeHandlerVersion": "1.0",
                "autoUpgradeMinorVersion": true,
                "settings": {
                    "master_address": "[parameters('master_address')]",
                    "salt_version": "[parameters('salt_version')]",
                    "minion_id": "[parameters('minion_id')]"
                }
            }
        }
    ]
}
```

## Install Salt Minion using Terraform

Assuming that you have defined a VM resource in TerraForm named `vm_ubuntu`, then use something like this to install the extension on it:

```hcl
resource "azurerm_virtual_machine_extension" "vmext_ubuntu" {
  name                 = "vmext_ubuntu"
  virtual_machine_id   = azurerm_linux_virtual_machine.vm_ubuntu.id
  publisher            = "turtletraction.oss"
  type                 = "salt-minion.linux"
  type_handler_version = "1.0"

  settings = <<SETTINGS
{
  "salt_version": "3006.1",
  "master_address": "x.x.x.x",
  "minion_id": "ubuntu22"
}
SETTINGS
}
```

## Support

- The source code of this extension is available on [GitLab](https://gitlab.com/turtletraction-oss/azure-salt-vm-extensions/)
- For Azure related issues, you can file an Azure support incident. Go to the [Azure support site](https://azure.microsoft.com/support/options/) and select Get support