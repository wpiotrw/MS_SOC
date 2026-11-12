---
layout: Conceptual
title: Set up data integration runtime Kubernetes in Unified Catalog (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-integration-runtime-kubernetes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-10-13T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
description: Learn how to set up data integration runtime Kubernetes for data quality in Microsoft Purview Unified Catalog (preview)
locale: en-us
document_id: 37e4c2dc-df5b-23cf-b7b0-1c1d8842a02c
document_version_independent_id: 37e4c2dc-df5b-23cf-b7b0-1c1d8842a02c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-integration-runtime-kubernetes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-integration-runtime-kubernetes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-integration-runtime-kubernetes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e1f6bb5c-2210-d9d4-839d-0f5db4961add
---

# Set up data integration runtime Kubernetes in Unified Catalog (preview) | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Microsoft Purview Data Quality for on-premises data sources enables organizations to assess, monitor, and improve the quality of data stored within internal systems such as databases and legacy platforms. It supports rule-based validation, error detection, and remediation workflows, while ensuring compliance with organizational policies. By integrating with existing infrastructure, it delivers consistent data quality insights and governance across both on-premises and cloud environments.

By using a self-hosted data integration runtime, you can scale data quality processes by securely connecting on-premises data sources to Purview. This article covers the Kubernetes-based, Linux self-hosted data integration runtime, which enhances the underlying infrastructure and provides several key benefits:

- Scalability: Ability to scale to hundreds of machines.
- Performance: Improved performance for scanning workloads.
- Security (containerized): Enables containerized deployment on a Kubernetes cluster, eliminating the need to host the data integration runtime directly on a Windows machine.

## Supported data sources

- Oracle
- SQL Server

## Architecture

At a high-level architectural view, when you install a Kubernetes-based data integration runtime, several pods are autocreated on the nodes of your Kubernetes cluster. A command line tool named DIRCTL triggers this installation. DIRCTL connects to the Microsoft Purview Service to register the data integration runtime and connect to the Kubernetes cluster to install the self-hosted data integration runtime. 

During the installation, the process downloads data integration runtime images from MCR (Microsoft Container Registries) to the data integration runtime pods. After installation is done, the pods in your cluster connect to the Purview service to pull scan jobs. As a scan job is pulled, it can connect your on-premises data source for Data Quality scanning.

![dir architecture](media/data-quality-virtual-network-support/dir-architecture.png)

## Prerequisites

### Data Integration Runtime Command Line tool (DIRCTL)

You need the Data Integration Runtime Command Line tool (DIRCTL) to set up data integration runtime. For download and installation instructions, see [Set up DIRCTL tool for self-hosted integration runtime (preview)](unified-catalog-data-integration-runtime-command-line-tool).

### Roles

To set up a self-hosted integrated runtime in Purview, you need the Data Governance Administrator role.

### Kubernetes cluster

You need an existing Linux-based Kubernetes cluster, or you need to prepare one. Identify the nodes by using a node selector, which follows the definition of Kubernetes node selector. Minimum configuration:

- Container type: Linux
- Kubernetes version: 1.24.9 or later
- Node OS: Linux based OS running on x86 architecture
- Node spec: minimal eight cores CPU, 32-GB memory, and at least 80 GB of available hard disk space
- Node count: 1 or more (fixed, not enabled cluster auto scaler)
- Pod number per Node: 20 or more (max Pod number – count of other Pods not belonging to Self-Hosted IR)

Note

The folder `/var/irstorage/` of each node is reserved for self-hosted integrated runtime. It's readable and writable to data integration runtime. You can get logs from this folder or upload external drivers to this folder. Data integration runtime creates the folder if it doesn't exist, and it doesn't delete the folder after data integration runtime is deleted. The container images used by data integration runtime are managed by [Kubernetes Garbage Collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#containers-images), which isn't cleaned up by data integration runtime. Configure the proper threshold for your Kubernetes cluster.

Outbound connectivity is required to pull in container images as well as for further operation, which includes activities such as pulling data quality jobs and pushing generated stats.

### Kubernetes context

Kubernetes context, which contains Kubernetes cluster information and user’s permissions and credential for this cluster, is needed to talk to your Kubernetes cluster. To ease the configuration for the user’s permissions for DIR management, you can start with Kubernetes Admin role. This context is generated with the setup of your Kubernetes cluster and saved in a config file. Where and how you can get this file depends on your setting up the Kubernetes cluster.

- If you use kubeadm init to set up the Kubernetes cluster, you can find the config file under `/etc/Kubernetes/admin.conf`.
- If you use AKS, you can follow the guidance of AKS to use Az PowerShell module command to get credentials of this cluster to your local machine. You can merge the context to the config file under `$HOME/.kube/config` directly.
- If you're using other tools setting up a Kubernetes cluster, refer to the [Kubernetes documentation](https://kubernetes.io/docs/home/).
- After you get the config file for the Kubernetes context, merge it into the config file `$HOME/.kube/config` on the machine where you want to run the IRCTL command. Or, you can set the config file of the Kubernetes context in an environment variable named `KUBECONFIG`. For more information about the Kubernetes context, see [how to configure access to multiple clusters](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/#set-the-kubeconfig-environment-variable).

## Set up a self-hosted data integration runtime

1. Go to **Settings** &gt; **Microsoft Purview Unified Catalog** &gt; **Data Integration Runtime**, and then select **New** to create a data integration runtime.
2. Enter a **Name** and **Description** for the self-hosted integrated runtime, and then select **Create**.

    ![create new data integration runtime](media/data-quality-virtual-network-support/new-data-integration-runtime.png)
3. Select **Generate key** to generate a registration key and register your data integration runtime.

    ![generate key](media/data-quality-virtual-network-support/generate-key.png)
4. Copy the key value and select **Done**.

    Tip

    If needed, you can regenerate a key or revoke a generated key.
5. Select **For Linux** to download the Data Integration Runtime Command Line (DIRCTL) tool. Get details on [how to install and manage DIRCTL](unified-catalog-data-integration-runtime-command-line-tool).

    ![download command line tool](media/data-quality-virtual-network-support/download-data-integration-runtime.png)
6. On the machine where you want to run the DIRCTL command line, install DIRCTL from the download. DIRCTL connects to your Kubernetes cluster by context of the Kube config. If you don't specify a context, DIRCTL uses the current context. You can set the context in one of two ways:

    1. Run `kubectl`command line and execute this command to confirm the current context:
        - `kubectl config get-contexts`: List all contexts configured on the machine
        - `kubectl config current-context`: Get the current context name
        - `kubectl config use-context <name of context>`
    2. Run DIRCTL and execute `-context` to specify the context in the Kube config.
7. Run the DIRCTL Create command: `./DIRCTL create - -registration-key <registration-key copied from the portal> `. The DIRCTL Create command registers a new data integration runtime with Data Quality and initiates the creation of an application in Kubernetes as a pod specific to the registered data integration runtime. It handles the provisioning of resources and configuration essential for data integration runtime functionality while maintaining compatibility with existing system requirements.

After registration finishes, you can check the status of the data integration runtime on the **Data Integration Runtime** page in **Settings**. The status is displayed as **Online**. You can also check the status of your data integration runtime by running this command: ` ./DIRCTL describe`.

Tip

These are the public endpoints that data integration runtime connects to that need to be allow listed:

- &lt;purview\_account\_name&gt;.purview.azure.com
- Mcr.microsoft.com
- \*.data.mcr.microsoft.com

## Create the namespace

1. Run the following command to create the namespace:

    ```bash
    kubectl create namespace dirctl
    ```
2. Create and apply the `rolebindingv2.yaml` file with the following content:

    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1 
    kind: RoleBinding 
    metadata:
      name: readwrite-mongodb-secret
      namespace: dirctl
    subjects:
    - kind: ServiceAccount
      name: default
      namespace: dirctl
    roleRef:
      kind: Role
      name: secret-manager
      apiGroup: rbac.authorization.k8s.io
    ```

    Apply the file:

    ```bash
    kubectl apply -f rolebindingv2.yaml
    ```
3. Create and apply the `secret-manager-role.yaml` file with the following content:

    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      namespace: dirctl
      name: secret-manager
    rules:
    - apiGroups: [""]
      resources: ["secrets"]
      verbs: ["get", "list", "create", "update", "patch", "delete"]
    - apiGroups: [""]
      resources: ["configmaps"]
      verbs: ["get", "list", "watch"]
    - apiGroups: ["apps"]
      resources: ["deployments"]
      verbs: ["get", "list", "watch","update"]
    ```

    Apply the file:

    ```bash
    kubectl apply -f secret-manager-role.yaml
    ```

## Set up on-premises data source connection with data integration runtime

### Connect to your Oracle database

Create connections by associating them with a data integration runtime instance.

- In Unified Catalog, go to **Health management** &gt; **Data quality**.
- Select the governance domain where you created your data product with Oracle data asset.
- Select **Manage**, and then select **Connection** to set up connection for your Oracle database.

Add the following information to set up the connection:

- Enter a **Display name** for the connection.
- Enter a **Description**.
- At **Source type**, select **Oracle**.
- Select the **Data integration runtime** that you created as part of the prerequisite.
- Enter the **Host** name.
- Enter the **Port** number.
- Enter the **Service name**.
- Enter the **Schema name**.
- Select an **Authentication method**.
- Enter the **Username**.
- At **Credential**, enter the **Azure subscription**, **Azure Key Vault connection**, **Secret name**, and **Secret version**.
- Select **Submit** to complete the connection setup.

Tip

If you don't have all the required information, select **Save as draft** to continue later when you have the rest of the information to complete the connection setup.

This image illustrates how to create a connection:

![oracle connection](media/dq-connectors/oracle-connection.png)

### Connect to your SQL Server database

Create connections by associating them with a data integration runtime instance, just like you do for Oracle. In SQL Server, a single database can contain tables belonging to multiple schemas, so you can use a single connection to scan all schemas in a single database. A connection accepts only database information but not schema. Create connections for SQL Server just like you do for other data source types.

- In Unified Catalog, go to **Health management** &gt; **Data quality**.
- Select the governance domain where you created your data product with Oracle data asset.
- Select **Manage**, and then select **Connection** to set up connection for your Oracle database.

Add the following information to set up connection successfully:

- Enter a **Display name** for the connection.
- Enter a **Description**.
- At **Source type**, select **SQL Server**.
- Select the **Data integration runtime** that you created as part of the prerequisite.
- Enter the **Server Endpoint**.
- Enter the **Database** name.
- Select an **Authentication method**.
- Enter the **Username**.
- At **Credential**, enter the **Azure subscription**, **Azure Key Vault connection**, and **Secret name**.
- Select **Submit** to complete the connection setup.

Tip

If you don't have all the required information, select **Save as draft** to continue later when you have the rest of the information to complete the connection setup.

This image illustrates how to create a connection:

![sqlserver connection](media/dq-connectors/sqlserver-connection.png)

## Data quality scan

After you complete the connection setup, follow data quality profiling and scanning documents to measure and monitor data quality of Oracle and SQL Server on-premises data sources.

- [Data quality overview](unified-catalog-data-quality)
- [Supported data sources](unified-catalog-data-quality-supported-sources-file-formats)
- [Set up data source connection](unified-catalog-data-quality-supported-sources-connection)
- [Data product quality scan](unified-catalog-data-quality-scan)
- [Data asset quality scan](unified-catalog-data-quality-scan-asset)
- [Incremental data quality scan](unified-catalog-data-quality-scan-incremental)

## High availability and scalability

Assign multiple nodes in the Kubernetes cluster for high availability by using the node selector during the installation of the Kubernetes supported self-hosted integration runtime. The benefits of having multiple nodes include:

- Higher availability of the self-hosted integration runtime so that it isn't a single point of failure for scans.
- More concurrent scans. Each node can handle many scan runs at the same time. You can manually scale out nodes of the Kubernetes cluster if you need more concurrent scans.
- When scanning some sources like Azure Blob, Azure Data Lake Storage Gen2, and Azure Files, each scan run can use multiple nodes to boost the scan performance. For other sources, scans run on only one of the nodes.

You can update the capabilities of the Kubernetes supported self-hosted integration runtime by manually scaling out or scaling in nodes of the Kubernetes cluster.

Note

You must upload all necessary drivers for scanning on each new node.

## Networking requirement

| Domain name | Outbound port | Description |
| --- | --- | --- |
| Public cloud: `<tenantID>-`api.purview-service.microsoft.com  Azure Government: `<tenantID>-`api.purview-service.microsoft.us  China: `<tenantID>-`api.purview-service.microsoft.cn | 443 | Required to connect to the Microsoft Purview service. If you use Microsoft Purview Private Endpoints, account private endpoint covers this endpoint. |
| Public cloud: `<purview_account>`.purview.azure.com  Azure Government: `<purview_account>`.purview.azure.us  China: `<purview_account>`.purview.azure.cn | 443 | Required to connect to the Microsoft Purview service. If you use Microsoft Purview Private Endpoints, account private endpoint covers this endpoint. |
| mcr.microsoft.com | 443 | Required to download images. |
| \*.data.mcr.microsoft.com | 443 | Required to download images. |