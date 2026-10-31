---
layout: Conceptual
title: Configure Microsoft Purview Information Protection scanner features (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/deploy-scanner-feature-control
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
- purview-information-protection
search.appverid:
- MOE150
- MET150
ROBOTS: NOINDEX, NOFOLLOW
description: Use admin-controlled feature configuration to enable or disable Microsoft Purview Information Protection scanner features at the cluster level.
ms.custom: msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 9ed88075-1403-c9ba-5459-6c6b1ffd871c
document_version_independent_id: 9ed88075-1403-c9ba-5459-6c6b1ffd871c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/deploy-scanner-feature-control.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: deploy-scanner-feature-control
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/deploy-scanner-feature-control.md
platformId: d4d2fbc1-9676-c6ad-fb39-10aa04dfa902
---

# Configure Microsoft Purview Information Protection scanner features (preview) | Microsoft Learn

Scanner administrators can enable, disable, and configure Microsoft Purview Information Protection scanner features at the cluster level. Use PowerShell to manage feature settings across all nodes in a cluster.

Admin-controlled feature configuration is available with Microsoft Purview Information Protection client and scanner [version 3.2.89.0 (preview)](information-protection-client-relnotes#version-32890-preview) or later.

## How feature control works

Scanner features are configured once per scanner cluster. The settings are stored centrally in the shared scanner cluster database, which means:

- An administrator runs a configuration cmdlet once from any node in the cluster, and all nodes pick up the change on the next scan cycle.
- No service restart is required.
- Nodes can't get into mismatched feature states.
- Disabling a feature stops the action that the feature performs (for example, writing to a new database table or producing a new file). Existing data isn't deleted, so a disabled feature can be re-enabled later without data loss.
- Features that aren't explicitly configured use their default state (typically **off**). Defaults for each feature are listed under Currently supported features.

Custom Reporting is the first feature delivered through admin-controlled feature configuration. For details about that feature, see [Custom Reporting (preview)](deploy-scanner-custom-reporting).

## Evolution of control: PowerShell and the Microsoft Purview portal

Admin-controlled feature configuration is designed to evolve over time. Supported features are initially configured by using PowerShell. As features become available in the Microsoft Purview portal, the portal becomes the source of truth for those features.

The following rules apply when both surfaces are available for a feature:

- **PowerShell first.** Until a feature is exposed in the Microsoft Purview portal, administrators configure it from PowerShell on any node in the cluster. Settings configured this way are tracked as managed by PowerShell.
- **Portal takes precedence.** When a feature has been configured from the Microsoft Purview portal, the portal becomes the source of truth for that feature. PowerShell attempts to change a portal-managed feature are ignored with a warning, and the cluster state remains unchanged. Other features in the same `-FeatureSettings` call that aren't portal-managed are still applied.
- **No synchronization.** Settings aren't synchronized between PowerShell and the portal. Not every scanner feature will end up being configurable from the portal. When a feature *is* available in the portal and has been configured there, that portal-configured setting takes precedence and prevents updates from PowerShell. There's a single source of truth for each feature at any time.
- **Get always reflects state.** Regardless of where a feature was configured, [Get-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/get-scannerconfiguration) returns the current state and source for every configured feature. Administrators can audit the cluster from PowerShell at any time.

This PowerShell-to-portal management model means scanner administrators can adopt new features through PowerShell as soon as they reach public preview, and switch to portal-based management at their own pace as features become available there.

## Supported cmdlets and the `-FeatureSettings` parameter

The following cmdlets accept the `-FeatureSettings` parameter:

| Cmdlet | Purpose |
| --- | --- |
| [Install-Scanner](/en-us/powershell/module/purviewinformationprotection/install-scanner) | Configure features as part of a new scanner node installation. |
| [Set-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/set-scannerconfiguration) | Configure features on an existing scanner cluster. The change applies to every node in the cluster. |
| [Get-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/get-scannerconfiguration) | Return the current state and source for every configured feature, including features that were configured from the Microsoft Purview portal. |

`-FeatureSettings` accepts a PowerShell **hashtable** of feature name and setting pairs, using the same pattern as `-AdvancedSettings`:

- The hashtable key is the feature name (for example, `CustomReporting`).
- The hashtable value is the setting for that feature. Supported values for each feature are listed in the Currently supported features table.

Both the feature name and its value are validated before any change is written. If any entry is invalid, the cmdlet terminates with an error and no entries from the hashtable are applied.

For background on the `-AdvancedSettings` pattern, including PowerShell quoting and hashtable tips, see [PowerShell tips for specifying the advanced settings](create-sensitivity-labels#powershell-tips-for-specifying-the-advanced-settings) and the [`-AdvancedSettings`](/en-us/powershell/module/exchangepowershell/set-label#-advancedsettings) parameter on **Set-Label**.

### Example: Enable Custom Reporting on an existing cluster

Run the following from any node in the scanner cluster:

```powershell
Set-ScannerConfiguration -FeatureSettings @{CustomReporting=$true}
```

All nodes in the cluster pick up the change on their next scan cycle.

### Example: Enable Custom Reporting at install time

Use the following command to enable Custom Reporting when you install a new scanner node:

```powershell
Install-Scanner -SqlServerInstance SQLSERVER1 -Cluster Europe -FeatureSettings @{CustomReporting=$true}
```

### Example: Review the current feature state

Run the following command to review the current feature configuration for the cluster:

```powershell
Get-ScannerConfiguration
```

For each configured feature, the `Features` line in the output shows the current state and which surface configured it (PowerShell or the Microsoft Purview portal). For example, with Custom Reporting enabled from PowerShell:

```
Features            : {CustomReporting: True (Source: PowerShell)}
```

Features that have never been configured don't appear and use their default state.

### Disable a feature

To turn Custom Reporting off, set its value to `$false`. Existing data that the feature wrote isn't deleted; the scanner stops performing the feature's action on the next scan cycle.

```powershell
Set-ScannerConfiguration -FeatureSettings @{CustomReporting=$false}
```

## Currently supported features

The following table lists the currently supported scanner features and their configuration values:

| Feature name | Default | Supported values | Description |
| --- | --- | --- | --- |
| `CustomReporting` | Off | `$true`, `$false` | Populates the Custom Reporting tables and columns in the scanner cluster database. See [Custom Reporting (preview)](deploy-scanner-custom-reporting). |

Additional features will be added over time and listed in the [Microsoft Purview Information Protection client release notes](information-protection-client-relnotes).