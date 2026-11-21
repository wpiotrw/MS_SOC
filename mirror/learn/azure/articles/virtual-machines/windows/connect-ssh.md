---
layout: Conceptual
title: Connect using SSH to an Azure VM running Windows - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/windows/connect-ssh
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
author: kaza-sriram
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: migreene
ms.update-cycle: 365-days
description: Learn how to connect using Secure Shell and sign on to a Windows VM.
ms.service: azure-virtual-machines
ms.topic: how-to
ms.date: 2022-06-29T00:00:00.0000000Z
ms.custom: devx-track-azurepowershell, devx-track-azurecli
locale: en-us
document_id: 19d379b5-89e1-a347-adb7-aaab19068661
document_version_independent_id: 3d232c7e-e92b-0414-4caf-504198a07869
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/windows/connect-ssh.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
interactive_type: azurecli,azurepowershell
toc_rel: ../toc.json
asset_id: virtual-machines/windows/connect-ssh
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/windows/connect-ssh.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 6482a291-fc56-73b4-5a7c-1e1ad42d75b4
---

# Connect using SSH to an Azure VM running Windows - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Windows VMs ✔️ Flexible scale sets

The [Win32 OpenSSH](https://github.com/PowerShell/Win32-OpenSSH) project makes remote connectivity with Secure Shell ubiquitous by providing native support in Windows. The capability is provided in Windows Server version 2019 and later, and can be added to older versions of Windows using a virtual machine (VM) extension.

The examples below use variables. You can set variables in your environment as follows.

| Shell | Example |
| --- | --- |
| Bash/ZSH | myResourceGroup='resGroup10' |
| PowerShell | $myResourceGroup='resGroup10' |

## Enable SSH

First, you'll need to enable SSH in your Windows machine.

Deploy the SSH extension for Windows. The extension provides an automated installation of the Win32 OpenSSH solution, similar to enabling the capability in newer versions of Windows. Use the following examples to deploy the extension.

# [Azure CLI](#tab/azurecli)
```azurecli
az vm extension set --resource-group $myResourceGroup --vm-name $myVM --name WindowsOpenSSH --publisher Microsoft.Azure.OpenSSH --version 3.0
```

# [Azure PowerShell](#tab/azurepowershell-interactive)
```azurepowershell
Set-AzVMExtension -ResourceGroupName $myResourceGroup -VMName $myVM -Name 'OpenSSH' -Publisher 'Microsoft.Azure.OpenSSH' -Type 'WindowsOpenSSH' -TypeHandlerVersion '3.0'
```

# [ARM template](#tab/json)
```json
{
  "type": "Microsoft.Compute/virtualMachines/extensions",
  "name": "[concat(parameters('VMName'), '/WindowsOpenSSH')]",
  "apiVersion": "2020-12-01",
  "location": "[parameters('location')]",
  "properties": {
    "publisher": "Microsoft.Azure.OpenSSH",
    "type": "WindowsOpenSSH",
    "typeHandlerVersion": "3.0"
  }
}
```

# [Bicep](#tab/bicep)
```bicep
resource windowsOpenSSHExtension 'Microsoft.Compute/virtualMachines/extensions@2020-12-01' = {
  parent: virtualMachine
  name: 'WindowsOpenSSH'
  location: resourceGroup().location
  properties: {
    publisher: 'Microsoft.Azure.OpenSSH'
    type: 'WindowsOpenSSH'
    typeHandlerVersion: '3.0'
  }
}
```

---

## Open TCP port

Ensure the appropriate port (by default, TCP 22) is open to allow connectivity to the VM.

# [Azure CLI](#tab/azurecli)
```azurecli
az network nsg rule create -g $myResourceGroup --nsg-name $myNSG -n allow-SSH --priority 1000 --source-address-prefixes 208.130.28.4/32 --destination-port-ranges 22 --protocol TCP
```

# [Azure PowerShell](#tab/azurepowershell-interactive)
```azurepowershell
Get-AzNetworkSecurityGroup -Name $MyNSG -ResourceGroupName $myResourceGroup | Add-AzNetworkSecurityRuleConfig -Name allow-SSH -access Allow -Direction Inbound -Priority 1000 -SourceAddressPrefix 208.130.28.4/32 -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange 22 -Protocol TCP | Set-AzNetworkSecurityGroup
```

# [ARM template](#tab/json)
```json
{
  "type": "Microsoft.Network/networkSecurityGroups/securityRules",
  "apiVersion": "2021-08-01",
  "name": "allow-SSH",
  "properties": {
    "access": "Allow",
    "destinationAddressPrefix": "*",
    "destinationPortRange": "22",
    "direction": "Inbound",
    "priority": "1000",
    "protocol": "TCP",
    "sourceAddressPrefix": "208.130.28.4/32",
    "sourcePortRange": "*"
  }
}
```

# [Bicep](#tab/bicep)
```bicep
resource allowSSH 'Microsoft.Network/networkSecurityGroups/securityRules@2021-08-01' = {
  name: 'allowSSH'
  parent: MyNSGSymbolicName
  properties: {
    access: 'Allow'
    destinationAddressPrefix: '*'
    destinationPortRange: 'string'
    destinationPortRanges: [
      '22'
    ]
    direction: 'Inbound'
    priority: 1000
    protocol: 'TCP'
    sourceAddressPrefix: '208.130.28.4/32'
    sourcePortRange: '*'
  }
}
```

---

- Your VM must have a public IP address. To check if your VM has a public IP address, select **Overview** from the left menu and look at the **Networking** section. If you see an IP address next to **Public IP address**, then your VM has a public IP. To learn more about adding a public IP address to an existing VM, see [Associate a public IP address to a virtual machine](/en-us/azure/virtual-network/ip-services/associate-public-ip-address-vm)
- Verify your VM is running. On the Overview tab, in the essentials section, verify the status of the VM is Running. To start the VM, select **Start** at the top of the page.

## Authentication

You can authenticate to Windows machines using either username and password or SSH keys. Azure doesn't support provisioning public keys to Windows machines automatically, however you can copy the key using the RunCommand extension.

## Overview of SSH and keys

[SSH](https://www.ssh.com/ssh/) is an encrypted connection protocol that provides secure sign-ins over unsecured connections. Although SSH provides an encrypted connection, using passwords with SSH connections still leaves the VM vulnerable to brute-force attacks. We recommend connecting to a VM over SSH using a public-private key pair, also known as *SSH keys*.

- The *public key* is placed on your VM.
- The *private key* remains on your local system. Protect this private key. Do not share it.

When you use an SSH client to connect to your VM (which has the public key), the remote VM tests the client to make sure it has the correct private key. If the client has the private key, it's granted access to the VM.

Depending on your organization's security policies, you can reuse a single public-private key pair to access multiple Azure VMs and services. You do not need a separate pair of keys for each VM or service you wish to access.

Your public key can be shared with anyone, but only you (or your local security infrastructure) should have access to your private key.

## Supported SSH key formats

Azure currently supports following key types:

- SSH protocol 2 (SSH-2) RSA (Rivest, Shamir, Adleman) with a minimum length of 2048 bits
- ED25519 Keys with a fixed length of 256 bits

Other key formats such as Elliptic-curve Diffie–Hellman (ECDH) and Elliptic Curve Digital Signature Algorithm (ECDSA) are currently not supported.

### Copy a public key using the RunCommand extension.

The RunCommand extension provides an easy solution to copying a public key into Windows machines and making sure the file has correct permissions.

# [Azure CLI](#tab/azurecli)
```azurecli
az vm run-command invoke -g $myResourceGroup -n $myVM --command-id RunPowerShellScript --scripts "MYPUBLICKEY | Add-Content 'C:\ProgramData\ssh\administrators_authorized_keys' -Encoding UTF8;icacls.exe 'C:\ProgramData\ssh\administrators_authorized_keys' /inheritance:r /grant 'Administrators:F' /grant 'SYSTEM:F'"
```

# [Azure PowerShell](#tab/azurepowershell-interactive)
```azurepowershell
Invoke-AzVMRunCommand -ResourceGroupName $myResourceGroup -VMName $myVM -CommandId 'RunPowerShellScript' -ScriptString "MYPUBLICKEY | Add-Content 'C:\ProgramData\ssh\administrators_authorized_keys' -Encoding UTF8;icacls.exe 'C:\ProgramData\ssh\administrators_authorized_keys' /inheritance:r /grant 'Administrators:F' /grant 'SYSTEM:F'"
```

# [ARM template](#tab/json)
```json
{
  "type": "Microsoft.Compute/virtualMachines/runCommands",
  "apiVersion": "2022-03-01",
  "name": "[concat(parameters('VMName'), '/RunPowerShellScript')]",
  "location": "[parameters('location')]",
  "properties": {
    "timeoutInSeconds":600
    "source": {
      "script": "MYPUBLICKEY | Add-Content 'C:\\ProgramData\\ssh\\administrators_authorized_keys -Encoding UTF8';icacls.exe 'C:\\ProgramData\\ssh\\administrators_authorized_keys' /inheritance:r /grant 'Administrators:F' /grant 'SYSTEM:F'"
    }
  }
}
```

# [Bicep](#tab/bicep)
```bicep
resource runPowerShellScript 'Microsoft.Compute/virtualMachines/runCommands@2022-03-01' = {
  name: 'RunPowerShellScript'
  location: resourceGroup().location
  parent: virtualMachine
  properties: {
    timeoutInSeconds: 600
    source: {
      script: "MYPUBLICKEY | Add-Content 'C:\ProgramData\ssh\administrators_authorized_keys' -Encoding UTF8;icacls.exe 'C:\ProgramData\ssh\administrators_authorized_keys' /inheritance:r /grant 'Administrators:F' /grant 'SYSTEM:F'"
    }
  }
}
```

---

## Connect using Az CLI

Connect to Windows machines using `Az SSH` commands.

```azurecli
az ssh vm  -g $myResourceGroup -n $myVM --local-user $myUsername
```

It's also possible to create a network tunnel for specific TCP ports through the SSH connection. A good use case for this is Remote Desktop which defaults to port 3389.

```azurecli
az ssh vm  -g $myResourceGroup -n $myVM --local-user $myUsername -- -L 3389:localhost:3389
```

### Connect from Azure portal

1. Go to the [Azure portal](https://portal.azure.com/) to connect to a VM. Search for and select **Virtual machines**.
2. Select the virtual machine from the list.
3. Select **Connect** from the left menu.
4. Select the option that fits with your preferred way of connecting. The portal helps walk you through the prerequisites for connecting.