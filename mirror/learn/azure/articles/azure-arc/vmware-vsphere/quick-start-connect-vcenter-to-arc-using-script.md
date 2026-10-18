---
layout: Conceptual
title: Connect VMware vCenter Server to Azure Arc by using the helper script - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/vmware-vsphere/quick-start-connect-vcenter-to-arc-using-script
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: Jeronika-MS
learn_banner_products:
- azure
ms.author: v-gajeronika
ms.service: azure-arc
description: In this quickstart, you learn how to use the helper script to connect your VMware vCenter Server instance to Azure Arc.
ms.topic: quickstart
ms.date: 2026-10-04T00:00:00.0000000Z
ms.subservice: vmware-vsphere-azure-arc
ms.reviewer: v-gajeronika
locale: en-us
document_id: 9851604f-a846-d221-b83a-2bb1f16584fa
document_version_independent_id: d1440e41-f4ce-c2c6-a40f-feedf73b04ba
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/vmware-vsphere/quick-start-connect-vcenter-to-arc-using-script.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
interactive_type: powershell
toc_rel: toc.json
asset_id: azure-arc/vmware-vsphere/quick-start-connect-vcenter-to-arc-using-script
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/vmware-vsphere/quick-start-connect-vcenter-to-arc-using-script.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
platformId: 25cf4a9c-37af-4e40-f9fb-a373c9b9e8e3
---

# Connect VMware vCenter Server to Azure Arc by using the helper script - Azure Arc | Microsoft Learn

To start using the Azure Arc-enabled VMware vSphere features, you need to connect your VMware vCenter Server instance to Azure Arc. This quickstart shows you how to connect your VMware vCenter Server instance to Azure Arc by using a helper script.

First, the script deploys a virtual appliance called [Azure Arc resource bridge](../resource-bridge/overview) in your vCenter environment. Then, it installs a VMware cluster extension to provide a continuous connection between vCenter Server and Azure Arc.

Important

This article describes a way to connect a generic vCenter Server to Azure Arc. If you're trying to enable Arc for Azure VMware Solution (AVS) private cloud, follow this guide instead - [Deploy Arc-enabled VMware vSphere for Azure VMware Solution private cloud](/en-us/azure/azure-vmware/deploy-arc-for-azure-vmware-solution). With the Arc for AVS onboarding process you need to provide fewer inputs and Arc capabilities are better integrated into the AVS private cloud portal experience.

## Prerequisites

### Azure

- An Azure subscription.
- A resource group in the subscription where you have the *Owner*, *Contributor*, or *Azure Arc VMware Private Clouds Onboarding* role for onboarding.

### Azure Arc Resource Bridge

