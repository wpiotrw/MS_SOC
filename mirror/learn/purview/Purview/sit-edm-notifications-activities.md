---
layout: Conceptual
title: Create notifications for exact data match activities | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-edm-notifications-activities
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.date: 2026-06-22T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Learn how to create notifications for exact data match activities.
ms.custom: msecd-doc-authoring-1014, seo-marvel-apr2020, sfi-ga-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 55bd8d55-3d25-169d-d5ba-75bdd736cabb
document_version_independent_id: 55bd8d55-3d25-169d-d5ba-75bdd736cabb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-edm-notifications-activities.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-edm-notifications-activities
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-edm-notifications-activities.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: 4e4008cc-c688-74a8-fb8a-4a2d88f4aeb3
---

# Create notifications for exact data match activities | Microsoft Learn

When you [create custom sensitive information types with exact data match (EDM)](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types), there are a number of activities that are created in the [audit log](audit-search). You can use the [New-ProtectionAlert](/en-us/powershell/module/exchange/new-protectionalert) PowerShell cmdlet to create notifications that let you know when these activities occur:

- `CreateSchema`
- `EditSchema`
- `RemoveSchema`
- `UploadDataFailed`
- `UploadDataCompleted`

Note

The ability to create notifications for EDM activities is available for the World Wide and GCC clouds only.

## Prerequisites

Your account must have one of the following roles:

- Global administrator
- Compliance administrator
- Exchange Online administrator

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

To learn more about DLP permissions, see [Permissions in the Microsoft Purview portal](purview-permissions).

EDM-based classification is included in these subscriptions:

- Office 365 E5
- Microsoft 365 E5
- Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance)
- Microsoft E5/A5 Information Protection and Governance

To learn more about DLP licensing, see [Microsoft 365 licensing guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#information-protection).

Before you begin, ensure you can connect to [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

## Configure notifications for EDM activities

1. Connect to [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
2. Run the `New-ProtectionAlert` cmdlet using the activity that you want to create the notification for. For example, if you want to be notified when the `UploadDataCompleted` action occurred, run:

    ```powershell
    New-ProtectionAlert -Name "EdmUploadCompleteAlertPolicy" -Category Others -NotifyUser <address to send notification to> -ThreatType Activity -Operation UploadDataCompleted -Description "Custom alert policy to track when EDM upload Completed" -AggregationType None
    ```

    For the `UploadDataFailed` activity, you can run:

    ```powershell
    New-ProtectionAlert -Name "EdmUploadFailAlertPolicy" -Category Others -NotifyUser <SMTP address to send notification to> -ThreatType Activity -Operation UploadDataFailed -Description "Custom alert policy to track when EDM upload Failed" -AggregationType None -Severity High
    ```