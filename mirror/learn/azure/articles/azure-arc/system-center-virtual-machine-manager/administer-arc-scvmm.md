---
layout: Conceptual
title: Perform ongoing maintenance and administration for Azure Arc-enabled System Center Virtual Machine Manager - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/administer-arc-scvmm
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
description: Learn how to perform administrator operations related to Azure Arc-enabled System Center Virtual Machine Manager.
ms.topic: how-to
ms.date: 2026-09-24T00:00:00.0000000Z
ms.subservice: azure-arc-scvmm
ms.custom:
- devx-track-azurecli
- build-2025
ms.reviewer: v-gajeronika
locale: en-us
document_id: e39f3e7e-6fdb-70eb-f784-3a309a84cb81
document_version_independent_id: 685d9e27-9f2b-25e5-95f8-d31c47e7ca0e
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/system-center-virtual-machine-manager/administer-arc-scvmm.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/system-center-virtual-machine-manager/administer-arc-scvmm
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/system-center-virtual-machine-manager/administer-arc-scvmm.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/c89972e1-0a93-4ce3-b588-9c24d08ca424
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/b2144970-2aee-47fb-9df2-af491ca710ec
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: baacff22-847f-919c-983c-5cd6590dfc64
---

# Perform ongoing maintenance and administration for Azure Arc-enabled System Center Virtual Machine Manager - Azure Arc | Microsoft Learn

In this article, you learn how to perform various maintenance and administrative operations related to Azure Arc-enabled System Center Virtual Machine Manager (SCVMM), such as:

- Maintain the Azure Arc resource bridge manually by following the best practices.
- Update the SCVMM account credentials.
- Collect logs from the Azure Arc resource bridge.

Note

Azure Arc-enabled SCVMM retires in September 2029. If you're using Azure Arc-enabled SCVMM, transition to [Azure Arc-enabled Servers](/en-us/azure/azure-arc/servers/overview) or contact arc-vmm-feedback@microsoft.com. For more information, see the [transition guidance](transition-guidance).

## Best practices to maintain the Azure Arc-enabled SCVMM resources

The Azure Arc resource bridge connects the on-premises SCVMM management server to Azure. By using the components of the resource bridge, you can bring the benefits of Azure to your on-premises SCVMM managed virtual machines.

Follow these best practices as they fit your organization:

- **Securely maintain the `.yaml` and `kubeconfig` files**: After you successfully deploy the Azure Arc resource bridge, the process creates three configuration files: `\<resource-bridge-name\>-resource.yaml`, `\<resource-bridge-name\>-appliance.yaml`, and `\<resource-bridge-name\>-infra.yaml`. The resource bridge VM hosts a management Kubernetes cluster. By default, the deployment process generates a `kubeconfig` file in the current CLI directory to maintain the resource bridge VM. Securely store and maintain these files because you need them to manage and upgrade the resource bridge.
- **Resource bridge lock**: Because of the critical nature of the resource bridge, you can lock the Azure resource of the resource bridge to protect it from accidental deletion and prevent loss of connectivity to SCVMM server from Azure. To place a resource lock on your resource bridge, go to its Azure resource and select **Locks** under the **Settings** blade. You can add a **Delete** lock from here which prevents self-service users from accidentally deleting the resource bridge.

    Important

    Both Read-only and Delete type resource locks disable the upgrade of the resource bridge. Remove the locks before triggering an upgrade.
