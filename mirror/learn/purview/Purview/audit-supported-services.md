---
layout: Conceptual
title: Microsoft services that support auditing | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-supported-services
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover Microsoft services that support auditing in Microsoft Purview. Learn how to search the unified audit log for activities across various apps and features.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-02-18T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-audit
ms.collection:
- purview-compliance
- audit
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-apr2020
- admindeeplinkEXCHANGE
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 770444f2-e073-657a-e1ef-950050d3a49f
document_version_independent_id: 770444f2-e073-657a-e1ef-950050d3a49f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-supported-services.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-supported-services
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-supported-services.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5711eaa5-435f-4c40-8d89-924ef7945eec
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ee4d551-d6c4-4e91-986e-0f1afd52559f
platformId: d2c7dd20-743d-763c-4700-d51fd3d6dea6
---

# Microsoft services that support auditing | Microsoft Learn

You can search the unified audit log for activities performed in different Microsoft services. The following table lists the Microsoft services, apps, and features that the unified audit log supports.

| Microsoft service or feature | Record types |
| --- | --- |
| Microsoft Entra ID | AzureActiveDirectory, AzureActiveDirectoryAccountLogon, AzureActiveDirectoryStsLogon |
| Azure Information Protection  (For the Microsoft Purview Information Protection client and scanner) | AipDiscover, AipSensitivityLabelAction, AipProtectionAction, AipFileDeleted, AipHeartBeat |
| Communication compliance | ComplianceSupervisionExchange |
| Content explorer | LabelContentExplorer |
| Data connectors | ComplianceConnector |
| Data loss prevention (DLP) | ComplianceDLPSharePoint, ComplianceDLPExchange, DLPEndpoint |
| Dynamics 365 | CRM |
| eDiscovery (Standard + Premium) | Discovery, AeD |
| Encrypted message portal | OMEPortal |
| Exact Data Match | MipExactDataMatch |
| Exchange Online | ExchangeAdmin, ExchangeItem, ExchangeItemAggregated |
| Forms | MicrosoftForms |
| Information barriers | InformationBarrierPolicyApplication |
| Microsoft Defender XDR | AirInvestigation, AirManualInvestigation, AirAdminActionInvestigation, MS365DCustomDetection |
| Microsoft 365 Copilot and Microsoft 365 Copilot Chat | CopilotInteraction |
| Microsoft Defender Experts | DefenderExpertsforXDRAdmin |
| Microsoft Defender for Identity (MDI) | MicrosoftDefenderForIdentityAudit |
| Microsoft Planner | PlannerCopyPlan, PlannerPlan, PlannerPlanList, PlannerRoster, PlannerRosterSensitivityLabel, PlannerTask, PlannerTaskList, PlannerTenantSettings |
| Microsoft Project for the web | ProjectAccessed, ProjectCreated, ProjectDeleted, ProjectTenantSettingsUpdated, ProjectUpdated, RoadmapAccessed,RoadmapCreated, RoadmapDeleted, RoadmapItemAccessed,RoadmapItemCreated,RoadmapItemDeleted, RoadmapItemUpdated, RoadmapTenantSettingsUpdated, RoadmapUpdated, TaskAccessed, TaskCreated,TaskDeleted, TaskUpdated |
| Microsoft Purview Information Protection (MIP) labels | MIPLabel, MipAutoLabelExchangeItem, MipAutoLabelSharePointItem, MipAutoLabelSharePointPolicyLocation |
| Microsoft Teams | MicrosoftTeams |
| Microsoft To Do | MicrosoftToDo, MicrosoftToDoAudit |
| MyAnalytics | MyAnalyticsSettings |
| OneDrive for Business | OneDrive |
| Power Apps | PowerAppsApp, PowerAppsPlan |
| Power Automate | MicrosoftFlow |
| Power BI | PowerBIAudit |
| Quarantine | Quarantine |
| Sensitive information types | DlpSensitiveInformationType |
| Sensitivity labels | MIPLabel, SensitivityLabelAction, SensitivityLabeledFileAction, SensitivityLabelPolicyMatch |
| SharePoint Online | SharePoint, SharePointFileOperation,SharePointSharingOperation, SharePointListOperation, SharePointCommentOperation |
| Stream | MicrosoftStream |
| SystemSync | DataShareCreated, DataShareDeleted, GenerateCopyOfLakeData, DownloadCopyOfLakeData |
| Threat Intelligence | ThreatIntelligence, ThreatIntelligenceUrl, ThreatFinder, ThreatIntelligenceAtpContent |
| Viva Goals | VivaGoals |
| Viva Insights | VivaInsights |
| Viva Engage | Viva Engage |

For more information about the operations that each service audits, see the [Audit log activities](audit-log-activities) article.

The previous table also identifies the record type value to use to search the audit log for activities in the corresponding service by using the **Search-UnifiedAuditLog** cmdlet in Exchange Online PowerShell or by using a PowerShell script. Some services have multiple record types for different types of activities within the same service. For a more complete list of auditing record types, see [Office 365 Management Activity API schema](/en-us/office/office-365-management-api/office-365-management-activity-api-schema#auditlogrecordtype).

For more information about using PowerShell to search the audit log, see:

- [Search-UnifiedAuditLog](/en-us/powershell/module/exchange/search-unifiedauditlog)
- [Use a PowerShell script to search the audit log](audit-log-search-script)