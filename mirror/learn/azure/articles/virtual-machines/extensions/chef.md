---
layout: Conceptual
title: Chef extension for Azure VMs - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/chef
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
description: Deploy the Chef Client to a virtual machine using the Chef VM Extension.
ms.topic: concept-article
ms.service: azure-virtual-machines
ms.subservice: extensions
ms.custom: devx-track-azurecli, linux-related-content
ms.author: gabsta
author: GabstaMSFT
ms.collection: linux
ms.date: 2026-09-17T00:00:00.0000000Z
locale: en-us
document_id: 0c283d52-543a-cf98-dd6e-0c9471da1829
document_version_independent_id: 5ed544f6-6888-e813-37f2-27d94b60118d
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/extensions/chef.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/extensions/chef
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/extensions/chef.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 0530bbf5-8e83-839d-3e59-abcc3ab7ec90
---

# Chef extension for Azure VMs - Azure Virtual Machines | Microsoft Learn

Chef Software provides a DevOps automation platform for Linux and Windows that enables the management of both physical and virtual server configurations. The Chef VM Extension is an extension that enables Chef on virtual machines.

Note

Try VM assist for faster diagnostics. We recommend that you run [VM assist for Windows](https://aka.ms/vmassistwindows) or [VM assist for Linux](https://aka.ms/vmassistlinux). These script-based diagnostic tools help you to identify common issues that affect the Azure VM Guest Agent and overall VM health.

If you're experiencing performance problems with virtual machines, before contacting support, run these tools.

## Prerequisites

### Operating system

The Chef VM Extension is supported on all the [Extension Supported OS's](https://support.microsoft.com/help/4078134/azure-extension-supported-operating-systems) in Azure.

### Internet connectivity

The Chef VM Extension requires that the target virtual machine is connected to the internet in order to retrieve the Chef Client payload from the content delivery network (CDN).

## Extension schema

The following JSON shows the schema for the Chef VM Extension. The extension requires at a minimum the Chef Server URL, the Validation Client Name and the Validation Key for the Chef Server; these values can be found in the `knife.rb` file in the starter-kit.zip that is downloaded when you install [Chef Automate](https://azuremarketplace.microsoft.com/marketplace/apps/chef-software.chef-automate) or a standalone [Chef Server](https://www.chef.io/downloads). Because the validation key should be treated as sensitive data, it should be configured under the **protectedSettings** element, meaning that it will only be decrypted on the target virtual machine.

```json
{
  "type": "Microsoft.Compute/virtualMachines/extensions",
  "name": "[concat(variables('vmName'),'/', parameters('chef_vm_extension_type'))]",
  "apiVersion": "2017-12-01",
  "location": "[parameters('location')]",
  "dependsOn": [
    "[concat('Microsoft.Compute/virtualMachines/', variables('vmName'))]"
  ],
  "properties": {
    "publisher": "Chef.Bootstrap.WindowsAzure",
    "type": "[parameters('chef_vm_extension_type')]",
    "typeHandlerVersion": "1210.15.11.1",
    "settings": {
      "bootstrap_options": {
        "chef_server_url": "[parameters('chef_server_url')]",
        "validation_client_name": "[parameters('chef_validation_client_name')]"
      },
      "runlist": "[parameters('chef_runlist')]"
    },
    "protectedSettings": {
      "validation_key": "[parameters('chef_validation_key')]",
      "chef_license_key": "[parameters('chef_license_key')]"
    }
  }
}  
```

### Core property values

| Name | Value / Example | Data Type |
| --- | --- | --- |
| apiVersion | `2017-12-01` | string (date) |
| publisher | `Chef.Bootstrap.WindowsAzure` | string |
| type | `LinuxChefClient` (Linux), `ChefClient` (Windows) | string |
| typeHandlerVersion | `1210.15.11.1` | string (double) |

### Settings

| Name | Value / Example | Data Type | Required? |
| --- | --- | --- | --- |
| settings/bootstrap\_options/chef\_server\_url | `https://api.chef.io/organizations/myorg` | string (url) | Y |
| settings/bootstrap\_options/validation\_client\_name | `myorg-validator` | string | Y |
| settings/runlist | `recipe[mycookbook::default]` | string | Y |
| settings/CHEF\_LICENSE | `accept-no-persist` | string | For Chef Infra Client 15+, accepting the [Chef EULA](https://docs.chef.io/chef_license_accept/#accept-the-chef-eula) is required. Accepted values are `accept`, `accept-silent`, or `accept-no-persist`. |
| settings/chef\_license\_key | `<your Chef commercial license key>` | string | **Deprecated.** Still supported for backward compatibility, but this location is public — readable via ARM deployment history/parameters and by anyone with Reader access to the VM extension resource. Set this under `protectedSettings/chef_license_key` instead; using this location logs a deprecation warning and it will be removed in a future release. |

### Protected settings

| Name | Example | Data Type | Required? |
| --- | --- | --- | --- |
| protectedSettings/validation\_key | `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>` | string | Y |
| protectedSettings/chef\_license\_key | `<your Chef commercial license key>` | string | Required by default for downloading Chef Infra Client. The extension decrypts this value on the target VM and exports it as `CHEF_LICENSE_KEY` before running the installer, downloading packages from `chefdownload-commercial.chef.io`. If omitted, the extension falls back to the deprecated, unlicensed `omnitruck.chef.io` download path. |

## Template deployment

Azure VM extensions can be deployed with Azure Resource Manager templates. Templates can be used to deploy one or more virtual machines, install the Chef Client, connect to the Chef Server and perform the initial configuration on the server as defined by the [Run-list](https://docs.chef.io/client/19/policy/run_lists/)

A sample Resource Manager template that includes the Chef VM Extension can be found in the [Azure quickstart gallery](https://github.com/Azure/azure-quickstart-templates/tree/master/application-workloads/chef/chef-json-parameters-linux-vm).

The JSON configuration for a virtual machine extension can be nested inside the virtual machine resource, or placed at the root or top level of a Resource Manager JSON template. The placement of the JSON configuration affects the value of the resource name and type. For more information, see [Set name and type for child resources](/en-us/azure/azure-resource-manager/templates/child-resource-name-type).

## Azure CLI deployment

The Azure CLI can be used to deploy the Chef VM Extension to an existing VM. Replace the **validation\_key** with the contents of your validation key (this file as a `.pem` extension). Replace **validation\_client\_name**, **chef\_server\_url** and **run\_list** with those values from the `knife.rb` file in your Starter Kit.

```azurecli
az vm extension set \
  --resource-group myResourceGroup \
  --vm-name myExistingVM \
  --name LinuxChefClient \
  --publisher Chef.Bootstrap.WindowsAzure \
  --version 1210.15.11.1 --protected-settings '{"validation_key": "<validation_key>", "chef_license_key": "<chef_license_key>"}' \
  --settings '{ "bootstrap_options": { "chef_server_url": "<chef_server_url>", "validation_client_name": "<validation_client_name>" }, "runlist": "<run_list>" }'
```

## Troubleshooting and support

Data about the state of extension deployments can be retrieved from the Azure portal, and by using the Azure CLI. To see the deployment state of extensions for a given VM, run the following command using the Azure CLI.

```azurecli
az vm extension list --resource-group myResourceGroup --vm-name myExistingVM -o table
```

Extension execution output is logged to the following file:

### Linux

```bash
/var/lib/waagent/Chef.Bootstrap.WindowsAzure.LinuxChefClient
```

### Windows

```powershell
C:\Packages\Plugins\Chef.Bootstrap.WindowsAzure.ChefClient\
```

### Error codes and their meanings

| Error Code | Meaning | Possible Action |
| --- | --- | --- |
| 51 | This extension is not supported on the VM's operating system |  |

Additional troubleshooting information can be found in the [Chef VM Extension readme](https://github.com/chef-partners/azure-chef-extension).

Note

For anything else directly related to Chef, contact [Chef Support](https://www.chef.io/support/).