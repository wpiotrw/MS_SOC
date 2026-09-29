---
layout: Conceptual
title: Programmability and Extensibility - Permission reference - Power Platform | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/power-platform/admin/programmability-permission-reference
breadcrumb_path: /power-platform/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://powerusers.microsoft.com/
recommendations: true
uhfHeaderId: MSDocsHeader-PowerPlatform
ms.service: power-platform
ms.subservice: admin
search.app:
- administration-docs
description: Overview of granular permissions available in Power Platform programmability tools
author: laneswenka
ms.reviewer: ellenwehrle
ms.component: pa-admin
ms.topic: reference
ms.date: 2025-09-26T00:00:00.0000000Z
ms.author: laswenka
search.audienceType:
- admin
locale: en-us
document_id: 8bfd60cf-f58c-2d48-d22b-881d637135ef
document_version_independent_id: 8bfd60cf-f58c-2d48-d22b-881d637135ef
original_content_git_url: https://github.com/MicrosoftDocs/power-platform-pr/blob/live/power-platform/admin/programmability-permission-reference.md
site_name: Docs
depot_name: MSDN.power-platform
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.power-platform/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/programmability-permission-reference
moniker_range_name: 
monikers: []
item_type: Content
source_path: power-platform/admin/programmability-permission-reference.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/e6f942e8-55a7-4c86-b8e3-7456508ea850
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/f1834696-48d6-470d-966b-6ee418881596
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 05c0bdce-72c8-d908-b8d2-9fb5f949926a
---

# Programmability and Extensibility - Permission reference - Power Platform | Microsoft Learn

This article provides an overview of the Power Platform API granular permissions. These permissions are available for registering client applications in Microsoft Entra ID and might become available in security role form in the future.

## Naming convention

Permissions in the Power Platform API are named in this manner: `{namespace}.{resourceType}.{action}`, where:

- `namespace` is a logical grouping of resources and functionality
- `resourceType` is the specific resource type where the permission is defined. It must be unique across the resource type's namespace, and
- `action` is described in the following table

    | HTTP Method | Path Structure | Action Name(s) |
    | --- | --- | --- |
    | GET or HEAD | Any | Read |
    | DELETE | Any | Delete |
    | PATCH | Any | Update |
    | PUT | Any | Create and Update |
    | POST | `/{namespace}/.../{resourceType}` | Create |
    | POST | `/{namespace}/.../{resourceType}/{resourceId}/{action}` | `{action}` |

## Defined permissions

The following table lists the currently defined permissions in Power Platform API:

