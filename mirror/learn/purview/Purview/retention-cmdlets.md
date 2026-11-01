---
layout: Conceptual
title: Identify the available PowerShell cmdlets for retention | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/retention-cmdlets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-06-03T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- purview-compliance
- SPO_Content
description: Identify the PowerShell cmdlets for Microsoft 365 retention that support configuration at-scale, automation, or might be needed for advanced configuration scenarios.
locale: en-us
document_id: 9adffe53-aa95-992c-a61e-fd654f0194e8
document_version_independent_id: 9adffe53-aa95-992c-a61e-fd654f0194e8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/retention-cmdlets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: retention-cmdlets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/retention-cmdlets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: acd69775-af67-6f5d-ea5e-74d9c5edfeb3
---

# Identify the available PowerShell cmdlets for retention | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following sections to identify the main PowerShell cmdlets that are available for retention policies and retention labels that you might need for configuration at-scale, automated scripts, or advanced configuration scenarios. For the full list of cmdlets, see the [policy-and-compliance-retention list](/en-us/powershell/module/exchange#policy-and-compliance-retention) from the PowerShell documentation.

Before you use these cmdlets, you must first [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

In the descriptions that follow, a policy for retention can refer to a retention policy (no labels), or a retention label policy. Each policy defines whether it's static or adaptive and the locations for the policy to be applied.

When you use retention policies, the policy requires one rule to complete the configuration, for example, a rule that defines the retention settings, such as retain for five years and then delete.

When you use retention labels, these labels contain the retention settings and their policies need different rules:

- A retention label policy that you publish needs a rule that defines which labels should be displayed in apps.
- An auto-apply retention label policy needs a rule that defines the label to apply and the conditions for applying the label.

## Retention cmdlets for older locations

Use the cmdlets in the following table when the locations are **Exchange mailboxes**, **SharePoint sites** or **SharePoint classic and communication sites**, **OneDrive accounts**, **Microsoft 365 Group mailboxes & sites**, **Skype for Business**, **Exchange public folders**, **Teams chats and Copilot interactions**, or **Teams channel messages**.

Don't use these cmdlets when the locations are for Teams private channel messages (applicable [premigration](retention-policies-teams#migration-of-private-channel-messages-in-2025) only), Viva Engage user messages, Viva Engage community messages, Teams chats (without Copilot interactions), Microsoft Copilot experiences, Enterprise AI apps, or Other AI apps. These locations have alternative cmdlets that are identified in the next section.

| Cmdlet | Description | Applicable locations |
| --- | --- | --- |
| [Enable-ComplianceTagStorage](/en-us/powershell/module/exchange/enable-compliancetagstorage)[Get-ComplianceTagStorage](/en-us/powershell/module/exchange/get-compliancetagstorage) | A one-time operation to create storage, or view that storage for retention labels | Exchange mailboxes SharePoint sites (or SharePoint classic and communication sites)  OneDrive accounts  Microsoft 365 Group mailboxes & sites |
| [Get-ComplianceTag](/en-us/powershell/module/exchange/get-compliancetag)[New-ComplianceTag](/en-us/powershell/module/exchange/new-compliancetag)[Remove-ComplianceTag](/en-us/powershell/module/exchange/remove-compliancetag)[Set-ComplianceTag](/en-us/powershell/module/exchange/set-compliancetag) | View, create, delete, configure retention labels | Exchange mailboxes  SharePoint sites (or SharePoint classic and communication sites)  OneDrive accounts  Microsoft 365 Group mailboxes & sites |
| [Get-RecordReviewNotificationTemplateConfig](/en-us/powershell/module/exchange/get-recordreviewnotificationtemplateconfig)[Set-RecordReviewNotificationTemplateConfig](/en-us/powershell/module/exchange/set-recordreviewnotificationtemplateconfig) | View or configure the disposition review notification and reminder settings | Exchange mailboxes  SharePoint sites (or SharePoint classic and communication sites)  OneDrive accounts  Microsoft 365 Group mailboxes & sites |
| [Get-RetentionCompliancePolicy](/en-us/powershell/module/exchange/get-retentioncompliancepolicy)[New-RetentionCompliancePolicy](/en-us/powershell/module/exchange/new-retentioncompliancepolicy)[Remove-RetentionCompliancePolicy](/en-us/powershell/module/exchange/remove-retentioncompliancepolicy)[Set-RetentionCompliancePolicy](/en-us/powershell/module/exchange/set-retentioncompliancepolicy) | View, create, delete, configure retention policies and retention label policies | Exchange email  SharePoint sites (or SharePoint classic and communication sites)  OneDrive accounts Microsoft 365 Group mailboxes & sites  Skype for Business  Exchange public folders  Teams chats and Copilot interactions  Teams channel messages |
| [Get-RetentionComplianceRule](/en-us/powershell/module/exchange/get-retentioncompliancerule)[New-RetentionComplianceRule](/en-us/powershell/module/exchange/new-retentioncompliancerule)[Set-RetentionComplianceRule](/en-us/powershell/module/exchange/set-retentioncompliancerule)[Remove-RetentionComplianceRule](/en-us/powershell/module/exchange/remove-retentioncompliancerule) | View, create, configure, delete settings (rules) for retention policies and retention labels | Exchange email  SharePoint sites (or SharePoint classic and communication sites)  OneDrive accounts  Microsoft 365 Group mailboxes & sites  Skype for Business  Exchange public folders  Teams chats and Copilot interactions  Teams channel messages |

## Retention cmdlets for newer locations

Use the following cmdlets when the locations are for **Teams private channel messages** (applicable [premigration](retention-policies-teams#migration-of-private-channel-messages-in-2025) only), **Viva Engage user messages**, **Viva Engage community messages**, **Teams chats**, **Microsoft Copilot experiences**, **Enterprise AI apps**, **Other AI apps**, and for Teams call logs.

When the locations are for Teams chats and Copilot interactions, Teams channel messages, Exchange email, SharePoint sites (or SharePoint classic and communication sites), OneDrive accounts, Microsoft 365 Group mailboxes & sites, Skype for Business, or Exchange public folders, use the cmdlets listed in the previous section.

| Cmdlet | Description | Applicable locations |
| --- | --- | --- |
| [Get-AppRetentionCompliancePolicy](/en-us/powershell/module/exchange/get-appretentioncompliancepolicy)[New-AppRetentionCompliancePolicy](/en-us/powershell/module/exchange/new-appretentioncompliancepolicy)[Remove-AppRetentionCompliancePolicy](/en-us/powershell/module/exchange/remove-appretentioncompliancepolicy)[Set-AppRetentionCompliancePolicy](/en-us/powershell/module/exchange/set-appretentioncompliancepolicy) | View, create, delete, configure retention policies | Teams private channel messages  Viva Engage user messages  Viva Engage community messages  Teams chats  Teams call logs  Microsoft Copilot experiences  Enterprise AI apps  Other AI apps |
| [Get-AppRetentionComplianceRule](/en-us/powershell/module/exchange/get-appretentioncompliancerule)[New-AppRetentionComplianceRule](/en-us/powershell/module/exchange/new-appretentioncompliancerule)[Remove-AppRetentionComplianceRule](/en-us/powershell/module/exchange/remove-appretentioncompliancerule)[Set-AppRetentionComplianceRule](/en-us/powershell/module/exchange/set-appretentioncompliancerule) | View, create, configure, delete settings (rules) for retention policies | Teams private channel messages  Viva Engage user messages  Viva Engage community messages  Teams chats  Teams call logs  Microsoft Copilot experiences  Enterprise AI apps  Other AI apps |

## Configuration guidance

Use the help pages associated with each cmdlet for detailed information and examples.

For guided help to create and then publish retention labels, see [Create and publish retention labels by using PowerShell](bulk-create-publish-labels-using-powershell).