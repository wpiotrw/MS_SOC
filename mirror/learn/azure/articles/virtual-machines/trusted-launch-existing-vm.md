---
layout: Conceptual
title: Enable Trusted launch on existing Gen2 VMs - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch-existing-vm
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
author: AjKundnani
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: ajkundna
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Learn how to enable Trusted launch on existing Azure Gen2 virtual machines (VMs).
ms.subservice: trusted-launch
ms.topic: how-to
ms.date: 2023-08-13T00:00:00.0000000Z
ms.custom:
- template-how-to
- devx-track-azurepowershell
- sfi-image-nochange
locale: en-us
document_id: 64a33175-bfa9-d22e-a581-cf47d72a7307
document_version_independent_id: b168a6a3-022d-2996-4101-dde31a832fdd
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/trusted-launch-existing-vm.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli,azurepowershell
toc_rel: toc.json
asset_id: virtual-machines/trusted-launch-existing-vm
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/trusted-launch-existing-vm.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 817397ba-7615-be45-d114-bf38f41a23ac
---

# Enable Trusted launch on existing Gen2 VMs - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VM ✔️ Windows VM

Azure Virtual Machines supports enabling Azure Trusted launch on existing [Azure Generation 2](generation-2) virtual machines (VM) by upgrading to the [Trusted launch](trusted-launch) security type.

[Trusted launch](trusted-launch) is a way to enable foundational compute security on [Azure Generation 2 VMs](generation-2) and protects against advanced and persistent attack techniques like boot kits and rootkits. It does so by combining infrastructure technologies like Secure Boot, virtual Trusted Platform Module (vTPM), and boot integrity monitoring on your VM.

Important

Support for enabling Trusted launch on existing Azure Generation 1 VMs is available. Refer to [Upgrade existing Azure Gen1 VMs to Gen2-Trusted launch](trusted-launch-existing-vm-gen-1).

## Prerequisites

Azure VM is configured with:

