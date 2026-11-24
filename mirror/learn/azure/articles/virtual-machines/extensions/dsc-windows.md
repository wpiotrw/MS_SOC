---
layout: Conceptual
title: Azure Desired State Configuration Extension Handler - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/dsc-windows
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
description: Upload and apply PowerShell Desired State Configuration on an Azure VM using DSC Extension
ms.topic: concept-article
ms.service: azure-virtual-machines
ms.subservice: extensions
author: mgreenegit
ms.author: migreene
ms.collection: windows
ms.date: 2026-11-23T00:00:00.0000000Z
locale: en-us
document_id: c2e15d16-5405-f4e9-e899-d4c74e418cad
document_version_independent_id: 00474e00-329e-772d-da02-c82c2c7a455a
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/extensions/dsc-windows.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/extensions/dsc-windows
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/extensions/dsc-windows.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: bc1c08e4-c906-4215-e8e5-aacb616578f9
---

# Azure Desired State Configuration Extension Handler - Azure Virtual Machines | Microsoft Learn

The PowerShell DSC Extension for Windows uploads and applies a PowerShell DSC Configuration on an Azure virtual machine. The DSC Extension calls into PowerShell DSC to enact the received DSC configuration on the virtual machine. This article details the supported platforms, configurations, and deployment options for the DSC virtual machine extension for Windows.

Note

