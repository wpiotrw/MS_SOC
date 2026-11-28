---
layout: Conceptual
title: Upgrade existing Azure Gen1 VMs to Gen2 (Trusted launch) - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch-existing-vm-gen-1
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
description: Learn how to upgrade existing Azure Gen1 virtual machines (VMs) to Trusted launch.
ms.subservice: trusted-launch
ms.topic: how-to
ms.date: 2026-03-09T00:00:00.0000000Z
ms.custom: template-how-to, devx-track-azurepowershell
locale: en-us
document_id: 893a476c-5921-3219-090b-85a6013e19d1
document_version_independent_id: f8882311-65fb-ed61-17b3-c5dddb567608
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/trusted-launch-existing-vm-gen-1.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurepowershell,azurecli
toc_rel: toc.json
asset_id: virtual-machines/trusted-launch-existing-vm-gen-1
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/trusted-launch-existing-vm-gen-1.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: 321e35e7-6689-6e6d-6518-a3274bd06040
---

# Upgrade existing Azure Gen1 VMs to Gen2 (Trusted launch) - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VM ✔️ Windows VM ✔️ Generation 1 VM

Azure Virtual Machines supports upgrading Generation 1 virtual machines (VM) to [Generation 2](generation-2) by upgrading to the [Trusted launch](trusted-launch) security type.

[Trusted launch](trusted-launch) is a way to enable foundational compute security on [Azure Generation 2 VMs](generation-2) and protects against advanced and persistent attack techniques like boot kits and rootkits. It does so by combining infrastructure technologies like Secure Boot, virtual Trusted Platform Module (vTPM), and boot integrity monitoring on your VM.

Important

- *Upgrade of Gen1 VMs to Gen2 without enabling Trusted launch* is **not supported**.
- This upgrade path doesn't change the VM CPU architecture. To use Arm64 with Trusted launch, create a new VM from an Arm64 Trusted launch image in Azure Marketplace on supported [Cobalt 100 sizes](sizes/cobalt-overview) .

## Prerequisites

