---
layout: Conceptual
title: Red Hat Enterprise Linux bring-your-own-subscription Azure images - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/redhat/byos
breadcrumb_path: ../../../breadcrumb/azure-compute/toc.json
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
ms.reviewer: divargas
description: Learn about bring-your-own-subscription images for Red Hat Enterprise Linux on Azure.
author: MarckK
ms.service: azure-virtual-machines
ms.subservice: redhat
ms.custom: devx-track-azurecli, linux-related-content, devx-track-azurepowershell
ms.collection: linux
ms.topic: concept-article
ms.date: 2024-10-23T00:00:00.0000000Z
ms.author: kdelamarck
locale: en-us
document_id: 8feaa3bf-2654-8f8a-6bec-e9021549103b
document_version_independent_id: 0dc2a245-19d8-99aa-210e-b6e8e082cebf
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/workloads/redhat/byos.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli,powershell
toc_rel: toc.json
asset_id: virtual-machines/workloads/redhat/byos
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/workloads/redhat/byos.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: cdbf3809-c7ec-43a7-8ca4-4744dd2c242e
---

# Red Hat Enterprise Linux bring-your-own-subscription Azure images - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs

Red Hat Enterprise Linux (RHEL) images are available in Azure via a pay-as-you-go or bring-your-own-subscription (BYOS) (Red Hat Gold Image) model. This article provides an overview of the Red Hat Gold Images in Azure.

Note

During December 2025, StoreAPI Engineering team identified an enforcement gap related to an existing business rule under which Private plans are not supported for CSP subscriptions. Although this rule had been in place for a long time, the enforcement was not functioning as intended. Once the issue was identified, Engineering team corrected the enforcement. Although this business rule has existed for some time, it might only now be surfacing for some customers due to corrected enforcement.

