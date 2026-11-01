---
layout: Conceptual
title: Troubleshoot Data Integration Runtime and DIRCTL for Unified Catalog (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-integration-runtime-troubleshoot
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-04-09T00:00:00.0000000Z
audience: Admin
ms.topic: troubleshooting
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Troubleshoot data integration runtime and the DIRCTL tool to resolve setup and configuration issues when using data quality in Microsoft Purview Unified Catalog (preview).
locale: en-us
document_id: 967fa7d3-e797-b63b-b638-9d11a894892e
document_version_independent_id: 967fa7d3-e797-b63b-b638-9d11a894892e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-integration-runtime-troubleshoot.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-integration-runtime-troubleshoot
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-integration-runtime-troubleshoot.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5402aafe-0c4b-7fcc-510f-04e08fbae538
---

# Troubleshoot Data Integration Runtime and DIRCTL for Unified Catalog (preview) | Microsoft Learn

This article helps you resolve common setup and configuration issues with the data integration runtime and the DIRCTL command-line tool in Microsoft Purview Unified Catalog. For setup instructions, see [Set up a Kubernetes self-hosted data integration runtime](unified-catalog-data-integration-runtime-kubernetes). Learn how to [download, install, and manage DIRCTL](unified-catalog-data-integration-runtime-command-line-tool).

## Verify prerequisites

Before deployment, verify the following prerequisites to avoid setup errors:

- Linux machine with Kubernetes installed
- Hardware requirements. Minimum specs:
    - CPU – eight cores
    - RAM – 32 GB
    - HDD – 80 GB
- Kubernetes tools
    - To access the `K8s` cluster from a Windows machine, install Kubectl.
    - To check the installation, run: `kubectl version --client`
- Permissions: You need the Data Governance Administrator role to run the DIRCTL CLI tool.

### Networking: Firewall and ports

| Domain Name | Outbound Ports | Description |
| --- | --- | --- |
| Public cloud: https:`//<purview_account>`.purview.azure.com  https:`//mcr.microsoft.com` | 443 | Required to connect to Microsoft Purview service. If you use Microsoft Purview private endpoints, the account private endpoint covers this endpoint. |

## Common issues and solutions

### Issue 1: Kubernetes setup isn't available

If you don't have a Kubernetes cluster set up, follow these steps to prepare the environment. You can set up Kubernetes in two ways:

1. Install Kubernetes on any Linux-based virtual machine, such as Ubuntu; or
2. Enable Hyper-V on an existing Windows Server, create a Linux-based virtual machine, and install Kubernetes.

### Issue 2: Data integration runtime can't reach the database

#### Cause

Data integration runtime and the database might be running on different machines or networks. As a result, you might see this error message as the failure reason:

`TNS: destination host unreachable.`

#### Resolution

Ensure that the firewall in the database network allows inbound traffic on the configured database listener port from the IP address of the machine hosting the data integration runtime.

### Issue 3: Config file isn't found in host machine

After installing Kubernetes inside the Linux-based machine, it's essential that the Kubernetes configuration file (config) is present in the `.kube` directory on the host machine.

1. Verify that the config file exists in the `.kube` directory.
2. If it's missing, copy the Kubernetes admin config file `~/.kube/config` to the required user location.

This file enables kubectl to connect to the Kubernetes cluster.

### Issue 4: DIRCTL connectivity error to Microsoft Purview service endpoint

When you try to register the Kubernetes supported self-hosted data integration runtime, the DIRCTL create command throws errors.

#### Cause

DIRCTL can't connect to Microsoft Purview service endpoint. This issue is usually caused by network settings or a firewall.

#### Resolution

- Review the network topology of the DIRCTL host machine.
- Allow port 443 outbound to https:`//<Accountname>`.purview.azure.com

### Issue 5: Kubernetes connectivity error with Microsoft Purview service endpoint

When you try to register the Kubernetes supported self-hosted data integration runtime, the DIRCTL create command could run long until it eventually times out. Or, after a successful installation, the self-hosted data integration runtime status shows as unhealthy or offline in the Microsoft Purview portal.

#### Resolution

Verify network reachability to the Microsoft Purview service endpoint as specified in the documentation. Ensure that outbound traffic on port 443 to the Microsoft Purview service endpoint https:`//<AccountName>`.purview.azure.com is allowed through the firewall.

### Issue 6: Kubernetes self-hosted data integration runtime creation timed out error

If the DIRCTL create command doesn't complete all operations successfully within 10 minutes, it throws a timeout error. Check the status of pods under the namespaces mentioned by the kubectl command.

`Kubectl get pods –n dirctl`

#### Resolution

You should reinitiate the process of DIRCTL delete, wait for pods to destroy completely, and then do create command.

### Issue 7: Registration key isn't authorized

When you try to register the Kubernetes supported self-hosted data integration runtime, the DIRCTL create command returns this error:

`[Error] DIR failed for registration.`

#### Cause

The registration key might have expired past its 24 hour validity time, or was manually revoked.

#### Resolution

Regenerate the key from the data integration runtime's page in the Microsoft Purview portal and register again.

### Issue 8: Self-hosted data integration runtime isn't functional or has been offline for more than 14 days

The refresh token expires if data integration runtime isn't functional for more than 14 days due to any reason. In that case, reregister the data integration runtime using this command:

`./DIRCTL create --registration-key <registration-key>`

### Issue 9: Download data integration runtime logs locally for troubleshooting

Each day’s data integration runtime log file only persists for 14 days. After 14 days, the log files are deleted. Download logs locally using DIRCTL log download command if necessary:

`e.g.  ./DIRCTL log download –d <relative path>`