- **Resource bridge health alert**: To ensure the continuous functioning of the Azure Arc enabled SCVMM offering, maintain the Azure Arc resource bridge online and healthy with a *Running* status. The resource bridge can periodically go into an *offline* status due to rotation of credentials as part of your regular security practices or any change in the network. To be notified of any unintended downtime of the resource bridge, set up health alerts on the Azure resource of your resource bridge by following these steps:

    1. Sign in to the [Azure portal](https://portal.azure.com), search for **Service Health**, and navigate to it.
    2. In the left pane, select **Resource Health** &gt; **Resource Health**.
    3. In the **Subscription** dropdown, choose the subscription where your resource bridge is located. In the **Resource type** dropdown, select **Azure Arc Resource Bridge**. After the list of resource bridge is populated, choose the resource bridge for which you want to set up the alert and select **Add resource health alert**. If you want to set up alerts for all the resource bridges in your subscription, select **Add resource health alert** without choosing any resource bridges. This action adds health alerts for any resource bridges you deploy in the future.![Screenshot of Service Health.](media/administer-arc-scvmm/service-health.png)
    4. Configure the conditions in the alert rule depending on if you want to receive continuous notifications on the health status or if you want to receive notifications only when the resource bridge becomes unhealthy. To receive notifications only when the resource bridge becomes unhealthy, set the following conditions in the **Condition** tab:

        - **Event status**: Active
        - **Current resource status**: Unavailable
        - **Previous resource status**: Available
    5. In the **Actions** tab, configure the action group with the type of notification and the recipient of the alert.
    6. Complete creating the alert rule by filling in the details of the alert rule location, identifiers, and optional tags.

        Alternatively, you can create health alert from the Azure resource of your resource bridge.![Screenshot of resource health.](media/administer-arc-scvmm/resource-health.png)

## Update the SCVMM account credentials (using a new password or a new SCVMM account after onboarding)

Azure Arc-enabled SCVMM uses the SCVMM account credentials you provide during onboarding to communicate with your SCVMM management server. The Arc resource bridge VM stores these credentials locally.

As part of your security practices, you might need to rotate credentials for your SCVMM accounts. When you rotate credentials, update the credentials you provided to Azure Arc to ensure Azure Arc-enabled SCVMM continues functioning. You can also use the same steps if you need to use a different SCVMM account after onboarding. Make sure the new account has all the [required SCVMM permissions](quickstart-connect-system-center-virtual-machine-manager-to-arc#prerequisites).

The Arc resource bridge stores two different sets of credentials. You can use the same account credentials for both sets.

# [Account for Arc resource bridge](#tab/account-for-arc-resource-bridge)
Use this account to deploy the Arc resource bridge VM. Azure Arc uses this account for upgrade operations.

**Update the credentials for the account for Arc resource bridge**

To update the credentials for the account for Arc resource bridge, run the following Azure CLI commands. Run the commands from a workstation that can access the cluster configuration IP address of the Arc resource bridge locally:

```azurecli
az account set -s <subscription id>
az arcappliance get-credentials -n <name of the appliance> -g <resource group name> 
az arcappliance update-infracredentials scvmm --kubeconfig kubeconfig
```

For more information on the commands, see [`az arcappliance get-credentials`](/en-us/cli/azure/arcappliance#az-arcappliance-get-credentials) and [`az arcappliance update-infracredentials scvmm`](/en-us/cli/azure/arcappliance/update-infracredentials#az-arappliance-update-infracredentials-scvmm).

# [Account for SCVMM cluster extension](#tab/account-for-scvmm-cluster-extension)
Use this account to discover inventory and perform all the VM operations through Azure Arc-enabled SCVMM.

**Update the credentials used by the SCVMM cluster extension**

To update the credentials used by the SCVMM cluster extension on the resource bridge, run the following command. This command can be run from anywhere with the `connectedscvmm` CLI extension installed.

```azurecli
az scvmm vmmserver connect --custom-location <name of the custom location> --location <Azure region>  --name <name of the SCVMM resource in Azure>       --resource-group <resource group for the SCVMM resource>  --username   <username for the SCVMM account>  --password  <password to the SCVMM account>
```

---

## Collect logs from the Arc resource bridge

If you encounter any problems with the Azure Arc resource bridge, collect logs for further investigation. To collect the logs, use the Azure CLI [`Az arcappliance log`](/en-us/cli/azure/arcappliance/logs#az-arcappliance-logs-scvmm) command.

To save the logs to a destination folder, run the following commands. These commands need connectivity to cluster configuration IP address.

```azurecli
az account set -s <subscription id>
az arcappliance get-credentials -n <name of the appliance> -g <resource group name> 
az arcappliance logs scvmm --kubeconfig kubeconfig --out-dir <path to specified output directory>
```

If the Kubernetes cluster on the Azure Arc resource bridge isn't in functional state, you can use the following commands. These commands require connectivity to IP address of the Azure Arc resource bridge VM via SSH.

```azurecli
az account set -s <subscription id>
az arcappliance get-credentials -n <name of the appliance> -g <resource group name> 
az arcappliance logs scvmm --out-dir <path to specified output directory> --ip XXX.XXX.XXX.XXX
```