- CSP-led customers cannot purchase the BYOS offering via private plans. Instead, they should use private offers.
- For more information, see [CSP private offers](/en-us/partner-center/marketplace-offers/private-offers-for-channel#csp-private-offers).
- For more information, see [Private plans in Microsoft Marketplace](/en-us/partner-center/marketplace-offers/private-plans).

RHEL BYOS Gold Images are available in Azure Public (commercial) and Azure Government clouds. They're not available in Microsoft Azure operated by 21Vianet or Azure Blackforest clouds.

## Important points to consider

- The Red Hat Gold Images provided in this program are production-ready RHEL images similar to the RHEL pay-as-you-go images in Azure Marketplace.
- The images follow the current policies described in [Red Hat Enterprise Linux images on Azure](redhat-images).
- Standard support policies apply to VMs created from these images.
- The VMs provisioned from Red Hat Gold Images don't carry RHEL fees associated with RHEL pay-as-you-go images.
- The images are unentitled. You must use Red Hat Subscription-Manager to register and subscribe the VMs to get updates from Red Hat directly.
- It's possible to switch from pay-as-you-go images to BYOS using the [Azure Hybrid Benefit](../../linux/azure-hybrid-benefit-linux). To convert from RHEL BYOS to pay-as-you-go, follow the steps in [Azure Hybrid Benefit for bring-your-own-subscription Linux virtual machines](../../linux/azure-hybrid-benefit-byos-linux#get-started)

## Requirements and conditions to access the Red Hat Gold Images

1. Get familiar with the [Red Hat Cloud Access program](https://www.redhat.com/en/technologies/cloud-computing/cloud-access) terms. Enable your Red Hat subscriptions for Cloud Access at [Red Hat Subscription-Manager](https://access.redhat.com/management/cloud). You need to have on hand the Azure subscriptions that are going to be registered for Cloud Access.
2. If the Red Hat subscriptions you enabled for Cloud Access meet the eligibility requirements, your Azure subscriptions are automatically enabled for Gold Image access.

### Expected time for image access

After you finish the Cloud Access enablement steps, Red Hat validates your eligibility for the Red Hat Gold Images. If validation is successful, you receive access to the Gold Images within three hours.

## Use the Red Hat Gold Images from the Azure portal

1. After your Azure subscription receives access to Red Hat Gold Images, you can locate them in the [Azure portal](https://portal.azure.com). Go to **Create a Resource** &gt; **MarketPlace**.
2. At the top of the page, you'll see that you have private offers.

    ![Marketplace private offers](media/rhel-byos-privateoffers-2.png)
3. Select the purple link, or scroll down to the bottom of the page to see your private offers.
4. The rest of provisioning in the UI is no different to any other existing Red Hat image. Choose your RHEL version, and follow the prompts to provision your VM. This process also lets you accept the terms of the image at the final step.

Note

These steps so far won't enable your Red Hat Gold Image for programmatic deployment. An additional step is required as described in the "Additional information" section.

The rest of this document focuses on the CLI method to provision and accept terms on the image. The UI and CLI are fully interchangeable as far as the final result (a provisioned RHEL Gold Image VM) is concerned.

## Use the Red Hat Gold Images from the Azure CLI

The following instructions walk you through the initial deployment process for a RHEL VM by using the Azure CLI. These instructions assume that you have the [Azure CLI installed](/en-us/cli/azure/install-azure-cli).

Important

Make sure you use all lowercase letters in the publisher, offer, plan, and image references for all the following commands.

1. Check that you're in your desired subscription.

    ```azurecli
    az account show -o=json
    ```
2. Create a resource group for your Red Hat Gold Image VM.

    ```azurecli
    az group create --name <name> --location <location>
    ```
3. Accept the image terms.

    **Option 1:**

    ```azurecli
    az vm image terms accept --publisher redhat --offer rhel-byos --plan <SKU value here> -o=jsonc
    ```

    **Example:**

    ```azurecli
    az vm image terms accept --publisher redhat --offer rhel-byos --plan rhel-lvm87 -o=jsonc
    ```

    **Option 2:**

    ```azurecli
    az vm image terms accept --urn <SKU value here>
    ```

    **Example:**

    ```azurecli
    az vm image terms accept --urn RedHat:rhel-byos:rhel-lvm87:8.7.2023021503
    ```

    Note

    These terms need to be accepted *once per Azure subscription, per image SKU*.
4. (Optional) Validate your VM deployment with the following command:

    ```azurecli
    az vm create -n <VM name> -g <resource group name> --image <image urn> --validate
    ```

    Example:

    ```azurecli
    az vm create -n rhel-byos-vm -g rhel-byos-group --image redhat:rhel-byos:rhel-lvm8:latest --validate
    ```
5. Provision your VM by running the same command as shown in the previous example without the `--validate` argument.

    ```azurecli
    az vm create -n <VM name> -g <resource group name> --image <image urn>
    ```

    Example:

    ```azurecli
    az vm create -n rhel-byos-vm -g rhel-byos-group --image redhat:rhel-byos:rhel-lvm8:latest
    ```
6. SSH into your VM, and verify that you have an unentitled image. To do this step, run `sudo yum repolist`. For RHEL 8 or 9, use `sudo dnf repolist`. The output asks you to use Subscription-Manager to register the VM with Red Hat.

Note

On RHEL 8 and up, `dnf` and `yum` are interchangeable. For more information, see the [RHEL 8 admin guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/packaging_and_distributing_software/index).

## Use the Red Hat Gold Images from PowerShell

The following script is an example. Replace the resource group, location, VM name, login information, and other variables with the configuration of your choice. Publisher and plan information must be lowercase.

```powershell
    $resourceGroup = "testbyos"
    $location = "canadaeast"
    $vmName = "test01"

    # Define user name and blank password
    $securePassword = ConvertTo-SecureString 'TestPassword1!' -AsPlainText -Force
    $cred = New-Object System.Management.Automation.PSCredential("azureuser",$securePassword)
    Get-AzMarketplaceTerms -Publisher redhat -Product rhel-byos -Name rhel-lvm87
    Set-AzMarketplaceTerms -Accept  -Publisher redhat -Product rhel-byos -Name rhel-lvm87

    # Create a resource group
    New-AzResourceGroup -Name $resourceGroup -Location $location

    # Create a subnet configuration
    $subnetConfig = New-AzVirtualNetworkSubnetConfig -Name mySubnet -AddressPrefix 192.168.1.0/24

    # Create a virtual network
    $vnet = New-AzVirtualNetwork -ResourceGroupName $resourceGroup -Location $location -Name MYvNET -AddressPrefix 192.168.0.0/16 -Subnet $subnetConfig

    # Create a public IP address and specify a DNS name
    $pip = New-AzPublicIpAddress -ResourceGroupName $resourceGroup -Location $location -Name "mypublicdns$(Get-Random)" -AllocationMethod Static -IdleTimeoutInMinutes 4

    # Create an inbound network security group rule for port 22
    $nsgRuleSSH = New-AzNetworkSecurityRuleConfig -Name myNetworkSecurityGroupRuleSSH -Protocol Tcp  -Direction Inbound -Priority 1000 -SourceAddressPrefix * -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 22 -Access Allow

    # Create a network security group
    $nsg = New-AzNetworkSecurityGroup -ResourceGroupName $resourceGroup -Location $location -Name myNetworkSecurityGroup -SecurityRules $nsgRuleSSH

    # Create a virtual network card and associate with public IP address and NSG
    $nic = New-AzNetworkInterface -Name myNic -ResourceGroupName $resourceGroup -Location $location -SubnetId $vnet.Subnets[0].Id -PublicIpAddressId $pip.Id -NetworkSecurityGroupId $nsg.Id

    # Create a virtual machine configuration
    $vmConfig = New-AzVMConfig -VMName $vmName -VMSize Standard_D3_v2 |
    Set-AzVMOperatingSystem -Linux -ComputerName $vmName -Credential $cred |
    Set-AzVMSourceImage -PublisherName redhat -Offer rhel-byos -Skus rhel-lvm87 -Version latest |Add-AzVMNetworkInterface -Id $nic.Id
    Set-AzVMPlan -VM $vmConfig -Publisher redhat -Product rhel-byos -Name "rhel-lvm87"

    # Configure SSH Keys
    $sshPublicKey = Get-Content "$env:USERPROFILE\.ssh\id_rsa.pub"
    Add-AzVMSshPublicKey -VM $vmconfig -KeyData $sshPublicKey -Path "/home/azureuser/.ssh/authorized_keys"

    # Create a virtual machine
    New-AzVM -ResourceGroupName $resourceGroup -Location $location -VM $vmConfig
```

## Encrypt Red Hat Enterprise Linux bring-your-own-subscription Gold Images

Red Hat Enterprise Linux BYOS Gold Images can be secured through the use of [Azure Disk Encryption](../../linux/disk-encryption-overview). The subscription *must* be registered before you can enable encryption. For more information on how to register a RHEL BYOS Gold Image, see [How to register and subscribe a system to the Red Hat Customer Portal using Red Hat Subscription-Manager](https://access.redhat.com/solutions/253273). If you have an active Red Hat subscription, you can also read [Creating Red Hat Customer Portal Activation Keys](https://access.redhat.com/articles/1378093).

Azure Disk Encryption isn't supported on [Red Hat custom images](../../linux/redhat-create-upload-vhd). Additional Azure Disk Encryption requirements and prerequisites are documented in [Azure Disk Encryption for Linux VMs](../../linux/disk-encryption-overview#additional-vm-requirements).

For steps to apply Azure Disk Encryption, see [Azure Disk Encryption scenarios on Linux VMs](../../linux/disk-encryption-linux) and related articles.

## Additional information

- If you attempt to provision a VM on a subscription that isn't enabled for this offer, you get the following message:

    ```output
    "Offer with PublisherId: redhat, OfferId: rhel-byos, PlanId: rhel-lvm87 is private and can not be purchased by subscriptionId: GUID"
    ```

    In this case, contact Microsoft or Red Hat to enable your subscription.
- If you modify a snapshot from a RHEL BYOS image and attempt to publish that custom image to the [Azure Compute Gallery](../../shared-image-galleries) (formerly known as Shared Image Gallery), you must provide plan information that matches the original source of the snapshot. For example, the command might look like this:

    ```azurecli
    az vm create -image \
    "/subscriptions/GUID/resourceGroups/GroupName/providers/Microsoft.Compute/galleries/GalleryName/images/ImageName/versions/1.0.0" \
    -g AnotherGroupName --location EastUS2 -n VMName \
    --plan-publisher redhat --plan-product rhel-byos --plan-name rhel-lvm87
    ```

    Note the plan parameters in the final line.

    Azure Disk Encryption isn't supported on custom images.
- If you use automation to provision VMs from the RHEL BYOS images, you must provide plan parameters similar to what was shown in the sample commands. For example, if you use Terraform, you provide the plan information in a [plan block](https://www.terraform.io/docs/providers/azurerm/r/virtual_machine.html#plan).