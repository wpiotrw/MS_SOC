---
layout: Conceptual
title: IRCTL for Kubernetes Supported Self-hosted Integration Runtime | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-integration-runtime-kubernetes-irctl
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-10-11T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to install IRCTL and the commands available in the tool for managing your Microsoft Purview Kubernetes SHIR locally.
locale: en-us
document_id: 4c31eb17-5d64-8b32-9a09-f1dbfe73d681
document_version_independent_id: 4c31eb17-5d64-8b32-9a09-f1dbfe73d681
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-integration-runtime-kubernetes-irctl.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-integration-runtime-kubernetes-irctl
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-integration-runtime-kubernetes-irctl.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/d44a5346-5de4-439c-b804-7b2a536cbb55
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/da41a22b-b7a0-42d3-9c35-50da1c2b7b87
platformId: 6ace3653-5677-0a1a-a3c5-91541316d241
---

# IRCTL for Kubernetes Supported Self-hosted Integration Runtime | Microsoft Learn

In order to manage your Microsoft Purview Kubernetes SHIR locally, you need a command line tool named IRCTL. You can download this tool during the SHIR creation process. IRCTL is a command line tool to manage your Microsoft Purview SHIR.

## Prerequisites

The system requirements for IRCTL are:

- **Machine running IRCTL** - OS is Linux or Windows supporting TLS 1.2
- The machine to run IRCTL should be able to connect to the following endpoints:

| Domain name | Outbound ports | Description |
| --- | --- | --- |
| Public cloud: `*.compute.governance.azure.com`Azure Government: `*.compute.governance.azure.us`China: `*.compute.governance.azure.cn` | 443 | Required to connect to Microsoft Purview service. If you use Microsoft Purview Private Endpoints, this endpoint is covered by account private endpoint. |