- [Trusted launch supported size family](trusted-launch#virtual-machines-sizes).
- [Trusted launch supported operating system (OS) version](trusted-launch#operating-systems-supported). For custom OS images or disks, the base image should be *Trusted launch capable*.
- For Arm64 VMs, use Trusted launch-capable Arm64 images from Azure Marketplace and a supported Arm64 size family. [Cobalt 100-based Arm64 sizes](sizes/cobalt-overview) support Trusted launch.
- Azure VM isn't using [features currently not supported with Trusted launch](trusted-launch#unsupported-features).
- Azure Backup, if enabled, for VMs should be configured with the [Enhanced Backup policy](/en-us/azure/backup/backup-azure-vms-enhanced-policy). The Trusted launch security type can't be enabled for VMs configured with *Standard policy*backup protection.
    - Existing Azure VM backup can be migrated from the *Standard* to the *Enhanced* policy. Follow the steps in [Migrate Azure VM backups from Standard to Enhanced policy (preview)](/en-us/azure/backup/backup-azure-vm-migrate-enhanced-policy).
- Azure site recovery (ASR), if enabled, **should be disabled** before upgrading the Gen2 VM to Trusted launch. After the upgrade, ASR can be re-enabled and reconfigured as needed. For more details, see documentation [Migrate Azure Site Recovery protected Azure Generation 2 VM to trusted VM](/en-us/azure/site-recovery/concepts-trusted-vm#migrate-azure-site-recovery-protected-azure-generation-2-vm-to-trusted-vm).

## Best practices

- Enable Trusted launch on a test Generation 2 VM and determine if any changes are required to meet the prerequisites before you enable Trusted launch on Generation 2 VMs associated with production workloads.
- [Create restore points](create-restore-points) for Azure Generation 2 VMs associated with production workloads before you enable the Trusted launch security type. You can use the restore points to re-create the disks and Generation 2 VM with the previous well-known state.
- *For Linux VMs*, validate secure boot compatibility using `SBInfo` tool. Refer to [Linux Trusted launch secure boot validation](trusted-launch-faq#linux-trusted-launch-virtual-machines) for distribution-based `SBInfo` installation commands.

## Enable Trusted launch on an existing VM

The following steps apply to both x64 and Arm64-based Generation 2 VMs when using Trusted launch-capable images.

Note

- These steps apply equally to x64 and Arm64 Gen2 VMs.
- vTPM is enabled by default.
- Secure boot isn't enabled by default. We strongly recommend that you enable Secure Boot, if you aren't using custom unsigned kernel or drivers. Secure Boot preserves boot integrity and enables foundational security for VMs.

# [Portal](#tab/portal)
Enable Trusted launch on an existing Azure Generation 2 VM by using the Azure portal.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Confirm that the VM generation is **V2** and select **Stop** for the VM.

    ![Screenshot that shows the Gen2 VM to be deallocated.](media/trusted-launch/02-generation-2-to-trusted-launch-stop-vm.png)
3. On the **Overview** page in the VM properties, under **Security type**, select **Standard**. The **Configuration** page for the VM opens.

    ![Screenshot that shows the Security type as Standard.](media/trusted-launch/03-generation-2-to-trusted-launch-click-standard.png)
4. On the **Configuration** page, under the **Security type** section, select the **Security type** dropdown list.

    ![Screenshot that shows the Security type dropdown list.](media/trusted-launch/04-generation-2-to-trusted-launch-select-dropdown.png)
5. Under the dropdown list, select **Trusted launch**. Select checkboxes to enable **Secure Boot** and **vTPM**. After you make the changes, select **Save**.

    Note

    - Generation 2 VMs created by using [Azure Compute Gallery (ACG)](azure-compute-gallery), [Managed image](capture-image-resource), or an [OS disk](scripts/create-vm-from-managed-os-disks) can't be upgraded to Trusted launch by using the portal. Ensure that the [OS version is supported for Trusted launch](trusted-launch#operating-systems-supported). Use PowerShell, the Azure CLI, or an Azure Resource Manager template (ARM template) to run the upgrade.

    ![Screenshot that shows the Secure Boot and vTPM settings.](media/trusted-launch/05-generation-2-to-trusted-launch-select-uefi-settings.png)
6. After the update successfully finishes, close the **Configuration** page. On the **Overview** page in the VM properties, confirm the **Security type** settings.

    ![Screenshot that shows the Trusted launch upgraded VM.](media/trusted-launch/06-generation-2-to-trusted-launch-validate-uefi.png)
7. Start the upgraded Trusted launch VM. Verify that you can sign in to the VM by using either the Remote Desktop Protocol (RDP) for Windows VMs or the Secure Shell Protocol (SSH) for Linux VMs.

# [CLI](#tab/cli)
Follow the steps to enable Trusted launch on an existing Azure Generation 2 VM by using the Azure CLI.

Make sure that you install the latest [Azure CLI](/en-us/cli/azure/install-az-cli2) and are signed in to an Azure account with [az login](/en-us/cli/azure/reference-index).

1. Sign in to the VM Azure subscription.

    ```azurecli
    az login
    
    az account set --subscription 00000000-0000-0000-0000-000000000000
    ```
2. Deallocate the VM.

    ```azurecli
    az vm deallocate \
       --resource-group myResourceGroup --name myVm
    ```
3. Enable Trusted launch by setting `--security-type` to `TrustedLaunch`.

    ```azurecli
    az vm update \
        --resource-group myResourceGroup --name myVm \
        --security-type TrustedLaunch \
        --enable-secure-boot true --enable-vtpm true
    ```
4. Validate the output of the previous command. Ensure that the `securityProfile` configuration is returned with the command output.

    ```json
    {
      "securityProfile": {
        "securityType": "TrustedLaunch",
        "uefiSettings": {
          "secureBootEnabled": true,
          "vTpmEnabled": true
        }
      }
    }
    ```
5. Start the VM.

    ```azurecli
    az vm start \
        --resource-group myResourceGroup --name myVm
    ```
6. Start the upgraded Trusted launch VM. Verify that you can sign in to the VM by using either RDP (for Windows VMs) or SSH (for Linux VMs).

# [PowerShell](#tab/powershell)
Follow the steps to enable Trusted launch on an existing Azure Generation 2 VM by using Azure PowerShell.

Make sure that you install the latest [Azure PowerShell](/en-us/powershell/azure/install-azps-windows) and are signed in to an Azure account with [Connect-AzAccount](/en-us/powershell/module/az.accounts/connect-azaccount).

1. Sign in to the VM Azure subscription.

    ```azurepowershell
    Connect-AzAccount -SubscriptionId 00000000-0000-0000-0000-000000000000
    ```
2. Deallocate the VM.

    ```azurepowershell
    Stop-AzVM -ResourceGroupName myResourceGroup -Name myVm
    ```
3. Enable Trusted launch by setting `-SecurityType` to `TrustedLaunch`.

    ```azurepowershell
    Get-AzVM -ResourceGroupName myResourceGroup -VMName myVm `
        | Update-AzVM -SecurityType TrustedLaunch `
            -EnableSecureBoot $true -EnableVtpm $true
    ```
4. Validate `securityProfile` in the updated VM configuration.

    ```azurepowershell
    # Following command output should be `TrustedLaunch`
    
    (Get-AzVM -ResourceGroupName myResourceGroup -VMName myVm `
        | Select-Object -Property SecurityProfile `
            -ExpandProperty SecurityProfile).SecurityProfile.SecurityType
    
    # Following command output should return `SecureBoot` and `vTPM` settings
    (Get-AzVM -ResourceGroupName myResourceGroup -VMName myVm `
        | Select-Object -Property SecurityProfile `
            -ExpandProperty SecurityProfile).SecurityProfile.Uefisettings
    
    ```
5. Start the VM.

    ```azurepowershell
    Start-AzVM -ResourceGroupName myResourceGroup -Name myVm
    ```
6. Start the upgraded Trusted launch VM. Verify that you can sign in to the VM by using either RDP (for Windows VMs) or SSH (for Linux VMs).

# [Template](#tab/template)
Follow the steps to enable Trusted launch on an existing Azure Generation 2 VM by using an ARM template.

An [Azure Resource Manager template](/en-us/azure/azure-resource-manager/templates/overview) is a JavaScript Object Notation (JSON) file that defines the infrastructure and configuration for your project. The template uses declarative syntax. You describe your intended deployment without writing the sequence of programming commands to create the deployment.

1. Review the template.

    ```json
    {
        "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
            "vmsToUpgrade": {
                "type": "object",
                "metadata": {
                    "description": "Specifies the list of Azure virtual machines to be upgraded to Trusted launch."
                }
            },
            "vTpmEnabled": {
                "type": "bool",
                "defaultValue": true,
                "metadata": {
                    "description": "Specifies whether vTPM should be enabled on the virtual machine."
                }
            }
        },
        "resources": [
            {
                "type": "Microsoft.Compute/virtualMachines",
                "apiVersion": "2022-11-01",
                "name": "[parameters('vmsToUpgrade').virtualMachines[copyIndex()].vmName]",
                "location": "[parameters('vmsToUpgrade').virtualMachines[copyIndex()].location]",
                "properties": {
                    "securityProfile": {
                        "uefiSettings": {
                            "secureBootEnabled": "[parameters('vmsToUpgrade').virtualMachines[copyIndex()].secureBootEnabled]",
                            "vTpmEnabled": "[parameters('vTpmEnabled')]"
                        },
                        "securityType": "TrustedLaunch"
                    }
                },
                "copy": {
                    "name": "vmCopy",
                    "count": "[length(parameters('vmsToUpgrade').virtualMachines)]"
                }
            }
        ]
    }
    ```
2. Edit the `parameters` JSON file with VMs to be updated with the `TrustedLaunch` security type.

    ```json
    {
        "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
            "vmsToUpgrade": {
                "value": {
                    "virtualMachines": [
                        {
                            "vmName": "myVm01",
                            "location": "westus3",
                            "secureBootEnabled": true
                        },
                        {
                            "vmName": "myVm02",
                            "location": "westus3",
                            "secureBootEnabled": true
                        }
                    ]
                }
            }
        }
    }
    ```

    **Parameter file definition**

    | Property | Description of property | Example template value |
    | --- | --- | --- |
    | vmName | Name of Azure Generation 2 VM. | `myVm` |
    | location | Location of Azure Generation 2 VM. | `westus3` |
    | secureBootEnabled | Enable Secure Boot with the Trusted launch security type. | `true` |
3. Deallocate all Azure Generation 2 VMs to be updated.

    ```azurepowershell
    Stop-AzVM -ResourceGroupName myResourceGroup -Name myVm01
    ```
4. Run the ARM template deployment.

    ```azurepowershell
    $resourceGroupName = "myResourceGroup"
    $parameterFile = "folderPathToFile\parameters.json"
    $templateFile = "folderPathToFile\template.json"
    
    New-AzResourceGroupDeployment `
        -ResourceGroupName $resourceGroupName `
        -TemplateFile $templateFile -TemplateParameterFile $parameterFile
    ```

    ![Screenshot that shows the Trusted launch properties of the VM.](media/trusted-launch/generation-2-trusted-launch-settings.png)

    ![Screenshot that shows the Trusted launch properties of the VM.](media/trusted-launch/generation-2-trusted-launch-settings.png)
5. Start the upgraded Trusted launch VM. Verify that you can sign in to the VM by using either RDP (for Windows VMs) or SSH (for Linux VMs).

---

## Roll back

To roll back changes from Trusted launch to the previous Gen2 known good configuration, set the `securityType` of the VM to **Standard**.

Important

Rolling back Trusted launch to Gen2 (Non-Trusted launch) configuration is a one-way operation. After you roll back to Gen2 (Non-Trusted launch) configuration, you can't re-enable Trusted launch on the same VM.

# [Portal](#tab/portal)
The Azure portal doesn't currently support rolling back Trusted launch to Gen2 (Non-Trusted launch) configuration.

# [Template](#tab/template)
To roll-back changes from Trusted launch to previous known good configuration, set `securityProfile` to **Standard** as shown in the sample template used for executing Trusted launch upgrade.

Note

Use Microsoft.Compute API version 2025-11-01+ to roll back changes from Trusted launch to Gen2 (Non-Trusted launch) configuration.

```json
"securityProfile": {
    "securityType": "Standard",
    "uefiSettings": "[null()]"
}
```

# [CLI](#tab/cli)
Follow the steps to disable Trusted launch on an existing Azure Generation 2 VM by using the Azure CLI.

Make sure that you install the latest [Azure CLI](/en-us/cli/azure/install-az-cli2) and are signed in to an Azure account with [az login](/en-us/cli/azure/reference-index).

Note

Use Azure CLI version 2.86.0 or later to roll back changes from Trusted launch to Gen2 (Non-Trusted launch) configuration.

1. Sign in to the VM Azure subscription.

    ```azurecli
    az login
    
    az account set --subscription 00000000-0000-0000-0000-000000000000
    ```
2. Deallocate the VM.

    ```azurecli
    az vm deallocate \
       --resource-group myResourceGroup --name myVm
    ```
3. Disable Trusted launch by setting `--security-type` to `Standard`.

    ```azurecli
    az vm update \
        --resource-group myResourceGroup --name myVm \
        --security-type Standard
    ```
4. Validate the output of the previous command. Ensure that the `securityProfile` configuration is returned with the command output.

    ```json
    {
      "securityProfile": {
        "securityType": null,
        "uefiSettings": null
      }
    }
    ```
5. Start the VM.

    ```azurecli
    az vm start \
        --resource-group myResourceGroup --name myVm
    ```

# [PowerShell](#tab/powershell)
To roll-back changes from Trusted launch to previous known good configuration, set `-SecurityType` to `Standard` as shown.

Note

Use Azure PowerShell version 15.6.1 or later to roll back changes from Trusted launch to Gen2 (Non-Trusted launch) configuration.

1. Sign in to the VM Azure subscription.

    ```azurepowershell
    Connect-AzAccount -SubscriptionId 00000000-0000-0000-0000-000000000000
    ```
2. Deallocate the VM.

    ```azurepowershell
    Stop-AzVM -ResourceGroupName myResourceGroup -Name myVm
    ```
3. Disable Trusted launch by setting `-SecurityType` to `Standard`.

    ```azurepowershell
    Get-AzVM -ResourceGroupName myResourceGroup -VMName myVm `
        | Update-AzVM -SecurityType Standard
    ```
4. Validate `securityProfile` in the updated VM configuration.

    ```azurepowershell
    # Following command output should be `null`
    
    (Get-AzVM -ResourceGroupName myVm -VMName myResourceGroup `
        | Select-Object -Property SecurityProfile `
            -ExpandProperty SecurityProfile).SecurityProfile.SecurityType
    ```
5. Start the VM.

    ```azurepowershell
    Start-AzVM -ResourceGroupName myResourceGroup -Name myVm
    ```

---

## Azure Advisor Recommendation

Azure Advisor populates an **Enable Trusted launch foundational excellence, and modern security for Existing Generation 2 VM(s)** operational excellence recommendation for existing Generation 2 VMs to adopt [Trusted launch](trusted-launch), a higher security posture for Azure VMs at no extra cost to you. Ensure Generation 2 VM has all prerequisites to migrate to Trusted launch, follow all the best practices including validation of OS image, VM Size, and creating restore points. For the Advisor recommendation to be considered complete, follow the steps outlined in the [**Enable Trusted launch on an existing VM**](trusted-launch-existing-vm#enable-trusted-launch-on-an-existing-vm) to upgrade the virtual machines security type and enable Trusted launch.

**What if there are Generation 2 VMs that don't fit the prerequisites for Trusted launch?**

For a Generation 2 VM that doesn't meet the prerequisites to upgrade to Trusted launch, look how to fulfill the prerequisites. For example, If using a virtual machine size not supported, look for an [equivalent Trusted launch supported size](trusted-launch#virtual-machines-sizes) that supports Trusted launch.

Note

Dismiss the recommendation if Gen2 virtual machine is configured with VM size families that are currently not supported with Trusted launch like MSv2-series.