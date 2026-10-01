---
layout: Conceptual
title: Azure machine configuration Windows agent release notes - Azure Machine Configuration | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/machine-configuration/whats-new/agent/windows
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
description: Details guest configuration agent for Windows release notes, issues, and frequently asked questions.
ms.date: 2026-06-22T00:00:00.0000000Z
ms.topic: release-notes
locale: en-us
document_id: 91dbb93b-a4b9-7a12-f2ba-e3f2e916ec7e
document_version_independent_id: 5ddf76bf-1913-cd9f-53fe-2418dcf1a706
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/machine-configuration/whats-new/agent/windows.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/machine-configuration/whats-new/agent/windows
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/machine-configuration/whats-new/agent/windows.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
platformId: 603592fa-0261-7cd4-e264-bce290432b34
---

# Azure machine configuration Windows agent release notes - Azure Machine Configuration | Microsoft Learn

The machine configuration agent receives improvements on an ongoing basis. To stay up to date with the most recent developments, this article provides you with information about:

- The latest releases
- Known issues
- Bug fixes

For information on release notes for the connected machine agent, see [What's new with the connected machine agent](/en-us/azure/azure-arc/servers/agent-release-notes).

Note

This article includes the release notes for the Windows extension for Azure machine configuration (`Microsoft.GuestConfiguration.ConfigurationforWindows`).

To review the release notes for Linux (`Microsoft.GuestConfiguration.ConfigurationforLinux`), see [Azure machine configuration Windows agent release notes](linux).

The following sections of this article detail the notes for each release of the agent. The heading for each section includes the specific version for that release and the date for the release.

## Version 1.29.119.0 - September 2026

### Updated

- Updated OpenSSL library from version 3.6.3 to 3.6.4.

## Version 1.29.118.0 - September 2026

### Updated

- Updated bundled PowerShell version from 7.4.15 to 7.4.19.
- Improved configuration package download performance.

### Fixed

- Fixed PowerShell-based policy execution failures caused by Mark-of-the-Web metadata.
- Strengthened configuration package integrity validation.

## Version 1.29.116.0 - July 2026

### Updated

- Improved baseline customization pre-installation support for PowerShell script and module files.

### Fixed

- Fixed an issue where Machine Configuration assignments that failed during processing were not fetched again.
- Strengthened configuration package extraction validation.

## Version 1.29.113.0 - July 2026

### New Features

- Resolved TLS connection failures to HTTPS endpoints when the intermediate or root certificate isn't already in the local Windows certificate store.
- Fixed a periodic memory spike during routine assignment-refresh checks.

## Version 1.29.112.0 - July 2026

### Updated

- Updated OpenSSL library from version 3.6.2 to 3.6.3.

## Version 1.29.110.0 - June 2026

### Updated

- Strengthened TLS certificate validation to address CVE-2026-47632.
- Updated bundled PowerShell version from 7.4.14 to 7.4.15.
- Improved network efficiency by avoiding repeated downloads of unchanged policy assignments.

### Fixed

- Improved reliability of baseline customization compliance reporting for configurations with parameter values longer than `1024` characters.

## Version 1.29.108.0 - April 2026

### Updated

- Updated OpenSSL library from version `3.6.1` to `3.6.2`.
- Updated bundled PowerShell version from `7.4.13` to `7.4.14`.
- Improved compliance reporting for security baseline policy assignments.

### Fixed

- Improved reliability of unzip during installation.

## Version 1.29.106.0 - March 2026

### Updated

- Updated OpenSSL library from version `3.6.0` to `3.6.1`.

## Version 1.29.104.0 - January 2026

### Updated

- Updated bundled PowerShell version from `7.4.7` to `7.4.13`.
- Updated Azure Storage API version from `2019-02-02` to `2025-11-05`.

### Fixed

- Fixed support for security baseline customization on localized operating systems.
- Enhanced reliability for compliance evaluation for `ApplyAndAutoCorrect` Machine Configuration policy assignments.

## Version 1.29.101.0 - November 2025

### New Features

- Baseline customization.

### Updated

- Updated OpenSSL library from version `3.4.1` to `3.6.0`.

## Version 1.29.98.0 - July 2025

### New Features

- Announcing the general availability of System Assigned Identities for Azure Machine Configuration as well as Arc Machines, enhancing security and simplifying at-scale server management by allowing private access to configuration packages in Azure Storage. For more information, see [System-Assigned Identity-based Access for Machine Configuration Packages](https://techcommunity.microsoft.com/blog/azuregovernanceandmanagementblog/system-assigned-identity-based-access-for-machine-configuration-packages-%E2%80%93-ga-on/4446603).

### Fixed

- Resolved an issue where the compliance status didn't update correctly until services were restarted.
- Updated local `PATH` environment variable to resolve service install and delete errors.

## Version 1.29.92.0 - April 2025

### New features

- Today our extension uses a maximum of 5% CPU. For cases where this needs to be configured, a configuration file `cpu_config.json` can be written under the path, `C:\ProgramData\AzureConnectedMachineAgent\Config`. This file should contain the following configuration:

```json
{
    "PolicyAgentCpu": 5
}
```

In this case the maximum CPU utilization of the service will be 5%. This can be configured per the needs of the required scenario.

### Updated

- Migrated to .NET 8
- Upgraded to PowerShell `7.4.7`

## Version 1.29.91.0 - March 2025

### Updated

- Updated OpenSSL from version `3.4.0` to `3.4.1`.

### Fixed

- Resolved an issue causing a deadlock during policy execution.

## Version 1.29.86.0 - January 2025

### Updated

- Updated OpenSSL from version `3.3.2` to `3.4.0`.

## Version 1.29.85.0 - October 2024

### Updated

- Updated OpenSSL from version `3.3.1` to `3.3.2`.

### Fixed

- Added timeouts to address an issue that caused the agent to become unresponsive when trying to read a response from the service. If the agent takes more than 3 minutes to read a response or send a request to the service, it will now time out and continue execution.

## Version 1.29.82.0 - September 2024

### New Features

- Announcing the general availability of User Assigned Identities for Azure Machine Configuration, enhancing security and simplifying at-scale server management by allowing private access to configuration packages in Azure Storage. For more information, see [User-Assigned Identity-based Access for Machine Configuration Packages](https://techcommunity.microsoft.com/blog/azuregovernanceandmanagementblog/user-assigned-identity-based-access-for-machine-configuration-packages-%E2%80%93-general/4305594).