- Azure VM is configured with:
    - [Trusted launch supported size family](trusted-launch#virtual-machines-sizes).
    - [Trusted launch supported operating system (OS) version](trusted-launch#operating-systems-supported) (*excluding Windows Server 2016, Debian, Azure Linux*). For custom OS images or disks, the base image should be *Trusted launch capable*.
- Azure VM isn't using [features currently not supported with Trusted launch](trusted-launch#unsupported-features).
- Azure Backup, if enabled, for VMs should be configured with the [Enhanced Backup policy](/en-us/azure/backup/backup-azure-vms-enhanced-policy). The Trusted launch security type can't be enabled for VMs configured with *Standard policy*backup protection.
    - Existing Azure VM backup can be migrated from the *Standard* to the *Enhanced* policy. Follow the steps in [Migrate Azure VM backups from Standard to Enhanced policy](/en-us/azure/backup/backup-azure-vm-migrate-enhanced-policy).
- Azure site recovery (ASR), if enabled, **should be disabled** before upgrading the Gen1 VM to Trusted launch. After the upgrade, ASR can be re-enabled and reconfigured as needed. For more details, see documentation [Migrate Azure Site Recovery protected Azure Generation 2 VM to trusted VM](/en-us/azure/site-recovery/concepts-trusted-vm#migrate-azure-site-recovery-protected-azure-generation-2-vm-to-trusted-vm).
- Upgrade a test Gen1 VM to Trusted launch and determine if any changes are required to meet the prerequisites before you upgrade Gen1 VMs associated with production workloads to Trusted launch.
- Disable any *Windows OS volume encryption* including BitLocker before upgrade if enabled. All Windows OS volume encryptions should be re-enabled post successful upgrade. This action isn't required for data disks or Linux OS volume.

## Unsupported Gen1 VM configurations

Gen1 to Trusted launch VM upgrade is **NOT** supported if Gen1 VM is configured with:

- **Operating system**: Windows Server 2016, Azure Linux, Debian, and any other operating system not listed under [Trusted launch supported operating system (OS) version](trusted-launch#operating-systems-supported). For *Windows Server 2016 only*, workaround is to [update the Guest OS to Windows Server 2019 or 2022](windows-in-place-upgrade#perform-in-place-upgrade-to-windows-server-2016-2019-2022-or-2025).
- **VM size**: Gen1 VM configured with VM size not listed under [Trusted launch supported size families](trusted-launch#virtual-machines-sizes). As workaround, update the VM size to Trusted launch supported VM size family.
- **Azure Backup**: Gen1 VM configured with Azure Backup using *Standard policy*. As workaround, [migrate Gen1 VM backups from Standard to Enhanced policy](/en-us/azure/backup/backup-azure-vm-migrate-enhanced-policy).
- **BitLocker or equivalent encryption**: Windows Gen1 VM *guest OS volume* is encrypted using BitLocker or equivalent encryption technology. As workaround, disable Windows OS volume encryption before upgrade and re-enable post successful completion of Trusted launch upgrade.

## Best practices

Important

VM once upgraded to Trusted launch can't be rolled back to Gen1 configuration. It has to be fully recovered using Backup taken before upgrade.

- [Take full backup](/en-us/azure/backup/quick-backup-vm-portal) OR [Create restore points](create-restore-points) for Azure VMs associated with production workloads before you enable the Trusted launch security type. You can use the backup OR restore points to re-create the disks and VM with the previous Gen1 configuration well-known state.
- Review known issues and roll-back steps before executing Trusted launch upgrade.
- You won't be able to extend Windows OS disk system volume after `MBR to GPT conversion` as part of upgrade. Recommendation is to extend system volume for future before upgrading to Trusted launch.
- *Windows OS disk volume* should be defragmented using command `Defrag C: /U /V`. Defragmentation of OS volume reduces the risk of MBR (Master boot record) to GPT (GUID partition table) conversion failure by freeing up end of partitions. Refer to [defrag](/en-us/windows-server/administration/windows-commands/defrag).
- *For Linux VMs*, validate secure boot compatibility using `SBInfo` tool. Refer to [Linux Trusted launch secure boot validation](trusted-launch-faq#linux-trusted-launch-virtual-machines) for distribution-based `SBInfo` installation commands.

## Update Guest OS volume

[Generation 2](generation-2) VMs requires guest OS volume with following configurations:

- **GPT Disk layout**: Guest OS volume of Gen1 VMs is mostly set to `MBR` and requires to be updated to `GPT`
- **EFI system partition**: Guest OS volume of Gen1 VMs mostly doesn't include this partition.

Complete the update of OS volume with required configuration before upgrading Azure Gen1 VM to Trusted launch.

Important

- Upgrade a test Gen1 VM to Trusted launch and determine if any changes are required to meet the prerequisites before you upgrade Gen1 VMs associated with production workloads to Trusted launch.

# [Windows](#tab/windows)
Using in-built [MBR2GPT.exe](/en-us/windows/deployment/mbr-to-gpt) utility, you can enable `GPT` disk layout AND add `EFI system partition` required for Gen2 upgrade.

Caution

You won't be able to extend Windows OS disk system volume after `MBR to GPT conversion`. Recommendation is to extend system volume for future before executing the upgrade.

Note

Windows Server 2016 doesn't support `MBR2GPT.exe`. Workaround is to update the Guest OS to Windows Server 2019 or 2022 and followed by `MBR to GPT conversion`. Refer to [In-place upgrade for VMs running Windows Server in Azure](windows-in-place-upgrade#perform-in-place-upgrade-to-windows-server-2016-2019-2022-or-2025).

1. Remotely connect (using Remote desktop (RDP) or command-line) to Gen1 Windows VM for executing conversion.
2. Run command `MBR2GPT /validate /allowFullOS` and ensure `Disk layout validation` completes successfully. **Do not proceed** if the `Disk layout validation` fails. Refer to Known issues for list of common causes and associated resolution for failure. For more information and troubleshooting, see [MBR2GPT troubleshooting](/en-us/windows/deployment/mbr-to-gpt#troubleshooting).
3. Run command `MBR2GPT /convert /allowFullOS` to **execute** MBR to GPT conversion. Sample successful output:

    ```log
    If conversion is successful the disk can only be booted in GPT mode.
    These changes cannot be undone!
    
    MBR2GPT: Attempting to convert disk 0
    MBR2GPT: Retrieving layout of disk
    MBR2GPT: Validating layout, disk sector size is: 512 bytes
    MBR2GPT: Trying to shrink the OS partition
    MBR2GPT: Creating the EFI system partition
    MBR2GPT: Installing the new boot files
    MBR2GPT: Performing the layout conversion
    MBR2GPT: Migrating default boot entry
    MBR2GPT: Adding recovery boot entry
    MBR2GPT: Fixing drive letter mapping
    MBR2GPT: Conversion completed successfully
    MBR2GPT: Before the new system can boot properly you need to switch the firmware to boot to UEFI mode!
    ```

# [Linux](#tab/linux)
Important

Upgrade of existing Azure Gen1 Linux VMs to Trusted launch is **only supported** for VMs created using [supported OS](trusted-launch#operating-systems-supported) images published in Azure Marketplace (*excluding Debian, Azure Linux*).

Azure Gen1 Linux VMs created using endorsed distros (Canonical, RedHat (RHEL), SUSE) images published in [Azure Marketplace](https://azuremarketplace.microsoft.com/) don't require any change in Guest OS volume. That is, they already have `GPT` disk layout and `EFI system partition` configured. For other Azure Gen1 Linux VMs requiring this upgrade support including Azure Linux & Debian, submit registration at [Linux Gen1 to Trusted launch upgrade support](https://aka.ms/Gen1ToTLUpgrade).

Validate Guest OS volume readiness for Trusted launch upgrade with following commands. **DO NOT** proceed with Trusted launch upgrade if any of the validation step fails.

1. SSH or remotely connect to Gen1 Linux VM for executing validation commands.
2. Identify boot device and store in variable.`bootDevice=$(echo "/dev/$(sudo lsblk -no pkname $(sudo df /boot | awk 'NR==2 {print $1}'))")`
3. Check disk type of boot device. Output of command should return `gpt`.`sudo blkid $bootDevice -o value -s PTTYPE`
4. Validate if `EFI system partition` is available on boot volume. Output of command should return specific partition like `\dev\sda3`.`sudo fdisk -l $bootDevice | grep EFI | awk '{print $1}'`
5. Validate EFI mountpoint is configured. Output of command should return `/boot/efi present in /etc/fstab``sudo grep -qs '/boot/efi' /etc/fstab && echo '/boot/efi present in /etc/fstab' || echo '/boot/efi missing in /etc/fstab'`

---

## Upgrade Gen1 VM to Trusted launch

Note

- vTPM is enabled by default.
- Secure boot isn't enabled by default. We strongly recommend that you enable Secure Boot, if you aren't using custom unsigned kernel or drivers. Secure Boot preserves boot integrity and enables foundational security for VMs.

# [Portal](#tab/portal)
Enable Trusted launch on an existing Azure Generation 1 VM by using the Azure portal.

1. Complete the Guest OS Volume update.
2. Sign in to the [Azure portal](https://portal.azure.com).
3. Confirm that the VM generation is **V1** and ensure VM is **Running**.

    [![Screenshot that shows the Gen1 VM to be deallocated.](media/trusted-launch/generation-1-to-trusted-launch-stop-vm.png)](media/trusted-launch/generation-1-to-trusted-launch-stop-vm.png#lightbox)
4. On the **Overview** page in the VM properties, under **Security type**, select **Standard**. The **Configuration** page for the VM opens.

    [![Screenshot that shows the Security type as Standard.](media/trusted-launch/generation-1-to-trusted-launch-click-standard.png)](media/trusted-launch/generation-1-to-trusted-launch-click-standard.png#lightbox)
5. On the **Configuration** page, under the **Security type** section, select the **Security type** dropdown list.

    [![Screenshot that shows the Security type dropdown list.](media/trusted-launch/generation-1-to-trusted-launch-select-dropdown.png)](media/trusted-launch/generation-1-to-trusted-launch-select-dropdown.png#lightbox)
6. Under the dropdown list, select **Trusted launch**. Acknowledge that Guest OS Volume was updated & validated.

    [![Screenshot that shows the Validate guest OS volume button.](media/trusted-launch/generation-1-to-trusted-launch-validate-guest-os-volume.png)](media/trusted-launch/generation-1-to-trusted-launch-validate-guest-os-volume.png#lightbox)
7. Select checkboxes to enable **Secure Boot** and **vTPM**. After you make the changes, select **Save**.

    [![Screenshot that shows the Secure Boot and vTPM settings.](media/trusted-launch/generation-1-to-trusted-launch-select-secure-boot-settings.png)](media/trusted-launch/generation-1-to-trusted-launch-select-secure-boot-settings.png#lightbox)
8. VM needs to be **deallocated** to complete the upgrade. Confirm VM deallocate operation by clicking **Yes**.

    [![Screenshot that shows the VM deallocate confirmation prompt.](media/trusted-launch/generation-1-to-trusted-launch-deallocate-vm.png)](media/trusted-launch/generation-1-to-trusted-launch-deallocate-vm.png#lightbox)
9. After the update successfully finishes, close the **Configuration** page. On the **Overview** page in the VM properties, confirm the **Security type** settings.

    [![Screenshot that shows the Trusted launch upgraded VM.](media/trusted-launch/generation-1-to-trusted-launch-validate-secure-boot.png)](media/trusted-launch/generation-1-to-trusted-launch-validate-secure-boot.png#lightbox)
10. Start the upgraded Trusted launch VM. Verify that you can sign in to the VM by using either RDP (for Windows VMs) or SSH (for Linux VMs).

# [PowerShell](#tab/powershell)
Make sure that you install the latest [Azure PowerShell](/en-us/powershell/azure/install-azps-windows) and are signed in to an Azure account with [Connect-AzAccount](/en-us/powershell/module/az.accounts/connect-azaccount).

Follow the steps to upgrade existing Gen1 VM to Gen2 and enable Trusted launch by using Azure PowerShell.

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

# [CLI](#tab/cli)
Follow the steps to upgrade existing Gen1 VM to Gen2 and enable Trusted launch by using the Azure CLI.

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
    | vmName | Name of Azure VM. | `myVm` |
    | location | Location of Azure VM. | `westus3` |
    | secureBootEnabled | Enable Secure Boot with the Trusted launch security type. | `true` |
3. Deallocate all Azure VMs to be updated.

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

Azure VM once upgraded to Trusted launch can't be rolled back to Gen1 configuration. You can [disable Trusted launch](trusted-launch-existing-vm#roll-back) to roll-back VM from Trusted launch to Gen2 (Non-Trusted launch) configuration.

Use the Backup or Restore point of Gen1 VM taken before upgrade and restore entire VM along with disks to roll back fully to Gen1 VM.

Important

Roll back Trusted launch to Gen2 (Non-Trusted launch) configuration is a one-way operation. After you roll back to Gen2 (Non-Trusted launch) configuration, you can't re-enable Trusted launch on the same VM.

## Known issues

### VM image reference doesn't change post Trusted launch upgrade

Post upgrade of Azure Gen1 VM to Trusted launch, the image reference still reflects source as Gen1 OS image. Image reference not updated is a known limitation.

This limitation doesn't impacts the VM or hosted application functionality post Trusted launch upgrade. Following VM operations are impacted due to disconnect between image reference and running OS:

- **Guest patching**: For *Server* OS, [Automatic guest patching](automatic-vm-guest-patching) installs updates based on the image reference of VM.
- **Reimage**: Reimaging VM using Gen1 image reference post Trusted launch upgrade causes VM boot failure.

### Windows 11 boot fails after Trusted launch upgrade of Windows 10 VM

Windows 10 Gen1 VM is successfully upgraded to Trusted launch followed by successful Windows 11 in-place upgrade. However, the Windows 11 boot fails after Azure VM is stopped and started with error shown.

**Resolution**: This issue is fixed with [24H2 build version 26100.2314](/en-us/windows/release-health/windows11-release-information#windows-11-current-versions-by-servicing-option) and [23H2 build version 22631.5624](/en-us/windows/release-health/windows11-release-information#windows-11-current-versions-by-servicing-option).

![Screenshot that shows boot failure of Azure Windows VM.](media/trusted-launch/01-error-windows-11-boot.jpg)

Note

The upgrade can fail if you use outdated Windows 11 installation media. To avoid this issue, ensure you use the most recent Windows 11 image. You can download the latest ISO from the [Microsoft Software Download page](https://www.microsoft.com/software-download/windows11). If you have a volume licensing agreement, use the [Microsoft 365 admin center](https://admin.microsoft.com/adminportal/home#/subscriptions/vlnew) to access updated Windows 11 images.

### Windows Server 2022 boot fails after in-place upgrade of Trusted launch VM migrated from Gen1

Windows Server 2019 Gen1 VMs upgraded to Trusted launch followed by an in-place upgrade to Windows Server 2022 might fail to boot with **"The boot loader did not load an operating system"**. This issue is due to partition number mismatch in the UEFI boot entry after MBR-to-GPT conversion. The issue is fixed in Windows Server 2025 and later. Take a snapshot of the OS disk before performing the in-place upgrade.

### [Windows] MBR to GPT conversion fails with error Cannot find room for the EFI system partition

This error occurs for one of following reason:

- There's no free space available on the system volume
- System volume is corrupted. You can validate by trying to Shrink Volume by few MBs under Disk Management console. Use command `chkdsk C:/v/f` to repair system volume.
- `Virtual Disk` service isn't running or unable to communicate successfully. Service startup type should be set to `Manual`.
- `Optimize Drives` service isn't running or unable to communicate successfully. Service startup type should be set to `Manual`.
- System volume disk is already configured with four MBR partitions (maximum supported by MBR disk layout). You need to delete one of the partitions to make room for EFI system partition.
    1. Run `ReAgentc /info` to identify partition actively used by Recovery. Example: `Windows RE location:       \\?\GLOBALROOT\device\harddisk0\partition4\Recovery\WindowsRE`
    2. Run PowerShell cmdlet `Get-Partition -DiskNumber 0` to identify current partitions that are configured.
    3. Run PowerShell cmdlet `Remove-Partition -DiskNumber 0 -PartitionNumber X` to remove any extra Recovery partition not actively used by Recovery service as identified in Step 1.

### [Windows] MBR to GPT failed to update ReAgent.xml

For certain Windows OS versions like Windows 10, MBR2GPT generates pass-through error `MBR2GPT: Failed to update ReAgent.xml, please try to  manually disable and enable WinRE.`

The warning indicates that `MBR2GPT.exe` was unable to update Recovery partition GUID in `C:\Windows\System32\Recovery\ReAgent.xml`. This issue shouldn't cause issue with Guest OS functionality or further upgrade operations like Windows 11 Upgrade to succeed or Windows 11 to work properly post Upgrade. `ReAgent.xml` is updated with correct GUID post Windows 11 upgrade, that is, if you don’t take any action between MBR2GPT conversion & Windows 11 upgrade, the GUID value in `ReAgent.xml` is synced with Windows recovery configuration.

To manually fix The warning, you can disable and re-enable WinRE post MBR2GPT conversion or post Gen1 to Trusted launch upgrade before Windows 11 upgrade using listed steps, these steps forces sync the WinRE GUID in `ReAgent.xml`

1. Complete Gen1 -&gt; Trusted launch upgrade.
2. Run `reagentc /disable`
3. Run `reagentc /enable`
4. Run `reagentc /info`
5. Open `C:\Windows\System32\Recovery\ReAgent.xml` and validate BCD GUID in xml file is matching the output from Step 4.

### [Windows] D Drive assigned to System Reserved Post upgrade

Temporary storage Drive letter assignment 'D' is changed to 'E' with previous letter assigned to System Reserved post-upgrade of Gen1 VM. Execute below steps manually post-upgrade to work around the issue:

After the upgrade check the disks on the server, if system reserved partition has the letter D, do the following actions:

1. Reconfigure pagefile from D: to C:
2. Reboot the VM
3. Remove letter D: from the partition
4. Reboot the VM to show the temporary storage disk with D: letter

## Frequently asked questions

**What if there is Generation 1 VMs, that doesn't fit the prerequisites for Trusted launch?**

For a Generation 1 VM that doesn't meet the prerequisites to upgrade to Trusted launch, look how to fulfill the prerequisites. For example, If using a virtual machine size not supported, look for an [equivalent Trusted launch supported size](trusted-launch#virtual-machines-sizes) that supports Trusted launch.

**Why is upgrade to Generation 2 only (without Trusted launch) not supported?**

Trusted launch enables foundational compute security on [Azure Generation 2 VMs](generation-2) with no extra cost associated. Also, Trusted launch VMs are majorly on parity with Generation 2 VMs. Hence, there's no added benefit for upgrading only to Generation 2 VM without enabling Trusted launch.