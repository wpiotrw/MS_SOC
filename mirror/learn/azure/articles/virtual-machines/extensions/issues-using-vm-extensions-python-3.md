---
layout: Conceptual
title: Issues using VM extensions in Python 3-enabled Linux Azure Virtual Machines systems - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/issues-using-vm-extensions-python-3
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
manager: dcscontentpm
ms.reviewer: wwilliams
description: Learn about using VM extensions in Python 3-enabled Linux systems
author: v-miegge
ms.author: jparrel
tags: top-support-issue,azure-resource-manager
ms.custom: devx-track-python, linux-related-content
ms.service: azure-virtual-machines
ms.subservice: extensions
ms.collection: linux
ms.topic: how-to
ms.date: 2026-11-23T00:00:00.0000000Z
locale: en-us
document_id: db5e2e62-b8fd-71e7-33c7-f0725aa9fda5
document_version_independent_id: 5d936c2a-b42f-885a-7cab-1db79714b621
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/extensions/issues-using-vm-extensions-python-3.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/extensions/issues-using-vm-extensions-python-3
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/extensions/issues-using-vm-extensions-python-3.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/837687b0-8846-4eb2-adb6-2b853e8c70c4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/8c797fa2-4419-46e7-a4e3-4c97d0a1f2a0
platformId: d1b6962e-d422-19a6-06f6-cc5a1e19c3bc
---

# Issues using VM extensions in Python 3-enabled Linux Azure Virtual Machines systems - Azure Virtual Machines | Microsoft Learn

This article explains why some Azure VM extensions fail to deploy on Python 3-enabled Linux systems and how to resolve issues with the legacy `/usr/bin/python` entrypoint.

Note

Microsoft encourages users to adopt **Python 3.x** in their systems unless your workload requires **Python 2.x** support. Examples of this requirement might include legacy administration scripts, or extensions such as **Azure Disk Encryption** and **Azure Monitor**.

Before installing **Python 2.x** in production, consider the question of long-term support of Python 2.x, particularly their ability to receive security updates. As products, including some of the extension mentioned, update with **Python 3.8** support, you should discontinue use of Python 2.x.

Some Linux distributions have transitioned to Python 3.8 and removed the legacy `/usr/bin/python` entrypoint for Python altogether. This transition impacts the out-of-the-box, automated deployment of certain virtual machine (VM) extensions with these two conditions:

- Extensions that are still transitioning to Python 3.x support
- Extensions that use the legacy `/usr/bin/python` entrypoint

Linux distribution users who have transitioned to **Python 3.x** must ensure the legacy `/usr/bin/python` entrypoint exists before attempting to deploy those extensions to their VMs. Otherwise, the extension deployment might fail.

- Endorsed Linux distributions that are affected include **Ubuntu Server 20.04 LTS** and **Ubuntu Pro 20.04 LTS**.
- Affected VM Extensions include **Azure Disk Encryption**, **Log Analytics**, **VM Access** (used for Password Reset), and **Guest Diagnostics** (used for additional performance counters).

In-place upgrades, such as upgrading from **Ubuntu 18.04 LTS** to **Ubuntu 20.04 LTS**, should retain the `/usr/bin/python` symlink, and remain unaffected.

Note

Try VM assist for faster diagnostics. We recommend that you run [VM assist for Windows](https://aka.ms/vmassistwindows) or [VM assist for Linux](https://aka.ms/vmassistlinux). These script-based diagnostic tools help you to identify common issues that affect the Azure VM Guest Agent and overall VM health.

If you're experiencing performance problems with virtual machines, before contacting support, run these tools.

## Resolution

Consider these general recommendations before deploying extensions in the known-affected scenarios described previously in the Summary:

1. Before deploying the extension, reinstate the `/usr/bin/python` symlink by using the Linux distribution vendor-provided method.

    - For example, for **Python 2.7**, use: `sudo apt update && sudo apt install python-is-python2`
2. This recommendation is for Azure customers and isn't supported in Azure Stack:

    - If you’ve already deployed an instance that exhibits this problem, use the Run command functionality in the VM blade to run the commands mentioned above. The Run command extension itself isn't affected by the transition to Python 3.8.
3. If you're deploying a new instance, and need to set an extension at provisioning time, use **cloud-init** user data to install the packages mentioned above.

    For example, for Python 2.7:

    ```python
    # create cloud-init config
    cat > cloudinitConfig.json <<EOF
    #cloud-config
    package_update: true
    
    runcmd:
    - sudo apt update
    - sudo apt install python-is-python2 
    EOF
    
    # create VM
    az vm create \
        --resource-group <resourceGroupName> \
        --name <vmName> \
        --image <Ubuntu 20.04 Image URN> \
        --admin-username azadmin \
        --ssh-key-value "<sshPubKey>" \
        --custom-data ./cloudinitConfig.json
    ```
4. If your organization’s policy administrators determine that extensions shouldn’t be deployed in VMs, you can disable extension support at provisioning time:

    - REST API

        To disable and enable extensions when you can deploy a VM with this property:

        ```python
          "osProfile": {
            "allowExtensionOperations": false
          },
        ```