- **Kubernetes context**: Kubernetes context, which contains Kubernetes cluster information and user’s permissions and credential for this cluster, is needed to talk to your Kubernetes cluster. To ease the configuration for the user’s permissions for SHIR management, you can start with Kubernetes Admin role. This context is generated with the setup of your Kubernetes cluster and saved in a config file. Where and how you can get this file depends on your setting up the Kubernetes cluster.
    - If you use `kubeadm init` to set up the Kubernetes cluster, you can find the config file under `/etc/Kubernetes/admin.conf`.
    - If you use AKS, you can follow the guidance of AKS to use Az PowerShell module command to get credentials of this cluster to your local machine. The context can be merged to the config file under `$HOME/.kube/config` directly.
    - If you're using other tools setting up a Kubernetes cluster, refer to the [Kubernetes documentation.](https://kubernetes.io/docs/home/)
    - As you have the config file of the Kubernetes context, merge it to the config file, which is `$HOME/.kube/config`, on the machine you would like to run IRCTL command. Or you can set the config file of the Kubernetes context in an environment variable named KUBECONFIG as well. For more information about the Kubernetes context, see [Configure Access to Multiple Clusters](https://Kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/#set-the-kubeconfig-environment-variable).

## Install and run IRCTL

To control and manage a Kubernetes supported self-hosted integration runtime, users can download a command line tool named IRCTL. Users can also monitor the status on the Portal by IRCTL and kubectl command line. The following are the steps to your Kubernetes supported self-hosted integration runtime.

# [Windows](#tab/windows)
## Specific version

To download a specific version of the IRCTL, change the version segment in the URL: `https://aka.ms/purview-irctl/irctl-windows-<version>.tar.gz`

For example for version 1.0.0: `https://aka.ms/purview-irctl/irctl-windows-1.0.0.tar.gz`

Available IRCTL versions can be found in the [IRCTL release notes](https://aka.ms/purview-irctl/releasenotes).

# [Linux](#tab/linux)
```Bash
wget https://aka.ms/purview-irctl/irctl-linux.tar.gz
```

## Specific version

To download a specific version of the IRCTL, change the version segment in the URL: `https://aka.ms/purview-irctl/irctl-linux-<version>.tar.gz`

For example for version 1.0.0: `https://aka.ms/purview-irctl/irctl-linux-1.0.0.tar.gz`

Available IRCTL versions can be found in the [IRCTL release notes](https://aka.ms/purview-irctl/releasenotes).

---

After you download the tool:

1. Unzip and open the tool folder.
2. Move it to a location on your machine where you can access it from the command line.
3. Open the command line and navigate to the folder where the IRCTL application is housed.
4. Use the below commands to interact with IRCTL and [follow these steps to install a Kubernetes supported integration runtime.](data-map-integration-runtime-kubernetes)

## IRCTL command details

You can download the IRCTL command line tool from your integration runtime settings in Microsoft Purview. Select your integration runtime and under **Settings** you can see the **Download IRCTL and install integration runtime** link. Select it to download the tool.

You can use the IRCTL command line to set up or manage a Kubernetes supported self-hosted integration runtime. Use this syntax to run IRCTL commands from your terminal window:

```bash
./irctl [command][flags]...
```

- **Command** specifies the operation you want to perform
- **Flags** specifies parameters for the operation

| Command | Description |
| --- | --- |
| config | Manages IRCTL configurations |
| create | Create a new SHIR resource |
| delete | Delete an SHIR resource |
| describe | Describes the SHIR running on the Kubernetes cluster |
| help | Provides help about any command |
| storage | Manage local storage reserved for SHIR |
| log | Manage logs of SHIR |
| upgrade | Upgrade an SHIR to the same version with IRCTL |

### Config

Manage IRCTL configurations.

```bash
./irctl config [flags]
./irctl config [command]
```

| Command | Description |
| --- | --- |
| set | Modify one SHIR configuration. |
| view | View all SHIR configurations. |

| Flag | Parameter type | Description |
| --- | --- | --- |
| -h,--help |  | Help for config |

#### Config set

Modify one self-hosted integration runtime configuration.

```bash
./irctl config set <config-name> <config-value> [flags]
```

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c, --context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used. |
| -h,--help |  | Help for config |

#### Config view

View all SHIR configurations.

```bash
./irctl 
```

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c, --context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used. |
| -h,--help |  | Help for config |

#### Allowed SHIR Configurations

| Config name | Config type | Valid values | Default value (value unset) | Description | Persists through reinstallation |
| --- | --- | --- | --- | --- | --- |
| autoUpdate.enabled | Boolean | true/false | true | Controls whether the current SHIR should be autoupdated. | Yes |

### Create

Create a new SHIR resource.

```bash
./irctl create [flags]
```

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c,--context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used |
| -h,--help |  | Help for create |
| -r,--registration-key | string | Key to register SHIR |
| -s,--selector | string | Node selector (label query) to filter on, supports '='. (for example,--selector key1=value1,key2=value2) Select nodes by given labels for SHIR to run on. Default is empty, which means SHIR runs on all nodes. |

Example:

```bash
./irctl create --registration-key 1234@keyvalue
```

### Upgrade

Upgrade an SHIR to the same version with IRCTL.

```bash
./irctl upgrade [flags]
./irctl upgrade [command]
```

| Command | Description |
| --- | --- |
| status | Monitors the status the latest SHIR upgrade. |

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c,--context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used |
| -h,--help |  | Help for upgrade |

### Delete

Delete an SHIR resource.

```bash
./irctl delete [flags]
```

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c,--context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used |
| -h,--help |  | Help for delete |

### Describe

Describe SHIR running on the Kubernetes cluster.

```bash
./irctl describe [flags]
```

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c,--context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used |
| -h,--help |  | Help for describe |

### Storage

Manage files in SHIR shared storage.

```bash
./irctl storage [flags]
./irctl storage [command]
```

| Command | Description |
| --- | --- |
| upload | Upload files to SHIR shared storage. |
| list | List files in SHIR shared storage. |
| delete | Delete files in SHIR shared storage. |

| Flag | Parameter type | Description |
| --- | --- | --- |
| -h,--help |  | Help for storage |

#### Storage upload

Upload files to SHIR shared storage.

```bash
./irctl storage upload -s <source> -d <destination> [flags]
```

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c,--context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used. |
| -d,--destination string | string | Path to store file/folder uploaded in SHIR shared storage. |
| -h,--help |  | Help for delete |
| -s,--source | string | Path to the file/folder to be uploaded. |

#### Storage list

List files in SHIR shared storage.

```bash
./irctl storage list <path> [flags]
```

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c,--context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used. |
| -h,--help |  | Help for list. |

#### Storage delete

Delete files in SHIR shared storage.

```bash
./irctl storage delete <path> [flags]
```

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c,--context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used. |
| -h,--help |  | Help for delete. |

### Log

Log operations from SHIR.

```bash
./irctl log [flags]
./irctl log [command]
```

| Command | Description |
| --- | --- |
| upload | Upload logs from SHIR. |
| download | Download logs from SHIR. |

| Flag | Parameter type | Description |
| --- | --- | --- |
| -h,--help |  | Help for log. |

#### Log upload

Upload logs from SHIR.

```bash
./irctl log upload [flags]
./irctl log upload [command]
```

| Command | Description |
| --- | --- |
| Status | Monitors the status of SHIR log uploading. |

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c,--context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used. |
| -h,--help |  | Help for upload. |
| -t,--timeout | int | Timeout for the log upload operation in seconds: [900, 3600]. Default is 900 seconds. (Default 900) |

#### Log download

Upload logs from SHIR.

```bash
./irctl log download [flags]
```

| Flag | Parameter type | Description |
| --- | --- | --- |
| -c,--context | string | Name of the Kubernetes context to use, if not specified, current context of Kube config is used. |
| -d,--destination | string | Local path to store logs downloaded from SHIR. |
| -h,--help |  | Help for download. |