- Azure Arc resource bridge IP needs access to the URLs listed [here](support-matrix-for-arc-enabled-vmware-vsphere#resource-bridge-networking-requirements).

### vCenter Server

- vCenter Server version 8.
- A virtual network that provides internet access, directly or through a proxy. VMs on this network must communicate with the vCenter server on TCP port (usually 443).
- At least three free static IP addresses on the network.
- A resource pool or a cluster with a minimum capacity of 8 GB of RAM and 4 vCPUs.
- A datastore with a minimum of 200 GB of free disk space or 400 GB for High Availability deployment, available through the resource pool or cluster.

Note

Azure Arc-enabled VMware vSphere supports vCenter Server instances with a maximum of 9,500 virtual machines (VMs). If your vCenter Server instance has more than 9,500 VMs, don't use Azure Arc-enabled VMware vSphere.

### vSphere account

You need a vSphere account that can:

- Read all inventory.
- Deploy and update VMs to all the resource pools or clusters, networks, and VM templates that you want to use with Azure Arc.

Important

The Azure Arc-enabled VMware onboarding script prompts you to provide a vSphere account to deploy the Azure Arc resource bridge VM on the ESXi host. The process stores this account locally within the Azure Arc resource bridge VM and encrypts it as a Kubernetes secret at rest. The vSphere account allows Azure Arc-enabled VMware to interact with VMware vSphere. If your organization practices routine credential rotation, you must [update the credentials in Azure Arc-enabled VMware](/en-us/azure/azure-arc/vmware-vsphere/administer-arc-vmware?tabs=account-for-arc-resource-bridge#update-the-vsphere-account-credentials-using-a-new-password-or-a-new-vsphere-account-after-onboarding) to maintain the connection between Azure Arc-enabled VMware and VMware vSphere.

### Workstation

You need a Windows or Linux machine that can access both your vCenter Server instance and the internet, directly or through a proxy. The workstation must also have outbound network connectivity to the ESXi host backing the datastore. Datastore connectivity is needed for uploading the Arc resource bridge image to the datastore as part of the onboarding.

## Prepare vCenter Server

1. Create a resource pool with a reservation of at least 16 GB of RAM and four vCPUs. It should also have access to a datastore with at least 100 GB of free disk space.
2. Ensure that the vSphere accounts have the appropriate permissions.

## (Optional) Enable Arc gateway for Arc-enabled VMware vSphere (preview)

Note

Arc gateway for Arc-enabled VMware vSphere (preview) is optional and can be used to reduce the number of required endpoints that you must allow-list. For more information, see [Plan for deployment](support-matrix-for-arc-enabled-vmware-vsphere#resource-bridge-networking-requirements).

When you enable [Azure Arc gateway for Arc-enabled VMware vSphere (preview)](support-matrix-for-arc-enabled-vmware-vsphere#arc-gateway-for-arc-resource-bridge-on-arc-enabled-vmware-vsphere-preview), supported endpoint traffic routes to a single Azure Arc gateway endpoint instead of going to each individual required networking endpoint. This setup simplifies firewall configuration and improves onboarding and operational reliability.

To use Arc gateway (preview), you need an existing Arc gateway resource before running the Arc-enabled VMware vSphere onboarding script. The Arc-enabled VMware vSphere onboarding experience prompts you to use Arc gateway (preview). To enable Arc gateway for Arc-enabled VMware vSphere (preview), follow these steps:

1. Reuse or [create a new Arc gateway resource](../servers/arc-gateway#create-an-azure-arc-gateway-resource) and get its resource ID.
2. Run the Arc-enabled VMware vSphere onboarding script that you generate in the Azure portal (covered later in this article).
3. During the onboarding script execution, provide the Arc gateway resource ID when prompted to use Arc gateway.
4. Track the onboarding progress and confirm that the Arc gateway enablement is successful.

## Download the onboarding script

1. Go to [Azure portal](https://portal.azure.com).
2. Search for **Azure Arc** and select it.
3. Under **Supported environments**, select **VMware vCenter** and then **Add**.

    [![Screenshot that shows how to add VMware vCenter through Azure Arc.](media/quick-start-connect-vcenter-to-arc-using-script/add-vmware-vcenter.png)](media/quick-start-connect-vcenter-to-arc-using-script/add-vmware-vcenter.png#lightbox)
4. Select **Create a new resource bridge** and select **Next : Basics &gt;**.
5. Enter a name for **Azure Arc resource bridge**. For example: *contoso-nyc-resourcebridge*.
6. Select a subscription and resource group where you want to create the resource bridge.
7. Under **Region**, select an Azure location where you want to store the resource metadata.
8. Enter a name for **Custom location**. This is the name that you see when you deploy virtual machines. Name it for the datacenter or the physical location of your datacenter. For example: *contoso-nyc-dc.*
9. Leave the option **Use the same subscription and resource group as your resource bridge** selected.
10. Enter a name for your vCenter Server instance in Azure. For example: **contoso-nyc-vcenter**.
11. Select **Next: Tags &gt;**.
12. Assign Azure tags to your resources in **Value** under **Physical location tags**. You can add extra tags to help you organize your resources and make administrative tasks easier by using custom tags.
13. Select **Next: Download and run script**.
14. If your subscription isn't registered with all the required resource providers, a **Register** button appears. Select the button before you proceed to the next step.

    ![Screenshot that shows the button to register required resource providers during vCenter onboarding to Azure Arc.](media/quick-start-connect-vcenter-to-arc-using-script/register-arc-vmware-providers.png)
15. Based on the operating system of your workstation, download the PowerShell or Bash script and copy it to the workstation.

## Run the script

Use the following instructions to run the script, depending on which operating system your machine is using.

### Windows

1. Open a PowerShell window as an administrator and go to the folder where you downloaded the PowerShell script.

    Note

    On Windows workstations, run the script in a PowerShell window. Don't use the PowerShell Integrated Script Editor (ISE) because PowerShell ISE doesn't display the input prompts from Azure CLI commands. If you run the script on PowerShell ISE, it might seem like the script is stuck while it's waiting for input.
2. Run the following command to allow the script to run, because it's an unsigned script. If you close the session before you complete all the steps, run this command again for the new session.

    ```powershell
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    ```
3. Run the script:

    ```powershell
    ./resource-bridge-onboarding-script.ps1
    ```

### Linux

1. Open the terminal and go to the folder where you downloaded the Bash script.
2. Run the script by using the following command:

    ```sh
    bash resource-bridge-onboarding-script.sh
    ```

## Inputs for the script

A typical onboarding that uses the script takes 30 to 60 minutes. During the process, the script prompts you for the following details:

| **Requirement** | **Details** |
| --- | --- |
| **Azure login** | When prompted, go to the [device sign-in page](https://www.microsoft.com/devicelogin), enter the authorization code shown in the terminal, and sign in to Azure. |
| **vCenter FQDN/Address** | Enter the fully qualified domain name for the vCenter Server instance (or an IP address). For example: **10.160.0.1** or **nyc-vcenter.contoso.com**. |
| **vCenter Username** | Enter the username for the vSphere account. The required permissions for the account are listed in the prerequisites. You can scope the VMware vCenter resources that you want Azure to discover by customizing the scope of this account. |
| **vCenter password** | Enter the password for the vSphere account. |
| **Data center selection** | Select the name of the datacenter (as shown in the vSphere client) where the Azure Arc resource bridge VM should be deployed. |
| **Network selection** | Select the name of the virtual network or segment to which the Azure Arc resource bridge VM must be connected. This network should allow the appliance to communicate with vCenter Server and the Azure endpoints (or internet). |
| **Static IP** | Arc Resource Bridge requires static IP address assignment and DHCP isn't supported.  1. **Static IP address prefix**: Network address in CIDR notation. For example: **192.168.0.0/24**.  2. **Static gateway**: Gateway address. For example: **192.168.0.0**.  3. **DNS servers**: IP addresses of DNS servers used by Azure Arc resource bridge VM for DNS resolution. Azure Arc resource bridge VM must be able to resolve external sites, like mcr.microsoft.com and the vCenter server.  4. **Start range IP**: Minimum size of two available IP addresses is required. One IP address is for the Azure Arc resource bridge VM, and the other is reserved for upgrade scenarios. Provide the starting IP address of that range. Ensure the Start range IP has internet access.  5. **End range IP**: Last IP address of the IP range requested in the previous field. Ensure the End range IP has internet access. |
| **Control Plane IP address** | Azure Arc resource bridge runs a Kubernetes cluster, and its control plane always requires a static IP address. Provide an IP address that meets the following requirements:  - The IP address must have internet access.  - The IP address must be within the subnet defined by IP address prefix.  - If you're using static IP address option for resource bridge VM IP address, the control plane IP address must be outside of the IP address range provided for the VM (Start range IP - End range IP). |
| **Resource pool** | Select the name of the resource pool to which the Azure Arc resource bridge VM will be deployed. |
| **Data store** | Select the name of the datastore to be used for the Azure Arc resource bridge VM. |
| **Folder** | Select the name of the vSphere VM and the template folder where the Azure Arc resource bridge's VM will be deployed. |
| **Appliance proxy settings** | Enter **y** if there's a proxy in your appliance network. Otherwise, enter **n**.  You need to populate the following boxes when you have a proxy set up:  1. **Http**: Address of the HTTP proxy server.  2. **Https**: Address of the HTTPS proxy server.  3. **NoProxy**: Addresses to be excluded from the proxy.  4. **CertificateFilePath**: For SSL-based proxies, the path to the certificate to be used. |
| **(Optional) Arc gateway resource ID (preview)** | Provide the resource ID of the Arc gateway Azure resource. This resource ID is used by the Arc gateway router in the Arc resource bridge to direct supported networking endpoints to the Arc gateway. |

After the command finishes running, your setup is complete. You can now use the capabilities of Azure Arc-enabled VMware vSphere.

Important

After the successful installation of Azure Arc Resource Bridge, it's recommended to retain a copy of the resource bridge config.yaml files in a place that facilitates easy retrieval. These files could be needed later to run commands to perform management operations (e.g. [az arcappliance upgrade](/en-us/cli/azure/arcappliance/upgrade#az-arcappliance-upgrade-vmware)) on the resource bridge. You can find the three .yaml files (config files) in the same folder where you ran the script.

## Recovering from failed deployments

If the Azure Arc resource bridge deployment fails, consult the [Azure Arc resource bridge troubleshooting document](../resource-bridge/troubleshoot-resource-bridge). While many reasons can cause deployment failure, one common reason is a KVA timeout error. For more information about the KVA timeout error and how to troubleshoot it, see [KVA timeout error](../resource-bridge/troubleshoot-resource-bridge#kva-timeout-error).

To clean up the installation and retry the deployment, use the following commands.

### Retry command - Windows

Run the command with `-Force` to clean up the installation and onboard again.

```powershell
./resource-bridge-onboarding-script.ps1 -Force
```

### Retry command - Linux

Run the command with `--force` to clean up the installation and onboard again.

```bash
bash resource-bridge-onboarding-script.sh --force
```