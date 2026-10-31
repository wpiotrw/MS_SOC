---
layout: Conceptual
title: Create a Kubernetes Supported Self-hosted Integration Runtime | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-integration-runtime-kubernetes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-10-08T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand the steps to create and manage a Kubernetes supported self-hosted integration runtime in Microsoft Purview.
locale: en-us
document_id: ba050b83-4a95-1e05-a8cc-d2fdff179f48
document_version_independent_id: ba050b83-4a95-1e05-a8cc-d2fdff179f48
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-integration-runtime-kubernetes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-integration-runtime-kubernetes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-integration-runtime-kubernetes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: dd5e63e1-0d86-10df-e956-ebbce4111089
---

# Create a Kubernetes Supported Self-hosted Integration Runtime | Microsoft Learn

This article covers the details for the new SHIR feature that is Kubernetes-based for Linux that improves the underlying infrastructure to provide several benefits:

- **Scalability**: Ability to scale to hundreds of machines.
- **Performance**: Improved performance in scanning workloads.
- **Security** (containerized): Ability to have containerized security on a Kubernetes cluster, instead of hosting SHIR on a Windows machine directly

This article covers the details to install and manage a Kubernetes supported self-hosted integration runtime.

## Supported data sources

For a list of all supported sources, see the [supported data sources for each integration runtime table](data-map-integration-runtime-choose#supported-data-sources).

## Architecture

At a high-level architectural view, when a Kubernetes based SHIR is installed, several pods get autocreated on the nodes of users' Kubernetes cluster. This installation can be triggered by a command line tool named IRCTL (more detail in following sections). IRCTL connects to the Microsoft Purview Service to register the SHIR and connect to the Kubernetes cluster to install the SHIR. 

During the installation, SHIR images are downloaded from MCR (Microsoft Container Registries) to the SHIR pods. After installation is done, the pods in users’ cluster will connect to the Microsoft Purview Service to pull scan jobs. As a scan job is pulled, it can connect users’ on-premises Data Source for Data Scanning.

[![Infographic of the network architecture for the Kubernetes supported self-hosted integration runtime.](media/kubernetes-integration-runtime/architecture-inline.png)](media/kubernetes-integration-runtime/architecture.png#lightbox)

## Prerequisites

- A Microsoft Purview account using [enterprise](data-governance-free-version-upgrade-to-enterprise) data governance solutions.
- **Kubernetes cluster**: You need to have an existing Linux-based Kubernetes cluster or to prepare one. The nodes can be identified by node selector, which follows the definition of Kubernetes node selector. Minimum configuration:

    - Container type: Linux
    - Kubernetes version: 1.24.9 or above
    - Node OS: Linux based OS running on x86 architecture
    - Node spec: minimal eight cores CPU, 32-GB memory, and at least 80 GB of available hard disk space
    - Node count: &gt;=1 (should be fixed, **not** enable cluster auto scaler)
    - Pod number per Node: &gt;= 20 (max Pod number – count of other Pods not belonging to Self-Hosted IR)

    Note

    The folder /var/irstorage/ of each Node is reserved for SHIR. It is readable and writable to SHIR. You can get logs being persisted from this folder or upload external drivers to this folder. It will be created by SHIR if it doesn't exist, and it will not be deleted after SHIR being deleted. The container images used by SHIR are managed by [Kubernetes Garbage Collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#containers-images), which won't be cleaned-up by SHIR. Configure the proper threshold for your Kubernetes cluster.
- **Kubernetes cluster network**: The Kubernetes cluster you have should be able to connect to the endpoint listed in networking requirements.
- [**Integration runtime command line tool**](data-map-integration-runtime-kubernetes-irctl): In order manage your Microsoft Purview Kubernetes SHIR locally, you need a command line tool named IRCTL. You can download this tool during the SHIR creation process. IRCTL is a command line tool to manage your Microsoft Purview SHIR. For more information, see the [IRCTL documentation.](data-map-integration-runtime-kubernetes-irctl)

- **Kubernetes context**: Kubernetes context, which contains Kubernetes cluster information and user’s permissions and credential for this cluster, is needed to talk to your Kubernetes cluster. To ease the configuration for the user’s permissions for SHIR management, you can start with Kubernetes Admin role. This context is generated with the setup of your Kubernetes cluster and saved in a config file. Where and how you can get this file depends on your setting up the Kubernetes cluster.
    - If you use `kubeadm init` to set up the Kubernetes cluster, you can find the config file under `/etc/Kubernetes/admin.conf`.
    - If you use AKS, you can follow the guidance of AKS to use Az PowerShell module command to get credentials of this cluster to your local machine. The context can be merged to the config file under `$HOME/.kube/config` directly.
    - If you're using other tools setting up a Kubernetes cluster, refer to the [Kubernetes documentation.](https://kubernetes.io/docs/home/)
    - As you have the config file of the Kubernetes context, merge it to the config file, which is `$HOME/.kube/config`, on the machine you would like to run IRCTL command. Or you can set the config file of the Kubernetes context in an environment variable named KUBECONFIG as well. For more information about the Kubernetes context, see [Configure Access to Multiple Clusters](https://Kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/#set-the-kubeconfig-environment-variable).

## Create Kubernetes supported self-hosted integration runtime

To control and manage a Kubernetes SHIR, users can download a command line tool named [IRCTL](data-map-integration-runtime-kubernetes-irctl). The following are the steps to your Kubernetes supported self-hosted integration runtime.

The steps take you through downloading IRCTL, but for direct links, see the [IRCTL documentation.](data-map-integration-runtime-kubernetes-irctl#install-and-run-irctl)

### Set up a Kubernetes supported self-hosted integration runtime

1. Open the **Integration runtimes** window in the Microsoft Purview Data Map

    - If you're using the new [Microsoft Purview portal](purview-portal):
        1. Open the **Data Map**
        2. Select **Source management**
        3. Select **Integration runtimes**
    - If you're using the classic [Microsoft Purview governance portal](use-microsoft-purview-governance-portal):
        1. Open the **Data Map**
        2. Select **Integration runtimes**
2. Select the **+ New** button

    [![Screenshot of the integration runtimes window in the Microsoft Purview Data Map.](media/kubernetes-integration-runtime/new-integration-runtime-inline.png)](media/kubernetes-integration-runtime/new-integration-runtime.png#lightbox)
3. Select **Self-hosted** and then select **Continue**

    [![Screenshot of the new integration runtime window, with self-hosted selected.](media/kubernetes-integration-runtime/select-self-hosted-inline.png)](media/kubernetes-integration-runtime/select-self-hosted.png#lightbox)
4. Give your runtime a name, then select the **Kubernetes service support** toggle to enable

    [![Screenshot of the new integration runtime window with the Kubernetes toggle enabled.](media/kubernetes-integration-runtime/enable-kubernetes-service-support-inline.png)](media/kubernetes-integration-runtime/enable-kubernetes-service-support.png#lightbox)
5. Select **Create**
6. Select **Get registration key**

    [![Screenshot of the view integration runtime page with the Get registration key button highlighted.](media/kubernetes-integration-runtime/select-get-registration-key-inline.png)](media/kubernetes-integration-runtime/select-get-registration-key.png#lightbox)
7. Copy the key value. You need it to run commands in IRCTL later.

    Tip

    If needed, you can regenerate a key or revoke a generated key.
8. Select the **Download IRCTL and install integration runtime** link to download the IRCTL tool. ([You can also follow these steps to download IRCTL directly.](data-map-integration-runtime-kubernetes-irctl#install-and-run-irctl))
9. On the machine where you want to run the IRCTL command line, install IRCTL from the download. IRCTL connects to your Kubernetes cluster by context of the Kube config. If context isn't specified, IRCTL uses the current context. You can set the context in one of two ways:

    - Run kubectl command line and execute this command to confirm the current context:

        ```bash
        kubectl config get-contexts – List all contexts configured on the machine
        ```

        ```bash
        kubectl config current-context – Get the current context name
        ```

        ```bash
        kubectl config use-context <name of context>
        ```
    - Run IRCTL and execute `--context` to specify the context in the Kube config
10. Run the IRCTL command line and execute this command with the registration key you copied.

    ```bash
    ./irctl create --registration-key <registration key copied from the portal>
    ```

    Note

    If node selector isn't specified, will use all nodes of the Kubernetes cluster. For AKS, we suggest using the label of AKS node pool as the node selector or you can customize different labels to the SHIR nodes.
11. You see this printout:

    ```bash
    [Info] Start to create SHIR with Kubernetes context [your-context]......
    [Info] Environment validation passed!
    [Info] Registering SHIR[example-k8s-shir] for Microsoft Purview Account [yourpurviewaccount]......
    [Info] SHIR Registration done!
    [Info] Provisioning SHIR, it may take about 5-30 minutes......done!
    [Info] SHIR creation succeeded!  
    ```

    Tip

    If the installation progress is broken by Ctrl-C or other reasons, the following command can be used to monitor the installation progress: `./irctl install status`
12. Once installation is complete, to check the current status of the SHIR, run this command:

    ```bash
    ./irctl describe
    ```
13. You can also check the status of your SHIR in the Microsoft Purview portal, on the **Integration runtimes** page.

## Set up a scan with external drivers

When scanning some data sources, you need to install the corresponding driver on the machine where the SHIR is installed for Microsoft Purview to connect with the data source. Below is an example for Db2 scan. Refer to respective connector article for specific prerequisites.

Note

Data sources that need these external drivers have the information listed in their prerequisites.

In this example, we are installing the Db2 driver. Steps for other drivers are similar.

1. First, install the integration runtime.
2. Download the driver (each source has their individual driver listed.) For example, you can find the DB2 driver here: [Connect to and manage Db2](register-scan-db2#prerequisites).
3. Upload the driver to each node for your integration runtime. You can use a command like this:

    ```bash
    ./irctl storage upload --source jdbc_sqlj/db2_driver --destination driver/db2
    ```

    A successful upload confirmation looks like this:

    ```bash
    ========== Context ========== 
    Kubernetes Context             : k8s-shir-test-cluster 
    Purview Account                : test-purview-1 
    Self-hosted Intrgration Runtime: k8s-shir-demo 
    ========== Progress ========== 
    Processing 2/2 nodes... 
    aks-shirpool-27141791-vmss000000: SUCCEEDED 
    aks-shirpool-27141791-vmss000001: SUCCEEDED 
    ========== Results ========== 
    jdbc_sqlj/db2_driver -> /var/irstorage/driver/db2 
    ```

    Note

    If you replace nodes or scale out to new nodes, you need to upload the external driver again.
4. Verify the files uploaded with this command:

    ```bash
    ./irctl storage list driver/db2
    ```

    You should see a response like this:

    ```bash
    ========== Context ========== 
    Kubernetes Context             : k8s-shir-test-cluster 
    Purview Account                : test-purview-1 
    Self-hosted Intrgration Runtime: k8s-shir-demo 
    ========== Progress ========== 
    Processing 2/2 nodes... 
    aks-shirpool-27141791-vmss000000: SUCCEEDED 
    aks-shirpool-27141791-vmss000001: SUCCEEDED 
    ========== Results ========== 
    Node: aks-shirpool-27141791-vmss000000 - Succeeded 
    /var/irstorage/driver/db2 
    total 9364 
    drwxr-xr-x    2 root     root          4096 May 15 14:23 . 
    drwxr-xr-x    3 root     root          4096 May 15 14:23 .. 
    -rwxrwxr-x    1 root     root       6568346 May 15 14:23 db2jcc4.jar 
    Node: aks-shirpool-27141791-vmss000001 - Succeeded 
    /var/irstorage/driver/db2 
    total 9364 
    drwxr-xr-x    2 root     root          4096 May 15 14:23 . 
    drwxr-xr-x    3 root     root          4096 May 15 14:23 .. 
    -rwxrwxr-x    1 root     root       6568346 May 15 14:23 db2jcc4.jar 
    ```
5. Create scan with the value for **DriverLocation** with the **Destination** value from step 3.

    ![Screenshot of the scan setup window, showing the driver location listed as driver/db2.](media/kubernetes-integration-runtime/driver-location-example.png)

## High availability and scalability

You can assign multiple nodes of the Kubernetes cluster to have high availability by using the node-selector during the Kubernetes supported self-hosted integration runtime installation. The benefits of having multiple nodes are:

- Higher availability of the self-hosted integration runtime so that it's no longer the single point of failure for scans.
- Run more concurrent scans. Each node can empower many scan runs at the same time. You can manually scale out nodes of the Kubernetes cluster if you need more concurrent scans.
- When scanning some sources like Azure Blob, Azure Data Lake Storage Gen2, and Azure Files, each scan run can use multiple nodes to boost the scan performance. For other sources, scans are executed on only one of the nodes.

The capability of Kubernetes supported self-hosted integration runtime can be updated by manually scaling out/in nodes of the Kubernetes cluster.

Note

You must upload all necessary drivers for scanning on each new node.

## Networking requirements

| Domain name | Outbound ports | Description |
| --- | --- | --- |
| Public cloud: `<tenantID>-api.purview-service.microsoft.com`Azure Government: `<tenantID>-api.purview-service.microsoft.us`China: `<tenantID>-api.purview-service.microsoft.cn` | 443 | Required to connect to Microsoft Purview service. If you use Microsoft Purview Private Endpoints, this endpoint is covered by account private endpoint. |
| Public cloud: `<purview_account>.purview.azure.com`Azure Government: `<purview_account>.purview.azure.us`China: `<purview_account>.purview.azure.cn` | 443 | Required to connect to Microsoft Purview service. If you use Microsoft Purview Private Endpoints, this endpoint is covered by account private endpoint. |
| Public cloud: `<managed_storage_account>.blob.core.windows.net` or `<ingestion_storage_account>.*.blob.storage.azure.net`Azure Government: `<managed_storage_account>. blob.core.usgovcloudapi.net` or `<ingestion_storage_account>.   blob.core.usgovcloudapi.net`China: `<managed_storage_account>.blob.core.chinacloudapi.cn`or `<ingestion_storage_account>.blob.core.chinacloudapi.cn` | 443 | Required to connect to the Microsoft Purview managed Azure Blob storage account. |
| Public cloud: `<managed_storage_account>.queue.core.windows.net` or `<ingestion_storage_account>.*.queue.storage.azure.net`Azure Government: `<managed_storage_account>. queue.core.usgovcloudapi.net` or `<ingestion_storage_account>.   queue.core.usgovcloudapi.net`China: `<managed_storage_account>.queue.core.chinacloudapi.cn`or `<ingestion_storage_account>.queue.core.chinacloudapi.cn` | 443 | Required to connect to the Microsoft Purview managed Azure Queue storage account. |
| Public cloud: `*.compute.governance.azure.com`Azure Government: `*.compute.governance.azure.us`China: `*.compute.governance.azure.cn` | 443 | Required to connect to the Microsoft Purview service. Currently wildcard is required as there's no dedicated resource. |
| mcr.microsoft.com | 443 | Required to download images. |
| \*.data.mcr.microsoft.com | 443 | Required to download images. |

Note

Depending on the sources users want to scan, they also need to allow other domains and outbound ports for other Azure or external sources.

## Version

Typically, we release one new minor version of self-hosted integration runtime every month, which includes features, enhancements, and bug fixes.

Each version of the self-hosted integration runtime expires in one year.

### How to check the current version

You can check the version of your Kubernetes self-hosted integration runtime either on the portal, or with the IRCTL.

#### Portal

1. In the Microsoft Purview portal, navigate to the Data Map.
2. Select **Integration runtimes**
3. The fourth column in your integration runtime's description line will be **Version**, and you can check the version there.

#### IRCTL (1.1.0 and above)

The [describe command](data-map-integration-runtime-kubernetes-irctl#describe) returns the integration runtime's version.

```bash
./irctl describe
```

### Auto-update

Starting from version 1.1.0, the Kubernetes self-hosted integration runtime supports auto-update, which is enabled by default. This feature ensures your integration runtime is automatically upgraded to the latest Microsoft-managed version approximately once a month.

#### Opt-out

We recommend keeping auto-update enabled to benefit from the newest features and enhancements. However, you have the option to opt-out of auto-update using IRCTL. The auto-update configuration persists through reinstallation, so you don't need to disable it with each installation.

```bash
./irctl config set autoUpdate.enabled false
./irctl config view
```

#### Auto-update version vs latest version

To ensure stability, the auto-update is usually behind the latest version with a one-month delay. The auto-update version is managed by Microsoft.

If you would like to upgrade your integration runtime to newer versions, a manual upgrade should be performed with [IRCTL of the specific version](data-map-integration-runtime-kubernetes-irctl#specific-version).