| Name | Display name | Description |
| --- | --- | --- |
| AiFlows.Ai.Execute | Execute AI related operations (like Generate) on AI flow | Allows you to execute AI-related operations (like Generate) on AI flows. |
| AiFlows.Ai.Read | AI related read operations on AI flow | Allows you to do AI-related read operations on AI flows. |
| AiFlows.Ai.Write | AI-related write operations on AI flow | Allows you to do AI-related write operations on AI flows. |
| AiFlows.Connections.Read | Read AI flow connection | Allows reading AI flow connections. |
| AiFlows.Runs.Execute | Perform actions on AI flow run | Allows performing actions on AI flow runs. |
| AiFlows.Runs.Read | Read Copilot flow run | Allows reading AI flow runs. |
| AiFlows.Runs.Write | Write AI flow run | Allows writing AI flow runs. |
| AiFlows.Workflows.Execute | Perform actions (like activate) AI flow | Allows you to perform actions (like activate) on AI flows. |
| AiFlows.Workflows.Read | Read AI flow | Allows reading AI flows. |
| AiFlows.Workflows.Write | Write AI flow | Allows writing AI flows. |
| AiTools.Prompt.Invoke | Invoke AI prompts | Allows invoking of AI prompts. |
| AiTools.Prompt.Read | Read AI prompts | Allows reading of AI prompts. |
| AiTools.Prompt.Write | Read and write AI prompts | Allows reading and writing of AI prompts. |
| Analytics.AdvisorActions.Execute | Analytics.AdvisorActions.Execute | Allows users to execute advisor actions. |
| Analytics.AdvisorRecommendations.Read | Analytics.AdvisorRecommendations.Read | Allows users to read advisor recommendations. |
| AppManagement.ApplicationPackages.Install | Install application packages | Allows installing application packages. |
| AppManagement.ApplicationPackages.Read | Read application packages | Allows reading of application packages. |
| Authorization.RoleAssignments.Read | Power Platform role assignment reader | Allows reading of Power Platform role assignments. |
| Authorization.RoleAssignments.Write | Power Platform role assignment writer | Allows assigning of Power Platform role assignments. |
| Connectivity.Connectors.Read | Read connectors | Allows reading of connectors. |
| Connectivity.Connections.Read | Read connections | Allows reading of connections. |
| CopilotFlows.ChatAssistant.Execute | Call cloud flows chat assistant | Allows calling cloud flows chat assistant. |
| CopilotFlows.CloudFlows.ChatAssistant | Cloud flows chat assistant | Allows cloud flows chat assistant. |
| CopilotFlows.Workflows.Generate | Generate Copilot flow suggestion | Allows generating Copilot flow suggestions. |
| CopilotGovernance.Features.Execute | Perform actions related to Copilot governance features | Permission required to perform actions related to Copilot governance features. |
| CopilotGovernance.Features.Read | Read Copilot governance features | Permission required to read Copilot governance features. |
| CopilotGovernance.Settings.Read | Read Copilot governance settings | Permission required to read Copilot governance settings. |
| CopilotGovernance.Settings.Write | Write Copilot governance settings | Permission required to write Copilot governance settings. |
| CopilotStudio.AdminActions.Invoke | Allows admins to invoke administrative actions | Allow admins to invoke administrative actions on agents created in Microsoft Copilot Studio. |
| CopilotStudio.Copilots.Invoke | Allows invoking Copilots | Allows interacting with authenticated Copilots hosted by Copilot Studio. |
| EnvironmentManagement.Environments.Read | Read environments | Allows reading of environments. |
| EnvironmentManagement.Groups.Read | Read environment groups | Allows reading of environment groups. |
| EnvironmentManagement.Groups.ReadWrite | Read and write environment groups | Allows reading and writing of environment groups. |
| EnvironmentManagement.Settings.Read | Read environment management settings | Allows reading of Environment Management Settings |
| EnvironmentManagement.Settings.ReadWrite | Update environment management settings | Allows update of environment management settings. |
| Governance.CrossTenantConnectionReports.Read | Read cross-tenant connection reports | Allows reading cross-tenant connection reports |
| Governance.CrossTenantConnectionReports.ReadWrite | Read and write cross-tenant connection reports | Allows reading and writing of cross-tenant connection reports. |
| Licensing.Allocations.Read | Read currency allocations | Allows reading currency allocations. |
| Licensing.Allocations.ReadWrite | Read and write currency allocations | Allows reading and writing of currency allocations. |
| Licensing.BillingPolicies.Read | Read billing policies | Allows reading of billing policies. |
| Licensing.BillingPolicies.ReadWrite | Read and write billing policies | Allows read and writing of billing policies. |
| Licensing.IsvContracts.Read | Read ISV contracts | Allows reading of ISV contracts. |
| Licensing.IsvContracts.ReadWrite | Read and write ISV contracts | Allows reading and writing of ISV contracts. |
| PowerApps.Apps.Play | Play Power Apps | Allows playing of Power Apps applications. |
| PowerApps.Apps.Read | Read Power App | Allows reading of Power Apps applications. |
| PowerAutomate.Flows.Read | Read Power Automate flows | Allows reading of Power Automate flows. |
| PowerAutomate.Flows.Write | Write Power Automate flows | Allows writing of Power Automate flows. |
| PowerPages.Websites.Read | Read Power Pages websites | Allows reading of Power Pages websites. |
| PowerPages.Websites.Write | Write Power Pages websites | Allows writing of Power Pages websites. |
| ResourceQuery.Resources.Read | Query resources | Allows querying of resources. |
| Security.Recommendations.Read | Read Power Platform security information | Allows reading of security recommendations in Power Platform. |