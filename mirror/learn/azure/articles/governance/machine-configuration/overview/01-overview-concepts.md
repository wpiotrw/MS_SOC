---
layout: Conceptual
title: What is Azure Machine Configuration? - Azure Machine Configuration | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/machine-configuration/overview/01-overview-concepts
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
author: michaeltlombardi
learn_banner_products:
- azure
ms.author: mlombardi
ms.service: azure-machine-configuration
description: Learn the core concepts of Azure Policy's machine configuration feature and understand key scenarios for configuration management and compliance.
ms.date: 2025-11-07T00:00:00.0000000Z
ms.topic: overview
locale: en-us
document_id: 134c9129-275e-eb83-874c-fc24ce78dcad
document_version_independent_id: 550a8a3b-3bfa-c426-0bf5-2c9a2e855b03
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/machine-configuration/overview/01-overview-concepts.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/machine-configuration/overview/01-overview-concepts
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/machine-configuration/overview/01-overview-concepts.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
platformId: 6adbe758-9e70-ecb6-7770-c021be47a4da
---

# What is Azure Machine Configuration? - Azure Machine Configuration | Microsoft Learn

Caution

This article references CentOS, a Linux distribution that is End Of Life (EOL) status. Consider your use and planning accordingly. For more information, see the [CentOS End Of Life guidance](/en-us/azure/virtual-machines/workloads/centos/centos-end-of-life).

Azure Policy's machine configuration feature provides native capability to audit or configure operating system settings as code for machines running in Azure and hybrid [Arc-enabled machines](/en-us/azure/azure-arc/servers/overview). You can use the feature directly per-machine, or orchestrate it at scale by using Azure Policy.

Configuration resources in Azure are designed as an [extension resource](/en-us/azure/azure-resource-manager/management/extension-resource-types). You can imagine each configuration as an extra set of properties for the machine. Configurations can include settings such as:

- Operating system settings
- Application configuration or presence
- Environment settings

Configurations are distinct from policy definitions. Machine configuration uses Azure Policy to dynamically assign configurations to machines. You can also assign configurations to machines [manually](../concepts/assignments#manually-creating-machine-configuration-assignments).

Examples of each scenario are provided in the following table.

| Type | Description | Example story |
| --- | --- | --- |
| [Configuration management](../concepts/assignments) | You want a complete representation of a server, as code in source control. The deployment should include properties of the server (size, network, storage) and configuration of operating system and application settings. | "This machine should be a web server configured to host my website." |
| [Compliance](../../policy/assign-policy-portal) | You want to audit or deploy settings to all machines in scope. Apply settings reactively to existing machines or proactively to new machines as they're deployed. | "All machines should use Transport Layer Security (TLS) 1.2. Audit existing machines so I can release change where it's needed, in a controlled way, at scale. For new machines, enforce the setting when they're deployed." |

You can view the per-setting results from configurations in the [Guest assignments page](../../policy/how-to/determine-non-compliance#compliance-details-for-guest-configuration). If an Azure Policy assignment orchestrated the configuration is orchestrated, you can select the "Last evaluated resource" link on the ["Compliance details" page](../../policy/how-to/determine-non-compliance).

Note

Machine Configuration currently supports the creation of up to 50 guest assignments per machine.

## Enforcement Modes for Custom Policies

In order to provide greater flexibility in the enforcement and auditing of server settings, applications, and workloads, Machine Configuration offers three main enforcement modes for each policy assignment as described in the following table.

| Mode | Description |
| --- | --- |
| Audit | Only report on the state of the machine |
| Apply and Monitor | Configuration applied to the machine and then monitored for changes |
| Apply and Autocorrect | Configuration applied to the machine and brought back into conformance if drift occurs |

[A video walk-through of this document is available](https://youtu.be/t9L8COY-BkM).

## Supported client types

Machine configuration policy definitions are inclusive of new versions. Older versions of operating systems available in Azure Marketplace are excluded if the Guest Configuration client isn't compatible. Additionally, Linux server versions that are out of lifetime support by their respective publishers are excluded from the support matrix.

The following table shows a list of supported operating systems on Azure images. The `.x` text is symbolic to represent new minor versions of Linux distributions. To view supported server editions on Azure Arc, refer to [this list of supported server editions on Azure Arc](/en-us/azure/azure-arc/servers/prerequisites).

| Publisher | Name | Versions |
| --- | --- | --- |
| Alma | AlmaLinux | 9 |
| Amazon | Linux | 2 |
| Canonical | Ubuntu Server | 16.04 - 24.x |
| Credativ | Debian | 10.x - 13.x |
| Microsoft | CBL-Mariner | 1 - 2 |
| Microsoft | Azure Linux | 3 |
| Microsoft | Windows Client | Windows 10, 11 |
| Microsoft | Windows Server | 2012 - 2025 |
| Oracle | Oracle-Linux | 7.x - 9.x |
| OpenLogic | CentOS | 7.3 - 8.x |
| Red Hat | Red Hat Enterprise Linux\* | 7.4 - 10.x |
| Rocky | Rocky Linux | 8 - 9 |
| SUSE | SUSE Linux Enterprise Server | 12 SP5, 15.x |

\* Red Hat CoreOS isn't supported. \* \* Arm64 architecture isn't supported on Azure VMs.

Machine configuration policy definitions support custom virtual machine images as long as they're one of the operating systems in the previous table. Machine Configuration doesn't support VMSS uniform but does support [VMSS Flex](/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes#scale-sets-with-flexible-orchestration).

## Machine configuration samples

Machine configuration built-in policy samples are available in the following locations:

- [Built-in policy definitions - Guest Configuration](/en-us/azure/governance/policy/samples/built-in-policies#guest-configuration)
- [Built-in initiatives - Guest Configuration](/en-us/azure/governance/policy/samples/built-in-initiatives#guest-configuration)
- [Azure Policy samples GitHub repository](https://github.com/Azure/azure-policy/tree/master/built-in-policies/policySetDefinitions/Guest%20Configuration)
- [Sample DSC resource modules](https://github.com/Azure/azure-policy/tree/master/samples/GuestConfiguration/package-samples/resource-modules)