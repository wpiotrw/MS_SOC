---
layout: Conceptual
title: Azure machine configuration Linux agent release notes - Azure Machine Configuration | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/machine-configuration/whats-new/agent/linux
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
description: Details guest configuration agent for Linux release notes, issues, and frequently asked questions.
ms.date: 2024-06-22T00:00:00.0000000Z
ms.topic: release-notes
locale: en-us
document_id: fad0bcb1-b293-c044-63e2-b48b1e402414
document_version_independent_id: 1dd88be9-b0ab-6c14-7df9-f6563b70cd46
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/machine-configuration/whats-new/agent/linux.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
interactive_type: azurepowershell
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/machine-configuration/whats-new/agent/linux
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/machine-configuration/whats-new/agent/linux.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
platformId: 81988481-98d1-8778-8d07-a2dc844ea99f
---

# Azure machine configuration Linux agent release notes - Azure Machine Configuration | Microsoft Learn

The machine configuration agent receives improvements on an ongoing basis. To stay up to date with the most recent developments, this article provides you with information about:

- The latest releases
- Known issues
- Bug fixes

For information on release notes for the connected machine agent, see [What's new with the connected machine agent](/en-us/azure/azure-arc/servers/agent-release-notes).

Note

This article includes the release notes for the Linux extension for Azure machine configuration (`Microsoft.GuestConfiguration.ConfigurationforLinux`).

To review the release notes for Windows (`Microsoft.GuestConfiguration.ConfigurationforWindows`), see [Azure machine configuration Windows agent release notes](windows).

The following sections of this article detail the notes for each release of the agent. The heading for each section includes the specific version for that release and the date for the release.

## Version 1.26.119 - September 2026

### Updated

- Updated OpenSSL library from version `3.6.3` to `3.6.4`.

## Version 1.26.118 - September 2026

### Updated

- Updated bundled PowerShell version from `7.4.15` to `7.4.19`.
- Improved configuration package download performance.

### Fixed

- Prevented security baseline settings intended for one Linux distribution from being applied to another distribution.

## Version 1.26.116 - July 2026

### Updated

- Improved baseline customization pre-installation support for PowerShell script and module files.

### Fixed

- Fixed an issue where Machine Configuration assignments that failed during processing were not fetched again.
- Strengthened configuration package extraction validation.

## Version 1.26.113 - July 2026

### Updated

- Updated OpenSSL library from version `3.6.2` to `3.6.3`.

## Version 1.26.111 - June 2026

### New features

- Added support for Azure Linux 4.0.

### Updated

- Strengthened TLS certificate validation to address CVE-2026-47632.
- Updated bundled PowerShell version from `7.4.14` to `7.4.15`.
- Improved network efficiency by avoiding repeated downloads of unchanged policy assignments.

### Fixed

- Improved reliability of baseline customization compliance reporting for configurations with parameter values longer than `1024` characters.
- Fixed a crash related to a heap memory corruption error that could occur on service shut down.
- Unsupported Linux distributions are now reported as non-compliant for CIS baseline assignments.

## Version 1.26.109 - April 2026

### New Features

- Added support for Azure Container Linux.

### Updated

- Updated OpenSSL library from version `3.6.1` to `3.6.2`.
- Updated bundled PowerShell version from `7.4.13` to `7.4.14`.
- Improved compliance reporting for security baseline policy assignments.

## Version 1.26.107 - March 2026

### Updated

- Updated OpenSSL library from version `3.4.3` to `3.6.1`.

## Version 1.26.104 - January 2026

### Updated

- Updated bundled PowerShell version from `7.4.7` to `7.4.13`.
- Updated Azure Storage API version from `2019-02-02` to `2025-11-05`.

### Fixed

- Fixed support for security baseline customization on localized operating systems.
- Enhanced reliability for compliance evaluation for ApplyAndAutoCorrect Machine Configuration policy assignments.
- Fixed bugs that cause Machine Configuration agent and GC worker to crash.

## Version 1.26.101 - November 2025

### New Features

- Baseline customization.

### Updated

- Updated OpenSSL library from version `3.4.1` to `3.4.3`.

### Fixed

- Use `systemctl daemon-reload` instead of `systemctl daemon-reexec` for better stability and compatibility.

## Version 1.26.93 - July 2025

### New Features

- Announcing the general availability of System Assigned Identities for Azure Machine Configuration as well as Arc Machines, enhancing security and simplifying at-scale server management by allowing private access to configuration packages in Azure Storage. For more information, see [System-Assigned Identity-based Access for Machine Configuration Packages](https://techcommunity.microsoft.com/blog/azuregovernanceandmanagementblog/system-assigned-identity-based-access-for-machine-configuration-packages-%E2%80%93-ga-on/4446603).

### Fixed

- Resolved an issue where the compliance status didn't update correctly until services were restarted.
- Updated Boost on Linux to resolve service start issues caused by compatibility problems.
- Resolved "No public key" error by adding GPG package signature validation.
- Resolved gpg installation issues on debian

## Version 1.26.87 - April 2025

### New features

- Today our extension uses a maximum of 5% CPU. For cases where this needs to be configured, a configuration file `cpu_config.json` can be written under the path, `/var/opt/azcmagent/`. This file should contain the following configuration:

```json
{
    "PolicyAgentCpu": 5
}
```

In this case the maximum CPU utilization of the service will be 5%. This can be configured per the needs of the required scenario.

### Updated

- Updated .NET from version `6` to `8`
- Updated PowerShell from version `7.2.x` to `7.4.7`

## Version 1.26.85 - March 2025

### New Features

- Added support for the Linux distribution Azure Linux 3!

### Updated

- Updated OpenSSL from version `3.4.0` to `3.4.1`.

### Fixed

- Resolved an issue causing a deadlock during policy execution.

## Version 1.26.80 - January 2025

### Updated

- Updated OpenSSL from version `3.0.15` to `3.4.0`.

## Version 1.26.79 - October 2024

#### Fixed

- Added timeouts to address an issue that caused the agent to become unresponsive when trying to read a response from the service. If the agent takes more than 3 minutes to read a response or send a request to the service, it will now time out and continue execution.

## Version 1.26.77 - September 2024

### Updated

- Updated OpenSSL from version `3.0.14` to `3.0.15`.

## Version 1.26.76 - September 2024

### New Features

- Announcing the general availability of User Assigned Identities for Azure Machine Configuration, enhancing security and simplifying at-scale server management by allowing private access to configuration packages in Azure Storage. For more information, see [User-Assigned Identity-based Access for Machine Configuration Packages](https://techcommunity.microsoft.com/blog/azuregovernanceandmanagementblog/user-assigned-identity-based-access-for-machine-configuration-packages-%E2%80%93-general/4305594).

## Version 1.26.48 - January 2023

### New Features

- Added support for Linux distributions such as Red Hat Enterprise Linux (RHEL) 9, Mariner 1 and 2, Alma 9, and Rocky 9.

### Fixed

- Improved reliability for the guest configuration policy engine.

## Version 1.26.38

### New features

- You can now restrict which URLs can be used to download machine configuration packages by setting the `allowedGuestConfigPkgUrls` tag on the server resource and providing a comma-separated list of URL patterns to allow. If the tag exists, the agent only allows custom packages to be downloaded from the specified URLs. Built-in packages are unaffected by this feature.

### Fixed

- Resolves local elevation of privilege vulnerability [CVE-2022-38007](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-38007).
- If you're currently running an older version of the `AzurePolicyforLinux` extension, use the PowerShell or Azure CLI commands in the following examples to update your extension to the latest version.

```azurepowershell
$params = @{
    Publisher              = 'Microsoft.GuestConfiguration'
    Type                   = 'ConfigurationforLinux'
    Name                   = 'AzurePolicyforLinux'
    TypeHandlerVersion     = '1.26.38'
    ResourceGroupName      = '<resource-group>'
    Location               = '<location>'
    VMName                 = '<vm-name>'
    EnableAutomaticUpgrade = $true
}
Set-AzVMExtension @params
```

```azurecli
az vm extension set \
    --publisher Microsoft.GuestConfiguration \
    --name ConfigurationforLinux \
    --extension-instance-name AzurePolicyforLinux \
    --resource-group <resource-group> \
    --vm-name <vm-name> \
    --version 1.26.38 \
    --enable-auto-upgrade true
```