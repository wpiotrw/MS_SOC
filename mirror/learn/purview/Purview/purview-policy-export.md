---
layout: Conceptual
title: Export policy configuration in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-policy-export
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to export your Microsoft Purview policy configuration as a ZIP file for support requests, configuration backup, and policy analysis.
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-04-13T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-portal
audience: ITPro
ms.topic: concept-article
ms.collection:
- purview-compliance
- essentials-get-started
ms.custom:
- admindeeplinkCOMPLIANCE
- intro-overview
ai-usage: ai-assisted
locale: en-us
document_id: cb351098-e45e-71ba-a04d-62c76c0d8196
document_version_independent_id: cb351098-e45e-71ba-a04d-62c76c0d8196
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-policy-export.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-policy-export
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-policy-export.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: 4ef5c27b-c5ad-09d7-1d80-ac3c28b4b28d
---

# Export policy configuration in Microsoft Purview | Microsoft Learn

The **Export to zip** option on the policies page downloads a point-in-time snapshot of all your policy configurations as a ZIP file in XML format. The export captures the full configuration details for every policy in the current solution at the moment of export, including rules, conditions, actions, scoping, and priority settings where relevant. For example, Label policies include the labels in the export, but not rules or conditions as they don't have any. You can't select individual policies for export—the ZIP file always contains all policies.

Important

The exported ZIP file is a read-only, point-in-time snapshot of your policy configuration. It's intended for reference only. You can't import it back into your tenant to restore or create policies, and it doesn't automatically update to reflect subsequent configuration changes.

Note

The **Export to CSV** option exports only the summary information shown in the policies table, such as policy name, status, and last modified date.

## Common scenarios

Common scenarios for using the ZIP export include:

- **Support requests** — Attach the ZIP file to a support ticket so that support engineers can review your complete policy configuration without a live troubleshooting session.
- **Configuration backup** — Save periodic snapshots of your policy configuration for version control and change tracking purposes.
- **Configuration analysis** — Extract the XML file and analyze your policies locally by using PowerShell or by uploading the file to Microsoft 365 Copilot.

## Export your policy configuration

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Navigate to the policies page for the solution whose policies you want to export. If exporting is supported for that solution, the **Export to zip** option will be available.
3. Select **Export to zip**.
4. Save the ZIP file when prompted. The file downloads to your default downloads folder.
5. Extract the ZIP file to access the XML configuration file.

## View the exported configuration by using PowerShell

You can use the standard PowerShell `Import-Clixml` cmdlet to deserialize the exported XML file into PowerShell objects for local analysis. This cmdlet reads the file locally and doesn't connect to any service.

1. Open a PowerShell window.
2. Import the XML file into a variable by using the `Import-Clixml` cmdlet. Replace the path with the location of your extracted XML file.

    ```powershell
    $p = Import-Clixml -Path "<path to extracted XML file>"
    ```
3. List the available properties in the exported configuration.

    ```powershell
    $p | Get-Member -MemberType Properties
    ```
4. View the data for a specific property by using `Format-Table` for a readable summary.

    ```powershell
    $p.<PropertyName> | Format-Table
    ```

    For example, if the export contains DLP policies:

    ```powershell
    $p.DlpCompliancePolicies | Format-Table
    $p.DlpComplianceRules | Format-Table
    ```

Tip

The property names in the exported XML vary by solution. Use `$p | Get-Member -MemberType Properties` to discover which properties are available in your export.