DSC extension will be retired on March 31, 2028. Move to [Azure Machine Configuration](/en-us/azure/governance/machine-configuration/overview) by that date. For more information, see the [blog post](https://azure.microsoft.com/updates/?id=485828) announcement. The Azure Machine Configuration service combines certain features of DSC Extension, Azure Automation State Configuration, and commonly requested features from customer feedback. Azure Machine Configuration also includes hybrid machine support through [Arc-enabled servers](/en-us/azure/azure-arc/servers/overview).

Note

Try VM assist for faster diagnostics. We recommend that you run [VM assist for Windows](https://aka.ms/vmassistwindows) or [VM assist for Linux](https://aka.ms/vmassistlinux). These script-based diagnostic tools help you to identify common issues that affect the Azure VM Guest Agent and overall VM health.

If you're experiencing performance problems with virtual machines, before contacting support, run these tools.

## Prerequisites

### Operating system

The DSC Extension supports the following operating systems

Windows Server 2022, Windows Server 2019, Windows Server 2016, Windows Server 2012R2, Windows Server 2012, Windows Server 2008 R2 SP1, Windows Client 7/8.1/10

### Internet connectivity

The DSC extension for Windows requires that the target virtual machine is able to communicate with Azure and the location of the configuration package (.zip file) if stored outside of Azure.

## Extension schema

The following JSON shows the schema for the settings portion of the DSC Extension in an Azure Resource Manager template.

```json
{
  "type": "Microsoft.Compute/virtualMachines/extensions",
  "name": "Microsoft.Powershell.DSC",
  "apiVersion": "2018-10-01",
  "location": "<location>",
  "properties": {
    "publisher": "Microsoft.Powershell",
    "type": "DSC",
    "typeHandlerVersion": "2.77",
    "autoUpgradeMinorVersion": true,
    "settings": {
        "wmfVersion": "latest",
        "configuration": {
            "url": "http://validURLToConfigLocation",
            "script": "ConfigurationScript.ps1",
            "function": "ConfigurationFunction"
        },
        "configurationArguments": {
            "argument1": "Value1",
            "argument2": "Value2"
        },
        "configurationData": {
            "url": "https://foo.psd1"
        },
        "privacy": {
            "dataCollection": "enable"
        },
        "advancedOptions": {
            "forcePullAndApply": false,
            "downloadMappings": {
             "specificDependencyKey": "https://myCustomDependencyLocation"
            }
        }
    },
    "protectedSettings": {
        "configurationArguments": {
            "parameterOfTypePSCredential1": {
                "userName": "UsernameValue1",
                "password": "PasswordValue1"
            },
            "parameterOfTypePSCredential2": {
                "userName": "UsernameValue2",
                "password": "PasswordValue2"
            }
        },
        "configurationUrlSasToken": "?g!bber1sht0k3n",
        "configurationDataUrlSasToken": "?dataAcC355T0k3N"
    }
  }
}
```

### Property values

| Name | Value / Example | Data Type |
| --- | --- | --- |
| apiVersion | 2018-10-01 | date |
| publisher | Microsoft.Powershell.DSC | string |
| type | DSC | string |
| typeHandlerVersion | 2.77 | int |

### Settings Property values

| Name | Data Type | Description |
| --- | --- | --- |
| settings.wmfVersion | string | Specifies the version of the Windows Management Framework that should be installed on your VM. Setting this property to 'latest' installs the most updated version of WMF. The only current possible values for this property are ‘4.0’, ‘5.0’, and 'latest'. These possible values are subject to updates. The default value is 'latest'. |
| settings.configuration.url | string | Specifies the URL location from which to download your DSC configuration zip file. If the URL provided requires a SAS token for access, set the protectedSettings.configurationUrlSasToken property to the value of your SAS token. This property is required if settings.configuration.script and/or settings.configuration.function are defined. |
| settings.configuration.script | string | Specifies the file name of the script that contains the definition of your DSC configuration. This script must be in the root folder of the zip file downloaded from the URL specified by the configuration.url property. This property is required if settings.configuration.url and/or settings.configuration.script are defined. |
| settings.configuration.function | string | Specifies the name of your DSC configuration. The configuration named must be contained in the script defined by configuration.script. This property is required if settings.configuration.url and/or settings.configuration.function are defined. |
| settings.configurationArguments | Collection | Defines any parameters you would like to pass to your DSC configuration. This property won't be encrypted. |
| settings.configurationData.url | string | Specifies the URL from which to download your configuration data (.pds1) file to use as input for your DSC configuration. If the URL provided requires a SAS token for access, set the protectedSettings.configurationDataUrlSasToken property to the value of your SAS token. |
| settings.privacy.dataEnabled | string | Enables or disables telemetry collection. The only possible values for this property are ‘Enable’, ‘Disable’, ”, or $null. Leaving this property blank or null enables telemetry |
| settings.advancedOptions.forcePullAndApply | Bool | This setting is designed to enhance the experience of working with the extension to register nodes with Azure Automation DSC. If the value is `$true`, the extension waits for the first run of the configuration pulled from the service before returning success/failure. If the value is set to $false, the status returned by the extension refers to whether the node was registered with Azure Automation State Configuration successfully and the node configuration won't run during the registration. |
| settings.advancedOptions.downloadMappings | Collection | Defines alternate locations to download dependencies such as WMF and .NET |

### Protected Settings Property values

| Name | Data Type | Description |
| --- | --- | --- |
| protectedSettings.configurationArguments | string | Defines any parameters you would like to pass to your DSC configuration. |
| protectedSettings.configurationUrlSasToken | string | Specifies the SAS token to access the URL defined by configuration.url. |
| protectedSettings.configurationDataUrlSasToken | string | Specifies the SAS token to access the URL defined by configurationData.url. |

## Template deployment

Azure VM extensions can be deployed with Azure Resource Manager templates. Templates are ideal when deploying one or more virtual machines that require post deployment configuration. A sample Resource Manager template that includes the DSC extension for Windows can be found on the [Azure Quick Start Gallery](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.automation/automation-configuration/nested/provisionServer.json#L91).

## Troubleshoot and support

### Troubleshoot

Data about the state of extension deployments can be retrieved from the Azure portal, and by using the Azure CLI. To see the deployment state of extensions for a given VM, run the following command using the Azure CLI.

```azurecli
az vm extension list --resource-group myResourceGroup --vm-name myVM -o table
```

Extension package is downloaded and deployed to this location on the Azure VM

```
C:\Packages\Plugins\{Extension_Name}\{Extension_Version}
```

Extension status file contains the sub status and status success/error codes along with the detailed error and description for each extension run.

```
C:\Packages\Plugins\{Extension_Name}\{Extension_Version}\Status\{0}.Status  -> {0} being the sequence number
```

Extension output logs are logged to the following directory:

```
C:\WindowsAzure\Logs\Plugins\{Extension_Name}\{Extension_Version}
```

### Error codes and their meanings

| Error Code | Meaning | Possible Action |
| --- | --- | --- |
| 1000 | Generic error | The message for this error is provided by the specific exception in extension logs |
| 52 | Extension Install Error | The message for this error is provided by the specific exception |
| 1002 | Wmf Install Error | Error while installing WMF. |
| 1004 | Invalid Zip Package | Invalid zip ; Error unpacking the zip |
| 1100 | Argument Error | Indicates a problem in the input provided by the user. The message for the error is provided by the specific exception |

### Support

If you need more help at any point in this article, you can contact the Azure experts on the [MSDN Azure and Stack Overflow forums](https://azure.microsoft.com/support/forums/). Alternatively, you can file an Azure support incident. Go to the [Azure support site](https://azure.microsoft.com/support/options/) and select Get support. For information about using Azure Support, read the [Microsoft Azure support FAQ](https://azure.microsoft.com/support/faq/).