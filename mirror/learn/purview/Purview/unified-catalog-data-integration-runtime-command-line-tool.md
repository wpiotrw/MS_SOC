---
layout: Conceptual
title: Data Integration Runtime Command Line Tool for Data Quality (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-integration-runtime-command-line-tool
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
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to install and configure the data integration runtime command line (DIRCTL) tool for on-premises data sources for Microsoft Purview Data Quality.
locale: en-us
document_id: 688e60c4-9a6a-3b05-6c76-6dca5e629885
document_version_independent_id: 688e60c4-9a6a-3b05-6c76-6dca5e629885
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-integration-runtime-command-line-tool.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-integration-runtime-command-line-tool
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-integration-runtime-command-line-tool.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e288bf89-d519-ded9-a763-34e51bab1b0f
---

# Data Integration Runtime Command Line Tool for Data Quality (preview) | Microsoft Learn

Data integration runtime command line (DIRCTL) is a .NET-based command line interface (CLI) tool that automates data integration runtime management within Kubernetes clusters. It simplifies complex Kubernetes operations with straightforward commands and ensures secure communication with Microsoft Purview for registration and token lifecycle management.

To manage your Microsoft Purview Kubernetes self-hosted data integration runtime locally, you need the DIRCTL command line tool. You can download this tool during the data integration runtime creation process. See the setup instructions below for Windows and Linux operating systems.

## Windows setup for DIRCTL CLI

1. [Download](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/) and install the Kubectl CLI tool.
2. Place the generated kube config file in the user-specific folder according to this path: `C:/Users/<user-folder>/.kube/`. Copy the file and name it **config**. 
    Note

    This config file is required for DIRCTL authentication on Kubernetes clusters.
3. Download the DIRCTL CLI package .zip for Windows.
4. Extract the contents to a preferred directory on your local machine.
5. Open a terminal on Windows.
6. Navigate to the extracted DIRCTL directory.
7. Use the cd command `<path-to-dirctl>` to move into the folder.
8. Run commands using `./`DIRCTL```.

## Linux setup for DIRCTL CLI

1. [Download](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) and install the kubectl CLI for your Linux distribution.
2. Place the kubeconfig file, for authentication to Kubernetes, in the default kube folder: ` ~/.kube/`.
3. Copy your generated kubeconfig file to the user-specific directory. Make sure the file is named **config**: `mkdir -p ~/.kube cp /path/to/your/kubeconfig ~/.kube/config `
    Note

    This config file is required for DIRCTL authentication on Kubernetes clusters.
4. Download the DIRCTL CLI package for Windows or Linux.
5. Open a terminal and navigate to the DIRCTL directory: `cd /your/target/directory/DIRCTL`
6. Run commands by using: `./DIRCTL `.

## DIRCTL commands

1. **DIRCTL Help**: The Help command provides a comprehensive overview of all the available commands and functionalities within the DIRCTL tool. It ensures you can use the tool effectively by providing guidance and context for your data integration tasks.
2. **DIRCTL Re-register**: `./DIRCTL re-register –registration-key <re-registration-key-value> ` Use the Re-register command to re-register an existing data integration runtime resource, if it's inactive for a long time, by using a new registration key.
3. **DIRCTL Delete**: `./DIRCTL delete` When you want to deregister a data integration runtime from the system and release all associated application Kubernetes pods, the Delete command provides a streamlined solution. This command completely removes the DIR from the SQL Server Data Quality Services (DQS), ensuring that no remnants of the runtime or its application pods remain. The command also handles the termination of all running Kubernetes pods associated with the DIR application, freeing up resources within the system.
4. **DIRCTL Upgrade**: `./DIRCTL upgrade –v <image version> ` The Upgrade command enables you to seamlessly upgrade the version of a data integration runtime to the latest available version specified by the user. This process ensures that the data integration runtime operates with the most up-to-date features, enhancements, and security patches, maintaining its compatibility and efficiency within the system.
5. **DIRCTL Describe:**` ./DIRCTL describe` The Describe command provides detailed insights into the status and performance of the running DIR and DIRCTL applications. It checks the health of application pods, ensuring that any problems or anomalies are promptly identified. By offering visibility into the runtime environment, this functionality supports troubleshooting and proactive system maintenance.
6. **DIRCTL Log**: `./DIRCTL log download –d <relative-destination-folder-path> ` Use the Log command to download logs of all active data integration runtime application pods into a specified destination folder path. This functionality is especially vital for debugging, performance monitoring, or audit activities as it ensures you have access to detailed runtime records. By retaining comprehensive logs, you can effectively identify patterns, anomalies, and potential problems, making it a key tool in system maintenance and optimization.
7. **DIRCTL Config**: `./DIRCTL config auto-update-enable <true/false> ` Update the configuration for auto-update-enable to false or true.